
---
title: '分布式缓存与DB秒级一致设计实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/9fa04f887c9399f81161fc63e6ade9ac.png'
author: Dockone
comments: false
date: 2021-03-28 08:08:45
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/9fa04f887c9399f81161fc63e6ade9ac.png'
---

<div>   
<br><h3>前言</h3>爆款项目是2020年携程的一个新项目，目标是将全品类、高性价比的旅行商品统一集合在一个频道供用户选购。出于这样的业务定位，项目有三个特点：<br>
<ul><li>高流量</li><li>部分商品会成为热卖商品</li><li>承担下单职能</li></ul><br>
<br>那么在系统设计之初，就必须考虑下面两个点：<br>
<ul><li>如何应对高QPS（包括整体高QPS和个别商品的高QPS），高流量，保障C端用户体验？</li><li>在满足第一点的情况下，如何保障信息的时效性，让用户尽可能看到最新的信息，避免下单时的信息和看到的信息不一致？</li></ul><br>
<br>很显然，要想较好的应对高QPS，高流量的前端请求，需要借助缓存（我们使用了公司推荐的Redis，后文不再做特别说明）。但是怎么使用好缓存解决上面两个问题，这是需要考虑的。我们对比了本文讨论的方案，和另外几个传统方案的优缺点，见下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/9fa04f887c9399f81161fc63e6ade9ac.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/9fa04f887c9399f81161fc63e6ade9ac.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
综上，本方案除了第一次实现有较高的复杂度外，带来的其他优势都是很可观的。目前线上运行下来，数据访问层应用相关的数据如下：<br>
<ul><li>QPS：近万QPS</li><li>性能：平均耗时个位数毫秒</li><li>缓存数据更新延时：秒级</li><li>Redis集群的请求量：进行热点key处理后，减少原本1/4的请求量</li><li>Redis集群内存占用：按需进行缓存，内存占用为传统方案的1/10</li><li>Redis集群CPU使用情况：整体平稳，未出现局部机器CPU异常</li></ul><br>
<br>本文将从应用架构、缓存访问组件、缓存更新平台几方面介绍本方案。<br>
<h3>应用架构</h3>本方案的应用架构大致如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/b86b60ac4055f7721d5360223930f6b4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/b86b60ac4055f7721d5360223930f6b4.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其中，浅绿色部分由业务实现，深绿色部分是本方案实现的。后文会详细介绍缓存访问组件和缓存更新平台的设计思路。<br>
<h3>缓存访问组件</h3>该组件的存在主要是为了封装缓存的访问。主要做了两件事：<br>
<ul><li>按需异步将缓存中需要增、删、改的键值对通过消息传递给缓存更新平台，让其进行实际的缓存更新操作。</li><li>对热点key进行本地缓存与更新，避免对某个key的大量请求直接打到缓存导致缓存雪崩。</li></ul><br>
<br><h4>为什么要异步操作缓存？</h4>这里，可能大家会有一个疑问，为什么要将简单的缓存操作由传统方案中的同步操作变为基于消息机制的异步操作呢？<br>
<br>这是由于我们的业务场景要求DB数据与缓存数据能够快速最终一致而决定的。如果采取传统的同步操作，那么极端情况下，可能会出现下面这样的多线程执行时序：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/9cc024d97158abe3e99b03ad2510c9e8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/9cc024d97158abe3e99b03ad2510c9e8.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以发现，这样的时序执行完后，缓存中key对应的value是过期的v1而不是数据库中最新的v2，这就会导致严重的用户体验问题，并且这个问题很难被发现。<br>
<br>那么我们是不是可以采用Redis的SETNX命令来解决这个问题呢？其实也是不行的。比如，上面的时序变为线程1先执行完，线程3再执行完，那么实际上缓存中的数据依然会是过期的v1。因为线程3在采用SETNX命令设置缓存时，发现key已经有对应的值了，所以线程3最终的SETNX命令不会执行成功，也就导致了该更新的缓存反而没有更新。<br>
<br>不难看出，这类问题就是由于我们会有大量的并行操作同一个key导致的。所以，这里引入消息机制来异步执行缓存操作就是为了使同一个key的并行操作变为串行操作。<br>
<br><strong>异步操作带来的问题</strong><br>
<br>由于缓存操作由传统方案中的同步操作变为异步操作，那么引入了两个新问题：<br>
<ul><li>如果投递消息失败了怎么办？</li><li>业务希望数据更新成功后缓存务必更新成功，也就是说希望DB数据更新和缓存更新近乎在一个事务里面，这该怎么办？</li></ul><br>
<br>在这个组件中，我们通过引入一张存放于业务的DB的消息记录表来解决上述两个问题。它相当于是一个容灾方案，只要消息进入这张表，缓存更新平台就保证这条消息必然会被消费。<br>
<h4>关于热点key的处理</h4> 该组件还有一大功能就是对热点key的处理。众所周知，缓存热点key在很多业务中都存在。例如若页面中存在长列表/瀑布流，那么第一屏的产品的访问量肯定比第二屏的产品访问量要高很多；又例如某些商品做活动，那么这类商品肯定要比没做活动的商品访问量高很多。<br>
<br>而爆款业务在可预见的未来，肯定也会出现热点key的问题。若热点key的问题不及时解决，当对单一key的请求量足够大时，可能导致缓存集群中存储该key的机器性能严重下降，从而导致缓存雪崩。所以在系统设计上，我们需要为解决热点key预留可扩展性。<br>
<br>目前组件内部热点key的处理流程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/2c08a48d981fb89b7f0c9877a82e234e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/2c08a48d981fb89b7f0c9877a82e234e.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通过上述流程可以看到，组件内部解决热点key主要是要解决下面三个问题：<br>
<ul><li>如何判断是热点key？</li><li>热点key如何存储？</li><li>热点key的内容如何更新？</li></ul><br>
<br><strong>如何判断是热点key？</strong><br>
<br>首先我们需要知道哪些key是热点key才能解决热点key的问题，识别热点key采取下面两个方案互补：<br>
<ul><li>动态识别热点key：主要针对部分key的访问流量增长相对平稳没那么陡的场景，使应用有能力应对线上一些无法预知的突发情况。</li><li>预设热点key：主要针对定点开始的活动（比如电商的秒杀），这类流量增长通常会非常陡且高峰很短暂。如果这种场景也采取方案1来主动识别通常就会导致滞后性，其实最终不会起到任何作用。所以我们就需要预设热点key。</li></ul><br>
<br>由于爆款业务处于起步阶段，场景1的问题尚不紧急，所以目前方案1我们计划在未来的迭代实现，这里不做过多讨论。<br>
<br>对于方案2，业务目前可以主动将可以判定为热点的key灌给缓存访问组件。组件收到这类key后，当它在从缓存拿到这类key的内容后会主动将内容存入本地内存。后续所有的访问，都会从本地内存读取，从而大幅降低对远端缓存服务器的访问。<br>
<br><strong>热点key如何存储？</strong><br>
<br>在前文已经提到，针对热点key，我们选择将其内容存放于应用服务器的内存中，这样做基于下面两个原因：<br>
<ul><li>应用服务器本身一般都是以集群来部署，可以弹性缩扩容；</li><li>应用服务器的内存基本上可用空间都在50%以上；</li></ul><br>
<br>这样做带来的好处是：应用服务器在基于流量变化进行横向缩扩容时，热点key的内存与并发量的支持也跟着一起调整了，避免了多余的维护成本。<br>
<br>缓存访问组件在进行本地缓存时，考虑到热点key的访问流量通常是增长快下降也快，而且极端情况下可能出现本地缓存内容和数据库中的内容不一致，所以我们选择在本地进行一个很短时间的缓存，便于其能够应对突发的流量增长的同时也能在极端情况下快速与数据保持一致。<br>
<br><strong>热点key的内容如何更新？</strong><br>
<br>前文有提到，我们希望尽可能快的将数据库中最新的数据反映到缓存，热点key的本地缓存也不例外。所以，我们需要建立一个广播机制，让本地缓存能够知晓远端缓存的内容变化了。<br>
<br>这里，我们借助了缓存更新平台。由于所有的缓存更新都是发生在缓存更新平台（见后文），所以其可以将发生变化的缓存key通过消息队列广播给所有缓存访问组件，组件消费到这条消息后，若key是热点key，则进行本地缓存的更新。极端情况下，可能会出现组件消费消息失败从而未更新的问题。针对这种情况，前文有提到，我们采取了很短时间的本地缓存，所以即便出现这个问题，也只会在较短时间有问题，最大程度保障了用户体验。<br>
<h3>缓存更新平台</h3>缓存更新平台主要有下面两大功能：<br>
<ul><li>执行实际的缓存增、删、改命令；</li><li>缓存内容发生了变更后通知业务方；</li></ul><br>
<br>由于缓存更新平台汇总了所有的缓存更新操作，所以它能够在缓存发生变更后，通过广播消息及时通知业务方，业务方拿到该消息后可以判断是否要做处理。目前这个功能主要用于解决热点key的内容更新问题，这在前文热点key处理的相关章节已做了详细说明，后文不再赘述。<br>
<br>后文主要介绍该平台的第一点功能。<br>
<br>前文有讲到，我们为了规避并行操作同一个key导致缓存中存储旧值而非最新值的问题，从而引入消息机制将缓存操作串行化。该缓存更新平台就用于串行的从消息队列消费缓存操作消息。<br>
<br>所以我们的核心需求是：单线程处理同一个key的缓存操作消息且不让旧的缓存覆盖新的缓存。<br>
<br>基于上面的需求，产生了四个问题：<br>
<ul><li>怎么判断多个消息属于同一个key的缓存消息？</li><li>缓存操作的消息量级非常大（峰值情况下几十万条/分钟），怎么快速消费完？</li><li>怎么知道缓存内容是新还是旧，是否该对该消息进行处理？</li><li>由于基于消息，如何保障消息一定会被处理？</li></ul><br>
<br><h4>怎么判断多个消息是属于同一个key的缓存消息？</h4>针对这个问题，我们通过在消息中携带缓存的key来解决这个问题，这样做带来了几个好处：<br>
<ul><li>将业务和缓存更新平台解耦，key的内容由业务全权决定；</li><li>通过首先计算key的hash值，然后对其取模，可以将相同的key分配到相同的线程处理（见后文）；</li><li>可扩展性强，针对后续热点key的分析和自动化加载热点key也起到了关键作用（后续迭代计划的功能）；</li></ul><br>
<br><h4>怎么快速消费消息？</h4>由于核心需求是单线程的处理同一类key的消息，所以不同key的消息由不同的线程处理既能很好的解决性能问题，又不会产生逻辑问题。<br>
<br>我们采取了如下架构去消费产生的消息：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/31df03a4d4e203096ef055520362129a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/31df03a4d4e203096ef055520362129a.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
同一类key通过计算其hash值，然后再对结果进行取模，可以保证它们进到同一个内存队列和线程，从而规避并行操作同一个key的问题。通过这个架构，如果某个key的消息消费过慢，也不会影响其他key的消费进度，从而既保障了消费速度也满足了需求。<br>
<br>实践下来，目前我们仅用了两台机器就能做到每分钟消费几十万条消息，且远未遇到瓶颈。<br>
<h4>怎么知道缓存内容是新还是旧，是否该对该消息进行处理？</h4> 虽然我们做到了同一类key的单线程处理，并且，我们使用的公司的消息队列能保障消息的有序性。但依然有个问题没解决，那就是旧的缓存可能会覆盖新的缓存，因为我们没法保障新的缓存消息一定在旧的缓存消息产生之后再产生。考虑下面这个场景：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/2666b79dc2e3b9ac4d0d21c151a75776.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/2666b79dc2e3b9ac4d0d21c151a75776.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从上面可以看到，由于线程3的key<->v2消息先产生，所以它会被先消费，此时缓存的数据会变为v2, 然后缓存更新平台再处理key<->v1这条消息，从而导致v1覆盖缓存中的v2，出现旧值覆盖新值的问题。<br>
<br>在这里，我们引入了缓存版本的概念来解决这个问题，我们认为每条缓存的数据都应该有一个版本号（业务提供，例如可以是修改数据的时间戳，只要满足单调递增即可）。基于此，缓存的增、删、改操作全部基于这个版本号来进行判断是否执行操作。具体的判断逻辑，在后文介绍。<br>
<br><strong>缓存的增、删、改流程</strong><br>
<br><strong>删除缓存流程</strong><br>
<br>先看下面流程图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/23185465d4e74bdd1d7a29e18912f715.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/23185465d4e74bdd1d7a29e18912f715.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
 我们整个流程上是基于消息通知，这个消息生产的时机是只要业务删除了数据库中的数据就可以向缓存更新平台发送一条删除缓存消息。<br>
