
---
title: 'Metabase v0.41.5 发布，更新 Log4j 至 2.16.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9270'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9270'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Metabase 是一个开源的团队数据分析工具，提供<span style="color:#24292f">简单快捷的</span>商业智能和分析功能，<span style="color:#000000">无论是配置还是使用都非常轻松</span>，让团队的每位成员都能轻松看懂数据细节并参与其中。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Metabase 更新到 0.41.5 版本，主要将 Log4j 更新至 2.16.0 版本，顺带修复一些 Bug，完整更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Bug 修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将 Log4j 升级到 2.16.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19371" target="_blank">#19371</a>)</li> 
 <li>XLSX 导出不尊重“分隔符样式”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19006" target="_blank"><u>#19006</u></a>）</li> 
 <li>完成初始设置，就无法更改任何 LDAP 设置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18936" target="_blank">#18936</a>)</li> 
 <li>自定义表达式<span> </span><code>case</code><span> </span>在嵌套查询时使用错误的字段引用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17512" target="_blank">#17512</a>)</li> 
 <li>同上，<span style="color:#24292f"><code>coalesce</code><span> </span>也存在错误字段问题 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18513" target="_blank">#18513</a><span style="color:#24292f">)</span></li> 
 <li>当单击到没有访问权限的仪表板链接时，会导致权限错误问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15368" target="_blank">#15368</a>)</li> 
 <li>站点 URL 验证过于严格，不接受下划线 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F14491" target="_blank">#14491</a>)</li> 
 <li>反向代理在重置电子邮件时，应在电子邮件正文中使用站点 URL ，而不是 localhost (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F14028" target="_blank">#14028</a>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.41.5" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.41.5</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            