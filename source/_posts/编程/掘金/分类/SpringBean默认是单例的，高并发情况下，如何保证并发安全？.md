
---
title: 'SpringBean默认是单例的，高并发情况下，如何保证并发安全？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0933fd2c9bf44281b0d167b43375ac8e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 01:49:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0933fd2c9bf44281b0d167b43375ac8e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Spring的bean默认都是单例的，某些情况下，单例是并发不安全的，以Controller举例，问题根源在于，我们可能会在Controller中定义成员变量，如此一来，多个请求来临，进入的都是同一个单例的Controller对象，并对此成员变量的值进行修改操作，因此会互相影响，无法达到并发安全（不同于线程隔离的概念，后面会解释到）的效果。</p>
<h3 data-id="heading-0">一、抛出问题</h3>
<p>首先来举个例子，证明单例的并发不安全性：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0933fd2c9bf44281b0d167b43375ac8e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>多次访问此url，可以看到每次的结果都是自增的，所以这样的代码显然是并发不安全的。</p>
<h3 data-id="heading-1">二、解决方案</h3>
<p>因此，我们为了让无状态的海量Http请求之间不受影响，我们可以采取以下几种措施：</p>
<h3 data-id="heading-2">2.1 单例变原型</h3>
<p>对web项目，可以Controller类上加注解@Scope("prototype")或@Scope("request")，对非web项目，在Component类上添加注解@Scope("prototype")。</p>
<ul>
<li>优点：实现简单；</li>
<li>缺点：很大程度上增大了bean创建实例化销毁的服务器资源开销。</li>
</ul>
<h3 data-id="heading-3">2.2 线程隔离类ThreadLocal</h3>
<p>有人想到了线程隔离类ThreadLocal，我们尝试将成员变量包装为ThreadLocal，以试图达到并发安全，同时打印出Http请求的线程名，修改代码如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d3755b4ba4b4f2abe6ba9b40f74bbe5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>多次访问此url测试一把，打印日志如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9993f61c4a69430287d9f64b6571ce33~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从日志分析出，二十多次的连续请求得到的结果有1有2有3等等，而我们期望不管我并发请求有多少，每次的结果都是1；同时可以发现web服务器默认的请求线程池大小为10，这10个核心线程可以被之后不同的Http请求复用，所以这也是为什么相同线程名的结果不会重复的原因。</p>
<p>总结：ThreadLocal的方式可以达到线程隔离，但还是无法达到并发安全。</p>
<h3 data-id="heading-4">2.3 尽量避免使用成员变量</h3>
<p>有人说，单例bean的成员变量这么麻烦，能不用成员变量就尽量避免这么用，在业务允许的条件下，将成员变量替换为RequestMapping方法中的局部变量，多省事。这种方式自然是最恰当的，本人也是最推荐。代码修改如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf37cf0e0c434e8dac99b8b993a20fd8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但当很少的某种情况下，必须使用成员变量呢，我们该怎么处理？</p>
<h3 data-id="heading-5">3.4 使用并发安全的类</h3>
<p>Java作为功能性超强的编程语言，API丰富，如果非要在单例bean中使用成员变量，可以考虑使用并发安全的容器，如ConcurrentHashMap、ConcurrentHashSet等等等等，将我们的成员变量（一般可以是当前运行中的任务列表等这类变量）包装到这些并发安全的容器中进行管理即可。</p>
<h3 data-id="heading-6">2.5 分布式或微服务的并发安全</h3>
<p>如果还要进一步考虑到微服务或分布式服务的影响，方式4便不足以处理了，所以可以借助于可以共享某些信息的分布式缓存中间件如Redis等，这样即可保证同一种服务的不同服务实例都拥有同一份共享信息（如当前运行中的任务列表等这类变量）。</p>
<h3 data-id="heading-7">三、补充说明</h3>
<ul>
<li>
<p>spring bean作用域有以下5个：</p>
</li>
<li>
<p>singleton：单例模式，当spring创建applicationContext容器的时候，spring会欲初始化所有的该作用域实例，加上lazy-init就可以避免预处理；</p>
</li>
<li>
<p>prototype：原型模式，每次通过getBean获取该bean就会新产生一个实例，创建后spring将不再对其管理；</p>
</li>
<li>
<p>（下面是在web项目下才用到的）</p>
</li>
<li>
<p>request：搞web的大家都应该明白request的域了吧，就是每次请求都新产生一个实例，和prototype不同就是创建后，接下来的管理，spring依然在监听；</p>
</li>
<li>
<p>session：每次会话，同上；</p>
</li>
<li>
<p>global session：全局的web域，类似于servlet中的application。</p>
</li>
</ul>
<p>作者 | 智哥</p>
<p><strong><a href="https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/ia2kOHHlKTxYjBHZ9ttRAg" target="_blank" rel="nofollow noopener noreferrer">原文链接</a></strong></p>
<p><strong>更多技术干货敬请关注码农架构知乎号：</strong><a href="https://www.zhihu.com/people/na-zhao-kou-qin-dao-chu-zhuang-bi" target="_blank" rel="nofollow noopener noreferrer">码农架构 - 知乎</a></p>
<p>本文为**<a href="https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/hr70P_PajsUNXjsADrlaCw" target="_blank" rel="nofollow noopener noreferrer">码农架构</a>**原创内容，未经允许不得转载。</p></div>  
</div>
            