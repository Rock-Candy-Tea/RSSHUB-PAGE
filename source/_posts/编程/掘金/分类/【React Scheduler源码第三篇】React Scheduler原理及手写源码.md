
---
title: '【React Scheduler源码第三篇】React Scheduler原理及手写源码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80008e3b78bb4972b28df4f8ab42cf3a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 06:21:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80008e3b78bb4972b28df4f8ab42cf3a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>欢迎关注我的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flizuncong" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flizuncong" target="_blank">Github</a>一起学习前端各种框架的源码。掘金的文章只是仓库中的一部分，如果对源码感兴趣，可以直接关注github，github里面的文章是最新的</p>
</blockquote>
<blockquote>
<p>本章是手写 React Scheduler 异步任务调度源码系列的第三篇文章，前两篇可以点击下面链接查看：1.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flizuncong%2Fmini-react%2Fblob%2Fmaster%2Fdocs%2Fschedule%2F%25E5%2593%25AA%25E4%25BA%259BAPI%25E9%2580%2582%25E5%2590%2588%25E7%2594%25A8%25E4%25BA%258E%25E4%25BB%25BB%25E5%258A%25A1%25E8%25B0%2583%25E5%25BA%25A6.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lizuncong/mini-react/blob/master/docs/schedule/%E5%93%AA%E4%BA%9BAPI%E9%80%82%E5%90%88%E7%94%A8%E4%BA%8E%E4%BB%BB%E5%8A%A1%E8%B0%83%E5%BA%A6.md" ref="nofollow noopener noreferrer">哪些 API 适合用于任务调度</a>。2.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flizuncong%2Fmini-react%2Fblob%2Fmaster%2Fdocs%2Fschedule%2Fscheduler%25E7%2594%25A8%25E6%25B3%2595%25E8%25AF%25A6%25E8%25A7%25A3.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lizuncong/mini-react/blob/master/docs/schedule/scheduler%E7%94%A8%E6%B3%95%E8%AF%A6%E8%A7%A3.md" ref="nofollow noopener noreferrer">scheduler 用法详解</a>。来看看为啥采用 MessageChannel 而不是 setTimeout 等 api 实现异步任务调度。任务切片，时间切片这些概念听着吓人，但原理其实很简单。实际上这篇文章不需要 react 背景即可看懂，给我们提供了一种解决耗时长的任务的思路。</p>
</blockquote>
<h2 data-id="heading-0">学习目标</h2>
<ul>
<li>同步更新 & 异步更新</li>
<li>为什么不使用 setTimeout</li>
<li>为什么使用 Message Channel</li>
<li>任务切片</li>
<li>时间切片</li>
</ul>
<h2 data-id="heading-1">前置基础知识</h2>
<p>如果对 <code>requestAnimationFrame</code>、<code>requestIdleCallback</code>、<code>setTimeout</code>、<code>MessageChannel</code>、<code>MutationObserver</code>、<code>Promise</code>等 API 还不熟悉的，可以先看<a href="https://link.juejin.cn/?target=.%2F%25E5%2593%25AA%25E4%25BA%259BAPI%25E9%2580%2582%25E5%2590%2588%25E7%2594%25A8%25E4%25BA%258E%25E4%25BB%25BB%25E5%258A%25A1%25E8%25B0%2583%25E5%25BA%25A6.md" target="_blank" title="./%E5%93%AA%E4%BA%9BAPI%E9%80%82%E5%90%88%E7%94%A8%E4%BA%8E%E4%BB%BB%E5%8A%A1%E8%B0%83%E5%BA%A6.md" ref="nofollow noopener noreferrer">这篇文章</a>熟悉一下。如果对 React Scheduler 用法还不熟悉的，可以先看<a href="https://link.juejin.cn/?target=.%2Fscheduler%25E7%2594%25A8%25E6%25B3%2595%25E8%25AF%25A6%25E8%25A7%25A3.md" target="_blank" title="./scheduler%E7%94%A8%E6%B3%95%E8%AF%A6%E8%A7%A3.md" ref="nofollow noopener noreferrer">这篇文章</a>熟悉一下。当然，不看也不影响理解本章的内容</p>
<h2 data-id="heading-2">故事从一个动画开始</h2>
<p>这天，老板让小李开发一个放大缩小的无限循环的动画。这是老板的一句话需求，没有 UI 也没有需求文档。那既然是一句话需求，小李也就三两句代码就实现了：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>schedule源码<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span>
      <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span>
      <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1"</span>
    /></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-id">#animation</span> &#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">justify-content</span>: center;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">background</span>: red;
        <span class="hljs-attribute">animation</span>: myfirst <span class="hljs-number">5s</span>;
        <span class="hljs-attribute">animation-iteration-count</span>: infinite;
      &#125;

      <span class="hljs-keyword">@keyframes</span> myfirst &#123;
        <span class="hljs-selector-tag">from</span> &#123;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">30px</span>;
          <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
          <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">background</span>: red;
        &#125;
        <span class="hljs-selector-tag">to</span> &#123;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
          <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
          <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
          <span class="hljs-attribute">background</span>: yellow;
        &#125;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>perform work<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"animation"</span>></span>Animation<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"btn"</span>);
      <span class="hljs-keyword">const</span> animate = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"animation"</span>);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>呐，老板，我实现了，效果如下，小李开心的说。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80008e3b78bb4972b28df4f8ab42cf3a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-01.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>老板看了看，摇了摇头，这是啥玩意啊</p>
