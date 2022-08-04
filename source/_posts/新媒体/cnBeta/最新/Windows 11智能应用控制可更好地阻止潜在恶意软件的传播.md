
---
title: 'Windows 11智能应用控制可更好地阻止潜在恶意软件的传播'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0804/dd5ec7b040fe2e7.webp'
author: cnBeta
comments: false
date: Thu, 04 Aug 2022 09:41:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0804/dd5ec7b040fe2e7.webp'
---

<div>   
在经历了一段时间的拉锯后，Microsoft Office 生产力套件终于在 7 月下旬默认阻止 VBA 宏的运行。<strong>然而对于用户基数庞大的 Windows 操作系统来说，它还是很容易被各类威胁参与者给盯上。</strong>Neowin 指出，新的策略、基数和程序（TTP）层出不穷，使得 ISO、LNK 和 RAR 等文件格式都极易被注入恶意软件。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0804/dd5ec7b040fe2e7.webp" alt="1.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（via <a href="https://www.bleepingcomputer.com/news/microsoft/windows-11-smart-app-control-blocks-files-used-to-push-malware/" target="_self">Bleeping Computer</a>）</p><p>好消息是，<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 的“智能应用控制”（SAC）实用程序，将在阻止潜在恶意软件的传播方面做到更好。</p><p><img src="https://static.cnbetacdn.com/article/2022/0804/8c7f54133e6c72f.png" alt="2.png" referrerpolicy="no-referrer"></p><p>微软企业与操作系统安全副总裁 David Weston 在周二的推文上宣布：“我们改进了 Windows 11 上的 SAC，现可阻止带有 web 标记（MOTW）的 ISO 镜像和 LNK 快捷方式”。</p><p><img src="https://static.cnbetacdn.com/article/2022/0804/a9180554b46c4a5.png" alt="3-0.png" referrerpolicy="no-referrer"></p><p>据悉，微软在今年四月发布了 Smart App Control，且 David Weston 将之描述为“Windows 11 安全模型的重大增强”，旨在仅放行那些安全可靠的应用程序。</p><p><a href="https://static.cnbetacdn.com/article/2022/0804/2fece85abec7bfd.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0804/2fece85abec7bfd.jpg" alt="3-3.jpg" referrerpolicy="no-referrer"></a></p><p>然而正如安全研究员 Will Dormann 所发现的那样，SAC 其实蕴含了更强大的潜力。</p><p><a href="https://static.cnbetacdn.com/article/2022/0804/4d0c9933b814dbc.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0804/4d0c9933b814dbc.jpg" alt="3-2.jpg" referrerpolicy="no-referrer"></a></p><p>除了 ISO 和 LNK，其现也能够阻止 IMG 压缩包、以及 VDH / VHDX 虚拟机磁盘等文件类型。</p><p><a href="https://static.cnbetacdn.com/article/2022/0804/a99bbd3e9e40e32.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0804/a99bbd3e9e40e32.jpg" alt="3-1.jpg" referrerpolicy="no-referrer"></a></p><p>以下是 Bleeping Computer 分享的可被 SAC 阻止的更多文件类型：（列表不断增长中）</p><blockquote><p>● .appref-ms</p><p>● .bat</p><p>● .cmd</p><p>● .chm</p><p>● .cpl</p><p>● .js</p><p>● .jse</p><p>● .msc</p><p>● .msp</p><p>● .reg</p><p>● .vbe</p><p>● .vbs</p><p>● .wsf</p></blockquote><p>需要注意的是，<a href="https://www.neowin.net/news/windows-11-smart-app-control-gets-a-whole-lot-better-at-blocking-potential-malware/" target="_self">Neowin</a> 发现最近于 MSDT“DogWalk”漏洞中被使用的 .diagcabb 文件类型，目前尚未被加入 SAC 的阻止列表。</p><p><img src="https://static.cnbetacdn.com/article/2022/0804/514428664137b20.png" alt="4.png" referrerpolicy="no-referrer"></p><p>感兴趣的 Windows 11 22H2 Insider 测试者们，现在就可以尝试 SMART App Control 。但若你想要禁用这项 SAC 功能，官方是并不建议这么的。</p><p>最后，在被问及具体的 SAC 受限扩展名时，微软公司的 Jeffery Sutherland 表示将很快公布。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1295879.htm" target="_blank">Microsoft Office今日起默认阻止VBA宏的运行</a></p></div>   
</div>
            