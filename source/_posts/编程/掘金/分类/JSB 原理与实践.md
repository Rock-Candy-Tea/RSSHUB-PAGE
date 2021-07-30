
---
title: 'JSB 原理与实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9571f0f668145ca902e770d98d69389~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 05:49:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9571f0f668145ca902e770d98d69389~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是 JSB</h1>
<p>我们开发的 h5 页面运行在端上的 WebView 容器之中，很多业务场景下 h5 需要依赖端上提供的信息/能力，这时我们需要一个可以连接原生运行环境和 JS 运行环境的桥梁 <strong>。</strong> 这个桥梁就是 JSB，<strong>JSB</strong> <strong>让 Web 端和 Native 端得以实现双向通信</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9571f0f668145ca902e770d98d69389~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">WebView 概述</h1>
<p>WebView 是移动端中的一个控件，它为 JS 运行提供了一个沙箱环境。WebView 能够加载指定的 url，拦截页面发出的各种请求等各种页面控制功能，JSB 的实现就依赖于 WebView 暴露的各种接口。由于历史原因，安卓和 iOS 均有高低两套版本的 WebView 内核：</p>

























<table><thead><tr><th><strong>平台和版本</strong></th><th><strong>WebView</strong> <strong>内核</strong></th></tr></thead><tbody><tr><td>iOS 8+</td><td>WKWebView</td></tr><tr><td>iOS 2-8</td><td>UIWebView</td></tr><tr><td>Android 4.4+</td><td>Chrome</td></tr><tr><td>Android 4.4-</td><td>Webkit</td></tr></tbody></table>
<p>PS: 下文中出现的高版本均代指 iOS 8+ 或 Android 4.4+，低版本则相反。</p>
<h1 data-id="heading-2">JSB 原理</h1>
<p>要实现双向通信自然要依次实现 Native 向 Web 发送消息和 Web 向 Native 发送消息。</p>
<h2 data-id="heading-3">Native 向 Web 发送消息</h2>
<p>Native 向 Web 发送消息基本原理上是在 WebView 容器中动态地执行一段 JS 脚本，通常情况下是调用一个挂载在全局上下文的方法。Android 和 iOS 均提供了不同的接口来实现这一过程。</p>
<h3 data-id="heading-4">方法</h3>
<ul>
<li>Android 高低版本存在两种直接执行 JS 字符串的方法：</li>
</ul>




















<table><thead><tr><th><strong>Android 版本</strong></th><th><strong>API</strong></th><th><strong>特点</strong></th></tr></thead><tbody><tr><td>低版本</td><td>WebView.loadUrl</td><td>无法执行回调</td></tr><tr><td>高版本</td><td>WebView.evaluateJavascript</td><td>可以拿到 JS 执行完毕的返回值</td></tr></tbody></table>
<ul>
<li>iOS 高低版本同样存在两种不同的实现方式：</li>
</ul>




















