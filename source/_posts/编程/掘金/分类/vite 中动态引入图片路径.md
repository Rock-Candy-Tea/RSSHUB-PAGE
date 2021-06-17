
---
title: 'vite 中动态引入图片路径'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'static/icon/123.jpg'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 18:31:14 GMT
thumbnail: 'static/icon/123.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>vite 官方默认的配置，打包后会把图片名加上 hash值，但是直接通过 <code>:src="imgSrc"</code>方式引入并不会在打包的时候解析，导致开发环境可以正常引入，打包后却不能显示的问题，示例如下：</p>
</blockquote>
<p>打包后路径：</p>
<pre><code class="copyable"><img src="static/icon/123.jpg">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际打包后的图片路径：<code>static/icon/123.hash.jpg</code></p>
<hr>
<p>可以尝试以下方法解决：</p>
<p>HTML：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"getSrc('123')"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JS:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getSrc = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> path = <span class="hljs-string">`/static/icon/<span class="hljs-subst">$&#123;name&#125;</span>.svg`</span>;
    <span class="hljs-keyword">const</span> modules = <span class="hljs-keyword">import</span>.meta.globEager(<span class="hljs-string">"/static/icon/*.svg"</span>);
    <span class="hljs-keyword">return</span> modules[path].default;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            