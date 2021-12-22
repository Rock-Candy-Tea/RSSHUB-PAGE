
---
title: '从0开始设计Twitter系统架构'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/e939b1343aae112cf0746565eb731631.png'
author: Dockone
comments: false
date: 2021-12-22 02:34:31
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/e939b1343aae112cf0746565eb731631.png'
---

<div>   
<br>【编者的话】Twitter是全球最大的社交网络之一，如果让我们从0开始设计twitter的系统架构，该怎么做呢？有哪些服务是必须的？有哪些点需要提前考虑？这篇文章简单介绍了设计类twitter系统的思路并在最后给出了参考设计。原文：<a href="https://medium.com/interviewnoodle/twitter-system-architecture-8dafce16aec4">Twitter System Architecture</a>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/e939b1343aae112cf0746565eb731631.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/e939b1343aae112cf0746565eb731631.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Twitter是全球领先的在线社交网络服务，用户可以在这里发布和阅读被称为“推文（tweets）”的短消息。在系统架构设计面试过程中，当被问及如何设计Twitter时，大多数候选人都会将其设计为单体服务。然而，将Twitter这样的大型服务设计为单体，表明候选人缺乏设计分布式系统的经验。从微服务甚至lambda（或函数）的角度来设计分布式系统在今天是很正常的选择。目前的趋势是，没有人会将新服务设计为单体，公司正逐渐将其庞大的单体服务转换为一组微服务。因此，候选人应该以微服务的方式设计Twitter。<br>
<h3>功能需求</h3><ol><li>用户可以发布或分享新的推文（tweet）</li><li>每条推文最多不超过140个字符</li><li>用户可以删除推文，但不能更新/编辑发布的推文（写操作）</li><li>户可以标记喜欢的推文（写操作）</li><li>用户可以关注或取消关注另一个用户（写操作），关注一个用户意味着用户可以看到其他用户在他的时间线上的推文</li><li>可以生成两种类型的时间线（读操作），用户时间线由他最后N个推文组成，主页时间线由他正在关注的用户的热门推文按照时间降序生成</li><li>用户可以根据关键字搜索推文（读操作）</li><li>用户需要有一个帐户来发布或读取推文（暂时使用外部身份服务）</li><li>用户可以注册和删除帐户</li><li>Twitter支持包含文字和图片/视频的推文，但在我们当前的设计中，将只支持文本</li><li>分析/监视服务，以确定其负载、运行状况和功能</li><li>分析还可为用户提供关于关注谁、推文通知、热门话题、推送通知和分享推文的意见或建议</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/3eaaa0d991d9d293fd786be6d862320e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/3eaaa0d991d9d293fd786be6d862320e.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>非功能需求</h3><ol><li>服务的高可用是最重要的需求，这意味着用户可以在自己的主页时间线上阅读推文，而感受不到任何停顿</li><li>生成时间线的时间最长不得超过半秒</li><li>不需要强一致性，只需要最终一致性，可以使用关键词数据库用于搜索基于关键词的推文</li><li>随着用户和推文的增加，系统负载也在增加，因此系统应该具有可伸缩性</li><li>持久化用户数据</li></ol><br>
<br>现在我们来做一些计算。<br>
<ul><li>日活跃用户平均请求/天 = 150M*60/86400 = 100k/秒</li><li>峰值用户 = 平均并发用户* 3 = 300k</li><li>三月内最大峰值用户数 = 峰值用户数*2 = 600k</li><li>读QPS = 300k</li><li>写QPS = 5k</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/6129cc1e9990b40e2e0142874d6836be.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/6129cc1e9990b40e2e0142874d6836be.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>twitter服务的概要设计</h3>由于系统的复杂性，可以将其划分为若干个服务，其中包括若干个微服务。<br>
<ol><li>推文服务（Tweet service）</li><li>用户时间线服务（User timeline service）</li><li>扇出服务（Fanout Service）</li><li>主页时间线服务（Home timeline service）</li><li>社交网络服务（Social graph service）</li><li>搜索服务（Search service）</li></ol><br>
<br>下面是Twitter服务中不同逻辑组件或微服务架构。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/d6d8eaf374735f698591b36e237803b8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/d6d8eaf374735f698591b36e237803b8.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>twitter服务的详细设计</h3>所有微服务都可以被称为模块。<br>
<h4>推文服务（Tweet service）</h4><ul><li>接收用户推文，转发用户推文到关注者时间线和搜索服务</li><li>存储用户信息，推文信息，包括用户的推文数量以及用户喜欢的状态</li><li>包括应用服务器、分布式的内存缓存以及后端的分布式数据库，或者使用直接由数据库（例如Redis）支持的内存缓存</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/f9bf33bb631ca99ebe73809b251618e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/f9bf33bb631ca99ebe73809b251618e7.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后我们看一下tweet服务的数据库表结构。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/46bbf5f317917311662687007d769926.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/46bbf5f317917311662687007d769926.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
用户（Users）表包含用户的所有信息，推文（Tweet）表存储所有推文，Favorite_tweet表存储了喜欢的推文记录，也就是说，每当用户喜欢一条推文时，就会在Favorite_tweet表中插入一条记录。<br>
<h4>生成唯一的推文Id</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/17e70207b1bc1345769dff954b5ee2b1.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/17e70207b1bc1345769dff954b5ee2b1.jpeg" class="img-polaroid" title="7.jpeg" alt="7.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
当用户调用postTweet()时，调用会发送给应用服务器。应用服务器为该推文生成一个唯一的id，同样的机制也可以用来为推文生成短URL。另一个方式是基于应用服务器的UUID（Universally unique identifier）。推文ID生成后，应用服务器将该推文插入分布式缓存和数据库的tweet表中。由于需要在执行推文的创建/更新/删除操作的同时更新缓存和数据库，所以我们使用缓存透写机制。<br>
<h4>可扩展性设计</h4>我们可以将分布式缓存和数据库划分为多个分区和副本。<br>
<ul><li>基于用户ID分片</li><li>基于推文ID分片</li><li>基于用户ID和推文ID进行两层/级别分片</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/d710a76e52e64378ea08382f7caa4a87.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/d710a76e52e64378ea08382f7caa4a87.jpeg" class="img-polaroid" title="8.jpeg" alt="8.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/59a6eaef6d68695edcd12e1ad11edcee.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/59a6eaef6d68695edcd12e1ad11edcee.jpeg" class="img-polaroid" title="9.jpeg" alt="9.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>社交网络服务（Social graph service）</h4><ul><li>实现Following API，跟踪用户之间的关注关系</li><li>包括应用服务器、分布式缓存和数据库</li><li>用于存储用户关系的数据库表结构</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/4db40df55e5168a9bc70fb2f0173ca79.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/4db40df55e5168a9bc70fb2f0173ca79.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Following API：<br>
<ul><li>将被关注用户的时间线异步合并到关注者的信息事件流中</li><li>取消关注一个用户后，从关注者的事件流中异步删除他的推文</li><li>异步的从信息事件流中挑选推文</li><li>之所以需要异步操作，是因为这个过程比较慢，而用户在关注和取消关注其他用户时，希望很快得到反馈</li><li>异步的缺点是用户在取消关注后，如果刷新信息事件流，会发现这些信息仍然存在，但最终它们会被删除</li></ul><br>
<br><h4>用户时间线服务（User timeline service）</h4><ul><li>返回用户的时间线，以降序排列的方式包含用户所有推文。此服务可用于主页时间线或其他用户的时间线。</li><li>该服务包括应用服务器和分布式内存缓存，但没有涉及该服务的数据库。</li><li>用户时间线是使用包含用户推文链接列表的数据结构设计的</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/1a21f911036b50b39b0eb1e82ea3c526.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/1a21f911036b50b39b0eb1e82ea3c526.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>当用户发布一条推文时，tweet服务调用用户时间线服务，将该推文插入到用户时间线的推文列表顶部，运算复杂度为O(1)。</li><li>此外，分析仪表板可以配置参数K，表示可以保留的推文个数，K默认为1000，表示保留用户时间线轴中的最后K条推文。</li><li>在用户时间线列表中，推文按creationTime（创建时间）降序存储。当用户时间线列表达到最大K条推文时，最老的条目将被删除。</li></ul><br>
<br><h4>扇出服务（Fanout Service）</h4><ul><li>将新推文转发到搜索和主页时间线服务，以及其他组件/微服务，比如趋势服务或通知服务</li><li>由多个分布式队列组成</li><li>当用户发送一条推文消息时，该服务把消息放入推文队列，社交网络服务必须获得用户的关注者列表，并在第二组队列中插入尽可能多的消息。对于名人用户来说，他们拥有非常多的粉丝，其粉丝数甚至超过了每次推送的阈值。那么，如何处理这个问题呢?</li><li>该服务是一个先进先出的任务队列列表，处理共享相同列表的任务，并在完成后反馈给队列服务器。队列服务器是异步任务的重要组成部分，其执行的任务可能不会立即收到响应，但却能够保证最终一致性。</li></ul><br>
<br><h4>主页时间线服务（Home timeline service）</h4><ul><li>显示用户的主页时间线</li><li>包括来自其他关注的用户的推文，按照推文的creationTime（创建时间）降序显示。</li><li>其设计类似于用户时间线服务。</li><li>但是比用户时间线服务稍微复杂一点，因为用户将插入最新的推文，并且当推文数量超过K值时需要删除最老的推文，如果用户关注了很多其他用户，服务还需要一些机制来给不同关注用户的推文赋予不同的权重。</li></ul><br>
<br><h4>搜索服务（Search service）</h4><ul><li>为用户提供搜索查询服务</li><li>扇出服务将推文传递给搜索服务</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/7b69b7d1af4fb02efade52a554b36ce0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/7b69b7d1af4fb02efade52a554b36ce0.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Ingester（或ingestion engine）：给推文标记上许多标签、术语或关键字。例如这条推文：“我想成为像亚马逊的杰夫·贝索斯一样非常富有的人”，它会过滤掉那些在搜索中没有用的词。除了杰夫·贝索斯（Jeff Bezos）和亚马逊（Amazon），所有其他词都将被丢弃。Ingester可以通过配置或数据库获得词汇表。</li><li>一个叫做“词根提取（stemming）”的过程对剩下的单词进行分析，以确定它们的词根。Stemming是处理词干、词根或词根的词形变化(或派生)的过程。因此，会在数据库中保存一个查找表。这种方法的优点是可以简单、快速、轻松的处理异常。缺点是新的或不熟悉的单词即使是完全符合规则的，也不会被处理。</li><li>传递到搜索索引</li><li>搜索索引微服务将创建反向索引，并存储从内容(如单词)到其所在文档或一组文档中的位置的术语映射索引，在我们的例子中，这是一个或一组推文。</li><li>Blender服务：在twitter平台上为用户提供搜索查询。当请求搜索查询时，首先确定搜索条件，然后进行词干分析，最后使用词根在术语的倒排索引上运行搜索查询。</li></ul><br>
<br><h4>照片和视频</h4><ul><li>使用NoSQL数据库</li><li>媒体文件（使用文件系统）</li><li>数据表格式</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/17817fd98a8e5fca05a7973d2193039a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/17817fd98a8e5fca05a7973d2193039a.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Twitter的网络</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/f8ca7839ce0d87ce507bd3139ec595b7.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/f8ca7839ce0d87ce507bd3139ec595b7.jpeg" class="img-polaroid" title="14.jpeg" alt="14.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Twitter的最终详细设计</h3>系统设计：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/88fe98c7f9a44894fab29ace63e3823f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/88fe98c7f9a44894fab29ace63e3823f.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
数据架构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211219/845e01ee48177b18957cb494e860d0a9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211219/845e01ee48177b18957cb494e860d0a9.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>译文链接：<a href="https://mp.weixin.qq.com/s/v08_YF78Im-Z_Qy8iX3yMQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/v08_YF78Im-Z_Qy8iX3yMQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            