<table><thead><tr><th><strong>iOS 版本</strong></th><th><strong>API</strong></th><th><strong>特点</strong></th></tr></thead><tbody><tr><td>低版本</td><td>UIWebView.stringByEvaluatingJavaScriptFromString</td><td>无法执行回调</td></tr><tr><td>高版本</td><td>WKWebView.evaluateJavaScript</td><td>可以拿到 JS 执行完毕的返回值</td></tr></tbody></table>
<h3 data-id="heading-5">实践</h3>
<p>下面我们通过一个小 Demo 来看一下在 iOS 端实现 Native 向 Web 端发消息的实际效果：</p>
<p>（<strong>本文所有 Demo 均运行在 iOS14.5 模拟器中，WebView 容器采用 WKWebView 内核</strong>）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea16642b37c1447f877a4ce2bfabf851~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>页面上半部分的 UI 是由 HTML + CSS 渲染所得，是一个纯静态的 webpage，中间的输入框和按钮是 Native 原生控件，直接覆盖在 WebView 容器之上。<strong>在 Native 按钮上绑定了一个点击事件：将文本框输入的字符视为 JS 字符串并调用相关 API 直接执行</strong>。</p>
<p>可以看到当我们在文本框中输入下列字符并点击按钮后，h5 页面中 id 为 test 的 p 标签内容被修改了。</p>
<pre><code class="copyable">document.querySelector('#test').innerHTML = 'I am from native';
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daefcd5a0b3b47f9b31c6ed2d539bf6a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>敏锐同学到这一步其实就已经知道我们在日常使用 JSB 时客户端是如何调用前端 JS 代码了，我们在刚刚的静态 html 文件中添加几行 JS 代码：</p>
<pre><code class="copyable">function evaluateByNative(params) &#123;
    const p = document.createElement('p');
    p.innerText = params;
    document.body.appendChild(p);
    return 'Hello Bridge!';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在文本框中输入 <code>evaluateByNative(23333)</code>，来看一下调用的结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95c669cfa7e547eea04822a67a883fce~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0ee852344f944d0be86c337bb9fd720~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 <strong>Native 端可以直接调用挂载在 window 上的全局方法并传入相应的函数执行参数</strong>，<strong>并且在函数执行结束后 Native 端可以直接拿到执行成功的返回值。</strong></p>
<h2 data-id="heading-6">Web 向 Native 发送消息</h2>
<p>Web 向 Native 发送消息本质上就是某段 JS 代码的执行端上是可感知的，目前业界主流的实现方案有两种，分别是<strong>拦截式</strong>和<strong>注入式</strong>。</p>
<h3 data-id="heading-7">拦截式</h3>
<p>和浏览器类似 WebView 中发出的所有请求都是可以被 Native 容器感知到的（是不是想到了Gecko），因此拦截式具体指的是 Native 拦截 Web 发出的 URL 请求，双方在此之前约定一个 JSB 请求格式，如果该请求是 JSB 则进行相应的处理，若不是则直接转发。</p>
<p><strong>Native 拦截请求的钩子方法：</strong></p>





















<table><thead><tr><th><strong>平台</strong></th><th><strong>API</strong></th></tr></thead><tbody><tr><td>Android</td><td>shouldOverrideUrlLoading</td></tr><tr><td>iOS 8+</td><td>decidePolicyForNavigationAction</td></tr><tr><td>iOS 8-</td><td>shouldStartLoadWithRequest</td></tr></tbody></table>
<p><strong>拦截式的基本流程如下</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fb5a08a438f438db7f3b36d058fef91~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述流程存在几个问题：</p>
<ol>
<li><strong>通过何种方式发出请求？</strong></li>
</ol>
<p>Web 端发出请求的方式非常多样，例如 <code><a/></code> 、<code>iframe.src</code>、<code>location.href</code>、<code>ajax</code> 等，但 <code><a/></code> 需要用户手动触发，<code>location.href</code> 可能会导致页面跳转，安卓端拦截 <code>ajax</code> 的能力有所欠缺，因此<strong>绝大多数拦截式实现方案均采用</strong><code>iframe</code> <strong>来发送请求</strong>。</p>
<ol start="2">
<li><strong>如何规定</strong> <strong>JSB</strong> <strong>的请求格式？</strong></li>
</ol>
<p>一个标准的 URL 由 <code><scheme>://<host>:<port><path></code> 组成，相信大家都有过从微信或手机浏览器点击某个链接意外跳转到其他 App 的经历，如果有仔细留意过这些链接的 URL 你会发现目前主流 App 都有其专属的一个 scheme 来作为该应用的标识，例如微信的 URL scheme 就是 <code>weixin://</code>。<strong>JSB</strong> <strong>的实现借鉴这一思路，定制业务自身专属的一个 URL scheme 来作为 JSB 请求的标识</strong>，例如字节内部实现拦截式 JSB 的 SDK 中就定义了 <code>bytedance://</code> 这样一个 scheme。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Web 通过动态创建 iframe，将 src 设置为符合双端规范的 url scheme</span>
<span class="hljs-keyword">const</span> CUSTOM_PROTOCOL_SCHEME = <span class="hljs-string">'prek'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">web2Native</span>(<span class="hljs-params">event</span>) </span>&#123;    
    <span class="hljs-keyword">const</span> messagingIframe = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'iframe'</span>);
    messagingIframe.style.display = <span class="hljs-string">'none'</span>;
    messagingIframe.src = CUSTOM_PROTOCOL_SCHEME + <span class="hljs-string">'://'</span> + event;
    <span class="hljs-built_in">document</span>.documentElement.appendChild(messagingIframe);

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">document</span>.documentElement.removeChild(messagingIframe);
    &#125;, <span class="hljs-number">200</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拦截式在双端都具有非常好的向下兼容性，曾经是最主流的 JSB 实现方案，但目前在高版本的系统中已经逐渐被淘汰，理由是它有如下几个劣势：</p>
