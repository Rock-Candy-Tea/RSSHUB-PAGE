
---
title: '【今天你更博学了么】一个神奇的交叉观察 API Intersection Observer'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd6c03692fbf4f12880e8f8d17c5e06c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 19:54:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd6c03692fbf4f12880e8f8d17c5e06c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
<p>前端开发肯定离不开判断一个元素是否能被用户看见，然后再基于此进行一些交互。</p>
<blockquote>
<p>过去，要检测一个元素是否可见或者两个元素是否相交并不容易，很多解决办法不可靠或性能很差。然而，随着互联网的发展，这种需求却与日俱增，比如，下面这些情况都需要用到相交检测：</p>
<ul>
<li>图片懒加载——当图片滚动到可见时才进行加载</li>
<li>内容无限滚动——也就是用户滚动到接近内容底部时直接加载更多，而无需用户操作翻页，给用户一种网页可以无限滚动的错觉</li>
<li>检测广告的曝光情况——为了计算广告收益，需要知道广告元素的曝光情况</li>
<li>在用户看见某个区域时执行任务或播放动画</li>
</ul>
<p>过去，相交检测通常要用到事件监听，并且需要频繁调用 <code>Element.getBoundingClientRect()</code> 方法以获取相关元素的边界信息。事件监听和调用 <code>Element.getBoundingClientRect()</code>  都是在主线程上运行，因此频繁触发、调用可能会造成性能问题。这种检测方法极其怪异且不优雅。</p>
</blockquote>
<p>上面这一段话来自 <code>MDN</code> ，中心思想就是现在判断一个元素是否能被用户看见的使用场景越来越多，监听 <code>scroll</code> 事件以及通过 <code>Element.getBoundingClientRect()</code> 获取节点位置的方式，又麻烦又不好用，那么怎么办呢。于是就有了今天的内容 <strong>Intersection Observer API</strong>。</p>
<h1 data-id="heading-1">Intersection Observer API 是什么</h1>
<p>我们需要观察的元素被称为 <strong>目标元素(target)</strong>，设备视窗或者其他指定的元素视口的边界框我们称它为 <strong>根元素</strong>(<strong>root</strong>)，或者简称为 <strong>根</strong> 。</p>
<p><code>Intersection Observer API</code> 翻译过来叫做 <strong>“交叉观察器”</strong>，因为判断元素是否可见（<strong>通常情况下</strong>）的本质就是判断目标元素和根元素是不是产生了 <strong>交叉区域</strong> 。</p>
<p>为什么是通常情况下，因为当我们 <code>css</code> 设置了 <code>opacity: 0</code>，<code>visibility: hidden</code> 或者 <code>用其他的元素覆盖目标元素</code> 的时候，对于视图来说是不可见的，但对于交叉观察器来说是可见的。这里可能有点抽象，大家只需记住，交叉观察器只关心 <strong>目标元素</strong> 和 <strong>根元素</strong> 是否有 <strong>交叉区域</strong>， 而不管视觉上能不能看见这个元素。当然如果设置了 <code>display：none</code>，那么交叉观察器就不会生效了，其实也很好理解，因为元素已经不存在了，那么也就监测不到了。</p>
<blockquote>
<p>一句话总结：<strong>Intersection Observer API</strong> 提供了一种异步检测目标元素与祖先元素或 <strong>viewport</strong> 相交情况变化的方法。 -- MDN</p>
</blockquote>
<p>现在不懂没关系，咱们接着往下看，看完自然就明白了。</p>
<h1 data-id="heading-2">Intersection Observer API 怎么玩</h1>
<h2 data-id="heading-3">生成观察器</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 调用构造函数 IntersectionObserver 生成观察器</span>
<span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先调用浏览器原生构造函数 <code>IntersectionObserver</code> ，构造函数的返回值是一个 <strong>观察器实例</strong> 。</p>
<p>构造函数 <code>IntersectionObserver</code> 接收两个参数</p>
<ul>
<li><strong>callback：</strong>  可见性发生变化时触发的回调函数</li>
<li><strong>options：</strong>  配置对象（可选，不传时会使用默认配置）</li>
</ul>
<h3 data-id="heading-4">构造函数接收的参数 options</h3>
<p>为了方便理解，我们先看第二个参数 <code>options</code> 。一个可以用来配置观察器实例的对象，那么这个配置对象都包含哪些属性呢？</p>
<ul>
<li>
<p><strong>root：</strong> 设置目标元素的根元素，也就是我们用来判断元素是否可见的区域，必须是目标元素的父级元素，如果不指定的话，则使用浏览器视窗，也就是 <code>document</code>。</p>
</li>
<li>
<p><strong>rootMargin：</strong> 一个在计算交叉值时添加至根的边界中的一组偏移量，类型为字符串 <code>(string)</code>  ，可以有效的缩小或扩大根的判定范围从而满足计算需要。语法大致和CSS 中 <code>margin</code> 属性等同，默认值 <code>“0px 0px 0px 0px”</code> ，如果有指定 <code>root</code> 参数，则 <code>rootMargin</code> 也可以使用百分比来取值。</p>
</li>
<li>
<p><strong>threshold：</strong> 介于 <code>0</code> 和 <code>1</code> 之间的数字，指示触发前应可见的百分比。也可以是一个数字数组，以创建多个触发点，也被称之为 <strong>阈值</strong>。如果构造器未传入值, 则默认值为 <code>0</code> 。</p>
</li>
<li>
<p><strong>trackVisibility：</strong> 一个布尔值，指示当前观察器是否将跟踪目标可见性的更改，默认为 <code>false</code> ，注意，此处的可见性并非指目标元素和根元素是否相交，而是指视图上是否可见，这个我们之前就已经分析过了，如果此值设置为 <code>false</code> 或不设置，那么回调函数参数中 <code>IntersectionObserverEntry</code> 的 <code>isVisible</code> 属性将永远返回 <code>false</code> 。</p>
</li>
<li>
<p><strong>delay：</strong> 一个数字，也就是回调函数执行的延迟时间（毫秒）。如果 <code>trackVisibility</code> 设置为 <code>true</code>，则此值必须至少设置为 <code>100</code> ，否则会报错（但是这里我也只是亲测出来的，并不知道为什么会设计成这样，如果有大佬了解请指教一下）。</p>
</li>
</ul>
<h3 data-id="heading-5">构造函数接收的参数 callback</h3>
<p>当元素可见比例超过指定阈值后，会调用一个回调函数，此回调函数接受两个参数：存放 <code>IntersectionObserverEntry</code> 对象的数组和观察器实例(可选)。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">(<span class="hljs-params">doc</span>) =></span> &#123;
  <span class="hljs-comment">//回调函数</span>
  <span class="hljs-keyword">const</span> callback = <span class="hljs-function">(<span class="hljs-params">entries, observer</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ 执行了一次callback'</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ entries:'</span>, entries);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ observer:'</span>, observer);
  &#125;;
  <span class="hljs-comment">//配置对象</span>
  <span class="hljs-keyword">const</span> options = &#123;&#125;;
  <span class="hljs-comment">//创建观察器</span>
  <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
  <span class="hljs-comment">//获取目标元素</span>
  <span class="hljs-keyword">const</span> target = doc.querySelector(<span class="hljs-string">".target"</span>)
  <span class="hljs-comment">//开始监听目标元素</span>
  myObserver.observe(target);
