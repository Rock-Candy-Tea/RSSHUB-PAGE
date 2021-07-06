
---
title: '《平凡的DDD》第五弹：以领域为中心的架构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb8fd58db61e43cd94d9dc19ad7325b4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 22:52:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb8fd58db61e43cd94d9dc19ad7325b4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在本篇文章中，将介绍<strong>以领域为中心</strong>的架构以及它和传统的<strong>以数据为中心</strong>的架构之间的区别和联系。之所以写这篇文章，是为了给DDD分层架构做一些补充说明，以便更好地了解它的前因后果。</p>
<p>众所周知，在人类科学史上，对于宇宙运行方式的讨论，有过两大学说，即“<strong>地心说</strong>”和“<strong>日心说</strong>”。今天我们都知道日心说才是科学的，地球和行星围绕着太阳转，大概幼儿园的小朋友也知道这是基本的常识。<strong>不过，在数百年前，坚持日心说可能要被处以极刑</strong>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb8fd58db61e43cd94d9dc19ad7325b4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>人类数百年来对于宇宙运行认知的变化，恰似数十年来对软件架构认知的变化。日心说取代了地心说，以领域为中心的架构也正在逐步成为主流</strong>。</p>
<p>当然，软件架构思想的变迁，也不完全与人类对宇宙认知的变迁相同，毕竟“地心说”完全是错误的。但是，<strong>软件架构中没有绝对的正确或错误</strong>。以数据为中心的软件架构，也并非一无是处。客观地说，它的诞生和流行有着历史的原因，甚至今天仍有用武之地，只不过在某些复杂业务中，它有着一定的局限性。</p>
<p>在以数据为中心的架构中，它的关键是<strong>用户界面层</strong>（见下图），业务逻辑层和数据访问层围绕着数据库旋转。因此，<strong>数据库是名副其实的架构中心</strong>。在这样的架构中，你不必太在意对业务逻辑层的设计。换言之，无论业务逻辑层的代码如何堆砌，数据落库无误即可。这种场面看起来似乎耳熟能详，但实际正是如此。不要误会，这里没有贬低的意思。只是说，<strong>如果你的业务逻辑较为复杂，而你又使用了以数据为中心的架构，那么你可能要重新审视你的架构了</strong>。</p>
<p>那么，从以数据为中心的架构到以领域为中心的架构，人们审视架构的视角是如何变化的呢？原因可能有很多，行业的老专家、《敏捷软件开发》的作者 <strong>Robert C. Martin（Bob大叔）</strong> 曾经说过一句话：</p>
<blockquote>
<p>The first concern of the architect is to make sure that the house is usable, it is not to ensure that the house is made of brick.</p>
</blockquote>
<p>大叔拿建筑师造房子来举例子。对于建筑师来说，造房子最关键的是什么呢？材料是砖头还是木头？显然不是，对于一所房屋来说，最关键的是它要<strong>可用</strong>，这是<strong>根本。<strong>否则建它干什么呢？至于用什么材料、选什么样的装修风格，那些都不过是</strong>细节</strong>。</p>
<p>这个例子牵扯出了架构中的两个重要概念，即<strong>根本（Essential）<strong>和</strong>细节（Detail）</strong>。在一个架构中如果理不清什么是根本，什么只是细节，不能把它们放在合适的位置，那么无异于<strong>本末倒置</strong>。对于房子来说，“可用”是根本，“砖头”、“装修”不过是它实现的一个细节，除了砖头还可以用木头嘛！同样，对于汽车来说，“可靠、安全”才是它的根本，至于是电动还是燃油，不过是它不同的实现。</p>
<p>如此，再回头来看以数据为中心的软件架构就会发现，它的问题在于搞错了<strong>根本。<strong>在企业架构中，“<strong>业务逻辑</strong>”才是根本，数据库作为一种存储方式，不过是承载业务数据的一种具体的</strong>细节</strong>，它可以有着不同的实现，关系型数据库、NoSQL甚至文件存储都可以用。<strong>需要注意的是，这里并不是说数据不重要，而是从本质上来说，架构是对复杂度的治理，而不是对数据的管理</strong>。<strong>很显然，在大多数的企业架构中，复杂的业务逻辑是治理的重点</strong>。</p>
<p>于是，这就催生出了<strong>以领域为中心的架构（Domain-centric Architecture）</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f378147dbbdb4742b8dfd192c19876b3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在以领域为中心的架构中，<strong>领域</strong>是架构的中心。这样的好处是，<strong>通过分层架构，隔离领域复杂度与技术复杂度，从而实现对两种不同类型的复杂度独立治理，并将重点放在领域上</strong>。另外，良好的分层和解耦有利于架构的扩展和稳定，也更易于维护。所以，针对复杂业务场景，或具有较长生命周期的产品，应当考虑这种架构。</p>
<p>当然，<strong>以领域为中心的架构只是一种思想，而思想就必然会有不同的实现，DDD是其中的一种实现</strong>。在后面的文章里，会介绍<strong>六边形架构</strong>和<strong>洋葱架构</strong>是如何实现以领域为中心架构的。</p></div>  
</div>
            