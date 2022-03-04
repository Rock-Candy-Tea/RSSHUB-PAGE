
---
title: 'Nest.js 8.4 发布，渐进式 Node.js 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8915'
author: 开源中国
comments: false
date: Fri, 04 Mar 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8915'
---

<div>   
<div class="content">
                                                                                            <p>Nest.js 是一个用于构建高效、可扩展的 Node.js 服务器端应用程序的框架。它使用 TypeScript 和 JavaScript 构建，并结合了 OOP（面向对象编程）、FP（功能编程）和 FRP（功能反应式编程）等元素。</p> 
<p>Nest.js 8.4 正式发布，该版本更新内容如下：</p> 
<h3>特性</h3> 
<ul> 
 <li><code>common</code>, <code>core</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9227" target="_blank">#9227</a> feat(core): 支持 factory providers 中的可选依赖关系</li> 
  </ul> </li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li><code>microservices</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9277" target="_blank">#9277</a> fix(microservices): 从数据包（rmq 和 mqtt）中移除选项对象</li> 
  </ul> </li> 
 <li><code>core</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9271" target="_blank">#9271</a> fix(core): 使用类引用作为键（容器）</li> 
  </ul> </li> 
</ul> 
<h3><strong>增强功能</strong></h3> 
<ul> 
 <li><code>microservices</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9059" target="_blank">#9059</a> feat(microservices): 添加 tcp 原始数据处理能力</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9270" target="_blank">#9270</a> feat(microservices): 向 clientkafka 添加 commit-offsets 功能</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9200" target="_blank">#9200</a> feat(microservices): 将选项参数添加到序列化程序</li> 
  </ul> </li> 
 <li><code>common</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9209" target="_blank">#9209</a> feat(common): 添加抽象类型以捕获装饰器</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9247" target="_blank">#9247</a> fix(common): 为中间件中的可选错误处理提供类型</li> 
  </ul> </li> 
 <li><code>common</code>, <code>platform-express</code>, <code>platform-fastify</code> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9240" target="_blank">#9240</a> feat(common): 扩展 streamable-file header 支持</li> 
  </ul> </li> 
</ul> 
<h3>依赖项</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9274" target="_blank">#9274</a> chore(deps-dev): 将 mongoose 从 6.2.3 升级到 6.2.4</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9275" target="_blank">#9275</a> chore(deps-dev): 将 @types/cache-manager 从 3.4.2 升级到 3.4.3</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9250" target="_blank">#9250</a> chore(deps-dev): 将 @nestjs/apollo 从 10.0.4 升级到 10.0.5</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9251" target="_blank">#9251</a> chore(deps-dev): 将 @types/node 从 17.0.18 升级到 17.0.21</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Fpull%2F9253" target="_blank">#9253</a> chore(deps-dev): 将 @nestjs/graphql 从 10.0.4 升级到 10.0.5</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Freleases%2Ftag%2Fv8.4.0" target="_blank">https://github.com/nestjs/nest/releases/tag/v8.4.0</a></p>
                                        </div>
                                      
</div>
            