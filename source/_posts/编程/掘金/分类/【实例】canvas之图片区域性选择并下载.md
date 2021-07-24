
---
title: '【实例】canvas之图片区域性选择并下载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f440265823c499da93a65146617e726~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 05:01:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f440265823c499da93a65146617e726~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>实现样式</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f440265823c499da93a65146617e726~tplv-k3u1fbpfcp-watermark.image" alt="选择拉动框.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>主要是通过鼠标来对图片进行区域选择，然后将图片进行下载和灰度处理</strong></p>
<blockquote>
<p>实现代码</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>加水印<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.container</span>&#123;
        <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">50px</span>;
    &#125;
    <span class="hljs-selector-class">.edit</span>&#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">justify-content</span>: center;
    &#125;

    <span class="hljs-selector-class">.edit-item</span>&#123;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">34px</span>;
        <span class="hljs-attribute">background-color</span>: salmon;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">34px</span>;
        <span class="hljs-attribute">text-align</span>: center;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">5px</span>;
        <span class="hljs-attribute">cursor</span>: pointer;
        <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">20px</span>;
    &#125;
    <span class="hljs-selector-class">.edit-item</span> <span class="hljs-selector-tag">input</span>&#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-selector-class">.previwe</span>&#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">100px</span>;
    &#125;

    <span class="hljs-selector-tag">canvas</span>&#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">800px</span>;
        <span class="hljs-attribute">display</span>: block;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#eee</span>;
    &#125;
    <span class="hljs-selector-tag">img</span>&#123;
        <span class="hljs-attribute">object-fit</span>: contain;
        <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">100px</span>;
    &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"edit"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"edit-item"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>上传背景图片<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bgImage"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"edit-item"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"selected"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>下载选中区域<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"edit-item"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"gray"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>灰度处理<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"previwe"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCanvas"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"800"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"600"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">""</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"showImage"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./utils.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> bgImage = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'bgImage'</span>)
    <span class="hljs-keyword">let</span> selected = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'selected'</span>)
    <span class="hljs-keyword">let</span> showImage = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'showImage'</span>)
    <span class="hljs-keyword">let</span> gray = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'gray'</span>)
    <span class="hljs-keyword">let</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'myCanvas'</span>)
    <span class="hljs-keyword">let</span> ctx = canvas.getContext(<span class="hljs-string">'2d'</span>)
    <span class="hljs-keyword">let</span> bgImageData = &#123;&#125;,selectData = &#123;&#125;
    bgImage.addEventListener(<span class="hljs-string">'change'</span>,waterMarkChange,<span class="hljs-literal">false</span>)
    
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">waterMarkChange</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> file = bgImage.files[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">let</span> type = file.type
        <span class="hljs-keyword">if</span>(type.indexOf(<span class="hljs-string">'image'</span>) == -<span class="hljs-number">1</span>)&#123;
            alert(<span class="hljs-string">'仅支持图片,请重新上传'</span>)
        &#125;
        getImageData(file)
    &#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getImageData</span>(<span class="hljs-params">file</span>)</span>&#123;
    <span class="hljs-keyword">let</span> image = <span class="hljs-keyword">new</span> Image()
        image.src = <span class="hljs-built_in">window</span>.URL.createObjectURL(file)
        image.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        bgImageData.data = image
        bgImageData.width = image.width
        bgImageData.height = image.height
        <span class="hljs-keyword">let</span> x = canvas.width / <span class="hljs-number">2</span> - bgImageData.width / <span class="hljs-number">2</span>
        <span class="hljs-keyword">let</span> y = canvas.height / <span class="hljs-number">2</span> - bgImageData.height / <span class="hljs-number">2</span>
        bgImageData.x = x , bgImageData.y = y
        putImageData()
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">putImageData</span>(<span class="hljs-params"></span>)</span>&#123;
  ctx.clearRect(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,canvas.width,canvas.height)
  ctx.drawImage(bgImageData.data,bgImageData.x,bgImageData.y,bgImageData.width,bgImageData.height)
