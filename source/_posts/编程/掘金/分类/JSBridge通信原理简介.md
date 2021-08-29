
---
title: 'JSBridge通信原理简介'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64129ae7e0734ab096ef7a3a497a005f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 01:19:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64129ae7e0734ab096ef7a3a497a005f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>一直在做Hybrid App（混合模式移动应用）,就是传统意义上的App 内嵌H5开发, 目前已经开发一年多了, 突然有一天想着, 业务开发中总是调用客户端的能力, 比如说在App里面打开一个webView, 关闭一个webView, 或者调用原生客户端的能力,比如说, 调用手机的拍照能力等等,这个是怎么实现的(不想一直做api调用工程师)? 怀着这样的疑问, 看了一下公司的jss-sdk的源码, 于是有了这边关于客户端和H5通信的文章.</p>
<h2 data-id="heading-1">技术介绍</h2>
<p>JSBridge定义: bridge的英文意思是"<strong>桥梁</strong>", 这里可以理解为原生JS和客户端(native)通讯的桥梁,他可以通过一种方式将native能力提供给JavaScript，同时native也可能需要调用JavaScript的一些功能，而JSBridge就是JavaScript和native之间的桥梁，提供两者相互调用的能力。</p>
<p>我们来看看原理图:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64129ae7e0734ab096ef7a3a497a005f~tplv-k3u1fbpfcp-watermark.image" alt="JSBridge通讯图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">技术实现</h3>
<p>主要分为</p>
<ul>
<li>native --> webView</li>
<li>webView --> natvie</li>
</ul>
<h4 data-id="heading-3">native调用webView能力实现:</h4>
<p>首先来说Native端调用Web端，这个比较简单，JavaScript作为解释性语言，最大的一个特性就是可以随时随地地通过解释器执行一段JS代码，所以可以将拼接的JavaScript代码字符串，传入<strong>JS解析器执</strong>行就可以，JS解析器在这里就是webView。</p>
<h4 data-id="heading-4">webView调用native能力:</h4>
<p>Web调用Native端主要有两种方式</p>
<ul>
<li>拦截Webview请求的URL Schema</li>
</ul>
<p>URL Schema是类URL的一种请求格式，格式如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><protocol>:<span class="hljs-comment">//<host>/<path>?<qeury>#fragment</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以自定义JSBridge通信的URL Schema，比如：jsbridge://showToast?text=hello
Native加载WebView之后，Web发送的所有请求都会经过WebView组件，所以Native可以重写WebView里的方法，拦截Web发起的请求，我们对请求的格式进行判断：
如果符合我们自定义的URL Schema，对URL进行解析，拿到相关操作、操作，进而调用原生Native的方法
如果不符合我们自定义的URL Schema，我们直接转发，请求真正的服务</p>
<p>Web发送URL请求的方法有这么几种：</p>
<ul>
<li>a标签</li>
<li>location.href</li>
<li>使用iframe.src</li>
<li>发送ajax请求</li>
</ul>
<p>这些方法，a标签需要用户操作，location.href可能会引起页面的跳转丢失调用，发送ajax请求Android没有相应的拦截方法，所以使用<strong>iframe.src</strong>是经常会使用的方案</p>
<p>看看实现的伪代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">iosBridge</span> (<span class="hljs-params">action, param</span>) </span>&#123;
  param[<span class="hljs-string">'methodName'</span>] = action
  <span class="hljs-comment">//创建一个iframe</span>
  <span class="hljs-keyword">let</span> iframe = env.createIframe()
  <span class="hljs-keyword">let</span> paramStr = <span class="hljs-built_in">JSON</span>.stringify(param)
  <span class="hljs-comment">//iframe链接, 携带参数, 约定好的URL Schema格式, native端拦截, 拿到携带的方法</span>
  iframe.src = <span class="hljs-string">`xxx://xxx.hybrid.ios/?message=<span class="hljs-subst">$&#123;<span class="hljs-built_in">encodeURIComponent</span>(paramStr)&#125;</span>`</span>
  <span class="hljs-built_in">document</span>.body.appendChild(iframe)
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> iframe.remove(), <span class="hljs-number">300</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结: 这种方式主要是打开一个iframe, 然后加载和客户端约定好的<strong>URL Schema</strong>, 客户端通过拦截这个<strong>URL Schema</strong>, 拿到url上面携带的方法,然后再客户端调用, 就实现了webView调用native的能力了.</p>
<ul>
<li>通过API全局注入</li>
</ul>
<p>这个方法会通过webView提供的接口，App将Native的相关接口注入到JS的Context（window）的对象中，一般来说这个对象内的方法名与Native相关方法名是相同的，Web端就可以直接在全局window下使用这个全局JS对象，进而调用原生端的方法。</p>
<p>看看实现的伪代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">andrExecute</span> (<span class="hljs-params">action, param</span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.minApplication) &#123;
      <span class="hljs-keyword">let</span> oriParam = <span class="hljs-built_in">JSON</span>.stringify(param)
      <span class="hljs-built_in">window</span>.minMApplication.executeCmd(action, oriParam)
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    <span class="hljs-built_in">console</span>.log(error)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结: 这种通过api注入的方式, 我们在window对象下面定义了一个minApplication对象,这个对象里面就是存储native端的方法了.</p>
<p>完整的调用是双向通信，需要一个回调函数，技术实现上就是使用了两次单向通信.</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-comment">//CB.getCallbackName就是客户端处理后的回调,这样就是实现了双向通信了</span>
enterDetail (obj, callback) &#123;
  <span class="hljs-built_in">this</span>.compatInvoke(<span class="hljs-string">'enterInfoDetail'</span>, obj, CB.getCallbackName(callback))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">总结</h2>
<p>Hybrid开发是目前移动端开发的主流技术选项，其中Native和Web端的双向通信就离不开JSBridge
其中Native调用Web端是直接在JS的Context直接执行JS代码，Web端调用Native端有两种方法，一种是基于URL Schema的拦截操作，另一种是向JS的Context（window）注入Api，其中注入Api是目前最好的选择.</p></div>  
</div>
            