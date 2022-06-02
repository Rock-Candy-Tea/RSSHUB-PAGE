
---
title: '国产开源物联网平台 IoTSharp v2.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1277'
author: 开源中国
comments: false
date: Thu, 02 Jun 2022 13:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1277'
---

<div>   
<div class="content">
                                                                                            <p>IoTSharp 是一个 基于.Net 6 的开源物联网平台， 支持 HTTP、MQTT 、CoAp 协议， 支持系统将遥测数据存储在TDengine 、 InfluxDB、 TimescaleDB等流行的时序数据库， 支持相将关系型<span style="background-color:#ffffff; color:#24292f">数据存储在PostgreSql、MySql、Oracle、SQLServer、Sqlite等。 支持基于数据流处理的规则链，你可以使用JS、Python、C#、SQL、等脚本或者.Net 程序集任务块来处理数据，使用规则链中的表达式处理数据走向，包括数据清洗、数据推送、事件告警等。 </span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIoTSharp%2FIoTSharp%2Fcommit%2F8d5df6b4e9d86c7bd749a8b29f93bd3ae5529700" target="_blank">升级新的mqttnet4.0 版本</a></li> 
 <li>遥测、属性时间刷新;时间轴显示 by<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiioter" target="_blank">@iioter</a><span> </span>in<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIoTSharp%2FIoTSharp%2Fpull%2F691" target="_blank">#691</a></li> 
 <li>调整所有数据库EF初始化结构信息。</li> 
 <li>增加了在线文档。</li> 
 <li>增加了XML和Json根据网关配置进行解析的数据网关RawDataGateway ， Mqtt和Http协议均有效</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIoTSharp%2FIoTSharp%2Fcommit%2F604fd5616f69d0d92870a83bb452da5f1e5b38aa" target="_blank">滑动验证码，国际化资源文件</a></li> 
 <li>增加了gateway 批量上传设备遥测的topic，也兼容了ThingsBoard 的格式。</li> 
 <li>优化了规则链中C#脚本第一次编译后期使用缓存编译， 使得速度更快。</li> 
 <li>增加了挂载类型，上线、离线等。</li> 
 <li>增加了告警接口和查询页面</li> 
 <li>增加了资产功能， 可以把多个设备组装成一个资产， 形同于一个设备。</li> 
 <li>遥测数据中增加了 数据断面和滤波取值等。 UI中增加了遥测数据展示图表等功能。</li> 
 <li>使用了.Net 6.0的 SPA方式， 加速启动项目。</li> 
 <li>调整了设备详情显示方式。</li> 
 <li>修正了pengxiwei 提出的涛思时序中的bug问题</li> 
 <li>优化处理了动态对象问题</li> 
 <li>将项目文档合并到docs目录中</li> 
 <li>告警的传播处理</li> 
 <li>规则级联删除，设计器自定义工具</li> 
 <li>修正了sdk的编译错误。</li> 
</ul> 
<p>国内:  https://gitee.com/iotsharp</p> 
<p>国外地址: https://github.com/IoTSharp</p>
                                        </div>
                                      
</div>
            