
---
title: '今天来学习下CSP（内容安全策略）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fba558aa7c9450ba3e88a8ef1c1a47d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 07:57:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fba558aa7c9450ba3e88a8ef1c1a47d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">前言</h3>
<p>昨天讲了<a href="https://juejin.cn/post/6998541496945213477" target="_blank" title="https://juejin.cn/post/6998541496945213477">如何限制网站不能被iframe嵌套</a>，里面有一种方式是<strong>设置CSP（内容安全策略）</strong>，它不单单只是可以限制网站被iframe嵌套，还有别的用法，今天来讲讲它。</p>
<h3 data-id="heading-1">CSP（内容安全策略）</h3>
<p>CSP，内容安全策略,全称是<code>Content-Security-Policy</code>,主要是允许网页加载的哪些资源，不符合这些策略的资源无法加载，一定程度上可以防范XSS的攻击。</p>
<h3 data-id="heading-2">语法</h3>
<blockquote>
<p>Content-Security-Policy: 指令 指令值,指令值; 指令 指令值,指令值...</p>
</blockquote>
<p>对应的指令有以下这些：</p>

































































<table><thead><tr><th>指令</th><th>描述</th></tr></thead><tbody><tr><td><code>default-src</code></td><td>设置所有加载资源的默认策略，当其它指令没设置时，就会走默认策略</td></tr><tr><td><code>script-src</code></td><td>设置script标签加载资源的策略</td></tr><tr><td><code>style-src</code></td><td>设置style标签加载样式的策略</td></tr><tr><td><code>font-src</code></td><td>设置font标签加载字体的策略</td></tr><tr><td><code>img-src </code></td><td>设置img标签加载图片的策略</td></tr><tr><td><code>media-src </code></td><td>设置视频或者音频文件加载的策略</td></tr><tr><td><code>frame-ancestors</code></td><td>设置本页面是否能够被ifame嵌套的策略</td></tr><tr><td><code>frame-src </code></td><td>设置本页面是否能够加载ifame标签的策略（旧）</td></tr><tr><td><code>child-src </code></td><td>设置本页面是否能够加载ifame标签的策略（新）</td></tr><tr><td><code>object-src </code></td><td>设置flash插件加载的策略</td></tr><tr><td><code>connect-src </code></td><td>设置http请求的策略</td></tr><tr><td><code>base-uri</code></td><td>设置基本链接的策略</td></tr><tr><td><code>form-action</code></td><td>设置表单提交url的策略</td></tr><tr><td><code>report-uri</code></td><td>设置上报uri的策略</td></tr></tbody></table>
<p>对应的指令值有以下值：</p>

















































<table><thead><tr><th>指令值</th><th>描述</th></tr></thead><tbody><tr><td><code>'none'</code></td><td>不允许加载任何资源（注意是带引号的，下同）</td></tr><tr><td><code>'self'</code></td><td>加载同源资源</td></tr><tr><td><code>'unsafe-inline'</code></td><td>加载内联样式（style，script等）</td></tr><tr><td><code>'unsafe-eval'</code></td><td>加载eval函数的代码</td></tr><tr><td><code>http:</code></td><td>加载http协议的资源</td></tr><tr><td><code>https:</code></td><td>加载https协议的资源</td></tr><tr><td><code>data:</code></td><td>加载data协议(比如base64地址开头就是data)的资源</td></tr><tr><td><code>域名</code></td><td>加载该域名下的资源 比如aaa.com</td></tr><tr><td><code>路径</code></td><td>加载该路径下的资源 比如aaa.com/js</td></tr><tr><td><code>*</code></td><td>通配符，代表所有</td></tr></tbody></table>
<h3 data-id="heading-3">设置方式</h3>
<p>设置CSP有两种方式，请求头上<code>http header</code>设置和<code>meta</code>标签设置。</p>
<h4 data-id="heading-4"><code>http header</code>设置</h4>
<p>新建一个页面 index.html</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>你好，我是cp3！<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新增index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>)
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
http.createServer(<span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  fs.readFile(<span class="hljs-string">'./index.html'</span>, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
    res.writeHead(<span class="hljs-number">200</span>, &#123;
      <span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'text/html; charset=UTF-8'</span>,
      <span class="hljs-string">"Content-Security-Policy"</span>: <span class="hljs-string">"script-src  'self' test.com"</span>
    &#125;)
    res.write(data)
    res.end()
  &#125;)
&#125;).listen(<span class="hljs-number">8081</span>)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'服务已开启，请打开http://127.0.0.1:8081'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>node执行<code>index.js</code></p>
<p>因为我加载了一个cdn的jquery文件，然后我<code>csp</code>设置了 <code>"script-src  'self' test.com"</code>，只允许加载同源资源和test.com域名的资源</p>
<p>所以控制台报错了，如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fba558aa7c9450ba3e88a8ef1c1a47d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5"><code>meta标签</code>设置</h4>
<p>上面的效果也可以通过设置<code>meta</code>来实现：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-comment"><!-- csp meta标签 --></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Content-Security-Policy"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"script-src  'self' test.com"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>你好，我是cp3！<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本地运行，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/663991b8b8734e9996815a9a20bfba0a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">总结</h3>
<p>以上就是我总结的CSP（内容安全策略），它支持的属性是比较多的，大家都可以复制代码去试试。</p>
<p>感谢你们的阅读。</p></div>  
</div>
            