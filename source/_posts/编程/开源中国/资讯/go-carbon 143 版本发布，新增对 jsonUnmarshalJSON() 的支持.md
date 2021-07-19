
---
title: 'go-carbon 1.4.3 版本发布，新增对 json.UnmarshalJSON() 的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=410'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 10:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=410'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">carbon 是一个轻量级、语义化、对开发者友好的Golang时间处理库，支持链式调用、农历和gorm、xorm等主流orm。</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">如果您觉得不错，请给个 star 吧</span><br> github:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang-module%2Fcarbon" target="_blank">github.com/golang-module/carbon</a><br> gitee:<a href="https://gitee.com/go-package/carbon">gitee.com/go-package/carbon</a></p> 
<p style="text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>优化IsZero()方法的判断逻辑</li> 
 <li>修复Microsecond()方法获取毫秒数错误的bug</li> 
 <li>修复SetMicrosecond()方法设置毫秒数错误的bug</li> 
 <li>修复Lunar().Festival()方法不是任何节气时panic的bug</li> 
 <li>修复Format()方法无法原样解析的bug, 如carbon.Parse("2020-08-05 13:14:15").Format("\I\t \i\s Y-m-d H:i:s")</li> 
 <li>修复ParseByFormat()方法无法原样解析的bug，如carbon.ParseByFormat("It is 2020-08-05 13:14:15", "\I\t \i\s Y-m-d H:i:s")</li> 
 <li>使用github.com/stretchr/testify/assert库替代原生testing库</li> 
 <li>增加单元测试覆盖场景，单元测试覆盖率提升到96%</li> 
 <li>统一错误格式，修改部分错误文案</li> 
 <li>Lunar()方法实现Stringer接口，可以直接作为字符串输出农历年月日，同Lunar().ToString()</li> 
 <li>新增CreateFromTimestamp()方法对时间戳是0的判断</li> 
 <li>新增Lunar().ToString()方法获取农历年月日，如二零二零年六月十六</li> 
 <li>新增对json.UnmarshalJSON()的支持</li> 
</ul>
                                        </div>
                                      
</div>
            