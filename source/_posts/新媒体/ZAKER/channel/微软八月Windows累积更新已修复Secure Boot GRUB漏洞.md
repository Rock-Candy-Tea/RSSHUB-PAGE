
---
title: '微软八月Windows累积更新已修复Secure Boot GRUB漏洞'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f614808e9f096fba5971d0_1024.jpg'
author: ZAKER
comments: false
date: Fri, 12 Aug 2022 03:19:24 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f614808e9f096fba5971d0_1024.jpg'
---

<div>   
<p>ZAKER 科技 8 月 12 日消息，在本月的补丁星期二活动日中，微软面向尚处于支持状态的 Windows 系统发布了累积更新。安全方面，累积更新 KB5012170 增强了 Secure Boot DBX 的防护能力。Secure Boot DBX 基本上就是目前发现可破坏设备的 UEFI 可执行文件黑名单。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202208/62f614808e9f096fba5971d0_1024.jpg" data-height="428" data-width="760" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202208/62f614808e9f096fba5971d0_1024.jpg" referrerpolicy="no-referrer"></div></div>在本次 KB5012170 更新中为 DBX 中添加了目前已知的漏洞 UEFI 模组，意味着在本次更新之后将不会再允许执行。而本次阻止的最出名漏洞就是名为 BootHole 的 GRand Unified Boot Loader（GRUB）漏洞。<p></p><p>微软官方公告解释了攻击的工作原理：</p><p></p><div class="zaker_div"><div class="zaker_quote_v3"><p>Microsoft 知道 Linux 常用的 GRand Unified Boot Loader ( GRUB ) 中的一个漏洞。此漏洞被称为 "There ’ s a Hole in the Boot"，可能允许绕过安全启动。</p><p>要利用此漏洞，攻击者需要在安全启动配置为信任 Microsoft 统一可扩展固件接口 ( UEFI ) 证书颁发机构 ( CA ) 的系统上拥有管理权限或物理访问权限。攻击者可以安装受影响的 GRUB 并在目标设备上运行任意引导代码。成功利用此漏洞后，攻击者可以禁用进一步的代码完整性检查，从而允许将任意可执行文件和驱动程序加载到目标设备上。</p></div><div class="edi_oper"></div></div><p></p><p>Microsoft 已发布独立的安全更新 5012170，以针对此通报中描述的漏洞提供保护。</p><p>本次更新适用于以下 Windows 和版本</p><p>● Windows Server 2012</p><p>● Windows 8.1 and Windows Server 2012 R2</p><p>● Windows 10, version 1507</p><p>● Windows 10, version 1607 and Windows Server 2016</p><p>● Windows 10, version 1809 and Windows Server 2019</p><p>● Windows 10, version 20H2</p><p>● Windows 10, version 21H1</p><p>● Windows 10, version 21H2</p><p>● Windows Server 2022</p><p>● Windows 11, version 21H2 ( original release ) </p><p>● Azure Stack HCI, version 1809</p><p>● Azure Stack Data Box, version 1809 ( ASDB ) </p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            