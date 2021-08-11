
---
title: '🚀🚀🚀 EasySwoole 发布部分组件更新 _ 企业级分布式 PHP 协程框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=135'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 23:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=135'
---

<div>   
<div class="content">
                                                                                            <h1>EasySwoole 发布 v3.4.6 部分组件更新 | 一款企业级分布式 PHP 协程框架</h1> 
<h1>更新内容 </h1> 
<p>此次更新我们更新了部分组件的功能，并且修复部分组件的 bug，继续提升了 EasySwoole 的稳定性。</p> 
<p>- 发布组件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasy-swoole%2Fcomponent%2Freleases%2Ftag%2F2.3.1" target="_blank">easyswoole/component v2.3.1</a> 版本；<br> - 发布组件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasy-swoole%2Frpc%2Freleases%2Ftag%2F5.0.5" target="_blank">easyswoole/rpc v5.0.5</a> 版本；<br> - 发布组件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasy-swoole%2Frpc%2Freleases%2Ftag%2F1.3.0" target="_blank">easyswoole/pay v1.3.0</a> 版本；</p> 
<p>关于以上组件的具体使用，请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.easyswoole.com" target="_blank">EasySwoole 官方文档</a>。</p> 
<h3>修复 </h3> 
<p>- 修复 easyswoole/pay 组件，修复不兼容最新支付宝单笔转账接口的 bug。</p> 
<h2>优化</h2> 
<p>- 优化 easyswoole/component 组件，避免进程对象被重复注册的问题。<br> - 优化 easyswoole/rpc 组件，让用户可以自定义配置 rpc 服务端使用的最大内存限制。</p> 
<h1>关于 EasySwoole  </h1> 
<div> 
 <div>
  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.juejin.cn%3Ftarget%3Dhttps%253A%252F%252Fwww.easyswoole.com" target="_blank">EasySwoole</a> 是一款支持企业级分布式部署的协程 
  <code>PHP</code> 框架，它是一款常驻内存型的分布式 
  <code>Swoole</code> 框架，专为 
  <code>API</code> 而生，摆脱传统 
  <code>PHP</code> 运行模式在进程唤起和文件加载上带来的性能损失，支持高并发、高可用，相比于其他的 
  <code>Swoole</code> 框架（例如 
  <code>Hyperf</code>、
  <code>Swoft</code> 等），
  <code>EasySwoole</code> 的并发能力更强。
  <code>EasySwoole</code> 高度封装了 
  <code>Swoole Server</code> 而依旧维持 
  <code>Swoole Server</code> 原有特性，支持同时混合监听 
  <code>HTTP</code>、
  <code>WebSocket</code>、
  <code>自定义 TCP、UDP 协议</code>，并且拥有丰富的组件。例如 
  <code>协程通用连接池</code>、
  <code>TP 风格的协程 ORM</code>、
  <code>协程微信 SDK</code>、
  <code>协程支付宝 SDK</code>、
  <code>协程 Kafka 客户端</code>、
  <code>协程 ElasticSearch 客户端</code>、
  <code>协程 Consul 客户端</code>、
  <code>协程 Redis 客户端</code>、
  <code>协程 Apollo 客户端</code>、
  <code>协程 NSQ 客户端</code>、
  <code>协程自定义队列</code>、 
  <code>协程 Memcached 客户端</code>、
  <code>协程视图引擎</code>、
  <code>JWT</code>、
  <code>协程 RPC</code>、
  <code>协程 SMTP 客户端</code>、
  <code>协程 HTTP/WebSocket 客户端</code>、
  <code>协程 Actor</code>、
  <code>Crontab 定时器</code>、
  <code>协程 Redis 连接池</code>、
  <code>协程 MySQL 连接池</code>、
  <code>协程上下文管理</code>、
  <code>IOC</code>、
  <code>雪花算法 Snowflake Id 生成器</code>、
  <code>协程 HTTP、TCP、UDP、WebSocket 服务端</code> 、
  <code>验证器</code>、
  <code>验证码</code>、
  <code>自定义进程</code>、
  <code>Tracker 链路追踪</code>、
  <code>Atomic限流器</code>、
  <code>Fast-Cache 缓存</code>、
  <code>注解及 API 文档自动生成</code>、
  <code>Policy 权限</code>、
  <code>Casbin 验证权限</code>、
  <code>自动生成代码</code>、
  <code>OAuth</code>、
  <code>协程 OSS/COS 客户端</code>、
  <code>Printer 易联云打印机 SDK</code>、
  <code>数据库迁移</code>、
  <code>协程 Etcd 客户端</code> 等诸多组件。让开发者以最低的学习成本和精力编写出多进程、可异步、高可用的应用服务。
 </div> 
