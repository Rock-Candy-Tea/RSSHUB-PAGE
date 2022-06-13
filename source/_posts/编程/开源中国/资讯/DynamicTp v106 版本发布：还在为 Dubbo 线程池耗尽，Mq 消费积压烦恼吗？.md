
---
title: 'DynamicTp v1.0.6 版本发布：还在为 Dubbo 线程池耗尽，Mq 消费积压烦恼吗？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129af3b9192d42cd87ecd8c5f603caf5~tplv-k3u1fbpfcp-watermark.image'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 09:39:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129af3b9192d42cd87ecd8c5f603caf5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="content">
                                                                                            <h2><span>DynamicTp 简介</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">DynamicTp 是一个基于配置中心实现的轻量级动态线程池管理工具，主要功能可以总结为 动态调参、通知报警、运行监控、三方包线程池管理等几大类。</p> 
<p style="color:black; margin-left:0; margin-right:0">经过几个版本迭代，目前最新版本v1.0.6具有以下特性</p> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">特性</strong> ✅</p> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">代码零侵入</strong>：所有配置都放在配置中心，对业务代码零侵入</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">轻量简单</strong>：基于 springboot 实现，引入 starter，接入只需简单4步就可完成，顺利3分钟搞定</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">高可扩展</strong>：框架核心功能都提供 SPI 接口供用户自定义个性化实现（配置中心、配置文件解析、通知告警、监控数据采集、任务包装等等）</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">线上大规模应用</strong>：参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftech.meituan.com%2F2020%2F04%2F02%2Fjava-pooling-pratice-in-meituan.html" target="_blank">美团线程池实践</a>，美团内部已经有该理论成熟的应用经验</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">多平台通知报警</strong>：提供多种报警维度（配置变更通知、活性报警、容量阈值报警、拒绝触发报警、任务执行或等待超时报警），已支持企业微信、钉钉、飞书报警，同时提供 SPI 接口可自定义扩展实现</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">监控</strong>：定时采集线程池指标数据，支持通过 MicroMeter、JsonLog 日志输出、Endpoint 三种方式，可通过 SPI 接口自定义扩展实现</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">任务增强</strong>：提供任务包装功能，实现TaskWrapper接口即可，如 TtlTaskWrapper 可以支持线程池上下文信息传递，以及给任务设置标识id，方便问题追踪</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">兼容性</strong>：JUC 普通线程池也可以被框架监控，@Bean 定义时加 @DynamicTp 注解即可</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">可靠性</strong>：框架提供的线程池实现 Spring 生命周期方法，可以在 Spring 容器关闭前尽可能多的处理队列中的任务</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">多模式</strong>：参考Tomcat线程池提供了 IO 密集型场景使用的 EagerDtpExecutor 线程池</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">支持多配置中心</strong>：基于主流配置中心实现线程池参数动态调整，实时生效，已支持 Nacos、Apollo、Zookeeper、Consul，同时也提供 SPI 接口可自定义扩展实现</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">中间件线程池管理</strong>：集成管理常用第三方组件的线程池，已集成Tomcat、Jetty、Undertow、Dubbo、RocketMq、Hystrix等组件的线程池管理（调参、监控报警）</p> </li> 
</ul> 
<h2><span>官网上线</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">随着v1.0.6的发布我们上线了DynamicTp官网：https://dynamictp.cn</p> 
<p style="color:black; margin-left:0; margin-right:0">介绍文档、使用说明等都可以查看官网了解更多，以后新特性也会优先发布到官网上</p> 
<p style="color:black; margin-left:0; margin-right:0">欢迎大家体验 👏🏻</p> 
<p><img alt src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/129af3b9192d42cd87ecd8c5f603caf5~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
<h2><span>v1.0.6 发布记录</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">距离v1.0.5发布已经有差不多2个月时间，这个版本框架源码调整还是比较大的，重构了好一些功能，主要是围绕第三方中间件线程池集成来改动的，是向前兼容的，同时修复了三个小bug。</p> 
<p style="color:black; margin-left:0; margin-right:0">如果你有下述痛点，快快升级体验吧。</p> 
<p style="color:black; margin-left:0; margin-right:0">1）如果你在使用 Dubbo，那么你大概率遇到过 Dubbo 线程池耗尽的情况，是不是很烦恼呢？尝试使用下 DynamicTp 的 Dubbo 线程池管理功能，结合告警、实时监控、动态调参等功能尽可能降低 Dubbo 线程池耗尽，请求拒绝的风险。</p> 
<p style="color:black; margin-left:0; margin-right:0">2）mq 应该是很多互联网系统都会使用到的中间件，使用 mq 经常会遇到的其中一个问题就是消息积压问题，具体啥原因导致积压需要具体问题具体分析，就RocketMq来说，消费端是使用线程池进行处理消息的，所以说线程池的设置也会直接或者间接影响到消费速度，需要对此进行监控、告警、以及动态调参，尽可能降低因线程池设置而导致的积压风险。</p> 
<p style="color:black; margin-left:0; margin-right:0">注意：springboot 内置的三大 webserver 集成包默认会引入，不需要额外引入，其他三方组件的包需要自己引入，具体查看官网</p> 
<h4><span>Features</span></h4> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:black; margin-left:0; margin-right:0">报警渠道接入飞书</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">支持 Apache Dubbo & Alibab Dubbo 服务端提供端线程池管理</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">支持 RocketMq 消费端线程池管理</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">支持 Hystrix 线程池管理</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">支持 SpringBoot 内置三大WebServer（Tomcat、Jetty、Undertow）线程池管理</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">增加线程池别名配置，提升告警信息可读易懂性</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">提供任务包装类NamedRunable，提交任务时设置标识名称，方便问题追踪</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">告警项自定义配置，不配置的项用默认值</p> </li> 
</ul> 
<h4><span>BugFix</span></h4> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:black; margin-left:0; margin-right:0">修复并发导致通知报警信息发送多条的问题</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">修复通知渠道配置修改不能动态更新问题</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">修复钉钉手机端报警信息高亮失效问题</p> </li> 
</ul> 
<h4><span>Refactor</span></h4> 
<ul style="list-style-type:disc"> 
 <li> <p style="color:black; margin-left:0; margin-right:0">重构部分通知告警模块实现，支持三方中间件通知告警</p> </li> 
 <li> <p style="color:black; margin-left:0; margin-right:0">重构调整 adapter、starter 模块代码组织结构</p> </li> 
</ul> 
<h2><span>项目地址</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">目前累计 1.3k star，感谢你的star，欢迎pr，业务之余一起给开源贡献一份力量</p> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">官网</strong>：<strong style="color:#1e6bb8">https://dynamictp.cn</strong>[1]</p> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">gitee地址</strong>：<strong style="color:#1e6bb8">https://gitee.com/dromara/dynamic-tp</strong>[2]</p> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">github地址</strong>：<strong style="color:#1e6bb8">https://github.com/dromara/dynamic-tp</strong>[3]</p>
                                        </div>
                                      
</div>
            