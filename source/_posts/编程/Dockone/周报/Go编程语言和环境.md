
---
title: 'Go编程语言和环境'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/c52a9e77fa8b002416827a7095181837.jpg'
author: Dockone
comments: false
date: 2022-05-16 08:12:12
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/c52a9e77fa8b002416827a7095181837.jpg'
---

<div>   
<br>Go 是一种编程语言，2007 年底在谷歌创建，2009 年 11 月正式开源发布。从那时起，它开始作为一个公共项目运作，有成千上万的个人和数十家公司参与贡献。Go 已成为构建云基础设施的流行语言：Linux 容器管理器 Docker 和容器部署系统 Kubernetes 是用 Go 编写的核心云技术。今天，Go 是每个主要云提供商的关键基础设施的基础，并且是云原生计算基金会托管的大多数项目的实现语言。<br>
<br>早期用户被 Go 吸引的原因有很多。用于构建系统的垃圾收集、静态编译的语言，这并不常见。Go 对并发和并行的原生支持有助于利用当时成为主流的多核机器。自包含的二进制文件和简单的交叉编译简化了部署。而谷歌的名字无疑也是一个加成。<br>
<br>但是为什么用户能留下来？为什么Go 变得越来越流行，而许多其他语言项目却没有？我们相信语言本身只是答案的一小部分。完整的故事必须涉及整个 Go 环境：库、工具、约定和软件工程的整体方法，它们都支持使用该语言进行编程。因此，在语言设计中做出的最重要的决定是让 Go 更适合大型软件工程，并帮助我们吸引志同道合的开发人员。<br>
<br>本文研究了我们认为对 Go 的成功作出最大贡献的设计决策，探索它们如何不仅适用于语言，还适用于更广泛的环境。很难分离出某个特定决策的贡献，因此本文不应被视为科学分析，而应作为对过去十年经验和用户反馈的最佳理解的呈现。<br>
<h3>起源</h3>Go 源于在 Google 构建大型分布式系统的经验，在由数千名软件工程师共享的大型代码库中工作。我们希望为这种环境设计的语言和工具能够解决公司和整个行业面临的挑战。由于开发工作的规模和正在部署的生产系统的规模，挑战出现了。<br>
<br><strong>发展规模</strong>。在开发方面，Google 在 2007 年有大约 4,000 名活跃用户使用单一、共享、多语言（C++、Java、Python）代码库。单一代码库可以很容易地修复，例如内存分配器的问题正在减慢主 Web 服务器的响应速度。但是在使用这些库时，很容易在不知不觉中破坏以前的客户端，因为很难找到包的所有依赖项。<br>
<br>此外，在我们使用的现有语言中，导入一个库可能会导致编译器递归加载一个导入的所有库。在 2007 年的一次 C++ 编译中，我们观察到编译器（在<code class="prettyprint">#include</code>处理之后）在处理一组总计 4.2 MB 的文件时读取了超过 8 GB 的数据，在一个已经很大的程序上，扩展因子几乎是 2,000。如果为编译给定源文件而读取的头文件数量随源文件树呈线性增长，则整个树的编译成本呈二次方增长。<br>
<br>为了解决这样的减速问题，我们开始着手开发一个新的、大规模并行和可缓存的构建系统，该系统最终成为开源的 Bazel 构建系统。但并行和缓存对于修复低效系统的作用有限。我们认为语言本身需要做更多的事情来提供帮助。<br>
<br><strong>生产规模</strong>。在生产方面，谷歌运行着很多非常大的系统。例如，在 2005 年 3 月，Sawzall 日志分析系统的一个 1,500-CPU 集群处理了 2.8 PB 的数据。2006 年 8 月，Google 的 388 个 Bit-table 服务集群由 24,500 台平板服务器组成，其中一组 8,069 台服务器每秒处理总计 120 万个请求。<br>
<br>然而，谷歌和业内其他公司一样，都在努力编写高效的程序以充分利用多核系统。我们的许多系统都需要在一台机器上运行相同二进制文件的多个副本，因为现有的多线程支持既麻烦又低性能。大型、固定大小的线程堆栈、重量级堆栈开关以及用于创建新线程和管理它们之间交互的笨拙语法都使得使用多核系统变得更加困难。但很明显，服务器里的核数量只会持续增加。<br>
<br>在这里，我们也相信语言本身可以通过提供轻量级、易于使用的并发原语来提供帮助。我们还在这些额外的内核中看到了一个机会：垃圾收集器可以与专用内核上的主程序并行运行，从而降低其延迟成本。<br>
<br>Go 是我们对于应对这些挑战的语言可能是什么样子的问题的回答。毫无疑问，Go受欢迎的部分原因是整个科技行业现在每天都面临着这些挑战。云提供商使即使是最小的公司也可以实现非常大的生产部署。虽然大多数公司没有数千名活跃的员工在编写代码，但几乎所有公司现在都依赖于由数千名程序员开发的大量开源的基础设施。<br>
<br>本文的其余部分将探讨具体的设计决策如何实现这些扩展开发和生产的目标。我们从核心语言本身开始，向外拓展到周围环境。我们不会对语言进行完整的介绍。为此，请参阅 Go 语言规范或诸如《The Go Programming Language》等书籍。<br>
<h3>包（Package）</h3>Go 程序由一个或多个可导入包组成，每个包包含一个或多个文件。图 1 中的 Web 服务器说明了有关 Go 包系统设计的许多重要细节：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220504/c52a9e77fa8b002416827a7095181837.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/c52a9e77fa8b002416827a7095181837.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1. 一个Go的web服务器</em><br>
<br>该程序启动一个本地 Web 服务器（第 9 行），该服务器通过调用 <code class="prettyprint">hello</code> 函数来处理每个请求，该函数以消息 “hello, world”（第 14 行）进行响应。<br>
<br>一个包使用显式 <code class="prettyprint">import</code> 语句（第 3-6 行）导入另一个包，这与许多语言一样，但与 C++ 的文本 <code class="prettyprint">#include</code> 机制相反。然而，与大多数语言不同的是，Go 的每次导入只读取一个文件。例如，<code class="prettyprint">fmt</code> 包的公开 API 引用来自 <code class="prettyprint">io</code> 包的类型：<code class="prettyprint">fmt.Fprintf</code> 的第一个参数是 <code class="prettyprint">io.Writer</code> 类型的接口值。在大多数语言中，编译器处理 <code class="prettyprint">fmt</code> 导入时还需要加载所有 <code class="prettyprint">io</code> 以便理解 <code class="prettyprint">fmt</code> 的定义，这反过来可能就需要加载额外的包以理解所有 <code class="prettyprint">io</code> 的定义。单个导入语句可能最终需要处理数十或数百个包。<br>
<br>Go 避免了这项工作，类似于 Modula-2，为编译的 <code class="prettyprint">fmt</code> 包的元数据安排包含了解其自身依赖项所需的所有内容，例如 <code class="prettyprint">io.Writer</code> 的定义。因此，<code class="prettyprint">import &quot;fmt&quot;</code> 的编译只读取一个完整描述 <code class="prettyprint">fmt</code> 及其依赖关系的文件。此外，这种扁平化只进行一次，在编译 <code class="prettyprint">fmt</code> 时进行，避免每次导入时的多次加载。这种方法可以减少编译器的工作量并加快构建速度，从而有助于大规模开发。此外，包的循环导入是不允许的：因为 <code class="prettyprint">fmt</code> 导入 <code class="prettyprint">io</code>，<code class="prettyprint">io</code> 不能导入 <code class="prettyprint">fmt</code>，也不能导入其他导入了 <code class="prettyprint">fmt</code> 的包，即使是间接导入。这也减少了编译器的工作量，确保特定构建可以在拆分成单个的、分别编译的包。这也就支持了增量程序分析，甚至在运行测试之前就可以运行它以捕获错误，如下所述。<br>
<br>导入 <code class="prettyprint">fmt</code> 不会使 <code class="prettyprint">io.Writer</code> 对客户端可用。如果主包想要使用 <code class="prettyprint">io.Writer</code> 类型，它必须自己去 <code class="prettyprint">import &quot;io&quot;</code>。因此，一旦从源文件中删除了对 <code class="prettyprint">fmt</code> 限定名称的所有引用——例如，如果 <code class="prettyprint">fmt.Fprintf</code> 调用被删除——<code class="prettyprint">import &quot;fmt&quot;</code> 语句就可以安全地从源文件中删除而无需进一步分析。这样的属性使得可以自动管理源代码中的导入。事实上，Go 不允许导入未被使用的包，以避免将未使用的代码链接到程序里而造成的不必要的膨胀。<br>
<br>导入路径是带引号的字符串文字，这样可以灵活地对其进行解释。斜杠分隔的路径在 <code class="prettyprint">import</code> 中标识了导入的包，但是随后源代码使用包语句中声明的短标识符来引用包。例如，<code class="prettyprint">import &quot;net/http&quot;</code> 声明了提供访问其内容的顶级名称 <code class="prettyprint">http</code>。在标准库之外，包由以域名开头的类似 URL 的路径来标识，如 <code class="prettyprint">import &quot;github.com/google/uuid&quot;</code>。稍后我们将对此类软件包进行更多说明。<br>
<br>最后一个细节，请注意名称 <code class="prettyprint">fmt.Fprintf</code> 和 <code class="prettyprint">io.Writer</code> 中的大写字母。Go 对 C++ 和 Java 的 public、private 和 protected 概念和关键字的模拟是一种命名约定。带有前导大写字母的名称，例如 <code class="prettyprint">Printf</code> 和 <code class="prettyprint">Writer</code>，被 “导出”（公开）。其他则不是。基于大小写、编译器强制执行的导出规则适用于常量、函数和类型的包级标识符；方法名称；和结构字段名称。我们确定这条规则是为了避免在公开 API 中涉及的每个标识符旁边都需要写一个关键字（如 <code class="prettyprint">export</code>）。随着时间的推移，我们开始重视查看标识符是在包外部可用还是纯粹在内部可用。<br>
<h3>类型</h3>Go 提供了一组常用的基本类型：布尔值、大小整数如 <code class="prettyprint">uint8</code> 和 <code class="prettyprint">int32</code>、无大小的 <code class="prettyprint">int</code> 和 <code class="prettyprint">uint</code>（32 位或 64 位，取决于机器大小），以及大小的浮点数和复数。它以类似于 C 的方式提供指针、固定大小的数组和结构。它还提供内置的字符串类型、称为 map 的哈希表和称为 slice 的动态大小的数组。大多数 Go 程序都依赖这些类型，没有其他特殊的容器类型。<br>
<br>Go 不定义类，但允许将方法绑定到任何类型，包括结构、数组、slice、map 甚至是整数等基本类型。它没有类型的层次结构；我们认为继承往往会使程序在成长过程中更难适应。相反，Go 鼓励类型的组合。<br>
<br><blockquote><br>如今，Go 是主流云提供商的关键基础架构的基石。</blockquote>Go 通过其接口类型提供了面向对象的多态性。与 Java 接口或 C++ 抽象虚拟类一样，Go 接口包含方法名称和签名的列表。比如前面提到的 <code class="prettyprint">io.Writer</code> 接口是在 <code class="prettyprint">io</code> 包中定义的，如图 2 所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220504/8bcf99fd59013c2176e88f3ba24778e2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/8bcf99fd59013c2176e88f3ba24778e2.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 2. io 包的 Writer 接口</em><br>
<br><code class="prettyprint">Write</code> 接受一个字节 slice 并返回一个整数以及可能的错误。与 Java 和 C++ 不同，任何具有与接口相同名称和签名的方法的 Go 类型都被认为实现了该接口，而无需明确声明它这样做。例如，类型 <code class="prettyprint">os.File</code> 有一个具有相同签名的 <code class="prettyprint">Write</code> 方法，因此它实现了 <code class="prettyprint">io.Writer</code>，而不需要像 Java 那样显式的 “implements” 注释。<br>
<br>避免接口和实现之间的显式关联允许 Go 程序员定义小的、灵活的、通常是 ad hoc 接口，而不是将它们用作复杂类型层次结构中的基础块。它鼓励在开发过程中捕获关系和操作，而不需要提前计划和定义它们。这尤其有助于大型程序，在这些程序中，刚开始开发时，最终的结构更加难以看清。无需声明实现的方式鼓励使用精确的、一种或两种方法的接口，例如 <code class="prettyprint">Writer、Reader、Stringer</code>（类似于 Java 的 <code class="prettyprint">toString</code> 方法）等，这些接口遍布标准库。<br>
<br>首次学习 Go 的开发人员经常担心某个类型会意外地实现某个接口。虽然很容易建立假设，但实际上不太可能为两个不兼容的操作选择相同的名称和签名，而且我们从未在真正的 Go 程序中看到过这种情况。<br>
<h3>并发</h3>当我们开始设计 Go 时，多核计算机变得广泛可用，但线程仍然是所有流行语言和操作系统中的重量级概念。创建、使用和管理线程的困难使它们不受欢迎，限制了对多核 CPU 全部功能的使用。解决这种紧张关系是创建 Go 的主要动机之一。<br>
<br>Go 在语言本身中包含多个并发控制线程的概念，称为 <em>goroutine</em>，在单个共享地址空间中运行并有效地多路复用到操作系统线程上。对阻塞操作的调用，例如从文件或网络中读取，只会阻塞执行该操作的 goroutine；线程上的其他 goroutine 可能会移动到另一个线程，以便在调用者被阻塞时它们可以继续执行。Goroutines 开始时只有几千字节的堆栈，可以根据需要调整大小，无需程序员参与。开发人员将 goroutine 用作构建程序的丰富且廉价的原语。服务器程序拥有数千甚至数百万个 goroutine 是很正常的，因为它们比线程便宜得多。<br>
<br>例如，<code class="prettyprint">net.Listener</code> 是一个带有 <code class="prettyprint">Accept</code> 方法的接口，可以侦听并返回新的入站网络连接。图 3 显示了一个函数 <code class="prettyprint">listen</code>，它接受连接并启动一个新的 goroutine 来为每个连接运行 serve 函数。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220504/3fd39f44a0a3191aec2f6c52f981e3cc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/3fd39f44a0a3191aec2f6c52f981e3cc.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 3. Go 网络服务器</em><br>
<br>监听函数体中的无限 <code class="prettyprint">for</code> 循环（第 22-28 行）调用 <code class="prettyprint">listener.Accept</code>，它返回两个值：连接和可能的错误。假设没有错误，<code class="prettyprint">go</code> 语句（第 27 行）在一个新的 goroutine 中开始它的参数——函数调用 <code class="prettyprint">serve(conn)</code>，类似于 Unix shell 命令的 & 后缀，但在同一个操作系统进程中。要调用的函数及其参数在原始 goroutine 中进行评估；这些值被复制以创建新 goroutine 的初始堆栈帧。因此，该程序为每个传入的网络连接运行一个独立的 <code class="prettyprint">serve</code> 函数实例。<code class="prettyprint">serve</code> 的一次调用处理一个给定连接上的请求（第 37 行对 <code class="prettyprint">handle(req)</code> 的调用没有  <code class="prettyprint">go</code> 前缀）；每个调用都可以阻塞而不影响其他网络连接的处理。<br>
<br>在底层，Go 实现使用了高效的多路复用操作，例如 Linux 的 epoll，来处理并发 I/O 操作，但用户看不到这一点。相反，Go 运行时库提供了阻塞 I/O 的抽象，其中每个 goroutine 都按顺序执行——不需要回调——这很容易推理。<br>
<br>在创建了多个 goroutine 之后，程序必须经常在它们之间进行协调。Go 提供了<em>通道（channel）</em>，它允许 goroutine 之间的通信和同步：通道是一个单向的、有限大小的管道，在 goroutine 之间传输类型化的消息。Go 还提供了一个多路 <code class="prettyprint">select</code> 原语，可以根据哪些通信可以进行来控制执行。这些想法改编自 Hoare 的 “Communicating Sequential Processes” 和早期的语言实验，特别是 Newsqueak、Alef、和 Limbo。<br>
<br>图 4 显示了另一种版本的 <code class="prettyprint">listen</code>，用于限制任意时刻服务的连接数。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220504/e0080295f85ee05485d8520db4c6cd2f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/e0080295f85ee05485d8520db4c6cd2f.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 4. Go 网络服务器，限制 10 个连接</em><br>
<br>这个版本的 <code class="prettyprint">listen</code> 首先创建一个名为 <code class="prettyprint">ch</code> 的通道（第 42 行），然后启动一个包含 10 个服务器 goroutine 的池（第 44-46 行），它们从单个通道接收连接。当新连接被接受时，<code class="prettyprint">listen</code> 使用 send 语句在 <code class="prettyprint">ch</code> 上发送每个连接，<code class="prettyprint">ch &lt; - conn</code>（第 53 行）。服务器执行接收表达式 <code class="prettyprint">&lt; - ch</code>（第 59 行），完成通信。创建通道时没有空间来缓冲正在发送的值（Go 中的默认值），因此在 10 个服务器忙于前 10 个连接后，第十一个 <code class="prettyprint">ch &lt; - conn</code> 将被阻塞，直到服务器完成其对服务的调用并执行新连接。阻塞的通信操作对侦听器产生隐含的背压，阻止它接受新连接，直到它处理完前一个连接。<br>
<br>请注意这些程序中缺少互斥锁或其他传统同步机制。通道上数据值的通信兼作同步；按照惯例，在通道上发送数据会将所有权从发送者传递给接收者。Go 有提供互斥体、条件变量、信号量和原子值的库以供底层使用，但通道通常是更好的选择。根据我们的经验，和互斥锁和条件变量相比，人们更容易理解消息传递（使用通信在 goroutine 之间转移所有权）。早期的口头禅是：“不要通过共享内存进行交流；相反，要通过交流来共享内存。”<br>
<br>Go 的垃圾收集器极大地简化了并发 API 的设计，消除了关于哪个 goroutine 负责释放共享数据的问题。与大多数语言一样（但与 Rust 不同），类型系统不会静态跟踪可变数据的所有权。相反，Go 与 TSAN 集成，以提供用于测试和有限生产​​用途的动态竞争检测器。<br>
<h2>安全</h2>出现任何新语言的部分原因是为了解决以前语言的缺陷，在 Go 的案例中，包括影响网络软件安全的安全问题。Go 删除​​了 C 和 C++ 程序中导致许多安全问题的未定义行为。整数类型不会自动相互强制转换。空指针取消引用和越界数组和slice索引会导致运行时异常。堆栈帧中没有悬空指针：任何可能超过其堆栈帧的变量，例如在闭包中捕获的变量，都将被移动到堆中。堆中也没有悬空指针；使用垃圾收集器代替手动内存管理消除了释放后使用错误。当然，Go 并不能解决所有问题，而且有些事情可能本应被解决。例如，整数溢出可能已成为运行时错误。<br>
<br>由于 Go 是一种用于编写系统的语言，它可能要求破坏类型安全的机器级操作，因此它能够将指针从一种类型强制转换为另一种类型并执行地址算术，但只能通过使用 <code class="prettyprint">unsafe</code> 包及其限制特殊类型 <code class="prettyprint">unsafe.Pointer</code>。必须注意保持类型系统违规与垃圾收集器兼容——例如，垃圾收集器必须始终能够识别特定单词是整数还是指针。在实践中，<code class="prettyprint">unsafe</code> 包很少出现：safe Go 相当有效。因此，看到 <code class="prettyprint">import &quot;unsafe&quot;</code> 是一个信号，需要更仔细地检查源文件是否存在可能的安全问题。<br>
<br>Go 的安全特性使其比 C 或 C++ 等语言更适合加密和其他特别需要关注安全的代码。一个小错误，例如数组越界索引，就可能导致敏感数据泄露或 C 和 C++ 中的远程执行，这样的错误在 Go 中会导致运行时异常，直接停止程序，这可以极大地限制潜在影响的范围。 Go 附带一整套加密库，包括 SSL/TLS 的支持；标准库包括生产可用的 HTTPS 客户端和服务器。事实上，Go 结合了安全性、性能和高质量库，使其成为现代安全工作的热门试验场。例如，免费提供的证书颁发机构 Let's Encrypt 的生产服务依赖于 Go，并且最近跨越了发行 10 亿个证书的里程碑。 <br>
<h3>完整性</h3>Go 在语言、库和工具级别提供了现代开发所需的核心部分。这里需要谨慎的平衡，添加足够的 “开箱即用” 工具，同时又不会添加太多以至于我们自己的开发过程会因为试图支持太多功能而陷入困境。<br>
<br>该语言提供字符串、哈希 map 和动态大小的数组作为内置的、易于使用的数据类型。如前所述，这些对于大多数 Go 程序来说已经足够了。结果是 Go 程序之间的互操作性更高——例如，没有字符串或哈希 map 的竞争实现来分割包的生态系统。 Go 包含 goroutine 和通道是另一种形式的完整性。这些提供了现代网络程序所需的核心并发功能。与库相比，直接以语言提供它们可以更容易地调整语法、语义和实现，以使它们尽可能轻量级并易于使用，同时为所有用户提供统一的方法。<br>
<br>标准库包括一个生产可用的 HTTPS 客户端和服务器。对于与 Internet 上的其他机器交互的程序，这是至关重要的。直接满足这种需求可以避免额外的碎片化。我们已经看到了 <code class="prettyprint">io.Writer</code> 接口；任何输出数据流都按约定实现此接口，并与所有其他 I/O 适配器互操作。作为另一个示例，图 1 的 <code class="prettyprint">ListenAndServe</code> 调用需要类型为 <code class="prettyprint">http.Handler</code> 的第二个参数，其定义如图 5 所示。参数 <code class="prettyprint">http.HandlerFunc(hello)</code> 通过调用 <code class="prettyprint">hello</code> 实现其 <code class="prettyprint">ServeHTTP</code> 方法。该库创建了一个新的 goroutine 来处理每个连接，如本文 “并发” 部分中的侦听器示例所示，因此可以以简单的阻塞样式编写处理程序，并且服务器可以自动扩展以处理许多并发连接。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220504/b7285da516f389c5153f402e8be73fa2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220504/b7285da516f389c5153f402e8be73fa2.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图 5. net/http 包 handler 接口</em><br>
<br><code class="prettyprint">http</code> 包还提供了一个基本的调度程序，它本身是 <code class="prettyprint">Handler</code> 的另一个实现，它允许为不同的 URL 路径注册不同的处理程序。将 <code class="prettyprint">Handler</code> 建立为商定的接口使许多不同类型的 HTTP 服务器中间件能够被创建和互操作。我们不需要将所有这些实现添加到标准库中，但我们确实需要建立允许它们一起工作的接口。<br>
<br>标准的 Go 发行版还为交叉编译、测试、分析、代码覆盖、模糊测试等提供集成支持。测试是另一个在核心概念上达成一致的领域——例如测试用例是什么以及它是如何运行的——可以创建自定义测试库和测试执行环境，它们都可以很好地互操作。<br>
<h3>一致性</h3>Go 的一个目标是让它在不同的实现、执行上下文甚至随着时间的推移中表现得一样。这种 “无聊” 的一致行为让开发人员可以专注于他们的日常工作，并让 Go 退居幕后。<br>
<br>首先，该语言尽可能地指定一致的结果，即使对于诸如空指针取消引用和超出范围的数组索引等错误行为，如本文的 “安全” 部分所述。 Go 需要不一致行为的一个例外是对哈希 map 的迭代。我们发现程序员经常不经意地编写依赖于哈希函数的代码，导致在不同的架构或 Go 实现上产生不同的结果。<br>
<br>为了使程序在任何地方都表现相同，一种选择是强制使用特定的散列函数。相反，Go 定义 map 迭代是非确定性的。该实现对每个 map 使用不同的随机种子，并在哈希 map 中的随机偏移处开始对 map 的每次迭代。结果是 map 在实现之间始终是不可预测的：代码不会意外地依赖于实现细节。同样，竞争检测器为调度决策增加了额外的随机性，创造了更多观察竞争的机会。<br>
<br><blockquote><br>当我们开始设计 Go 时，多核计算机变得广泛可用，但线程仍然是所有流行语言和操作系统中的重量级概念。</blockquote>一致性的另一个方面是程序生命周期内的性能。使用传统编译器，而不是 Java 和 Node.js 等语言使用的 JIT，来实现 Go 的决定在启动时和短期程序中提供了一致的性能：没有 “慢启动” 来惩罚进程生命周期的前几秒。这种快速启动使 Go 成为命令行工具（如上一节所述），和 Google App Engine 这样可扩展网络服务器的上佳选择。<br>
<br>一致的性能包括垃圾收集的开销。最初的 Go 原型使用​​了一个基本的、让一切停止的垃圾收集器，当然，这在网络服务器中引入了显著的尾部延迟。今天，Go 使用完全并发的垃圾收集器，其暂停时间不到一毫秒，通常只有几微秒，与堆大小无关。主要延迟是操作系统将信号传递给必须中断的线程所花费的时间。<br>
<br>最后一种一致性是随着时间的推移语言和库的一致性。在 Go 存在的最初几年，我们在每周发布的每个版本中都对其进行了修补和调整。用户在更新到新的 Go 版本时经常不得不更改他们的程序。自动化工具减轻了负担，但也需要手动调整。从 2012 年发布的 Go 1.0 开始，我们公开承诺只对语言和标准库进行向后兼容的更改，以便程序在使用较新的 Go 版本编译时可以继续以不变的方式运行。这一承诺吸引了业界，并鼓励那些长期存在的工程项目的使用，以及其他努力，例如书籍、培训课程和蓬勃发展的第三方软件包生态系统。<br>
<h3>工具辅助开发</h3>大规模软件开发需要大量的自动化和工具。从一开始，Go 就旨在通过使其易于创建来鼓励此类工具。<br>
<br>开发者对 Go 的日常体验是通过 <code class="prettyprint">go</code> 命令进行的。与只编译或运行代码的语言命令不同，<code class="prettyprint">go</code> 命令为开发周期的所有关键部分提供子命令：<code class="prettyprint">go build</code> 和 <code class="prettyprint">go install</code> 构建并安装可执行文件，<code class="prettyprint">go test</code> 运行测试用例，<code class="prettyprint">go get</code> 添加新的依赖项。 <code class="prettyprint">go</code> 命令还通过提供对构建详细信息（例如包图）的编程访问来启用新工具的创建。<br>
<br>一个这样的工具是 <code class="prettyprint">go vet</code>，它执行增量的、一次打包的程序分析，可以以缓存编译的目标文件一样的方式进行缓存，来支持增量构建。<code class="prettyprint">go vet</code> 工具旨在以高精度识别常见的正确性问题，以便开发人员有条件注意其报告。简单的示例包括检查调用 <code class="prettyprint">fmt.Printf</code> 和相关函数时格式和参数是否匹配，或诊断未使用的变量或结构字段写入。这些不是编译器错误，因为我们不希望旧代码仅仅因为识别出新的可能错误而停止编译。它们也不是编译器警告；用户学会忽略这些。将检查放置在单独的工具中可以让它们在开发人员方便的时间运行，而不会干扰普通的构建过程。它还使所有开发人员都可以使用相同的检查，即使在使用 Go 编译器的替代实现时，例如 Gccgo 或 Gollvm。增量方法使这些静态检查足够高效，我们可以在 <code class="prettyprint">go test</code> 期间自动运行它们，然后再运行测试自己。测试是用户寻找错误的时候，报告通常有助于解释实际的测试错误。这个增量框架也可供其他工具重用。<br>
<br>分析程序的工具很有帮助，但编辑程序的工具更好，特别是对于程序维护，其中大部分是乏味的，而且是可以自动化的。<br>
<br>Go 程序的标准布局是通过算法定义的。<code class="prettyprint">gofmt</code> 工具将源文件解析为抽象语法树，然后使用一致应用的布局规则将其格式化回源代码。在 Go 中，最佳实践是将代码存储到源码控制之前对其进行格式化。这种方法使成千上万的开发人员能够在共享代码库上工作，而无需浪费大量时间辩论大括号的样式和其他细节。更重要的是，工具可以通过操作抽象语法的格式，然后使用 <code class="prettyprint">gofmt</code> 的 printer 写出结果来修改 Go 程序。只有实际更改的部分才会被触及，从而导致 “差异” 与人们手动到达的部分相匹配。人员和程序可以在同一个代码库中无缝协作。<br>
<br>为了启用这种方法，Go 的语法旨在使源文件能够在没有类型信息或任何其他外部输入的情况下被解析，并且没有预处理器或其他宏系统。Go 标准库提供了包，允许工具重新创建 <code class="prettyprint">gofmt</code> 的输入和输出，以及完整的类型检查器。<br>
<br>在发布 Go 1.0（第一个稳定的 Go 版本）之前，我们编写了一个名为 <code class="prettyprint">gofix</code> 的重构工具，它使用这些包来解析源代码、重写树并编写格式良好的代码。例如，当从 map 中删除条目的语法发生更改时，我们使用 <code class="prettyprint">gofix</code>。每次用户更新到新版本时，他们也可以在其源文件上运行 <code class="prettyprint">gofix</code> 自动应用所需的大部分变更，从而更新到新版本。<br>
<br>这些技术也适用于支持 Go 程序员的 IDE 插件和其他工具（profiler、调试器、分析器、构建自动化器、测试框架等）的构建。 Go 的常规语法，已建立的算法代码布局约定，和直接的标准库支持，使这些工具比其他方式更容易构建。因此，Go 世界拥有了一个丰富的、不断扩展的、互操作的工具包。<br>
<h3>库函数</h3>在语言和工具之后，用户体验 Go 的下一个关键方面是可用的库函数。作为一种适合分布式计算的语言，在 Go 里，没有发布 Go 包的中央服务器。相反，每个以域名开头的导入路径都被解释为一个 URL（带有隐式前导 https://），给出了远程源代码的位置。例如， <code class="prettyprint">import &quot;github.com/google/uuid&quot;</code> 获取托管在相应 GitHub 存储库中的代码。<br>
<br>托管源代码的最常见方式是指向公共 Git 或 Mercurial 服务器，但同样支持私有服务器，并且作者可以选择发布静态文件包，而不是开放对源代码控制系统的访问。这种灵活的设计和易于发布的库创建了一个蓬勃发展的可导入 Go 包社区。依靠域名避免了在扁平的包名称空间中作出声明来抢占有价值的条目。<br>
<br>仅仅下载包是不够的；我们还必须知道要使用什么版本。 Go 将包分组为称为模块的版本化单元。模块可以为其依赖项之一指定最低要求的版本，但没有其他约束。在构建特定程序时，Go 通过选择最大值来解决依赖模块的版本竞争问题：如果程序的一部分需要依赖项的 1.2.0 版本，而另一部分需要 1.3.0 版本，则 Go 选择 1.3.0 版本——也就是说，Go 需要使用语义版本控制，其中版本 1.3.0 必须是 1.2.0 的直接替代品。另一方面，在这种情况下，即使版本 1.4.0 可用，Go 也不会选择，因为程序的任何部分都没有明确要求更新的版本。此规则保证了构建的可重复性，并将新版本引入的意外破坏的潜在风险降至最低。<br>
<br>在语义版本控制中，模块可能仅在新的主要版本（例如 2.0.0）中引入有意的破坏性更改。在 Go 中，从 2.0.0 开始的每个主要版本都由其导入路径中的主要版本后缀（例如 <code class="prettyprint">/v2</code>）标识：不同的主要版本与任何其他具有不同名称的模块保持独立。这种方法不允许钻石依赖问题，并且在实践中它适应不兼容性并且具有更细粒度约束的系统。<br>
<br>为了提高从 Internet 上下载包的构建的可靠性和可重复性，我们运行 Go 工具链中默认使用的两项服务：可用 Go 包的公共镜像和其预期内容的加密签名透明日志。尽管如此，从 Internet 下载的软件包的广泛使用仍然存在安全和其他风险。我们正在努力使 Go 工具链能够主动识别并向用户报告易受攻击的软件包。<br>
<h3>结论</h3>尽管大多数语言的设计都集中在语法、语义或类型方面的创新，但 Go 专注于软件开发过程本身。Go 高效、易于学习且免费提供，但我们相信它成功的原因在于编写程序的方法，尤其是在多个程序员在共享代码库上工作的情况下。该语言本身的主要不寻常属性——并发性——解决了 2010 年代多核 CPU 激增所出现的问题。但更重要的是为软件开发世界的打包、依赖关系、构建、测试、部署和其他日常任务建立基础的早期工作，这些方面通常在语言设计中并不重要。<br>
<br>这些想法吸引了志同道合的开发人员，他们重视结果：简单的并发性、清晰的依赖关系、可扩展的开发和生产、安全的程序、简单的部署、自动代码格式化、工具辅助开发等等。那些早期的开发人员帮助普及了 Go，并为最初的 Go 包生态系统播下了种子。他们还推动了该语言的早期发展，例如，将编译器和库移植到 Windows 和其他操作系统（最初的版本仅支持 Linux 和 MacOS X）。<br>
<br>不是每个人都喜欢——例如，有些人反对这种语言省略了继承和泛型类型等常见的特性。但是 Go 以开发为中心的理念足够有趣和有效，以至于社区在保持最初推动 Go 存在的核心原则的同时蓬勃发展。在很大程度上要归功于该社区及其构建的技术，Go 现在已成为现代云计算环境的重要组成部分。<br>
<br>自从 Go 1.0 发布以来，该语言几乎被冻结了。然而，相关的工具已经显著扩展，拥有了更好的编译器、更强大的构建和测试工具以及改进的依赖管理，更不用说支持 Go 的大量开源工具了。尽管如此，变化即将到来：2022 年 3 月发布的 Go 1.18 包含对语言进行真正更改的第一个版本，这个需求被广泛要求——参数多态性的第一次削减。我们在原始语言中留下了任何形式的泛型，因为我们敏锐地意识到设计良好是非常困难的，而且在其他语言中，这往往是复杂性而非生产力的来源。在 Go 的第一个十年中，我们考虑了一些设计，但直到最近才发现适合 Go 的设计。在坚持一致性、完整性和社区性原则的同时进行如此大的语言更改将是对该方法的严峻考验。<br>
<h3>致谢</h3>Go 最早的工作得益于 Google 许多同事的建议和帮助。自从公开发布以来，由于 Google 扩大了 Go 团队以及大量的开源贡献者，Go 得到了发展和改进。Go 现在是数以千计的人的作品，这里不一一列举。我们感谢所有帮助 Go 成为今天的人。<br>
<br><strong>原文链接：<a href="https://cacm.acm.org/magazines/2022/5/260357-the-go-programming-language-and-environment/fulltext">The Go Programming Language and Environment</a>（翻译：崔婧雯）</strong> <br>
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝<br>
译者介绍<br>
崔婧雯，现就职于IBM，高级软件工程师，负责IBM WebSphere业务流程管理软件的系统测试工作。曾就职于VMware从事桌面虚拟化产品的质量保证工作。对虚拟化，中间件技术，业务流程管理有浓厚的兴趣。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            