
---
title: '搜索引擎 RediSearch 发布 2.0.8 和 2.0.13 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6187'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 06:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6187'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RediSearch 是一个高性能的全文搜索引擎，RediSearch 2.0.8 和 2.0.13 版本正式发布，两个版本都是 RediSearch 2.0 的维护版本，但更新的紧急程度不同。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">RediSearch 2.0.8 </h3> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#2e3033">紧急度：高</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">有一个严重的 bug 修复，可能会影响一部分用户，</span>此版本修复了 2.0 版本引入的重要回归，只有在设置了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redis.com%2Fredisearch%2Fpayloads%2F%23retrieving_payloads_from_documents" target="_blank">WITHPAYLOADS</a><span> </span>参数时才应该返回有效负载 。</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">Bug 修复：</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fissues%2F1959" target="_blank">#1959</a><span> </span>将<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redislabs.com%2Fredisearch%2FAggregations%2F%23list_of_datetime_apply_functions" target="_blank">parse_time()</a><span> </span>重命名为<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foss.redislabs.com%2Fredisearch%2FAggregations%2F%23list_of_datetime_apply_functions" target="_blank">parsetime()</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fissues%2F1932" target="_blank">#1932</a><span> </span>修复了由 LIMIT 参数导致的崩溃</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fissues%2F1919" target="_blank">#1919</a><span> </span>防止 GC fork 崩溃</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F1914" target="_blank">#1914</a><span> </span>不要将有效负载作为字段返回</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">增强功能：</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fissues%2F1880" target="_blank">#1880</a><span> </span>优化交叉迭代器</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Freleases%2Ftag%2Fv2.0.8" target="_blank">https://github.com/RediSearch/RediSearch/releases/tag/v2.0.8</a></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">RediSearch 2.0.13 </h3> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">紧急度：低</h3> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">Bug修复：</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2269" target="_blank">#2269<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2291" target="_blank">#2291</a>从<span> </span><span style="color:#24292f">Garbage Collection<span> </span></span>没有条目的 trie 中删除 TAG 值。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2287" target="_blank">#2287</a><span> </span>未初始化读取<code>FT.ADD</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2342" target="_blank">#2342</a><span> </span><span style="color:#2e3033">在交叉迭代器上检查 NULL 结果</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2350" target="_blank">＃2350</a><span> </span><span style="color:#24292f"><code>LIMIT 0 0</code><span> </span> 在<span> </span><code>FT.AGGREGATE<span> </span></code>上的崩溃问题</span></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">改进：</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2243" target="_blank">#2243</a><span> </span><span style="color:#2e3033">为<span> </span><code>FT.AGGREGATE</code><span> </span>添加<span> </span><code>LOAD *</code>，它将加载所有字段。</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Freleases%2Ftag%2Fv2.0.13" target="_blank">https://github.com/RediSearch/RediSearch/releases/tag/v2.0.1</a></p>
                                        </div>
                                      
</div>
            