
---
title: 'Mongoose 6.1.5 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=950'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=950'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Mongoose 是设计用于异步环境的 MongoDB 对象模型工具。Mongoose 支持 promises 和 callbacks。Mongoose 6.1.5 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>perf(index.d.ts)：简化查询助手和方法的 Schema 类型定义，以大大减少 TS 编译器的开销 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10349" target="_blank">#10349</a></li> 
 <li>fix(document)：允许将深度嵌套的模型填充为字符串 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11168" target="_blank">#11168</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11160" target="_blank">#11160</a></li> 
 <li>fix(query): 允许用字符串调用 limit() 和 skip() <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11017" target="_blank">#11017</a></li> 
 <li>fix(cursor): 在加载带有查询光标的判别器文档时，正确应用选定字段 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11130" target="_blank">#11130</a></li> 
 <li>fix(mongoose+connection): 当向 Connection.prototype.model() 传递另一个 Mongoose 实例的 Schema 时，正确克隆 Schema <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11047" target="_blank">#11047</a></li> 
 <li>fix(index.d.ts): 用 FlattenMaps 处理基元 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11117" target="_blank">#11117</a></li> 
 <li>fix(index.d.ts): 在精益查询结果类型上强制执行 id <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11118" target="_blank">#11118</a></li> 
 <li>fix(index.d.ts): 导出 facet 阶段类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11150" target="_blank">#11150</a></li> 
 <li>fix(index.d.ts): 更正 projection 方法的返回类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11176" target="_blank">#11176</a></li> 
 <li>fix(index.d.ts): 额外修复 <code>$group</code> pipeline 阶段 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11140" target="_blank">#11140</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11067" target="_blank">#11067</a></li> 
 <li>文档：为 TS 测试更新 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FCONTRIBUTING.md" target="_blank">CONTRIBUTING.md</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11164" target="_blank">#11164</a></li> 
 <li>文档：使用 es6 对象解构而不是普通的点运算符来访问对象中的值 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11147" target="_blank">#11147</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.1.5" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.1.5</a></p>
                                        </div>
                                      
</div>
            