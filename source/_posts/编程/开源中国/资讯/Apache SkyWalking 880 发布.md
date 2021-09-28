
---
title: 'Apache SkyWalking 8.8.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2195'
author: 开源中国
comments: false
date: Tue, 28 Sep 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2195'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache SkyWalking 8.8.0 现已发布，SkyWalking 是观察性分析平台和应用性能管理系统 (APM)，提供分布式追踪、服务网格遥测分析、度量聚合和可视化一体化解决方案，支持 Java, .Net Core, PHP, NodeJS, Go, Lua 语言探针，支持 Envoy + Istio 构建的 Service Mesh。</span></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>将 javaagent 拆分为 skywalking-java 存储库</li> 
 <li>将来自 apache/skywalking-docker 的 Dockerfiles 合并到代码库中</li> 
 <li>kubernetes java 客户端从 12.0.1 升级到 13.0.0</li> 
 <li>添加事件 http 接收器</li> 
 <li>支持 MAL 中的度量级函数 serviceRelation</li> 
 <li>支持 Envoy 指标绑定到拓扑中</li> 
 <li>修复 openapi-definitions 文件夹未正确读取的问题</li> 
 <li>跟踪段不会被识别为 TopN 示例服务</li> 
 <li>删除段实体中的 version 和 endTime，减少索引负载</li> 
 <li>修复 ElasticSearch 7.14 中的 mapper_parsing_exception</li> 
 <li>支持 Go-Kratos 框架的组件 ID</li> 
 <li>删除跟踪查询条件中的端点名称，仅支持通过端点 id 查询。</li> 
 <li>修复了 OpenJDK 运行时环境中的 ProfileSnapshotExporterTest 案例</li> 
 <li>删除浏览器日志查询条件中的页面路径，只支持按页面路径 id 查询</li> 
 <li>删除后端日志查询条件中的端点名称，仅支持通过端点 id 查询</li> 
 <li>修复了存储实体 browser_error_log 的 page_path_id（was pate_path_id）列的拼写错误</li> 
 <li>为 Python falcon 插件添加组件 ID。</li> 
 <li>为 rpc.status_code 标签添加 rpcStatusCode，responseCode 字段被标记为已弃用并替换为 httpResponseStatusCode 字段</li> 
 <li>删除重复的标签以减少存储负载</li> 
 <li>添加新的 API 来测试日志分析语言</li> 
 <li>加强基于 Groovy 的 DSL、MAL 和 LAL 的安全性</li> 
 <li>支持动态配置核心中的集合类型</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202109.mbox%2F%253CCANh7qnQwVGGKJpOGa5VK9APXpPRvxgmMZS9GEv%3Dwod6j5Y%3DYCA%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            