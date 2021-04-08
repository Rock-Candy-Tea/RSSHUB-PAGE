
---
title: 'MongoDB 4.4.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7336'
author: 开源中国
comments: false
date: Thu, 08 Apr 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7336'
---

<div>   
<div class="content">
                                                                                            <p>MongoDB 是一种面向文档的数据库管理系统，用 C++ 等语言撰写而成，以解决应用程序开发社区中的大量现实问题。MongoDB 由 MongoDB Inc. 于 2007 年 10 月开发，2009 年 2 月首度推出，现以服务器端公共许可（SSPL）分发。</p> 
<p>MongoDB 4.4.5 正式发布，本次更新内容如下：</p> 
<h3>修复：</h3> 
<ul> 
 <li>SERVER-55298: 调查并重现 BSONObjectTooLarge 错误；</li> 
 <li>SERVER-53566：调查并重现 "opCtx != nullptr && _opCtx == nullptr" 的不变式；</li> 
 <li>SERVER-51281：mongod live 被锁定；</li> 
 <li>SERVER-46686: Explain 不遵循 maxTimeMS；</li> 
 <li>SERVER-45836：在默认的日志级别提供更多的 LDAP 细节（如服务器 IP）；</li> 
 <li>所有 JIRA 问题在 4.4.5 中关闭；</li> 
</ul> 
<h3><strong>Sharding</strong></h3> 
<ul> 
 <li>SERVER-53462：改进 range-deleter 日志记录；</li> 
 <li>SERVER-53827：range_deleter_server_status.js 应该使用 assert.soon 来检查范围删除任务的数量；</li> 
 <li>SERVER-54014：为 checkOID 请求定义一个合理的 maxTimeMsOverride；</li> 
 <li>SERVER-54701：shardCollection 可能会成功地写入配置服务器，但最终在主 Shard 上缺少索引；</li> 
</ul> 
<h3>查询</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-48963" target="_blank">SERVER-48963</a>：使 max_time_ms_sharded.js 更强大</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjira.mongodb.org%2Fbrowse%2FSERVER-54710" target="_blank">SERVER-54710</a>： 大量的 <code>$or</code> 子句可以创建超过最大 BSON 大小的概要分析条目，从而导致查询失败；</li> 
</ul> 
<h3>存储</h3> 
<ul> 
 <li>SERVER-45847：将 JournalFlusher 从存储引擎层中拉出，并将其放在存储引擎的上方；</li> 
 <li>SERVER-46826 为短暂的引擎和非持久的引擎实例化 JournalFlusher 线程；</li> 
 <li>SERVER-48149：将 waitUntilDurable 的调用者移至 JournalFlusher::waitForJournalFlush 上；</li> 
 <li>SERVER-49191：将 oplogTruncateAfterPoint 缓存在内存中，只有当它发生变化时才进行更新；</li> 
 <li>SERVER-53875：停止 JournalFlusher 线程的运行，除非在单元测试中提出请求，这样它就不会访问仍在初始化的基础设施；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.mongodb.com%2Fmanual%2Frelease-notes%2F4.4%2F" target="_blank">https://docs.mongodb.com/manual/release-notes/4.4/</a></p>
                                        </div>
                                      
</div>
            