
---
title: 'ip2region 2.8.0 发布 - 增加 lua_python xdb 查询客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7623'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 11:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7623'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">ip2region (2.0 - xdb) 是一个离线的 IP 数据管理框架和定位库，支持亿级别的 IP 断管理，10 微秒级别的查询性能，提供了很多主流编程语言的 xdb 数据格式的生成和查询实现。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">ip2region 2.8.0  具体更新如下：</span></p> 
<p>1、增加 lua xdb 查询客户端实现：<a href="https://gitee.com/lionsoul/ip2region/tree/master/binding/lua">https://gitee.com/lionsoul/ip2region/tree/master/binding/lua</a></p> 
<p>默认的 bench 测试结果如下（<strong>建议使用 lua_c 代替 lua，查询性能不是一个数量级的</strong>）：</p> 
<pre><code class="language-bash">➜  lua git:(master) lua bench_test.lua --db=../../data/ip2region.xdb --src=../../data/ip.merge.txt --cache-policy=vectorIndex
Bench finished, &#123;cachePolicy: vectorIndex, total: 3417955, took: 31.000 s, cost: 7.607 μs/op&#125;</code></pre> 
<p>2、增加 python 查询客户端实现：<a href="https://gitee.com/lionsoul/ip2region/tree/master/binding/python">https://gitee.com/lionsoul/ip2region/tree/master/binding/python</a></p> 
<p>默认的 bench 测试结果如下：</p> 
<pre><code class="language-bash">➜  python git:(master) python3 bench_test.py --db=../../data/ip2region.xdb --src=../../data/ip.merge.txt --cache-policy=vectorIndex
Bench finished, &#123;cachePolicy: vectorIndex, total: 3417955, took: 29.55 s, cost: 0.0081 ms/op&#125;</code></pre> 
<p>3、golang maker 和 searcher 优化。</p> 
<p>4、java xdb searcher 优化，maven 版本为 2.6.4：</p> 
<pre><code class="language-xml"><dependency>
    <groupId>org.lionsoul</groupId>
    <artifactId>ip2region</artifactId>
    <version>2.6.4</version>
</dependency></code></pre> 
<p> </p> 
<p><span style="background-color:#ffffff; color:#333333">资源下载地址：</span></p> 
<p>1、Gitee：<a href="https://gitee.com/lionsoul/ip2region/tree/v2.8.0">https://gitee.com/lionsoul/ip2region/tree/v2.8.0</a></p> 
<p>2、Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flionsoul2014%2Fip2region%2Ftree%2Fv2.8.0" target="_blank">https://github.com/lionsoul2014/ip2region/tree/v2.8.0</a></p>
                                        </div>
                                      
</div>
            