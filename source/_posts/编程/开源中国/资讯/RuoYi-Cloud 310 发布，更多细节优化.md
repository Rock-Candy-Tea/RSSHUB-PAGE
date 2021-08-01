
---
title: 'RuoYi-Cloud 3.1.0 发布，更多细节优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
author: 开源中国
comments: false
date: Sun, 01 Aug 2021 09:15:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">若依Cloud微服务版本<span style="background-color:#ffffff; color:#333333"> v3.1.0 已发布，更新日志：</span></p> 
<ol> 
 <li>支持配置XSS跨站脚本过滤</li> 
 <li>支持配置验证码开关&类型</li> 
 <li>新增是否开启用户注册功能</li> 
 <li>用户管理新增分配角色功能</li> 
 <li>角色管理新增分配用户功能</li> 
 <li>系统布局配置支持动态标题开关</li> 
 <li>增加字典标签样式回显dict组件</li> 
 <li>FileUpload组件支持多文件上传</li> 
 <li>ImageUpload组件支持多图片上传</li> 
 <li>封装通用iframe组件</li> 
 <li>菜单路由配置支持内链访问</li> 
 <li>全局注册通用组件</li> 
 <li>富文本默认上传返回url类型</li> 
 <li>富文本新增上传文件大小限制</li> 
 <li>增加自定义弹窗拖拽指令</li> 
 <li>顶部菜单排除隐藏的默认路由</li> 
 <li>跳转路由高亮相对应的菜单栏</li> 
 <li>日志列表支持排序操作</li> 
 <li>分页组件新增pagerCount属性</li> 
 <li>定时任务屏蔽http(s)远程调用</li> 
 <li>文件服务本地资源允许跨域访问</li> 
 <li>升级spring-boot到最新版本2.5.3</li> 
 <li>升级spring-boot-admin到最新版2.4.3</li> 
 <li>升级spring-boot-mybatis到最新版2.2.0</li> 
 <li>升级nacos到最新版2.0.3</li> 
 <li>升级pagehelper到最新版1.3.1</li> 
 <li>升级minio到最新版本8.2.2</li> 
 <li>升级tobato到最新版本1.27.2</li> 
 <li>升级dynamic-ds到最新版本3.4.1</li> 
 <li>升级commons.io到最新版本v2.11.0</li> 
 <li>升级common-pool到最新版本2.10.0</li> 
 <li>升级commons.fileupload到最新版本v1.4</li> 
 <li>升级element-ui到最新版本2.15.3</li> 
 <li>优化统一网关错误码响应</li> 
 <li>修复导出含params属性对象参数问题</li> 
 <li>修复任意账户越权问题</li> 
 <li>修复定时任务日志执行状态显示</li> 
 <li>修改登录失效返回值code401</li> 
 <li>用户信息长度校验限制</li> 
 <li>角色&菜单新增字段属性提示信息</li> 
 <li>修复用户搜索分页变量错误</li> 
 <li>优化部门父级启用状态</li> 
 <li>启用部门状态排除顶级节点</li> 
 <li>定时任务新增更多操作</li> 
 <li>优化代码生成模板</li> 
 <li>优化顶部菜单显示样式</li> 
 <li>优化导入用户显示样式</li> 
 <li>优化用户不能删除自己</li> 
 <li>密码框新增显示切换密码图标</li> 
 <li>BLOB下载时清除URL对象引用</li> 
 <li>其他细节优化</li> 
</ol> 
<p style="text-align:left">基于Spring Boot、Spring Cloud & Alibaba、Redis的分布式微服务架构权限管理系统。</p> 
<p style="text-align:left">下载地址<a href="https://gitee.com/y_project/RuoYi-Cloud">RuoYi-Cloud</a></p> 
<p style="text-align:left">若依是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。</p> 
<ul> 
 <li>采用前后端分离的模式，微服务版本前端(基于 [RuoYi-Vue](<a href="https://gitee.com/y_project/RuoYi-Vue">https://gitee.com/y_project/RuoYi-Vue</a>))。</li> 
 <li>后端采用Spring Boot、Spring Cloud & Alibaba、Redis。</li> 
 <li>注册中心、配置中心选型Nacos，权限认证使用Redis。</li> 
 <li>流量控制框架选型Sentinel，分布式事务选型Seata。</li> 
</ul> 
<h2 style="text-align:left">系统模块</h2> 
<pre style="text-align:left">com.ruoyi     
├── ruoyi-ui              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 前端框架 [80]</span></span></span></span></span>
├── ruoyi-gateway         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 网关模块 [8080]</span></span></span></span></span>
├── ruoyi-auth            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 认证中心 [9200]</span></span></span></span></span>
├── ruoyi-api             <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 接口模块</span></span></span></span></span>
│       └── ruoyi-api-system                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span>
├── ruoyi-common          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 通用模块</span></span></span></span></span>
│       └── ruoyi-common-core                         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 核心模块</span></span></span></span></span>
│       └── ruoyi-common-datascope                    <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 权限范围</span></span>
</span></span></span>│       └── ruoyi-common-datasource                   <span style="color:#6a737d"><span style="color:#6a737d">// </span></span><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">多数据源</span></span></span>
│       └── ruoyi-common-log                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 日志记录</span></span></span></span></span>
│       └── ruoyi-common-redis                        <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 缓存服务</span></span></span></span></span>
│       └── ruoyi-common-security                     <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 安全模块</span></span></span></span></span>
│       └── ruoyi-common-swagger                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span></span>
├── ruoyi-modules         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 业务模块</span></span></span></span></span>
│       └── ruoyi-system                              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统模块 [9201]</span></span></span></span></span>
│       └── ruoyi-gen                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 代码生成 [9202]</span></span></span></span></span>
│       └── ruoyi-job                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 定时任务 [9203]</span></span></span></span></span>
│       └── ruoyi-file                                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 文件服务 [9300]</span></span></span></span></span>
├── ruoyi-visual          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 图形化管理模块</span></span></span></span></span>
│       └── ruoyi-visual-monitor                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 监控中心 [9100]</span></span></span></span></span>
├──pom.xml                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 公共依赖</span></span></span></span></span></pre> 
<h2 style="text-align:left">架构图</h2> 
<p style="text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">系统演示  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fruoyi.vip%2F" target="_blank">http://ruoyi.vip</a></h3> 
<table cellspacing="0" style="width:776px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/cd1f90be5f2684f4560c9519c0f2a232ee8.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/1cbcf0e6f257c7d3a063c0e3f2ff989e4b3.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-8074972883b5ba0622e13246738ebba237a.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-9f88719cdfca9af2e58b352a20e23d43b12.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-39bf2584ec3a529b0d5a3b70d15c9b37646.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-936ec82d1f4872e1bc980927654b6007307.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-b2d62ceb95d2dd9b3fbe157bb70d26001e9.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-d67451d308b7a79ad6819723396f7c3d77a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/5e8c387724954459291aafd5eb52b456f53.jpg" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/644e78da53c2e92a95dfda4f76e6d117c4b.jpg" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-8370a0d02977eebf6dbf854c8450293c937.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-49003ed83f60f633e7153609a53a2b644f7.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-d4fe726319ece268d4746602c39cffc0621.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-c195234bbcd30be6927f037a6755e6ab69c.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-ece3fd37a3d4bb75a3926e905a3c5629055.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-92ffb7f3835855cff100fa0f754a6be0d99.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-ff9e3066561574aca73005c5730c6a41f15.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img src="https://oscimg.oschina.net/oscnet/up-5e4daac0bb59612c5038448acbcef235e3a.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            