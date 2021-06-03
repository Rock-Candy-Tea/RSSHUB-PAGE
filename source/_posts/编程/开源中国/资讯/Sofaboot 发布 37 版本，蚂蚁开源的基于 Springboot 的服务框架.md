
---
title: 'Sofaboot 发布 3.7 版本，蚂蚁开源的基于 Springboot 的服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1606'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 09:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1606'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <div>
  <span style="background-color:#ffffff; color:#333333">SOFABoot 是蚂蚁金服开源的基于 Spring Boot 的研发框架，它在 Spring Boot 的基础上，提供了诸如 Readiness Check，类隔离，日志空间隔离等等能力。在增强了 Spring Boot 的同时，SOFABoot 提供了让用户可以在 Spring Boot 中非常方便地使用 SOFA 中间件的能力。</span>
 </div> 
 <div>
   
 </div> 
 <div>
  3.7版本已经发布，本次最大的更新是把依赖的Springboot版本升级到了2.3.9, 
 </div> 
 <div>
  另外对应的SOFARPC版本升级到了5.7.8
 </div> 
 <div>
   
 </div> 
 <div>
  主要变更如下:
 </div> 
 <div>
   
 </div> 
 <div>
  新功能:
 </div> 
 <ul> 
  <li>升级Spring boot版本到2.3.9.RELEASE</li> 
  <li>适配SOFABOOT符合Springboot readiness和liveness检查规范</li> 
 </ul> 
 <p>优化</p> 
 <ul> 
  <li>可以使用静态sofa bean作为配置</li> 
  <li>增加issue banner</li> 
  <li>提供英文版README</li> 
  <li>分离ark/spring的shutdown</li> 
 </ul> 
 <div>
  完整列表可访问:
 </div> 
 <div>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Freleases%2Ftag%2Fv3.7.0" target="_blank">Release v3.7.0 · sofastack/sofa-boot (github.com)</a>
 </div> 
 <div>
   
 </div> 
 <div>
   
 </div> 
 <div>
  ⭐️ New Features
 </div> 
</div> 
<div style="text-align:start"> 
 <ul> 
  <li>Update Spring Boot version to 2.3.9.RELEASE <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F809" target="_blank">#809</a></li> 
  <li>Adapt SOFABoot to Spring Boot readiness and liveness <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F825" target="_blank">#825</a></li> 
 </ul> 
 <p>🔨 Optimize</p> 
 <ul> 
  <li>Add config to statics sofa bean <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F812" target="_blank">#812</a></li> 
  <li>Add issue banner <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F813" target="_blank">#813</a></li> 
  <li>Provide English version README <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F815" target="_blank">#815</a></li> 
  <li>Seperate ark/spring shutdown <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F817" target="_blank">#817</a></li> 
  <li>Use revision instead of hard-code version <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F827" target="_blank">#827</a></li> 
  <li>Add check style of newline for eof <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F828" target="_blank">#828</a></li> 
  <li>Update sofa-common-tools version to 1.3.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F832" target="_blank">#832</a></li> 
 </ul> 
 <p>🐞 Bug fixes</p> 
 <ul> 
  <li>Fix sofa.middleware.log.console overridden problem <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F808" target="_blank">#808</a></li> 
  <li>Fix properties overridden in ark environment <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F814" target="_blank">#814</a></li> 
  <li>Fix startup auto configuration in Isle <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F824" target="_blank">#824</a></li> 
  <li>Fix tracer bean name conflicting with spring cloud <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F830" target="_blank">#830</a></li> 
  <li>Fix grpc version problem <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-boot%2Fpull%2F834" target="_blank">#834</a></li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            