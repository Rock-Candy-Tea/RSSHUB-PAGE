
---
title: '技术leader教你看源码的本质'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/e06028a8c3076563658dd7132d6fc4b9.png'
author: Dockone
comments: false
date: 2021-08-30 03:11:41
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/e06028a8c3076563658dd7132d6fc4b9.png'
---

<div>   
<br>前面我说过技术leader的几个特质，今天还想跟大家分享下，作为技术leader，还要懂得研究和引入技术，引入的前提一定是要Hold住。怎么才叫Hold住呢？就是能精通使用它，能够深入了解它的架构、原理，能够剖析它的核心源代码。<br>
<br>以研究Nacos为例，这次我分享下研究技术的方法，授之以渔，希望大家有所收获，当然也欢迎留言共同讨论更好的技巧。<br>
<h3>官方文档，搭建demo使用</h3>很多人喜欢买书看，看别人的博客，其实都是吃剩饭，别人也是看了官方文档写的。一名合格的技术人员，尽量从源头看，看官方的文档，原汁原味的，耐心点一点点看。<br>
<br>Nacos的官方文档，怎么看这个过程我就不讲了，基本上就是按目录过一遍，然后根据官方例子搭建起来，知道它的基本功能使用。<br>
<br>重点看看里面的架构设计、模型概念。<br>
<h3>了解功能设计主线，确定研究主线，高维度抽象功能模型</h3>看完官方文档，基本会用后，要确定深入研究的主线。Nacos不仅仅包含了服务管理功能，还包含了配置管理，元数据管理。看到这里其实也能明白为什么Nacos未来会成为注册中心的趋势，因为它同时包含了微服务的两个套件：注册中心、配置中心，用了它能少部署一个配置中心。下图来自官方文档：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/e06028a8c3076563658dd7132d6fc4b9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/e06028a8c3076563658dd7132d6fc4b9.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图片来源：Nacos官方文档</em><br>
<br>这篇文章我们研究的主线是注册中心，所以只研究它如何实现注册中心的。这个时候，我们要高维度看，注册中心需要哪些功能？这些功能，是任何注册中心都需要实现的功能，要把这些掌握清楚。显然，注册中心通用的功能模型包含：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/bc575ceb3dc9c3f2e477083c1fde1bcb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/bc575ceb3dc9c3f2e477083c1fde1bcb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ol><li>服务注册</li><li>服务心跳保活</li><li>服务下线（正常下线、异常下线）</li><li>服务发现</li></ol><br>
<br>基本上实现上面四点，一个单体的注册中心就实现了。然后如果考虑分布式，还要设计它如何实现CP/AP模式。<br>
<h3>下载源代码，提取精华</h3>很多人看源码，学源码，往往都是看了一个寂寞，为了寂寞而寂寞。到底要看什么？<br>
<h4>源码看什么？</h4>看源码，要看作者怎么架构、怎么设计、怎么实现，并思考为什么要这么实现，通过源码看到了它里面的精髓，才算真看了源码。不然就是看了个西瓜，吃了就没了，就是个吃瓜群众。相反，看源代码，提炼模型、原理、机制、设计模式、并发经验、网络经验、OS存储机制等，那你才算真看了源码，吸收了它的营养。<br>
<h4>源代码怎么看呢？</h4>抛开技术积累和经验因素外，方法也是很重要的一个部分。很多看源代码都没有经验，看到源代码复杂，代码又多，一看就懵逼，也不知道从哪里看起。<br>
<br>我先分享3个经验：<br>
<ul><li><strong>找源头，就是启动的地方</strong>。这个一般从脚本里看可以到，大部分中间件都是封装了启动脚本的，你就从这个启动脚本里找启动类，让源码能跑起来，后续可以debug验证。</li><li><strong>只看主线代码</strong>。就是我们上面提炼的功能模型。那些日志、统计分析、异常分支、非主线分支第一次都不要看。</li><li><strong>先静态看源码</strong>。不要动态debug，因为debug，很容易陷入细节，陷入各种分支，几绕几绕就懵逼了，然后就放弃了。静态看源代码，就是不断锻炼自己，让自己只看主线代码，那种明显是分支的直接跳过不看，这样快速的过主线。 实在有疑惑了，然后debug验证下。</li></ul><br>
<br><strong>我们来看看Nacos的源码，版本是1.4.2，分析下我是怎么看的。</strong><br>
<br>1、服务注册如何实现的？如何确保高并发？<br>
<br>客户端启动的时候，会通过http请求发送注册请求，请求链接采用RESTful模式。服务端接受到注册请求后，会把请求参数封装放到一个阻塞队列里，然后基于一个线程不断的获取这个阻塞队列的信息，放入到注册表中。<br>
<br>可以看到高并发设计的一个关键点：异步。这里还可以对比延伸，ZooKeeper如何实现的？Eureka如何实现的？这些实现之间有什么优劣？它们能否做到高并发？是否也是异步？  这些就留给读者探索了。<br>
<br>2、服务注册表是如何设计的？为什么这么设计？以及怎么防止多节点的读写并发冲突？<br>
<br>Nacos支持CP和AP模式，如果不懂CP和AP的自己百度了，这种简单的概念我就不科普了。<br>
<br>①AP模式下，是基于内存存储的，底层其实是一个双重的map结构。CP模式下，数据是存储到文件的。这里我们主要还是研究AP模式。因为大多数场景下，我们注册中心更适合AP模式。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/138af2d93e1c8d5a92afec020c49486c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/138af2d93e1c8d5a92afec020c49486c.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
看到这个map结构，有没有思考过为什么这么设计？namespace的目的是？group的目的是什么？如果有一定DevOps经验的同学知道，我们一个项目环境往往可能有多套，比如开发环境、测试环境、预发布环境、线上环境等。如果每一套环境都部署一个注册中心，是不是很麻烦。所以这里namespace的目的，就是可以用同一套注册中心，基于namespace来隔离这些不同的环境。<br>
<br>那么group的目的是什么呢？如果我们用过Dubbo就知道这个概念了，对服务进行分组。有时候我们一个服务刚开始是一个大服务，但随着业务扩展，有时候需要拆成几个小服务，这样就可以设置为一个group。<br>
<br>这些都是基于<strong>可扩展性</strong>来考虑设计的。我们看看官方文档的数据模型：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/b68401b3bd806f8fb10dd2f467fab09e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/b68401b3bd806f8fb10dd2f467fab09e.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图片来源：Nacos官方文档</em><br>
<br>②怎么防止读写冲突呢？<br>
<br><strong>核心点：读写分离，采用了写时复制模式，提升了高并发</strong>。就是写的时候，拷贝一份旧的实例，对这份拷贝数据修改，修改完后，再复制过去，读直接读旧实例。<br>
<br>读写分离这种模式，避免了加锁冲突，提升了高并发能力。读过Eureka源码的了解，它的实现是基于多级缓存来实现的，然后缓存之间同步数据。时效性显然没有Nacos的好。<br>
<br>这里还要思考一个点，这里复制，复制的是什么？如果写时复制，把所有的数据都复制，显然内存吃不消的。这里研究下官网的服务模型，服务下面封装的是一个个集群，集群下面是实例。<br>
<br>为什么有集群这个概念呢？ 如果公司规模大一点的同学会知道，为了容灾高可用，一个服务，可能是多机房部署的。比如一个服务可能在亦庄机房部署一个集群，兆维机房下也有一个集群。这里可以看到Nacos模型设计的是非常巧妙的，基本上很多点都考虑到。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/a22436a343ed00f911fcaba47bde491d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/a22436a343ed00f911fcaba47bde491d.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们看源代码也可以验证，可以看到Service下面，封装了一个clusterMap。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/8f80cd0509156f5f5a87412195553cd9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/8f80cd0509156f5f5a87412195553cd9.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
而cluster下面又封装了具体的实例集合，画横线的部分。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/5b6791adac04f320f121c89c40cd499c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/5b6791adac04f320f121c89c40cd499c.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
所以，这里的写时复制，它复制的是这个实例所属的集群结构，我把核心代码截图出来，<br>
<br>先复制旧的实例，放到一个oldMap里面。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/8345d3c83a48cb9d07499e4e8087280a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/8345d3c83a48cb9d07499e4e8087280a.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对旧的Map做一系列运算操作，比如下线一个实例，然后把结果放到IPS。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/929d77988e0b01231ec957a462198b2f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/929d77988e0b01231ec957a462198b2f.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最后把新的服务实例集合赋值回去。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/bf3e31307e6fde59996e7f0ba4161bb1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/bf3e31307e6fde59996e7f0ba4161bb1.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到这里面有很多技巧，这些都可以学习，以后自己设计中间件或者写代码的时候，都是可以直接用的。<br>
<br>3、服务心跳是如何保活的？<br>
<br>客户端每5s发送心跳给服务端，通过http请求调用发送给服务端。服务端开启健康检查任务，每隔5s检查一次，如果发现超过15s没有收到心跳，设置健康状态为false，如果超过30s没有收到心跳，直接剔除实例。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/0ba7c8bc3bf839f82ea10f0ad5e2e388.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/0ba7c8bc3bf839f82ea10f0ad5e2e388.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里我们想一个问题，服务端开启健康检查任务，如果集群模式下，每个服务端都要判断吗？这个会不会很耗性能？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/141b33d1f01c4c5367e97f44e2a625e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/141b33d1f01c4c5367e97f44e2a625e6.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们看到健康检查任务里有这样一段代码,它会根据服务名称通过hash运算后对机器结点数取模，判断是否要执行健康检查代码。也就是说，集群模式下，不管启动了多个服务实例，任何一个服务，正常情况下只有一个结点来执行健康检查代码。但可能以为时效性，如果其他节点多执行一次，也没什么大影响对吧。当然这里面还有一些细节，都可以深扣，服务发现，时效性是多大？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/c37a92cbacf35e3174746b84967c00ea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/c37a92cbacf35e3174746b84967c00ea.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
4、服务是如何下线的？<br>
<br>超过30s未收到心跳，就会剔除，这个上面我们知道了，剔除调用的其实是自己的deregister方法：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/b879eb54a7e8eea53b3dc8dfa38dacc3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/b879eb54a7e8eea53b3dc8dfa38dacc3.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
跟进去看一下，我们发现删除方法对Service也是加了锁的，也就是说对同一个服务的修改，是做了防并发的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/6063b1b2dd7cec072f947d21532aedf7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/6063b1b2dd7cec072f947d21532aedf7.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最后删除，本质也是基于异步的，这个和注册逻辑类似。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/cc2d4658621f27d3deaf7f95e73c87cf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/cc2d4658621f27d3deaf7f95e73c87cf.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
5、户端如何发现服务的，服务修改是如何感知的？<br>
<br>① 客户端先从本地缓存获取服务实例，如果为空，则从服务端拉取。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/b107d9fce34f5bbf0e3d1f5546684524.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/b107d9fce34f5bbf0e3d1f5546684524.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
并启动一个定时任务，定期更新服务端最新实例信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/1bdc188387897b0f258438b0f883494c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/1bdc188387897b0f258438b0f883494c.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
② 服务端修改后，通过UDP协议推送<br>
<br>一方面基于UDP推送提升了实时性，另一方面，UDP虽然可能丢包，但客户端定时拉取可以作为兜底。这个设计真的很巧妙。<br>
<br>然后Nacos的CP模式，基于Raft协议实现的一致性。还有它的配置中心架构是如何设计的，限于篇幅，就不再展开了。大家按照我的思路，去研究就好。记住看源码，根据主线看，然后学习它的机制、原理。不要紧紧只是看个代码。<br>
<h4>提取源码精华</h4>看完源码后，需要提取总结里面的精华，这里提取了部分用于举例，大家可以根据自己的逻辑提取精华，不断提取精华，不断内化成自己的经验，技术才能得到质的飞跃。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210826/f089c64084f98fe45f9413eb32ac0a30.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210826/f089c64084f98fe45f9413eb32ac0a30.jpg" class="img-polaroid" title="19.jpg" alt="19.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>学以致用</h4>学习完源码，吸取精华不是目的，目的还是要学以致用。常见的路径有：参加开源社区，自研中间件投入到生产实践，内部分享经验，外部演讲分享。<br>
<br>学以致用才是本质！<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/eAc9F1ddb5WiiSZEdxCX7Q" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/eAc9F1ddb5WiiSZEdxCX7Q</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            