&#125;)(<span class="hljs-built_in">document</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把这两个参数打印出来看一下，可以看到，第一个参数是一个数组，每一项都是一个目标元素对应的
<code>IntersectionObserverEntry</code>对象，第二个参数是观察器实例对象 <code>IntersectionObserver</code> 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd6c03692fbf4f12880e8f8d17c5e06c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">什么是 IntersectionObserverEntry 对象</h4>
<p>展开 <code>IntersectionObserverEntry</code> 看一下都有什么。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edae03d1399c43bd815c5a42c2f00c03~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>boundingClientRect：</strong> 一个对象，包含目标元素的 <code>getBoundingClientRect()</code> 方法的返回值。</p>
</li>
<li>
<p><strong>intersectionRatio：</strong>   一个对象，包含目标元素与根元素交叉区域 <code>getBoundingClientRect()</code> 的返回值。</p>
</li>
<li>
<p><strong>intersectionRect：</strong> 目标元素的可见比例，即 <code>intersectionRect</code> 占 <code>boundingClientRect</code> 的比例，完全可见时为 <code>1</code> ，完全不可见时小于等于 <code>0</code> 。</p>
</li>
<li>
<p><strong>isIntersecting：</strong> 返回一个布尔值，如果目标元素与根元素相交，则返回 <code>true</code> ，如果 <code>isIntersecting</code> 是 <code>true</code>，则 <code>target</code> 元素至少已经达到 <code>thresholds</code> 属性值当中规定的其中一个阈值，如果是 <code>false</code>，<code>target</code> 元素不在给定的阈值范围内可见。</p>
</li>
<li>
<p><strong>isVisible：</strong> 这个看字面意思应该是 <strong>“是否可见”</strong> ，如果要让这个属性生效，那么在使用构造函数生成观察器实例的时候，传入的 <code>options</code> 参数必须配置 <code>trackVisibility</code> 为 <code>true</code>，并且 <code>delay</code> 设置为大于  <code>100</code> ，否则该属性将永远返回 <code>false</code> 。</p>
</li>
<li>
<p><strong>rootBounds：</strong> 一个对象，包含根元素的 <code>getBoundingClientRect()</code> 方法的返回值。</p>
</li>
<li>
<p><strong>target：：</strong> 被观察的目标元素，是一个 <code>DOM</code> 节点。在观察者包含多个目标的情况下，这是确定哪个目标元素触发了此相交更改的简便方法。</p>
</li>
<li>
<p><strong>time：</strong> 该属性提供从 <strong>首次创建观察者</strong> 到 <strong>触发此交集改变</strong> 的时间（以毫秒为单位）。通过这种方式，你可以跟踪观察器达到特定阈值所花费的时间。即使稍后将目标再次滚动到视图中，此属性也会提供新的时间。这可用于跟踪目标元素进入和离开根元素的时间，以及两个阈值触发的间隔时间。</p>
</li>
</ul>
<p>这里再看一下 <strong>boundingClientRect</strong> ，<strong>intersectionRatio</strong> ， <strong>rootBounds</strong> 三个属性展开的内容都有什么。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9a102f0231247f3adbd1ea49ba7a990~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>bottom：</strong> 元素下边距离页面上边的距离</li>
<li><strong>left：</strong> 元素左边距离页面左边的距离</li>
<li><strong>right：</strong> 元素右边距离页面左边的距离</li>
<li><strong>top：</strong> 元素上边距离页面上边的距离</li>
<li><strong>width：</strong> 元素的宽</li>
<li><strong>height：</strong> 元素的高</li>
<li><strong>x：</strong> 等同于 <code>left</code>，元素左边距离页面左边的距离</li>
<li><strong>y：</strong> 等同于 <code>top</code>，元素上边距离页面上边的距离</li>
</ul>
<p>用一张图来展示一下这几个属性，特别需要注意的是 <code>right</code> 和 <code>bottom</code> ，跟我们平时写 <code>css</code> 的 <code>position</code> 那个不一样 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1819cda28798437fbd68cfe9d87c9473~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">那么第二个参数 IntersectionObserver 观察器实例对象都有什么呢</h4>
<p>别着急，接着往下看，实例属性部分。</p>
<h2 data-id="heading-8">观察器实例属性</h2>
<p>上面留了一个坑，回调函数的第二个参数 <code>IntersectionObserver</code> 观察器实例对象都有什么呢？</p>
<p>我们把实例对象打印出来看一下</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">(<span class="hljs-params">doc</span>) =></span> &#123;
  <span class="hljs-comment">//回调函数</span>
  <span class="hljs-keyword">const</span> callback = <span class="hljs-function">() =></span> &#123;&#125;;
  <span class="hljs-comment">//配置对象</span>
  <span class="hljs-keyword">const</span> options = &#123;&#125;;
  <span class="hljs-comment">//创建观察器</span>
  <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
  <span class="hljs-comment">//获取目标元素</span>
  <span class="hljs-keyword">const</span> target = doc.querySelector(<span class="hljs-string">".target"</span>)
  <span class="hljs-comment">//开始监听目标元素</span>
  myObserver.observe(target);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ myObserver:'</span>, myObserver);
