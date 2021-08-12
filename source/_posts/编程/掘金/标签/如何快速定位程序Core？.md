
---
title: '如何快速定位程序Core？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37f51fc3a3974fbe8212d4066e8952ea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 22:15:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37f51fc3a3974fbe8212d4066e8952ea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>导读</strong>：程序core是指应用程序无法保持正常running状态而发生的崩溃行为。程序core时会生成相关的core-dump文件，是程序崩溃时程序状态的数据备份。core-dump文件中包含内存、处理器、寄存器、程序计数器、栈指针等状态信息。本文将介绍一些利用core-dump文件定位程序core原因的方法和技巧。</p>
<p><em>全文7023字，预计阅读时间 13分钟。</em></p>
<h1 data-id="heading-0"><strong>一、程序Core定义及分类</strong></h1>
<p>程序core是指应用程序无法保持正常running状态而发生的崩溃行为。程序core时会生成相关的core-dump文件，core-dump文件是程序崩溃时程序状态的状态数据备份。core-dump文件包含内存、处理器、寄存器、程序计数器、栈指针等状态信息。我们可以借助core-dump文件来分析定位程序Core的原因。</p>
<p>这里我们从三个方面对程序Core进行分类：机器、资源、程序Bug。下表对常见的Core原因进行了分类：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37f51fc3a3974fbe8212d4066e8952ea~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1"><strong>二、函数栈介绍</strong></h1>
<p>当我们打开core文件时，首先关注的是程序崩溃时的函数调用栈状态，为了方便理解后续定位core的一些技巧，这里先简单介绍一下函数栈。</p>
<h2 data-id="heading-2"><strong>2.1 寄存器介绍</strong></h2>
<p>目前生产环境都为64位机，这里只介绍64位机的寄存器，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2369919f18d4d5cbe2040cba2454d02~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于x86-64架构，共有16个64位寄存器，每个寄存器的用途并不单一，如%rax通常保存函数返回结果，但也被应用于imul和idiv指令。这里重点关注%rsp（栈顶指针寄存器）、%rbp（栈底指针寄存器）、%rdi、%rsi、%rdx、%rcx、%r8、%r9（分别对应第1～6函数参数）。</p>
<p>Callee Save说明是否需要被调用者保存寄存器的值。</p>
<h2 data-id="heading-3"><strong>2.2 函数调用</strong></h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1ec05d1d3f24c63afbd6ad2e7e5e588~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4"><strong>2.2.1 调用函数栈帧：</strong></h3>
<p>在调用一个函数时首先进行的是<strong>参数压栈</strong>，参数压栈的顺序跟参数定义的顺序相反。注意，<strong>并不是参数一定会压栈</strong>，在x86-64架构中会针对可以使用寄存器传递的变量，直接通过寄存器传值，如数字、指针、引用等。</p>
<p>接着是**返回地址压栈，**返回地址为被调用函数执行完后，调用函数执行的下一个指令地址。这里牢记返回地址的位置，后续章节会利用到这个返回地址的特性。</p>
<p>针对上面的介绍举个例子说明：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/856fede38e9b4f2299e95305956247ee~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，在main函数中调用了foo函数，首先对参数压栈，三个参数都可以直接用寄存器传递（分别对应%edi、%esi、%edx），然后call指令将下一个指令压栈。</p>
<h3 data-id="heading-5"><strong>2.2.2 被调用函数栈帧：</strong></h3>
<p>被调用函数首先会将上一个函数的栈底指针（%rbp）保存，即%rbp压栈。然后再保存需要被保存的寄存器值，即Callee Save为True的寄存器。接着为临时变量、局部变量申请栈空间。</p>
<p>针对被调用函数，举个例子说明：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f05d09decfa49128fcf611bc4c61528~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，在foo函数执行时，先对main函数的%rbp压栈，再把寄存器中的参数值存放到局部变量(a, b, c)中。</p>
<h2 data-id="heading-6"><strong>2.3 总结</strong></h2>
<p>通过对函数调用的简单介绍，我们可以发现函数栈是一个缜密且脆弱的结构，内存结构必须按照严格的方式被访问，如稍有不慎就可能导致程序崩溃。</p>
<h1 data-id="heading-7"><strong>三、GDB定位Core</strong></h1>
<p>这一节将介绍从core文件打开到定位全流程中可能会遇到的问题以及解决技巧。</p>
<h2 data-id="heading-8"><strong>3.1 Core文件</strong></h2>
<p><strong>core文件在哪里？</strong></p>
<p>查看“/proc/sys/kernel/core_pattern”确定core文件生成规则。</p>
<h2 data-id="heading-9"><strong>3.2 变量打印</strong></h2>
<p>程序debug过程中常常要查看各种变量（内存、寄存器、函数表等）的值是否正确，维持单独用一节介绍下常用的变量打印方法以及一些冷门小技巧。</p>
<h3 data-id="heading-10"><strong>3.2.1 print命令</strong></h3>
<pre><code class="copyable">print [Expression]
print $[Previous value number]
print &#123;[Type]&#125;[Address]
print [First element]@[Element count]
print /[Format] [Expression]