<br>从流程上可以看到，针对该消息的处理，流程里面并不是简单的删除一个key，而是将删除的内容标记一下存入缓存。这样做带来了如下的好处：<br>
<ul><li>能够避免缓存穿透；</li><li>能够避免缓存“复活”已经删除的数据；</li></ul><br>
<br>如果我们简单的删除缓存中的内容而不是将被删除的内容标记起来存入缓存，那么当出现下面这个场景时，缓存中就会长期存在已经删除的数据，从而导致数据使用方误认为该数据仍然有效。<br>
<br>首先假设现在某个key在缓存中不存在。线程先消费了删除该key的消息且删除的数据版本是v1，然后消费了存储缓存key<->v1的消息，这个时候就会将key<->v1写入缓存，但其实这个数据已经被删除了。<br>
<br>但即便将删除的内容放入缓存，考虑极端情况，仍然可能会有问题，考虑下面这个场景：<br>
<br>有两条邻近产生的消息：<br>
<br>消息1：删除key<->v1的缓存消息<br>
消息2：新增key<->v1的缓存消息<br>
<br>假设消费完消息1后，因为某种原因（如平台宕机或者消息队列出问题等等），消息2过了很久（缓存key已经过期）才被消费到，这时在缓存中存入该消息也会导致被删除的数据“复活”。所以针对这类情况，有两种措施：<br>
<ul><li>缓存永久有效</li><li>超过一定时间未处理的消息就不处理了（我们采取的方案）</li></ul><br>
<br>关于删除缓存消息中的版本，前文有提到，我们认为每条缓存数据都是有版本的。所以即便业务要删一条数据，那么被删的数据肯定也是有版本号的，而这个版本就是该条消息的版本。我们借助这个版本，就知道缓存中的数据是否是更新的版本，是否可以被覆盖并且被标记为删除了。<br>
<br><strong>新增&修改缓存流程</strong><br>
<br>新增缓存消息的处理流程和修改缓存消息的处理流程一致，见下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/360eaaa4717ea14a25764422709266f2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/360eaaa4717ea14a25764422709266f2.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
首先，消息的生产时机是：<br>
<br>新增缓存消息：<br>
<ul><li>业务往数据库中插入数据</li><li>业务流程因为缓存缺失导致直接访问到数据库的数据</li></ul><br>
<br>修改缓存消息：<br>
<br>业务修改了数据库中的数据<br>
<br>流程上可以看到，当缓存更新平台收到新增/修改缓存消息时，拿着消息中的key去查缓存，如果没有，则直接存入缓存；如果缓存中存在，则拿着缓存中的数据版本与消息的数据版本进行对比，如果消息中的数据版本更高（即更新），那么就可以安全覆盖缓存中的数据；反之，则不应该覆盖。通过这个流程，就可以很好的避免传统缓存更新里面经常出现的低版本数据覆盖缓存中高版本的数据。<br>
<br>新增&修改缓存流程与删除缓存流程大体一致，仅有一个区别点，如下：<br>
<br>新增&修改缓存：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/6f42150309da2e6f9c95f569b273e55a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/6f42150309da2e6f9c95f569b273e55a.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
删除缓存：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210326/6981a71adb4166020a86907c36ea5d7b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210326/6981a71adb4166020a86907c36ea5d7b.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
删除流程中关心的是消息中的版本是否大于等于缓存中的版本，而新增&修改缓存流程只关心消息中的版本是否大于缓存中的版本，为什么删除流程要关心版本相同的情况而新增&修改流程不关心呢？<br>
<br>针对删除，假设删除的数据对应的版本是3，而缓存中正好也有这个数据且数据版本也是3，这说明删除操作其实针对的是最新的数据，所以可以将缓存标记为删除态。<br>
<br>针对新增&修改，假设某条数据修改后，数据版本为3。此时缓存里面正好也有版本为3的数据，那么缓存中的这条数据会有下面两种情况：<br>
<br>1）该数据在缓存中被标记为删除态了（即被业务删除了该数据）<br>
<br>若此时写入缓存，会导致删除态数据重新“复活”<br>
<br>2）该数据处于正常状态<br>
<br>若此时写入缓存，没有任何意义。<br>
<br>综上，无论针对上述哪种情况，只要不对这条消息进行处理，就不会有任何问题。所以，修改流程只有当消息中的版本高于缓存中的版本时才设置缓存。<br>
<h4>如何保障消息一定会被处理？</h4> 由于整个平台依赖于消息队列中间件，那么如果消息队列中间件出了问题（如宕机/网络问题/消息投递失败等等）导致消费变得很慢或漏掉消息，怎么办？<br>
<br>前文提到，我们提供的缓存访问组件内部会将每条消息记录到业务DB。缓存更新平台通过业务提供的接口增量轮询该表，确保所有消息都被及时消费掉。通过这样的容错措施，确保不会因为单点故障导致缓存来不及更新。<br>
<h3>小结</h3>可以看到，通过上述的缓存访问组件和缓存更新平台，可以做到缓存与数据库数据的快速一致，从而既保障了性能同时又最大程度的降低了用户看到过期数据的可能性。<br>
<br>接下来，我们将继续迭代，解决1）减少缓存访问组件在业务代码上的侵入性；2）在缓存更新平台引入缓存key的分析机制，可以自动判定是否是热点key等问题。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/_RlOAvjfTINJrhwHUogs7Q" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/_RlOAvjfTINJrhwHUogs7Q</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            