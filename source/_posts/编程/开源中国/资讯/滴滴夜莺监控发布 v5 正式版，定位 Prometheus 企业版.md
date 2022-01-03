
---
title: '滴滴夜莺监控发布 v5 正式版，定位 Prometheus 企业版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-89ad644047eeb062daa21de516d6eda126c.png'
author: 开源中国
comments: false
date: Mon, 03 Jan 2022 12:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-89ad644047eeb062daa21de516d6eda126c.png'
---

<div>   
<div class="content">
                                                                                            <p>大家好，经过几个月的研发，夜莺v5正式版跟大家见面了，这个版本做了巨大的产品定位调整，不再是一个运维平台，而是专注监控告警这个细分领域，拥抱Prometheus生态，争取把监控这个事情，做到极致！这是新版的截图，给大家一个直观的认识先。</p> 
<p><img height="982" src="https://oscimg.oschina.net/oscnet/up-89ad644047eeb062daa21de516d6eda126c.png" width="1964" referrerpolicy="no-referrer"></p> 
<p>这个版本的功能设计全部是围绕监控告警来的，比如告警规则、屏蔽规则、订阅规则的管理，活跃告警、历史告警的查看，监控数据查看，提供不同的看图视角，监控对象的管理，告警自愈机制，人员权限等等</p> 
<p> </p> 
<p><strong>为啥开始拥抱Prometheus生态呢？</strong></p> 
<p>核心是PromQL的能力，作为一款完备的监控产品，一定要具备QL的能力，否则灵活性将大大降低，之前Open-Falcon或者Nightingale的老版本，只能通过标签做匹配，灵活性不好，需要把一些计算逻辑前置到采集侧，新版本我们想解决这个问题，但是重复造轮子也不可取，所以就沿用了PromQL的能力。</p> 
<p>这个版本非常的开放，不止可以和Prometheus深度集成，也可以和Telegraf、Grafana、Grafana-Agent、Datadog-Agent、VictoriaMetrics、M3DB等良好协同，没有软件绑定问题。</p> 
<p> </p> 
<p><strong>与Open-Falcon的区别</strong></p> 
<p style="color:#323232; margin-left:0; margin-right:0; text-align:start">因为开发Open-Falcon和Nightingale的是一拨人，所以很多社区伙伴会比较好奇，为何要新做一个监控开源软件。核心点是Open-Falcon和Nightingale的差异点实在是太大了，Nightingale并非是Open-Falcon设计逻辑的一个延续，就看做两个不同的软件就好。</p> 
<p style="color:#323232; margin-left:0; margin-right:0; text-align:start">Open-Falcon是14年开发的，当时是想解决Zabbix的一些容量问题，可以看做是物理机时代的产物，整个设计偏向运维视角，虽然数据结构上已经开始设计了标签，但是查询语法还是比较简单，无法应对比较复杂的场景。</p> 
<p style="color:#323232; margin-left:0; margin-right:0; text-align:start">Nightingale直接支持PromQL，支持Prometheus、M3DB、VictoriaMetrics多种时序库，支持Telegraf做监控数据采集，支持Grafana看图，整个设计更加云原生，虽然也保留了机器归组的逻辑以应对物理机时代的需求，但是设计上，更倾向于使用标签来分组，而不是HostGroup或者树形结构。</p> 
<p style="color:#323232; margin-left:0; margin-right:0; text-align:start"> </p> 
<p><strong>与Prometheus的区别</strong></p> 
<p style="color:#323232; margin-left:0; margin-right:0; text-align:start">Nightingale可以简单看做是Prometheus的一个企业级版本，把Prometheus当做Nightingale的一个内部组件-时序库，当然，也不是必须的，时序库除了Prometheus，还可以使用VictoriaMetrics、M3DB等。各种Exporter也可以继续使用，不过我们更推荐使用All-in-one的Telegraf，运维代价会更小一些。</p> 
<p style="color:#323232; margin-left:0; margin-right:0; text-align:start">Nightingale可以接入多个Prometheus/M3DB/VictoriaMetrics，可以允许用户在页面上配置告警规则、屏蔽规则、订阅规则，在页面上查看告警事件，配置告警自愈机制，管理监控对象，配置监控大盘等，就把Nightingale看做是Prometheus的一个WEBUI也是可以的，不过实际上，它远远不止是一个WEBUI，用一下就会深有感触。</p> 
<p> </p> 
<p><strong>夜莺v5版本架构</strong></p> 
<p><span style="background-color:#ffffff; color:#323232">夜莺v5的设计非常简单，核心是server和webapi两个模块，webapi无状态，放到中心端，承接前端请求，将用户配置写入数据库；server是告警引擎和数据转发模块，一般随着时序库走，一个时序库就对应一套server，每套server可以只用一个server实例，也可以多个实例组成集群，server可以接收Telegraf上报的数据，写入后端时序库，周期性从数据库同步告警规则，然后查询时序库做告警判断。每套server依赖一个redis。架构图如下：</span></p> 
<p><img height="846" src="https://oscimg.oschina.net/oscnet/up-801edcc939934ff481e52ffa6972cd429f5.png" width="1762" referrerpolicy="no-referrer"></p> 
<p>新版本的文档放到了gitee.io，地址是 https://n9e.gitee.io/ 感谢开源中国提供的平台，访问速度挺快的 :)</p>
                                        </div>
                                      
</div>
            