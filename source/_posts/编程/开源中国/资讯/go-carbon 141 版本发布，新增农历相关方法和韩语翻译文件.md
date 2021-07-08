
---
title: 'go-carbon 1.4.1 版本发布，新增农历相关方法和韩语翻译文件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=972'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 10:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=972'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm。</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">如果您觉得不错，请给个 star 吧</span><br> github:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> gitee:<a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>新增韩语翻译文件kr.json</li> 
 <li>新增Lunar().Year()方法获取农历年份</li> 
 <li>新增Lunar().Month()方法获取农历月份</li> 
 <li>新增Lunar().LeapMonth()方法获取农历闰月月份</li> 
 <li>新增Lunar().Day()方法获取农历日期</li> 
 <li>新增Lunar().ToChineseYearString()方法获取农历年字符串</li> 
 <li>新增Lunar().ToChineseMonthString()方法获取农历月字符串</li> 
 <li>新增Lunar().ToChineseDayString()方法获取农历日字符串</li> 
 <li>新增Lunar().ToGanZhiYearString()方法获取干支纪年字符串</li> 
 <li>新增Lunar().ToGanZhiMonthString()方法获取干支纪月字符串</li> 
 <li>新增Lunar().ToGanZhiDayString()方法获取干支纪日字符串</li> 
 <li>新增Lunar().IsLeapYear()方法判断是否是闰年</li> 
 <li>新增Lunar().IsLeapMonth()方法判断是否是闰月</li> 
 <li>修复Tomorrow()、Yesterday()、AddMonths()方法缺少时区的bug</li> 
 <li>database.go文件拆分成database.go和json.go两个文件</li> 
</ul>
                                        </div>
                                      
</div>
            