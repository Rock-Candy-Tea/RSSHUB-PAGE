
---
title: 'Metabase v0.41.1 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=737'
author: 开源中国
comments: false
date: Sat, 23 Oct 2021 08:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=737'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Metabase 发布了 v0.41.1 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>Enhancements</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>导出中列排序的更好方法 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18450" target="_blank">#18450</a> )</li> 
 <li>修复 Postgres 极限语义的错误问题的工具（错误表的空白显示）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F18432" target="_blank">#18432</a>）</li> 
 <li><code>MB_DB_CONNECTION_TIMEOUT_MS</code>默认提高到 10000 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18354" target="_blank">#18354</a> )</li> 
 <li>允许缓存字体和图像 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F18239" target="_blank">#18239</a> )</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Bug 修复</strong></p> 
<ul> 
 <li>在进行 FullApp 嵌入时，并非所有端点都被调用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18552" target="_blank">#18552</a>）</li> 
 <li>由于格式限制， XLSX 的大列导出失败 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18531" target="_blank">#18531</a> )</li> 
 <li>0.41.0 上的缓存会缓存很长时间的结果（不考虑定义的设置）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18458" target="_blank">#18458</a>）</li> 
 <li>导出大量数据可能导致 OutOfMemory ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18455" target="_blank">#18455</a> )</li> 
 <li>图表说明（表格除外）未显示在仪表板中 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18454" target="_blank">#18454</a> )</li> 
 <li>重新映射（显示值）列在下载中被删除 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18440" target="_blank">#18440</a> )</li> 
 <li>通过 drill-through 操作菜单过滤空列会导致空白屏幕 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18386" target="_blank">#18386</a> )</li> 
 <li>如果数据库中有任何隐藏表，数据模型显示空白页 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18384" target="_blank">#18384</a> )</li> 
 <li>当 <span style="background-color:#ffffff; color:#24292f">viz </span>设置使用较旧的字段维度时，导出的列丢失 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18382" target="_blank">#18382</a> )</li> 
 <li>带有四舍五入浮点数的脉冲在 0.41.0 中呈现一个悬挂小数点 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18363" target="_blank">#18363</a> )</li> 
 <li>具有两列（字符串、整数）的 Pulse/Subscription table cards 无法呈现（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18352" target="_blank">#18352</a>）</li> 
 <li>[Add Database > Presto] 多个 JDBC 字段选项 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18351" target="_blank">#18351</a> )</li> 
 <li>无法从字段过滤器的不同 schema 中选择字段 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18349" target="_blank">#18349</a> )</li> 
 <li>在电子邮件订阅中，显示原始问题标题而不是策划标题 (v41) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18344" target="_blank">#18344</a> )</li> 
 <li>Audit > Questions > Total runtime 显示链接而不是实际时间 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18317" target="_blank">#18317</a> )</li> 
 <li>key type=ssh-rsa 的 KeyExchange 签名验证失败 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18316" target="_blank">#18316</a> )</li> 
 <li>当整数值非常高时，导出到 XLSX 可能会失败 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18310" target="_blank">#18310</a> )</li> 
 <li>Questions -> 审计功能中的所有问题按空值排序 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18271" target="_blank">#18271</a> )</li> 
 <li>Dashboard Subscription 测试电子邮件按钮不显示错误消息 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18235" target="_blank">#18235</a> )</li> 
 <li>如果查询失败，EE Audit 应用程序前端不会显示错误消息 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18124" target="_blank">#18124</a> )</li> 
 <li>Dashboard Textbox 不呈现链接，除非使用 Markdown ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18114" target="_blank">#18114</a> )</li> 
 <li>仅包含空位置结果的 Pin 图导致前端不断重新加载或空白页面 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18061" target="_blank">#18061</a> )</li> 
 <li>X-Rays：表字段在标题中显示为“null”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15737" target="_blank">#15737</a>）</li> 
 <li>与表列同名的自定义列在分组时返回不正确的结果 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F14255" target="_blank">#14255</a> )</li> 
 <li>将数据系列添加到仪表板小部件会滞后，然后有时会挂起 UI ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F13100" target="_blank">#13100</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.41.1" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.41.1</a></p>
                                        </div>
                                      
</div>
            