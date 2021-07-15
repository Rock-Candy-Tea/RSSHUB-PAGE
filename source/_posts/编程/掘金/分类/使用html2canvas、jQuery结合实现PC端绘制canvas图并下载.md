
---
title: '使用html2canvas、jQuery结合实现PC端绘制canvas图并下载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69ac6535e3964112866bd9b4968c0a61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 18:53:35 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69ac6535e3964112866bd9b4968c0a61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前言：</p>
<ul>
<li>文本虽然所提到的是在jQuery中使用，但是在vue等框架中实现PC端绘制canvas图并下载依然是适用的。</li>
<li>本文使用的<code>html2canvas版本是：1.0.0-rc.7</code>。</li>
<li>本文接口返回采用的图片地址格式是base64的，主要是为了兼容所有浏览器，而且下载速度挺快。若不想如此粗暴，让性能体验更佳，则可以分接口处理，但是注意IE相关的浏览器是不兼容的哦；如谷歌等浏览器可以处理成图片url地址进行返回，IE相关的浏览器处理为另外一个接口则返回base64格式的。</li>
</ul>
</blockquote>
<p>贴出本作者处理的具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 判断是否是isIE11或isEdge或isLessIE11 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isIE11Fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> userAgent = navigator.userAgent; <span class="hljs-comment">//取得浏览器的userAgent字符串</span>
    <span class="hljs-keyword">var</span> isLessIE11 = userAgent.indexOf(<span class="hljs-string">"compatible"</span>) > -<span class="hljs-number">1</span> && userAgent.indexOf(<span class="hljs-string">"MSIE"</span>) > -<span class="hljs-number">1</span>;
    <span class="hljs-comment">// 判断是否为IE的Edge浏览器</span>
    <span class="hljs-keyword">var</span> isEdge = userAgent.indexOf(<span class="hljs-string">"Edge"</span>) > -<span class="hljs-number">1</span> && !isLessIE11;
    <span class="hljs-comment">// 判断是否为IE11浏览器</span>
    <span class="hljs-keyword">var</span> isIE11 = userAgent.indexOf(<span class="hljs-string">"Trident"</span>) > -<span class="hljs-number">1</span> && userAgent.indexOf(<span class="hljs-string">"rv:11.0"</span>) > -<span class="hljs-number">1</span>;

    <span class="hljs-keyword">return</span> isLessIE11 || isIE11 || isEdge;
&#125;;
<span class="hljs-comment">// 请求接口，举例子：</span>
<span class="hljs-keyword">var</span> api = <span class="hljs-string">"xxx接口url地址"</span>; <span class="hljs-comment">// 返回</span>
<span class="hljs-keyword">if</span> (isLessIE11 || isIE11 || isEdge) &#123;
  api += <span class="hljs-string">"&is_base64image=1"</span>; <span class="hljs-comment">// 返回base64格式图片</span>
