
---
title: '联想 Yoga、ThinkPad 笔记本发现两个漏洞，官方已修复'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/12/5c40e2d2-3780-44bf-bc5f-c9ae906f042c.png'
author: IT 之家
comments: false
date: Sat, 18 Dec 2021 00:23:26 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/12/5c40e2d2-3780-44bf-bc5f-c9ae906f042c.png'
---

<div>   
<p data-vmark="d622"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 12 月 18 日消息，据外媒报道，有海外安全研究人员发现了联想 Yoga、ThinkPad 系列笔记本中存在的两个安全漏洞。这一漏洞并非 Windows 系统内的 Bug，而是 OEM 软件的缺陷。安全人员发现，黑客可以利用这两项漏洞获得权限提升，从而便于控制系统。</p><p data-vmark="6ec8"><img src="https://img.ithome.com/newsuploadfiles/2021/12/5c40e2d2-3780-44bf-bc5f-c9ae906f042c.png" w="1060" h="596" alt="ThinkPad X1 Carbon Gen 9" title="联想 Yoga、ThinkPad 笔记本发现两个漏洞，官方已修复" width="1060" height="461" referrerpolicy="no-referrer"></p><p data-vmark="8f64">以下为漏洞详情：</p><ul class=" list-paddingleft-2"><li><p data-vmark="ae6c">CVE-2021-3922：Lenovo System Interface Foundation 的组件 IMController 中存在一个竞争条件漏洞。本地攻击者可以利用该漏洞与 IMController 子进程里的命名管道（named pipe）进行连接，并与之交互。</p></li><li><p data-vmark="50f9">CVE-2021-3969：这一漏洞同样来自于 IMController 组件。一个时间检查漏洞（TOCTOU）可以允许本地攻击者提升权限。</p></li></ul><p data-vmark="7324">虽然这两个漏洞属于本地漏洞，但是攻击者也可以通过其它手段远程连接电脑，并利用漏洞进行攻击。幸运的是，联想已经为 Lenovo System Interface Foundation 提供了更新，<span class="accentTextColor">将其升级至 1.1.20.3 版本之后</span>，可以修复 IMController 的问题。</p><p data-vmark="634c">据IT之家了解，本次更新将自动推送，用户也可以通过重启计算机或重启“System Interface Foundation Service”服务来获取更新。</p><p data-vmark="a0f5">想要检查 Lenovo IMController 当前版本号，可以执行以下操作：</p><ul class="ai-word-checked list-paddingleft-2"><li><p data-vmark="4f18">打开文件资源管理器，进入 C:\Windows\Lenovo\ImController\PluginHost\ 目录。</p></li><li><p data-vmark="3020">右键单击“Lenovo.Modern.ImController.PluginHost.exe”，打开属性。</p></li><li><p data-vmark="ce20">点击“详细信息”标签。</p></li><li><p data-vmark="e0ff">查看程序版本号。</p></li></ul><p data-vmark="8715"><img src="https://img.ithome.com/newsuploadfiles/2021/12/ef164b73-ad12-4e67-8949-98aacd4a5596.png" w="1341" h="616" alt="联想官方页面截图" title="联想 Yoga、ThinkPad 笔记本发现两个漏洞，官方已修复" width="1341" height="377" referrerpolicy="no-referrer"></p><p data-vmark="aabe">IT之家获悉，截至目前，联想官网中 Lenovo System Interface Foundation 软件还未更新至最新版，当前版本号为：1.1.19.8。</p>
          
</div>
            