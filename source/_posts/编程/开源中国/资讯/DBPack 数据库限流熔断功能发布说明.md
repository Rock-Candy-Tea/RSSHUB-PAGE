
---
title: 'DBPack 数据库限流熔断功能发布说明'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1723'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 00:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1723'
---

<div>   
<div class="content">
                                                                                            <p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">上周我们发布了 v0.4.0 版本，增加了限流熔断功能，现对这两个功能做如下说明。</p> 
<h2 style="margin-left:.8rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.4.0%3Fid%3D%25e9%2599%2590%25e6%25b5%2581" target="_blank"><span style="color:#34495e">限流</span></a></h2> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">DBPack 限流熔断功能通过 filter 实现。要设置限流规则，首先要定义<span> </span><code>RateLimitFilter</code>：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>    - name: rateLimiterFilter
      kind: RateLimiterFilter
        conf:
        # 1000 requests per second
        insert_limit: 1000
        # 1000 requests per second
        update_limit: 1000
        # 1000 requests per second
        delete_limit: 1000
        # 1000 requests per second
        select_limit: 1000</code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">支持对增删改查请求单独限流。限流策略以秒为单位，即允许每秒执行多少次请求（RPS）。如果设置为 0 表示不限流。上面的例子表示限制为每秒执行 1000 次请求。</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">定义好<span> </span><code>RateLimitFilter</code><span> </span>后，将 filter 的名字加入到 Executor 的 filter list 中：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>    executors:
      - name: redirect
        mode: sdb
        config:
          data_source_ref: employees
        filters:
          - cryptoFilter
          # 限流 filter
          - rateLimiterFilter</code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">这样就配置好限流功能了。</p> 
<h2 style="margin-left:.8rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.4.0%3Fid%3D%25e7%2586%2594%25e6%2596%25ad" target="_blank"><span style="color:#34495e">熔断</span></a></h2> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">配置 DBPack 的熔断功能，需要先定义<span> </span><code>CircuitBreakerFilter</code>：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>      - name: circuitBreakerFilter
        kind: CircuitBreakerFilter
        conf:
          # error 次数
          error_threshold: 20
          # success 次数
          success_threshold: 5
          // seconds
          timeout: 60</code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">上面的配置表示：</p> 
<ol> 
 <li>60 秒内累计错误次数达到 20 次，熔断器状态为<span> </span><code>Open</code><span> </span>打开状态，此时请求不能执行。</li> 
 <li>熔断器打开 60 秒后，熔断器状态变为<span> </span><code>HalfOpen</code><span> </span>半开状态，此时可以执行请求。</li> 
 <li>熔断器状态变为<span> </span><code>HalfOpen</code><span> </span>半开状态后，执行的第一个请求，如果执行失败，熔断器再次变为<span> </span><code>Open</code><span> </span>打开状态；如果连续 5 次请求执行成功，则关闭熔断器，熔断器状态变为<span> </span><code>Closed</code>。</li> 
</ol> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">定义好<span> </span><code>CircuitBreakerFilter</code><span> </span>后，将 filter 的名字加入到 Executor 的 filter list 中：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>    executors:
      - name: redirect
        mode: sdb
        config:
          data_source_ref: employees
        filters:
          - cryptoFilter
          # 熔断 filter
          - circuitBreakerFilter</code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">这样就配置好了熔断功能。</p> 
<h2 style="margin-left:.8rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.4.0%3Fid%3D%25e7%25bb%25bc%25e8%25bf%25b0" target="_blank"><span style="color:#34495e">综述</span></a></h2> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">在 v0.1.0 版本我们发布了分布式事务功能，支持各种编程语言协调分布式事务。</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">在 v0.2.0 版本我们发布了读写分离功能，用户在开启读写分离功能的情况下，使用分布式事务协调功能不再需要做复杂的集成，DBPack 提供了一站式的解决方案。</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">在 v0.3.0 版本，我们加入 SQL Tracing 的功能，使用该功能可以收集到一个完整的分布式事务链路，查看事务的执行情况。我们还加入了数据加密功能，通过该功能保护用户的重要数据资产。</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">在 v0.4.0 版本，我们加入了限流熔断功能，该功能能保护数据库不受到超过自身处理能力的请求流量冲击。</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">在 v0.5.0 版本中，我们将加入分库分表功能。</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">欢迎开源爱好者和我们一起建设 DBPack 社区，加群或参与社区建设，请微信联系：scottlewis。</p> 
<h2 style="margin-left:.8rem; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcectc.github.io%2Fdbpack-doc%2F%23%2Fblogs%2Frelease-v0.4.0%3Fid%3D%25e9%2593%25be%25e6%258e%25a5" target="_blank"><span style="color:#34495e">链接</span></a></h2> 
<ul> 
 <li>dbpack:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack" target="_blank">https://github.com/CECTC/dbpack</a></li> 
 <li>dbpack-samples:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-samples" target="_blank">https://github.com/CECTC/dbpack-samples</a></li> 
 <li>dbpack-doc:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-doc" target="_blank">https://github.com/CECTC/dbpack-doc</a></li> 
 <li>事件驱动分布式事务设计：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fr43JvRY3LCETMoZjrdNxXA" target="_blank">https://mp.weixin.qq.com/s/r43JvRY3LCETMoZjrdNxXA</a></li> 
 <li>视频介绍： 
  <ul> 
   <li>《dbpack 分布式事务功能详解》<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1cg411X7Ek" target="_blank">https://www.bilibili.com/video/BV1cg411X7Ek</a></li> 
   <li>《高性能分布式事务框架实践》<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Xr4y1L7kD" target="_blank">https://www.bilibili.com/video/BV1Xr4y1L7kD</a></li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            