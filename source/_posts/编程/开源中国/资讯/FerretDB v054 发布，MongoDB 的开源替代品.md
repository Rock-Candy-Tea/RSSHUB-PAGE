
---
title: 'FerretDB v0.5.4 发布，MongoDB 的开源替代品'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3331'
author: 开源中国
comments: false
date: Fri, 23 Sep 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3331'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">FerretDB（以前被称为 MangoDB）的成立是为了成为 MongoDB 的开源替代品。FerretDB 是一个开源代理，将 MongoDB wire protocol 查询转换为 SQL —— 使用 PostgreSQL 作为数据库引擎。</p> 
<p style="margin-left:0px">目前 FerretDB 已发布 0.5.0 版本，此版本带来如下改进：</p> 
<h3><strong>修复错误</strong></h3> 
<ul> 
 <li>在 Tigris 中创建集合时，添加缺失的<code>$k</code>到架构中 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1136" target="_blank">#1136</a></li> 
</ul> 
<h3><strong>文档📄</strong></h3> 
<ul> 
 <li>删除 docusaurus 引用，并通过以下方式更新文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1130" target="_blank">#1130</a></li> 
 <li>通过以下方式将文档 PR 部署到 Vercel <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1131" target="_blank">#1131</a></li> 
</ul> 
<h3><strong>其他变化🤖</strong></h3> 
<ul> 
 <li>将交易添加到<code>msg_drop</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1129" target="_blank"> #1129</a></li> 
 <li>将交易添加到<code>pg</code>'s <code>msg_listcollections </code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1135" target="_blank">#1135</a></li> 
 <li>修复 Tigris 的测试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1134" target="_blank">#1134</a></li> 
 <li>在任务目标中使用修复的 <code>-test-record</code> 目录 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1139" target="_blank">#1139</a></li> 
 <li>在更多 <code>pgdb</code> 函数中使用事务 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1143" target="_blank">#1143</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1144" target="_blank">#1144</a></li> 
 <li>升级依赖项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1158" target="_blank">#1158</a></li> 
 <li>重构<code>msg_delete</code>处理程序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1152" target="_blank">#1152</a></li> 
 <li>更新问题和 PR 模板 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F1155" target="_blank">#1155</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Freleases%2Ftag%2Fv0.5.4" target="_blank">https://github.com/FerretDB/FerretDB/releases/tag/v0.5.4</a></p>
                                        </div>
                                      
</div>
            