
---
title: 'Canvas实现点赞效果以及使用离屏画卡实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6c9ec98890742c097089e878d2cf40f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 12 May 2021 03:03:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6c9ec98890742c097089e878d2cf40f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6c9ec98890742c097089e878d2cf40f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>本文会介绍Web Worker实现离屏Canvas点赞和单纯Canvas实现点赞效果。</p>
</blockquote>
<h1 data-id="heading-0">Canvas实现点赞</h1>
<h3 data-id="heading-1">创建Canvas</h3>
<p>页面元素上新建 canvas 标签，初始化 canvas。</p>
<p>canvas 上可以设置 width 和 height 属性，也可以在 style 属性里面设置 width 和 height。</p>
<ul>
<li>canvas 上 style 的 width 和 height 是 canvas 在浏览器中被渲染的高度和宽度，即在页面中的实际宽高。</li>
<li>canvas 标签的 width 和 height 是画布实际宽度和高度。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <canvas ref=&#123;canvasNode&#125; width=<span class="hljs-string">"180"</span> height=<span class="hljs-string">"400"</span>></canvas>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">图片加载</h3>
<p>初始化加载送花图片，获取图片相关信息</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">/**
 * 加载图片
 * <span class="hljs-doctag">@private</span>
 * <span class="hljs-doctag">@memberof <span class="hljs-variable">SendLove</span></span>
 */</span>
