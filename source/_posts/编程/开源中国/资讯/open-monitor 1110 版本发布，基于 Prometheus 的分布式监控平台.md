
---
title: 'open-monitor 1.11.0 版本发布，基于 Prometheus 的分布式监控平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6413'
author: 开源中国
comments: false
date: Mon, 10 May 2021 15:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6413'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">open-monitor是一套基于Prometheus的分布式监控平台，适用于wecube，WeCube通过监控插件来对资源以及应用的监控及告警。此插件底层引用Prometheus，上层封装了对Prometheus的配置管理和图表展示，后端技术选型为Go + Gin + Xorm, 前端技术选型为Vue + ECharts。</span></p> 
<p style="text-align:left">此次版本包含以下内容。</p> 
<p style="text-align:start">新增：<br> 1、增加历史告警定时清理；<br> 2、调整k8s监控配置，增加namespace等信息；<br> 3、业务日志监控支持正则匹配转换；<br> 4、更新第三方redis-exporter版本；<br> 5、增加监控对象采集间隔配置。</p> 
<p style="text-align:start">修复：<br> 1、修复对象组阈值导入导出功能；<br> 2、修复node_exporter进程监控大小写区分问题；<br> 3、修复表单误操作关闭问题。</p>
                                        </div>
                                      
</div>
            