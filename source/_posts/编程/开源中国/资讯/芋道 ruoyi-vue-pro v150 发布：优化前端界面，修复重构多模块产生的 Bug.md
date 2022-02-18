
---
title: '芋道 ruoyi-vue-pro v1.5.0 发布：优化前端界面，修复重构多模块产生的 Bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6994'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 23:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6994'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目地址</span></span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/zhijiantianya/ruoyi-vue-pro">https://gitee.com/zhijiantianya/ruoyi-vue-pro</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c"><span style="background-color:#ffffff">项目介绍</span></span></h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>芋道</strong>，一套<strong>全部开源</strong>的<strong>企业级</strong>的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">有任何问题，或者想要的功能，可以在<span><span> </span></span><em>Issues</em><span><span> </span></span>中提给艿艿。</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端采用<span><span> </span></span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FPanJiaChen%2Fvue-element-admin">vue-element-admin</a><span><span> </span></span>，正在支持 Vue 3 + ElementUI Plus 最新方案。</li> 
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
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>账号密码：admin/admin123</li> 
</ul> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">⚠️ Warning</h3> 
<ul> 
 <li>修复各种多 Maven Module 重构带来的 Bug，感谢大量群友的 PR 支持！</li> 
 <li>跟进 ruoyi-vue 3.4.0 ~ 3.8.1 版本，感谢这么优秀的开源项目！</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">📈 Statistic</h3> 
<ul> 
 <li>总代码行数：69299</li> 
 <li>源码代码行数：42687</li> 
 <li>注释行数：15888</li> 
 <li>单元测试用例数：278</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">⭐ New Features</h3> 
<ul> 
 <li>【优化】使用 Lombok 简化 JsonUtils 工具类</li> 
 <li>【新增】兼容 Node 16 版本，通过升级 BPMN-JS 相关库</li> 
 <li>【新增】前端的表格右侧工具栏组件支持显隐列，具体可见【用户管理】功能</li> 
 <li>【新增】前端的菜单导航显示风格 TopNav（false 为 左侧导航菜单，true 为顶部导航菜单），支持布局的保存与重置</li> 
 <li>【新增】前端的网页标题支持根据选择的菜单，动态展示标题<span> </span></li> 
 <li>【新增】字典标签样式回显，例如说开启的状态展示为 primary 蓝色，禁用的状态为 info 灰色</li> 
 <li>【新增】前端的 iframe 组件，方便内嵌网页</li> 
 <li>【新增】在基础设施-配置管理菜单，可通过修改<span> </span><code>yudao.captcha.enable</code><span> </span>配置项，动态修改登录是否需要验证码</li> 
 <li>【新增】在代码生成的预览界面，支持一键复制代码</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🐞 Bug Fixes</h3> 
<ul> 
 <li>【修复】数据权限的<span> </span><code>DEPT_AND_CHILD</code><span> </span>范围时，未设置自己所在的部门</li> 
 <li>【修复】Knife4j 接口文档 404 的问题，原因是<span> </span><code>spring.mvc.static-path-pattern</code><span> </span>配置项，影响了基础路径</li> 
 <li>【修复】修复文件访问地址错误</li> 
 <li>【修复】工作流程发起以及审批异常，由<span> </span><code>@NotEmpty</code><span> </span>校验、和 Long 类型异常导致</li> 
 <li>【修复】自定义 DefaultStreamMessageListenerContainerX 实现，解决 Redisson Stream 读取不到数据返回<span> </span><code>null</code><span> </span>导致 NPE 问题</li> 
 <li>【修复】部门更新后，本地缓存不刷新的问题</li> 
 <li>【修复】获取拥有指定的角色用户时，返回错误的 id 编号</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c">未来计划</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3 月初，基于 Flowable 实现的工作流，即将发布！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">逻辑已经在 https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/feature%2Fflowable/ 实现完成~</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">近期主要会对相关逻辑，补充一些单元测试，提高下质量~</p>
                                        </div>
                                      
</div>
            