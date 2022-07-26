
---
title: 'Categraf v0.2.5 版本发布，框架调优，扩展监控采集插件更加简单了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=804'
author: 开源中国
comments: false
date: Tue, 26 Jul 2022 14:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=804'
---

<div>   
<div class="content">
                                                                                            <h4>Categraf v0.2.5 更新内容</h4> 
<ul> 
 <li>做了重大重构，把很多插件侧的代码提取到了框架层，写监控插件的代价更小了，代码看起来也更干净了</li> 
 <li>在框架侧做了一些通用的逻辑，比如： 
  <ul> 
   <li>所有的插件都支持配置labels，可以为时序数据附加一些自定义标签</li> 
   <li>所有插件都可以通过interval和interval_times配置，来控制执行频率</li> 
   <li>所有插件都支持metrics_drop和metrics_pass配置，通过黑白名单的方式来过滤监控指标，丢弃一些没用的指标</li> 
   <li>所有插件都支持metrics_name_prefix，可以为指标名字添加前缀</li> 
   <li>所有插件都支持processor_enum配置，可以做value映射，比如采集的数据如果是字符串枚举，可以转换为数字，这对prometheus生态是必须的，因为prometheus生态的时序库只能接收数值类型的数据</li> 
  </ul> </li> 
</ul> 
<p> </p> 
<h4>Categraf 是什么？</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Categraf 是一个监控采集 Agent，类似 Telegraf、Grafana-Agent、Datadog-Agent，希望对所有常见监控对象提供监控数据采集能力，采用 All-in-one 的设计，不但支持指标采集，也希望支持日志和调用链路的数据采集。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Categraf 采集到数据可以推给 Prometheus、VictoriaMetrics、M3DB、InfluxDB、TDEngine 等，如果大家觉得搞很多个 exporter 不方便，可以尝试一下 Categraf，我们不但希望Categraf能支持丰富的采集插件，也能够把我们10年来的监控系统构建经验落地到这个产品，让大家享受到开箱即用的最佳实践。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">国内目前没有一款特别好用的 all-in-one 的监控数据采集器，希望 Categraf 能肩负这个重任，在大家的共同参与下，逐渐打磨成为一款开箱即用的采集器。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            