&#125;)(<span class="hljs-built_in">document</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cec6edce1c34f29af6f1f456b510acf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，我们的观察器实例上面包含如下属性</p>
<ul>
<li><strong>root</strong></li>
<li><strong>rootMargin</strong></li>
<li><strong>thresholds</strong></li>
<li><strong>trackVisibility</strong></li>
<li><strong>delay</strong></li>
</ul>
<p>是不是特别眼熟，没错，就是我们创建观察者实例的时候，传入的 <code>options</code> 对象，只不过 <code>options</code> 对象是可选的，观察器实例的属性就使用我们传入的 <code>options</code> 对象，如果没传就使用默认值，唯一不同的是，<code>options</code>  中 的属性 <code>threshold</code> 是单数，而我们实例获取到的 <code>thresholds</code> 是复数。</p>
<p>值得注意的是，这里的所有属性都是 <strong>只读</strong> 的，也就是说一旦观察器被创建，则 <strong>无法</strong> 更改其配置，所以一个给定的观察者对象只能用来监听可见区域的特定变化值。</p>
<p>接下来我们就通过代码结合动图演示一下这些属性</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">(<span class="hljs-params">doc</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>
  <span class="hljs-comment">//获取目标元素</span>
  <span class="hljs-keyword">const</span> target = doc.querySelector(<span class="hljs-string">".target"</span>)
  <span class="hljs-comment">//获取根元素</span>
  <span class="hljs-keyword">const</span> root = doc.querySelector(<span class="hljs-string">".out-container"</span>)
  <span class="hljs-comment">//回调函数</span>
  <span class="hljs-keyword">const</span> callback = <span class="hljs-function">(<span class="hljs-params">entries, observer</span>) =></span> &#123;
    n++
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀~ 执行了 <span class="hljs-subst">$&#123;n&#125;</span> 次callback`</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ entries:'</span>, entries);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ observer:'</span>, observer);
  &#125;;
  <span class="hljs-comment">//配置对象</span>
  <span class="hljs-keyword">const</span> options = &#123;
    <span class="hljs-attr">root</span>: root,
    <span class="hljs-attr">rootMargin</span>: <span class="hljs-string">'0px 0px 0px 0px'</span>,
    <span class="hljs-attr">threshold</span>: [<span class="hljs-number">0.5</span>],
    <span class="hljs-attr">trackVisibility</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">delay</span>: <span class="hljs-number">100</span>
  &#125;;
  <span class="hljs-comment">//创建观察器</span>
  <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
  <span class="hljs-comment">//开始监听目标元素</span>
  myObserver.observe(target);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ myObserver:'</span>, myObserver);
