
---
title: '理解IM消息_可靠性_和_一致性_问题，以及解决方案探讨'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce7f042fe374eacb7865c910fb48c99~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 04:53:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce7f042fe374eacb7865c910fb48c99~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文作者“商文默”，有修订和改动。</p>
<h1 data-id="heading-0">1、写在前面</h1>
<p>我整理的大量IM技术文章中（见本文末“参考资料”一节），有关消息可靠性和一致性问题的文章占了很大比重，原因是IM这类系统抛开各种眼花缭乱的产品功能和技术特性，保证消息的可靠性和一致性几乎是IM产品必需的素质。</p>
<p>试想如果一个IM连发出的消息都不知道对方到底能不能收到、发出的聊天内容对方看到的到底是不是“胡言乱语”（严重乱序问题），这样的APP用户肯定不会让他在手机上过夜（肯定第一时间卸载了），因为最基本的聊天逻辑都无法实现，它已经失去了IM软件本身的意义。</p>
<p>不过，另一个方面来讲，IM系统是不标准的（虽然曾经<a href="http://www.52im.net/thread-314-1-1.html" target="_blank" rel="nofollow noopener noreferrer">XMPP</a>这种协议试图解决这个问题，但事实证明那根本不现实），各家几乎都是自已的私有协议、不同的实现逻辑，这也决定了即使同一个技术问题，对于IM来说很难有固定的实现套路和标准的解决方案。</p>
<p>所以，对于本文来说，文中作者虽然提供了有关IM消息“可靠性”与“一致性”问题的解决方案，但方案到底合不合理、适不适合你，这就是仁者见仁、智者见智的事了。用人话说就是：本文内容仅供参考，具体的解决方案请务结合自已的系统构架和实现情况，多阅读几篇有关这个技术话题的文章，取其精华，找到适合自已的技术方案和思路才是最明智的。</p>
<h1 data-id="heading-1">2、本文引言</h1>
<p>丛所周之，即时通讯聊天（IM）系统必需要解决消息可靠性及消息一致性问题（**PS：**如果具体IM系统是什么你都还没弄明白，先读这篇《<a href="http://www.52im.net/thread-3065-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(一)：什么是IM系统？</a>》）。</p>
<p><strong>这两个问题，通俗来说就是：</strong></p>
<ul>
<li>1）消息可靠性：简单来说就是不丢消息，会话一方发送消息，消息成功到达对方并正确显示；</li>
<li>2）消息一致性：包括发送一方消息一致及会话双方消息一致，要求消息不重复，不乱序。</li>
</ul>
<p>本文会从典型的IM消息发送逻辑开始，简单易懂地阐明消息可靠性、一致性问题的原理及可参考的技术解决方法，或许技术方案并不完美，但希望能为你的IM技术问题解决带来启发。</p>
<h1 data-id="heading-2">3、典型IM消息发送过程</h1>
<p><strong>IM的消息发送一般的实现过程可以分为两个阶段：</strong></p>
<ul>
<li>1）发送方发送消息、服务端接收、返回消息 ACK 给发送方；</li>
<li>2）服务端将消息推送到接收方。</li>
</ul>
<p>判断消息发送是否成功主要依据第一阶段——即服务器是否接受到消息。</p>
<p><strong>对于消息发送者来说，消息状态可以分为三类：</strong></p>
<ul>
<li>1）正在发送；</li>
<li>2）发送成功；</li>
<li>3）发送失败。</li>
</ul>
<p><strong>具体来说，这三类状态的具体意义是：</strong></p>
<ul>
<li>1）正在发送：发送方触发发送事件开始，到收到服务端返回消息对应 ACK 之前；</li>
<li>2）发送成功：发送方收到消息对应 ACK 回复；</li>
<li>3）发送失败：超过一定重发次数，未收到消息对应 ACK 回复。</li>
</ul>
<p><strong>对应的消息发送流程如下图所示：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce7f042fe374eacb7865c910fb48c99~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">4、IM消息可靠性</h1>
<p>限于篇幅，对于IM消息可靠性的基本概念和详细原理建议阅读《<a href="http://www.52im.net/thread-3182-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(三)：什么是IM系统的可靠性？</a>》，本文着重谈谈解决思路。</p>
<h3 data-id="heading-4">4.1 重发机制</h3>
<p>保证消息发送第一阶段（见本文“<a href="http://www.52im.net/thread-3574-1-1.html%233" target="_blank" rel="nofollow noopener noreferrer">3、典型IM消息发送过程</a>”一节）消息成功发送的方法是设立重发机制：</p>
<ul>
<li>1）依据一定时长内是否收到消息对应 ACK，判断消息是否要重发；</li>
<li>2）如果超过预设时长，就重新发送；</li>
<li>3）当重发次数超过预设次数，就不再重发，判定该消息发送失败，修改消息发送状态。</li>
</ul>
<p><strong>PS：</strong> 具体的完整方案级代码实现，可以参考<a href="https://links.jianshu.com/go?to=https%3A//github.com/JackJiang2011/MobileIMSDK" target="_blank" rel="nofollow noopener noreferrer">MobileIMSDK</a> 中有关QoS机制的代码实现。</p>
<h3 data-id="heading-5">4.2 会话记录检查</h3>
<p>消息发送第二阶段（见本文“<a href="http://www.52im.net/thread-3574-1-1.html%233" target="_blank" rel="nofollow noopener noreferrer">3、典型IM消息发送过程</a>”一节）服务端推送消息到接收方，如果连接断开，会丢失消息。</p>
<p>所以要保证消息完整，就需要在建立连接后，根据上一条消息（已经 ACK）时间戳，获取会话记录，一次返回一段时间内所有消息（<strong>PS：</strong> 中大型应用中，消息的拉取也不是个简单事情，详情可以阅读《<a href="http://www.52im.net/thread-3069-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发干货分享：如何优雅的实现大量离线消息的可靠投递</a>》）。</p>
<p>另一种保证方法是加入定时轮询，检查消息完整性，具体的思路如下图所示。</p>
<p><strong>建立连接流程图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ba03d27f8346288ca5e72c2a6a51a9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">4.3 需要考虑的两个问题</h3>
<p><strong>消息重发、会话记录检查需要考虑两个问题：</strong></p>
<ul>
<li>1）消息是否会重复发送；</li>
<li>2）消息顺序是否会被打乱。</li>
</ul>
<p>举两个例子。</p>
<p><strong>关于消息重发问题：</strong></p>
<ul>
<li>1）如果丢消息的点在消息达到服务端之前，服务端并没有收到消息，发送方重新发送丢失消息，服务端接收成功，不会产生两条相同消息；</li>
<li>2）而如果服务端接收到消息，返回 ACK 丢失，这时再发送一次相同消息，就可能造成消息重复。</li>
</ul>
<p><strong>关于消息顺序问题：</strong></p>
<ul>
<li>1）如果发送方连发三条消息，第一、第三条成功被服务端接收，第二条丢了，那第三条消息是否会被记录？</li>
<li>2）如果这时第二条消息达到服务端，其顺序是在第三条时间之前还是之后（服务端一般都会给记录打一个时间戳）？</li>
</ul>
<h1 data-id="heading-7">5、IM消息一致性</h1>
<p>同上节一样，对于IM消息一致性的基本概念和详细原理建议阅读《<a href="http://www.52im.net/thread-3189-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(四)：什么是IM系统的消息时序一致性？</a>》。</p>
<h3 data-id="heading-8">5.1 使用 uuid 消息去重</h3>
<p>对于消息重发问题，可以给每条消息增加属性 uuid 作为消息唯一标识，重发消息 uuid 不变，前端根据 uuid 去重。大致思路就是这样。</p>
<p><strong>PS：</strong> 对于IM来说，消息ID也是个很大的技术话题，有兴趣可以读下面这个系列：</p>
<blockquote>
<p>《<a href="http://www.52im.net/thread-1998-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(一)：微信的海量IM聊天消息序列号生成实践（算法原理篇）</a>》</p>
<p>《<a href="http://www.52im.net/thread-1999-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(二)：微信的海量IM聊天消息序列号生成实践（容灾方案篇）</a>》</p>
<p>《<a href="http://www.52im.net/thread-2747-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(三)：解密融云IM产品的聊天消息ID生成策略</a>》</p>
<p>《<a href="http://www.52im.net/thread-2751-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(四)：深度解密美团的分布式ID生成算法</a>》</p>
<p>《<a href="http://www.52im.net/thread-2953-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(五)：开源分布式ID生成器UidGenerator的技术实现</a>》</p>
<p>《<a href="http://www.52im.net/thread-3129-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息ID技术专题(六)：深度解密滴滴的高性能ID生成器(Tinyid)</a>》</p>
</blockquote>
<h3 data-id="heading-9">5.2 使用向量时钟进行消息排序</h3>
<p><strong>对于消息排序问题：</strong> 因为在聊天中，消息的顺序对于发送方的表述有重要的影响，消息不完整或顺序颠倒都可能造成语意不连贯，甚至曲解。所以需要保证发送方发送消息顺序，而会话双方消息排序需要考虑实际情况。</p>
<p><strong>在一般的认知里：</strong> 状态是正在发送的消息，应该还没有被对方看到，只有发送成功的消息，才会被对方看到。但在实现中，消息发送成功是以服务器接收消息并返回 ACK 成功为判断依据，而不是被对方接收到。</p>
<p><strong>那么就会出现这样一个问题：</strong> 如果一条消息状态是正在发送，此时收到一条消息，那么收到的消息是在正在发送的消息之前还是之后？</p>
<p>这是一个上下文关系，关键问题是：发送方是以哪条所见消息为依据发送消息的。</p>
<p><strong>这里提供一种思路：</strong> 借鉴分布式系统中的向量时钟算法（见《<a href="https://links.jianshu.com/go?to=https%3A//zhuanlan.zhihu.com/p/56886156" target="_blank" rel="nofollow noopener noreferrer">分布式系统中的向量时钟算法</a>》）。</p>
<p><strong>先简单描述向量时钟算法：</strong></p>
<blockquote>
<p>向量时钟算法用于在分布式系统中生成事件偏序关系，并纠正因果关系。一个系统包含 N 个节点，每个节点产生的消息体中包含该节点的逻辑时钟，整体系统的向量时钟由 N 维逻辑时钟组成，并在每个节点产生的消息体中传递。</p>
</blockquote>
<p><strong>简单来说，向量时钟算法的实现原理如下：</strong></p>
<ul>
<li>1）初始状态，向量值为 0；</li>
<li>2）每次节点处理完节点事件，该节点时钟+1；</li>
<li>3）每次节点发送消息，将包含自身时钟的系统向量时钟一起发送；</li>
<li>4）每次节点收到消息，更新向量时钟，该节点时钟+1，其他节点对比每个节点本地保留的向量时钟值和消息体中向量时钟值，取最大值；</li>
<li>5）节点同时收到多条消息，判断接收消息的向量时钟之间是否存在偏序关系。</li>
</ul>
<p><strong>针对上述的第5）点：</strong></p>
<ul>
<li>1）如果存在偏序关系，则合并向量时钟，取偏序较大的向量时钟；</li>
<li>2）如果不存在偏序关系，则不能合并。</li>
</ul>
<p><strong>偏序关系：</strong> 如果 A 向量中的每一维都大于等于 B 向量，则 A、B 之间存在偏序关系，否则不存在偏序关系。</p>
<p>对于IM为聊天消息排序来说，其实就是处理聊天消息的上下文语境，决定消息之间的因果关系。</p>
<p><strong>参考向量时钟算法：</strong> 假设有 N 个消息会话方，系统的向量时钟由 N 维时钟组成，向量时钟在各方发送的消息体中传递，并依据向量时钟排序。</p>
<p><strong>具体实现思路如下：</strong></p>
<ul>
<li>1）系统向量时钟设为 (0, 0, …, N)；</li>
<li>2）节点发送消息，更新系统向量时钟，该节点时钟加一，其他节点不变；</li>
<li>3）节点接收消息，更新系统向量时钟，该节点时钟加一；其他节点对比每个节点本地保留的向量时钟的值和消息中向量时钟的值，取最大值；</li>
<li>4）依据消息体内系统向量时钟的偏序关系决定消息顺序。</li>
</ul>
<p><strong>针对上述第4）点：</strong></p>
<ul>
<li>1）如果可以确定偏序关系，则根据偏序关系由小到大显示；</li>
<li>2）如果多条消息不能确定偏序关系，则按照自然顺序（接收到的顺序）显示。</li>
</ul>
<p>向量时钟在理论上可以解决大部分消息一致性的问题，但在实现中还需要考虑实际使用时的体验。</p>
<p><strong>这其中最需要关注的问题是：</strong> 是否要强制排序，或者说，如果实际显示顺序和向量时钟之间的偏序关系不一致，是否要移动消息之间的顺序。</p>
<p><strong>举个例子：</strong> 在一个有多人的会话中，如果有一方网速特别慢，收不到消息，也发不出消息。在他看到的最后的消息之后，其他人已经开始新的话题，这时他关于上一个话题的消息终于发送成功，并被其他人收到。</p>
<p><strong>此时就存在这样一个问题：</strong> 这条关于上一个话题的消息是显示在最后，还是移到较早时间？</p>
<ul>
<li>1）如果显示在最后，但消息内容和目前的话题不相关，其他人可能会感到莫名其妙；</li>
<li>2）如果把消息移到较早时间，那么这条消息可能不会被其他人看到，或者看到前面多了一条消息，会有种突兀的感觉。</li>
</ul>
<p>IM 的场景很多，也很复杂，更多的时候需要从产品角度考虑问题。</p>
<p><strong>对于消息是否需要排序的问题，这里只提出一个比较通用的方案：</strong> 建议会话中不强制排序，会话历史记录中按照向量时钟的偏序关系进行排序。</p>
<h1 data-id="heading-10">6、本文小结</h1>
<p>对于 IM 系统消息可靠性及一致性问题，通过消息重发机制保证消息成功被服务端接收，通过会话记录检查保证收取消息完整，从而保证整个消息发送过程的可靠性。使用 uuid 消息去重，参考向量时钟算法进行消息排序，为保证消息一致性提供一种解决方案。</p>
<p>总之，IM这类系统看似简单，实则水深似海，如果你是IM开发新手，可以从《<a href="http://www.52im.net/thread-464-1-1.html" target="_blank" rel="nofollow noopener noreferrer">新手入门一篇就够：从零开发移动端IM</a>》这篇入手系统学习。如果你自认为已是IM老手，这里整理的 <a href="http://www.52im.net/forum.php%3Fmod%3Dcollection%26action%3Dview%26ctid%3D7%26fromop%3Dall" target="_blank" rel="nofollow noopener noreferrer">IM中大型架构设计</a> 方面的文章或许可以参考一下。</p>
<h1 data-id="heading-11">7、参考资料</h1>
<blockquote>
<p>[1] <a href="http://www.52im.net/thread-3182-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(三)：什么是IM系统的可靠性？</a></p>
<p>[2] <a href="http://www.52im.net/thread-3189-1-1.html" target="_blank" rel="nofollow noopener noreferrer">零基础IM开发入门(四)：什么是IM系统的消息时序一致性？</a></p>
<p>[3] <a href="http://www.52im.net/thread-294-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息送达保证机制实现(一)：保证在线实时消息的可靠投递</a></p>
<p>[4] <a href="http://www.52im.net/thread-594-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM消息送达保证机制实现(二)：保证离线消息的可靠投递</a></p>
<p>[5] <a href="http://www.52im.net/thread-714-1-1.html" target="_blank" rel="nofollow noopener noreferrer">如何保证IM实时消息的“时序性”与“一致性”？</a></p>
<p>[6] <a href="http://www.52im.net/thread-866-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一个低成本确保IM消息时序的方法探讨</a></p>
<p>[7] <a href="http://www.52im.net/thread-753-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM群聊消息如此复杂，如何保证不丢不重？</a></p>
<p>[8] <a href="http://www.52im.net/thread-280-1-1.html" target="_blank" rel="nofollow noopener noreferrer">完全自已开发的IM该如何设计“失败重试”机制？</a></p>
<p>[9] <a href="http://www.52im.net/thread-3069-1-1.html" target="_blank" rel="nofollow noopener noreferrer">IM开发干货分享：如何优雅的实现大量离线消息的可靠投递</a></p>
<p>[10] <a href="http://www.52im.net/thread-1470-1-1.html" target="_blank" rel="nofollow noopener noreferrer">从客户端的角度来谈谈移动端IM的消息可靠性和送达机制</a></p>
<p>[11] <a href="http://www.52im.net/thread-3445-1-1.html" target="_blank" rel="nofollow noopener noreferrer">一套亿级用户的IM架构技术干货(下篇)：可靠性、有序性、弱网优化等</a></p>
<p>[12] <a href="http://www.52im.net/thread-3472-1-1.html" target="_blank" rel="nofollow noopener noreferrer">从新手到专家：如何设计一套亿级消息量的分布式IM系统</a></p>
</blockquote>
<blockquote>
<p><strong>本文已同步发布于</strong>**：** <a href="http://www.52im.net/thread-3574-1-1.html" target="_blank" rel="nofollow noopener noreferrer">www.52im.net/thread-3574…</a></p>
</blockquote></div>  
</div>
            