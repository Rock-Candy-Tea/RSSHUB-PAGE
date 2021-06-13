
---
title: 'JS_node获取本机ip的方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7577'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 06:30:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=7577'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>公众号：<strong><a href="https://juejin.cn/post/6972913930226106399#wechat">暮北林</a></strong><br></p>
</blockquote>
<p>Q Q 群 :  <strong><a href="https://juejin.cn/post/6972913930226106399#qq">一起学前端</a></strong><br>
Javascript/node如何获取本机IP</p>
<p>[TOC]</p>
<h3 data-id="heading-0">为什么要获取本机IP</h3>
<ol>
<li>以前做的一个Electron的客户端启动Server需要把本机IP显示出来</li>
<li>一个基于RK3399的硬件平台的APP进行串口通信另一方需要进行IP校验</li>
</ol>
<h3 data-id="heading-1">如何获取</h3>
<p>我们知道JS是客户端语言,单纯的JS是无法获取本机IP的,即使有navigator也只能获取网络的连接类型和监听网络的变化,而无法得知IP信息</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.navagator.connection;
&#123;
  <span class="hljs-attr">downlink</span>: <span class="hljs-number">2.95</span>
  <span class="hljs-attr">downlinkMax</span>: <span class="hljs-literal">Infinity</span>
  <span class="hljs-attr">effectiveType</span>: <span class="hljs-string">"4g"</span>
  <span class="hljs-attr">onchange</span>: <span class="hljs-literal">null</span>
  <span class="hljs-attr">ontypechange</span>: <span class="hljs-literal">null</span>
  <span class="hljs-attr">rtt</span>: <span class="hljs-number">50</span>
  <span class="hljs-attr">saveData</span>: <span class="hljs-literal">false</span>
  <span class="hljs-attr">type</span>: <span class="hljs-string">"wifi"</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然BOM的API无法获取我们可以采取其他方式</p>
<h3 data-id="heading-2">JS获取本机IP</h3>
<ol>
<li>通过接口让Server端告知我们的client ip</li>
<li>通过WebRTC来获取本机IP</li>
</ol>
<h3 data-id="heading-3">JS通过接口获取</h3>
<p>我们可以发送一个Request,在Server端就可以得知我们的IP,连接外网的情况外网Server得知的就是外网IP,只有内网的情况下Server得知的就是我们的内网IP,总之一句话通过接口获取的IP都是相对IP</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">"express"</span>);
<span class="hljs-keyword">const</span> app = express();

