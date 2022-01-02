
---
title: '微软 Exchange 服务器出现 2022 年日期 Bug，暂时无法处理邮件'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/6152d33eb15ec070d04a6106_1024.jpg'
author: ZAKER
comments: false
date: Sat, 01 Jan 2022 18:24:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/6152d33eb15ec070d04a6106_1024.jpg'
---

<div>   
<p>IT 之家 1 月 2 日消息，据 NeoWin 报道，微软 Exchange 服务器无法正确解析 2022 年的新日期，暂时无法处理邮件。</p><p>根据挪威公司 Sopra Steria 经理 Marius Sandbu 发布的报告，微软推送的 Exchange 新日期补丁无法正常运行，"220101001" 无法被正常解析，因为微软使用了 signed int32 作为日期格式，结果 2.201.010.001 超过了 long int 的最大值 2.147.483.647。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202109/6152d33eb15ec070d04a6106_1024.jpg" data-height="602" data-width="806" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/6152d33eb15ec070d04a6106_1024.jpg" referrerpolicy="no-referrer"></div></div>此外，为了恢复邮件处理，系统管理员不得不在他们的 Exchange 服务器上禁用恶意软件扫描，这可能会使用户和服务器本身受到攻击。<p></p><p>IT 之家了解到，该问题将影响 Exchange Server 2013、2016 和 2019。微软还未就此问题做出回应。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            