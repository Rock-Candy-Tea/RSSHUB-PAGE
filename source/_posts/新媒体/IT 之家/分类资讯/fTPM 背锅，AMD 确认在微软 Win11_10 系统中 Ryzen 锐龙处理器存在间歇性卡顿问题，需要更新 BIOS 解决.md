
---
title: 'fTPM 背锅，AMD 确认在微软 Win11_10 系统中 Ryzen 锐龙处理器存在间歇性卡顿问题，需要更新 BIOS 解决'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/3/f2b11003-69b1-4bee-994e-2a76a284219f.png'
author: IT 之家
comments: false
date: Tue, 08 Mar 2022 00:03:18 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/3/f2b11003-69b1-4bee-994e-2a76a284219f.png'
---

<div>   
<p data-vmark="f0fe"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 3 月 8 日消息，如果你有一台搭载 AMD 处理器的 <a class="s_tag" href="https://win10.ithome.com/" target="_blank">Windows 10</a> 或 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Windows 11</a> 电脑，你可能会感觉你的系统运行时偶尔犯病，而且从网友反馈来看这种情况并不算少。</p><p data-vmark="854a">AMD 在其官网发表了一篇<a href="https://www.amd.com/en/support/kb/faq/pa-410" target="_blank">文章</a>，详细介绍了在启用 fTPM 时，系统可能会出现的间歇性卡顿问题。据该公司称，挂起和卡顿是由串行外设接口 (SPI) 闪存 ROM 内的扩展内存事务操作导致的。</p><p data-vmark="1ef5">AMD 表示，这个问题会影响 AMD Ryzen 用户对于 Windows 系统的选择，它可能会间歇性地在主板上的 SPI 闪存中执行与 ftpm 相关的扩展内存任务。</p><p data-vmark="a768">官方指出，这可能导致系统交互性或响应性暂时暂停，直到任务完成。</p><p data-vmark="36e2">AMD 称，目前给出的修复方法是更新主板 BIOS，新版 BIOS 对与 fTPM 相关的内存执行模块进行了更新和增强。但问题是，该修复补丁要到 2022 年 5 月初才能发布，而且只适用于基于 AMD AGESA 1207 以及更新的主板。</p><p data-vmark="c158">为了解决这个问题，AMD 建议使用硬件 TPM 设备搭配新版 Windows 系统，毕竟硬件 TPM 是利用板载非易失性存储器 (NVRAM) 取代了有问题的 SPI 闪存。</p><p data-vmark="e29e">IT之家了解到，AMD 也提到了微软的这个<a href="https://docs.microsoft.com/zh-cn/previous-versions/windows/it-pro/windows-8.1-and-8/dn466538(v=ws.11)#clear-all-the-keys-from-the-tpm" target="_blank">网页</a>，它可能会帮助到 TPM 用户，但似乎也不是什么治本的方案。</p><p data-vmark="bb30" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/f2b11003-69b1-4bee-994e-2a76a284219f.png" w="275" h="183" title="fTPM 背锅，AMD 确认在微软 Win11/10 系统中 Ryzen 锐龙处理器存在间歇性卡顿问题，需要更新 BIOS 解决" width="275" height="183" referrerpolicy="no-referrer"></p>
          
</div>
            