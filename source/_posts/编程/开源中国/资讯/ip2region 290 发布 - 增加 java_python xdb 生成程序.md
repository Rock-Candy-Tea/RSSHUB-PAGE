
---
title: 'ip2region 2.9.0 发布 - 增加 java_python xdb 生成程序'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5242'
author: 开源中国
comments: false
date: Mon, 18 Jul 2022 12:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5242'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">ip2region (2.0 - xdb) 是一个离线的 IP 数据管理框架和定位库，支持亿级别的 IP 断管理，10 微秒级别的查询性能，提供了很多主流编程语言的 xdb 数据格式的生成和查询实现。</span></p> 
<p>ip2region 2.9.0 更新如下：</p> 
<p>1、增加 java xdb maker：<a href="https://gitee.com/lionsoul/ip2region/tree/master/maker/java">https://gitee.com/lionsoul/ip2region/tree/master/maker/java</a></p> 
<p>运行生成过程类似如下：</p> 
<pre><code class="language-bash">2022-07-18 12:35:49 INFO  org.lionsoul.ip2region.xdb.Maker try to write the vector index block ... 
2022-07-18 12:35:49 INFO  org.lionsoul.ip2region.xdb.Maker try to write the segment index ptr ... 
2022-07-18 12:35:49 INFO  org.lionsoul.ip2region.xdb.Maker write done, dataBlocks: 13804, indexBlocks: (683591, 720221), indexPtr: (982904, 11065984)
2022-07-18 12:35:49 INFO  org.lionsoul.ip2region.MakerTest Done, elapsed: 49 s</code></pre> 
<p>2、增加 python xdb maker：<a href="https://gitee.com/lionsoul/ip2region/tree/master/maker/python">https://gitee.com/lionsoul/ip2region/tree/master/maker/python</a></p> 
<p>运行生成过程类似如下：</p> 
<pre><code class="language-bash">2022-07-18 12:40:08,277-root-258-INFO - try to write the vector index block ... 
2022-07-18 12:40:08,296-root-266-INFO - try to write the segment index ptr ... 
2022-07-18 12:40:08,296-root-271-INFO - write done, dataBlocks: 13804, indexBlocks: (683591, 720221), indexPtr: (982904, 11065984)
2022-07-18 12:40:08,297-root-67-INFO - Done, elapsed: 2m45s</code></pre> 
<p>3、golang maker 优化。</p> 
<p> </p> 
<p>资源下载地址：</p> 
<p>Gitee：<a href="https://gitee.com/lionsoul/ip2region/tree/v2.9.0/">https://gitee.com/lionsoul/ip2region/tree/v2.9.0/</a></p> 
<p>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flionsoul2014%2Fip2region%2Ftree%2Fv2.9.0" target="_blank">https://github.com/lionsoul2014/ip2region/tree/v2.9.0</a></p>
                                        </div>
                                      
</div>
            