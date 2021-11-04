
---
title: 'Eurynome Cloud v2.5.6.20 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8076'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 12:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8076'
---

<div>   
<div class="content">
                                                                                            <p>Eurynome Cloud v2.5.6.20 已经发布，企业级技术中台微服务架构。</p> 
<p><strong>Eurynome Cloud</strong> 是一款企业级微服务架构和服务能力开发平台。基于Spring Boot 2.5.6、Spring Cloud 2020.0.4、Spring Cloud Alibaba 2021.1、Nacos 2.0.3 等最新版本开发，遵循SpringBoot编程思想，高度模块化和可配置化。具备服务发现、配置、熔断、限流、降级、监控、多级缓存、分布式事务、工作流等功能</p> 
<p><strong>平台定位</strong></p> 
<ul> 
 <li>构建成熟的、完善的、全面的，基于 OAuth2 的、前后端分离的微服务架构解决方案。</li> 
 <li>面向企业级应用和互联网应用设计开发，既兼顾传统项目的微服务化，又满足互联网应用开发建设、快速迭代的使用需求。</li> 
 <li>平台架构使用微服务领域及周边相关的各类新兴技术或主流技术进行建设，是帮助快速跨越架构技术选型、研究探索阶段的利器。</li> 
 <li>代码简洁规范、结构合理清晰，是新技术开发应用的典型的、综合性案例，助力开发人员对新兴技术的学习和掌握。</li> 
</ul> 
<p><strong>本次更新内容</strong></p> 
<p><strong>后端更新</strong></p> 
<ol> 
 <li>修复 <code>Gateway</code> 网关服务，在生产环境下，关闭 <code>SpringDoc</code> 和 <code>Swagger</code> ，Bean 注入不正确问题。</li> 
 <li>优化 <code>Gateway</code> 网关服务发现服务动态接入服务 <code>Swagger</code> 文档监听器配置，通过配置动态关闭，在生产环境下不再开启。</li> 
 <li>单体版应用默认端口修改为 8847，与微服务版 <code>Gateway</code> 一致，方便前端接入</li> 
 <li>升级依赖包版本： 
  <ul> 
   <li>Redisson 升级至 3.16.4</li> 
   <li>Okhttps 升级至 3.3.0</li> 
   <li>weixin-java-miniapp 升级至 4.2.0</li> 
  </ul> </li> 
</ol> 
<p><strong>前端更新</strong></p> 
<ol> 
 <li>优化组件库中，各个组件的配置以及导出逻辑，解决在生产模式下，组件库中组件显示不正确问题。</li> 
 <li>对生产模式下，Vue工程打包进行深度性能优化。</li> 
 <li>对打包生成的各类资源进一步压缩，降低资源文件大小。</li> 
 <li>依赖包拆分变更为使用动态配置，编译时将所有依赖包都动态拆分为独立js文件，无须再根据分析结果手动进行拆分配置，极大地降低Vue 默认打包文件的大小，解决首屏加载时间过长问题。</li> 
 <li>修复前端工程打包之后，部署至 Nginx 或 Express 页面空白或显示不正确问题。</li> 
 <li>解决 Vue 工程打包，index.html 文件丢失问题。</li> 
 <li>升级大量依赖包版本，重新编译库</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.20">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.6.20</a></p>
                                        </div>
                                      
</div>
            