
---
title: 'Hyperf 发布 v2.1.16 版本，企业级的 PHP 微服务云原生协程框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9317'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 15:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9317'
---

<div>   
<div class="content">
                                                                    
                                                        <h1>更新内容</h1> 
<p>本周主要新增了部分特性，并修复了一些组件的 🐛Bug，继续提升 Hyperf 的稳定性，发布于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Freleases%2Ftag%2Fv2.1.16" target="_blank">2.1.16</a> 版。</p> 
<p>建议用户使用以下命令更新此版本。</p> 
<pre><code>composer update "hyperf/*" -o
</code></pre> 
<p>直接访问 官网 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.io" target="_blank">hyperf.io</a> 或 文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.wiki" target="_blank">hyperf.wiki</a> 查看更新内容</p> 
<h2>修复</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3510" target="_blank">#3510</a> 修复 <code>consul</code> 无法将节点强制离线的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3513" target="_blank">#3513</a> 修复 <code>Nats</code> 因为 <code>Socket</code> 超时时间小于最大闲置时间，导致连接意外关闭的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3520" target="_blank">#3520</a> 修复 <code>@Inject</code> 无法作用于嵌套 <code>Trait</code> 的问题。</li> 
</ul> 
<h2>新增</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3514" target="_blank">#3514</a> 新增方法 <code>Hyperf\HttpServer\Request::clearStoredParsedData()</code>。</li> 
</ul> 
<h2>优化</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf%2Fpull%2F3517" target="_blank">#3517</a> 优化 <code>Hyperf\Di\Aop\PropertyHandlerTrait</code>。</li> 
</ul> 
<h1>关于 Hyperf</h1> 
<p>Hyperf 是基于 <code>Swoole 4.5+</code> 实现的高性能、高灵活性的 PHP 协程框架，内置协程服务器及大量常用的组件，性能较传统基于 <code>PHP-FPM</code> 的框架有质的提升，提供超高性能的同时，也保持着极其灵活的可扩展性，标准组件均基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php-fig.org%2Fpsr" target="_blank">PSR 标准</a> 实现，基于强大的依赖注入设计，保证了绝大部分组件或类都是 <code>可替换</code> 与 <code>可复用</code> 的。</p> 
<p>框架组件库除了常见的协程版的 <code>MySQL 客户端</code>、<code>Redis 客户端</code>，还为您准备了协程版的 <code>Eloquent ORM</code>、<code>WebSocket 服务端及客户端</code>、<code>JSON RPC 服务端及客户端</code>、<code>GRPC 服务端及客户端</code>、<code>OpenTracing(Zipkin, Jaeger) 客户端</code>、<code>Guzzle HTTP 客户端</code>、<code>Elasticsearch 客户端</code>、<code>Consul、Nacos 服务中心</code>、<code>ETCD 客户端</code>、<code>AMQP 组件</code>、<code>Nats 组件</code>、<code>Apollo、ETCD、Zookeeper、Nacos 和阿里云 ACM 的配置中心</code>、<code>基于令牌桶算法的限流器</code>、<code>通用连接池</code>、<code>熔断器</code>、<code>Swagger 文档生成</code>、<code>Swoole Tracker</code>、<code>Blade、Smarty、Twig、Plates 和 ThinkTemplate 视图引擎</code>、<code>Snowflake 全局ID生成器</code>、<code>Prometheus 服务监控</code> 等组件，省去了自己实现对应协程版本的麻烦。</p> 
<p>Hyperf 还提供了 <code>基于 PSR-11 的依赖注入容器</code>、<code>注解</code>、<code>AOP 面向切面编程</code>、<code>基于 PSR-15 的中间件</code>、<code>自定义进程</code>、<code>基于 PSR-14 的事件管理器</code>、<code>Redis/RabbitMQ 消息队列</code>、<code>自动模型缓存</code>、<code>基于 PSR-16 的缓存</code>、<code>Crontab 秒级定时任务</code>、<code>Session</code>、<code>i18n 国际化</code>、<code>Validation 表单验证</code> 等非常便捷的功能，满足丰富的技术场景和业务场景，开箱即用。</p> 
<h1>框架初衷</h1> 
<p>尽管现在基于 PHP 语言开发的框架处于一个百花争鸣的时代，但仍旧未能看到一个优雅的设计与超高性能的共存的完美框架，亦没有看到一个真正为 PHP 微服务铺路的框架，此为 Hyperf 及其团队成员的初衷，我们将持续投入并为此付出努力，也欢迎你加入我们参与开源建设。</p> 
<h1>设计理念</h1> 
<p><code>Hyperspeed + Flexibility = Hyperf</code>，从名字上我们就将 <code>超高速</code> 和 <code>灵活性</code> 作为 Hyperf 的基因。</p> 
<ul> 
 <li>对于超高速，我们基于 Swoole 协程并在框架设计上进行大量的优化以确保超高性能的输出。</li> 
 <li>对于灵活性，我们基于 Hyperf 强大的依赖注入组件，组件均基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php-fig.org%2Fpsr" target="_blank">PSR 标准</a> 的契约和由 Hyperf 定义的契约实现，达到框架内的绝大部分的组件或类都是可替换的。</li> 
</ul> 
<p>基于以上的特点，Hyperf 将存在丰富的可能性，如实现 单体 Web 服务，API 服务，网关服务，分布式中间件，微服务架构，游戏服务器，物联网（IOT）等。</p> 
<h1>文档齐全</h1> 
<p>我们投入了大量的时间用于文档的建设以提供高质量的文档体验，以解决各种因为文档缺失所带来的问题，文档上也提供了大量的示例，对新手同样友好。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.wiki" target="_blank">Hyperf 官方开发文档</a></p> 
<h1>生产可用</h1> 
<p>我们为组件进行了大量的单元测试以保证逻辑的正确，目前存在 <code>1781</code> 个单测共 <code>5502</code> 个断言条件，Hyperf 是一款经历过严酷的生产环境考验的一个项目，目前已有很多的大型互联网企业都已将 Hyperf 部署到了自己的生产环境上并稳定运行。</p> 
<h1>官网及交流</h1> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhyperf%2Fhyperf" target="_blank">Github</a> 👈👈👈👈👈 点 Star 支持我们<br> <a href="https://gitee.com/hyperf/hyperf">Gitee 码云</a> 👈👈👈👈👈 点 Star 支持我们<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.io" target="_blank">Hyperf 官网</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhyperf.wiki" target="_blank">Hyperf 文档</a></p>
                                        </div>
                                      
</div>
            