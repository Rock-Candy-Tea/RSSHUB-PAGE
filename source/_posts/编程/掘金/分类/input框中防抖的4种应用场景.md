
---
title: 'input框中防抖的4种应用场景'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bcc16c771fd43d8b3f4f0b5eec820ef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 07:40:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bcc16c771fd43d8b3f4f0b5eec820ef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、为什么要写这个文章？</h3>
<p>节流/防抖的文章想必大家也看过了很多，大多数都是分为<code>立即执行</code>和<code>非立即执行</code>两种版本的。最近在使用的过程的中，发现这两个版本在input框输入的时候得到的效果都不理想。下面就一起来看一下对应的场景，以及优化方式。</p>
<h3 data-id="heading-1">二、使用场景</h3>
<h4 data-id="heading-2">1. 非立即执行</h4>
<p><code>非立即执行</code>的版本就是在连续输入的时候，只要输入的间隔不超过设置的时间间隔，那么这个事件就会只执行一次，也就是最末尾的那一次。</p>
<ul>
<li>
<h5 data-id="heading-3">对应的代码为：</h5>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 防抖函数非立即执行版
 * <span class="hljs-doctag">@author <span class="hljs-variable">waldon</span></span>
 * <span class="hljs-doctag">@date </span>2021-05-01
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>- 防抖函数
 */</span>
<span class="hljs-keyword">const</span> debounce = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-number">0</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn, delay = <span class="hljs-number">300</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (timer) &#123;
      <span class="hljs-built_in">clearTimeout</span>(timer)
    &#125;
    <span class="hljs-comment">// 非立即执行</span>
    timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      fn()
    &#125;, delay)
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h5 data-id="heading-4">效果展示：</h5>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bcc16c771fd43d8b3f4f0b5eec820ef~tplv-k3u1fbpfcp-zoom-1.image" alt="非立即执行" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h5 data-id="heading-5">缺陷</h5>
</li>
</ul>
<p>通过上面的动图，可以很清晰的看到，input的值改变后，要等300毫秒，事件才会执行。但是vue的v-model中使用了<code>compositionstart</code>和<code>compositionend</code>帮我们对中文输入进行了优化，一般用户打出第一个词的时候，就想到看到对应的搜索结果了。这种防抖牺牲了用户在速度上的体验。</p>
<h4 data-id="heading-6">2. 立即执行</h4>
<p><code>立即执行</code>的版本就是在连续输入的时候，只触发第一个关键词改变时的事件。除非后面输入的间隔大于设置的时间间隔，否则不会再次触发</p>
<ul>
<li>
<h5 data-id="heading-7">对应的代码为：</h5>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 防抖函数立即执行版
 * <span class="hljs-doctag">@author <span class="hljs-variable">waldon</span></span>
 * <span class="hljs-doctag">@date </span>2021-05-01
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>- 防抖函数
 */</span>
<span class="hljs-keyword">const</span> debounce = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-number">0</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn, delay = <span class="hljs-number">300</span>, immediate = <span class="hljs-literal">true</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (timer) &#123;
      <span class="hljs-built_in">clearTimeout</span>(timer)
    &#125;
    <span class="hljs-keyword">if</span> (immediate) &#123;
      <span class="hljs-keyword">const</span> callNow = !timer
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        timer = <span class="hljs-number">0</span>
      &#125;, delay)
      <span class="hljs-keyword">if</span> (callNow) &#123;
        fn()
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 非立即执行</span>
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        fn()
      &#125;, delay)
    &#125;
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h5 data-id="heading-8">效果展示：</h5>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0a91db786f04ba38dd19690c8266ab1~tplv-k3u1fbpfcp-zoom-1.image" alt="立即执行" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h5 data-id="heading-9">缺陷</h5>
</li>
</ul>
<p>这个立即执行的防抖在input框中使用算是有bug的。</p>
<ol>
<li>输入快的时候，只会搜索第一个关键词，后面的都会被忽略掉。如果使用在搜索列表中的话，这个搜索结果肯定是不对的</li>
<li>长按back/delete键删除，频率也是很快的。即使到后面删完了，显示的搜索结果还是删除第一个关键词的那个搜索结果。</li>
</ol>
<p>这时候，细心一点的朋友就会想到了。那在输入的头和尾都触发一次不就可以了嘛？我们继续来看第三种。</p>
<h4 data-id="heading-10">3. 立即执行 + 延迟执行</h4>
<p>这个的效果就是前面两种结合。会在输入第一个关键词的时候执行一次逻辑，然后中间连续输入的话不会执行，等到停止输入的时候，再执行最后一次输入的逻辑。</p>
<ul>
<li>
<h5 data-id="heading-11">对应的代码为：</h5>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 防抖函数重复执行版
 * <span class="hljs-doctag">@author <span class="hljs-variable">waldon</span></span>
 * <span class="hljs-doctag">@date </span>2021-05-01
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>- 防抖函数
 */</span>
