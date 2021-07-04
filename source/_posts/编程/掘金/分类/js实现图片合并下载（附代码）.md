
---
title: 'js实现图片合并下载（附代码）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357e735041da46f792b74fca05e354a1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 19:49:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357e735041da46f792b74fca05e354a1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><a href="https://github.com/danygitgit/document-library" target="_blank" rel="nofollow noopener noreferrer">js实现图片合并下载（附代码）</a></h1>
<blockquote>
<p><strong>闲时要有吃紧的心思，忙时要有悠闲的趣味</strong></p>
</blockquote>
<p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<p><a id="user-content-catalog" href="https://juejin.cn/post/undefined">目录</a></p>
<ul>
<li>
<p><a href="https://juejin.cn/post/6980170760258060324#preface">前言</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6980170760258060324#main-body">正文</a></p>
<ul>
<li><a href="https://juejin.cn/post/6980170760258060324#chapter-1">一、实现步骤</a></li>
<li><a href="https://juejin.cn/post/6980170760258060324#chapter-2">二、代码实现</a></li>
</ul>
</li>
<li>
<p><a href="https://juejin.cn/post/6980170760258060324#summary">总结</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6980170760258060324#reference-documents">参考文档</a></p>
</li>
</ul>
<h1 data-id="heading-1"><a id="user-content-preface" href="https://juejin.cn/post/undefined">前言</a></h1>
<blockquote>
<p><a href="https://juejin.cn/post/6980170760258060324#catalog">返回目录</a></p>
</blockquote>
<p> 前些日子碰到一个需求，关于图像合并下载并转换为文件格式。综合考虑，决定使用Canvas实现，本文以记录实现流程，供大家参考。</p>
<p> 需求如下：</p>
<p> 用户上传图片，或者是传入图片url列表，根据图片数量合成新图片，一张平铺，二张并列，三张品字形，四张田字形，最后返回Blob对象或者Base64格式。</p>
<h1 data-id="heading-2"><a id="user-content-main-body" href="https://juejin.cn/post/undefined">正文</a></h1>
<h2 data-id="heading-3"><a id="user-content-chapter-1" href="https://juejin.cn/post/undefined">一、实现步骤</a></h2>
<blockquote>
<p><a href="https://juejin.cn/post/6980170760258060324#catalog">返回目录</a></p>
</blockquote>
<p> 实现步骤如下：</p>
<ol>
<li>获取用户上传图片列表，支持用户手动上传及传入图片url列表</li>
<li>处理图片列表。如果用户手动上传的图片，直接获取元素对象使用；对于图片url列表需要使用<code>new Image()</code>处理成对象列表再使用；</li>
<li>生成一块<code>canvas</code>画布，使用<code>drawImage</code>方法按照一定位置把我们的拓片画上去。</li>
<li>将生成的<code>canvas</code>画布按照所需格式返回（Blob对象或者Base64）</li>
<li>利用<code>a</code>标签实现下载</li>
</ol>
<h2 data-id="heading-4"><a id="user-content-chapter-2" href="https://juejin.cn/post/undefined">二、代码实现</a></h2>
<blockquote>
<p><a href="https://juejin.cn/post/6980170760258060324#catalog">返回目录</a></p>
</blockquote>
<p> 因为是蛮简单的一个功能实现，所以直接贴代码了。</p>
<p>Demo代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>实现图片合并下载<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.img_style</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">height</span>: auto;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">fieldset</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">onchange</span>=<span class="hljs-string">"imageUpload(this,'#firstImg')"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"firstImg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img_style"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">legend</span>></span>上传图1<span class="hljs-tag"></<span class="hljs-name">legend</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">fieldset</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">fieldset</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">onchange</span>=<span class="hljs-string">"imageUpload(this,'#secondImg')"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"secondImg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img_style"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">legend</span>></span>上传图2<span class="hljs-tag"></<span class="hljs-name">legend</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">fieldset</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">fieldset</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">onchange</span>=<span class="hljs-string">"imageUpload(this,'#thirdImg')"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"thirdImg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img_style"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">legend</span>></span>上传图3<span class="hljs-tag"></<span class="hljs-name">legend</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">fieldset</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">fieldset</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">onchange</span>=<span class="hljs-string">"imageUpload(this,'#fourthImg')"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"fourthImg"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img_style"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">legend</span>></span>上传图4<span class="hljs-tag"></<span class="hljs-name">legend</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">fieldset</span>></span>


  <span class="hljs-tag"><<span class="hljs-name">fieldset</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"clickPreview()"</span>></span>点击合成<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"clickDownload()"</span>></span>点击下载<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">fieldset</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'base64ObjBox'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>生成base64文件<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'blobObjBox'</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>生成file文件<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-comment"><!-- <canvas id="myCanvas" width="200" height="200" style="border:1px solid #c3c3c3;"></canvas> --></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">/**
  * <span class="hljs-doctag">@description </span>合并图片并返回文件方法
  * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Array&#125;</span> </span>imgsList  图片列表（url或者对象），必填
  * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Boolean&#125;</span> </span>isFileObj  是否返回文件对象，默认false，返回base64
  * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Number&#125;</span> </span>canvasWidth  生成图片宽度，默认200px
  * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Number&#125;</span> </span>canvasHeight  生成图片高度，默认200px
  * <span class="hljs-doctag">@return  </span>合并成的图片文件，base64或者file
  */</span>

  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">returnPicMerge</span>(<span class="hljs-params">imgsList, isFileObj = <span class="hljs-literal">false</span>, canvasWidth = <span class="hljs-number">200</span>, canvasHeight = <span class="hljs-number">200</span></span>) </span>&#123;
    <span class="hljs-comment">// 图片列表为空或者非数组，直接返回</span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(imgsList) || imgsList.length === <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 初始化图片列表</span>
    <span class="hljs-keyword">let</span> imgEles = []
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> (imgsList[<span class="hljs-number">0</span>]) === <span class="hljs-string">'object'</span>) &#123;
      <span class="hljs-comment">// 图片对象列表直接使用</span>
      imgEles = imgsList
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 图片链接列表需要处理成对象列表</span>
      <span class="hljs-keyword">let</span> imgSrcs = imgsList.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-keyword">let</span> image = <span class="hljs-keyword">new</span> Image()
        image.src = item + <span class="hljs-string">'?v='</span> + <span class="hljs-built_in">Math</span>.random() <span class="hljs-comment">// 处理缓存</span>
        image.crossOrigin = <span class="hljs-string">'*'</span> <span class="hljs-comment">// 支持跨域图片</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
          image.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            resolve(image)
          &#125;
        <span class="hljs-comment">//   image.onerror = function() &#123;</span>
        <span class="hljs-comment">//     let defaultImg = new Image();</span>
        <span class="hljs-comment">//     defaultImg.src = Config.publicTfsUrl + "/" + Config.defaultImg + '?v=' + Math.random();</span>
        <span class="hljs-comment">//     defaultImg.crossOrigin = '*' // 支持跨域图片</span>
        <span class="hljs-comment">//     defaultImg.onload = () => &#123;</span>
        <span class="hljs-comment">//         resolve(defaultImg);</span>
        <span class="hljs-comment">//     &#125;</span>
        &#125;);
      &#125;);
      imgEles = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all(imgSrcs);
    &#125;

    <span class="hljs-comment">// 初始化图片宽高及位置坐标</span>
    <span class="hljs-keyword">let</span> imgWidth = canvasWidth
    <span class="hljs-keyword">let</span> imgHeight = canvasHeight
    <span class="hljs-keyword">let</span> xCoordinate = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> yCoordinate = <span class="hljs-number">0</span>

    <span class="hljs-comment">// 创建canvas对象</span>
    <span class="hljs-keyword">let</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>);
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    <span class="hljs-keyword">let</span> ctx = canvas.getContext(<span class="hljs-string">"2d"</span>);

    <span class="hljs-comment">// 填充背景色</span>
    <span class="hljs-comment">// ctx.fillStyle = "#87CEEB";</span>
    <span class="hljs-comment">// ctx.fillRect(0, 0, canvasWidth, canvasHeight);</span>


    <span class="hljs-keyword">if</span> (imgEles.length === <span class="hljs-number">1</span>) &#123;
      <span class="hljs-comment">// 绘制图片，一张图铺满</span>
      ctx.drawImage(imgEles[<span class="hljs-number">0</span>], xCoordinate, yCoordinate, imgWidth, imgHeight);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (imgEles.length === <span class="hljs-number">2</span>) &#123;
      <span class="hljs-comment">// 两张图并列</span>
      imgWidth = canvasWidth / <span class="hljs-number">2</span>
      imgHeight = canvasHeight/<span class="hljs-number">2</span>
      yCoordinate = (canvasHeight - imgHeight) / <span class="hljs-number">2</span>
      imgEles.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        ctx.drawImage(item, xCoordinate, yCoordinate, imgWidth, imgHeight);
        xCoordinate += imgWidth
      &#125;);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (imgEles.length === <span class="hljs-number">3</span>) &#123;
      <span class="hljs-comment">// 三张图品字形</span>
      imgWidth = canvasWidth / <span class="hljs-number">2</span>
      imgHeight = canvasHeight / <span class="hljs-number">2</span>
      xCoordinate = (canvasWidth - imgWidth) / <span class="hljs-number">2</span>
      imgEles.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (index === <span class="hljs-number">1</span>) &#123;
          yCoordinate += imgHeight
          xCoordinate = (canvasWidth - imgWidth * <span class="hljs-number">2</span>) / <span class="hljs-number">2</span>
        &#125;
        ctx.drawImage(item, xCoordinate, yCoordinate, imgWidth, imgHeight);
        xCoordinate += imgWidth
      &#125;);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (imgEles.length === <span class="hljs-number">4</span>) &#123;
      <span class="hljs-comment">// 四张图田字形</span>
      imgWidth = canvasWidth / <span class="hljs-number">2</span>
      imgHeight = canvasHeight / <span class="hljs-number">2</span>
      imgEles.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (index === <span class="hljs-number">2</span>) &#123;
          yCoordinate += imgHeight
          xCoordinate = (canvasWidth - imgWidth * <span class="hljs-number">2</span>) / <span class="hljs-number">2</span>
        &#125;
        ctx.drawImage(item, xCoordinate, yCoordinate, imgWidth, imgHeight);
        xCoordinate += imgWidth
      &#125;);
    &#125;

    <span class="hljs-comment">// 返回文件</span>
    <span class="hljs-keyword">if</span> (isFileObj) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        canvas.toBlob(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">blobObj</span>) </span>&#123;
          resolve(blobObj)
        &#125;)
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> canvas.toDataURL(<span class="hljs-string">'image/png'</span>)
    &#125;
  &#125;
  <span class="hljs-comment">// 点击上传图片</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">imageUpload</span>(<span class="hljs-params">imgFile, id</span>) </span>&#123;
    <span class="hljs-keyword">let</span> f = imgFile.files[<span class="hljs-number">0</span>];<span class="hljs-comment">//获取上传的图片文件</span>
    <span class="hljs-keyword">let</span> filereader = <span class="hljs-keyword">new</span> FileReader();<span class="hljs-comment">//新建一个图片对象</span>
    filereader.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;<span class="hljs-comment">//图片加载完成后执行的函数</span>
      <span class="hljs-keyword">let</span> srcpath = event.target.result;<span class="hljs-comment">//这里获取图片的路径（图片会被转为base6格式）</span>
      <span class="hljs-built_in">document</span>.querySelector(id).setAttribute(<span class="hljs-string">"src"</span>, srcpath);<span class="hljs-comment">//将获取的图片插入到相应的图片元素里</span>
    &#125;;
    filereader.readAsDataURL(f);<span class="hljs-comment">//读取图片（将插入的图片读取显示出来）</span>
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getImgSize</span>(<span class="hljs-params">str</span>) </span>&#123;
    <span class="hljs-comment">//获取base64图片大小，返回KB数字</span>
    <span class="hljs-comment">// var str = base64url.replace('data:image/jpeg;base64,', '');//这里根据自己上传图片的格式进行相应修改</span>
    <span class="hljs-keyword">var</span> strLength = str.length;
    <span class="hljs-keyword">var</span> fileLength = <span class="hljs-built_in">parseInt</span>(strLength - (strLength / <span class="hljs-number">8</span>) * <span class="hljs-number">2</span>);
    <span class="hljs-comment">// 由字节转换为KB</span>
    <span class="hljs-keyword">var</span> size = <span class="hljs-string">""</span>;
    size = (fileLength / <span class="hljs-number">1024</span>/<span class="hljs-number">1024</span>).toFixed(<span class="hljs-number">2</span>);
    
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">parseInt</span>(size);

  &#125;

  <span class="hljs-comment">// 点击预览</span>
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickPreview</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 获取图片列表</span>
    <span class="hljs-keyword">let</span> imgsList = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">"img_style"</span>)).filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (item.src) &#123;
        <span class="hljs-keyword">return</span> item
      &#125;
    &#125;);
    <span class="hljs-comment">// 如果用户没有上传文件，初始化赋值</span>
    <span class="hljs-keyword">if</span> (imgsList.length === <span class="hljs-number">0</span>) &#123;
      imgsList = [
        <span class="hljs-string">'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3080163631,1117627422&fm=26&gp=0.jpg'</span>,
        <span class="hljs-string">'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fyouimg1.c-ctrip.com%2Ftarget%2Ftg%2F374%2F780%2F501%2F559858dc54b34a979c8816a8377fcf01.jpg&refer=http%3A%2F%2Fyouimg1.c-ctrip.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1625888610&t=9a05b684a1f8426b8f3ccddc236ec271'</span>,
      ]
    &#125;

    <span class="hljs-comment">// 调用方法，获取base64</span>
    <span class="hljs-keyword">let</span> base64Obj = <span class="hljs-keyword">await</span> returnPicMerge(imgsList)

    <span class="hljs-comment">// 调用方法，获取blob</span>
    <span class="hljs-keyword">let</span> blobObj = <span class="hljs-keyword">await</span> returnPicMerge(imgsList, <span class="hljs-literal">true</span>,<span class="hljs-number">200</span>,<span class="hljs-number">200</span>)

    <span class="hljs-keyword">var</span> strLength = base64Obj.length;
    <span class="hljs-keyword">var</span> fileLength = <span class="hljs-built_in">parseInt</span>(strLength - (strLength / <span class="hljs-number">8</span>) * <span class="hljs-number">2</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'base64Obj'</span>, base64Obj)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'base64Obj大小'</span>, fileLength / <span class="hljs-number">1024</span>/<span class="hljs-number">1024</span>)

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'blobObj'</span>, blobObj)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'blobObj大小'</span>, blobObj.size/<span class="hljs-number">1024</span>/<span class="hljs-number">1024</span>)
    

    <span class="hljs-keyword">let</span> image1, image2
    <span class="hljs-keyword">let</span> base64ObjBox = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'base64ObjBox'</span>);
    <span class="hljs-keyword">let</span> blobObjBox = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'blobObjBox'</span>);
    <span class="hljs-comment">// 没有图片元素就创建，有就更新</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'image1'</span>)) &#123;
      image1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'image1'</span>)
      image1.src = base64Obj
    &#125; <span class="hljs-keyword">else</span> &#123;
      image1 = <span class="hljs-keyword">new</span> Image()
      image1.src = base64Obj
      image1.setAttribute(<span class="hljs-string">'id'</span>, <span class="hljs-string">'image1'</span>);
      base64ObjBox.appendChild(image1);
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'image2'</span>)) &#123;
      image2 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'image2'</span>)
      image2.src = <span class="hljs-built_in">window</span>.URL.createObjectURL(blobObj)
    &#125; <span class="hljs-keyword">else</span> &#123;
      image2 = <span class="hljs-keyword">new</span> Image()
      image2.src = <span class="hljs-built_in">window</span>.URL.createObjectURL(blobObj)
      image2.setAttribute(<span class="hljs-string">'id'</span>, <span class="hljs-string">'image2'</span>);
      blobObjBox.appendChild(image2);
    &#125;
  &#125;
  <span class="hljs-comment">// 点击下载</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickDownload</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">let</span> img = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"image1"</span>);
    <span class="hljs-keyword">let</span> link = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>);<span class="hljs-comment">//创建一个a标签</span>
    link.download = <span class="hljs-string">'my-image-name.jpg'</span>;<span class="hljs-comment">//a标签增加一个download属性，属性值（my-image-name.jpg）就是合成下载后的文件名</span>
    link.href = img.src;<span class="hljs-comment">//将路径赋给a标签的href</span>
    link.click();<span class="hljs-comment">//模拟a标签被点击，这样就可以下载了</span>
  &#125;

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5"><a id="user-content-summary" href="https://juejin.cn/post/undefined">总结</a></h1>
<blockquote>
<p><a href="https://juejin.cn/post/6980170760258060324#catalog">返回目录</a></p>
</blockquote>
<p> 其实自己实现一些功能也是一个蛮不错的体验。可以加强对一些功能的熟悉以及对一些API的认识，也可以为自己积累一些备用代码，免得如后万一碰到还要耽误时间到处找资料。</p>
<p> 路漫漫其修远兮，与诸君共勉。</p>
<p><strong>后记：Hello 小伙伴们，如果觉得本文还不错，记得点个赞或者给个 star，你们的赞和 star 是我编写更多更丰富文章的动力！<a href="https://github.com/danygitgit/document-library" target="_blank" rel="nofollow noopener noreferrer">GitHub 地址</a></strong></p>
<h1 data-id="heading-6">文档协议</h1>
<blockquote>
<p><a rel="nofollow noopener noreferrer" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank"><img alt="知识共享许可协议" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/357e735041da46f792b74fca05e354a1~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></a><br><a href="https://juejin.cn/post/undefined"><strong>db</strong> 的文档库</a> 由 <a href="https://juejin.cn/post/db" rel="cc:attributionURL">db</a> 采用 <a rel="nofollow noopener noreferrer" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a>进行许可。<br>基于<a href="https://github.com/danygitgit" rel="nofollow noopener noreferrer" target="_blank"></a><a href="https://github.com/danygitgit" target="_blank" rel="nofollow noopener noreferrer">github.com/danygitgit</a>上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" rel="nofollow noopener noreferrer" target="_blank"></a><a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            