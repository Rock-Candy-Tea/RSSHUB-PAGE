
---
title: 'Golang 实现的微服务框架 DMicro 发布 v1.1.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1374'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 10:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1374'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><strong>更新记录:</strong></h2> 
<p>1. 替换 `dserver` 组件的命令行解析工具为 `Cobra`组件。<br> 2. `dserver` 组件中的 `ctrl` 命令替换为 `ctl`<br> 3. `dserver` 组件中的 `rpc server option`参数变成 `ServerName`<br> 4. 取消`endpoint`与`eventbus`强关联。<br> 5. 新增 `Metrics` 指标组件,支持统计运行指标。<br> 6. 修复 `rpc client` 与 `rpc server` 中 `close` 报错的问题.<br> 7. 移除 `EndpiontConfig`中的`CountTime`参数，默认开启请求耗时统计。<br> 8. 完善 `Rpc Server`,`Rpc Client`,`Metrics`组件的使用文档。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>框架简介:</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><br> <strong>DMicro</strong><span> </span>是一个高效、可扩展且简单易用的微服务框架。包含 DRPC,DServer 等多个组件。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">其中 DRPC 组件是 rpc 框架，使用 `endpoint` 作为统一对象，为 `RPC Server`，`RPC Clinet` 提供统一的 API 封装。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>DRPC 组件特性：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 易于理解，科学合理的多层抽象。 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>     `endpoint`,`session`,`handle`,`message`,`protoco`,`codec`,`transfer filter`,`plugin`.</li> 
  </ul> </li> 
 <li> 支持常见的消息通讯协议 `json`，`prototbuf`,`http`,`jsronrpc`, 良好的抽象层让自定义消息协议变得简单快捷。</li> 
 <li> 支持多种网络协议 `tcp`,`unix`,`kcp`,`quic`,`websocket` 等。。。</li> 
 <li> 全生命周期的插件埋点 (多达 27 个埋点), 让插件系统能实现的功能丰富多彩。 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>     内置 `auth`,`heartbeat`，`ignorecase`,`proxy`,`securebody` 等插件</li> 
  </ul> </li> 
 <li> 依托丰富的插件埋点，抽象出易于使用的 `Event` 事件系统，让你的开发如虎添翼。</li> 
 <li> 高性能的网络传输层，让性能不再是瓶颈。</li> 
 <li> 客户端自动重拨。</li> 
 <li> 配合 `DServer` 组件，实现优雅的平滑重启，让你的服务时刻在线。</li> 
 <li> 配合 `Registry` 组件，实现服务注册。 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>     `Registry` 组件抽象出合理的接口，方便接入多个服务注册中心，目前已实现 `etcd`,`mdns`。</li> 
  </ul> </li> 
 <li> 配合 `Selector` 组件实现 `服务发现` 功能。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">`DServer` 应用管理组件帮助大家封装好了应用的全生命周期管理。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>DServer 组件特性：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 采用 `server`,`service`,`sandbox` 三层结构。 让业务专注于 `sandbox` 层，支持单进程，多进程模式。做到开发 debug 单进程，运行单 / 多进程可选。</li> 
 <li> 完善合理的启动命令封装，支持 `start`,`stop`，`reload`,`ctrl` 等命令。</li> 
 <li> 不但支持 `drpc` 组件，还支持 `ghttp` 等实现平滑重启接口的其他组件 (如果不需要平滑重启，所有服务组件都支持)</li> 
 <li> 好用的命令行管理功能，让你能实时的管理正在运行的应用。</li> 
 <li> 完善的进程管理组件 `supervisor`, 支持对进程的全生命周期管理。</li> 
</ul>
                                        </div>
                                      
</div>
            