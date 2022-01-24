
---
title: 'RuoYi-Cloud 3.4.0 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 10:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依 Cloud 微服务版本<span style="background-color:#ffffff; color:#333333"> v3.4.0 已发布，更新日志：</span></p> 
<ul> 
 <li>新增Vue3前端代码生成模板</li> 
 <li>新增图片预览组件</li> 
 <li>新增压缩插件实现打包Gzip</li> 
 <li>新增docker一键复制的脚本</li> 
 <li>自定义xss校验注解实现</li> 
 <li>路由支持单独配置菜单或角色权限</li> 
 <li>前端支持设置是否需要防止数据重复提交</li> 
 <li>预览组件支持多图显示</li> 
 <li>代码生成列表图片支持预览</li> 
 <li>代码生成新增Java类型Boolean</li> 
 <li>定时任务目标字符串过滤特殊字符</li> 
 <li>定时任务目标字符串验证包名白名单</li> 
 <li>升级nacos到最新版2.0.4</li> 
 <li>升级spring-cloud到最新版2021.0.0</li> 
 <li>升级spring-boot到最新版本2.6.3</li> 
 <li>升级spring-boot-admin到最新版2.6.1</li> 
 <li>升级pagehelper到最新版1.4.1</li> 
 <li>升级fastjson到最新版1.2.79</li> 
 <li>SQL工具类新增检查关键字方法</li> 
 <li>修复打包后字体图标偶现的乱码问题</li> 
 <li>修复版本差异导致的懒加载报错问题</li> 
 <li>修复选项卡点击右键刷新丢失参数问题</li> 
 <li>修复登录失效后多次请求提示多次弹窗问题</li> 
 <li>优化加载字典缓存数据</li> 
 <li>优化代码生成同步更新字段</li> 
 <li>优化代码生成字典组重复问题</li> 
 <li>优化空值不进行回显数据字典</li> 
 <li>优化用户导入提示溢出则显示滚动条</li> 
 <li>优化定时任务cron表达式小时设置24</li> 
 <li>优化部门修改缩放后出现的错位问题</li> 
 <li>优化分页方法设置成通用方便灵活调用</li> 
 <li>优化用户管理部门查询选择节点后分页参数初始</li> 
 <li>其他细节优化</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">基于Spring Boot、Spring Cloud & Alibaba、Redis的分布式微服务架构权限管理系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi-Cloud">RuoYi-Cloud</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>采用前后端分离的模式，微服务版本前端(基于 [RuoYi-Vue](<a href="https://gitee.com/y_project/RuoYi-Vue">https://gitee.com/y_project/RuoYi-Vue</a>))。</li> 
 <li>后端采用Spring Boot、Spring Cloud & Alibaba、Redis。</li> 
 <li>注册中心、配置中心选型Nacos，权限认证使用Redis。</li> 
 <li>流量控制框架选型Sentinel，分布式事务选型Seata。</li> 
 <li>* 提供了技术栈(Vue3 Element Plus Vite)版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyangzongzhuan%2FRuoYi-Cloud-Vue3" target="_blank">RuoYi-Cloud-Vue3</a>，保持同步更新。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统模块</h2> 
<pre style="margin-left:0; margin-right:0; text-align:left">com.ruoyi     
├── ruoyi-ui              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 前端框架 [80]</span></span></span></span></span></span></span></span>
├── ruoyi-gateway         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 网关模块 [8080]</span></span></span></span></span></span></span></span>
├── ruoyi-auth            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 认证中心 [9200]</span></span></span></span></span></span></span></span>
├── ruoyi-api             <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 接口模块</span></span></span></span></span></span></span></span>
│       └── ruoyi-api-system                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span></span></span></span>
├── ruoyi-common          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 通用模块</span></span></span></span></span></span></span></span>
│       └── ruoyi-common-core                         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 核心模块</span></span></span></span></span></span></span></span>
│       └── ruoyi-common-datascope                    <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 权限范围</span></span></span></span></span>
</span></span></span>│       └── ruoyi-common-datasource                   <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// </span></span></span></span></span><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">多数据源</span></span></span></span></span></span>
│       └── ruoyi-common-<span><span><span>log</span></span></span>                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 日志记录</span></span></span></span></span></span></span></span>
│       └── ruoyi-common-redis                        <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 缓存服务</span></span></span></span></span></span></span></span>
│       └── ruoyi-common-security                     <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 安全模块</span></span></span></span></span></span></span></span>
│       └── ruoyi-common-swagger                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span></span></span></span>
├── ruoyi-modules         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 业务模块</span></span></span></span></span></span></span></span>
│       └── ruoyi-system                              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统模块 [9201]</span></span></span></span></span></span></span></span>
│       └── ruoyi-gen                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 代码生成 [9202]</span></span></span></span></span></span></span></span>
│       └── ruoyi-job                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 定时任务 [9203]</span></span></span></span></span></span></span></span>
│       └── ruoyi-file                                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 文件服务 [9300]</span></span></span></span></span></span></span></span>
├── ruoyi-visual          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 图形化管理模块</span></span></span></span></span></span></span></span>
│       └── ruoyi-visual-monitor                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 监控中心 [9100]</span></span></span></span></span></span></span></span>
├──pom.xml                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 公共依赖</span></span></span></span></span></span></span></span></pre> 
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
            