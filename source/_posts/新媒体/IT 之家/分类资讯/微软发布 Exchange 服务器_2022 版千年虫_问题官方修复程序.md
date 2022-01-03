
---
title: '微软发布 Exchange 服务器_2022 版千年虫_问题官方修复程序'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/9/f2f81663-2cc3-414c-ba9b-74fcaf0f2e0c.png'
author: IT 之家
comments: false
date: Sun, 02 Jan 2022 23:40:29 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/9/f2f81663-2cc3-414c-ba9b-74fcaf0f2e0c.png'
---

<div>   
<p data-vmark="1adf"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 1 月 3 日消息，微软 Exchange 服务器无法<span class="accentTextColor">正确解析 2022 年的新日期</span>，导致出现了无法处理邮件的问题，被用户调侃为“2022 版千年虫”。</p><p data-vmark="1930"><img src="https://img.ithome.com/newsuploadfiles/2021/9/f2f81663-2cc3-414c-ba9b-74fcaf0f2e0c.png" title="微软发布 Exchange 服务器“2022 版千年虫”问题官方修复程序" referrerpolicy="no-referrer"></p><blockquote><p data-vmark="87f8">FIP-FS 扫描引擎加载失败 – 无法将“2201010001”转换为 long (2022/01/01 00:00 UTC)</p></blockquote><p data-vmark="c77d">根据挪威公司 Sopra Steria 经理 Marius Sandbu 发布的报告，因为微软使用了 signed int32 作为日期格式，结果 2201010001 超过了 long int 的最大值 2147483647。</p><p data-vmark="9f05">（“千年虫”是指由于部分计算机程序只采用两位十进制数表示年份，在跨世纪时就会出现错误。）</p><p data-vmark="aa9c">微软现已发布了针对该问题的<span class="accentTextColor">修复程序</span>，该修复程序可以通过自动脚本执行。</p><p data-vmark="60bf"><strong>脚本地址：</strong></p><p data-vmark="3185"><a href="https://aka.ms/ResetScanEngineVersion" target="_blank"><span class="link-text-start-with-http">https://aka.ms/ResetScanEngineVersion</span></a></p><p data-vmark="e796">IT之家了解到，该问题影响 <span class="accentTextColor">Exchange Server 2013、2016 和 2019</span>。</p>
          
</div>
            