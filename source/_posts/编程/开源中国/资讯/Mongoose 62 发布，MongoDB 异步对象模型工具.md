
---
title: 'Mongoose 6.2 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9973'
author: 开源中国
comments: false
date: Fri, 04 Feb 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9973'
---

<div>   
<div class="content">
                                                                                            <p>Mongoose 是设计用于异步环境的 MongoDB 对象模型工具。Mongoose 支持 promises 和 callbacks。Mongoose 6.2 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>feat(connection+mongoose): 增加对 continueOnError 的支持</li> 
 <li>feat(schema+mongoose): 增加 pluginTags，允许将全局插件只应用于具有匹配标签的模式</li> 
 <li>feat(discriminator): 支持 overwriteModels:true 以重复使用 discriminator</li> 
 <li>feat(index.d.ts): 为返回查询的 Model 函数添加 DocType 通用参数，以更好地支持映射（projections）</li> 
 <li>feat(error): 输出 MongooseServerSelectionError</li> 
 <li>feat(schematype): 添加验证器、path、isRequired 到公共 API 和 TypeScript 类型</li> 
 <li>fix(model): 使 exists(...) 返回带有 _id 或 null 的 Lean 文档，而不是布尔值</li> 
 <li>fix(model): 支持在嵌套路径中存储 versionKey</li> 
 <li>fix(index.d.ts): 给 <code>bulkSave()</code> 类型的定义添加选项</li> 
 <li>fix(index.d.ts): 更好地支持查询映射</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.2.0" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.2.0</a></p>
                                        </div>
                                      
</div>
            