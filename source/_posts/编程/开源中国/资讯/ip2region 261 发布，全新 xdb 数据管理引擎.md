
---
title: 'ip2region 2.6.1 发布，全新 xdb 数据管理引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4067'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 10:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4067'
---

<div>   
<div class="content">
                                                                                            <p>ip2region (2.0 - xdb) 是一个离线的 IP 数据管理框架和定位库，10微秒级别的查询性能，提供了很多主流编程语言的 xdb 数据格式的生成和查询实现。</p> 
<p>ip2region 2.6.1 弃用了之前的 1.0 的数据管理方式，重新设计了全新的 xdb 数据管理引擎，相比旧的引擎优缺点如下：<br> <br> 1、xdb 可以管理上亿级别的 IP 数据段，旧的数据引擎因为设计上的缺陷，超过 50 万行就会导致 btree 索引溢出，xdb 会彻底告别这个问题。</p> 
<p>2、更快的查询速度 - 10微秒级别的查询性能，xdb 数据管理引擎采用了 512KiB 固定的向量空间索引，利用一次固定的磁盘 IO 操作 (可缓存) 即可最大化的减少后续 binary 查询的次数，大部分的查询固定在 3 次 IO 操作，如果提前缓存 512KiB 的向量索引，可以固定的减少一次 IO 操作。如下是我的 razer 笔记本的 bench 测试结果 (三星 860 pro SSD磁盘，缓存向量索引)：<br> <br> golang bench 程序: <a href="https://gitee.com/lionsoul/ip2region/blob/master/binding/golang">https://gitee.com/lionsoul/ip2region/blob/master/binding/golang</a></p> 
<pre><code class="language-bash">➜  golang git:(master) ./xdb_searcher bench --src=../../data/ip.merge.txt --db=../../data/ip2region.xdb --cache-policy=vectorIndex
Bench finished, &#123;cachePolicy: vectorIndex, total: 3417955, took: 24.153655822s, cost: 6 μs/op&#125;</code></pre> 
<p>php bench 程序：<a href="https://gitee.com/lionsoul/ip2region/blob/master/binding/php">https://gitee.com/lionsoul/ip2region/blob/master/binding/php</a></p> 
<pre><code class="language-bash">➜  php git:(master) php ./bench_test.php --db=../../data/ip2region.xdb --src=../../data/ip.merge.txt --cache-policy=vectorIndex
Bench finished, &#123;cachePolicy: vectorIndex, total: 3417955, took: 27s, cost: 0.008 ms/op&#125;
</code></pre> 
<p>java bench 程序：<a href="https://gitee.com/lionsoul/ip2region/blob/master/binding/java">https://gitee.com/lionsoul/ip2region/blob/master/binding/java</a></p> 
<pre><code class="language-bash">➜  java git:(master) java -jar target/ip2region-2.6.1.jar bench --db=../../data/ip2region.xdb --src=../../data/ip.merge.txt
Bench finished, &#123;cachePolicy: vectorIndex, total: 3417955, took: 23s, cost: 6 μs/op&#125;</code></pre> 
<p>3、更简洁的代码和 API 实现：相比旧的三种查询算法，xdb 只有一个 search 接口，而且这个查询接口的实现代码也少很多，其他都是工具函数。</p> 
<p>4、缓存加速支持：xdb 引擎支持完全基于文件查询，也可以用固定的 512KiB 的内存缓存 `向量索引` 固定的减少一次磁盘 IO 加速查询，也可以完全的缓存整个 xdb 数据实现完全基于内存的查询，类似旧版本的 memorySearch。</p> 
<p>5、因为向量空间索引的设计，xdb 数据库文件会变大，这是相对旧版本来说是一个劣势的地方。</p> 
<p><strong>下载地址</strong>：</p> 
<p>目前发布的 2.6.1 版本包含了 golang 的生成程序和 golang/php/java 的查询程序，每个实现都有详细的 ReadMe 文档，c和lua的查询程序将会再下一个版本发布，资源地址如下：</p> 
<p>Gitee：<a href="https://gitee.com/lionsoul/ip2region/tree/v2.6.1">https://gitee.com/lionsoul/ip2region/tree/v2.6.1</a><br> Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flionsoul2014%2Fip2region%2Ftree%2Fv2.6.1" target="_blank">https://github.com/lionsoul2014/ip2region/tree/v2.6.1</a></p>
                                        </div>
                                      
</div>
            