
---
title: '苹果 watchOS 8.5 正式版发布：修复了可能暴露 IP 地址的邮件隐私保护漏洞'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/3/75708e67-329c-4c01-87db-bf37f2651867.png'
author: IT 之家
comments: false
date: Tue, 15 Mar 2022 14:50:03 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/3/75708e67-329c-4c01-87db-bf37f2651867.png'
---

<div>   
<p data-vmark="6af2"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 3 月 15 日消息，苹果 watchOS 8.5 正式版今日已向 Apple Watch 用户推送。据 MacRumors 报道，安全研究人员发现，<span class="accentTextColor">watchOS 8.5 修复了邮件 App 中的一个安全漏洞</span>，该漏洞可能会在下载远程内容时泄露用户的 IP 地址。</p><p style="text-align: center;" data-vmark="9f3c"><img src="https://img.ithome.com/newsuploadfiles/2022/3/75708e67-329c-4c01-87db-bf37f2651867.png" w="774" h="432" title="苹果 watchOS 8.5 正式版发布：修复了可能暴露 IP 地址的邮件隐私保护漏洞" width="774" height="432" referrerpolicy="no-referrer"></p><p data-vmark="ccc2">苹果的邮件隐私保护是 iOS 15、<a class="s_tag" href="https://ipad.ithome.com/" target="_blank">iPad</a>OS 15 和 macOS Monterey 中引入的一项新功能，<span class="accentTextColor">可隐藏用户的 IP 地址</span>，因此发件人无法确定用户的位置。该功能还可以防止发件人跟踪用户是否打开电子邮件、查看电子邮件的次数以及是否转发了电子邮件。</p><p data-vmark="4685">IT之家了解到，该功能的工作原理是通过多个代理服务器路由以剥离用户的 IP 地址，然后分配一个与用户一般区域相对应的<span class="accentTextColor">随机 IP 地址</span>，使电子邮件发件人无法看到用户的特定信息。</p><p data-vmark="a2b9">然而，该功能并不支持 Apple Watch，因此产生了安全漏洞。安全研究人员和开发人员 Talal Haj Bakry 和 Tommy Mysk 发现，Apple Watch 不会隐藏收件人的 IP 地址，在接收邮件通知和打开电子邮件时，都会使用收件人的真实 IP 地址。</p><p data-vmark="4e2f">现在，Bakry 和 Mysk 发现苹果已经在 watchOS 8.5 中修复了这个问题。从 watchOS 8.5 开始，Apple Watch 会自动阻止加载远程内容，而是提供“<span class="accentTextColor">是否直接加载内容</span>”选项。</p>
          
</div>
            