<span class="hljs-keyword">const</span> debounce = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-number">0</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn, delay = <span class="hljs-number">300</span>, immediate = <span class="hljs-literal">true</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (timer) &#123;
      <span class="hljs-built_in">clearTimeout</span>(timer)
    &#125;
    <span class="hljs-keyword">if</span> (immediate) &#123;
      <span class="hljs-keyword">const</span> callNow = !timer
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        fn() <span class="hljs-comment">// 比立即执行的版本多了这一步</span>
        timer = <span class="hljs-number">0</span>
      &#125;, delay)
      <span class="hljs-keyword">if</span> (callNow) &#123;
        fn()
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 非立即执行</span>
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        fn()
      &#125;, delay)
    &#125;
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h5 data-id="heading-12">效果展示：</h5>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d02f73a27ae483a8d589a82f83c75c5~tplv-k3u1fbpfcp-zoom-1.image" alt="非立即执行 + 立即执行" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h5 data-id="heading-13">点评</h5>
</li>
</ul>
<p>这个版本已经能解决 延迟 和 执行结果不准确 这两个问题了。但是更细心的朋友可能就会发现了：“上面的动图中，只输入了一个关键词的时候，也执行了两次。”如果项目里面没有处理重复请求的逻辑的话，那岂不是要发两个重复的请求？那肯定得优化一下了。</p>
<h4 data-id="heading-14">4. 立即执行 + 延迟执行 + cacheKey</h4>
<p>这个和第三个版本的效果是一致的，只是加入了一个cacheKey的字段作为缓存值来判断上一次输入的值是否一致，避免执行重复的逻辑。</p>
<ul>
<li>
<h5 data-id="heading-15">对应的代码为：</h5>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 防抖函数cacheKey版
 * <span class="hljs-doctag">@author <span class="hljs-variable">waldon</span></span>
 * <span class="hljs-doctag">@date </span>2021-05-01
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>- 防抖函数
 */</span>
<span class="hljs-keyword">const</span> debounce = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> cacheKey = <span class="hljs-string">''</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn, delay = <span class="hljs-number">300</span>, immediate = <span class="hljs-literal">true</span>, key = <span class="hljs-string">''</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (timer) &#123;
      <span class="hljs-built_in">clearTimeout</span>(timer)
    &#125;
    <span class="hljs-keyword">if</span> (immediate) &#123;
      <span class="hljs-comment">// 立即执行</span>
      <span class="hljs-keyword">let</span> callNow = !timer
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        timer = <span class="hljs-number">0</span>
        <span class="hljs-keyword">if</span> (cacheKey !== key) &#123;
          fn()
        &#125;
      &#125;, delay)
      <span class="hljs-keyword">if</span> (callNow) &#123;
        cacheKey = key
        fn()
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 非立即执行</span>
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        fn()
      &#125;, delay)
    &#125;
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h5 data-id="heading-16">效果展示：</h5>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/841a3fdfe32b43338dd1d7aac10b71e8~tplv-k3u1fbpfcp-zoom-1.image" alt="cacheKey" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h5 data-id="heading-17">点评</h5>
</li>
</ul>
<p>解决了关键词一样还会重复执行的问题。在input事件里面可以把input的value值作为key，pageScroll事件的话可以将scrollTop的值作为key。这个其实是能应付大部分场景的，但是有些比较特殊的场景，他连续触发的时候，没有传改变的值的，那这样肯定不适用了。</p>
<h4 data-id="heading-18">5. 立即执行 + 延迟执行 + lastTimer</h4>
<p>这个版本其实是看了lodash的源码后思考出来的。大致的思路就是，在第一次定时任务定义的时候，把任务池的id也赋值给另一个变量。当连续触发后，timer是会一直变的，而最开始赋值的lastTimer是不会变的。判断这两个值不一致的时候，不触发回调函数，等到连续触发的行为停止之后，再在回调函数里面重置这两个变量。</p>
<ul>
<li>
<h5 data-id="heading-19">对应的代码为：</h5>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 防抖函数lastTimer版
 * <span class="hljs-doctag">@author <span class="hljs-variable">waldon</span></span>
 * <span class="hljs-doctag">@date </span>2021-05-01
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;Function&#125;</span> </span>- 防抖函数
 */</span>
