
---
title: 'PwnKit漏洞曝光：所有主流Linux发行版本均受影响'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0126/da90fb5adc92189.webp'
author: cnBeta
comments: false
date: Wed, 26 Jan 2022 07:08:33 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0126/da90fb5adc92189.webp'
---

<div>   
<strong>Qualys 的 Linux 安全研究人员近日发现了存在 12 年以上的“PwnKit”漏洞，所有主要 Linux 发行版本都容易受到攻击。</strong>黑客利用该漏洞可以提升本地权限（LPE），目前这个漏洞已经被分配为“CVE-2021-4034”。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0126/da90fb5adc92189.webp" alt="z9llmfya.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">研究人员团队表示，利用该漏洞，他们能够在 Ubuntu、Debian、Fedora 和 CentOS 等一些 Linux 发行版的默认安装下获得完全的 root 权限，同时团队也认为其他 Linux 发行版应该也会受到影响。这是因为所发现的缺陷是存在于 Polkit 的 pkexec 程序中的内存损坏漏洞，这是一个安装在所有主要 Linux 发行版上的 SUID-root 程序。</p><p style="text-align: left;"><iframe src="//player.bilibili.com/player.html?bvid=BV1DY411b7WJ&page=1" width="750" height="480" frameborder="0"></iframe></p><p style="text-align: left;">该漏洞从一开始就存在于 pkexec 中，Qualys 认为在过去 12 年时间里，各大 Linux 发行版本都是黑客的靶子。虽然该漏洞不能被远程利用，但黑客如果以非特权用户的身份获得访问权，就能利用它获得 root 权限。</p>   
</div>
            