<h2 data-id="heading-3">同步更新页面</h2>
<p>老板说了，他有一组任务，点击按钮的时候，需要遍历执行完这组任务，统计全部任务执行完成的耗时，然后更新到页面。每个任务执行耗时差不多 2ms，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> works = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3000</span>; i++) &#123;
  works.<span class="hljs-title function_">push</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
    <span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>() - start < <span class="hljs-number">2</span>) &#123;&#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小李看了看，老板的需求总是这么简单，不到 2 秒，小李已经实现了如下：</p>
<pre><code class="hljs language-js copyable" lang="js">btn.<span class="hljs-property">onclick</span> = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> startTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  <span class="hljs-title function_">flushWork</span>();
  <span class="hljs-keyword">const</span> endTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  animate.<span class="hljs-property">innerHTML</span> = endTime - startTime;
&#125;;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params"></span>) &#123;
  works.<span class="hljs-title function_">forEach</span>(<span class="hljs-function">(<span class="hljs-params">w</span>) =></span> <span class="hljs-title function_">w</span>());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小李屁颠屁颠的跑过去给老板看效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f193ed0cc54d4870b93a624732d7e53a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-02.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>老板心想小伙子能力不错，10 点钟给的需求，10:02 分就已经完成了，真是一个有(压榨)潜力的员工。于是老板满心欢喜的点了下按钮。结果，过了差不多 6 秒页面才更新，同时页面卡死了。。。再次点击按钮都点不了。老板的脸渐渐黑化，这又是啥玩意，赶紧优化一下</p>
<h3 data-id="heading-4">问题分析</h3>
<p>失望的小李分析了下，点击按钮时，这组任务是同步执行的，所有任务执行完成，总共耗时差不多 6 秒，而在这个过程中，js 引擎一直占用着控制权，浏览器无法绘制页面，也无法响应用户，用户体验相当不好，怪不得老板的脸黑了。所以，这组耗时长的任务不应该同步执行</p>
<h2 data-id="heading-5">使用 setTimeout 异步更新页面</h2>
<p>这次，小李打算使用异步的方式执行任务，将任务放到 setTimeout 定时器里面执行。为了不长时间占用主线程，阻塞浏览器渲染，小李将任务拆分到定时器执行，每个定时器执行一个任务。每执行一次都判断 works 是否全部执行完成，如果全部执行完成，则更新页面。每执行完一次任务，都主动将控制权让出给浏览器。这次，小李花了 10 分钟整改了下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">btn.<span class="hljs-property">onclick</span> = <span class="hljs-function">() =></span> &#123;
  startTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  <span class="hljs-title function_">flushWork</span>();
