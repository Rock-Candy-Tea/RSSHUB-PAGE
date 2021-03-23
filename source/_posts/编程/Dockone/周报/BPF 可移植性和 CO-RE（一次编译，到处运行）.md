
---
title: 'BPF 可移植性和 CO-RE（一次编译，到处运行）'
categories: 
 - 编程
 - Dockone
 - — 周报
headimg: ''
author: Dockone
comments: false
date: 2021-03-23 08:27:22
thumbnail: ''
---

<div>   
<br>本文介绍 BPF 可移植性面临的问题，以及 BPF CO-RE（Compile Once – Run Everywhere） 是如何解决这些问题的。<br>
<h3>BPF 现状</h3>(e)BPF 出来之后，社区一直在试图简化 BPF 程序的开发过程 —— 最好能像开发 用户空间应用程序（userspace application）一样简单直接 —— 可惜这个目标从未实现。 具体来说，在使用性（usability）方面确实有很大进步，但另一个重要方面却被忽略了 （大部分出于技术原因）：可移植性。<br>
<br>那么，什么是“BPF 可移植性（BPF portability）”？我们定义它是这样一种能力：编写的程序通过编译和内核校验之后，能正确地在不同版本的内核上运行 —— 而无需针对不同内核重新编译。<br>
<br>本文首先介绍 BPF 可移植性面临的问题，然后介绍我们的解决方案：BPF CO-RE （Compile Once – Run Everywhere）。接下来内容如下：<br>
<ul><li>首先讨论 BPF 可移植性问题本身，分析它所面临的挑战，以及为什么解决这些挑战如此重要；</li><li>然后从较高层次查看 BPF CO-RE 的各组件，以及它们是如何组织成一个完整方案解决这个问题的；</li><li>最后以一些例子（BPF 代码片段）结束本文，这些例子展示了 BPF CO-RE 中用户可见 API。</li></ul><br>
<br><h3>BPF 可移植性面临的问题</h3>BPF 程序是由用户提供的、经过验证之后在内核上下文中执行的程序。 BPF 运行在内核内存空间（kernel memory space）执行，能访问大量的 内核内部状态（internal kernel state）。 这使得 BPF 程序功能极其强大，也是为什么它能成功地应用在大量不同场景的原因之一。<br>
<br>但另一方面，与强大能力相伴而生的是我们如今面临的可移植性问题：BPF 程序 并不控制它运行时所在内核的内存布局（memory layout）。 因此，BPF 程序只能运行在开发和编译这些程序时所在的内核。<br>
<br>另外，内核类型（kernel types）和数据结构（data structures）也在不断变化。 不同的内核版本中，同一结构体的同一字段所在的位置可能会不同 —— 甚至已经 移到一个新的内部结构体（inner struct）中。此外，字段还可能会被重命名、删除、 改变类型，或者（根据不同内核配置）被条件编译掉。<br>
<h4>可移植：为什么理论上可行</h4>以上分析可知，内核版本升级时很多东西都会发生变化，而 BPF 开发者希望能够 避免这些变化对 BPF 程序造成影响。这听上去似乎不可能 —— 内核环境都在不断变化， 依赖内核环境执行的 BPF 程序又如何能幸免于难呢？<br>
<br>但实际上，这是可能的：<br>
<br>首先，不是所有 BPF 程序都依赖内核内部数据结构。<br>
<br>一个例子是 BPF 工具 opensnoop，它基于 kprobes/tracepoints 跟踪进程打开的文件， 因此只要能拦截到少数几个系统调用就能工作。由于系统调用接口 提供稳定的 ABI，不会随着内核版本而变，因此这样的 BPF 程序做到可移植是问题不大的。<br>
<br>不幸的是，这种类型的 BPF 程序很少，而且它们能做的事情通常也是非常有限的。<br>
<br>其次，内核 BPF 基础设施提供了一组有限的“稳定接口（stable interfaces）”， 内核版本升级时保证稳定，因此 BPF 程序可以依赖这组接口。<br>
<br>实际上，底层结构体和工作机制都可能发生变化，但这组稳定接口向用户程序屏蔽了这些变动。 一个例子是网络应用中的 struct sk_buff 和 struct __sk_buff。<br>
<ul><li>struct sk_buff 是内核中的数据包表示，字段非常多，并且经常发生变化；</li><li>struct __sk_buff 是 BPF 校验器提供的一个 sk_buff 的稳定接口， 或者说一组属性集合。将用户程序与底层的 struct sk_buff 解耦开来， 因此后者内存布局发生变化时，不会影响 BPF 程序。</li><li>所有对 struct __sk_buff 字段的访问都会被透明地转换成对 struct sk_buff 的访问。</li></ul><br>
<br>很多 BPF 程序类型都有类似的机制，这种封装在 BPF 中称为上下文（context），触发 BPF 程序执行时，一般传递的就是这样的上下文（指针类型，例如 struct __sk_buff *ctx）。因此，如果开发 BPF 程序时使用的是这些结构体，那这样的程序大概率是可移 植的。<br>
<h4>可移植：挑战</h4>但是，一旦需要查看原始的内核内部数据（raw internal kernel data）—— 例如 常见的表示进程或线程的 struct task_struct，这个结构体中有非常详细的进程信息 —— 那你就只能靠自己了。对于 tracing、monitoring 和 profiling 应用来说这个需求 非常常见，而这类 BPF 程序也是极其有用的。<br>
<br><strong>内核版本不同：字段被重命名或移动位置</strong><br>
<br>在这种情况下，如何保证读到的一定是我们期望读的那个字段呢 —— 例如：<br>
<ul><li>原来的程序是从 struct task_struct offset 8 地址读取数据，</li><li>由于新内核加个了 16 字节新字段，那此时正确的方式应该是从 offset 24 地址读，</li></ul><br>
<br>这还没完：如果这个字段被改名了呢？例如，thread_struct 的 fs 字段（获取 thread-local storage 用）， 在 4.6 到 4.7 内核升级时就被重命名为了 fsbase。<br>
<br><strong>内核版本相同但配置不同：字段在编译时被移除（compile out）</strong><br>
<br>另一种情况：内核版本相同，但内核编译时的配置不同，导致 结构体的某些字段在编译器时被完全移除了。<br>
<br>具体例子：某些可选的审计字段。<br>
<br><strong>小结</strong><br>
<br>所有这些都意味着：依赖开发环境本地的内核头文件编译的 BPF 程序， 是无法直接分发到其他机器运行 —— 然后期待它们返回正确结果的。 这是由于不同版本的内核头文件所假设的内存布局是不同的。<br>
<h4>可移植：BCC 方式</h4>目前，人们可以用 BCC (BPF Compiler Collection) 解决这个问题，使用方式如下：<br>
<ul><li>开发：将 BPF C 源码以文本字符串形式，嵌入（Python 编写的）用户空间控制应用（control application）；</li><li>部署：将控制应用以源码的形式拷贝到目标机器；</li><li>执行：在目标机器上，BCC 调用它内置的 Clang/LLVM，然后 include 本地内核头文件 （需要确保本机已经安装了正确版本的 kernel-devel 包）然后现场执行编译、加载、运行。</li></ul><br>
<br>这种方式能确保 BPF 程序期望的内存布局与目标机器内核的内存布局是完全一致的。<br>
<br>对于那些内核版本相关的可选字段或条件编译相关的配置代码，只需要在源代码中 用 #ifdef/#else 做处理，BCC 内置的 Clang 能正确处理这些宏，最终剩下的就是与 当前内核相匹配的源代码。这就是 BCC 解决内核版本差异的方式。<br>
<h4>BCC 方式的缺点</h4>BCC 方式可行，但存在一些很大的缺点：<br>
<ul><li>Clang/LLVM 是一个庞大的库，在部署时除了要分发 BPF 程序，还必须一起分发这个大库。</li><li><br>Clang/LLVM 这两个庞然大物非常消耗资源，因此每次在目标机器上编译 BPF 代码，都将消耗大量系统资源。<br>
<ul><li>尤其在线上的生产机器，现场编译可能会使机器负载瞬间飙高，导致生产问题。</li><li>同样，如果机器本身已经负载很高，那编译一段很小的 BPF 程序可能都要几分钟。</li></ul></li><li><br>此外，这里有个很强的前提：内核头文件在目标机器上一定存在。 在大部分情况下这都不是问题，但有时可能会带来麻烦。这对内核开发者来说也尤其头疼，因为他们经常要编译和部署一次性的内核，用于在 开发过程中验证某些问题。而机器上没有指定的、版本正确的内核头文件包，基于 BCC 的应用就无法正常工作。</li><li>这种方式会拖慢开发和迭代速度。BPF 程序的测试和开发过程也非常繁琐，很多错误只有到了运行时 （runtime）才会出现，而一旦出现就只能重启用户空间控制应用。</li></ul><br>
<br>总体来说，虽然 bcc 是一个很伟大的工具 —— 尤其是用于快速原型、实验和开发小工具 —— 但 当用于广泛部署生产 BPF 应用时，它存在非常明显的不足。<br>
<br>为了更彻底地解决 BPF 移植性问题，我们设计了 BPF CO-RE，并相信这是 BPF 程序的未来开发方式，尤其适用于开发复杂、真实环境中的 BPF 应用。<br>
<h3>BPF CO-RE：高层机制</h3>BPF CO-RE 将它所依赖的如下软件栈和它的数据集中到了一起：<br>
<ul><li>内核</li><li>用户空间 BPF 加载器库（libbpf）</li><li>编译器（clang）</li></ul><br>
<br>使得我们能以一种轻松的方式编写可移植 BPF 程序，在单个预编译的 BPF 程序内 （pre-compiled BPF program）处理不同内核之间的差异。<br>
<br>BPF CO-RE 需要下列组件之间的紧密合作：<br>
<ul><li>BTF 类型信息：使得我们能获取内核、BPF 程序类型及 BPF 代码的关键信息， 这也是下面其他部分的基础；</li><li>编译器（clang）：给 BPF C 代码提供了表达能力和记录重定位（relocation）信息的能力；</li><li>BPF loader（libbpf）：将内核的 BTF 与 BPF 程序联系起来， 将编译之后的 BPF 代码适配到目标机器的特定内核；</li><li>内核：虽然对 BPF CO-RE 完全不感知，但提供了一些 BPF 高级特性，使某些高级场景成为可能。</li></ul><br>
<br>以上几部分相结合，提供了一种开发可移植 BPF 程序的史无前例的能力：这个开发 过程不仅方便（ease），而且具备很强的适配性（adaptability）和表达能力（expressivity）。 在此之前，实现同样的可移植效果只能通过 BCC 在运行时编译 BPF C 程序，而前面也分析了， BCC 开销非常高。<br>
<h4>BTF（BPF Type Format）</h4>BTF 是 BPF CO-RE 的核心之一， 它是是一种与 DWARF 类似的调试信息，但：<br>
<ul><li>更通用、表达更丰富，用于描述 C 程序的所有类型信息。</li><li>更简单，空间效率更高（使用 <a href="https://facebookmicrosites.github.io/bpf/blog/2018/11/14/btf-enhancement.html">BTF 去重算法</a>）， 占用空间比 DWARF 低 100x。</li></ul><br>
<br>如今，让 Linux 内核在运行时（runtime）一直携带 BTF 信息是可行的， 只需在编译时指定 CONFIG_DEBUG_INFO_BTF=y。内核的 BTF 除了被内核自身使用， 现在还用于增强 BPF 校验器自身的能力 —— 某些能力甚至超越了一年之前我们的想象力所及（例 如，已经有了直接读取内核内存的能力，不再需要通过 bpf_probe_read() 间接读取了）。<br>
<br>更重要的是，内核已经将这个自描述的权威 BTF 信息（定义结构体的精确内存布局等信息） 通过 sysfs 暴露出来，在 /sys/kernel/btf/vmlinux。 下面的命令将生成一个与所有内核类型兼容的 C 头文件（通常称为 “vmlinux.h”）：<br>
<pre class="prettyprint">$ bpftool btf dump file /sys/kernel/btf/vmlinux format c<br>
</pre><br>
这里说的”所有“真的是”所有“：包括那些并未通过 kernel-devel package 导出的类型！<br>
<h4>编译器支持</h4>为了让 BPF 加载器（例如 libbpf）将 BPF 程序适配到目标机器所运行的内核上， Clang 增加了几个新的 built-in。它们的功能是导出（emit） BTF relocations（重定位信息），后者是对 BPF 程序想读取的那些信息的高层描述。<br>
<br>例如，如果想访问 task_struct->pid，那 clang 将做如下记录：这是一个 位于结构体 struct task_struct 中、类型为 pid_t、名为 pid 的字段。<br>
<br>有了这种方式，即使目标内核的 task_struct 结构体中，pid 字段位置已经发生了变 化（例如，由于这个字段前面加了新字段），甚至已经移到了某个内部嵌套的匿名结构体 或 union 中（在 C 语言中这种行为是完全透明的，因此内核开发者这样做时并不会有特别 的顾虑），我们仍然能通过名字和类型信息找到这个字段。这称为 field offset relocation（字段偏置重定位）。<br>
<br>除了字段重定位，其他一些字段相关的操作，例如判断 field existence（ 字段是否存在）或者 field size（字段长度）都是支持的。 甚至对 bitfields（比特位字段，在 C 语言中是出了名的”难处理“的类型，C 社区一直在努力让它们变得可重定位） ，我们仍然能基于 BTF 信息来使它们可重定位（relocatable），并且整个过程对 BPF 开 发者透明。<br>
<h4>BPF 加载器（libbpf）</h4>libbpf 作为一个 BPF 程序加载器（loader）， 处理前面介绍的内核 BTF 和 clang 重定位信息。它：<br>
<ul><li>读取编译之后得到的 BPF ELF 目标文件，</li><li>进行一些必要的后处理，</li><li>设置各种内核对象（bpf maps、bpf 程序等），然后</li><li>将 BPF 程序加载到内核，然后触发校验器的验证过程。</li></ul><br>
<br>libbpf 知道如何对 BPF 程序进行裁剪，以适配到目标机器的内核上。<br>
<ul><li>它会查看 BPF 程序记录的 BTF 和重定位信息，然后</li><li>拿这些信息跟当前内核提供的 BTF 信息相匹配。然后</li><li>解析和匹配所有的类型和字段，更新所有必要的 offsets 和其他可重定位数据。</li><li>最终确保 BPF 程序在这个特定的内核上是能正确工作的。</li></ul><br>
<br>如果一切顺利，你（作为 BPF 应用开发者）将得到一个针对目标机器”定制化裁剪“的 BPF 程序，就像这个程序是专门针对这个内核编译的一样。但这种工作方式无需将 clang 与 BPF 一起打包部署，也没有在目标机器上运行时编译（runtime）的开销。<br>
<h4>内核</h4>内核无需太多改动就能支持 BPF CO-RE，这一点可能令很多人感到惊讶。 由于设计合理，因此对于内核来说，libbpf 处理之后的 BPF 程序，与 其他任何合法的 BPF 程序是一样的 —— 与在这台机器上依赖最新内核头文件编译出的 BPF 程序并无区别。这意味要 BPF CO-RE 并不依赖最新的内核功能，因此 应用范围更广，适配速度更快。<br>
<br>某些高级场景可能会需要更新的内核，但这些场景很少。接下来介绍 BPF CO-RE 用户侧机制 时会讨论到这样的场景。<br>
<h3>BPF CO-RE：用户侧经验</h3>接下来看几个真实世界中 BPF CO-RE 的典型场景，以及它是如何解决面临的一些问题的。 我们将看到：<br>
<ul><li>一些可移植性问题（例如，兼容 struct 内存布局差异）能够处理地非常透明和自然，</li><li><br>而另一些则需要通过显式处理的，具体包括：<br>
<ul><li>通过 if/else 条件判断（而不是 BCC 中的那种条件编译 #ifdef/#else）。</li><li>BPF CO-RE 提供的其他一些额外机制。</li></ul></li></ul><br>
<br><h4>摆脱内核头文件依赖</h4>内核 BTF 信息除了用来做字段重定位之外，还可以用来生成一个大的头文件（”vmlinux.h“）， 这个头文件中包含了所有的内部内核类型，从而避免了依赖系统层面的内核头文件。<br>
<br>通过 bpftool 获得 vmlinux.h：<br>
<pre class="prettyprint">$ bpftool btf dump file /sys/kernel/btf/vmlinux format c > vmlinux.h<br>
</pre><br>
有了 vmlinux.h，就无需再像通常的 BPF 程序那样 #include <linux/sched.h>、#include <linux/fs.h> 等等头文件， 现在只需要 #include "vmlinux.h"，也不用再安装 kernel-devel 了。<br>
<br>vmlinux.h 包含了所有的内核类型：<br>
<ul><li>作为 UAPI 的一部分暴露的 API</li><li>通过 kernel-devel 暴露的内部类型</li><li>其他一些通过任何其他方式都无法获取的内部内核类型</li></ul><br>
<br>不幸的是，BPF（以及 DWARF）并不记录 #define 宏，因此某些常用 的宏可能在 vmlinux.h 中是缺失的。但这些没有记录的宏中 ，最常见的一些已经在 bpf_helpers.h （libbpf 提供的内核侧“库”）提供了。<br>
<h4>读取内核结构体字段</h4>最常见和最典型的场景就是从某些内核结构体中读取一个字段。<br>
<br><strong>例子：读取 task_struct->pid 字段</strong><br>
<br>假设我们想读取 task_struct 中的 pid 字段。<br>
<br>方式一：BCC（可移植）<br>
<br>用 BCC 实现，代码很简单：<br>
<pre class="prettyprint">pid_t pid = task->pid;<br>
</pre><br>
BCC 有强大的代码重写（rewrite）能力，能自动将以上代码转换成一次 bpf_probe_read() 调用 （但有时重写之后的代码并不能正确，具体取决于表达式的复杂程度）。<br>
<br>libbpf 没有 BCC 的代码重写魔法（code-rewriting magic），但提供了几种其他方式来 实现同样的目的。<br>
<br>方式二：libbpf + BPF_PROG_TYPE_TRACING（不可移植）<br>
<br>如果使用的是最近新加的 BTF_PROG_TYPE_TRACING 类型 BPF 程序，那校验器已经足够智 能了，能原生地理解和记录 BTF 类型、跟踪指针，直接（安全地）读取内核内存 。<br>
<pre class="prettyprint">pid_t pid = task->pid;<br>
</pre><br>
从而避免了调用 bpf_probe_read()，格式和语法更为自然，而且无需编译器重写（rewrite）。 但此时，这段代码还不是可移植的。<br>
<br>方式三：BPF_PROG_TYPE_TRACING + CO-RE（可移植）<br>
<br>要将以上 BPF_PROG_TYPE_TRACING 代码其变成可移植的，只需将待访问字段 task->pid 放到编译器内置的一个名为 __builtin_preserve_access_index() 的宏中：<br>
<pre class="prettyprint">pid_t pid = __builtin_preserve_access_index((&#123; task->pid; &#125;)); <br>
</pre><br>
这就是全部工作了：这样的程序在不同内核版本之间是可移植的。<br>
<br>方式四：libbpf + CO-RE bpf_core_read()（可移植）<br>
<br>如果使用的内核版本还没支持 BPF_PROG_TYPE_TRACING，就必须显式地使用 bpf_probe_read() 来读取字段。<br>
<br>Non-CO-RE libbpf 方式：<br>
<pre class="prettyprint">pid_t pid;<br>
bpf_probe_read(&pid, sizeof(pid), &task->pid); <br>
</pre><br>
有了 CO-RE+libbpf，我们有两种方式实现这个目的。<br>
<br>第一种，直接将 bpf_probe_read() 替换成 bpf_core_read()：<br>
<pre class="prettyprint">pid_t pid;<br>
bpf_core_read(&pid, sizeof(pid), &task->pid); <br>
</pre><br>
bpf_core_read() 是一个很简单的宏，直接展开成以下形式：<br>
<pre class="prettyprint">bpf_probe_read(&pid, sizeof(pid), __builtin_preserve_access_index(&task->pid)); <br>
</pre><br>
可以看到，第三个参数（&task->pid）放到了前面已经介绍过的编译器 built-int 中， 这样 clang 就能记录该字段的重定位信息，实现可移植。<br>
<br>第二种方式是使用 BPF_CORE_READ() 宏，我们通过下面的例子来看。<br>
<br><strong>例子：读取 task->mm->exe_file->f_inode->i_ino 字段</strong><br>
<br>这个字段表示的是当前进程的可执行文件的 inode。 来看一下访问嵌套层次如此深的结构体字段时，面临哪些问题。<br>
<br>方式一：BCC（可移植）<br>
<br>用 BCC 实现的话可能是下面这样：<br>
<pre class="prettyprint">u64 inode = task->mm->exe_file->f_inode->i_ino; <br>
</pre><br>
BCC 会对这个表达式进行重写（rewrite），转换成 4 次 bpf_probe_read()/bpf_core_read() 调用， 并且每个中间指针都需要一个额外的临时变量来存储。<br>
<br>方式二：BPF CO-RE（可移植）<br>
<br>下面是 BPF CO-RE 的方式，仍然很简洁，但无需 BCC 的代码重写（code-rewriting magic）：<br>
<pre class="prettyprint">u64 inode = BPF_CORE_READ(task, mm, exe_file, f_inode, i_ino); <br>
</pre><br>
另外一个变种是：<br>
<pre class="prettyprint">u64 inode;<br>
BPF_CORE_READ_INTO(&inode, task, mm, exe_file, f_inode, i_ino); <br>
</pre><br>
<strong>其他与字段读取相关的 CO-RE 宏</strong><br>
<br>bpf_core_read_str()：可以直接替换 Non-CO-RE 的 bpf_probe_read_str()。<br>
<br>BPF_CORE_READ_STR_INTO()：与 BPF_CORE_READ_INTO() 类似，但会对最后一个字段执行 bpf_probe_read_str()。<br>
<br>bpf_core_field_exists()：判断字段是否存在<br>
<pre class="prettyprint">pid_t pid = bpf_core_field_exists(task->pid) ? BPF_CORE_READ(task, pid) : -1; <br>
</pre><br>
bpf_core_field_size()：判断字段大小，同一字段在不同版本的内核中大小可能会发生变化<br>
<pre class="prettyprint">u32 comm_sz = bpf_core_field_size(task->comm); /* will set comm_sz to 16 */<br>
</pre><br>
BPF_CORE_READ_BITFIELD()：通过直接内存读取（direct memory read）方式，读取比特位字段<br>
<br>BPF_CORE_READ_BITFIELD_PROBED()：底层会调用 bpf_probe_read()<br>
<pre class="prettyprint">struct tcp_sock *s = ...;<br>
<br>
/* with direct reads */<br>
bool is_cwnd_limited = BPF_CORE_READ_BITFIELD(s, is_cwnd_limited);<br>
<br>
/* with bpf_probe_read()-based reads */<br>
u64 is_cwnd_limited;<br>
BPF_CORE_READ_BITFIELD_PROBED(s, is_cwnd_limited, &is_cwnd_limited); <br>
</pre><br>
<h4>处理内核版本和配置差异</h4>某些情况下，BPF 程序必须处理不同内核版本之间常用内核结构体的非细微差异。例如：<br>
<ul><li>字段被重命名了：对依赖这个字段的调用方来说，这其实变成了一个新字段（但语义没变）。</li><li>字段名字没变，但表示的意思变了：例如，从 4.6 之后的某个内核版本开始， task_struct 的 utime 和 stime 字段，原来单位是 jiffies，现在变成了 nanoseconds，因此 调用方必须自己转换单位。</li><li>需要从内核提取的某些数据是与内核配置有直接关系，某些内核在编译时并没有将相关代码编译进来。</li><li>其他一些无法用单个、通用的类型定义来适用于所有内核版本的场景。</li></ul><br>
<br>对于这些场景，BPF CO-RE 提供了两种互补的解决方式：<br>
<ul><li>libbpf 提供的 extern Kconfig 变量</li><li>struct flavors</li></ul><br>
<br><strong>libbpf 提供的 externs Kconfig 全局变量</strong><br>
<ul><li>系统中已经有一些”知名的“变量，例如 LINUX_KERNEL_VERSION，表示当前内核的版本。 BPF 程序能用 extern 关键字声明这些变量。</li><li>另外，BPF 还能用 extern 的方式声明 Kconfig 的某些 key 的名字（例如 CONFIG_HZ，表示内核的 HZ 数）。</li></ul><br>
<br>接下来的事情交给 libbpf，它会将这些变量分别匹配到系统中相应的值（都是常量）， 并保证这些 extern 变量与全局变量的效果是一样的。<br>
<br>此外，由于这些 extern ”变量“都是常量，因此 BPF 校验器能用它们来做一些 高级控制流分析和死代码消除。<br>
<br>下面是个例子，如何用 BPF CO-RE 来提取线程的 CPU user time：<br>
<pre class="prettyprint">extern u32 LINUX_KERNEL_VERSION __kconfig;<br>
extern u32 CONFIG_HZ __kconfig;<br>
<br>
u64 utime_ns;<br>
<br>
if (LINUX_KERNEL_VERSION >= KERNEL_VERSION(4, 11, 0))<br>
    utime_ns = BPF_CORE_READ(task, utime);<br>
else<br>
    /* convert jiffies to nanoseconds */<br>
    utime_ns = BPF_CORE_READ(task, utime) * (1000000000UL / CONFIG_HZ);<br>
</pre><br>
<strong>struct flavors</strong><br>
<br>有些场景中，不同版本的内核中有不兼容的类型，无法用单个通用结构体来为所有内核 编译同一个 BPF 程序。struct flavor 在这种情况下可以派上用场。<br>
<br>下面是一个例子，提取 fs/fsbase（前面提到过，字段名字在内核版本升级时改了）来 做一些 thread-local 的数据处理：<br>
<pre class="prettyprint">/* up-to-date thread_struct definition matching newer kernels */<br>
struct thread_struct &#123;<br>
...<br>
u64 fsbase;<br>
...<br>
&#125;;<br>
<br>
/* legacy thread_struct definition for <= 4.6 kernels */<br>
struct thread_struct___v46 &#123;   /* ___v46 is a "flavor" part */<br>
...<br>
u64 fs;<br>
...<br>
&#125;;<br>
<br>
extern<br>
int LINUX_KERNEL_VERSION __kconfig;<br>
...<br>
<br>
struct thread_struct *thr = ...;<br>
u64 fsbase;<br>
if (LINUX_KERNEL_VERSION > KERNEL_VERSION(4, 6, 0))<br>
fsbase = BPF_CORE_READ((struct thread_struct___v46 *)thr, fs);<br>
else<br>
fsbase = BPF_CORE_READ(thr, fsbase);<br>
</pre><br>
在这个例子中，对于 <=4.6 的内核，我们将原来的 thread_struct 定义为了 struct thread_struct___v46。 双下划线及其之后的部分，即 ___v46，称为这个 struct 的 “flavor”。<br>
<br>flavor 部分会被 libbpf 忽略，这意味着在目标机器上执行字段重定位时， struct thread_struct__v46 匹配的仍然是真正的 struct thread_struct。<br>
<br>这种方式使得我们能在单个 C 程序内，为同一个内核类型定义不同的（而且是不兼容的） 类型，然后在运行时（runtime）取出最合适的一个，这就是用 type cast to a struct flavor 来提取字段的方式。<br>
<br>没有 struct flavor 的话，就无法真正实现像上面那样“编译一次”，然后就能在不同内核 上都能运行的 BPF 程序 —— 而只能用#ifdef 来控制源代码，编译成两个独立的 BPF 程序变种，在运行时（runtime）由控制应用根据所在机器的内核版本选择其中某个变种。 所有这些都添加了不必要的复杂性和痛苦。 相比之下，以上 BPF CO-RE 方式虽然不是透明的（上面的代码中也包含了内核 版本相关的逻辑），但允许用熟悉的 C 代码结构解决即便是这样的高级场景的问题。<br>
<h4>根据用户提供的配置修改程序行为</h4>BPF 程序知道内核版本和配置信息，有时还不足以判断如何 —— 以及以何种方式 —— 从该版本的内核获取数据。 在这些场景中，用户空间控制应用（control application）可能是唯一知道 究竟需要做哪些事情，以及需要启用或禁用哪些特性的主体。 这通常是在用户空间和 BPF 程序之间通过某种形式的配置数据来通信的。<br>
<br><strong>BPF map 方式</strong><br>
<br>要实现这种目的，一种不依赖 BPF CO-RE 的方式是：将 BPF map 作为一个存储配置 数据的地方。BPF 程序从 map 中提取配置信息，然后基于这些信息改变它的控制流。<br>
<br>但这种方式有几个主要的缺点：<br>
<ul><li>BPF 程序每次执行 map 查询操作，都需要运行时开销（runtime overhead）。多次查询累积起来，开销就会比较比较明显，尤其在一些高性能 BPF 应用的场景。</li><li>配置内容（config value），虽然在 BPF 程序启动之后就是不可变和只读 （immutable and read-only）的了，但 BPF 校验器在校验时扔把它们当作未知的黑盒值。这意味着校验器无法消除死代码，也无法执行其他高级代码分析。进一步， 这意味着我们无法将代码逻辑放到 map 中，例如，能处理不同内核版本差异的 BPF 代 码，因为 map 中的内容对校验器都是黑盒，因此校验器对它们是不信任的 —— 即使用户配置信息是安全的。</li></ul><br>
<br><strong>只读的全局数据方式</strong><br>
<br>这种（确实复杂的）场景的解决方案：使用只读的全局数据（read-only global data）。 这些数据是在 BPF 程序加载到内核之前，由控制应用设置的。<br>
<ul><li>从 BPF 程序的角度看，这就是正常的全局变量访问，没有任何 BPF map lookup 开销 —— 全局变量实现为一次直接内存访问。</li><li>控制应用方面，在 BPF 程序加载到内核之前设置初始的配置值，此后配置值就是全局可 访问且只读（well known and read-only）的了。这使得 BPF 校验器能将它们作为常量对待，然后就能执行高级控制流分析 （advanced control flow analysis）来消除死代码。</li></ul><br>
<br>因此，针对上面那个例子，<br>
<ul><li>某些老内核的 BPF 校验器就能推断出，例如，代码中某个未知的 BPF helper 不可能会用到，接下来就可以将相关代码直接移除。</li><li>而对于新内核来说，应用提供的配置（application-provided configuration）会所有不 同，因此 BPF 程序就能用到功能更强大的 BPF helper，而且这个逻辑能成功通过 BPF 校验器的验证。</li></ul><br>
<br>下面的 BPF 代码例子展示了这种用法：<br>
<pre class="prettyprint">/* global read-only variables, set up by control app */<br>
const bool use_fancy_helper;<br>
const u32 fallback_value;<br>
<br>
...<br>
<br>
u32 value;<br>
if (use_fancy_helper)<br>
value = bpf_fancy_helper(ctx);<br>
else<br>
value = bpf_default_helper(ctx) * fallback_value;<br>
</pre><br>
从用户空间方面，通过 BPF skeleton 可以很方便地做这种配置。BPF skeleton 的讨论不在 本文讨论范围内，使用它来简化 BPF 应用的例子，可参考内核源码中的 <a href="https://github.com/torvalds/linux/tree/master/tools/bpf/runqslower">runqslower tool</a>。<br>
<h3>总结</h3>BPF CO-RE 的目标是：<br>
<ul><li>作为一种简单的方式帮助 BPF 开发者解决简单的移植性问题（例如读取结构体的字段），并且</li><li>作为一种仍然可行（不是最优，但可容忍）的方式 解决复杂的移植性问题（例如不兼容的数据结构改动、复杂的用户空间控制条件等）。</li><li>使得开发者能遵循“一次编译、到处运行”（Compile Once – Run Everywhere）范式。</li></ul><br>
<br>这是通过几个 BPF CO-RE 模块的组合实现的：<br>
<ul><li>vmlinux.h 消除了对内核头文件的依赖；</li><li>字段重定位信息（字段偏置、字段是否存在、字段大小等等）使得从内核提取数据这个过程变得可移植；</li><li>libbpf 提供的 Kconfig extern 变量允许 BPF 程序适应不同的内核版本 —— 以及配置相关的差异；</li><li>当其他方式都失效时，应用提供的只读配置和 struct flavor 最终救场，能解决 任何需要复杂处理的场景。</li></ul><br>
<br>要成功地编写、部署和维护可移植 BPF 程序，并不是必须用到所有这些 CO-RE 特性。 只需选择若干，用最简单的方式解决你的问题。<br>
<br>BPF CO-RE 使我们回到了熟悉、自然的工作流程：将 BPF C 源码编译成二进制，然后将 二进制文件分发到目标机器进行部署和运行 —— 无需再随着应用一起分发重量级的编译器库、无需消耗宝贵的运行时资源做运行时编译（runtime compilation），也无需等到运行之前才能捕捉一些细微的编译时错误（ compilation errors in runtime）了。<br>
<br>原文链接：<a href="https://facebookmicrosites.github.io/bpf/blog/2020/02/19/bpf-portability-and-co-re.html" rel="nofollow" target="_blank">https://facebookmicrosites.git ... .html</a><br>
<br>译文链接：<a href="http://arthurchiao.art/blog/bpf-portability-and-co-re-zh/" rel="nofollow" target="_blank">http://arthurchiao.art/blog/bp ... e-zh/</a>
                                
                                                              
</div>
            