private <span class="hljs-function"><span class="hljs-title">loadImage</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> imgs = [
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
    ]
    <span class="hljs-comment">// 承接所有加载后的图片信息</span>
    <span class="hljs-keyword">const</span> promiseAll: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">Promise</span><HTMLImageElement>> = []
    imgs.forEach(<span class="hljs-function">(<span class="hljs-params">img: string</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span><HTMLImageElement>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> image = <span class="hljs-keyword">new</span> Image()
            image.src = img
            image.crossOrigin = <span class="hljs-string">'Anonymous'</span>
            image.onerror = image.onload = resolve.bind(<span class="hljs-literal">null</span>, image)
        &#125;)
        promiseAll.push(p)
    &#125;)
    <span class="hljs-comment">// 获取所有图片信息</span>
    <span class="hljs-built_in">Promise</span>.all(promiseAll)
        .then(<span class="hljs-function"><span class="hljs-params">lists</span> =></span> &#123;
            <span class="hljs-built_in">this</span>.listImage = lists.filter(<span class="hljs-function">(<span class="hljs-params">img: HTMLImageElement</span>) =></span> img && img.width > <span class="hljs-number">0</span>)
        &#125;)
        .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'图片加载失败...'</span>, err)
        &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">平滑移动位置</h3>
<p>如果要做到平滑曲线，其实可以使用我们再熟悉不过的正弦( Math.sin )函数来实现均匀曲线。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">/**
 *  绘制每一个点赞；这里使用了闭包，初始化
 * <span class="hljs-doctag">@private</span>
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;(Loop<number, boolean | void>)&#125;</span></span>
 * <span class="hljs-doctag">@memberof <span class="hljs-variable">SendLove</span></span>
 */</span>
private createRender(): Loop<number, boolean | <span class="hljs-keyword">void</span>> &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.listImage.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
    <span class="hljs-comment">// 以下是在创建时，初始化默认值</span>
    <span class="hljs-keyword">const</span> context = <span class="hljs-built_in">this</span>.ctx
    <span class="hljs-comment">// 随机取出scale值</span>
    <span class="hljs-keyword">const</span> basicScale = [<span class="hljs-number">0.6</span>, <span class="hljs-number">0.9</span>, <span class="hljs-number">1.2</span>][<span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">0</span>, <span class="hljs-number">2</span>)]
    <span class="hljs-comment">//随机取一张图片</span>
    <span class="hljs-keyword">const</span> img = <span class="hljs-built_in">this</span>.listImage[<span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.listImage.length - <span class="hljs-number">1</span>)]
    <span class="hljs-keyword">const</span> offset = <span class="hljs-number">20</span>
    <span class="hljs-comment">// 随机动画X轴的位置，是动画不重叠在一起</span>
    <span class="hljs-keyword">const</span> basicX = <span class="hljs-built_in">this</span>.width / <span class="hljs-number">2</span> + <span class="hljs-built_in">this</span>.getRandom(-offset, offset)
    <span class="hljs-keyword">const</span> angle = <span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">2</span>, <span class="hljs-number">12</span>)
    <span class="hljs-comment">// x轴偏移量10 - 30</span>
    <span class="hljs-keyword">let</span> ratio = <span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">10</span>, <span class="hljs-number">30</span>) * (<span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>) ? <span class="hljs-number">1</span> : -<span class="hljs-number">1</span>)
    <span class="hljs-comment">// 获取X轴值</span>
    <span class="hljs-keyword">const</span> getTranslateX = (diffTime: number): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (diffTime < <span class="hljs-built_in">this</span>.scaleTime) &#123;
            <span class="hljs-keyword">return</span> basicX
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> basicX + ratio * <span class="hljs-built_in">Math</span>.sin(angle * (diffTime - <span class="hljs-built_in">this</span>.scaleTime))
        &#125;
    &#125;
    <span class="hljs-comment">// 获取Y轴值</span>
    <span class="hljs-keyword">const</span> getTranslateY = (diffTime: number): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>(img.height) / <span class="hljs-number">2</span> + (<span class="hljs-built_in">this</span>.height - <span class="hljs-built_in">Number</span>(img.height) / <span class="hljs-number">2</span>) * (<span class="hljs-number">1</span> - diffTime)
    &#125;
    <span class="hljs-comment">// scale方法倍数 针对一个鲜花创建一个scale值</span>
    <span class="hljs-keyword">const</span> getScale = (diffTime: number): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (diffTime < <span class="hljs-built_in">this</span>.scaleTime) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>((diffTime / <span class="hljs-built_in">this</span>.scaleTime).toFixed(<span class="hljs-number">2</span>)) * basicScale
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> basicScale
        &#125;
    &#125;
    <span class="hljs-comment">// 随机开始淡出时间,</span>
    <span class="hljs-keyword">const</span> fadeOutStage = <span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">16</span>, <span class="hljs-number">20</span>) / <span class="hljs-number">100</span>
    <span class="hljs-comment">// 透明度</span>
    <span class="hljs-keyword">const</span> getAlpha = (diffTime: number): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
        <span class="hljs-keyword">const</span> left = <span class="hljs-number">1</span> - diffTime
        <span class="hljs-keyword">if</span> (left > fadeOutStage) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-number">1</span> - <span class="hljs-built_in">Number</span>(((fadeOutStage - left) / fadeOutStage).toFixed(<span class="hljs-number">2</span>))
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-params">diffTime</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (diffTime >= <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        <span class="hljs-keyword">const</span> scale = getScale(diffTime)
        context.save()
        context.beginPath()
        context.translate(getTranslateX(diffTime), getTranslateY(diffTime))
        context.scale(scale, scale)
        context.globalAlpha = getAlpha(diffTime)
        context.drawImage(img, -img.width / <span class="hljs-number">2</span>, -img.height / <span class="hljs-number">2</span>, <span class="hljs-built_in">Number</span>(img.width), <span class="hljs-built_in">Number</span>(img.height))
        context.restore()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">实时绘制</h3>
<p>开启实时绘制扫描器，将创建的渲染对象放入 renderList 数组，数组不为空，说明 canvas 上还有动画，就需要不停的去执行 scan，直到 canvas 上没有动画结束为止。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 扫描
 * <span class="hljs-doctag">@private</span>
 * <span class="hljs-doctag">@memberof <span class="hljs-variable">SendLove</span></span>
 */</span>
private <span class="hljs-function"><span class="hljs-title">scan</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 清屏（清除上一次绘制内容）</span>
    <span class="hljs-built_in">this</span>.ctx.clearRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">this</span>.width, <span class="hljs-built_in">this</span>.height)
    <span class="hljs-built_in">this</span>.ctx.fillStyle = <span class="hljs-string">'#fff'</span>
    <span class="hljs-built_in">this</span>.ctx.fillRect(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">180</span>, <span class="hljs-number">400</span>)
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> len = <span class="hljs-built_in">this</span>.renderList.length
    <span class="hljs-keyword">if</span> (len > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// 重新扫描后index= 0；重新获取长度</span>
        requestFrame(<span class="hljs-built_in">this</span>.scan.bind(<span class="hljs-built_in">this</span>))
        <span class="hljs-built_in">this</span>.scanning = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>.scanning = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">while</span> (index < len) &#123;
        <span class="hljs-keyword">const</span> curRender = <span class="hljs-built_in">this</span>.renderList[index]
        <span class="hljs-keyword">if</span> (!curRender || !curRender.render || curRender.render.call(<span class="hljs-literal">null</span>, (<span class="hljs-built_in">Date</span>.now() - curRender.timestamp) / curRender.duration)) &#123;
            <span class="hljs-comment">// 动画已结束，删除绘制</span>
            <span class="hljs-built_in">this</span>.renderList.splice(index, <span class="hljs-number">1</span>)
            len--
        &#125; <span class="hljs-keyword">else</span> &#123;
            index++
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">提供对外的接口触发动画</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 提供对外的点赞的接口
 * <span class="hljs-doctag">@returns</span>
 * <span class="hljs-doctag">@memberof <span class="hljs-variable">SendLove</span></span>
 */</span>
public <span class="hljs-function"><span class="hljs-title">likeStart</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 初始化礼物数据、回调函数</span>
    <span class="hljs-keyword">const</span> render = <span class="hljs-built_in">this</span>.createRender()
    <span class="hljs-keyword">const</span> duration = <span class="hljs-built_in">this</span>.getRandom(<span class="hljs-number">1500</span>, <span class="hljs-number">3000</span>)
    <span class="hljs-built_in">this</span>.renderList.push(&#123;
        render,
        duration,
        <span class="hljs-attr">timestamp</span>: <span class="hljs-built_in">Date</span>.now()
    &#125;)
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.scanning) &#123;
        <span class="hljs-built_in">this</span>.scanning = <span class="hljs-literal">true</span>
        requestFrame(<span class="hljs-built_in">this</span>.scan.bind(<span class="hljs-built_in">this</span>))
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">Web Worker实现离屏Canvas点赞</h1>
<h3 data-id="heading-7">什么是Web Worker</h3>
<p>Web Worker允许Javascript创造多线程环境,允许主线程创建Worker线程,将任务分配在后台运行。这样高延迟，密集型的任务可以由Worker线程负担，主线程负责UI交互就会很流畅,不会会阻塞或拖慢</p>
<h3 data-id="heading-8">怎么在项目中使用Web Worker</h3>
<ul>
<li>在webpack 中引入worker-plugin</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">const</span> WorkerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'worker-plugin'</span>)
   <span class="hljs-comment">// 在plugins添加</span>
   <span class="hljs-keyword">new</span> WorkerPlugin()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>主线程使用new命令调用Worker()构造函数创建一个Worker线程</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">const</span> worker = <span class="hljs-keyword">new</span> Worker(<span class="hljs-string">'./like.worker'</span>, &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'module'</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>主线程与Worker线程存在通信限制,不再同一个上下文中,所以只能通过消息完成</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">worker.postMessage(&#123; <span class="hljs-attr">canvas</span>: offscreenCanvas &#125;, [offscreenCanvas <span class="hljs-keyword">as</span> OffscreenCanvas])
worker.onmessage = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;<span class="hljs-built_in">console</span>.log(event.data)&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>Worker使用注意事项：</p>
<ol>
<li>无法操作DOM,无法获取window, document, parent等对象</li>
<li>遵守同源限制, Worker线程的脚本文件，必须于主线程同源。并且加载脚本文件是阻塞的</li>
<li>不当的操作或者疏忽容易引起性能问题</li>
<li>postMessage不能传递函数</li>
</ol>
</li>
</ul>
<h3 data-id="heading-9">初始化</h3>
<p>首先要判断浏览器是否支持离屏Canvas</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> init = <span class="hljs-keyword">async</span> () => &#123;
   <span class="hljs-comment">// offscreenCanvas离屏画卡很多浏览器不兼容, offscreenCanvas可以在window下可以使用也可以在web worker下使用， canvas只能在window下使用</span>
   <span class="hljs-keyword">if</span> (<span class="hljs-string">'OffscreenCanvas'</span> <span class="hljs-keyword">in</span> <span class="hljs-built_in">window</span>) &#123;
       <span class="hljs-keyword">const</span> worker = <span class="hljs-keyword">new</span> Worker(<span class="hljs-string">'./like.worker'</span>, &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'module'</span> &#125;)
       <span class="hljs-keyword">const</span> offscreenCanvas = canvasNode.current.transferControlToOffscreen()
       worker.postMessage(&#123; <span class="hljs-attr">canvas</span>: offscreenCanvas &#125;, [offscreenCanvas <span class="hljs-keyword">as</span> OffscreenCanvas])
       worker.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
           <span class="hljs-built_in">console</span>.log(error)
       &#125;)
       setNewWorker(worker)
   &#125; <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-keyword">const</span> thumbsUpAni = <span class="hljs-keyword">new</span> SendLove(canvasNode.current)
       setCavasAni(thumbsUpAni)
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">关于Worker 图片加载问题</h3>
<p>Worker中没办法操作DOM, 所以new Image()会报错；使用来加载图片</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">fetch(img)
.then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> response.blob())
.then(<span class="hljs-function"><span class="hljs-params">blob</span> =></span> resolve(createImageBitmap(blob)))
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 初始化图片</span>
private <span class="hljs-function"><span class="hljs-title">loadImage</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> imgs = [
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
        <span class="hljs-string">'https://img.qlchat.com/qlLive/activity/image/LCP31WOW-4IMP-NLAE-1620807553972-OYWXNLLNFNJI.png'</span>,
    ]
    <span class="hljs-keyword">const</span> promiseAll: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">Promise</span><any>> = []
    imgs.forEach(<span class="hljs-function">(<span class="hljs-params">img: string</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-comment">// 用于处理图片数据，用于离屏画图</span>
            fetch(img)
                .then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> response.blob())
                .then(<span class="hljs-function"><span class="hljs-params">blob</span> =></span> resolve(createImageBitmap(blob)))
        &#125;)
        promiseAll.push(p)
    &#125;)
    <span class="hljs-comment">// 这里处理有点慢</span>
    <span class="hljs-built_in">Promise</span>.all(promiseAll)
        .then(<span class="hljs-function"><span class="hljs-params">lists</span> =></span> &#123;
            <span class="hljs-built_in">this</span>.listImage = lists.filter(<span class="hljs-function">(<span class="hljs-params">img: ImageData</span>) =></span> img && img.width > <span class="hljs-number">0</span>)
        &#125;)
        .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'图片加载失败...'</span>, err)
        &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>点赞效果逻辑还是和Canvas处理一致</p>
<pre><code class="hljs language-javascript] copyable" lang="javascript]">// 绘制
private createRender(): Loop<boolean | void> &#123;
    if (!this.listImage.length) return null
    // 一下是在创建时，初始化默认值
    const context = this.ctx
    // 随机取出scale值
    const basicScale = [0.6, 0.9, 1.2][this.getRandom(0, 2)]
    //随机取一张图片
    const img = this.listImage[this.getRandom(0, this.listImage.length - 1)]
    const offset = 20
    // 随机动画X轴的位置，是动画不重叠在一起
    const basicX = this.width / 2 + this.getRandom(-offset, offset)
    const angle = this.getRandom(2, 12)
    // x轴偏移量10 - 30
    let ratio = this.getRandom(10, 30) * (this.getRandom(0, 1) ? 1 : -1)
    // 获取X轴值
    const getTranslateX = (diffTime: number): number => &#123;
        if (diffTime < this.scaleTime) &#123;
            return basicX
        &#125; else &#123;
            return basicX + ratio * Math.sin(angle * (diffTime - this.scaleTime))
        &#125;
    &#125;
    // 获取Y轴值
    const getTranslateY = (diffTime: number): number => &#123;
        return Number(img.height) / 2 + (this.height - Number(img.height) / 2) * (1 - diffTime)
    &#125;
    // scale方法倍数 针对一个鲜花创建一个scale值
    const getScale = (diffTime: number): number => &#123;
        if (diffTime < this.scaleTime) &#123;
            return Number((diffTime / this.scaleTime).toFixed(2)) * basicScale
        &#125; else &#123;
            return basicScale
        &#125;
    &#125;
    // 随机开始淡出时间,
    const fadeOutStage = this.getRandom(16, 20) / 100
    // 透明度
    const getAlpha = (diffTime: number): number => &#123;
        const left = 1 - diffTime
        if (left > fadeOutStage) &#123;
            return 1
        &#125; else &#123;
            return 1 - Number(((fadeOutStage - left) / fadeOutStage).toFixed(2))
        &#125;
    &#125;
    return diffTime => &#123;
        if (diffTime >= 1) return true
        const scale = getScale(diffTime)
        context.save()
        context.beginPath()
        context.translate(getTranslateX(diffTime), getTranslateY(diffTime))
        context.scale(scale, scale)
        context.globalAlpha = getAlpha(diffTime)
        context.drawImage(img, -img.width / 2, -img.height / 2, Number(img.width), Number(img.height))
        context.restore()
    &#125;
&#125;
// 扫描渲染列表
private scan() &#123;
    // 清屏（清除上一次绘制内容）
    this.ctx.clearRect(0, 0, this.width, this.height)
    this.ctx.fillStyle = '#fff'
    this.ctx.fillRect(0, 0, 180, 400)
    let index = 0
    let len = this.renderList.length
    if (len > 0) &#123;
        // 重新扫描后index= 0；重新获取长度
        requestFrame(this.scan.bind(this))
        this.scanning = true
    &#125; else &#123;
        this.scanning = false
    &#125;
    while (index < len) &#123;
        const curRender = this.renderList[index]
        if (!curRender || !curRender.render || curRender.render.call(null, (Date.now() - curRender.timestamp) / curRender.duration)) &#123;
            // 动画已结束，删除绘制
            this.renderList.splice(index, 1)
            len--
        &#125; else &#123;
            index++
        &#125;
    &#125;
&#125;
// 点赞开始
public likeStart() &#123;
    // 初始化礼物数据、回调函数
    const render = this.createRender()
    const duration = this.getRandom(1500, 3000)
    this.renderList.push(&#123;
        render,
        duration,
        timestamp: Date.now()
    &#125;)
    if (!this.scanning) &#123;
        this.scanning = true
        requestFrame(this.scan.bind(this))
    &#125;
    return this
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">最后</h1>
<p>两种方式渲染点赞动画都已经完成。<a href="https://github.com/huazai128/react-mobx/tree/master/src/containers/views/Canvas/Like" target="_blank" rel="nofollow noopener noreferrer">完整代码</a></p>
<p>本文到此结束。希望对你有帮助。</p>
<p>小编第一次写文章文笔有限、才疏学浅，文中如有不正之处，万望告知。</p></div>  
</div>
            