</div> 
<h1>设计理念</h1> 
<div> 
 <div> 
  <p><code>EasySwoole</code> 作者最早接触 <code>Swoole</code>，是 <code>2015</code> 年年初，为实现一个可以实时控制的多进程爬虫而接触的 <code>Swoole</code>，进而为 <code>Swoole</code> 的各种便捷、高效所着迷。 为此，做了综合技术评审之后，公司决定开始全线推广 <code>Swoole</code>，并利用 <code>Swoole</code> 实现承载每天对外过亿的任务爬取与投递服务。<code>2017</code> 年年初，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.juejin.cn%3Ftarget%3Dhttp%253A%252F%252Frango.swoole.com%252F" target="_blank">Rango</a> 的鼓励下，作者决定将框架进行开源，并在 <code>Rango</code> 的建议下，命名为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.juejin.cn%3Ftarget%3Dhttps%253A%252F%252Fwww.easyswoole.com" target="_blank">EasySwoole</a>。</p> 
  <p>目前为止，<code>EasySwoole</code> 一直秉承着 “ 让开发者学习使用 Swoole 更 Easy ” 的理念，我们逐步完善 <code>EasySwoole</code> 框架的文档，让更多的 <code>phper</code> 能够更好、更快、更加容易地入门<code>Swoole</code>，拥抱 <code>Swoole</code> 的怀抱，让更多的开发者能够轻轻松松就能写出支持高并发、高并发的应用服务。</p> 
 </div> 
</div> 
<h1>文档齐全</h1> 
<p>我们投入了大量的时间用于文档的建设，以解决各种因为文档缺失所带来的问题，文档上也提供了大量的示例，对新手非常友好。EassySwoole 官网文档地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.easyswoole.com" target="_blank">https://www.easyswoole.com</a></p> 
<h1>生产可用</h1> 
<div> 
 <div>
  我们为组件进行了大量的单元测试以保证逻辑的正确，同时维护了高质量的文档。并且目前为止，
  <code>EasySwoole</code> 已经在 
  <code>CCTV</code>、
  <code>腾讯 IEG</code>、
  <code>360 金融</code>、
  <code>360 小游戏</code>、
  <code>9377 小游戏</code>、
  <code>厦门美图网</code>、
  <code>网宿科技</code>、
  <code>元初食品</code>、
  <code>蝉大师</code>、
  <code>宝宝巴士</code>、
  <code>瑞祥科技集团</code> 等诸多公司的项目的生产环境中使用，可以说是经过了严酷的生产环境的考验。也正是因为经历了大量线上项目生产环境的使用，我们才正式地对外开放该项目。因为我们足够稳定，所以客户使用足够放心。
 </div> 
</div> 
<h1>官网及交流</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasy-swoole%2Feasyswoole" target="_blank">Github</a> <- 点 Star 支持我们</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.easyswoole.com" target="_blank">EasySwoole 官网</a></p> 
<p>EasySwoole 交流 QQ 群：853946743</p> 
<p>EasySwoole VIP QQ 群：579434607 （本群需要付费599元）</p>
                                        </div>
                                      
</div>
            