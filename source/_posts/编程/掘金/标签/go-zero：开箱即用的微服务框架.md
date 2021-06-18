
---
title: 'go-zero：开箱即用的微服务框架'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1aa76619efea4348bd38c8e0b9b5fcb9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 18:44:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1aa76619efea4348bd38c8e0b9b5fcb9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>go-zero 是一个集成了各种工程实践的 Web 和 rpc 框架，它的弹性设计保障了大并发服务端的稳定性，并且已经经过了充分的实战检验。</p>
<p>go-zero 在设计时遵循了 “工具大于约定和文档” 的理念，所以 go-zero 包含极简的 API 定义和生成工具 goctl，可以根据定义的 API 文件一键生成 Go、iOS、Android、Kotlin、Dart、TypeScript、JavaScript 代码，并可直接运行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1aa76619efea4348bd38c8e0b9b5fcb9~tplv-k3u1fbpfcp-zoom-1.image" alt="go-zero 的架构图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，不同客户端的请求都会先进入 go-zero 的 API 端。API 端最主要的作用是通过 ETCD 将对应的请求通过 gRPC 协议转发到 Service 端。根据请求的具体内容，Service 端负责对数据进行查询或存储。如果是查询请求，go-zero 有内置的 API 会先查询缓存层，减少数据库的查询压力。</p>
<p>由图可见，API 端和 Service 端中框架已经内置了非常丰富的功能，在开发过程中只需要我们填充对应的业务逻辑，即可轻松实现 CRDU 级的需求。</p>
<p>我们为什么说 go-zero 是开箱即用的微服务架构呢？不急，我们来盘点下 go-zero 中有哪些强大的特性。</p>
<h2 data-id="heading-0">go-zero 适合做微服务快速开发的特性</h2>
<p>Go-zero 拥有强大的项目脚手架工具 goctl。 goctl 和前端中的 Vue-cli、React-cli 一样方便。goctl 通过配置文件可以生成 API、rpc 和 model 等相关代码。 同时，go-zero 拥有较完备的项目框架。脚手架生成的项目框架足以应对常见的需求。CRDU 等需求只需要做 “填空题”，在已生成的代码上填充必要的业务逻辑。 其他缓存鉴权等需求，框架中也早已内置。</p>
<p>另外，go-zero 拥有独特的“渐进式”框架。“渐进式”是前端 Vue 框架的一大特性，大意是“易于上手，还便于与第三方库或既有项目整合”。本文借用这个概念是想表明 go-zero 对项目的入侵性较少，go-zero 生成的代码可以拆开使用，逐步对老项目进行改造。</p>
<p>低耦合的模块设计，丰富的中间件，插件和工具：</p>
<ul>
<li>
<p>go-zero 中各模块耦合程度低，我们可以通过文档中的组件中心寻找合适的中间件或自研中间件。</p>
</li>
<li>
<p>如果觉得 goctl 不能满足需求，goctl 还支持 plugin 命令对 goctl 进行扩展。</p>
</li>
<li>
<p>go-zero 的很多配置文件是自定义语法。 go-zero 还提供了 intellij 和 vscode 插件，提供了语法高亮错误检查等编辑增强功能。</p>
</li>
</ul>
<h2 data-id="heading-1">goctl 介绍</h2>
<p>goctl 是 go-zero 微服务框架下的代码生成工具。使用 goctl 可显著提升开发效率，让开发人员将时间重点放在业务开发上。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71432380260843e4b98d9fb20f78ea08~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>goctl 的命令可归纳为如下几类：</p>
<ul>
<li>
<p>API 命令，快速生成一个 API 服务</p>
</li>
<li>
<p>rpc 命令，支持 proto 模板生成和 rpc 服务代码生成</p>
</li>
<li>
<p>model 命令，目前支持识别 mysql ddl 进行 model 层代码生成</p>
</li>
<li>
<p>plugin 命令，支持针对 API 自定义插件</p>
</li>
<li>
<p>其他命令，目前是发布相关</p>
</li>
</ul>
<p>goctl 的命令众多，本次涉及到的只是其中 API、rpc 和 model 相关的基础命令。</p>
<p><strong>使用 goctl 的基本流程</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8ce9bc0782249d7b4222c9e3ba220e6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用 goctl 生成代码的流程大致可以分为 4 步：</p>
<ul>
<li>
<p>使用命令 a 生成默认的配置文件；</p>
</li>
<li>
<p>按照业务需求编辑该配置文件；</p>
</li>
<li>
<p>使用命令 b 按照配置文件生成默认的代码文件；</p>
</li>
<li>
<p>按照业务逻辑填充对应的代码文件。</p>
</li>
</ul>
<h2 data-id="heading-2">什么情况不适宜使用 go-zero 做微服务快速开发？</h2>
<p>看完上面的介绍，想必大家对于 go-zero 开发微服务已经有点跃跃欲试了吧。不过经过一番实践，我认为当出现以下情况时，不适宜采用 go-zero 作为开发微服务的框架。</p>
<p><strong>当前需求与 goctl 的理念相冲突</strong></p>
<p>go-zero 的一大卖点是脚手架工具 goctl，如果定制需求过多可能与 goctl 生成的代码相冲突。但是如果放弃 goctl 手动编写代码的话，开发效率会大大降低。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06263e4d69e048fdac1881581021e88e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>举个例子，如上图所示，go-zero 在 Service 端目前只支持 gRPC，在数据库层只支持 Mysql、MongoDB 和 ClickHouse，服务发现只支持 ETCD。在这种情况下如果想实现 PostgreSQL 替换 Mysql、Consul 替换 ETCD 等定制操作，goctl 生成的代码执行时很可能会出现异常。</p>
<p><strong>希望框架提供的功能非常完善</strong></p>
<p>go-zero 大部分组件是自研，比如 sqlx，httpx 等。这些自研组件满足 CRDU 的操作绰绰有余，但是与 gorm、gin 等专攻某一方向的开源项目相比还是有非常大的差距的。</p>
<p>所以随着公司业务发展需求越来越五花八门，当前的主要矛盾从“快速开发”变成“精细化开发”时，会发现该框架有这样或那样的不足。这种情况下就需要提 RP 或自己 fork 一份魔改了。个人觉得这种情况比 Spring 或 Django 那样一个“全家桶” 改动起来要省力省心。</p>
<h4 data-id="heading-3">推荐阅读</h4>
<p><a href="https://www.upyun.com/tech/article/640/%E5%AE%9E%E6%93%8D%E7%AC%94%E8%AE%B0%EF%BC%9A%E4%B8%BA%20NSQ%20%E9%85%8D%E7%BD%AE%E7%9B%91%E6%8E%A7%E6%9C%8D%E5%8A%A1%E7%9A%84%E5%BF%83%E8%B7%AF%E5%8E%86%E7%A8%8B.html" target="_blank" rel="nofollow noopener noreferrer">为 NSQ 配置监控服务的心路历程</a></p>
<p><a href="https://www.upyun.com/tech/article/620/Flink%20%E5%9C%A8%E5%8F%88%E6%8B%8D%E4%BA%91%E6%97%A5%E5%BF%97%E6%89%B9%E5%A4%84%E7%90%86%E4%B8%AD%E7%9A%84%E5%AE%9E%E8%B7%B5.html" target="_blank" rel="nofollow noopener noreferrer">Flink 在又拍云日志批处理中的实践</a></p></div>  
</div>
            