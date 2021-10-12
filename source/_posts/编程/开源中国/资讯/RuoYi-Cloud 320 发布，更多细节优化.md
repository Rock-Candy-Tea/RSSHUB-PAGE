
---
title: 'RuoYi-Cloud 3.2.0 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
author: 开源中国
comments: false
date: Tue, 12 Oct 2021 08:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依Cloud微服务版本<span style="background-color:#ffffff; color:#333333"> v3.2.0 已发布，更新日志：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>菜单管理支持配置路由参数</li> 
 <li>定时任务支持在线生成cron表达式</li> 
 <li>自定义弹层溢出滚动样式</li> 
 <li>自定义可拖动弹窗宽度指令</li> 
 <li>自定义可拖动弹窗高度指令</li> 
 <li>修改时检查用户数据权限范围</li> 
 <li>修复保存配置主题颜色失效问题</li> 
 <li>新增暗色菜单风格主题</li> 
 <li>菜单&部门新增展开/折叠功能</li> 
 <li>页签新增关闭左侧&添加图标</li> 
 <li>代码生成主子表多选行数据</li> 
 <li>日期范围支持添加多组</li> 
 <li>Excel导入支持@Excels注解</li> 
 <li>Excel注解支持导入导出标题信息</li> 
 <li>Excel注解支持自定义数据处理器</li> 
 <li>日志注解新增是否保存响应参数</li> 
 <li>定时任务对检查异常进行事务回滚</li> 
 <li>补充定时任务表字段注释</li> 
 <li>定时任务屏蔽ldap远程调用</li> 
 <li>新增通用方法简化下载使用</li> 
 <li>新增通用方法简化模态/缓存使用</li> 
 <li>新增data-dict组件简化数据字典使用</li> 
 <li>禁用dict-tag组件的渐变动画</li> 
 <li>默认首页使用keep-alive缓存</li> 
 <li>升级springcloud到最新版2020.0.4</li> 
 <li>升级spring-boot到最新版本2.5.5</li> 
 <li>升级spring-boot-admin到最新版2.5.2</li> 
 <li>升级pagehelper到最新版1.4.0</li> 
 <li>升级fastjson到最新版1.2.78</li> 
 <li>升级druid到最新版1.2.8</li> 
 <li>升级element-ui到最新版本2.15.6</li> 
 <li>升级sass-loader到最新版本10.1.1</li> 
 <li>升级dart-sass到版本1.32.13</li> 
 <li>升级file-saver到最新版本2.0.5</li> 
 <li>优化异常处理信息</li> 
 <li>验证码默认20s超时</li> 
 <li>优化代码生成导入表按创建时间排序</li> 
 <li>优化代码生成点击预览重置激活tab</li> 
 <li>修复主子表代码模板方法名错误问题</li> 
 <li>修复xss过滤后格式出现的异常</li> 
 <li>修复多图组件验证失败被删除问题</li> 
 <li>请求参数新增reasonable分页合理化属性</li> 
 <li>修复代码生成页面数据编辑保存之后总是跳转第一页的问题</li> 
 <li>修复带safari浏览器无法格式化utc日期格式yyyy-MM-dd'T'HH🇲🇲ss.SSS问题</li> 
 <li>其他细节优化</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">基于Spring Boot、Spring Cloud & Alibaba、Redis的分布式微服务架构权限管理系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi-Cloud">RuoYi-Cloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>采用前后端分离的模式，微服务版本前端(基于 [RuoYi-Vue](<a href="https://gitee.com/y_project/RuoYi-Vue">https://gitee.com/y_project/RuoYi-Vue</a>))。</li> 
 <li>后端采用Spring Boot、Spring Cloud & Alibaba、Redis。</li> 
 <li>注册中心、配置中心选型Nacos，权限认证使用Redis。</li> 
 <li>流量控制框架选型Sentinel，分布式事务选型Seata。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统模块</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left">com.ruoyi     
├── ruoyi-ui              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 前端框架 [80]</span></span></span></span></span></span>
├── ruoyi-gateway         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 网关模块 [8080]</span></span></span></span></span></span>
├── ruoyi-auth            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 认证中心 [9200]</span></span></span></span></span></span>
├── ruoyi-api             <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 接口模块</span></span></span></span></span></span>
│       └── ruoyi-api-system                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span></span>
├── ruoyi-common          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 通用模块</span></span></span></span></span></span>
│       └── ruoyi-common-core                         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 核心模块</span></span></span></span></span></span>
│       └── ruoyi-common-datascope                    <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 权限范围</span></span></span>
</span></span></span>│       └── ruoyi-common-datasource                   <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// </span></span></span><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">多数据源</span></span></span></span>
│       └── ruoyi-common-<span>log</span>                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 日志记录</span></span></span></span></span></span>
│       └── ruoyi-common-redis                        <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 缓存服务</span></span></span></span></span></span>
│       └── ruoyi-common-security                     <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 安全模块</span></span></span></span></span></span>
│       └── ruoyi-common-swagger                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span></span>
├── ruoyi-modules         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 业务模块</span></span></span></span></span></span>
│       └── ruoyi-system                              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统模块 [9201]</span></span></span></span></span></span>
│       └── ruoyi-gen                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 代码生成 [9202]</span></span></span></span></span></span>
│       └── ruoyi-job                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 定时任务 [9203]</span></span></span></span></span></span>
│       └── ruoyi-file                                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 文件服务 [9300]</span></span></span></span></span></span>
├── ruoyi-visual          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 图形化管理模块</span></span></span></span></span></span>
│       └── ruoyi-visual-monitor                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 监控中心 [9100]</span></span></span></span></span></span>
├──pom.xml                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 公共依赖</span></span></span></span></span></span></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">架构图</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">系统演示  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fruoyi.vip%2F" target="_blank">http://ruoyi.vip</a></h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/1cbcf0e6f257c7d3a063c0e3f2ff989e4b3.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-8074972883b5ba0622e13246738ebba237a.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-9f88719cdfca9af2e58b352a20e23d43b12.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-39bf2584ec3a529b0d5a3b70d15c9b37646.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-936ec82d1f4872e1bc980927654b6007307.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-b2d62ceb95d2dd9b3fbe157bb70d26001e9.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-d67451d308b7a79ad6819723396f7c3d77a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/5e8c387724954459291aafd5eb52b456f53.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/644e78da53c2e92a95dfda4f76e6d117c4b.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-8370a0d02977eebf6dbf854c8450293c937.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-49003ed83f60f633e7153609a53a2b644f7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-d4fe726319ece268d4746602c39cffc0621.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-c195234bbcd30be6927f037a6755e6ab69c.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-ece3fd37a3d4bb75a3926e905a3c5629055.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-92ffb7f3835855cff100fa0f754a6be0d99.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-ff9e3066561574aca73005c5730c6a41f15.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img src="https://oscimg.oschina.net/oscnet/up-5e4daac0bb59612c5038448acbcef235e3a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            