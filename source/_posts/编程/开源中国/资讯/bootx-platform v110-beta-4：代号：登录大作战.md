
---
title: 'bootx-platform v1.1.0-beta-4：代号：登录大作战'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3cc781820c9799569889d7c256a24d19a67.png'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 09:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3cc781820c9799569889d7c256a24d19a67.png'
---

<div>   
<div class="content">
                                                                                            <h2>项目介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">项目地址：<a href="https://gitee.com/bootx/bootx-platform">https://gitee.com/bootx/bootx-platform</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">基于 Spring Boot 框架打造，针对单体式应用进行专门设计，提供整套服务模块，努力为打造全方位企业级开发解决方案， 致力将开源版打造成超越商业版后台管理框架的项目。</p> 
<h2><span>特色功能</span></h2> 
<ul> 
 <li><span>针对敏感信息，可以通过注解配置实现返回时自动脱敏</span></li> 
 <li><span>针对重要信息，可以通过添加注解，实现在数据库中保密存储，配合数据脱敏使用可以更好的保护系统数据的安全</span></li> 
 <li><span>支持多种范围的数据权限控制，如只能查看自己、只能查询指定部门、用户、可以查询全部的数据等等</span></li> 
 <li><span>支持嵌套查询的超级查询构造器，自动生成对应条件 SQL 语句</span></li> 
 <li><span>异常时返回链路追踪 id，方便错误日志追踪</span></li> 
 <li><span>提供项目对应的代码生成器，方便开发</span></li> 
 <li><span>定制 Mybatis Plus 组件，更方便开发</span></li> 
 <li><span>支持多种消息中间件，MQTT、RabbitMQ、Redis</span></li> 
 <li><span>支持全局级 Websocket 集成，通过事件机制可以分发到指定页面</span></li> 
 <li>支持通过ELK和轻量级PlumeLog来管理项目日志,以适应不同的场景</li> 
 <li>提供移动端开发脚手架，方便开发H5与各种小程序</li> 
 <li> <p>支持通过微信、钉钉、企业微信等第三方开放平台进行扫码登录</p> </li> 
</ul> 
<h2><span>更新预报</span></h2> 
<p>1.1.0-beta5（七月中旬）：支付宝和微信的支付权限成功申请下来了，完善支付模块，主要是微信支付方面，升级成V3版本API</p> 
<p>1.1.0-bate6（七月下旬）：微信服务号消息通知、钉钉消息通知、短信消息通知等通知相关功能实现</p> 
<h2>本次功能更新</h2> 
<ul> 
 <li>增加忘记密码功能</li> 
 <li>增加账号注册功能</li> 
 <li>增加微信扫码登录和绑定</li> 
 <li>增加企业扫码微信登录和绑定</li> 
 <li>增加钉钉扫码登录和绑定</li> 
 <li>优化终端拆分为认证应用和认证终端</li> 
 <li>优化登录界面和逻辑</li> 
 <li>优化密码设置时提示安全等级</li> 
 <li>优化文件上传管理功能</li> 
 <li>fix: 部分字段在MySQL高版本编程关键字</li> 
 <li>fix: 支付宝WAP支付无法发起错误</li> 
 <li>fix: 队列生成器跨区间生成检查问题修复</li> 
</ul> 
<h2>新功能截图</h2> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-3cc781820c9799569889d7c256a24d19a67.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>第三方开放平台账号绑定</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-e38be2a55e3ddc1b42a2288d7d5c482db9c.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>登录方式和界面优化</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-49ca749809e414682ccbd1c477b8112b0d1.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>钉钉扫码登录</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-fa5a3c22461e1bf33948d1d2a215e13723c.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>企业微信扫码登录</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-bf8299a45de0f7141b6af15ba280052b455.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>密码重置</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-8e856527f67423ec9f2bdd331dfdcbd515e.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>账号注册</p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-ebfe5256cd05295c1a1d81533f124164e51.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><img height="1391" src="https://oscimg.oschina.net/oscnet/up-8e7660ceb200f728fc43146307c209d14ce.png" width="2560" referrerpolicy="no-referrer"></p> 
<p>终端管理拆分为认证管理</p> 
<p> </p>
                                        </div>
                                      
</div>
            