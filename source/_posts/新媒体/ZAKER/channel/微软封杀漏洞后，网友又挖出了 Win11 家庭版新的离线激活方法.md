
---
title: '微软封杀漏洞后，网友又挖出了 Win11 家庭版新的离线激活方法'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/613e1bf8b15ec03cce542222_1024.jpg'
author: ZAKER
comments: false
date: Sun, 12 Sep 2021 18:08:39 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/613e1bf8b15ec03cce542222_1024.jpg'
---

<div>   
<p>IT 之家 9 月 12 日消息 微软对 Windows 11 家庭版用户规定了特殊要求，要求用户必须在 OOBE 联网登录微软账户后方可进入桌面从而完成系统激活，而专业版和企业版都没有这一限制因此可直接创建本地账户。</p><p>IT 之家了解到，此前网友 Adam ( warwagon ) 发现，直接拔下网线并 "Alt + F4" 关闭提示窗即可绕过 OOBE 限制创建本地账户，但很可惜在经过泛滥传播后已经被微软封杀。</p><p>有趣的是，现在他又找出了一个新的漏洞，现在需要安装 Windows 11 家庭版的用户在首次配置开机向导时可通过以下步骤绕过联网要求实现离线激活：</p><p>在 OOBE 提示联网的界面同时按下 Shift + F10 打开命令行</p><p>在命令行窗口输入 taskmgr 并回车找到并结束 Network Connection Flow 进程，或者直接输入 taskkill /F/IM oobenetworkconnectionflow.exe 结束上述进程</p><p>现在你就会发现已经可以正常通过 OOBE 创建本地账户</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202109/613e1bf8b15ec03cce542222_1024.jpg" data-height="821" data-width="1077" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202109/613e1bf8b15ec03cce542222_1024.jpg" referrerpolicy="no-referrer"></div></div><p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            