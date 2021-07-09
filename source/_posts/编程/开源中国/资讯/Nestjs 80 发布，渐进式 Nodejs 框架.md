
---
title: 'Nest.js 8.0 发布，渐进式 Node.js 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5207'
author: 开源中国
comments: false
date: Fri, 09 Jul 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5207'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Nest.js 是一个用于构建高效、可扩展的 Node.js 服务器端应用程序的框架。它使用 TypeScript 和 JavaScript 构建，并结合了 OOP（面向对象编程）、FP（功能编程）和 FRP（功能反应式编程）等元素。</p> 
<p>Nest.js 8.0 正式发布，该版本更新内容如下：</p> 
<h3>特性：</h3> 
<ul> 
 <li>重构内置的控制台记录器类，分离出 <code>Logger</code> wrapper 类和 <code>ConsoleLogger</code> 类，添加缓冲日志功能，添加日志级别输出，支持日志级别功能；</li> 
 <li>添加 <code>StreamableFile</code> 类，用于从控制器路由流式传输文件（跨平台）；</li> 
 <li>增加 <code>ParseFloatPipe</code>和 <code>ParseEnumPipe</code> 类；</li> 
 <li>添加 lazy 模块加载器类；</li> 
 <li>添加 <code>RouterModule</code>，用于定义每个模块的控制器前缀；</li> 
 <li>增加从全局前缀中排除某些路由的能力；</li> 
 <li>API 版本管理功能；</li> 
 <li>支持多个事件订阅者；</li> 
 <li>支持向 <code>@Payload()</code> 装饰器传递一个属性键；</li> 
 <li>支持向 <code>@MessageBody()</code> 装饰器传递一个属性键；</li> 
 <li><code>WsAdapter</code> 支持在不同路径上注册网关，并让它们共享同一个 HTTP 服务器；</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li>调用生命周期 hooks 时按拓扑结构对模块进行排序；</li> 
 <li>使用类的引用作为提供者/控制者/注入物的键，而不是它们的名字；</li> 
 <li><code>BaseExceptionFilter</code> 支持 <code>http-errors</code>（以及任何其他指定了 <code>statusCode</code> 属性的错误对象）;</li> 
 <li>将 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ferror.name%2F" target="_blank"><code>Error.name</code></a> 属性设置为类的名称；</li> 
</ul> 
<h3>错误修复：</h3> 
<ul> 
 <li>为 mixin() 函数添加一个缺失的类型参数；</li> 
 <li>对于用 <code>@All()</code> 装饰器注释的路由使用 <code>router.all()</code> 方法，而不是 <code>router.use()</code> ；</li> 
 <li>在服务器绑定失败时拒绝 <code>listen()</code>；</li> 
 <li>指定 <code>@nestjs/platform-socket.io</code> 作为可选的对等依赖，以支持 PnP 模式；</li> 
</ul> 
<h3>依赖：</h3> 
<ul> 
 <li>更新以使用 <code>@grpc/grpc-js</code> 包，而不是 <code>grpc</code>；</li> 
 <li>将 NATS 升级到 v2 版；</li> 
 <li>将 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsocket.io%2F" target="_blank">Socket.io</a> 升级到 v4 版；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnestjs%2Fnest%2Freleases%2Ftag%2Fv8.0.0" target="_blank">https://github.com/nestjs/nest/releases/tag/v8.0.0</a></p>
                                        </div>
                                      
</div>
            