<ul>
<li>连续发送时可能会造成消息丢失（可以使用消息队列解决该问题）</li>
<li>URL  字符串长度有限制</li>
</ul>

<ul>
<li>性能一般，URL request 创建请求有一定的耗时（Android 端 200-400ms）</li>
</ul>
<p><strong>实践案例</strong></p>
<p>同样用一个简单的 Demo2 来看一下如何使用拦截式实现 Web 向 Native 发送消息，这里实现了在 Web 端唤起 Native 的相册。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e2048463ae14c6b9d36c6be64f3899b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>遵循上述实现方式，Web 发送消息的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CUSTOM_PROTOCOL_SCHEME = <span class="hljs-string">'prek'</span> <span class="hljs-comment">// 自定义 url scheme</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">web2Native</span>(<span class="hljs-params">event_name</span>) </span>&#123;
    <span class="hljs-keyword">const</span> messagingIframe = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'iframe'</span>)
    messagingIframe.style.display = <span class="hljs-string">'none'</span>
    messagingIframe.src = CUSTOM_PROTOCOL_SCHEME + <span class="hljs-string">'://'</span> + event_name
    <span class="hljs-built_in">document</span>.documentElement.appendChild(messagingIframe)
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">document</span>.documentElement.removeChild(messagingIframe)
    &#125;, <span class="hljs-number">0</span>)
&#125;

<span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btn'</span>)

