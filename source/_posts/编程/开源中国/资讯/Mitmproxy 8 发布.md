
---
title: 'Mitmproxy 8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0322/073445_XLy8_4937141.png'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 07:35:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0322/073445_XLy8_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Mitmproxy 是一个免费开源的交互式 HTTPS 代理。它可以用来拦截、检查、修改和重放网络流量，还可以对从 HTML 到 Protobuf 的各种消息类型进行预设和解码，实时拦截特定的消息，在它们到达目的地之前对其进行修改，并在之后对客户端或服务器进行重放。</p> 
<p>Mitmproxy 8 正式发布，具体更新内容如下：</p> 
<h3>Web UI 的改进</h3> 
<p><img alt height="134" src="https://static.oschina.net/uploads/space/2022/0322/073445_XLy8_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>这个版本针对 mitmweb 进行了大量改进，mitmweb 现在可以显示 TCP 和 WebSocket 流量，提供直接的 cURL/HTTPie/原始 HTTP 输出，并带有一个实验性的命令栏。在后端，整个代码库已被转换为 TypeScript。</p> 
<h3>新的 TLS Event Hooks</h3> 
<p><img alt height="108" src="https://static.oschina.net/uploads/space/2022/0322/073454_Ks3n_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>Mitmproxy 有了新的 Event Hooks，可以用来指示客户端和服务器连接的 TLS 握手成功和失败。</p> 
<h3>其他更新内容</h3> 
<ul> 
 <li>支持 SOCKS v5 模式的代理认证</li> 
 <li>在 tls_clienthello event hook 中可以忽略连接</li> 
 <li>修复某些响应在编码为大写时无法正确解码的问题</li> 
 <li>改进 TLS 版本不匹配的错误信息</li> 
 <li>Windows：切换到 Python 默认的 asyncio 事件循环，这增加了可以同时处理的套接字的数量</li> 
 <li>增加 <code>client_replay_concurrency</code> 选项</li> 
 <li>新的内容视图可以处理 gRPC/protobuf，允许使用自定义的定义来显示不同的字段解码</li> 
 <li>修复了编辑字符串选项时引起的崩溃</li> 
 <li>基础容器镜像升级到 Debian 11 Bullseye</li> 
 <li>删除旧版 pyOpenSSL 的解决方法</li> 
 <li>修复了使用 view.flow.resolve 时崩溃的问题</li> 
 <li>修复启动时 <code>running()</code> 被调用两次的问题</li> 
 <li>修复与 BoringSSL 的兼容性</li> 
 <li>添加 <code>WebSocketMessage.injected</code> 标志</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmitmproxy%2Fmitmproxy%2Freleases%2Ftag%2Fv8.0.0" target="_blank">https://github.com/mitmproxy/mitmproxy/releases/tag/v8.0.0</a></p>
                                        </div>
                                      
</div>
            