&#125;
<span class="hljs-comment">// 请求接口</span>
jqueryAjaxGet(api, <span class="hljs-literal">null</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
    <span class="hljs-comment">// 里边进行相关的逻辑处理等</span>
    <span class="hljs-keyword">if</span> (res.status == <span class="hljs-number">1</span>) &#123;
        _this.poster = res.data;
        <span class="hljs-keyword">var</span> imgarr = [_this.poster.background_img];
        <span class="hljs-keyword">if</span>(_this.poster.goods_list.length) &#123;
          $.each(_this.poster.goods_list, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">i, item</span>)</span>&#123;
            imgarr.push(item.goods_image);
          &#125;)
        &#125;
        downloadImg(<span class="hljs-string">".poster_con"</span>, <span class="hljs-string">'poster'</span>, imgarr);
    &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-0">一、安装</h1>
<p>script形式引入“<code>html2canvas.min.js</code>”，实际路径按项目的来（记得修改路径~）</p>
<pre><code class="hljs language-js copyable" lang="js">script src=<span class="hljs-string">"xxx/..../common/html2canvas.min.js"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">二、使用</h1>
<h2 data-id="heading-2">封装成公共的方法进行使用</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@Author</span>: acaiEncode 
 * <span class="hljs-doctag">@File</span>: 保存图片or保存海报
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>canvasImgClass  截图的包裹的dom对象（原生）
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>imgName 图片名称
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>imgArr dom图片数组
 * 提示：前提需要先引入html2canvas.js，版本号：1.0.0-rc.7
 * 使用：downloadImg(".poster_con", 'poster', imgarr);
 */</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">downloadImg</span>(<span class="hljs-params">canvasImgClass, imgName, imgArr</span>) </span>&#123;
    loading.showloading();
    <span class="hljs-keyword">var</span> canEle = $(canvasImgClass)[<span class="hljs-number">0</span>];   <span class="hljs-comment">// 获取截图的包裹的dom对象（原生）</span>
    <span class="hljs-keyword">var</span> width = canEle.offsetWidth; <span class="hljs-comment">// 获取dom宽</span>
    <span class="hljs-keyword">var</span> height = canEle.offsetHeight;   <span class="hljs-comment">// 获取dom高</span>
    <span class="hljs-keyword">var</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>);  <span class="hljs-comment">// 创建一个canvas节点</span>
    <span class="hljs-comment">// var scale = height / (height * window.devicePixelRatio); // 定义任意放大倍数 支持小数</span>
    <span class="hljs-keyword">var</span> scale = <span class="hljs-built_in">window</span>.devicePixelRatio; <span class="hljs-comment">// 定义任意放大倍数 支持小数</span>
    canvas.width = width * scale; <span class="hljs-comment">// 定义canvas 宽度 * 缩放</span>
    canvas.height = height * scale; <span class="hljs-comment">// 定义canvas高度 *缩放</span>
    <span class="hljs-keyword">var</span> content = canvas.getContext(<span class="hljs-string">"2d"</span>);
    content.scale(scale, scale); <span class="hljs-comment">//获取context,设置scale </span>
    <span class="hljs-comment">// var rect = canEle.getBoundingClientRect(); //获取元素相对于视察的偏移量</span>
    <span class="hljs-comment">// content.translate(-rect.left, -rect.top); //设置context位置，值为相对于视窗的偏移量负值，让图片复位</span>
    <span class="hljs-keyword">var</span> options = &#123;
        <span class="hljs-attr">scale</span>: scale, <span class="hljs-comment">// 添加的scale 参数</span>
        <span class="hljs-attr">canvas</span>: canvas, <span class="hljs-comment">// 自定义 canvas</span>
        <span class="hljs-attr">width</span>: width, <span class="hljs-comment">// dom 原始宽度</span>
        <span class="hljs-attr">height</span>: height,
        <span class="hljs-attr">x</span>: <span class="hljs-built_in">window</span>.pageXOffset, <span class="hljs-comment">// 裁剪画布X坐标</span>
        <span class="hljs-attr">y</span>: <span class="hljs-built_in">window</span>.pageYOffset,
        <span class="hljs-comment">// foreignObjectRendering: true, // 最主要是这句话，官方给出解释是否在浏览器支持的情况下使用ForeignObject渲染，</span>
        <span class="hljs-comment">// scrollX: 0, // 渲染元素时要使用的x滚动位置（例如，如果Element使用position: fixed）</span>
        <span class="hljs-comment">// scrollY: 0,</span>
        <span class="hljs-attr">tainttest</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 检测每张图片都已经加载完成</span>
        <span class="hljs-attr">useCORS</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 【重要】开启跨域配置</span>
    &#125;;
    <span class="hljs-comment">// 重点：接口图片返回较多时需等图片加载完成才进行截图描绘</span>
    <span class="hljs-keyword">if</span>(imgArr && imgArr.length) &#123;
        <span class="hljs-keyword">var</span> img = [],
        flag = <span class="hljs-number">0</span>,
        mulitImg = imgArr;
        <span class="hljs-keyword">var</span> imgTotal = mulitImg.length;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < imgTotal; i++) &#123;
            img[i] = <span class="hljs-keyword">new</span> Image()
            img[i].onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-comment">//第i张图片加载完成</span>
                flag++
                <span class="hljs-keyword">if</span> (flag == imgTotal) &#123;
                    <span class="hljs-comment">// 全部加载完成,进行画布的裁剪</span>
                    getCanvas(canvas,canEle,options,imgName)
                &#125;
            &#125;
            img[i].src = mulitImg[i];
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 画布的裁剪</span>
        getCanvas(canvas,canEle,options,imgName)
    &#125;
