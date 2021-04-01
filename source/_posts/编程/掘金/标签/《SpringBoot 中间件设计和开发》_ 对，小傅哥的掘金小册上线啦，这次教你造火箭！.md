
---
title: '《SpringBoot 中间件设计和开发》_ 对，小傅哥的掘金小册上线啦，这次教你造火箭！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/760dc29d36d44a95877603a3ffe1ed94~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 19:31:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/760dc29d36d44a95877603a3ffe1ed94~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：小傅哥
<br>博客：<a href="https://bugstack.cn/" target="_blank" rel="nofollow noopener noreferrer">bugstack.cn</a></p>
<blockquote>
<p>沉淀、分享、成长，让自己和他人都能有所收获！😄</p>
</blockquote>
<h2 data-id="heading-0">一、前言</h2>
<p><code>年纪轻轻，为什么要搞中间件开发？</code></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/760dc29d36d44a95877603a3ffe1ed94~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>五年前，香河<code>大厂</code>村，开张大吉。我和弟兄们雄心壮志，坐公交车去面试，谁知道求职不到半个月，每天平均1.3个人挂在八股文造火箭，一年内6个兄弟去了外包。</p>
<p>佛祖保佑！算命的说我是“CRUD搬砖996”，不过我不同意。我认为出来混的，是<code>20K</code>是<code>40K</code>，要由自已决定。</p>
<p>你们跟着我的日子最短，底子最薄，路怎么走，让你们自已挑。</p>
<p>好了，祝你们，在大厂，一帆风顺！ 干杯各位架构师！</p>
<hr>
<p>说到底，为什么要扒开CRUD的表面，深入到核心源码实践学一些中间件开发技能，还不是希望自己对技术栈学习有一定的深度，免得面试时被人忽悠压薪资。就像人家问你：</p>
<ul>
<li>类的代理、反射调用是在什么场景用到的？</li>
<li>自定义注解是怎么和切面一起获取到信息使用的？</li>
<li>你需要的yml配置信息是如何被SpringBoot加载并初始化的？</li>
<li>Bean 是如何被注入到 Spring 容器，提供服务的？</li>
<li>ORM 框架是怎么解决不需要写接口的实现类就能执行CRUD操作的？</li>
<li>扰动函数和数据库路由实现中的数据散列有什么关系？</li>
<li>分布式任务调度与zookeeper配置中心是怎么联动的？</li>
<li>字节码插桩对方法增强怎么拦截程序方法运行时信息？</li>
</ul>
<p><strong>综上</strong>，等等这些技术点可能很多时候你所学到的只能称作为<code>背答案</code>、<code>记结果</code>，因为没有实操所以过后就忘而且也扛不住面试官的接连发问。</p>
<p><strong>那么</strong>，为了让所有对需要对自己技术栈知识加深，拓展相关技能的实战经验，同时也让感兴趣于薪资高的中间件开发的小伙伴，有一个能入门并上手的教程。特此准备了专栏小册<code>《SpringBoot 中间件设计和开发》</code>，欢迎大家加入！</p>
<p><strong>全小册19个章节，包括16个中间件的设计和开发，包括测试案例共30个代码库提供给读者学习使用。小册实现的中间件场景涵盖：技术框架、数据服务、数据组件、分布式技术、服务治理、字节码、IDEA插件七个方面，贯穿整个互联网系统架构中常用的核心内容。非常值得了解、学习、实践到掌握。</strong></p>
<p>💋<code>鉴于作者水平有限</code>，如果书中含有不易理解的内容，一定是作者在编写的过程中缺少必要的描述和严格的校准，感谢把你的意见或者疑问提交给我，也欢迎与我多一些交互，互相进步共同成长。</p>
<h2 data-id="heading-1">二、中间件开发技术</h2>
<p>如果平常只是更多的做一些业务代码的开发，那么接触的技术一般是在各类组件的 API 使用上，以及对不同接口的包装。而中间件开发会涉及到各类框架的源码和原理，以及相应的技术迁移和复用。那么在我们这次中间件的设计和实现中，会学到框架、数据、治理、分布式以及字节码的相关技术栈知识，整体包括如下：</p>
<p><img alt="图 2-1" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8620db7bb9e457c8829ebd08b330ca6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>技术框架</strong>：包括 Spring、SpringBoot 配置加载、自定义注解、扫描注册Bean等，以及 ORM 框架设计原理和实现。这部分技术主要是把开发的中间件与框架结合，开发相应的组件或者包装为各类 SpringBoot Starter 的能力学习。</li>
<li><strong>数据服务</strong>：Mysql、Redis、Elasticsearch，都是数据服务，通常需要开发各类组件对数据服务的使用进行封装，Mysql 我们知道有 JDBC，Redis 我们知道有 Jedis，但 Elasticsearch 有 x-pack 你是否了解。</li>
<li><strong>数据组件</strong>：这类组件的开发就是为了简化对数据服务的使用，Mysql+JDBC+ORM，可以非常方便的使用数据库服务，那么 Elasticsearch  是否也可以做相应的组件研发，让它的查询也能像使用 MyBatis 一样呢？二折页的技术能力就需要对 MyBatis 等 ORM 框架的实现原理熟悉，同时需要了解 JDBC 的概念。</li>
<li><strong>分布式技术</strong>：RPC 框架、注册中心、分布式任务，都是现有互联网分布式架构中非常重要的技术，而对于如何实现一个 RPC 框架，也技术是研发人员要掌握的重点，同时如何使用注册中心、怎么下发分布式调度任务，等等，这些技术的学习能让对现有的框架使用有更深入的认识。</li>
<li><strong>服务治理</strong>：熔断、降级、限流、切量、黑白名单以及对现有方法的非入侵式扩展增强等，都可以成为是服务治理类组件，原本这类技术在早期是与业务逻辑代码融合的，后来逐步被拆解出来，开发成对应的组件。所以我们可以学习到，关于这类组件的包装、集成是如何做的。</li>
<li><strong>字节码&插件</strong>：在互联网的系统应用运维过程中，你一定会接触到各类的监控系统，而很多监控系统是非入侵的全链路监控，那么这些是如何实现的呢？其实它们是基于字节码插桩，对系统方法的增强，采集相应的运行时信息，进行监控的。再到扩展 JVMTI、IDEA 插件开发，都是为了整个研发过程的可持续交付和上线提高交付质量和降低人效的。</li>
</ul>
<p><strong>综上</strong>，这些贯穿整个互联网系统架构中的各类典型中间件，都会在后续章节中陆续讲解出来，它们是如何设计和实现的，一点点带你解开中间件的神秘面纱，让你的技术栈知识也增加一些有深度的并且是可以亲自操作的内容。</p>
<h2 data-id="heading-2">三、中间件设计和实现列表</h2>











































































































