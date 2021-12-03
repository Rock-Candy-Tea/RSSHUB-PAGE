
---
title: 'MateCloud 4.1.8正式版发布,Spring Cloud和Spring Boot大版本升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/Spring%20Boot-2.6.1-blue'
author: 开源中国
comments: false
date: Fri, 03 Dec 2021 15:50:00 GMT
thumbnail: 'https://img.shields.io/badge/Spring%20Boot-2.6.1-blue'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left">一、发布说明</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">MateCloud 4.1.8 对 Spring Boot 和 Spring Cloud 进行一次大版本升级，Spring Boot 升级至 <span style="background-color:#f1c40f">2.6.1</span> 版本，Spring Cloud 升级至 <span style="background-color:#f1c40f">2021.0.0</span> 版本，欢迎尝鲜体验。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.1 功能升级</h2> 
<ul> 
 <li>修改提交 dist 目录，解决 xxl-job 部分 css 未成功提交</li> 
 <li>删除 jecache 依赖包</li> 
 <li>删除 mate-uaa 中暂时不用的依赖 mate-starter-auth</li> 
 <li>修改 security 版本与 spring boot 版本一致</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.2 文档更新</h2> 
<ul> 
 <li>更新中央仓库最新版本</li> 
 <li>修改文档里 spring cloud 的版本号</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">1.3 依赖升级</h2> 
<ul> 
 <li>升级至 Spring Boot 2.6.1</li> 
 <li>升级至 Spring Cloud 2021.0.0</li> 
 <li>升级至 Druid 1.2.8</li> 
 <li>升级至 transmittable-thread-local 2.12.2</li> 
 <li>升级至 okhttp 4.9.2</li> 
 <li>升级至 hutool 5.7.14</li> 
 <li>升级至 AWS Java SDK For Amazon S3 1.12.86</li> 
 <li>升级至 spring-security-oauth2-autoconfigure 2.5.5</li> 
 <li>升级至 Spring Boot Admin 2.5.4</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">二、系统演示</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.1 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcloud.mate.vip" target="_blank">http://cloud.mate.vip</a></h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">admin</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">matecloud</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">mate-system模块不能执行增删改请求</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果需要验证手机号码登录，手机号码采用页面默认号码，点击获取验证码，输入1188，即可登录。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.2 商业版：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fplus.mate.vip" target="_blank">http://plus.mate.vip</a></h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">admin</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">matecloud123</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">不能执行增删改请求，如需全部权限加微信 matecloud 联系</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">2.3 版本演进</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,system-ui,"> 
 <thead> 
  <tr> 
   <th>核心中间件</th> 
   <th>2.5.8及以下</th> 
   <th>3.0.8+</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Boot</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.3.*.RELEASE</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="SpringBoot" src="https://img.shields.io/badge/Spring%20Boot-2.6.1-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Cloud</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Hoxton SR*</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="SpringCloud" height="20" src="https://img.shields.io/badge/Spring%20Cloud-2021.0.0-blue" width="140" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Cloud Alibaba</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.2.*.RELEASE</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="SpringCloudAlibaba" src="https://img.shields.io/badge/Spring%20Cloud%20Alibaba-2021.1-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Nacos</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.4.*及以下</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="nacos" src="https://img.shields.io/badge/Nacos-2.0.3-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Sentinel</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.8.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="sentinel" src="https://img.shields.io/badge/Sentinel-1.8.2-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">2.4 官方文档</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.4.1 文档地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.mate.vip%2Fdocs" target="_blank">http://www.mate.vip/docs</a></h3> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.4.2 商业版文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.mate.vip" target="_blank">http://doc.mate.vip</a></h3> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.4.3 快速安装：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.mate.vip%2Farchives%2F107" target="_blank">http://www.mate.vip/archives/107</a></h3> 
<h2 style="margin-left:0; margin-right:0; text-align:left">三、 前端重大更新</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">前端采用<code>Vue3.2</code>、<code>Vite 2.5.*</code>、 <code>Ant-Design-Vue 2.*</code>、<code>TypeScript</code> 的大型中后台解决方案。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">3.1 技术栈</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Vue 3.2.12</li> 
 <li>Pinia 2.0.0-rc.7</li> 
 <li>vue-i18n 9.1.7</li> 
 <li>typescript 4.29.1</li> 
 <li>ant-design-vue 2.2.8</li> 
 <li>axios 0.21.3</li> 
 <li>vue-router 4.0.11</li> 
 <li>vite 2.5.8</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">四、 版本发布</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>4.1.8</code>版本已经发布，实现了系统管理的基础功能，主要包括菜单管理、用户管理、角色管理、部门管理、日志管理、客户端管理等功能。欢迎体验。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">五、技术架构</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="系统架构" src="https://cdn.mate.vip/matecloud-framework.jpg" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">六、 功能特点</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">主体框架：采用最新的<code>Spring Cloud 2021.0.0</code>, <code>Spring Boot 2.6.1</code>, <code>Spring Cloud Alibaba 2021.1</code>版本进行系统设计；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">统一注册：支持<code>Nacos</code>作为注册中心，实现多配置、分群组、分命名空间、多业务模块的注册和发现功能；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">统一认证：统一<code>Oauth2</code>认证协议，采用jwt的方式，实现统一认证，并支持自定义grant_type实现手机号码登录，第三方登录集成JustAuth实现微信、支付宝等多种登录模式；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">业务监控：利用<code>Spring Boot Admin</code>来监控各个独立Service的运行状态。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">内部调用：集成了<code>Feign</code>和<code>Dubbo</code>两种模式支持内部调用，并且可以实现无缝切换，适合新老程序员，快速熟悉项目；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">业务熔断：采用<code>Sentinel</code>实现业务熔断处理，避免服务之间出现雪崩;</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">身份注入：通过注解的方式，实现用户登录信息的快速注入；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">在线文档：通过接入<code>Knife4j</code>，实现在线API文档的查看与调试;</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">代码生成：基于<code>Mybatis-plus-generator</code>自动生成代码，提升开发效率，生成模式不断优化中，暂不支持前端代码生成；</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">消息中心：集成消息中间件<code>RocketMQ</code>和<code>Kafka</code>，对业务进行异步处理;</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">业务分离：采用前后端分离的框架设计，前端采用<code>vue-element-admin</code>,商业版采用<code>antd-pro-vue</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">链路追踪：自定义traceId的方式，实现简单的链路追踪功能</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">多租户功能：集成<code>Mybatis Plus</code>,实现SAAS多租户功能</p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">七、 项目源码</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>GITHUB</th> 
   <th>码云</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">MateCloud后端源码</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatevip%2Fmatecloud" target="_blank">https://github.com/matevip/matecloud</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">Artemis前端源码</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatevip%2Fartemis" target="_blank">https://github.com/matevip/artemis</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/matevip/artemis">https://gitee.com/matevip/artemis</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">MateBoot后端源码</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatevip%2Fmateboot" target="_blank">https://github.com/matevip/mateboot</a></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><a href="https://gitee.com/matevip/mateboot">https://gitee.com/matevip/mateboot</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left">7.1 微服务项目示例</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://gitee.com/matevip/mate-demo">https://gitee.com/matevip/mate-demo</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">八、部分截图</h2> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,system-ui,"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page2.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page3.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page4.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page6.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/7.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/9.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            