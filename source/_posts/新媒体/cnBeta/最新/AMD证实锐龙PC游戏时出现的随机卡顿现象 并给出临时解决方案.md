
---
title: 'AMD证实锐龙PC游戏时出现的随机卡顿现象 并给出临时解决方案'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0308/69d689c260f1a2f.jpg'
author: cnBeta
comments: false
date: Tue, 08 Mar 2022 05:44:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0308/69d689c260f1a2f.jpg'
---

<div>   
最近一两个月，许多使用 AMD 锐龙处理器的 PC 游戏玩家，都在吐槽于 Windows 10 / 11 操作系统中玩游戏时遇到的随机卡顿故障。<strong>经过漫长的调查，AMD 终于在近日证实，故障与启用了 fTPM 可信平台模块功能有关。</strong>该公司在公告中称，挂起和卡顿，是由串行外设接口闪存（SPIROM）内的扩展内存事务操作而引发的。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0308/69d689c260f1a2f.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">视频截图（via Harrison S / YouTube）</p><p>AMD 指出：特定的锐龙系统配置，可能间歇性地遇到于主板 SPIROM 中执行与 fTPM 相关的扩展内存事务而导致的系统交互 / 响应卡顿，直到事务完成才恢复。</p><p><img src="https://static.cnbetacdn.com/article/2022/0308/23b654261ff3ca0.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">Reddit r/<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>11 子版块上的网友吐槽</p><p>庆幸的是，AMD 还在公告中提到了一个临时解决方案，且后续会通过预计 5 月发布的 AGESA 1207 更新来彻底修复，届时有需要的玩家可手动更新他们的主板 BIOS 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0308/55a121716111e46.gif" alt="3.gif" referrerpolicy="no-referrer"></p><p style="text-align: center;">游戏内随机卡顿示例</p><p><strong>更新公告写道：</strong></p><blockquote><p>● 新版 BIOS 将包含用于 fTPM 与 SPIROM 交互的增强模块，至于特定主板的 BIOS 发布时间，则取决于各大厂商的测试安排。</p><p>● 作为一种直接的解决方案，以来 fTPM 以获得可信平台模块支持的受影响客户，可改用基于硬件的 dTPM 方案 —— 后者使用了非易失性内存（NVRAM）来取代上述 TPM / SPIROM 交互。</p><p>● 至于兼容性，在尝试实施该解决方案之前，还请提前与您的系统或主板制造商联系，以确认当前平台是否支持附加的 dTPM 硬件模块。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0308/57f5d30f1859970.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">AMD 官方<a href="https://www.amd.com/en/support/kb/faq/pa-410" target="_self">公告</a></p><p><strong>注意事项：</strong></p><blockquote><p>【1】若将活动系统从 fTPM 切换至 dTPM，还请务必在切换 TPM 设备之前，禁用掉基于 TPM 的加密系统（比如 BitLocker 驱动器加密）、以及备份重要的系统数据。</p><p>【2】此外这项操作需要通过具有完全系统管理权限的账户去实施，若您的系统受到组织的同意管理，还请明确获得 IT 管理员的支持。</p></blockquote><p>有关将所有权转移至新 TPM 设备的更多信息，还请移步至<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>专题页查看（<a href="https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-8.1-and-8/dn466538(v=ws.11)" target="_self">传送门</a>）。</p>   
</div>
            