&#125;;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-built_in">setTimeout</span>(workLoop, <span class="hljs-number">0</span>);
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> work = works.<span class="hljs-title function_">shift</span>();
  <span class="hljs-keyword">if</span> (work) &#123;
    <span class="hljs-title function_">work</span>();
    <span class="hljs-built_in">setTimeout</span>(workLoop, <span class="hljs-number">0</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> endTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
    animate.<span class="hljs-property">innerHTML</span> = endTime - startTime;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小李这次不太敢屁颠屁颠的去找老板了，转而悄咪咪地过去。老板以为会有惊喜，立马点击按钮，这次页面动画终于不卡顿了，老板似乎看到了希望，嘴角微微上扬，然而等了差不多 19 秒的时间，页面才更新。这又是啥玩意啊，老板突然歇斯底里。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d624f65c8da4e5fa9300b6dabe523c6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-03.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小李确实大意了，在上一次的时候，任务执行总耗时才 6000 毫秒，每个任务执行耗时 2 毫秒，3000 个任务，最多也就 6000 毫秒，为啥这次执行耗时 19266 毫秒，远比之前多出了 13266 毫秒？</p>
<p>小李看了下 Performance。虽然使用了<code>setTimeout(workLoop, 0)</code>0 毫秒的时间间隔，但是浏览器依然会有 4 到 5 毫秒的间隔时间。如果两次 setTimeout 之间最少间隔 4 毫秒，都有至少 3000 * 4 = 12000 毫秒的耗时了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b98db1f139904c7b88a7df97680f5253~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-04.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">问题分析</h3>
<p>即使<code>setTimeout(workLoop, 0)</code>设置了 0 毫秒的时间间隔，但浏览器也会有至少 4 到 5 毫秒的延迟。在执行一组数量不限的任务时，这个耗时是不容忽视的。<strong>作为一个专业的前端切图仔，我们在追求页面动画流畅、不卡顿的同时，应该还要快速响应用户的输入从而快速更新页面</strong>。显然，setTimeout 由于 4 毫秒间隔的原因，不适用于我们的场景。那还有哪些 API 既可以出发宏任务事件，两次宏任务之间间隔有非常短呢？小李想起了在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flizuncong%2Fmini-react%2Fblob%2Fmaster%2Fdocs%2Fschedule%2F%25E5%2593%25AA%25E4%25BA%259BAPI%25E9%2580%2582%25E5%2590%2588%25E7%2594%25A8%25E4%25BA%258E%25E4%25BB%25BB%25E5%258A%25A1%25E8%25B0%2583%25E5%25BA%25A6.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lizuncong/mini-react/blob/master/docs/schedule/%E5%93%AA%E4%BA%9BAPI%E9%80%82%E5%90%88%E7%94%A8%E4%BA%8E%E4%BB%BB%E5%8A%A1%E8%B0%83%E5%BA%A6.md" ref="nofollow noopener noreferrer">哪些 API 适用于任务调度</a>一文中学到的知识，<code>MessageChannel</code>在一帧内的调用频率超高，且两次调用的时间间隔极短。于是小李决定尝试一下这个 API</p>
<blockquote>
<p>不使用 Promise 或者 MutationObserver 等微任务 API 的原因是，微任务是在页面更新前全部执行完成的，效果和同步执行任务差不多。</p>
</blockquote>
<h2 data-id="heading-7">使用 MessageChannel 异步更新页面</h2>
<p>这次，小李使用 <code>MessageChannel</code> 触发一个宏任务，在宏任务事件中执行工作。每执行完一个工作，判断是否已经执行完全部的工作，如果是，则更新页面，否则调用<code>port.postMessage(null)</code>触发下一个宏任务，继续执行剩余的工作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> channel = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MessageChannel</span>();
<span class="hljs-keyword">var</span> port = channel.<span class="hljs-property">port2</span>;
channel.<span class="hljs-property">port1</span>.<span class="hljs-property">onmessage</span> = workLoop;

<span class="hljs-keyword">let</span> startTime;
btn.<span class="hljs-property">onclick</span> = <span class="hljs-function">() =></span> &#123;
  startTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
&#125;;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> work = works.<span class="hljs-title function_">shift</span>();
  <span class="hljs-keyword">if</span> (work) &#123;
    <span class="hljs-title function_">work</span>();
    port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> endTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
    animate.<span class="hljs-property">innerHTML</span> = endTime - startTime;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次小李学聪明了，自测了下，效果如下，可以发现耗时只用了 6090 毫秒！！！为什么会多出了 90 毫秒？观察 performance 可以看出，虽然两次宏任务之间间隔非常短，但也会导致额外的开销，累积起来就有了几毫秒的差异。不过，这已经很贴近 6000 毫秒的执行耗时了，优势远胜于 setTimeout</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d0c5e852879489e82e8467a43b9d156~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-05.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到一帧之内浏览器的绘制时间，以及 message channel 触发的次数</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/713a7b7dae9a4f52b30bc7c08152bb71~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-06.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意，这里的执行耗时也会受机器性能的影响，目前小李在多台电脑上尝试了下，一样的代码，执行耗时不太一样。当然不影响我们理解 schedule 的原理。在同一台电脑上跑，有时候耗时也不一样，比如：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6deafd540eb3450cbd18c18897b75719~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-07.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>老板终于满意了</p>
<h3 data-id="heading-8">问题分析</h3>
<p>这次，小李能够同时兼顾页面动画流畅、不卡顿以及快速响应用户输入，尽早更新页面。但是还有一点小瑕疵，由于两次任务之间还是会有一点点的时间间隔，执行数量众多的任务时，这些间隔的时间就会累加起来，就会有几毫秒的额外开销。作为一个有追求有理想的专业切图仔，小李是不允许有这种时间消耗的</p>
<h2 data-id="heading-9">任务切片：一次宏任务事件尽可能执行更多的任务</h2>
<p>在上一节中，额外消耗的时间等于两次宏任务之间的时间间隔 * 工作的数量：</p>
<pre><code class="hljs language-js copyable" lang="js">额外消耗的时间 = 两次宏任务之间的时间间隔 * works.<span class="hljs-property">length</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然，我们无法控制两次宏任务之间的时间间隔，但是我们可以减少触发宏任务事件的次数。可以通过在一次宏任务事件中执行更多的任务来达到这个目的。同时，一次宏任务事件的执行耗时又不能超过 1 帧的时间(16.6ms)，毕竟我们需要留点时间给浏览器绘制页面</p>
<p><strong>因此，我们需要在一次宏任务事件中尽可能多的执行任务，同时又不能长时间占用浏览器。<strong>为了达到这个目的，小李将任务拆分成几小段执行，即</strong>任务切片</strong>。既然一帧 16.6 毫秒，执行一次任务需要 2 毫秒，那只需要在一次宏任务事件中执行 7 个任务就好，这样浏览器还有 2.6 毫秒绘制页面。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> channel = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MessageChannel</span>();
<span class="hljs-keyword">var</span> port = channel.<span class="hljs-property">port2</span>;
channel.<span class="hljs-property">port1</span>.<span class="hljs-property">onmessage</span> = workLoop;

<span class="hljs-keyword">let</span> startTime;
btn.<span class="hljs-property">onclick</span> = <span class="hljs-function">() =></span> &#123;
  startTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
&#125;;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">while</span> (i < <span class="hljs-number">7</span>) &#123;
    <span class="hljs-keyword">let</span> work = works.<span class="hljs-title function_">shift</span>();
    <span class="hljs-keyword">if</span> (work) &#123;
      <span class="hljs-title function_">work</span>();
      i++;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">const</span> endTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
      animate.<span class="hljs-property">innerHTML</span> = endTime - startTime;
      i = <span class="hljs-number">7</span>; <span class="hljs-comment">// 没有剩余工作就直接退出循环</span>
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (works.<span class="hljs-property">length</span>) &#123;
    port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c58a482cdf50433bb4aa4fd43ab7ac57~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-08.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>放大每一帧可以看到：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/424d0a042bca40a0acf368f65996effa~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-09.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">问题分析</h3>
<p>这次，小李采用任务切片的方法极大减少了触发 message channel 的次数，减少了宏任务之间调度的额外消耗。但是这里还有个问题，任务切片的一个前提是，每个任务执行耗时是确定的，比如这里是 2 毫秒，但真实的业务场景是无法知道任务的执行耗时的，因此我们很难判断该如何将任务进行切片，本例中我们采用的是 7 个任务一个片段，那如果一个任务的执行耗时不确定，我们又怎么设置这个片段的大小？可想而知，任务切片虽然理想，但不太现实</p>
<h2 data-id="heading-11">时间切片</h2>
<p>我们来探讨一种时间切片的方式。我们知道浏览器一帧只有 16.6ms，同时我们的工作执行耗时又不是确定的。那我们是不是可以，将一次宏任务的执行时间尽可能的控制在一定的时间内，比如 5ms。在当前的宏任务事件内，我们循环执行我们的工作任务，每完成一个工作任务，都判断执行时间是否超出了 5 毫秒，如果超出了 5 毫秒，则不继续执行下一个工作任务，结束本轮宏任务事件，<strong>主动让出控制权</strong>给浏览器绘制页面。如果没有超过 5 毫秒，则继续执行下一个工作任务。</p>
<p>实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> works = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3000</span>; i++) &#123;
  works.<span class="hljs-title function_">push</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
    <span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>() - start < <span class="hljs-number">2</span>) &#123;&#125;
  &#125;);
