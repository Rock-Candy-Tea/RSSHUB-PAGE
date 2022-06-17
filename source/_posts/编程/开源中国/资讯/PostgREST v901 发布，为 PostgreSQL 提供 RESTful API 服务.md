
---
title: 'PostgREST v9.0.1 发布，为 PostgreSQL 提供 RESTful API 服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4166'
author: 开源中国
comments: false
date: Fri, 17 Jun 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4166'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PostgREST v9.0.1 现已发布。<span style="color:#333333">PostgREST 可以方便的为任何 </span>PostgreSQL<span style="color:#333333"> 数据库提供完全的 RESTful API 服务，采用 </span>Haskell<span style="color:#333333"> 语言开发。</span></p> 
<p><span style="color:#333333">具体更新内容如下：</span></p> 
<p><strong>Fixed</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2165" target="_blank">#2165</a>，修复 OpenAPI 规范中 json/jsonb 列不应该有的类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2020" target="_blank">#2020</a> , 使用<code>Prefer: tx=rollback</code>时执行延迟约束触发器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2077" target="_blank">#2077</a>，修复对 NULL、TrUe、FaLsE 等大写或混合大小写值的不适应</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2024" target="_blank">#2024</a>，当视图中存在 XMLTABLE 和 DEFAULT 时，修复模式缓存加载</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fpull%2F1724" target="_blank">#1724</a>，修复错误的 CORS header Authentication -> Authorization</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2120" target="_blank">#2120</a>，修复当<code>=</code>存在于值中时正确读取数据库配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fpull%2F2135" target="_blank">#2135</a>，从模式缓存和 OpenAPI output 中删除 trigger functions，因为它们无论如何都不能直接调用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2101" target="_blank">#2101</a>，从模式缓存和 OpenAPI output 中删除 aggregates、procedures 和 window functions</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fpull%2F2153" target="_blank">#2153</a>，修复 --dump-schema 在错误的 PG 版本下运行</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2147" target="_blank">#2147</a>，调用 RPC 时忽略<code>GET</code>请求的<code>Content-Type</code>headers。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fpull%2F2239" target="_blank">#2239</a>，修复误导性消歧错误，其中<code>relationship</code>键的内容看起来像有效的语法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F2294" target="_blank">#2294</a>，禁用并行 GC 以在 higher core CPU 上获得更好的性能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Fissues%2F1076" target="_blank">#1076</a>，修复空闲时使用 CPU 的问题</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPostgREST%2Fpostgrest%2Freleases%2Ftag%2Fv9.0.1" target="_blank">https://github.com/PostgREST/postgrest/releases/tag/v9.0.1</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            