
---
title: 'Grafana 8.5 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3767'
author: 开源中国
comments: false
date: Sun, 24 Apr 2022 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3767'
---

<div>   
<div class="content">
                                                                                            <p>Grafana 是一个用于监控和可观察性的开源平台，可视化来自 Prometheus、Loki、Elasticsearch、InfluxDB、Postgres 等多个来源的指标、日志等。</p> 
<p>Grafana 8.5 正式发布，更新内容如下：</p> 
<h3><strong>重大变化</strong></h3> 
<p>对于代理的请求，例如 Grafana 的数据源或插件代理：</p> 
<ul> 
 <li>如果请求被取消，例如从浏览器/客户端，HTTP 状态代码现在是 <code>499 Client closed request</code>，而不是 <code>502 Bad gateway</code></li> 
 <li>如果请求超时，例如超过允许的时间，HTTP 状态代码现在是 <code>504 Gateway timeout</code>，而不是 <code>502 Bad gateway</code></li> 
</ul> 
<h3>弃用</h3> 
<ul> 
 <li><code>/api/tsdb/query</code>API 已被弃用，并将在未来的版本中删除。请使用 <code>/api/ds/query</code> 代替。</li> 
</ul> 
<h3>功能和改进</h3> 
<ul> 
 <li><strong>Instrumentation:</strong> 代理状态代码更正和各种改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47473" target="_blank">#47473</a></li> 
 <li><strong>NewsPanel:</strong> 添加对 Atom feeds 的支持. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45390" target="_blank">#45390</a></li> 
 <li><strong>Prometheus:</strong> 默认启用新的可视化查询构建器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46634" target="_blank">#46634</a></li> 
 <li><strong>SAML:</strong> 允许禁用 SAML 注册</li> 
 <li><strong>TablePanel:</strong> 添加单元格检查选项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45620" target="_blank">#45620</a></li> 
 <li><strong>Tempo:</strong> 单独跟踪日志和 loki 搜索数据源配置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46655" target="_blank">#46655</a></li> 
 <li><strong>Transformations:</strong> 支持键值对解析中的转义字符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47901" target="_blank">#47901</a></li> 
</ul> 
<h3>Bug 修复</h3> 
<ul> 
 <li><strong>Azure Monitor:</strong> 针对模板变量的不正确变量级联的错误修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47478" target="_blank">#47478</a></li> 
 <li><strong>CloudWatch:</strong> 在 SQL 自动完成中正确列出所有指标 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45898" target="_blank">#45898</a></li> 
 <li><strong>CloudWatch:</strong> 在日志查询字段中运行模糊查询 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47454" target="_blank">#47454</a></li> 
 <li><strong>Postgres:</strong> 返回带有连字符方案的表 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45754" target="_blank">#45754</a></li> 
 <li><strong>Variables:</strong> 确保查询参数中的变量被正确识别 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47049" target="_blank">#47049</a></li> 
 <li><strong>Variables:</strong> 修正改变查询变量数据源时的崩溃 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44957" target="_blank">#44957</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases" target="_blank">https://github.com/grafana/grafana/releases</a></p>
                                        </div>
                                      
</div>
            