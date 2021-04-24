
---
title: '通过canvas画板学习PointerEvent、MouseEvent和TouchEvent'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d630e4f49945168511dbdbb963516e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 20:03:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d630e4f49945168511dbdbb963516e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近想开发个草稿纸功能, 所以学习了下canvas实现简单的画板功能, 但是我们知道在PC端我们可以用MouseEvent来监听我们的鼠标点按相关操作, 移动端可以使用TouchEvent来监听我们手指触摸相关操作, 所以我们做画板的时候要想兼顾鼠标点按和手指触摸就得写两套逻辑. 但是别忘了, 还存在PointerEventer, 它可以监听鼠标, 手指触摸以及触摸笔, 支持多点触控, 它还有个特殊的参数, 即压感, 在压感屏上可以获取获取压感笔的压感值, 只要根据压感值, 我们可以控制笔画的粗细</p>
<h3 data-id="heading-0">1. PointerEvent、MouseEvent和TouchEvent相对应的事件</h3>



































<table><thead><tr><th>PointerEvent</th><th>MouseEvent</th><th>TouchEvent</th></tr></thead><tbody><tr><td>poninterdown</td><td>mousedown</td><td>touchstart</td></tr><tr><td>pointermove</td><td>mousemove</td><td>touchmove</td></tr><tr><td>pointerup</td><td>mouseup</td><td>touchend</td></tr><tr><td>pointerleave</td><td>mouseleave</td><td>-</td></tr><tr><td>pointercancel</td><td>-</td><td>touchcancel</td></tr></tbody></table>
<h3 data-id="heading-1">2. 做个画板</h3>
<h4 data-id="heading-2">1) 共用的部分</h4>
<p>先写出公共的画板部分代码, 后面只会写不同的事件监听部分代码</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">body</span> &#123;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
      <span class="hljs-attribute">overflow</span>: hidden;
    &#125;
    <span class="hljs-selector-class">.canvas-block</span> &#123;
      <span class="hljs-attribute">position</span>: relative;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    &#125;
    <span class="hljs-selector-id">#canvas</span> &#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-id">#canvas</span> &#123;
      <span class="hljs-attribute">z-index</span>: <span class="hljs-number">1</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"canvas-block"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"400"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>


  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'canvas'</span>)
    <span class="hljs-keyword">const</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>)
    <span class="hljs-keyword">let</span> width = canvas.width
    <span class="hljs-keyword">let</span> height = canvas.height
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.devicePixelRatio) &#123;
      canvas.style.width = width + <span class="hljs-string">'px'</span>
      canvas.style.height = height + <span class="hljs-string">'px'</span>
      canvas.height = height * <span class="hljs-built_in">window</span>.devicePixelRatio
      canvas.width = width * <span class="hljs-built_in">window</span>.devicePixelRatio
      ctx.scale(<span class="hljs-built_in">window</span>.devicePixelRatio, <span class="hljs-built_in">window</span>.devicePixelRatio)
    &#125;
    canvas.getContext(<span class="hljs-string">'2d'</span>).imageSmoothingEnabled = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">let</span> lineWidth = <span class="hljs-number">3</span>
    <span class="hljs-keyword">let</span> lineColor = <span class="hljs-string">'#fff'</span>
    <span class="hljs-keyword">let</span> painting = <span class="hljs-literal">false</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2) 使用MouseEvent监听事件</h3>
<blockquote>
<p><a href="https://codepen.io/klren0312/pen/BapMBvE" target="_blank" rel="nofollow noopener noreferrer">codepen.io/klren0312/p…</a></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 落笔</span>
 canvas.onmousedown = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
      painting = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">const</span> event = e || <span class="hljs-built_in">window</span>.event
      ctx.lineCap = <span class="hljs-string">'round'</span>
      ctx.lineJoin = <span class="hljs-string">'round'</span>
      <span class="hljs-keyword">const</span> x = event.offsetX
      <span class="hljs-keyword">const</span> y = event.offsetY
      ctx.beginPath()
      ctx.moveTo(x, y)
      ctx.lineWidth = lineWidth
      ctx.strokeStyle = lineColor
    &#125;
    <span class="hljs-comment">// 移动</span>
    canvas.onmousemove = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (!painting) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">const</span> event = e || <span class="hljs-built_in">window</span>.event
      <span class="hljs-keyword">const</span> x = event.offsetX
      <span class="hljs-keyword">const</span> y = event.offsetY
      ctx.lineTo(x, y)
      ctx.stroke()
    &#125;
    <span class="hljs-comment">// 抬笔</span>
    canvas.onmouseup = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!painting) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      painting = <span class="hljs-literal">false</span>
      ctx.closePath()
    &#125;

    <span class="hljs-comment">// 离开画板</span>
    canvas.onmouseleave = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!painting) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      painting = <span class="hljs-literal">false</span>
      ctx.closePath()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3d630e4f49945168511dbdbb963516e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">3) 使用TouchEvent</h4>