&#125;)(<span class="hljs-built_in">document</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>root</strong></p>
<p>这个没什么说的，就是设置指定节点为根元素</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2d29653c60442acb25ecaec40938d2d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>rootMargin</strong></p>
<p>我们把 <code>rootMargin</code> 修改为  <code>'50px 50px 50px 50px'</code>，可以看到，我们的目标元素还没有露出来的时候回调函数就已经执行了，也就是说目标元素距离根元素还有 <code>50px</code> 的 <code>margin</code> 时，观察器就认为是发生了交叉。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7af428f23f6b498799ac682078d3947f~tplv-k3u1fbpfcp-watermark.image" alt="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>thresholds</strong></p>
<p>我们把 <code>threshold</code> 修改为 <code> [0.1, 0.3, 0.5, 0.8, 1]</code>,可以看到，回调函数触发了多次，也就是说当交叉区域的百分比，每达到指定的阈值时都会触发一次回调函数。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb18580104924eea93ea08909aaff2b6~tplv-k3u1fbpfcp-watermark.image" alt="7.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意 <code>Intersection Observer API</code> 无法提供重叠的像素个数或者具体哪个像素重叠，他的更常见的使用方式是——当两个元素相交比例在 <code>N%</code> 左右时，触发回调，以执行某些逻辑。 -- MDN</p>
</blockquote>
<p><strong>trackVisibility</strong></p>
<p>修改 <code>trackVisibility</code> 为 <code>true</code> ，可以看到， <code>isVisible</code> 属性值为 <code>true</code> 。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e06f622665b34cae9a837a383e261176~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改 <code>css</code> 属性 为 <code>opacity: 0</code>，可以看到，虽然我们蓝色小方块并没有出现在视图中，但是回调函数已经执行了，并且 <code>isVisible</code> 属性值为 <code>false</code> 而 <code>isIntersecting</code> 值为 <code>true</code> 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40f55b63594848ca95893aba9c96d93f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>delay</strong></p>
<p>回调函数延迟触发，我们修改 <code>delay</code> 为 <code>3000</code>，可以看到 <code>log</code> 是 <code>3000ms</code> 以后才输出的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88334810497e46819caaf9a8e2f961e5~tplv-k3u1fbpfcp-watermark.image" alt="8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">观察器实例方法</h2>
<p>通过此段代码来演示观察器实例方法，为了方便演示，我添加了几个对应的按钮。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">(<span class="hljs-params">doc</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> n = <span class="hljs-number">0</span>
  <span class="hljs-comment">//获取目标元素</span>
  <span class="hljs-keyword">const</span> target1 = doc.querySelector(<span class="hljs-string">".target1"</span>)
  <span class="hljs-keyword">const</span> target2 = doc.querySelector(<span class="hljs-string">".target2"</span>)
  <span class="hljs-comment">//添加几个按钮方便操作</span>
  <span class="hljs-keyword">const</span> observe = doc.querySelector(<span class="hljs-string">".observe"</span>)
  <span class="hljs-keyword">const</span> unobserve = doc.querySelector(<span class="hljs-string">".unobserve"</span>)
  <span class="hljs-keyword">const</span> disconnect = doc.querySelector(<span class="hljs-string">".disconnect"</span>)
  observe.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> myObserver.observe(target1))
  unobserve.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> myObserver.unobserve(target1))
  disconnect.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> myObserver.disconnect())
  <span class="hljs-comment">//获取根元素</span>
  <span class="hljs-keyword">const</span> root = doc.querySelector(<span class="hljs-string">".out-container"</span>)
  <span class="hljs-comment">//回调函数</span>
  <span class="hljs-keyword">const</span> callback = <span class="hljs-function">(<span class="hljs-params">entries, observer</span>) =></span> &#123;
    n++
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀~ 执行了 <span class="hljs-subst">$&#123;n&#125;</span> 次callback`</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ entries:'</span>, entries);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ observer:'</span>, observer);
  &#125;;
  <span class="hljs-comment">//配置对象</span>
  <span class="hljs-keyword">const</span> options = &#123;
    <span class="hljs-attr">root</span>: root,
    <span class="hljs-attr">rootMargin</span>: <span class="hljs-string">'0px 0px 0px 0px'</span>,
    <span class="hljs-attr">threshold</span>: [<span class="hljs-number">0.1</span>, <span class="hljs-number">0.2</span>, <span class="hljs-number">0.3</span>, <span class="hljs-number">0.5</span>],
    <span class="hljs-attr">trackVisibility</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">delay</span>: <span class="hljs-number">100</span>
  &#125;;
  <span class="hljs-comment">//创建观察器</span>
  <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
  <span class="hljs-comment">//开始监听目标元素</span>
  myObserver.observe(target2);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ myObserver:'</span>, myObserver);
