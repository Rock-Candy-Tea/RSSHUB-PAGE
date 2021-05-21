
---
title: 'Netty 4.1.65.Final 发布，异步事件驱动的网络应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=196'
author: 开源中国
comments: false
date: Fri, 21 May 2021 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=196'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Netty 4.1.65.Final 已经发布。Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。本次更新除了修复各种错误之外，还包含了一个安全修复（CVE-2021-21295）的后续工作，可能会影响使用 codec-http2 包和代理 HTTP/2 到 HTTP/1.1 的用户。</p> 
<p>该版本中的主要变化包括：</p> 
<ul> 
 <li>在最后一个解码的数据块之后触发 SslHandshakeCompletionEvent (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11148" target="_blank">#11148</a>)</li> 
 <li>在初始化代码中记录更少的堆栈追踪 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11164" target="_blank">#11164</a>)</li> 
 <li>修复 StreamBufferingEncoder GOAWAY 中的错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11144" target="_blank">#11144</a>)</li> 
 <li>确保 DnsNameResolver 能解决 Windows 上的主机（计算机）名称 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11167" target="_blank">#11167</a>)</li> 
 <li>修复在使用本地 epoll 传输时对 IP_RECVORIGDSTADDR 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11173" target="_blank">#11173</a>)</li> 
 <li>支持 BouncyCastle (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11157" target="_blank">#11157</a>)</li> 
 <li>SimpleChannelPromiseAggregator 使用第一个异常而不是最后一个 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11168" target="_blank">#11168</a>)</li> 
 <li>增加一个新的 HTTP/2 伪 header :protocol (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11192" target="_blank">#11192</a>)</li> 
 <li>使用 BouncyCastle ALPN 支持时启用 TLSv1.3 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11193" target="_blank">#11193</a>)</li> 
 <li>在解码时正确地抛出 ErrorDataDecoderException 的错误 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11198" target="_blank">#11198</a>)</li> 
 <li>如果构造方法抛出，则销毁 HttpPostMultipartRequestDecoder (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11207" target="_blank">#11207</a>)</li> 
 <li>ReferenceCountedOpenSslEngine 解包握手完成状态修复 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11210" target="_blank">#11210</a>)</li> 
 <li>修复多部分解码器中内存释放不正确的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11188" target="_blank">#11188</a>)</li> 
 <li>在调用本地 OnLoad 函数前预加载类，以防止类加载器死锁 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11215" target="_blank">#11215</a>)</li> 
 <li>在 A/AAAA 查询中仅回退到 CNAME (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11216" target="_blank">#11216</a>)</li> 
 <li>根据 searchOrder 重新排列解析器的列表 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11236" target="_blank">#11236</a>)</li> 
 <li>默认禁用 TLSv1 和 TLSv1.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11237" target="_blank">#11237</a>)</li> 
 <li>当使用基于 openssl 的 SSL 提供程序时，默认使用任务 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11242" target="_blank">#11242</a>)</li> 
 <li>增加 DefaultHostsFileEntriesResolver#addresses，以提供一个主机名的所有 hosts 文件的条目 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11246" target="_blank">#11246</a>)</li> 
 <li>引入 BrotliDecoder (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F10960" target="_blank">#10960</a>)</li> 
 <li>修复 macOS 上用于 DNS 解析的本地库的加载 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11260" target="_blank">#11260</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2021%2F05%2F19%2F4-1-65-Final.html" target="_blank">https://netty.io/news/2021/05/19/4-1-65-Final.html</a></p>
                                        </div>
                                      
</div>
            