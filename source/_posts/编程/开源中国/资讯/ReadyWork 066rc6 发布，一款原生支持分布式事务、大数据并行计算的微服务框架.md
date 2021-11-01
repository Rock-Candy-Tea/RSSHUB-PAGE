
---
title: 'Ready.Work 0.6.6.rc6 发布，一款原生支持分布式事务、大数据并行计算的微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4483'
author: 开源中国
comments: false
date: Mon, 01 Nov 2021 10:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4483'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:start">Ready.Work 0.6.6.rc6 发布，本次更新以下内容：</p> 
<p>1. 单体应用增加多数据源事务支持。<br> 2. 集群应用新增支持负载均衡优化器，可以将关联的分布式事务优化到同一个节点，提高性能。<br> 3. 框架缓存服务默认使用<span style="color:#1c1e21">caffeine，不在试用ehcache。<br> 4. JDBC事件支持优化，并新增数据变更事件，支持监听表格数据的insert/update/delete等行为。</span><br> <span style="color:#1c1e21">5. 切面编程新增支持自定义注解拦截器支持，新增java代码修改器支持。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">Ready.Work 是一款超简单，</span>原生支持分布式事务、大数据并行计算的微服务框架<span style="background-color:#ffffff; color:#333333">。框架特点如下：</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">易于使用</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架原生集成微服务组件，自动识别彼此，大幅度减少了微服务组件之间的耦合配置及微服务组件之间的依赖关系。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">节点自动发现</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">各节点自动发现，注册中心自动发现，配置中心自动发现，无中央节点，集群全节点分布式注册中心，不依赖第三方注册中心。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">应用模块化</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">支持模块化设计，每个应用可以分为多个模块进行开发和挂载，各模块拥有独立版本号，install, uninstall, load, unload逻辑，各模块可以拥有各自配置文件。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">分布式事务</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架原生分布式事务支持，无需依赖外部事务协调管理器或特别的服务支持，目前支持TCC、LCN(原生回滚)和TXC(补偿回滚)三种事务模型。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">分布式缓存</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架原生分布式 Key/Value 缓存支持，一般无需外部依赖 redis 或其他Key/Value数据库。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">分布式数据库</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架原生内置分布式数据库，无需外部依赖Mysql及其他数据库组件即可实现分库分表（开发中）。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">并行计算</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架原生并行计算支持，可将计算任务分发到各节点并行计算，支持类MapReduce操作模式。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">分布式限流</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">支持分布式限流，支持IP黑白名单每秒通过请求限流设定，支持每IP并发数限制及每线程下行速率限制，任意节点设定，其他节点自动应用相同设定。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">时间及ID服务</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架自行计算时间，不依赖主机或服务器系统时间，确保集群节点间时间统一可靠。建立在此时间保障下的改良版雪花分布式ID，无需担心时间回拨问题。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">事件驱动</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架支持事件驱动，事件监听器可以接收当前节点应用的内部事件，也可以接收集群节点事件，任意节点可以接收集群其他节点发出的特定全局事件。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">子域名支持</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架原生支持子域名解析，只需将泛域名解析到服务器，controller上可以直接注解指定子域名。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">敬请期待</h3> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">框架原生分布式OAUTH2，原生APM系统，原生审计及数据权限系统，原生分布式人工智能支持。</p> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start"><span style="color:#1c1e21">社区版第一个版本于国庆节发布，很多文档和测试用例还没来得及补上。本框架来源自开源社区，完全属于内部项目框架，考虑到或许有人也会有需要，拆分整理出来提供给需要到人。 比较仓促，很多地方尚不完善，也不优雅，如果您不喜欢，路过就好，如果对您有帮助，那就点个赞吧!  如果您有志加入本项目，或投资关联项目（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fready.work%2Fzh-CN%2Fmedicine%2F" target="_blank">分布式医疗数据辅助决策与科研平台</a><span style="color:#1c1e21">），请联系cleverbug@163.com</span></p> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#24292f">Gitee仓库：</span><a href="https://gitee.com/LyuWeihua/ReadyWork" target="_blank">https://gitee.com/LyuWeihua/ReadyWork</a><br> <span style="background-color:#ffffff; color:#24292f">Github仓库：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FLyuWeihua%2FReadyWork" target="_blank">https://github.com/LyuWeihua/ReadyWork</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fready.work%2Fzh-CN%2Fdocs%2F" target="_blank">https://ready.work/zh-CN/docs/</a></p>
                                        </div>
                                      
</div>
            