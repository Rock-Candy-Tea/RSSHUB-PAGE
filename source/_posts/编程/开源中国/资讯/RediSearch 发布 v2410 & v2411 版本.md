
---
title: 'RediSearch 发布 v2.4.10 & v2.4.11 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5703'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5703'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p style="margin-left:0px">RediSearch v2.4.10 & v2.4.11 版本发布了，RediSearch 是 RedisLabs 团队开发的一个高性能全文搜索引擎，可作为一个 Redis Module 运行在 Redis 上。</p> 
   <p style="margin-left:0px">版本带来如下变更：</p> 
   <h3 style="margin-left:0px"><strong>v2.4.10</strong></h3> 
   <ul> 
    <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2863" target="_blank">#2863</a><span style="color:#24292f"> </span>由于 FT.SPELLCHECK 中的 (Levenstein) 距离太高而导致崩溃。 此修复将距离限制为 4。 (MOD-3563) </li> 
    <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2875" target="_blank">#2875</a><span style="color:#24292f"> </span>并非所有具有 Vector 字段的文档都使用 Redis-on-Flash 进行索引 (MOD-3584) </li> 
    <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Fpull%2F2846" target="_blank">#2846</a><span style="color:#24292f"> </span>对矢量索引实施 Redis Enterprise 内存限制。</li> 
   </ul> 
   <p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Freleases%2Ftag%2Fv2.4.10" target="_blank">https://github.com/RediSearch/RediSearch/releases/tag/v2.4.10</a> </p> 
   <p> </p> 
   <h3><strong>v2.4.11</strong></h3> 
   <p><strong>Bug修复</strong></p> 
   <ul> 
    <li>#2892 在 FT.SEARCH 上将 SORTBY 与 MAX 结合使用（不支持），导致响应不一致和内存不足（MOD-3540、MOD-3644）</li> 
   </ul> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRedisAI%2FVectorSimilarity%2Freleases%2Ftag%2Fv0.3.1" target="_blank">VecSim v0.3.1</a>：</p> 
   <ul> 
    <li>HNSW 索引：删除时回收内存 - HNSW 索引的数据结构现在回收内存并在删除时收缩</li> 
   </ul> 
   <p><strong>改进</strong></p> 
   <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRedisAI%2FVectorSimilarity%2Freleases%2Ftag%2Fv0.3.1" target="_blank">VecSim v0.3.1</a>：</p> 
   <ul> 
    <li>HNSW 指数：删除过程加速 40% 。</li> 
    <li>为 HNSW 指数提供更准确的内存消耗报告</li> 
   </ul> 
   <p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRediSearch%2FRediSearch%2Freleases%2Ftag%2Fv2.4.11" target="_blank">https://github.com/RediSearch/RediSearch/releases/tag/v2.4.11</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            