
---
title: 'Apache Maven 3.8.6 发布，项目管理和构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7273'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7273'
---

<div>   
<div class="content">
                                                                                            <p>Apache Maven 3.8.6 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaven.apache.org%2Fdocs%2F3.8.6%2Frelease-notes.html" target="_blank">发布</a>。Apache Maven 是一个项目管理和构建工具。基于项目对象模型（POM）的概念， Maven 可以从中心位置管理项目的构建、报告和文档。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Bug</strong></p> 
<ul> 
 <li>[MNG-7432] - [REGRESSION] Resolver 会话包含非 MavenWorkspaceReader</li> 
 <li>[MNG-7433] - [REGRESSION] 在同一源码树上工作的多个 maven 实例会相互锁定</li> 
 <li>[MNG-7441] - 更新（可选）Logback 的版本以解决 CVE-2021-42550 问题</li> 
 <li>[MNG-7448] - 不要忽略 bin/，否则 apache-maven 中的 bin/ 模块不能被读取</li> 
 <li>[MNG-7455] - [REGRESSION] 在多线程构建中的 guice 注入期间，SessionScope 中的 IllegalStateException。</li> 
 <li>[MNG-7459] - Revert MNG-7347（SessionScoped Bean 应该是给定会话的 singletons）。</li> 
 <li>[MNG-7467] - [REGRESSION] 重定位传递依赖导致编译失败</li> 
 <li>[MNG-7487] - <span style="background-color:#ffffff; color:#222233">修复分叉生命周期中的死锁执行</span></li> 
 <li>[MNG-7493] - [REGRESSION] 解决子模块之间的依赖关系失败。</li> 
</ul> 
<p><strong style="color:#333333">New Feature</strong></p> 
<p>[MNG-7486] - 为 boxed log messages 创建多行消息助手</p> 
<p><strong style="color:#333333"><span style="background-color:#ffffff; color:#222233">Improvement</span></strong></p> 
<ul> 
 <li>[MNG-7445] - 重构一些无用的代码</li> 
 <li>[MNG-7476] - 当聚合器 mojo 锁定其他 mojo 执行时显示警告</li> 
</ul> 
<p><strong>Task</strong></p> 
<ul> 
 <li>[MNG-7466] - 对齐 Assembly Descriptor NS 版本</li> 
</ul> 
<p><strong style="color:#333333"><span style="background-color:#ffffff; color:#222233">Dependency upgrade</span></strong></p> 
<ul> 
 <li>[MNG-7488] - 将 SLF4J 升级到 1.7.36</li> 
 <li>[MNG-7489] - 将 JUnit 升级到 4.13.2</li> 
 <li>[MNG-7490] - 将 Plexus Utils 升级到 3.3.1</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情可</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.apache.org%2Fthread%2F44817jckpzy7gtrkds9xfrgybmrrbm1z" target="_blank">查看官方公告</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            