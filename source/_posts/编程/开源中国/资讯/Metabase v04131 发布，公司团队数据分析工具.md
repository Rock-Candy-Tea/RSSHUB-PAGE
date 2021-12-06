
---
title: 'Metabase v0.41.3.1 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8505'
author: 开源中国
comments: false
date: Mon, 06 Dec 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8505'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Metabase 发布了 v0.41.3.1 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Bug 修复</strong></p> 
<ul> 
 <li>BigQuery 和 Google Analytics 驱动程序在 x.41.3 上损坏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19173" target="_blank">#19173</a> )</li> 
 <li>0.41.1 上的 BigQuery 连接错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18788" target="_blank">#18788</a> )</li> 
 <li> 缓慢的 Notebook 优化 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F19048" target="_blank">#19048 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F19131" target="_blank">#19131</a> ) - 部分解决<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F12378" target="_blank">#12378</a></li> 
 <li>当数据是无序的 Timeseries 时，静态可视化创建 Picaso 绘画 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19098" target="_blank">#19098</a> )</li> 
 <li>协调 Google 依赖版本，这可能会导致 GA 和新的 BigQuery 驱动程序之间发生冲突 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F19080" target="_blank">#19080</a> )</li> 
 <li>在大型实例上保存/更新问题可能需要很长时间（几秒或几分钟）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19053" target="_blank">#19053</a>）</li> 
 <li>Funnel chart 显示当聚合列中的所有行都为零时保留的 NaN% ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18980" target="_blank">#18980</a> )</li> 
 <li>将（旧）pivoted table 更改为少于 3 列会导致空白屏幕 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18976" target="_blank">#18976</a> )</li> 
 <li>当存在无效的可视化<code>column_settings</code>引用时，导出失败( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18972" target="_blank">#18972</a> )</li> 
 <li>使用非默认过滤器值时，无法在创建订阅之前发送测试电子邮件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F18669" target="_blank">#18669</a> )</li> 
 <li>Native editor 的自动完成建议使对象查找没有<code>limit</code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16736" target="_blank">#16736</a> )</li> 
 <li>从 Google 登录客户端 ID 中去除空格 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15976" target="_blank">#15976</a> )</li> 
 <li>验证 Google 登录客户端 ID ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15975" target="_blank">#15975</a> )</li> 
 <li>当“Click Behavior”链接到没有访问权限的 dashboard/question 时，Dashboard 会导致权限错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15368" target="_blank">#15368</a> )</li> 
 <li>单击本机问题中的图例会破坏 UI ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F12439" target="_blank">#12439</a> )</li> 
 <li>仪表板上的 Trend tile 与全屏上的 tile 不同 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F10786" target="_blank">#10786</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.41.3.1" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.41.3.1</a></p>
                                        </div>
                                      
</div>
            