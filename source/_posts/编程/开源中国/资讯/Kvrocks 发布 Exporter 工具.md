
---
title: 'Kvrocks 发布 Exporter 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-09e7ccdc9f7a1110755ca4eaffe00947bce.png'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 10:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-09e7ccdc9f7a1110755ca4eaffe00947bce.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#b8bfc6; text-align:start"><span style="color:#000000">跟 Redis 一样，Kvrocks 也使用 INFO 命令来暴露相关指标(metrics)。Redis 社区有 redis_exporter 用来将 INFO 命令返回信息转为 Prometheus 指标，方便用户进行监控和报警。我们也是基于 redis_exporter 改造以支持 Kvrocks 相关指标。同时，我们也提供了 Grafana 报表模板，用户也可以通过 ID(15286) 或者下载 JSON 文件来导入监控报表。</span></p> 
<p style="color:#b8bfc6; text-align:start"><span style="color:#000000">GitHub 链接:</span> <span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKvrocksLabs%2Fkvrocks_exporter" target="_blank">https://github.com/KvrocksLabs/kvrocks_exporter</a></span></p> 
<p style="color:#b8bfc6; text-align:start"><span style="color:#000000">Grafana 链接:</span> <span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fgrafana%2Fdashboards%2F15286" target="_blank">https://grafana.com/grafana/dashboards/15286</a></span></p> 
<p><span>然后使用 ./kvrocks_exporter -kvrocks.addr &#123;YOUR KVROCKS ADDRESS&#125; 启动。</span></p> 
<p><strong>编译</strong></p> 
<pre><code class="language-bash">git clone https://github.com/KvrocksLabs/kvrocks_exporter.git
cd kvrocks_exportergo build
../kvrocks_exporter --version</code></pre> 
<p><span><strong><span>Grafana  展示</span></strong></span></p> 
<p><span>整体分为几个部分:</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p><span>概要信息</span></p> </li> 
 <li> <p><span>Server 相关，包含 CPU、内存、OPS 以及延时等</span></p> </li> 
 <li> <p><span>复制信息，Full/Partial Sync 以及 Lag 等</span></p> </li> 
 <li> <p><span>磁盘相关，磁盘的使用情况以及大小</span></p> </li> 
 <li> <p><span>RocksDB 指标，各种 Cache  使用以及 Slowdown/Stop 信息等</span></p> </li> 
</ul> 
<p><strong><span>整体效果如下:</span></strong></p> 
<p><img height="3336" src="https://oscimg.oschina.net/oscnet/up-09e7ccdc9f7a1110755ca4eaffe00947bce.png" width="1080" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            