&#125;
<span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"btn"</span>);
<span class="hljs-keyword">const</span> animate = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"animation"</span>);

<span class="hljs-keyword">var</span> channel = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MessageChannel</span>();
<span class="hljs-keyword">var</span> port = channel.<span class="hljs-property">port2</span>;
channel.<span class="hljs-property">port1</span>.<span class="hljs-property">onmessage</span> = workLoop;

<span class="hljs-keyword">let</span> endTime;
<span class="hljs-keyword">let</span> startTime;
btn.<span class="hljs-property">onclick</span> = <span class="hljs-function">() =></span> &#123;
  startTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
&#125;;
<span class="hljs-keyword">const</span> yieldInterval = <span class="hljs-number">5</span>; <span class="hljs-comment">// 单位毫秒</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> currentEventStartTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  <span class="hljs-keyword">let</span> work = works.<span class="hljs-title function_">shift</span>();
  <span class="hljs-keyword">while</span> (work) &#123;
    <span class="hljs-title function_">work</span>();
    <span class="hljs-comment">// 执行完当前工作，则判断时间是否超过5ms，如果超过，则退出while循环</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>() - currentEventStartTime > yieldInterval) &#123;
      <span class="hljs-comment">// 执行耗时超过了5ms，结束本轮事件，主动让出控制权给浏览器绘制页面或者执行其他操作</span>
      <span class="hljs-keyword">break</span>;
    &#125;
    work = works.<span class="hljs-title function_">shift</span>();
  &#125;
  <span class="hljs-comment">// 如果还有剩余的工作，则放到下一个事件中处理</span>
  <span class="hljs-keyword">if</span> (works.<span class="hljs-property">length</span>) &#123;
    port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> endTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
    animate.<span class="hljs-property">innerHTML</span> = endTime - startTime;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43ac0c2483504ee8846864198167cec8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-10.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>放大每一帧可以看到，每一个宏任务事件执行时间大约 5-6ms。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2573d9674da4afb9d588d67f25a3cfe~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-11.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">问题分析</h3>
