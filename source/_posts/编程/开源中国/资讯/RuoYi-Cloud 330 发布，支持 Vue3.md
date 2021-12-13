
---
title: 'RuoYi-Cloud 3.3.0 发布，支持 Vue3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 08:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依 Cloud 微服务版本<span style="background-color:#ffffff; color:#333333"> v3.3.0 已发布，更新日志：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>新增配套并同步的Vue3前端版本</li> 
 <li>新增认证对象简化权限验证</li> 
 <li>新增tab对象简化页签操作</li> 
 <li>修改获取缓存信息方式</li> 
 <li>修改权限认证注解实现</li> 
 <li>自定义文字复制剪贴指令</li> 
 <li>升级axios到最新版本0.24.0</li> 
 <li>升级core-js到最新版本3.19.1</li> 
 <li>升级jsencrypt到最新版本3.2.1</li> 
 <li>升级js-cookie到最新版本3.0.1</li> 
 <li>升级clipboard到最新版本2.0.8</li> 
 <li>升级velocity到最新版本2.3</li> 
 <li>升级spring-boot到最新版本2.5.6</li> 
 <li>升级spring-boot-admin到最新版2.5.4</li> 
 <li>升级dynamic-ds到最新版本3.5.0</li> 
 <li>代码生成预览支持复制内容</li> 
 <li>修复五级以上菜单出现的404问题</li> 
 <li>生产环境使用路由懒加载提升页面响应速度</li> 
 <li>任务屏蔽违规字符&参数忽略双引号中的逗号</li> 
 <li>优化用户个人信息接口防止修改用户名</li> 
 <li>优化登录/验证码请求headers不设置token</li> 
 <li>优化注册成功提示消息类型success</li> 
 <li>优化下载解析blob响应是否登录失效</li> 
 <li>修复字符串无法被反转义问题</li> 
 <li>修复响应体过大出现的乱码问题</li> 
 <li>修复回显数据字典组的键值错误</li> 
 <li>修复代码生成复选框字典遗漏问题</li> 
 <li>修复代码生成模板主子表删除缺少事务</li> 
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
├── ruoyi-ui              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 前端框架 [80]</span></span></span></span></span></span></span>
├── ruoyi-gateway         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 网关模块 [8080]</span></span></span></span></span></span></span>
├── ruoyi-auth            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 认证中心 [9200]</span></span></span></span></span></span></span>
├── ruoyi-api             <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 接口模块</span></span></span></span></span></span></span>
│       └── ruoyi-api-system                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span></span></span>
├── ruoyi-common          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 通用模块</span></span></span></span></span></span></span>
│       └── ruoyi-common-core                         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 核心模块</span></span></span></span></span></span></span>
│       └── ruoyi-common-datascope                    <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 权限范围</span></span></span></span>
</span></span></span>│       └── ruoyi-common-datasource                   <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// </span></span></span></span><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">多数据源</span></span></span></span></span>
│       └── ruoyi-common-<span><span>log</span></span>                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 日志记录</span></span></span></span></span></span></span>
│       └── ruoyi-common-redis                        <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 缓存服务</span></span></span></span></span></span></span>
│       └── ruoyi-common-security                     <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 安全模块</span></span></span></span></span></span></span>
│       └── ruoyi-common-swagger                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span></span></span>
├── ruoyi-modules         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 业务模块</span></span></span></span></span></span></span>
│       └── ruoyi-system                              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统模块 [9201]</span></span></span></span></span></span></span>
│       └── ruoyi-gen                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 代码生成 [9202]</span></span></span></span></span></span></span>
│       └── ruoyi-job                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 定时任务 [9203]</span></span></span></span></span></span></span>
│       └── ruoyi-file                                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 文件服务 [9300]</span></span></span></span></span></span></span>
├── ruoyi-visual          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 图形化管理模块</span></span></span></span></span></span></span>
│       └── ruoyi-visual-monitor                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 监控中心 [9100]</span></span></span></span></span></span></span>
├──pom.xml                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 公共依赖</span></span></span></span></span></span></span></pre> 
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
<p> </p>
                                        </div>
                                      
</div>
            