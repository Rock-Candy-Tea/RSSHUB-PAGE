
---
title: 'Apache Impala 4.0 发布，大规模并行处理 SQL 查询引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7780'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7780'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Impala 是一个开源的大规模并行处理（MPP）SQL 查询引擎，用于存储在运行 Apache Hadoop 的计算机集群中的数据。</p> 
<p>Apache Impala 4.0 正式发布，更新内容如下：</p> 
<h3>重大变化：</h3> 
<ul> 
 <li>移除对 Hive 2.x 的支持；</li> 
 <li>移除对 Impala-lzo 的支持 
  <ul> 
   <li>Impala-lzo 提供了允许 Impala 读取 LZO 压缩表的代码。鉴于 LZO 的低采用率和其他可用的压缩选项，Impala 删除了 Impala-lzo 支持及其使用的低级别接口；</li> 
  </ul> </li> 
 <li>移除对 Sentry 的支持 
  <ul> 
   <li>从 4.0 开始，Impala 将只支持授权中的 Ranger；</li> 
  </ul> </li> 
 <li>为 x86_64 设置最低 CPU 要求为 AVX 
  <ul> 
   <li>在 4.0 之前，最低 CPU 要求是 SSSE3。现在我们把它提升到 AVX。对于只支持 AVX 而不支持 AVX2 的机器，请使用 --enable_legacy_avx_support 标志来启动 Impala；</li> 
  </ul> </li> 
 <li>删除了对无数据时间戳的支持；</li> 
 <li>增加对使用 || 的字符串连接操作的支持 
  <ul> 
   <li>此前，"||" 意味着逻辑 OR 表达式的 "OR"。现在，如果左边操作数的类型是 STRING，"||" 意味着对字符串连接的 "concat"；</li> 
  </ul> </li> 
 <li>默认不允许 HAVING 子句中的序数；</li> 
</ul> 
<h3>新功能：</h3> 
<ul> 
 <li>在所有运算符中支持多线程（MT_DOP）；</li> 
 <li>更密集的（聚合的）运行时配置文件，即 profile-v2；</li> 
 <li>支持所有 TPC-DS 99 查询，无需手动重写；</li> 
 <li>透明查询重试；</li> 
 <li>支持按 Z-Order 排序；</li> 
 <li>支持 Async Codegen；</li> 
 <li>支持对 Hive full-ACID ORC 表的读取；</li> 
 <li>与 Apache DataSketches 的内置函数；</li> 
 <li>Iceberg 支持；</li> 
 <li>使用 docker-compose 的 Impala 快速启动集群；</li> 
 <li>支持 aarch64 (ARM)</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimpala.apache.org%2Fdocs%2Fchangelog-4.0.html" target="_blank">https://impala.apache.org/docs/changelog-4.0.html</a></p>
                                        </div>
                                      
</div>
            