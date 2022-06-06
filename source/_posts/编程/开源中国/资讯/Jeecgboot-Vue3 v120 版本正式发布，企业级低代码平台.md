
---
title: 'Jeecgboot-Vue3 v1.2.0 版本正式发布，企业级低代码平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142327.png'
author: 开源中国
comments: false
date: Mon, 06 Jun 2022 16:12:00 GMT
thumbnail: 'https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142327.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Jeecgboot-Vue3 采用 Vue3.0、Vite、 Ant-Design-Vue、TypeScript 等新技术方案，包括二次封装组件、utils、hooks、动态菜单、权限校验、按钮级别权限控制等功能。JeecgBoot 企业级的低代码平台对应的 vue3 前端版本！</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">强大的代码生成器让前后端代码一键生成！JeecgBoot 引领低代码开发模式 (OnlineCoding-> 代码生成 -> 手工 MERGE)， 帮助解决 Java 项目 70% 的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v1.2.0 | 2022-06-06</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">源码下载</h3> 
<p>Github</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3" target="_blank">https://github.com/jeecgboot/jeecgboot-vue3</a></li> 
 <li>后端：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
</ul> 
<p>Gitee</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>前端：<a href="https://gitee.com/jeecg/jeecgboot-vue3">https://gitee.com/jeecg/jeecgboot-vue3</a></li> 
 <li>后端：<a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">技术文档</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue3.jeecg.com" target="_blank">http://vue3.jeecg.com</a></li> 
 <li>官方网站：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>在线演示：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot3.jeecg.com" target="_blank">http://boot3.jeecg.com</a></li> 
 <li>快速入门：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1V34y187Y9" target="_blank">入门视频</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue3.jeecg.com%2F2677352" target="_blank">代码生成</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">升级日志</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">此版本重点支持 online 表单、online 报表、popup 等新功能，升级修复很多已知 bug、解决首次访问慢等问题。</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">重点升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持低代码模块：online 表单、online 报表</li> 
 <li>新增数字范围组件 JRangeNumber</li> 
 <li>支持 popup 弹窗组件</li> 
 <li>JVxeTable 支持键盘操作</li> 
 <li>vite 首次打开界面加载慢问题 / 解决</li> 
 <li>框架进行整体大重构，解决非常多问题</li> 
 <li>支持 jeeccgboot3.2.0 版本的路由配置界面</li> 
 <li>【签名改造】 X-TIMESTAMP 牵扯</li> 
 <li>【websocket 安全】websocket 服务端，存在性能和安全问题。 #3278</li> 
 <li>修复目前后台接口挂了界面跳转 404, 改为直接跳转到登录界面</li> 
 <li>调用表单的 resetFields 不会清空当前信息，界面显示上一次的数据</li> 
 <li>设置 disabled，图片上传没有被禁用</li> 
 <li>【vue3】用户管理抽屉移动不能自适应</li> 
 <li>解决菜单配置外部网址带 #号，打不开的问题</li> 
 <li>租户管理确认删除样式问题</li> 
 <li>职务管理，职务编码重复时，没有友好提示</li> 
 <li>修复更多下拉菜单，只有点到字上才有效</li> 
 <li>解决字典组件，赋值的时候，闪动效果</li> 
 <li>系统管理等功能 页面样式、引入文件首字母大小写不匹配问题修复</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Issues 处理</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>vue3 编辑功能无效<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I52955">#I52955</a></li> 
 <li>顶部菜单混合模式与想象中的不一样，应该是有顶部菜单，点击对应的顶部菜单显示左侧菜单<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I4YRRC">#I4YRRC</a></li> 
 <li>按时间查询，浏览器会提示无效的时间<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I51WTI">#I51WTI</a></li> 
 <li>点击 popup 弹框报错<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I4YZE2">#I4YZE2</a></li> 
 <li>使用 vue2 版本 online 生成的 vue3 代码中，出现 activeKey.value=ref ('XXX') 的情况<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I515ZE">#I515ZE</a></li> 
 <li>用 docker 构建报 JavaScript heap out of memory<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I530MB">#I530MB</a></li> 
 <li>首页功能搜索功能，当搜索结果为菜单含子菜单时，选中此菜单，路由前端错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F33" target="_blank">#33</a></li> 
 <li>使用自定义组件 Table 刷新 报错<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F40" target="_blank">#40</a></li> 
 <li>VUE3 启用 CAS SSO 后项目打包后无法获取到配置环境变量<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F38" target="_blank">#38</a></li> 
 <li>RangePicker 日期区间选择器异常<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I53NY4">#I53NY4</a></li> 
 <li>使用 JSelectInput 控件，当输入用户自己的标签时，点击清空按钮会报错<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I52BN3">#I52BN3</a></li> 
 <li>注释错别字<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F29" target="_blank">#29</a></li> 
 <li>vue3 首页打开慢<a href="https://gitee.com/jeecg/jeecg-boot/issues/I53WHR">#I53WHR</a></li> 
 <li>代码生成器生成列表页面批量删除操作后” 已选择 n 条记录 “不自动清空<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F34" target="_blank">#34</a></li> 
 <li>useJvxeMethods.ts 打包后 getAllTable () 方法 tableRefs 没有值<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I4ZWFP">#I4ZWFP</a></li> 
 <li>jvxe 无法进行行禁用<a href="https://gitee.com/jeecg/jeecg-boot/issues/I52YEI">#I52YEI</a></li> 
 <li>数据字典，_ 属于特殊字符，添加不了数据<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I52VH2">#I52VH2</a></li> 
 <li>使用 vue2 的 online 代码生成器生成的代码中，edit 时，没有将 id 暂存，导致更新时传至后台的数据缺少 id 报错<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I51EAR">#I51EAR</a></li> 
 <li>如何获取动态的路由地址，或者如何改成为顶部主菜单 配合左侧次级菜单<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F36" target="_blank">#36</a></li> 
 <li>日期区间组件 RangePicker<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I53G9Y">#I53G9Y</a></li> 
 <li>JSelectUser 组件请求值异常<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I53VZH">#I53VZH</a></li> 
 <li>ts 文件热更新失效<a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I4ZSQD">#I4ZSQD</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装与使用</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Get the project code</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#005cc5">git</span> clone https://github.com/jeecgboot/jeecgboot-vue3.git
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Installation dependencies</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">cd</span> <span style="color:#032f62">jeecgboot-vue3</span>
<span style="color:#6f42c1">yarn</span> <span style="color:#032f62">install</span>
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>配置后台接口地址</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">.env</span><span style="color:#6f42c1">.development</span>
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>run</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">yarn</span> <span style="color:#032f62">serve</span>
</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>build</li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">yarn</span> <span style="color:#032f62">build</span>
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">系统效果</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">系统后台</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142327.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142354.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142339.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142409.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_20220310142401.png" referrerpolicy="no-referrer"><span> </span><img alt="输入图片说明" src="https://jeecgos.oss-cn-beijing.aliyuncs.com/files/site/vue3_11.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Online 表单 & Online 报表<span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-e8862f2c3c14eace9090c20a8fb928234a4.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-e3b3a736236bc66f255a9a32ab3f9b7196b.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-221b8cbdea3c17d31a1365023a73d3d439f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">报表效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://static.oschina.net/uploads/img/201904/14160828_pkFr.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160834_Lo23.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160842_QK7B.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160849_GBm5.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160858_6RAM.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">接口文档</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-e6ea09dbaa01b8458c2e23614077ba9507f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">流程设计 & 表单设计</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-fe98e9f766e5abb6759f6f13d5f9186f0cf.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160917_9Ftz.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201904/14160633_u59G.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://static.oschina.net/uploads/img/201907/05165142_yyQ7.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">报表设计</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-da89eb034b8583d57b3f61493fec313ed28.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-35deca9d020d61ad464accfdeb3bb90ba5c.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-d1695b4a53ebbc9e9651e309e5af1c8bd30.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://oscimg.oschina.net/oscnet/up-4cc634b612e97f08ab702ef34f2ede53f2a.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">大屏模板</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://static.oschina.net/uploads/img/201912/25133248_Ag1C.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://static.oschina.net/uploads/img/201912/25133301_k9Kc.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-649cb79c01eb95d5c2217a5dad28515da82.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能模块</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Vue3 版已实现了系统管理、系统监控、报表、各种组件、前端权限、GUI 代码生成、Online 表单、Online 报表等平台功能。</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>├─首页
│  ├─首页（四套首页满足不同场景需求）
│  ├─工作台
├─系统管理
│  ├─用户管理
│  ├─角色管理
│  ├─菜单管理
│  ├─权限设置（支持按钮权限、数据权限）
│  ├─表单权限（控制字段禁用、隐藏）
│  ├─部门管理
│  ├─我的部门（二级管理员）
│  └─字典管理
│  └─分类字典
│  └─系统公告
│  └─职务管理
│  └─通讯录
│  └─对象存储
│  └─多租户管理
├─系统监控
│  ├─网关路由配置（<span style="color:#d73a49">gateway</span>）
│  ├─定时任务
│  ├─数据源管理
│  ├─系统日志
│  ├─消息中心（支持短信、邮件、微信推送等等）
│  ├─数据日志（记录数据快照，可对比快照，查看数据变更情况）
│  ├─系统通知
│  ├─<span style="color:#d73a49">SQL</span>监控
│  ├─性能监控
│  │  ├─监控 <span style="color:#d73a49">Redis</span>
│  │  ├─<span style="color:#d73a49">Tomcat</span>
│  │  ├─<span style="color:#d73a49">jvm</span>
│  │  ├─服务器信息
│  │  ├─请求追踪
│  │  ├─磁盘监控
├─消息中心
│  ├─我的消息
│  ├─消息管理
│  ├─模板管理
├─积木报表设计器
│─报表示例
│  ├─曲线图
│  └─饼状图
│  └─柱状图
│  └─折线图
│  └─面积图
│  └─雷达图
│  └─仪表图
│  └─进度条
│  └─排名列表
│  └─等等
│─大屏模板
│  ├─作战指挥中心大屏
│  └─物流服务中心大屏
├─代码生成器（<span style="color:#d73a49">GUI</span>）
│  ├─代码生成器功能（一键生成前后端代码，生成后无需修改直接用，绝对是后端开发福音）
│  ├─代码生成器模板（提供<span style="color:#d73a49">4</span>套模板，分别支持单表和一对多模型，不同风格选择）
│  ├─代码生成器模板（生成代码，自带<span style="color:#d73a49">excel</span>导入导出）
│  ├─查询过滤器（查询逻辑无需编码，系统根据页面配置自动生成）
│  ├─高级查询器（弹窗自动组合查询条件）
│  ├─<span style="color:#d73a49">Excel</span>导入导出工具集成（支持单表，一对多 导入导出）
│  ├─平台移动自适应支持
│─常用示例
│  ├─自定义组件示例
│  ├─<span style="color:#d73a49">JVxeTable</span>示例(ERP行业复杂排版效果)
│  ├─单表模型例子
│  └─一对多模型例子
│  └─打印例子
│  └─一对多内嵌示例
│  └─异步树<span style="color:#d73a49">Table</span>
│  └─图片拖拽排序
│  └─图片翻页
│  └─图片预览
│  └─<span style="color:#d73a49">PDF</span>预览
│─封装通用组件
│  ├─行编辑表格<span style="color:#d73a49">JVxeTable</span>
│  └─省略显示组件
│  └─时间控件
│  └─高级查询 (未实现)
│  └─用户选择组件
│  └─报表组件封装
│  └─字典组件
│  └─下拉多选组件
│  └─选人组件
│  └─选部门组件
│  └─通过部门选人组件
│  └─封装曲线、柱状图、饼状图、折线图等等报表的组件（经过封装，使用简单）
│  └─在线<span style="color:#d73a49">code</span>编辑器
│  └─上传文件组件
│  └─树列表组件
│  └─表单禁用组件
│  └─等等
│─更多页面模板
│  └─<span style="color:#d73a49">Mock</span>示例（子菜单很多）
│  └─页面<span style="color:#d73a49">&</span>导航（子菜单很多）
│  └─组件<span style="color:#d73a49">&</span>功能（子菜单很多）
├─高级功能
│  ├─支持微前端
│  ├─提供<span style="color:#d73a49">CAS</span>单点登录
│  ├─集成<span style="color:#d73a49">Websocket</span>消息通知机制
│  ├─支持第三方登录（<span style="color:#d73a49">QQ</span>、钉钉、微信等）
│  ├─系统编码规则
├─<span style="color:#d73a49">Online</span>在线开发
│  ├─<span style="color:#d73a49">Online</span>在线表单 
│  ├─<span style="color:#d73a49">Online</span>代码生成器
│  ├─<span style="color:#d73a49">Online</span>在线报表 
└─更多功能开发中。。
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">入门必备</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本项目需要一定前端基础知识，请确保掌握 Vue 的基础知识，以便能处理一些常见的问题。 建议在开发前先学一下以下内容，提前了解和学习这些知识，会对项目理解非常有帮助:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2F" target="_blank">Vue3 文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.typescriptlang.org%2F" target="_blank">TypeScript</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnext.router.vuejs.org%2F" target="_blank">Vue-router</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2F2x.antdv.com%2Fdocs%2Fvue%2Fintroduce-cn%2F" target="_blank">Ant-Design-Vue</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvvbin.cn%2Fdoc-next" target="_blank">Vben 文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank">Es6</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitejs.dev%2F" target="_blank">Vitejs</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpinia.esm.dev%2Fintroduction.html" target="_blank">Pinia (vuex 替代方案)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Frfcs" target="_blank">Vue-RFCS</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fguide%2Fmigration%2Fintroduction.html" target="_blank">Vue2 迁移到 3</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">浏览器支持</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本地开发</strong>推荐使用<span> </span><code>Chrome 最新版</code>浏览器，<strong>不支持</strong><code>Chrome 80</code><span> </span>以下版本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>生产环境</strong>支持现代浏览器，不支持 IE。</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="IE" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/archive/internet-explorer_9-11/internet-explorer_9-11_48x48.png" referrerpolicy="no-referrer"></a>IE</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt=" Edge" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png" referrerpolicy="no-referrer"></a>Edge</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="Firefox" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png" referrerpolicy="no-referrer"></a>Firefox</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="Chrome" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" referrerpolicy="no-referrer"></a>Chrome</th> 
   <th><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgodban.github.io%2Fbrowsers-support-badges%2F" target="_blank"><img alt="Safari" src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png" referrerpolicy="no-referrer"></a>Safari</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">not support</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">last 2 versions</td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            