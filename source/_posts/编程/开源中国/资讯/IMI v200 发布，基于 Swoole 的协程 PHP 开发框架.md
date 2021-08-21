
---
title: 'IMI v2.0.0 发布，基于 Swoole 的协程 PHP 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0820/155727_6d8999ad_105007.png'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 15:58:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0820/155727_6d8999ad_105007.png'
---

<div>   
<div class="content">
                                                                                            <p>IMI v2.0.0 已经发布，基于 Swoole 的协程 PHP 开发框架。</p> 
<p><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0820/155727_6d8999ad_105007.png" referrerpolicy="no-referrer"></p> 
<h1>imi v2.0</h1> 
<h2>框架介绍</h2> 
<p>imi 是一款支持长连接微服务分布式的 PHP 开发框架，它可以运行在 PHP-FPM、Swoole、Workerman 多种容器环境下。</p> 
<p>imi 支持开发 Http 接口，以及 Http2、WebSocket、TCP、UDP、MQTT 等常驻内存服务。</p> 
<p>imi 拥有丰富的功能组件，v2.0 版本内置了 2 个分布式长连接服务的解决方案。</p> 
<p>imi 框架现在已经稳定运行在：文旅电商平台、物联网充电云平台、停车云平台、支付微服务、短信微服务、钱包微服务、卡牌游戏服务端、数据迁移服务（虎扑）等项目中。</p> 
<blockquote> 
 <p>imi 第一个版本发布于 2018 年 6 月 21 日</p> 
</blockquote> 
<ul> 
 <li>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fimiphp%2Fimi" target="_blank">https://github.com/imiphp/imi</a>;</li> 
 <li>Gitee: <a href="https://gitee.com/yurunsoft/IMI" target="_blank">https://gitee.com/yurunsoft/IMI</a>; (GVP 项目)</li> 
 <li>文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.imiphp.com%2F" target="_blank">https://doc.imiphp.com/</a>;</li> 
 <li>imi v2.0 发布介绍视频： 知乎：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fzvideo%2F1404410018154770432" target="_blank">https://www.zhihu.com/zvideo/1404410018154770432</a> B站：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Bv411E7ce%2F" target="_blank">https://www.bilibili.com/video/BV1Bv411E7ce/</a></li> 
</ul> 
<h2>鸣谢</h2> 
<p>感谢群里抢先体验 imi 2.0，提出建议和反馈 bug 的开发者们！</p> 
<p>感谢 @Gumo666 @NHZEX <a href="https://www.oschina.net/loyating">@loyating </a> 等开发者对 imi 文档或代码的贡献！</p> 
<h2>作者介绍</h2> 
<p>宇润（张润宇），1994 年 3 月 12 日（植树节）出生于无锡。</p> 
<p>初二开始就自学编程，喜欢 C#，但事与愿违，工作后一直从事 PHP 开发工作。</p> 
<p>imi 框架创始人，Swoole 开发组成员，宇润 PHP 系列组件作者。</p> 
<p>开源项目包括但不限于：imi、PaySDK、YurunHttp、Guzzle-Swoole、YurunOAuthLogin、ChineseUtil 等</p> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/yurunsoft" target="_blank">https://gitee.com/yurunsoft</a></li> 
 <li>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FYurunsoft" target="_blank">https://github.com/Yurunsoft</a></li> 
 <li>b站：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspace.bilibili.com%2F768718" target="_blank">https://space.bilibili.com/768718</a></li> 
 <li>程序员划水专用QQ群：74401592</li> 
 <li>imi 交流QQ群：17916227</li> 
</ul> 
<h2>2.0 版本介绍</h2> 
<ul> 
 <li> <p>多容器：支持 Swoole、Workerman、PHP-FPM 等</p> </li> 
 <li> <p>分布式：无心智负担的长连接分布式解决方案</p> </li> 
 <li> <p>高性能：常驻内存 + PHP 8.0 JIT</p> </li> 
 <li> <p>次世代：下一代 PHP 框架（与 Laravel Octane 的多容器支持理念，不谋而合）</p> </li> 
</ul> 
<blockquote> 
 <p>2.0 版本目前处于测试阶段，不久之后将发布正式版本</p> 
