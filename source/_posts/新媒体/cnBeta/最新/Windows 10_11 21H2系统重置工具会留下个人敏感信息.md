
---
title: 'Windows 10_11 21H2系统重置工具会留下个人敏感信息'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0224/b64028b1418ef8a.png'
author: cnBeta
comments: false
date: Thu, 24 Feb 2022 03:03:26 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0224/b64028b1418ef8a.png'
---

<div>   
微软最有价值专家（MVP）Rudy Ooms 近日指出 —— <strong>在 Windows 10 21H2 或 Windows 11 21H2 上执行远程 / 本地数据擦除，会导致在 Windows.old 文件夹中留下敏感的用户个人数据。</strong>然而微软的官方表述却是 —— 执行擦除功能，会从设备中删除所有个人 / 企业数据和设置。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0224/b64028b1418ef8a.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0224/b64028b1418ef8a.png" alt="0.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">网页翻译（via <a href="https://call4cloud.nl/2022/02/the-dark-and-the-windows-11-remote-wipe/" target="_self">Call4Cloud.nl</a>）</p><p>经过进一步测试，Ooms 发现该操作可在 21H1 版本上正常执行。但不知为何，21H2 版本竟然又引入了这个奇怪的 Bug 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/0740ca2f5432f48.png" alt="5.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">系统重置的数据遗留问题，实测与登录了 OneDrive 账号有关。</p><p>更糟糕的是，由于 BitLocker 保护已被移除，想要读取遗留文件和访问潜在敏感数据的话，也并不需要太多的工作。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/0ea87ead4f30507.png" alt="1.png" referrerpolicy="no-referrer"></p><p>在微软推出正式修复补丁之前，Ooms 已经提供了一个临时化解该问题的 PowerShell 脚本。感兴趣的朋友，可移步至他的个人博客网站去翻看更多细节。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/12d91077f2fad98.png" alt="2.png" referrerpolicy="no-referrer"></p><p>不过更好的办法，还是尽量选用纯净安装（抹盘）去替代系统重置（到初始化状态）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0224/dadf63b77b1bdd7.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">微软<a href="https://docs.microsoft.com/en-us/mem/intune/remote-actions/devices-wipe" target="_self">官网解释</a> / <a href="https://docs.microsoft.com/en-us/answers/questions/40514/intune-full-device-wipe-passes.html" target="_self">问答</a></p><p>最后，在出手二手硬盘的时候，也请尽量使用更加安全的软硬结合数据抹除方法，或者干脆用物理手段（比如打孔后注入铝热剂）送老旧硬盘上天。</p>   
</div>
            