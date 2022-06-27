
---
title: 'dynamic-tp v1.0.7 发布，轻量级动态线程池'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5295'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 15:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5295'
---

<div>   
<div class="content">
                                                                                            <p>dynamic-tp v1.0.7 已经发布，轻量级动态线程池。</p> 
<p>此版本更新内容包括：</p> 
<h2>Features</h2> 
<ul> 
 <li> <p>报警渠道接入飞书</p> </li> 
 <li> <p>支持 Apache Dubbo & Alibab Dubbo 服务端提供端线程池管理</p> </li> 
 <li> <p>支持 RocketMq 消费端线程池管理</p> </li> 
 <li> <p>支持 Hystrix 线程池管理</p> </li> 
 <li> <p>支持 SpringBoot 内置三大WebServer（Tomcat、Jetty、Undertow）线程池管理</p> </li> 
 <li> <p>增加线程池别名配置，提升告警信息可读易懂性</p> </li> 
 <li> <p>提供任务包装类NamedRunable，提交任务时设置标识名称，方便问题追踪</p> </li> 
 <li> <p>告警项自定义配置，不配置的项用默认值</p> </li> 
</ul> 
<h2>BugFix</h2> 
<ul> 
 <li> <p>修复并发导致通知报警信息发送多条的问题</p> </li> 
 <li> <p>修复通知渠道配置修改不能动态更新问题</p> </li> 
 <li> <p>修复钉钉手机端报警信息高亮失效问题</p> </li> 
</ul> 
<h2>Refactor</h2> 
<ul> 
 <li> <p>重构部分通知告警模块实现，支持三方中间件通知告警</p> </li> 
 <li> <p>重构调整 adapter、starter 模块代码组织结构</p> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/dromara/dynamic-tp/releases/v1.0.7">https://gitee.com/dromara/dynamic-tp/releases/v1.0.7</a></p>
                                        </div>
                                      
</div>
            