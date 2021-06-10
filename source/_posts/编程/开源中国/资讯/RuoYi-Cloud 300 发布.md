
---
title: 'RuoYi-Cloud 3.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
author: 开源中国
comments: false
date: Thu, 10 Jun 2021 01:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-82e9722ecb846786405a904bafcf19f73f3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">若依Cloud微服务版本<span style="background-color:#ffffff; color:#333333"> v3.0.0 已发布，更新日志：</span></p> 
<ol> 
 <li>新增菜单导航显示风格TopNav（false为左侧导航菜单，true为顶部导航菜单）</li> 
 <li>布局设置支持保存&重置配置</li> 
 <li>富文本编辑器支持自定义上传地址</li> 
 <li>富文本编辑组件新增readOnly属性</li> 
 <li>优化参数&字典缓存操作</li> 
 <li>新增IE浏览器版本过低提示页面</li> 
 <li>页签TagsView新增关闭右侧功能</li> 
 <li>显隐列组件加载初始默认隐藏列</li> 
 <li>关闭头像上传窗口还原默认图片</li> 
 <li>个人信息添加手机&邮箱重复验证</li> 
 <li>代码生成模板树表操作列添加新增按钮</li> 
 <li>代码生成模板修复主子表字段重名问题</li> 
 <li>支持docker部署项目</li> 
 <li>升级springcloud到最新版2020.0.3</li> 
 <li>升级spring-boot-alibaba到最新版2021.1</li> 
 <li>升级nacos到最新版2.0.1 性能提升</li> 
 <li>升级spring-boot到最新版本2.5.0</li> 
 <li>升级spring-boot-admin到最新版2.4.1</li> 
 <li>升级swagger到最新版本3.0.0</li> 
 <li>升级mybatis到最新版3.5.6</li> 
 <li>升级dynamic-ds到最新版本3.3.2</li> 
 <li>升级minio到最新版本8.2.1</li> 
 <li>升级fastjson到最新版1.2.76</li> 
 <li>升级druid到最新版本v1.2.6</li> 
 <li>修复四级菜单无法显示问题</li> 
 <li>修复树表数据显示不全&加载慢问题</li> 
 <li>修复关闭confirm提示框控制台报错问题</li> 
 <li>上传媒体类型添加视频格式</li> 
 <li>增加feign客户端IP头部信息</li> 
 <li>修复两处存在SQL注入漏洞问题</li> 
 <li>优化图片工具类读取文件，防止异常</li> 
 <li>修复导出角色数据范围翻译缺少仅本人</li> 
 <li>修复表单构建选择下拉选择控制台报错问题</li> 
 <li>修复请求形参未传值记录日志异常问题</li> 
 <li>调整sql默认为当前时间</li> 
 <li>修改ip字段长度防止ipv6地址长度不够</li> 
 <li>删除操作日志记录信息</li> 
 <li>修复firefox下表单构建拖拽会新打卡一个选项卡</li> 
 <li>用户&角色单条删除时使其逻辑删除</li> 
 <li>优化树表代码生成模板</li> 
 <li>修正通知公告日志记录类型</li> 
 <li>修正后端导入表权限标识</li> 
 <li>过滤BindingResult对象，防止异常</li> 
 <li>Redis设置HashKey序列化</li> 
 <li>优化Excel导入增加空行判断</li> 
 <li>树级结构更新子节点使用replaceFirst</li> 
 <li>富文本工具栏配置视频</li> 
 <li>修正模板字符编码</li> 
 <li>优化通用下载完成后删除节点</li> 
 <li>角色非自定义权限范围清空选择值</li> 
 <li>修改主题后mini类型按钮无效问题</li> 
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
├── ruoyi-ui              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 前端框架 [80]</span></span></span></span>
├── ruoyi-gateway         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 网关模块 [8080]</span></span></span></span>
├── ruoyi-auth            <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 认证中心 [9200]</span></span></span></span>
├── ruoyi-api             <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 接口模块</span></span></span></span>
│       └── ruoyi-api-system                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span>
├── ruoyi-common          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 通用模块</span></span></span></span>
│       └── ruoyi-common-core                         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 核心模块</span></span></span></span>
│       └── ruoyi-common-datascope                    <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 权限范围</span>
</span></span></span>│       └── ruoyi-common-datasource                   <span style="color:#6a737d">// </span><span style="color:#6a737d"><span style="color:#6a737d">多数据源</span></span>
│       └── ruoyi-common-log                          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 日志记录</span></span></span></span>
│       └── ruoyi-common-redis                        <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 缓存服务</span></span></span></span>
│       └── ruoyi-common-security                     <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 安全模块</span></span></span></span>
│       └── ruoyi-common-swagger                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统接口</span></span></span></span>
├── ruoyi-modules         <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 业务模块</span></span></span></span>
│       └── ruoyi-system                              <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 系统模块 [9201]</span></span></span></span>
│       └── ruoyi-gen                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 代码生成 [9202]</span></span></span></span>
│       └── ruoyi-job                                 <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 定时任务 [9203]</span></span></span></span>
│       └── ruoyi-file                                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 文件服务 [9300]</span></span></span></span>
├── ruoyi-visual          <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 图形化管理模块</span></span></span></span>
│       └── ruoyi-visual-monitor                      <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 监控中心 [9100]</span></span></span></span>
├──pom.xml                <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">// 公共依赖</span></span></span></span></pre> 
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
            