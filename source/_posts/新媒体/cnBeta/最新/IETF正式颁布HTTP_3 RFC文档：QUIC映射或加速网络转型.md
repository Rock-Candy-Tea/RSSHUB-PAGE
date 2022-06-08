
---
title: 'IETF正式颁布HTTP_3 RFC文档：QUIC映射或加速网络转型'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0608/324c23059a7a787.jpg'
author: cnBeta
comments: false
date: Wed, 08 Jun 2022 09:05:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0608/324c23059a7a787.jpg'
---

<div>   
本周一，互联网工程任务组（IETF）颁布了 HTTP/3 的 RFC 文档。<strong>作为超文本传输协议的第三个大版本，其主要描述了如何在 QUIC 上映射 HTTP 语义。</strong>通过从 TCP 向 UDP 连接转型，QUIC 传输协议还具有 HTTP 传输所需的多项特性，例如流式多路复用、分路流控、以及更低的连接建立延迟。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0608/324c23059a7a787.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">视频截图（via <a href="https://www.youtube.com/watch?v=R83fvpFi9us" target="_self">Weecli</a> / YouTube）</p><p>与此同时，该文档确定了 QUIC 包含的 HTTP/2 功能，并描述了如何将 HTTP/2 扩展迁移至 HTTP/3 。</p><blockquote><p>QUIC 全称为‘快速 UDP 互联网连接’，由 Google 创建并于 2013 年发布。</p><p>其诞生旨在化解传输控制协议（TCP）需要多次来回握手，才能建立连接并开始传输数据的短板。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0608/5de67b288b59f98.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图自：<a href="https://blog.cloudflare.com/http3-the-past-present-and-future/" target="_self">Cloudflare</a>）</p><p>由于 TCP 三次握手会造成较长的往返延时，用户体验也可能受到极大的影响。正因如此，Google 才决定基于数据报协议（UDP）来打造 QUIC 。</p><blockquote><p>即使 UDP 连接有‘丢包’的问题，但它至少可以减少客户端 / 服务器之间的往返次数，从而极大地改善传输速度。</p><p>对于正在大力向移动领域转型的 Google 来说，UDP 更是可以化解共享基站与移动终端之间访问速度缓慢且稀疏的困扰。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0608/db570433064fdc2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0608/db570433064fdc2.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>事实上，早在 IETF 颁布 HTTP/3 的意见征求稿前，这家科技巨头就已经将 QUIC 支持内嵌于 Google Chrome 浏览器、并在自家的诸多服务上启用。</p><p>2018 年的时候，Cloudflare 也将 QUIC 作为一个可选的实施项。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>对此也相当青睐，甚至打造了自己的开源版本，此外 NGINX 也添加了 HTTP/3 支持。</p><p><img src="https://static.cnbetacdn.com/article/2022/0608/0d97eb1f86b964f.png" alt="4.png" referrerpolicy="no-referrer"></p><p>需要指出的是，尽管 QUIC 的普及率有所提高，但目前全球绝大部分数据流量，仍依赖基于 TCP 的 HTTP/2 传输。</p><p>所以早在 2016 年，就有网络专家开始建议通过 QUIC 映射的方式，让 HTTP/2 也能享受到 HTTP/3 的一些优势与和谐共存。</p><p><a href="https://static.cnbetacdn.com/article/2022/0608/78ff335c23c4cc7.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0608/78ff335c23c4cc7.png" alt="5.png" referrerpolicy="no-referrer"></a></p><p>本周一（6 月 6 日），他们的努力终于得到了回报。随着 IETF 颁布 <a href="https://www.rfc-editor.org/info/rfc9114" target="_self">RFC 9114</a> 这个建议标准（完整文档字数超 20000），我们终于可以详细地了解 HTTP/3 。</p><p>虽然仍有一些批评者和竞争对手（比如主推 HTTPD 的 Apache），但 Cloudflare 表示目前来自 Google Chrome 浏览器的 HTTP/3 流量已占八成。</p><p><img src="https://static.cnbetacdn.com/article/2022/0608/9d1ffbb558f2533.webp" alt="6.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">Web 流量观测表明 HTTP/3 已成为超文本传输协议的次流行版本</p><p>最后，除了来自隐私倡导者的顾虑，一些网络专家也发现 QUIC 承诺的速度提升有些难以捉摸。</p><p>所以 HTTP/3 并不一定是能够解决所有网络问题的万金油，且 Apache 也推迟了将之引入 Web 服务器的计划。</p>   
</div>
            