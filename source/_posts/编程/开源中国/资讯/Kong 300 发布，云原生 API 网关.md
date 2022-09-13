
---
title: 'Kong 3.0.0 发布，云原生 API 网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2154'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2154'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Kong 是一款可扩展、快速且开源的微服务 API 网关，用于管理、保护与连接混合及云原生架构。</p> 
<p style="margin-left:0px">目前 Kong 发布了 3.0.0 版本，这个主要版本添加了一个用 Rust 编写的新路由器，和一个与 OpenTelemetry API 规范兼容的跟踪 API。此外，还进行了各种内部更改以提高 Kong 的性能和内存消耗。由于它是主要版本，建议用户查看更改列表，以确定升级时是否需要更改配置。</p> 
<h3><strong>重大变化</strong></h3> 
<ul> 
 <li>不支持从 2.1.0 之前的 Kong 进行蓝绿部署，升级到 2.1.0 或更高版本再升级到 3.0.0 进行蓝绿部署。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8896" target="_blank">#8896</a> </li> 
 <li>弃用/停止生产 Amazon Linux (1) 容器和软件包（2020 年 12 月 31 日停产）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fdocs.konghq.com%2Fpull%2F3966" target="_blank">#3966</a> </li> 
 <li>弃用/停止生产 Debian 8 “Jessie” 容器和软件包（2020 年 6 月停产）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong-distributions%2Fpull%2F766" target="_blank">#766</a></li> 
</ul> 
<h3 style="margin-left:0px">核心</h3> 
<ul> 
 <li>当给定上下文为“选择”时，Kong 模式库的 process_auto_fields 函数将不再制作传递给它的数据的深层副本。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8796" target="_blank">#8796</a> </li> 
 <li>Kong Plugin 或 DAO 模式中已弃用的简写字段已被删除，取而代之的是或键入的 shorthand_fields。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8815" target="_blank">#8815</a> </li> 
 <li>从 Kong 模式和 Kong 字段模式中删除了对 legacy = true/false 属性的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8958" target="_blank">#8958</a></li> 
 <li>Kong.serve_admin_api 已弃用的别名已被删除。如果自定义 Nginx 模板仍然使用它，请将其更改为 Kong.admin_content。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8815" target="_blank">#8815</a></li> 
 <li>删除了 dataplane 配置缓存，配置持久性现在使用 LMDB 自动完成。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fpull%2F8704" target="_blank">#8704</a> </li> 
</ul> 
<p> </p> 
<p>更多内容可以查看完整 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKong%2Fkong%2Fblob%2F3.0.0%2FCHANGELOG.md%23300" target="_blank"><strong>CHANGELOG</strong></a><strong>。</strong></p>
                                        </div>
                                      
</div>
            