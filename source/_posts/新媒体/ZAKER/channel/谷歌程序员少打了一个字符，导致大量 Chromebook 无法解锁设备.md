
---
title: '谷歌程序员少打了一个字符，导致大量 Chromebook 无法解锁设备'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/60fbc04cb15ec011b3303537_1024.jpg'
author: ZAKER
comments: false
date: Sat, 24 Jul 2021 00:07:33 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/60fbc04cb15ec011b3303537_1024.jpg'
---

<div>   
<p>IT 之家 7 月 24 日消息 近日，谷歌为 Chromebook 推送了 Chrome OS 91 版本，版本号 91.0.4772.165。本次更新出现了重大 Bug，导致许多用户的 Chromebook 无法解锁设备，官方已紧急撤销更新。</p><p>据用户反馈，在更新到该版本后，设备会卡在锁屏界面，无法进入桌面。即使用户输入了正确的密码，也无法使用，有的设备甚至会循环重启。</p><p>而开发者从谷歌官网源码中发现，该问题是由一个极其低级的错误引发的。从下图可以看到，开发者在 if 判断语句中，两个条件之间的与连接符本来是 "&&"，但开发者粗心只打了一个 "&"，造成程序的运行错误，系统无法对用户登录信息进行解密。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202107/60fbc04cb15ec011b3303537_1024.jpg" data-height="477" data-width="1440" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202107/60fbc04cb15ec011b3303537_1024.jpg" referrerpolicy="no-referrer"></div></div>IT 之家了解到，谷歌已紧急发布修复补丁解决了该问题，用户可放心更新了。<p></p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202107/60fbc04cb15ec011b3303538_1024.jpg" data-height="547" data-width="1201" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202107/60fbc04cb15ec011b3303538_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            