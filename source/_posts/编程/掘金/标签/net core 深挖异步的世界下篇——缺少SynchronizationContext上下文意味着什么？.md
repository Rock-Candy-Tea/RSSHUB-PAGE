
---
title: '.net core 深挖异步的世界下篇——缺少SynchronizationContext上下文意味着什么？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a21bb14a39ce42c3a28e6e3352325e76~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 07:48:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a21bb14a39ce42c3a28e6e3352325e76~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第19天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>最近和.net core中的异步杠上了，我觉得很有必要深挖下.net core下的异步编程的方方面面，由于传统asp.net以及.net framework类库的干扰，因此网上充斥着奇奇怪怪的关于异步的言论和实践，由于没有说明环境的关系，导致大量的.net core console/asp.net core的新手，对于处理异步也存在着深深的误解，因此深挖下其本质区别，对于我自己或更多的.net core新手来说，是有巨大的帮助的。</p>
<h1 data-id="heading-1">🎏 5、您不需要ConfigureAwait（false），在编写库中尽量使用它</h1>
<p>由于不再有上下文，因此不需要ConfigureAwait(false)。任何知道它在ASP.NET Core下运行的代码都不需要显式地避免其上下文。实际上，ASP.NET Core团队本身已经放弃使用ConfigureAwait(false)。</p>
<p>但是，我仍然建议您在核心库中使用它-可以在其他应用程序中重用的任何东西。如果库中的代码也可以在UI应用程序或旧版ASP.NET应用程序中运行，或者在其他任何可能存在上下文的环境中运行，则仍应ConfigureAwait(false)在该库中使用。</p>
<h1 data-id="heading-2">🎏 6、当心隐式并行</h1>
<p>从同步上下文移到线程池上下文（即从旧版ASP.NET到ASP.NET Core）时，还有另一个主要问题。</p>
<p>旧式ASP.NETSynchronizationContext是实际的同步上下文，这意味着在请求上下文中，一次只能有一个线程实际执行代码。也就是说，异步延续可以在任何线程上运行，但一次只能运行一个。ASP.NET Core没有SynchronizationContext，因此await默认为线程池上下文。因此，在ASP.NET Core世界中，异步延续可以在任何线程上运行，并且它们都可以并行运行。</p>
<p>作为一个人为的示例，请考虑以下代码，该代码将下载两个字符串并将它们放入列表中。此代码在旧式ASP.NET中可以正常工作，因为请求上下文一次仅允许一个连续：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">private</span> HttpClient _client = <span class="hljs-keyword">new</span> HttpClient();

<span class="hljs-keyword">async</span> Task<List<<span class="hljs-built_in">string</span>>> GetBothAsync(<span class="hljs-built_in">string</span> url1, <span class="hljs-built_in">string</span> url2)
&#123;
    <span class="hljs-keyword">var</span> result = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">string</span>>();
    <span class="hljs-keyword">var</span> task1 = GetOneAsync(result, url1);
    <span class="hljs-keyword">var</span> task2 = GetOneAsync(result, url2);
    <span class="hljs-keyword">await</span> Task.WhenAll(task1, task2);
    <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-function"><span class="hljs-keyword">async</span> Task <span class="hljs-title">GetOneAsync</span>(<span class="hljs-params">List<<span class="hljs-built_in">string</span>> result, <span class="hljs-built_in">string</span> url</span>)</span>
