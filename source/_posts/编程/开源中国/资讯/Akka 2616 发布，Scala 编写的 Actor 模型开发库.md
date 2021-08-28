
---
title: 'Akka 2.6.16 发布，Scala 编写的 Actor 模型开发库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4826'
author: 开源中国
comments: false
date: Sat, 28 Aug 2021 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4826'
---

<div>   
<div class="content">
                                                                                            <p>Akka 2.6.16 现已发布，这是 2.6 的一个补丁版本，一共修复了 44 个问题。Akka 是一个用 Scala 编写的库，用于简化编写容错的、高可伸缩性的 Java 和 Scala 的 Actor 模型应用。</p> 
<p>一些亮点更新内容如下：</p> 
<ul> 
 <li>添加 Durable State persistence。Durable State 是一个新的 persistence model，是对 Event Sourced persistence 的补充。</li> 
 <li>排除 Sharding 使用的 Read/Write MajorityPlus 中的 exiting members <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fakka%2Fakka%2Fissues%2F30327" target="_blank">#30327</a></li> 
 <li>优雅地终止分片区域会不必要地延迟进一步的重新平衡 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fakka%2Fakka%2Fissues%2F30401" target="_blank">#30401</a></li> 
 <li>Coalesce 在 TCP Streams 中写入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fakka%2Fakka%2Fpull%2F30334" target="_blank">#30334</a></li> 
 <li>可以为 Streams 和 Actors 的回退重启配置日志级别<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fakka%2Fakka%2Fissues%2F30445" target="_blank">#30445</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fakka.io%2Fblog%2Fnews%2F2021%2F08%2F19%2Fakka-2.6.16-released" target="_blank">https://akka.io/blog/news/2021/08/19/akka-2.6.16-released</a></p> 
<p>完整的变更记录见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fakka%2Fakka%2Fmilestone%2F177%3Fclosed%3D1" target="_blank">https://github.com/akka/akka/milestone/177?closed=1</a></p>
                                        </div>
                                      
</div>
            