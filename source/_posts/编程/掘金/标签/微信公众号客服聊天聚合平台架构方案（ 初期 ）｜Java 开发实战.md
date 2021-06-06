
---
title: '微信公众号客服聊天聚合平台架构方案（ 初期 ）｜Java 开发实战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/593ed37848574ca98838439260cb26b5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 14:57:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/593ed37848574ca98838439260cb26b5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文正在参加「Java主题月 - Java 开发实战」，详情查看 <a href="https://juejin.cn/post/6968267217121050660/" target="_blank">活动链接</a></p>
</blockquote>
<p>现实业务环境中，由于微信团队并未提供对公众号客服系统的聚合。使得许多商家在选用云服务商提供的聚合平台还是基于团队自行开发的问题上进行抉择。</p>
<p>接下来我们将分别讨论：</p>
<h2 data-id="heading-0">云服务商聚合平台</h2>
<p>使用云服务商的聚合平台最大的优势便是节省了工作量。你只要给钱，云服务商就会给你提供 "一篮子" 解决方案。通常云服务商会按照客服座席来收费。有的可能还会有一些特殊的技术服务费。</p>
<blockquote>
<p>座席：即每个客服所使用的账号，一般来说一个座席对应一个客服。</p>
</blockquote>
<h2 data-id="heading-1">基于团队自行开发</h2>
<p>微信开放平台提供了该功能，微信官方文档 <a href="https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Service_Center_messages.html" target="_blank" rel="nofollow noopener noreferrer">客服消息</a> 模块中有相关接口文档。我们可以基于此接口来开发自己的聚合平台。并实现自定义拓展等。</p>
<h2 data-id="heading-2">如何选择 ？</h2>
<p>在这么多的解决方案中，我们需要综合自身企业情况进行取舍。如果你是一个比较小的企业，需要快速且实用的接入自己的公众号聊天系统， 那么你可以采用云服务商提供的聚合平台，但是它的缺点是显而易见的。随着客服人员的增多，服务费会越来越高。并且也不能完美的兼容自己的业务系统， 实现更加方便的功能。如果有一定的经济实力和时间基础，那么你可以考虑基于团队自行开发。这样你就控制了整个系统，你可以做任何你想做的事情。
也不会有客服人数的限制。</p>
<h2 data-id="heading-3">基于团队自行开发聚合平台架构</h2>
<p>下面我们将讲一下如何基于团队自行开发聚合平台。</p>
<h3 data-id="heading-4">平台</h3>
<ul>
<li>后台管理平台 - 用于参数配置、数据分析展示等。</li>
<li>客服聊天平台 - 基于腾讯 IM 平台提供的聊天平台，进行二次开发。</li>
<li>开发者服务 - 用于对消息进行转接与转发，实现自定义功能。</li>
</ul>
<h3 data-id="heading-5">相关技术与中间件</h3>
<p>由于我们为了节省时间与人力物力，我们使用了腾讯云平台的 IM 平台来作为部分实现。</p>
<ul>
<li>前端开发语言 - Vue.js 全家桶</li>
<li>管理平台前端框架 - Layui</li>
<li>后端开发语言 - Java</li>
<li>日志框架 - Log4j2</li>
<li>后端服务框架 - Spring Boot</li>
<li>后端权限验证 - Spring Security</li>
<li>后端 ORM 框架 - Mybatis Dynamic</li>
<li>反向代理 - Kong Gateway</li>
<li>消息队列 - RabbitMQ</li>
<li>缓存 - Redis</li>
<li>数据库 - Mysql</li>
</ul>
<h3 data-id="heading-6">外部接口服务</h3>
<ul>
<li>微信官方文档（ 公众号 ） ( <a href="https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Service_Center_messages.html" target="_blank" rel="nofollow noopener noreferrer">developers.weixin.qq.com/doc/offiacc…</a> )</li>
<li>腾讯 IM 平台 ( <a href="https://cloud.tencent.com/document/product/269" target="_blank" rel="nofollow noopener noreferrer">cloud.tencent.com/document/pr…</a> )</li>
</ul>
<blockquote>
<p>本篇文章仅仅讲解架构思路，并不涉及源代码等实现。</p>
</blockquote>
<h2 data-id="heading-7">整体架构思路</h2>
<p>贴一张我从腾讯云 IM 平台 "借鉴" 来的最佳实现图。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/593ed37848574ca98838439260cb26b5~tplv-k3u1fbpfcp-watermark.image" alt="img_31.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>依照此图片，我们可以看出，我们只需要作为两端外部 API 接口服务中间的 < 开发者服务器 >，来实现我们的自定义逻辑处理。</p>
<h3 data-id="heading-8">简单的实现 - 微信端</h3>
<p>首先，我们需要对接微信公众号平台接口的接收消息与发送消息,他们分别是 <a href="https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Receiving_standard_messages.html" target="_blank" rel="nofollow noopener noreferrer">微信公众号 - 接收普通消息</a>
和 <a href="https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Service_Center_messages.html" target="_blank" rel="nofollow noopener noreferrer">微信公众号 - 客服消息</a>
。</p>
<h4 data-id="heading-9">接收普通消息</h4>
<p>想要接收普通消息，我们需要绑定微信的服务器配置。</p>
<blockquote>
<p>路径为公众号管理平台 - 设置与开发 - 开发 - 基本配置。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8dd2689ae7d46ccb6fc57784e0b090a~tplv-k3u1fbpfcp-watermark.image" alt="img_33.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当启动该服务器配置以后，微信将会把接收到的消息转发给服务器地址。你只需要根据文档对接即可。</p>
<blockquote>
<p>坑1：微信在通知时，不仅仅将消息进行通知。也将一些点击事件等进行通知。所以要做好过滤。</p>
</blockquote>
<h4 data-id="heading-10">发送客服消息</h4>
<p>在发送时我们则需要调用微信公众号的相关接口，参照 API 文档的消息格式进行发送。</p>
<h3 data-id="heading-11">简单实现 - Tencent IM端</h3>
<h4 data-id="heading-12">接收消息</h4>
<p>在 Tencent IM 平台的 <a href="https://console.cloud.tencent.com/" target="_blank" rel="nofollow noopener noreferrer">管理页面</a>  配置回调的连接和相关回调事件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e29fe50fc9443c1a237cac49fbc6fd9~tplv-k3u1fbpfcp-watermark.image" alt="img_34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">发送消息</h4>
<p>调用 Tencent IM 平台服务端 API 的<code>单发单聊</code>接口进行消息发送。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d055f5b3db1e412283a05a72d892978c~tplv-k3u1fbpfcp-watermark.image" alt="img_35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">实现中间转接服务</h2>
<p>现在两端的接口我们已经对接成功，接下来我们将讨论如何实现基本的桥接功能和其他自定义功能。</p>
<h3 data-id="heading-15">架构图</h3>
<p>我们采用基于命令的模式来实现类似于机器人的插件（ 没错，想法从 Slack 里面抄的 🤪 ）, 从而实现基本的会话管理、消息转发、用户排队等基本功能。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a4c474582eb4cda84595fbcaeb1cc69~tplv-k3u1fbpfcp-watermark.image" alt="img_36.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">Filters</h4>
<p>基于过滤器模式，实现一个消息进入系统时必须做的的事情。</p>
<ul>
<li>Decode filter ：用于对微信或腾讯端加密的请求进行解密。</li>
<li>Conversation Filter ：用于第一次的会话创建等。</li>
<li>Command Parse Filter ：对于命令模式 <code>#Trasfor -n system</code> 进行分析，解析出<code>Transfor</code>命令和参数<code>n</code>，它的值为<code>system</code>。</li>
<li>Chat Bot Filter：基于会话现在处于的命令状态采用策略模式，获取相应的处理机器人对该消息进行处理。</li>
</ul>
<h4 data-id="heading-17">ChatBots</h4>
<ul>
<li>Transform ChatBot ：对新来的用户进行分配客服。（ 可选一些权重算法等 ）</li>
<li>Send ChatBot - 基础通信机器人，解析获取到的信息然后利用相应的<code>Convertor</code> 进行转换。例如微信来的消息，我们将使用<code>WechatCallback2TencentMsgConvertror</code> 将微信的回调消息转换为符合腾讯接口的请求，从而实现转发。</li>
<li>Stack ChatBot - 根据每个客服的接待上线实现排队处理。</li>
<li>Qui ChatBot - 退出命令模式</li>
</ul>
<h3 data-id="heading-18">一些其他功能的实现</h3>
<h4 data-id="heading-19">聊天上下文</h4>
<p>由于腾讯 IM 平台未提供转发用户提供上下文的功能，但是我们也不想花那么多的钱去存储聊天记录，于是就想了一个办法。</p>
<p>在 Redis 内构建一个限长的队列，记录最后 n 条消息。当客服进行转接的时候，系统将该消息统一重发给被转接的客服，从而实现上下文功能。并随着会话的关闭而删除。</p>
<h2 data-id="heading-20">总结</h2>
<p>本章简单的介绍了一下微信公众号客服聊天聚合平台架构的方案。并且采用多种设计模式来进行解耦。虽然仅仅实现了基本的功能，但整体框架已经搭建完善，剩下的就可以利用<code>ChatBot</code>的插件模式进行扩展即可。</p></div>  
</div>
            