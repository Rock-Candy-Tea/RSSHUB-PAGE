
---
title: 'OpenSSH 8.7版本发布：支持实验性的SFTP for SCP'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0821/13a9a87d4d18729.png'
author: cnBeta
comments: false
date: Sat, 21 Aug 2021 03:34:01 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0821/13a9a87d4d18729.png'
---

<div>   
<strong>OpenSSH 刚刚迎来了 8.7 正式版，相关改进主要围绕 SCP 展开，以及为将来的变化做准备。</strong>首先，开发团队准备在下一个版本中默认禁用 ssh-rsa 签名方案，并鼓励用户立即转向更好、更安全的替代方案。其次，用户远程到远程副本的 SCP，现将默认通过本地主机传输，以避免在源跃点上暴露凭据，且包含了其它细节改进。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0821/13a9a87d4d18729.png" referrerpolicy="no-referrer"></p><p>（3）SCP 添加了对使用 SFTP 协议作为最终替代 SCP/RCP 传输协议的实验性支持，意味着用户可享受到更佳可预测的文件名处理和其它改进，且它会在“不久的将来”成为一项默认设置。</p><p>（4）SSH 和 SSHD 现将使用更加严格的配置文件解析器。</p><p>（5）许多 bug 修复和其它小改进。</p><p>感兴趣的朋友，可移步至 OpenSSH.com <a href="https://www.openssh.com/" target="_self">官网</a>，以下载并获取有关 OpenSSH 8.7 的更多细节。</p>   
</div>
            