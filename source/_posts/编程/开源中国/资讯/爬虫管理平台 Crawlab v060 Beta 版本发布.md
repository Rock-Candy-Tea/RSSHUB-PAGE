
---
title: '爬虫管理平台 Crawlab v0.6.0 Beta 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6377'
author: 开源中国
comments: false
date: Wed, 04 Aug 2021 16:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6377'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:start">概览</h1> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrawlab-team%2Fcrawlab" target="_blank">Crawlab</a> <span style="background-color:#ffffff; color:#333333">基于 Golang 的分布式爬虫管理平台，支持多种编程语言以及多种爬虫框架。</span>此次发布的是下一个正式版本 v0.6.0 的 beta 版本。<strong>不推荐将此 beta 版本用作生产环境中</strong>，因为它还没有被全面测试，也不足够稳定。另外，一些实用功能（例如 Git、Scrapy、消息通知）不计划在此 beta 版本发布，它们将以插件形式被整合进正式版本。</p> 
<h2 style="text-align:start">升级优化</h2> 
<p style="text-align:start">作为一个重要版本发布，Crawlab v0.6（包括 beta 版本）由一些重大的功能升级组成，包括性能、稳定性、健壮性、易用性方面的大量优化。本次 beta 版本理论上会比老版本更加健壮，特别是任务执行、文件同步、节点通信上面。但是，我们还是推荐用户在 Crawlab 信版本上更全面的测试不同的爬虫任务。</p> 
<h4 style="text-align:start">后端</h4> 
<ul> 
 <li> <p><strong>文件同步</strong>. 将文件同步从原先的 MongoDB GridFS 迁移到分布式文件系统 SeaweedFS，以提升文件同步和爬虫部署的稳定性和健壮性。</p> </li> 
 <li> <p><strong>节点通信</strong>. 将节点通信从原先基于 Redis 套壳的 RPC 迁移到 gRPC。工作节点通过向主节点发起 gRPC 请求来与 MongoDB 数据库间接交互。</p> </li> 
 <li> <p><strong>任务队列</strong>. 将任务队列从 Redis 列表迁移到 MongoDB 集合，以提高灵活性，例如优先级队列。</p> </li> 
 <li> <p><strong>日志</strong>. 将日志储存迁移到 SeaweedFS，以解决 MongoDB 数据库中的性能问题。</p> </li> 
 <li> <p><strong>SDK 集成</strong>. 将结果数据储存从原生 SDK 迁移到了任务处理器集中导入到数据库。</p> </li> 
 <li> <p><strong>任务相关</strong>. 将任务相关逻辑抽象为了任务调度器、任务处理器以及任务执行器，以减少系统耦合度，提升可扩展性和可维护性。</p> </li> 
 <li> <p><strong>组件化</strong>. 引入依赖注入框架，将模块、服务以及子系统进行模块化。</p> </li> 
</ul> 
<h4 style="text-align:start">前端</h4> 
<ul> 
 <li> <p><strong>Vue 3</strong>. 迁移到了最新的前端框架 Vue 3，以支持更高级的功能，例如组合式 API 和 TypeScript。</p> </li> 
 <li> <p><strong>UI 框架</strong>. 从之前的 Vue-Element-Admin 迁移到了基于 Vue 3 的 UI 框架 Element-Plus，更多灵活性和功能性。</p> </li> 
 <li> <p><strong>高级文件编辑器</strong>. 支持更高级的文件编辑器功能，包括拖砖操作、复制、移动、重命名、删除、文件编辑、代码高亮、导航标签等。</p> </li> 
 <li> <p><strong>可自定义表格</strong>. 内置更多高级功能，包括自定义列、批量操作、搜索、过滤、排序等。</p> </li> 
 <li> <p><strong>导航标签</strong>. 支持多导航标签查看不同的页面。</p> </li> 
 <li> <p><strong>批量创建</strong>. 支持批量创建对象，包括爬虫、项目、定时任务等。</p> </li> 
 <li> <p><strong>详情导航</strong>. 详情页里的侧边栏导航。</p> </li> 
 <li> <p><strong>更优化的仪表盘</strong>. 主页仪表盘中更多的数据图表。</p> </li> 
</ul> 
<h2 style="text-align:start">待完成</h2> 
<p style="text-align:start">您可能已经知晓，这是一个 beta 版本，因此一些既有的实用功能（例如 Git 和 Scrapy 集成）还不支持。不过，由于代码中已经有一些基础功能，我们正努力将它们涵盖在 v0.6.0 的正式版本中。我们只会在它们被全面测试之后再加入到稳定版本中。</p> 
<ul> 
 <li><strong>插件框架</strong>. 高级功能会以插件的形式集成到 Crawlab 中。</li> 
 <li><strong>Git 集成</strong>. 将作为插件存在。</li> 
 <li><strong>Scrapy 集成</strong>. 将作为插件存在。</li> 
 <li><strong>消息通知</strong>. 将作为插件存在。</li> 
 <li><strong>关联人物</strong>. 如果任务执行模式为 “所有节点” 或 “指定节点”，那么将会有主任务和子任务之分。</li> 
 <li><strong>Crontab 编辑器</strong>. 可视化 Crontab 编辑的前端组件。</li> 
 <li><strong>结果去重</strong>.</li> 
 <li><strong>环境变量</strong>.</li> 
 <li><strong>国际化</strong>. 支持中文.</li> 
 <li><strong>前端易用性优化</strong>. 更多高级功能，例如表格形式保存。</li> 
 <li><strong>日志自动清理</strong>.</li> 
 <li><strong>文档</strong>.</li> 
</ul> 
<h2 style="text-align:start">未来计划</h2> 
<p style="text-align:start">此次 beta 版本发布只是作为 Crawlab v0.6 核心功能测试的预览版本。我们诚信希望各位用户能下载安装并运行更多测试爬虫任务。在 beta 版中发现的主要问题解决后，以及插件框架和其他重要功能完成并通过测试之后，我们将发布正式版本。因此，在此之前，还可能会存在第二个更完善的 beta 版本。</p> 
<h2 style="text-align:start">参考</h2> 
<ul> 
 <li> <p>官网: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.crawlab.cn" target="_blank">https://www.crawlab.cn</a></p> </li> 
 <li> <p>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrawlab-team%2Fcrawlab" target="_blank">https://github.com/crawlab-team/crawlab</a></p> </li> 
 <li> <p>Demo: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrawlab.cn%2Fdemo" target="_blank">https://crawlab.cn/demo</a></p> </li> 
</ul> 
<h2 style="text-align:start">社区</h2> 
<p style="text-align:start">如果您觉得 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrawlab-team%2Fcrawlab">Crawlab</a> 对您的日常开发或公司有帮助，欢迎在 Github 上进行 star，以及，如果遇到任何问题，请随时在 Github 上提 issue。另外，欢迎您对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcrawlab-team%2Fcrawlab">Crawlab</a> 做开发贡献。</p>
                                        </div>
                                      
</div>
            