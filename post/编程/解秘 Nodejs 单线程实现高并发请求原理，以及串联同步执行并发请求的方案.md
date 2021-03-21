
---
title: 解秘 Node.js 单线程实现高并发请求原理，以及串联同步执行并发请求的方案
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 01:33:59 GMT
thumbnail: https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e4ad23f96d84d49b86456e78dc1b179~tplv-k3u1fbpfcp-zoom-1.image
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><p>最近在做一个支持多进程请求的 Node 服务，要支持多并发请求，而且请求要按先后顺序串联同步执行返回结果。</p>
<p>对，这需求就是这么奇琶，业务场景也是那么奇琶。</p>
<p>需求是完成了，为了对 Node.js 高并发请求原理有更深一些的理解，特意写一篇文章来巩固一下相关的知识点。</p>
<h2 data-id="heading-0">问题</h2>
<p>Node.js 由这些关键字组成： <strong>事件驱动、非阻塞I/O、高效、轻量</strong>。</p>
<p>于是在我们刚接触 Node.js 时，会有所疑问：</p>
<ul>
<li>
<p>为什么在浏览器中运行的 JavaScript 能与操作系统进行如此底层的交互？</p>
</li>
<li>
<p>Node 真的是单线程吗？</p>
</li>
<li>
<p>如果是单线程，他是如何处理高并发请求的？</p>
</li>
<li>
<p>Node 事件驱动是如何实现的？</p>
</li>
</ul>
<p>下来我们一起来解秘这是怎么一回事！</p>
<h2 data-id="heading-1">架构一览</h2>
<p>上面的问题，都挺底层的，所以我们从 Node.js 本身入手，先来看看 Node.js 的结构。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e4ad23f96d84d49b86456e78dc1b179~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>Node.js 标准库，这部分是由 Javascript编写的，即我们使用过程中直接能调用的 API。在源码中的 lib 目录下可以看到。</p>
</li>
<li>
<p>Node bindings，这一层是 Javascript 与底层 C/C++ 能够沟通的关键，前者通过 bindings 调用后者，相互交换数据。</p>
</li>
<li>
<p>第三层是支撑 Node.js 运行的关键，由 C/C++ 实现。</p>
</li>
</ul>
<ul>
<li>
<p>V8：Google 推出的 Javascript VM，也是 Node.js 为什么使用的是 JavaScript 的关键，它为 JavaScript 提供了在非浏览器端运行的环境，它的高效是 Node.js 之所以高效的原因之一。</p>
</li>
<li>
<p>Libuv：它为 Node.js 提供了跨平台，线程池，事件池，异步 I/O 等能力，是 Node.js 如此强大的关键。</p>
</li>
<li>
<p>C-ares：提供了异步处理 DNS 相关的能力。</p>
</li>
<li>
<p>http_parser、OpenSSL、zlib 等：提供包括 http 解析、SSL、数据压缩等其他的能力。</p>
</li>
</ul>
<h2 data-id="heading-2">单线程、异步</h2>
<ul>
<li>
<p>单线程：所有任务需要排队，前一个任务结束，才会执行后一个任务。如果前一个任务耗时很长，后一个任务就不得不一直等着。Node 单线程指的是 Node 在执行程序代码时，<strong>主线程是单线程</strong>。</p>
</li>
<li>
<p>异步：主线程之外，还维护了一个"事件队列"（Event queue）。当用户的网络请求或者其它的异步操作到来时，Node 都会把它放到 Event Queue 之中，此时并不会立即执行它，代码也不会被阻塞，继续往下走，直到主线程代码执行完毕。</p>
</li>
</ul>
<p>注：</p>
<ul>
<li>JavaScript 是单线程的，Node 本身其实是多线程的，只是 I/O 线程使用的 CPU 比较少；还有个重要的观点是，除了用户的代码无法并行执行外，所有的 I/O (磁盘 I/O 和网络 I/O) 则是可以并行起来的。</li>
<li>libuv 线程池默认打开 4 个，最多打开 128 个 线程。</li>
</ul>
<h2 data-id="heading-3">事件循环</h2>
<p>Nodejs 所谓的单线程，只是主线程是单线程。</p>
<ul>
<li>主线程运行 V8 和 JavaScript</li>
<li>多个子线程通过 <code>事件循环</code> 被调度</li>
</ul>
<p>可以抽象为：主线程对应于老板，正在工作。一旦发现有任务可以分配给职员（子线程）来做，将会把任务分配给底下的职员来做。同时，老板继续做自己的工作，等到职员（子线程）把任务做完，就会通过事件把结果回调给老板。老板又不停重复处理职员（子线程）子任务的完成情况。</p>
<p>老板（主线程）给职员（子线程）分配任务，当职员（子线程）把任务做完之后，通过事件把结果回调给老板。老板（主线程）处理回调结果，执行相应的 JavaScript。</p>
<p>更具体的解释请看下图：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa9d18bbf1f94e9c9432971cee1453c1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>1、每个 Node.js 进程只有一个主线程在执行程序代码，形成一个执行栈（execution context stack)。</p>
<p>2、Node.js 在主线程里维护了一个"事件队列"（Event queue），当用户的网络请求或者其它的异步操作到来时，Node 都会把它放到 Event Queue之中，此时并不会立即执行它，代码也不会被阻塞，继续往下走，直到主线程代码执行完毕。</p>
<p>3、主线程代码执行完毕完成后，然后通过 Event Loop，也就是事件循环机制，检查队列中是否有要处理的事件，这时要分两种情况：如果是非 I/O 任务，就亲自处理，并通过回调函数返回到上层调用；如果是 I/O 任务，就从 <code>线程池</code> 中拿出一个线程来处理这个事件，并指定回调函数，当线程中的 I/O 任务完成以后，就执行指定的回调函数，并把这个完成的事件放到事件队列的尾部，线程归还给线程池，等待事件循环。当主线程再次循环到该事件时，就直接处理并返回给上层调用。 这个过程就叫 <code>事件循环 (Event Loop)</code>。</p>
<p>4、期间，主线程不断的检查事件队列中是否有未执行的事件，直到事件队列中所有事件都执行完了，此后每当有新的事件加入到事件队列中，都会通知主线程按顺序取出交 Event Loop 处理。</p>
<h2 data-id="heading-4">优缺点</h2>
<p>Nodejs 的优点：I/O 密集型处理是 Nodejs 的强项，因为 Nodejs 的 I/O 请求都是异步的（如：sql 查询请求、文件流操作操作请求、http 请求...）</p>
<p>Nodejs 的缺点：不擅长 cpu 密集型的操作（复杂的运算、图片的操作）</p>
<h2 data-id="heading-5">总结</h2>
<p>1、Nodejs 与操作系统交互，我们在 JavaScript 中调用的方法，最终都会通过 process.binding 传递到 C/C++ 层面，最终由他们来执行真正的操作。Node.js 即这样与操作系统进行互动。</p>
<p>2、Nodejs 所谓的单线程，只是主线程是单线程，所有的网络请求或者异步任务都交给了内部的线程池去实现，本身只负责不断的往返调度，由事件循环不断驱动事件执行。</p>
<p>3、Nodejs 之所以单线程可以处理高并发的原因，得益于 libuv 层的事件循环机制，和底层线程池实现。</p>
<p>4、Event loop 就是主线程从主线程的事件队列里面不停循环的读取事件，驱动了所有的异步回调函数的执行，Event loop 总共 7 个阶段，每个阶段都有一个任务队列，当所有阶段被顺序执行一次后，event loop 完成了一个 tick。</p>
<p>参考文章：<a href="https://blog.csdn.net/j2iayu7y/article/details/81623516" target="_blank" rel="nofollow noopener noreferrer">Nodejs探秘：深入理解单线程实现高并发原理</a></p>
<h2 data-id="heading-6">串联同步执行并发请求</h2>
<p>就像上面说的：Node.js 在主线程里维护了一个"事件队列"（Event queue），当用户的网络请求或者其它的异步操作到来时，Node 都会把它放到 Event Queue之中，此时并不会立即执行它，代码也不会被阻塞，继续往下走，直到主线程代码执行完毕。</p>
<p>所以要串联同步执行并发请求的关键在于维护一个队列，队列的特点是 <code>先进先出</code>，按队列里面的顺序执行就可以达到串联同步执行并发请求的目的。</p>
<p><strong>方案</strong></p>
<ul>
<li>根据每个请求的 uniqueId 变量作为唯一令牌</li>
<li>队列里面维护一个结果数组和一个执行队列，把执行队列完成的 <code>令牌与结果</code> 存储在结果数组里面</li>
<li>根据唯一令牌，一直去获取执行完成的结果，间隔 200 毫秒，超时等待时间为 10 分钟</li>
<li>一直等待并获取结果，等待到有结果时，才返回给请求；并根据令牌把结果数组里面相应的项删除</li>
</ul>
<h3 data-id="heading-7">队列</h3>
<p>代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Recorder</span> </span>{
    private list: any[];

    private queueList: any[];

    private intervalTimer;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> {
        <span class="hljs-built_in">this</span>.list = [];
        <span class="hljs-built_in">this</span>.queueList = [];
        <span class="hljs-built_in">this</span>.intervalTimer = <span class="hljs-literal">null</span>;
    }

    <span class="hljs-comment">// 根据 id 获取任务结果</span>
    public <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">id: string</span>)</span> {
        <span class="hljs-keyword">let</span> data;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'this.list: '</span>, <span class="hljs-built_in">this</span>.list);
        <span class="hljs-keyword">let</span> index;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.list.length; i++) {
            <span class="hljs-keyword">const</span> item = <span class="hljs-built_in">this</span>.list[i];
            <span class="hljs-keyword">if</span> (id === item.id) {
                data = item.data;
                index = i;
                <span class="hljs-keyword">break</span>;
            }
        }
        <span class="hljs-comment">// 删除获取到结果的项</span>
        <span class="hljs-keyword">if</span> (index !== <span class="hljs-literal">undefined</span>) {
            <span class="hljs-built_in">this</span>.list.splice(index, <span class="hljs-number">1</span>);
        }
        <span class="hljs-keyword">return</span> data;
    }

    public <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span> {
        <span class="hljs-built_in">this</span>.list = [];
        <span class="hljs-built_in">this</span>.queueList = [];
    }

    <span class="hljs-comment">// 添加项</span>
    public <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">addQueue</span>(<span class="hljs-params">item: any</span>)</span> {
        <span class="hljs-built_in">this</span>.queueList.push(item);
    }

    public <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">runQueue</span>(<span class="hljs-params"></span>)</span> {
        <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.intervalTimer);
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.queueList.length) {
            <span class="hljs-comment">// console.log('队列执行完毕');</span>
            <span class="hljs-keyword">return</span>;
        }
        <span class="hljs-comment">// 取出队列里面的最后一项</span>
        <span class="hljs-keyword">const</span> item = <span class="hljs-built_in">this</span>.queueList.shift();
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'item: '</span>, item);
        <span class="hljs-comment">// 执行队列的回调</span>
        <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> item.callback();
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'回调执行完成: '</span>, data);
        <span class="hljs-comment">// 把结果放进 结果数组</span>
        <span class="hljs-built_in">this</span>.list.push({ <span class="hljs-attr">id</span>: item.id, data });
    }

    public <span class="hljs-function"><span class="hljs-title">interval</span>(<span class="hljs-params"></span>)</span> {
        <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.intervalTimer);
        <span class="hljs-built_in">this</span>.intervalTimer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-keyword">async</span> () => {
            <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.intervalTimer);
            <span class="hljs-comment">// 一直执行里面的任务</span>
            <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.runQueue();
            <span class="hljs-built_in">this</span>.interval();
        }, <span class="hljs-number">200</span>);
    }
}

