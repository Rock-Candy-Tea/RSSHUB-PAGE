
---
title: 'App数据持久化管理设计'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/554b5fd2e0f541d4821527f40c7bfec7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 17:58:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/554b5fd2e0f541d4821527f40c7bfec7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p>在迭代过程中，我们碰到了不少持久化相关的问题，经历了数据模型逻辑爆炸，数据库API使用混乱，以及业务对数据库框架产生了强依赖。前两者通过不断的抽象整理，收敛的还算可以，但数据库框架的强依赖导致我们在做框架切换时遇到了大麻烦。</p>
<p>为了解决持久化遇到的问题，我在原有架构基础上增加DAO层设计，解耦数据库框架依赖，提升数据库查询与写入性能。</p>
<h2 data-id="heading-1">方案设计</h2>
<h3 data-id="heading-2">持久化方案1.0</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/554b5fd2e0f541d4821527f40c7bfec7~tplv-k3u1fbpfcp-zoom-1.image" alt="持久化方案1.0" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Data Observer，基于Realm的数据集合变更通知做的观察器，当数据集合变更时，为UI数据源提供刷新回调，或者触发其他的数据操作。</p>
<p>Data Hander，用于数据入库前的预处理，比如Json String的预解析，或者触发其他的数据操作。</p>
<p>早期选型使用了Realm作为数据库底层，优势是Realm提供的ORM简单易用，支持跨平台方便统一逻辑。同时项目初期，也没有数据模型上的历史包袱。</p>
<p>数据库CRUD API由业务层直接调用，优点是在快速迭代中节约工作量，业务端可以充分使用数据库框架特性。缺点是随着项目体量的上升，五花八门的API用法无法统一管理，对数据库框架产生了强依赖。</p>
<p>随着单表数量不断上升，IO量不断上升，Realm框架逐渐出现瓶颈，也没能找到可行的解决方案，综合考虑后决定引入稳定的Sqlite来替换需要承载高IO的Realm数据库。</p>
<p>简单的提下Realm，Realm支持事务，数据版本管理，数据集合变更通知，表结构半自动迁移等比较方便的特性。</p>
<p>优势：</p>
<ol>
<li>
<p>数据版本管理，即多个线程中，相同的表数据，Realm内核会帮你做数据同步。类似于Git仓库的逻辑，每个线程都是一个分支，每个分支上会做不同的commit，Realm能帮你把不同的分支最终都合并到mater上，保证数据的一致性。</p>
</li>
<li>
<p>数据集合变更通知，Realm支持监听表数据的增删改变化，比如创建一个Person表的Observer对象，当Person表新增了数据时，Observer即可获得到变更的数据集合。或者监听一个Person对象，当数据库中Person的字段发生变化，Observer也能收到具体变更了什么字段。</p>
</li>
</ol>
<p>事与愿违，Realm作为一个较新的数据库框架，在使用过程中也是频频踩坑。</p>
<ol>
<li>
<p>首先Realm没有索引，在检索大量数据时力不从心，单表数据超过500M的时候，查询性能明显下降。</p>
</li>
<li>
<p>同时Realm的数据模型是无法跨线程使用的，线程切换时，需要对数据进行Copy操作，有一定的性能占用。</p>
</li>
<li>
<p>多线程频繁写入时，Realm偶尔会出现数据库文件写坏的情况（<code>Assertion failed: header.m_top_ref[1] == 0 with (header.m_top_ref[1], get_file_path_for_assertions())</code>），提了issues也未能得到解决方案。</p>
</li>
<li>
<p>当表数据量过大，频繁写入时，Realm偶尔会出现mmap溢出的问题（<code>Error Domain=io.realm Code=9 "mmap()failed: Cannot allocate memory size:1455652864 offse</code>）。</p>
</li>
<li>
<p>Realm的数据集合变更通知有概率会丢失，Realm的多线程的数据同步时机不可控。</p>
</li>
</ol>
<p>综上所属，个人认为Realm在重度IO的项目中并不是很适合，首先填坑会占用大量时间，其次Realm相关文档确实少，很多问题再Github的issues上有记录，但官方也不能给出解决方案，最后填坑变挖坑。</p>
<h3 data-id="heading-3">持久化方案2.0</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8c18fe52ccc4104bd5c1e2a5ff0565c~tplv-k3u1fbpfcp-zoom-1.image" alt="持久化方案2.0" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">抽象数据库协议</h4>
<p>抽象数据库协议（Database Protocol）需要包含基本的CRUD API，还需要实现Where，Order By，Limit，Transaction等数据库基本功能。</p>
<p>我们的项目使用Sqlite与Realm两种数据库框架，使用抽象数据库协议可以解决数据库框架的强依赖，业务层只需实现抽象数据库，那么以后不论数据层是数据库框架变更，或者多版本数据库使用，都可以做到无缝切换。</p>
<h4 data-id="heading-5">数据持久化管理器</h4>
<p>设计数据持久化管理器（Storage Manager）的目的是减少数据库查询的次数，以及减少数据库写入时对业务层造成的逻辑影响（如果业务层直接使用数据库API，则在处理业务逻辑的同时，还需要处理数据库API的各类异常情况）。</p>
<p>简单理解，数据持久化管理器是一个缓存池管理，提供了与数据库相同的CRUD API。其内部实现了将新增缓存数据入库，以及从数据库中获取需要的数据转入缓存等能力。</p>
<p>除去基本的CRUD，还实现了数据预处理插件以及数据变更观察器的能力。</p>
<p>数据预处理插件（Data Handler），当业务层将一个新数据模型写入到持久化管理器后，相关联的预处理插件即会生效。在插件中，可以做一些关联业务处理，比如当用户的名字更新时，同步触发会话名称的更新。</p>
<p>数据变更观察器（Data Observer），当持久化管理器将缓存数据写入到数据库后，将通知数据变更观察器。观察器可以得知当前数据源是发生更新、新增还是删除。同时观察器支持通过Where规则对数据源进行筛选，比如在聊天界面，ViewModel只关心当前会话的消息数据，通过Where规则筛选，当前会话数据发生变更时，ViewModel将收到通知回调，立即刷新消息气泡UI。</p>
<h4 data-id="heading-6">缓存模块</h4>
<p>用于支撑数据持久化管理器的数据缓存能力（Storage Cache），实现CRUD API。</p>
<p>根据不同的场景，缓存模块分为有序型，无序型。</p>
<p>无序型，提供给对数据排列顺序没有要求的数据源使用。</p>
<p>有序型，提供给对数据排泄顺序有要求的数据源使用，可以指定排序规则，当变更发生时对数据源重新排序。比如会话列表需要根据创建时间倒序排列，群组列表需要根据创建时间升序排列。</p>
<p>缓存还需实现清理策略，避免对内存的不合理占用，比如iOS端收到系统内存预警时，会将缓存进行释放。</p>
<h4 data-id="heading-7">数据流向</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a01a3ee7e324a44865713ab3e786b34~tplv-k3u1fbpfcp-zoom-1.image" alt="数据流向" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图举例了网络数据从获取到入库，到UI刷新的整个流程。</p>
<ol>
<li>数据请求器接收到IM消息，转换为数据模型，并将数据存入持久化管理器。</li>
<li>持久化管理器将数据存入持久化缓存，同时触发数据预处理插件（比如更新会话模型的最近聊天记录）。</li>
<li>持久化管理器通过调用抽象数据库，将IM消息数据入库。</li>
<li>完成数据存储后，数据变更通知中心将变更通知给观察器（比如播放收到新消息的提示音）。</li>
<li>UI数据源收到数据通知，并将数据模型转换成UI模型，最终刷新UI。</li>
</ol>
<p>PS：当数据存储到达高IO状态时，UI会由于用了通知刷新的逻辑，也会频繁被触发刷新，要注意对UI刷新的节流。</p></div>  
</div>
            