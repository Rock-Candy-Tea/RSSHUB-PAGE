
---
title: '学会这个flex-shrink再进大厂'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f9229d178bc4f288db8cec64c5d1729~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:06:16 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f9229d178bc4f288db8cec64c5d1729~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先来一段简单的代码</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .container &#123;
        display: flex;
        margin-bottom: 20px;
      &#125;
      .left &#123;
        width: 50px;
        background-color: #f00;
      &#125;
      .right &#123;
        flex-grow: 1;
        display: flex;
        flex-wrap: wrap;
      &#125;
    </style>
  </head>
  <body>
    <div id="app">
      <div class="container">
        <div class="left">50</div>
        <div class="right">Last</div>
      </div>
      <div class="container">
        <div class="left">50</div>
        <div class="right">
          <label>这是一段很长很长的话，这是一段很长很长的话，这是一段很长很长的话，这是一段很长很长的话</label>
          <label>这是一段很长很长的话，这是一段很长很长的话，这是一段很长很长的话，这是一段很长很长的话</label>
          <label>这是一段很长很长的话，这是一段很长很长的话，这是一段很长很长的话，这是一段很长很长的话</label>
        </div>
      </div>
    </div>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随便建个HTML文件复制这段话，你就可以看到如下图像</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f9229d178bc4f288db8cec64c5d1729~tplv-k3u1fbpfcp-watermark.image" alt="image-20210618105152607.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，第二个50，已经被挤占了空间，不足50px的宽度了。</p>
<p>这是怎么回事呢？width属性不起作用了吗？</p>
<p>原来是flex在搞鬼。</p>
<p>来看一个属性：flex-shrink。</p>
<pre><code class="copyable">flex-shrink属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就懂了，原来是这个属性导致了flex item都是默认可以被缩小，被挤占空间的。</p>
<p>所以，在固定宽度的item里，都需要加上这个属性 flex-shrink: 0。</p>
<p>所以，敲重点，<strong>下次面试再遇到让我们写双列布局或者三列布局的时候，固定宽度那个item千万别忘了加上这个属性，面试官看到了问起你（没看到就自己说出来）</strong>，同样都是flex布局，你懂这么深，这不就是加分小技巧嘛。</p></div>  
</div>
            