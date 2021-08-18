
---
title: 'IM开发技术学习：揭秘微信朋友圈这种信息推流背后的系统设计'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57947953057948d291c84373cba0a4a8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 23:37:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57947953057948d291c84373cba0a4a8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文由徐宁发表于腾讯大讲堂，原题“程序员如何把你关注的内容推送到你眼前？揭秘信息流推荐背后的系统设计”，有改动和修订。</p>
<h1 data-id="heading-0">1、引言</h1>
<p>信息推流（以下简称“Feed流”）这种功能在我们手机APP中几乎无处不在（尤其是社交/社群产品中），最常用的就是微信朋友圈、新浪微博等。</p>
<p>对Feed流的定义，可以简单理解为只要大拇指不停地往下划手机屏幕，就有一条条的信息不断涌现出来。就像给牲畜喂饲料一样，只要它吃光了就要不断再往里加，故此得名Feed（饲养）。</p>
<p><strong>大多数带有Feed流功能的产品都包含两种Feed流：</strong></p>
<ul>
<li>1）一种是基于算法：即动态算法推荐，比如今日头条、抖音短视频；</li>
<li>2）一种是基于关注：即社交/好友关系，比如微信、知乎。</li>
</ul>
<p>例如下图中的微博和知乎，顶栏的页卡都包含“关注”和“推荐”这两种：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57947953057948d291c84373cba0a4a8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图中这两种Feed流，它们背后用到的技术差别会比较大。不同于“推荐”页卡那种千人千面算法推荐的方式，通常“关注”页卡所展示的内容先后顺序都有固定的规则，最常见的规则是基于时间线来排序，也就是展示“我关注的人所发的帖子、动态、心情，根据发布时间从晚到早依次排列”。</p>
<p>本文将重点讨论的是“关注”功能对应的技术实现：先总结常用的基于时间线Feed流的后台技术实现方案，再结合具体的业务场景，根据实际需求在基本设计思路上做一些灵活的运用。</p>
<h1 data-id="heading-1">2、本文作者</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f242b458a24d4cd3bd1e577af2cd7985~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>**徐宁：**腾讯应用开发工程师，腾讯学院讲师，毕业于上海交通大学。目前负责腾讯智慧零售业务的后端开发工作，有丰富的视频直播，自动化营销系统开发经验。</p>
<h1 data-id="heading-2">3、Feed流技术实现方案1：读扩散</h1>
<p>读扩散也称为“拉模式”，这应该是最符合我们认知直觉的一种技术实现方式。</p>
<p><strong>原理如下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f272ca44359c45fab166b32972803596~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如上图所示：</strong> 每一个内容发布者都有一个自己的发件箱（“我发布的内容”），每当我们发出一个新帖子，都存入自己的发件箱中。当我们的粉丝来阅读时，系统首先需要拿到粉丝关注的所有人，然后遍历所有发布者的发件箱，取出他们所发布的帖子，然后依据发布时间排序，展示给阅读者。</p>
<p><strong>这种设计：</strong> 阅读者读一次Feed流，后台会扩散为N次读操作（N等于关注的人数）以及一次聚合操作，因此称为读扩散。每次读Feed流相当于去关注者的收件箱主动拉取帖子，因此也得名——拉模式。</p>
<p><strong>这种模式：</strong></p>
<ul>
<li>1）好处是：底层存储简单，没有空间浪费；</li>
<li>2）坏处是：每次读操作会非常重，操作非常多。</li>
</ul>
<p><strong>设想一下：</strong> 如果我关注的人数非常多，遍历一遍我所关注的所有人，并且再聚合一下，这个系统开销会非常大，时延上可能达到无法忍受的地步。</p>
<p><strong>因此：</strong> 读扩散主要适用系统中阅读者关注的人没那么多，并且刷Feed流并不频繁的场景。</p>
<p><strong>拉模式还有一个比较大的缺点：</strong> 就是分页不方便，我们刷微博或朋友圈，肯定是随着大拇指在屏幕不断划动，内容一页一页的从后台拉取。如果不做其他优化，只采用实时聚合的方式，下滑到比较靠后的页码时会非常麻烦。</p>
<h1 data-id="heading-3">4、Feed流技术实现方案2：写扩散</h1>
<p><strong>据统计：</strong> 大多数Feed流产品的读写比大概在100:1，也就是说大部分情况都是刷Feed流看别人发的朋友圈和微博，只有很少情况是自己亲自发一条朋友圈或微博给别人看。</p>
<p><strong>因此：</strong> 读扩散那种很重的读逻辑并不适合大多数场景。</p>
<p>我们宁愿让发帖的过程复杂一些，也不愿影响用户读Feed流的体验，因此稍微改造一下前面方案就有了写扩散。写扩散也称为“推模式”，这种模式会对拉模式的一些缺点做改进。</p>
<p><strong>原理如下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f22f68fd55425b84d28b0c7bd5b342~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如上图所示：</strong> 系统中每个用户除了有发件箱，也会有自己的收件箱。当发布者发表一篇帖子的时候，除了往自己发件箱记录一下之外，还会遍历发布者的所有粉丝，往这些粉丝的收件箱也投放一份相同内容。这样阅读者来读Feed流时，直接从自己的收件箱读取即可。</p>
<p><strong>这种设计：</strong> 每次发表帖子，都会扩散为M次写操作（M等于自己的粉丝数），因此成为写扩散。每篇帖子都会主动推送到所有粉丝的收件箱，因此也得名推模式。</p>
<p><strong>这种模式可想而知：</strong> 发一篇帖子，背后会涉及到很多次的写操作。通常为了发帖人的用户体验，当发布的帖子写到自己发件箱时，就可以返回发布成功。后台另外起一个异步任务，不慌不忙地往粉丝收件箱投递帖子即可。</p>
<p>写扩散的好处在于通过数据冗余（一篇帖子会被存储M份副本），提升了阅读者的用户体验。通常适当的数据冗余不是什么问题，但是到了微博明星这里，完全行不通。比如目前微博粉丝量Top2的谢娜与何炅，两个人微博粉丝过亿。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5c03d3b32ce46e9ba57fbbe5b44791f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>设想一下：</strong> 如果单纯采用推模式，那每次谢娜何炅发一条微博，微博后台都要地震一次。一篇微博导致后台上亿次写操作，这显然是不可行的。</p>
<p><strong>另外：</strong> 由于写扩散是异步操作，写的太慢会导致帖子发出去半天，有些粉丝依然没能看见，这种体验也不太好。</p>
<p>通常写扩散适用于好友量不大的情况，比如微信朋友圈正是写扩散模式。每一名微信用户的好友上限为5000人，也就是说你发一条朋友圈最多也就扩散到5000次写操作，如果异步任务性能好一些，完全没有问题。</p>
<p><strong>关于微信朋友圈的技术资料：</strong></p>
<ul>
<li>1）《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-178-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-178-1-1.html" ref="nofollow noopener noreferrer">微信朋友圈海量技术之道PPT [附件下载]</a>》</li>
<li>2）《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-1569-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-1569-1-1.html" ref="nofollow noopener noreferrer">微信朋友圈千亿访问量背后的技术挑战和实践总结</a>》</li>
<li>3）《<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-177-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-177-1-1.html" ref="nofollow noopener noreferrer">架构之道：3个程序员成就微信朋友圈日均10亿发布量[有视频]</a>》</li>
</ul>
<h1 data-id="heading-4">5、Feed流技术实现方案2：读写混合模式</h1>
<p>读写混合也可以称作“推拉结合”，这种方式可以兼具读扩散和写扩散的优点。</p>
<p><strong>我们首先来总结一下读扩散和写扩散的优缺点：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df7e1c4172e74e87be371a2ff7a6a32c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>见上图：</strong> 仔细比较一下读扩散与写扩散的优缺点，不难发现两者的适用场景是互补的。</p>
<p><strong>因此：</strong> 在设计后台存储的时候，我们如果能够区分一下场景，在不同场景下选择最适合的方案，并且动态调整策略，就实现了读写混合模式。</p>
<p><strong>原理如下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48a76ac3f4f418b872dadc429703a4b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>以微博为例：</strong> 当何炅这种粉丝量超大的人发帖时，将帖子写入何炅的发件箱，另外提取出来何炅粉丝当中比较活跃的那一批（这已经可以筛掉大部分了），将何炅的帖子写入他们的收件箱。当一个粉丝量很小的路人甲发帖时，采用写扩散方式，遍历他的所有粉丝并将帖子写入粉丝收件箱。</p>
<p><strong>对于那些活跃用户登录刷Feed流时：</strong> 他直接从自己的收件箱读取帖子即可，保证了活跃用户的体验。</p>
<p><strong>当一个非活跃的用户突然登录刷Feed流时：</strong></p>
<ul>
<li>1）一方面需要读他的收件箱；</li>
<li>2）另一面需要遍历他所关注的大V用户的发件箱提取帖子，并且做一下聚合展示。</li>
</ul>
<p><strong>在展示完后：</strong> 系统还需要有个任务来判断是否有必要将该用户升级为活跃用户。</p>
<p>因为有读扩散的场景存在，因此即使是混合模式，每个阅读者所能关注的人数也要设置上限，例如新浪微博限制每个账号最多可以关注2000人。</p>
<p><strong>如果不设上限：</strong> 设想一下有一位用户把微博所有账号全部关注了，那他打开关注列表会读取到微博全站所有帖子，一旦出现读扩散，系统必然崩溃（即使是写扩散，他的收件箱也无法容纳这么多的微博）。</p>
<p><strong>读写混合模式下，系统需要做两个判断：</strong></p>
<ul>
<li>1）哪些用户属于大V，我们可以将粉丝量作为一个判断指标；</li>
<li>2）哪些用户属于活跃粉丝，这个判断标准可以是最近一次登录时间等。</li>
</ul>
<p>这两处判断标准就需要在系统发展过程中动态地识别和调整，没有固定公式了。</p>
<p><strong>可以看出：</strong> 读写结合模式综合了两种模式的优点，属于最佳方案。</p>
<p><strong>然而他的缺点是：</strong> 系统机制非常复杂，给程序员带来无数烦恼。通常在项目初期，只有一两个开发人员，用户规模也很小的时候，一步到位地采用这种混合模式还是要慎重，容易出bug。当项目规模逐渐发展到新浪微博的水平，有一个大团队专门来做Feed流时，读写混合模式才是必须的。</p>
<h1 data-id="heading-5">6、Feed流中的分页问题</h1>
<p>上面几节已经叙述了基于时间线的几种Feed流常见设计方案，但实操起来会比理论要麻烦许多。</p>
<p>接下来专门讨论一个Feed流技术方案中的痛点——Feed流的分页。</p>
<p>不管是读扩散还是写扩散，Feed流本质上是一个动态列表，列表内容会随着时间不断变化。传统的前端分页参数使用page_size和page_num，分表表示每页几条，以及当前是第几页。</p>
<p><strong>对于一个动态列表会有如下问题：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc8e266f7af4f1c99676a8572b01592~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如上图所示：</strong> 在T1时刻读取了第一页，T2时刻有人新发表了“内容11”，在T3时刻如果来拉取第二页，会导致错位出现，“内容6”在第一页和第二页都被返回了。事实上，但凡两页之间出现内容的添加或删除，都会导致错位问题。</p>
<p><strong>为了解决这一问题：</strong> 通常Feed流的分页入参不会使用page_size和page_num，而是使用last_id来记录上一页最后一条内容的id。前端读取下一页的时候，必须将last_id作为入参，后台直接找到last_id对应数据，再往后偏移page_size条数据，返回给前端，这样就避免了错位问题。</p>
<p><strong>如下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/621119d98da54285888d02098ac1c57c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>采用last_id的方案有一个重要条件：就是last_id本身这条数据不可以被硬删除。</p>
<p><strong>设想一下：</strong></p>
<ul>
<li>1）上图中T1时刻返回5条数据，last_id为内容6；</li>
<li>2）T2时刻内容6被发布者删除；</li>
<li>3）那么T3时刻再来请求第二页，我们根本找不到last_id对应的数据了，也就无法确认分页偏移量。</li>
</ul>
<p><strong>通常碰到删除的场景：</strong> 我们采用软删除方式，只是在内容上置一个标志位，表示内容已删除。</p>
<p>由于已经删除的内容不应该再返回给前端，因此软删除模式下，找到last_id并往后偏移page_size条，如果其中有被删除的数据会导致获得足够的数据条数给前端。</p>
<p>这里一个解决方案是找不够继续再往下找，另一种方案是与前端协商，允许返回条数少于page_size条，page_size只是个建议值。甚至大家约定好了以后，可以不要page_size参数。</p>
<h1 data-id="heading-6">7、Feed流技术方案在某直播应用中的实践</h1>
<h3 data-id="heading-7">7.1 需求背景</h3>
<p>本节将结合实际业务，分享一下实际场景中碰到的一个非常特殊的Feed流设计方案。</p>
<p>xx 直播是一款直播带货工具，主播可以创建一场未来时刻的直播，到时间后开播卖货，直播结束后，主播的粉丝可以查看直播回放。</p>
<p>这样，每个直播场次就有三种状态——预告中（创建一场直播但还未开播）、直播中、回放。</p>
<p>作为观众，我可以关注多位主播，这样从粉丝视角来看，也会有个直播场次的Feed流页面。</p>
<p><strong>这个Feed流最特殊的地方在于它的排序规则：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b087de922ef430f82ba467a6a121f45~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>解释一下这个Feed流排序规则：</strong></p>
<ul>
<li>1）我关注的所有主播：正在直播中的场次排在最前；预告中的场次排中间；回放场次排最后；</li>
<li>2）多场次都在直播中的：按开播时间从晚到早排序；</li>
<li>3）多场次都在预告中的：按预计开播时间从早到晚排序；</li>
<li>4）多场次都在回放的：按直播结束时间从晚到早排序。</li>
</ul>
<h3 data-id="heading-8">7.2 问题分析</h3>
<p>本需求最复杂的点在于Feed流内容融入的“状态”因素，状态的转变会直接导致Feed流顺序不同。</p>
<p><strong>为了更清晰解释一下对排序的影响，我们可以用下图详细说明：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9e9f73844df49c9a7f8f6b35248abf7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>上图中：</strong> 展示了4个主播的5个直播场次，作为观众，当我在T1时刻打开页面，看到的顺序是场次3在最上方，其余场次均在预告状态，按照预计开播时间从早到晚展示。当我在T2时刻打开页面，场次5在最上方，其余有三场在预告状态排在中间，场次3已经结束了所以排在最后。以此类推，直到所有直播都结束，所有场次最终的状态都会变为回放。</p>
<p><strong>这里需要注意一点：</strong> 如果我在T1时刻打开第一页，然后盯着页面不动，一直盯到T4时刻再下划到第二页，这时上一页的last_id，即分页偏移量很有可能因为直播状态变化而不知道飞到了什么位置，这会导致严重的错位问题，以及直播状态展示不统一的问题（第一页展示的是T1时刻的直播状态，第二页展示的是T4时刻的直播状态）。</p>
<h3 data-id="heading-9">7.3 解决方案</h3>
<p>直播系统是个单向关系链，和微博有些类似，每个观众会关注少量主播，每个主播会可能有非常多的关注者。</p>
<p>由于有状态变化的存在，写扩散几乎无法实现。</p>
<p><strong>因为：</strong> 如果采用写扩散的方式，每次主播创建直播、直播开播、直播结束这三个事件发生时导致的场次状态变化，会扩散为非常多次的写操作，不仅操作复杂，时延上也无法接受。</p>
<p><strong>微博之所以可以写扩散：</strong> 就是因为一条微博发出后，这篇微博就不会再有任何影响排序的状态转变。</p>
<p><strong>而在我们场景中：</strong> “预告中”与“直播中”是两个中间态，而“回放”状态才是所有直播的最终归宿，一旦进入回放，这场直播也就不会再有状态转变。因此“直播中”与“预告中”状态可以采用读扩散方式，“回放”状态采取写扩散方式。</p>
<p><strong>最终的方案如下图所示：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dc899426a8c48d39ab12530ee21783b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如上图：</strong> 会影响直播状态的三种事件（创建直播、开播、结束直播）全部采用监听队列异步处理。</p>
<p><strong>我们为每一位主播维护一个直播中+预告中状态的优先级队列：</strong></p>
<ul>
<li>1）每当监听到有主播创建直播时，将直播场次加入队列中，得分为开播的时间戳的相反数（负数）；</li>
<li>2）每当监听到有主播开播时，把这场直播在队列中的得分修改为开播时间（正数）；</li>
<li>3）每当监听到有主播结束直播，则异步地将播放信息投递到每个观众的回放队列中。</li>
</ul>
<p><strong>这里有一个小技巧：</strong> 前文提到，直播中状态按照开播时间从大到小排序，而预告中状态则按照开播时间从小到大排序，因此如果将预告中状态的得分全部取开播时间相反数，那排序同样就成为了从大到小。这样的转化可以保证直播中与预告中同处于一个队列排序。预告中得分全都为负数，直播中得分全都为正数，最后聚合时可以保证所有直播中全都自然排在预告中前面。</p>
<p><strong>另外：</strong> 前文还提到的另一个问题是T1时刻拉取第一页，T4时刻拉取第二页，导致第一页和第二页直播间状态不统一。</p>
<p>解决这个问题的办法是通过快照方式：当观众来拉取第一页Feed流时，我们依据当前时间，将全部直播中和预告中状态的场次建立一份快照，使用一个session_id标识，每次前端分页拉取时，我们直接从快照中读取即可。如果快照中读取完毕，证明该观众的直播中和预告中场次全部读完，剩下的则使用回放队列进行补充。</p>
<p><strong>照此一来，我们的Feed流系统，前端分页拉取的参数一共有4个：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6a9a4c6c18b4dcead818bce6f7b6791~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>每当碰到session_id和last_id为空，则证明用户想要读取第一页，需要重新构建快照。</p>
<p><strong>这里还有一个衍生问题：</strong> session_id的如何取值？</p>
<p><strong>答案是：</strong></p>
<ul>
<li>1）如果不考虑同一个观众在多端登录的情况，其实每一位观众维护一个快照id即可，也就是直接将系统用户id设为session_id；</li>
<li>2）如果考虑多端登录的情况，则session_id中必须包含每个端的信息，以避免多端快照相互影响；</li>
<li>3）如果不心疼内存，也可以每次随机一个字符串作为session_id，并设置一个足够长的过期时间，让快照自然过期。</li>
</ul>
<p><strong>以上设计：</strong> 其实系统计算量最大的时刻就是拉取第一页，构建快照的开销。</p>
<p>目前的线上数据，对于只关注不到10个主播的观众（这也是大多数场景），拉取第一页的QPS可以达到1.5万。如果将第二页以后的请求也算进来，Feed流的综合QPS可以达到更高水平，支撑目前的用户规模已经绰绰有余。如果我们拉取第一页时只获取到前10条即可直接返回，将构建快照操作改为异步，也许QPS可以更高一些，这可能是后续的优化点。</p>
<h1 data-id="heading-10">8、本文小结</h1>
<p><strong>几乎所有基于时间线和关注关系的Feed流都逃不开三种基本设计模式：</strong></p>
<ul>
<li>1）读扩散；</li>
<li>2）写扩散；</li>
<li>3）读写混合。</li>
</ul>
<p><strong>具体到实际业务中，可能会有更复杂的场景，比如本文所说的：</strong></p>
<ul>
<li>1）状态流转影响排序；</li>
<li>2）微博朋友圈场景中会有广告接入、特别关注、热点话题等可能影响到Feed流排序的因素。</li>
</ul>
<p>这些场景就只能根据业务需求，做相对应的变通了。（本文同步发布于：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.52im.net%2Fthread-3675-1-1.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.52im.net/thread-3675-1-1.html" ref="nofollow noopener noreferrer">www.52im.net/thread-3675…</a> ）</p></div>  
</div>
            