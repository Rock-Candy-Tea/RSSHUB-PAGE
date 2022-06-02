
---
title: 'Seth Schoen呼吁清理并释放数以亿计的IPv4编码地址'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0602/31c2f2b28d4f17d.png'
author: cnBeta
comments: false
date: Thu, 02 Jun 2022 07:55:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0602/31c2f2b28d4f17d.png'
---

<div>   
ITNews.au 报道称：<strong>自 1980 年以来，某些特殊范围的 IPv4 地址一直无法在互联网上得到应用，比如保留地址、无效地址、以及用于环回网络的地址。</strong>然而随着可用的 32-bit IPv4 地址逐渐枯竭、以及全球受 IPv6 转进缓慢的拖累，免费传输层安全数字证书提供商 Let's Encrypt 联合创始人 Seth Schoen 正在发起一个“IPv4 清理倡议”。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0602/31c2f2b28d4f17d.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://github.com/schoen/unicast-extensions" target="_self">GitHub</a>）</p><p>Seth Schoen 在亚太互联网运营技术大会（<a href="https://blog.apnic.net/2022/05/31/cutting-down-on-ip-address-waste/" target="_self">APRICOT</a>）上介绍 IPv4 单拨扩展项目（Unicast Extensions Project）时指出：</p><blockquote><p>尽管背后的原因尚未得到证实，但 1980 年代做出的将诸多 IPv4 地址设置为‘特殊预留网段’的决定，还是导致了大量的编码资源被白白浪费。</p><p>而 IPv4 清理项目的使命，就是将当前当前未在公共互联网上路由的地址变得普遍可用。</p></blockquote><p>具体说来是，如果能采纳 240/4、0/8、127/8、225/8-232/8 的编码范围，并将之视作普通的单播编码（ordinary unicast numbering）资源，便可增加大约 4.19 亿个 IPv4 地址。</p><p>毕竟随着互联网的飞速发展，32-bit IPv4 地址正变得愈加稀缺，甚至导致某些区域的注册管理机构无法为网络分配额外的编码块。</p><p>这种固有的稀缺性，直接导致了 IPv4 地址的囤积、抬高了分配的价格、甚至引发了一系列欺诈。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0602/a4d931943558ebd.jpeg" alt="0_0_0_0_70__News_Seth_Schoen_Mystery_Hunt.jpeg" referrerpolicy="no-referrer"></p><p>为此，Seth Schoen 希望能够通过特殊的编码方法，修复“将 0 分配为网络广播地址”的设计错误。</p><blockquote><p>据悉，作为 80 年代初为 4.2 版 Berkeley Software Distribution UNIX 操作系统而作的一个古早设计限制，他认为实在没有必要再固步自封。</p><p>毕竟 4.2 BSD 早已被埋到历史长河的谷底，过去 3 年里没有任何操作系统在使用‘0’进行广播。</p></blockquote><p>同样，IPv4 为 localhost 环回接口保留了超过 1670 万个地址（整个 /8 区块）。若能够将其缩小到只有 65526 个地址（/16 区块），亦可释放大量的编号资源。</p><p>当然，Seth Shoen 没有拒绝向新一代 IPv6 系统过渡的意思。只是受当前保留 / 不可路由的 IPv4 地址限制，全球网络通讯仍不可避免地遇到一些挑战。</p><p>假如这一倡议能够得到广泛的支持，我们大可期待从 FreeBSD / OpenBSD 和 Linux 平台开始，为其提供配套的网络堆栈软件修改，以尽可能地提升扩展 IPv4 地址在私有和公共互联网上的兼容性。</p>   
</div>
            