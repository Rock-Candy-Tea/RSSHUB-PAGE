
---
title: 'Node.js 17.1.0 发布，支持 JSON 导入断言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3717'
author: 开源中国
comments: false
date: Thu, 11 Nov 2021 06:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3717'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Node.js 17.1.0 版本正式发布了，此版本包含支持 JSON 导入断言、新的 promise hook api 等内容，值得注意的更新项如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>添加 VoltrexMaster 为 Node.js 项目合作者</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FVoltrexMaster" target="_blank">VoltrexMaster<span> </span></a>为 Node.js 项目做了许多帮助，包括贡献代码、问题分类和帮助用户解答问题，此版本将他列入合作者之一。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>支持 JSON 导入断言（import assertion）</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">这个 PR 在 9月底被提出，经过大量测试和调试，最终在 Node.js 17.1.0 版本支持 JSON 的导入断言 。随着对 JSON 类型的支持，Node.js 维护者之一  GeoffreyBooth 提出了支持更多引入断言类型的提案<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fissues%2F40766" target="_blank">#40766</a>。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>对非活跃的诊断通道（</strong><code><strong>non-active diagnostics_channel</strong></code><strong>）添加取消订阅 （</strong><code><strong>unsubscribe</strong></code><strong>）方法</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前，如果用户试图在非活跃诊断通道（non-active channel）上使用<span> </span><code>unsubscribe</code><span> </span>方法，将抛出“<code>channel.unsubscribe is not a function</code>”异常。但如果通道是活跃通道（<code>ActiveChannel</code><span> </span>）的一个实例，则不会抛出异常。<br> 用户没必要知道非活跃频道和活跃频道之间的区别，所以两种频道中都应该存在取消订阅的<span> </span><code>unsubscribe</code><span> </span>方法。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>对诊断通道的<span> </span></strong><code><strong>unsubscribe</strong></code><strong><span> </span>方法添加返回值</strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">对<span> </span><code>unsubscribe</code> 方法添加一个布尔类型的返回值，如果订阅者（<code>subscriber</code>）已经被删除，则返回 true，如果未找到，则返回 false 。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>新增 multi-tenant promise hook api </strong></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">引入了这个新的<span> </span><code>Promise Hook</code><span> </span>模块，可以更直接地向用户展示 V8 中的 PromiseHook API。此 PR  出自 N</span>ode.js 核心贡献者 Qard，他的计划是<span style="color:#2e3033">把<span> </span><code>async_hooks</code><span> </span>分解成针对特定目的的组件，以后就可以直接使用这些组件而不是<span> </span><code>async_hooks</code><span> </span>本身，因为<span> </span><code>async_hooks</code><span> </span>合并了很多不同的数据源，有时使用起来很别扭。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">除了以上重点更新，Node.js 还包含了多个提交的处理结果，包含 bug 修复、文档变更等内容，详情请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnodejs.org%2Fen%2Fblog%2Frelease%2Fv17.1.0%2F" target="_blank">查看更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            