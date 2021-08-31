
---
title: 'IM技术分享：万人群聊消息投递方案的思考和实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f96ecc5f924ebdb861fc7d5a06f7d7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 06:32:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f96ecc5f924ebdb861fc7d5a06f7d7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文由融云技术团队原创分享，原题“技术实践丨万人群聊的消息分发控速方案”，为使文章更好理解，内容有修订。</p>
<h1 data-id="heading-0">1、引言</h1>
<p>传统意义上的IM群聊，通常都是像微信这样的500人群，或者QQ的2000人群（QQ有3000人群，但那是单独收费的，也就意味着它并非无门槛标配，能用上的人并不多）。</p>
<p>自从国外某号称“世界上最安全的IM”搞出万人群聊之后，万人群迅速被国内的使用者们接受。伴随着移动互联网的发展，即时通讯服务被广泛应用于各个行业（以经不再局限于传统IM社交应用领域），随着业务快速发展，传统百人、千人上限的群聊已经无法满足很多业务场景需求，所以万人甚至十万人的超大群也算是相伴而生、顺应潮流。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f96ecc5f924ebdb861fc7d5a06f7d7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>▲ “纸飞机”的万人群（开发人员颤抖中...）</p>
<p>IM群聊一直是IM应用中比较有难度的热点技术之一，通常意义的群聊，无非就是500人群、1000人群、2000人群这样，技术实现上比单聊要复杂不少。然而对于万人群聊（甚至十万人群聊）来说，相比百人、千人群聊，技术实现上那几乎是另一个技术维度的事情，难度要高很多。</p>
<p>本文根据融云技术团队的实践经验，总结了万人群聊消息投递方案的一些思考和实践，希望能给你带来启发。</p>
<h1 data-id="heading-1">2、相关文章</h1>
<p><strong>万人群聊有关的技术文章还可读一读以下这篇：</strong></p>
<ol>
<li>《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-2707-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-2707-1-1.html" ref="nofollow noopener noreferrer">网易云信技术分享：IM中的万人群聊技术方案实践总结</a>》</li>
<li>《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-3631-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-3631-1-1.html" ref="nofollow noopener noreferrer">企业微信的IM架构设计揭秘：消息模型、万人群、已读回执、消息撤回等</a>》</li>
<li>《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-2848-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-2848-1-1.html" ref="nofollow noopener noreferrer">阿里钉钉技术分享：企业级IM王者——钉钉在后端架构上的过人之处</a>》</li>
</ol>
<p><strong>融云技术团队分享的其它文章：</strong></p>
<ol>
<li>《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-2744-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-2744-1-1.html" ref="nofollow noopener noreferrer">融云技术分享：融云安卓端IM产品的网络链路保活技术实践</a>》</li>
<li>《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-3638-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-3638-1-1.html" ref="nofollow noopener noreferrer">融云技术分享：全面揭秘亿级IM消息的可靠投递机制</a>》</li>
<li>《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-3169-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-3169-1-1.html" ref="nofollow noopener noreferrer">融云技术分享：基于WebRTC的实时音视频首帧显示时间优化实践</a>》</li>
<li>《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-2747-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-2747-1-1.html" ref="nofollow noopener noreferrer">IM消息ID技术专题(三)：解密融云IM产品的聊天消息ID生成策略</a>》</li>
</ol>
<h1 data-id="heading-2">3、超大群面临的技术挑战</h1>
<p>与百人群、千人群相比，万人、甚至十万人超大群，大幅提升了群的触达人数，对于很多业务场景来说，好处不言而喻。</p>
<p>然而单群成员如此之大，给 IM 系统的流量冲击非常巨大，技术难度可想而之。我们先来分析一下超大群的技术挑战。</p>
<p><strong>以一个万人群的模型为例：</strong></p>
<ul>
<li>1）如果群中有人发了消息，那么这条消息需要按照 1:9999 的比例进行分发投递，如果我们按照常规消息的处理流程，那么消息处理服务压力巨大；</li>
<li>2）消息量大的情况下，服务端向客户端直推消息的处理速度将会成为系统瓶颈，而一旦用户的消息下发队列造成了挤压，会影响到正常的消息分发，也会导致服务缓存使用量激增；</li>
<li>3）在微服务架构中，服务以及存储（DB，缓存）之间的 QPS 和网络流量也会急剧增高；</li>
<li>4）以群为单位的消息缓存，内存和存储开销较大（消息体的存储被放大了万倍）。</li>
</ul>
<p>基于这些技术挑战，要想真正达成超大群的技术目标，势必要做特定的技术优化来应对。</p>
<h1 data-id="heading-3">4、一般群聊的消息投递模型</h1>
<p>先来看看普通群聊的消息投递模型。</p>
<p><strong>我们的普通群聊消息投递模型如下图所示：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b71c2021787b466eb1fcd9910a0a4d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如上图所示，当用户在普通群里发了一条消息后，投递路径是：</strong></p>
<ul>
<li>1）消息先到群组服务；</li>
<li>2）然后通过群组服务缓存的群关系，锁定这条消息最终需要分发的目标用户；</li>
<li>3）再根据一定的策略分发到消息服务上；</li>
<li>4）消息服务再根据用户的在线状态和消息状态来判断这条消息是直推、通知拉取还是转 Push，最终投递给目标用户。</li>
</ul>
<p>普通群聊的消息投递，正像您期待的那样，基本上大家的实现手段都大差不差。然而对于万人群来说，这显然还不够。</p>
<p>下面来看看我们针对万人群聊消息投递的技术优化手段。</p>
<h1 data-id="heading-4">5、万人群聊消息投递优化手段1：控速</h1>
<p>针对万人群的消息投递，我们的一个主要手段就是控速。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25f1633328e24acda2aa3e56398d6391~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示。</p>
<p><strong>首先：</strong> 我们会根据服务器的核数来建立多个群消息分发队列，这些队列我们设置了不同的休眠时间以及不同的消费线程数。</p>
<p>通俗来讲，可以将队列这样划分为快、中、慢等队列。</p>
<p><strong>其次：</strong> 我们根据群成员数量的大小来将所有群映射到相应的队列中。</p>
<p><strong>规则是：</strong></p>
<ul>
<li>1）小群映射到快队列中；</li>
<li>2）大群映射到相应的慢队列中。</li>
</ul>
<p>**然后：**小群由于人数少，对服务的影响很小，所以服务利用快队列快速的将群消息分发出去，而大群群消息则利用慢队列的相对高延时来起到控速的作用。</p>
<h1 data-id="heading-5">6、万人群聊消息投递优化手段2：合并</h1>
<p>在本文第3节中提到的万人群聊所面临的技术挑战，最主要的挑战其实就是消息进行扩散分发投递后，消息被克隆出N条，消息流量瞬间被放大。</p>
<p><strong>举个例子：</strong> 当一条群消息发送到 IM 服务器后，需要从群组服务投递给消息服务，如果每一个群成员都投递一次，并且投递的群消息内容是一致的话，那肯定会造成相应的资源浪费和服务压力。</p>
<p>那么针对这种情况，我们的解决方案就是进行消息合并投递。</p>
<p><strong>原理就是：</strong> 服务落点计算中我们使用的是一致性哈希，群成员落点相对固定，所以落点一致的群成员我们可以合并成一次请求进行投递，这样就大幅提高了投递效率同时减少了服务的压力。</p>
<p><strong>下图是云信团队分享的万人群消息合并投递逻辑：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48491aa88c584eebb945e2aa3bcaf38b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>▲ 上图引用自《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-2707-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-2707-1-1.html" ref="nofollow noopener noreferrer">IM中的万人群聊技术方案实践总结</a>》</p>
<p>如上图所示，云信团队的万人群消息合并投递方案是：按Link分组路由消息，同一Link上的全部群成员只需要路由一条消息即可。</p>
<h1 data-id="heading-6">7、十万、百万级的超大群处理方案</h1>
<p>在实际群聊业务中，还有一种业务场景是超大规模群，这种群的群人数达到了数十万甚至上百万。</p>
<p>这种群如果按照上述的投投递方案，势必仍会造成消息节点的巨大压力。</p>
<p>比如我们有一个十万人的群，消息节点五台，消息服务处理消息的上限是一秒钟 4000 条，那每台消息节点大约会分到 2 万条群消息，这已大大超出了消息节点的处理能力。</p>
<p>所以为了避免上述问题，我们会将群成员上线超过3000的群识别为万人群、超级群，这种级别的群可以根据服务器数量和服务器配置相应做调整针对这种超级群会用特殊的队列来处理群消息的投递。</p>
<p>这个特殊的队列1秒钟往后端消息服务投递的消息数是消息服务处理上限的一半（留相应的能力处理其他消息），如果单台消息服务处理的 QPS 上限是 4000，那群组服务一秒往单台消息服务最多投递 2000 条。</p>
<h1 data-id="heading-7">8、写在最后</h1>
<p>未来，我们也会针对群消息进行引用投递，对于大群里发的消息体比较大的消息，我们给群成员只分发和缓存消息的索引，比如 MessageID。等群成员真正拉取群消息时再从将消息组装好给客户端分发下去。这样做会节省分发的流量以及存储的空间。</p>
<p>随着互联网的发展，群组业务的模型和压力也在不停地扩展，后续可能还会遇到更多的挑战，当然也会不断迭代出更优的处理方式来应对。（本文同步发布于：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-3687-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-3687-1-1.html" ref="nofollow noopener noreferrer">www.52im.net/thread-3687…</a>）</p></div>  
</div>
            