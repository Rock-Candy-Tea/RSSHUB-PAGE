
---
title: 'Appwrite 1.0 发布，Firebase 开源替代品'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2047'
author: 开源中国
comments: false
date: Mon, 26 Sep 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2047'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Appwrite 是一个基于 Docker 的端到端开发者平台，其容器化的微服务库可应用于网页端、移动端，以及后端。Appwrite 通过视觉化界面极简了从零编写 API 的繁琐过程，在保证软件安全的前提下为开发者创造了一个高效的开发环境。</p> 
<p>Appwrite 可以提供给开发者用户验证、外部授权、用户数据读写检索、文件储存、图像处理、云函数计算等多种服务.</p> 
<h3>特性</h3> 
<ul> 
 <li>增加了在用户界面中查看所有资源的 Parent ID 的用户界面</li> 
 <li>为 Appwrite 内部服务增加了自动缓存清理功能</li> 
 <li>增加了 Appwrite 处理导入散列密码的功能，这可以用来从其他系统导入现有的用户数据</li> 
 <li>在 Appwrite 控制台中， <code>Users</code>现在被重新命名为 <code>Authentication</code></li> 
 <li>更多的端点被公开（针对客人），并有适当的速率限制</li> 
 <li>增加了 Discuz、Podio 和 Etsy OAuth 提供者</li> 
 <li>功能日志现在可以捕获 stdout</li> 
 <li>增加了授予客人对文档、文件和执行的写入权限的功能</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>修正在 Appwrite 控制台重设密码后，你不会被重定向到登录页面</li> 
 <li>修正了无效的数据可能被载入 Appwrite 控制台</li> 
 <li>修正了一个使用 MySQL 适配器的用户会遇到全文索引的问题</li> 
 <li>修复了团队被创建时没有所有者的问题</li> 
 <li>修正了一个无法通过电话搜索用户的问题</li> 
 <li>修正了一个未接受的邀请会授予对项目的访问权的问题</li> 
</ul> 
<h3>重要变化</h3> 
<ul> 
 <li>所有的 Date 值现在都存储为 ISO-8601 而不是 UNIX 时间戳</li> 
 <li>权限级别和语法已被重新设计</li> 
 <li>函数变量现在被存储在一个单独的集合中，有自己的 API 端点</li> 
 <li>在函数中， <code>req.env</code> 已被重命名为 <code>req.variables</code></li> 
 <li>异步计算的资源，现在将返回 <code>202 Accepted</code> 状态代码，而不是 <code>200 OK</code></li> 
 <li>查询已经得到改进，允许更多的灵活性，并引入了新的端点</li> 
 <li>复合索引现在更加灵活</li> 
 <li><code>createExecution</code> 参数的 <code>async</code> 默认值从 <code>true</code> 改为 <code>false</code></li> 
 <li>在函数集合中，字符串属性 <code>status</code> 已被重构为一个 <code>enabled</code> 的布尔属性</li> 
 <li>Execution 响应模型中的 <code>time</code> 属性已被重命名为 <code>duration</code>，以便与其他响应模型更加一致</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappwrite%2Fappwrite%2Freleases%2Ftag%2F1.0.0" target="_blank">https://github.com/appwrite/appwrite/releases/tag/1.0.0</a></p>
                                        </div>
                                      
</div>
            