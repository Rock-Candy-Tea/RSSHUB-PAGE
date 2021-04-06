
---
title: 'vue+canvas实现数据实时从上到下刷新瀑布图效果（类似QT的）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b83131e46b44472971ab46b632cadfd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 19:52:43 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b83131e46b44472971ab46b632cadfd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>话不多说了，先上一张Demo图，实现的功能有：左侧图例、右侧瀑布图、鼠标移入弹出当前坐标对应的数据信息（有优化的空间，大家自由发挥）。</p>
<p><img alt="微信图片_20210406110749.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b83131e46b44472971ab46b632cadfd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">图例使用到的插件</h2>
<p><strong>这里推荐使用安装npm插件<a href="https://www.npmjs.com/package/colormap" target="_blank" rel="nofollow noopener noreferrer">colormap</a></strong></p>
<h2 data-id="heading-1">瀑布图主体内容</h2>
<ol>
<li>这里不多做解释了，都是一些原生标签还有vue绑定的事件，可以根据实际项目情况自己封装成组件，我这里是写在一起的。</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"neirong"</span>></span>
                <span class="hljs-comment"><!--图例--></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"legend"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"legend"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-comment"><!--瀑布图--></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"waterFall"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"waterFallContent"</span>
                     @<span class="hljs-attr">mousemove</span>=<span class="hljs-string">"waterFallMove($event)"</span>
                     @<span class="hljs-attr">mouseleave</span>=<span class="hljs-string">"waterFallLeave"</span>
                ></span>
                    <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"waterFall"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
                    <span class="hljs-comment"><!--鼠标移入弹出框--></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"tip"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tip"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>这里是用到的Data数据</li>
</ol>
<p><code>colormap：颜色库</code><br>
<code>legend：图例</code><br>
<code>waterFall：瀑布图</code><br>
<code>waterFallList：瀑布图源数据</code><br>
<code>waterFallIndex：瀑布图定时器用到的计数标识</code><br>
<code>waterFallCopyList：瀑布图二维数组（用来显示数据做的临时储存）</code><br>
<code>waterFallIntervals：瀑布图定时器</code><br>
<code>waterFallWidth：瀑布图的宽度（后端返回的数据length）</code><br>
<code>waterFallHeight：瀑布图定高度（也可以理解成渲染次数 例如30次渲染完成）</code><br>
<code>maxNum：图例最大值</code><br>
<code>minNum：图例最小值</code><br></p>
<pre><code class="hljs language-js copyable" lang="js"><script>
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"index"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">colormap</span>: [],
                <span class="hljs-attr">legend</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">waterFall</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">waterFallList</span>: [],
                <span class="hljs-attr">waterFallIndex</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">waterFallCopyList</span>: [],
                <span class="hljs-attr">waterFallIntervals</span>: <span class="hljs-literal">null</span>,
                <span class="hljs-attr">waterFallWidth</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">waterFallHeight</span>: <span class="hljs-number">0</span>,
                <span class="hljs-attr">maxNum</span>: <span class="hljs-number">10</span>,
                <span class="hljs-attr">minNum</span>: <span class="hljs-number">0</span>
            &#125;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>下面是具体的方法，写的比较粗略，大家凑活看吧，觉得有用的大家拿走，不足之处自由发挥修改</li>