<p>这次，我们采用时间切片的方式，每个宏任务事件最多执行 5ms，超过 5ms 则主动结束执行，让出控制权给浏览器。时间切片的好处就是我们不用关心每个任务的执行耗时。比如，这里我用随机的方法，让每个工作任务执行耗时在 0-1 毫秒之间。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> works = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3000</span>; i++) &#123;
  works.<span class="hljs-title function_">push</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> start = performance.<span class="hljs-title function_">now</span>();
    <span class="hljs-keyword">const</span> time = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>();
    <span class="hljs-keyword">while</span> (performance.<span class="hljs-title function_">now</span>() - start < time) &#123;&#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/160864468b854f2696702fab709ab0ff~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-12.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>放大每一帧可以看到：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9eaf6a6c11942dda4bbd63357ae5831~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="schedule-13.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，似乎我们的目标已经达成：在尽可能短的时间内完成耗时长的一组工作任务，同时又不会长时间占用浏览器，让浏览器处理高优先级的任务，比如响应用户输入、绘制页面等</p>
<h2 data-id="heading-13">小结</h2>
<p>到目前为止，效果还是很不错的。小李收获了以下知识：</p>
<ul>
<li>耗时长的同步任务会长时间占用浏览器导致无法响应用户输入，页面卡顿等问题</li>
<li>setTimeout 由于有至少 4 毫秒的延迟，因此不适合用于异步任务的调度</li>
<li>MessageChannel 在一帧的时间内调用频率超高，两次 message channel 宏任务事件之间的间隔开销极少，适合用于异步任务的调度。</li>
<li>由于无法提前得知任务执行时间，从而无法计算一帧之内应该执行几个任务，所以任务切片不太适用于一帧内调度异步任务。</li>
<li>时间切片是比较理想的选择</li>
</ul>
<p>小李决定将这个小工具开源</p>
<h2 data-id="heading-14">开源第一步</h2>
<p>首先需要将 Message Channel 抽成一个公用的调度方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> yieldInterval = <span class="hljs-number">5</span>;
<span class="hljs-keyword">let</span> deadline = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> <span class="hljs-title class_">MessageChannel</span>();
<span class="hljs-keyword">let</span> port = channel.<span class="hljs-property">port2</span>;
channel.<span class="hljs-property">port1</span>.<span class="hljs-property">onmessage</span> = performWorkUntilDeadline;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">performWorkUntilDeadline</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">if</span> (scheduledHostCallback) &#123;
    <span class="hljs-comment">// 当前宏任务事件开始执行</span>
    <span class="hljs-keyword">let</span> currentTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
    <span class="hljs-comment">// 计算当前宏任务事件结束时间</span>
    deadline = currentTime + yieldInterval;
    <span class="hljs-keyword">const</span> hasMoreWork = <span class="hljs-title function_">scheduledHostCallback</span>(currentTime);
    <span class="hljs-keyword">if</span> (!hasMoreWork) &#123;
      scheduledHostCallback = <span class="hljs-literal">null</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果还有工作，则触发下一个宏任务事件</span>
      port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">requestHostCallback</span>(<span class="hljs-params">callback</span>) &#123;
  scheduledHostCallback = callback;
  port.<span class="hljs-title function_">postMessage</span>(<span class="hljs-literal">null</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过 requestHostCallback 触发一个 message channel 事件，同时在 performWorkUntilDeadline 接收事件，这里需要注意，我们必须在 performWorkUntilDeadline 开始时获取到当前的时间 currentTime，然后计算出本次事件执行的截止时间，performWorkUntilDeadline 的执行时间控制在 5 毫秒内，因此截止时间就是 deadline = currentTime + yieldInterval;</p>
<p>如果 scheduledHostCallback 返回 true，说明还有剩余的工作没完成，则调度下一个宏任务事件执行剩余的工作。</p>
<p>其次，我们需要一个 scheduleCallback 方法给用户添加任务，我们将用户添加的任务保存在 taskQueue 中。然后触发一个 message channel 事件，异步执行任务。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> taskQueue = [];
<span class="hljs-keyword">let</span> isHostCallbackSchedule = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">scheduleCallback</span>(<span class="hljs-params">callback</span>) &#123;
  <span class="hljs-keyword">var</span> newTask = &#123;
    <span class="hljs-attr">callback</span>: callback,
  &#125;;
  taskQueue.<span class="hljs-title function_">push</span>(newTask);
  <span class="hljs-keyword">if</span> (!isHostCallbackScheduled) &#123;
    isHostCallbackScheduled = <span class="hljs-literal">true</span>;
    <span class="hljs-title function_">requestHostCallback</span>(flushWork);
  &#125;
  <span class="hljs-keyword">return</span> newTask;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后需要实现 flushwork 方法，在 workLoop 方法中，每执行一个工作，都需要判断当前 performWorkUntilDeadline 事件执行时间是否超过 5ms</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> currentTask = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">flushWork</span>(<span class="hljs-params">initialTime</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-title function_">workLoop</span>(initialTime);
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">workLoop</span>(<span class="hljs-params">initialTime</span>) &#123;
  currentTask = taskQueue[<span class="hljs-number">0</span>];

  <span class="hljs-keyword">while</span> (currentTask) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>() >= deadline) &#123;
      <span class="hljs-comment">// 每执行一个任务，都需要判断当前的performWorkUntilDeadline执行时间是否超过了截止时间</span>
      <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-keyword">var</span> callback = currentTask.<span class="hljs-property">callback</span>;
    <span class="hljs-title function_">callback</span>();

    taskQueue.<span class="hljs-title function_">shift</span>();
    currentTask = taskQueue[<span class="hljs-number">0</span>];
  &#125;
  <span class="hljs-keyword">if</span> (currentTask) &#123;
    <span class="hljs-comment">// 如果taskQueue中还有剩余工作，则返回true</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们就可以这样使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"btn"</span>);
<span class="hljs-keyword">const</span> animate = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"animation"</span>);
<span class="hljs-keyword">let</span> startTime;
btn.<span class="hljs-property">onclick</span> = <span class="hljs-function">() =></span> &#123;
  startTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3000</span>; i++) &#123;
    <span class="hljs-keyword">if</span> (i === <span class="hljs-number">2999</span>) &#123;
      <span class="hljs-title function_">scheduleCallback</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
        <span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>() - start < <span class="hljs-number">2</span>) &#123;&#125;
        <span class="hljs-keyword">const</span> endTime = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
        animate.<span class="hljs-property">innerHTML</span> = endTime - startTime;
      &#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-title function_">scheduleCallback</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> start = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>();
        <span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-title class_">Date</span>().<span class="hljs-title function_">getTime</span>() - start < <span class="hljs-number">2</span>) &#123;&#125;
      &#125;);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是 schedule 的简单实现。下一篇文章会继续实现优先级、延迟任务。</p></div>  
</div>
            