
---
title: '文件直传 OSS 实践（三）：Angular 篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1179'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 19:18:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=1179'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在<a href="https://juejin.cn/post/6997224305306107918" target="_blank" title="https://juejin.cn/post/6997224305306107918">《文件直传 OSS 实践（一）：服务端篇》</a>文章中讲解了如何在服务端生成用于客户端直传 OSS 的直传传凭证，本文讲解在使用 Angular 框架的 Web 页面中将文件直传 OSS 的整体流程。相对于在小程序中使用已经由官方封装好的上传方法，在 Angular 中使用上传功能会稍微复杂一些。
​</p>
<h2 data-id="heading-1">获取直传凭证</h2>
<p>我们假定获取直传凭证的 API 为：
​</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">GET https:<span class="hljs-comment">//api.xxx.com/upload/token</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以将请求获取直传传凭证的过程进行封装（为方便演示，将所有的方法均放在了 <code>app.component.ts</code> 文件中，实际上涉及 HTTP 请求的方法应放在 <code>*.service.ts</code> 文件中）：
​</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// app.component.ts</span>
<span class="hljs-keyword">import</span> &#123; HttpClient &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/common/http'</span>
<span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>

<span class="hljs-comment">/** 直传凭证 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> UploadToken &#123;
  <span class="hljs-attr">key</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">policy</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">signature</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">OSSAccessKeyId</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'app-root'</span>,
  <span class="hljs-attr">templateUrl</span>: <span class="hljs-string">'./app.component.html'</span>,
  <span class="hljs-attr">styleUrls</span>: [<span class="hljs-string">'./app.component.scss'</span>],
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppComponent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> http: HttpClient</span>)</span> &#123;&#125;

  token!: UploadToken

  <span class="hljs-comment">/** 获取直传凭证 */</span>
  <span class="hljs-function"><span class="hljs-title">getUploadToken</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.http.get(<span class="hljs-string">'https://api.xxx.com/upload/token'</span>).subscribe(<span class="hljs-function">(<span class="hljs-params">data: UploadToken</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.token = data
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">选择文件</h2>
<p>相对于在小程序中可以直接使用 <code>wx.chooseMedia</code> 方法获取资源的路径，在 Angular 获取资源的路径会稍微复杂一些，需要在文档中获取到上传文件使用的子组件，然后再在其内部获取到文件路径。
​</p>
<p>首先，定义 HTML 模板。
​</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// app.component.html</span>
<input #uploader <span class="hljs-keyword">type</span>=<span class="hljs-string">"file"</span> />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个获取文件的输入框，其中 <code>#uploader</code> 表示模板名，可用于在 <code>*.component.ts</code> 文件中获取该模板。需要使用 <code>ViewChild</code> 装饰器获取该模板。
​</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; HttpClient &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/common/http'</span>
<span class="hljs-keyword">import</span> &#123; Component, ElementRef, ViewChild &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>

<span class="hljs-comment">/** 直传凭证 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> UploadToken &#123;
  <span class="hljs-attr">key</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">policy</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">signature</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">OSSAccessKeyId</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'app-root'</span>,
  <span class="hljs-attr">templateUrl</span>: <span class="hljs-string">'./app.component.html'</span>,
  <span class="hljs-attr">styleUrls</span>: [<span class="hljs-string">'./app.component.scss'</span>],
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppComponent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> http: HttpClient</span>)</span> &#123;&#125;

  <span class="hljs-meta">@ViewChild</span>(<span class="hljs-string">'uploader'</span>)
  FileElement!: ElementRef

  token!: UploadToken

  <span class="hljs-comment">/** 获取直传凭证 */</span>
  <span class="hljs-function"><span class="hljs-title">getUploadToken</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.http.get(<span class="hljs-string">'https://api.xxx.com/upload/token'</span>).subscribe(<span class="hljs-function">(<span class="hljs-params">data: UploadToken</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.token = data
    &#125;)
  &#125;

  <span class="hljs-comment">/** 显示第一个文件的路径 */</span>
  <span class="hljs-function"><span class="hljs-title">showFile</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.FileElement.nativeElement.files[<span class="hljs-number">0</span>])
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>核心部分为：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-meta">@ViewChild</span>(<span class="hljs-string">'uploader'</span>)
  FileElement!: ElementRef
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，各部分的含义是：
（1）<code>'uploader'</code> 与 <code><input #uploader type="file" /></code> 中的 <code>uploader</code> 对应。
（2）<code>!</code> 为非空断言。
​</p>
<p>在点击绑定的按钮选择文件后，调用 <code>showFile</code> 方法可以查看选中的文件。
​</p>
<h2 data-id="heading-3">上传文件</h2>
<p>获取到文件和上传凭证后，然后进行上传流程。这里需要注意的一点是：在添加 <code>FormData</code> 属性时，需要把 <code>file</code> 项放在最后，否则会失败。
​</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; HttpClient &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/common/http'</span>
<span class="hljs-keyword">import</span> &#123; Component, ElementRef, ViewChild &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>

<span class="hljs-comment">/** 直传凭证 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> UploadToken &#123;
  <span class="hljs-attr">key</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">policy</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">signature</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">OSSAccessKeyId</span>: <span class="hljs-built_in">string</span>
  <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'app-root'</span>,
  <span class="hljs-attr">templateUrl</span>: <span class="hljs-string">'./app.component.html'</span>,
  <span class="hljs-attr">styleUrls</span>: [<span class="hljs-string">'./app.component.scss'</span>],
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppComponent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> http: HttpClient</span>)</span> &#123;&#125;

  <span class="hljs-meta">@ViewChild</span>(<span class="hljs-string">'uploader'</span>)
  FileElement!: ElementRef

  token!: UploadToken

  <span class="hljs-comment">/** 获取直传凭证 */</span>
  <span class="hljs-function"><span class="hljs-title">getUploadToken</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.http.get(<span class="hljs-string">'https://api.xxx.com/upload/token'</span>).subscribe(<span class="hljs-function">(<span class="hljs-params">data: UploadToken</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.token = data
    &#125;)
  &#125;

  <span class="hljs-comment">/** 显示第一个文件的路径 */</span>
  <span class="hljs-function"><span class="hljs-title">showFile</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.FileElement.nativeElement.files[<span class="hljs-number">0</span>])
  &#125;

  <span class="hljs-comment">/** 直传至 OSS */</span>
  <span class="hljs-function"><span class="hljs-title">upload</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> file = <span class="hljs-built_in">this</span>.FileElement.nativeElement.files[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData()
    formData.append(<span class="hljs-string">'OSSAccessKeyId'</span>, <span class="hljs-built_in">this</span>.token.OSSAccessKeyId)
    formData.append(<span class="hljs-string">'key'</span>, <span class="hljs-built_in">this</span>.token.key)
    formData.append(<span class="hljs-string">'policy'</span>, <span class="hljs-built_in">this</span>.token.policy)
    formData.append(<span class="hljs-string">'signature'</span>, <span class="hljs-built_in">this</span>.token.signature)
    formData.append(<span class="hljs-string">'file'</span>, file)

    <span class="hljs-built_in">this</span>.http.post(<span class="hljs-built_in">this</span>.token.url, formData).subscribe(<span class="hljs-function">(<span class="hljs-params">data: <span class="hljs-built_in">any</span></span>) =></span> &#123;
      <span class="hljs-comment">// 打印最终的资源 URL 地址</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.token.url + <span class="hljs-string">'/'</span> + <span class="hljs-built_in">this</span>.token.key)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            