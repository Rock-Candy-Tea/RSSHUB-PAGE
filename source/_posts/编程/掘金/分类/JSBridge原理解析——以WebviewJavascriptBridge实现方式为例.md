
---
title: 'JSBridge原理解析——以WebviewJavascriptBridge实现方式为例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55564a3453f14601b32feb40d5d1c923~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 02:34:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55564a3453f14601b32feb40d5d1c923~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、什么是JSBridge？</h2>
<p>JSBridge是一种webview侧和native侧进行通信的手段，webview可以通过jsb调用native的能力，native也可以通过jsb在webview上执行一些逻辑。</p>
<h2 data-id="heading-1">二、JSB的实现方式</h2>
<p>在比较流行的JSBridge中，主要是通过拦截URL请求来达到native端和webview端相互通信的效果的。</p>
<p>这里我们以比较火的WebviewJavascriptBridge为例，来解析一下它的实现方式。</p>
<p>源码地址：<a href="https://github.com/marcuswestin/WebViewJavascriptBridge" target="_blank" rel="nofollow noopener noreferrer">github.com/marcuswesti…</a></p>
<h3 data-id="heading-2">2-1、在native端和webview端注册Bridge</h3>
<p>注册的时候，需要在webview侧和native侧分别注册bridge，其实就是用一个对象把所有函数储存起来。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerHandler</span>(<span class="hljs-params">handlerName, handler</span>) </span>&#123;
    messageHandlers[handlerName] = handler;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)registerHandler:(<span class="hljs-built_in">NSString</span> *)handlerName handler:(WVJBHandler)handler &#123;
    _base.messageHandlers[handlerName] = [handler <span class="hljs-keyword">copy</span>];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2-2、在webview里面注入初始化代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupWebViewJavascriptBridge</span>(<span class="hljs-params">callback</span>) </span>&#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.WebViewJavascriptBridge) &#123; <span class="hljs-keyword">return</span> callback(WebViewJavascriptBridge); &#125;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.WVJBCallbacks) &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">window</span>.WVJBCallbacks.push(callback); &#125;