<span class="hljs-keyword">const</span> recorder = <span class="hljs-keyword">new</span> Recorder();
recorder.interval();

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> recorder;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">服务</h3>
<p>下面模拟一个请求端口的的 Node 服务。</p>
<p>代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Koa = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa'</span>)
<span class="hljs-keyword">const</span> Router = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-router'</span>)
<span class="hljs-keyword">const</span> cuid = <span class="hljs-built_in">require</span>(<span class="hljs-string">'cuid'</span>);
<span class="hljs-keyword">const</span> bodyParser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-bodyparser'</span>)
<span class="hljs-keyword">import</span> recorder <span class="hljs-keyword">from</span> <span class="hljs-string">"./libs/recorder"</span>;

<span class="hljs-keyword">const</span> MAX_WAITING_TIME = <span class="hljs-number">60</span> * <span class="hljs-number">5</span>; <span class="hljs-comment">// 最大等待时长</span>
<span class="hljs-comment">// web服务端口</span>
<span class="hljs-keyword">const</span> SERVER_PORT: number = <span class="hljs-number">3000</span>;
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Koa();
app.use(bodyParser());
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> Router();


<span class="hljs-comment">/**
 * 程序睡眠
 * <span class="hljs-doctag">@param </span>time 毫秒
 */</span>
