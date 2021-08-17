
---
title: '了解CSS3背景新增的东西 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://upload-images.jianshu.io/upload_images/18658207-a96fea39ffdf2c20.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 16:54:24 GMT
thumbnail: 'https://upload-images.jianshu.io/upload_images/18658207-a96fea39ffdf2c20.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>在CSS3中，关于background新增了三个子属性</p>
<p><code>1. background-origin</code></p>
<p><code>2. background-clip</code></p>
<p><code>3. background-size</code></p>
<p>先来看background-origin，这里铺垫一下background-position，我们知道background-position是用于设置背景图片在元素中出现的位置</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-pseudo">:root</span>,<span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"./bg.jpg"</span>);
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
    <span class="hljs-attribute">background-position</span>: <span class="hljs-number">100px</span> <span class="hljs-number">100px</span>; 
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果是背景图在body中出现的位置是在距离左边100px，距离上边100px的地方。</p>
<p><code>而background-origin是用于设置背景图在计算background-position时的参考点位置</code>
<code>取值包括：border-box padding-box content-box三个，分别表示从border区域开始显示图片，从padding区域开始显示背景图片，以及从内容区域开始显示背景图片。默认是padding-box</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-pseudo">:root</span>,<span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-selector-tag">body</span> <span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">50px</span> solid <span class="hljs-built_in">rgba</span>(<span class="hljs-number">244</span>, <span class="hljs-number">333</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">5</span>);
    <span class="hljs-attribute">background-color</span>: pink;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"./bg.jpg"</span>);
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
    <span class="hljs-comment">/* background-origin: border-box; */</span>
    <span class="hljs-comment">/* background-origin: padding-box;
    background-origin: content-box; */</span>
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    这里是content区域，这里是content区域，这里是content区域，这里是content区域，这里是content区域
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三种情况分别如下：<img src="https://upload-images.jianshu.io/upload_images/18658207-a96fea39ffdf2c20.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="分别对应border-box，padding-box，content-box" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上div中添加代码</p>
<pre><code class="copyable">background-origin: content-box;
background-position: 50px 50px;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://upload-images.jianshu.io/upload_images/18658207-a0d985263889c9bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="结果，背景图片出现位置相对于content-box" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着来看下一个新增属性<code> background-clip</code></p>
<p><code>background-clip用于背景裁剪，取值也有三个：border-box，padding-box和content-box；分别表示背景从边框区域开始裁剪，背景从padding区域开始裁剪，和背景从content区域开始裁剪</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-pseudo">:root</span>,
    <span class="hljs-selector-tag">body</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;

    <span class="hljs-selector-tag">div</span> &#123;
      <span class="hljs-attribute">float</span>: left;
      <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">50px</span>;
      <span class="hljs-attribute">border</span>: <span class="hljs-number">10px</span> solid <span class="hljs-built_in">rgba</span>(<span class="hljs-number">244</span>, <span class="hljs-number">333</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">5</span>);
      <span class="hljs-attribute">background-color</span>: deeppink;
      <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"./bg.jpg"</span>);
      <span class="hljs-attribute">background-repeat</span>: no-repeat;
      <span class="hljs-attribute">background-origin</span>: border-box;
    &#125;
    <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">1</span>)&#123;
      <span class="hljs-attribute">background-clip</span>: border-box;
    &#125;
    <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">2</span>)&#123;
      <span class="hljs-attribute">background-clip</span>: padding-box;
    &#125;
    <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">3</span>)&#123;
      <span class="hljs-attribute">background-clip</span>: content-box;
      
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这里是content区域<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这里是content区域<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这里是content区域<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这里是content区域<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这里是content区域<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这里是content区域<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://upload-images.jianshu.io/upload_images/18658207-e42f70505341cac1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="分别对应border-box，padding-box，content-box" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着来看CSS3背景新增的最后一个属性background-size</p>
<p><code>background-size用于设置背景尺寸大小，取值可以是数值可以是百分比也可以是关键词auto、cover、contain分别表示背景图真实大小、将背景图等比缩放到完全覆盖容器（背景图有可能超出容器）、将背景图等比缩放到宽度或高度与容器的宽度或高度相等（背景图始终被包含在容器内）。</code></p>
<p>注意：该属性接受1~2个参数值。两个分别表示背景图宽度和高度；只提供一个，表示背景图宽度，而高度将依据背景图宽度进行等比缩放计算得到。另外百分比是参照背景图的background-origin区域大小进行换算的</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-pseudo">:root</span>,
  <span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">float</span>: left;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid <span class="hljs-built_in">rgba</span>(<span class="hljs-number">244</span>, <span class="hljs-number">333</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">5</span>);
    <span class="hljs-attribute">background-color</span>: deeppink;
    <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"./bg.jpg"</span>);
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
  &#125;
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">1</span>) &#123;
    <span class="hljs-attribute">background-size</span>: auto;
  &#125;
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">2</span>) &#123;
    <span class="hljs-attribute">background-size</span>: cover;
  &#125;
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">3</span>) &#123;
    <span class="hljs-attribute">background-size</span>:contain;
  &#125;
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">4</span>) &#123;
    <span class="hljs-attribute">background-size</span>:<span class="hljs-number">50%</span>;
  &#125;
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">5</span>) &#123;
    <span class="hljs-attribute">background-size</span>:<span class="hljs-number">100px</span>;
  &#125;
  <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-of-type</span>(<span class="hljs-number">6</span>) &#123;
    <span class="hljs-attribute">background-size</span>:<span class="hljs-number">100px</span> <span class="hljs-number">100px</span>;
  &#125;    
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>background-size: auto<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>background-size: cover<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>background-size:contain<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>background-size: 50%<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>background-size: 100px<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>background-size:100px 100px<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是CSS3 background新增属性的全部内容！</p></div>  
</div>
            