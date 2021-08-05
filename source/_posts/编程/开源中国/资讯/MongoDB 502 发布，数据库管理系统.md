
---
title: 'MongoDB 5.0.2 发布，数据库管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3187'
author: 开源中国
comments: false
date: Thu, 05 Aug 2021 06:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3187'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MongoDB 是一种面向文档的数据库管理系统，用 C++ 等语言撰写而成，以解决应用程序开发社区中的大量现实问题。MongoDB 由 MongoDB Inc. 于 2007 年 10 月开发，2009 年 2 月首度推出，现以服务器端公共许可（SSPL）分发。</p> 
<p>MongoDB 5.0.2 正式发布，本次更新内容如下：</p> 
<h3><strong>Sharding：</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-47372" target="_blank">SERVER-47372</a> config.cache 集合即使在集合被放弃后仍然可以保留；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-50521" target="_blank">SERVER-50521</a> 在创建临时 resharding 集合后，写入 reshardBegin no-op oplog 条目；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-56647" target="_blank">SERVER-56647</a> 使 dropDatabase 对网络分区具有弹性 ；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-57488" target="_blank">SERVER-57488</a> 创建命令，从 config.tags 中删除与 ns 匹配的标签，这些标签可以作为可重试的写入运行。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-57496" target="_blank">SERVER-57496</a> 在删除数据库/集合后主动逐出缓存的条目</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-57559" target="_blank">SERVER-57559</a> 为 DDL 协调器实施 LSID 缓存</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58465" target="_blank">SERVER-58465</a> 修复了重命名操作中路由信息的清理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58535" target="_blank">SERVER-58535</a> _shardsvrRenameCollection 应在降级时中断</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58589" target="_blank">SERVER-58589</a> 删除 ShardingFullDDLSupportTimestampedVersion 功能标志</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58624" target="_blank">SERVER-58624</a> 更改 reshard_collection_basic.js 的 resharding 临界区超时值</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58747" target="_blank">SERVER-58747</a> ShardServerCatalogCacheLoader 在升级时不会中断正在进行的操作</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58749" target="_blank">SERVER-58749</a> 删除数据库协调器必须获取集合分布式锁</li> 
</ul> 
<h3>Replication：</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-37904" target="_blank">SERVER-37904</a> 允许一个节点覆盖集群链（启用/禁用）的设置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58625" target="_blank">SERVER-58625</a> 在 geo_update1.js 中增加 multi_update 标签，以从某些套件中排除。</li> 
</ul> 
<h3><strong>Query</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-54078" target="_blank">SERVER-54078</a> [SBE] 提高 bestbuy_agg_merge_wordcount 基准套件的性能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58127" target="_blank">SERVER-58127</a> 修复 benchRun() 内存泄漏，用于在异常情况下解析 benchRun() args</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58372" target="_blank">SERVER-58372</a> 加强 deprecated_wire_ops_mongos.js</li> 
</ul> 
<h3><strong>Operations</strong></h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58510" target="_blank">SERVER-58510</a> 修复了 getExecutorForSimpleDistinct() 函数中的 UAF 问题</p> 
<h3><strong>Build and Packaging</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-54729" target="_blank">SERVER-54729</a>  MongoDB Enterprise Debian/Ubuntu 软件包应依赖于 libsasl2-modules 和 libsasl2-modules-gssapi-mit</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-55446" target="_blank">SERVER-55446</a> 在支持 Xcode 12 的主机上建立 Apple Silicon 仅编译构建器。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.mongodb.com%2Fv5.0%2Frelease-notes%2F5.0-changelog%2F%235.0.2-changelog" target="_blank">https://docs.mongodb.com/v5.0/release-notes/5.0-changelog/#5.0.2-changelog</a></p>
                                        </div>
                                      
</div>
            