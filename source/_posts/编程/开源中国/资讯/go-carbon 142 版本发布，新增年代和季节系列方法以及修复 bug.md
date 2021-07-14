
---
title: 'go-carbon 1.4.2 版本发布，新增年代和季节系列方法以及修复 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4279'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 09:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4279'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm。</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">如果您觉得不错，请给个 star 吧</span><br> github:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> gitee:<a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>Lunar().ToChineseYearString()方法更改为Lunar().ToYearString()</li> 
 <li>Lunar().ToChineseMonthString()方法更改为Lunar().ToMonthString()</li> 
 <li>Lunar().ToChineseDayString()方法更改为Lunar().ToDayString()</li> 
 <li>New()方法更改为NewCarbon()，以避免New()和Now()相似而混淆</li> 
 <li>优化CreaterFromXXX系列方法对默认纳秒的处理，将默认纳秒设为当前纳秒</li> 
 <li>增加单元测试覆盖场景</li> 
 <li>增加对无效时间的判断</li> 
 <li>新增Decade()方法获取当前年代</li> 
 <li>新增StartOfDecade()方法获取当前年代的开始时间</li> 
 <li>新增EndOfDecade()方法获取当前年代的结束时间</li> 
 <li>新增Season()方法获取当前季节，支持i18n</li> 
 <li>新增StartOfSeason()方法获取当前季节的开始时间</li> 
 <li>新增EndOfSeason()方法获取当前季节结束时间</li> 
 <li>新增IsSpring()方法判断是否是春季</li> 
 <li>新增IsSummer()方法判断是否是夏季</li> 
 <li>新增IsAutumn()方法判断是否是秋季</li> 
 <li>新增IsWinter()方法判断是否是冬季</li> 
</ul>
                                        </div>
                                      
</div>
            