<table><thead><tr><th align="center">序号</th><th align="center">图标</th><th>名称</th><th>描述</th></tr></thead><tbody><tr><td align="center">1</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cb4ab75b6984f249ef28a98f84d0697~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>服务治理，统一白名单控制</td><td>解决上线验证风险，白名单特定用户开量验证</td></tr><tr><td align="center">2</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25c5723159d647c5aae7d5787121c717~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>服务治理，超时熔断</td><td>包装超时调用熔断，降低业务系统接入成本</td></tr><tr><td align="center">3</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efc194496acc48c1a0eb3732d20e9099~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>服务治理，调用限流</td><td>包装接口调用限流，降低业务系统接入成本</td></tr><tr><td align="center">4</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c56b4f9b804a48bf9adecf15446b89f7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>服务治理，自定义拦截方法</td><td>不破坏现有方法，增强方法服务能力</td></tr><tr><td align="center">5</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b11cf3d6afc4421f8c5dc2a81c043f58~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>ORM 框架实现</td><td>学习 ORM 框架核心设计，实现简单版 MyBatis</td></tr><tr><td align="center">6</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c21b320a85ea40f19476aa569a6954fa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>ORM 框架与 Spring 集合</td><td>熟悉 Bean 扫描、代理、注册、管理等，以及对 ORM 的包装</td></tr><tr><td align="center">7</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b428727cdc484cd8ac79b37173cf38f2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>结合 SpringBoot 开发 ORM Starter</td><td>ORM、Spring 与 SpringBoot 结合，自动化记载初始配置，开发 Starter</td></tr><tr><td align="center">8</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e529d2567a294377a788d236fa755d73~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>ES-JDBC 查询引擎</td><td>了解 Elasticsearch JDBC 组件的源码实现，x-pack-jdbc</td></tr><tr><td align="center">9</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b524d1446b764b6bbd38d416af6b7692~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>ES SpringBoot Starter 服务框架</td><td>运用 ORM 技术迁移，开发 ES 类的 ORM 框架，解决查询映射复杂性，做面向对象开发包装</td></tr><tr><td align="center">10</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a710cfc5bcf4916baafe4f86ba75c6e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>RPC 框架实现</td><td>学习 RPC 框架的设计和开发，了解通信原理和实现</td></tr><tr><td align="center">11</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9da969f9ed834c59a1f0a41a33d48016~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>数据库路由组件</td><td>把散列算法、切面处理、数据源切换、自定义配置结合在一起实践，开发路由组件</td></tr><tr><td align="center">12</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f80355775d14f7ba5d4fd0754165fb1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>Redis 简化使用封装</td><td>处理 Redis 的二次包装，简化为接口代理方式使用，降低应用成本，以及增加升级容易度</td></tr><tr><td align="center">13</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e65c3d651c354949a263c93950ac8015~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>分布式任务调度</td><td>在注册中、任务、控制台，多方内容组合下开发分布式任务调度</td></tr><tr><td align="center">14</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8f1a47897524e3aaa3937cac7543990~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>非入侵监控设计，ASM 字节码插桩</td><td>了解字节码插桩技术，学习 Javaagent 处理的非入侵监控方式</td></tr><tr><td align="center">15</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdf46e9dde3644a2a023123bbfd25474~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>非入侵监控设计，JVMTI 定位代码</td><td>了解 JVMTI 的技术能力，开发 C++ dll 组件，增强监控能力</td></tr><tr><td align="center">16</td><td align="center"><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3adb5909ec02404fb7b70e35c3e553d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></td><td>IDEA插件与字节码插桩结合</td><td>结合 IDEA 插件开发与字节码增强技术，采集代码研发运行过程中的执行信息，分析和提升交付质量</td></tr></tbody></table>
<hr>
<p><strong>小册16个中间件实现，包括测试工程等共计30个代码库</strong>，每一章节都会对应有一个中间件的设计和实现，为了便于读者快速有效的学习小册中的技术内容，这里介绍下小册中章节的内容结构，涵盖以下5方面内容：</p>
<ol>
<li><strong>开篇引导</strong>，在技术、经验、成长等各方面汇总的内容，帮助大家扩宽知识面和增加成长经验。</li>
<li><strong>需求背景</strong>，讲述此中间件会因为什么场景、什么需求下用于解决什么痛点而提出的。</li>
<li><strong>方案设计</strong>，针对需求背景的痛点问题，做中间件架构方案设计，包括设计图稿和实现描述。</li>
<li><strong>技术实现</strong>，主要是对方案设计的具体实现落地，这个过程会包括完整的实现源码以及所有核心代码的讲解。保证大家在学习的过程中也能完成中间件的设计和开发。</li>
<li><strong>测试验证</strong>，每一个中间件的实现都有一个对应的测试工程，例如：<code>whitelist-spring-boot-starter</code> 与 <code>whitelist-spring-boot-starter-test</code>。通过测试工程对中间件实现预期的验证，可以让大家更加容易的理解一个需求的背景、设计、实现到交付验证的过程。</li>
<li><strong>文末总结</strong>，是对每一篇文章的概要汇总，也是给读者在文末针对此篇文章的学习的一个帮助提醒，也希望你学到的信息要远比站在作者视角总结的内容还要完善。</li>
</ol>
<h2 data-id="heading-3">四、你会学到什么？</h2>
<ul>
<li>Spring 对配置文件的加载、Bean 扫描、定义、注册等</li>
<li>Spring Boot 关于 Starter 开发的常用技术手段和技巧</li>
<li>ORM、RPC、数据库路由、服务治理、系统监控、IDEA插件等各类场景下的中间件设计</li>
<li>类的代理、反射调用、切面处理、字节码插桩、扰动函数增强散列以及JVMTI等核心技术的实际运用</li>
<li>30个代码库让你对中间件的设计、实现、验证，有清晰的认识</li>
</ul>
<h2 data-id="heading-4">五、适宜人群</h2>
<ul>
<li>具备 Java 编程基础的研发人员，略懂部分框架源码，经常使用各类技术组件</li>
<li>需要提升个人的核心技术能力</li>
<li>对中间件开发感兴趣，但不知道从哪入手</li>
<li>有在 SpringBoot 开发 Starter 的技术需求</li>
</ul>
<h2 data-id="heading-5">六、📚小册购买优惠</h2>
<p><a href="https://juejin.cn/book/6940996508632219689" target="_blank">《SpringBoot 中间件设计和开发》</a>掘金专栏小册首发<code>8折</code>，涵盖19章和一套章节内容对应的完整代码库，购买后可以按照小册第二节说明进行使用。</p>
<h3 data-id="heading-6">1. 可获得内容包括</h3>
<ol>
<li><a href="https://juejin.cn/book/6940996508632219689" target="_blank">《SpringBoot 中间件设计和开发》</a> 专栏小册完整阅读权限</li>
<li>30组对应的代码库一套，可以随时交流讨论提交 issues</li>
<li>可以加入专栏小册交流群，添加我的微信：fustack 备注：<code>中间件加群</code></li>
</ol>
<h3 data-id="heading-7">2. 购买方式</h3>
<ol>
<li>点击或复制链接：<a href="https://juejin.cn/book/6940996508632219689" target="_blank">juejin.cn/book/694099…</a></li>
<li>公众号读者，阅读原文直接进入购买链接</li>
<li>添加专栏作者<code>小傅哥</code>微信：<code>fustack</code>，备注购买小册
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85462cbdf76146489378e3ca759b2519~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
<li>扫描二维码限时8折购买，也可以保存下来珍藏哦
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1368b1dba34341749269da748c5d027b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ol>
<h2 data-id="heading-8">七、🎁粉丝抽奖</h2>
<p><code>牛吹完了，接下来回馈粉丝一波奖品，感谢一直依赖对小傅哥的支持。</code></p>
<ol>
<li>礼品包括</li>
</ol>
<ul>
<li>一等奖、书籍[3名]：了不起的程序员、Head First Java、JavaScript 高级程序设计</li>
<li>二等奖、玩具[3名]：象棋、公仔、小颗粒玩具</li>
<li>三等奖、水杯[10名]：掘金赞助的搪瓷杯，很有程序员风格，摆在桌子上很能吸引测试小姐姐</li>
</ul>
<p><em>赞赏内的钱💰当做邮费使用，超出部分进小傅哥裤兜了。嘿嘿，当做红包雨露均沾给大家！🎁</em></p>
<ol start="2">
<li>得奖规则</li>
</ol>
<p>在本公众号：bugstack虫洞栈，活动原文中 <a href="https://mp.weixin.qq.com/s/zSM3ahTC0yqbB-_mmuGvHA" target="_blank" rel="nofollow noopener noreferrer">mp.weixin.qq.com/s/zSM3ahTC0…</a>。对文章进行<code>留言并转发朋友圈</code>。以个人留言<code>被读者点赞数量</code>为排名，仅记录个人攒点最高的留言。</p>
<ol start="3">
<li>活动说明</li>
</ol>
<ul>
<li><strong>时间范围</strong>：2021-04-01 07:55:00 - 2020-04-02 23:59:59，共计2天计票</li>
<li><strong>公布时间</strong>：2021年04月06日，星期二，节日后</li>
<li><strong>公布方式</strong>：小傅哥的朋友圈公布，<em>记得添加小傅哥微信：<code>fustack</code></em></li>
<li><strong>领奖方式</strong>：看到小傅哥朋友圈后，主动联系小傅哥。提供；收获人、收获地址、手机号等必要信息。<em>😄嘿...嘿，我会保密的你的信息！</em></li>
</ul>
<h2 data-id="heading-9">八、🎉收尾感谢</h2>
<p>谢谢掘金平台和运营<code>优弧</code>对小册校对审核到上架的帮助，谢谢<code>粉丝伙伴</code>对小傅哥技术内容的认可和期待，也谢谢家人在过年和周末期间给我提供的时间<code>只干饭不洗完😄哈哈哈哈，专心码文章</code>。</p>
<p><strong>好嘛</strong>，就是在大家的帮助、支持、认可、鼓励中，你希望看到的<code>中间件设计和开发</code>小册和大家见面了！这是一个程序员成长阶段突破技术瓶颈和提升技术认知，都应该了解和学习的内容，加油！<em>记住在专栏学习过程中遇到任何问题，请联系这个优秀的男人：小傅哥，微信：fustack</em></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            