<span class="hljs-built_in">window</span>.WVJBCallbacks = [callback];
<span class="hljs-keyword">var</span> WVJBIframe = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'iframe'</span>);
WVJBIframe.style.display = <span class="hljs-string">'none'</span>;
WVJBIframe.src = <span class="hljs-string">'https://__bridge_loaded__'</span>;
<span class="hljs-built_in">document</span>.documentElement.appendChild(WVJBIframe);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-built_in">document</span>.documentElement.removeChild(WVJBIframe) &#125;, <span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码主要做了以下几件事：</p>
<p>（1）创建一个名为WVJBCallbacks的数组，将传入的callback参数放到数组内</p>
<p>（2）创建一个iframe，设置不可见，设置src为 <code>https://__bridge_loaded__</code></p>
<p>（3）设置定时器移除这个iframe</p>
<h3 data-id="heading-4">2-3、在native端监听URL请求</h3>
<p>iOS中有两种webview，一种是UIWebview，另一种是WKWebview，这里以WKWebview为例：</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)webView:(<span class="hljs-built_in">WKWebView</span> *)webView decidePolicyForNavigationResponse:(<span class="hljs-built_in">WKNavigationResponse</span> *)navigationResponse decisionHandler:(<span class="hljs-keyword">void</span> (^)(<span class="hljs-built_in">WKNavigationResponsePolicy</span>))decisionHandler &#123;
    <span class="hljs-keyword">if</span> (webView != _webView) &#123; <span class="hljs-keyword">return</span>; &#125;

    __<span class="hljs-keyword">strong</span> <span class="hljs-keyword">typeof</span>(_webViewDelegate) strongDelegate = _webViewDelegate;
    <span class="hljs-keyword">if</span> (strongDelegate && [strongDelegate respondsToSelector:<span class="hljs-keyword">@selector</span>(webView:decidePolicyForNavigationResponse:decisionHandler:)]) &#123;
        [strongDelegate webView:webView decidePolicyForNavigationResponse:navigationResponse decisionHandler:decisionHandler];
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        decisionHandler(<span class="hljs-built_in">WKNavigationResponsePolicyAllow</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码主要做了以下几件事：</p>
<p>（1）拦截了所有的URL请求并拿到url</p>
<p>（2）首先判断<code>isWebViewJavascriptBridgeURL</code>，判断这个url是不是webview的iframe触发的，具体可以通过host去判断。</p>
<p>（3）继续判断，如果是<code>isBridgeLoadedURL</code>，那么会执行<code>injectJavascriptFile</code>方法，会向webview中再次注入一些逻辑，其中最重要的逻辑就是，在window对象上挂载一些全局变量和<code>WebViewJavascriptBridge</code>属性，具体值如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.WebViewJavascriptBridge = &#123;
<span class="hljs-attr">registerHandler</span>: registerHandler,
<span class="hljs-attr">callHandler</span>: callHandler,
<span class="hljs-attr">disableJavscriptAlertBoxSafetyTimeout</span>: disableJavscriptAlertBoxSafetyTimeout,
<span class="hljs-attr">_fetchQueue</span>: _fetchQueue,
<span class="hljs-attr">_handleMessageFromObjC</span>: _handleMessageFromObjC
&#125;;

<span class="hljs-keyword">var</span> sendMessageQueue = [];
<span class="hljs-keyword">var</span> messageHandlers = &#123;&#125;;

<span class="hljs-keyword">var</span> responseCallbacks = &#123;&#125;;
<span class="hljs-keyword">var</span> uniqueId = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）继续判断，如果是isQueueMessageURL，那么这就是个处理消息的回调，需要执行一些消息处理的方法（第四步会详细讲）
<br></p>
<h3 data-id="heading-5">2-4、webview调用native能力</h3>
<p>当native和webview都注册好了Bridge之后，双方就可以互相调用了，这里先介绍webview调用native能力的过程。</p>
<h4 data-id="heading-6">2-4-1、webview侧callHandler</h4>
<p>当webview调用native时，会调用callHandler方法，这个方法具体逻辑如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">bridge.callHandler(<span class="hljs-string">'ObjC Echo'</span>, &#123;<span class="hljs-string">'key'</span>:<span class="hljs-string">'value'</span>&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">responseCallback</span>(<span class="hljs-params">responseData</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"JS received response:"</span>, responseData)
&#125;)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHandler</span>(<span class="hljs-params">handlerName, data, responseCallback</span>) </span>&#123;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length == <span class="hljs-number">2</span> && <span class="hljs-keyword">typeof</span> data == <span class="hljs-string">'function'</span>) &#123;
responseCallback = data;
data = <span class="hljs-literal">null</span>;
&#125;
_doSend(&#123; <span class="hljs-attr">handlerName</span>:handlerName, <span class="hljs-attr">data</span>:data &#125;, responseCallback);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_doSend</span>(<span class="hljs-params">message, responseCallback</span>) </span>&#123;
<span class="hljs-keyword">if</span> (responseCallback) &#123;
<span class="hljs-keyword">var</span> callbackId = <span class="hljs-string">'cb_'</span>+(uniqueId++)+<span class="hljs-string">'_'</span>+<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
responseCallbacks[callbackId] = responseCallback;
message[<span class="hljs-string">'callbackId'</span>] = callbackId;
&#125;
sendMessageQueue.push(message);
messagingIframe.src = CUSTOM_PROTOCOL_SCHEME + <span class="hljs-string">'://'</span> + QUEUE_HAS_MESSAGE;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上就是先生成一个message，然后push到sendMessageQueue里，然后更改iframe的src。</p>
<h4 data-id="heading-7">2-4-2、native侧flushMessageQueue</h4>
<p>然后，当native端检测到iframe src的变化时，会走到isQueueMessageURL的判断逻辑，然后执行WKFlushMessageQueue函数，获取到JS侧的sendMessageQueue中的所有message。</p>
<pre><code class="hljs language-objectivec copyable" lang="objectivec">- (<span class="hljs-keyword">void</span>)<span class="hljs-built_in">WKFlushMessageQueue</span> &#123;
    [_webView evaluateJavaScript:[_base webViewJavascriptFetchQueyCommand] completionHandler:^(<span class="hljs-built_in">NSString</span>* result, <span class="hljs-built_in">NSError</span>* error) &#123;
        <span class="hljs-keyword">if</span> (error != <span class="hljs-literal">nil</span>) &#123;
            <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"WebViewJavascriptBridge: WARNING: Error when trying to fetch data from WKWebView: %@"</span>, error);
        &#125;
        [_base flushMessageQueue:result];
    &#125;];
&#125;

- (<span class="hljs-keyword">void</span>)flushMessageQueue:(<span class="hljs-built_in">NSString</span> *)messageQueueString&#123;
    <span class="hljs-keyword">if</span> (messageQueueString == <span class="hljs-literal">nil</span> || messageQueueString.length == <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"WebViewJavascriptBridge: WARNING: ObjC got nil while fetching the message queue JSON from webview. This can happen if the WebViewJavascriptBridge JS is not currently present in the webview, e.g if the webview just loaded a new page."</span>);
        <span class="hljs-keyword">return</span>;
    &#125;

    <span class="hljs-keyword">id</span> messages = [<span class="hljs-keyword">self</span> _deserializeMessageJSON:messageQueueString];
    <span class="hljs-keyword">for</span> (WVJBMessage* message <span class="hljs-keyword">in</span> messages) &#123;
        <span class="hljs-keyword">if</span> (![message isKindOfClass:[WVJBMessage <span class="hljs-keyword">class</span>]]) &#123;
            <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"WebViewJavascriptBridge: WARNING: Invalid %@ received: %@"</span>, [message <span class="hljs-keyword">class</span>], message);
            <span class="hljs-keyword">continue</span>;
        &#125;
        [<span class="hljs-keyword">self</span> _log:<span class="hljs-string">@"RCVD"</span> json:message];
        
        <span class="hljs-built_in">NSString</span>* responseId = message[<span class="hljs-string">@"responseId"</span>];
        <span class="hljs-keyword">if</span> (responseId) &#123;
            WVJBResponseCallback responseCallback = _responseCallbacks[responseId];
            responseCallback(message[<span class="hljs-string">@"responseData"</span>]);
            [<span class="hljs-keyword">self</span>.responseCallbacks removeObjectForKey:responseId];
        &#125; <span class="hljs-keyword">else</span> &#123;
            WVJBResponseCallback responseCallback = <span class="hljs-literal">NULL</span>;
            <span class="hljs-built_in">NSString</span>* callbackId = message[<span class="hljs-string">@"callbackId"</span>];
            <span class="hljs-keyword">if</span> (callbackId) &#123;
                responseCallback = ^(<span class="hljs-keyword">id</span> responseData) &#123;
                    <span class="hljs-keyword">if</span> (responseData == <span class="hljs-literal">nil</span>) &#123;
                        responseData = [<span class="hljs-built_in">NSNull</span> null];
                    &#125;
                    
                    WVJBMessage* msg = @&#123; <span class="hljs-string">@"responseId"</span>:callbackId, <span class="hljs-string">@"responseData"</span>:responseData &#125;;
                    [<span class="hljs-keyword">self</span> _queueMessage:msg];
                &#125;;
            &#125; <span class="hljs-keyword">else</span> &#123;
                responseCallback = ^(<span class="hljs-keyword">id</span> ignoreResponseData) &#123;
                    <span class="hljs-comment">// Do nothing</span>
                &#125;;
            &#125;
            
            WVJBHandler handler = <span class="hljs-keyword">self</span>.messageHandlers[message[<span class="hljs-string">@"handlerName"</span>]];
            
            <span class="hljs-keyword">if</span> (!handler) &#123;
                <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"WVJBNoHandlerException, No handler for message from JS: %@"</span>, message);
                <span class="hljs-keyword">continue</span>;
            &#125;
            
            handler(message[<span class="hljs-string">@"data"</span>], responseCallback);
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当一个message结构存在responseId的时候说明这个message是执行bridge后传回的。取不到responseId说明是第一次调用bridge传过来的，这个时候会生成一个返回给调用方的message，其reponseId是传过来的message的callbackId，当native执行responseCallback时，会触发_dispatchMessage方法执行webview环境的的js逻辑，将生成的包含responseId的message返回给webview。</p>
<h4 data-id="heading-8">2-4-3、webview侧handleMessageFromObjC</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_handleMessageFromObjC</span>(<span class="hljs-params">messageJSON</span>) </span>&#123;
    _dispatchMessageFromObjC(messageJSON);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_dispatchMessageFromObjC</span>(<span class="hljs-params">messageJSON</span>) </span>&#123;
