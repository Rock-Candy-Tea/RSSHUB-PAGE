
---
title: '优雅封装微信小程序Websocket(Remax版)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e812ac7cfd874809bd6b00765eb3d3d8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 01:45:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e812ac7cfd874809bd6b00765eb3d3d8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>使用了Remax很长的时间，之前使用javascript版本</p>
<p>在六月份项目准备使用Typescript重构，故重新思考整理一个版本</p>
<h3 data-id="heading-0">小小知识点</h3>
<p>微信小程序的<a href="https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.close.html" target="_blank" rel="nofollow noopener noreferrer">wx.connectSocket</a>只能同时对一个ws/wss的websocket发起最多两次请求，对于多个不同的websocket地址可以使用最多5个连接。</p>
<p>微信<a href="https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.html" target="_blank" rel="nofollow noopener noreferrer">SocketTask</a>是先使用connectSocket建立连接后可以返回一个SocketTask的对象。可以将这个连接存储在当前内部。但是不推荐，因为当页面刷新后websocket的连接很可能会丢失。而使用本地的localstroage进行缓存是拿不到的socket.
所以建议，每次使用新的websocket连接的时候实例化一次。再传入相应的ws/wss连接进行链接操作。</p>
<p>Websocket的调用是有时序的
( 连接 - 判断是否已打开 - 接收服务器的参数 - 发送给服务器信息 )
wx.connectSocket -> wx.onSocketOpen -> wx.onReceivedMsg -> wx.sendSocketMessage</p>
<p>所以当遇到无法发送或者接收服务器和推送数据到服务器的时候，应该检查一下执行时序的问题。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-attr">filename</span>: src/utils/websocket.ts

