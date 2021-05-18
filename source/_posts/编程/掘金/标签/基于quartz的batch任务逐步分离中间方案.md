
---
title: '基于quartz的batch任务逐步分离中间方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18a85d41d03d46aa8fa7e456e434faef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 19:41:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18a85d41d03d46aa8fa7e456e434faef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">情境（Situation）</h2>
<p>　　项目所有的定时任务和业务都在同一个应用中，现在甲方提出需求：为避免在升级发布时程序异常导致batch无法正常执行。所以要把batch从原程序中分离出来。但是需要一个一个的分离。由于项目中的quartz框架用的是数据库模式，并且新程序和原程序使用的是同一个数据库，这导致了程序之间的source不一致。而quartz随机分配任务，没有分离的batch可能会被分配到新程序中导致batch执行失败。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18a85d41d03d46aa8fa7e456e434faef~tplv-k3u1fbpfcp-watermark.image" alt="1621304609(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">任务（Task）</h2>
<p>　　与项目组成员讨论解决方案，分析每个方案的利弊，选择合适的方案并且实施。</p>
<h2 data-id="heading-2">行动（Action）</h2>
<h3 data-id="heading-3">方案提出</h3>
<p>　　我们讨论出的解决方案主要是三种：</p>
<pre><code class="copyable">1. 分离出来的batch使用新的框架管理（Spring Task、Spring Batch）。
2. 取消quartz框架，使用shell定时调用。
3. 加一个数据库给新程序的quartz框架使用。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">方案选择</h3>
<p>　　第一个方案需要花费的调查时间较长，而且能否顺利实施，实施完成后还需要测试框架的正确性。所以被pass掉了。<br>
第二个方案取消掉quartz看起来是很好的方案，但是有两个不好的地方。其一，不能使用集群模式；其二，shell调用启动应用会导致cpu占用高。<br>
第三个方案就比较合理一些，因为在把所有的batch分离完成过后，还可以把新程序的quartz的数据库移回至原数据库。而且添加一个数据源的时间不会很长。</p>
<h3 data-id="heading-5">方案实施</h3>
<p>　　方案三的流程图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2504074c79c412fa322dbc208bfb28e~tplv-k3u1fbpfcp-watermark.image" alt="S6IBC9_WI4H1I4F7QLA`R.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　参照<a href="https://www.cnblogs.com/CryOnMyShoulder/p/12218876.html" target="_blank" rel="nofollow noopener noreferrer">Mybatis plus 配置多数据源</a>把项目的多数据源配置好了，给quartz指定了新配置的数据源。<br>
开跑，batch业务执行时报错了。后来发现是因为项目中使用了Mybatis-plus框架，而在之前写多数据源时提供给Spring的SqlSessionFactory是原生的，而不是MybatisSqlSessionFactory，导致了Mybatis-plus不兼容。要问我怎么发现的，我只能说有人踩过坑了✈️。<a href="https://blog.csdn.net/wwrzyy/article/details/86034458" target="_blank" rel="nofollow noopener noreferrer">mybatis plus报Invalid bound statement (not found):解决</a></p>
<h2 data-id="heading-6">结果（Result）</h2>
<p>　　最后项目运行正常，没有和原程序的batch相互干扰。这也是我第一次用多数据源，感觉还是很简单的。</p>
<h2 data-id="heading-7">总结（Summarize）</h2>
<p>　　使用@Primary注解让Mybatis默认使用我们自定义的DynamicDataSource，在生成DynamicDataSource对象时，我们把多个的数据源都以map的形式保存到了DynamicDataSource对象中。后面切换数据源主要是通过改变DataSourceContextHolder类中的contextHolder成员保存的key，而在需要进行数据库连接时，Mybatis在DynamicDataSource中索取数据源，DynamicDataSource通过determineTargetDataSource()方法从map中获取具体的数据源。而key是通过重写的determineCurrentLookupKey()方法在DataSourceContextHolder类中的contextHolder成员那里拿到的。这样就达到了数据源切换的效果了。总之就是有些东西用了就知道很简单。</p></div>  
</div>
            