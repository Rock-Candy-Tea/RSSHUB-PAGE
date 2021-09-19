
---
title: '甲骨文为VirtualBox开发新驱动 以符合升级Windows 11的TPM 2.0要求'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0919/5e15013419c584e.jpg'
author: cnBeta
comments: false
date: Sun, 19 Sep 2021 00:57:17 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0919/5e15013419c584e.jpg'
---

<div>   
在最新发布的 Windows 11 Build 22000.194 预览版中，微软为虚拟机（VM）也增加了可信平台模块（TPM）2.0 的要求。这就意味着如果用户无法满足这个要求，那么通过虚拟化运行的 Windows 11 版本将不会收到后续的版本更新。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0919/5e15013419c584e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0919/5e15013419c584e.jpg" alt="w7u2djwp.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><strong>可能是为了这个，甲骨文（Oracle）正在为 VirtualBox 开发一个新的驱动实现。</strong>在该驱动的帮助下，新驱动应该能够执行直通（passthrough），并使用主机的 TPM 模块来克服这个新的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 标准。</p><p style="text-align: left;">8 月 27 日添加的编号为 90946 的 VirtualBox 变更集列出了这一新变化。可能甲骨文公司内部知道即将到来的 Windows 11 TPM 对虚拟机的必要性，大约几周后，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>面向 Beta 频道发布了 Windows 11 Build 22000.194 预览版更新。</p>   
</div>
            