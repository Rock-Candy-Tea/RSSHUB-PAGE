
---
title: 'go-carbon 2.0.0 版本发布， 要求最低 golang 版本 1.16'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9858'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 10:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9858'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm</p> 
<p style="text-align:left">目前已被 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Favelino%2Fawesome-go%23date-and-time" target="_blank">awesome-go</a> 收录，如果您觉得不错，请给个 star 吧<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> <a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li> <p>对 <code>go</code> 版本最低要求升级到1.16，利用 <code>embed</code> 特性，无需再将lang语言目录复制到当前项目下</p> </li> 
 <li> <p>Carbon结构体里的公共字段Time改成私有字段time</p> </li> 
 <li> <p>移除ToTimestamp()方法，只保留Timestamp()方法</p> </li> 
 <li> <p>移除ToTimestampWithSecond()方法，只保留TimestampWithSecond()方法</p> </li> 
 <li> <p>移除ToTimestampWithMillisecond()方法，只保留TimestampWithMillisecond()方法</p> </li> 
 <li> <p>移除ToTimestampWithMicrosecond()方法，只保留TimestampWithMicrosecond()方法</p> </li> 
 <li> <p>移除ToTimestampWithNanosecond()方法，只保留TimestampWithNanosecond()方法</p> </li> 
 <li> <p>移除ToTimestamp结构体，只保留Timestamp结构体</p> </li> 
 <li> <p>移除ToTimestampWithSecond结构体，只保留TimestampWithSecond结构体</p> </li> 
 <li> <p>移除ToTimestampWithMillisecond结构体，只保留TimestampWithMillisecond结构体</p> </li> 
 <li> <p>移除ToTimestampWithMicrosecond结构体，只保留TimestampWithMicrosecond结构体</p> </li> 
 <li> <p>移除ToTimestampWithNanosecond结构体，只保留ToTimestampWithNanosecond结构体</p> </li> 
 <li> <p>移除ToDateTimeString结构体，只保留DateTime结构体</p> </li> 
 <li> <p>移除ToDateTimeString结构体，只保留Date结构体</p> </li> 
 <li> <p>移除ToTimeString结构体，只保留Time结构体</p> </li> 
</ul>
                                        </div>
                                      
</div>
            