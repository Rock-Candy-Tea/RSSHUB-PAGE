
---
title: '基于websocket实现《全双工协议》的TS同步调用之Request_Response_Notify 原理与实战~'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22460aaf30854d12a50dd0c84b5a6c55~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 15:20:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22460aaf30854d12a50dd0c84b5a6c55~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">本章核心内容</h2>
<ul>
<li>什么是<code>全双工</code>协议，与<code>半双工</code>有什么本质区别？</li>
<li>如何实现全双工协议的<code>同步语法</code>调用？
<ul>
<li>即通过websocket向服务器发送一条消息，然后等待它的结果。如下图所示：</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22460aaf30854d12a50dd0c84b5a6c55~tplv-k3u1fbpfcp-watermark.image" alt="ws_sync_invoke.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>文末有<code>Go服务端</code>与<code>Web Typescript</code>源码~</p>
<blockquote>
<p>建议各位看官先<code>点赞</code>加<code>收藏</code>，方便以后查找~</p>
</blockquote>
<h2 data-id="heading-1">背景介绍</h2>
<p>在很多场景下，前端都会使用websocket实现一些长连相关的功能。但是在Web端，WebSocket接口的发送消息与接收消息是在<strong>两个不同的方法</strong>中，如下：</p>
<ul>
<li><code>WebSocket.onmessage</code>
<ul>
<li>An event listener to be called when a message is received from the server.</li>
</ul>
</li>
<li><code>WebSocket.send(data)</code>
<ul>
<li>Enqueues data to be transmitted.</li>
</ul>
</li>
</ul>
<blockquote>
<p>摘自【Websocket - <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebSocket" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket" ref="nofollow noopener noreferrer"><code>Web APIs | MDN</code></a>】</p>
</blockquote>
<p>因此如果你要实现一个上面的<code>请求</code>、<code>响应</code>的模式，对发送端来说，一种调用方式可能就是这样的：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> conn = <span class="hljs-keyword">new</span> w3cwebsocket(url)
conn.binaryType = <span class="hljs-string">"arraybuffer"</span>
conn.onopen = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.info(<span class="hljs-string">"websocket open - readyState:"</span>, conn.readyState)
    <span class="hljs-keyword">if</span> (conn.readyState === w3cwebsocket.OPEN) &#123;
        <span class="hljs-keyword">let</span> req = <span class="hljs-built_in">JSON</span>.stringify(&#123; <span class="hljs-string">"seq"</span>: <span class="hljs-number">1</span>, <span class="hljs-string">"msg"</span>: <span class="hljs-string">"hello world"</span> &#125;)
        conn.send(req)  <-- 请求
    &#125;
&#125;

conn.onclose = <span class="hljs-function">(<span class="hljs-params">e: ICloseEvent</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.debug(<span class="hljs-string">"event[onclose] fired"</span>)
&#125;

conn.onmessage = <span class="hljs-function">(<span class="hljs-params">evt: IMessageEvent</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> resp = <span class="hljs-built_in">JSON</span>.parse(<<span class="hljs-built_in">string</span>>evt.data)
    <span class="hljs-built_in">console</span>.info(resp) <-- 响应
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>请求与响应<code>分离</code>的编码逻辑，难受不~~</p>
</blockquote>
<p>因此，我们接下来就介绍如何解决这个问题。不过，在编码实现之前，容我介绍下关键点：<code>全双工</code>与<code>半双工</code>通信的区别。</p>
<h2 data-id="heading-2">全双工</h2>
<ul>
<li>全双工：通信双方可以<strong>同时</strong>发送信息对对方。</li>
<li>半双工：可以双向通信，但是<strong>同一时刻</strong>只能有一个方向在传输信息。</li>
</ul>
<blockquote>
<p>理解下基本概念即可，在不同的层级会不同的含义。</p>
</blockquote>
<p>我们都知道，Websocket与Http1.x都是基于TCP/IP之上的协议，而TCP也是全双工通信协议。为什么说Websocket就是全双工的通信协议，而Http1.x是半双工协议。而且Websocket还是在Http协议的基础上升级而来。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d52a4947b2a84c1c87fa076c2c9a1b37~tplv-k3u1fbpfcp-watermark.image" alt="http_websocket.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>难道Http1.x不是亲生的~</p>
</blockquote>
<p>本质的原因HTTP1.x协议是一个请求、响应的<strong>模式</strong>。在一次请求中，<code>Respose必定是在Request之后发生的</code>，请求包与响应包是不可能同时在网络中传输：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e41397b599004543b4beba59cb6a8d7d~tplv-k3u1fbpfcp-watermark.image" alt="http_half_duplex.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这就是为什么说Http1.x是一个半双工协议。</p>
</blockquote>
<p>如果从编码的角度来看，代码就很好写，因为请求与返回是有顺序的，一个伪逻辑如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">request</span>(<span class="hljs-params">req</span>)</span>&#123;
    conn.send(req)
    <span class="hljs-keyword">let</span> resp = conn.read()
    <span class="hljs-keyword">return</span> resp
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在一个全双工的通信中，消息之间是没有明确的顺序与关联关系的。如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0aaed14955bc448d8a23bcfc30bb10e8~tplv-k3u1fbpfcp-watermark.image" alt="ws_full_duplex.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然说websocket是一个全双工的通信协议，但是在它的协议中也没有<code>不同消息之间的关联信息</code>，当web端收到一条消息它也区分不出来谁与谁。因此，我们可以定义一个简单的<code>上层业务协议</code>，如下：</p>

























<table><thead><tr><th>属性</th><th>类型</th><th>说明</th></tr></thead><tbody><tr><td>Sequence</td><td>整形</td><td>消息序号</td></tr><tr><td>Type</td><td>枚举</td><td>1:请求/2:响应/3:通知</td></tr><tr><td>Message</td><td>string</td><td>消息内容</td></tr></tbody></table>
<p>如此一来，在逻辑上就可以对每个消息打下标记，还以上图为例：</p>

































<table><thead><tr><th>格式</th><th>消息</th></tr></thead><tbody><tr><td>Sequence: 1,Type: 1,Message: hello</td><td>Request1</td></tr><tr><td>Sequence: 2,Type: 1,Message: world</td><td>Request2</td></tr><tr><td>Sequence: 1,Type: 2,Message: ok</td><td>Response1</td></tr><tr><td>Sequence: 2,Type: 2,Message: ok</td><td>Response2</td></tr><tr><td>Sequence: 1,Type: 1,Message: test</td><td>Request3</td></tr><tr><td>Sequence: 1,Type: 3,Message: test</td><td>Notify3</td></tr></tbody></table>
<p>如此一来，就可以完成我们想要的逻辑了，只要通过<code>Sequence</code>和<code>Type</code>两个属性，就可以把一个请求与一个响应关联在一起。</p>
<blockquote>
<p>Sequence在客户端生成一条消息时<code>自增</code>即可。</p>
</blockquote>
<h2 data-id="heading-3">实战</h2>
<h3 data-id="heading-4">typescript代码</h3>
<p><code>第一步</code>：定义好相关对象：</p>
<ul>
<li>Message：业务协议</li>
<li>Request：模拟请求缓存</li>
<li>Response：模拟响应</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Message</span> </span>&#123;
    <span class="hljs-attr">sequence</span>: <span class="hljs-built_in">number</span> = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">type</span>: <span class="hljs-built_in">number</span> = <span class="hljs-number">1</span>;
    message?: <span class="hljs-built_in">string</span>;
    <span class="hljs-keyword">from</span>?: <span class="hljs-built_in">string</span>; <span class="hljs-comment">// sender</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">message?: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.message = message;
        <span class="hljs-built_in">this</span>.sequence = Seq.Next() <--- 自动生成序号
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Request</span> </span>&#123;
    <span class="hljs-attr">sendTime</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">callback</span>: <span class="hljs-function">(<span class="hljs-params">response: Message</span>) =></span> <span class="hljs-built_in">void</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">callback: (response: Message) => <span class="hljs-built_in">void</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.sendTime = <span class="hljs-built_in">Date</span>.now()
        <span class="hljs-built_in">this</span>.callback = callback
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Response</span> </span>&#123;
    <span class="hljs-attr">success</span>: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>
    message?: Message
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">success: <span class="hljs-built_in">boolean</span>, message?: Message</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.success = success;
        <span class="hljs-built_in">this</span>.message = message;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意，在Request中会有一个<code>callback</code>回调方法，这是实现<code>同步调用</code>的关键。</p>
</blockquote>
<p><code>第二步</code>：创建WebsocketClient对象，并创建一个名为<code>sendq</code>的用于保存请求的Map，然后实现一个<code>request</code>方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WebsocketClient</span> </span>&#123;
    <span class="hljs-keyword">private</span> sendq = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span><<span class="hljs-built_in">number</span>, Request>()      <--- 创建map
    
    <span class="hljs-keyword">async</span> request(data: Message): <span class="hljs-built_in">Promise</span><Response> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, _</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> seq = data.sequence

            <span class="hljs-comment">// asynchronous wait ack from server</span>
            <span class="hljs-keyword">let</span> callback = <span class="hljs-function">(<span class="hljs-params">msg: Message</span>) =></span> &#123;     <--- 创建回调
                // remove from sendq
                this.sendq.delete(seq)
                resolve(new Response(true, msg))
            &#125;

            this.sendq.set(seq, new Request(callback))  <--- 暂存 Request

            if (!this.send(JSON.stringify(data))) &#123;   <--- 发送消息
                resolve(new Response(false))
            &#125;
        &#125;)
    &#125;
    send(data: string): boolean &#123;
        try &#123;
            if (this.conn == null) &#123;
                return false
            &#125;
            this.conn.send(data)
        &#125; catch (error) &#123;
            return false
        &#125;
        return true
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果说Http的请求与响应是基于先后顺序关联，那么全双工的请求与响应关联的核心就是<code>sendq</code>这个Map对象了，它相当于在客户端缓存着<code>所有等待响应的请求</code>，有点拗口。</p>
<p>在这里request方法中，主要逻辑分三步：</p>
<ol>
<li>创建回调</li>
<li>暂存Request</li>
<li>发送消息</li>
</ol>
<p><code>第三步</code>：接收消息的处理，它在登录方法中：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">async</span> login(): <span class="hljs-built_in">Promise</span><&#123; <span class="hljs-attr">success</span>: <span class="hljs-built_in">boolean</span> &#125;> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state == State.CONNECTED) &#123;
        <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">success</span>: <span class="hljs-literal">false</span> &#125;
    &#125;
    <span class="hljs-built_in">this</span>.state = State.CONNECTING
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, _</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> conn = <span class="hljs-keyword">new</span> w3cwebsocket(<span class="hljs-built_in">this</span>.wsurl)
        conn.binaryType = <span class="hljs-string">"arraybuffer"</span>
        <span class="hljs-keyword">let</span> returned = <span class="hljs-literal">false</span>
        conn.onopen = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.info(<span class="hljs-string">"websocket open - readyState:"</span>, conn.readyState)
            <span class="hljs-keyword">if</span> (conn.readyState === w3cwebsocket.OPEN) &#123;
                returned = <span class="hljs-literal">true</span>
                resolve(&#123; <span class="hljs-attr">success</span>: <span class="hljs-literal">true</span> &#125;)
            &#125;
        &#125;

        <span class="hljs-comment">// overwrite onmessage</span>
        conn.onmessage = <span class="hljs-function">(<span class="hljs-params">evt: IMessageEvent</span>) =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-keyword">let</span> msg = <span class="hljs-keyword">new</span> Message();
                <span class="hljs-built_in">Object</span>.assign(msg, <span class="hljs-built_in">JSON</span>.parse(<<span class="hljs-built_in">string</span>>evt.data))
                <span class="hljs-keyword">if</span> (msg.type == <span class="hljs-number">2</span>) &#123;
                    <span class="hljs-keyword">let</span> req = <span class="hljs-built_in">this</span>.sendq.get(msg.sequence)       <----读取request
                    <span class="hljs-keyword">if</span> (req) &#123;
                        req.callback(msg)                        <----触发回调 
                    &#125;
                &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (msg.type == <span class="hljs-number">3</span>) &#123;
                    <span class="hljs-built_in">console</span>.log(msg.message, msg.from)
                &#125;
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                <span class="hljs-built_in">console</span>.error(evt.data, error)
            &#125;
        &#125;

        conn.onerror = <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.info(<span class="hljs-string">"websocket error: "</span>, error)
            <span class="hljs-keyword">if</span> (returned) &#123;
                resolve(&#123; <span class="hljs-attr">success</span>: <span class="hljs-literal">false</span> &#125;)
            &#125;
        &#125;

        conn.onclose = <span class="hljs-function">(<span class="hljs-params">e: ICloseEvent</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.debug(<span class="hljs-string">"event[onclose] fired"</span>)
            <span class="hljs-built_in">this</span>.onclose(e.reason)
        &#125;
        <span class="hljs-built_in">this</span>.conn = conn
        <span class="hljs-built_in">this</span>.state = State.CONNECTED
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在全双工的消息收发中没有统一顺序。因此在这里解析出<code>Message</code>对象之后，就会判断它的<strong>类型</strong>，如果是Response消息，就去<strong>sendq</strong>中找这个消息的请求<strong>Request</strong>，并调用回调方法。</p>
<h3 data-id="heading-5">Go服务端代码逻辑：</h3>
<p>在服务端主要实现了一个消息的广播，完成之后就给<code>发送者一个response消息</code>。主要逻辑在<code>handle</code>方法中，这里就不详细介绍了，感兴趣的可以直接看<code>源码</code>。</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">type</span> Message <span class="hljs-keyword">struct</span> &#123;
Sequence <span class="hljs-keyword">int</span>    <span class="hljs-string">`json:"sequence,omitempty"`</span>
Type     <span class="hljs-keyword">int</span>    <span class="hljs-string">`json:"type,omitempty"`</span>
Message  <span class="hljs-keyword">string</span> <span class="hljs-string">`json:"message,omitempty"`</span>
From     <span class="hljs-keyword">string</span> <span class="hljs-string">`json:"from,omitempty"`</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(m *Message)</span> <span class="hljs-title">MarshalJSON</span><span class="hljs-params">()</span> []<span class="hljs-title">byte</span></span> &#123;
bts, _ := json.Marshal(m)
<span class="hljs-keyword">return</span> bts
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">parseMessage</span><span class="hljs-params">(text <span class="hljs-keyword">string</span>)</span> *<span class="hljs-title">Message</span></span> &#123;
<span class="hljs-keyword">var</span> msg Message
_ = json.Unmarshal([]<span class="hljs-keyword">byte</span>(text), &msg)
<span class="hljs-keyword">return</span> &msg
&#125;

<span class="hljs-comment">// 广播消息</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(s *Server)</span> <span class="hljs-title">handle</span><span class="hljs-params">(user <span class="hljs-keyword">string</span>, text <span class="hljs-keyword">string</span>)</span></span> &#123;
logrus.Infof(<span class="hljs-string">"recv message %s from %s"</span>, text, user)
s.Lock()
<span class="hljs-keyword">defer</span> s.Unlock()
msg := parseMessage(text)
msg.From = user
msg.Type = <span class="hljs-number">3</span> <span class="hljs-comment">//notify type</span>
notice := msg.MarshalJSON()
<span class="hljs-keyword">for</span> u, conn := <span class="hljs-keyword">range</span> s.users &#123;
<span class="hljs-keyword">if</span> u == user &#123;
<span class="hljs-keyword">continue</span>
&#125;
logrus.Infof(<span class="hljs-string">"send to %s : %s"</span>, u, text)
err := s.writeText(conn, notice)
<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> &#123;
logrus.Errorf(<span class="hljs-string">"write to %s failed, error: %v"</span>, user, err)
&#125;
&#125;

conn := s.users[user]
        resp := Message&#123;                 <--- 创建响应包
Sequence: msg.Sequence,  <--- 序号一定要与请求包中相同
Type:     <span class="hljs-number">2</span>, <span class="hljs-comment">//response type</span>
Message:  <span class="hljs-string">"ok"</span>,
&#125;
_ = s.writeText(conn, resp.MarshalJSON())
&#125;

<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-params">(s *Server)</span> <span class="hljs-title">writeText</span><span class="hljs-params">(conn net.Conn, message []<span class="hljs-keyword">byte</span>)</span> <span class="hljs-title">error</span></span> &#123;
<span class="hljs-comment">// 创建文本帧数据</span>
f := ws.NewTextFrame(message)
err := conn.SetWriteDeadline(time.Now().Add(s.options.writewait))
<span class="hljs-keyword">if</span> err != <span class="hljs-literal">nil</span> &#123;
<span class="hljs-keyword">return</span> err
&#125;
<span class="hljs-keyword">return</span> ws.WriteFrame(conn, f)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">演示示例</h3>
<p>最终得到我们想要的结果：</p>
<blockquote>
<p>let resp = await cli.request(req)</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// index.ts</span>
<span class="hljs-keyword">const</span> main = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">let</span> cli = <span class="hljs-keyword">new</span> WebsocketClient(<span class="hljs-string">"ws://localhost:8000"</span>, <span class="hljs-string">"ccc"</span>);
    <span class="hljs-keyword">let</span> &#123; success &#125; = <span class="hljs-keyword">await</span> cli.login()
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"client login return -- "</span>, success)

    <span class="hljs-keyword">let</span> req = <span class="hljs-keyword">new</span> Message(<span class="hljs-string">"hello"</span>)
    <span class="hljs-keyword">let</span> resp = <span class="hljs-keyword">await</span> cli.request(req)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"client request"</span>, req, <span class="hljs-string">"return"</span>, resp.message)

    <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">5</span>)
    cli.logout()
&#125;

main()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行看到输出如下：</p>
<pre><code class="copyable">$ ts-node index.ts
websocket open - readyState: 1
client login return --  true
client request Message &#123; sequence: 1, type: 1, message: 'hello' &#125; return Message &#123; sequence: 1, type: 2, message: 'ok' &#125;
event[onclose] fired
connection closed due to Normal connection closure
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">最后总结</h2>
<p>本文介绍了全双工与半双工<strong>概念</strong>与<strong>本质区别</strong>。同时通过<code>业务协议</code>与<code>Promise</code>完成了全双工通信下的请求与响应的同步调用逻辑。</p>
<p>github源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fklintcheng%2Fdemo%2Ftree%2Fmaster%2Fwebsocket" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/klintcheng/demo/tree/master/websocket" ref="nofollow noopener noreferrer">klintcheng/demo</a></p>
<blockquote>
<p>最后，最多精彩知识尽在我编写的这本小册中 <a href="https://juejin.cn/book/6963277002044342311/section" target="_blank" title="https://juejin.cn/book/6963277002044342311/section">分布式IM原理与实战: 从0到1打造即时通讯云</a>。</p>
</blockquote>
<p><a href="https://juejin.cn/book/6963277002044342311" target="_blank" title="https://juejin.cn/book/6963277002044342311"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea69f8ffb2f444b7ab6e83a998e3806f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<blockquote>
<p>看都看到这里了，还不顺手一个<code>点赞</code>。</p>
</blockquote></div>  
</div>
            