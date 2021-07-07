
---
title: 'TimescaleDB 2.3.1 发布，基于 PostgreSQL 的时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2046'
author: 开源中国
comments: false
date: Wed, 07 Jul 2021 06:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2046'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TimescaleDB 2.3.1 现已发布。TimescaleDB 是基于 PostgreSQL 开发的一款时序数据库，以插件化的形式打包提供。 </p> 
<p>此版本更新内容如下：</p> 
<p><strong>Bug修复</strong></p> 
<ul> 
 <li>#3279 为 chunk assignment 添加更多随机性</li> 
 <li>#3288 修复 parallel workers 的更新失败</li> 
 <li>#3300 改进分布式 hypertables 的 trigger handling</li> 
 <li>#3304 移除压缩块中引用父级 relids 的路径</li> 
 <li>#3305 修复 pull_varnos 对 relids 集的错误计算</li> 
 <li>#3310 生成降级脚本</li> 
 <li>#3314 修复 hypertable 扩展中的堆缓冲区溢出</li> 
 <li>#3317 修复远程连接缓存中的堆缓冲区溢出。</li> 
 <li>#3327 使 caggs 中的聚合完全合格</li> 
 <li>#3336 修复 pg_init_privs objsubid 处理</li> 
 <li>#3345 修复 SkipScan 不同的列标识</li> 
 <li>#3355 在重命名压缩的 hypertable 列时修复堆缓冲区溢出。</li> 
 <li>#3367 改进 DecompressChunk qual pushdown</li> 
 <li>#3377 修复 repalloc 的错误使用</li> 
</ul> 
<p>更多详情可查看： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftimescale%2Ftimescaledb%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">https://github.com/timescale/timescaledb/blob/master/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            