&#125;)(<span class="hljs-built_in">document</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">observe</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
 myObserver.observe(target);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接受一个目标元素作为参数。很好理解，当我们创建完观察器实例后，要手动的调用 <code>observe</code> 方法来通知它开始监测目标元素。</p>
<p><strong>可以在同一个观察者对象中配置监听多个目标元素</strong></p>
<p><code>target2</code> 元素是通过代码自动监测的，而 <code>target1</code> 则是我们在点击了 <code>observe</code> 按钮之后开始监测的。通过动图可以看到，当我单击 <code>observe</code> 按钮后，我们的 <code>entries</code> 数组里面就包含了两条数据，前文中说到，可以通过 <code>target</code> 属性来判断是哪个目标元素。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6600819737546359ea5568e435b11f7~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">unobserve</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
 myObserver.observe(target);
 myObserver.unobserve(target)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接收一个目标元素作为参数，当我们不想监听某个元素的时候，需要手动调用 <code>unobserve</code> 方法来停止监听指定目标元素。通过动图可以发现，当我们点击 <code>unobserve</code> 按钮后，由两条数据变成了一条数据，说明 <code>target1</code> 已经不再接受监测了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b937096b1847478c8ff462093bd17450~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">disconnect</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
 myObserver.disconnect()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们不想监测任何一个目标元素时，我们需要手动调用 <code>disconnect</code> 方法停止监听工作。通过动图可以看到，当我们点击 <code>disconnect</code> 按钮后，控制台不再输出 <code>log</code> ，说明监听工作已经停止，可以通过 <code>observe</code> 再次开启监听工作。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd460be53fdd40999958dfa39eca28b0~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">takeRecords</h3>
<p>返回所有观察目标的 <code>IntersectionObserverEntry</code> 对象数组，应用场景较少。</p>
<p>当观察到交互动作发生时，回调函数并不会立即执行，而是在空闲时期使用 <code>requestIdleCallback</code> 来异步执行回调函数，但是也提供了同步调用的 <code>takeRecords</code> 方法。</p>
<p>如果异步的回调先执行了，那么当我们调用同步的 <code>takeRecords</code> 方法时会返回空数组。同理，如果已经通过 <code>takeRecords</code> 获取了所有的观察者实例，那么回调函数就不会被执行了。</p>
<h1 data-id="heading-14">注意事项</h1>
<h2 data-id="heading-15">构造函数 IntersectionObserver 配置的回调函数都在哪些情况下被调用?</h2>
<p>构造函数 <code>IntersectionObserver</code> 配置的回调函数，在以下情况发生时可能会被调用</p>
<ul>
<li>当目标（<strong>target</strong>）元素与根（<strong>root</strong>）元素发生交集的时候执行。</li>
<li>两个元素的相交部分大小发生变化时。</li>
<li><code>Observer</code> 第一次监听目标元素的时候。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function">(<span class="hljs-params">doc</span>) =></span> &#123;
  <span class="hljs-comment">//回调函数</span>
  <span class="hljs-keyword">const</span> callback = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ 执行了一次callback'</span>);
  &#125;;
  <span class="hljs-comment">//配置对象</span>
  <span class="hljs-keyword">const</span> options = &#123;&#125;;
  <span class="hljs-comment">//观察器实例</span>
  <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options);
  <span class="hljs-comment">//目标元素</span>
  <span class="hljs-keyword">const</span> target = doc.querySelector(<span class="hljs-string">"#target"</span>)
  <span class="hljs-comment">//开始观察</span>
  myObserver.observe(target);