&#125;;
<span class="hljs-comment">/**
 * 画布生成后下载图片
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>canvas 画布
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>canEle dom对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>options 配置项
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>imgName 图片名称
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCanvas</span>(<span class="hljs-params">canvas, canEle, options, imgName</span>) </span>&#123;
    <span class="hljs-keyword">var</span> canvas = canvas;
    html2canvas(canEle,options).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">canvas</span>) </span>&#123;
        <span class="hljs-keyword">var</span> context = canvas.getContext(<span class="hljs-string">'2d'</span>);
        <span class="hljs-comment">// 关闭抗锯齿 保证生成的分享图是清晰的</span>
        context.mozImageSmoothingEnabled = <span class="hljs-literal">false</span>;
        context.webkitImageSmoothingEnabled = <span class="hljs-literal">false</span>;
        context.msImageSmoothingEnabled = <span class="hljs-literal">false</span>;
        context.imageSmoothingEnabled = <span class="hljs-literal">false</span>;
        <span class="hljs-keyword">var</span> imgDataUrl = canvas
        .toDataURL(<span class="hljs-string">"image/"</span> + <span class="hljs-string">".jpg"</span>)
        .replace(<span class="hljs-string">"image/"</span> + <span class="hljs-string">".jpg"</span>, <span class="hljs-string">"image/octet-stream"</span>); <span class="hljs-comment">// 得到图片base64编码数据</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.navigator.msSaveOrOpenBlob) &#123;
            <span class="hljs-comment">// 允许用户在客户端上保存文件</span>
            <span class="hljs-keyword">var</span> bstr = atob(imgDataUrl.split(<span class="hljs-string">","</span>)[<span class="hljs-number">1</span>]);
            <span class="hljs-keyword">var</span> n = bstr.length;
            <span class="hljs-keyword">var</span> u8arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Uint8Array</span>(n);
            <span class="hljs-keyword">while</span> (n--) &#123;
              u8arr[n] = bstr.charCodeAt(n);
            &#125;
            <span class="hljs-keyword">var</span> blob = <span class="hljs-keyword">new</span> Blob([u8arr]);
            <span class="hljs-built_in">window</span>.navigator.msSaveOrOpenBlob(blob, imgName + <span class="hljs-string">"."</span> + <span class="hljs-string">"jpg"</span>);
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 这里就按照chrome等新版浏览器来处理保存图片</span>
            <span class="hljs-keyword">var</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"a"</span>);
            a.href = imgDataUrl;
            <span class="hljs-comment">// a.id = 'imgDownBtn';</span>
            a.setAttribute(<span class="hljs-string">"download"</span>, imgName+<span class="hljs-string">".jpg"</span>);
            a.click();
            $().remove(a);
            <span class="hljs-comment">// document.remove($('#imgDownBtn'));</span>
          &#125;
          loading.hideloading();
    &#125;);
&#125;
<span class="hljs-comment">// loading</span>
<span class="hljs-keyword">var</span> loading = &#123;
    <span class="hljs-attr">showloading</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">msg</span>) </span>&#123;
        <span class="hljs-keyword">var</span> hadMask = $(<span class="hljs-string">"body div"</span>).hasClass(<span class="hljs-string">".win-mask"</span>);
        <span class="hljs-keyword">if</span> (hadMask) &#123;
            $(<span class="hljs-string">".win-mask"</span>).show();
        &#125; <span class="hljs-keyword">else</span> &#123;
            loading.innerloading(msg);
        &#125;
    &#125;,
    <span class="hljs-attr">hideloading</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        $(<span class="hljs-string">".win-mask"</span>).remove();
    &#125;,
    <span class="hljs-attr">innerloading</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">msg</span>) </span>&#123;
        <span class="hljs-keyword">var</span> def_msg = <span class="hljs-string">""</span>;
        def_msg = msg ? msg : <span class="hljs-string">'正在加载中...'</span>;
        $(<span class="hljs-string">"body"</span>).append(<span class="hljs-string">'<div class="win-mask">\
                              <div class="loading-box">\
                                  <div class="loadings"></div>&nbsp;&nbsp;'</span> + def_msg + <span class="hljs-string">'\
                              </div>\
                          </div>'</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">具体页面上的详细使用</h2>
<pre><code class="hljs language-html copyable" lang="html">// html

<span class="hljs-tag"><<span class="hljs-name">section</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"liveShareWin"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"commonPopup"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"z-index: 999; display: none"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"commonPopup-container"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"z-index: 8000; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); display: none; margin-left: -500px; margin-top: -296.5px;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"commonPopup-header"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>分享<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"close-img commonPopup-close-js"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"commonPopup-body"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"col-md-6 leftBox"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>直播间小程序码<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"liveCodeImg"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">""</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"liveCode"</span>></span>  
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-comment"><!-- <button class="saaveCodeBtn imgSaveBtn">保存图片</button> --></span>
            <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"saveCodeBtn imgSaveBtn"</span> <span class="hljs-attr">download</span>=<span class="hljs-string">"直播间小程序码.jpg"</span>></span>保存图片<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"col-md-6 rightBox"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>直播间分享海报<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"posterShare"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bannerImg"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">""</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"banner"</span>></span>  
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h6</span>></span><span class="hljs-tag"></<span class="hljs-name">h6</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footerContent row"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"col-md-8"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"timesBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tips"</span>></span>长按识别小程序码，观看直播<span class="hljs-tag"></<span class="hljs-name">p</span>></span>  
              <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"col-md-4"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"miniCode"</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">""</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"miniCode"</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"savePosterBtn imgSaveBtn"</span>></span>保存图片<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">// css

<span class="hljs-selector-id">#liveShareWin</span> <span class="hljs-selector-class">.row</span>><span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">text-align</span>: center;
&#125;

<span class="hljs-selector-id">#liveShareWin</span> <span class="hljs-selector-class">.row</span>><span class="hljs-selector-class">.rightBox</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">border-right</span>: <span class="hljs-number">1px</span> dashed <span class="hljs-number">#ccc</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">94px</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-id">#liveShareWin</span> <span class="hljs-selector-tag">h4</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
    <span class="hljs-attribute">font-weight</span>: bold;
    <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">40px</span>;
&#125;

<span class="hljs-selector-class">.liveCodeImg</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">180px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">180px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">40px</span>;
&#125;

<span class="hljs-selector-class">.liveCodeImg</span>><span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="hljs-selector-id">#beginnerGuide</span> <span class="hljs-selector-class">.openQuliyBtn</span>,
<span class="hljs-selector-id">#liveShareWin</span> <span class="hljs-selector-class">.imgSaveBtn</span> &#123;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">160px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fe5043</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-selector-class">.saveCodeBtn</span> &#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">60px</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">40px</span>;
&#125;

<span class="hljs-selector-class">.posterShare</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-comment">/* height: 395px; */</span>
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">13</span>) <span class="hljs-number">0px</span> <span class="hljs-number">0px</span> <span class="hljs-number">13px</span> <span class="hljs-number">1px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20px</span>;
&#125;

