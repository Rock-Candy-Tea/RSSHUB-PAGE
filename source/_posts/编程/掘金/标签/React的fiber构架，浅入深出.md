
---
title: 'React的fiber构架，浅入深出'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/431cd350b5354e9c979d6e139134b4ac~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 23:12:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/431cd350b5354e9c979d6e139134b4ac~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">1. 出现背景</h2>
<p>js是单线程的，执行js脚本的时候，js引擎和页面渲染引擎在同一个渲染线程，<code>GUI</code> 渲染和<code>js</code>执行 两者是互斥的。正好<code>React</code>渲染虚拟dom是递归的找出需要变动的节点，然后同步更新它们, 一气呵成（这个过程 React称为Reconcilation）。这样当页面复杂（描述的虚拟节点也会复杂）。就会导致js一直占用渲染进程，而导致<code>GUI</code>无法进行，使得页面页面卡顿，或者用户触发的事件得不到响应</p>
<p>因此需要一种手段可以中断Reconcilation,让渲染进程能做一些其他的事情。为此<code>fiber</code>构架应运而生。</p>
<h2 data-id="heading-1">2. 前置知识</h2>
<h3 data-id="heading-2">2.1 <code>requestAnimationFrame</code></h3>
<p>该方法需要传入一个回调函数作为参数，该回调函数会在浏览器下一次重绘之前执行</p>
<h3 data-id="heading-3">2.2 <code>requestIdleCallback</code></h3>
<p>方法将在浏览器的空闲时段内调用的函数排队。这使开发者能够在主事件循环上执行后台和低优先级工作，而不会影响延迟关键事件，如动画和输入响应。函数一般会按先进先调用的顺序执行，然而，如果回调函数指定了执行超时时间timeout，则有可能为了在超时前执行函数而打乱执行顺序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/431cd350b5354e9c979d6e139134b4ac~tplv-k3u1fbpfcp-watermark.image" alt="requestIdleCallback执行示意图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>模拟工作分片，使用requestIdleCallback进行调度</strong></p>
<ol>
<li>首先是将一个大的工作分成几个小块的工作</li>
<li>然后处理工作，进入工作队列循环
<ul>
<li>检查浏览器是否有剩余时间能处理工作分片，</li>
<li>如果没有，有还有任务分片，就使用<code>requestIdleCallback</code>向浏览器申请处理时间，进入事件处理等待队列，</li>
<li>如果有，并且也存在任务分片就从工作队列弹出一个工作分片进行处理</li>
</ul>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这个是为了增加程序运行事件，可以动态的延长工作耗时</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">weak</span>(<span class="hljs-params">duration</span>)</span>&#123;
    <span class="hljs-keyword">let</span> start = <span class="hljs-built_in">Date</span>.now();
    <span class="hljs-keyword">while</span>(start + duration > <span class="hljs-built_in">Date</span>.now())&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'weak'</span>)
    &#125;
&#125;
<span class="hljs-comment">// 工作分片，这个工作本来是一个整体</span>
<span class="hljs-keyword">const</span> works = [
    <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'A1开始'</span>)
        weak(<span class="hljs-number">20</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'A1结束'</span>)
    &#125;,
    <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'B1开始'</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'B1结束'</span>)
    &#125;,
    <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'C1开始'</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'C1结束'</span>)
    &#125;,
]
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span>(<span class="hljs-params">IdleDeadline </span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'本帧的剩余时间'</span>,<span class="hljs-built_in">parseInt</span>( IdleDeadline.timeRemaining() ))
    <span class="hljs-keyword">while</span>(IdleDeadline.timeRemaining()><span class="hljs-number">0</span> && works.length><span class="hljs-number">0</span>)&#123;
        preformUnitOfWork()
    &#125;
    <span class="hljs-keyword">if</span>(works.length><span class="hljs-number">0</span>)&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'只剩下'</span>+IdleDeadline.timeRemaining()+<span class="hljs-string">',时间片即将到期，等待下次申请'</span>)
        requestIdleCallback(workLoop)
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">preformUnitOfWork</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> work = works.shift();
    work();
