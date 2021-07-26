
---
title: 'MixPHP V3 发布，有哪些变化和特点'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2984'
author: 开源中国
comments: false
date: Mon, 26 Jul 2021 11:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2984'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">最近把 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fmix" target="_blank">MixPHP</a> 逐步重构到了 V3 版本，之前停更了很长时间，是因为一直在开发 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-go%2Fmix" target="_blank">MixGo</a> ，回想起 V2~V2.2 版本中我做了很多尝试，其中特别是 V2.2 我非常激进的直接 all in 单线程协程。</p> 
<h2 style="text-align:start">完全独立的模块</h2> 
<p style="text-align:start">以前我开发框架是先构建整体，然后根据框架的需要拆分模块，这导致了模块太多了，有些代码老是感觉放哪里都不太对非常的纠结，各个库之间总是有千丝万缕的联系，独立使用的时候老是连带下载一堆的库。</p> 
<p style="text-align:start">V3 开始我采用了完全 golang 的那种可插拔的封装思想，我先开发很多个独立的库，这些库的代码尽量的内聚，然后我编写一个骨架，将这些库组合起来使用，我逐步的重构了这些最重要的库。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fvega" target="_blank">mix/vega</a> PHP 编写的 CLI 模式 HTTP 网络框架，支持 FPM、Swoole、WorkerMan，与 Go 生态的 gin 定位一致</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fdatabase" target="_blank">mix/database</a> 可在各种环境中使用的轻量数据库，支持 FPM、CLI、Swoole、WorkerMan，可选的连接池 (协程)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fredis" target="_blank">mix/redis</a> 可在各种环境中使用的 PHP Redis，支持 FPM、CLI、Swoole、WorkerMan，可选的连接池 (协程)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fredis-subscribe" target="_blank">mix/redis-subscribe</a> 基于 Swoole 协程的 Redis 原生协议订阅库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fgrpc" target="_blank">mix/grpc</a> 基于 Swoole 协程的 PHP gRPC 库，包含 protoc 代码生成器、服务器、客户端</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fwebsocket" target="_blank">mix/websocket</a> 基于 Swoole 协程的 PHP WebSocket 服务器与客户端</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fvalidate" target="_blank">mix/validate</a> 基于 PSR-7 的验证库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fworker-pool" target="_blank">mix/worker-pool</a> 基于 Swoole 的协程池、工作池库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fevent" target="_blank">mix/event</a> 基于 PSR-14 标准的事件调度库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fcli" target="_blank">mix/cli</a> PHP 命令行交互指挥官 <code>重构中</code></li> 
</ul> 
<p style="text-align:start">每个库都是独立可执行的，你可以只使用 mix/vega 来搭配 laravel orm 使用；可以在任意环境中使用 mix/database 和 mix/redis；可以使用 mix/grpc 原生代码编写 gRPC；所有的模块你可以像搭积木一样随意组合。</p> 
<h2 style="text-align:start">更多的使用场景，暴露原生接口</h2> 
<p style="text-align:start">在 V1,V2 的时候，我们总是只能在一种固定的进程模式下使用，因为我们这些框架把 swoole 底层封装起来了，因为封装导致原生接口其实是无法暴露出来的，因此都是通过配置的方式来做一些有限的模式切换。</p> 
<p style="text-align:start">V3 我做的比较彻底，我通过封装的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fmix-php%2Fvega" target="_blank">mix/vega</a> 只在请求事件那里引入框架，完全把原生代码暴露出来，带来了非常灵活的启动方式，可以同时支持：Swoole 多进程同步，多进程协程，单进程协程，WorkerMan 多进程同步，还有 FPM。包含了 CLI 下两大生态的全部执行模式，并且代码完全一致，可以随意切换，这带来了巨大的可选择性，对协程兼容性困扰的用户可以选择同步模式，在 windows 下无法开发的用户可以选择 WorkerMan，FPM 驱动，甚至如果需要 Swow 我都可以接入进来。</p> 
<h2 style="text-align:start">数据库组件</h2> 
<p style="text-align:start">这次数据库解决了之前的持有连接导致死锁的问题，同时优化了池的实现，同时废弃了之前复杂的 where 设计，采用的更加简单的 ? 绑定方式，这种方式在 golang 中普通采用。这些改变带来了稳定性和性能的提升，同时更加雅观了，当然还增加了 FPM 的支持，我看到有些用户喜欢单独使用他们。</p> 
<p style="text-align:start">数据库不管在协程、同步、FPM 执行，代码无需修改，只有在协程时单独调用一下 <code>startPool()</code> 即可。</p> 
<h2 style="text-align:start">独立、灵活、性能好</h2> 
<p style="text-align:start">以上，MixPHP V3 带来了很多显著的变化，但依然是一个轻量的高性能框架，现在你可以像使用 <code>symfony</code> 一样独立使用我们的模块了。</p>
                                        </div>
                                      
</div>
            