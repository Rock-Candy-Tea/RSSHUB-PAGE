
---
title: '手摸手教你实现react Scheduler（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2220a74ab2414ccd8c99f830d22b7082~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 00:59:58 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2220a74ab2414ccd8c99f830d22b7082~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:30px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:60px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:24px 0 12px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#a862ea&#125;.markdown-body ol li.task-list-item,.markdown-body ul li.task-list-item&#123;list-style:none&#125;.markdown-body ol li.task-list-item ol,.markdown-body ol li.task-list-item ul,.markdown-body ul li.task-list-item ol,.markdown-body ul li.task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body a,.markdown-body code,.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6,.markdown-body li,.markdown-body p&#123;opacity:.85;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body a:hover,.markdown-body code:hover,.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover,.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:1px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;transition:transform .2s ease 0s;background-color:#f8f5ff;box-shadow:0 0 10px #e7daff&#125;.markdown-body img:hover&#123;opacity:1;box-shadow:0 0 20px #e7daff;transform:translateY(-1px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:12px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:3px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body .math&#123;font-style:italic;margin:12px 0;padding:.5em 1em;background-color:#f8f5ff&#125;.markdown-body .math>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:18px;color:#383838;border-radius:2px;scroll-behavior:smooth;box-shadow:0 0 10px #e7daff&#125;.markdown-body pre>code:hover&#123;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;width:100%;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:.5em;border:1px solid #e7daff&#125;.markdown-body tr&#123;background-color:#f8f5ff&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>最近在看react源码，react构建fiber树这一块逻辑还比较好理解，但是一旦涉及到任务调度相关的逻辑，看起来是一头雾水。在参考了一些资料和react scheduler源码后，我决定来实现一个简单版的scheduler，相信跟着本文的思路实现一遍，就可以理解为什么react需要有scheduler这个东西来调度任务。</p>
<p>简单的背景知识：</p>
<p>我们知道现在大部分设备的帧率都是60fps,也就是说浏览器每16.7ms会绘制一次。如果页面上有一些动画，那么16.7s绘制一次，看起来是比较流畅的。</p>
<p>先来写一个简单的css动画：一个普通的div左右滑动</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-id">#block</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#ddd</span>;
            <span class="hljs-attribute">animation</span>: move <span class="hljs-number">5s</span> linear infinite;
            <span class="hljs-attribute">position</span>: absolute;
        &#125;
        <span class="hljs-keyword">@keyframes</span> move &#123;
            <span class="hljs-number">0%</span> &#123;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            &#125;
            <span class="hljs-number">25%</span> &#123;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">100px</span>;
            &#125;
            <span class="hljs-number">50%</span> &#123;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">200px</span>;
            &#125;
            <span class="hljs-number">75%</span> &#123;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">100px</span>;
            &#125;
            <span class="hljs-number">100%</span> &#123;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"block"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用谷歌浏览器的性能录制面板可以看到：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2220a74ab2414ccd8c99f830d22b7082~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1663129187558.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在主线程上，一帧的时间是16.7ms，我们放大看看一帧时间里面，浏览器做了什么：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13bf1d51f5994d27bc5255119490022d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1663136182178.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成一次绘制需要执行Schedule Style Recalculation, Recalculate Style, Layout, Pre-Paint, Paint, Composite Layers。这里我们不细究在每个阶段浏览器做了什么，只需要关注这个渲染是在主线程上进行，由CPU完成的就行了。通常每16.7ms浏览器会绘制一次，但是如果本轮事件循环有任务在执行，那么需要等任务执行完再进行绘制。如果任务耗时过长，绘制次数就会变少，也就是所谓“掉帧”。因为我们现在页面非常简单，没有js任务，所以浏览器每16.7ms绘制一次，动画看起来很流畅。</p>
<p>现在我们来加上一个按钮，点击之后会创建5个任务，每个任务耗时20ms，并且马上执行。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绑定事件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> works = [];
<span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'btn'</span>);
btn.<span class="hljs-property">onclick</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
        works.<span class="hljs-title function_">push</span>(macroTask)
    &#125;
    <span class="hljs-title function_">flushWork</span>();
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">macroTask</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
    <span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>() - start < <span class="hljs-number">20</span>) &#123;&#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">while</span>(works.<span class="hljs-property">length</span>)&#123;
        <span class="hljs-keyword">const</span> work = works.<span class="hljs-title function_">shift</span>();
        work.<span class="hljs-title function_">call</span>(<span class="hljs-literal">null</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击按钮会发现，正在滑动的div卡顿了一下，通过下图可以看到，浏览器直到5个宏任务完成后才会执行渲染，在这段时间里面，页面不能更新，也不能响应用户操作。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8a40e9aeae14b9cb52077f28a90757b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1663137618473.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果点击按钮要执行成千上百个任务，那么浏览器会卡死很长一段时间，这显然是不能接受的。最简单的改造方法是执行一个任务后，把后续的任务处理放到下一个事件循环，让浏览器可以在本轮事件循环执行绘制。精通浏览器原理的你肯定知道可以利用setTimeout来实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> works = [];
<span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'btn'</span>);
btn.<span class="hljs-property">onclick</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">50</span>; i++) &#123;
        works.<span class="hljs-title function_">push</span>(macroTask)
    &#125;
    <span class="hljs-title function_">flushWork</span>();
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">macroTask</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> start = <span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>();
    <span class="hljs-keyword">while</span> (<span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>() - start < <span class="hljs-number">20</span>) &#123;&#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-title function_">workLoop</span>();
