
---
title: 'go-carbon 1.4.4 版本发布，部分方法新增时区可选参数和新增功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8378'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 13:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8378'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">如果您觉得不错，请给个 star 吧</span><br> github:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> gitee:<a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>修复CreateFromDate()和CreateFromTime()方法缺少时区的bug</li> 
 <li>删除ToUtcString()方法，用ToString(carbon.UTC)代替</li> 
 <li>新增Format()方法对C和Q的解析，获取当前世纪数和季节数</li> 
 <li>新增IsInvalid()方法判断是否无效</li> 
 <li>新增Location()方法获取位置，如<code>PRC</code></li> 
 <li>新增Offset()方法获取获取距离UTC时区的偏移量，如<code>28800</code></li> 
 <li>新增Layout()方法输出指定布局的字符串</li> 
 <li>新增ToIso8601String()方法获取ISO8601格式字符串，如<code>2020-08-05T13:14:15+08:00</code></li> 
 <li>优化Now()、Yesterday()、Tomorrow()方法，新增可选参数timezone</li> 
 <li>优化CreaterFromXXX()系列方法，新增可选参数timezone</li> 
 <li>优化ToXXXString()系列方法，新增可选参数timezone</li> 
 <li>优化CreateFromTimestamp()方法，支持负数时间戳</li> 
 <li>优化单元测试覆盖场景，单元测试覆盖率提升到99%</li> 
 <li>将各类错误独立到errors.go文件，并修改部分错误文案</li> 
</ul>
                                        </div>
                                      
</div>
            