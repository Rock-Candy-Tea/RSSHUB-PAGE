
---
title: 'WKWebView进阶填坑指南-Swift'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=5087'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 18:11:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=5087'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Cookie处理</h2>
<p>在设置<code>Cookie</code>的时候，我们经常做的是在请求的请求头里添加<code> Cookie</code>，但是这只是把<code>Cookie</code>发送给了服务端，我们本地并没有保存<code> Cookie</code>，<code>Cookie </code>最终要写到<code>WebView</code>的一个<code>Cookie</code>文件目录里面，后续<code>WebView</code>里面自己的发起的请求或者跳转才能在发起请求的时候在对应的域名下面取到<code>Cookie</code>传出去。</p>
<p><code>Webview </code>加载 H5 页面，实际上是把页面相关的<code>.html、js、css</code>文件下载到本地，然后再加载，这时页面去获取<code> Cookie</code> 的时候，是去本地<code>WebView</code>里的<code>Cookie</code>文件目录里查找，如果没有设置的话肯定就找不到了。所以在设置<code>Cookie</code>的时候，服务端和客户端都要设置。</p>
<h4 data-id="heading-1">一、服务端 Cookie 设置</h4>
<p>在使用<code>UIWebView</code>的时候，我们是通过<code> NSHTTPCookieStorage</code>来管理 <code>Cookie </code>的，下面我们给<code>devqiaoyu.tech</code>这个域名添加一个名为<code>user</code>的<code>Cookie</code>。</p>
<pre><code class="copyable">var props = Dictionary<HTTPCookiePropertyKey, Any>()
props[HTTPCookiePropertyKey.name] = "user"
props[HTTPCookiePropertyKey.value] = "admin"
props[HTTPCookiePropertyKey.path] = "/"
props[HTTPCookiePropertyKey.domain] = "devqiaoyu.tech"
props[HTTPCookiePropertyKey.version] = "0"
props[HTTPCookiePropertyKey.originURL] = "devqiaoyu.tech"
if let cookie = HTTPCookie(properties: props) &#123;
    HTTPCookieStorage.shared.setCookie(cookie)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>WKWebView Cookie</code>问题在于<code>WKWebView</code>发起的请求不会自动带上存储于<code>NSHTTPCookieStorage</code>容器中的<code>Cookie</code>。</strong></p>
<p>解决办法也很简单，就是在<code>WKWebView</code>发起请求之前，先从<code>NSHTTPCookieStorage</code>读取<code>Cookie</code>，然后手动往<code>URLRequest</code>的请求头里添加一下<code>Cookie</code>。</p>
<pre><code class="copyable">func getCookie() -> String &#123;
    var cookieString = ""
if let cookies = HTTPCookieStorage.shared.cookies &#123;
for cookie in cookies &#123;
if cookie.domain == cookieDomain &#123;
let str = "\(cookie.name)=\(cookie.value)"
cookieString.append("\(str);")
&#125;
&#125;
return cookieString
&#125;

var request = URLRequest(url: URL(string: "https://devqiaoyu.com"))
request.addValue(getCookie(), forHTTPHeaderField: "Cookie")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当服务器页面发生重定向的时候，此时第一次在<code>RequestHeader</code>中写入的<code>Cookie</code>会丢失，还需要对重定向的请求重新做添加<code>Cookie</code>的处理。具体方法请往下看~</p>
<h4 data-id="heading-2">二、客户端 Cookie 设置</h4>
<p>上面这么写完了，当页面加载的时候，后端无论是啥语言，都能从请求头里看到<code>Cookie</code>了，但是后端渲染返回页面后，在客户端的<code>WebView</code>里运行的时候，JS 在执行的时候调用<code> document.cookie</code> API 是读取不到<code>Cookie</code>的，所以还得针对客户端<code>Cookie</code>进行处理。</p>
<pre><code class="copyable">var cookieString = ""
if let cookies = HTTPCookieStorage.shared.cookies &#123;
for cookie in cookies &#123;
if cookie.domain == "devqiaoyu.tech" &#123;
let str = "\(cookie.name)=\(cookie.value)"
cookieString.append("document.cookie='\(str);path=/;domain=devqiaoyu.tech';")
&#125;
&#125;
&#125;
let cookieScript = WKUserScript(source: cookieString, injectionTime: .atDocumentStart, forMainFrameOnly: false)
let userContentController = WKUserContentController()
userContentController.addUserScript(cookieScript)

