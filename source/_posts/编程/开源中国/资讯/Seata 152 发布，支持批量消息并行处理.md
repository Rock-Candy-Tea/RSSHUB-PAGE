
---
title: 'Seata 1.5.2 发布，支持批量消息并行处理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6046'
author: 开源中国
comments: false
date: Thu, 14 Jul 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6046'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Seata 是一款开源的分布式事务解决方案，提供高性能和简单易用的分布式事务服务。</p> 
<p>目前 Seata 发布了 1.5.2 版本，带来如下修改：</p> 
<h3>新功能</h3> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4713" target="_blank">#4661</a> ] 支持 xid 一致性负载均衡</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4676" target="_blank">#4676</a> ] 支持服务器通过挂载 SLB 暴露 Nacos 服务</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4642" target="_blank">#4642</a> ] 支持批量消息并行处理</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4567" target="_blank">#4567</a> ] 支持 where 方法条件（find_in_set）</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4515" target="_blank">#4515</a> ] 修复未使用数据库时 SeataTCCFenceAutoConfiguration 的错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4661" target="_blank">#4661</a> ] 修复模块控制台中 PostgreSQL 的 sql 异常</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4682" target="_blank">#4667</a> ] 修复 RedisTransactionStoreManager 在迭代期间更新 map 的异常</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4678" target="_blank">#4678</a> ] 修复 key transport.enableRmClientBatchSendRequest 缓存穿透如果不配置的错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4701" target="_blank">#4701</a> ] 修复缺少的命令行参数</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4607" target="_blank">#4607</a> ] 修复跳过锁检查的错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4696" target="_blank">#4696</a> ] 修复 oracle 数据库插入值</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4726" target="_blank">#4726</a> ] 修复批量消息发送可能返回 NullPointException</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4729" target="_blank">#4729</a> ] 修复 set AspectTransactional.rollbackForClassName 的值错误</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4653" target="_blank">#4653</a> ] 修复 INSERT_ON_DUPLICATE SQL 中 pk 为非数字时的 sql 异常</li> 
</ul> 
<h3><strong>优化</strong></h3> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4650" target="_blank">#4650</a> ] 修复一些安全漏洞</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4670" target="_blank">#4670</a> ] 优化 branchResultMessageExecutor 的线程池大小</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4662" target="_blank">#4662</a> ] 优化回滚事务指标</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4693" target="_blank">#4693</a> ] 优化控制台导航栏</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4700" target="_blank">#4700</a> ] 修复 maven-compiler-plugin 和 maven-resources-plugin 执行失败</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4711" target="_blank">#4711</a> ] 为部署单独的 lib 依赖项</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4720" target="_blank">#4720</a> ] 优化pom描述</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4728" target="_blank">#4728</a> ] 升级 logback 依赖到 1.2.9</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4745" target="_blank">#4745</a> ] 发布包支持mysql8</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4626" target="_blank">#4626</a> ] 替换<code>flatten-maven-plugin</code>为<code>easyj-maven-plugin</code>，以解决<code>shade</code>和 <code>flatten</code> 间的冲突</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4629" target="_blank">#4629</a> ] 更新全局会话时，检查前后状态的关系</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4662" target="_blank">#4662</a> ] 使 EnhancedServiceLoader 更具可读性</li> 
</ul> 
<h3><strong>测试</strong></h3> 
<ul> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4544" target="_blank">#4544</a> ] 优化 TransactionContextFilterTest 中的 jackson 依赖项</li> 
 <li>[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4731" target="_blank">#4731</a> ] 修复 AsyncWorkerTest 和 LockManagerTest 中的 UT 失败</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Freleases%2Ftag%2Fv1.5.2" target="_blank">https://github.com/seata/seata/releases/tag/v1.5.2</a></p>
                                        </div>
                                      
</div>
            