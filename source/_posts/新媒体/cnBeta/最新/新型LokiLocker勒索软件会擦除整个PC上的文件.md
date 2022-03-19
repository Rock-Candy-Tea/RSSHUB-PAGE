
---
title: '新型LokiLocker勒索软件会擦除整个PC上的文件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0319/326dc005ea92bde.png'
author: cnBeta
comments: false
date: Sat, 19 Mar 2022 01:53:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0319/326dc005ea92bde.png'
---

<div>   
黑莓威胁情报（BlackBerry Threat Intelligence）团队刚刚发出警报 —— 一款自 2021 年 8 月存续至今的 LokiLocker 勒索软件，正在互联网上传播肆虐。<strong>据悉，该恶意软件采用了 AES + RSA 的加密方案，若用户拒绝在指定期限内支付赎金，它就会擦除其 PC 上的所有文件</strong> —— 包括删除所有非系统文件、以及覆盖硬盘上的主引导记录（MBR）。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0319/326dc005ea92bde.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图自：<a href="https://blogs.blackberry.com/en/2022/03/lokilocker-ransomware" target="_self">BlackBerry Threat Intelligence</a>）</p><p>目前尚不清楚 LokiLocker 勒索软件的起源，但代码分析发现它是用英语编写的，这点让安全研究人员感到很是疑惑。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0319/805a58a8e210ebe.png" alt="lokilocker-fig01.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 1 - KoiVM 混淆器版本号</p><p>至于 LokiLocker 的受害者，世界各地都有分散，但主要分布在东欧和亚洲地区。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0319/c1e95ece58ba529.png" alt="lokilocker-fig02.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 2 - Koi、NETGuard 与混淆类名</p><p>不过黑莓威胁情报团队认为，用于开发 LokiLocker 的工具，是由名为 AccountCrack 的伊朗破解团队开发的。</p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2022/0319/faa08b29f7070f1.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0319/faa08b29f7070f1.png" alt="lokilocker-fig03.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">图 3 - Loki 函数为空或无法反编译</p><p>当然，仅凭这一点，还无法最终认定 LokiLocker 勒索软件的起源。</p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2022/0319/9a08f71e57977f1.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0319/9a08f71e57977f1.png" alt="lokilocker-fig04.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">图 4 - WinAPI 包装器</p><p>对于普通用户来说，还请始终对各种不明链接保持警惕、确保开启 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 安全中心、并在启用受控文件夹访问策略。</p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2022/0319/55555d51a2d7af3.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0319/55555d51a2d7af3.png" alt="lokilocker-fig05.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">图 5 - Loki 配置</p><p>最后，为了在不幸中招后有机会恢复文件，平日里也可通过 OneDrive 等网盘服务进行定期同步备份。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0319/01076a618989538.png" alt="lokilocker-fig06.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 6 - KoiVM 虚拟化功能</p>   
</div>
            