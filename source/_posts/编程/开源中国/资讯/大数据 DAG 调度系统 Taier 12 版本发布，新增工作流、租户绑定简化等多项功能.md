
---
title: '大数据 DAG 调度系统 Taier 1.2 版本发布，新增工作流、租户绑定简化等多项功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f51e52de112d6cd6cc683f783e9db6e1ed0.png'
author: 开源中国
comments: false
date: Wed, 27 Jul 2022 10:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f51e52de112d6cd6cc683f783e9db6e1ed0.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2022 年 7 月 26 日，Taier1.2 版本正式发布！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次版本发布更新功能：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增工作流</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 OceanBase SQL</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 Flink jar 任务</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">数据同步、实时采集支持脏数据管理</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Hive UDF</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">控制台 UI 升级</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">租户绑定简化</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本的使用文档已在社区中推送，大家可以随时下载查阅，欢迎大家体验新版本功能 **（喜欢我们的项目欢迎大家点个 Star）**，体验地址：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDTStack%2FTaier" target="_blank">https://github.com/DTStack/Taier</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dtstack_dev_0/taier">https://gitee.com/dtstack_dev_0/taier</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">社区：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdtstack.github.io%2FTaier%2F" target="_blank">https://dtstack.github.io/Taier/</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"> </h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left">Taier1.2 版本介绍</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Taier 是一个大数据分布式可视化的 DAG 任务调度系统，旨在降低 ETL 开发成本、提高大数据平台稳定性，大数据开发人员可以在 Taier 直接进行业务逻辑的开发，而不用关心任务错综复杂的依赖关系与底层的大数据平台的架构实现，将工作的重心更多地聚焦在业务之中。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Taier 脱胎于袋鼠云数栈，技术实现来源于数栈分布式调度引擎 DAGScheduleX，是数栈产品的重要基础设施之一，负责大数据平台所有任务实例的调度运行。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2022 年 2 月 22 日，Taier 正式开源并发布 1.0 版本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2022 年 5 月 8 日，Taier1.1 版本发布，更新对 Flink 的支持升级到 Flink1.12，支持多种流类型任务等功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2022 年 7 月 26 日，Taier1.2 版本发布，本次发布重点新增工作流功能，实现配置化编排业务；租户简化绑定，不同类型计算组件无强制依赖等功能。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"> </h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left">Taier1.2 新增功能详解</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">1. 新增工作流</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">通过可视化操作拖动任务节点到画板中，手动连接上下游任务组成依赖关系，形成一个 DAG 的工作流。同时支持任意类型的任务通过工作流拖拽的方式，直接实现配置化编排业务</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-f51e52de112d6cd6cc683f783e9db6e1ed0.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">2. 新增 OceanBase SQL</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增 OceanBaseSQL 任务，支持 OceanBaseSQL 的任务调度和运维展示。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">3. 新增 Flink jar 任务</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">支持上传自定义开发的 Flink jar 任务，通过 Taier 提交运行和监控。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">4. 数据同步、实时采集支持脏数据管理</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据同步、实时采集支持脏数据管理，可以配置脏数据数量限制和保存方式，可保存至数据库实时查看。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">5.Hive UDF</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Hive SQL 支持 udf 函数开发配置。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">6. 控制台 UI 升级</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">控制台交互和页面全新升级，通过树形结构展示组件配置信息，同时支持扩展自定义组件进行配置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-24b44548c674471c1d59931cec36da34cf7.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">7. 租户绑定简化</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">集群和租户绑定简化，移除租户对接集群 schema 的强制绑定关系，不同类型计算组件无强制依赖；优化任务开发流程逻辑，支持自定义扩展任务类型。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"> </h1> 
<h1 style="margin-left:0; margin-right:0; text-align:left">未来规划</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Taier 自今年 2 月份开源以来，已更新迭代 Taier1.1、Taier1.2 两个版本，目前 Taier1.3 的版本已在规划中，在新版本中我们将着重解决以下几个问题：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">支持 Flink Standalone 不依赖 Hadoop 也可以使用 Flink 相关的功能，降低上手环境成本</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">适配开发者 Window 环境，支持 Window 环境下的任务提交流程</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">DatouSourceX 版本升级，新增更多的数据源类型支持</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了不断保持迭代更新外，Taier 将持续保持每月一次开源技术直播，帮助 Taier 开发者们更好的使用产品，欢迎有兴趣的小伙伴们加入我们的交流社群（钉钉 qun：30537511），一起交流 Taier 的技术问题及难点，和 Taier 一起共同进步！</p> 
<p> </p>
                                        </div>
                                      
</div>
            