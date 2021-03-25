
---
title: 'open-monitor 1.9.0 版本发布，基于 Prometheus 的分布式监控平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7879'
author: 开源中国
comments: false
date: Thu, 25 Mar 2021 15:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7879'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">open-monitor是一套基于Prometheus的分布式监控平台，适用于wecube，WeCube通过监控插件来对资源以及应用的监控及告警。此插件底层引用Prometheus，上层封装了对Prometheus的配置管理和图表展示，后端技术选型为Go + Gin + Xorm, 前端技术选型为Vue + ECharts。</span></p> 
<p>此次版本包含以下内容</p> 
<p style="text-align:start">新增：<br> 1、阈值配置支持告警发送与延时设置<br> 2、分离access_log日志<br> 3、增加作为插件时对wecube的访问鉴权</p> 
<p style="text-align:start">修复：<br> 1、关键字告警逻辑优化<br> 2、优化代码里的时区设置<br> 3、修复多实例注册同步问题<br> 4、修复agent_manager对象管理状态问题<br> 5、修复mysql归档工具的并发问题<br> 6、修复告警列表历史数据查询过滤条件不生效问题</p>
                                        </div>
                                      
</div>
            