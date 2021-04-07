
---
title: 'open-monitor 1.10.0 版本发布，基于 Prometheus 的分布式监控平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1002'
author: 开源中国
comments: false
date: Wed, 07 Apr 2021 14:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1002'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">open-monitor是一套基于Prometheus的分布式监控平台，适用于wecube，WeCube通过监控插件来对资源以及应用的监控及告警。此插件底层引用Prometheus，上层封装了对Prometheus的配置管理和图表展示，后端技术选型为Go + Gin + Xorm, 前端技术选型为Vue + ECharts。</span></p> 
<p style="text-align:left">此次版本包含以下内容。</p> 
<p style="text-align:start">新增：<br> 1、对象视图界面增加历史告警展示<br> 2、更新Docker基础镜像，更新Prometheus版本<br> 3、关键字监控增加对象关联<br> 4、关键字监控支持正则匹配<br> 5、关键字监控支持告警是否发送通知选项<br> 6、指标设计增加对象视图编辑<br> 7、调整告警配置交互，移动部分按钮与表单</p> 
<p style="text-align:start">修复：<br> 1、告警列表分类统计图逻辑优化<br> 2、修复插件模式前端冲突<br> 3、修复多实例告警重复发送问题<br> 4、修复角色同步失败问题<br> 5、ping_exporter修复请求超时指标不显示问题<br> 6、修复对象搜索SQL延时注入问题</p>
                                        </div>
                                      
</div>
            