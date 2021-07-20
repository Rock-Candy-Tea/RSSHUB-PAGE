
---
title: 'RTCPeerConnection 配置详解之 bundlePolicy'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7158'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 20:42:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=7158'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>先上结论，在使用浏览器和 Janus 互动时，RTCPeerConnection.bundlePolicy 最终视频和音频的传输都是使用一个端口，不同的取值影响的注意是 ICE 协商阶段，建议使用 <code>"max-bundle"</code> 提高 ICE 协商速度。</strong></p>
<h2 data-id="heading-0">官方定义</h2>
<p><code>RTCPeerConnection.bundlePolicy</code> 指定了当远程对等方不兼容标准 SDP BUNDLE 时如何处理候选项的协商，默认值为 <code>"balanced"</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pc = <span class="hljs-keyword">new</span> RTCPeerConnection(&#123; <span class="hljs-attr">bundlePolicy</span>: <span class="hljs-string">'max-bundle'</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果远程端点时 BUNDLE 感知的，则在协商完成时，所有媒体轨道和数据通道都被捆绑到一个单一的传输上，而不管使用的策略如何，并且最初创建的任何多余的传输都在此时关闭。</strong></p>
<p><strong>所有浏览器实现都是 BUNDLE 感知的。</strong></p>
<h2 data-id="heading-1">枚举值说明</h2>
<p><code>"balanced"</code>（默认值）：ICE 代理为每种使用的媒体类型（视频、音频和数据）收集 ICE 选项。如果远程端点不支持捆绑，在单独的传输上仅协商一个音频和视频轨道。</p>
<p><code>"max-compat"</code>：ICE 代理为每个轨道收集 ICE 选项。如果远程端点不支持捆绑，在单独的传输上协商所有的媒体轨道。</p>
<p><code>"max-bundle"</code>：ICE 代理只收集一个轨道候选项。如果远程端点不支持捆绑，仅协商一个媒体轨道。</p>
<h2 data-id="heading-2">SDP BUNDLE</h2>
<p>学些 RTP 的 rfc 文档时，2.2 节说明，如果会议中同时使用音频和视频媒体，则他们是使用单独的 RTP 会话传输 RTCP 数据包，每个媒体使用两个不同的 UDP 端口对或多播地址。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc1889%23section-2.2" target="_blank" rel="nofollow noopener noreferrer" title="https://datatracker.ietf.org/doc/html/rfc1889#section-2.2" ref="nofollow noopener noreferrer">datatracker.ietf.org/doc/html/rf…</a></p>
<p>按照这种方式，如果是 5 个人同时开会的场景，每个浏览器上需要协商的端口有 2 个发布流的端口可以 4x2 个受流端口，一共需要协商 10 端口，在和后端沟通的时候收到的反馈是视频和音频传输用的是同一个端口，继续看 RFC 文档中的 5.2 节，专门有复用 RTP 会话的说明。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdatatracker.ietf.org%2Fdoc%2Fhtml%2Frfc1889%23section-5.2" target="_blank" rel="nofollow noopener noreferrer" title="https://datatracker.ietf.org/doc/html/rfc1889#section-5.2" ref="nofollow noopener noreferrer">datatracker.ietf.org/doc/html/rf…</a></p>
<p>复用 RTP 会话的情况下，同样是 5 个开会的场景，每个浏览器需要协商的端口数量是 5 个，在 Janus 的实现中，可以通过信令通知 Janus 不要发送视频或者音频给客户端，也能实现只订阅视频或者音频的需求。</p>
<h2 data-id="heading-3">对各个取值的理解</h2>
<p>使用 <code>"max-bundle"</code> 时只协商为一个轨道收集候选项，速度最快，兼容性最差，当远端不支持 SDP 捆绑是，只能传输一个视频轨或者音频轨。</p>
<p>使用 <code>"max-compat"</code> 时为每个轨道收集候选项，速度最慢，兼容性最差，当远端不支持时也能正常传输所有媒体数据。</p>
<p>使用过程中，Janus 和浏览器都是支持 SDP 捆绑的，所以最终的传输都是使用一个端口，不同的取值影响的注意是 ICE 协商阶段，使用过程中使用 <code>"max-bundle"</code> 。</p>
<h2 data-id="heading-4">实际环境进行验证</h2>
<p>使用一台 Janus 服务器和一个电脑进行验证，查看信令数据中浏览器上报的 candidate 信息</p>
<h3 data-id="heading-5">信令及抓包文件备份位置</h3>
<blockquote>
<ul>
<li>链接: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F15ypf3al6jQFZM0nnfygMXA" target="_blank" rel="nofollow noopener noreferrer" title="https://pan.baidu.com/s/15ypf3al6jQFZM0nnfygMXA" ref="nofollow noopener noreferrer">pan.baidu.com/s/15ypf3al6…</a></li>
<li>提取码: gthc</li>
<li>复制这段内容后打开百度网盘手机App，操作更方便哦</li>
</ul>
</blockquote>
<h3 data-id="heading-6">max-bundle</h3>
<pre><code class="copyable">candidate:360945858 1 udp 2122260223 172.25.64.1 49885 typ host generation 0 ufrag LzwC network-id 1
candidate:6840418 1 udp 2122194687 192.168.0.23 49886 typ host generation 0 ufrag LzwC network-id 2
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">max-compat</h3>
<pre><code class="copyable">candidate:360945858 1 udp 2122260223 172.25.64.1 53782 typ host generation 0 ufrag HtWM network-id 1
candidate:6840418 1 udp 2122194687 192.168.0.23 53783 typ host generation 0 ufrag HtWM network-id 2
candidate:360945858 1 udp 2122260223 172.25.64.1 53784 typ host generation 0 ufrag HtWM network-id 1
candidate:6840418 1 udp 2122194687 192.168.0.23 53785 typ host generation 0 ufrag HtWM network-id 2
candidate:1526752306 1 tcp 1518280447 172.25.64.1 9 typ host tcptype active generation 0 ufrag HtWM network-id 1
candidate:1324063890 1 tcp 1518214911 192.168.0.23 9 typ host tcptype active generation 0 ufrag HtWM network-id 2
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">抓包分析</h3>
<p>根据浏览器上报的 candidate 信息可以知道使用 max-bundle 时，每个 IP 只协商了一个端口，使用 max-compat 时每个 IP 上协商了多个端口（第一次 3 个，第二次 2 个）。</p>
<p>使用 max-compat 进行互动并使用 Wireshark 进行抓包分析，浏览器上报的 candidate 信息中 192.168.0.23 一共协商了 53707 和 53709 两个端口，互动是只有 53707 在被使用，没有抓到 53709 端口的数据包。</p>
<h2 data-id="heading-9">结论</h2>
<p>在使用浏览器和 Janus 互动时，RTCPeerConnection.bundlePolicy 最终视频和音频的传输都是使用一个端口，不同的取值影响的注意是 ICE 协商阶段，建议使用 <code>"max-bundle"</code> 提高 ICE 协商速度。</p>
<h2 data-id="heading-10">参考文档</h2>
<ul>
<li>RTCBundlePolicy 枚举值：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fw3c.github.io%2Fwebrtc-pc%2F%23dom-rtcbundlepolicy" target="_blank" rel="nofollow noopener noreferrer" title="https://w3c.github.io/webrtc-pc/#dom-rtcbundlepolicy" ref="nofollow noopener noreferrer">w3c.github.io/webrtc-pc/#…</a></li>
<li>MDN RTCBundlePolicy 枚举值：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FRTCConfiguration%23rtcbundlepolicy_enum" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/RTCConfiguration#rtcbundlepolicy_enum" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li>SDP 捆绑：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebrtcstandards.info%2Fsdp-bundle%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webrtcstandards.info/sdp-bundle/" ref="nofollow noopener noreferrer">webrtcstandards.info/sdp-bundle/</a></li>
</ul></div>  
</div>
            