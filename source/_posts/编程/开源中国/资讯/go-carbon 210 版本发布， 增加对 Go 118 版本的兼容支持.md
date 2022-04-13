
---
title: 'go-carbon 2.1.0 版本发布， 增加对 Go 1.18 版本的兼容支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9424'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 09:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9424'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">目前已被 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Favelino%2Fawesome-go%23date-and-time" target="_blank">awesome-go</a> 收录，如果您觉得不错，请给个 star 吧<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> <a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>增加对 go1.18 版本的兼容支持</li> 
 <li>新增CreateFromTimestampMilli()、CreateFromTimestampMicro()、CreateFromTimestampNano()、CreateFromDateTimeMilli()、CreateFromDateTimeMicro()、CreateFromDateTimeNano()方法</li> 
 <li>新增TimestampMilli()、TimestampMicro()、TimestampNano()方法</li> 
 <li>新增DateTime()、Time()方法</li> 
 <li>新增ToDateTimeMilliString()、ToDateTimeMicroString()、ToDateTimeNanoString()、ToShortDateTimeMilliString()、ToShortDateTimeMicroString()、ToShortDateTimeNanoString()、ToRfc3339MilliString()、ToRfc3339MicroString()方法</li> 
 <li>新增SetDateTime()、SetDate()、SetTime()方法</li> 
 <li>新增TimestampMilli、TimestampMicro、TimestampNano结构体</li> 
 <li>Parse()方法增加对RFC3339、RFC3339Milli、RFC3339Micro、RFC3339Nano等格式的解析支持</li> 
 <li>精简优化代码，提取公共方法</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            