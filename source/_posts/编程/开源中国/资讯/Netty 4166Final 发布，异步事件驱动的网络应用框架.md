
---
title: 'Netty 4.1.66.Final 发布，异步事件驱动的网络应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7477'
author: 开源中国
comments: false
date: Sat, 17 Jul 2021 23:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7477'
---

<div>   
<div class="content">
                                                                                            <p>Netty 4.1.66.Final 已经发布。Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。本次更新除了修复各种错误之外，还包含了一个安全修复（CVE-2021-21295）的后续工作，可能会影响使用 codec-http2 包和代理 HTTP/2 到 HTTP/1.1 的用户。</p> 
<p><strong>主要变化包括：</strong></p> 
<ul> 
 <li>引入 BrotliEncoder (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11256" target="_blank">#11256</a>)</li> 
 <li>修复带有 IPv6 默认路由的 IpSubnetFilterRule 不接受所有的 IPv6 地址 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11351" target="_blank">#11351</a>)</li> 
 <li>修复启用编码但未使用的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11358" target="_blank">#11358</a>)</li> 
 <li>MqttDecoder 在抛出 TooLongFrameException 前错误地跳过字节 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11362" target="_blank">#11362</a>)</li> 
 <li>使用双向算法来优化 ByteBufUtil.indexOf() 方法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11367" target="_blank">#11367</a>)</li> 
 <li>HttpUtil.getCharset() 对双引号的字符集失效 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11371" target="_blank">#11371</a>)</li> 
 <li>让所有的压缩编解码器支持没有数组的缓冲区 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11387" target="_blank">#11387</a>)</li> 
 <li>如果用户试图显式设置 TLSv1.3 密码并使用 BoringSSL，日志将会记录下来 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11392" target="_blank">#11392</a>)</li> 
 <li>接受比请求更小的 server_max_window_bits (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11394" target="_blank">#11394</a>)</li> 
 <li>更新 graal annotations 的依赖性 GAV，以允许许可证 GPL2+CE (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11404" target="_blank">#11404</a>)</li> 
 <li>添加 ALPN 缓冲以支持 HTTP/2 Prior Knowledge (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11407" target="_blank">#11407</a>)</li> 
 <li>HttpUtil#normalizeAndGetContentLength() 应该处理空值 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11409" target="_blank">#11409</a>)</li> 
 <li>支持 GMSSL (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11410" target="_blank">#11410</a>)</li> 
 <li>当握手失败并产生警报时，正确地使用 HandshakeStatus.NEED_WRAP (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11412" target="_blank">#11412</a>)</li> 
 <li>CombinedChannelDuplexHandler.removeOutboundHandler() 导致 connect(...) 不能传递正确的参数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11414" target="_blank">#11414</a>)</li> 
 <li>将 io.netty.handler.codec.compression.BrotliDecoder 的初始化推迟到运行时 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11428" target="_blank">#11428</a>)</li> 
 <li>修复 Lz4FrameEncoder 关闭时的缓冲区溢出 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11429" target="_blank">#11429</a>)</li> 
 <li>修复 HttpHeaderValue#XML_HTTP_REQUEST 案例 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11433" target="_blank">#11433</a>)</li> 
 <li>添加 zstd 编码器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11437" target="_blank">#11437</a>)</li> 
 <li>添加 SslProtocols 和 Cipher suites 常量 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11457" target="_blank">#11457</a>)</li> 
 <li>引入 OpenSslAsyncPrivateKeyMethod，允许异步签署/解密私钥 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11460" target="_blank">#11460</a>)</li> 
 <li>每个委派只运行一个 SSL 任务 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11462" target="_blank">#11462</a>)</li> 
 <li>增加 application/zstd content-type 和 zstd content-encoding (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11463" target="_blank">#11463</a>)</li> 
 <li>增加 zstd http 内容压缩支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11470" target="_blank">#11470</a>)</li> 
 <li>修复 SslHandler 客户端不能及时处理 Server Hello 消息的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11472" target="_blank">#11472</a>)</li> 
 <li>SelfSignedCertificate 应首先尝试 BouncyCastle (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11487" target="_blank">#11487</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2021%2F07%2F16%2F4-1-66-Final.html" target="_blank">https://netty.io/news/2021/07/16/4-1-66-Final.html</a></p>
                                        </div>
                                      
</div>
            