<span class="hljs-selector-class">.bannerImg</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">240px</span>;
&#125;
<span class="hljs-selector-class">.bannerImg</span>><span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;

<span class="hljs-selector-class">.savePosterBtn</span> &#123;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">30px</span>;
&#125;

<span class="hljs-selector-class">.posterShare</span> <span class="hljs-selector-tag">h6</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">20px</span> <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
    <span class="hljs-attribute">text-align</span>: left;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;    <span class="hljs-comment">/* 一定要固定高度，火狐和ie浏览器超过省略，但是点点不会出来 */</span> 
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">word-break</span>: break-all;
    <span class="hljs-comment">/* white-space: nowrap; */</span>
    <span class="hljs-attribute">overflow</span>: hidden;
    <span class="hljs-comment">/* text-overflow: ellipsis; */</span>
&#125;
<span class="hljs-selector-class">.footerContent</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span> <span class="hljs-number">10px</span>;
&#125;

<span class="hljs-selector-class">.footerContent</span>><span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;

<span class="hljs-selector-class">.footerContent</span> <span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">text-align</span>: left;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">20px</span>
&#125;

<span class="hljs-selector-class">.footerContent</span> <span class="hljs-selector-tag">p</span><span class="hljs-selector-class">.tips</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">10px</span>
&#125;

<span class="hljs-selector-class">.footerContent</span> <span class="hljs-selector-tag">p</span><span class="hljs-selector-class">.tips</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>: block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">2px</span>;
    <span class="hljs-attribute">background-color</span>: red;
    <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">5px</span>;
&#125;

<span class="hljs-comment">/* .col-md-8 &#123;
    border-right: 1px dashed #fedada;
&#125; */</span>

