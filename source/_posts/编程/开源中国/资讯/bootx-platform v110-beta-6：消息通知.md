
---
title: 'bootx-platform v1.1.0-beta-6：消息通知'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9f0044b76071d5a7f598ceab591c5fedb02.png'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 09:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9f0044b76071d5a7f598ceab591c5fedb02.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left"> 🍈项目介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址：<a href="https://gitee.com/bootx/bootx-platform">https://gitee.com/bootx/bootx-platform</a>，非常欢迎看看项目介绍留以及个<span> </span><strong>Star</strong><span> </span>呀🤺🤺🤺</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">基于 Spring Boot 框架打造，针对单体式应用进行专门设计，提供整套服务模块，努力为打造全方位企业级开发解决方案， 致力将开源版打造成超越商业版后台管理框架的项目。前端分为 vue2 版和 vue3 版，vue2 使用</span><span style="background-color:#ffffff"> </span>ANTD PRO VUE<span style="background-color:#ffffff"> 作为脚手架，vue3 使用 </span>Vben-Admin-Next<span style="background-color:#ffffff"> 作为脚手架（开发中）。 移动端使用 </span>Taro<span style="background-color:#ffffff"> vue3+TS 为技术栈（开发中）。分布式版本 Bootx-Cloud（计划后期重启），尽请期待。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>🍒</span>特色功能</h2> 
<ul> 
 <li>支持单通道支付、聚合支付、组合支付、部分和全部退款等支付功能</li> 
 <li>支持支付宝、微信、云闪付、现金、钱包、储值卡等多种支付方式</li> 
 <li>针对敏感信息，可以通过添加注解实现返回时自动脱敏</li> 
 <li>针对重要信息，可以通过添加注解，实现在数据库中保密存储，配合数据脱敏使用可以更好的保护系统数据的安全</li> 
 <li>支持多种范围的数据权限控制，如只能查看自己、只能查询指定部门、用户、可以查询全部的数据等等</li> 
 <li>支持嵌套查询的超级查询构造器，自动生成对应条件SQL语句</li> 
 <li>支持通过ELK和轻量级PlumeLog来管理项目日志,以适应不同的场景</li> 
 <li>提供移动端开发脚手架，方便开发H5与各种小程序</li> 
 <li>支持通过微信、钉钉、企业微信等第三方开放平台进行扫码登录</li> 
 <li>支持微信、钉钉、企业微信的消息推送</li> 
</ul> 
<p><img height="272" src="https://oscimg.oschina.net/oscnet/up-9f0044b76071d5a7f598ceab591c5fedb02.png" width="500" referrerpolicy="no-referrer"><img height="253" src="https://oscimg.oschina.net/oscnet/up-cbeede194e54f0be45624429019f15a479a.jpg" width="500" referrerpolicy="no-referrer"></p> 
<p><img height="272" src="https://oscimg.oschina.net/oscnet/up-87bad58464672ce5b9d62dd45e8f2bd44e5.jpg" width="500" referrerpolicy="no-referrer"><img height="272" src="https://oscimg.oschina.net/oscnet/up-a84ae4e7ab71669bb727f74ececf456652b.jpg" width="500" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🛠️本次功能更新</h2> 
<ul> 
 <li>新增钉钉工作通知、普通消息通知</li> 
 <li>新增钉钉机器人管理和消息发送</li> 
 <li>新增钉钉文件上传接口</li> 
 <li>新增企业微信消息通知</li> 
 <li>新增企业微信机器人管理</li> 
 <li>新增企业微信机器人上传媒体文件接口</li> 
 <li>将各类第三方平台（钉钉、企微、微信）对接进行结构优化</li> 
 <li>优化mybatis-plus中获取一条的操作方法</li> 
 <li>优化vxe组件的z-index层级</li> 
 <li>优化多页签为固定顶部</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">🥞新功能截图</h2> 
<p><img height="858" src="https://oscimg.oschina.net/oscnet/up-01ccc99dc77cc4f1ad31991b195bf6cf245.png" width="1036" referrerpolicy="no-referrer"></p> 
<p><img height="1917" src="https://oscimg.oschina.net/oscnet/up-8dc1cd6bb1e430c3df356952316a2109b44.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>企业微信机器人</p> 
<p><img height="1163" src="https://oscimg.oschina.net/oscnet/up-61c2c75940ff501ab8cfcf366d687fad1b3.png" width="1315" referrerpolicy="no-referrer"></p> 
<p>企业微信通知</p> 
<p><img height="1137" src="https://oscimg.oschina.net/oscnet/up-2b601313676897efe4a8d3d48289597abcb.png" width="1911" referrerpolicy="no-referrer"></p> 
<p>钉钉机器人通知</p> 
<p><img height="1458" src="https://oscimg.oschina.net/oscnet/up-8c87facfff9cb5e0770316684a66374361f.png" width="1784" referrerpolicy="no-referrer"></p> 
<p>钉钉通知</p> 
<p> </p>
                                        </div>
                                      
</div>
            