<span class="hljs-keyword">import</span> &#123;
    connectSocket,
    closeSocket,
    onSocketOpen,
    onSocketClose,
    sendSocketMessage,
    onSocketMessage,
    getNetworkType,
    onNetworkStatusChange,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'remax/wechat'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Websocket</span> </span>&#123;
    <span class="hljs-comment">// 是否连接</span>
    <span class="hljs-attr">isConnect</span>: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
    <span class="hljs-comment">// 当前网络状态</span>
    <span class="hljs-keyword">private</span> netWork: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
    <span class="hljs-comment">// 是否人为退出</span>
    <span class="hljs-keyword">private</span> isClosed: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
    <span class="hljs-comment">// 心跳检测频率</span>
    <span class="hljs-keyword">private</span> timeout: <span class="hljs-built_in">number</span> = <span class="hljs-number">3</span> * <span class="hljs-number">1000</span>;
    <span class="hljs-keyword">private</span> timeoutObj: NodeJS.Timeout | <span class="hljs-literal">undefined</span>;
    <span class="hljs-comment">// 当前重连次数</span>
    <span class="hljs-keyword">private</span> connectNum: <span class="hljs-built_in">number</span> = <span class="hljs-number">0</span>;
    <span class="hljs-comment">// 心跳检测和断线重连开关，true为启用，false为关闭</span>
    heartCheck: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>
    <span class="hljs-attr">isReconnect</span>: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>
    <span class="hljs-comment">// 连接信息</span>
    wsUrl = <span class="hljs-string">''</span>
    <span class="hljs-comment">// 消息队列</span>
    messageQueue = []

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">heartCheck: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>, isReconnect: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span></span>)</span> &#123;
        <span class="hljs-comment">// 心跳检测和断线重连开关，true为启用，false为关闭</span>
        <span class="hljs-built_in">this</span>.heartCheck = heartCheck;
        <span class="hljs-built_in">this</span>.isReconnect = isReconnect;
    &#125;

    <span class="hljs-comment">// 心跳开始</span>
    <span class="hljs-function"><span class="hljs-title">start</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>;
        <span class="hljs-built_in">this</span>.timeoutObj = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
            sendSocketMessage(&#123;
                <span class="hljs-comment">// 发送心跳信息</span>
                <span class="hljs-attr">data</span>: <span class="hljs-built_in">JSON</span>.stringify(&#123;
                    <span class="hljs-attr">beat</span>: <span class="hljs-string">'dj'</span>,
                &#125;),
                <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-comment">// console.log("发送心跳成功");</span>
                &#125;,
                <span class="hljs-function"><span class="hljs-title">fail</span>(<span class="hljs-params">err</span>)</span> &#123;
                    <span class="hljs-built_in">console</span>.log(err);
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'连接失败'</span>);
                    self.reConnect()
                    self.reset();
                &#125;,
            &#125;).then();
        &#125;, <span class="hljs-built_in">this</span>.timeout);
    &#125;

    <span class="hljs-comment">// 心跳重置</span>
    <span class="hljs-function"><span class="hljs-title">reset</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.timeoutObj) &#123;
            <span class="hljs-built_in">clearTimeout</span>(<span class="hljs-built_in">this</span>.timeoutObj);
        &#125;
        <span class="hljs-comment">// 返回this即可支持链式调用</span>
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
    &#125;

    <span class="hljs-comment">// 初始化连接</span>
    <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">wsUrl: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isConnect) &#123;
            <span class="hljs-built_in">this</span>.onSocketOpened()
            <span class="hljs-built_in">this</span>.onNetworkChange()
            <span class="hljs-built_in">this</span>.onSocketClosed()
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 检查网络状态</span>
            <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>;
            getNetworkType(&#123;
                <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
                    <span class="hljs-keyword">if</span> (res.networkType !== <span class="hljs-string">'none'</span>) &#123;
                        <span class="hljs-comment">// 开始建立连接</span>
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始连接'</span>)
                        self.connect(wsUrl)
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        self.netWork = <span class="hljs-literal">false</span>;
                        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'网络已断开'</span>);
                    &#125;
                &#125;,
            &#125;).then();
        &#125;
    &#125;

    <span class="hljs-comment">// 连接websocket</span>
    <span class="hljs-function"><span class="hljs-title">connect</span>(<span class="hljs-params">wsUrl: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-comment">// connectSocket不支持异步调用</span>
        <span class="hljs-keyword">let</span> self = <span class="hljs-built_in">this</span>;
        connectSocket(&#123;
            <span class="hljs-attr">url</span>: wsUrl,
            <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
                <span class="hljs-keyword">if</span> (res.errMsg == <span class="hljs-string">'connectSocket:ok'</span>) &#123;
                    self.isConnect = <span class="hljs-literal">true</span>
                    self.wsUrl = wsUrl
                    self.onSocketOpened()
                    self.onNetworkChange()
                    self.onSocketClosed()
                &#125;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">fail</span>(<span class="hljs-params">err</span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(err)
            &#125;,
        &#125;);
    &#125;

    <span class="hljs-comment">// 重连方法，会根据时间频率越来越慢，分别为3秒，10秒，45秒</span>
    <span class="hljs-function"><span class="hljs-title">reConnect</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.connectNum)
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isConnect) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.connectNum < <span class="hljs-number">3</span>) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">this</span>.init(<span class="hljs-built_in">this</span>.wsUrl);
                &#125;, <span class="hljs-number">3</span> * <span class="hljs-number">1000</span>);
                <span class="hljs-built_in">this</span>.connectNum += <span class="hljs-number">1</span>;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.connectNum < <span class="hljs-number">10</span>) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">this</span>.init(<span class="hljs-built_in">this</span>.wsUrl);
                &#125;, <span class="hljs-number">10</span> * <span class="hljs-number">1000</span>);
                <span class="hljs-built_in">this</span>.connectNum += <span class="hljs-number">1</span>;
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">this</span>.init(<span class="hljs-built_in">this</span>.wsUrl);
                &#125;, <span class="hljs-number">45</span> * <span class="hljs-number">1000</span>);
                <span class="hljs-built_in">this</span>.connectNum += <span class="hljs-number">1</span>;
            &#125;
        &#125;
    &#125;

    <span class="hljs-comment">// 关闭websocket连接</span>
    <span class="hljs-function"><span class="hljs-title">close</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isConnect) &#123;
            closeSocket().then()
            <span class="hljs-comment">// 重置心跳并改变相应状态</span>
            <span class="hljs-built_in">this</span>.reset()
            <span class="hljs-built_in">this</span>.isClosed = <span class="hljs-literal">true</span>;
            <span class="hljs-built_in">this</span>.isConnect = <span class="hljs-literal">false</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'没有websocket连接'</span>)
        &#125;
    &#125;

    <span class="hljs-comment">// 监听websocket连接关闭</span>
    <span class="hljs-function"><span class="hljs-title">onSocketClosed</span>(<span class="hljs-params"></span>)</span> &#123;
        onSocketClose(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`当前websocket连接已关闭,错误信息为:<span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(err)&#125;</span>`</span>);
            <span class="hljs-comment">// 停止心跳连接</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.heartCheck) &#123;
                <span class="hljs-built_in">this</span>.reset();
            &#125;
            <span class="hljs-comment">// 关闭已登录开关</span>
            <span class="hljs-built_in">this</span>.isConnect = <span class="hljs-literal">false</span>;
            <span class="hljs-comment">// 检测是否是用户自己退出小程序</span>
            <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isClosed) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'进来了这里...'</span>)
                <span class="hljs-comment">// 进行重连</span>
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isReconnect) &#123;
                    <span class="hljs-built_in">this</span>.reConnect();
                &#125;
            &#125;
        &#125;);
    &#125;

    <span class="hljs-comment">// 检测网络变化</span>
    <span class="hljs-function"><span class="hljs-title">onNetworkChange</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> self = <span class="hljs-built_in">this</span>;
        onNetworkStatusChange(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (res.isConnected) &#123;
                self.isConnect = <span class="hljs-literal">false</span>;
                self.reConnect()
            &#125;
        &#125;);
    &#125;

    <span class="hljs-comment">// socket已开启</span>
    <span class="hljs-function"><span class="hljs-title">onSocketOpened</span>(<span class="hljs-params"></span>)</span> &#123;
        onSocketOpen(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'websocket已打开'</span>);
            <span class="hljs-comment">// 打开已连接开关</span>
            <span class="hljs-built_in">this</span>.isConnect = <span class="hljs-literal">true</span>;
            <span class="hljs-built_in">this</span>.netWork = <span class="hljs-literal">true</span>;
            <span class="hljs-comment">// 发送心跳</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.heartCheck) &#123;
                <span class="hljs-built_in">this</span>.reset().start();
            &#125;
        &#125;);
    &#125;

    <span class="hljs-comment">// 接收服务器返回的消息</span>
    <span class="hljs-function"><span class="hljs-title">onReceivedMsg</span>(<span class="hljs-params">callBack: <span class="hljs-built_in">any</span></span>)</span> &#123;
        onSocketMessage(<span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callBack === <span class="hljs-string">'function'</span>) &#123;
                callBack(msg);
            &#125;
        &#125;);
    &#125;

    <span class="hljs-comment">// 发送ws消息</span>
    <span class="hljs-function"><span class="hljs-title">sendWebSocketMsg</span>(<span class="hljs-params">options: <span class="hljs-built_in">any</span></span>)</span> &#123;
        sendSocketMessage(&#123;
            <span class="hljs-attr">data</span>: options.data,
            <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
                <span class="hljs-keyword">if</span> (options.success && <span class="hljs-keyword">typeof</span> options.success === <span class="hljs-string">'function'</span>) &#123;
                    options.success(res);
                &#125;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">fail</span>(<span class="hljs-params">err</span>)</span> &#123;
                <span class="hljs-keyword">if</span> (options.fail && <span class="hljs-keyword">typeof</span> options.fail === <span class="hljs-string">'function'</span>) &#123;
                    options.fail(err);
                &#125;
            &#125;,
        &#125;).then();
    &#125;
&#125;

<span class="hljs-keyword">const</span> websocket = <span class="hljs-keyword">new</span> Websocket(
    <span class="hljs-comment">// true代表启用心跳检测和断线重连</span>
    <span class="hljs-literal">true</span>,
    <span class="hljs-literal">true</span>,
);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> websocket;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何使用呢？</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">filename: src/page/index.tsx

<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123;View, Text, Image, Button&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'remax/wechat'</span>;
<span class="hljs-keyword">import</span> styles <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-keyword">import</span> websocket <span class="hljs-keyword">from</span> <span class="hljs-string">"@/utils/wxsocket"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => &#123;
    <span class="hljs-keyword">const</span> connectWs = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> wsUrl = <span class="hljs-string">`ws://测试或者线上的ws地址信息如果是https加密则使用wss://`</span>
        <span class="hljs-keyword">if</span> (!websocket.isConnect) &#123;
            websocket.init(wsUrl)
        &#125;
    &#125;
    <span class="hljs-keyword">const</span> closeWs = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span> (websocket.isConnect) &#123;
            websocket.close()
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.app&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.header&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Image</span>
                    <span class="hljs-attr">src</span>=<span class="hljs-string">"https://gw.alipayobjects.com/mdn/rms_b5fcc5/afts/img/A*OGyZSI087zkAAAAAAAAAAABkARQnAQ"</span>
                    <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;styles.logo&#125;</span>
                /></span>
                <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> connectWs()&#125;>开始连接ws服务器<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> closeWs()&#125;>关闭ws连接服务器<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">View</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    );
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>连接上后
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e812ac7cfd874809bd6b00765eb3d3d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
关闭链接后
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83d2dbab21c143e4916291f5be43dc8c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            