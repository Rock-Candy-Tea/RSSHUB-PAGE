
---
title: 'ip2region 2.7.0 发布 - 增加 c_lua_c xdb 查询客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1456'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 10:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1456'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">ip2region (2.0 - xdb) 是一个离线的 IP 数据管理框架和定位库，支持亿级别的 IP 断管理，10 微秒级别的查询性能，提供了很多主流编程语言的 xdb 数据格式的生成和查询实现。</span></p> 
<p>ip2region 2.7.0  具体更新如下：</p> 
<p>1、增加 c xdb 查询客户端实现：<a href="https://gitee.com/lionsoul/ip2region/tree/master/binding/c">https://gitee.com/lionsoul/ip2region/tree/master/binding/c</a></p> 
<p>默认数据的 bench 测试结果如下：</p> 
<pre><code class="language-bash">➜  c git:(master) ./xdb_searcher bench --db=../../data/ip2region.xdb --src=../../data/ip.merge.txt --cache-policy=vectorIndex
Bench finished, &#123;cache_policy: vectorIndex, total: 3417955, took: 3.896s, cost: 1 μs/op&#125;</code></pre> 
<p>2、增加 lua_c xdb 查询客户端实现：<a href="https://gitee.com/lionsoul/ip2region/tree/master/binding/lua_c">https://gitee.com/lionsoul/ip2region/tree/master/binding/lua_c</a></p> 
<p>默认数据的 bench 测试结果如下：</p> 
<pre><code class="language-bash">➜  lua_c git:(master) lua bench_test.lua --db=../../data/ip2region.xdb --src=../../data/ip.merge.txt --cache-policy=vectorIndex
Bench finished, &#123;cachePolicy: vectorIndex, total: 3417955, took: 5.381 s, cost: 1.269 μs/op&#125;</code></pre> 
<p>3、优化 java xdb 查询器的代码和稳定，maven 版本为 2.6.3：</p> 
<pre><code class="language-xml"><dependency>
    <groupId>org.lionsoul</groupId>
    <artifactId>ip2region</artifactId>
    <version>2.6.3</version>
</dependency></code></pre> 
<p>4、php/golang xdb 客户的一些文档和细节的优化。</p> 
<p>资源下载地址：</p> 
<p>1、Gitee：<a href="https://gitee.com/lionsoul/ip2region/tree/v2.7.0">https://gitee.com/lionsoul/ip2region/tree/v2.7.0</a></p> 
<p>2、Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flionsoul2014%2Fip2region%2Ftree%2Fv2.7.0" target="_blank">https://github.com/lionsoul2014/ip2region/tree/v2.7.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            