<span class="hljs-keyword">if</span> (dispatchMessagesWithTimeoutSafety) &#123;
<span class="hljs-built_in">setTimeout</span>(_doDispatchMessageFromObjC);
&#125; <span class="hljs-keyword">else</span> &#123;
 _doDispatchMessageFromObjC();
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_doDispatchMessageFromObjC</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> message = <span class="hljs-built_in">JSON</span>.parse(messageJSON);
<span class="hljs-keyword">var</span> messageHandler;
<span class="hljs-keyword">var</span> responseCallback;
<span class="hljs-keyword">if</span> (message.responseId) &#123;
responseCallback = responseCallbacks[message.responseId];
<span class="hljs-keyword">if</span> (!responseCallback) &#123;
<span class="hljs-keyword">return</span>;
&#125;
responseCallback(message.responseData);
<span class="hljs-keyword">delete</span> responseCallbacks[message.responseId];
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">if</span> (message.callbackId) &#123;
<span class="hljs-keyword">var</span> callbackResponseId = message.callbackId;
responseCallback = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">responseData</span>) </span>&#123;
_doSend(&#123; <span class="hljs-attr">handlerName</span>:message.handlerName, <span class="hljs-attr">responseId</span>:callbackResponseId, <span class="hljs-attr">responseData</span>:responseData &#125;);
&#125;;
&#125;

<span class="hljs-keyword">var</span> handler = messageHandlers[message.handlerName];
<span class="hljs-keyword">if</span> (!handler) &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"WebViewJavascriptBridge: WARNING: no handler for message from ObjC:"</span>, message);
&#125; <span class="hljs-keyword">else</span> &#123;
handler(message.data, responseCallback);
&#125;
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果从native获取到的message中有responseId，说明这个message是JS调Native之后回调接收的message，所以从一开始sendData中添加的responseCallbacks中根据responseId（一开始存的时候是用的callbackId，两个值是相同的）取出这个回调函数并执行，这样就完成了一次JS调用Native的流程。
<br></p>
<h4 data-id="heading-9">2-4-4、过程总结</h4>
<p>过程如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55564a3453f14601b32feb40d5d1c923~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-06-14 23.28.32.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1、native端注册jsb</p>
<p>2、webview侧创建iframe，设置src为<code>__bridge_load__</code></p>
<p>3、native端捕获请求，注入jsb初始化代码，在window上挂载相关对象和方法</p>
<p>4、webview侧调用<code>callHandler</code>方法，并在<code>responseCallback</code>上添加<code>callbackId: responseCallback</code>，并修改iframe的src，触发捕获</p>
<p>5、native收到message，生成一个<code>responseCallback</code>，并执行native侧注册好的方法</p>
<p>6、native执行完毕后，通过webview执行<code>_handleMessageFromObjC</code>方法，取出callback函数，并执行</p>
<h3 data-id="heading-10">2-5、native调用webview能力</h3>
<p>native调用webview注册的jsb的逻辑是相似的，不过就不是通过触发iframe的src触发执行的了，因为Native可以自己主动调用JS侧的方法。其具体过程如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66d091c1bb6a45e493b3039b77cf32fd~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-06-14 23.28.26.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1、native侧调用<code>callHandler</code>方法，并在<code>responseCallback</code>上添加<code>callbackId: responseCallback</code></p>
<p>2、native侧主动调用<code>_handleMessageFromObjC</code>方法，在webview中执行对应的逻辑</p>
<p>3、webview侧执行结束后，生成带有<code>responseId</code>的message，添加到<code>sendMessageQueue</code>中，并修改iframe的src为<code>__wvjb_queue_message__</code></p>
<p>4、native端拦截到url变化，调用webview的逻辑获取到message，拿到<code>responseId</code>，并执行对应的callback函数</p>
<p><strong>作者：赵越</strong></p></div>  
</div>
            