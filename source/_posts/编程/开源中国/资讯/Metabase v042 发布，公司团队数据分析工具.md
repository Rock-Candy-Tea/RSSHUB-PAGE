
---
title: 'Metabase v0.42 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-586a15c3225959cbe1b87b21ba54d2dbd80.gif'
author: 开源中国
comments: false
date: Thu, 10 Feb 2022 07:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-586a15c3225959cbe1b87b21ba54d2dbd80.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Metabase v0.42 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.metabase.com%2Fblog%2FMetabase-0.42%2Findex.html" target="_blank">发布</a>，此版本</span><span style="background-color:#ffffff; color:#24292f">引入了 Models，并附带了许多改进、润色和错误修复。</span><span style="background-color:#ffffff; color:#000000">Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</span></p> 
<p><span style="background-color:#ffffff; color:#000000"><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-586a15c3225959cbe1b87b21ba54d2dbd80.gif" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="background-color:#ffffff; color:#000000">具体更新内容如下：</span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>Enhancements</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>时间选择器 AM 和 PM 颜色无法明显区分（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20010" target="_blank">#20010</a>）</li> 
 <li>警报停止的电子邮件没有帮助 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19814" target="_blank">#19814</a> )</li> 
 <li>在配置期间清理数据库指南可用性 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19641" target="_blank">#19641</a> )</li> 
 <li>清理我们如何显示已弃用的数据库驱动 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19529" target="_blank">#19529</a> )</li> 
 <li>添加从登录页面返回上一页的方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19476" target="_blank">#19476</a>）</li> 
 <li>整合第一个 db 同步模式和 X-ray 选择 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19440" target="_blank">#19440</a> )</li> 
 <li>将 Slack 实现从 Bot 迁移到 App ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19435" target="_blank">#19435</a> )</li> 
 <li>改进 Filters for 42（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19354" target="_blank">#19354</a>）</li> 
 <li>清理设置导航 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19348" target="_blank">#19348</a> )</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><strong>Bug 修复</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>Waterfall static viz 的默认设置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20332" target="_blank">#20332</a> )</li> 
 <li>People X-ray 中的“By coordinates”图显示了一个无意义的 pin map ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20182" target="_blank">#20182</a> )</li> 
 <li>pin map 上未显示 pins ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20090" target="_blank">#20090</a> )</li> 
 <li>为无数据用户显示的“Explore results”，点击后出现空白屏幕 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20044" target="_blank">#20044</a> )</li> 
 <li>使用无数据用户访问模型时出现空白屏幕 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20042" target="_blank">#20042</a> )</li> 
 <li>重新访问数据库编辑页面时不保留秘密连接属性文件路径（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20030" target="_blank">#20030</a>）</li> 
 <li>如果令牌过期，许可页面将进入重新加载循环 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20020" target="_blank">#20020</a> )</li> 
 <li>搜索结果中缺少描述 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F20018" target="_blank">#20018</a> )</li> 
 <li>固定表格的水平滚动不适用于 Firefox ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19997" target="_blank">#19997</a> )</li> 
 <li>colum header 上的 Metadata 工具提示弹出，导致数据表重置为全为 NULL 的数字列 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19976" target="_blank">#19976</a> )</li> 
 <li>某些可视化设置可能会导致导出时出现空列/缺失列 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19889" target="_blank">#19889</a> )</li> 
 <li>Postgres 在 date_trunc() 中不必要地将 timestamptz 和 date 列转换为 timestamp ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19816" target="_blank">#19816</a> )</li> 
 <li>导出时忽略了 v0.41.6 中的列排序回归 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19796" target="_blank">#19796</a> )</li> 
 <li>在<code>sql.qp/-&gt;honeysql</code>方法中过早调用<code>to-sql</code> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19753" target="_blank">#19753</a> )</li> 
 <li>更改返回的字段时，可视化“auto-viz”不保留现有设置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19747" target="_blank">#19747</a> )</li> 
 <li>如果值不在字段过滤器下拉列表中，则无法添加过滤器 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19685" target="_blank">#19685</a> )</li> 
 <li>defsetting :tag metadata 应该在 arglists 本身，而不是 var ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19627" target="_blank">#19627</a> )</li> 
 <li>SQLite/Redshift/SQL Server/MySQL 查询不能正确处理具有相同名称但大小写不同的多个列别名 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19618" target="_blank">#19618</a> )</li> 
 <li>归档的子集合仍在权限中显示 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19603" target="_blank">#19603</a> )</li> 
 <li>XLSX 导出会留下临时文件，这可能会阻止实例工作 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F19480" target="_blank">#19480</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.42.0" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.42.0</a></p>
                                        </div>
                                      
</div>
            