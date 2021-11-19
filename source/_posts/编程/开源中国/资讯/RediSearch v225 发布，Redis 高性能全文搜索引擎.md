
---
title: 'RediSearch v2.2.5 发布，Redis 高性能全文搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2003'
author: 开源中国
comments: false
date: Thu, 18 Nov 2021 23:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2003'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">RediSearch v2.2.5 发布了<strong>，</strong></span><span style="color:#333333">RediSearch 是 RedisLabs 团队开发的一个高性能全文搜索引擎，可作为一个 Redis Module 运行在 Redis 上。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><strong>此版本的重大更新有如下三项：</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033"><strong>JSON 文档索引/搜索</strong></span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此版本引入了<span style="color:#2e3033">使用 JSONPath 查询对 JSON 文档进行索引、查询和全文搜索的功能。</span>现在在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redis.com%2Fredisearch%2Fmaster%2FCommands%2F%23ftcreate" target="_blank">FT.CREATE </a>架构创建上可以将 JSONPath 查询与字段映射。<span style="color:#2e3033">建立JSON 文档索引时，JSONPath 查询提取的值将在给定字段中建立索引。</span><strong>注意，此功能需要安装<span> </span></strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.redisjson.io%2F" target="_blank"><strong><u>RedisJSON 2.0</u></strong></a><span> </span>。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033"><strong>分析查询（</strong></span><strong>Profiling queries</strong><span style="color:#2e3033"><strong>）</strong></span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">v2.2.5<span> </span><span style="color:#2e3033">还引入一个新的<span> </span><code>FT.PROFILE</code><span> </span>命令用来分析查询，它可以详细分析 FT.SEARCH 和 FT.AGGREGATE 执行过程中涉及的内部步骤的执行时间，从而了解到底是查询的哪个部分在占用大部分资源。</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033"><strong>字段别名（</strong></span><strong>Field aliasing</strong><span style="color:#2e3033"><strong>）</strong></span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">随着支持 JSON 文档索引，现在可以将 JSONPath 查询映射到别名。可以使用不同的索引策略以在不同的字段中索引相同的值。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033"><strong>其他详细更新项：</strong></span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>改进</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加对 redis COPY 命令的支持 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2337" target="_blank">#2337</a><span> </span>)</li> 
 <li><span style="color:#24292f">为<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redis.com%2Fredisearch%2Fmaster%2FCommands%2F%23ftaggregate" target="_blank">FT.AGGREGATE</a><span> </span>添加<span> </span><code>LOAD *</code><span> </span>命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2243" target="_blank">＃2243</a>）</li> 
 <li>加入恰当的多值回归标签（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2207" target="_blank">#2207</a>）</li> 
 <li><span style="color:#2e3033">为可排序字段（</span>SORTABLE fields<span style="color:#2e3033">）添加 UNF 标记</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2188" target="_blank">#2188</a>）</li> 
 <li>添加用于分数、语言和<span> </span><span style="color:#2e3033">stopwords 列表</span>的<span> </span><code>LLAPI getter</code><span> </span>函数 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2184" target="_blank">#2184</a><span> </span>)</li> 
 <li>现在 JSON 数组可以存储在 TAG 字段中（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2133" target="_blank">#2133</a>）</li> 
 <li>将<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redis.com%2Fredisearch%2Fmaster%2FCommands%2F%23ftinfo" target="_blank">FT.INFO</a><span> </span>复杂度提高到 O(1) (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2153" target="_blank">#2153</a><span> </span>)</li> 
 <li>将<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redis.com%2Fredisearch%2Fmaster%2FTags%2F%23creating_a_tag_field" target="_blank">CASESENSITIVE</a><span> </span>添加到 TAG 字段（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2138" target="_blank">#2138</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redis.com%2Fredisearch%2Fmaster%2FCommands%2F%23ftinfo" target="_blank">FT.INFO</a><span> </span>已具有字段的标识符和属性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2137" target="_blank">#2137</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033"><strong>bug 修复</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 JSON 的分数字段（<span style="color:#24292f">score field</span>） (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2341" target="_blank">#2341</a><span> </span>)</li> 
 <li>修复标签转义 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2325" target="_blank">#2325</a><span> </span>)</li> 
 <li>删除空标签值 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2269" target="_blank">#2269</a><span> </span>)</li> 
 <li><span style="color:#2e3033">将负迭代器的子迭代器换成空迭代器</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2223" target="_blank">#2223</a>）</li> 
 <li>更新标签的字段限制 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2215" target="_blank">#2215</a><span> </span>)</li> 
 <li>部分 JSON 文档未编入索引的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2143" target="_blank">#2143</a>）</li> 
 <li><span style="color:#2e3033">用'AS'加载的字段不能被 funcs 使用的问题</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2109" target="_blank">#2109</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Freleases%2Ftag%2Fv2.2.5" target="_blank">https://github.com/RediSearch/RediSearch/releases/tag/v2.2.5</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            