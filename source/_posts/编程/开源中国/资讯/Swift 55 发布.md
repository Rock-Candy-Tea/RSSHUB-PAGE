
---
title: 'Swift 5.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7671'
author: 开源中国
comments: false
date: Thu, 23 Sep 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7671'
---

<div>   
<div class="content">
                                                                                            <p>Swift 5.5 稳定版现已发布。这是一个大规模的版本，引入了全新的<span style="background-color:#ffffff; color:#333333">并发编程方式</span>，包括 async/await 语法、结构化并发和 Actors。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Swift Evolution 流程中的一些提案也在 Swift 5.5 中得以实现：</p> 
<ul> 
 <li>SE-0291 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0291-package-collections.md" target="_blank">包集合</a></li> 
 <li>SE-0293 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0293-extend-property-wrappers-to-function-and-closure-parameters.md" target="_blank">将属性包装器扩展到函数和闭包参数</a></li> 
 <li>SE-0295 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0295-codable-synthesis-for-enums-with-associated-values.md" target="_blank">具有关联值的枚举的可编码合成</a></li> 
 <li>SE-0296 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0296-async-await.md" target="_blank">Async/await</a></li> 
 <li>SE-0297 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0297-concurrency-objc.md" target="_blank">与 Objective-C 的并发互操作性</a></li> 
 <li>SE-0298 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0298-asyncsequence.md" target="_blank">Async/Await: Sequences</a></li> 
 <li>SE-0299 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0299-extend-generic-static-member-lookup.md" target="_blank">在 Generic Contexts 中扩展</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0299-extend-generic-static-member-lookup.md" target="_blank">Static Member Lookup</a></li> 
 <li>SE-0300 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0300-continuation.md" target="_blank">用于将异步任务与同步代码连接的延续</a></li> 
 <li>SE-0304 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0304-structured-concurrency.md" target="_blank">结构化并发</a></li> 
 <li>SE-0306 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0306-actors.md" target="_blank">Actors</a></li> 
 <li>SE-0307 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0307-allow-interchangeable-use-of-double-cgfloat-types.md" target="_blank">允许互换使用 CGFloat 和 Double 类型</a></li> 
 <li>SE-0308 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0308-postfix-if-config-expressions.md" target="_blank">if for postfix member expressions</a></li> 
 <li>SE-0310 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0310-effectful-readonly-properties.md" target="_blank">有效的只读属性</a></li> 
 <li>SE-0311 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0311-task-locals.md" target="_blank">Task Local Values</a></li> 
 <li>SE-0313 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0313-actor-isolation-control.md" target="_blank">改进了对 actor isolation 的控制</a></li> 
 <li>SE-0314 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0314-async-stream.md" target="_blank">AsyncStream 和 AsyncThrowingStream</a></li> 
 <li>SE-0316 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0316-global-actors.md" target="_blank">Global actors</a></li> 
 <li>SE-0317 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0317-async-let.md" target="_blank">async let bindings</a></li> 
 <li>SE-0319 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapple%2Fswift-evolution%2Fblob%2Fmain%2Fproposals%2F0319-never-identifiable.md" target="_blank">Conform Never to Identifiable</a></li> 
</ul> 
<p>详情可查看发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fswift.org%2Fblog%2Fswift-5-5-released%2F" target="_blank">https://swift.org/blog/swift-5-5-released/</a></p>
                                        </div>
                                      
</div>
            