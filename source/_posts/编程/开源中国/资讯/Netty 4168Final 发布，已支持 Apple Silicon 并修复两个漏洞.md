
---
title: 'Netty 4.1.68.Final 发布，已支持 Apple Silicon 并修复两个漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2372'
author: 开源中国
comments: false
date: Fri, 10 Sep 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2372'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Netty 4.1.68.Final 已经发布。Netty 是一个异步事件驱动的网络应用框架，主要用于可维护的高性能协议服务器和客户端的快速开发。</p> 
 <p>这个版本包括两个与 Bzip2 和 Snappy 的压缩/解压有关的安全修复，所以建议尽快更新到这个版本。除此之外，还增加了对 M1 Mac 的支持。</p> 
 <p>重要的变化包括：</p> 
 <ul> 
  <li>Bzip2Decoder 不允许为解压缩数据设置大小限制 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fsecurity%2Fadvisories%2FGHSA-grg4-wf29-r9vv" target="_blank">#CVE-2021-37136</a>)</li> 
  <li>SnappyFrameDecoder 不限制块长度，可能以不必要的方式缓冲可跳过的块 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fsecurity%2Fadvisories%2FGHSA-9vjp-v76f-g363" target="_blank">#CVE-2021-37137</a>)</li> 
  <li>使用本机 SSL 实现时遵循 jdk.tls.namedGroups ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11660" target="_blank">#11660</a>)</li> 
  <li>添加对 m1 Mac 的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11666" target="_blank">#11666</a>)</li> 
  <li>确保 HttpData#addContent/setContent 在抛出 IOException 之前释放缓冲区 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11621" target="_blank">#11621</a>)</li> 
  <li>[HTTP2] 修复写入带有 padding 的空数据 frame 时的内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11633" target="_blank">#11633</a>)</li> 
  <li>在允许的算法列表中添加了 “RSASSA-PSS” 算法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11626" target="_blank">#11626</a>）</li> 
  <li>将 netty-tcnative* 的版本添加到 bom ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11609" target="_blank">#11609</a>)</li> 
  <li>SimpleChannelPool::notifyConnect 应该在发生异常时 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11566" target="_blank">tryFailure</a>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11566" target="_blank">#11566</a> )</li> 
  <li>使用基于 OpenSSL/BoringSSL 的 SSLEngine 时允许服务器启动重新协商 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11601" target="_blank">#11601</a>)</li> 
  <li>只有当 JDK 也支持 TLSv1.3 时才支持它 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11604" target="_blank">#11604</a>)</li> 
  <li>修复对 HttpContentCompressor 中可选编码器错误的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11582" target="_blank">#11582</a>)</li> 
  <li>修复启用 TCP FastOpen 时 MacOS 上 IP 协议版本混乱的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11588" target="_blank">#11588</a>)</li> 
  <li>修复 DatagramDnsQueryDecoder 中多次消耗缓冲区导致的 IndexOutOfBoundsException ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11592" target="_blank">#11592</a>)</li> 
  <li>加入 multicast 组时使用 StandardSocketOptions#IP_MULTICAST_IF 作为默认源 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11585" target="_blank">#11585</a>)</li> 
  <li>确保我们仅在密码不是默认密码时才在 BoringSSL 上记录消息 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetty%2Fnetty%2Fpull%2F11583" target="_blank">#11583</a>)</li> 
 </ul> 
 <p>更多详情可查：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnetty.io%2Fnews%2F2021%2F09%2F09%2F4-1-68-Final.html" target="_blank">https://netty.io/news/2021/09/09/4-1-68-Final.html</a></p> 
</div>
                                        </div>
                                      
</div>
            