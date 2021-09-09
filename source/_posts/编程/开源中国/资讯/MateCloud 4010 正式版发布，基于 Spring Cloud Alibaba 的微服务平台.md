
---
title: 'MateCloud 4.0.10 正式版发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/Spring%20Boot-2.5.4-blue'
author: 开源中国
comments: false
date: Thu, 09 Sep 2021 07:20:00 GMT
thumbnail: 'https://img.shields.io/badge/Spring%20Boot-2.5.4-blue'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:left">一、发布说明</h2> 
<p style="text-align:left">MateCloud 4.0.10基于Spring Cloud Alibaba推出的微服务快速开发平台，集成Nacos 2.0.3、Sentinel 1.8.2、Jetcache等诸多中间件。前端采用<code>Vue3.2.4</code>、<code>Vite 2.5.1</code>、 <code>Ant-Design-Vue 2.2.6</code>、<code>TypeScript</code> 的大型中后台解决方案。 其中前端<code>4.0.8-M2</code>版本正在发布，实现了系统管理的基础功能，主要包括菜单管理、用户管理、角色管理、部门管理、日志管理、客户端管理等功能。正持续更新中，欢迎体验。</p> 
<h3 style="text-align:start">1.1 功能升级</h3> 
<ul> 
 <li>解决mate-system报循环引用错误</li> 
 <li>解决Mybatis-Plus升级后的报错</li> 
 <li>修复顶级菜单上配置菜单应用报错的bug</li> 
 <li>完善README的中央仓库版本和前端的一些版本描述</li> 
 <li>修改 redission 构造时的配置</li> 
 <li>API管理功能允许serviceId为空，为空则查询所有列表</li> 
 <li>简化swagger信息，统一风格</li> 
 <li>增加业务单元测试示例</li> 
 <li>调整前端更新的位置和部署组件的版本号</li> 
 <li>修改数据源对象的status字段为String类型</li> 
 <li>升级Dubbo至[2.7.13,)，解决CVE-2021-36162安全漏洞</li> 
</ul> 
<h3 style="text-align:start">1.2 依赖升级</h3> 
<ul> 
 <li>升级至FastJson 1.2.78</li> 
 <li>升级至Mybatis Plus 3.4.3.3</li> 
 <li>升级至EasyPoi 4.4.0</li> 
 <li>升级至Jasypt-spring-boot-starter 3.0.4</li> 
 <li>升级至gson 2.8.8</li> 
 <li>升级至aws-java-sdk-s3 1.12.63</li> 
 <li>升级至hutool 5.7.11</li> 
 <li>升级至dubbo 2.7.13+</li> 
</ul> 
<h2 style="text-align:left">二、系统演示</h2> 
<h3 style="text-align:left">2.1 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcloud.mate.vip" target="_blank">http://cloud.mate.vip</a></h3> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">admin</td> 
   <td style="border-color:#dddddd">matecloud</td> 
   <td style="border-color:#dddddd">mate-system模块不能执行增删改请求</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left">如果需要验证手机号码登录，手机号码采用页面默认号码，点击获取验证码，输入1188，即可登录。</p> 
<h3 style="text-align:left">2.2  企业版：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fplus.mate.vip" target="_blank">http://plus.mate.vip</a></h3> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>账号</th> 
   <th>密码</th> 
   <th>操作权限</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">admin</td> 
   <td style="border-color:#dddddd">matecloud123</td> 
   <td style="border-color:#dddddd">不能执行增删改请求，如需全部权限加微信 matecloud 联系</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">2.3  版本演进</h2> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>核心中间件</th> 
   <th>2.5.8及以下</th> 
   <th>3.0.8+</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">Spring Boot</td> 
   <td style="border-color:#dddddd">2.3.*.RELEASE</td> 
   <td style="border-color:#dddddd"><img alt src="https://img.shields.io/badge/Spring%20Boot-2.5.4-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Spring Cloud</td> 
   <td style="border-color:#dddddd">Hoxton SR*</td> 
   <td style="border-color:#dddddd"><img alt src="https://img.shields.io/badge/Spring%20Cloud-2020.0.3-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Spring Cloud Alibaba</td> 
   <td style="border-color:#dddddd">2.2.*.RELEASE</td> 
   <td style="border-color:#dddddd"><img alt src="https://img.shields.io/badge/Spring%20Cloud%20Alibaba-2021.1-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Nacos</td> 
   <td style="border-color:#dddddd">1.4.*及以下</td> 
   <td style="border-color:#dddddd"><img alt src="https://img.shields.io/badge/Nacos-2.0.2-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Sentinel</td> 
   <td style="border-color:#dddddd">1.8.1</td> 
   <td style="border-color:#dddddd"><img alt src="https://img.shields.io/badge/Sentinel-1.8.1-blue" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">2.4  官方文档</h2> 
