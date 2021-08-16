
---
title: 'go-carbon 1.5.2 版本发布， 修复已知 bug 和新增功能及葡萄牙语翻译文件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2689'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 09:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2689'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm</p> 
<p style="text-align:left">目前已被 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Favelino%2Fawesome-go%23date-and-time" target="_blank">awesome-go</a> 收录，如果您觉得不错，请给个 star 吧<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> <a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li> <p>修复某些情况下parseByFormat()方法解析无效的bug</p> </li> 
 <li> <p>修复某些情况下Format()方法解析无效的bug</p> </li> 
 <li> <p>carbon结构体里的公共字段Loc、Lang改成私有字段loc和lang</p> </li> 
 <li> <p>新增SetWeekStartsAt()方法设置一周的开始日期</p> </li> 
 <li> <p>新增Timestamp()方法获取秒级时间戳，ToTimestamp()方法将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithSecond()方法获取秒级时间戳，ToTimestampWithSecond()方法将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithMillisecond()方法获取毫秒时间戳，ToTimestampWithMillisecond()方法将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithMicrosecond()方法获取微妙时间戳，ToTimestampWithMicrosecond()方法将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithNanosecond()方法获取纳秒时间戳，ToTimestampWithNanosecond()方法将在v2.0版本移除</p> </li> 
 <li> <p>新增Timestamp类型用来定义json结构体时间戳字段，ToTimestamp类型将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithSecond类型用来定义json结构体秒级时间戳字段，ToTimestampWithSecond类型将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithMillisecond类型用来定义json结构体毫秒时间戳字段，ToTimestampWithMillisecond类型将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithMicrosecond类型用来定义json结构体微妙时间戳字段，ToTimestampWithMicrosecond类型将在v2.0版本移除</p> </li> 
 <li> <p>新增TimestampWithNanosecond类型用来定义json结构体纳秒时间戳字段，ToTimestampWithNanosecond类型将在v2.0版本移除</p> </li> 
 <li> <p>新增DateTime类型用来定义json结构体日期时间字段，ToDateTimeString类型将在v2.0版本移除</p> </li> 
 <li> <p>新增Date类型用来定义json结构体日期字段，ToDateString类型将在v2.0版本移除</p> </li> 
 <li> <p>新增Time类型用来定义json结构体时间字段，ToTimeString类型将在v2.0版本移除</p> </li> 
 <li> <p>新增 .editorconfig 编辑器配置文件</p> </li> 
 <li> <p>新增葡萄牙语翻译文件lang/pt.json，由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffelipear89" target="_blank">felipear89</a> 翻译</p> </li> 
 <li> <p>按照 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fuber-go%2Fguide" target="_blank">uber-go</a> 代码规范优化代码</p> </li> 
</ul>
                                        </div>
                                      
</div>
            