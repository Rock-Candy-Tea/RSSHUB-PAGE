
---
title: '《灯灯多租户快速开发平台》 4.5.2 发布， 升级 SpringCloud2021、antdv3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 01:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzuihou%2Fzuihou-admin-cloud%2F1465302" target="_blank">4.5.2 版本 更新详情:</a></h2> 
<h2>build</h2> 
<p> </p> 
<ul> 
 <li>依赖升级</li> 
</ul> 
<pre><code>spring.boot.version>2.6.6
spring.cloud.version>2021.0.1
spring-cloud-alibaba-dependencies.version>2021.0.1.0
spring-boot-admin.version>2.6.6
dynamic.datasource.version>3.5.1
fastjson.version>1.2.80

"ant-design-vue"> "3.1.1",
"typescript"> "^4.6.3",
"vite"> "^2.9.1",</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">feat</h2> 
<ul> 
 <li>接入vxe-table，并将代码生成配置页面的表格使用vxe-table编写</li> 
 <li>生成datasource项目的新服务（仅项目结构和配置类）</li> 
 <li>代码生成器支持生成 树结构页面</li> 
 <li>代码生成器支持生成 通过路由跳转到编辑页面</li> 
 <li>代码生成器支持生成 创建菜单的sql脚本</li> 
 <li>树结构增删改查示例</li> 
</ul> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">refactor</h2> 
<ul> 
 <li>优化datasource模式配置类、配置文件、数据库脚本</li> 
 <li>枚举字段通过@Echo注解回显（原来低版本通过重写序列化的方式使得枚举返回对象，在vben框架前端传参时，不太友好）</li> 
 <li>(lamp-generator): 代码生成器服务代码优化</li> 
 <li>(lamp-generator): 代码生成页面导入表结构功能 支持将mysql 5.7的表注释读取并存储到配置表</li> 
 <li>(lamp-generator): 优化代码生成器模板，以适配ant design vue3.1.1</li> 
 <li>(lamp-generator): 优化模板，给表单设置name属性，防止同一个页面生成相同id的表单</li> 
 <li>(lamp-web-pro): BasicTree支持设置加载状态，并将资源维护页面修改为支持加载状态</li> 
 <li>(lamp-web-pro): 优化 findNodeByKey 方法</li> 
 <li>(lamp-web-pro): 优化图片预览组件，支持预览本地图片</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">fix</h2> 
<ul> 
 <li>(lamp-generator):  修复生成serviceImpl和manageImpl代码并配置了子包名时，路径和包地址拼接异常</li> 
 <li>(lamp-web-pro): 修复应用切换时，重复点击问题和切换后地址栏地址仍然为切换前的地址的bug</li> 
 <li>(lamp-web-pro): 已经存在rules时，required不生效</li> 
 <li>(lamp-web-pro): ApiTreeSelect修复 fieldNames</li> 
 <li>(lamp-web-pro): 使用了Table的页面去除控制台警告： "Warning: [ant-design-vue: Table] `column.slots` is deprecated. Please use `v-slot:headerCell` `v-slot:bodyCell` instead"</li> 
 <li>(lamp-web-pro): 修复Dropdown组件placement属性警告</li> 
 <li>(lamp-web-pro): 修复同一个页面使用多个表单时，表单id一致导致的 警告</li> 
 <li>(lamp-web-pro): 消除消息发送页面的警告：" [ant-design-vue: Form.Item] FormItem can only collect one field item, you haved set `ARadioGroup`, `ASelect` 2 field items. You can set not need to be collected fields into `a-form-item-rest`"</li> 
</ul> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更多功能，等你来体验：     </h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li style="text-align:left">《灯灯》官网： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftangyh.top%2F" target="_blank">https://tangyh.top/</a> </li> 
 <li style="text-align:left">4.x体验地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpro.tangyh.top%2F" target="_blank">https://pro.tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址1： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.tangyh.top%2F" target="_blank">https://boot.tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址2： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fboot.tangyh.top%2Flamp-web%2F" target="_blank">https://boot.tangyh.top/lamp-web/</a></li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">《灯灯》中后台快速开发平台</h1> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如果你非要说 lamp 是 Linux+Apache+MySQL+PHP，那就算是吧，毕竟 PHP 是世界上最好的语言，我也希望此项目成为世界上最好的后台框架！😈😈😈</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>lamp-cloud</code><span> </span>基于 jdk11/jdk8 +<span> </span><code>SpringCloud</code><span> </span>+ SpringCloudAlibaba+<span> </span><code>SpringBoot</code><span> </span>的微服务快速开发平台，专注于解决 SaaS 多租户体系问题， 具备 RBAC 功能、网关统一鉴权、Xss 防跨站攻击、自动代码生成、多种存储系统、分布式事务、分布式定时任务等多个模块，支持多业务系统并行开发， 支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">核心技术采用 Spring Cloud Alibaba、SpringBoot、Mybatis、Seata、Sentinel、RabbitMQ、FastDFS/MinIO、SkyWalking 等主要框架和中间件。 希望能努力打造一套从<span> </span><code>JavaWeb基础框架</code><span> </span>-<span> </span><code>分布式微服务架构</code><span> </span>-<span> </span><code>持续集成</code><span> </span>-<span> </span><code>系统监测</code><span> </span>的解决方案。<code>本项目旨在实现基础能力，不涉及具体业务。</code></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">项目截图：</h1> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>预览</th> 
   <th>预览</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt src="https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/99e21a50fe4cd8e644bc2a2c693b9b86.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/315afa0201968de0b20c1af42fb981c5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cdb488d0ed1c35613025613df6a36f96.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/c8d8936b144fe568ef394289ddbf0268.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt src="https://oscimg.oschina.net/oscnet/up-16787bac9c056bad7ff6538a0fa5f676234.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/58ae227c8b3e98129091dc86efb219c8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/7e34b4c35c24445f72898c95fb2d6347.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/2f1bcc485ca1ff3ee22995b6b276cc6f.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cbcafbcff1e2404f2fb466ab257de6de.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/45111269e0acd9173e480e31505b04f3.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/67e0575c0c9acb0e787e17194e5fba0d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            