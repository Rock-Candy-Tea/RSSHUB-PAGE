
---
title: 'Cordova screenshot IOS 截屏无效'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9432'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 06:38:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=9432'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一、简介 cordova-screenshot</h4>
<p><a href="https://github.com/gitawego/cordova-screenshot" target="_blank" rel="nofollow noopener noreferrer">cordova-screenshot</a> 为 cordova 截屏插件， 适用于<code>Android IOS</code></p>
<p>基本用法：</p>
<pre><code class="copyable">navigator.screenshot.save((error,res) => &#123;
  if(error)&#123;
    console.error(error);
  &#125;else&#123;
    console.log('ok',res.filePath); // 图片路径
  &#125;
&#125;,'jpg',50);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方推荐用法只适用于 Android，在 IOS 会出现截屏无效的情况</p>
<p><strong>原因：截屏保存的图片路径并不是在相册，而是在 tem 一个路径</strong></p>
<h4 data-id="heading-1">二、 解决 IOS 截屏失效</h4>
<blockquote>
<p>解决思路：先用 img 标题，src 指向 res.filePath 保存的图片路径，再调用  Canvas2ImagePlugin 插件，使用 Canvas 保存至相册</p>
</blockquote>
<ol>
<li>安装 <code>cordova plugin add https://github.com/devgeeks/Canvas2ImagePlugin.git</code></li>
<li></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"qr-box"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"isCordova === true"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">van-button</span>
    @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleSaveQrcode"</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"qr-btn"</span>
    <span class="hljs-attr">color</span>=<span class="hljs-string">"linear-gradient(to right, #E5CC87, #C39C69)"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"qr-recharge"</span>></span>保存二维码<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">van-button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"hideCanvas"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myCanvas"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"myCanvas"</span>></span><span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"hideImg"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"myImg"</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"fileSrc"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.hideImg</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">999</span>;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">9999px</span>;
&#125;

<span class="hljs-selector-class">.hideCanvas</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">999</span>;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">9999px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// vue
data () &#123;
    return &#123;
      fileSrc: ''
    &#125;
  &#125;,
methods: &#123;
    // 截屏操作
    handleSaveQrcode () &#123;
      // 调用 cordova-screenshot 方法
      navigator.screenshot.save((error, res) => &#123;
        if (error) &#123;
          Toast.error(error)
        &#125; else &#123;
          // 判断UA，ios android 情况不同
          var u = navigator.userAgent; var app = navigator.appVersion
          var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Linux') > -1 // g
          var isIOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/) // ios终端

          if (isIOS) &#123;
            // 针对IOS做处理 res.filePath 为路径
            this.handleSystemSaveAlbum(res.filePath)
          &#125; else if (isAndroid) &#123;
            // Android 不需要特殊处理
            Toast.success('图片保存至相册')
          &#125;
        &#125;
      &#125;, 'jpg', 50)
    &#125;,
    // 保存相册
    handleSystemSaveAlbum (filePath) &#123;
      let img = this.$refs.myImg
      this.fileSrc = filePath

      img.onload = () => &#123;
        let canvas = this.$refs.myCanvas
        canvas.width = img.width
        canvas.height = img.height
        let context = canvas.getContext('2d')
        context.drawImage(img, 0, 0)
        try &#123;
          // 使用 canvas2ImagePlugin 保存至相册
          window.canvas2ImagePlugin.saveImageDataToLibrary((gmsg) => &#123;
            Toast.success('图片保存至相册')
          &#125;, () => &#123;
            Toast.fail('保存失败')
          &#125;,
          document.getElementById('myCanvas')
          )
        &#125; catch (e) &#123;
          Toast.fail(e.message)
        &#125;
      &#125;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            