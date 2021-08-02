
---
title: '内网 coturn（TURN Server）联通性测试与验证 ｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5c7a25d7e874fc78ea8a779d648f9d0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:53:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5c7a25d7e874fc78ea8a779d648f9d0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>使用 Trickle ICE 验证 TURN Server 是否可以正常工作时，Trickle ICE 和 coturn 的 log 都有错误打印，对于配置是否正确不敢确认，搭建了完整的测试环境验证后通过抓包才最终放心，解除了心中的疑虑。</p>
<h2 data-id="heading-0">安装与配置</h2>
<p>网上介绍 TURN Server 安装与配置的文章挺多的，我是在 CentOS 上使用，参考的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fhaeasringnar%2Farticle%2Fdetails%2F94607464" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/haeasringnar/article/details/94607464" ref="nofollow noopener noreferrer">Centos7 安装coturn部署一套 STUN/TURN 服务 webRTC打洞服务器</a>。</p>
<p>按照文章的步骤一步一步操作基本上就 OK 了，碰到一个问题需要注意一下，4.5.2 版本在使用 CentOS 7 系统下无法正常工作，回退版本可以了，当时以为配置文件的问题查了很久，最后看到下面两个 Issue 才知道。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcoturn%2Fcoturn%2Fissues%2F697" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/coturn/coturn/issues/697" ref="nofollow noopener noreferrer">github.com/coturn/cotu…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcoturn%2Fcoturn%2Fissues%2F686" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/coturn/coturn/issues/686" ref="nofollow noopener noreferrer">github.com/coturn/cotu…</a></li>
</ul>
<h2 data-id="heading-1">使用 Trickle ICE 测试</h2>
<p>参考网上的文章使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebrtc.github.io%2Fsamples%2Fsrc%2Fcontent%2Fpeerconnection%2Ftrickle-ice%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/" ref="nofollow noopener noreferrer">Trickle ICE</a> 测试 TURN Server ，说是看到下面的 Done 就可以了。</p>
<p>但是看到下面的错误提示，对于是否可以正常工作还是很大疑虑。</p>
<blockquote>
<p>The server turn:192.168.0.221:3478?transport=udp returned an error with code=701: TURN allocate request timed out.</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5c7a25d7e874fc78ea8a779d648f9d0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过查看 Trickle ICE 的源码发现指定 iceTransportPolicy 可以让 ICE 直接使用 TURN Server 进行转发而不是使用默认的优先级，这样可以进行抓包观察验证 TURN Server 是否正常的进行转发了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd18a248618442582b5e9709b8666a9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>从图中可以看到，ICE 获取到了三个 UDP 的主机候选项和三个 TCP 的主机候选项，以及一个中继候选项，因为是在同一个局域网中，获取不到反射候选项。</p>
</blockquote>









































































