&#125;

selected.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 获取canvas中的数据</span>
    <span class="hljs-keyword">if</span>(selectData.data)&#123;
        <span class="hljs-keyword">let</span> bas64 = returnImageUrl(selectData.data)
        <span class="hljs-keyword">let</span> blobData = C.dataURLToBlob(bas64)
        C.download(blobData)
    &#125;
&#125;)

gray.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(selectData.data)&#123;
        selectData.data = C.grey_processing(selectData.data)
        showImage.src = returnImageUrl(selectData.data)
    &#125;
&#125;)
canvas.addEventListener(<span class="hljs-string">'mousedown'</span>,mousedown,<span class="hljs-literal">false</span>)
canvas.addEventListener(<span class="hljs-string">'mousemove'</span>,mousemove,<span class="hljs-literal">false</span>)
canvas.addEventListener(<span class="hljs-string">'mouseup'</span>,mouseup,<span class="hljs-literal">false</span>)
<span class="hljs-keyword">let</span> mouse = C.getMousePosition(canvas)
<span class="hljs-keyword">let</span> isMoving = <span class="hljs-literal">false</span>
<span class="hljs-keyword">let</span> initX = <span class="hljs-number">0</span>,initY = <span class="hljs-number">0</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousedown</span>(<span class="hljs-params"></span>)</span>&#123;
    isMoving = <span class="hljs-literal">true</span>
    initY = mouse.y
    initX = mouse.x
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mousemove</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-keyword">if</span>(isMoving)&#123;
    putImageData()
    ctx.save()
    ctx.strokeStyle = <span class="hljs-string">'#fff'</span>
    selectData.width = <span class="hljs-built_in">Math</span>.abs(mouse.x - initX)
    selectData.height = <span class="hljs-built_in">Math</span>.abs(mouse.y - initY)
    <span class="hljs-keyword">if</span>(selectData.width && selectData.height)&#123;
        selectData.data = ctx.getImageData(initX,initY,selectData.width,selectData.height)
        showImage.width = selectData.width,showImage.height = selectData.height
        showImage.src = returnImageUrl(selectData.data)
    &#125;
    ctx.strokeRect(initX,initY,selectData.width,selectData.height)
    ctx.restore()
  &#125;

&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mouseup</span>(<span class="hljs-params"></span>)</span>&#123;
    isMoving = <span class="hljs-literal">false</span>
    initY = initX = <span class="hljs-number">0</span>
&#125;

<span class="hljs-comment">// 重新生成一个canvas用来下载图片</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">returnImageUrl</span>(<span class="hljs-params">data</span>)</span>&#123;
    <span class="hljs-keyword">let</span> canvasElm = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>)
    <span class="hljs-keyword">let</span> ctxElm = canvasElm.getContext(<span class="hljs-string">'2d'</span>)
    canvasElm.width = showImage.width , canvasElm.height = showImage.height
    ctxElm.putImageData(data,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>)
    <span class="hljs-keyword">return</span> canvasElm.toDataURL(<span class="hljs-string">'image/png'</span>,<span class="hljs-number">1</span>)

&#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>utils.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 转换坐标</span>
C.getMousePosition = <span class="hljs-function">(<span class="hljs-params">el</span>) =></span>&#123;
        <span class="hljs-keyword">let</span> mouse = &#123;<span class="hljs-attr">x</span>:<span class="hljs-number">0</span>,<span class="hljs-attr">y</span>:<span class="hljs-number">0</span>&#125;
        el.addEventListener(<span class="hljs-string">'mousemove'</span>,<span class="hljs-function">(<span class="hljs-params">e</span>)=></span>&#123;
        <span class="hljs-keyword">let</span> &#123;x,y&#125; = C.eventWrapper(e)
        mouse.x = x
        mouse.y = y
    &#125;)
    <span class="hljs-keyword">return</span> mouse
&#125;
C.eventWrapper = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>)</span>&#123;
    <span class="hljs-keyword">let</span> &#123;pageX, pageY, target&#125; = e
    <span class="hljs-keyword">let</span> &#123;left,top&#125; = target.getBoundingClientRect() <span class="hljs-comment">// 获取元素相对于视口位置距离</span>
    <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">x</span> : pageX - left ,<span class="hljs-attr">y</span>: pageY - top&#125;
