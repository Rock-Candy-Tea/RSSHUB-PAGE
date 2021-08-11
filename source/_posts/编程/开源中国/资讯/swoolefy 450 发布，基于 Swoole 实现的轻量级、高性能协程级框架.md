
---
title: 'swoolefy 4.5.0 发布，基于 Swoole 实现的轻量级、高性能协程级框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3360'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 10:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3360'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">swoolefy是一个基于swoole实现的轻量级高性能的常驻内存型的API和Web应用服务框架， 高度封装了http，websocket，udp服务器，以及基于tcp实现可扩展的rpc服务， 同时支持composer包方式安装部署项目。基于实用，swoolefy抽象Event事件处理类， 实现与底层的回调的解耦，支持协程调度，同步|异步调用，全局事件注册，心跳检查，异步任务，多进程(池)等.</span></p> 
<p><span style="background-color:#ffffff; color:#333333">github: </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbingcool%2Fswoolefy" target="_blank">https://github.com/bingcool/swoolefy</a></p> 
<p>主要更新如下：</p> 
<ul> 
 <li>抽离swoolefy内置的组件库，作为独立的公共协程库bingcool/library, swoolefy仅作为核心模型，详情：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbingcool%2Flibrary" target="_blank">https://github.com/bingcool/library</a></li> 
 <li><span style="background-color:#ffffff; color:#24292e">支持mqtt服务,依赖swoole以及simps/mqtt</span></li> 
 <li><span style="background-color:#ffffff; color:#24292e">重构 exception handle，上下兼容</span></li> 
 <li><span style="background-color:#ffffff; color:#24292e">优化进程管理器，支持自定义进程作为附属进程绑定在worker进程上处理</span></li> 
 <li><span style="background-color:#ffffff; color:#24292e">fixed  some bugs</span></li> 
</ul>
                                        </div>
                                      
</div>
            