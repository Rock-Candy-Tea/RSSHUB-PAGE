
---
title: 'Golang 实现的微服务框架 DMicro 发布 v1.0.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5697'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 14:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5697'
---

<div>   
<div class="content">
                                                                                            <h2><strong>更新记录:</strong></h2> 
<ol> 
 <li>发布新组件DServer,该组件是easyserver组件的升级版本。 <p>   1. DServer服务管理功能能够让你专注于编写业务代码，编译部署后的运行时管理就交给它吧。<br>    2. 支持单进程，多进程模式，单进程模式方便开发，多进程模式适合业务隔离。<br>    3. 原生支持平滑重启功能。<br>    4. 方便的扩展命令行功能。<br>    5. 原生支持命令行ctrl，方便开启关闭服务，重启服务，开启debug模式，查看实时运行日志，查看运行指标。</p> </li> 
 <li> <p>supervisor组件api大改,从功能独立的组件融合进框架，更好的与`dServer`组合。</p> </li> 
 <li> <p>drpc组件修复unix socket链接的监听。</p> </li> 
 <li> <p> 增加`benchmark`测试用例。</p> </li> 
 <li> <p>完善文档，增加更多的使用示例。</p> </li> 
</ol> 
<h2><strong>框架简介:</strong></h2> 
<p><br> <strong>DMicro</strong>是一个高效、可扩展且简单易用的微服务框架。包含DRPC,DServer等多个组件。</p> 
<p>其中DRPC组件是rpc框架，使用`endpoint`作为统一对象，为`RPC Server`，`RPC Clinet`提供统一的API封装。</p> 
<p><strong>DRPC组件特性：</strong></p> 
<ul> 
 <li> 易于理解，科学合理的多层抽象。 
  <ul> 
   <li>     `endpoint`,`session`,`handle`,`message`,`protoco`,`codec`,`transfer filter`,`plugin`.</li> 
  </ul> </li> 
 <li> 支持常见的消息通讯协议`json`，`prototbuf`,`http`,`jsronrpc`,良好的抽象层让自定义消息协议变得简单快捷。</li> 
 <li> 支持多种网络协议`tcp`,`unix`,`kcp`,`quic`,`websocket`等。。。</li> 
 <li> 全生命周期的插件埋点(多达27个埋点),让插件系统能实现的功能丰富多彩。 
  <ul> 
   <li>     内置 `auth`,`heartbeat`，`ignorecase`,`proxy`,`securebody`等插件</li> 
  </ul> </li> 
 <li> 依托丰富的插件埋点，抽象出易于使用的`Event`事件系统，让你的开发如虎添翼。</li> 
 <li> 高性能的网络传输层，让性能不再是瓶颈。</li> 
 <li> 客户端自动重拨。</li> 
 <li> 配合`DServer`组件，实现优雅的平滑重启，让你的服务时刻在线。</li> 
 <li> 配合`Registry`组件，实现服务注册。 
  <ul> 
   <li>     `Registry`组件抽象出合理的接口，方便接入多个服务注册中心，目前已实现`etcd`,`mdns`。</li> 
  </ul> </li> 
 <li> 配合`Selector`组件实现`服务发现`功能。</li> 
</ul> 
<p>`DServer`应用管理组件帮助大家封装好了应用的全生命周期管理。</p> 
<p><strong>DServer组件特性：</strong></p> 
<ul> 
 <li> 采用`server`,`service`,`sandbox`三层结构。 让业务专注于`sandbox`层，支持单进程，多进程模式。做到开发debug单进程，运行单/多进程可选。</li> 
 <li> 完善合理的启动命令封装，支持`start`,`stop`，`reload`,`ctrl`等命令。</li> 
 <li> 不但支持`drpc`组件，还支持`ghttp`等实现平滑重启接口的其他组件(如果不需要平滑重启，所有服务组件都支持)</li> 
 <li> 好用的命令行管理功能，让你能实时的管理正在运行的应用。</li> 
 <li> 完善的进程管理组件`supervisor`,支持对进程的全生命周期管理。</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            