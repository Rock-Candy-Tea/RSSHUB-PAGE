
---
title: 'ReactNative在游戏营销场景中的实践和探索-集成'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24eb8980098c4b3bb66c843fdd683e0a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 23:03:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24eb8980098c4b3bb66c843fdd683e0a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>作者：字节游戏中台客户端团队 - 熊文源</strong></p>
<p>客户端跨端框架已经发展了很多年了，最近比较流行的小程序、Flutter、ReactNative，都算是比较成功、成熟的框架，面向的开发者也不一样，很多大型App都广泛的使用了，笔者有幸很早就参与学习使用了这些优秀的跨端方案，在这几年的开发和架构设计中，除了在App中支撑了千万级DAU，也慢慢将ReactNative跨端方案运用到了游戏，来提升开发、迭代效率。本次文章我们会分5个章节介绍我们在游戏中的一些探索和实践，相信大家也能从中有所收获：</p>
<ul>
<li><strong><a href="https://juejin.cn/post/7000628820814331918" target="_blank" title="https://juejin.cn/post/7000628820814331918">第一篇：游戏中使用ReactNative的背景介绍</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000630849402044453" target="_blank" title="https://juejin.cn/post/7000630849402044453">第二篇：简介游戏中怎么集成ReactNative</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000631869628743688" target="_blank" title="https://juejin.cn/post/7000631869628743688">第三篇：简介游戏中的ReactNative性能优化</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000632245824258079" target="_blank" title="https://juejin.cn/post/7000632245824258079">第四篇：ReactNative Hermes引擎简介</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000634295668703246" target="_blank" title="https://juejin.cn/post/7000634295668703246">第五篇：ReactNative 新架构介绍</a></strong></li>
</ul>
<p>（本篇为系列第二篇）</p>
<p>上面章节已经聊过游戏环境和App的差异了，也是因为这些特殊性，我们最初的方案采用了ReactNative，官方标准的设计和脚手架工程可以帮助我们很好的搭建一个App，可以帮助开发者在不需要有原生客户端开发的经验的情况下，生成跨端的App。但游戏不一样，拿Unity的游戏来说，游戏的打包、开发环境是Unity的IDE，另外游戏的页面是自渲染的，如何在游戏中显示原生的UI，这些都是要解决的问题，总结下来要在游戏环境中运行ReactNative，要解决几个问题：</p>
<ol>
<li>
<p>工程化，快速支持ReactNative的调试和集成</p>
</li>
<li>
<p>ReactNative页面容器，承载并管理ReactNative页面</p>
</li>
<li>
<p>支持热更新服务，支持灵活、快速上线业务</p>
</li>
</ol>
<p>因整体原理不复杂，很多文章也做了很详细的介绍，下面就简单说在游戏中的一些差异和思路：</p>
<ol>
<li>
<h2 data-id="heading-0"><strong>工程化</strong></h2>
</li>
</ol>
<ul>
<li>在游戏中引入原生端的组件库都是以plugin方式集成，所以首先要将引擎作为一个Module、Plugin集成到游戏中，拿Android举例，将ReactNative sdk封装成独立的aar module，在游戏中引入这个aar作为Plugin，游戏的Native代码能访问我们aar plugin，这点和原生开发其实是一致的</li>
<li>在游戏中很多页面和游戏都是游戏中实现的，所以还需要解决游戏调用native code问题，比如我们需要在游戏中的某个按钮打开ReactNative页面，拿unity来说，就要实现c#代码到ReactNative代码的调用，这里要封装一层bridge，这些都是标准的游戏API，具体可以参考《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_15585751%2Farticle%2Fdetails%2F106278895" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_15585751/article/details/106278895" ref="nofollow noopener noreferrer">浅谈Unity与Android原生的桥接</a>》，其他游戏平台也比较类似</li>
<li>Debug也是开发调试中必要环境，需要在游戏中引入debug开关和入口，如悬浮窗等，并要做好release包关闭入口</li>
</ul>
<ol start="2">
<li>
<h2 data-id="heading-1"><strong>ReactNative页面容器</strong></h2>
</li>
</ol>
<p>上面也介绍了游戏都是采用自绘引擎，所有交互都是在一个Activity页面中，任何新的页面的跳转都会导致游戏pause或者stop，打断其沉浸式体验，而ReactNative是在ReactRootView中承载所有的UI渲染的，所以容器的设计思路考虑了以下几种方案：</p>
<ul>
<li>将ReactRootView加载到游戏Activity的Rootview中，作为一个子View，关闭页面时，从Rootview阶段移除</li>
<li>将ReactRootView封装到系统的Dialog窗口中，这样既可以做到独立窗口加载到游戏中，也不打断游戏进程</li>
<li>有了页面容器后，跳转不同功能的页面，就需要制定一个协议了，通过协议完成页面数据和功能的传递，可以参考开源的Router协议等</li>
<li>活动页面多了后，就涉及到页面之间跳转和窗口管理了，所以需要一套完善的窗口管理API，并通过Unity api，让游戏可以快速通过pop协议或者指定id关闭页面</li>
</ul>
<p>以下是设计完成后大概能力介绍：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24eb8980098c4b3bb66c843fdd683e0a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<h2 data-id="heading-2"><strong>热更新能力</strong></h2>
</li>
</ol>
<p>热更新能力是ReactNative最基础的能力，因引擎支持从asset目录或者磁盘分区中加载JS文件，解决好加载路径和包下载问题，就能很好的支持热更新能力，其中包更新：</p>
<ul>
<li>考虑引擎的统一性，可以采用native的包下载机制</li>
<li>游戏也支持资源更新，也可考虑将js文件作为资源更新</li>
</ul>

