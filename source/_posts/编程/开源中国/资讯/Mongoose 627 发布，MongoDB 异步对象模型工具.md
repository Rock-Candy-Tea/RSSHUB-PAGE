
---
title: 'Mongoose 6.2.7 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9172'
author: 开源中国
comments: false
date: Fri, 18 Mar 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9172'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Mongoose 是设计用于异步环境的 MongoDB 对象模型工具，支持 promises 和 callbacks。</span></p> 
<p><span style="color:#333333">Mongoose 6.2.7 正式发布，本次更新内容如下：</span></p> 
<ul> 
 <li>perf(document): 如果没有要运行的验证器，则避免对每个数组元素运行验证 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11380" target="_blank">#11380</a></li> 
 <li>fix(cursor): 设置 batchSize 时正确地分批填充 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11509" target="_blank">#11509</a></li> 
 <li>fix(connection):避免在 useDb() 连接上设置 MongoClient，直到在基础连接上设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11445" target="_blank">#11445</a></li> 
 <li>fix(schema):使用来自不同版本的 Mongoose 模块模式时抛出更多有用的错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10453" target="_blank">#10453</a></li> 
 <li>fix: 添加缺少的时间序列过期处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11489" target="_blank">#11489 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11229" target="_blank">#11229</a></li> 
 <li>docs: <span style="color:#24292f">正确的 Model.findOneAndReplace 文档参数命名</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11524" target="_blank">#11524</a> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.2.7" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.2.7</a></p>
                                        </div>
                                      
</div>
            