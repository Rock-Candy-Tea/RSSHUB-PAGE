
---
title: '【日拱一卒】JavaScript异步编程 二'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=2045'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 06:30:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=2045'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第13天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<h2 data-id="heading-0">前言</h2>
<p>JavaScript异步编程 第二章 分布式事件</p>
<h2 data-id="heading-1">PubSub模式（发布、订阅）</h2>
<p>实践中如何处理事件，直接给每一个事件添加一个处理器。那一个事件多个处理结果，那就会导致处理器的规模急剧膨胀。（可以理解为一个事见通过一个函数去实现，那么这个函数就要调用特别多的方法，这个函数就会有特别多行，难以维护。这一节也就是讨论通过PubSub模式去实现事件。）</p>
<p>接下来介绍Node的EventEmitter对象、Backbone的事件化模型、jQuery的自定义事件</p>
<p>浏览器允许向DOM元素附加事件处理器，形如<code>link.onclick = clickHandler</code></p>
<p>如果想向一个元素附加两个点击事件处理器，则必须自行用一个封装函数汇集这两个处理器。</p>
<pre><code class="copyable">link.onclick = function() &#123;
    clickHandler1.apply(this, arguments)
    clickHandler2.apply(this, arguments)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>W3C于2000年向DOM规范中添加了<code>addEventListener</code>方法，而jQuery将其抽象成bind方法。</p>
<pre><code class="copyable">$(link)
    .bind('click', clickHandler1)    .bind('click', clickHandler2)

$( "button" ).on( "click", notify );
$( "button" ).on( "click", notify );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>jQuery将link元素的事件发布给了任何想订阅此事件的人。</p>
<p>而在Nodejs中，有实现了发布订阅模式的实体，这个实体是EventEmitter（事件发生器），其他对象可以继承它。且Nodejs中几乎所有的I/O源都是EventEmitter对象：文件流、HTTP服务器，甚至是应用进程本身。参考一个EventEmitter实例。</p>
<pre><code class="copyable">['room'，'moon','cow jumping over the moon']
.forEach(function(name)&#123;
    process.on('exit',function()&#123;
        console.log('GoodNight, ' + name)
    &#125;)
&#125;)
// 当exit事件发生时，发布给他人，执行匿名函数 打印信息
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（这个例子蛮水的）</p>
<h3 data-id="heading-2">EventEmitter对象</h3>
<p>Node中的EventEmitter对象</p>
<p>1. 通过on方法给EventEmitter对象添加一个事件处理器</p>
<p>2. 通过emit方法调用给定事件类型的所有处理器</p>
<p>此处的事件与队列中的事件没有任何关系，nodejs约定，只能从EventEmitter对象的‘内部’触发事件。</p>
<h3 data-id="heading-3">实现PubSub</h3>
<pre><code class="copyable">PubSub = &#123;handlers: &#123;&#125;&#125;
PubSub.on = function(eventType,handler)&#123;
    if(!(eventType in this.handlers))&#123;
        this.handlers[eventType] = []
    &#125;
    
    this.handlers[eventType].push(handler)
    return this
&#125;
PubSub.emit = function(eventType)&#123;
    var handlerArgs = Array.prototype.slice.call(arguments, l);
    for(var i=0;i<this.handlers[eventType].length;i++)&#123;
        this.handlers[eventType][i].apply(this,handlerArgs)
    &#125;
    return this
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">同步性</h3>
<p>JS中，事件触发同步执行处理器，处理器过多会导致相应迟钝。这里本书给出了一个简单解决方法，在之后的第四章会给出更复杂精妙的作业排队技术。</p>
<pre><code class="copyable">var tasks = [] 
setInterval(function()&#123;
    var nextTask
    if(nextTask = tasks.shift())&#123;
        nextTask()
    &#125;
&#125;, 0)
// 这个函数就不会一次同步执行所有的处理器
// 而是通过setInterval，异步执行各个处理器，不会阻塞到其他操作。
// 大概是这么回事，更细节精妙的参考第四章
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">事件化模型</h2>
<p>只要对象带有PubSub的借口，就可以称之为<code>事件化对象</code>。</p>
<p>用于存储数据的对象因内容变化而发布事件时，这里用于存储数据的对象又称为Model。</p>
<p>MVVM，MVC中的Model。所以发布订阅模式可以用于实现MVC、MVVM模型。</p>
<p>（Vue双向绑定源码就用到了）</p>
<p>老式的javaScript靠输入事件的处理器，直接修改DOM。新式的JavaScript先改变模型，通过模型触发事件而导致DOM的更新。</p>
<h3 data-id="heading-6">事件循环与嵌套式变化</h3>
<p>Backbone设置了两道保险，以防双向绑定，change事件无线触发。</p>
<p>1. 新值等于旧值，不触发change事件</p>
<p>2. change事件期间，不触发change事件</p>
<p>这里这本书举了一个关于backbone框架set/get的例子，个人觉得他讲的比较浅，但这个框架暂时有没接触到。可惜这里不是用vue双向绑定做例子讲解的。</p>
<h3 data-id="heading-7"></h3>
<h2 data-id="heading-8">jQuery自定义事件</h2>
<p>自定义事件作为DOM事件冒泡技术的一个补充。</p>
<p>jQuery提供了非冒泡事式的triggerHandler方法。</p>
<p>书中举了一个进度条的例子</p>
<pre><code class="copyable">// 假设正在编写一个关于工具提示条的库，并希望任一时刻只能看到一个工具提示条

$('.tooltip').remove()
// 每次新建一个工具提示条的时候，先调用这个函数，删除当前的工具提示条


// 新场景，独立出某些容器，侧边栏显示新的提示条，其它地方的工具提示条不受影响，即独立出侧边栏

// $container 可以是 $('#sidebar') 或者 $(document)
$container.triggerHandler('newTootip')
$container.one('newTooltip',function()&#123;
    $tooltip.remove
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于triggerHandler可参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq%255C_22855325%2Farticle%2Fdetails%2F72955628" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq%5C_22855325/article/details/72955628" ref="nofollow noopener noreferrer">blog.csdn.net/qq\_2285532…</a></p>
<p>当事件冒泡技术破坏我们的意图时，使用自定义事件。</p>
<h2 data-id="heading-9">小结</h2>
<p>PubSub事件模型，难以解决一次性事件（一次性事件要求对异步函数执行的一次性任务的两种结果做不同的处理。如Ajax），这正是下一张要讲的Promise</p>
<p>PS：</p>
<p>今天读这一章的时候，还是挺开心的。特别是当自己之前阅读vue双向绑定源码，在这里的pubSub模式中，又得到了重温。有种温故知新的感觉。</p>
<p>但遗憾的是这本书的作者主讲的是nodejs,jquery,backbone。自己很多内容都只能看一遍，理清思路，还是有好多内容有卡壳。</p>
<p>不够深入，但有所收获，知道了很多概念，为知识体系添砖加瓦。</p>
<p>这个周末把这本书看完把，正好也把promise异步相关的内容解决掉。</p>
<p>继续看吧，看这些偏门书，还是很有乐趣的，你永远不知道下一章讲的你搞不搞得定。搞得定你赚了，搞不定你就亏了。不知道为什么，好象这样的体验更有趣一些，比起永远一板一眼的正确的学习。</p></div>  
</div>
            