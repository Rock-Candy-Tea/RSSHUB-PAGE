
---
title: 'Seata 1.5.2 正式发布，欢迎试用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=395'
author: 开源中国
comments: false
date: Mon, 25 Jul 2022 11:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=395'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0">Seata 1.5.2 正式发布。</h3> 
<p style="margin-left:0; margin-right:0">Seata 是一款开源的分布式事务解决方案，提供高性能和简单易用的分布式事务服务。</p> 
<p style="margin-left:0; margin-right:0">此版本更新如下：</p> 
<h3 style="margin-left:0; margin-right:0">feature：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4713" target="_blank">#4661</a>] 支持根据xid负载均衡算法</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4676" target="_blank">#4676</a>] 支持Nacos作为注册中心时，server通过挂载SLB暴露服务</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4642" target="_blank">#4642</a>] 支持client批量请求并行处理</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4567" target="_blank">#4567</a>] 支持where条件中find_in_set函数</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0">bugfix：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4515" target="_blank">#4515</a>] 修复develop分支SeataTCCFenceAutoConfiguration在客户端未使用DB时，启动抛出ClassNotFoundException的问题。</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4661" target="_blank">#4661</a>] 修复控制台中使用PostgreSQL出现的SQL异常</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4682" target="_blank">#4667</a>] 修复develop分支RedisTransactionStoreManager迭代时更新map的异常</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4678" target="_blank">#4678</a>] 修复属性transport.enableRmClientBatchSendRequest没有配置的情况下缓存穿透的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4701" target="_blank">#4701</a>] 修复命令行参数丢失问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4607" target="_blank">#4607</a>] 修复跳过全局锁校验的缺陷</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4696" target="_blank">#4696</a>] 修复 oracle 存储模式时的插入问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4726" target="_blank">#4726</a>] 修复批量发送消息时可能的NPE问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4729" target="_blank">#4729</a>] 修复AspectTransactional.rollbackForClassName设置错误</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4653" target="_blank">#4653</a>] 修复 INSERT_ON_DUPLICATE 主键为非数值异常</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0">optimize：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4650" target="_blank">#4650</a>] 修复安全漏洞</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4670" target="_blank">#4670</a>] 优化branchResultMessageExecutor线程池的线程数</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4662" target="_blank">#4662</a>] 优化回滚事务监控指标</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4693" target="_blank">#4693</a>] 优化控制台导航栏</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4700" target="_blank">#4700</a>] 修复 maven-compiler-plugin 和 maven-resources-plugin 执行失败</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4711" target="_blank">#4711</a>] 分离部署时 lib 依赖</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4720" target="_blank">#4720</a>] 优化pom描述</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4728" target="_blank">#4728</a>] 将logback版本依赖升级至1.2.9</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4745" target="_blank">#4745</a>] 发行包中支持 mysql8 driver</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4626" target="_blank">#4626</a>] 使用<span> </span><code>easyj-maven-plugin</code><span> </span>插件代替<span> </span><code>flatten-maven-plugin</code>插件，以修复<code>shade</code><span> </span>插件与<span> </span><code>flatten</code><span> </span>插件不兼容的问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4629" target="_blank">#4629</a>] 更新globalSession状态时检查更改前后的约束关系</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4662" target="_blank">#4662</a>] 优化 EnhancedServiceLoader 可读性</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0">test：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4544" target="_blank">#4544</a>] 优化TransactionContextFilterTest中jackson包依赖问题</li> 
 <li>[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Fpull%2F4731" target="_blank">#4731</a>] 修复 AsyncWorkerTest 和 LockManagerTest 的单测问题。</li> 
</ul> 
<p style="margin-left:0; margin-right:0">非常感谢以下 contributors 的代码贡献。若有无意遗漏，请报告。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fslievrly" target="_blank">slievrly</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpengten" target="_blank">pengten</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FYSF-A" target="_blank">YSF-A</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftuwenlin" target="_blank">tuwenlin</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F2129zxl" target="_blank">2129zxl</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FIfdevil" target="_blank">Ifdevil</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwingchi-leung" target="_blank">wingchi-leung</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frobynron" target="_blank">liurong</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopelok-z" target="_blank">opelok-z</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fa364176773" target="_blank">a364176773</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSmery-lxm" target="_blank">Smery-lxm</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flvekee" target="_blank">lvekee</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FdoubleDimple" target="_blank">doubleDimple</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwangliang181230" target="_blank">wangliang181230</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FBughue" target="_blank">Bughue</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAYue-94" target="_blank">AYue-94</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flingxiao-wu" target="_blank">lingxiao-wu</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcaohdgege" target="_blank">caohdgege</a></li> 
</ul> 
<p style="margin-left:0; margin-right:0">同时，我们收到了社区反馈的很多有价值的issue和建议，非常感谢大家。</p> 
<h4 style="margin-left:0; margin-right:0">Link</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>Seata:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata" target="_blank">https://github.com/seata/seata</a></li> 
 <li><strong>Seata-Samples:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata-samples" target="_blank">https://github.com/seata/seata-samples</a></li> 
 <li><strong>Release:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseata%2Fseata%2Freleases" target="_blank">https://github.com/seata/seata/releases</a></li> 
 <li><strong>WebSite:</strong><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fseata.io%2F" target="_blank">https://seata.io</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            