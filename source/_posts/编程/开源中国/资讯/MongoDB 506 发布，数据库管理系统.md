
---
title: 'MongoDB 5.0.6 发布，数据库管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3583'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3583'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">MongoDB 是一种面向文档的数据库管理系统，用 C++ 等语言撰写而成，以解决应用程序开发社区中的大量现实问题。MongoDB 由 MongoDB Inc. 于 2007 年 10 月开发，2009 年 2 月首度推出，现以服务器端公共许可（SSPL）分发。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">MongoDB 5.0.6 现已正式发布，本次更新内容如下：</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">Platform Support</h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Community Edition</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#21313c">从 MongoDB 5.0.6 开始，不再支持以下平台：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>RHEL -72-s390x</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">Sharding</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-45149" target="_blank">SERVER-45149</a> txn_two_phase_commit_failover.js 中的 replSetStepDown 命令不应超时</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-56127" target="_blank">SERVER-56127</a> 如果 chunk 被迁移并且 shard key pattern 使用嵌套字段，Retryable update 可能会执行多次</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-56227" target="_blank">SERVER-56227</a> 添加面向用户的命令，为 sharded collection 设置 allowMigrations 为 false。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-60624" target="_blank">SERVER-60624</a> txn_commit_optimizations_for_read_only_shards.js 暂停协调器上的复制，并且可能使 transaction 卡在准备阶段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-60682" target="_blank">SERVER-60682</a> TransactionCoordinator 可能会阻止获取 WiredTiger 写票以坚持其决定，从而延长 transactions 处于准备状态</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-60860" target="_blank">SERVER-60860</a> 在最接近的情况下，ReshardingCollectionCloner 使用 primary 读取 preference</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-61003" target="_blank">SERVER-61003</a> 来自 ShardRegistry 的 ReadConcernMajorityNotAvailableYet errors 必须重试</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-61105" target="_blank">SERVER-61105</a> moveChunk 期间的会话迁移逻辑污染日志</li> 
 <li>......</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Replication </strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-59721" target="_blank">SERVER-59721</a> 执行回滚到稳定时间戳后，节点可能无法与其他 members 同步</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Query</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-57588" target="_blank">SERVER-57588</a> 当数组位置被索引其值为数组时，查询结果不一致</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#21313c"><strong>Storage</strong></span></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-30846" target="_blank">SERVER-30846</a> 在 FSM 测试中将 dbCheck 作为后台工作负载运行</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-55483" target="_blank">SERVER-55483</a> 添加一个新的启动参数，跳过验证表日志设置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58409" target="_blank">SERVER-58409</a> Startup RecordId 初始化存在持久历史和重建准备事务的缺陷</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#21313c"><strong>Operations</strong></span></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-28953" target="_blank">SERVER-28953</a> 在 FTDC 中捕获 df（disk full）统计信息</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">Internals</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-49748" target="_blank">SERVER-49748</a> 初始同步应在任何其他集合之前克隆 admin.system.version</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-54468" target="_blank">SERVER-54468</a> 启用最小化支持 sharding time-series collections 的特性标志</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-56167" target="_blank">SERVER-56167</a> 保证挂起分析器至少收集 sharded clusters 的核心转储</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-57037" target="_blank">SERVER-57037</a> 提高 operator counters 的精度</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-57289" target="_blank">SERVER-57289<span> </span></a>redact 不应将 BSONArray 转换为 BSONObj</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-58135" target="_blank">SERVER-58135</a> ReplSetTest 在禁用链接的 replica sets 中启动失败</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-59781" target="_blank">SERVER-59781</a> multi_statement_transaction.js 不在 StaleConfig 上重试 transaction</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-60217" target="_blank">SERVER-60217</a> [v5.0] enableReconfigRollbackCommittedWritesCheck 应应用于 4.4</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-60310" target="_blank">SERVER-60310</a> OCSP 响应验证不应考虑不相关证书的状态</li> 
 <li>......</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.mongodb.com%2Fv5.0%2Frelease-notes%2F5.0-changelog%235.0.6-changelog" target="_blank">https://docs.mongodb.com/v5.0/release-notes/5.0-changelog#5.0.6-changelog</a></p>
                                        </div>
                                      
</div>
            