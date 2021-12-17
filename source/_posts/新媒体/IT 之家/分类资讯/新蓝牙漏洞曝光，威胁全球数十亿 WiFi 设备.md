
---
title: '新蓝牙漏洞曝光，威胁全球数十亿 WiFi 设备'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://picsum.photos/400/300?random=9668'
author: IT 之家
comments: false
date: Fri, 17 Dec 2021 03:40:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=9668'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://www.ithome.com/0/593/001.htm#">dluter</a> 的线索投递！</div>
            <p data-vmark="e095"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 12 月 17 日消息，达姆施塔特大学、布雷西亚、CNIT 和安全移动网络实验室的研究人员近日发表了一篇论文，揭示了攻击者可以通过针对具有多种无线技术的移动设备的蓝牙组件来提取密码并操纵 Wi-Fi 芯片上的网络流量。</p><p data-vmark="bdc7">智能手机、平板电脑和其他现代移动设备的芯片系统（SoC）包含独立的蓝牙、Wi-Fi 和 LTE 组件，每个组件都有自己专门的安全措施。然而，<span class="accentTextColor">这些组件往往共享许多相同的资源，如设备的天线或无线频谱。</span></p><p data-vmark="9a39">根据上述论文，<span class="accentTextColor">攻击者有可能利用这些共享资源作为桥梁，跨越无线芯片边界发起横向权限升级攻击</span>。如果攻击者能够利用这些漏洞，<span class="accentTextColor">他们可以实现代码执行、内存读出和拒绝服务</span>。</p><p data-vmark="ee68">为了利用这些漏洞，研究人员首先需要在蓝牙或 Wi-Fi 芯片上进行代码执行。完成后，他们就能通过使用共享内存资源对设备的其他芯片进行横向攻击。</p><p data-vmark="777a">研究人员总共发现了九个不同的漏洞，虽然有些漏洞可以通过固件更新来修复，<span class="accentTextColor">但一些漏洞只能通过新的硬件修改来修复</span>，这使得数十亿的现有设备处于潜在的被攻击风险之中。</p><p data-vmark="1863">在他们的测试中，研究人员调查了博通、Silicon Labs 和 Cypress 的芯片，这些芯片存在于数十亿的设备中。在他们向这些芯片供应商报告了这些缺陷后，一些供应商已经发布了安全更新来解决这些问题。然而，一些厂商还没有解决这些问题，因为它们影响到不再支持的产品，如 Nexus 5 和 <a class="s_tag" href="https://iphone.ithome.com/" target="_blank">iPhone</a> 6。</p><p data-vmark="927d">IT之家了解到，为了防止成为利用这些缺陷的任何攻击的受害者，用户应该删除不必要的蓝牙设备配对，从他们的设备设置中删除未使用的 Wi-Fi 网络，并使用移动数据而不是公共 Wi-Fi。</p>
          
</div>
            