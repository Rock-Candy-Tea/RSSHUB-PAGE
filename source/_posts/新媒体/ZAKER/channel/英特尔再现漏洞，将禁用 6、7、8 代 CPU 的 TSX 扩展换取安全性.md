
---
title: '英特尔再现漏洞，将禁用 6、7、8 代 CPU 的 TSX 扩展换取安全性'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202106/60dbcb21b15ec02c0c681902_1024.jpg'
author: ZAKER
comments: false
date: Tue, 29 Jun 2021 20:12:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202106/60dbcb21b15ec02c0c681902_1024.jpg'
---

<div>   
<p>IT 之家 6 月 30 日消息 据 Phoronix 报道，英特尔很快将再次以性能换安全，用微码禁用更多 CPU 的 TSX 支持。</p><p>据称，英特尔将通过微码更新将其第 6 代、第 7 代和第 8 代处理器上默认禁用英特尔事务性同步扩展 ( TSX ) ，禁用该特性是为了堵上内存漏洞，但也可能会导致使用 TSX 的任务出现性能降低的问题。</p><p>Phoronix 表示，此次更新是由于 TSX 中的内存排序问题导致的。一份 PDF 表明，英特尔自 2018 年 6 月以来就发现了这一问题，但但直到 2021 年 6 月才推出微码更新以默认禁用 TSX。</p><p>尽管如此，英特尔为受影响的 CPU 禁用 TSX 还是花了将近三年的时间。这些更新已经包含在 6 月 8 日首次亮相的英特尔平台 2021.1 更新中。</p><p>IT 之家了解到，自 Haswell 以来，事务同步扩展 ( TSX ) 就一直存在于英特尔 CPU 中，并且在特定工作负载中比英特尔前代产品快 40% 左右，或者在数据库事务基准测试中快 4 到 5 倍。</p><p>英特尔此前也表示 :" 受益于英特尔 TSX 的工作负载可能会产生性能上的变化。" 它还表示，由于微码更新，" 一些性能监视的高级用户可能需要更改他们的收集脚本和方法 "。但英特尔并没有提供更多的信息。</p><p>还有一个好消息：英特尔表示它 " 不希望这些微码更新会影响不使用 [ 性能监控单元 ] 或仅使用更新的 PMU 驱动程序和工具的用户 "，尽管它建议 PMU 驱动程序开发人员和性能工具开发人员遵循官方文档中的指导。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202106/60dbcb21b15ec02c0c681902_1024.jpg" data-height="791" data-width="1116" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202106/60dbcb21b15ec02c0c681902_1024.jpg" referrerpolicy="no-referrer"></div></div><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202106/60dbcb21b15ec02c0c681903_1024.jpg" data-height="104" data-width="1062" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202106/60dbcb21b15ec02c0c681903_1024.jpg" referrerpolicy="no-referrer"></div></div>当然，大多数普通用户根本不会注意到更新后的性能变化，但目前开发人员已经为这些微码更新适配了最新的 Linux 内核。<p></p><p>Phoronix 指出，针对 Linux 5.14 的补丁进行了这一更改：" 在某些型号上添加对弃用 TSX 的新英特尔微码的支持，并且当 TSX 事务总是因该微码更新而中止时，不会为那些 cpu 启用内核解决方案。" 这种支持也可能会出现在 Linux 5.13 版本中。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            