<h3 style="text-align:left">2.4.1 文档地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.mate.vip%2Fdocs" target="_blank">http://www.mate.vip/docs</a></h3> 
<h3 style="text-align:left">2.4.2 商业版文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.mate.vip" target="_blank">http://doc.mate.vip</a></h3> 
<h3 style="text-align:left">2.4.3 快速安装：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.mate.vip%2Farchives%2F107" target="_blank">http://www.mate.vip/archives/107</a></h3> 
<h2 style="text-align:left">三、 前端重大更新</h2> 
<p style="text-align:left">前端采用<code>Vue3.2</code>、<code>Vite 2.5.*</code>、 <code>Ant-Design-Vue 2.*</code>、<code>TypeScript</code> 的大型中后台解决方案。</p> 
<h3 style="text-align:left">3.1  技术栈</h3> 
<ul> 
 <li>Vue 3.2.2</li> 
 <li>Pinia 2.0.0-rc.4</li> 
 <li>vue-i18n 9.1.7</li> 
 <li>typescript 4.29.1</li> 
 <li>ant-design-vue 2.2.6</li> 
 <li>axios 0.21.1</li> 
 <li>vue-router 4.0.11</li> 
 <li>vite 2.5.0-beta.2</li> 
</ul> 
<h3 style="text-align:left">四、 版本发布</h3> 
<p style="text-align:left"><code>4.0.8-M2</code>版本已经发布，实现了系统管理的基础功能，主要包括菜单管理、用户管理、角色管理、部门管理、日志管理、客户端管理等功能。欢迎体验。</p> 
<h2 style="text-align:left">五、技术架构</h2> 
<p style="text-align:left"><img alt="系统架构" src="https://cdn.mate.vip/matecloud-framework.jpg" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">六、 功能特点</h2> 
<ul> 
 <li> <p>主体框架：采用最新的<code>Spring Cloud 2020.0.3</code>, <code>Spring Boot 2.5.4</code>, <code>Spring Cloud Alibaba 2021.1</code>版本进行系统设计；</p> </li> 
 <li> <p>统一注册：支持<code>Nacos</code>作为注册中心，实现多配置、分群组、分命名空间、多业务模块的注册和发现功能；</p> </li> 
 <li> <p>统一认证：统一<code>Oauth2</code>认证协议，采用jwt的方式，实现统一认证，并支持自定义grant_type实现手机号码登录，第三方登录集成JustAuth实现微信、支付宝等多种登录模式；</p> </li> 
 <li> <p>业务监控：利用<code>Spring Boot Admin</code>来监控各个独立Service的运行状态。</p> </li> 
 <li> <p>内部调用：集成了<code>Feign</code>和<code>Dubbo</code>两种模式支持内部调用，并且可以实现无缝切换，适合新老程序员，快速熟悉项目；</p> </li> 
 <li> <p>业务熔断：采用<code>Sentinel</code>实现业务熔断处理，避免服务之间出现雪崩;</p> </li> 
 <li> <p>身份注入：通过注解的方式，实现用户登录信息的快速注入；</p> </li> 
 <li> <p>在线文档：通过接入<code>Knife4j</code>，实现在线API文档的查看与调试;</p> </li> 
 <li> <p>代码生成：基于<code>Mybatis-plus-generator</code>自动生成代码，提升开发效率，生成模式不断优化中，暂不支持前端代码生成；</p> </li> 
 <li> <p>消息中心：集成消息中间件<code>RocketMQ</code>和<code>Kafka</code>，对业务进行异步处理;</p> </li> 
 <li> <p>业务分离：采用前后端分离的框架设计，前端采用<code>vue-element-admin</code>,商业版采用<code>antd-pro-vue</code></p> </li> 
 <li> <p>链路追踪：自定义traceId的方式，实现简单的链路追踪功能</p> </li> 
 <li> <p>多租户功能：集成<code>Mybatis Plus</code>,实现SAAS多租户功能</p> </li> 
</ul> 
<h2 style="text-align:left">七、 项目源码</h2> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>GITHUB</th> 
   <th>码云</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">MateCloud后端源码</td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatevip%2Fmatecloud" target="_blank">https://github.com/matevip/matecloud</a></td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/matevip/matecloud">https://gitee.com/matevip/matecloud</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Artemis前端源码</td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatevip%2Fartemis" target="_blank">https://github.com/matevip/artemis</a></td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/matevip/artemis">https://gitee.com/matevip/artemis</a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">MateBoot后端源码</td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatevip%2Fmateboot" target="_blank">https://github.com/matevip/mateboot</a></td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/matevip/mateboot">https://gitee.com/matevip/mateboot</a></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">7.1  微服务项目示例</h2> 
<ul> 
 <li> <a href="https://gitee.com/matevip/mate-demo">https://gitee.com/matevip/mate-demo</a></li> 
</ul> 
<h2 style="text-align:left">八、部分截图</h2> 
<table cellspacing="0" style="width:634px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page1.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page2.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page3.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page4.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/artemis_page6.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/7.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5"><img src="https://gitee.com/matevip/matecloud/raw/master/doc/images/9.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            