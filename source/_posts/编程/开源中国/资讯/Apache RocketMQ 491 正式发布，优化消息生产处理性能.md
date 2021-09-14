
---
title: 'Apache RocketMQ 4.9.1 正式发布，优化消息生产处理性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7467'
author: 开源中国
comments: false
date: Tue, 14 Sep 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7467'
---

<div>   
<div class="content">
                                                                                            <p>Apache RocketMQ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Flvivsq_9zAPB2BKekLlzmw" target="_blank">官宣</a>发布了 4.9.1 版本。据介绍，此<span style="color:#333333">版本包含 Improvement 30 个、bugfix 5 个、代码和文档优化 13 个，其中最值得关注的是小消息实时生产的 TPS 提升约 28%。</span></p> 
<p><span style="color:#333333">以下是 4.9.1 版本的重要修改，包括：</span></p> 
<h3>亮点</h3> 
<ul> 
 <li style="margin-left: 0px;">消息生产处理性能优化</li> 
</ul> 
<p style="margin-left:0; text-align:justify">在[ISSUE-2883] 中，针对消息生产性能进行了一系列优化，和 4.9.0 版本相比，小消息实时生产的 TPS 提升约 28%。该ISSUE包含6个PR，内容包括锁、线程、数据复制、数据编码等。</p> 
<h3 style="margin-left:0px; text-align:justify">改进</h3> 
<ul> 
 <li style="margin-left: 0px;">[ISSUE-3128] – ACL 支持删除全局白名单</li> 
</ul> 
<p style="margin-left:0; text-align:justify">支持通过 DefaultMQAdminExt 删除全局白名单</p> 
<ul> 
 <li style="margin-left: 0px; text-align: justify;">[ISSUE-2990] - mqadmin 增加消息跟踪选项</li> 
</ul> 
<p style="margin-left:0; text-align:justify">使用mqadmin发送消息时，可以通过 <code>-m </code>选项打开消息轨迹</p> 
<ul> 
 <li style="margin-left: 0px;">[ISSUE-3031] - netty-all版本升级到 4.1.65.Final</li> 
</ul> 
<p style="margin-left:0; text-align:justify">将Netty版本从4.0.42升级到4.1.65.Final，以支持在 JDK11 以上版本运行</p> 
<ul> 
 <li style="margin-left: 0px;">[ISSUE-2873]  [ISSUE-3009] - benchmark支持批量消息、定时消息</li> 
</ul> 
<p style="margin-left:0">增加支持对批量消息、定时消息进行benchmark，使得benchmark更完备</p> 
<ul> 
 <li style="margin-left: 0px;">[ISSUE-2715] – 支持可通过系统属性设置Netty属性</li> 
</ul> 
<p style="margin-left:0; text-align:justify">支持通过系统属性设置Netty相关属性，如connectTimeoutMillis、clientChannelMaxIdleTimeSeconds、clientCloseSocketIfTimeout等。</p> 
<h3 style="margin-left:0px; text-align:justify">Bug Fix</h3> 
<ul> 
 <li style="margin-left: 0px;">[ISSUE-2708] - 从 broker 异常获取 offset 时修复 offset 回滚的问题</li> 
</ul> 
<p style="margin-left:0; text-align:justify">针对Client初始化请求offset超时的情况，修复回退到正确的offset，而不是minLogicOffset。</p> 
<ul> 
 <li style="margin-left: 0px;">[ISSUE-3066] - 修复在一个进程中频繁启动和停止消费者时会产生幽灵消费者的问题registerConsumer()、unregisterConsumer()改为线程同步操作，避免同时启停消费者产生幽灵消费者。</li> 
</ul> 
<h3 style="margin-left:0px; text-align:justify">代码风格与文档优化</h3> 
<ul> 
 <li style="margin-left: 0px;">[ISSUE-3037]等ISSUE中添加了多个中文文档</li> 
</ul> 
<p style="margin-left:0px">详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Flvivsq_9zAPB2BKekLlzmw" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            