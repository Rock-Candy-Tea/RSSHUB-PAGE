
---
title: '携程Apollo(阿波罗）配置中心研究'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b59fb72468964db19bfe000d1cc7779e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 07:49:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b59fb72468964db19bfe000d1cc7779e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">1.Apollo简介</h1>
<p>Apollo配置是携程框架组开源的一个配置中心，其不依赖于Java Sprint，但对Java Sprint支持度良好，并且也支持.net core，是跨界配置中心的成熟大作。</p>
<p>其具有良好的前端界面，能够集中化管理应用不同环境、不同集群的配置，配置修改后能够实时推送到应用端程序，具备规范的管理权限、灰度等特性。</p>
<h1 data-id="heading-1">2.Apollo特点和优势</h1>
<p>Apollo配置中心应用广泛，有大量的用户背书，是较为成熟的一款开箱即用的服务，其具备如下特点和优势。</p>
<p>广告下地址： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fctripcorp%2Fapollo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ctripcorp/apollo" ref="nofollow noopener noreferrer">github</a>。</p>
<ol>
<li>支持不同应用的配置隔离；</li>
<li>支持框架和组件的配置，并可以利用命名空间特性实现应用内的配置继承和覆盖；</li>
<li>支持不同的环境配置，内置四种环境配置；</li>
<li>支持不同的集群或安全区配置；</li>
<li>支持用户赋权管理，用户审核功能，以及日志活动记录；</li>
<li>支持编辑配置和发布配置分离，避免误操作；</li>
<li>支持java和.net sdk客户端，并实现了缓存、离线缓存、推、拉模式，长连接等；</li>
<li>支持分布式部署，以实现高可用；</li>
<li>一个前端管理多种环境的配置；</li>
<li>支持Kubernetes部署，并支持K8s的原生服务发现；</li>
<li>各种大佬背书：广泛用于网易严选、有赞、土巴兔、平安银行、易车、小红书等等等等</li>
</ol>
<h1 data-id="heading-2">3. Apollo 的劣势</h1>
<p>非要说劣势，估计只有一点，架构稍显笨重，其依赖于MySQL、Java，有配置服务、管理服务、服务发现（Eureka 或K8s的Api 服务）、元服务、前端等组成。</p>
<p>对于运维来说，稍微有点重量级。</p>
<h1 data-id="heading-3">4. Apollo 的架构组成</h1>
<p>官网公布的架构图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b59fb72468964db19bfe000d1cc7779e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置服务和管理服务均通过Eureka进行服务的注册工作，通过注册后，使得 元服务可以通过Eureka找到这些服务的地址。</p>
<p>这样客户端和前端在通过访问配置的负载访问元服务后，获取到配置服务和管理服务的地址，就可以进行配置的读取和编写、发布工作了。</p>
<p>各类配置都会落盘到配置DB，使得配置的编写和发布可以很好的进行分离。</p>
<p>通过数据保存到MysQL，配置服务、管理服务在K8s内就可以部署成无状态的服务了。</p>
<p>客户端在拉取到配置后，会在本地缓存一份文件，这样就可以对配置中心形成弱依赖关系，如果配置中心挂了，还有本地的配置可供读写。</p>
<p>不过这块如果部署到K8s内，有点纠结是否还是无状态的服务，我们当然不希望，使用了配置的客户端后，就把自己搞成有状态的服务，这块我没研究清楚。</p>
<h1 data-id="heading-4">5. .net core 客户端访问</h1>
<p>客户端的访问如图所示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52b0e6cc75f441eeb63af5418dd73dbe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码支持也很简单：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"> <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> IHostBuilder <span class="hljs-title">CreateHostBuilder</span>(<span class="hljs-params"><span class="hljs-built_in">string</span>[] args</span>)</span> =>
Host.CreateDefaultBuilder(args)
    .AddApollo(<span class="hljs-literal">false</span>)
    .ConfigureWebHostDefaults(builder => builder.UseStartup<Startup>());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">var</span> <span class="hljs-keyword">value</span> = context.RequestServices.GetRequiredService<IConfiguration>()[key];
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">5. 小结</h1>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            