
---
title: 'Apache Druid 0.21.1 发布，实时分析数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6022'
author: 开源中国
comments: false
date: Sat, 12 Jun 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6022'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Druid 0.21.1 发布了。Druid 是一个分布式的、支持实时多维 OLAP 分析的数据处理系统。它既支持高速的数据实时摄入处理，也支持实时且灵活的多维数据分析查询。因此 Druid 最常用的场景就是大数据背景下、灵活快速的多维 OLAP 分析。 另外，Druid 还有一个关键的特点：它支持根据时间戳对数据进行预聚合摄入和聚合分析，因此也有用户经常在有时序数据处理分析的场景中用到它。 </p> 
<p>0.21.1 是一个错误修复版本，修复了 0.21 版本的一些回归问题。首先是已发布的 Docker 镜像的问题，由于卷的权限问题，导致容器无法启动，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fissues%2F11166" target="_blank">#11166</a> 中描述的问题在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11167" target="_blank">#11167</a> 中得到了修复。此版本还修复了一个由 0.21 中发布的升级 Jetty 版本中的错误引起的问题，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fissues%2F11206" target="_blank">#11206</a> 中描述，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11207" target="_blank">#11207 </a>中修复。最后，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11228" target="_blank">#11228 </a>中增加了一个与字段验证有关的 web console 回归。</p> 
<p><strong>Bug fixes</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11167" target="_blank">#11167</a> 修复 docker 卷权限</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11207" target="_blank">#11207</a> 升级  jetty 版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11228" target="_blank">#11228</a> Web console：修复必填字段的处理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11299" target="_blank">#11299</a> 修复 docker 中的权限问题</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Freleases%2Ftag%2Fdruid-0.21.1" target="_blank">https://github.com/apache/druid/releases/tag/druid-0.21.1</a> </p>
                                        </div>
                                      
</div>
            