&#125;
<span class="hljs-comment">//下载blob对象数据</span>
C.download = <span class="hljs-function">(<span class="hljs-params">blob</span>) =></span>&#123;
    <span class="hljs-comment">// 创建一个blob链接</span>
    <span class="hljs-keyword">let</span> url = URL.createObjectURL(blob)
    <span class="hljs-keyword">let</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>)
    a.setAttribute(<span class="hljs-string">'download'</span>, url)
    a.href=url ;
    a.style.display = <span class="hljs-string">'none'</span>
    a.click()
    <span class="hljs-comment">// 每次调用URL.createObjectURL,都会创建一个新的URL对象，浏览器内存中会保持对该对象的引用</span>
    <span class="hljs-comment">// 只有在document销毁时，才会释放此部分内存</span>
    <span class="hljs-comment">// 在考虑性能的情况下，在url使用结束后，最好释放此部分内存</span>
    URL.revokeObjectURL(url)
&#125;

<span class="hljs-comment">// 将base64转换成blob对象</span>
C.dataURLToBlob = <span class="hljs-function">(<span class="hljs-params">code</span>)=></span> &#123;
    <span class="hljs-keyword">let</span> parts = code.split(<span class="hljs-string">';base64,'</span>)
    <span class="hljs-keyword">let</span> contentType = parts[<span class="hljs-number">0</span>].split(<span class="hljs-string">':'</span>)[<span class="hljs-number">1</span>]
    <span class="hljs-keyword">let</span> raw = <span class="hljs-built_in">window</span>.atob(parts[<span class="hljs-number">1</span>])
    <span class="hljs-keyword">let</span> rawLength = raw.length
    <span class="hljs-keyword">let</span> uInt8Array = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(rawLength)
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < rawLength; ++i) &#123;
        uInt8Array[i] = raw.charCodeAt(i)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Blob([uInt8Array], &#123;
        <span class="hljs-attr">type</span>: contentType
    &#125;)
&#125;

<span class="hljs-comment">// 对图片数据进行灰度处理</span>
C.grey_processing = <span class="hljs-function">(<span class="hljs-params">imageData</span>) =></span>&#123;
    <span class="hljs-keyword">let</span> data = imageData.data
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < data.length ; i+=<span class="hljs-number">4</span>)&#123;
    <span class="hljs-keyword">let</span> avg = <span class="hljs-number">0</span>
    avg = (data[i]+data[i+<span class="hljs-number">1</span>]+data[i+<span class="hljs-number">2</span>]) / <span class="hljs-number">3</span>
        data[i] = data[i+<span class="hljs-number">1</span>] = data[i+<span class="hljs-number">2</span>] = avg
    &#125;
    <span class="hljs-keyword">return</span> imageData
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>步骤</strong>：</p>
<ul>
<li>图片上传现在到canvas上，显示图片
<ul>
<li><code>drawImage</code>来将获取到的图片会知道canvas上</li>
</ul>
</li>
<li>在利用鼠标和canvas进行交互区域选择，获取到图片数据
<ul>
<li>主要是利用<code>mouseup</code>|<code>mousemove</code>|<code>mousedown</code>事件来进行事件交互</li>
<li>利用<code>putImageData</code>|<code>getImageData</code>来实现获取区域性的图像数据</li>
</ul>
</li>
</ul></div>  
</div>
            