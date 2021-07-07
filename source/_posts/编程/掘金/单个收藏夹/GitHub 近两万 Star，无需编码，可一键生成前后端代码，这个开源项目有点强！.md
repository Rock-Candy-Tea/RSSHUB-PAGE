
---
title: 'GitHub 近两万 Star，无需编码，可一键生成前后端代码，这个开源项目有点强！'
categories: 
 - 编程
 - 掘金
 - 单个收藏夹
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9721198117794f459fc56eecaa44f903~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 13 Mar 2021 20:36:50 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9721198117794f459fc56eecaa44f903~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>公众号：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ft.1yb.co%2Fjwkk" target="_blank" rel="nofollow noopener noreferrer" title="https://t.1yb.co/jwkk" ref="nofollow noopener noreferrer">Java小咖秀</a>，网站：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.javaxks.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.javaxks.com" ref="nofollow noopener noreferrer">javaxks.com</a></p>
</blockquote>
<blockquote>
<p>作者 : zhangdaiscott,   链接:  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhangdaiscott/jeecg-boot" ref="nofollow noopener noreferrer">github.com/zhangdaisco…</a></p>
</blockquote>
<h3 data-id="heading-0">项目介绍：</h3>
<p>JeecgBoot 是一款基于代码生成器的低代码开发平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT，支持微服务。强大的代码生成器让前后端代码一键生成，实现低代码开发! JeecgBoot 引领新的低代码开发模式(OnlineCoding-> 代码生成器-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省研发成本，同时又不失灵活性！</p>
<p>JeecgBoot 提供了一系列低代码模块，实现在线开发真正的零代码：Online表单开发、Online报表、报表配置能力、在线图表设计、大屏设计、移动配置能力、表单设计器、在线设计流程、流程自动化配置、插件能力（可插拔）等等！</p>
<p>JEECG宗旨是: 简单功能由OnlineCoding配置实现，做到零代码开发；复杂功能由代码生成器生成进行手工Merge 实现低代码开发，既保证了智能又兼顾灵活；实现了低代码开发的同时又支持灵活编码，解决了当前低代码产品普遍不灵活的弊端！</p>
<p>JEECG业务流程: 采用工作流来实现、扩展出任务接口，供开发编写业务逻辑，表单提供多种解决方案：表单设计器、online配置表单、编码表单。同时实现了流程与表单的分离设计（松耦合）、并支持任务节点灵活配置，既保证了公司流程的保密性，又减少了开发人员的工作量。</p>
<h3 data-id="heading-1">适用项目</h3>
<p>Jeecg-Boot低代码开发平台，可以应用在任何J2EE项目的开发中，尤其适合SAAS项目、企业信息管理系统（MIS）、内部办公系统（OA）、企业资源计划系统（ERP）、客户关系管理系统（CRM）等，其半智能手工Merge的开发方式，可以显著提高开发效率70%以上，极大降低开发成本。</p>
<h3 data-id="heading-2">技术架构：</h3>
<h4 data-id="heading-3">开发环境</h4>
<ul>
<li>语言：Java 8</li>
<li>IDE(JAVA)：IDEA / Eclipse安装lombok插件</li>
<li>IDE(前端)：WebStorm 或者 IDEA</li>
<li>依赖管理：Maven</li>
<li>数据库：MySQL5.7+ & Oracle 11g & Sqlserver2017</li>
<li>缓存：Redis</li>
</ul>
<h4 data-id="heading-4">后端</h4>
<ul>
<li>基础框架：Spring Boot 2.3.5.RELEASE</li>
<li>微服务框架：Spring Cloud Alibaba 2.2.3.RELEASE</li>
<li>持久层框架：Mybatis-plus 3.4.1</li>
<li>安全框架：Apache Shiro 1.7.0，Jwt 3.11.0</li>
<li>微服务技术栈：Spring Cloud Alibaba、Nacos、Gateway、Sentinel、Skywarking</li>
<li>数据库连接池：阿里巴巴Druid 1.1.22</li>
<li>缓存框架：redis</li>
<li>日志打印：logback</li>
<li>其他：fastjson，poi，Swagger-ui，quartz, lombok（简化代码）等。</li>
</ul>
<h4 data-id="heading-5">前端</h4>
<ul>
<li>Vue 2.6.10</li>
<li>Axios</li>
<li>ant-design-vue</li>
<li>webpack,</li>
<li>vue-cropper- 头像裁剪组件</li>
<li>@antv/g2 - Alipay AntV 数据可视化图表</li>
<li>Viser-vue - antv/g2 封装实现</li>
<li>eslint，@vue/cli 3.2.1</li>
<li>vue-print-nb - 打印</li>
</ul>
<h4 data-id="heading-6">功能模块</h4>
<pre><code class="hljs language-java copyable" lang="java">├─系统管理
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
│  └─多租户管理
├─消息中心
│  ├─消息管理
│  ├─模板管理
├─代码生成器(低代码)
│  ├─代码生成器功能（一键生成前后端代码，生成后无需修改直接用，绝对是后端开发福音）
│  ├─代码生成器模板（提供<span class="hljs-number">4</span>套模板，分别支持单表和一对多模型，不同风格选择）
│  ├─代码生成器模板（生成代码，自带excel导入导出）
│  ├─查询过滤器（查询逻辑无需编码，系统根据页面配置自动生成）
│  ├─高级查询器（弹窗自动组合查询条件）
│  ├─Excel导入导出工具集成（支持单表，一对多 导入导出）
│  ├─平台移动自适应支持
├─系统监控
│  ├─Gateway路由网关
│  ├─性能扫描监控
│  │  ├─监控 Redis
│  │  ├─Tomcat
│  │  ├─jvm
│  │  ├─服务器信息
│  │  ├─请求追踪
│  │  ├─磁盘监控
│  ├─定时任务
│  ├─系统日志
│  ├─消息中心（支持短信、邮件、微信推送等等）
│  ├─数据日志（记录数据快照，可对比快照，查看数据变更情况）
│  ├─系统通知
│  ├─SQL监控
│  ├─swagger-ui(在线接口文档)
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
│─常用示例
│  ├─自定义组件
│  ├─对象存储(对接阿里云)
│  ├─JVXETable示例（各种复杂ERP布局示例）
│  ├─单表模型例子
│  └─一对多模型例子
│  └─打印例子
│  └─一对多TAB例子
│  └─内嵌table例子
│  └─常用选择组件
│  └─异步树table
│  └─接口模拟测试
│  └─表格合计示例
│  └─异步树列表示例
│  └─一对多JEditable
│  └─JEditable组件示例
│  └─图片拖拽排序
│  └─图片翻页
│  └─图片预览
│  └─PDF预览
│  └─分屏功能
│─封装通用组件 
│  ├─行编辑表格JEditableTable
│  └─省略显示组件
│  └─时间控件
│  └─高级查询
│  └─用户选择组件
│  └─报表组件封装
│  └─字典组件
│  └─下拉多选组件
│  └─选人组件
│  └─选部门组件
│  └─通过部门选人组件
│  └─封装曲线、柱状图、饼状图、折线图等等报表的组件（经过封装，使用简单）
│  └─在线code编辑器
│  └─上传文件组件
│  └─验证码组件
│  └─树列表组件
│  └─表单禁用组件
│  └─等等
│─更多页面模板
│  ├─各种高级表单
│  ├─各种列表效果
│  └─结果页面
│  └─异常页面
│  └─个人页面
├─高级功能
│  ├─系统编码规则
│  ├─提供单点登录CAS集成方案
│  ├─提供APP发布方案
│  ├─集成Websocket消息通知机制
├─Online在线开发(低代码)
│  ├─Online在线表单 - 功能已开放
│  ├─Online代码生成器 - 功能已开放
│  ├─Online在线报表 - 功能已开放
│  ├─Online在线图表(暂不开源)
│  ├─Online图表模板配置(暂不开源)
│  ├─Online布局设计(暂不开源)
│  ├─多数据源管理 - 功能已开放
├─积木报表设计器(低代码)
│  ├─打印设计器
│  ├─数据报表设计
│  ├─图形报表设计（支持echart）
│  ├─大屏设计器(暂不开源)
│─流程模块功能 (暂不开源)
│  ├─流程设计器
│  ├─在线表单设计
│  └─我的任务
│  └─历史流程
│  └─历史流程
│  └─流程实例管理
│  └─流程监听管理
│  └─流程表达式
│  └─我发起的流程
│  └─我的抄送
│  └─流程委派、抄送、跳转
│  └─。。。
└─其他模块
   └─更多功能开发中。。
   
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">微服务整体解决方案</h3>
<h4 data-id="heading-8">微服务架构图</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9721198117794f459fc56eecaa44f903~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">Jeecg Boot 产品功能蓝图</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cd21262d990498e838bc7eb30fc29fb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">项目下载和运行</h3>
<ul>
<li>拉取项目代码</li>
</ul>
<pre><code class="copyable">git clone https://github.com/zhangdaiscott/jeecg-boot.git
cd  jeecg-boot/ant-design-jeecg-vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.安装node.js</p>
<p>2.切换到ant-design-jeecg-vue文件夹下</p>
<pre><code class="hljs language-java copyable" lang="java"># 安装yarn
npm install -g yarn

# 下载依赖
yarn install

# 启动
yarn run serve

# 编译项目
yarn run build

# Lints and fixes files
yarn run lint
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">系统效果</h3>
<h4 data-id="heading-12">大屏模板</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/833a028a474144b0b6dd4460d842d275~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0589c221efa848949a955a62bbffe62b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">PC端</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2532c8aab8c44caba8e97800657cc465~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/166b5bfe69db499cb5609216203afad4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4560b9504ac4254a3bc6d6b81dc609a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94e76911d0484ec1b7b3f6472fdba378~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/defc90d5c9cd438d9c534308922a90df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">在线接口文档</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb58df709ded4ccb8fbee8a7afaa8a50~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be1d3b30ab3048f1ab88b661b885e69b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">报表</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/091a6bb7edbd4666a94853eb5702481a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2fe47292ccd40e5b0650cfe46249a72~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00e9bbc0e0b9476eb4032139e84eb96f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">流程</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1d1394ed1834aaea23d809c87abd207~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7a8ff0b76014f8197b61c7fe4ac64d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb63b7b931aa482db932f7465376100f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6f526d897eb4b079c54980ea515e4f3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">手机端</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15456d5fc3624b24b445b41660c67b24~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">PAD端</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/242594b39ab04df3827f54e040ce9e2f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3ec54dd07340819d3916342e66290a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">其他说明</h3>
<ul>
<li>项目使用的 vue-cli3, 请更新您的 cli</li>
<li>关闭 Eslint (不推荐) 移除 package.json 中 eslintConfig 整个节点代码</li>
<li>修改 Ant Design 配色，在文件 vue.config.js 中，其他 less 变量覆盖参考 ant design 官方说明</li>
</ul>
<pre><code class="copyable">  css: &#123;
    loaderOptions: &#123;
      less: &#123;
        modifyVars: &#123;
          /* less 变量覆盖，用于自定义 ant design 主题 */

          'primary-color': '#F5222D',
          'link-color': '#F5222D',
          'border-radius-base': '4px',
        &#125;,
        javascriptEnabled: true,
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            