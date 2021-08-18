
---
title: '.net core 深挖异步的世界上篇——缺少SynchronizationContext上下文意味着什么？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff635c4fba6149ca91b251087ec325c1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 04:10:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff635c4fba6149ca91b251087ec325c1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>最近和.net core中的异步杠上了，我觉得很有必要深挖下.net core下的异步编程的方方面面，由于传统asp.net以及.net framework类库的干扰，因此网上充斥着奇奇怪怪的关于异步的言论和实践，由于没有说明环境的关系，导致大量的.net core console/asp.net core的新手，对于处理异步也存在着深深的误解，因此深挖下其本质区别，对于我自己或更多的.net core新手来说，是有巨大的帮助的。</p>
<h1 data-id="heading-1">🎏 1、没有同步上下文（SynchronizationContext）</h1>
<p>是的，深深内置于传统asp.net 的SynchronizationContext 上下文，在asp.net core和.net core console项目内被砍掉了。
*** <strong>当然.netcore 下的winform 是有synchronizationContext的概念的</strong>***</p>
<h1 data-id="heading-2">🎏 2、什么是同步上下文</h1>
<p>MSDN描述：提供在各种同步模型中传播同步上下文的基本功能，感觉是不是很拗口，反正翻译过来大致如此。
由于多线程编程相当的困难，而且要进行多线程编程需要了解无数概念和工具。为此，Microsoft  提供了 SynchronizationContext 类。</p>
<p>很遗憾，很多开发人员甚至不知道这个有用的工具。</p>
<p>在以.net framework为基础的大部分项目中，都是支持同步上下文概念的。包括ASP.NET、Windows 窗体、Windows Presentation Foundation (WPF)、Silverlight 或其他。</p>
<p>以传统的asp.net 为例，其设计之初每个 ASP.NET 请求都需要一个线程，直到该请求完成。这会造成线程利用率低下，因为创建网页通常依赖于数据库查询和 Web 服务调用，并且处理请求的线程必须等待，直到所有这些操作结束。使用异步页面，处理请求的线程可以开始每个操作，然后返回到 ASP.NET 线程池；当操作结束时，ASP.NET 线程池的另一个线程可以完成该请求。</p>
<p>ASP.NET SynchronizationContext 在线程池线程执行页面代码时安装在上面。当委托列捕获 AspNetSynchronizationContext 中时，它恢复原始页面的标识和区域，然后直接执行委托。即使委托是通过调用 Post“异步”列队的，也会直接调用委托。</p>
<p>从概念上讲，AspNetSynchronizationContext 的上下文非常复杂。在异步页面的生存期中，该上下文从来自 ASP.NET 线程池的一个线程开始。异步请求开始后，该上下文不包含任何线程。异步请求结束时，执行其完成例程的线程池线程进入该上下文。这些可能是启动请求的线程，但更可能是操作完成时处于空闲状态的任何线程。</p>
<ul>
<li>提供一种将工作单元排队到上下文的方法</li>
<li>每个线程都有一个“当前”上下文</li>
<li>保留大量的异步操作</li>
<li>ASP.NET（System.Web）SynchronizationContext最值得注意的事情是，它“排他地”执行，换句话说，每个委托一次执行一个（但不一定按顺序执行）。</li>
<li>如果同一应用程序的多项操作同时完成，AspNetSynchronizationContext 确保一次只执行其中一项。它们可以在任意线程上执行，但该线程将具有原始页面的标识和区域。</li>
</ul>
<p>一个常见的示例是在异步网页中使用 WebClient。DownloadDataAsync 将捕获当前 SynchronizationContext，之后在该上下文中执行其 DownloadDataCompleted 事件。当页面开始执行时，ASP.NET 会分配它的一个线程执行该页面中的代码。该页面可能调用 DownloadDataAsync，然后返回；ASP.NET 对未完成的异步操作进行计数，以便了解页面是否完成。当 WebClient 对象下载所请求的数据后，它将接收到一个线程池线程的通知。此线程将在捕获的上下文中引发 DownloadDataCompleted。该上下文将保持在相同的线程中，但会确保事件处理程序使用正确的标识和区域运行。</p>
<p>说了这么多，你明白了吗？
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff635c4fba6149ca91b251087ec325c1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哦哦哦，让我们弄清楚一些技术要点，SynchronizationContext允许一个线程与另一个线程进行通信。假设您有两个线程，Thread1和Thread2。Thread1正在做一些工作，然后Thread1希望在Thread2上执行代码。一种实现的可能方法是询问Thread2的SynchronizationContext对象，将其提供给Thread1，然后Thread1可以调用SynchronizationContext.Send，在Thread2上执行代码。听起来像魔术...好吧，您应该知道一些事情。并非每个线程都SynchronizationContext附加有它。SynchronizationContextUI线程始终是一个线程。</p>
<h1 data-id="heading-3">🎏 3、为什么砍掉了同步上下文</h1>
<p>退一步，一个好问题是为什么AspNetSynchronizationContext在ASP.NET Core中将其删除。尽管我不了解团队内部关于该主题的讨论，但我认为这是出于两个原因：性能和简单性。首先考虑性能方面。</p>
<p>当异步处理程序在旧版ASP.NET上恢复执行时，继续操作将排队到请求上下文中。后续工作必须等待已排队的任何其他工作（一次只能运行一个）。准备好运行时，将从线程池中获取线程，进入<strong>请求上下文</strong>，然后继续执行处理程序。“重新输入”请求上下文涉及许多内务处理任务，例如设置HttpContext.Current以及当前线程的身份和文化。</p>
<p>使用无上下文ASP.NET Core方法，当异步处理程序恢复执行时，将从线程池中获取线程并执行继续。避免了上下文队列，并且不需要“输入”请求上下文。此外，async/await机制针对无上下文情况进行了高度优化。异步请求要做的工作很少。 哈哈，因此 ASP.NET Core没有HttpContext.Current，这就是其中的原因之一吧。</p>
<p>简单性是该决定的另一个方面。AspNetSynchronizationContext效果很好，但是它包含一些棘手的部分，尤其是在身份管理方面。</p>
<p>好，所以没有SynchronizationContext。这对开发人员意味着什么？</p>
<h1 data-id="heading-4">🎏 4、您可以阻止异步代码</h1>
<p>第一个也是最明显的结果是不会捕获任何上下文await。这意味着阻塞异步代码不会导致死锁。您可以使用Task.GetAwaiter().GetResult()（或Task.Wait或Task.Result）而不必担心死锁。</p>
<p>但是，您不应该这么做，这就是我们常说的 Sync over Async。因为阻塞异步代码的那一刻，您就放弃了异步代码的所有好处。阻塞线程后，异步处理程序增强的可伸缩性将被取消。</p>
<p>在（传统）ASP.NET中有两种情况，不幸的是必须进行阻止：ASP.NET MVC筛选器和子操作。但是，在ASP.NET Core中，整个管道是完全异步的。筛选器和视图组件均异步执行。
因此，你需要注意的是</p>
<ul>
<li>任务继续在线程池中排队，可以并行运行</li>
<li>HttpContext不是线程安全的！</li>
<li>如果使用Task.Wait或Task.Result阻止任务，则不会死锁</li>
</ul>
<p>总之，理想情况下，您应该努力使用async实现所有方式。但是如果您的代码需要，<em>也可以毫无危险地阻塞</em>。
毫无危险是指的没有死锁风险，但由于采用这种方式需要占用2个线程，因此在Windows上，可能性能下降了，但应用程序始终保持响应状态；在Linux上，可能会遇到了线程池耗尽。</p>
<blockquote>
<p>据大牛解释许多Linux I / O实际上是伪异步的。也就是说，底层API是同步的，并且应用程序必须刻录线程以异步处理它们，从而增加了线程池耗尽的可能性。造成这种情况的主要原因是Linux驱动程序堆栈，其中驱动程序必须同时支持同步和异步操作（相反，在Windows上，任何I / O数据传输都必须是异步的；所有同步API都位于设备上方的Win32层中驱动程序）。异步驱动程序是世界上最难编写的东西，因此Linux在该领域落后于Windows。</p>
</blockquote>
<h1 data-id="heading-5">🎏 5. 小结</h1>
<p>嗯，本篇还有下篇，敬请期待。</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            