<span class="hljs-keyword">const</span> timeSleep = <span class="hljs-function">(<span class="hljs-params">time: number</span>) =></span> {
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> {
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> {
            resolve(<span class="hljs-string">""</span>);
        }, time);
    });
};

<span class="hljs-comment">/**
 * 程序睡眠
 * <span class="hljs-doctag">@param </span>second 秒
 */</span>
<span class="hljs-keyword">const</span> sleep = <span class="hljs-function">(<span class="hljs-params">second: number</span>) =></span> {
    <span class="hljs-keyword">return</span> timeSleep(second * <span class="hljs-number">1000</span>);
};

router.post(<span class="hljs-string">"/getPort"</span>, <span class="hljs-keyword">async</span> (ctx, next) => {
<span class="hljs-keyword">const</span> { num } = ctx.request.body;
<span class="hljs-keyword">const</span> uniqueId = cuid();
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'uniqueId: '</span>, uniqueId);
    recorder.addQueue({
<span class="hljs-attr">id</span>: uniqueId,
<span class="hljs-attr">callback</span>: getPortFun(num)
});
    <span class="hljs-keyword">let</span> waitTime = <span class="hljs-number">0</span>;
<span class="hljs-keyword">while</span> (!ctx.body) {
<span class="hljs-keyword">await</span> sleep(<span class="hljs-number">0.2</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'1'</span>);
<span class="hljs-keyword">const</span> data: any = recorder.get(uniqueId);
<span class="hljs-keyword">if</span> (data) {
ctx.body = {
<span class="hljs-attr">code</span>: <span class="hljs-number">0</span>,
<span class="hljs-attr">data</span>: data,
<span class="hljs-attr">msg</span>: <span class="hljs-string">'success'</span>
};
}
waitTime++;
        <span class="hljs-comment">// 超过最大时间就返回一个结果</span>
<span class="hljs-keyword">if</span> (waitTime > MAX_WAITING_TIME) {
ctx.body = {};
}
}
});