&#125;
requestIdleCallback (workLoop)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是一个利用<code>requestIdleCallback</code>，对任务分片调度的处理</p>
<h3 data-id="heading-4">2.3 使用<code>MessageChannel</code>模拟<code>requestIdleCallback</code></h3>
<p>因为requestIdleCallback目前还是一个实验阶段的功能，支持性不是很好，所以我们必须要使用另一种方式来实现requestIdleCallback的功能，来获取浏览器每帧空余时间处理事件的能力,react中就是使用的<code>MessageChannel</code>配合<code>requestAnimationFrame</code>模拟的<code>requestIdleCallback</code></p>
<p><strong>MessageChannel基本使用</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> MessageChannel();
<span class="hljs-keyword">const</span> port1 = channel.port1;
<span class="hljs-keyword">const</span> port2 = channel.port2;

port1.addEventListener(<span class="hljs-string">'message'</span>,<span class="hljs-function">(<span class="hljs-params">event</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(event.data)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>重要参考：</strong>  <code>requestAnimationFrame</code>中的回调函数接受一个参数，该参数与<code>performance.now()</code>的返回值相同(表现上近似)，可以这么理解，打开或刷新页面开始执行代码的那一刻为0以这个为参考点，<code>performance.now()</code>就代表执行到这里时，花了多少时间</p>
<p><strong>模拟requestIdleCallback具体代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.myRequestIdleCallback = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback,options</span>)</span>&#123;
    requestAnimationFrame(<span class="hljs-function">(<span class="hljs-params">DOMHighResTimeStamp</span>)=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`DOMHighResTimeStamp:<span class="hljs-subst">$&#123;DOMHighResTimeStamp&#125;</span>-<span class="hljs-subst">$&#123;performance.now()&#125;</span>`</span>)
        myRequestIdleCallback.IdleDeadline = DOMHighResTimeStamp + myRequestIdleCallback.activeAnimationTime
        myRequestIdleCallback.peedingCallback = callback;
        myRequestIdleCallback.channel.port1.postMessage(<span class="hljs-string">'start'</span>);
    &#125;)
&#125;
myRequestIdleCallback.activeAnimationTime = <span class="hljs-number">1000</span>/<span class="hljs-number">60</span>; <span class="hljs-comment">// 每一帧的时间 ms</span>
myRequestIdleCallback.IdleDeadline; <span class="hljs-comment">// 这一帧的截止时间</span>
myRequestIdleCallback.tiemRemaing = <span class="hljs-function">()=></span> myRequestIdleCallback.IdleDeadline - performance.now(); <span class="hljs-comment">// 执行到此语句还有多少空余时间剩余</span>
myRequestIdleCallback.channel = <span class="hljs-keyword">new</span> MessageChannel();
myRequestIdleCallback.channel.port2.onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
    <span class="hljs-comment">// 当收到消息的时候表示，浏览器已经空闲,处理该任务</span>
    <span class="hljs-keyword">const</span> currentTime = performance.now();<span class="hljs-comment">//运行到当前回调函数的时刻</span>
    <span class="hljs-comment">// 如果deadline为true，意味着当前时间已经超出了每一帧的截止时间，也就等同于本帧没有任何时间可以处理回调函数，此帧过期</span>
    <span class="hljs-keyword">const</span> isDeadLine = currentTime > myRequestIdleCallback.IdleDeadline
    <span class="hljs-keyword">if</span>( !isDeadLine || myRequestIdleCallback.tiemRemaing()><span class="hljs-number">0</span>)&#123;
        <span class="hljs-keyword">if</span>(myRequestIdleCallback.peedingCallback)&#123;
            myRequestIdleCallback.peedingCallback(&#123;
                <span class="hljs-attr">timeRemaining</span>:myRequestIdleCallback.tiemRemaing
            &#125;);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码分析：</p>
<ol>
<li>利用requestAnimationFrame的回调函数接受的参数得到执行到该条语句时的时间，然后通过DOMHighResTimeStamp + 每帧消耗的时间长度得到的就是这一帧执行完的时间</li>
<li>使用<code>myRequestIdleCallback</code>的port1去发送消息，当port2接受到消息就认为，此时浏览器在此有空闲时间。</li>
<li>port2接受到消息，被触发紧紧是浏览器到这里有空余时间，不代表有空余时间执行任务，因此，要计算运行到port2 这里的时候当前时间是多少</li>
<li>然后利用运行到port2的时间和这一帧结束的时间做比较，如果当前的时间超过了这一帧结束的时间，代表此帧失效，不能用在处理回调任务</li>
<li>如果没有超过，就用这一帧结束的时间减去执行到此的时间，看看还有多少剩余时间可以执行任务，如果剩余时间大于0，并且有回调任务函数，那就运行回调任务函数吗，并且将<code>timeRemaining:myRequestIdleCallback.tiemRemaing</code>作为其回调任务函数参数的属性</li>
</ol>
<h2 data-id="heading-5">3. fiber构架的实现</h2>
<p>前置知识弄明白了，现在就真正进入主题，认识和实现<code>fiber</code>架构</p>
<p>在react中, 每个渲染都有两个阶段，一个是<code>Reconcilation</code>（协调），一个是<code>Commit</code>（提交）</p>
<ul>
<li>协调阶段：可以简单的任务是diff阶段，这个过程可以被中断（可以被拆成很多小任务块，可以这么认为，一个组件就是一个任务），这个阶段会找出所以的节点变更（例如，节点的新增删除，属性的变更，这些变更在react里面称为副作用）</li>
<li>提交阶段：将上一次计算出的副作用，一次执行，这个阶段必须同步执行，不能被打断</li>
</ul>
<h3 data-id="heading-6">2.1 react子节点存储结构</h3>
<p>react的遍历的节点其实就是一个节点树，这个节点树使用的存储结构其实就是使用的 <strong>兄弟孩子表示法</strong> 的链表式存储，具体如图：
【节点存储示意图】</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3f81f26587b4ce98fe52c50bf52bcd4~tplv-k3u1fbpfcp-watermark.image" alt="fiber节点存储示意图.png" loading="lazy" referrerpolicy="no-referrer">
只是这个子节点每个都加了一个<code>parent</code>域，方便查找其父亲
因为这是一个典型的树形结构，react在遍历整个虚拟dom树的时候，采取的是<code>先根遍历</code>，例如上面的存储示意图上的结构，先根遍历的顺序就是：<code>根->B->C->C1->B1->B2</code>，</p>
<p>(重点复习二叉树，树的遍历如果看的吃力的话)</p>
<h3 data-id="heading-7">2.2 react的fiber</h3>
<ol>
<li>按先<code>先根遍历</code>遍历整个虚拟dom树</li>
<li>在遍历虚拟dom树的时候,会重头开始建立fiber树，这样每个fiber子树就是就是一个工作单元（一开始的根节点就会包装成fiber树的根节点）</li>
<li>然后申请每一帧浏览器的可用时间，执行工作单元，如果可用时间消耗完毕就，当前帧没有可用时间该帧就作废，申请下一帧</li>
<li>执行工作单元，并建立其fiber子树</li>
<li>建立fiber子树的同时，这时候就相当于是<code>后根遍历</code>顺序，建立副作用域链</li>
<li>当没有工作单元可以执行的时候，这时候就遍历副作用域链，做相关的副作用操作(节点的增删改)</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 模拟的测试虚拟节点</span>
<span class="hljs-keyword">const</span> VnodeEelemet = &#123;
    <span class="hljs-attr">type</span>:<span class="hljs-string">'div'</span>,
    <span class="hljs-attr">props</span>:&#123;
        <span class="hljs-attr">id</span>:<span class="hljs-string">'A'</span>,
        <span class="hljs-attr">children</span>:[
            &#123;
                <span class="hljs-attr">type</span>:<span class="hljs-string">'div'</span>,
                <span class="hljs-attr">props</span>:&#123;
                    <span class="hljs-attr">id</span>:<span class="hljs-string">'B'</span>,
                    <span class="hljs-attr">children</span>:[
                        &#123;
                            <span class="hljs-attr">type</span>:<span class="hljs-string">'div'</span>,
                            <span class="hljs-attr">props</span>:&#123;
                                <span class="hljs-attr">id</span>:<span class="hljs-string">'C'</span>,
                                <span class="hljs-attr">children</span>:[]
                            &#125;
                        &#125;,
                        &#123;
                            <span class="hljs-attr">type</span>:<span class="hljs-string">'div'</span>,
                            <span class="hljs-attr">props</span>:&#123;
                                <span class="hljs-attr">id</span>:<span class="hljs-string">'C1'</span>,
                                <span class="hljs-attr">children</span>:[]
                            &#125;
                        &#125;,
                    ]
                &#125;
            &#125;,
            &#123;
                <span class="hljs-attr">type</span>:<span class="hljs-string">'div'</span>,
                <span class="hljs-attr">props</span>:&#123;
                    <span class="hljs-attr">id</span>:<span class="hljs-string">'B1'</span>
                &#125;
            &#125;,
            &#123;
                <span class="hljs-attr">type</span>:<span class="hljs-string">'div'</span>,
                <span class="hljs-attr">props</span>:&#123;
                    <span class="hljs-attr">id</span>:<span class="hljs-string">'B2'</span>
                &#125;
            &#125;
        ]
    &#125;
&#125;

<span class="hljs-keyword">let</span> root = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>);
<span class="hljs-comment">// 最开始的工作单元,也就是一个fiber树</span>
<span class="hljs-keyword">let</span> workUnit = &#123;
    <span class="hljs-attr">stateNode</span>:root, <span class="hljs-comment">// 此fiber对应的静态节点</span>
    <span class="hljs-attr">props</span>:&#123; <span class="hljs-comment">// fiber的属性</span>
        <span class="hljs-attr">children</span>:[VnodeEelemet],
        <span class="hljs-attr">id</span>:<span class="hljs-string">'root'</span>
    &#125;,
    <span class="hljs-attr">sibling</span>:<span class="hljs-literal">null</span>,
    <span class="hljs-attr">child</span>:<span class="hljs-literal">null</span>,
    <span class="hljs-attr">parent</span>:<span class="hljs-literal">null</span>
&#125;

<span class="hljs-comment">// 下一个工作单元</span>
<span class="hljs-keyword">let</span> nextUnitWork = workUnit;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span> (<span class="hljs-params">deadline</span>)</span>&#123;
    <span class="hljs-keyword">while</span>(nextUnitWork &&deadline.timeRemaining()><span class="hljs-number">0</span>)&#123;
        <span class="hljs-comment">// 执行当前工作单元并返回下一个工作单元</span>
        nextUnitWork = preformUnitOfWork(nextUnitWork)
    &#125;
    <span class="hljs-keyword">if</span>(!nextUnitWork)&#123;
        commitRoot()
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> currentFiber = workUnit.firstEffect;
    <span class="hljs-built_in">console</span>.log(workUnit,<span class="hljs-string">'fistEffect'</span>)
    <span class="hljs-keyword">while</span>(currentFiber)&#123;
        <span class="hljs-keyword">if</span>(currentFiber.effectTag === <span class="hljs-string">'PLACEMENT'</span>)&#123;
            currentFiber.parent.stateNode.appendChild(currentFiber.stateNode);
        &#125;
        currentFiber = currentFiber.nextEffect
    &#125;
    workUnit = <span class="hljs-literal">null</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">preformUnitOfWork</span>(<span class="hljs-params">workingFiber</span>)</span>&#123;
    <span class="hljs-comment">// 1. 创建真实dome</span>
    <span class="hljs-comment">// 2. 创建fiber子树</span>
    <span class="hljs-built_in">console</span>.log(workingFiber,<span class="hljs-string">''</span>)
    beginWork(workingFiber);
    <span class="hljs-keyword">if</span>(workingFiber.child)&#123;
        <span class="hljs-keyword">return</span> workingFiber.child
    &#125;
    <span class="hljs-keyword">while</span>(workingFiber)&#123;
        <span class="hljs-comment">// 如果没有儿子，其实当前节点就结束了完成了</span>
        completeUnitWork(workingFiber);
        <span class="hljs-keyword">if</span>(workingFiber.sibling)&#123;
            <span class="hljs-keyword">return</span> workingFiber.sibling
        &#125;
        <span class="hljs-comment">// 指向父亲，方便查询兄弟</span>
        workingFiber = workingFiber.parent
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">beginWork</span>(<span class="hljs-params">workingFiber</span>)</span>&#123;
    <span class="hljs-comment">// console.log( workingFiber)</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'beginWork'</span>, workingFiber,workingFiber.props.id)
    <span class="hljs-comment">// 创建真实节点，但是此时并不挂载</span>
    <span class="hljs-keyword">if</span>(!workingFiber.stateNode)&#123;
        workingFiber.stateNode = <span class="hljs-built_in">document</span>.createElement(workingFiber.type)
        <span class="hljs-built_in">Object</span>.keys( workingFiber.props ).forEach( <span class="hljs-function"><span class="hljs-params">key</span>=></span>&#123;
            <span class="hljs-keyword">if</span>(key !== <span class="hljs-string">'children'</span>)&#123;
                workingFiber.stateNode[key] = workingFiber.props[key]
            &#125;
        &#125;)
    &#125;
    <span class="hljs-comment">//创建子fiber</span>
    <span class="hljs-keyword">let</span> previousFiber;
    <span class="hljs-keyword">if</span>(!workingFiber.props.children)&#123;
        <span class="hljs-keyword">return</span>
    &#125;
    workingFiber.props.children.forEach( <span class="hljs-function">(<span class="hljs-params">child,index</span>)=></span>&#123;
        <span class="hljs-keyword">let</span> childFiber = &#123;
            <span class="hljs-attr">type</span>:child.type,
            <span class="hljs-attr">props</span>:child.props,
            <span class="hljs-attr">parent</span>:workingFiber,
            <span class="hljs-attr">effectTag</span>:<span class="hljs-string">'PLACEMENT'</span>, <span class="hljs-comment">//插入操作</span>
            <span class="hljs-attr">nextEffect</span>:<span class="hljs-literal">null</span><span class="hljs-comment">//下一个有副作用的节点</span>
        &#125;
        <span class="hljs-built_in">console</span>.log(child,<span class="hljs-string">'xxx'</span>)
        <span class="hljs-keyword">if</span>(index === <span class="hljs-number">0</span>)&#123;
            workingFiber.child = childFiber
            previousFiber = childFiber
            <span class="hljs-comment">//console.log(previousFiber,'previousFiber')</span>
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">//console.log(previousFiber,'previousFiberxxx')</span>
            previousFiber.sibling = childFiber
            previousFiber = childFiber
        &#125;
    &#125;)
    <span class="hljs-comment">// console.log(previousFiber,'end')</span>
&#125;

<span class="hljs-comment">// 在建立副作用链上，firstEffect作用就是将链头提升，lastEffect就是用来构建整个链表的（构建方式是后根遍历）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">completeUnitWork</span>(<span class="hljs-params">workingFiber</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'completeUnitWork'</span>, workingFiber.parent,workingFiber.props.id)
    <span class="hljs-comment">// 构建副作用链nextEffect !== null(对dom进行插入，更改属性都属于副作用操作)</span>
    <span class="hljs-keyword">const</span> parentFiber = workingFiber.parent;
    <span class="hljs-keyword">if</span>( parentFiber )&#123;
        <span class="hljs-comment">// 当前fiber有副作用的子链表挂载到父亲身上</span>
        <span class="hljs-keyword">if</span>(!parentFiber.firstEffect)&#123;
            <span class="hljs-comment">// 副作用头节点提升</span>
            <span class="hljs-comment">// console.log(parentFiber,'提升firstEffect')</span>
            parentFiber.firstEffect = workingFiber.firstEffect
        &#125;
        
        <span class="hljs-keyword">if</span>(workingFiber.lastEffect)&#123;
            <span class="hljs-keyword">if</span>(parentFiber.lastEffect)&#123;
                parentFiber.lastEffect.nextEffect = workingFiber.firstEffect
            &#125;
            parentFiber.lastEffect = workingFiber.lastEffect
        &#125;
        <span class="hljs-comment">// 再把自己挂上去(如果自己有副作用的话)</span>
        <span class="hljs-keyword">if</span>(workingFiber.effectTag)&#123;
            <span class="hljs-keyword">if</span>(parentFiber.lastEffect)&#123;
                parentFiber.lastEffect.nextEffect = workingFiber
            &#125;<span class="hljs-keyword">else</span>&#123;
                parentFiber.firstEffect = workingFiber
            &#125;
            parentFiber.lastEffect = workingFiber
        &#125;

    &#125;
    
    
&#125;
myRequestIdleCallback(workLoop)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            