let webViewConfig = WKWebViewConfiguration()
webViewConfig.userContentController = userContentController

let webV = WKWebView(frame: CGRect.zero, configuration: webViewConfig)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**客户端<code>Cookie</code>注入实际上就是创建一个 JS 脚本，让<code>WebView</code>去执行，推荐在<code>.atDocumentStart</code>这个时机进行预置静态  JS 的注入。**这样<code>WebView</code>在加载后端返回的静态页面的时候，就可以拿到保存着客户端的<code>Cookie</code>了。</p>
<blockquote>
<p><strong>注意：document.cookie() 无法跨域设置 Cookie</strong>，比如你第一次加载的请求时 <a href="http://www.baidu.com/" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com</a> ，在重定向的时候跳转到了 <a href="http://www.google.com/" target="_blank" rel="nofollow noopener noreferrer">www.google.com</a> ，那么第二个请求就可能因为没有携带 <code>Cookie</code>而无法访问。当然啦，解决办法还是有的，请往下看~</p>
</blockquote>
<h2 data-id="heading-3">URL拦截</h2>
<p>在<code>WKWebView</code>中，每一次页面跳转之前，都会调用下面的回调函数：</p>
<pre><code class="copyable">func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">Web 页面重定向问题</h4>
<p>重定向问题有两种：</p>
<ul>
<li>服务器页面重定向，需要对新发起的请求重新种<code>Cookie</code></li>
<li>本地页面重定向，只要客户端设置了<code>Cookie</code>，那么就不需要处理了</li>
</ul>
<p>所以如果是服务器页面重定向，那么判断此时<code>Request</code>是否有你要的<code>Cookie</code>没有就<code>Cancel</code>掉，修改<code>Request </code>重新发起。</p>
<pre><code class="copyable">func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void)
&#123;
    var shouldCancelLoadURL = false
    if let cookie = navigationAction.request.value(forHTTPHeaderField: "Cookie") &#123;
        if cookie.contains("user") &#123;
            shouldCancelLoadURL = false
        &#125; else &#123;
            var request = URLRequest(url: URL(string: (navigationAction.request.url?.absoluteString)!)!)
            request.addValue(getCookie(), forHTTPHeaderField: "Cookie")
            webView.load(request)
            shouldCancelLoadURL = true
        &#125;
    &#125; else &#123;
        var request = URLRequest(url: URL(string: (navigationAction.request.url?.absoluteString)!)!)
        request.addValue(getCookie(), forHTTPHeaderField: "Cookie")
webView.load(request)
shouldCancelLoadURL = true
    &#125;
    
    if shouldCancelLoadURL &#123;
    decisionHandler(WKNavigationActionPolicy.cancel)
&#125; else &#123;
decisionHandler(WKNavigationActionPolicy.allow)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">跨域问题</h4>
<p>针对跨域的问题，解决办法和上面的方法类似，仅仅是判断条件不同。</p>
<pre><code class="copyable">func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void)
&#123;
    var shouldCancelLoadURL = false
    if let url = navigationAction.request.url?.absoluteString &#123;
        if url.contains("devqiaoyu.tech") &#123; // 原来的域名
            shouldCancelLoadURL = false
        &#125; else &#123;
        // 重新发起请求，种Cookie
            shouldCancelLoadURL = true
        &#125;
    &#125; else &#123;
    // 重新发起请求，种Cookie
shouldCancelLoadURL = true
    &#125;
    
    if shouldCancelLoadURL &#123;
    decisionHandler(WKNavigationActionPolicy.cancel)
