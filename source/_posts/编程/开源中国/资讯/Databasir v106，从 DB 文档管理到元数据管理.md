
---
title: 'Databasir v1.0.6，从 DB 文档管理到元数据管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-52767b9487cc3422610f0491cf8d52fbb0c.png'
author: 开源中国
comments: false
date: Thu, 02 Jun 2022 09:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-52767b9487cc3422610f0491cf8d52fbb0c.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">Databasir 最初是为了解决数据库文档维护的问题，随着最近几个版本的迭代，项目不知不觉已经逐渐朝着元数据管理的方向在演进了，那索性就朝这个方向去努力吧。</p> 
<h2 style="text-align:start">多图展示</h2> 
<p>1. 版本历史差异对比</p> 
<p><img height="1146" src="https://oscimg.oschina.net/oscnet/up-52767b9487cc3422610f0491cf8d52fbb0c.png" width="2034" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start">2. 在线 UML</p> 
<p><img height="1158" src="https://oscimg.oschina.net/oscnet/up-c2da35a8631529aed5b9f6b4fef74f1e896.png" width="2048" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start">3. 元数据搜索</p> 
<p><img height="1145" src="https://oscimg.oschina.net/oscnet/up-bb709a6e3f54be27d4723f1f55c29e1cef8.png" width="2033" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">变更记录</h2> 
<p style="color:#24292f; text-align:start">⚔️<span> </span><strong>feature</strong></p> 
<ol> 
 <li>全新的元数据搜索功能，支持分组、项目、表、列等信息搜索</li> 
 <li>文档导出联动多选模式，支持部分导出</li> 
 <li>使用 Plantuml 导出 ER 图（SVG、PNG），支持外键血缘关系</li> 
 <li>优化文档页渲染性能，单选模式下轻松渲染 1000+ 表数据量</li> 
 <li>版本对比支持快速筛选差异项</li> 
 <li>版本对比支持显示上个版本被删除的表</li> 
 <li>新项目列表页 UI 设计</li> 
 <li>docker file 新增启动参数 PARAMS</li> 
</ol> 
<p style="color:#24292f; text-align:start">🪲<span> </span><strong>bug-fix</strong></p> 
<ol> 
 <li>fix：差异对比时概览显示 NONE，但实际表为 ADDED</li> 
</ol> 
<p style="color:#24292f; text-align:start">⚙️<span> </span><strong>others</strong></p> 
<ol> 
 <li>文档从 docsify 迁移到 vuepress，更快的访问速度</li> 
 <li>文档新增开发指南内容，包括技术栈列表、项目构建、模块介绍等</li> 
 <li>更新 Docker 部署文档</li> 
 <li>重构 trigger provider 设计</li> 
</ol> 
<p style="color:#24292f; text-align:start"><strong>Full Changelog</strong>:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir%2Fcompare%2Fv1.0.5...v1.0.6" target="_blank">v1.0.5...v1.0.6</a></p> 
<h2>项目信息</h2> 
<ol style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>项目地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir" target="_blank"><span>https://github.com/vran-dev/databasir</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>文档地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.databasir.com%2F" target="_blank"><span>https://doc.databasir.com/</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.databasir.com%2F" target="_blank"><span>http://demo.databasir.com/</span></a>  </span><span style="background-color:#ffffff; color:#333333">// 请查看文档获取登录账号密</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span style="background-color:#ffffff; color:#333333">Release Tag：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvran-dev%2Fdatabasir%2Freleases" target="_blank">https://github.com/vran-dev/databasir/releases</a></p> </li> 
</ol>
                                        </div>
                                      
</div>
            