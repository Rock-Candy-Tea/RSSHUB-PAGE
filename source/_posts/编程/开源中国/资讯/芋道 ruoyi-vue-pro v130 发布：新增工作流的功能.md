
---
title: '芋道 ruoyi-vue-pro v1.3.0 发布：新增工作流的功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E5%88%97%E8%A1%A8.jpg'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 08:27:00 GMT
thumbnail: 'https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E5%88%97%E8%A1%A8.jpg'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目地址</span></span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<h1><span style="color:#e74c3c"><span style="background-color:#ffffff">项目介绍</span></span></h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>芋道</strong>，一套<strong>全部开源</strong>的<strong>企业级</strong>的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">有任何问题，或者想要的功能，可以在<span> </span><em>Issues</em><span> </span>中提给艿艿。</p> 
</blockquote> 
<ul> 
 <li>前端采用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin">vue-element-admin</a><span> </span>，正在支持 Vue 3 + ElementUI Plus 最新方案。</li> 
 <li>后端采用 Spring Boot、MySQL + MyBatis Plus、Redis + Redisson。</li> 
 <li>权限认证使用 Spring Security & Token & Redis，支持多终端、多种用户的认证系统。</li> 
 <li>支持加载动态权限菜单，按钮级别权限控制，本地缓存提升性能。</li> 
 <li>工作流使用 Activiti ，支持动态表单、在线设计流程、多种任务分配方式。</li> 
 <li>高效率开发，使用代码生成器可以一键生成前后端代码 + 单元测试 + Swagger 接口文档 + Validator 参数校验。</li> 
 <li>集成微信小程序、微信公众号、企业微信、钉钉等三方登陆，集成支付宝、微信等支付与退款。</li> 
 <li>集成阿里云、腾讯云、云片等短信渠道，集成阿里云、腾讯云、七牛云等云存储服务。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">在线体验</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">演示地址：<a href="https://gitee.com/link?target=http%3A%2F%2Fdashboard.yudao.iocoder.cn">http://dashboard.yudao.iocoder.cn</a></p> 
<ul> 
 <li>账号密码：admin/admin123</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">更新说明</span></span></h1> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">⚠️ Warning</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">基于 Activiti 7.X 版本实现工作流功能，支持可配置的动态表单、自定义的业务表单。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">下个版本会提供基于 Flowable 6.X 版本实现的工作流！</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">📈 Statistic</h3> 
<ul> 
 <li>总代码行数：61594</li> 
 <li>源码代码行数：37931</li> 
 <li>注释行数：14225</li> 
 <li>单元测试用例数：278</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">⭐ New Features</h3> 
<ul> 
 <li>【优化】引入 form generator 0.2.0 版本，并重构相关代码</li> 
 <li>【修改】修改部门负责人，从 String 字符串，调整成和后台用户的用户编号绑定</li> 
 <li>【新增】流程表单，支持动态进行表单的配置</li> 
 <li>【新增】工作组，用于支持指定工作组进行任务的审批</li> 
 <li>【新增】流程模型的管理，支持新增、导入、编辑、删除、发布流程模型</li> 
 <li>【新增】我的流程的管理，支持发起流程</li> 
 <li>【新增】待办任务的管理，支持任务的审批通过与不通过</li> 
 <li>【新增】已办任务的管理，支持详情的查看</li> 
 <li>【新增】任务分配规则，可指定角色、部门成员、部门负责人、用户、用户组、自定义脚本等维度，进行任务的审批</li> 
 <li>【新增】引入 bpmn-process-designer 0.0.1 版本，提供流程设计器的能力</li> 
 <li>【优化】新增 LambdaQueryWrapperX 类，改成使用 Lambda 的方式选择字段，避免手写导致字段不正确</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🐞 Bug Fixes</h3> 
<ul> 
 <li>【修复】biz-data-permission 组件的缓存机制，导致部分 SQL 未进行数据过滤</li> 
 <li>【修复】codegen 生成代码时，delete 接口补充 dataTypeClass 属性，避免 Swagger 打印 WARN 日志</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🔨 Dependency Upgrades</h3> 
<ul> 
 <li>【升级】redisson from 3.16.3 to 3.16.6，解决 Stream 在调试场景下会存在 NPE 的问题</li> 
 <li>【升级】spring-boot from 2.4.5 to 2.4.12，最新的 Spring Boot 2.6.X 在等更流行一些，稳定第一</li> 
 <li>【升级】druid from 1.2.4 to 1.2.8，提升数据库连接池的稳定性</li> 
 <li>【升级】dynamic-datasource from 3.3.2 to 3.5.0，修复动态数据源切换的问题</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">工作流程</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,"system-ui","Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:835px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>biu</th> 
   <th>biu</th> 
   <th>biu</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">流程模型</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程模型-列表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E5%88%97%E8%A1%A8.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程模型-设计" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E8%AE%BE%E8%AE%A1.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程模型-定义" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E6%A8%A1%E5%9E%8B-%E5%AE%9A%E4%B9%89.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">表单 & 分组</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="流程表单" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%B5%81%E7%A8%8B%E8%A1%A8%E5%8D%95.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="用户分组" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E7%94%A8%E6%88%B7%E5%88%86%E7%BB%84.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">我的流程</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="我的流程-列表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%88%91%E7%9A%84%E6%B5%81%E7%A8%8B-%E5%88%97%E8%A1%A8.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="我的流程-发起" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%88%91%E7%9A%84%E6%B5%81%E7%A8%8B-%E5%8F%91%E8%B5%B7.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="我的流程-详情" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E6%88%91%E7%9A%84%E6%B5%81%E7%A8%8B-%E8%AF%A6%E6%83%85.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">待办 & 已办</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="任务列表-审批" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8-%E5%AE%A1%E6%89%B9.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="任务列表-待办" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8-%E5%BE%85%E5%8A%9E.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="任务列表-已办" src="https://static.iocoder.cn/images/ruoyi-vue-pro/%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8-%E5%B7%B2%E5%8A%9E.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OA 请假</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="OA请假-列表" src="https://static.iocoder.cn/images/ruoyi-vue-pro/OA%E8%AF%B7%E5%81%87-%E5%88%97%E8%A1%A8.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="OA请假-发起" src="https://static.iocoder.cn/images/ruoyi-vue-pro/OA%E8%AF%B7%E5%81%87-%E5%8F%91%E8%B5%B7.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><img alt="OA请假-详情" src="https://static.iocoder.cn/images/ruoyi-vue-pro/OA%E8%AF%B7%E5%81%87-%E8%AF%A6%E6%83%85.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c">未来计划</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v1.4.0 计划：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>基于 uniapp 实现跨端的用户前台</li> 
</ul> 
<p>v1.5.0 计划：</p> 
<ul> 
 <li>三方支付：https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/pay_extension</li> 
</ul> 
<p>v1.6.0 计划：</p> 
<ul> 
 <li>简易商城，支持商品、交易、支付、营销等基本功能</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            