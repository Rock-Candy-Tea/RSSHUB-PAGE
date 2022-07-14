
---
title: '_技巧_如何在Windows 11新预览版中启用DoT'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0714/99785181b250807.webp'
author: cnBeta
comments: false
date: Thu, 14 Jul 2022 09:02:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0714/99785181b250807.webp'
---

<div>   
今天发布的 Windows 11 Build 25158 预览版更新中，微软引入了 DNS over TLS (DoT)，这项网络增强技术已经邀请 Insider 成员进行测试。DoT 是 DNS over HTTPS (DoH)的替代者，同样用于加密网络流量。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0714/99785181b250807.webp" alt="by7wc3o7.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">DoH 目前已经在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 和 Windows Server 2022 中上线，通过 443 端口将 DNS 流量作为 HTTPS 流重新路由。不过，DoT 路由在专有的 853 端口上通过 TLS 隧道路由经过加密的 DNS 流量。虽然 DoT 在某些情况下提供更好的网络性能，但缺乏 DoH 的某些灵活性。</p><p style="text-align: left;">如果你对 DoT 感兴趣，你可以根据<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>官方的指导手册来启用 DoT。目前 DoT 已经仅在 Windows 11 和 Windows Server Build 25158 中上线：</p><blockquote><p style="text-align: left;">1. 访问“设置”→“网络”页面（可以查看默认的网络连接）</p><p style="text-align: left;">2. 点击 Wi-Fi 或者以太网</p><p style="text-align: left;">3. 点击“硬件属性”</p><p style="text-align: left;">4. 在“DNS server assignment:”中点击“编辑”按钮</p><p style="text-align: left;">5. 打开“IPv4”和/或“IPv6”开关</p><p style="text-align: left;">6. 在“Preferred DNS”文本框上输入 DoT 服务器的 IP 地址</p><p style="text-align: left;">7. 保存并确认</p></blockquote><p style="text-align: left;">然后，以管理员权限打开命令窗口中输入</p><blockquote><p style="text-align: left;">netsh dns add global dot=yes</p><p style="text-align: left;">netsh dns add encryption server=[the-ip-address-configured-as-the-DNS-resolver] dothost=: autoupgrade=yes</p><p style="text-align: left;">ipconfig /flushdns</p></blockquote><p style="text-align: left;">现阶段，853 端口是处理 DoT 的唯一端口，用户无法自行配置其他的端口。</p>   
</div>
            