
---
title: 'ip2region 2.10.0 发布，增加 c#_nodejs xdb 查询客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8179'
author: 开源中国
comments: false
date: Thu, 04 Aug 2022 11:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8179'
---

<div>   
<div class="content">
                                                                                            <p>ip2region (2.0 - xdb) 是一个离线的 IP 数据管理框架和定位库，支持亿级别的 IP 断管理，10 微秒级别的查询性能，提供了很多主流编程语言的 xdb 数据格式的生成和查询实现。</p> 
<p>ip2region 2.10.0 更新如下：</p> 
<p>1、增加 c# 查询客户端实现：<a href="https://gitee.com/lionsoul/ip2region/tree/master/binding/csharp">https://gitee.com/lionsoul/ip2region/tree/master/binding/csharp</a></p> 
<p>默认的 bench 测试结果如下：</p> 
<pre><code class="language-bash">IP2Region.SearchTest.exe bench --db=../../../../../data/ip2region.xdb --src=../../../../../data/ip.merge.txt
Bench finished, &#123;cachePolicy: vectorIndex, total: 3417955, took: 00:00:48.0082981, cost: 0 ms/op&#125;</code></pre> 
<p>2、增加 nodejs 查询客户端实现：<a href="https://gitee.com/lionsoul/ip2region/tree/master/binding/nodejs">https://gitee.com/lionsoul/ip2region/tree/master/binding/nodejs</a></p> 
<p>默认的 bench 测试结果如下：</p> 
<pre><code class="language-bash">➜  nodejs git:(v2.0-for-nodejs) ✗ node ./tests/bench.app.js
options: 
    dbPath: ../../data/ip2region.xdb
    src: ../../data/ip2region.xdb
    cache-policy: content

Bench finished, &#123;cachePolicy: content, total: 3417955, took: 20.591887765s, cost: 6.02462225658325μs/op&#125;</code></pre> 
<p>3、python xdb searcher 错误修复：<a href="https://gitee.com/lionsoul/ip2region/commit/268f659d788bd57810cb723ded2a5b0f64982d54">https://gitee.com/lionsoul/ip2region/commit/268f659d788bd57810cb723ded2a5b0f64982d54</a></p> 
<p>4、关闭 c/lua/java/go/php 的 buffer 相关函数的 handle。</p> 
<p>java maven 地址如下：</p> 
<pre><code class="language-xml"><dependency>
    <groupId>org.lionsoul</groupId>
    <artifactId>ip2region</artifactId>
    <version>2.6.5</version>
</dependency></code></pre> 
<p>ip2region 2.9.0 资源下载：</p> 
<p>1、Gitee：<a href="https://gitee.com/lionsoul/ip2region/tree/v2.10.0">https://gitee.com/lionsoul/ip2region/tree/v2.10.0</a></p> 
<p>2、Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flionsoul2014%2Fip2region%2Ftree%2Fv2.10.0" target="_blank">https://github.com/lionsoul2014/ip2region/tree/v2.10.0</a></p>
                                        </div>
                                      
</div>
            