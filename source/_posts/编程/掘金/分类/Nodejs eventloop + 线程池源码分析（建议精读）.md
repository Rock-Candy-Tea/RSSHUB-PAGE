
---
title: 'Node.js eventloop + 线程池源码分析（建议精读）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aca7402c97b4e848b66135b48758bfa~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 00:47:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aca7402c97b4e848b66135b48758bfa~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文由团队成员<a href="https://juejin.cn/user/747323638163768" target="_blank">宗纬</a> 撰写，已授权涂鸦大前端独家使用，包括但不限于编辑、标注原创等权益。</p>
</blockquote>
<h3 data-id="heading-0">线程池</h3>
<h5 data-id="heading-1">线程池是个啥</h5>
<p>先开启第一个问题，何为线程池。 <strong>一项技术的诞生往往是为了解决某个问题</strong>，那线程池也不例外。</p>
<p>我们先来假设一个场景。</p>
<p>假如你在某纪佳缘网上班，你的老板让你开发一个推荐服务，做的事情很简单，当有用户访问你的服务的时候，你需要根据用户的一些特性（比如性别）给他推荐对象。比如怪怪在访问的时候，你就需要推荐 <strong>富婆</strong>。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aca7402c97b4e848b66135b48758bfa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当你接到这个任务，首先要想到的就是每个用户过来的请求应该是个 <strong>独立的线程</strong>。因为 <strong>用户和用户之间是隔离的</strong>，而每个线程做的事情就是一系列推荐操作。</p>
<p>当然，这难不倒优秀的你，你可以在每个用户请求的时候新建一个线程，在请求响应结束后销毁它，一切都很美好。</p>
<p>燃鹅，因为你推荐的太到位了，你们 <strong>网站火了</strong>，一群富婆争着来注册。这个时候问题也就来了，如果 1000 个富婆同时点击，那意味着 1000 个请求会过来，你是不是就要建立 1000 个线程呢？</p>
<p>在这一系列请求结束后，这些线程是不是又会被销毁？线程创建最直观的开销就是 <strong>内存</strong>，这样的频繁创建和销毁对性能的影响显而易见，同时这样的设计并不能撑其瞬时 <strong>峰值流量</strong>。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9b769d102cf425eb07d142c2275110c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>因为这样的设计，富婆们得不到满足，某纪佳缘岌岌可危。</p>
<p>这时，线程池应运而生。之前讲过，一项技术的诞生永远是为了解决某些问题，那线程池解决了什么问题呢？总结下其实就是线程的生命周期管控。下面我们来细细分析。</p>
<h5 data-id="heading-2">线程生命周期管控</h5>
<p>先看我们的问题，频繁的创建和销毁线程。解决的办法是啥呢？必然是 <strong>线程复用</strong>。</p>
<p>一个线程被创建之后，即使这一次响应结束了，也不让他被回收，下一次请求来的时候依然让他去处理。</p>
<p>这里很关键的点在于如何让一个 <strong>线程不被回收</strong>。</p>
<p>看似很神奇，一个线程执行完了操作还能继续存在？这么持久？做法其实很简单，写一个 <strong>死循环</strong> 即可。线程一直处于循环中，当有请求来的时候处理请求，当没有的时候就一直等待，等到了再执行处理，处理完再等待，反复横跳，无限循环。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a8c5a9370be41e39934e45b292ee0e9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里引申出了第二个关键点，处于 <strong>死循环中的线程怎么知道啥时候有请求要给他处理</strong>？</p>
<p>这里不同语言实现方式不完全相同，但大同小异，本质上一定是基于阻塞唤醒。当没有任务的时候，所有线程处于阻塞状态，当任务来的时候，空闲线程去竞争这个任务，取到的线程开始执行，未取到的继续阻塞。</p>
<p>这里大家可能网上看过行行色色的线程池解读，但要深刻理解的话，还是要 <strong>从源码入手</strong>。（在源码面前，一切的花里胡哨都苍白无力）</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53654a9d8564499abe907a8513b773de~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>先给出 <strong>libuv threadPool 源码</strong> 地址： <a href="https://github.com/libuv/libuv/blob/4ed2a78f0eb1c9d2a0c98ea4a88c6824e5958dc6/src/threadpool.c" target="_blank" rel="nofollow noopener noreferrer">源码地址</a></p>
<p>我们直接截取线程池实现的核心部分，如下图里的注释，基本实现符合预期。</p>
<p><img alt="线程池源码1" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2214c88e0a34bb7b80271d558f0b5d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">线程池源码1<img alt="线程池源码2" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ad2b1c57a5a4079863922499924790b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">线程池源码2</p>
<p>简单说明下，上面代码里 uv_cond_signal 等同于唤醒阻塞线程，uv_cond_wait 等同于让当前线程进入阻塞状态。</p>
<h5 data-id="heading-3">线程池总结</h5>
<p>最后总结下就是，线程池利用死循环让线程无法结束，在等待任务期间处于阻塞状态，利用阻塞唤醒来让线程接收任务（本质上阻塞唤醒基于信号量），从而达到线程复用，结束当前任务后进入下一次循环，周而复始。</p>
<h3 data-id="heading-4">eventloop</h3>
<h4 data-id="heading-5">eventloop 是个啥</h4>
<p>eventloop 的含义如同其名字一样：事件循环。</p>
<p>说的通俗一点其实就是一个 while(true)循环，循环里面做的事情就是不断的 check 有没有待处理的任务，如果有就处理任务，如果没有就继续下一次循环。</p>
<p>大致流程如下图。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c9d09ba4b04109b58e97f164289301~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>eventloop 的思想很简单，他并不关心你的回调如何实现，IO 操作何时结束。</p>
<p>他做的事情就是不断的去取事件，取到了就执行。那这里有一个关键的点就是他在哪里取的 event 呢？</p>
<p>答案是： <strong>watcher</strong>。每个事件循环中都会有观察者，每轮循环都会去观察者中拿事件，然后执行。其实这个所谓的 watcher 就是一个用来存放事件的 <strong>queue</strong>（队列）。</p>
<p>怎么来理解这个 watcher 呢，深入浅出 nodejs 里面给了一个很形象的比喻。</p>
<hr>
<p>在餐厅里，前台小妹往往负责记录客人的点菜，厨师在后厨做菜。小妹在拿到客人的菜单后会把菜单放到厨房，而厨师只需要不断的看菜单，做菜，再看菜单，做菜。他并不关心是谁点的菜，也不关心这个菜在什么时候点的。</p>
<p>这里这个放菜单的地方就是那个 watcher，本质上是一个 queue，厨师就如同 eventloop，不断的处于做菜的循环中，每一轮循环会去取 queue 里面的请求，如果有回调就执行回调，没有的话进入下一轮循环。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ab07574dddb4ac69e1933c879b049ce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">eventloop + 线程池 = 异步非阻塞</h3>
<p>上面比较详细的讲解了线程池和 eventpoll，接下来我们来看一下如何用其来实现异步非阻塞。</p>
<p>我们来一步一步捋清思路。首先，可爱的你发起了一个 IO 调用，从 <a href="https://juejin.im/post/6844904116586545159" target="_blank" rel="nofollow noopener noreferrer">《大前端进阶 Node.js》系列 异步非阻塞</a> 中讲过，一个 IO 调用要么是阻塞调用，要么是先非阻塞的发起 IO，再在需要看结果的时候阻塞的去获取，显然这两种模式都不是我们想要的。</p>
<p>我们要的是异步非阻塞，所以这个 IO 调用一定不是在主线程中执行，这个时候我们就能联想到上面的线程池。</p>
<p>主线程不能被阻塞，但线程池里面的线程可以，主线程只需要把 IO 调用交给线程池来执行，自己就可以愉快的玩耍，以此达到了我们的第一个目标： <strong>非阻塞</strong>。</p>
<p>那 <strong>异步</strong> 呢？如何让线程池里面的调用在结束的时候去执行回调？这个时候 eventloop 闪亮登场。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c287b644c0524beeb4db18d9b305891d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在线程池 IO 处理结束后，会主动的把结束的请求放入 eventloop 的观察者（watcher）中，也就是我们的 queue 中，eventloop 处于不断循环的状态，当下一次循环 check 到 queue 里有请求的时候，就会取出来然后执行回调，这样我们想要的 <strong>异步</strong> 就达到了。</p>
<p>最终通过线程池和 eventloop 结合，呈现出的效果就是，当你发起一次 IO 调用，你无需阻塞的等待 IO 结束，也无需在想利用 IO 结果的时候不断的轮询，整个 IO 过程 <strong>对主线程而言非阻塞</strong>，并且自动结束时执行回调，达到我们想要的异步非阻塞。</p>
<p>最后，我们引用一张《深入浅出 Nodejs》里的图。</p>
<p><img alt="异步非阻塞" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58e81e6322d84a6a9f0d63b10c5a385c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">异步非阻塞</p>
<p>如上图，在发起异步调用后，会封装一个请求参数，里面会包括参数和结束时要执行的回调。</p>
<p>这个 <strong>request(请求参数)</strong> 封装好后会扔给线程池执行，线程池里面的线程如果有空闲，就会在线程池的 queue 中去取这个 request 并执行 IO 操作。</p>
<p>在执行结束之后通知 <strong>IOCP</strong>，其实就是把这个 requeat 放入一个 queue，这个队列就是线程池和事件循环之间的枢纽。</p>
<p>事件循环在循环的时候发现队列里面有请求，就会取出来并执行相应的回调，一次完美的异步非阻塞就此完成。</p>
<h3 data-id="heading-7">总结</h3>
<blockquote>
<p>本文已收录 <a href="https://github.com/ponkans/F2E" target="_blank" rel="nofollow noopener noreferrer">Github https://github.com/ponkans/F2E</a>，里面有一线大厂进阶指南，欢迎 Star，持续更新</p>
</blockquote>
<p>仔细的看完怪怪的 Node 异步非阻塞（上）（下）两个系列，还不能吊打面试题你尽管来找我~</p>
<p><strong>libuv threadPool 源码</strong> 都带你看过了，还不明白，就真的说不过去了！！</p>
<p>最后，精辟的完美总结如下。</p>
<hr>
<p><strong>核心总结</strong>：Node 利用线程池来执行 IO 调用，避免阻塞主线程，执行结束后把结果和请求放入一个队列，利用事件循环来取出队列的请求，最后执行回调，达到了异步非阻塞的效果。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f83c65e7d3444d38aacd2576b9083052~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>作者更多原创热文传送门，biubiu~：</p>
<ul>
<li><a href="https://juejin.im/post/6844904103114440718" target="_blank" rel="nofollow noopener noreferrer">《吐血整理》系列 大厂前端组件库工具集合（PC 端、移动端、JS、CSS 等）</a></li>
<li><a href="https://juejin.im/post/6844904099972907021" target="_blank" rel="nofollow noopener noreferrer">《大前端进阶 Node.js》系列 多进程模型底层实现（字节跳动被问）</a></li>
<li><a href="https://juejin.im/post/6844904095514378254" target="_blank" rel="nofollow noopener noreferrer">《大前端进阶 Node.js》系列 双十一秒杀系统</a></li>
<li><a href="https://juejin.im/post/6844904116586545159" target="_blank" rel="nofollow noopener noreferrer">《大前端进阶 Node.js》系列 异步非阻塞（上）</a></li>
</ul>
<p>喜欢的小伙伴加个关注，点个赞哦，感恩💕😊</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            