&#123;
    <span class="hljs-keyword">var</span> data = <span class="hljs-keyword">await</span> _client.GetStringAsync(url);
    result.Add(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该result.Add(data)行一次只能由一个线程执行，因为它在请求上下文中执行。</p>
<p>但是，相同的代码在ASP.NET Core上是不安全的。具体来说，该result.Add(data)行可以由两个线程同时执行，而不保护shared List。</p>
<p>这样的代码很少见；异步代码本身具有功能，因此从异步方法返回结果比修改共享状态要自然得多。但是，异步代码的质量确实会有所不同，并且毫无疑问，其中有些代码没有充分地屏蔽并行执行。</p>
<h1 data-id="heading-3">7、异步任务需要线程吗？</h1>
<p>异步任务不会“执行”，因此不需要线程。这是最纯净的异步基本真理：<strong>没有线程</strong>。
有巨多的小白反对这一真理。他们喊道：“不，如果我正在等待操作，必须有一个正在等待的线程！这可能是线程池线程。还是操作系统线程！或带有设备驱动程序的东西……”</p>
<p>这里所说的异步任务单纯的指定为IO密集操作，如果是CPU密集操作本质上是同步的。一个线程可以通过将其装载到另一个线程来假装它是异步的。例如，UI线程可以通过将CPU绑定的代码包装在Task.Run中来假装是异步的。从UI线程的角度来看，它似乎是异步的（即，它可以等待操作）。但是从另一个线程（线程池线程）的角度来看，它仍然是同步的，因此看清楚，这里所指的是IO密集型真正的异步。
<strong>不要听那些胡言乱语。如果异步操作是纯操作，则没有线程</strong>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a21bb14a39ce42c3a28e6e3352325e76~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小白们不相信，让我们来调戏他们。</p>
<p>我们将一直跟踪到硬件的异步操作，尤其要注意.NET部分和设备驱动程序部分。我们将通过省略一些中间层细节来简化此描述，但是我们不会偏离事实。
考虑一个通用的“写”操作（对文件，网络流，USB烤面包机等）。我们的代码很简单：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">async</span> <span class="hljs-keyword">void</span> <span class="hljs-title">Button_Click</span>(<span class="hljs-params"><span class="hljs-built_in">object</span> sender, RoutedEventArgs e</span>)</span>
&#123;
  <span class="hljs-built_in">byte</span>[] data = ...
  <span class="hljs-keyword">await</span> myDevice.WriteAsync(data, <span class="hljs-number">0</span>, data.Length);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们已经知道UI线程在期间没有被阻塞await。问题：是否有另一个线程必须在“阻止祭坛”上牺牲自己，以便UI线程可以生存？</p>
<p>第一站：库（例如，输入BCL代码）。让我们假设它WriteAsync是使用.NET中基于重叠I / O的标准P / Invoke异步I / O系统实现的。因此，这将在设备的底层启动Win32重叠I / O操作HANDLE。</p>
<p>然后，操作系统转向设备驱动程序，并要求其开始写入操作。为此，首先要构造一个代表写请求的对象。这称为I / O请求包（IRP）。</p>
<p>设备驱动程序接收IRP并向设备发出命令以写出数据。如果设备支持直接内存访问（DMA），则可以像将缓冲区地址写入设备寄存器一样简单。这就是设备驱动程序所能做的；它将IRP标记为“待处理”，然后返回操作系统。</p>
<p>事实的核心在这里：处理IRP时不允许设备驱动程序阻塞。这意味着，如果该IRP无法完成立即，那么它必须被处理异步。即使对于同步API，也是如此！<strong>在设备驱动程序级别，所有请求都是异步的</strong>。</p>
<p>在IRP为“挂起”的情况下，操作系统将返回到库，该库会将未完成的任务返回到按钮单击事件处理程序，该事件处理程序将挂起async方法，并且UI线程将继续执行。</p>
<p>我们已将请求跟踪到系统的深处，一直到物理设备。</p>
<p>写入操作现在处于“运行中”状态。正在处理多少个线程？ <strong>答案是没有线程</strong>。没有设备驱动程序线程，OS线程，BCL线程或线程池线程正在处理该写操作。没有线程。</p>
<p>现在，让我们关注内核守护程序领域对（用户程序）凡人世界的响应。</p>
<p>写请求开始后的一段时间，设备完成写操作。通过中断通知CPU。</p>
<p>设备驱动程序的中断服务程序（ISR）响应该中断。中断是CPU级别的事件，它使CPU的控制权暂时脱离正在运行的任何线程。您可以将ISR视为“借用”当前正在运行的线程，但我更喜欢将ISR视为执行水平很低，以至于不存在“线程”的概念-因此它们位于所有“之下”线程，可以这么说。</p>
<p>无论如何，ISR均已正确编写，因此它所要做的就是告诉设备“感谢您的中断”，并将延迟过程调用（DPC）排队。</p>
<p>当CPU受中断困扰后，它将进入其DPC。DPC的执行水平也很低，以至于不能说“线程”。与ISR一样，DPC在线程系统“下方”直接在CPU上执行。</p>
<p>DPC接收代表写请求的IRP，并将其标记为“完成”。但是，“完成”状态仅存在于OS级别。进程具有其自己的内存空间，必须通知该内存空间。因此，操作系统会将专用内核模式的异步过程调用（APC）排队到拥有的线程中HANDLE。</p>
<p>由于库/ BCL使用的是标准P / Invoke重叠I / O系统，因此它已向线程池的一部分I / O完成端口（IOCP）注册了句柄。因此，短暂借用了一个I / O线程池线程来执行APC，这将通知任务已完成。</p>
<p>该任务已捕获UI上下文，因此它不会async直接在线程池线程上恢复该方法。而是将方法的延续性排队到UI上下文中，并且UI线程在到达该方法时将继续执行该方法。</p>
<p>因此，我们看到请求进行期间没有线程。请求完成后，各个线程被“借用”或将工作短暂排队。这项工作通常需要大约一毫秒（例如，运行在线程池中的APC）到大约一毫秒（例如，ISR）。但是没有线程被阻塞，只是在等待该请求完成。</p>
<p>释放你的心灵。不要试图找到这个“异步线程”——这是不可能的。相反，请仅尝试了解事实：
<strong>没有线程</strong>。</p>
<h1 data-id="heading-4">🎏 8、await后面的代码跑在线程池上</h1>
<p>还有一点，await后面的任何代码都将在线程池线程上运行。除非存在SynchronizationContext或，否则这是默认行为TaskScheduler。</p>
<p>这些是最常见的上下文：</p>
<ul>
<li>UI上下文-UI应用程序使用它来确保后面的代码await将在UI线程上恢复。</li>
<li>ASP.NET Classic请求上下文-由ASP.NET Classic使用，以确保后面的代码await将恢复具有相同的特定于请求的 全局属性（例如HttpContext.Current）。</li>
<li>单线程上下文-由某些测试框架（例如xUnit）用来确保后面的代码await将在同一线程上恢复。这旨在模拟UI上下文行为，但没有完整的UI线程。</li>
<li>线程池上下文-如果不存在其他上下文（例如，ASP.NET Core和控制台应用程序），则为默认值。await在线程池线程上运行之后的代码。</li>
</ul>
<h1 data-id="heading-5">🎏 9. 小结</h1>
<p>嗯，本篇已完结。</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            