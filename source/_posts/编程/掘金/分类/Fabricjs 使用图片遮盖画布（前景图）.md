
---
title: 'Fabric.js 使用图片遮盖画布（前景图）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e3fc21281d94bcb831ea02b91ceb78d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 15:32:25 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e3fc21281d94bcb831ea02b91ceb78d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第16篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<hr>
<h1 data-id="heading-0">本文简介</h1>
<p><strong>点赞 + 关注 + 收藏 = 学会了</strong></p>
<br>
<p>在 <a href="https://juejin.cn/post/7141548864573538318" target="_blank" title="https://juejin.cn/post/7141548864573538318">《Fabric.js 使用纯色遮挡画布（前景色）》</a> 中讲到使用纯色的方式遮盖画布。如果你的常见需要使用图片来遮盖的话，<code>fabric.js</code> 也提供了相应的属性来配置。</p>
<p>相比起使用纯色遮盖画布，使用图片会更复杂。</p>
<p>因为图片本身是有尺寸大小的，所以可能会遇到缩放画布、平移画布等操作。</p>
<p>而纯色的话就不需要管色块的尺寸，移动到哪，怎么缩放都是全屏（整个画布）纯色。</p>
<br>
<br>
<h1 data-id="heading-1">使用图片覆盖画布</h1>
<p>如果需要用图片遮盖画布，可以设置 <code>canvas</code> 的 <code>overlayImage</code> 属性，传入的值就是图片地址。</p>
<p>可以使用网图，也可以使用本地图片。和 <code>backgroundImage</code> 的用法差不多。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e3fc21281d94bcb831ea02b91ceb78d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvasBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> canvas = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Canvas</span>(<span class="hljs-string">'canvasBox'</span>, &#123;
    <span class="hljs-comment">// 覆盖图像</span>
    <span class="hljs-attr">overlayImage</span>: <span class="hljs-string">'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27d1b4e5f8824198b6d51a2b1c2d0d75~tplv-k3u1fbpfcp-zoom-crop-mark:400:400:400:400.awebp'</span>,
    <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'red'</span>, <span class="hljs-comment">// 背景色</span>
  &#125;)

  <span class="hljs-comment">// 元素也会被 overlayColor 覆盖</span>
  <span class="hljs-keyword">let</span> rect = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Rect</span>(&#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">80</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">80</span>,
  &#125;)

  canvas.<span class="hljs-title function_">add</span>(rect)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中，原本应该有一个矩形在画布上的，而且背景色也应该是红色。</p>
<p>但设置了 <code>overlayImage</code> ，所以整个画布都被图片覆盖了。</p>
<br>
<p><code>overlayImage</code> 和 <code>overlayColor</code> 一样，都可以将画布上的所有元素覆盖掉，比如背景图、背景色、图形等元素。</p>
<br>
<br>
<h1 data-id="heading-2">覆盖图像不受视口变换的影响</h1>
<p>由于图片是有尺寸的，如果你的场景中，画布可以缩放或者被拖拽，就会出现下图的效果。</p>
<p>覆盖的图片被缩小或者移动后，就露出了背景色（红色）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a17e96e8bc842be87322b88d0eb29ca~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="02.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<p>如果不希望覆盖图被缩放和平移等操作影响（不受视口变换的影响），可以将 <code>overlayVpt</code> 设为 <code>false</code> 。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bceeb85c783f471dbfcaac2324cadb21~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="03.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvasBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> canvas = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Canvas</span>(<span class="hljs-string">'canvasBox'</span>, &#123;
    <span class="hljs-comment">// 覆盖图像</span>
    <span class="hljs-attr">overlayImage</span>: <span class="hljs-string">'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27d1b4e5f8824198b6d51a2b1c2d0d75~tplv-k3u1fbpfcp-zoom-crop-mark:400:400:400:400.awebp'</span>,
    <span class="hljs-attr">overlayVpt</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 如果设置为假覆盖图像不受视口变换的影响</span>
    <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">'red'</span>, <span class="hljs-comment">// 背景色</span>
  &#125;)

  <span class="hljs-comment">// 元素也会被 overlayColor 覆盖</span>
  <span class="hljs-keyword">let</span> rect = <span class="hljs-keyword">new</span> fabric.<span class="hljs-title class_">Rect</span>(&#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">80</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">80</span>,
  &#125;)
  
  canvas.<span class="hljs-title function_">add</span>(rect)

  <span class="hljs-comment">// 通过鼠标滚轮缩放画布</span>
  canvas.<span class="hljs-title function_">on</span>(<span class="hljs-string">'mouse:wheel'</span>, <span class="hljs-function"><span class="hljs-params">opt</span> =></span> &#123;
    <span class="hljs-keyword">const</span> delta = opt.<span class="hljs-property">e</span>.<span class="hljs-property">deltaY</span> <span class="hljs-comment">// 滚轮，向上滚一下是 -100，向下滚一下是 100</span>
    <span class="hljs-keyword">let</span> zoom = canvas.<span class="hljs-title function_">getZoom</span>() <span class="hljs-comment">// 获取画布当前缩放值</span>
    zoom *= <span class="hljs-number">0.999</span> ** delta
    <span class="hljs-keyword">if</span> (zoom > <span class="hljs-number">20</span>) zoom = <span class="hljs-number">20</span>
    <span class="hljs-keyword">if</span> (zoom < <span class="hljs-number">0.01</span>) zoom = <span class="hljs-number">0.01</span>
    canvas.<span class="hljs-title function_">zoomToPoint</span>(
      &#123; <span class="hljs-comment">// 关键点</span>
        <span class="hljs-attr">x</span>: opt.<span class="hljs-property">e</span>.<span class="hljs-property">offsetX</span>,
        <span class="hljs-attr">y</span>: opt.<span class="hljs-property">e</span>.<span class="hljs-property">offsetY</span>
      &#125;,
      zoom
    )
    opt.<span class="hljs-property">e</span>.<span class="hljs-title function_">preventDefault</span>()
    opt.<span class="hljs-property">e</span>.<span class="hljs-title function_">stopPropagation</span>()
  &#125;)


  <span class="hljs-comment">// 鼠标拖拽画布</span>
  canvas.<span class="hljs-title function_">on</span>(<span class="hljs-string">'mouse:down'</span>, <span class="hljs-function"><span class="hljs-params">opt</span> =></span> &#123; <span class="hljs-comment">// 鼠标按下时触发</span>
    <span class="hljs-keyword">let</span> evt = opt.<span class="hljs-property">e</span>
    canvas.<span class="hljs-property">isDragging</span> = <span class="hljs-literal">true</span> <span class="hljs-comment">// isDragging 是自定义的</span>
    canvas.<span class="hljs-property">lastPosX</span> = evt.<span class="hljs-property">clientX</span> <span class="hljs-comment">// lastPosX 是自定义的</span>
    canvas.<span class="hljs-property">lastPosY</span> = evt.<span class="hljs-property">clientY</span> <span class="hljs-comment">// lastPosY 是自定义的</span>
  &#125;)

  canvas.<span class="hljs-title function_">on</span>(<span class="hljs-string">'mouse:move'</span>, <span class="hljs-function"><span class="hljs-params">opt</span> =></span> &#123; <span class="hljs-comment">// 鼠标移动时触发</span>
    <span class="hljs-keyword">if</span> (canvas.<span class="hljs-property">isDragging</span>) &#123;
      <span class="hljs-keyword">let</span> evt = opt.<span class="hljs-property">e</span>
      <span class="hljs-keyword">let</span> vpt = canvas.<span class="hljs-property">viewportTransform</span> <span class="hljs-comment">// 聚焦视图的转换</span>
      vpt[<span class="hljs-number">4</span>] += evt.<span class="hljs-property">clientX</span> - canvas.<span class="hljs-property">lastPosX</span>
      vpt[<span class="hljs-number">5</span>] += evt.<span class="hljs-property">clientY</span> - canvas.<span class="hljs-property">lastPosY</span>
      canvas.<span class="hljs-title function_">requestRenderAll</span>()
      canvas.<span class="hljs-property">lastPosX</span> = evt.<span class="hljs-property">clientX</span>
      canvas.<span class="hljs-property">lastPosY</span> = evt.<span class="hljs-property">clientY</span>
    &#125;
  &#125;)

  canvas.<span class="hljs-title function_">on</span>(<span class="hljs-string">'mouse:up'</span>, <span class="hljs-function"><span class="hljs-params">opt</span> =></span> &#123; <span class="hljs-comment">// 鼠标松开时触发</span>
    canvas.<span class="hljs-title function_">setViewportTransform</span>(canvas.<span class="hljs-property">viewportTransform</span>) <span class="hljs-comment">// 设置此画布实例的视口转换  </span>
    canvas.<span class="hljs-property">isDragging</span> = <span class="hljs-literal">false</span>
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>感觉这和 <a href="https://juejin.cn/post/7105789686395699230" target="_blank" title="https://juejin.cn/post/7105789686395699230">《Fabric.js 锁定背景图，不受缩放和拖拽的影响》</a> 里讲到的有点像，对吧~</p>
<p>所以当看到 <code>fabric.js</code> 的相关属性和方法名称里出现 <code>Vpt</code> ，大概率就和 <strong>视口</strong> 有关。</p>
<br>
<br>
<h1 data-id="heading-3">更灵活的操作方法  setOverlayImage</h1>
<p>使用 <code>setOverlayImage</code> 支持更多配置。</p>
<p><code>setOverlayImage(image, callback, optionsopt)</code>  接收3个参数</p>
<ul>
<li><code>image</code>:  图像实例或者URL</li>
<li><code>callback</code>: 回调函数（主要是设置完后刷新画布）</li>
<li><code>optionsopt</code>: 这是可选项，不填也没事。填了就可以设置图像的配置。</li>
</ul>
<br>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83496cba422641cb886e7458d5bce0f7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 省略部分代码</span>

canvas.<span class="hljs-title function_">setOverlayImage</span>(
  <span class="hljs-string">'../../images/bg4.png'</span>,
  canvas.<span class="hljs-property">renderAll</span>.<span class="hljs-title function_">bind</span>(canvas),
  &#123;
    <span class="hljs-attr">originX</span>: <span class="hljs-string">'left'</span>,
    <span class="hljs-attr">originY</span>: <span class="hljs-string">'top'</span>
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了设置 <code>originX</code> 和 <code>originY</code> 外，还可以设置 <code>top</code>、<code>left</code>、<code>opacity</code>、<code>angle</code> 等参数。</p>
<p>更多用法可以查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fk21vin%2Ffabricjs-demo%2Fblob%2Fmaster%2Ftutorial%2FCanvas%2FsetOverlayImage.html" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/k21vin/fabricjs-demo/blob/master/tutorial/Canvas/setOverlayImage.html" ref="nofollow noopener noreferrer">代码仓库</a>。</p>
<br>
<br>
<h1 data-id="heading-4">代码仓库</h1>
<p>⭐<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fk21vin%2Ffabricjs-demo%2Fblob%2Fmaster%2Ftutorial%2FCanvas%2FoverlayImage%26overlayVpt.html" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/k21vin/fabricjs-demo/blob/master/tutorial/Canvas/overlayImage&overlayVpt.html" ref="nofollow noopener noreferrer">overlayImage 和 overlayVpt</a></p>
<p>⭐<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fk21vin%2Ffabricjs-demo%2Fblob%2Fmaster%2Ftutorial%2FCanvas%2FsetOverlayImage.html" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/k21vin/fabricjs-demo/blob/master/tutorial/Canvas/setOverlayImage.html" ref="nofollow noopener noreferrer">setOverlayImage</a></p>
<br>
<br>
<h1 data-id="heading-5">推荐阅读</h1>
<p>👍<a href="https://juejin.cn/post/7026941253845516324" target="_blank" title="https://juejin.cn/post/7026941253845516324">《Fabric.js 从入门到_ _ _ _ _ _》</a></p>
<p>👍<a href="https://juejin.cn/post/7111191499932434439" target="_blank" title="https://juejin.cn/post/7111191499932434439">《Fabric.js 控制元素层级》</a></p>
<p>👍<a href="https://juejin.cn/post/7108489281764589604" target="_blank" title="https://juejin.cn/post/7108489281764589604">《Fabric.js 上划线、中划线（删除线）、下划线》</a></p>
<p>👍<a href="https://juejin.cn/post/7107000176283222047" target="_blank" title="https://juejin.cn/post/7107000176283222047">《Fabric.js 激活输入框》</a></p>
<p>👍<a href="https://juejin.cn/post/7106159817361719304" target="_blank" title="https://juejin.cn/post/7106159817361719304">《Fabric.js 输出精简的JSON》</a></p>
<p>👍<a href="https://juejin.cn/post/7111733967488811022" target="_blank" title="https://juejin.cn/post/7111733967488811022">《Fabric.js IText 手动设置斜体》</a></p>
<br>
<p><strong>点赞 + 关注 + 收藏 = 学会了</strong></p></div>  
</div>
            