Format格式：
o - 8进制
x - 16进制
u - 无符号十进制
t - 二进制
f - 浮点数
a - 地址
c - 字符
s - 字符串
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11"><strong>3.2.2 x命令</strong></h3>
<pre><code class="copyable">x /<n/f/u>  <addr>
n:是正整数，表示需要显示的内存单元的个数，即从当前地址向后显示n个内存单元的内容，一个内存单元的大小由第三个参数u定义。

f:表示addr指向的内存内容的输出格式，
s对应输出字符串，此处需特别注意输出整型数据的格式：  
x 按十六进制格式显示变量.  
d 按十进制格式显示变量。  
u 按十进制格式显示无符号整型。  
o 按八进制格式显示变量。  
t 按二进制格式显示变量。  
a 按十六进制格式显示变量。  
c 按字符格式显示变量。  
f 按浮点数格式显示变量。
u:就是指以多少个字节作为一个内存单元-unit,默认为4。
u还可以用被一些字符表示:  
如b=1 byte, h=2 bytes,w=4 bytes,g=8 bytes.<addr>:表示内存地址。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12"><strong>3.2.3 容器对象打印</strong></h3>
<p>利用上面的print和x命令，再结合容器的数据结构，我们就能知道容器的详细信息。这里举个完整打印二进制string的例子，string的数据结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ca01a022236411190c45e85713f2122~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>string为空时，_M_dataplus._M_p是指向nullptr的。当赋值后会在堆上申请一段内存，分为两段，前半段是meta信息（类型为std::string::_Rep），如length、capacity、refcount，后半段为数据区，_M_p指向数据区。</p>
<p>通常情况下非二进制的string，直接print即可显示数据内容，但当数据为二进制时，'\0'会截断打印内容。因此，打印二进制string的首要任务是确认string的size。</p>
<p>string的size信息保存在std::string::_Rep结构体中，根据上面的数据结构可以发现，_Rep与_M_dataplus._M_p相差一个结构体大小，因此打印_Rep结构体的命令为：</p>
<pre><code class="copyable">#先把_M_p转成_Rep指针，再让指针向低地址偏移一个结构体大小
p *((std::string::_Rep*)(s._M_dataplus._M_p) - 1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到string的size（_M_length）后，再通过x命令打印相关的内存区即可，命令为：</p>
<pre><code class="copyable">#这里的n是_Rep._M_length
x /ncb s._M_dataplus._M_p
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a62786398f042cf923695e8ea4d3176~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了方便，这里推荐一个方便的脚本：stl-views.gdb（链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsourceware.org%2Fgdb%2Fwiki%2FSTLSupport%3Faction%3DAttachFile%26do%3Dview%26target%3Dstl-views-1.0.3.gdb%25EF%25BC%258C%25E7%259B%25B4%25E6%258E%25A5%25E5%259C%25A8gdb%25E7%25BB%2588%25E7%25AB%25AFsourcestl-views.gdb" target="_blank" rel="nofollow noopener noreferrer" title="https://sourceware.org/gdb/wiki/STLSupport?action=AttachFile&do=view&target=stl-views-1.0.3.gdb%EF%BC%8C%E7%9B%B4%E6%8E%A5%E5%9C%A8gdb%E7%BB%88%E7%AB%AFsourcestl-views.gdb" ref="nofollow noopener noreferrer">sourceware.org/gdb/wiki/ST…</a> 即可，支持常见的容器打印，如vector、map、list、string等。</p>
<h3 data-id="heading-13"><strong>3.2.4 静态变量打印</strong></h3>
<p>程序中经常会使用到静态变量，有时我们需要查看某个静态对象的值是否正确，就涉及到静态对象的打印。看如下例子：</p>
<pre><code class="copyable">void foo() &#123;
    static std::string s_foo("foo");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以借助<strong>nm -C</strong> ./bin  | grep xx找到静态变量的<strong>内存地址</strong>，再通过gdb的print打印。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd71b49102a84cdbbe6a39d3e3ac3bfc~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">3.2.5 内存dump</h3>
<pre><code class="copyable">dump [format] memory filename start_addr end_addr
dump [format] value filename expr
format一般使用binary，其他的可以查看gdb手册。

比如我们可以结合上面查看string内容的例子dump整个string数据到文件中。
dump binary memory file1 s._M_dataplus._M_p s._M_dataplus._M_p + length

如果想查看文件内容的话可把vim -b和xxd结合使用。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接上面string的例子，举一个dump string内存数据到文件的例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61d749229ebb41a4a0ade72d28e11a29~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15"><strong>3.3 定位代码行</strong></h2>
<p>定位core的原因，首先要定位崩溃时正在执行的代码行，这一节主要介绍一些定位代码行的方法。通常情况下直接通过gdb的breaktrace即可一览整个函数栈，但有时候函数栈信息并非如此清晰明了，这时就可利用一些小技巧来查看函数栈。</p>
<h3 data-id="heading-16"><strong>3.3.1 去编译优化</strong></h3>
<hr>
<p>有时候会发现core的函数栈跟实际的代码行不匹配，如果是在线下环境中，可以尝试把编译优化设置成**-O0**，然后再重新复现core问题。</p>
<h3 data-id="heading-17"><strong>3.3.2 程序计数器 + addr2line</strong></h3>
<p>对于线上core问题，一般没法再对程序进行去编译优化操作，只能在现有的core文件基础上进行代码定位。这一节我们采用一个例子来介绍如何使用<strong>程序计数器 + addr2line</strong>来定位代码行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de9824ab5b6e4bd9bec3993e6d54aaef~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从截图可以发现frame 20指示的代码行与实际的代码行是不匹配的，定位步骤如下：</p>
<pre><code class="copyable"># 跳转到第20号栈
frame 20
 
# 使用display命令显示程序计数器
display /i $rip
 
# 使用addrline工具做地址转换
shell /opt/compiler/gcc-8.2/bin/addr2line -e bin address
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.3.3 函数栈修复</strong></p>
<p>有时候我们会发现函数调用栈里面会出现很多？？的情况，这常发生于栈被写花，某些情况下手动进行修复。函数栈的修复利用的函数栈内存分布知识，见第一节。</p>
<pre><code class="copyable">-----------------------------------
Low addresses
-----------------------------------
0(%rsp)  | top of the stack frame          
         | (this is the same as -n(%rbp))
---------|--------------------------
n(%rbp) | variable sized stack frame-
8(%rbp) | varied
0(%rbp)  | previous stack frame address
8(%rbp)  | return address
-----------------------------------
High addresses

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的栈示意图可以发现，利用%rbp寄存器即可找到上一个<strong>函数的返回地址</strong>和<strong>栈底指针，<strong>再利用</strong>addr2line</strong>命令找到对应的代码行。这里举一个例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bca78e97ccbc4be6836db4c5b33eacfe~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">#首先找到当前被调用栈上一个栈的栈底指针值和返回地址
x /2ag $rbp # 2个单位，a=十六进制，g=8字节单元
  
#使用上一条命令得到的栈底指针值依次递归
x /2ag address
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18"><strong>3.3.4 无规律core栈</strong></h3>
<p>无规律core栈问题一般发生于堆内存写坏。函数调用是一个非常精密的过程，任何一个位置发生非预期的读写都会导致程序崩溃。这里可以举个小例子来说明：</p>
<pre><code class="copyable">int main(int argc, char* argv[]) &#123;
    std::string s("abcd");
    *reinterpret_cast<uint64_t*>(&s) = 0x11;
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子core在string析构上，原因是因为string的_M_ptr被改写成了0x11，析构流程变成了非法内存操作。</p>
<p>同理，由于进程堆空间是共享的，一个线程对堆的非法操作就可能会影响另一个线程的正常操作，由于堆分配的随机性，表现出来的现象就是无规律core栈。</p>
<p>针对无规律core栈最好的方式还是借助AddressSanitizer。</p>
<pre><code class="copyable">#设置编译参数CXXFLAGS
CXXFLAGS="-fPIC -fsanitize=address  -fno-omit-frame-pointer"
 
#设置链接参数
LDFLAGS="-lasan"
 
# 设置启动环境变量
export ASAN_OPTIONS=halt_on_error=0:abort_on_error=1:disable_coredump=0
 
# 启动
LD_PRELOAD=/opt/compiler/gcc-8.2/lib/libasan.so ./bin/xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.3.5 总结</strong></p>
<p>上面提到的几种方法都是为了找到具体的问题代码行，为后续分析core的具体原因提供线索。</p>
<h2 data-id="heading-19"><strong>3.4 定位Core原因</strong></h2>
<p>这一节主要介绍定位Core原因的方法以及一些常见原因的介绍。</p>
<h3 data-id="heading-20"><strong>3.4.1 确认信号量</strong></h3>
<hr>
<p>从上面的Core分类我们可以发现某些场景的core是由于机器故障导致的，如SIGBUS，因此可以先通过信号量排除掉一些core原因。</p>
<h3 data-id="heading-21"><strong>3.4.2 定位异常汇编指令</strong></h3>
<hr>
<p>通过上面的代码行定位我们可以大致找到程序core在哪一行，比较简单的core直接print程序上下文即可找到core的原因。</p>
<p>但有些场景下，通过排查上下文无任何异常，这个时候就需要准确定位具体的异常汇编指令，根据指令找原因。</p>
<p>查看汇编指令比较简单的方法是使用<strong>layout asm</strong>命令，frame指向那个栈，就显示对应栈的汇编。这里举个core例子，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f96cbddf7e764543b16dbd2126472ca8~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>程序显示core在start函数，查看相关上下文变量均无异常。使用layout asm打开正在执行的汇编指令，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/204f0b6a2a7548e098ea81a4a5aae8d8~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看汇编定位到程序core在mov指令，mov指令上一个指令为sub，为栈申请了3M空间，怀疑是栈空间不足。采用frame 0的%rsp - frame N的%rbp排查为栈空间不足。</p>
<p>通过上面的例子，可以发现定位异常汇编指令位置后，我们能够把异常点进一步压缩，定位到是哪个<strong>指令、变量、地址</strong>导致的core问题。</p>
<h3 data-id="heading-22"></h3>
<h3 data-id="heading-23"><strong>3.4.3 排查异常变量</strong></h3>
<p>通过上面的操作我们可以准确定位到具体是哪一行代码的哪一条指令出现了问题，根据异常指令我们可以排查相关的变量，确定变量值是否符合预期。</p>
<p>这里举一个比较经典的空指针例子，如下：</p>
<pre><code class="copyable">int main(int argc, char* argv[]) &#123;
    int* a = nullptr;
    *a = 1;
    return *a;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33acadf559af4c6ebfe4e8b0646b55d9~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过汇编指令我们可以发现是<strong>movl $0x1, (%rax)<strong>出现了问题，</strong>%rax</strong>的值来自于<strong>0x8(%rbp)</strong>，<strong>x命令</strong>打印相关的地址就可以发现为空指针错误。</p>
<h3 data-id="heading-24"></h3>
<h3 data-id="heading-25"><strong>3.4.4 查看被优化变量</strong></h3>
<p>通常情况下程序都是开启了编译优化的，就会出现变量无法被print，提示变量被优化，有时可利用<strong>汇编 + 寄存器</strong>的方式查看被优化的变量。</p>
<p>这里举一个例子说明下：</p>
<pre><code class="copyable">void foo(char const* str) &#123;
    char buf[1024] = &#123;'\0'&#125;;
    memcpy(buf, str, sizeof(buf));
&#125;

int main(int argc, char* argv[]) &#123;
    foo("abcd");
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常情况下在foo函数内部，str变量是会直接别优化掉的，因为可以直接利用%rdi寄存器传递参数。为了能够打印出str的值，这个时候我们可以借助<strong>汇编 + 寄存器</strong>的方式找到具体的变量值，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49ae83b1a12d45c8b4d6c75f2d788120~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先找到main函数调用foo函数的参数压栈汇编：<strong>mov $0x402011, %edi，<strong>这里的</strong>0x402011</strong>即为str的内存地址，通过x命令即可显示str的值了。</p>
<p>比较复杂的场景可能没法直接找到被优化变量，这时可以采用汇编回溯的方式找到变量。</p>
<h3 data-id="heading-26"></h3>
<h3 data-id="heading-27"><strong>3.4.5 异常函数地址排查</strong></h3>
<p>有时的core问题是因为数据异常导致，有时也可能是优化函数地址导致，如调用虚函数地址错误、函数返回地址错误、函数指针值错误。</p>
<p>异常函数地址排查同理于异常变量排查，根据汇编指令确认调用是否异常即可。这里举一个虚函数地址异常的例子，如下：</p>
<pre><code class="copyable">class
A &#123;
public:
    virtual ~A() = default;
    virtual void foo() = 0;
&#125;;
class
B : public A &#123;
public:
    void foo() &#123;&#125;
&#125;;
 
int main(int argc, char* argv[])
&#123;
    A* a = new B;
    a->foo();
    A* b = new B;
    *reinterpret_cast<void**>(b) = 0x0;
    b->foo();
 
    return 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b86c7c06d84e49a19c63083cc0a0cce1~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从汇编指令看是core在了mov (%rax), %rax，结合指令上下文可发现是在虚函数地址寻址操作，对比两个变量的虚函数表即可发现是函数地址load错误导致的core。</p>
<h3 data-id="heading-28"></h3>
<h3 data-id="heading-29"><strong>3.4.6 总结</strong></h3>
<p>定位core的基本流程可总结为以下几步：</p>
<ol>
<li>
<p>明确core的大致触发原因。机器问题？自身程序问题？</p>
</li>
<li>
<p>定位代码行。哪一行代码出现了问题。</p>
</li>
<li>
<p>定位执行指令。哪一行指令干了什么事。</p>
</li>
<li>
<p>定位异常变量。指令不会有问题，是指令操作的变量不符合预期。</p>
</li>
</ol>
<p>善于利用汇编指令以及打印指令（x、print、display）可以更有效的定位Core。</p>
<h1 data-id="heading-30"><strong>参考资料：</strong></h1>
<p>汇编查看工具：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgodbolt.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://godbolt.org/" ref="nofollow noopener noreferrer">godbolt.org/</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcppinsights.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cppinsights.io/" ref="nofollow noopener noreferrer">cppinsights.io/</a><br>
标准GDB文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsourceware.org%2Fgdb%2Fcurrent%2Fonlinedocs%2Fgdb%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://sourceware.org/gdb/current/onlinedocs/gdb/" ref="nofollow noopener noreferrer">sourceware.org/gdb/current…</a></p>
<p><strong>招聘信息：</strong></p>
<p>欢迎加入百度移动生态事业群内容中台架构团队，我们常年需求后端、C++、模型架构、大数据、性能调优的同学、社招，实习，校招都要哦</p>
<p>简历投递邮箱：<a href="https://link.juejin.cn/?target=mailto%3Ageektalk%40baidu.com" target="_blank" title="mailto:geektalk@baidu.com" ref="nofollow noopener noreferrer">geektalk@baidu.com</a> （投递备注【内容架构】）</p>
<p><strong>推荐阅读</strong>：</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">｜面向大规模商业系统的数据库设计和实践</a></p>
<p>｜<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497425%26idx%3D1%26sn%3D27ea50893896ba590613fffbd5221795%26chksm%3Dc03ec6adf7494fbbdb5f6649f328059e2ff46efe83f9e93a31f3d0b15c0abc6a89affd57c1a5%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497425&idx=1&sn=27ea50893896ba590613fffbd5221795&chksm=c03ec6adf7494fbbdb5f6649f328059e2ff46efe83f9e93a31f3d0b15c0abc6a89affd57c1a5&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">百度爱番番移动端网页秒开实践</a></p>
<p>｜<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497221%26idx%3D1%26sn%3D3d215bade9fa07297acf2cdcaf0e4b92%26chksm%3Dc03ec679f7494f6fc3d41ad3b5cfed065c16119a087037aad84029e95098137ee8be0d4185c2%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497221&idx=1&sn=3d215bade9fa07297acf2cdcaf0e4b92&chksm=c03ec679f7494f6fc3d41ad3b5cfed065c16119a087037aad84029e95098137ee8be0d4185c2&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">解密百TB数据分析如何跑进45秒</a></p>
<p>---------- END ----------</p>
<p><strong>百度Geek说</strong></p>
<p>百度官方技术公众号上线啦！</p>
<p>技术干货 · 行业资讯 · 线上沙龙 · 行业大会</p>
<p>招聘信息 · 内推信息 · 技术书籍 · 百度周边</p>
<p>欢迎各位同学关注</p></div>  
</div>
            