&#125; else &#123;
decisionHandler(WKNavigationActionPolicy.allow)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">假跳转的请求拦截</h4>
<p><strong>一种 JS 调用 Native 的通信方案</strong>，详细介绍可以看<a href="http://www.cocoachina.com/ios/20180109/21795.html" target="_blank" rel="nofollow noopener noreferrer">从零收拾一个hybrid框架（一）-- 从选择JS通信方案开始</a>。下面内容是从该文章内摘录的。</p>
<p>何谓 <strong>假跳转的请求拦截</strong> 就是由网页发出一条新的跳转请求，跳转的目的地是一个非法的压根就不存在的地址，比如</p>
<pre><code class="copyable">//常规的Http地址
https://wenku.baidu.com/xxxx?xx=xx
//假的请求通信地址
wakaka://wahahalalala/action?param=paramobj
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看我下面写的那条假跳转地址，这么一条什么都不是的扯淡地址，直接放到浏览器里，直接扔到<code>WebView</code>里，肯定是妥妥的什么都打不开的，而如果在经过我们改造过的<code>Hybrid WebView</code>里，进行拦截不进行跳转</p>
<p>url 地址分为这么几个部分</p>
<ul>
<li>协议：也就是 <code>http/https/file</code> 等，上面用了<code> wakaka</code></li>
<li>域名：上面的 <code>wenku.baidu.com</code> 或 <code>wahahalalala</code></li>
<li>路径：上面的 <code>xxxx?</code> 或 <code>action？</code></li>
<li>参数：上面的 <code>xx=xx</code> 或 <code>param=paramobj</code></li>
</ul>
<p>如果我们构建一条假url</p>
<ul>
<li>用协议与域名当做通信识别</li>
<li>用路径当做指令识别</li>
<li>用参数当做数据传递</li>
</ul>
<p>客户端会无差别拦截所有请求，真正的 url 地址应该照常放过，只有协议域名匹配的 url 地址才应该被客户端拦截，拦截下来的 url 不会导致 WebView 继续跳转错误地址，因此无感知，相反拦截下来的 url 我们可以读取其中路径当做指令，读取其中参数当做数据，从而根据约定调用对应的 Native 原生代码</p>
<p>以上其实是一种 <strong>协议约定</strong> 只要 JS 侧按着这个约定协议生成假 url，Native 按着约定协议拦截/读取假 url，整个流程就能跑通。</p>
<h2 data-id="heading-7">User-Agent设置</h2>
<h4 data-id="heading-8">全局设置</h4>
<p>就是<code>App</code>内所有<code>Web</code>请求的<code>User-Agent</code>全部被修改。</p>
<pre><code class="copyable">// UIWebView
let webView = UIWebView(frame: CGRect.zero)
let userAgent = webView.stringByEvaluatingJavaScript(from: "navigator.userAgent")
if let agent = userAgent &#123;
    let user = "@\(agent);extra_user_agent"
    let dict = ["UserAgent":user]
    UserDefaults.standard.register(defaults: dict)
&#125;

// WKWebView
let webV = WKWebView(frame: CGRect.zero)
webV.evaluateJavaScript("navigator.userAgent") &#123; (result, error) in
if let oldAgent = result as? String &#123;
let user = "@\(oldAgent);extra_user_agent"
let dict = ["UserAgent":user]
UserDefaults.standard.register(defaults: dict)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">单个WebView设置</h3>
<p>在<code>iOS9</code>，<code>WKWebView</code>提供了一个非常便捷的属性去更改<code>User-Agent</code>，就是<code>customUserAgent</code>属性。这样使用起来不仅方便，也不会全局更改<code>User-Agent</code>，可惜的是<code>iOS9</code>才有，如果适配<code>iOS8</code>，还是要使用上面的方法。</p>
<pre><code class="copyable">let webView = UIWebView(frame: CGRect.zero)
let userAgent = webView.stringByEvaluatingJavaScript(from: "navigator.userAgent")
if let agent = userAgent &#123;
    let user = "@\(agent);extra_user_agent"
    webView.customUserAgent = user
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">参考文章</h2>
<p><a href="https://www.jianshu.com/p/06963b57d78e" target="_blank" rel="nofollow noopener noreferrer">WKWebView 那些坑</a></p></div>  
</div>
            