&#125;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> work = works.<span class="hljs-title function_">shift</span>();
    <span class="hljs-keyword">if</span>(work)&#123;
        work.<span class="hljs-title function_">call</span>(<span class="hljs-literal">null</span>);
        <span class="hljs-comment">// 只执行一个任务，后面的下个事件循环再处理</span>
        <span class="hljs-built_in">setTimeout</span>(workLoop, <span class="hljs-number">0</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开控制台分析一下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a25cab7d1c4f419988b61bc6b1d5cd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1663139245105.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在可以看到，现在每个宏任务都没有连在一起，它们在不同的事件循环里执行。每个任务完成后，浏览器都会执行一次绘制，就算要执行的任务非常多，动画也不会卡住不动了。</p>
<p>但是，仔细观察一下，后面的宏任务间隔好像都比较大，放大看间隔大概是4ms左右。我们现在一个任务的执行时间是20ms，超过了16.7ms，事实上页面已经有一点卡顿了。主线程资源这么紧张，每个事件循环居然还要浪费4ms，这肯定是不能接受的。很多人应该都听说过setTimeout的最小延时限制，大概意思就是虽然你是setTimeout零秒，实际上嵌套多层之后，至少要过4ms左右，宏任务才会进入到任务队列。</p>
<p>setTimeout不能用了，有其他替代方案吗？答案是有的，我们可以使用MessageChannel来把任务放到宏任务队列。
MessageChannel的用法就不详细介绍了，简单地说，就是利用这个api，我们可以监听一个message事件，当事件触发的时候，事件处理函数这个任务会加入到宏任务队列。对应我们的例子，我们就可以绑定onmessage的时候执行workLoop, 在workLoop里面只执行一个任务，如果还有任务没有执行，那就postMessage，在下一个事件循环继续处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MessageChannel</span>();
<span class="hljs-keyword">const</span> port2 = channel.<span class="hljs-property">port2</span>;
<span class="hljs-keyword">const</span> port1 = channel.<span class="hljs-property">port1</span>;
port1.<span class="hljs-property">onmessage</span> = workLoop;

<span class="hljs-keyword">const</span> works = [];
<span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'btn'</span>);
btn.<span class="hljs-property">onclick</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">50</span>; i++) &#123;
        works.<span class="hljs-title function_">push</span>(macroTask)
    &#125;
    <span class="hljs-title function_">flushWork</span>();
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">macroTask</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> start = <span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>();
    <span class="hljs-keyword">while</span> (<span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>() - start < <span class="hljs-number">20</span>) &#123;&#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-title function_">workLoop</span>();
&#125;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> work = works.<span class="hljs-title function_">shift</span>();
    <span class="hljs-keyword">if</span>(work)&#123;
        work.<span class="hljs-title function_">call</span>(<span class="hljs-literal">null</span>);
        port2.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新执行后再分析一下，宏任务之间基本没有间隔了：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71bcc676c66140f0b2bf52f1a1eaebbc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1663141415359.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前我们的最小任务单元的执行时间是20ms。因为超过了16.7ms会导致页面变卡顿，所以实际上我们应该确保单个任务不能超过16.7ms。假设经过合理的设计，我们的最小任务单元执行时间不会超过2ms（这里随机设置成1ms或2ms）。然后再来看看点击按钮后执行1000个任务会怎么样。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MessageChannel</span>();
<span class="hljs-keyword">const</span> port2 = channel.<span class="hljs-property">port2</span>;
<span class="hljs-keyword">const</span> port1 = channel.<span class="hljs-property">port1</span>;
port1.<span class="hljs-property">onmessage</span> = workLoop;

<span class="hljs-keyword">const</span> works = [];
<span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'btn'</span>);
btn.<span class="hljs-property">onclick</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1000</span>; i++) &#123;
        works.<span class="hljs-title function_">push</span>(macroTask)
    &#125;
    <span class="hljs-title function_">flushWork</span>();
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">macroTask</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> time = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]; 
    <span class="hljs-keyword">const</span> zeroOrOne = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">round</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>());
    <span class="hljs-keyword">const</span> start = <span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>();
    <span class="hljs-keyword">while</span> (<span class="hljs-title class_">Date</span>.<span class="hljs-title function_">now</span>() - start < time[zeroOrOne]) &#123;&#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-title function_">workLoop</span>();