<blockquote>
<p><a href="https://codepen.io/klren0312/pen/YzNBKMj" target="_blank" rel="nofollow noopener noreferrer">codepen.io/klren0312/p…</a></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 手指按下</span>
canvas.ontouchstart = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(e.touches)
      painting = <span class="hljs-literal">true</span>
      <span class="hljs-keyword">const</span> event = e.touches[<span class="hljs-number">0</span>]
      ctx.lineCap = <span class="hljs-string">'round'</span>
      ctx.lineJoin = <span class="hljs-string">'round'</span>
      <span class="hljs-keyword">const</span> x = event.pageX
      <span class="hljs-keyword">const</span> y = event.pageY
      ctx.beginPath()
      ctx.moveTo(x, y)
      ctx.lineWidth = lineWidth
      ctx.strokeStyle = lineColor
    &#125;
    <span class="hljs-comment">// 手指移动</span>
    canvas.ontouchmove = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (!painting) &#123;
        <span class="hljs-keyword">return</span>
      &#125;
      <span class="hljs-keyword">const</span> event = e.touches[<span class="hljs-number">0</span>]
      <span class="hljs-keyword">const</span> x = event.pageX
      <span class="hljs-keyword">const</span> y = event.pageY
      ctx.lineTo(x, y)
      ctx.stroke()
    &#125;
    <span class="hljs-comment">// 手指抬起</span>
    canvas.ontouchend = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!painting) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      painting = <span class="hljs-literal">false</span>
      ctx.closePath()
    &#125;
    <span class="hljs-comment">// 手指离开区域</span>
    ontouchcancel = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!painting) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      painting = <span class="hljs-literal">false</span>
      ctx.closePath()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1645b64d9cf4248ad6e55ecb2d583c3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">3) 使用PointerEvent</h4>
<blockquote>
<p>这是这次的重点, 所以新开个项目写</p>
</blockquote>
<p>源码地址: <a href="https://github.com/klren0312/drawboard" target="_blank" rel="nofollow noopener noreferrer">klren0312/drawboard: drawboard with pressure ( 可以使用压感笔的画板 ) (github.com)</a>
示例地址: <a href="https://klren0312.github.io/drawboard/" target="_blank" rel="nofollow noopener noreferrer">klren0312.github.io/drawboard/</a></p>
<p><strong>注意点:</strong></p>
<ol>
<li>在移动端, 会出现触摸页面时, 产生页面滚动, 浏览器缩放等事件, 这时候需要给画布设置<code>touch-action: none;</code>样式, 来设置当触控事件发生在元素上时，不进行任何操作</li>
<li>因为我们需要实时根据压感来设置笔画粗细, 所以在每一次移动都作为一个路径的起始和结束, 当然这样的话我们需要记录每次移动的最终坐标, 在pointermove事件再次触发的时候, 将坐标移动到上一次结束的坐标处, 这样保证了笔画的连续性</li>
</ol>
<pre><code class="hljs language-vue copyable" lang="vue"> /**
     * @description 开始
     * @param &#123;PointerEvent&#125; e 事件
     */
    function startDraw(e: PointerEvent) &#123;
      painting = true
      pointerId = e.pointerId
      ctx.lineCap = 'round'
      ctx.lineJoin = 'round'
      doDraw(e, true)
    &#125;
    /**
     * @description 移动
     * @param &#123;PointerEvent&#125; e 事件
     */
    function moveDraw(e: PointerEvent) &#123;
      if (!painting && e.pointerId !== pointerId) &#123;
        return
      &#125; else &#123;
        doDraw(e)
      &#125;
    &#125;
    function cancelDraw(e: PointerEvent) &#123;
      console.log('cancel')
      pointerId = -1
      if (!painting) &#123;
        return false
      &#125;
      painting = false
      historyList.push(ctx.getImageData(0, 0, canvas.width, canvas.height))
      ctx.closePath()
    &#125;
    /**
     * 绘画
     * @param &#123;PointerEvent&#125; e 事件
     * @param &#123;Boolean&#125; isStart 是否是起始点
     */
    function doDraw(e, isStart = false) &#123;
      if (isPen.value && e.pointerType !== 'pen') &#123;
        return
      &#125;
      const event: PointerEvent = e || window.event
      const x: number = event.offsetX
      const y: number = event.offsetY
      ctx.lineWidth = getLineWidth(event)
      ctx.strokeStyle = lineColor.value
      ctx.beginPath()
      if (!isStart) &#123;
        ctx.moveTo(startXY.x, startXY.y)
        ctx.lineTo(x, y)
      &#125; else &#123;
        ctx.moveTo(x, y)
      &#125;
      ctx.closePath()
      ctx.stroke()
      startXY = &#123;
        x: x,
        y: y
      &#125;
    &#125;
    /**
     * @description 计算线宽
     * @param &#123;PointerEvent&#125; e 事件
     * @return &#123;number&#125; 线宽
     */
    function getLineWidth(e: PointerEvent): number &#123;
      switch (e.pointerType) &#123;
        case 'touch': &#123;
          if (e.width < 10 && e.height < 10) &#123;
            return (e.width + e.height) * 2 + 10;
          &#125; else &#123;
            return (e.width + e.height - 40) / 2;
          &#125;
        &#125;
        case 'pen': return e.pressure * 8;
        default: return (e.pressure) ? e.pressure * 8 : 4;
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到上面的代码 , 我们在每次完整的笔画绘制结束, 会向historyList数组里保存一个图片数据.</p>
<pre><code class="hljs language-js copyable" lang="js">historyList.push(ctx.getImageData(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, canvas.width, canvas.height))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么做主要是为了实现笔画的回退操作, 我们可以在点击回退按钮时, 取出上一步保存的图片绘制到canvas中, 达到此功能</p>
<p>清屏的功能就相对简单, 可以使用canvas的<code>clearRect</code>来将画布清空</p>
<pre><code class="hljs language-js copyable" lang="js">ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, canvas.width, canvas.height)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eb2e09d34ec4c63834a44c643f64a81~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">参考资料</h3>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/MouseEvent" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/TouchEvent" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Pointer_events" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/touch-action" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a>
<a href="https://zh.javascript.info/pointer-events" target="_blank" rel="nofollow noopener noreferrer">zh.javascript.info/pointer-eve…</a>
<a href="https://github.com/klren0312/daliy_knowledge/issues/372" target="_blank" rel="nofollow noopener noreferrer">github.com/klren0312/d…</a></p></div>  
</div>
            