btn.onclick = <span class="hljs-function">() =></span> &#123;
    web2Native(<span class="hljs-string">'openPhotoAlbum'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Native 侧通过 <code>decidePolicyForNavigationAction</code> 这一 delegate 实现请求拦截，解析 URL 参数，若 URL scheme 是 <code>prek</code> 则认为该请求是一个来自 Web 的 JSB 调用：</p>
<pre><code class="hljs language-js copyable" lang="js">- (<span class="hljs-keyword">void</span>)webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction decisionHandler:(<span class="hljs-keyword">void</span> (^)(WKNavigationActionPolicy))decisionHandler &#123;
  NSURL *url = navigationAction.request.URL;
  NSLog(@<span class="hljs-string">"拦截到 Web 发出的请求 = %@"</span>, url);

  <span class="hljs-keyword">if</span> ([self isSchemeMatchPrek:url]) &#123;
    NSString* host = url.host.lowercaseString;
    <span class="hljs-keyword">if</span> ([host isEqualToString: @<span class="hljs-string">"openphotoalbum"</span>]) &#123;
      [self openCameraForWeb]; <span class="hljs-comment">// 打开相册</span>
      NSLog(@<span class="hljs-string">"打开相册"</span>);
    &#125;
    decisionHandler(WKNavigationActionPolicyCancel);
    <span class="hljs-keyword">return</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    decisionHandler(WKNavigationActionPolicyAllow);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了更清晰地看到 Native 拦截的结果，在上述代理方法中打个断点：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9b48b6a58834578981947d6fb787933~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>继续执行，Congratulation！模拟器的相册被打开了！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c033e8668a2b40f2bd3969caebbf742a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">注入式</h3>
<p>注入式的原理是通过 WebView 提供的接口向 JS 全局上下文对象（window）中注入对象或者方法，当 JS 调用时，可直接执行相应的 Native 代码逻辑，从而达到 Web 调用 Native 的目的。</p>
<p><strong>Native 注入 API 的相关方法：</strong></p>

























<table><thead><tr><th><strong>平台</strong></th><th><strong>API</strong></th><th><strong>特点</strong></th></tr></thead><tbody><tr><td>Android</td><td>addJavascriptInterface</td><td>4.2 版本以下有安全风险</td></tr><tr><td>iOS 8+</td><td>WKScriptMessageHandler</td><td>无</td></tr><tr><td>iOS 7+</td><td>JavaSciptCore</td><td>无</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js">JSContext *context = [webView valueForKeyPath:@<span class="hljs-string">"documentView.webView.mainFrame.javaScriptContext"</span>];

context[@<span class="hljs-string">"getAppInfo"</span>] = ^(msg) &#123;
    <span class="hljs-keyword">return</span> @<span class="hljs-string">"ggl_2693"</span>;
&#125;;
<span class="hljs-built_in">window</span>.getAppInfo(); <span class="hljs-comment">// 'ggl_2693'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法简单而直观，并且不存在参数长度限制和性能瓶颈等问题，目前主流的 JSB SDK 都将注入式方案作为优先使用的对象。注入式的实现非常简单，这里不做案例展示。</p>
<h3 data-id="heading-9">两种方案对比</h3>
<p>为了更清晰地表达这两种方式的区别，这里贴一个对比表格：</p>























<table><thead><tr><th><strong>方案</strong></th><th><strong>兼容性</strong></th><th><strong>性能</strong></th><th><strong>参数长度限制</strong></th></tr></thead><tbody><tr><td>拦截式</td><td>无兼容性问题</td><td>较差，安卓端尤为明显</td><td>有限制</td></tr><tr><td>注入式</td><td>安卓4.2+ 和 iOS 7+以上可用</td><td>较好</td><td>无</td></tr></tbody></table>
<h2 data-id="heading-10">如何执行回调</h2>
<p>通过上述介绍我们已经知道如何实现双端互相发送消息，但上述两个通信过程缺少了“回应”这一动作，原因就是上述步骤缺少了回调函数的执行。以拦截式为例，常见的一个 JSB 调用是 Web 获取当前 App 信息， Native 拦截到 <code>bytedance://getAppInfo</code>这样一个请求后将获取当前 App 信息，那获取完成后如何让 Web 端拿到该信息呢？</p>
<p>一个最简单的做法是类比 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FJSONP" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/JSONP" ref="nofollow noopener noreferrer">JSONP</a> 的实现，我们可以在请求的 URL 上拼接回调方法的事件名，将该事件挂载在全局 window 上，由于 Native 端可以轻松执行 JS 代码，因此在完成端逻辑后直接执行该事件名对应的回调方法即可。以 <code>getAppInfo</code> 为例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Web</span>
<span class="hljs-keyword">const</span> uniqueID = <span class="hljs-number">1</span> <span class="hljs-comment">// 为防止事件名冲突，给每个 callback 设置一个唯一标识</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">webCallNative</span>(<span class="hljs-params">event, params, callback</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback === <span class="hljs-string">'Function'</span>) &#123;
        <span class="hljs-keyword">const</span> callbackID = <span class="hljs-string">'jsb_cb_'</span> + (uniqueID++) + <span class="hljs-string">'_'</span> + <span class="hljs-built_in">Date</span>.now();
        <span class="hljs-built_in">window</span>[callbackID] = callback
    &#125;
    <span class="hljs-keyword">const</span> params = &#123;<span class="hljs-attr">callback</span>: callbackID&#125;
    <span class="hljs-comment">// 构造 url scheme</span>
    <span class="hljs-keyword">const</span> src = <span class="hljs-string">'bytedance://getAppInfo?'</span> + <span class="hljs-built_in">JSON</span>.stringify(params)
    ...
&#125;

<span class="hljs-comment">// Native</span>
<span class="hljs-number">1.</span> 解析传入的参数 <span class="hljs-string">'getAppInfo'</span> 得知 Web 希望获取 AppInfo
<span class="hljs-number">2.</span> 执行端逻辑获取 AppInfo
<span class="hljs-number">3.</span> 执行参数中挂载在全局的 callback 方法，AppInfo 作为回调方法的参数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此只要把相应的回调方法挂载在全局对象上，Native 即可把每次调用后的响应通过动态执行 JS 方法的形式传递到 Web 端，这样一来整个通信过程就实现了闭环。</p>
<h2 data-id="heading-11">串联双端通信的过程</h2>
<p>现在我们已经知道如何实现两端互相发送消息以及执行回调了，但看起来并不好用：首先调用 JSB 时需要在方法名后拼接参数和对应的回调函数，其次回调函数还需要一个一个地挂载在全局对象上。</p>
<p>我们期望的使用方式其实是这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Web</span>
web.call(<span class="hljs-string">'event1'</span>, &#123;param1&#125;, <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;...&#125;) <span class="hljs-comment">// 触发 native event1 执行</span>
web.on(<span class="hljs-string">'event2'</span>, <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;...&#125;)

<span class="hljs-comment">// Native </span>
<span class="hljs-comment">// 这里用 js 代替，理解大致意思即可</span>
native.call(<span class="hljs-string">'event2'</span>, &#123;param2&#125;, <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;...&#125;) <span class="hljs-comment">// 触发 web event2 执行</span>
native.on(<span class="hljs-string">'event1'</span>, <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <strong>JSB 就像是一个跨越两端的 EventEmitter</strong>，因此需要 Web 和 Native 遵循同一套调度机制。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f7831d48e54404ebe7d4753bbf2374e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图给出了 Web 调用 -> Native 监听的执行过程，同理 Native 调用 -> Web 监听也是同样的逻辑，只是把两边的实现调换一种语言，这里不赘述了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fae5972c4b4f4713910fec7768ccaaa0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>贴一张其他同学画的时序图，帮助理解整个通信过程</p>
<p>Demo3 基于开源的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmarcuswestin%2FWebViewJavascriptBridge" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/marcuswestin/WebViewJavascriptBridge" ref="nofollow noopener noreferrer">WebViewJavascriptBridge</a> 演示了一套完整的通讯流程是怎样进行的，有兴趣的同学请自行戳源码地址 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.byted.org%2Fcaocheng.viccc%2FJSB_Demo" target="_blank" rel="nofollow noopener noreferrer" title="https://code.byted.org/caocheng.viccc/JSB_Demo" ref="nofollow noopener noreferrer">JSB_Demo</a> 自行体验。（需要使用 Xcode 打开，会涉及一些客户端的知识，请配合文档和 Google 使用）。</p>
<h1 data-id="heading-12">一点感受</h1>
<p>笔者所在业务使用的 bridge 即司内目前最新的 SDK，没有历史包袱、使用体验也非常良好。得益于客户端遵循该 SDK 配套的实现机制，即使完全不了解 JSB 原理的同学在与端上对接 bridge 时也几乎没有遇到障碍。倘若抛开公司完备的基础建设，想实现一个通用且好用的 JSB 并非易事，因此了解其中的门道还是非常有益的。（巨人的肩膀站久了，确实巴适得很🐶</p>
<p>字节跳动校/社招投递链接: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjob.toutiao.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://job.toutiao.com/" ref="nofollow noopener noreferrer">job.toutiao.com/</a></p>
<p>内推码：​7EZKXME</p>
<h1 data-id="heading-13">参考文献</h1>
<p><a href="https://juejin.cn/post/6936814903021797389#heading-8" target="_blank" title="https://juejin.cn/post/6936814903021797389#heading-8">深入浅出 JSBridge</a></p>
<p><a href="https://juejin.cn/post/6844903702721986568" target="_blank" title="https://juejin.cn/post/6844903702721986568">JSB 实战</a></p></div>  
</div>
            