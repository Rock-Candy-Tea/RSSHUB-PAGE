
---
title: 'Elide 5.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6304'
author: 开源中国
comments: false
date: Sun, 23 May 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6304'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Elide 是一个 Java 库，可以让你以最小的努力建立模型驱动的 GraphQL 或 JSON API 网络服务。Elide 支持两种变体的 API。</p> 
<ul> 
 <li>用于读取和操作模型的 CRUD（创建，读取，更新，删除）API；</li> 
 <li>用于汇总零个或多个模型属性的度量分析 API；</li> 
</ul> 
<p>Elide 5.0.0 正式发布，该版本的主要变化包括：</p> 
<ul> 
 <li>为 Aggregation Store 模型参数化表格、指标和尺寸。</li> 
 <li>一个新的安全模型（权限执行器）用于 Aggregation Store 模型。</li> 
 <li>包级别的 @Include 引入了 "命名空间" 的概念；</li> 
 <li>@Include 包括元数据（很快将被添加到 Swagger 和 Graphiql 文档中）；</li> 
 <li>为 Aggregation Store 添加了一个查询优化器；</li> 
 <li>为 Aggregation Store 改变元数据，以支持更丰富的搜索建议；</li> 
 <li>在 security.RequestScope 上公开查询参数；</li> 
 <li>允许自定义 serdes 覆盖默认 serdes；</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>表命名空间模型配置</li> 
 <li>更新 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freadme.md%2F" target="_blank">README.md</a></li> 
 <li>将 version.jackson 从 2.12.2 升级至 2.12.3；</li> 
 <li>将 groovy.version 从 3.0.7 升级至 3.0.8；</li> 
 <li>重构 column 和 argument 的 tableSource；</li> 
 <li>重构 AnyFieldExpression 逻辑；</li> 
 <li>对 elide-model-config 进行代码清理；</li> 
 <li>为 HJSON ID 列添加列元数据；</li> 
 <li>移除 SQLReferenceTable 的用法；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyahoo%2Felide%2Freleases%2Ftag%2F5.0.0" target="_blank">https://github.com/yahoo/elide/releases/tag/5.0.0</a></p>
                                        </div>
                                      
</div>
            