&#125;)(<span class="hljs-built_in">document</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，无论目标元素是否与根元素相交，当我们第一次监听目标元素的时候，回调函数都会触发一次，所以不要直接在回调函数里写逻辑代码，尽量通过 <code>isIntersecting</code> 或者 <code>intersectionRect</code> 进行判断之后再执行逻辑代码。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0530b83fcbaf4371809135c1d96f9ae2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">页面的可见性如何监测</h2>
<p>页面的可见性可以通过<code>document.visibilityState</code>或者<code>document.hidden</code>获得。</p>
<p>页面可见性的变化可以通过<code>document.visibilitychange</code>来监听。</p>
<h2 data-id="heading-17">可见性和交叉观察</h2>
<p>当 <code>css</code> 设置了<code>opacity: 0</code>，<code>visibility: hidden</code> 以及 <code>用其他的元素覆盖目标元素</code> ，都不会影响交叉观察器的监测，也就是都不会影响 <code>isIntersecting</code> 属性的结果，但是会影响 <code>isVisible</code> 属性的结果， 如果元素设置了 <code>display：none</code> 就不会被检测了。当然影响元素可视性的属性不止上述这些，还包括<code>position</code>，<code>margin</code>，<code>clip</code> 等等等等...就靠小伙伴们自行发掘了</p>
<h2 data-id="heading-18">交集的计算</h2>
<p>所有区域均被 <code>Intersection Observer API</code> 当做一个 <strong>矩形</strong> 看待。如果元素是不规则的图形也将会被看成一个包含元素所有区域的最小矩形，相似的，如果元素发生的交集部分不是一个矩形，那么也会被看作是一个包含他所有交集区域的最小矩形。</p>
<h2 data-id="heading-19">我怎么知道目标元素来自视口的上方还是下方</h2>
<p>目标元素滚动的方向也是可以判断的，原理是根元素的 <code>entry.rootBounds.y</code> 是固定不变的 ，所以我们只需要计算 <code>entry.boundingClientRect.y</code> 与 <code>entry.rootBounds.y</code> 的大小，当回调函数触发的时候，我们记录下当时的位置，如果 <code>entry.boundingClientRect.y < entry.rootBounds.y</code>，说明是在视口下方，那么当下一次目标元素可见的时候，我们就知道目标元素时来自视口下方的，反之亦然。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> wasAbove = <span class="hljs-literal">false</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callback</span>(<span class="hljs-params">entries, observer</span>) </span>&#123;
    entries.forEach(<span class="hljs-function"><span class="hljs-params">entry</span> =></span> &#123;
        <span class="hljs-keyword">const</span> isAbove = entry.boundingClientRect.y < entry.rootBounds.y;
        <span class="hljs-keyword">if</span> (entry.isIntersecting) &#123;
            <span class="hljs-keyword">if</span> (wasAbove) &#123;
                <span class="hljs-comment">// Comes from top</span>
            &#125;
        &#125;
        wasAbove = isAbove;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">应用场景</h1>
<p>介绍完基础知识，总得来几个实例(<strong>演示代码采用VUE3.0</strong>)，当然实际场景要比这复杂的多，如何在自己的工作学习中应用，还是要靠小伙伴们多多开动聪明的大脑~</p>
<h2 data-id="heading-21">数据列表无限滚动</h2>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>
         <span class="hljs-attr">v-for</span>=<span class="hljs-string">'item in list'</span>
         <span class="hljs-attr">:key</span>=<span class="hljs-string">'item'</span>></span>内容区域&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"reference"</span>
         <span class="hljs-attr">ref</span>=<span class="hljs-string">'reference'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'ts'</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, onMounted, reactive, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> reference = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> list = reactive([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>, <span class="hljs-number">10</span>])
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> n = <span class="hljs-number">10</span>
      <span class="hljs-comment">//回调函数</span>
      <span class="hljs-keyword">const</span> callback = <span class="hljs-function">(<span class="hljs-params">entries</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> myEntry = entries[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">if</span> (myEntry.isIntersecting) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀🚀~ 触发了无线滚动,开始模拟请求数据 <span class="hljs-subst">$&#123;n&#125;</span>`</span>)
          n++
          list.push(n)
        &#125;
      &#125;
      <span class="hljs-comment">//配置对象</span>
      <span class="hljs-keyword">const</span> options = &#123;
        <span class="hljs-attr">root</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">rootMargin</span>: <span class="hljs-string">'0px 0px 0px 0px'</span>,
        <span class="hljs-attr">threshold</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>],
        <span class="hljs-attr">trackVisibility</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">delay</span>: <span class="hljs-number">100</span>,
      &#125;
      <span class="hljs-comment">//观察器实例</span>
      <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options)
      <span class="hljs-comment">//开始观察</span>
      myObserver.observe(reference.value)
    &#125;)

    <span class="hljs-keyword">return</span> &#123; reference, list &#125;
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
* &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;
<span class="hljs-selector-class">.reference</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">visibility</span>: hidden;
&#125;
<span class="hljs-selector-class">.vbody</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">background-color</span>: red;
  <span class="hljs-attribute">color</span>: aliceblue;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们只需要在底部添加一个参考元素，当参考元素可见时，就向后台请求数据，就可以实现无线滚动的效果了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb5dea8ef7894548921e589f7fcfdcd0~tplv-k3u1fbpfcp-watermark.image" alt="6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">图片预加载</h2>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>
         <span class="hljs-attr">ref</span>=<span class="hljs-string">'header'</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"url"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'ts'</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, onMounted, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> header = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> url = ref(<span class="hljs-string">''</span>)
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">//回调函数</span>
      <span class="hljs-keyword">const</span> callback = <span class="hljs-function">(<span class="hljs-params">entries</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> myEntry = entries[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">if</span> (myEntry.isIntersecting) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ 预加载图片开始'</span>)
          url.value =
            <span class="hljs-string">'//img10.360buyimg.com/imgzone/jfs/t1/197235/15/2956/67824/6115e076Ede17a418/d1350d4d5e52ef50.jpg'</span>
        &#125;
      &#125;
      <span class="hljs-comment">//配置对象</span>
      <span class="hljs-keyword">const</span> options = &#123;
        <span class="hljs-attr">root</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">rootMargin</span>: <span class="hljs-string">'200px 200px 200px 200px'</span>,
        <span class="hljs-attr">threshold</span>: [<span class="hljs-number">0</span>],
        <span class="hljs-attr">trackVisibility</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">delay</span>: <span class="hljs-number">100</span>,
      &#125;
      <span class="hljs-comment">//观察器实例</span>
      <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options)
      <span class="hljs-comment">//开始观察</span>
      myObserver.observe(header.value)
    &#125;)

    <span class="hljs-keyword">return</span> &#123; header, url &#125;
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
* &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;
<span class="hljs-selector-class">.box</span> &#123;
&#125;
<span class="hljs-selector-class">.header</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
  <span class="hljs-attribute">background-color</span>: blue;
  <span class="hljs-attribute">color</span>: aliceblue;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">400px</span>;
&#125;
<span class="hljs-selector-class">.header</span> <span class="hljs-selector-tag">img</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="hljs-selector-class">.reference</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">visibility</span>: hidden;
&#125;
<span class="hljs-selector-class">.vbody</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">800px</span>;
  <span class="hljs-attribute">background-color</span>: red;
  <span class="hljs-attribute">color</span>: aliceblue;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">800px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用 <code>options</code> 的 <code>rootMargin</code>属性，可以在图片即将进入可视区域的时间进行图片的加载，即避免了提前请求大量图片造成的性能问题，也避免了图片进入窗口才加载已经来不及的问题。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d9ff670b6794e9e8dd5d88ac892b5f8~tplv-k3u1fbpfcp-watermark.image" alt="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">吸顶</h2>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"reference"</span>
         <span class="hljs-attr">ref</span>=<span class="hljs-string">'reference'</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>
         <span class="hljs-attr">ref</span>=<span class="hljs-string">'header'</span>></span>吸顶区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'ts'</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, onMounted, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> header = ref(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> reference = ref(<span class="hljs-literal">null</span>)

    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">//回调函数</span>
      <span class="hljs-keyword">const</span> callback = <span class="hljs-function">(<span class="hljs-params">entries</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> myEntry = entries[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">if</span> (!myEntry.isIntersecting) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ 触发了吸顶'</span>)
          header.value.style.position = <span class="hljs-string">'fixed'</span>
          header.value.style.top = <span class="hljs-string">'0px'</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ 取消吸顶'</span>)
          header.value.style.position = <span class="hljs-string">'relative'</span>
        &#125;
      &#125;
      <span class="hljs-comment">//配置对象</span>
      <span class="hljs-keyword">const</span> options = &#123;
        <span class="hljs-attr">root</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">rootMargin</span>: <span class="hljs-string">'0px 0px 0px 0px'</span>,
        <span class="hljs-attr">threshold</span>: [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>],
        <span class="hljs-attr">trackVisibility</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">delay</span>: <span class="hljs-number">100</span>,
      &#125;
      <span class="hljs-comment">//观察器实例</span>
      <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options)
      <span class="hljs-comment">//开始观察</span>
      myObserver.observe(reference.value)
    &#125;)

    <span class="hljs-keyword">return</span> &#123; reference, header &#125;
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
* &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;
<span class="hljs-selector-class">.header</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background-color</span>: blue;
  <span class="hljs-attribute">color</span>: aliceblue;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-class">.reference</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">visibility</span>: hidden;
&#125;
<span class="hljs-selector-class">.vbody</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">800px</span>;
  <span class="hljs-attribute">background-color</span>: red;
  <span class="hljs-attribute">color</span>: aliceblue;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">800px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>思路就是利用一个参考元素作为交叉观察器观察的对象，当参考元素可见的时候，取消吸顶区域的 <code>fixed</code> 属性，否则添加 <code>fixed</code> 属性，吸底稍微复杂一点，但是道理差不多，留给小伙伴们自行研究吧 ~ ~。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5f081e082a64bc3917aeef3995ba54d~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-24">埋点上报</h2>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"header"</span>
         <span class="hljs-attr">ref</span>=<span class="hljs-string">'header'</span>></span>埋点区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vbody"</span>></span>内容区域<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">'ts'</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, onMounted, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> header = ref(<span class="hljs-literal">null</span>)

    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">//回调函数</span>
      <span class="hljs-keyword">const</span> callback = <span class="hljs-function">(<span class="hljs-params">entries</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> myEntry = entries[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">if</span> (myEntry.isIntersecting) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🚀🚀~ 触发了埋点'</span>)
        &#125;
      &#125;
      <span class="hljs-comment">//配置对象</span>
      <span class="hljs-keyword">const</span> options = &#123;
        <span class="hljs-attr">root</span>: <span class="hljs-literal">null</span>,
        <span class="hljs-attr">rootMargin</span>: <span class="hljs-string">'0px 0px 0px 0px'</span>,
        <span class="hljs-attr">threshold</span>: [<span class="hljs-number">0.5</span>],
        <span class="hljs-attr">trackVisibility</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">delay</span>: <span class="hljs-number">100</span>,
      &#125;
      <span class="hljs-comment">//观察器实例</span>
      <span class="hljs-keyword">const</span> myObserver = <span class="hljs-keyword">new</span> IntersectionObserver(callback, options)
      <span class="hljs-comment">//开始观察</span>
      myObserver.observe(header.value)
    &#125;)

    <span class="hljs-keyword">return</span> &#123; header &#125;
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
* &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;
<span class="hljs-selector-class">.header</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
  <span class="hljs-attribute">background-color</span>: blue;
  <span class="hljs-attribute">color</span>: aliceblue;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">400px</span>;
&#125;
<span class="hljs-selector-class">.vbody</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">800px</span>;
  <span class="hljs-attribute">background-color</span>: red;
  <span class="hljs-attribute">color</span>: aliceblue;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">40px</span>;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">800px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span> <span class="hljs-number">0</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常情况下，我们统计一个元素是否被用户有效的看到，并不是元素刚出现就触发埋点，而是元素进入可是区域一定比例才可以，我们可以配置 <code>options</code> 的 <code>threshold</code> 为 <code>0.5</code>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e785b93efa0452b89b2fbf2ebb95f93~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-25">等等等等。。。。</h2>
<p>这个 <code>api</code> 可以说是非常强大了，可玩性也是极高，大家自由发挥 ~ ~</p>
<h1 data-id="heading-26">兼容性</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8df21141281f4f85991ba0e575db9013~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b54a3d22998454ebde6980b215c6c0f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么有两张兼容性的图呢？因为 <strong>trackVisibility</strong> 和 <strong>delay</strong> 两个属性是属于
<code>IntersectionObserver V2</code> 的。所以小伙伴们在用的时候一定要注意兼容性。</p>
<p>当然也有兼容解决方案，那就是</p>
<p>👉👉 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fintersection-observer-polyfill" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/intersection-observer-polyfill" ref="nofollow noopener noreferrer">intersection-observer-polyfill</a></p>
<h1 data-id="heading-27">参考</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%3Fsearch%3DIntersectionObserver%2520" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/?search=IntersectionObserver%20" ref="nofollow noopener noreferrer">Can I Use</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FIntersectionObserver" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/IntersectionObserver" ref="nofollow noopener noreferrer">MDN Intersection Observer</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2016%2F11%2Fintersectionobserver_api.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2016/11/intersectionobserver_api.html" ref="nofollow noopener noreferrer">IntersectionObserver API 使用教程</a></p></div>  
</div>
            