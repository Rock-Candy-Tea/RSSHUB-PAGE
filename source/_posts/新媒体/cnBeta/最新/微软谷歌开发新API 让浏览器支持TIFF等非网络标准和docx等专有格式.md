
---
title: '微软谷歌开发新API 让浏览器支持TIFF等非网络标准和docx等专有格式'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0712/039e261d140db3b.jpg'
author: cnBeta
comments: false
date: Mon, 12 Jul 2021 03:47:24 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0712/039e261d140db3b.jpg'
---

<div>   
<strong>援引外媒报道，微软正在和Google合作开发一套“Pickle Clipboard APIs”，用于改善 Chrome 和 Edge 浏览器的默认剪贴板功能。</strong>通过全新的 API，允许用户在浏览器和本地应用程序之间轻松复制和粘贴各种复杂的数据有效载荷（文件格式）。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0712/039e261d140db3b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0712/039e261d140db3b.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">目前，基于 Chromium 的 Edge/Chrome 浏览器在剪贴板（复制和粘贴）内容的访问方面存在诸多限制。目前这两款浏览器只支持 .txt、.jpg、.png、HTML 和其他常见主流格式，支持跨 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10、macOS、Linux 和移动平台剪贴。</p><p style="text-align: left;">不过，现有的 API 并不支持长尾的专有格式。例如，网络应用不能读取定制的网络格式，例如 TIFF（一种大型图像格式）的非网络标准格式，以及.docx（<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 文档格式）的专有格式。这些格式并不被支持，因此用户无法在大多数网络应用中复制粘贴它们。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0712/d3cd113f8e6bed2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0712/d3cd113f8e6bed2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">而通过全新的 Pickle Clipboard APIs，微软和Google正携手为这个问题提供一个解决方案。如果该功能在浏览器中实现并得到开发者的支持，你最喜欢的网络应用就可以使用标准化的腌制格式读写任意的未<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C13297%2C1301" target="_blank">消毒</a>的有效载荷。换句话说，你很快就可以在网络应用和Windows、macOS、Android和其他平台的本地应用之间复制和粘贴自定义文件格式。</p><p style="text-align: left;">Pickle Clipboard APIs 的好处：</p><p style="text-align: left;">● 允许在网络和本地应用程序之间复制/粘贴：这将不由浏览器处理，这意味着它将依赖于操作系统的剪贴板。</p><p style="text-align: left;">● 开发人员可以创建自定义剪贴板格式。</p><p style="text-align: left;">● 保护安全/隐私。</p><p style="text-align: left;">● 提供对剪贴板的精细化控制。</p><p style="text-align: left;">● 建立在现有的 Async Clipboard API 上。</p><p style="text-align: left;">在多个Chromium代码补丁中，微软已经确认它已经开始为Chromium浏览器提供自定义剪贴板格式支持。例如，一个补丁包含了 Async Clipboard API 中自定义剪贴板格式的运行时 Flag 实现。</p>   
</div>
            