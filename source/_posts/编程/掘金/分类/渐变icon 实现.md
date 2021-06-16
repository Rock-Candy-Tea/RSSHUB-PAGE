
---
title: '渐变icon 实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb6c7a9160148129f0d96af923bbc35~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:42:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb6c7a9160148129f0d96af923bbc35~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>
<h3 data-id="heading-0">前言</h3>
<p>平常开发中，有时候要为了展示一些炫酷的效果，然展示的色彩更加丰富，有时候会使用多种色彩进行组合呈现，这时候就会用到渐变了，正好在项目中icon的时候也用到了渐变icon。有哪些方式实现呢。</p>
</li>
<li>
<h3 data-id="heading-1">使用 png /svg 图片</h3>
<p>这类方法实现比较简单粗暴，直接叫UI截图就能快速搞定，省事。<br>
<strong>优点</strong>：省事，不存在什么兼容性问题。<br>
<strong>缺点</strong>：单独占用一个资源请求，换颜色之类的需再让UI切，对于高清屏icon会出现锯齿之类的。</p>
</li>
<li>
<h3 data-id="heading-2">使用 iconfont，CSS3 渐变处理</h3>
<p>使用iconfont 具体步骤：<br></p>
<ol>
<li>
<pre><code class="copyable">引入iconfont字体库对应样式。<br>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">CSS对icon进行处理。<br>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>具体代码如下：<br>
HTML</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><i <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"van-icon van-icon-like like-linear-gradient"</span>
<span class="hljs-string">"></i>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<br>
    CSS
<pre><code class="hljs language-js copyable" lang="js">    .like-linear-gradient &#123;
         background-image: linear-gradient(#01cdfe, #1f19fb);
        -webkit-background-clip: text;
        color:transparent;
    &#125;
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>兼容性：</strong><br>
background-clip:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb6c7a9160148129f0d96af923bbc35~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优点：后期替换颜色，只需要改变渐变颜色进行了，iconfont 矢量的，不会出现锯齿图。<br>
缺点：兼容性会得注意，线性的效果调起来没那么方便。</p></div>  
</div>
            