app.set(<span class="hljs-string">'trust proxy'</span>, <span class="hljs-literal">true</span>);
app.get(<span class="hljs-string">"/api/get_pubip"</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; ip &#125; = req;
    res.send(&#123;<span class="hljs-attr">code</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">data</span>: &#123;ip&#125;, <span class="hljs-attr">msg</span>: <span class="hljs-string">"success"</span>&#125;);
&#125;)
app.listen(<span class="hljs-number">3002</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>经过测试在没有经过代理的情况下本机localhost访问返回数据为</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// http://localhost:3002/api/get_pubip</span>
&#123;
  <span class="hljs-attr">"code"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">"data"</span>: &#123;<span class="hljs-attr">"ip"</span>: <span class="hljs-string">"::1"</span>&#125;,
  <span class="hljs-attr">"msg"</span>: <span class="hljs-string">"success"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>经过nginx代理本机访问的返回数据</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// http://localhost:8080/api/get_pubip</span>
&#123;
  <span class="hljs-attr">"code"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">"data"</span>: &#123;<span class="hljs-attr">"ip"</span>: <span class="hljs-string">"::ffff:127.0.0.1"</span>&#125;,
  <span class="hljs-attr">"msg"</span>: <span class="hljs-string">"success"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>其他机器(192.168.0.110)访问返回数据</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// http://l192.168.0.108/api/get_pubip</span>
&#123;
  <span class="hljs-attr">"code"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">"data"</span>: &#123;<span class="hljs-attr">"ip"</span>: <span class="hljs-string">"::ffff:192.168.0.110"</span>&#125;,
  <span class="hljs-attr">"msg"</span>: <span class="hljs-string">"success"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">WebRTC获取本机IP</h3>
<p>WebRTC进行音视频通话时是需要进行媒体协商和网络协商的,在网络协商的过程中就需要知道双方的内外网IP地址,网络协商是需要借助IceServer的帮助的,协商通过后就可以进行后续的UPD通信进行音视频数据的packet发送</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getIPs</span>(<span class="hljs-params">callback</span>)</span>&#123;
    <span class="hljs-keyword">var</span> ip_dups = &#123;&#125;;
    <span class="hljs-keyword">var</span> RTCPeerConnection = <span class="hljs-built_in">window</span>.RTCPeerConnection
        || <span class="hljs-built_in">window</span>.mozRTCPeerConnection
        || <span class="hljs-built_in">window</span>.webkitRTCPeerConnection;
    <span class="hljs-keyword">var</span> useWebKit = !!<span class="hljs-built_in">window</span>.webkitRTCPeerConnection;
    <span class="hljs-keyword">var</span> mediaConstraints = &#123;
        <span class="hljs-attr">optional</span>: [&#123;<span class="hljs-attr">RtpDataChannels</span>: <span class="hljs-literal">true</span>&#125;]
    &#125;;
    <span class="hljs-comment">// 这里就是需要的ICEServer了</span>
    <span class="hljs-keyword">var</span> servers = &#123;
        <span class="hljs-attr">iceServers</span>: [
            &#123;<span class="hljs-attr">urls</span>: <span class="hljs-string">"stun:stun.services.mozilla.com"</span>&#125;, 
            &#123;<span class="hljs-attr">urls</span>: <span class="hljs-string">"stun:stun.l.google.com:19302"</span>&#125;,
        ]
    &#125;;
    <span class="hljs-keyword">var</span> pc = <span class="hljs-keyword">new</span> RTCPeerConnection(servers, mediaConstraints);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleCandidate</span>(<span class="hljs-params">candidate</span>)</span>&#123;
        <span class="hljs-keyword">var</span> ip_regex = <span class="hljs-regexp">/([0-9]&#123;1,3&#125;(\.[0-9]&#123;1,3&#125;)&#123;3&#125;|[a-f0-9]&#123;1,4&#125;(:[a-f0-9]&#123;1,4&#125;)&#123;7&#125;)/</span>
        <span class="hljs-keyword">var</span> hasIp = ip_regex.exec(candidate)
        <span class="hljs-keyword">if</span> (hasIp) &#123;
            <span class="hljs-keyword">var</span> ip_addr = ip_regex.exec(candidate)[<span class="hljs-number">1</span>];
            <span class="hljs-keyword">if</span>(ip_dups[ip_addr] === <span class="hljs-literal">undefined</span>)
                callback(ip_addr);
            ip_dups[ip_addr] = <span class="hljs-literal">true</span>;
        &#125;
    &#125;
    <span class="hljs-comment">// 网络协商的过程</span>
    pc.onicecandidate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ice</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(ice.candidate) &#123;
            handleCandidate(ice.candidate.candidate);
        &#125;   
    &#125;;
    pc.createDataChannel(<span class="hljs-string">""</span>);
    <span class="hljs-comment">//创建一个SDP(session description protocol)会话描述协议 是一个纯文本信息 包含了媒体和网络协商的信息</span>
    pc.createOffer(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>)</span>&#123;
      pc.setLocalDescription(result, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;);
    &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> lines = pc.localDescription.sdp.split(<span class="hljs-string">'\n'</span>);
        lines.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">line</span>)</span>&#123;
            <span class="hljs-keyword">if</span>(line.indexOf(<span class="hljs-string">'a=candidate:'</span>) === <span class="hljs-number">0</span>)
                handleCandidate(line);
        &#125;);
    &#125;, <span class="hljs-number">1000</span>);
&#125;
getIPs(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ip</span>)</span>&#123;<span class="hljs-built_in">console</span>.log(ip);&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webrtc得到的IP结果和开源API获取的结果对比</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// WebRTC获取的结果 122.4.121.156</span>
<span class="hljs-comment">// 开源API获取到的IP地址</span>
&#123;
  <span class="hljs-attr">"ip"</span>: <span class="hljs-string">"122.4.121.156"</span>,
  <span class="hljs-attr">"city"</span>: <span class="hljs-number">1569</span>,
  <span class="hljs-attr">"region"</span>: <span class="hljs-string">"中国|0|山东省|青岛市|电信"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实Webrtc在媒体协商时获取的IP不止一个,总共有四种类型<code>host</code> <code>srflx</code> <code>prflx</code> <code>relay</code></p>
<h4 data-id="heading-5">candidate四种类型说明</h4>




































































<table><thead><tr><th align="center">候选类型</th><th align="center">code</th><th align="center">来源</th><th align="center">传输</th><th align="center">用途</th></tr></thead><tbody><tr><td align="center">主机候选项</td><td align="center">host</td><td align="center">网卡</td><td align="center">信令服务</td><td align="center">从网卡中获取本地传输地址</td></tr><tr><td align="center">服务器反射候选项</td><td align="center">srflx</td><td align="center">STUN</td><td align="center">信令服务</td><td align="center">从发给stun服务的stun检查中获取到的传输地址</td></tr><tr><td align="center">对象反射候选项</td><td align="center">prflx</td><td align="center">ICE代理</td><td align="center">STUN Binding</td><td align="center">从对方ice代理发送stun连接检查中获取的传输地址</td></tr><tr><td align="center">中继候选者</td><td align="center">relay</td><td align="center">TURN</td><td align="center">信令服务器</td><td align="center">媒体中继服务器的传输地址</td></tr><tr><td align="center">#### 你会发现Webrtc是无法获取到本机IP</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center"></td></tr><tr><td align="center">host获取的一直是xxxxx.local的东东为什么呢?</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center"></td></tr><tr><td align="center">请参考文末的<code>mdns</code>文档</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center"></td></tr><tr><td align="center">### 接下来看看用node如何获取本机ip</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center"></td></tr></tbody></table>
<ul>
<li>
<ol>
<li>通过os模块来获取</li>
</ol>
</li>
<li>
<ol start="2">
<li>通过广播来获取</li>
</ol>
</li>
</ul>
<h3 data-id="heading-6">OS模块获取本机IP</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> netDict = os.networkInterfaces();
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> devName <span class="hljs-keyword">in</span> netDict) &#123;
    <span class="hljs-keyword">let</span> netList = netDict[devName];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < netList.length; i++) &#123;
        <span class="hljs-keyword">let</span> &#123; address, family, internal,mac &#125; = netList[i],
            isvm = isVmNetwork(mac);
        <span class="hljs-keyword">if</span> (family === <span class="hljs-string">'IPv4'</span> && address !== <span class="hljs-string">'127.0.0.1'</span> && !internal) &#123;
            <span class="hljs-keyword">return</span> address;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上方法确实获取本机IP 但是<strong>假如你本机装了一个虚拟机</strong>获取的ip可能就是你虚拟机的IP了
或者<strong>你通过VPN访问网络</strong>获取到的有可能是你的VPN分配的IP,所以我们需要根据MAC地址来判断是否是虚拟机/VPN</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 增加一个判断VM虚拟机的方法  </span>
<span class="hljs-comment">// 在上面方法的if中加上这个方法的返回判断就行了</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isVmNetwork</span> (<span class="hljs-params">mac</span>) </span>&#123;
    <span class="hljs-comment">// 常见的虚拟网卡MAC地址和厂商</span>
    <span class="hljs-keyword">let</span> vmNetwork = [
        <span class="hljs-string">"00:05:69"</span>, <span class="hljs-comment">//vmware1</span>
        <span class="hljs-string">"00:0C:29"</span>, <span class="hljs-comment">//vmware2</span>
        <span class="hljs-string">"00:50:56"</span>, <span class="hljs-comment">//vmware3</span>
        <span class="hljs-string">"00:1C:42"</span>, <span class="hljs-comment">//parallels1</span>
        <span class="hljs-string">"00:03:FF"</span>, <span class="hljs-comment">//microsoft virtual pc</span>
        <span class="hljs-string">"00:0F:4B"</span>, <span class="hljs-comment">//virtual iron 4</span>
        <span class="hljs-string">"00:16:3E"</span>, <span class="hljs-comment">//red hat xen , oracle vm , xen source, novell xen</span>
        <span class="hljs-string">"08:00:27"</span>, <span class="hljs-comment">//virtualbox</span>
        <span class="hljs-string">"00:00:00"</span>, <span class="hljs-comment">// VPN</span>
    ]
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < vmNetwork.length; i++) &#123;
        <span class="hljs-keyword">let</span> mac_per = vmNetwork[i];
        <span class="hljs-keyword">if</span> (mac.startsWith(mac_per)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">广播获取本机IP</h3>
<p>开启一个广播服务端监听message并发送广播,就可以接受到本机发送的广播,从而获取到发送端(本机)的address信息</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> dgram = <span class="hljs-built_in">require</span>(<span class="hljs-string">"dgram"</span>);
<span class="hljs-keyword">const</span> socket = dgram.createSocket(<span class="hljs-string">"udp4"</span>);

<span class="hljs-keyword">const</span> getLocalIp = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        socket.on(<span class="hljs-string">"error"</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            reject(err);
            socket.close();
        &#125;)
        
        socket.on(<span class="hljs-string">"message"</span>, <span class="hljs-function">(<span class="hljs-params">msg, rinfo</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> &#123; address, port &#125; = rinfo;
            resolve(address);
        &#125;)
        
        socket.bind(<span class="hljs-number">19319</span>, <span class="hljs-function"><span class="hljs-params">_</span>=></span> &#123;
            socket.setBroadcast(<span class="hljs-literal">true</span>);
        &#125;);
        <span class="hljs-keyword">var</span> message = <span class="hljs-keyword">new</span> Buffer.from(<span class="hljs-string">"hello"</span>);
        socket.send(message, <span class="hljs-number">0</span>, message.length,  <span class="hljs-number">19319</span>, <span class="hljs-string">"255.255.255.255"</span>, <span class="hljs-function">(<span class="hljs-params">err, bytes</span>)=></span> &#123;
            <span class="hljs-keyword">if</span> (err) &#123;
                reject(err);
                <span class="hljs-keyword">return</span>
            &#125;
        &#125;)
    &#125;)
&#125;
getLocalIp().then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res);
    <span class="hljs-comment">// 192.168.0.108  这里打印的结果和ifconf得到的结果一致</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">你还知道哪些获取IP的方法欢迎留言或进群讨论</h3>
<h3 data-id="heading-9">参考文档</h3>
<p><a href="https://blog.csdn.net/m0_37263637/article/details/83831247" target="_blank" rel="nofollow noopener noreferrer">CSDN</a><br>
<a href="https://www.w3.org/TR/webrtc/#dom-rtcicecandidatetype" target="_blank" rel="nofollow noopener noreferrer">WebRTC cancidate文档</a><br>
<a href="https://stackoverflow.com/questions/3062594/differentiate-vmware-network-adapter-from-physical-network-adapters-or-detect" target="_blank" rel="nofollow noopener noreferrer">关于虚拟机MAC</a><br>
<a href="https://gist.github.com/hectorguo/672844c319547498dcb569df583f959d" target="_blank" rel="nofollow noopener noreferrer">mdns</a><br>
<a href="https://bloggeek.me/psa-mdns-and-local-ice-candidates-are-coming/" target="_blank" rel="nofollow noopener noreferrer">mdns</a></p></div>  
</div>
            