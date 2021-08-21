
---
title: '【Web架构系列】分析SOAP与HTTP的关系、REST与HTTP的关系'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f8e48c577a14d4589cfa0ea19667568~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 23:12:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f8e48c577a14d4589cfa0ea19667568~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<hr>
<blockquote>
<p>主要参考资料  <a id="user-content-main-reference" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.infoq.cn%2Fminibook%2Fweb-based-apps-archit-design" target="_blank" rel="nofollow noopener noreferrer" title="https://www.infoq.cn/minibook/web-based-apps-archit-design" ref="nofollow noopener noreferrer"><strong>架构风格与基于网络应用软件的架构设计(中文修订版)</strong></a>(李琨2013年修订)</li>
<li>学术期刊：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cnki.com.cn%2FArticle%2FCJFDTotal-RJSJ200717029.htm" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cnki.com.cn/Article/CJFDTotal-RJSJ200717029.htm" ref="nofollow noopener noreferrer"><strong>《REST与SOAP的冲突》</strong></a>(知网)
<ul>
<li>个人认为这篇文章中有一个错误的描述："SOAP是个架构"。实际上SOAP是个协议。只有这一段感觉不对，其他的都写得很好</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f8e48c577a14d4589cfa0ea19667568~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>延伸阅读</p>
<ul>
<li>了解REST：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_43413788%2Farticle%2Fdetails%2F118941182" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_43413788/article/details/118941182" ref="nofollow noopener noreferrer">详解REST和RESTful</a></li>
<li>了解REST与SOAP：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_43413788%2Farticle%2Fdetails%2F119114348" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_43413788/article/details/119114348" ref="nofollow noopener noreferrer">REST杂谈：REST发展初期的坎坷之路(技术环境分析以及REST&SOAP的冲突)</a></li>
</ul>
</blockquote>
<hr>
<h1 data-id="heading-0">序</h1>
<p>基本上，我们使用的REST、SOAP都是基于HTTP的
这造成了一种错误的意识：很多人以为REST、SOAP就是基于HTTP的</p>
<p>实际上，REST和SOAP理论上都没有指定要依赖于HTTP，事实上也完全可以不基于HTTP来实现。
但是理论归理论，作者在设计的时候，一定会十分考虑用当前稳定易用的HTTP来做==理论支撑==，这样才<strong>更贴近于现实、更好地解决问题、被容易被大家接收</strong></p>
<p>换句话说，有好用的轮子为什么不用，而要自己设计。自己设计到最后，可能还是回归了到如今的HTTP</p>
<p>所以<strong>可以先说结论</strong>：==REST和SOAP都不必须基于HTTP，之所以用HTTP是因为：HTTP真的很爽==</p>
<hr>
<p>那么HTTP到底爽在哪里？</p>
<h1 data-id="heading-1">一、SOAP与HTTP</h1>
<p>SOAP不是直接使用的HTTP，而是在HTTP之上包了一层，即SOAP是基于HTTP协议的协议。
之所以大多数SOAP都基于HTTP，除了因为HTTP的成熟易用之外，最主要的目的其实是利用HTTP来穿透防火墙</p>
<p>对此，《架构风格与基于网络应用软件的架构设计》(Fielding的REST论文) 和《REST与SOAP的冲突》中均指出：这明显是对HTTP的误用，因为这直接导致防火墙失去了它应有的意义</p>
<blockquote>
<ol>
<li>截自<a href="https://juejin.cn/post/6998777204037386270#main-reference" target="_blank" title="#main-reference">《架构风格与基于网络应用软件的架构设计》</a></li>
</ol>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42b0be8f1ccd4224a9816ecd66031b7a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol start="2">
<li>截自<a href="https://juejin.cn/post/6998777204037386270#main-reference" target="_blank" title="#main-reference">《REST与SOAP的冲突》</a></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fd8372ca49e448caaf978887ee72fc1~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p>也正是由于SOAP对HTTP的误用，以及其基于xml的实现方式，共同导致了SOAP越来越重量化，最终被REST取代 (推荐阅读《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_43413788%2Farticle%2Fdetails%2F119114348" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_43413788/article/details/119114348" ref="nofollow noopener noreferrer">REST杂谈：REST发展初期的坎坷之路(技术环境分析以及REST&SOAP的冲突)</a>》)</p>
</blockquote>
<h1 data-id="heading-2">二、REST与HTTP</h1>
<p>REST直接使用HTTP，主要是因为HTTP协议的无状态特性、能够表名操作语义的请求方式(GET、PUT、POST、DELETE等)、缓存处理等，这些都符合RESTful无状态、统一接口、的约束原则</p>
<p>REST基于HTTP仿佛是一个必然的方式。除了以上的好处，如果了解一下HTTP的发展(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fa6b142828326" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/a6b142828326" ref="nofollow noopener noreferrer">推荐阅读-HTTP的发展史</a>)以及REST的提出时间，我们还可以发现</p>
<ul>
<li>1999年HTTP1.1发布，新增了五种请求方法<code>OPTIONS、PUT、PATCH、DELETE、TRACE 、 CONNECT</code>、新增了缓存处理<code>cache-control</code></li>
<li>2000年REST论文发表</li>
<li>Fielding是REST的提出者，也是HTTP协议的主要设计者</li>
</ul>
<p>所以，==REST论文是Fielding以HTTP规范作者的视角描述了web架构应该是什么样子的。Fielding的思想在REST的设计和HTTP上是一致的==，REST论文是将HTTP协议的设计初衷做了诠释</p>
<blockquote>
<p>其实也可以这么说。Fielding虽然没说REST要基于HTTP，但其实背地里早就准备好连招了 (<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d61f9cb479b14908b169c266b8a0fbc4~tplv-k3u1fbpfcp-watermark.image" alt="狗头" loading="lazy" referrerpolicy="no-referrer">)</p>
</blockquote></div>  
</div>
            