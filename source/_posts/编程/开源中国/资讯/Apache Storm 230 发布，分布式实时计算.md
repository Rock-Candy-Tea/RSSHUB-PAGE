
---
title: 'Apache Storm 2.3.0 发布，分布式实时计算'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8273'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8273'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache Storm 2.3.0 现已发布。Apache Storm 是一个分布式的、容错的、高性能的实时计算系统，为数据的处理提供了有力的保障。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li>新功能 
  <ul> 
   <li>在 docker 容器中启动 Storm Worker</li> 
   <li>使用 runc 运行时在容器内启动工作器</li> 
  </ul> </li> 
 <li>改进 
  <ul> 
   <li>添加快速、更可靠的进程活跃度检查</li> 
   <li>将 JCQueue 指标切换到新的指标 API</li> 
   <li>将 AutoTGT 指标更新为新 API</li> 
   <li>改进 PacemakerClient 错误消息</li> 
   <li>为类似于 LIMIT-MEM 的 worker childopts 添加 OFF-HEAP 宏</li> 
   <li> Ackers 和 metricComponents 分布不均</li> 
   <li>在调度中对喜欢/不喜欢节点中的公共节点进行文档处理</li> 
   <li>JCQueue 不应在指标名称中包含执行程序字符串</li> 
   <li>Hadoop TGT 更新异常的更改处理</li> 
   <li> 如果在拓扑 conf 或集群 conf 中为 true，storm.messaging.netty.authentication 应该为 true</li> 
   <li>用户页面应在所有者拓扑表中显示 storm 版本</li> 
   <li>删除消息队列以更新 Executor 凭据</li> 
   <li>Netty 服务器应该更好地处理传入的消息</li> 
   <li>继续支持 2.x 拓扑的 Pacemaker</li> 
   <li>改进由于工作程序最大堆大小不正确而导致提交拓扑的异常消息</li> 
   <li>守护程序指标报告器和拓扑指标报告器的单独配置</li> 
   <li>将 TopologySummary 方法添加到 NImbus 以获得最佳 UI 查询</li> 
   <li>更新 BuiltinMetrics 以使用 v2 Metrics API</li> 
   <li>在 ServerUtils 中消除 ps 命令并使用 /proc/ status</li> 
   <li>减少调试日志到调度程序日志</li> 
   <li>升级 netty 客户端指标以使用 V2 API</li> 
  </ul> </li> 
 <li>Bug 修复 
  <ul> 
   <li>修复 ArtifactoryConfigLoader.load 上的竞争条件</li> 
   <li>修复关于storm.supervisor.medium.memory.grace.period.ms 的逻辑错误</li> 
   <li>worker 应在其任务变更时自杀</li> 
   <li>由于 ShutdownHooks 引起的死锁和竞争条件，有问题的 worker 没有及时杀死</li> 
   <li>修复 Mockito 1.x 的拓扑无法运行单元测试的问题</li> 
   <li> 在重新平衡命令中验证组件名称并修复 --executor 选项</li> 
   <li> 如果分配为空，则修复 worker 自杀功能</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstorm.apache.org%2F2021%2F09%2F27%2Fstorm230-released.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            