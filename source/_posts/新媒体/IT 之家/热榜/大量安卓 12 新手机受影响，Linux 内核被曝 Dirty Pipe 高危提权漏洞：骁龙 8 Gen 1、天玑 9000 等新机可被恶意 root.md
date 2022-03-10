
---
title: '大量安卓 12 新手机受影响，Linux 内核被曝 Dirty Pipe 高危提权漏洞：骁龙 8 Gen 1、天玑 9000 等新机可被恶意 root'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/3/295b62f2-af37-4293-b3bf-1a6e97ce3a2f.png'
author: IT 之家
comments: false
date: Wed, 09 Mar 2022 14:58:37 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/3/295b62f2-af37-4293-b3bf-1a6e97ce3a2f.png'
---

<div>   
<p data-vmark="9b61"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 3 月 9 日消息，Linux 内核由于开源性质，可以让许多人修改并重新分发。然而，面对未修补的安全漏洞时，开源就像一把双刃剑。</p><p data-vmark="14b1">近日，安全研究员 Max Kellermann 发现了 Linux 内核的一个高危漏洞，该漏洞被称为 <a href="https://dirtypipe.cm4all.com/" target="_blank">Dirty Pipe</a>（脏管道），编号 CVE-2022-0847，可以覆盖任意只读文件中的数据，<span class="accentTextColor">并获得 root 权限</span>。</p><p data-vmark="e3a5" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/295b62f2-af37-4293-b3bf-1a6e97ce3a2f.png" w="748" h="233" title="大量安卓 12 新手机受影响，Linux 内核被曝 Dirty Pipe 高危提权漏洞：骁龙 8 Gen 1、天玑 9000 等新机可被恶意 root" width="748" height="233" referrerpolicy="no-referrer"></p><p data-vmark="4887">该漏洞在 Linux 内核 5.8 版本及以上，5.16.11、5.15.25 和 5.10.102 版本以下受影响，也就是 <span class="accentTextColor">5.8 <= 影响版本 < 5.16.11 / 5.15.25 / 5.10.102</span>。</p><p data-vmark="c0be" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/a93e37ee-a204-4097-abf1-675935fd0c8c.png" w="1002" h="395" title="大量安卓 12 新手机受影响，Linux 内核被曝 Dirty Pipe 高危提权漏洞：骁龙 8 Gen 1、天玑 9000 等新机可被恶意 root" width="1002" height="323" referrerpolicy="no-referrer"></p><p data-vmark="9a23">而按照<a class="s_tag" href="https://android.ithome.com/" target="_blank">安卓</a>系统的要求，大量<span class="accentTextColor">新发布的</span><span class="accentTextColor"><a class="s_tag" href="https://android.ithome.com/" target="_blank">安卓 12</a> 手机</span>已经用上了 Linux 内核 5.8 版本及以上，因此这些设备将受到影响，包括搭载骁龙 8 Gen 1、天玑 8000 系列、天玑 9000、Exynos 2200 和谷歌 Tensor 的设备等。</p><p data-vmark="f1d6" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/e6e62ef4-7f5a-476a-8a93-ccd8cd09d5f5.png" w="1084" h="738" title="大量安卓 12 新手机受影响，Linux 内核被曝 Dirty Pipe 高危提权漏洞：骁龙 8 Gen 1、天玑 9000 等新机可被恶意 root" width="1084" height="558" referrerpolicy="no-referrer"></p><p data-vmark="073c" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/d72a6d46-f8f3-483d-bd69-6646f440bdf4.png" w="740" h="643" title="大量安卓 12 新手机受影响，Linux 内核被曝 Dirty Pipe 高危提权漏洞：骁龙 8 Gen 1、天玑 9000 等新机可被恶意 root" width="740" height="643" referrerpolicy="no-referrer"></p><p data-vmark="5f99" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/8abfd9cd-ded9-4d00-b6b9-44ea4bc58cb4.png" w="1440" h="353" title="大量安卓 12 新手机受影响，Linux 内核被曝 Dirty Pipe 高危提权漏洞：骁龙 8 Gen 1、天玑 9000 等新机可被恶意 root" width="1440" height="201" referrerpolicy="no-referrer"></p><p data-vmark="9d4e" style="text-align: justify;">IT之家了解到，根据 Kellermann 的说法，谷歌上个月将他的错误修复与安卓内核合并，将在 Linux 内核版本 <span class="accentTextColor">5.16.11、5.15.25 和 5.10.102 及以上</span>修复。不过，由于安卓手机市场的碎片化，这些补丁很大一部分要依赖 OEM 厂商来更新。</p>
          
</div>
            