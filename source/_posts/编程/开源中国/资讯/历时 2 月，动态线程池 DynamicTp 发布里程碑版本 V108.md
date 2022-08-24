
---
title: '历时 2 月，动态线程池 DynamicTp 发布里程碑版本 V1.0.8'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://files.mdnice.com/user/25315/a6d7ec1d-e944-4e9a-a182-206541161b95.png'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 09:11:00 GMT
thumbnail: 'https://files.mdnice.com/user/25315/a6d7ec1d-e944-4e9a-a182-206541161b95.png'
---

<div>   
<div class="content">
                                                                                            <h2>关于 DynamicTp</h2> 
<p>DynamicTp 是一个基于配置中心实现的轻量级动态线程池管理工具，主要功能可以总结为动态调参、通知报警、运行监控、三方包线程池管理等几大类。</p> 
<p><img alt src="https://files.mdnice.com/user/25315/a6d7ec1d-e944-4e9a-a182-206541161b95.png" referrerpolicy="no-referrer"></p> 
<p><img height="406" src="https://oscimg.oschina.net/oscnet/up-df62e5ad0068906e1dafedbed6608516dd2.png" width="1040" referrerpolicy="no-referrer"></p> 
<p>经过多个版本迭代，目前最新版本 <strong>v1.0.8</strong> 具有以下特性</p> 
<p><strong>特性</strong> ✅</p> 
<ul> 
 <li> <p><strong>代码零侵入</strong>：所有配置都放在配置中心，对业务代码零侵入</p> </li> 
 <li> <p><strong>轻量简单</strong>：基于 springboot 实现，引入 starter，接入只需简单4步就可完成，顺利3分钟搞定</p> </li> 
 <li> <p><strong>高可扩展</strong>：框架核心功能都提供 SPI 接口供用户自定义个性化实现（配置中心、配置文件解析、通知告警、监控数据采集、任务包装等等）</p> </li> 
 <li> <p><strong>线上大规模应用</strong>：参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftech.meituan.com%2F2020%2F04%2F02%2Fjava-pooling-pratice-in-meituan.html" target="_blank">美团线程池实践</a>，美团内部已经有该理论成熟的应用经验</p> </li> 
 <li> <p><strong>多平台通知报警</strong>：提供多种报警维度（配置变更通知、活性报警、容量阈值报警、拒绝触发报警、任务执行或等待超时报警），已支持企业微信、钉钉、飞书报警，同时提供 SPI 接口可自定义扩展实现</p> </li> 
 <li> <p><strong>监控</strong>：定时采集线程池指标数据，支持通过 MicroMeter、JsonLog 日志输出、Endpoint 三种方式，可通过 SPI 接口自定义扩展实现</p> </li> 
 <li> <p><strong>任务增强</strong>：提供任务包装功能，实现TaskWrapper接口即可，如 MdcTaskWrapper、TtlTaskWrapper、SwTraceTaskWrapper，可以支持线程池上下文信息传递</p> </li> 
 <li> <p><strong>兼容性</strong>：JUC 普通线程池和 Spring 中的 ThreadPoolTaskExecutor 也可以被框架监控，@Bean 定义时加 @DynamicTp 注解即可</p> </li> 
 <li> <p><strong>可靠性</strong>：框架提供的线程池实现 Spring 生命周期方法，可以在 Spring 容器关闭前尽可能多的处理队列中的任务</p> </li> 
 <li> <p><strong>多模式</strong>：参考Tomcat线程池提供了 IO 密集型场景使用的 EagerDtpExecutor 线程池</p> </li> 
 <li> <p><strong>支持多配置中心</strong>：基于主流配置中心实现线程池参数动态调整，实时生效，已支持 Nacos、Apollo、Zookeeper、Consul、Etcd，同时也提供 SPI 接口可自定义扩展实现</p> </li> 
 <li> <p><strong>中间件线程池管理</strong>：集成管理常用第三方组件的线程池，已集成Tomcat、Jetty、Undertow、Dubbo、RocketMq、Hystrix等组件的线程池管理（调参、监控报警）</p> </li> 