<span class="hljs-comment">// 返回一个函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getPortFun</span>(<span class="hljs-params">num</span>) </span>{
<span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> {
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> {
            <span class="hljs-comment">// 模拟异步程序</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> {
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`num<span class="hljs-subst">${num}</span>: `</span>, num);
resolve(num * num);
}, num * <span class="hljs-number">1000</span>);
});
};
}

app.use(router.routes()).use(router.allowedMethods());

app.listen(SERVER_PORT);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">最后</h2>
<p>最近状态很差劲，所以最近的原创技术文章有点难产了 😥</p>
<p>心态急需调整，周末想出去玩，放松一下自己，找回那个斗志满满的真我才行，唉。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfc8bfdad90c4d83923745f7180786fa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>往期精文</strong></p>
<ul>
<li><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/18" target="_blank" rel="nofollow noopener noreferrer">Vue3 的学习教程汇总、源码解释项目、支持的 UI 组件库、优质实战项目</a></li>
</ul>
<ul>
<li>
<p><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/6" target="_blank" rel="nofollow noopener noreferrer">10 个 GitHub 上超火的前端面试项目，打造自己的加薪宝库！</a></p>
</li>
<li>
<p><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/7" target="_blank" rel="nofollow noopener noreferrer">10 个 GitHub 上超火的 CSS 技巧项目，找到写 CSS 的灵感！</a></p>
</li>
<li>
<p><a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/9" target="_blank" rel="nofollow noopener noreferrer">11 个超火的前端必备在线工具，终于有时间上班摸鱼了</a></p>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            