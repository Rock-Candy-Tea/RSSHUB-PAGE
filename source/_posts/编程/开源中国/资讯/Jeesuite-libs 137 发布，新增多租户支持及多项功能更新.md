
---
title: 'Jeesuite-libs 1.3.7 发布，新增多租户支持及多项功能更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2331'
author: 开源中国
comments: false
date: Mon, 05 Apr 2021 20:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2331'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p><span style="background-color:#ffffff; color:#40485b">Jeesuite寓意为java企业级应用开发套件，定位是一站式分布式开发架构开源解决方案及快速开发平台。Jeesuite-libs为整体开发架构提供底层库支持。提供了数据库、缓存、消息中间件、分布式定时任务、SSO、文件服务、云存储等基础模块以及集成Dubbo、Spring Cloud底层支持。全部基于主流框架只做增强不做任何底层定制修改，每个组件可以独立使用。</span></p> 
</blockquote> 
<p>历经半年的线上运行验证以及三个临时版本迭代Jeesuite-libs终于迎来了1.3.7 release版本。1.3.7版本更新内容包含：</p> 
<ul> 
 <li>新增： jeesuite-mybatis 支持多租户模式</li> 
 <li>新增： jeesuite-mybatis 支持基于配置的数据权限</li> 
 <li>新增： jeesuite-mybatis 支持数据变更记录采集</li> 
 <li>优化： jeesuite-mybatis 自动缓存支持JOIN等多表关联自动刷新缓存</li> 
 <li>新增： jeesuite-cache 支持多租户模式</li> 
 <li>新增： jeesuite-mybatis 支持数据变更记录采集</li> 
 <li>新增： jeesuite-scheduler 支持多租户模式</li> 
 <li>新增： jeesuite-scheduler 监控rest API</li> 
 <li>优化： jeesuite-scheduler 持久化接口重新定义</li> 
 <li>新增： jeesuite-springweb 统一拦截器、异常处理，上下文管理等基础类</li> 
 <li>新增： jeesuite-common 增加异步任务工具</li> 
 <li>优化： jeesuite-common 统一管理基础的model类</li> 
</ul> 
<p>本次版本主打多租户功能，包括其他更新项目都已经在线上稳定运行了三个月以上。除此外重新更新了所有文档并迁移到码云的page服务。<br> 文档地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.jeesuite.com%2F" target="_blank">http://docs.jeesuite.com/</a> </p> 
<p>为了帮助大家快速熟悉及使用jeesuite-libs，本次更新还同步发布了一个实例项目：<a href="https://gitee.com/vakinge/jeesuite-demo">https://gitee.com/vakinge/jeesuite-demo</a></p>
                                        </div>
                                      
</div>
            