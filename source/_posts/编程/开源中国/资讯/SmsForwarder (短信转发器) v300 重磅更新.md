
---
title: 'SmsForwarder (短信转发器) v3.0.0 重磅更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4ae608d48a2887dd32f0bb3c605220d4e0f.webp'
author: 开源中国
comments: false
date: Thu, 09 Jun 2022 06:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4ae608d48a2887dd32f0bb3c605220d4e0f.webp'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start"><strong>短信转发器——不仅只转发短信，备用机必备神器！</strong></p> 
<p style="color:#24292f; text-align:start">        监控Android手机短信、来电、APP通知，并根据指定规则转发到其他手机：钉钉机器人、企业微信群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram机器人、Server酱、PushPlus、手机短信等。</p> 
<p style="color:#24292f; text-align:start"><strong>包括主动控制服务端与客户端，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。（V3.0 新增）</strong></p> 
<p> </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-4ae608d48a2887dd32f0bb3c605220d4e0f.webp" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h3 style="text-align:start">更新日志</h3> 
<ul> 
 <li>重构：采用 Kotlin 全新重构（不是迁移代码）</li> 
 <li>重构：全新的界面 XUI 实现（略微提升点前端美感）</li> 
 <li>重构：全新的 HttpServer 实现（采用 AndServer，目前有6个API）</li> 
 <li>新增：增加 Frpc 支持内网穿透（按需下载 FrpcLib 动态库支持）</li> 
 <li>新增：主动控制·客户端（界面直接远程发短信等）</li> 
 <li>新增：保活措施 Cactus（双进程前台服务，JobScheduler，onePix(一像素)，WorkManager，无声音乐）</li> 
 <li>优化：适配 Android 4.4 ~ 12.0</li> 
 <li>优化：舍弃 emailkit 依赖，直接基于 android-mail 重写</li> 
 <li>优化：自动过滤指定时间内的重复消息</li> 
 <li>修复：v2.x 的 issue</li> 
 <li>精简：一些不必要的功能（含尚未迁移的小功能）</li> 
</ul> 
<h2 style="text-align:start">V3.0 界面预览：</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-28cc7e6b314a88a88c3408fa339fac7d156.webp" referrerpolicy="no-referrer"></p> 
<p>更多更新细节参见Wiki：https://gitee.com/pp/SmsForwarder/wikis/Home</p> 
<p>最后，<span style="background-color:#ffffff; color:#333333">感谢大家的支持与厚爱，开源以来，收到很多优秀的改进建议，用第38个版本迎接即将到来的 3.8K 的 star！</span></p>
                                        </div>
                                      
</div>
            