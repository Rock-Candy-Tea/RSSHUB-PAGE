
---
title: 'Nacos源码结构和AP模式注册中心实现介绍'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8287b8c56a14978b3903afaa43e067a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 00:21:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8287b8c56a14978b3903afaa43e067a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<h1 data-id="heading-1">NacosAP模式源码分析目录</h1>
<ul>
<li>微服务下的注册中心如何选择</li>
<li>Nacos使用和注册部分源码介绍</li>
<li>Nacos服务心跳和健康检查源码介绍</li>
<li>Nacos服务发现</li>
</ul>
<h1 data-id="heading-2">Nacos源码结构介绍</h1>
<p>Nacos版本基于1.4.0版本，整体的项目结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8287b8c56a14978b3903afaa43e067a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到目录，第一眼的感觉就是职责分明，给人的感觉就是高手，关于源码部分我也没全看完，目前只是注册中心相关看完了，配置中心的就是略微看了一下，我先给大家介绍下重点的模块的作用的，到时候大家再结合上面几篇文章去理解源码:</p>
<ol>
<li>address模块: 主要查询nacos集群中节点个数以及IP的列表;</li>
<li>api模块: 主要给客户端调用的api接口的抽象;</li>
<li>client模块: 主要是对依赖api模块和common模块,对api的接口的实现,给nacos的客户端使用;</li>
<li>cmdb模块: 主要是操作的数据的存储在内存中,该模块提供一个查询数据标签的接口;</li>
<li>config模块: 主要是服务配置的管理, 提供api给客户端拉去配置信息,以及提供更新配置 的,客户端通过长轮询的更新配置信息.数据存储是Mysql;</li>
<li>naming模块: 主要是作为服务注册中心的实现模块,具备服务的注册和服务发现的功能;</li>
<li>console模块: 主要是实现与前端进行交互.具有权限校验、服务状态、健康检查等功能;</li>
<li>core模块: 主要初始化属性加载，监听器相关内容，用于加载nacos的default的配置信息，config和naming都依赖于这个包；</li>
</ol>
<p>我觉得上面8个模块相对来说是比较重要，对于大家研究Nacos源码是必须要掌握的，关系间的依赖如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33fd64b8fac5447487ea70dda41c5b68~tplv-k3u1fbpfcp-zoom-1.image" alt="Nacos源码结构和AP模式注册中心实现介绍" loading="lazy" referrerpolicy="no-referrer"></p>
<p>模块之间的调用关系如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2ee5164d1aa421889f7a232ac5e4af4~tplv-k3u1fbpfcp-zoom-1.image" alt="Nacos源码结构和AP模式注册中心实现介绍" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到调用关系就可以感觉出来，整体上源码不算太难，耐心看看还是可以看懂的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b9fb916aa1b484f8efc922b5384ef94~tplv-k3u1fbpfcp-zoom-1.image" alt="Nacos源码结构和AP模式注册中心实现介绍" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">Nacos AP模式源码核心部分介绍</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7243c6a4e3584cc7a1954275543861ea~tplv-k3u1fbpfcp-zoom-1.image" alt="Nacos源码结构和AP模式注册中心实现介绍" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">服务注册</h1>
<p>Nacos Client通过/nacos/v1/ns/instance接口将服务信息(包括服务的名称、IP、端口、状态等信息)注册到Nacos Server的注册表中，存放于类ServiceManager的内部对象Map<String, Map<String, Service>> serviceMap，这是一个两层Map的嵌套结构，第一层的Key是Namesapce名称，第二层的Key是Group名称和Service名称的组合，第二层的Value是Service的对象。</p>
<h1 data-id="heading-5">服务心跳</h1>
<p>用户服务和订单服务注册后，每个客户端会通过定时任务来维持一个定时心跳来持续通知Nacos Server，默认 5s发送一次心跳;</p>
<h1 data-id="heading-6">服务健康检查</h1>
<p>Nacos Server通过定时任务检查注册服务实例的健康状况，对于超过15s没有收到客户端心跳的实例会将它的 healthy属性置为false(客户端服务发现时不会发现)，如果某个实例超过30秒没有收到心跳，直接剔除该实例(被剔除的实例如果恢复发送 心跳则会重新注册);</p>
<h1 data-id="heading-7">服务同步</h1>
<p>服务同步我觉得主要分为两方面同步，一是Nacos Server集群之间的同步，会过
/nacos/v1/ns/instance/distro/datum互相同步服务实例的信息，二是服务的消费者同步变更新到客户端,服务消费者(Nacos Client)会接收服务端的UDP推送过来的服务变更信息(检测到不正常的服务的时候服务发生变更)，及时更新到本地缓存中，这是Nacos的亮点和其他注册中心不一样的地方，面试的时候可以和面试官聊，会让面试官眼前一亮的，因为UDP本身是不可靠的，不能保证所有的变更信息都可以同步到客户端，所以消费者还有一个定时任务的兜底机制;</p>
<h1 data-id="heading-8">谈谈收获</h1>
<p>看完这部分源码收获我觉得主要有两方面的收获:</p>
<h1 data-id="heading-9">技术方面</h1>
<p>技术方面的收获的是最多的，这里简单聊几个例子:</p>
<ol>
<li>从整体的框架的设计，还是到模块中类实现的设计，单一原则体现得淋淋尽致，下图是整体框架设计，体现到代码上就是每个模块职责很清晰，依赖关系很明确，另外框架层面的做的插件化的思想、高可用的思想，都是我们可以借鉴学习的;</li>
<li>很多技术细节的实现很精妙，比如服务变更时候的异步队列的设计、CopyOnWrite的思想、Spring事件机制的应用等等，这些都在我的博客中源码分析的细节中讲到,大家可以稍微花一些功夫看看;</li>
</ol>
<h1 data-id="heading-10">写作方面</h1>
<p>这部分其实还没形成一个完整的思想，只是初步的一个思考，关于这种源码分析的，以后会采用以下方式:</p>
<ol>
<li>框架选型的思考, 分析类似中间件对比；</li>
<li>框架搭建和使用介绍;</li>
<li>源码代码模块介绍和框架模块功能性的描述，类似就是做一个整体功能介绍;</li>
<li>每个模块功能源码的分析，附带时序图和类图关系，后面我会对Nacos系列的文章的内容进行一个改造;</li>
<li>完成每个模块的介绍以后会统一做代码的整体关键步骤的源码分析图和总结；</li>
</ol></div>  
</div>
            