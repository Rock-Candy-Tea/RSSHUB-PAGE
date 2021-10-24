
---
title: 'Mongoose 6.0.12 发布，MongoDB 异步对象模型工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7435'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 07:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7435'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Mongoose<span> </span></span>6.0.12<span style="color:#333333"><span> </span>正式发布，Mongoose 是设计用于异步环境的 MongoDB 对象模型工具，支持 promises 和 callbacks。</span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#333333">主要更新内容</span></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#000000"><strong>fix (cursor)：</strong>删除触发<span> </span><code>closed</code><span> </span>的逻辑，可以用<span> </span><code>autoDestroy</code><span> </span>功能来修复。（此功能仅支持 Node 12 及以上版本）。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F10906" target="_blank">#10906</a></li> 
 <li><span style="color:#24292f"><strong>fix(map)：</strong>支持将<span> </span><code>flattenMaps: false</code><span> </span>传递给<span> </span><code>Map toJSON()<span> </span></code>，</span><code>toJSON()<span> </span></code>在 TypeScript 中默认是<span> </span><span style="color:#24292f"><code>flatten</code><span> </span>地图类型。 </span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10872" target="_blank"><u>#10872</u></a></li> 
 <li><span style="color:#24292f"><strong>fix：</strong>升级 mongodb 驱动到 4.1.3 版本。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F10911" target="_blank">#10911 </a></li> 
 <li><span style="color:#24292f"><strong>fix (index.d.ts)：</strong>修正</span><span> </span><code>SchemaType.prototype.set()</code><span style="color:#24292f"><span> </span> 的 TS 函数签名。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10799" target="_blank">#10799</a></li> 
 <li><span style="color:#24292f"><strong>fix (index.d.ts)：</strong></span>更精确的<span> </span><code>Schema.clone()</code><span> </span>类型（<code>Schema</code><span style="color:#24292f"><span> </span>→<span> </span><code>schema</code></span>）。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F10899" target="_blank">#10899</a></li> 
 <li><span style="color:#24292f"><strong>fix (index.d.ts)：</strong></span>在 FilterQuery 中支持隐式 $in  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10826" target="_blank">#10826</a></li> 
 <li><span style="color:#24292f"><strong>fix (index.d.ts)：</strong></span><span style="color:#2e3033">向模式数组和文档数组添加<span> </span><code>cast</code><span> </span>属性<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F10865" target="_blank"><u>#10865</u></a></li> 
 <li><span style="color:#24292f"><strong>docs：</strong></span>更新<code>updateMany()</code><span> </span>和<span> </span><code>deleteMany()</code><span> </span>文档，用来映射新的<code>matchedCount</code><span> </span>、<code>modifiedCount</code><span> </span>、<span> </span><code>deletedCount</code><span> </span>属性。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F10908" target="_blank">#10908</a></li> 
 <li><span style="color:#24292f"><strong>docs：</strong></span>修复<span> </span><code>populate virtual</code><span> </span>文档的无效链接。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fissues%2F10870" target="_blank"><u>#10870</u></a></li> 
 <li><span style="color:#24292f"><strong>docs：</strong></span>更新了<span> </span><code>returnOriginal</code><span> </span>的文档，删除<span> </span><code>new</code><span> </span>和<span> </span><code>returnDocument</code><span> </span>文档。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Fpull%2F10887" target="_blank"><u>#10887</u></a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAutomattic%2Fmongoose%2Freleases%2Ftag%2F6.0.12" target="_blank">https://github.com/Automattic/mongoose/releases/tag/6.0.12</a></p>
                                        </div>
                                      
</div>
            