
---
title: 'go-carbon 1.5.0 版本发布， 优化功能和修复已知 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8065'
author: 开源中国
comments: false
date: Fri, 06 Aug 2021 10:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8065'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm</p> 
<p style="text-align:left">目前已被 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Favelino%2Fawesome-go%23date-and-time" target="_blank">awesome-go</a> 收录，如果您觉得不错，请给个 star 吧<br> github:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> gitee:<a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>移除SetDir()方法，语言目录不允许自定义</li> 
 <li>lunar.ToString()方法改名为lunar.ToDateString()</li> 
 <li>修复ToDayDateTimeString()输出错误的bug</li> 
 <li>修复Lunar()在其他时区输出错误的bug</li> 
 <li>优化多语言支持，无需再将lang目录复制到项目目录下</li> 
 <li>单元测试覆盖率提升到99.9%</li> 
 <li>新增SetYearNoOverflow()方法设置年份，月份不溢出</li> 
 <li>新增SetMonthNoOverflow()方法设置月份，月份不溢出</li> 
 <li>新增AddDecades()方法获取N个年代后的时间</li> 
 <li>新增AddDecadesNoOverflow()方法获取N个年代后的时间，月份不溢出</li> 
 <li>新增AddDecade()方法获取1个年代后的时间</li> 
 <li>新增AddDecadeNoOverflow()方法获取1个年代后的时间，月份不溢出</li> 
 <li>新增SubDecades()方法获取N个年代前的时间</li> 
 <li>新增SubDecadesNoOverflow()方法获取N个年代前的时间，月份不溢出</li> 
 <li>新增SubDecade()方法获取1个年代前的时间</li> 
 <li>新增SubDecadeNoOverflow()方法获取1个年代前的时间，月份不溢出</li> 
 <li>新增日文说明文件readme.jp.md</li> 
 <li>新增德语翻译文件lang/de.json，由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbenzammour" target="_blank">benzammour</a> 翻译</li> 
</ul>
                                        </div>
                                      
</div>
            