</ul> 
<h2>依赖 groupId 变更</h2> 
<p>v1.0.8开始，依赖包的 groupId 从之前的 io.github.lyh200 改为 cn.dynamictp，对使用者透明。</p> 
<h2>v1.0.8 发布记录</h2> 
<p>距离 v1.0.7 发布已经有差不多 2 个月时间，这个里程碑版本新增了好些功能，同时优化重构了一些代码设计，欢迎大家升级体验哦！</p> 
<h4>Features</h4> 
<ul> 
 <li> <p>新增内存安全队列 MemorySafeLinkedBlockingQueue，感谢 @dragon-zhang 提供实现</p> </li> 
 <li> <p>WebServer 线程池管理支持 Reactive 环境下使用，感谢 @abbottliu.liu 提供实现</p> </li> 
 <li> <p>支持 Dubbox 线程池管理，感谢 @Redick01 提供实现</p> </li> 
 <li> <p>支持 Spring 中的 ThreadPoolTaskExecutor 线程池管理，感谢 @Redick01 提供实现</p> </li> 
 <li> <p>支持 Etcd 配置中心接入，感谢 @Redick01 提供实现</p> </li> 
 <li> <p>监控指标采集器新增输出到应用日志中的 InternalLogCollector，感谢 @Redick01 提供实现</p> </li> 
 <li> <p>三方中间件线程池通知告警支持别名配置，感谢 @renbiao002 提供实现</p> </li> 
 <li> <p>新增 extension 模块，放置一些扩展功能</p> </li> 
 <li> <p>三方中间件线程池管理支持通知告警功能</p> </li> 
 <li> <p>指标数据采集支持同时配置多种采集方式</p> </li> 
 <li> <p>新增 MdcTaskWrapper 任务包装器，支持 MDC 上下文传递</p> </li> 
 <li> <p>新增 SwTraceTaskWrapper 任务包装器，支持 Skywalking TID 传递</p> </li> 
 <li> <p>新增通知告警集群限流插件，见 extension-limiter-redis 模块</p> </li> 
 <li> <p>ThreadPoolCreator 类新增一些内存安全快捷创建线程池方法</p> </li> 
</ul> 
<h4>BugFix</h4> 
<ul> 
 <li> <p>兼容 JDK11 当前要设置核心线程数不能大于上次设置的最大线程数限制</p> </li> 
 <li> <p>修复核心线程预热设置 preStartAllCoreThreads 不生效问题</p> </li> 
 <li> <p>修复 Hystrix 线程池获取失败 & 调参被覆盖问题</p> </li> 
 <li> <p>修复采集类型为logging模式时，配置更新后日志输出到应用日志中的问题</p> </li> 
</ul> 
<h4>Refactor</h4> 
<ul> 
 <li> <p>重构 logging 模块，去掉事件监听依赖</p> </li> 
 <li> <p>重构抽象 adapter 模块代码</p> </li> 
 <li> <p>责任链模式重构 notify 模块</p> </li> 
</ul> 
<h4>Optimize</h4> 
<ul> 
 <li> <p>example 添加 Hystrix 线程池的测试例子</p> </li> 
 <li> <p>低版本 Apollo 配置文件格式兼容</p> </li> 
 <li> <p>Undertow 容器开启活跃线程池数采集功能</p> </li> 
 <li> <p>Endpoint 端点接口支持三方中间件线程池指标数据获取</p> </li> 
 <li> <p>优化三方中间件参数刷新逻辑，增加校验判断逻辑及日志输出</p> </li> 
 <li> <p>各模块代码优化</p> </li> 
</ul> 
<h2>项目地址</h2> 
<p>目前累计 1.6k star，感谢你的 star，欢迎 pr，业务之余一起给开源贡献一份力量</p> 
<p><strong>官网</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdynamictp.cn" target="_blank">https://dynamictp.cn</a></p> 
<p><strong>gitee地址</strong>：<a href="https://gitee.com/dromara/dynamic-tp">https://gitee.com/dromara/dynamic-tp</a></p> 
<p><strong>github地址</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fdynamic-tp" target="_blank">https://github.com/dromara/dynamic-tp</a></p> 
<h2>加入社群</h2> 
<p><strong>看到这儿，方便的话给项目一个 star，你的支持是我们前进的动力！</strong></p>
                                        </div>
                                      
</div>
            