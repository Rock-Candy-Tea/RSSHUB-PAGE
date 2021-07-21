
---
title: '前端pdf在线预览大坑合集'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d51bab7c907e4798bcb10e5acecf26d4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 01:14:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d51bab7c907e4798bcb10e5acecf26d4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>背景：公司需要在线预览pdf<br>
之前使用的方法<br>
1.用iframe指向pdf路径：ios可以支持预览，安卓手机会跳转到下载页面。<br>
2.office web app: 可以预览部分pdf文件，方便，代码修改量基本问零，但是当需要密码的pdf会直接，有蒙层遮盖，文件看不了，也不能下载。但是也可以通过修改office web app的样式文件去掉css样式。还有出现了部分pdf损坏的情况，所以不使用office web app预览pdf，而且最新版本也不支持pdf预览。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d51bab7c907e4798bcb10e5acecf26d4~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-21 下午5.04.34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在使用的是<a href="https://link.juejin.cn/?target=http%3A%2F%2Fgithub.com%2Fmozilla%2Fpdf.js" target="_blank" rel="nofollow noopener noreferrer" title="http://github.com/mozilla/pdf.js" ref="nofollow noopener noreferrer">pdf.js</a>插件<br>
使用方式：之后再补充<br></p>
<p>坑1：我们公司是网页端和移动端都需要预览pdf文件，不要去下载官方推荐的2.8.335版本。该版本安卓手机不能用。经过本人测试，2.5.207可以让移动端可用，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmozilla%2Fpdf.js%2Freleases%2Ftag%2Fv2.5.207" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mozilla/pdf.js/releases/tag/v2.5.207" ref="nofollow noopener noreferrer">附上链接</a>
下载这个包。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b871e525fda14158ac6c12579b1a1514~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-21 下午5.11.14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>坑2：原本的包不支持跨域浏览文件<br>
将viewer.js 中的错误提示注释掉即可，记得viewer.js.map也要处理一下</p>
<pre><code class="hljs language-js copyable" lang="js">
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">var</span> viewerOrigin = <span class="hljs-keyword">new</span> URL(<span class="hljs-built_in">window</span>.location.href).origin || <span class="hljs-string">'null'</span>;
      <span class="hljs-keyword">if</span> (HOSTED_VIEWER_ORIGINS.indexOf(viewerOrigin) >= <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">var</span> fileOrigin = <span class="hljs-keyword">new</span> URL(file, <span class="hljs-built_in">window</span>.location.href).origin;
      <span class="hljs-comment">//跨域请求错误提示</span>
      <span class="hljs-comment">//if (fileOrigin !== viewerOrigin) &#123;</span>
        <span class="hljs-comment">//throw new Error('file origin does not match viewer\'s');</span>
      <span class="hljs-comment">//&#125;</span>
    &#125; <span class="hljs-keyword">catch</span> (ex) &#123;
      <span class="hljs-keyword">var</span> message = ex && ex.message;
      PDFViewerApplication.l10n.get(<span class="hljs-string">'loading_error'</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">'An error occurred while loading the PDF.'</span>).then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">loadingErrorMessage</span>) </span>&#123;
        PDFViewerApplication.error(loadingErrorMessage, &#123; <span class="hljs-attr">message</span>: message &#125;);
      &#125;);
      <span class="hljs-keyword">throw</span> ex;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            