<table><thead><tr><th>Time</th><th>Component</th><th>Type</th><th>Foundation</th><th>Protocol</th><th>Address</th><th>Port</th><th>Priority</th></tr></thead><tbody><tr><td>0.020</td><td>rtp</td><td>host</td><td>3598251130</td><td>udp</td><td>172.31.112.1</td><td>50126</td><td>126 | 32542 | 255</td></tr><tr><td>0.021</td><td>rtp</td><td>host</td><td>6840418</td><td>udp</td><td>192.168.0.23</td><td>50127</td><td>126  | 32286  | 255</td></tr><tr><td>0.021</td><td>rtp</td><td>host</td><td>1553261686</td><td>udp</td><td>192.168.30.23</td><td>50128</td><td>126  | 32030  | 255</td></tr><tr><td>0.072</td><td>rtp</td><td>relay</td><td>4222569549</td><td>udp</td><td>192.168.0.221</td><td>20412</td><td>2  | 32286  | 255</td></tr><tr><td>0.122</td><td>rtp</td><td>host</td><td>2566588554</td><td>tcp</td><td>172.31.112.1</td><td>9</td><td>90  | 32542  | 255</td></tr><tr><td>0.122</td><td>rtp</td><td>host</td><td>1324063890</td><td>tcp</td><td>192.168.0.23</td><td>9</td><td>90  | 32286  | 255</td></tr><tr><td>0.122</td><td>rtp</td><td>host</td><td>303503494</td><td>tcp</td><td>192.168.30.23</td><td>9</td><td>90  | 32030  | 255</td></tr><tr><td>39.867</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Done</td></tr><tr><td>39.871</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>
<blockquote>
<p>Type 中的 host 是主机候选，relay 是中继候选项</p>
</blockquote>
<h2 data-id="heading-2">搭建环境验证</h2>
<h3 data-id="heading-3">1. 网络环境</h3>
<ul>
<li>网段一：192.168.0.xxx</li>
<li>网段二：192.168.100.xxx</li>
</ul>
<p>网段一是主网络，模拟公网环境，TURN Server 和 Janus 的服务器在此网络中，两个服务都在一台设备上，IP 地址是 192.168.0.221.</p>
<p>网段二是自网络，模拟局域网，互动的电脑在此网络中，子网段路由器的 WAN IP 是 192.168.0.251。</p>
<h3 data-id="heading-4">2. 使用 Trickle ICE 测试 STUN 和 TURN</h3>
<p>对比之前，多了服务器反射候选项，说明 STUN 正常工作</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41bb3c799f7e40e6a7190e1e49c19293~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3. 使用 Janus 测试抓包</h3>
<p>修改 RTCPeerConnection 初始化配置，将 iceTransportPolicy 设置为 relay，然后开始互动并使用 WireShark 进行抓包。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> pc = <span class="hljs-keyword">new</span> RTCPeerConnection(&#123;
      <span class="hljs-attr">iceServers</span>: [
        &#123;
          <span class="hljs-attr">urls</span>: [<span class="hljs-string">'turn:192.168.0.221:3478'</span>],
          <span class="hljs-attr">username</span>: <span class="hljs-string">'test'</span>,
          <span class="hljs-attr">credential</span>: <span class="hljs-string">'123456'</span>,
          <span class="hljs-attr">credentialType</span>: <span class="hljs-string">'password'</span>,
        &#125;,
      ],
      <span class="hljs-attr">iceTransportPolicy</span>: <span class="hljs-string">'relay'</span>,
      <span class="hljs-attr">bundlePolicy</span>: <span class="hljs-string">'max-bundle'</span>,
      <span class="hljs-attr">rtcpMuxPolicy</span>: <span class="hljs-string">'require'</span>,
      <span class="hljs-comment">// certificates: '',</span>
      <span class="hljs-attr">iceCandidatePoolSize</span>: <span class="hljs-string">'0'</span>,
      <span class="hljs-attr">sdpSemantics</span>: <span class="hljs-string">'unified-plan'</span>,
      <span class="hljs-attr">tcpCandidatePolicy</span>: <span class="hljs-string">'disable'</span>,
      <span class="hljs-attr">IceTransportsType</span>: <span class="hljs-string">'nohost'</span>,
    &#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>开始互动后 publish 流成功了，观察 Janus 消息，浏览器上报的 candidate 里面只有 relay 地址，基本可以确定 TURN Server 可以正常工作。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac028fc23b544280af09fa6e256b1278~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过 wireshark 的过滤可以看到，所有发送给 192.168.0.221 的 udp 包目标端口都是 3478，可以确定流是通过 TURN Server 转发到 Janus 的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d52aa627fad42d18eb3b48f8e1bceed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37a2e4bf4d7848339648fc455e2094c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">配置文件参考</h2>
<p>测试时候的配置，有需要可以参考下</p>
<pre><code class="copyable"># TURN server name and realm
realm=192.168.0.221
server-name=turnserver

# Use fingerprint in TURN message
fingerprint

# IPs the TURN server listens to
# listening-ip=192.168.0.221

# External IP-Address of the TURN server
#external-ip=121.199.22.135

# Main listening port
listening-port=3478

# Further ports that are open for communication
min-port=20000
max-port=22000

# Enable verbose logging
verbose

# Specify the user for the TURN authentification
user=test:123456

# Enable long-term credential mechanism
lt-cred-mech
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">参考资料：</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fhaeasringnar%2Farticle%2Fdetails%2F94607464" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/haeasringnar/article/details/94607464" ref="nofollow noopener noreferrer">blog.csdn.net/haeasringna…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjoey.blue%2F2018%2F12%2F10%2Fwebrtc-coturn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://joey.blue/2018/12/10/webrtc-coturn/" ref="nofollow noopener noreferrer">joey.blue/2018/12/10/…</a></li>
</ul></div>  
</div>
            