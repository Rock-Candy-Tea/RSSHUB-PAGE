
---
title: '分布式爬虫管理平台 Crawlab v0.6.0 社区版正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://docs.crawlab.cn/assets/img/screenshots/screenshot-home.png'
author: 开源中国
comments: false
date: Mon, 23 May 2022 09:46:00 GMT
thumbnail: 'https://docs.crawlab.cn/assets/img/screenshots/screenshot-home.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1><span style="color:#40b8fa">概览</span></h1> 
<p style="color:#2b2b2b; margin-left:0; margin-right:0">作为一个重要版本发布，Crawlab v0.6.0 由一些重大的功能升级组成，包括性能、稳定性、健壮性、易用性方面的大量优化。本次版本将比老版本更加健壮，特别是任务执行、文件同步、节点通信上面。</p> 
<h2><span style="color:#40b8fa">新版本截图</span></h2> 
<h4><span>主页</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-home.png" referrerpolicy="no-referrer"></p> 
<h4><span>节点列表页</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-node-list.png" referrerpolicy="no-referrer"></p> 
<h4><span>爬虫列表页</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-spider-list.png" referrerpolicy="no-referrer"></p> 
<h4><span>爬虫文件编辑</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-spider-detail-files.png" referrerpolicy="no-referrer"></p> 
<h4><span>任务列表</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-task-list.png" referrerpolicy="no-referrer"></p> 
<h4><span>任务日志</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-task-detail-logs.png" referrerpolicy="no-referrer"></p> 
<h4><span>任务数据</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-task-detail-data.png" referrerpolicy="no-referrer"></p> 
<h4><span>创建定时任务</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-schedule-create.png" referrerpolicy="no-referrer"></p> 
<h4><span>Git 日志</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-git-logs.png" referrerpolicy="no-referrer"></p> 
<h4><span>依赖安装</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-plugin-dependency.png" referrerpolicy="no-referrer"></p> 
<h4><span>爬虫助手插件</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-plugin-spider-assistant.png" referrerpolicy="no-referrer"></p> 
<h4><span>自定义列表</span></h4> 
<p><img alt src="https://docs.crawlab.cn/assets/img/screenshots/screenshot-spider-list-columns-customization.png" referrerpolicy="no-referrer"></p> 
<h2><span style="color:#40b8fa">更新日志</span></h2> 
<h4><span>后端</span></h4> 
<ul style="list-style-type:circle"> 
 <li> <p><strong style="color:#3594f7"><span>「</span>文件同步<span>」</span></strong>. 将文件同步从原先的 MongoDB GridFS 迁移到分布式文件系统 SeaweedFS，以提升文件同步和爬虫部署的稳定性和健壮性。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>节点通信<span>」</span></strong>. 将节点通信从原先基于 Redis 套壳的 RPC 迁移到 gRPC。工作节点通过向主节点发起 gRPC 请求来与 MongoDB 数据库间接交互。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>任务队列<span>」</span></strong>. 将任务队列从 Redis 列表迁移到 MongoDB 集合，以提高灵活性，例如优先级队列。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>日志<span>」</span></strong>. 将日志储存迁移到 SeaweedFS，以解决 MongoDB 数据库中的性能问题。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>SDK 集成<span>」</span></strong>. 将结果数据储存从原生 SDK 迁移到了任务处理器集中导入到数据库。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>任务相关<span>」</span></strong>. 将任务相关逻辑抽象为了任务调度器、任务处理器以及任务执行器，以减少系统耦合度，提升可扩展性和可维护性。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>组件化<span>」</span></strong>. 引入依赖注入框架，将模块、服务以及子系统进行模块化。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>插件框架<span>」</span></strong>. <strong style="color:#3594f7"><span>「</span>Crawlab 插件框架 (CPF)<span>」</span></strong> 已发布. 详情请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.crawlab.cn%2Fzh%2Fguide%2Fplugin%2F" target="_blank">这里</a>.</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>Git 集成<span>」</span></strong>. Git 集成被作为内置功能.</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>Scrapy 集成<span>」</span></strong>. Scrapy 集成以插件形式存在，插件为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.crawlab.cn%2Fzh%2Fguide%2Fplugin%2Fplugin-spider-assistant.html" target="_blank">spider-assistant</a>.</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>依赖集成<span>」</span></strong>. Dependency 集成以插件形式存在，插件为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.crawlab.cn%2Fzh%2Fguide%2Fplugin%2Fplugin-dependency" target="_blank">dependency</a>.</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>消息通知<span>」</span></strong>. 消息通知功能以插件形式存在，插件为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.crawlab.cn%2Fzh%2Fguide%2Fplugin%2Fplugin-notification" target="_blank">notification</a>.</p> </li> 
