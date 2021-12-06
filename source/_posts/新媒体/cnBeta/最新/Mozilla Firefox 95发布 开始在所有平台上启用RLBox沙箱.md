
---
title: 'Mozilla Firefox 95发布 开始在所有平台上启用RLBox沙箱'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1206/5a1a7f3f66d0101.jpg'
author: cnBeta
comments: false
date: Mon, 06 Dec 2021 13:11:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1206/5a1a7f3f66d0101.jpg'
---

<div>   
Mozilla Firefox
95.0在明天正式发布之前已经可以在FTP上下载，使这个新版本变得有趣的是RLBox的整合。在所有平台上，Mozilla Firefox
95.0浏览器现在使用RLBox来保护第三方库的安全，RLBox旨在对第三方库进行沙盒处理，它由一个基于WebAssembly的沙盒和一个用于在沙盒库内改装现有应用程序代码的API组成。<br>
 <p>RLBox将把沙盒库的内存与应用程序/Firefox的内存隔离开来，与此同时还有其他安全优势。</p><p><img src="https://static.cnbetacdn.com/article/2021/1206/5a1a7f3f66d0101.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>RLBox通过GitHub上的文档得到了更详细的解释。在Mozilla Hacks上也有这样一篇博文，概述了这个基于WASM的沙箱工作：</p><p><a href="https://plsyssec.github.io/rlbox_sandboxing_api/sphinx/" _src="https://plsyssec.github.io/rlbox_sandboxing_api/sphinx/" target="_blank">https://plsyssec.github.io/rlbox_sandboxing_api/sphinx/</a><br></p><p>这个RLBox WebAssembly沙箱代码并不是专门针对Mozilla/Firefox的，它也可以被其他任意的应用程序使用。RLBox最初是由加州大学圣地亚哥分校以及德克萨斯大学奥斯汀分校和标准大学的研究人员设计的。在过去的一年半里，Mozilla一直致力于将RLBox纳入Firefox，对于Firefox 95.0来说，现在它已经达到了跨平台使用的里程碑，可以用于抵御由第三方库引起的问题。</p><p><img src="https://static.cnbetacdn.com/article/2021/1206/bcf420a247e8ab3.jpg" title alt="1.jpg" referrerpolicy="no-referrer"></p><p>Firefox 95现在还支持所有平台的"inputmode"全局属性（以前只支持Android系统），Android系统现在支持CSS光标属性，并通过避免每次运行非本地事件时总是向事件循环发布NSEvent来减少CPU使用，这可以提高电池续航。</p><p><strong>下载地址：</strong></p><p><a href="https://ftp.mozilla.org/pub/firefox/releases/95.0/" _src="http://ftp.mozilla.org/pub/firefox/releases/95.0/" target="_blank">http://ftp.mozilla.org/pub/firefox/releases/95.0/</a><br></p>   
</div>
            