<ul>
<li>热更模式一般会支持diff更新、强更、非强更，这些都有比较成熟的框架，这里就不细述了</li>
</ul>
<ol start="4">
<li>
<h2 data-id="heading-3"><strong>Common API设计</strong></h2>
</li>
</ol>
<p>在实际的业务开发工程中，仅仅靠ReactNative提供的基础API和组件是不够的，比如网络请求，大部分客户端都会有网关，标准的API基本无法满足要求，这里就涉及到要封装自己的API和组件的问题：</p>
<ul>
<li>基于ReactNative框架提供的ReactBaseJavaModule，完成对一些公共API的封装</li>
<li>基于ReactNative提供的ViewManager框架，扩展一些自定义的原生端组件</li>
</ul>
<p>但似乎这些还是不够，因为我们是在游戏环境中开发，实际上游戏中或者游戏开发者也需要注入一些API到ReactNative中，供业务使用、扩展，而上述的ReactNative的组件和API架构，对于不熟悉架构的同学来说，会有相当大的学习成本，所以我们基于ReactNative，提出了CommonModule的架构：</p>
<ul>
<li>不依赖ReactNative SDK，采用系统标准的数据结构和interface实现</li>
<li>提供标准的注册API，将这些interface注入到CommonModuleManager</li>
<li>初始化ReactPackge时，会根据CommonModule生成对应的ReactBaseJavaModule，并完成注册</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02a3afede5084950b57cdc88b50b6b26~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决好上述的问题后，基础的功能基本就覆盖了，而且API可扩展性强，当然除了这些外还是不够的，还需要基于基础版本不断迭代，丰富组件、窗口管理、降级冗灾等，以下是我们在游戏中的完整架构：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a6627ee11774ae88ce055d042dde4aa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从架构图中我们可以看到，基本覆盖了游戏活动中需要用到各种API及各种自定义场景：</p>
<ul>
<li>沉浸式原生体验，与游戏页面活动完美融合</li>
</ul>

<ul>
<li>快速、完善的接入、开发、验收体验</li>
</ul>

<ul>
<li>模版化的页面搭建，跨平台运行</li>
</ul>

<ul>
<li>业务活动热更上线，随时、动态、不发版上线</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d276e82650a94abaae15ec73dc8b9579~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            