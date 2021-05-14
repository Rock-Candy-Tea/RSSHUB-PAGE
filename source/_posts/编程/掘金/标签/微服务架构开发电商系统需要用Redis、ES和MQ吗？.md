
---
title: '微服务架构开发电商系统需要用Redis、ES和MQ吗？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c482235ae25842da970686e4f9000e62~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 02:07:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c482235ae25842da970686e4f9000e62~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>如果不用什么很高大上的东西，就是有多个微服务就行这种技术架构会很难吗？</p>
<p>我看了一些视频，他们都用到了es、mq、redis的东西，我想不用这些东西，就简单的有多个服务，这样可行吗？</p>
</blockquote>
<h1 data-id="heading-0">01 使用微服务你考虑好了吗？</h1>
<p>首先商场的开发要根据你的实际需要来定夺架构，例如，只是在微信小程序中商品滚动图片展示、产品分类、微信支付、订单、地址、简要配送信息，并且有一套后台管理系统，包括：用户、角色、商品、定价、订单等，基本上一个完整的商场系统就可以运行了。那么是不是要一定上微服务呢，还是单体服务就够用了呢？</p>
<p>需要上微服务架构最主要的目的就是为了解决服务功能频繁更新发布，导致总是影响业务大面积抖动，从而降低了新功能的敏捷迭代。因为对于单体服务，这个问题是无法避免的，一定会影响可靠性。</p>
<p><strong>1. 分布式CAP：</strong> 但是我接触过的微服务项目，往往微服务发布机制都不成熟，实际上每次发布微服务和发布单体是一个效果，所有服务都得停下来重新部署。为什么呢？因为在线事务系统一定是优先考虑强一致性，无论什么开发团队遇到微服务，嘴上说得再漂亮，到了部署的时候，身体都会很诚实。微服务在分布式环境下对CAP理论的付诸实施，你是否已经了然于心了呢？</p>
<p>只要是联机事务，在微服务环境下依然要保证分布式强一致性。如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c482235ae25842da970686e4f9000e62~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2. 分布式事务：</strong> 微服务另外遇到的一个问题就是将单体应用对数据库的SQL操作拆分成了PRC远程协作，那么这个时候就可能涉及分布式事务。</p>
<p>如下图所示：发起端向支付微服务发起一次支付提交，完成支付后，支付微服务需要用RPC调用来通知订单服务更新订单状态，那么这时候系统就已经掉入到了分布式事务的漩涡。你是否为分布式事务做好准备了?</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4a6c13a96094681b3e07e738acc270b~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">02 技术是随着业务规模的发展而逐步引入</h1>
<p>其次，这些都对你来说都没有问题了，为什么还会有Redis，elasticsearch(es)，MQ呢? 那我们就一一分析一遍这些技术在商场中的作用，你自己去评估是否引入。</p>
<p><strong>1. Redis：</strong> 主要作用是查询缓存，防止数据库被击穿，主要情境是商场出现了高并发的访问状态，不过也恭喜你，能用Redis证明你的业务很成功。</p>
<p>如下图所示：一个比较标准的MySQL读写分离，Redis作为查询缓冲区的联机事务处理的分布式架构耦。这种情况也是出现在MySQL读写分离都无法解决高并发带来的某个峰值时刻，对数据库的击穿，就需要通过增加一个二级缓存来解决。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e661e71a10ae4012902d2408f432fb6b~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>请一定要注意，贯彻K.I.S.S原则，技术上能不加就不加的原则。因为总是要面对分布式的一致性问题，在加入Redis缓存这个问题，实际上这是目前工程师们非常流行的一种做法，但是在保证MySQL主从复制的一致性方面本身就存在不可控的复杂度，更何况，又引入缓存系统（Redis）和数据库（MySQL）之间的数据同步的一致性问题，会使得整体架构的复杂性更高，会导致上线后遇到很多不可预知的麻烦，所以在没有做好充分准备工作之前，增加架构复杂度的事情要慎之又慎。</strong></p>
<p><strong>2. Elasticsearch：</strong> 对于大量的商品内容检索，高级一点就不仅仅是分类关键字查询了，更需要是专业搜索提供的商品内容的全文内容检索，方便用户通过组合关键字，更快查找到自己想要的商品，除非你对自己的编程功底认为不错，可以直接用luence，否则es是个很不错的选择。</p>
<p>如下图所示：为架构纳入Elasticsearch专业搜索引擎，需要引入的技术操作流程，MySQL binlog->Canal->Kafka->Elasticsearch，这是一个binlog实时推送架构，效果最好，也最复杂。这就是表面说起来简单，但真要做好，内部都要沁透工程师的辛勤与汗水。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c53c32c6144421d85cbd14a7f700c7b~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3. MQ：</strong> 当商场的微服务之间，以及商场与第三方服务之间形成犬牙交错的状况，一般微服务架构会形成事件驱动机制也就是EDA，例如订单发起后通过消息推送给下游，下游可能就是订单的配送系统接受处理。那么用到mq了，系统已经不再是一个小范围的商业服务了，应该算是平台级的！如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09b5b56b5c2540d6818375214c9b64da~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然mq的引入也不一定是发展到了规模化，也有可能一开始就面临O2O的业务需要，早期就需要将线上业务事件推送给线下业务系统，这就需要mq了，建议考虑支持分布式事务的mq，例如：rocketmq。如下图所示：传统企业搞互联网+，一开始就要考虑通过消息中心来解决线上线下的数据对接、信息安全、异步协作等问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e41b4f9986c49f9b0204ac9b4ce7e73~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">03 总结</h1>
<p>最后做个总结，对于上面聊的这些内容，我相信你心里至少应该有个底，可以明确一点——系统架构的技术体系都是不断迭代加厚，都是根据业务的需要不断地加持，逐步产生良好的业务支撑作用。</p>
<p>初期往往过度设计得越多，系统死掉的几率越大，因此微服务是不是一开始就要纳入设计? 系统性能优化，高级查询，复杂系统优化等等这些操作，是否需要在前期设计中完成?，是否已经有了与之匹配的团队组织形式? 这些都需要逐一斟酌，虽需长远规划但仍要从简入深。</p>
<p><strong>可以阅读另一篇关于微服务和分布式关系的详细文章：</strong></p>
<p><a href="https://mp.weixin.qq.com/s/d5fj9zL_YM3P13XR1Z0KJA" target="_blank" rel="nofollow noopener noreferrer">微服务都想用，先把分布式和微服务之间的关系说清楚</a></p>
<p><a href="https://mp.weixin.qq.com/s/iKwgG6pXiqeomtOjOw0mYQ" target="_blank" rel="nofollow noopener noreferrer">通俗地理解SOA与微服务之间的关系</a></p>
<p>前往<a href="http://www.readbyte.com/" target="_blank" rel="nofollow noopener noreferrer">读字节创作中心</a>——了解”读字节“更多创作内容</p>
<div align="center"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9df4d57620eb4309a9c3300e210ee1af~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></div></div>  
</div>
            