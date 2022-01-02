
---
title: '2022 版_千年虫_：微软 Exchange 服务器出现 2022 年日期 Bug，暂时无法处理邮件'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/9/f2f81663-2cc3-414c-ba9b-74fcaf0f2e0c.png'
author: IT 之家
comments: false
date: Sat, 01 Jan 2022 23:50:06 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/9/f2f81663-2cc3-414c-ba9b-74fcaf0f2e0c.png'
---

<div>   
<p data-vmark="92e4"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 1 月 2 日消息，据 NeoWin 报道，微软 Exchange 服务器无法正确解析 2022 年的新日期，<span class="accentTextColor">暂时无法处理邮件</span>。</p><p data-vmark="3835">根据挪威公司 Sopra Steria 经理 Marius Sandbu 发布的报告，微软推送的 Exchange 新日期补丁无法正常运行，“220101001”无法被正常解析，因为微软使用了 signed int32 作为日期格式，<span class="accentTextColor">结果 2.201.010.001 超过了 long int 的最大值 2.147.483.647</span>。</p><p data-vmark="f6fd"><img src="https://img.ithome.com/newsuploadfiles/2021/9/f2f81663-2cc3-414c-ba9b-74fcaf0f2e0c.png" title="2022 版“千年虫”：微软 Exchange 服务器出现 2022 年日期 Bug，暂时无法处理邮件" referrerpolicy="no-referrer"></p><p data-vmark="54ec">这一 Bug 听起来很像 2000 年的“千年虫”，由于部分计算机程序只采用两位十进制数表示年份，在跨世纪时就会出现错误。</p><p data-vmark="6b9b">此外，为了恢复邮件处理，系统管理员不得不在他们的 Exchange 服务器上禁用恶意软件扫描，这可能会使用户和服务器本身受到攻击。</p><p data-vmark="85ae">IT之家了解到，该问题将影响 <span class="accentTextColor">Exchange Server 2013、2016 和 2019</span>。</p><p data-vmark="9ea4">微软<a href="https://techcommunity.microsoft.com/t5/exchange-team-blog/email-stuck-in-transport-queues/ba-p/3049447" target="_blank">回应</a>称，工程师正在夜以继日地进行修复，以消除客户操作的需要，需要几天时间来开发和部署。此外，微软开发另一个更新，该更新正在最终测试验证中。更新需要客户采取行动，但它将提供最快的解决时间。</p><p data-vmark="9f33"><img src="https://img.ithome.com/newsuploadfiles/2022/1/1d10b1d2-2e14-49c8-af3f-cf54920ecb4c.png" w="1277" h="319" title="2022 版“千年虫”：微软 Exchange 服务器出现 2022 年日期 Bug，暂时无法处理邮件" width="1277" height="205" referrerpolicy="no-referrer"></p>
          
</div>
            