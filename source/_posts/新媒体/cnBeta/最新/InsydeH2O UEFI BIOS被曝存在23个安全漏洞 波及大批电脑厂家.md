
---
title: 'InsydeH2O UEFI BIOS被曝存在23个安全漏洞 波及大批电脑厂家'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0203/6582ca30c4377af.jpg'
author: cnBeta
comments: false
date: Thu, 03 Feb 2022 02:58:03 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0203/6582ca30c4377af.jpg'
---

<div>   
专业处理固件威胁的安全研究公司 Binarly，<strong>刚刚在周二的一篇博客文章中披露了 InsydeH2O“Hardware-2-Operating System”UEFI BIOS 中存在的问题。</strong>作为微软、英特尔、惠普、戴尔、联想、西门子、富士通等多家科技巨头的固件供应商，这意味着它们都易受将近两打安全漏洞的影响。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0203/6582ca30c4377af.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p><a href="https://www.binarly.io/posts/An_In_Depth_Look_at_the_23_High_Impact_Vulnerabilities/index.html" target="_self">Binarly.io</a> 在网站上披露了总共 23 个此类漏洞，可知其主要波及所谓的“系统管理模式”（简称 SMM）：</p><p><img src="https://static.cnbetacdn.com/article/2022/0203/1ed6dda6182b0f6.png" alt="1.png" referrerpolicy="no-referrer"></p><p>由于这是固件级别的缺陷，因而成功利用可能导致几乎无法摆脱的持久性恶意软件。</p><p><a href="https://static.cnbetacdn.com/article/2022/0203/b92318befe0e872.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/b92318befe0e872.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>其中大多数漏洞（CVSS 评分 7.5 - 8.2 / 高危）可利用 SMM 权限执行代码，在借此绕过安全功能之后，这些漏洞还可在长期持久性的第二阶段继续发挥作用。</p><p><a href="https://static.cnbetacdn.com/article/2022/0203/80869e115660bef.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/80869e115660bef.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>得逞后，攻击者可让消费者在重装系统后也无法摆脱顽固的恶意软件，并允许其绕过端点安全解决方案（EDR / AV）、安全启动、以及基于虚拟化的安全隔离措施。</p><p><img src="https://static.cnbetacdn.com/article/2022/0203/a5a0ec0be15064b.png" alt="4.png" referrerpolicy="no-referrer"></p><p>更糟糕的是，由于可信平台模块（TPM）的固件运行时可见性设计限制，固件完整性监测系统和远程设备健康证明解决方案也无法检测到对所有已发现漏洞的主动利用。</p><p><img src="https://static.cnbetacdn.com/article/2022/0203/538c9365225fa02.png" alt="5.png" referrerpolicy="no-referrer"></p><p>据悉，Binarly 首先是在富士通 LifeBook 笔记本电脑上发现了这一漏洞，然后很快意识到其它供应商也面临同样的问题 —— 因为它们都选用了 <a href="https://www.insyde.com/press_news/press-releases/insyde%C2%AE-software-credits-binarly%E2%80%99s-ai-powered-firmware-threat-detection" target="_self">InsydeH2O</a> UEFI 解决方案。</p>   
</div>
            