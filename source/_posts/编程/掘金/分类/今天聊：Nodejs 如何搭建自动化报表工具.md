
---
title: '今天聊：Node.js 如何搭建自动化报表工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 06:11:28 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端早早聊大会，与掘金联合举办。加 codingdreamer 进大会技术群，赢在新的起跑线。</p>
<hr>
<p>第二十七届|前端 Flutter 专场，了解 Web 渲染引擎|UI 框架|性能优化，6-5 下午直播，6 位讲师(淘宝/京东/闲鱼等)，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image" alt="大会海报.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<h2 data-id="heading-0">正文如下</h2>
<blockquote>
<p>本文是第十五届 - 前端早早聊报表专场，也是早早聊第 107 场，来自 宋小菜-智哥 的分享。</p>
</blockquote>
<h2 data-id="heading-1">一、SQL 是编程吗？</h2>
<h4 data-id="heading-2">SQL是怎么诞生的</h4>
<p>在讨论 SQL 是编程之前，我们先理清楚什么是 SQL，或者说 SQL 是怎么诞生的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c30666e37f954234948d0404261d11f0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在远古时代，最早初代数据库有两个，一个是层次型数据库，换成今天的说法也可以叫做树型数据库，既然叫树状数据库，就和我们现在接触的树状模型差不多。</p>
<p>所以这个数据的弊端也是很明显的，就是实际关系中，很多实体间的关系不是一对多的，而是多对多的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c8e94d113e1451ab4c4479e4ef8d225~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外一个就是网状模型，相较树状模型，它可以描述现实中的复杂关系，不过这个问题也相对明显，就是这个网会变得原来越复杂，维护使用的成本会越来越高。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ad2269016349a586190d37e2eaee25~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>后来有个叫 Codd 的老博士发布一篇论文，里面讲了通过关系代数去描述数据间的关系。</p>
<p>那我们先看下这个关系模型是怎么描述的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b501930e73749258d32ea1cc8f7ef5b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样看上去是不是一脸懵逼，所以这个门槛很是高的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43cc4d3b42934809bedd5c75aad40af0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是我们如果翻译成这样是不是很好懂了，基本上就很接近我们自然语言了吧。</p>
<p>这就是 Codd 的 SQL 模型最关键的两个原则，关系代数和关系演算。一个是基于集合的运算，用现在的 SQL 表示的话就是 JOIN 操作，另一个是元组演算和域演算，就比如 > = < 这样的逻辑运算。</p>
<h2 data-id="heading-3">二、关系型数据库管理系统</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/269e172b73fe4d2cbe0f18fbb637011a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后 System R 就诞生，不过由于这是实验室的产物，所以后来 IMB 做的 DB2 这些都是后话了，但是我们可以大致窥见最早的关系型数据库是怎么来的，以及怎么实现的。</p>
<p>我的猜想就是底层一个文件系统，中间是关系模型，上层是解析器，最上层就是 SQL，所以我们可以得出一个结论，SQL 是一个帮助我们管理数据库文件系统的计算机语言。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3be426142f9f4e648acbfe3b28994b68~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好，现在我们知道什么是 SQL 了，那接下来我们看下 SQL 是否已经过时了，毕竟作为一个出来 3、4 十年的标准，很难保证他是不是已经过时了，就比如说 NoSQL 的诞生，因为现在很多数据其实都是非结构化的或者半结构化的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472d4be8ec0a46dc92b1d7eed11cc397~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是这里有最新的编程语言排行榜，可以看到 SQL 还是排在前 10 的，这里我想的话主要是简单，其次它是声明式的，也就是写 SQL 的人不用去具体关心底层实现逻辑，只要描述清楚需要什么就可以了，参考一下身边有多少非程序员会 SQL 的数量就可以了。</p>
<h2 data-id="heading-4">三、架构演进与 SQL</h2>
<p>接下来我想聊聊关于架构的演进与 SQL 的一些事情。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccf8c664e31d44179d87b35f9af5bd37~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ccef502f93f44a5b12547b9f38b1f9e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们知道所有的应用都是从小到大，比如说一个网站，最早的时候也都是小网站，那个时候一般的架构是服务和数据库都放一起，后来慢慢的把服务和数据分离，再往后用户变多了，服务器性能开始慢慢跟不上了，这个最早是通过纵向扩展的方式来解决的，说白了就是升服务器配置。</p>
<p>这样做的弊端也很明显，因为服务器配置越往上升，性价比就会越来越低，其次这种做法是有极限的，后来渐渐的有了微服务的解决方式，但是你服务拆到了多个服务器上，服务的上限是提高了，可这些服务用的都是同一个数据库，数据库的性能没有提高也是白搭，后来有了分布式数据库，以及 OLAP。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc3f8e5a00fa4e5ab48775ca6d9ec3e3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>分布式数据库目前一共有 3 种架构：</p>
<ol>
<li><strong>share-disk</strong>：每一个 CPU 使用自己的私有内存区域，通过内部通讯机制直接访问所有磁盘系统；</li>
<li><strong>share-nothing</strong>：每一个 CPU 都有私有内存区域和私有磁盘空间，而且 2 个 CPU 不能访问相同磁盘空间， CPU 之间的通讯通过网络连接；</li>
<li><strong>share-memory</strong>：多个 CPU 共享同一片内存，CPU 之间通过内部通讯机制（interconnection network）进行通讯。</li>
</ol>
<p>1 和 3 都是一台机器装做很多台机器的样子，后者是很多台机器装做 1 台机器的样子。</p>
<p>然后我们讲讲分布式数据库与 SQL 间的关系：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7265dba634bf470db270425375f88ca1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最早在 03 年的时候谷歌发了一个 Paper 叫 GFS 即 Google File System，里面就是关于谷歌内部怎么实现的一个分布式文件系统，接着在 04、06 分别发 MapReduce 和 GigTable 的 Paper，MapReduce 就是分布式计算，BigTable 就是分布式的数据管理系统。谷歌把这三架马车放出来之后，这个社区的人就很兴奋，因为终于有解决方案了，然后就照着 Paper 实现，慢慢就形成了现在的 Hadoop 生态，这里面最重要的目前就是 HDFS，也就是 GFS 的社区版，其它很多相关的东西都是以这个为基石实现的，比如 Kafka，Druid 等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c57e158d8be04d759509b35e7f4a368c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一开始用这套查数据的时候都是通过 MapReduce 来查数据，但是 MapReduce 又很复杂，你要写很多代码来实现，很多人都觉得麻烦，这个时候今天话题的主角 SQL 又参与进来了，就在 MapReduce 之上封装了一套 SQL 的实现，所以用户其实就可以通过 SQL 来写 MapReduce 的代码，这个就是我们常听说的 Hive 了。</p>
<p>再往后因为 MapReduce 就写在磁盘上，有人就嫌弃它慢，就搞了个 Spark，利用内存提高数据的读写速度，以及其它的优化，比如动态生成执行计划这样的操作，同样的 Spark 也实现了 SQL，调的时候用 spark.sql 就可以了。</p>
<p>因为最早的 Spark 只能做离线数据的加工，所以后来有了很多做实时的，不过这里面目前最活跃还是 Flink，你会发现同样的，Flink 也是支持直接写 SQL 的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7170b69c3e2437393b2287ad8312c55~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了这些之外的，还出来了一些新的数据库和 Hive 工具，比如说 PrestoSQL/PrestoDB，同样的这类工具也是支持 SQL 的，原理和 Spark 类似，通过词法分析、语义分析、执行计划生成、优化执行计划、执行计划分段等几个步骤，让用户可以拿到自己想要的数据。<a href="https://mp.weixin.qq.com/s?__biz=MzI5MDEzMzg5Nw==&mid=2660400264&idx=1&sn=ebff65980ef45f7dffea1e5ec7d51fdc&chksm=f7425e6ec035d778dcc5704babe5241d8c80f3d21059434b00d8d4c46d9ce0bd232467ec92a6&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">link</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9fa8ca77073447ead1ffadc20bf3b92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后看一下 TiDB 概述，TiDB 主要有三个部分组成 TiDB、TiKV 还有 PD。TiDB 你可以看做类似前面说的能跑 SQL 的 MapReduce，PD 是用来调度的，同时还是你数据库的字典，帮你管理原数据，TiKV 可以看成 HDFS。</p>
<p>到目前为止我们可以看到，在 OLAP 场景下，绝大多数查询任务你都可以通过 SQL 实现，那么其实对于我们来说，只要给用户一个 SQL 的输入途径，在加上一个中间层的加工，那么基本就可以满足目前绝大多数数据需求了。</p>
<h2 data-id="heading-5">四 、项目实践</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95d56a7b544445bb90104f663fb4bf9a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
前面讲完了 SQL 目前的应用，现在来讲讲项目实践。</p>
<h4 data-id="heading-6">数据类型</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4078110b8ee847d8a58ddfd1c5c46f12~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先在做项目之前需要对数据有个基本概念的认知，其中最基础的数据类型的认知。现在数据类型主要分成 4 类，名称数据，顺序数据，等比数据和等距数据，等距的话，我们基本很少用到，所以这里就不讨论了。</p>
<p>所谓的名称数据或者说分类数据就是一堆离散没有什么逻辑关系的数据，比如城市名称，人名等，顺序数据就是在带有逻辑关系的名称数据，比如大杯/中杯/小杯或者 "2020-10-10" / "2020-10-11" 这样的时间序列，而等比数据就是身高、体重这样常用作度量的。</p>
<p>有了这些基本概念之后在画图表的时候你就可以更加明确我这组数据哪些字段是用作维度数据的，哪些字段是作为指标数据的。比如在一般情况下名称数据/顺序数据就可以作为 X 轴，而 Y 轴的值其实就是等比数据字段经过前面的维度聚合得出的结果。</p>
<h4 data-id="heading-7">数据存储</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67b161027d2046ab9405c06f6e57975e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24b11dda26fb49ca988e00c0ca61fa47~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>了解了上面的基本概念之后，再看看我们在数据存储这一块是怎么做的，一般情况下我们会把表分实体表、维表、事实表以及聚合表。</p>
<p>实体表顾名思义，就是我们现实中实体的数据映射，比如用户表里面就是存你的用户基本信息，一些基础属性。维表的话就是存的维度信息的表，比如城市表这样，作为维度数据。事实表是记录一些事实信息的表，比如记你的用户下单记录订单表。聚合表就是前面几种表通过指定维度聚合以及指标聚合算出来的结果表。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c038e907ab844577b47de9de40b27187~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，现在到实际服务设计的部分，一般来说，做一个可视化的 SQL 编辑器的话，可以有两种方式，一种是以富文本输入框的形式做一个 Web 版 SQL Editer，直接让用户在富文本 SQL 编辑器里面写 SQL。</p>
<p>另外一种就是把 SQL 编程转换成 OOP，从而实现可视化 ORM 的编辑操作，因为我们可以把每个对象，比如 select 哪些字段，这样的操作直接转换成可视化的多选框之类，让用户直接操作选择。</p>
<h4 data-id="heading-8">定时任务</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/128f8f8c30b44edaae5fb8861f4d3c7b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在有了 SQL 的输入与保存服务之后，你可能还需要一些定时任务服务，让你可以有办法拿到一些辅助数据让前端更好的实现展示与计算等。比如需要一个定时任务去同步你数据源的数据，去拿到数据源里面所有的表，以及所有的表的字段和表字段的类型等等，方便你去做你自己这个服务的数据字典，这样的话，当用户写完一个 SQL，数据源返回数据的同时，你结合你的数据字典，就知道哪些字段是顺序数据，哪些字段是名称数据，哪些字段是等比数据，哪些可以用来做维度，哪些是用来做指标的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fdbc6ec41464705a04d6f0d3206bd03~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果是在做可视化 ORM 的时候，会经常碰到复杂查询逻辑的情况，这个时候一般的交互很难满足用户的需求，比如 SUM(a.v1) / SUM(a.v2) 或者 CASE ... WHEN ... END 这样，你也不好直接给个 input 的框，因为容易拿到不规范的数据等情况都会出现。这个时候你就需要会写 DSL 表单，本质上是通过 CST 来实现你自己的富文本编辑器。</p>
<p>还有就是随着项目的表越来越多，数据源的数据也会越来越大，这个时候前端的性能就很关键了，这里的话推荐使用范式化的形式去管理你页面上的数据，你会发现页面的性能可以翻几十倍。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeec011225fd4e1dbe835222f4cac770~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着我们现在这个项目假设跑了几个月，这个时候里面的报表或者看板或者组件，可能从最开始的几个，增长到上千个。有的时候某个用户就可以拥有上百张表，那么如何让用户很好的管理他的报表或看板也是你需要考虑的事情，这里的我推荐一开始的这一块就设计成一个无限层级的菜单服务，类似于网盘那样，用户可以创建自己的文件夹，可以移动排序重命名等，类似网盘的那些操作去管理他的数据。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16a2fa8c77504f11a0b3a6660595fd90~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然你的用户都会写 SQL，但是每个人写 SQL 的水平是参差不齐的，这个时候你就需要一个 SQL 审核的服务对用户 SQL 进行分析，AST 解析 SQL（这里推荐用阿里的 Druid Parser），拿到用户写的 SQL 信息，比如用了多少张表，连了多少张表，连表的逻辑是否是不符合规范，再结合执行计划等对这个 SQL 进行审核和评分，避免发生什么一个 SQL 就把你整个数据库搞挂了的情况。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4216e80caf244b29b8571b4b79b5b8d8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你在写项目的时候遇到一些实现上的困扰，需要找一些项目实现来参考的时候，我推荐你去跑跑看这两个，一个是 <a href="https://github.com/metabase/metabase" target="_blank" rel="nofollow noopener noreferrer">Metabase</a>，另一个是 <a href="https://github.com/apache/incubator-superset" target="_blank" rel="nofollow noopener noreferrer">Superset</a> ，因为他们都是开源的，另外 <a href="https://github.com/elastic/kibana" target="_blank" rel="nofollow noopener noreferrer">Kibana</a> 也是很好的实践参考。</p>
<hr>
<p>别忘了6-5 下午直播哦，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image" alt="大会海报.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<p>期待更多文章，点个赞</p></div>  
</div>
            