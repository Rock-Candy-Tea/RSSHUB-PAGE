
---
title: 'Zscaler：伪装成电报应用程序的FFDroider恶意软件会窃取社交媒体账号'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0413/0f8c2e8b12421d0.png'
author: cnBeta
comments: false
date: Wed, 13 Apr 2022 05:28:04 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0413/0f8c2e8b12421d0.png'
---

<div>   
<strong>由安全专家、研究人员和网络工程师们组成的 Zscaler ThreatLabz 团队，刚刚曝光了一款名为 Win32.PWS.FFDroider 的新型恶意软件。</strong>据悉，这款基于 Windows 平台的恶意软件，能够创建一个名为 FFDroider 的注册表项，并将窃取到的凭据和 cookie 发送到被攻击者把持的命令与控制（C&C）服务器。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0413/0f8c2e8b12421d0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0413/0f8c2e8b12421d0.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：<a href="https://www.zscaler.com/blogs/security-research/ffdroider-stealer-targeting-social-media-platform-users" target="_self">Zscaler ThreatLabz</a>）</p><p>研究团队发现，FFDroider 恶意软件会将自己伪装成热门消息应用“电报”（Telegram）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0413/1608badbd63ad7e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0413/1608badbd63ad7e.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">命名与控制服务器记录（初始请求包括了受感染主机的文件名和 IP 地址）</p><p>在受害者访问设备时，FFDroider 会开始通过各大浏览器（包括 Google Chrome、Mozilla Firefox、Internet Explorer 和 Microsoft Edge）窃取 cookie 和凭据。</p><p><img src="https://static.cnbetacdn.com/article/2022/0413/99fae7024ec5729.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">显示被盗 Instagram 账户信息的加密请求</p><p>FFDroider 不仅会利用盗取来的 cookie 登录受害者使用的社交媒体平台以提取更多个人敏感信息，还会通过展示虚假广告来诱骗受害者输入他们的敏感信息，结果导致进一步的攻击。</p><p><a href="https://static.cnbetacdn.com/article/2022/0413/4963a5921dacfe7.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0413/4963a5921dacfe7.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">包含来自受感染的 Facebook Cookie 的被盗信息的解密请求</p><p>深入分析发现，FFDroider 广泛针对 Facebook / Instagram / Twitter 等社交平台、以及亚马逊 / eBay / Etsy 等电商网站的用户发起了攻击。</p><p><a href="https://static.cnbetacdn.com/article/2022/0413/1e81627e48ab6b4.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0413/1e81627e48ab6b4.png" alt="5.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">从 Instagram 窃取的敏感数据的解密请求</p><p>为避免造成更大的损失，Zscaler 团队呼吁大家不要通过来路不明的渠道下载 Telegram 应用程序、并设置必要的安全防护措施 —— 包括保持计算机软件更新至最新状态、以及对社交媒体账户设置双因素身份验证。</p>   
</div>
            