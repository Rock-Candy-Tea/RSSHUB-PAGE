
---
title: '【重大更新】CloudCanal 社区版 1.0.2 正式发布，开放众多新数据源'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9066'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 09:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9066'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:left"> 
 <div> 
  <p><span style="color:#212529">CloudCanal是一款由</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fwww.clougence.com" target="_blank">ClouGence公司</a><span style="color:#212529">发行的集结构迁移、数据全量迁移/校验/订正、增量实时同步为一体的多源多端数据迁移同步平台。产品包含完整的产品化能力，助力企业打破数据孤岛、完成数据互融互通，从而更好的使用数据。</span></p> 
 </div> 
</div> 
<p style="text-align:left">发版时间:2021年8月20日<br> 版本号: 1.0.2</p> 
<h1 style="text-align:left">新特性</h1> 
<ul> 
 <li>新增Oracle源端</li> 
 <li>新增PostgreSQL源端</li> 
 <li>新增Greenplum源端</li> 
 <li>新增PolarDbMySQL源端</li> 
 <li>新增Oracle目标端</li> 
 <li>新增PostgreSQL目标端</li> 
 <li>新增Greenplum目标端</li> 
 <li>新增Hive目标端</li> 
 <li>新增DRDS目标端</li> 
 <li>新增PolarDbMySQL目标端</li> 
 <li>新增AdbForMySQL目标端</li> 
 <li>新增校验任务结果查看</li> 
 <li>支持ClickHouse最新版本到22.1</li> 
 <li>ClickHouse 新增 ReplacingMergeTree 支持，并且默认选中该表引擎</li> 
</ul> 
<h1 style="text-align:left">BugFix&优化</h1> 
<ul> 
 <li>修复timestamp on update current timestamp不同步问题</li> 
 <li>修复树状选择，筛选表，勾选掉一张表后又加载全部的问题</li> 
 <li>修复校验、订正任务重跑刷新的问题</li> 
 <li>修复源端阿里云 kafka 初始位点问题</li> 
 <li>修复Clickhouse对端同步无主键表问题</li> 
 <li>修复sidecar stdout打印过多日志问题</li> 
 <li>修复Kafka任务，获取分区NPE问题</li> 
 <li>修复因机器规格低导致的sidecar访问管控超时问题</li> 
 <li>修复机器timezone非东八区时的时区问题，现在CloudCanal时间值的写入和机器操作系统时区解耦</li> 
 <li>修复sidecar容器重启，sidecar进程没法正常重启的问题</li> 
 <li>优化写入对端 RocketMQ 性能</li> 
 <li>放开任务创建数量限制</li> 
</ul> 
<div> 
 <h1>关联资料</h1> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Fcategory%2F14" target="_blank">CloudCanal社区</a></p> 
 <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F84" target="_blank">CloudCanal Release信息汇总</a></p> 
 <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F94" target="_blank">CloudCanal安装使用文档(含下载地址)</a></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F76" target="_blank">MySQL到ClickHouse实时同步-CloudCanal实战</a></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F77" target="_blank">构建基于kafka中转的混合云在线数据生态-cloudcanal实战</a></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.askcug.com%2Ftopic%2F97" target="_blank"><span style="color:inherit">5分钟搞定 MySQL 到 ElasticSearch 迁移同步-CloudCanal实战</span></a></p> 
</div>
                                        </div>
                                      
</div>
            