</ol>
<p>方法调用这就不解释了，离开页面销毁定时器。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
            dx.setColormap()
            dx.createLegendCanvas()
            dx.queryChartList()
        &#125;,
        <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
            <span class="hljs-built_in">clearInterval</span>(dx.waterFallIntervals)
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">创建颜色库</h3>
<p>这个地方具体看上面插件的官网有详细的介绍</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setColormap</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
      <span class="hljs-keyword">let</span> colormap = <span class="hljs-built_in">require</span>(<span class="hljs-string">'colormap'</span>)
      dx.colormap = colormap(&#123;
          <span class="hljs-attr">colormap</span>: <span class="hljs-string">'jet'</span>,
          <span class="hljs-attr">nshades</span>: <span class="hljs-number">150</span>,
          <span class="hljs-attr">format</span>: <span class="hljs-string">'rba'</span>,
          <span class="hljs-attr">alpha</span>: <span class="hljs-number">1</span>,
   &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">创建图例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">createLegendCanvas</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
                <span class="hljs-keyword">let</span> legendRefs = dx.$refs.legend
                dx.legend = legendRefs.getContext(<span class="hljs-string">'2d'</span>)
                <span class="hljs-keyword">let</span> legendCanvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
                legendCanvas.width = <span class="hljs-number">1</span>
                <span class="hljs-keyword">let</span> legendCanvasTemporary = legendCanvas.getContext(<span class="hljs-string">'2d'</span>)
                <span class="hljs-keyword">const</span> imageData = legendCanvasTemporary.createImageData(<span class="hljs-number">1</span>, dx.colormap.length)
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < dx.colormap.length; i++) &#123;
                    <span class="hljs-keyword">const</span> color = dx.colormap[i]
                    imageData.data[imageData.data.length - i * <span class="hljs-number">4</span> + <span class="hljs-number">0</span>] = color[<span class="hljs-number">0</span>]
                    imageData.data[imageData.data.length - i * <span class="hljs-number">4</span> + <span class="hljs-number">1</span>] = color[<span class="hljs-number">1</span>]
                    imageData.data[imageData.data.length - i * <span class="hljs-number">4</span> + <span class="hljs-number">2</span>] = color[<span class="hljs-number">2</span>]
                    imageData.data[imageData.data.length - i * <span class="hljs-number">4</span> + <span class="hljs-number">3</span>] = <span class="hljs-number">255</span>
                &#125;
                legendCanvasTemporary.putImageData(imageData, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
                dx.legend.drawImage(legendCanvasTemporary.canvas, 
                <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>, dx.colormap.length, <span class="hljs-number">50</span>, <span class="hljs-number">0</span>, <span class="hljs-number">200</span>, dx.legend.canvas.height)
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">创建瀑布图</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">createWaterFallCanvas</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
                <span class="hljs-keyword">let</span> waterFall = dx.$refs.waterFall
                dx.waterFall = waterFall.getContext(<span class="hljs-string">'2d'</span>)
                waterFall.width = dx.waterFallWidth
                waterFall.height = dx.$refs.waterFallContent.offsetHeight
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">绘制单行图像</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">rowToImageData</span>(<span class="hljs-params">data</span>)</span> &#123;
                <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
                <span class="hljs-keyword">if</span> (dx.$refs.waterFallContent !== <span class="hljs-literal">undefined</span>) &#123;
                    <span class="hljs-keyword">let</span> canvasHeight = <span class="hljs-built_in">Math</span>.floor(dx.$refs.waterFallContent.offsetHeight / dx.waterFallHeight)
                    <span class="hljs-keyword">let</span> imgOld = dx.waterFall.getImageData(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, dx.waterFallWidth, canvasHeight * dx.waterFallIndex + <span class="hljs-number">1</span>)
                    <span class="hljs-keyword">const</span> imageData = dx.waterFall.createImageData(data.length, <span class="hljs-number">1</span>)
                    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < imageData.data.length; i += <span class="hljs-number">4</span>) &#123;
                        <span class="hljs-keyword">const</span> cindex = dx.colorMapData(data[i / <span class="hljs-number">4</span>], <span class="hljs-number">0</span>, <span class="hljs-number">130</span>)
                        <span class="hljs-keyword">const</span> color = dx.colormap[cindex]
                        imageData.data[i + <span class="hljs-number">0</span>] = color[<span class="hljs-number">0</span>]
                        imageData.data[i + <span class="hljs-number">1</span>] = color[<span class="hljs-number">1</span>]
                        imageData.data[i + <span class="hljs-number">2</span>] = color[<span class="hljs-number">2</span>]
                        imageData.data[i + <span class="hljs-number">3</span>] = <span class="hljs-number">255</span>
                    &#125;
                    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < canvasHeight; i++) &#123;
                        dx.waterFall.putImageData(imageData, <span class="hljs-number">0</span>, i)
                    &#125;
                    dx.waterFall.putImageData(imgOld, <span class="hljs-number">0</span>, canvasHeight)
                &#125;
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">返回数据对应的Colormap颜色</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">colorMapData</span>(<span class="hljs-params">data, outMin, outMax</span>)</span> &#123;
                <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
                <span class="hljs-keyword">if</span> (data <= dx.minNum) &#123;
                    <span class="hljs-keyword">return</span> outMin
                &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (data >= dx.maxNum) &#123;
                    <span class="hljs-keyword">return</span> outMax
                &#125;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.round(((data - dx.minNum) / (dx.maxNum - dx.minNum)) * outMax)
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">鼠标移入瀑布图</h3>
<pre><code class="hljs language-js copyable" lang="js">            <span class="hljs-function"><span class="hljs-title">waterFallMove</span>(<span class="hljs-params">event</span>)</span> &#123;
                <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
                <span class="hljs-keyword">let</span> dataWidth = (dx.$refs.waterFallContent.offsetWidth / dx.waterFallWidth).toFixed(<span class="hljs-number">2</span>)
                <span class="hljs-keyword">let</span> dataHeight = (dx.$refs.waterFallContent.offsetHeight / dx.waterFallHeight).toFixed(<span class="hljs-number">2</span>)
                <span class="hljs-keyword">let</span> x = <span class="hljs-built_in">Math</span>.floor(event.offsetX / dataWidth)
                <span class="hljs-keyword">let</span> y = <span class="hljs-built_in">Math</span>.floor(event.offsetY / dataHeight)
                <span class="hljs-keyword">try</span> &#123;
                    dx.$refs.tip.innerHTML = <span class="hljs-string">'数值：'</span> + <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(dx.waterFallCopyList[y][x]))
                    <span class="hljs-keyword">let</span> xx = event.offsetX + <span class="hljs-number">5</span>
                    <span class="hljs-keyword">let</span> yy = event.offsetY - <span class="hljs-number">20</span>
                    <span class="hljs-keyword">if</span> (event.offsetX > <span class="hljs-number">1300</span>) &#123;
                        xx = event.offsetX - <span class="hljs-number">160</span>
                        yy = event.offsetY - <span class="hljs-number">20</span>
                    &#125;
                    dx.$refs.tip.style.position = <span class="hljs-string">'absolute'</span>
                    dx.$refs.tip.style.left = xx + <span class="hljs-string">'px'</span>
                    dx.$refs.tip.style.top = yy + <span class="hljs-string">'px'</span>
                    dx.$refs.tip.style.display = <span class="hljs-string">'block'</span>
                &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                    dx.$refs.tip.style.display = <span class="hljs-string">'none'</span>
                &#125;
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">鼠标移出瀑布图</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">waterFallLeave</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
                dx.$refs.tip.style.display = <span class="hljs-string">'none'</span>
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">瀑布图假数据模拟</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">queryChartList</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">let</span> dx = <span class="hljs-built_in">this</span>
                dx.waterFallWidth = <span class="hljs-number">1500</span>
                dx.waterFallHeight = <span class="hljs-number">30</span>
                <span class="hljs-keyword">let</span> data = []
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1500</span>; i++) &#123;
                    data.push(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * (<span class="hljs-number">20</span> - <span class="hljs-number">1</span>)) + <span class="hljs-number">1</span>)
                &#125;
                <span class="hljs-keyword">if</span> (dx.waterFall === <span class="hljs-literal">null</span>) &#123;
                    dx.createWaterFallCanvas(data.length)
                &#125;
                dx.rowToImageData(data)
                dx.waterFallCopyList.unshift(data)
                dx.waterFallIndex++
                <span class="hljs-keyword">if</span> (dx.waterFallIndex > dx.waterFallHeight) &#123;
                    dx.waterFallCopyList.pop()
                &#125;
                dx.waterFallIntervals = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    dx.queryChartList()
                &#125;, <span class="hljs-number">1000</span>)
            &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">样式代码</h3>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.neirong</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">1800px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">80px</span> auto;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">justify-content</span>: center;
    &#125;

    <span class="hljs-selector-class">.legend</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">25px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">500px</span>;
    &#125;

    <span class="hljs-selector-tag">canvas</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;

    <span class="hljs-selector-class">.waterFall</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">1500px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">500px</span>;
        <span class="hljs-attribute">position</span>: relative;
    &#125;

    <span class="hljs-selector-class">.tip</span> &#123;
        <span class="hljs-attribute">pointer-events</span>: none;
        <span class="hljs-attribute">display</span>: none;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#040404</span>9e;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
        <span class="hljs-attribute">box-sizing</span>: border-box;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里这个Demo基本就是可以运行的，不会有任何报错，代码写的不是很高级，我本人也是个初级的小菜鸟，也是第一次写文章，希望大佬可以给出一些更好的建议我也会好好学习的，也希望那些遇到类似这个需求没什么思路的小伙伴可以借鉴我的踩坑之旅，可以更快的成长起来。
最后，谢谢大家的阅读！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            