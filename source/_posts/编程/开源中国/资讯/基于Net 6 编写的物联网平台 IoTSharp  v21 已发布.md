
---
title: '基于.Net 6 编写的物联网平台 IoTSharp  v2.1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9668'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 21:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9668'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">IoTSharp 经过2021年的发展， 我们终于有了前端部分， 已经初具生产使用能力， 从规则链、数据清洗脚本支持等等， 设备控制、事件等皆有了完善和支持。 2021年11月是个不平凡的月份。 使得项目有了快速的成长。 于此同时我们也收到了首次捐赠. 同时我们也终于升级到了.Net 6.0 , 由于我们依赖的库实在太多， 推动依赖库更新升级是一个艰巨的任务。 </p> 
<p style="text-align:start"><strong>更新内容如下</strong></p> 
<ul> 
 <li> <p>升级到了 .Net 6.0  </p> </li> 
 <li> <p>调整 rpc 接口和通过网关控制子设备</p> </li> 
 <li> <p>增加挂载点 rpc , 上线， 下线， 可以在挂载点处挂载规则链。</p> </li> 
 <li> <p>增加Mysql迁移文件</p> </li> 
 <li> <p>修改docker镜像名字为 maikebing/iotsharp ，因为 iotsharp/iotsharp 需要单独缴费。</p> </li> 
 <li> <p>解决单例注入后，DbConext不能用于多线程问题 by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flable" target="_blank">@lable</a><span> </span>in<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIoTSharp%2FIoTSharp%2Fpull%2F538" target="_blank">#538</a></p> </li> 
 <li> <p>修复pgsql迁移设计 by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flable" target="_blank">@lable</a><span> </span>in<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIoTSharp%2FIoTSharp%2Fpull%2F539" target="_blank">#539</a></p> </li> 
 <li> <p>修正IPV6特殊处理 ::1 by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flable" target="_blank">@lable</a><span> </span>in<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIoTSharp%2FIoTSharp%2Fpull%2F541" target="_blank">#541</a></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            