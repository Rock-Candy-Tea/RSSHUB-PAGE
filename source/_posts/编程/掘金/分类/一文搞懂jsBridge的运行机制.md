
---
title: '一文搞懂jsBridge的运行机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3028'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 01:49:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=3028'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我司的APP是一个典型的混合开发APP，内嵌的都是前端页面，前端页面要做到和原生的效果相似，就避免不了调用一些原生的方法，<code>jsBridge</code>就是<code>js</code>和<code>原生</code>通信的桥梁，本文不讲概念性的东西，而是通过分析一下我司项目中的<code>jsBridge</code>源码，来从前端角度大概了解一下它是怎么实现的。</p>
<h1 data-id="heading-0">js调用方式</h1>
<p>先来看一下，<code>js</code>是怎么来调用某个原生方法的，首先初始化的时候会调用<code>window.WebViewJavascriptBridge.init</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.WebViewJavascriptBridge.init()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后如果要调用某个原生方法可以使用下面的函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">native</span> (<span class="hljs-params">funcName, args = &#123;&#125;, callbackFunc, errorCallbackFunc</span>) </span>&#123;
    <span class="hljs-comment">// 校验参数是否合法</span>
    <span class="hljs-keyword">if</span> (args && <span class="hljs-keyword">typeof</span> args === <span class="hljs-string">'object'</span> && <span class="hljs-built_in">Object</span>.prototype.toString.call(args).toLowerCase() === <span class="hljs-string">'[object object]'</span> && !args.length) &#123;
        args = <span class="hljs-built_in">JSON</span>.stringify(args);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'args不符合规范'</span>);
    &#125;
    <span class="hljs-comment">// 判断是否是手机环境</span>
    <span class="hljs-keyword">if</span> (getIsMobile()) &#123;
        <span class="hljs-comment">// 调用window.WebViewJavascriptBridge对象的callHandler方法</span>
        <span class="hljs-built_in">window</span>.WebViewJavascriptBridge.callHandler(
            funcName,
            args,
            <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
                res = <span class="hljs-built_in">JSON</span>.parse(res);
                <span class="hljs-keyword">if</span> (res.code === <span class="hljs-number">0</span>) &#123;
                    <span class="hljs-keyword">return</span> callbackFunc(res);
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-keyword">return</span> errorCallbackFunc(res);
                &#125;
            &#125;
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传入要调用的方法名、参数和回调即可，它先校验了一下参数，然后会调用<code>window.WebViewJavascriptBridge.callHandler</code>方法。</p>
<p>此外也可以提供回调供原生调用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.WebViewJavascriptBridge.registerHandler(funcName, callbackFunc);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来看一下<code>window.WebViewJavascriptBridge</code>对象到底是啥。</p>
<h1 data-id="heading-1">安卓</h1>
<p><code>WebViewJavascriptBridge.js</code>文件内是一个自执行函数，首先定义了一些变量：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义变量</span>
<span class="hljs-keyword">var</span> messagingIframe;
<span class="hljs-keyword">var</span> sendMessageQueue = [];<span class="hljs-comment">// 发送消息的队列</span>
<span class="hljs-keyword">var</span> receiveMessageQueue = [];<span class="hljs-comment">// 接收消息的队列</span>
<span class="hljs-keyword">var</span> messageHandlers = &#123;&#125;;<span class="hljs-comment">// 消息处理器</span>

<span class="hljs-keyword">var</span> CUSTOM_PROTOCOL_SCHEME = <span class="hljs-string">'yy'</span>;<span class="hljs-comment">// 自定义协议</span>
<span class="hljs-keyword">var</span> QUEUE_HAS_MESSAGE = <span class="hljs-string">'__QUEUE_MESSAGE__/'</span>;

<span class="hljs-keyword">var</span> responseCallbacks = &#123;&#125;;<span class="hljs-comment">// 响应的回调</span>
<span class="hljs-keyword">var</span> uniqueId = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据变量名简单翻译了一下，具体用处接下来会分析。接下来定义了<code>WebViewJavascriptBridge</code>对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> WebViewJavascriptBridge = <span class="hljs-built_in">window</span>.WebViewJavascriptBridge = &#123;
    <span class="hljs-attr">init</span>: init,
    <span class="hljs-attr">send</span>: send,
    <span class="hljs-attr">registerHandler</span>: registerHandler,
    <span class="hljs-attr">callHandler</span>: callHandler,
    <span class="hljs-attr">_fetchQueue</span>: _fetchQueue,
    <span class="hljs-attr">_handleMessageFromNative</span>: _handleMessageFromNative
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到就是一个普通的对象，上面挂载了一些方法，具体方法暂时不看，继续往下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> doc = <span class="hljs-built_in">document</span>;
_createQueueReadyIframe(doc);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用了<code>_createQueueReadyIframe</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createQueueReadyIframe</span> (<span class="hljs-params">doc</span>) </span>&#123;
    messagingIframe = doc.createElement(<span class="hljs-string">'iframe'</span>);
    messagingIframe.style.display = <span class="hljs-string">'none'</span>;
    doc.documentElement.appendChild(messagingIframe);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法很简单，就是创建了一个隐藏的<code>iframe</code>插入到页面，继续往下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建一个Events类型（基础事件模块）的事件（Event）对象</span>
<span class="hljs-keyword">var</span> readyEvent = doc.createEvent(<span class="hljs-string">'Events'</span>);
<span class="hljs-comment">// 定义事件名为WebViewJavascriptBridgeReady</span>
readyEvent.initEvent(<span class="hljs-string">'WebViewJavascriptBridgeReady'</span>);
<span class="hljs-comment">// 通过document来触发该事件</span>
doc.dispatchEvent(readyEvent);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里定义了一个自定义事件，并直接派发了，其他地方可以像通过监听原生事件一样监听该事件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.addEventListener(
    <span class="hljs-string">'WebViewJavascriptBridgeReady'</span>,
    <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.WebViewJavascriptBridge)
    &#125;,
    <span class="hljs-literal">false</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的用处我理解就是当该<code>jsBridge</code>文件如果是在其他代码之后引入的话需要保证之前的代码能知道<code>window.WebViewJavascriptBridge</code>对象何时可用，如果规定该<code>jsBridge</code>必须要最先引入的话那么就不需要这个处理了。</p>
<p>到这里自执行函数就结束了，接下来看一下最开始的<code>init</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span> (<span class="hljs-params">messageHandler</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (WebViewJavascriptBridge._messageHandler) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'WebViewJavascriptBridge.init called twice'</span>);
    &#125;
    <span class="hljs-comment">// init调用的时候没有传参，所以messageHandler=undefined</span>
    WebViewJavascriptBridge._messageHandler = messageHandler;
    <span class="hljs-comment">// 当前receiveMessageQueue也只是一个空数组</span>
    <span class="hljs-keyword">var</span> receivedMessages = receiveMessageQueue;
    receiveMessageQueue = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < receivedMessages.length; i++) &#123;
        _dispatchMessageFromNative(receivedMessages[i]);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从初始化的角度来看，这个<code>init</code>方法似乎啥也没做。接下来我们来看<code>callHandler</code>方法，看看是如何调用安卓的方法的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHandler</span> (<span class="hljs-params">handlerName, data, responseCallback</span>) </span>&#123;
    _doSend(&#123;
        <span class="hljs-attr">handlerName</span>: handlerName,
        <span class="hljs-attr">data</span>: data
    &#125;, responseCallback);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理了一下参数又调用了<code>_doSend</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_doSend</span> (<span class="hljs-params">message, responseCallback</span>) </span>&#123;
    <span class="hljs-comment">// 如果提供了回调的话</span>
    <span class="hljs-keyword">if</span> (responseCallback) &#123;
        <span class="hljs-comment">// 生成一个唯一的回调id</span>
        <span class="hljs-keyword">var</span> callbackId = <span class="hljs-string">'cb_'</span> + (uniqueId++) + <span class="hljs-string">'_'</span> + <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
        <span class="hljs-comment">// 回调通过id存储到responseCallbacks对象上</span>
        responseCallbacks[callbackId] = responseCallback;
        <span class="hljs-comment">// 把该回调id添加到要发送给native的消息里</span>
        message.callbackId = callbackId;
    &#125;
    <span class="hljs-comment">// 消息添加到消息队列里</span>
    sendMessageQueue.push(message);
    messagingIframe.src = CUSTOM_PROTOCOL_SCHEME + <span class="hljs-string">'://'</span> + QUEUE_HAS_MESSAGE;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法首先把调用原生方法时的回调函数通过生成一个唯一的<code>id</code>保存到最开始定义的<code>responseCallbacks</code>对象里，然后把该<code>id</code>添加到要发送的信息上，所以一个<code>message</code>的结构是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    handlerName,
    data,
    callbackId
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着把该<code>message</code>添加到最开始定义的<code>sendMessageQueue</code>数组里，最后设置了<code>iframe</code>的<code>src</code>属性：<code>yy://__QUEUE_MESSAGE__/</code>，这其实就是一个自定义协议的<code>url</code>，我简单搜索了一下，<code>native</code>会拦截这个<code>url</code>来做相应的处理，到这里我们就走不下去了，因为不知道原生做了什么事情，简单搜索了一下，发现了这个库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmarcuswestin%2FWebViewJavascriptBridge" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/marcuswestin/WebViewJavascriptBridge" ref="nofollow noopener noreferrer">WebViewJavascriptBridge</a>，我司应该是在这个库基础上修改的，结合了网上的一些文章后大概知道了，原生拦截到这个<code>url</code>后会调用<code>js</code>的<code>window.WebViewJavascriptBridge._fetchQueue</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_fetchQueue</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 把我们要发送的消息队列转成字符串</span>
    <span class="hljs-keyword">var</span> messageQueueString = <span class="hljs-built_in">JSON</span>.stringify(sendMessageQueue);
    <span class="hljs-comment">// 清空消息队列</span>
    sendMessageQueue = [];
    <span class="hljs-comment">// 安卓无法直接读取返回的数据，因此还是通过iframe的src和java通信</span>
    messagingIframe.src = CUSTOM_PROTOCOL_SCHEME + <span class="hljs-string">'://return/_fetchQueue/'</span> + <span class="hljs-built_in">encodeURIComponent</span>(messageQueueString);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安卓拦截到<code>url</code>后，知道<code>js</code>给安卓发送消息了，所以主动调用<code>js</code>的<code>_fetchQueue</code>方法，取出之前添加到队列里的消息，因为无法直接读取<code>js</code>方法返回的数据，所以把格式化后的消息添加到<code>url</code>上，再次通过<code>iframe</code>来发送，此时原生又会拦截到<code>yy://return/_fetchQueue/</code>这个<code>url</code>，那么取出后面的消息，解析出要其中要执行的原生方法名和参数后执行对应的原生方法，当原生方法执行完后又会主动调用<code>js</code>的<code>window.WebViewJavascriptBridge._handleMessageFromNative</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_handleMessageFromNative</span> (<span class="hljs-params">messageJSON</span>) </span>&#123;
    <span class="hljs-comment">// 根据之前的init方法的逻辑我们知道receiveMessageQueue是会被设置为null的，所以会走else分支</span>
    <span class="hljs-keyword">if</span> (receiveMessageQueue) &#123;
        receiveMessageQueue.push(messageJSON);
    &#125; <span class="hljs-keyword">else</span> &#123;
        _dispatchMessageFromNative(messageJSON);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下<code>_dispatchMessageFromNative</code>方法做了什么：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_dispatchMessageFromNative</span> (<span class="hljs-params">messageJSON</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 原生发回的消息是字符串类型的，转成json</span>
        <span class="hljs-keyword">var</span> message = <span class="hljs-built_in">JSON</span>.parse(messageJSON);
        <span class="hljs-keyword">var</span> responseCallback;
        <span class="hljs-comment">// java调用完成，发回的responseId就是我们之前发送给它的callbackId</span>
        <span class="hljs-keyword">if</span> (message.responseId) &#123;
            <span class="hljs-comment">// 从responseCallbacks对象里取出该id关联的回调方法</span>
            responseCallback = responseCallbacks[message.responseId];
            <span class="hljs-keyword">if</span> (!responseCallback) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
            <span class="hljs-comment">// 执行回调，js调用安卓方法后到这里顺利收到消息</span>
            responseCallback(message.responseData);
            <span class="hljs-keyword">delete</span> responseCallbacks[message.responseId];
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// ...</span>
        &#125;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>messageJSON</code>就是原生发回的消息，里面除了执行完原生方法后返回的相关信息外，还带着之前我们传给它的<code>callbackId</code>，所以我们可以通过这个<code>id</code>来在<code>responseCallbacks</code>里找到关联的回调并执行，本次<code>js</code>调用原生方法流程结束。但是，明显函数里还有不存在<code>id</code>时的分支，这里是用来干啥的呢，我们前面介绍的都是<code>js</code>调用原生方法，但是显然，原生也可以直接给<code>js</code>发消息，比如常见的拦截返回键功能，当原生监听到返回键事件后它会主动发送信息告诉前端页面，页面就可以执行对应的逻辑，这个<code>else</code>分支就是用来处理这种情况：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_dispatchMessageFromNative</span> (<span class="hljs-params">messageJSON</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">if</span> (message.responseId) &#123;
            <span class="hljs-comment">// ...</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 和我们传给原生的消息可以带id一样，原生传给我们的消息也可以带一个id，同时原生内部也会通过这个id关联一个回调</span>
            <span class="hljs-keyword">if</span> (message.callbackId) &#123;
                <span class="hljs-keyword">var</span> callbackResponseId = message.callbackId;
                <span class="hljs-comment">//如果前端需要再给原生回消息的话那么就带上原生之前传来的id，这样原生就可以通过id找到对应的回调并执行</span>
                responseCallback = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">responseData</span>) </span>&#123;
                    _doSend(&#123;
                        <span class="hljs-attr">responseId</span>: callbackResponseId,
                        <span class="hljs-attr">responseData</span>: responseData
                    &#125;);
                &#125;;
            &#125;
            <span class="hljs-comment">// 我们并没有设置默认的_messageHandler，所以是undefined</span>
            <span class="hljs-keyword">var</span> handler = WebViewJavascriptBridge._messageHandler;
            <span class="hljs-comment">// 原生发送的消息里面有处理方法名称</span>
            <span class="hljs-keyword">if</span> (message.handlerName) &#123;
                <span class="hljs-comment">// 通过方法名称去messageHandlers对象里查找是否有对应的处理方法</span>
                handler = messageHandlers[message.handlerName];
            &#125;
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-comment">// 执行处理方法</span>
                handler(message.data， responseCallback);
            &#125; <span class="hljs-keyword">catch</span> (exception) &#123;
                <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">console</span> !== <span class="hljs-string">'undefined'</span>) &#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'WebViewJavascriptBridge: WARNING: javascript handler threw.'</span>, message, exception);
                &#125;
            &#125;
        &#125;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如我们要监听原生的返回键事件，我们先通过<code>window.WebViewJavascriptBridge</code>对象的方法注册一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.WebViewJavascriptBridge.registerHandler(<span class="hljs-string">'onBackPressed'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 做点什么...</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>registerHandler</code>方法如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerHandler</span> (<span class="hljs-params">handlerName, handler</span>) </span>&#123;
    messageHandlers[handlerName] = handler;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很简单，把我们要监听的事件名和方法都存储到<code>messageHandlers</code>对象上，然后如果原生监听到返回键事件后会发送如下结构的消息：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">handlerName</span>: <span class="hljs-string">'onBackPressed'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以通过<code>handlerName</code>找到我们注册的函数进行执行了。</p>
<p>到此，安卓环境的<code>js</code>和原生互相调用的逻辑就结束了，总结一下就是：</p>
<p>1.<code>js</code>调用原生</p>
<p>生成一个唯一的<code>id</code>，把回调和<code>id</code>保存起来，然后将要发送的信息（带上本次生成的唯一id）添加到一个队列里，之后通过<code>iframe</code>发送一个自定义协议的请求，原生拦截到后调用<code>js</code>的<code>window.WebViewJavascriptBridge</code>对象的一个方法来获取队列的信息，解析出请求和参数后执行对应的原生方法，然后再把响应（带上前端传来的id）通过调用<code>js</code>的<code>window.WebViewJavascriptBridge</code>的指定方法传递给前端，前端再通过<code>id</code>找到之前存储的回调，进行执行。</p>
<p>2.原生调用<code>js</code></p>
<p>首先前端需要事先注册要监听的事件，把事件名和回调保存起来，然后原生在某个时刻会调用<code>js</code>的<code>window.WebViewJavascriptBridge</code>对象的指定方法，前端根据返回参数的事件名找到注册的回调进行执行，同时原生也会传过来一个<code>id</code>，如果前端执行完相应逻辑后还要给原生回消息，那么要把该<code>id</code>带回去，原生根据该<code>id</code>来找到对应的回调进行执行。</p>
<p>可以看到，<code>js</code>和原生两边的逻辑都是一致的。</p>
<h1 data-id="heading-2">ios</h1>
<p><code>ios</code>和安卓基本是一致的，部分细节上有点区别，首先是协议不一样，<code>ios</code>的是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> CUSTOM_PROTOCOL_SCHEME_IOS = <span class="hljs-string">'https'</span>;
<span class="hljs-keyword">var</span> QUEUE_HAS_MESSAGE_IOS = <span class="hljs-string">'__wvjb_queue_message__'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后<code>ios</code>初始化创建<code>iframe</code>的时候会发送一个请求：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> BRIDGE_LOADED_IOS = <span class="hljs-string">'__bridge_loaded__'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createQueueReadyIframe</span> (<span class="hljs-params">doc</span>) </span>&#123;
    messagingIframe = doc.createElement(<span class="hljs-string">'iframe'</span>);
    messagingIframe.style.display = <span class="hljs-string">'none'</span>;
    <span class="hljs-keyword">if</span> (isIphone()) &#123;
        <span class="hljs-comment">// 这里应该是ios需要先加载一下bridge</span>
        messagingIframe.src = CUSTOM_PROTOCOL_SCHEME_IOS + <span class="hljs-string">'://'</span> + BRIDGE_LOADED_IOS;
    &#125;
    doc.documentElement.appendChild(messagingIframe);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再然后是<code>ios</code>获取我们的消息队列时不需要通过<code>iframe</code>，它能直接获取执行<code>js</code>函数返回的数据：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_fetchQueue</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> messageQueueString = <span class="hljs-built_in">JSON</span>.stringify(sendMessageQueue);
    sendMessageQueue = [];
    <span class="hljs-keyword">return</span> messageQueueString;<span class="hljs-comment">// 直接返回，不需要通过iframe</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他部分都是一样的。</p>
<h1 data-id="heading-3">总结</h1>
<p>本文分析了一下<code>jsBridge</code>的源码，可以发现其实是个很简单的东西，但是平时可能就没有去认真了解过它，总想做一些”大“的事情，以至于沦为了一个”好高骛远“的人，希望各位不要像笔者一样。</p>
<p>另外本文分析的只是笔者公司的<code>jsBridge</code>实现，可能有不一样、更好或更新的实现，欢迎留言探讨。</p></div>  
</div>
            