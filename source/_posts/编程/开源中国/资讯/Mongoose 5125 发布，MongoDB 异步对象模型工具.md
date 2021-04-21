
---
title: 'Mongoose 5.12.5 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9661'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9661'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Mongoose 是设计用于异步环境的 MongoDB 对象模型工具。Mongoose 支持 promises 和 callbacks。Mongoose 5.12.5 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>fix(populate): 当数据库中文档数组属性不存在时，处理文档数组下方的填充；</li> 
 <li>fix(populate): 清除指向已填充文档的悬空指针，这样用 populate() 查询光标就可以垃圾回收已填充的子文档；</li> 
 <li>fix(connection): 在调用 <code>connect()</code> 之前创建新模型时，从 Mongoose 全局中正确拉取 <code>autoCreate</code> 的值；</li> 
 <li>fix(populate): 处理在文档上填充路径的问题，这些文档的鉴别器键指向不存在的鉴别器；</li> 
 <li>fix(index.d.ts): 允许用数字作为鉴别器名称；</li> 
 <li>fix(index.d.ts): 在 Schema 定义中允许 <code>type: Boolean</code> ；</li> 
 <li>fix(index.d.ts): 允许向 <code>updateOne()</code> 和 <code>updateMany()</code> 传递聚合 pipeline stages 数组；</li> 
 <li>fix(index.d.ts): 为 <code>deleteOne()</code> 和 <code>deleteMany()</code> 加入传统的的第二个参数回调语法的支持；</li> 
 <li>docs(mongoose): 在文档中让 <code>useCreateIndex</code> 始终为 <code>false</code>；</li> 
 <li>docs(schema): 修正 schema API 文档中的错误链接；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases" target="_blank">https://github.com/Automattic/mongoose/releases</a></p>
                                        </div>
                                      
</div>
            