<span class="hljs-keyword">const</span> debounce = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> lastTimer = <span class="hljs-number">0</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">fn, delay = <span class="hljs-number">300</span>, immediate = <span class="hljs-literal">true</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (timer) &#123;
      <span class="hljs-built_in">clearTimeout</span>(timer)
    &#125;
    <span class="hljs-keyword">if</span> (immediate) &#123;
      <span class="hljs-comment">// 立即执行</span>
      <span class="hljs-keyword">let</span> callNow = !timer
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span> (lastTimer !== timer) &#123;
          timer = <span class="hljs-number">0</span>
          lastTimer = <span class="hljs-number">0</span>
          fn()
        &#125;
      &#125;, delay)
      <span class="hljs-keyword">if</span> (callNow) &#123;
        lastTimer = timer
        fn()
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 非立即执行</span>
      timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        fn()
        timer = <span class="hljs-number">0</span>
      &#125;, delay)
    &#125;
  &#125;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h5 data-id="heading-20">效果展示：</h5>
</li>
</ul>
<p>这里的效果和第4版是一样的，就不重复贴图了。</p>
<ul>
<li>
<h5 data-id="heading-21">lodash的debounce实现源码</h5>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">func, wait, options</span>) </span>&#123;
  <span class="hljs-keyword">let</span> lastArgs,
    lastThis,
    maxWait,
    result,
    timerId,
    lastCallTime

  <span class="hljs-keyword">let</span> lastInvokeTime = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> leading = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">let</span> maxing = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">let</span> trailing = <span class="hljs-literal">true</span>

  <span class="hljs-comment">// Bypass `requestAnimationFrame` by explicitly setting `wait=0`.</span>
  <span class="hljs-keyword">const</span> useRAF = (!wait && wait !== <span class="hljs-number">0</span> && <span class="hljs-keyword">typeof</span> root.requestAnimationFrame === <span class="hljs-string">'function'</span>)

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> func !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Expected a function'</span>)
  &#125;
  wait = +wait || <span class="hljs-number">0</span>
  <span class="hljs-keyword">if</span> (isObject(options)) &#123;
    leading = !!options.leading
    maxing = <span class="hljs-string">'maxWait'</span> <span class="hljs-keyword">in</span> options
    maxWait = maxing ? <span class="hljs-built_in">Math</span>.max(+options.maxWait || <span class="hljs-number">0</span>, wait) : maxWait
    trailing = <span class="hljs-string">'trailing'</span> <span class="hljs-keyword">in</span> options ? !!options.trailing : trailing
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invokeFunc</span>(<span class="hljs-params">time</span>) </span>&#123;
    <span class="hljs-keyword">const</span> args = lastArgs
    <span class="hljs-keyword">const</span> thisArg = lastThis

    lastArgs = lastThis = <span class="hljs-literal">undefined</span>
    lastInvokeTime = time
    result = func.apply(thisArg, args)
    <span class="hljs-keyword">return</span> result
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">startTimer</span>(<span class="hljs-params">pendingFunc, wait</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (useRAF) &#123;
      root.cancelAnimationFrame(timerId)
      <span class="hljs-keyword">return</span> root.requestAnimationFrame(pendingFunc)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">setTimeout</span>(pendingFunc, wait)
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cancelTimer</span>(<span class="hljs-params">id</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (useRAF) &#123;
      <span class="hljs-keyword">return</span> root.cancelAnimationFrame(id)
    &#125;
    <span class="hljs-built_in">clearTimeout</span>(id)
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">leadingEdge</span>(<span class="hljs-params">time</span>) </span>&#123;
    <span class="hljs-comment">// Reset any `maxWait` timer.</span>
    lastInvokeTime = time
    <span class="hljs-comment">// Start the timer for the trailing edge.</span>
    timerId = startTimer(timerExpired, wait)
    <span class="hljs-comment">// Invoke the leading edge.</span>
    <span class="hljs-keyword">return</span> leading ? invokeFunc(time) : result
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remainingWait</span>(<span class="hljs-params">time</span>) </span>&#123;
    <span class="hljs-keyword">const</span> timeSinceLastCall = time - lastCallTime
    <span class="hljs-keyword">const</span> timeSinceLastInvoke = time - lastInvokeTime
    <span class="hljs-keyword">const</span> timeWaiting = wait - timeSinceLastCall

    <span class="hljs-keyword">return</span> maxing
      ? <span class="hljs-built_in">Math</span>.min(timeWaiting, maxWait - timeSinceLastInvoke)
      : timeWaiting
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shouldInvoke</span>(<span class="hljs-params">time</span>) </span>&#123;
    <span class="hljs-keyword">const</span> timeSinceLastCall = time - lastCallTime
    <span class="hljs-keyword">const</span> timeSinceLastInvoke = time - lastInvokeTime

    <span class="hljs-comment">// Either this is the first call, activity has stopped and we're at the</span>
    <span class="hljs-comment">// trailing edge, the system time has gone backwards and we're treating</span>
    <span class="hljs-comment">// it as the trailing edge, or we've hit the `maxWait` limit.</span>
    <span class="hljs-keyword">return</span> (lastCallTime === <span class="hljs-literal">undefined</span> || (timeSinceLastCall >= wait) ||
      (timeSinceLastCall < <span class="hljs-number">0</span>) || (maxing && timeSinceLastInvoke >= maxWait))
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timerExpired</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> time = <span class="hljs-built_in">Date</span>.now()
    <span class="hljs-keyword">if</span> (shouldInvoke(time)) &#123;
      <span class="hljs-keyword">return</span> trailingEdge(time)
    &#125;
    <span class="hljs-comment">// Restart the timer.</span>
    timerId = startTimer(timerExpired, remainingWait(time))
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trailingEdge</span>(<span class="hljs-params">time</span>) </span>&#123;
    timerId = <span class="hljs-literal">undefined</span>

    <span class="hljs-comment">// Only invoke if we have `lastArgs` which means `func` has been</span>
    <span class="hljs-comment">// debounced at least once.</span>
    <span class="hljs-keyword">if</span> (trailing && lastArgs) &#123;
      <span class="hljs-keyword">return</span> invokeFunc(time)
    &#125;
    lastArgs = lastThis = <span class="hljs-literal">undefined</span>
    <span class="hljs-keyword">return</span> result
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cancel</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (timerId !== <span class="hljs-literal">undefined</span>) &#123;
      cancelTimer(timerId)
    &#125;
    lastInvokeTime = <span class="hljs-number">0</span>
    lastArgs = lastCallTime = lastThis = timerId = <span class="hljs-literal">undefined</span>
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flush</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> timerId === <span class="hljs-literal">undefined</span> ? result : trailingEdge(<span class="hljs-built_in">Date</span>.now())
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pending</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> timerId !== <span class="hljs-literal">undefined</span>
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounced</span>(<span class="hljs-params">...args</span>) </span>&#123;
    <span class="hljs-keyword">const</span> time = <span class="hljs-built_in">Date</span>.now()
    <span class="hljs-keyword">const</span> isInvoking = shouldInvoke(time)

    lastArgs = args
    lastThis = <span class="hljs-built_in">this</span>
    lastCallTime = time

    <span class="hljs-keyword">if</span> (isInvoking) &#123;
      <span class="hljs-keyword">if</span> (timerId === <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">return</span> leadingEdge(lastCallTime)
      &#125;
      <span class="hljs-keyword">if</span> (maxing) &#123;
        <span class="hljs-comment">// Handle invocations in a tight loop.</span>
        timerId = startTimer(timerExpired, wait)
        <span class="hljs-keyword">return</span> invokeFunc(lastCallTime)
      &#125;
    &#125;
    <span class="hljs-keyword">if</span> (timerId === <span class="hljs-literal">undefined</span>) &#123;
      timerId = startTimer(timerExpired, wait)
    &#125;
    <span class="hljs-keyword">return</span> result
  &#125;
  debounced.cancel = cancel
  debounced.flush = flush
  debounced.pending = pending
  <span class="hljs-keyword">return</span> debounced
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">三、总结</h3>
<p>这里的使用场景只是针对用户量特别大或者请求特别耗性能的情况，如果服务器的压力允许的话，使用节流在适当的间隔时间给用户一定的反馈，其实用户体验会更好一些。</p>
<p>最后，五一快乐~</p>
<h3 data-id="heading-23">四、参考资源</h3>
<ul>
<li><a href="https://github.com/lodash/lodash" target="_blank" rel="nofollow noopener noreferrer">github.com/lodash/loda…</a></li>
</ul></div>  
</div>
            