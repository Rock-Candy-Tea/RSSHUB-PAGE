
---
title: 'Fabric.js 设置容器类名要注意这几点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d02ac7468eab45f8924721f1acefac31~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 19:03:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d02ac7468eab45f8924721f1acefac31~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第15篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<hr>
<h1 data-id="heading-0">本文简介</h1>
<p><strong>点赞 + 关注 + 收藏 = 学会了</strong></p>
<br>
<p>用 <code>fabric.js</code> 创建画布时，<code>fabric.js</code> 会在 <code>canvas</code> 元素外包一层 <code>div</code> 容器。</p>
<p>如果想方便设置容器样式或者想通过 <code>js</code> 控制该容器，可以先给容器一个类名。</p>
<p>本文主要讲<strong>如何给包装容器设置类名</strong>和<strong>相关注意事项</strong>。</p>
<br>
<br>
<h1 data-id="heading-1">设置容器类名</h1>
<p>在使用 <code>fabric.js</code> 创建画布时就可以 <strong>通过 <code>containerClass</code> 设置包装容器的类名</strong>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvasBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 创建画布</span>
  <span class="hljs-keyword">let</span> canvas = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Canvas</span>(<span class="hljs-string">'c'</span>, &#123;
    <span class="hljs-attr">containerClass</span>: <span class="hljs-string">'ccc'</span>
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我这里随便命名，使用了 <code>ccc</code> 。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d02ac7468eab45f8924721f1acefac31~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时打开控制台就可以看到外层包装容器的类名是 <code>ccc</code> 。</p>
<br>
<p>可以再配合 <code>css</code> 设置一些样式。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa601279e9df4edc8d5f0d7ff9646a7f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.ccc</span> &#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid pink;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvasBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 创建画布</span>
  <span class="hljs-keyword">let</span> canvas = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Canvas</span>(<span class="hljs-string">'c'</span>, &#123;
    <span class="hljs-attr">containerClass</span>: <span class="hljs-string">'ccc'</span>
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>使用 <code>fabric.js</code> 的话，建议使用该方法设置包装容器的类名。</p>
<br>
<br>
<h1 data-id="heading-2">注意事项</h1>
<p>虽然设置包装容器类名很方便，但也存在一些注意事项。</p>
<br>
<h2 data-id="heading-3">容器有默认类名</h2>
<p>如果没使用 <code>containerClass</code> 设置包装容器类名，<code>fabric.js</code> 会将容器的类名设置为 <code>canvas-container</code> 。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1683321c9f6b4bb699c45eca1a7a4a43~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h2 data-id="heading-4">不建议用css设置宽高</h2>
<p>如果用 <code>css</code> 设置容器的宽高，还需要使用 <code>!important</code> 才会生效。因为 <code>fabric.js</code> 会将默认宽高绑定在元素的 <code>style</code> 上，变成内联样式。</p>
<p>但即使是使用 <code>!important</code> 提高样式权重，只会改变容器宽高，并不会改变画布宽高。所以还需要设置画布宽高。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c55824c261034dcd84cc86bf626611d8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.ccc</span> &#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid pink;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span> <span class="hljs-meta">!important</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span> <span class="hljs-meta">!important</span>;
  &#125;

  <span class="hljs-selector-class">.ccc</span> <span class="hljs-selector-tag">canvas</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span> <span class="hljs-meta">!important</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span> <span class="hljs-meta">!important</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvasBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> canvas = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Canvas</span>(<span class="hljs-string">'canvasBox'</span>, &#123;
    <span class="hljs-attr">containerClass</span>: <span class="hljs-string">'ccc'</span>
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>在 <code>canvas</code> 中不推荐使用 <code>css</code> 的方式设置画布宽高，因为这样做会导致画布内容变形。</p>
<br>
<p>比如我在画布中添加一个正方形，这么一操作就不是正方形了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ac12447e4ba49d98095b6c6104fedd8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.ccc</span> &#123;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid pink;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span> <span class="hljs-meta">!important</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span> <span class="hljs-meta">!important</span>;
  &#125;

  <span class="hljs-selector-class">.ccc</span> <span class="hljs-selector-tag">canvas</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span> <span class="hljs-meta">!important</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span> <span class="hljs-meta">!important</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvasBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> canvas = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Canvas</span>(<span class="hljs-string">'canvasBox'</span>, &#123;
    <span class="hljs-attr">containerClass</span>: <span class="hljs-string">'ccc'</span>
  &#125;)

  <span class="hljs-keyword">let</span> rect = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Rect</span>(&#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">top</span>: <span class="hljs-number">10</span>,
    <span class="hljs-attr">left</span>: <span class="hljs-number">10</span>
  &#125;)

  canvas.<span class="hljs-title function_">add</span>(rect)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>如需设置画布宽高，可参考 <a href="https://juejin.cn/post/7053049468601499684" target="_blank" title="https://juejin.cn/post/7053049468601499684">《Fabric.js 3个api设置画布宽高》</a></p>
<br>
<h2 data-id="heading-5">不建议设置容器定位模式</h2>
<p><code>fabric.js</code> 在初始化画布时，会将容器的 <code>position</code> 设置成 <code>relative</code>；</p>
<p>将里面的2个 <code>canvas</code> 元素的 <code>position</code> 设置成 <code>absolute</code> 。</p>
<p>没特殊需求的话，应该尊重 <code>fabric.js</code> 的这个设定。</p>
<br>
<h2 data-id="heading-6">不建议设置容器的padding</h2>
<p>如果只是设置了容器的 <code>padding</code> 其实没多大意义。</p>
<p>因为内部的两个 <code>canvas</code> 元素都使用了绝对定位 ( <code>relative</code> ) 的定位模式，所以这样操作没啥意义。</p>
<br>
<br>
<h1 data-id="heading-7">代码仓库</h1>
<p>⭐<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fk21vin%2Ffabricjs-demo%2Fblob%2Fmaster%2Ftutorial%2FCanvas%2FcontainerClass.html" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/k21vin/fabricjs-demo/blob/master/tutorial/Canvas/containerClass.html" ref="nofollow noopener noreferrer">Fabric.js 设置容器类名</a></p>
<br>
<br>
<h1 data-id="heading-8">推荐阅读</h1>
<p>👍<a href="https://juejin.cn/post/7026941253845516324" target="_blank" title="https://juejin.cn/post/7026941253845516324">《Fabric.js 从入门到_ _ _ _ _ _》</a></p>
<p>👍<a href="https://juejin.cn/post/7142313318290554911" target="_blank" title="https://juejin.cn/post/7142313318290554911">《Fabric.js 元素中心缩放》</a></p>
<p>👍<a href="https://juejin.cn/post/7142664492122374158" target="_blank" title="https://juejin.cn/post/7142664492122374158">《Fabric.js 变换视窗》</a></p>
<p>👍<a href="https://juejin.cn/post/7143062674954256391" target="_blank" title="https://juejin.cn/post/7143062674954256391">《Fabric.js 拖拽平移画布》</a></p>
<p>👍<a href="https://juejin.cn/post/7143401584494542879" target="_blank" title="https://juejin.cn/post/7143401584494542879">《Fabric.js 元素被遮挡的部分也可以操作》</a></p>
<p>👍<a href="https://juejin.cn/post/7143794070513516581" target="_blank" title="https://juejin.cn/post/7143794070513516581">《Fabric.js 自定义子类，创建属于自己的图形》</a></p>
<br>
<p><strong>点赞 + 关注 + 收藏 = 学会了</strong></p></div>  
</div>
            