&#125;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> work = works.<span class="hljs-title function_">shift</span>();
    <span class="hljs-keyword">if</span>(work)&#123;
        work.<span class="hljs-title function_">call</span>(<span class="hljs-literal">null</span>);
        port2.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b55b8ead5677405ba5e115200108ae2f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1663144692017.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分析运行结果，可以看到现在浏览器绘制的帧率还是没有60fps，我们的任务占据主线程时间太长了。所以我们需要一种机制，使得在一帧的时间内尽可能执行多个任务，而且留有充足的时间给浏览器绘制页面和响应用户交互。</p>
<p>最终我们的设计方案是：在一个事件循环里面，我们只占用主线程5ms, 超过5ms就把主线程控制权交还给浏览器，在下一个事件循环处理任务。</p>
<p>具体思路：</p>
<p>声明一个全局队列taskQueue存放任务；</p>
<p>声明一个全局变量startTime表示任务调度的开始时间, 当接受到onmessage事件时，获取当前时间赋值给startTime，然后开始调度任务；</p>
<p>调度任务：从taskQueue队列中取出一个任务，获取当前时间currentTime, 计算currentTime - startTime，如果大于或等于5ms，说明调度任务时长已经达到5ms了，break出循环，如果队列里还有任务，postMessage交出主线程控制权，等下个事件循环再调度任务。</p>
<p>浏览器绘制完页面，响应用户交互后，在下一个事件循环再次调度任务，重新计算currentTime，startTime,此时它们的差值一定不会超过5ms, 取出一个任务执行，然后更新currentTime。再次进入while循环，判断currentTime - startTime是否大于5ms, 大于5ms就交出控制权，否则继续执行下一个任务。</p>
<p>改造后的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MessageChannel</span>();
<span class="hljs-keyword">const</span> port2 = channel.<span class="hljs-property">port2</span>;
<span class="hljs-keyword">const</span> port1 = channel.<span class="hljs-property">port1</span>;
port1.<span class="hljs-property">onmessage</span> = performWorkUntilDeadline;

<span class="hljs-keyword">const</span> taskQueue = [];
<span class="hljs-keyword">let</span> startTime = -<span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> frameYieldMs = <span class="hljs-number">5</span>; <span class="hljs-comment">// 任务的连续执行时间不能超过5ms</span>
<span class="hljs-keyword">let</span> currentTask = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 用来保存当前的任务</span>

btn.<span class="hljs-property">onclick</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1000</span>; i++) &#123;
        taskQueue.<span class="hljs-title function_">push</span>(macroTask)
    &#125;
    <span class="hljs-comment">// 在下个事件循环开始调度任务</span>
    port2.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">performWorkUntilDeadline</span>(<span class="hljs-params"></span>) &#123;
    startTime = performance.<span class="hljs-title function_">now</span>(); <span class="hljs-comment">// 更新开始时间</span>
    <span class="hljs-keyword">let</span> hasMoreWork = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">try</span> &#123;
        hasMoreWork = <span class="hljs-title function_">flushWork</span>();
    &#125; <span class="hljs-keyword">finally</span> &#123;
        currentTask = <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">if</span>(hasMoreWork) &#123;
            port2.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title function_">workLoop</span>();
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">// 这里用currentTask全局变量来保存当前任务看起来似乎有点丑。</span>
    <span class="hljs-comment">// 其实是为了后续实现任务优先级和任务插队功能，先不管，就这么写。</span>
    currentTask = taskQueue[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">while</span>(currentTask) &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-title function_">shouldYieldToHost</span>()) &#123;
            <span class="hljs-keyword">break</span>;
        &#125;
        currentTask.<span class="hljs-title function_">call</span>(<span class="hljs-literal">null</span>);
        taskQueue.<span class="hljs-title function_">shift</span>(); <span class="hljs-comment">// 执行完的任务从队列中删除</span>
        currentTask = taskQueue[<span class="hljs-number">0</span>]; <span class="hljs-comment">// 继续拿下一个任务</span>
    &#125;
    <span class="hljs-keyword">if</span>(currentTask) &#123;
        <span class="hljs-comment">// 还有任务需要在下个事件循环处理</span>
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">shouldYieldToHost</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">// 是否应该挂起任务</span>
    <span class="hljs-keyword">const</span> currentTime = performance.<span class="hljs-title function_">now</span>();
    <span class="hljs-keyword">if</span>(currentTime - startTime < frameYieldMs) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">macroTask</span>(<span class="hljs-params"></span>)&#123;
    <span class="hljs-keyword">const</span> time = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]; 
    <span class="hljs-keyword">const</span> zeroOrOne = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">round</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>());
    <span class="hljs-keyword">const</span> start = performance.<span class="hljs-title function_">now</span>();
    <span class="hljs-keyword">while</span> (performance.<span class="hljs-title function_">now</span>() - start < time[zeroOrOne]) &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了我们再看看运行结果：浏览器的帧率现在已经可以保持在60fps了，效果已经很不错了。但是目前我们的任务队列只是一个普通的先进先出队列，并没有实现优先级和任务插队功能。下一篇文章我们将继续跟着react的实现思路，用最小堆来实现优先队列。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f64d3b284cac4a2eb52ec7bbc9d6b935~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1663316870570.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            