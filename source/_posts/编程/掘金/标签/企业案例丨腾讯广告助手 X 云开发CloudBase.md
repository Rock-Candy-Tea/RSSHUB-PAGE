
---
title: '企业案例丨腾讯广告助手 X 云开发CloudBase'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa1f8dedc930407d8f1871c7c4ef6fad~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 23:22:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa1f8dedc930407d8f1871c7c4ef6fad~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>腾讯广告(ad.qq.com)是一站式广告投放平台，坐拥腾讯生态流量，拥有丰富统一的投放能力，广告主在该平台上可以进行微信、QQ、腾讯联盟、应用宝、手机QQ浏览器等渠道的广告投放。</p>
<p>本文讲介绍腾讯广告如何结合云原生一体化开发平台~云开发 CloudBase，发布了“腾讯广告助手”小程序端，实现降低广告主盯盘成本、提高广告优化效率的目标。</p>
<h2 data-id="heading-0"><strong>一、项目背景</strong></h2>
<p>为了降低广告主盯盘成本、提高广告优化效率，腾讯广告基于这一痛点，在云开发 CloudBase 能力的帮助下，发布了“腾讯广告助手”小程序端，提供多账户登录与切换功能、直观的数据报表、轻量化的操作和及时的新消息提醒，为广告主、服务商打造整合式的移动端优化管理解决方案，帮助广告主实现更高效便捷的广告管理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa1f8dedc930407d8f1871c7c4ef6fad~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1"><strong>二、架构设计</strong></h2>
<h4 data-id="heading-2"><strong>1、业务架构设计</strong></h4>
<p>“腾讯广告助手作为一款腾讯广告投放平台的工具，希望为广告主提供在移动设备上管理广告的能力。所以在小程序端里面，我们为广告主提供了 PC 端上的基础能力及高频使用的功能，业务功能设计如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cea089de55d745aaa6c9d27f406b02ad~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3"><strong>2、技术架构设计</strong></h4>
<p>腾讯广告投放服务主要是通过开放平台的MKT API (对外) 和 GDT API (对内) 提供服务，在小程序端引入 <strong>CloudBase 的云函数作为 BFF</strong> (Backend For Frontend) 层，调用层级如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1bc8e2217814a34b2340e8403aebc2a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>整体上来说，BFF 是一层设计来满足在特定客户端场景的API，它能够将多个后端微服务通过聚合、裁剪和编排等方式将处理后的数据提供给客户端使用，至于产品业务的功能、数据模型等则应该收敛在后台 API 实现，不落地在 BFF 中。</p>
<p>在项目立项前，团队就对多种小程序开发框架进行了对比，从性能、开发效率和稳定性等方面比较后，最终采用了<strong>原生开发框架配合云开发服务</strong>，理由如下：</p>
<ul>
<li>对于小程序端有较强的性能要求，无论是第三方框架的编译还是运行时方案，在健壮性和性能上，原生的小程序开发模式都相对更适合；</li>
<li>我们的小程序端无需支持多个不同小程序端，而且也没有历史代码迁移包袱，使用原生开发与第三方框架开发成本差别不大；</li>
<li>对于原生开发与使用框架在开发体验上的差异，如小程序不支持 less 等，后续采用前端工程化手段解决。</li>
</ul>
<p>目前使用到的技术栈如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7982a5aad86c49eb89c0567020f61df4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4"><strong>三、云开发 CloudBase 的应用及实践</strong></h2>
<h4 data-id="heading-5"><strong>1、聚合接口</strong></h4>
<p>在小程序开发初期，对是在小程序前端直接调用中台服务，随之而来遇到了些问题，例如对于某些页面或功能，需要调用多个接口获得数据后，再拼接成最终需要的数据。这个逻辑如果是在前端来做的话，那么就加大了整个请求的调用链路，是多个客户端到服务端的请求，如果有一个数据请求慢了或失败了，那么都会影响到最终的数据，比较影响用户体验。而如果放到 BFF 层上来做，那么则变成是1个客户端到服务端的请求和多个服务端到服务端的请求，调用链路相比小程序前端请求要短许多，而且稳定性更好。</p>
<p>在”腾讯广告助手“小程序上展示的报表数据会包含汇总、环比、同比等数据，那么就需要组合调用不同的中台接口才能获取到最终的数据。所以，团队将小程序上的报表相关的接口<strong>切换到直接调用云函数</strong>，由云函数并发调用中台服务接口并将数据做聚合返回到小程序端。同时对返回的数据按照小程序端所需要的按需返回。比如对于账户列表页面的请求，原先前端需要并发进行3个请求才能获取到最终的数据，而<strong>通过云函数，则小程序端只需调用一个接口</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef3cf48518804989b885c05b2e38a356~tplv-k3u1fbpfcp-watermark.image" alt="拉取报表数据的云函数运行数据" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/958e0d87e76d4956ab3aeb409b9887cd~tplv-k3u1fbpfcp-watermark.image" alt="聚合后云函数接口请求耗时数据" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6"><strong>2、提升云函数的开发体验</strong></h4>
<p>目前 CloudBase 上官方是推荐以层来管理公共依赖库和代码问题，但是从开发的角度来看，还是希望能够做到源码本地依赖，减少引入更多的概念及操作成本。</p>
<p>抽离公共代码通常需要将代码上移到公共目录或者发布成 npm 包，而在小程序的云函数中，每个云函数就是一个独立的目录，没有公共目录。而如果采用 npm 包的方式，那么调试，发布和更新版本号等操作上的成本就比较大了。</p>
<p>于是我们将公共代码抽离到项目内单独的目录中，同时在开发和代码构建时，通过构建工具实时同步公共代码到每个云函数的目录中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a261a83381d4e8b975668646abea668~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时，团队在项目内基于 <strong>cloudbase-manager-node sdk</strong> 实现了云函数本地的模板创建、代码及配置更新、查询状态等，提升开发体验。</p>
<p>查看云函数状态：</p>
<pre><code class="copyable">npm run cf:list
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实时更新代码并部署到指定的环境：</p>
<pre><code class="copyable">npm run cf:watch -- --func=getUserInfo,mktapi --env:preview
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7"><strong>3、多环境部署及蓝绿发布方案</strong></h4>
<p>”腾讯广告助手“的云开发环境目前有5个，分别对应主环境、备环境、测试环境、研发环境和预发布环境，在开发的时候可以通过命令行指定代码编译时连接是哪个环境，比如：</p>
<pre><code class="copyable">npm run dev -- --cloudEnv=development
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们的小程序就会连接到云开发的开发环境，同时在小程序页面的悬浮球上也会显示连接对应的环境。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb767bf1b0774d22902b2f64de43b385~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于云函数的发布，采用的是蓝绿发布策略。主环境和备环境同时在外网可用，每当发布的时候，就会将流量从一边逐渐切换到另外一边，若没有问题再逐步全量，大致流程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ac4e0760a18423b8c8fdc6193fd4840~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的流量切换逻辑，可以通过小程序发布时的按微信号灰度策略来控制，同时也可以通过在小程序上使用特性开关来控制。</p>
<h2 data-id="heading-8"><strong>四、项目总结及成果</strong></h2>
<h4 data-id="heading-9"><strong>1、影响力</strong></h4>
<p>”腾讯广告助手“小程序自2020年5月底上线以来，使用人数不断攀升。</p>
<p>同时从下图中可以看到，小程序端很好的弥补了上班高峰时段及下班后广告主不在电脑旁边的场景。有了小程序端，广告主可以随时管理广告。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1a8d4805f734874a48432e18457a3ab~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10"><strong>2、使用云开发 CloudBase 的收益</strong></h4>
<p>借助云开发能力，”腾讯广告助手“小程序项目获得了许多收益，包括：</p>
<ul>
<li>云函数提供了私有的传输协议，为数据传输提供了保障；</li>
<li>提升了整体的开发效率，能够在人力成本有限的场景下完成需求的开发；</li>
<li>通过集成 cloudbase-node-sdk 实现了一键部署，同时也免去了运维成本，无需考虑负载问题；</li>
<li>云开发方式给联调带来了极大的便利性，无需再去配置代理；</li>
<li>云开发提供了完整的生态及强大的监控体系。</li>
</ul>
<h2 data-id="heading-11">参考</h2>
<p>开通云开发：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fconsole.cloud.tencent.com%2Ftcb%3Ftdl_anchor%3Dtechsite" target="_blank" rel="nofollow noopener noreferrer" title="https://console.cloud.tencent.com/tcb?tdl_anchor=techsite" ref="nofollow noopener noreferrer">console.cloud.tencent.com/tcb?tdl_anc…</a></p>
<p>产品文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Ftcb%3Ffrom%3D12763" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/product/tcb?from=12763" ref="nofollow noopener noreferrer">cloud.tencent.com/product/tcb…</a></p>
<p>技术文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloudbase.net%3Ffrom%3D10004" target="_blank" rel="nofollow noopener noreferrer" title="https://cloudbase.net?from=10004" ref="nofollow noopener noreferrer">cloudbase.net?from=10004</a></p></div>  
</div>
            