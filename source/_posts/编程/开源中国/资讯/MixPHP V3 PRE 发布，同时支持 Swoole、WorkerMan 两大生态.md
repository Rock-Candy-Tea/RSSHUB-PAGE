
---
title: 'MixPHP V3 PRE 发布，同时支持 Swoole、WorkerMan 两大生态'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4659'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 11:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4659'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start"><span style="color:#000000">MixPHP 是一个 PHP 命令行模式开发框架；基于 <code>Vega</code> 驱动的 HTTP 可以同时支持 Swoole、WorkerMan 两大生态，并且可以无缝切换；<code>V3</code> 是一个高度解耦的版本，整体代码基于多个独立的模块构建，即便用户不使用我们的脚手架，也可以使用这些独立模块，并且全部模块都支持原生开发。例如：你可以只使用 mix/vega 来搭配 laravel orm 使用；可以在任意环境中使用 mix/database 和 mix/redis；可以使用 mix/grpc 原生代码编写 gRPC；所有的模块你可以像搭积木一样随意组合。</span></p> 
<h2 style="text-align:start">独立模块</h2> 
<p style="text-align:start"><span style="color:#000000">核心模块全部可独立使用，并且都支持原生代码开发。</span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fvega" target="_blank">mix/vega</a> PHP 编写的 CLI 模式 HTTP 网络框架，支持 Swoole、WorkerMan，与 Go 生态的 gin 定位一致</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fdatabase" target="_blank">mix/database</a> 可在各种环境中使用的轻量数据库，支持 FPM、CLI、Swoole、WorkerMan，可选的连接池 (协程)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fredis" target="_blank">mix/redis</a> 可在各种环境中使用的 PHP Redis，支持 FPM、CLI、Swoole、WorkerMan，可选的连接池 (协程)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fredis-subscribe" target="_blank">mix/redis-subscribe</a> 基于 Swoole 协程的 Redis 原生协议订阅库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fgrpc" target="_blank">mix/grpc</a> 基于 Swoole 协程的 PHP gRPC 库，包含 protoc 代码生成器、服务器、客户端</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fwebsocket" target="_blank">mix/websocket</a> 基于 Swoole 协程的 PHP WebSocket 服务器与客户端</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fvalidate" target="_blank">mix/validate</a> 基于 PSR-7 的验证库 <code>重构中</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fworker-pool" target="_blank">mix/worker-pool</a> 基于 Swoole 的协程池、工作池库 <code>重构中</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fcli" target="_blank">mix/cli</a> PHP 命令行交互指挥官 <code>重构中</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fevent" target="_blank">mix/event</a> 基于 PSR-14 标准的事件调度库 <code>重构中</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fsession" target="_blank">mix/session</a> PHP 命令行模式的 session 库 <code>重构中</code></li> 
</ul> 
<h2 style="text-align:start">快速开始</h2> 
<p style="text-align:start"><span style="color:#000000">提供了现成的脚手架，快速创建项目，立即产出。</span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fapi-skeleton%23readme" target="_blank">编写一个 API 接口</a></li> 
</ul> 
<div style="text-align:start"> 
 <pre><code>composer create-project --prefer-dist mix/api-skeleton api
</code></pre> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fweb-skeleton%23readme" target="_blank">编写一个 Web 页面</a></li> 
</ul> 
<div style="text-align:start"> 
 <pre><code>composer create-project --prefer-dist mix/web-skeleton web
</code></pre> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fwebsocket-skeleton%23readme" target="_blank">编写一个 WebSocket 服务</a></li> 
</ul> 
<div style="text-align:start"> 
 <pre><code>composer create-project --prefer-dist mix/websocket-skeleton websocket
</code></pre> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fgrpc-skeleton%23readme" target="_blank">编写一个 gRPC 接口</a></li> 
</ul> 
<div style="text-align:start"> 
 <pre><code>composer create-project --prefer-dist mix/grpc-skeleton grpc
</code></pre> 
</div> 
<h2 style="text-align:start">技术交流</h2> 
<ul> 
 <li style="text-align:start"><span style="color:#000000">知乎：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fpeople%2Fonanying" target="_blank"><span style="color:#2980b9">https://www.zhihu.com/people/onanying</span></a></li> 
 <li style="text-align:start"><span style="color:#000000">官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenmix.org%2Fmix-php" target="_blank">https://openmix.org/mix-php</a></span></li> 
</ul> 
<h2 style="text-align:start">Golang 框架</h2> 
<p style="text-align:start"><span style="color:#000000">OpenMix 同时还有 Golang 生态的框架</span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fmix" target="_blank">https://github.com/mix-go/mix</a></li> 
</ul> 
<h2 style="text-align:start">旧版文档</h2> 
<ul> 
 <li><code>V1</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fonanying%2Fmixphp1%2Fcontent" target="_blank">https://www.kancloud.cn/onanying/mixphp1/content</a></li> 
 <li><code>V2</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fonanying%2Fmixphp2%2Fcontent" target="_blank">https://www.kancloud.cn/onanying/mixphp2/content</a></li> 
 <li><code>V2.1</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fonanying%2Fmixphp2-1%2Fcontent" target="_blank">https://www.kancloud.cn/onanying/mixphp2-1/content</a></li> 
 <li><code>V2.2</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fonanying%2Fmixphp2-2%2Fcontent" target="_blank">https://www.kancloud.cn/onanying/mixphp2-2/content</a></li> 
</ul> 
<h2 style="text-align:start">License</h2> 
<p style="text-align:start">Apache License Version 2.0, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank">http://www.apache.org/licenses/</a></p>
                                        </div>
                                      
</div>
            