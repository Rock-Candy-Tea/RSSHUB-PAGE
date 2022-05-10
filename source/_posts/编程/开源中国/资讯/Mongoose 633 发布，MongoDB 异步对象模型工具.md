
---
title: 'Mongoose 6.3.3 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8851'
author: 开源中国
comments: false
date: Tue, 10 May 2022 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8851'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px"><span style="color:#333333">Mongoose 是设计用于异步环境的 MongoDB 对象模型工具，支持 promises 和 callbacks。</span></p> 
<p style="margin-left:0px"><span style="color:#333333">Mongoose 6.3.3 已正式发布，带来如下改动：</span></p> 
<ul> 
 <li>perf：<span style="color:#2e3033">在使用QueryCursor时避免内存泄漏，因为使用_docs时重用了填充选项</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11641" target="_blank">#11641</a></li> 
 <li>fix(types)：<span style="color:#2e3033">为LeanDocument添加_id</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11769" target="_blank">#11769</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11761" target="_blank">#11761</a></li> 
 <li>fix(model)：<span style="color:#2e3033">为bulkWrite()添加skipValidation选项，以允许跳过insertOne和replaceOne的验证</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11663" target="_blank">#11663</a></li> 
 <li>fix(document)：修正 <span style="color:#24292f">$__reset() 嵌套路径下的子文档</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11672" target="_blank">#11672</a></li> 
 <li>fix(query)<span style="color:#24292f">：在查询中处理将 BSONRegExp 实例转换为 RegExps</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11597" target="_blank">#11597</a></li> 
 <li>fix：<span style="color:#2e3033">正确转换 $not in $expr</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11689" target="_blank">#11689</a></li> 
 <li>perf：<span style="color:#24292f">优化浏览器包的大小，使用 buffer v.5.7.1 包来匹配浏览器包中 mongodb 的缓冲包</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11765" target="_blank">#11765</a> </li> 
 <li>docs:：<span style="color:#24292f">Query.populate 文档不使用字符串数组作为路径参数</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11768" target="_blank">#11768</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F11641" target="_blank">#11641</a> </li> 
 <li>chore：<span style="color:#24292f">删除 Makefile 对编译文档的依赖</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F11751" target="_blank">#11751</a> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.3.3" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.3.3</a></p>
                                        </div>
                                      
</div>
            