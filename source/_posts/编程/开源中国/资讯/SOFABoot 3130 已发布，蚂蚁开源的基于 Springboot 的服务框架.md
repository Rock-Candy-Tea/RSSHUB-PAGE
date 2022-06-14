
---
title: 'SOFABoot 3.13.0 已发布，蚂蚁开源的基于 Springboot 的服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3972'
author: 开源中国
comments: false
date: Tue, 14 Jun 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3972'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0"><span style="color:#333333">SOFABoot 是蚂蚁金服开源的基于 Spring Boot 的研发框架，它在 Spring Boot 的基础上，提供了诸如 Readiness Check，类隔离，日志空间隔离等等能力。在增强了 Spring Boot 的同时，SOFABoot 提供了让用户可以在 Spring Boot 中非常方便地使用 SOFA 中间件的能力。</span></p> 
<p style="margin-left:0"><span style="color:#333333">SOFABoot </span>3.13.0<span style="color:#333333"> 现已发布，具体更新内容如下：</span></p> 
<p><span style="color:#24292f"><strong>New Features</strong></span></p> 
<ul> 
 <li>在 readiness endpoint 中支持 showDetail=false <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F957" target="_blank">#957</a></li> 
 <li>支持配置跳过 ComponentManagerImpl 中的 shutdown method <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F960" target="_blank">#960</a></li> 
</ul> 
<p><span style="color:#24292f"><strong>Optimize</strong></span></p> 
<ul> 
 <li>使 ServiceBeanFactoryPostProcessor 实现 BeanDefinitionRegistry <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F967" target="_blank">#967</a></li> 
 <li>将 springframework 更新到 5.3.20 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F969" target="_blank">#969</a></li> 
 <li>在 sofa reference proxy 中添加 JvmBindingInterface <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F970" target="_blank">#970</a></li> 
 <li>更新 ProxyBeanFactoryPostProcessor 调用顺序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F971" target="_blank">#971</a></li> 
 <li>在 beanstat 中添加 beanname <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F973" target="_blank">#973</a></li> 
 <li>忽略 healthcheck 结果中的 component success detail <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F976" target="_blank">#976</a></li> 
</ul> 
<p><span style="color:#24292f"><strong>Bug fixes</strong></span></p> 
<ul> 
 <li>修复 StartupContextRefreshedListener 顺序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F966" target="_blank">#966</a></li> 
 <li>修复 <span style="color:#24292f">output bean stats sort 问题</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F968" target="_blank">#968</a></li> 
 <li>修复解析绑定编码问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F975" target="_blank">#975</a></li> 
 <li>修复关于应用程序事件忽略子事件的问题 #979</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Freleases%2Ftag%2Fv3.13.0" target="_blank">https://github.com/sofastack/sofa-boot/releases/tag/v3.13.0</a></p>
                                        </div>
                                      
</div>
            