
---
title: 'Mongoose 5.12.10 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6811'
author: 开源中国
comments: false
date: Thu, 20 May 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6811'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Mongoose 是设计用于异步环境的 MongoDB 对象模型工具。Mongoose 支持 promises 和 callbacks。Mongoose 5.12.10 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>修复（查询）：允许在查询选项的结果文档中设置 <code>defaults</code> 选项；</li> 
 <li>修复（populate）：处理用自定义 tiedValue 来填充嵌入式判别器；</li> 
 <li>修复（文档）：允许向 validate() 和 validateSync() 传递以空格分隔的 pathsToValidate 字符串；</li> 
 <li>修复（模型+模式）：支持在将 collection 作为静态属性的类上使用 loadClass()；</li> 
 <li>修复（SchemaArrayOptions）：更正属性名称；</li> 
 <li>修复（index.d.ts）：在所有的查询操作中添加 any，以减少在查询有 4 级深度子文档的文档时出现 "类型实例化过深" 的可能性；</li> 
 <li>修复（index.d.ts）：在 TS 定义中除了 parent() 之外，还增加了 $parent()；</li> 
 <li>修复（index.d.ts）：更正 QueryCursor 的异步迭代器返回类型；</li> 
 <li>修复（index.d.ts）：在 loadClass() 函数签名中增加 virtualsOnly 参数；</li> 
 <li>文档（typescript）：添加 typescript 填充文档</li> 
 <li>文档：从 AWS 切换到 Azure Functions 进行搜索；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F5.12.10" target="_blank">https://github.com/Automattic/mongoose/releases/tag/5.12.10</a></p>
                                        </div>
                                      
</div>
            