</blockquote> 
<h3>快速体验</h3> 
<p>创建 Http Server 项目：<code>composer create-project imiphp/project-http</code></p> 
<p>创建 WebSocket Server 项目：<code>composer create-project imiphp/project-websocket</code></p> 
<p>创建 TCP Server 项目：<code>composer create-project imiphp/project-tcp</code></p> 
<p>创建 UDP Server 项目：<code>composer create-project imiphp/project-udp</code></p> 
<h3>环境要求</h3> 
<ul> 
 <li>PHP 7.4、8.0</li> 
 <li>Swoole >= 4.7</li> 
 <li>Windows、Liunx、MacOS</li> 
</ul> 
<h3>新特性</h3> 
<ul> 
 <li> <p>PHP 8.0 原生注解（原注释写法依旧支持）</p> </li> 
 <li> <p>内置长连接服务分布式解决方案，助力 PHP 物联网生态</p> </li> 
 <li> <p>多容器支持，可以运行在 Swoole、Workerman、PHP-FPM、Cli 环境</p> </li> 
 <li> <p>解决痛点：beanScan、Main 类等现已是非必选项</p> </li> 
 <li> <p>解决痛点：PSR-7 基础上增加 setXXX 方法，保留 withXXX 并完全兼容 PSR-7</p> </li> 
 <li> <p>命令行包改用 symfony/console</p> </li> 
 <li> <p>日志组件改用 monolog/monolog</p> </li> 
 <li> <p>等……</p> </li> 
</ul> 
<h3>开发思路</h3> 
<ul> 
 <li> <p>废除 v1 中不合理、写法啰嗦的地方，简化配置，imi 让开发项目一把梭的理念从未改变</p> </li> 
 <li> <p>将一些功能，交给更加成熟的第三方包，imi 有它自己的使命</p> </li> 
 <li> <p>全部使用强类型、严格模式开发，保证代码质量</p> </li> 
 <li> <p>重构底层，让框架支持在多种服务容器下运行（Swoole、Workerman、PHP-FPM 等），方便扩展</p> </li> 
 <li> <p>专注提升分布式长连接服务开发体验，这是目前市面上框架的不足之处，还只是用来开发 Http 服务，这么用 Swoole 和 Workerman 简直是暴殄天物</p> </li> 
</ul> 
<h3>PHP 8.0 原生注解支持</h3> 
<p><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0820/155739_fd616aa5_105007.png" referrerpolicy="no-referrer"></p> 
<h3>长连接服务分布式解决方案</h3> 
<p><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0820/155744_d96f2436_105007.png" referrerpolicy="no-referrer"></p> 
<p><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0820/155754_f421a0ae_105007.png" referrerpolicy="no-referrer"></p> 
<p><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0820/155802_99a5f2e3_105007.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>Demo 体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fimiphp%2Fimi-project-websocket" target="_blank">https://github.com/imiphp/imi-project-websocket</a>;</p> 
</blockquote> 
<h2>后续计划</h2> 
<ul> 
 <li> <p>让更多组件支持在非 Swoole 环境下运行</p> </li> 
 <li> <p>支持 Swow、RoadRunner 环境</p> </li> 
 <li> <p>长连接分布式解决方案，支持更多消息中间件、网关</p> </li> 
 <li> <p>更多微服务化的组件开发和深度集成</p> </li> 
 <li> <p>imi v2 免费视频教程、源码分析视频等</p> </li> 
</ul> 
<h2>拥抱开源</h2> 
<ul> 
 <li> <p>我们日常开发中使用的绝大多数软件，都是开源软件（VSCode、PHP、Nginx、MySQL、Redis 等）</p> </li> 
 <li> <p>宇润非常希望能有更多的人可以参与到包括 imi 在内的开源项目中来，为 PHP 生态建设献出一份力！</p> </li> 
 <li> <p>参与开源门槛其实不高，你的使用、反馈、建议、bug 修复、代码贡献等等，才是为开源项目添砖加瓦，我为人人，人人为我，让开源项目能够帮助到更多的人。</p> </li> 
 <li> <p>开源不是免费、白嫖、无私奉献，且用且珍惜……</p> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/yurunsoft/IMI/releases/v2.0.0">https://gitee.com/yurunsoft/IMI/releases/v2.0.0</a></p>
                                        </div>
                                      
</div>
            