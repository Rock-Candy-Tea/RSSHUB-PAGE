
---
title: 'bootx-platform v1.1.0-bate4-fix：认证流程优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5c9f02bd0ef2cb14269ef7594c8f51b866e.png'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 11:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5c9f02bd0ef2cb14269ef7594c8f51b866e.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址：<a href="https://gitee.com/bootx/bootx-platform">https://gitee.com/bootx/bootx-platform</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">基于 Spring Boot 框架打造，针对单体式应用进行专门设计，提供整套服务模块，努力为打造全方位企业级开发解决方案， 致力将开源版打造成超越商业版后台管理框架的项目。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>特色功能</span></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span>针对敏感信息，可以通过注解配置实现返回时自动脱敏</span></li> 
 <li><span>针对重要信息，可以通过添加注解，实现在数据库中保密存储，配合数据脱敏使用可以更好的保护系统数据的安全</span></li> 
 <li><span>支持多种范围的数据权限控制，如只能查看自己、只能查询指定部门、用户、可以查询全部的数据等等</span></li> 
 <li><span>支持嵌套查询的超级查询构造器，自动生成对应条件 SQL 语句</span></li> 
 <li><span>异常时返回链路追踪 id，方便错误日志追踪</span></li> 
 <li><span>提供项目对应的代码生成器，方便开发</span></li> 
 <li><span>定制 Mybatis Plus 组件，更方便开发</span></li> 
 <li><span>支持多种消息中间件，MQTT、RabbitMQ、Redis</span></li> 
 <li><span>支持全局级 Websocket 集成，通过事件机制可以分发到指定页面</span></li> 
 <li>支持通过 ELK 和轻量级 PlumeLog 来管理项目日志，以适应不同的场景</li> 
 <li>提供移动端开发脚手架，方便开发 H5 与各种小程序</li> 
 <li> <p style="margin-left:0; margin-right:0">支持通过微信、钉钉、企业微信等第三方开放平台进行扫码登录</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">本次功能更新</h2> 
<p>bate4版本发布后发现认证终端这块设计有问题，秉持着有问题早解决的想法，把这一块进行了重构，同时修正了一些其他与登录认证相关的问题，特此发个版本</p> 
<ul> 
 <li>重构认证应用和认证终端重新设计为认证终端和登录方式</li> 
 <li>增加用户手机号/邮箱绑定功能</li> 
 <li>优化微信、钉钉、企业微信绑定时重复校验</li> 
 <li>优化<code>@IgnoreAuth</code>鉴权注解功能</li> 
 <li>fix: 开放平台登录报错问题</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">新功能截图</h2> 
<p><img height="1952" src="https://oscimg.oschina.net/oscnet/up-5c9f02bd0ef2cb14269ef7594c8f51b866e.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>新认证终端</p> 
<p><img height="1952" src="https://oscimg.oschina.net/oscnet/up-fa0447a0279bae96f65b135d461a38d6e2f.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>新登录方式</p> 
<p><img height="1952" src="https://oscimg.oschina.net/oscnet/up-eda2b837b46a83fc1f3b414217480e080f8.png" width="3840" referrerpolicy="no-referrer"></p> 
<p>手机号/邮箱绑定</p> 
<p> </p>
                                        </div>
                                      
</div>
            