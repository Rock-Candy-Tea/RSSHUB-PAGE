
---
title: 'Metabase 0.42.1 发布，团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8506'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8506'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Metabase 是一个开源的团队数据分析工具，提供<span style="color:#24292f">简单快捷的</span>商业智能和分析功能，<span style="color:#000000">无论是配置还是使用都非常轻松</span>，让团队的每位成员都能轻松看懂数据细节并参与其中。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Metabase 更新到 0.42.1 版本，主要修复了已知的 Bug 。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>增强功能</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>删除 aleph 上未使用的 dep（以及 Netty 上未使用的临时 dep）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F20342" target="_blank">#20342</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Bug 修复</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">过滤下拉菜单只允许过滤“以…开始”</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20551" target="_blank">#20551</a>）</li> 
 <li>无法过滤仪表板中的订阅电子邮件的仪表板 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20516" target="_blank">#20516</a><span> </span>)</li> 
 <li>具有默认值的仪表板过滤器，如果删除值则不起作用，导致查询失败（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20493" target="_blank">#20493</a>）</li> 
 <li>脉冲问题警报 Slack 发送裁剪图像 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20444" target="_blank">#20444</a><span> </span>)</li> 
 <li>无法删除 Google 登录设置 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20442" target="_blank">#20442</a><span> </span>)</li> 
 <li>选择单个选项时，嵌入仪表板字段筛选器无法工作 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20438" target="_blank">#20438</a><span> </span>)</li> 
 <li>自定义表达式 - Count 需要括号，但之后会自动删除 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20420" target="_blank">#20420</a><span> </span>)</li> 
 <li>在某些情况下无法打开模型侧边栏 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20414" target="_blank">#20414</a><span> </span>)</li> 
 <li>BigQuery 不正确的别名，可能导致查询失败 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20413" target="_blank">#20413</a><span> </span>)</li> 
 <li>过滤嵌套问题会导致公共和嵌入错误 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20393" target="_blank">#20393</a><span> </span>)</li> 
 <li>具有不明确列的 BigQuery 嵌套查询导致错误 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20362" target="_blank">#20362</a><span> </span>)</li> 
 <li>无法在嵌入中将过滤器设置为“锁定”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20357" target="_blank">#20357</a>）</li> 
 <li>当别名（自动生成或其他）包含双引号或空字符时，Oracle 查询不起作用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20307" target="_blank">#20307</a>）</li> 
 <li>当无数据用户查看嵌套问题时，所有编辑选项都会显示（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18978" target="_blank">#18978</a>）</li> 
 <li>当无数据用户查看嵌套问题时，会出现“提问”和“浏览数据”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18977" target="_blank">#18977</a>）</li> 
 <li>Oracle 对具有长显示名称的表的连接查询失败 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15978" target="_blank">#15978</a><span> </span>)</li> 
 <li>数据透视表：无法更改用于“值”的字段名称 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15353" target="_blank">#15353</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.42.1" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.42.1</a></p>
                                        </div>
                                      
</div>
            