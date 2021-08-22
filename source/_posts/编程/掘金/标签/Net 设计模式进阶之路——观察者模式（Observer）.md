
---
title: '.Net 设计模式进阶之路——观察者模式（Observer）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6634adc7de604eb5ac80db1acaaaa896~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 07:46:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6634adc7de604eb5ac80db1acaaaa896~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>观察者模式，又叫<strong>发布-订阅模式（Publish/Subscribe）</strong>，既然有观察者，当然也有被观察者，就如同在你的生活中，有一双明亮的眼睛时刻注视着你，你发生的大大小小的事情，它都了如指掌。</p>
<h1 data-id="heading-1">🎏 01.观察者模式的解释</h1>
<p><strong>意图：</strong> 定义对象间的一种一对多的依赖关系 ,当一个对象的状态发生改变时 , 所有依赖于它的对象 都得到通知并被自动更新。</p>
<p><strong>问题领域：</strong> 它一般用来解决下列问题。</p>
<ul>
<li>
<p>观察者和被观察者需要解耦，或者有多个观察者</p>
</li>
<li>
<p>需要把自己的状态通知给其他对象</p>
</li>
</ul>
<p><strong>解决方案</strong>： 我们使用UML图来描述它。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6634adc7de604eb5ac80db1acaaaa896~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中可以看出，被观察者是Subject，其可以有很多观察者Observer，被观察者发布通知，观察者收到通知。</p>
<p><strong>效果：</strong></p>
<ul>
<li>好处：</li>
</ul>
<ol>
<li>一个对象状态改变，可以通知所有的观察者；</li>
<li>观察者和被观察者只有抽象层耦合;</li>
<li>有一套触发机制</li>
</ol>
<ul>
<li>限定:</li>
</ul>
<ol>
<li>通知所有的观察者，在观察者多的时候会花费很多时间</li>
<li>观察者和被观察者间有循环依赖，可能导致系统崩溃</li>
</ol>
<h1 data-id="heading-2">🎏 02. dotnet core 源码赏析</h1>
<pre><code class="hljs language-csharp copyable" lang="csharp"> <span class="hljs-keyword">internal</span> <span class="hljs-keyword">interface</span> <span class="hljs-title">ICascadingValueComponent</span>
    &#123;
        <span class="hljs-comment">// This interface exists only so that CascadingParameterState has a way</span>
        <span class="hljs-comment">// to work with all CascadingValue<T> types regardless of T.</span>

        <span class="hljs-function"><span class="hljs-built_in">bool</span> <span class="hljs-title">CanSupplyValue</span>(<span class="hljs-params">Type valueType, <span class="hljs-built_in">string</span>? valueName</span>)</span>;

        <span class="hljs-built_in">object</span>? CurrentValue &#123; <span class="hljs-keyword">get</span>; &#125;

        <span class="hljs-built_in">bool</span> CurrentValueIsFixed &#123; <span class="hljs-keyword">get</span>; &#125;

        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">Subscribe</span>(<span class="hljs-params">ComponentState subscriber</span>)</span>;

        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">Unsubscribe</span>(<span class="hljs-params">ComponentState subscriber</span>)</span>;
    &#125;
    
    <span class="hljs-comment">//实现类</span>
     <span class="hljs-keyword">void</span> ICascadingValueComponent.Unsubscribe(ComponentState subscriber)
        &#123;
            _subscribers?.Remove(subscriber);
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">NotifySubscribers</span>(<span class="hljs-params"><span class="hljs-keyword">in</span> ParameterViewLifetime lifetime</span>)</span>
        &#123;
            <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> subscriber <span class="hljs-keyword">in</span> _subscribers!)
            &#123;
                subscriber.NotifyCascadingValueChanged(lifetime);
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发布订阅还是蛮常见的，在asp.net core代码中可以查看到很多类似的用法。</p>
<h1 data-id="heading-3">🎏 03. dotnet 生成器实现</h1>
<p>构建一个抽象的观察者，并实现几个实例。</p>
<p>实例观察者实现，可以加到被观察者的观察列表。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">class</span> <span class="hljs-title">Visitor</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">VisitConcreteElementA</span>(<span class="hljs-params">
            ConcreteElementA concreteElementA</span>)</span>;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">VisitConcreteElementB</span>(<span class="hljs-params">
            ConcreteElementB concreteElementB</span>)</span>;
    &#125;
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><summary></span></span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> A 'ConcreteVisitor' class</span>
    <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"></summary></span></span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">ConcreteVisitor1</span> : <span class="hljs-title">Visitor</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-keyword">void</span> <span class="hljs-title">VisitConcreteElementA</span>(<span class="hljs-params">
            ConcreteElementA concreteElementA</span>)</span>
        &#123;
            Console.WriteLine(<span class="hljs-string">"&#123;0&#125; visited by &#123;1&#125;"</span>,
                concreteElementA.GetType().Name, <span class="hljs-keyword">this</span>.GetType().Name);
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-keyword">void</span> <span class="hljs-title">VisitConcreteElementB</span>(<span class="hljs-params">
            ConcreteElementB concreteElementB</span>)</span>
        &#123;
            Console.WriteLine(<span class="hljs-string">"&#123;0&#125; visited by &#123;1&#125;"</span>,
                concreteElementB.GetType().Name, <span class="hljs-keyword">this</span>.GetType().Name);
        &#125;
    &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用方，可以按照实例类型调用直接使用。</p>
<pre><code class="copyable">ObjectStructure o = new ObjectStructure();
o.Attach(new ConcreteElementA());
o.Attach(new ConcreteElementB());
// Create visitor objects
ConcreteVisitor1 v1 = new ConcreteVisitor1();
ConcreteVisitor2 v2 = new ConcreteVisitor2();
// Structure accepting visitors
o.Accept(v1);
o.Accept(v2);
// Wait for user
Console.ReadKey();
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">🎏 04. 小结</h1>
<p>30天不停更，目标很远大，今天是第二天，加油吧，兄弟们！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            