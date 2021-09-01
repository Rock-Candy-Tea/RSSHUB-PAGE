
---
title: 'Apache RocketMQ 4.9.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3831'
author: 开源中国
comments: false
date: Wed, 01 Sep 2021 06:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3831'
---

<div>   
<div class="content">
                                                                                            <p>Apache RocketMQ 4.9.1 已发布，此版本的更新内容包括功能改进、Bugfix 以及文档和代码风格的优化。</p> 
<h2>改进</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3199" target="_blank">ISSUE-3199</a>] - RequestFutureTable 的两次定时任务</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3196" target="_blank">ISSUE-3196</a>] - 在使用"requestHeader.getTopic()"之前检查"requestHeader"是否为空</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3185" target="_blank">ISSUE-3185</a>] - 移除 travis ci 中的 arm 机器测试</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3177" target="_blank">ISSUE-3177</a>] - 对所有 brokers 中的 AclConfig 进行升级</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3030" target="_blank">ISSUE-3030</a>] - 当使用 G1 时移除 -Xmn JVM 参数</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3162" target="_blank">ISSUE-3162</a>] - 在 transaction producer 的基准测试中添加 msgTraceEnable 配置</li> 
</ul> 
<h2>Bugfix</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3175" target="_blank">ISSUE-3175</a>] - 修复 UpdateAclConfig 导致 broker 无法启动的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F2708" target="_blank">ISSUE-2708</a>] - 从 broker 异常获取 offset 时修复 offset 回滚的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3066" target="_blank">ISSUE-3066</a>] - 修复在一个进程中频繁启动和停止消费者时会产生幽灵消费者的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3118" target="_blank">ISSUE-3118</a>] - 修复当批量消息发送触发 pending full 会发生类型转换异常的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3019" target="_blank">ISSUE-3019</a>] - 修复批量发送消息统计的错误</li> 
</ul> 
<h2>优化文档和代码风格</h2> 
<ul> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3097" target="_blank">ISSUE-3097</a>] - 删除文档中过时和错误的配置信息</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3059" target="_blank">ISSUE-3059</a>] - 修复 Example_Transaction.md 的英文版本</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3055" target="_blank">ISSUE-3055</a>] - 为 API_Reference_DefaultMQProducer 英文版本添加部分文档</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3042" target="_blank">ISSUE-3042</a>] - 添加 SyncProducer 示例</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3037" target="_blank">ISSUE-3037</a>] - 添加 Deployment.md 的中文版本</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3063" target="_blank">ISSUE-3063</a>] - 添加 Example_Delay.md 的中文版本</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Frocketmq%2Fissues%2F3061" target="_blank">ISSUE-3061</a>] - 添加不同的发送示例和 FAQ.md 的中文版本</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frocketmq.apache.org%2Frelease_notes%2Frelease-notes-4.9.1%2F" target="_blank">详情查看 release note</a>。</p> 
<p>值得注意的是，上一个版本 Apache RocketMQ 4.9.0 是一个大版本更新，此版本包含大量的优化和问题修复，极大地提高了 RocketMQ 的分布式可观测性，主要在于：</p> 
<ul> 
 <li> <p>可见性全面提升，RocketMQ Client 客户端支持 OpenTracing 消息追踪插件</p> </li> 
 <li> <p>消息轨迹支持 LitePullConsumer 和事务消息的轨迹</p> </li> 
 <li> <p>Broker 启动依赖项全面梳理优化，启动过程更为顺畅</p> </li> 
 <li> <p>提升 LitePullConusmer Rebalance 效率及稳定性</p> </li> 
 <li> <p>提升了单测稳定性以及核心代码覆盖率</p> </li> 
 <li> <p>性能测试 Benchmark 部分增强，为 5.0 全新架构发布性能基线测试做好充分准备</p> </li> 
 <li> <p>提升事务消息运维管控的健壮性</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FJTNSFaidNqrctqyk5X9UzA" target="_blank">详情点此查看</a>。</p>
                                        </div>
                                      
</div>
            