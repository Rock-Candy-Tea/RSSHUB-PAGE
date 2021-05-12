
---
title: 'Mongoose 5.12.8 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4681'
author: 开源中国
comments: false
date: Wed, 12 May 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4681'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Mongoose 是设计用于异步环境的 MongoDB 对象模型工具。Mongoose 支持 promises 和 callbacks。Mongoose 5.12.8 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>fix(populate): 处理填充不可变数组的路径；</li> 
 <li>fix(CastError): 添加 toJSON() 函数以确保 name 属性始终最终出现在 JSON.stringify() 输出中；</li> 
 <li>fix(query): 增加 allowDiskUse() 方法，改进 MongoDB 4.4 新的 allowDiskUse 选项的设置；</li> 
 <li>fix(populate): 允许在一些文档具有非对象属性的混合模式下填充路径；</li> 
 <li>chore: 删除不必要的驱动动态导入，以便 Mongoose 能与 Parcel 一起工作；</li> 
 <li>fix(index.d.ts): 允许任何对象作为 create() 和 insertMany() 的参数；</li> 
 <li>fix(index.d.ts): 允许用原始接口创建 Model 类，没有 <code>extends Document</code></li> 
 <li>fix(index.d.ts): 当 UpdateQuery 作为函数参数的情况时，将 UpdateQuery 与 UpdateWithAggregationPipeline 分开；</li> 
 <li>fix(index.d.ts): 在 hooks 前/后中不需要错误值；</li> 
 <li>docs(typescript): 增加 typescript 入门教程和静态教程；</li> 
 <li>docs(typescript): 增加查询助手教程；</li> 
 <li>docs(deprecations): 增加可以安全忽略 useFindAndModify 和 useCreateIndex 的废弃警告的说明</li> 
 <li>chore(workflows): 添加 node 16 到 github actions；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fblob%2Fmaster%2FHistory.md" target="_blank">https://github.com/Automattic/mongoose/blob/master/History.md</a></p>
                                        </div>
                                      
</div>
            