
---
title: 'go-carbon 2.1.4 版本发布， 轻量级、语义化、对开发者友好的Golang时间处理库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8474'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 09:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8474'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">目前已被 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Favelino%2Fawesome-go%23date-and-time" target="_blank">awesome-go</a> 收录，如果您觉得不错，请给个 star 吧<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> <a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新日志</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><code>carbon.go</code>文件 文件新增 Version 版本号常量</li> 
 <li><code>carbon.go</code>文件 新增 Sydney、Melbourne和Darwin 时区常量</li> 
 <li><code>getter.go</code>文件 新增 TimeMilli(),TimeMicro(),TimeNano() 方法</li> 
 <li><code>comparer.go</code>文件 新增IsValid()方法</li> 
 <li><code>calendar.lunar.go</code>文件 新增DoubleHour()、IsXXXDoubleHour() 方法，由<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdmzlingyin">dmzlingyin</a><span> </span>贡献</li> 
 <li><code>calendar.lunar.go</code>文件 新增DateTime()、Date() 和 Time() 方法</li> 
 <li><code>calendar.lunar.go</code>文件 优化ToDayString()逻辑，精简不必要的变量 chineseDayPrefixes</li> 
 <li><code>carbon.go</code>文件 XXXFormat 常量 改名为 XXXLayout</li> 
 <li>精简优化代码</li> 
 <li>完善文档</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            