</ul> 
<h4><span>前端</span></h4> 
<ul style="list-style-type:circle"> 
 <li> <p><strong style="color:#3594f7"><span>「</span>Vue 3<span>」</span></strong>. 迁移到了最新的前端框架 Vue 3，以支持更高级的功能，例如组合式 API 和 TypeScript。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>UI 框架<span>」</span></strong>. 从之前的 Vue-Element-Admin 迁移到了基于 Vue 3 的 UI 框架 Element-Plus，更多灵活性和功能性。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>高级文件编辑器<span>」</span></strong>. 支持更高级的文件编辑器功能，包括拖砖操作、复制、移动、重命名、删除、文件编辑、代码高亮、导航标签等。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>可自定义表格<span>」</span></strong>. 内置更多高级功能，包括自定义列、批量操作、搜索、过滤、排序等。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>导航标签<span>」</span></strong>. 支持多导航标签查看不同的页面。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>批量创建<span>」</span></strong>. 支持批量创建对象，包括爬虫、项目、定时任务等。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>详情导航<span>」</span></strong>. 详情页里的侧边栏导航。</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>更优化的仪表盘<span>」</span></strong>. 主页仪表盘中更多的数据图表。</p> </li> 
</ul> 
<h4><span>其他</span></h4> 
<ul style="list-style-type:circle"> 
 <li> <p><strong style="color:#3594f7"><span>「</span>文档网站<span>」</span></strong>. 升级 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs-next.crawlab.cn" target="_blank">文档网站</a>.</p> </li> 
 <li> <p><strong style="color:#3594f7"><span>「</span>官方插件<span>」</span></strong>. 允许用户在 Crawlab 用户界面上安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.crawlab.cn%2Fzh%2Fguide%2Fplugin%2F" target="_blank">官方插件</a>.</p> </li> 
</ul> 
<h2><span style="color:#40b8fa">未来计划</span></h2> 
<p style="color:#2b2b2b; margin-left:0; margin-right:0">作为 Crawlab v0.6.x 新版本系列的首发版本，后续将收集新版本的用户反馈，并且进一步优化既有功能以及开发新功能。欢迎大家来试用 Crawlab v0.6.0 社区版，提出您的宝贵意见。</p> 
<h2><span style="color:#40b8fa">关于旧版本</span></h2> 
<p style="color:#2b2b2b; margin-left:0; margin-right:0">新版本 Crawlab v0.6.x 从底层架构方面做的根本性的更新，因此将不会兼容旧版本 Crawlab v0.5.x 及以下。如果您已经在使用旧版本，建议迁移少部分爬虫到新版本，做过充分测试之后再做全量迁移。</p> 
<p style="color:#2b2b2b; margin-left:0; margin-right:0">新版本发布并不意味着开发组将停止更新旧版本 Crawlab v0.5.x，我们将长期维护既有版本 Crawlab v0.5.x 版本系列直到新版本完全稳定以及旧版本用户已大部分迁移到新版本。</p> 
<p style="color:#2b2b2b; margin-left:0; margin-right:0">后续会提供迁移至新版本的相关文档，请随时关注微信交流社群、官方网站以及官方文档。</p> 
<h2><span style="color:#40b8fa">社区</span></h2> 
<p style="color:#2b2b2b; margin-left:0; margin-right:0">如果您觉得 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrawlab-team%2Fcrawlab" target="_blank">Crawlab</a> 对您的日常开发或公司有帮助，欢迎在 Github 上进行 star，以及，如果遇到任何问题，请随时在 Github 上提 issue。另外，欢迎您对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrawlab-team%2Fcrawlab" target="_blank">Crawlab</a> 做开发贡献。同时，您也可以加微信 tikazyq1 加入 Crawlab 技术交流群，在技术开发和部署使用上与其他开发者进行交流讨论。</p> 
<h2><span style="color:#40b8fa">参考</span></h2> 
<ul style="list-style-type:circle"> 
 <li> <p>官网: https://www.crawlab.cn</p> </li> 
 <li> <p>文档: https://docs.crawlab.cn</p> </li> 
 <li> <p>GitHub: https://github.com/crawlab-team/crawlab</p> </li> 
 <li> <p>Demo: https://demo-pro.crawlab.cn/</p> </li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            