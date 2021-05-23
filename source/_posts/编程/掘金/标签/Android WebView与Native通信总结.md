
---
title: 'Android WebView与Native通信总结'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=7331'
author: 掘金
comments: false
date: Sat, 22 May 2021 07:26:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=7331'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当前移动端App的开发很多都需要内嵌WebView来方便业务的快速开展，特别是电商App中，业务变化快，活动多。仅仅依靠native的开发方式难以满足快速的业务发展，于是混合开发模式便出现。当前比较知名的有<code>Cordova</code>, <code>Ionic</code>, 国内的有<code>Appcan</code>, <code>APICloud</code>开发平台，这几种都是依赖于WebView的实现。而Facebook的<code>React Native</code>和阿里的<code>Weex</code>是混合开发的另一种实现，<code>React Native</code>和<code>Weex</code>可以让原生开发者像H5开发一样写前端的代码，然后通过自己的SDK渲染成原生的组件，不依赖于<code>WebView</code>。本文主要总结一下当前<code>WebView</code>和native的交互方式。</p>
<p>Android中<code>WebView</code>和<code>JavaScript</code>的交互，其实就是Android native与网页中的<code>Javascript</code>之间的交互, 所以搞清楚了它们之间数据是如何传递的就明白了。以下从两个方面进行介绍：</p>
<h2 data-id="heading-0">Native 向 Javascript 发送数据</h2>
<p>Native 向 JavaScript发送数据有两种方式, 一种是<code>evaluateJavascript</code> 另一种是<code>loadUrl</code>。区别在于<code>evaluateJavascript</code>比<code>loadUrl</code>更高效，<code>evaluateJavascript</code>在android 4.4之后才能用，该方法的执行不会使页面刷新, 而<code>loadUrl</code>则会。所以通常我们如下使用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">if</span> (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) &#123;
    evaluateJavascript(jsCommand, <span class="hljs-keyword">null</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
    loadUrl(jsCommand);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，如果想要直接获得javascript代码的执行结果，我们可以这样写:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span> command = <span class="hljs-string">"ABC"</span>;
webView.evaluateJavascript(<span class="hljs-string">"(function() &#123; return "</span> + command + <span class="hljs-string">"; &#125;)();"</span>, <span class="hljs-keyword">new</span> ValueCallback<<span class="hljs-built_in">String</span>>() &#123;
    @Override
    public <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">onReceiveValue</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> result</span>)</span> &#123;
        <span class="hljs-comment">// 此处的result便是 ABC</span>
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">Javascript 向 Native 发送数据</h2>
<p>Javascript向Native发送数据有4种方式，第一种方式是借助<code>webChromClient</code>中的<code>onJsAlert()</code>, <code>onJsPromot()</code>的方法来获取Javascript相关数据。第二种方式是采用覆盖<code>shouldOverrideUrlLoading</code>方法，拦截url协议。第三种是最方便的,也就是<code>@JavascriptInterface</code>方案, 现在大多数App都会用到这种方式, 后面会详细介绍。最后一种是利用在<code>webView</code>中嵌入<code>iframe</code>的方式，通过更新<code>iframe</code>的url。比较出名的混合框架<a href="https://github.com/lzyzsd/JsBridge" target="_blank" rel="nofollow noopener noreferrer"><code>JsBridge</code></a>之前就是采用这种方式，现已改成采用<code>@JavascriptInterface</code>这种方式了。以下简单介绍一下各种方式的使用。</p>
<h3 data-id="heading-2"><code>onJsPrompt</code></h3>
<p><code>webChromeClient</code>中提供了<code>onJsAlert</code>, <code>onJsPrompt</code>方法，方便开发者重写Javascript中的<code>alert</code>, <code>prompt</code>方法对应的行为。我们可以在这两个方法中任选一个做为native和js进行交互的桥梁。通常我们借助于<code>onJsPrompt</code> 方法来实现, 就是因为在js中，这个方法通常我们用得比较少。而对于<code>onJsAlert()</code>, 当调用js中的<code>alert()</code>时会触发，我们可以通过重写这个方法来实现自定义的提示View</p>
<p>但是这种方式对传入的数据量有限制，和手机的WebView版本有关，以我的测试机为例，在<code>oppo reno</code>手机 android 10上面, 其传递数据最多只能是10k。 而用<code>@JavascriptInterface</code> 方案, 传递的数据最多可达20 - 30M</p>
<p>我们来看前端网页的写法, 直接调用<code>prompt</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> data = prompt(<span class="hljs-string">"native://getUserInfo?id=1"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'data:'</span> + data);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在为WebView设置<code>WebChromeClient</code>的时候重写<code>onJsPrompt</code>方法，如下：</p>
<pre><code class="hljs language-java copyable" lang="java">
 <span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">onJsPrompt</span><span class="hljs-params">(WebView view, String url, String message, String defaultValue, JsPromptResult result)</span> </span>&#123;
    Uri uri = Uri.parse(message);
    <span class="hljs-comment">//如果是调nativeAPI.</span>
    <span class="hljs-keyword">if</span> (url.startsWith(<span class="hljs-string">"native://"</span>)) &#123;
        result.confirm(<span class="hljs-string">"call natvie api success"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.onJsPrompt(view, url, message, defaultValue, result);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3"><code>shouldOverrideUrlLoading</code></h3>
<p>前端页面的Js代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">document</span>.location=<span class="hljs-string">"native://getUserInfo?id=1"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>native层面在为WebView设置<code>WebViewClient</code>对象时，我们需要重写<code>shouldOverrideUrlLoading</code>方法。需要注意的是，<code>WebViewClient</code>中有两个<code>shouldOverrideUrlLoading</code>方法的定义:</p>
<ul>
<li><code>public boolean shouldOverrideUrlLoading(WebView view, String url)</code></li>
<li><code>public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request)</code></li>
</ul>
<p>其中上面一个在sdk中已被标记<code>Deprecated</code>, 下面一个是在android 7.0中才引入的，所以为了避免兼容性问题。在使用时，建议这两个方法都重写。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">shouldOverrideUrlLoading</span><span class="hljs-params">(WebView view, String url)</span> </span>&#123;
    <span class="hljs-comment">//如果是调nativeAPI.</span>
    <span class="hljs-keyword">if</span> (url.startsWith(<span class="hljs-string">"native://"</span>)) &#123;
        Log.i(<span class="hljs-string">"CommonWebViewClient"</span>, <span class="hljs-string">"shouldOverrideUrlLoading execute------>"</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.shouldOverrideUrlLoading(view, url);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><code>@JavascriptInterface</code></h3>
<p>在 Android 4.2以下有安全漏洞, 但目前我们的app大部份最小支持版本都已经升到5.0了，这个可以忽略，当然感兴趣可以自己搜索。</p>
<p>在native层面，我们需为要WebView注入一个对象，用来处理两边的数据交互。注入方式如下：</p>
<ul>
<li>首先定义一个类来处理两边的交互:</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HybridAPI</span> </span>&#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> String TAG = <span class="hljs-string">"HybridAPI"</span>;

    <span class="hljs-meta">@JavascriptInterface</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sendToNative</span><span class="hljs-params">(<span class="hljs-keyword">final</span> String message)</span> </span>&#123;
        Log.i(TAG, <span class="hljs-string">"get data from js------------>"</span> + message);

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在<code>WebView</code>中注入这个类的实例</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">HybridAPI hybridAPI = <span class="hljs-keyword">new</span> HybridAPI();
webview.addJavascriptInterface(hybridAPI, <span class="hljs-string">"HybridAPI"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在网页中直接用如下代码便可以将数据发送到native端</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> HybridAPI.sendToNative(<span class="hljs-string">'Hello'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><code>iframe</code></h3>
<p>我们还可以利用<code>iframe</code>进行请求伪造向native端发送数据的。思路是向网页中添加一个<code>iframe</code>控件，通过修改其<code>src</code>属性，触发native端的<code>shouldOverrideUrlLoading</code>方法的执行, 同样，native端通过重写该方法，去拿到js端传过来的数据。具体操作方式如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> iframe = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'iframe'</span>);
iframe.style.display = <span class="hljs-string">'none'</span>;
<span class="hljs-built_in">document</span>.documentElement.appendChild(iframe);
iframe.src=<span class="hljs-string">"native://getUserInfo?id=1"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在操作完成后，我们再从当前的dom结构中移除这个组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    iframe && iframe.parentNode && iframe.parentNode.removeChild(iframe);
&#125;, <span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">具体实践</h2>
<p>在前面总结了WebView和Native交互的几种方案。但距离实际项目使用还有一段距离，在实际项目开发中还有很多问题需要考虑。如：</p>
<ul>
<li>交互的规则如何定义</li>
<li>数据如何传递</li>
<li>调用之后，如何拿到回调的结果</li>
<li>对于Javascript的请求，native端应该如何设计?</li>
<li>....</li>
</ul>
<p>native端向JavaScript发送消息只有<code>loadUrl</code>, <code>evaluateJavascript</code>这两种方式。Javascript向native端发送信息可以利用<code>onJsPrompt</code>, <code>@JavascriptInterface</code>, <code>shouldOverrideUrlLoading</code>等几种方案，以下
我们通过采用<code>@JavascriptInterface</code>这种方式(也就是大家通常说的注解方案)为例来看看如何解决实际项目开发中碰到的问题。</p>
<h3 data-id="heading-7">交互的规则</h3>
<p>首先我们来定义两端的交互规则。</p>
<h4 data-id="heading-8">Javascript向native发数据：</h4>
<p>我们约定在H5中采用<code>HybridAPI.sendToNative</code>方法向native端发送数据，于是我们需要在native端做如下支持：</p>
<ul>
<li>定义一个<code>HybridAPI</code>类，并向WebView中注册</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java">HybridAPI hybridAPI = <span class="hljs-keyword">new</span> HybridAPI(<span class="hljs-keyword">this</span>);
webview.addJavascriptInterface(hybridAPI, <span class="hljs-string">"HybridAPI"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在<code>HybridAPI</code>类中定义一个方法<code>sendToNative</code>, 该方法暴露给Javascript用来给native发送数据</li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@JavascriptInterface</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sendToNative</span><span class="hljs-params">(<span class="hljs-keyword">final</span> String message)</span> </span>&#123;
    Log.i(TAG, <span class="hljs-string">"get data from js------------>"</span> + message);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">native层向Javascript发数据：</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> String TO_JAVASCRIPT_PREFIX = <span class="hljs-string">"javascript:HybridAPI.onReceiveData('%s')"</span>;

<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sendToJavaScript</span><span class="hljs-params">(Map<String, Object> message)</span> </span>&#123;
    String str = <span class="hljs-keyword">new</span> Gson().toJson(message);
    <span class="hljs-keyword">final</span> String jsCommand = String.format(TO_JAVASCRIPT_PREFIX, escapeString(str));

    <span class="hljs-keyword">if</span> (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) &#123;
        evaluateJavascript(jsCommand, <span class="hljs-keyword">null</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
        loadUrl(jsCommand);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在H5中，我们这样写, 当native向Javascript发送数据时，便会触发Javascript中的<code>Hybrid.onReceiveData</code>方法, 该方法就能接收到native层传过来的数据</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">HybridAPI.onReceiveData = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">message</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[response from native]'</span> + message);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">数据结构的定义</h3>
<p>在上面我们已经基于<code>@JavascriptInterface</code>方案完成了native与WebView间通信机制的实现，双方可以交换数据，但开发的时候需要考虑更多问题。比如，如果是Javascript向native发送数据，需要将数据转换成一个字符串，然后再将字符串发给native, native再去解析这个字符串，找到对应的处理方法，提取出相关的业务参数，再进行相应的处理。所以我们需要定义这个字符串的数据结构。</p>
<p>在上面我们已经约定了，H5端可以采用<code>HybridAPI.sendToNative</code>向native发送数据，该方法只有一个字符串参数, 以<code>获取用户信息</code>这个业务功能为例，我们的字符串参数是<code>native://getUserInfo?id=1</code>，这个字符串中的<code>getUserInfo</code>表示当前通信的目的或行为(为了拿用户信息)， <code>?</code> 后面的<code>id=1</code> 表示的是参数（用户id为1), 如果参数多了，这个字符串会更长，再如果上面涉及到中文的转码，其可读性会大大降低，所以这种交互方式不够直观和友好，我们期望用户采用下面这个方法去与native通信:</p>
<p><code>HybridAPI.invoke(methodName, params, callbackFun)</code></p>
<ul>
<li><code>methodName</code>: 当前通信的行为</li>
<li><code>params</code>: 传递的参数</li>
<li><code>callbackFun</code>: 接收native端的返回数据</li>
</ul>
<p>于是，我们在js层面进行一层的封装</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> callbackId = <span class="hljs-number">0</span>;
<span class="hljs-keyword">var</span> callbackFunList = &#123;&#125;
HybridAPI.invoke = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">method, params, callbackFun</span>) </span>&#123;
    <span class="hljs-keyword">var</span> message = &#123;
        method,
        params
    &#125;
    <span class="hljs-keyword">if</span> (callbackFun) &#123;
        callbackId  = callbackId + <span class="hljs-number">1</span>;
        message.id = <span class="hljs-string">'Hybrid_CB_'</span> + callbackId;
        callbackFunList[callbackId] = callbackFun
    &#125;
    HybridAPI.sendToNative(<span class="hljs-built_in">JSON</span>.stringify(message));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终还是调用的是<code>sendToNative</code>与native层进行通信，但是采用<code>HybridAPI.invoke</code>方法对开发者更加友好。</p>
<p>由于需要在执行成功后调用回调函数。为此在发送消息的时候先把<code>callbackFun</code>保存起来，在执行成功后再响应。
当Javascript请求发送到native层时，会触发<code>sendToNative</code>方法，在该方法中, 我们来解析前端的数据：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@JavascriptInterface</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sendToNative</span><span class="hljs-params">(<span class="hljs-keyword">final</span> String message)</span> </span>&#123;
    JSONObject object = DataUtil.str2JSONObject(message);
    <span class="hljs-keyword">if</span> (object == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">final</span> String callbackId = DataUtil.getStrInJSONObject(object, <span class="hljs-string">"id"</span>);
    <span class="hljs-keyword">final</span> String method = DataUtil.getStrInJSONObject(object, <span class="hljs-string">"method"</span>);
    <span class="hljs-keyword">final</span> String params = DataUtil.getStrInJSONObject(object, <span class="hljs-string">"params"</span>);

    handleAPI(method, params, callbackId);
&#125;

<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handleAPI</span><span class="hljs-params">(String method, String params, String callbackId)</span>  </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-string">"getDeviceInfo"</span>.equals(method)) &#123;
        getDeviceInfo();
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-string">"getUserInfo"</span>.equals(method)) &#123;
        getUserInfo();
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-string">'login'</span>.equals(method)) &#123;
        login();
    &#125;
    ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>native端在处理完成后，再调用<code>evaluateJavascript</code>或<code>loadUrl</code>方法，反馈给前端。操作流程示例：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//指定了js端的接收入口 </span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> String TO_JAVASCRIPT_PREFIX = <span class="hljs-string">"javascript:HybridAPI.onReceiveData('%s')"</span>;


<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">callJs</span><span class="hljs-params">()</span> </span>&#123;
    Map<String, Object> responseData = <span class="hljs-keyword">new</span> HashMap<>();
    responseData.put(<span class="hljs-string">"error"</span>, error);
    responseData.put(<span class="hljs-string">"data"</span>, result);
    <span class="hljs-comment">//回调函数的id标识，返回给js,这样才能找到对应的回调函数</span>
    responseData.put(<span class="hljs-string">"id"</span>, callbackId);
    sendToJavaScript(responseData);
&#125;

<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sendToJavaScript</span><span class="hljs-params">(Map<String, Object> message)</span> </span>&#123;
    String str = <span class="hljs-keyword">new</span> Gson().toJson(message);
    <span class="hljs-keyword">final</span> String jsCommand = String.format(TO_JAVASCRIPT_PREFIX, escapeString(str));

    <span class="hljs-keyword">if</span> (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) &#123;
        evaluateJavascript(jsCommand, <span class="hljs-keyword">null</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
        loadUrl(jsCommand);
    &#125;
&#125;

<span class="hljs-comment">// 转义</span>
<span class="hljs-function"><span class="hljs-keyword">private</span> String <span class="hljs-title">escapeString</span><span class="hljs-params">(String javascript)</span> </span>&#123;
    String result;
    result = javascript.replace(<span class="hljs-string">"\\"</span>, <span class="hljs-string">"\\\\"</span>);
    result = result.replace(<span class="hljs-string">"\""</span>, <span class="hljs-string">"\\\""</span>);
    result = result.replace(<span class="hljs-string">"\'"</span>, <span class="hljs-string">"\\\'"</span>);
    result = result.replace(<span class="hljs-string">"\n"</span>, <span class="hljs-string">"\\n"</span>);
    result = result.replace(<span class="hljs-string">"\r"</span>, <span class="hljs-string">"\\r"</span>);
    result = result.replace(<span class="hljs-string">"\f"</span>, <span class="hljs-string">"\\f"</span>);
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的<code>callJs</code>方法中组织好相关的数据，然后利用<code>Gson</code>进行序列化，再转进行字符串的转义，最终调用<code>evaluateJavascript</code>或者<code>loadUrl</code>来传递给js。于是js端便可以利用<code>HybridAPI.onReceiveData</code>来接收到。</p>
<p>还记得这段代码中定义的<code>callbackFunList</code>吗？在上面native给js返回数据的时候，会带上一个<code>id</code>, 我们可以根据这个id找到本次通信的回调函数，然后将数据回调过去。</p>
<blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> callbackId = <span class="hljs-number">0</span>;
<span class="hljs-keyword">var</span> callbackFunList = &#123;&#125; <span class="hljs-comment">//看这里</span>
HybridAPI.invoke = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">method, params, callbackFun</span>) </span>&#123;
   <span class="hljs-keyword">var</span> message = &#123;
       method,
      params
   &#125;
   <span class="hljs-keyword">if</span> (callbackFun) &#123;
       callbackId  = callbackId + <span class="hljs-number">1</span>;
       message.id = <span class="hljs-string">'Hybrid_CB_'</span> + callbackId;
       callbackFunList[callbackId] = callbackFun
   &#125;
   HybridAPI.sendToNative(<span class="hljs-built_in">JSON</span>.stringify(message));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>所以，我们js端接收数据，可能是这样子：</p>
<pre><code class="hljs language-js copyable" lang="js">HybridAPI.onReceiveData = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">message</span>) </span>&#123;
    <span class="hljs-keyword">var</span> callbackFun = <span class="hljs-built_in">this</span>.callbackFunList[message.id];
    <span class="hljs-keyword">if</span> (callbackFun) &#123;
      callbackFun(message.error || <span class="hljs-literal">null</span>, message.data);
    &#125;
    <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.callbackFunList[message.id];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再回到我们上面的<code>获取用户信息</code>这个业务功能，我们的写法就会是这样子了：</p>
<pre><code class="hljs language-js copyable" lang="js">HybridAPI.invoke(<span class="hljs-string">'getUserInfo'</span>, &#123;<span class="hljs-string">"id"</span>: <span class="hljs-string">"1"</span>&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error, data</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (error) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'获取用户信息失败'</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'username:'</span> + data.username + <span class="hljs-string">', age:'</span> + data.age);
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，我们就将一具完整的数据通信流程实现了，由js端用<code>HybridAPI.invoke(method, params, callbackFun)</code>来向native端来发送数据，native处理完毕后，js端通过<code>callbackFun</code>来接收数据。</p>
<h2 data-id="heading-11">改进</h2>
<p>在上面的java代码中，我们可以看到，native层的入口是<code>sendToNative</code>方法，该方法中解析传入的字符串，再交给<code>handleAPI</code>方法来处理</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@JavascriptInterface</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sendToNative</span><span class="hljs-params">(<span class="hljs-keyword">final</span> String message)</span> </span>&#123;
    JSONObject object = DataUtil.str2JSONObject(message);
    <span class="hljs-keyword">if</span> (object == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">final</span> String callbackId = DataUtil.getStrInJSONObject(object, <span class="hljs-string">"id"</span>);
    <span class="hljs-keyword">final</span> String method = DataUtil.getStrInJSONObject(object, <span class="hljs-string">"method"</span>);
    <span class="hljs-keyword">final</span> String params = DataUtil.getStrInJSONObject(object, <span class="hljs-string">"params"</span>);

    handleAPI(method, params, callbackId);
&#125;

<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handleAPI</span><span class="hljs-params">(String method, String params, String callbackId)</span>  </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-string">"getDeviceInfo"</span>.equals(method)) &#123;
        getDeviceInfo();
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-string">"getUserInfo"</span>.equals(method)) &#123;
        getUserInfo();
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-string">'login'</span>.equals(method)) &#123;
        login();
    &#125;
    ....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们会发现，随着业务的发展，项目的迭代，js端可能会需要native提供越来越多的能力，所以我们的<code>handleAPI</code>方法中就会有越来越多的<code>if...else if...</code>了。</p>
<p>于是，我们可以按业务来划分，新建一个<code>UserController</code>类来处理<code>getUserInfo</code>, <code>login</code>, <code>logout</code>这种与用户相关的native 接口。新建一个<code>DeviceController</code>来处理类似于<code>getDeviceInfo</code>, <code>getDeviceXXX</code>,... 等与设备信息相关的接口。然后我们再维护一个controller list, 每次调用js api的时候从这个list里面去找对应的 controller中的方法处理。</p>
<p>这样，就可以把具体的业务处理方法抽取出来。然而即便这样，还是避免不了在每个Controller中去写一段这个<code>if...else if ...</code>这种代码。于是，其实我们可以很自然的想到用反射来做点事。</p>
<p>我们和H5开发约定好了，如果需要获取用户的信息，就调用<code>getUserInfo</code>方法，这个方法名始终不变。同时，我们在Java端这样定义<code>UserController</code>:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserController</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IController</span></span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">volatile</span> <span class="hljs-keyword">static</span> UserController instance;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">UserController</span><span class="hljs-params">()</span> </span>&#123;&#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> UserController <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (instance == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">synchronized</span>(UserController.class) &#123;
                <span class="hljs-keyword">if</span> (instance == <span class="hljs-keyword">null</span>) &#123;
                    instance = <span class="hljs-keyword">new</span> UserController();
                &#125;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> instance;
    &#125;

    <span class="hljs-meta">@APIMethod</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> UserInfo <span class="hljs-title">getUserInfo</span><span class="hljs-params">(Map<String, Object> params, String callbackId)</span> </span>&#123;
        <span class="hljs-comment">//TODO</span>
    &#125;

    <span class="hljs-meta">@APIMethod</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">login</span><span class="hljs-params">(Map<String, Object> params, INativeCallback callback)</span> </span>&#123;
        <span class="hljs-comment">//TODO</span>
    &#125;

    <span class="hljs-meta">@APIMethod</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">logout</span><span class="hljs-params">(Map<String, Object> params, INativeCallback callback)</span> </span>&#123;
        <span class="hljs-comment">//TODO</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们将该<code>UserController</code>添加到上面提到的controller list中，然后我们在handleAPI方法中:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handleNativeAPI</span><span class="hljs-params">(String methodName,  String params, String callback)</span> </span>&#123;
    <span class="hljs-keyword">for</span> (IController controller : controllerList) &#123;
        Method[] methods = controller.getClass().getDeclaredMethods();
        <span class="hljs-keyword">for</span> (Method method : methods) &#123;
            Annotation[] annotations = method.getAnnotations();
            <span class="hljs-keyword">for</span> (Annotation annotation : annotations) &#123;
                <span class="hljs-comment">// 获取注解的具体类型</span>
                Class<? extends Annotation> annotationType = annotation.annotationType();
                <span class="hljs-keyword">if</span> (method.getName().equals(methodName) &&  APIMethod.class == annotationType) &#123;
                    <span class="hljs-keyword">try</span> &#123;
                        Map<String, Object> map = DataUtil.jsonStr2Map(params);
                        method.invoke(controller, map, callback);
                    &#125; <span class="hljs-keyword">catch</span> (IllegalAccessException e) &#123;
                        e.printStackTrace();
                    &#125; <span class="hljs-keyword">catch</span> (InvocationTargetException e) &#123;
                        e.printStackTrace();
                    &#125;
                    <span class="hljs-keyword">return</span>;
                &#125;
            &#125;
        &#125;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面，每当新增一个交互的方法时，我们只需要在对应的java类中写一个方法，并用<code>@APIMethod</code>标识就可以。</p>
<p>以上我们总结了WebView与native通信的几种方式，并结合具体实践给出相应的实现思路，当然因为篇幅原因，这里并没有面面俱到。比如：</p>
<ul>
<li>如何实现H5端监听native端的某个事件的功能？</li>
<li>H5端监听native事件后，进行相应的操作，如何将操作的结果再返给native?</li>
<li>如果js端调了一个不存的native的方法，应该如何处理？</li>
<li>...</li>
</ul>
<p>如果仔细理解了前面介绍的两端通信方式，实现上面的这些功能应该不是问题。但如果想把代码更好的封装，使开发者用起来更舒服，那就需要下一点功夫了。</p></div>  
</div>
            