<span class="hljs-selector-class">.miniCode</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">62px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">62px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">6px</span> auto;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">20px</span>;
&#125;
<span class="hljs-selector-class">.miniCode</span>><span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// js</span>
<span class="hljs-keyword">var</span> room_mini_code = <span class="hljs-string">''</span>;
<span class="hljs-keyword">var</span> miniCodeArr,
poseterBannerArr = [];
$(<span class="hljs-string">'.liveManage .tbody'</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'.shareBtn'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> room_id = $(<span class="hljs-built_in">this</span>).data(<span class="hljs-string">'roomid'</span>);
    jqueryAjaxPost(api.shareLive, &#123;<span class="hljs-attr">room_id</span>: room_id&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        miniCodeArr,
        poseterBannerArr  = [];
        <span class="hljs-keyword">if</span>(res.status) &#123;
            <span class="hljs-keyword">var</span> res = res.data;
            miniCodeArr = [res.room_mini_code];
            poseterBannerArr = [res.room_mini_code, res.share_img];
            room_mini_code = res.room_mini_code;
            $(<span class="hljs-string">'#liveShareWin .liveCodeImg>img'</span>).prop(<span class="hljs-string">'src'</span>, res.room_mini_code);
            <span class="hljs-comment">// $('#liveShareWin .saveCodeBtn').prop('href', res.room_mini_code); // 直播间小程序码</span>

            $(<span class="hljs-string">'#liveShareWin .miniCode>img'</span>).prop(<span class="hljs-string">'src'</span>, res.room_mini_code);
            $(<span class="hljs-string">'#liveShareWin .bannerImg>img'</span>).prop(<span class="hljs-string">'src'</span>, res.share_img);
            $(<span class="hljs-string">'#liveShareWin .posterShare>h6'</span>).html(res.name);
            <span class="hljs-keyword">var</span> times = res.start_time + <span class="hljs-string">'&nbsp;-&nbsp;'</span> + res.end_time;
            $(<span class="hljs-string">'#liveShareWin .footerContent .timesBox'</span>).html(times);
            liveShareWin.show();
        &#125; <span class="hljs-keyword">else</span> &#123;
            alert(res.msg);
        &#125;
    &#125;);
&#125;);
<span class="hljs-comment">// 保存图片-download</span>
$(<span class="hljs-string">'#liveShareWin .saveCodeBtn'</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// （-html2canvas实现方式）</span>
<span class="hljs-comment">//     downloadImg('#liveShareWin .liveCodeImg', '小程序码', miniCodeArr);</span>
    <span class="hljs-keyword">if</span>(room_mini_code) &#123;
        init.compADown(room_mini_code, <span class="hljs-string">'直播间小程序码'</span>);
    &#125;
&#125;)
$(<span class="hljs-string">'#liveShareWin .savePosterBtn'</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    downloadImg(<span class="hljs-string">'#liveShareWin .posterShare'</span>, <span class="hljs-string">'海报'</span>, poseterBannerArr);
    <span class="hljs-comment">// liveShareWin.hide();</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果图：</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69ac6535e3964112866bd9b4968c0a61~tplv-k3u1fbpfcp-watermark.image" alt="poster_eg.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">三、遇到bug及对策</h1>
<h2 data-id="heading-5">1、在jQuery中<code>引入使用html2vanvas.js</code>，在IE浏览器会有出现一个报错：<code>SCRIPT5009: “Promise”</code>未定义</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76dcd1eb944c4831bd152d7bc1909ccd~tplv-k3u1fbpfcp-watermark.image" alt="error5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方案：引入<code>es6-promise.auto.min.js</code>插件进行处理。</p>
<h2 data-id="heading-6">2、jQuery配合html2canvas 使用时 报错<code> Uncaught (in promise) Provided element is not within a Document</code></h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4544708ec7c74b44a933fe4a20a2eb7c~tplv-k3u1fbpfcp-watermark.image" alt="error11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原因是：html2canvas接收的是 一个 js DOM 元素而不是 一个 jQuery DOM对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> canEle = $(canvasImgClass); <span class="hljs-comment">// jquery 获取元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解决思路：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> canEle = $(canvasImgClass)[<span class="hljs-number">0</span>];   <span class="hljs-comment">// 获取截图的包裹的dom对象（原生）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3、使用<code>img = new Image(); img.onload = function() &#123;&#125;</code>后html2canvas出现以下报错：</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb983984c3db44299f4d11837f02cc43~tplv-k3u1fbpfcp-watermark.image" alt="error12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>配置项加入：</strong></p>
<pre><code class="hljs language-js copyable" lang="js">foreignObjectRendering: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 最主要是这句话，官方给出解释是否在浏览器支持的情况下使用ForeignObject渲染，</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错虽然解决，但是出现另外的问题：图片无法显示，绘图错乱。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5409ede2556744118ab832a9b0d02ae7~tplv-k3u1fbpfcp-watermark.image" alt="error13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过排查，发现主要原因是：由如下代码导致图片还在onload，而画布还没有开始画，就隐藏了，因此画布就没有高度/宽度，以至于报错，注释后，则没有报错了。</p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">"#poster_body"</span>).attr(<span class="hljs-string">"style"</span>, <span class="hljs-string">"display:none;"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>因此得出结论：必须是dom可视才能很好的进行使用html2canvas截图生成海报！</code></strong></p>
<h2 data-id="heading-8">4、html2canvas对两行省略不识别，会直接丢弃，出来空白的结果；而一行省略的话，点点也是不识别的，会直接切掉文字</h2>
<blockquote>
<p><strong>解决方案：</strong></p>
<p>（1）一定要省略的话就用伪类做成点点；</p>
<p>（2）修改方案，不要省略符。</p>
</blockquote>
<h2 data-id="heading-9">5、html2canvas对虚线无效，会把虚线识别为实线展示出来</h2>
<blockquote>
<p>解决方案参考：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_34015860%2Farticle%2Fdetails%2F85982820" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_34015860/article/details/85982820" ref="nofollow noopener noreferrer">html2canvas 实现dashed虚线边框</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_34015860%2Farticle%2Fdetails%2F85982820" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_34015860/article/details/85982820" ref="nofollow noopener noreferrer">html2canvas 虚线渲染为实心的問題</a></p>
</blockquote>
<p>解决方案（本文采用的方案）：不用虚线或者改为实线！（一定要使用需要用虚线的客官，可以尝试贴出来解决的方案）。</p>
<h2 data-id="heading-10">6、弹窗使用html2canvas后一直都是空白的！</h2>
<p>原因是：截取区域在弹窗</p>
<p>解决方案：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d81d4fad24449a2bef4dad9bcbdb8fa~tplv-k3u1fbpfcp-watermark.image" alt="options.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">番外：移动端使用html2canvas进行生成海报并下载图片</h1>
<p>1、pc端所使用的方式在移动端在使用时，出现不适配兼容所有移动端的各个浏览器的问题。</p>
<p>目前qq打开h5页面，则前提需要安装qq浏览器，则可以进行下载，UC等类型的浏览器可以下载；</p>
<p>微信内置浏览器不兼容，原因其不支持下载文件的原因，要解决此问题。</p>
<p>具体的解决方案可参考以下：（主要是通过跳转第三方浏览器即可使用）</p>
<p>（1）<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fzaaakkmnb12%2Fp%2F9543400.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/zaaakkmnb12/p/9543400.html" ref="nofollow noopener noreferrer">微信内置浏览器不支持下载文件应用的解决方法</a></p>
<p>（2）<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fcnnrot984%2Farticle%2Fdetails%2F88554979" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/cnnrot984/article/details/88554979" ref="nofollow noopener noreferrer">微信内置浏览器不支持下载的解决方案 微信点击链接直接下载app安装包功能实现方式</a></p>
<p>（3）<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fyuerdong%2Fp%2F9768054.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/yuerdong/p/9768054.html" ref="nofollow noopener noreferrer">使用h5 标签 href='url' download 下载踩过的坑</a></p>
<p>其次，h5内嵌到自己的app上也有问题：安卓能够进行下载图片，前提是要传生成好的图片过去，但是安卓是不能够下载的，只能长按保存图片！总结如下：</p>
<blockquote>
<p><strong><code>Android 可以点击下载保存</code></strong></p>
<p><strong><code>IOS 只能长按保存</code></strong></p>
</blockquote>
<p>2、因此鉴于以上所描述的种种问题，若移动端想要实现海报的下载图片功能，又能够友好的兼容移动端端各个端，<strong>采用的最佳方案就是把html2canvas生成的海报图片，展示在页面上，引导用户进行长按保存图片。</strong></p>
<p><strong>效果案例图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9954d35285e4b75bac9397398eb0d74~tplv-k3u1fbpfcp-watermark.image" alt="banner2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体代码参考：
[html2canvas在vue2中的应用-移动端](html2canvas在vue2中的应用-移动端 #掘金文章# <a href="https://juejin.cn/post/6983870121949265950" target="_blank" title="https://juejin.cn/post/6983870121949265950">juejin.cn/post/698387…</a>)</p></div>  
</div>
            