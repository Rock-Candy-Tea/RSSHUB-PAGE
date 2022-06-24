
---
title: 'Categraf 发布 0.1.7 版本，增加 conntrack 和 zookeeper 等采集器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=300'
author: 开源中国
comments: false
date: Fri, 24 Jun 2022 11:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=300'
---

<div>   
<div class="content">
                                                                                            <p>Categraf 发布 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflashcatcloud%2Fcategraf%2Freleases%2Ftag%2Fv0.1.7" target="_blank">v0.1.7</a> 版本，新版本增加了一些新的采集器，包括：</p> 
<ul> 
 <li>contrack插件：用于采集linux的conntrack情况</li> 
 <li>zookeeper插件：使用四字命令，采集zookeeper的监控数据，对于小于 3.6.0 版本的zookeeper监控，比较实用，新版本的zookeeper已经内置了prometheus的支持</li> 
 <li>prometheus插件：修复histogram类型的数据的转换逻辑问题</li> 
</ul> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflashcatcloud%2Fcategraf" target="_blank">Categraf</a> 是什么？</strong></p> 
<p><span style="background-color:#ffffff; color:#333333">Categraf 是一个监控采集 Agent，类似 Telegraf、Grafana-Agent、Datadog-Agent，希望对所有常见监控对象提供监控数据采集能力，采用 All-in-one 的设计，不但支持指标采集，也希望支持日志和调用链路的数据采集。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">Categraf 采集到数据可以推给 Prometheus、VictoriaMetrics、M3DB、InfluxDB、TDEngine 等，如果大家觉得搞很多个 exporter 不方便，着实可以尝试一下 Categraf。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">国内目前没有一款特别好用的all-in-one的监控数据采集器，希望 Categraf 能肩负这个重任，在大家的共同参与下，逐渐打磨成为一款开箱即用的采集器。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            