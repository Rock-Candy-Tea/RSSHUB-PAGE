
---
title: 'Mongoose 6.1.6 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6631'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6631'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Mongoose 是设计用于异步环境的 MongoDB 对象模型工具，支持 promises 和 callbacks。Mongoose 6.1.6 正式发布，本次更新内容如下：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>perf(document):<span> </span><span style="color:#24292f">延迟创建文档事件发射器（document event emitter），用于提高内存使用率。通过一些小的优化，来改进大型数组的初始化文档<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10400" target="_blank">#10400</a></li> 
 <li>fix(model): 避免<span> </span><code>versionKey: false</code><span> </span>时的<span> </span><code>bulkSave()</code>错误<span style="color:#24292f"> </span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11186" target="_blank">#11186</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11071" target="_blank">#11071</a> </li> 
 <li>fix(model): 还原<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11079" target="_blank">#11079</a>：<code>findByIdAndUpdate(undefined)</code><span> </span>的重大更改<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11149" target="_blank">#11149</a></li> 
 <li>fix(index.d.ts): 在 deep populate 中支持字符串<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11181" target="_blank">#11181</a></li> 
 <li>fix(index.d.ts): 重命名 map() -> transform() ，以符合 v6.0 中的更改<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11161" target="_blank">#11161</a></li> 
 <li>fix(index.d.ts): 允许 new Model(obj) 进行更严格的类型检查<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11148" target="_blank">#11148</a></li> 
 <li>fix(index.d.ts):<span> </span><span style="color:#2e3033">将 Schema.prototype.pre() 和 post() 两个泛型默认为 HydratedDocument</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11180" target="_blank"><span> </span>#11180</a></li> 
 <li>docs: 改进 autoCreate 文档  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11116" target="_blank">#11116</a></li> 
 <li>docs(schematype):<span style="color:#24292f">将缺少的参数添加到示例</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11185" target="_blank">#11185</a> </li> 
 <li>docs(connections):<span> </span><span style="color:#2e3033">使用更新过的链接列表 MongoDB 节点驱动程序的<span> </span></span><span style="color:#24292f"><code>connect()<span> </span></code></span><span style="color:#2e3033">选项</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11184" target="_blank">#11184</a> </li> 
 <li>docs(aggregate):<span> </span><span style="color:#24292f">修复格式<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11191" target="_blank">#11191</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fenieber" target="_blank">enieber</a></li> 
 <li>docs: 修复损坏的文档链接  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11179" target="_blank">#11179</a> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.1.6" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.1.6</a></p>
                                        </div>
                                      
</div>
            