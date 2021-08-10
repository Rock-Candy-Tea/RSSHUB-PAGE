
---
title: '.Net 设计模式进阶之路——策略模式_Strategy_'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44d23549bb594a528f2acc841ff99697~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 05:33:36 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44d23549bb594a528f2acc841ff99697~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 01.代理模式</h1>
<p><strong>意图：</strong> 定义一系列的算法，把这些算法设计为可被互相替换。</p>
<p>形象的说：虽然算法不同，但客户端的执行调用均不用修改，不同的算法就如同不同的策略一样，可以被随时替换。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44d23549bb594a528f2acc841ff99697~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>问题领域：</strong></p>
<ul>
<li>有许多不同的算法，不希望被硬编码到系统，</li>
<li>算法可以按照情况互换，</li>
<li>算法内的其他数据不希望暴露出去，</li>
<li>旧系统重构，发现很多if分支的语句，可以考虑替换</li>
</ul>
<p><strong>解决方案</strong>： 我们使用UML图来描述它。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97db753b1ebb48da9caa76005d4df67d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们定义一个接口或抽象类Strategy，并设计其接口，由具体的实现类实现不同的算法，这里是ConcreteStrategy1和2类。</p>
<p>Client就是一个使用者，其内部可以实例化Strategy类，也可以按照条件进行配置不同的Strategy类，具体的应用方法通过接口或抽象类进行调用，而避免直接选定具体的类。</p>
<p><strong>效果：</strong></p>
<ul>
<li>好处：</li>
</ul>
<ol>
<li>可以扩算法系列；</li>
<li>可以替代直接继承的方案，避免把算法硬编码到使用类；</li>
<li>消除分支语句；</li>
<li>客户可以有多种选择；</li>
</ol>
<ul>
<li>限定:</li>
</ul>
<ol>
<li>客户需要知道算法的不同点。</li>
<li>增加了对象数</li>
</ol>
<h1 data-id="heading-1">🎏 02. dotnet core 源码赏析</h1>
<p>在 <code>aspnet Core</code>源代码内有一个验证策略的接口<code>IValidationStrategy</code>，采用了策略模式。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">public</span> <span class="hljs-keyword">interface</span> <span class="hljs-title">IValidationStrategy</span>
    &#123;       
        <span class="hljs-function">IEnumerator<ValidationEntry> <span class="hljs-title">GetChildren</span>(<span class="hljs-params">ModelMetadata metadata, <span class="hljs-built_in">string</span> key, <span class="hljs-built_in">object</span> model</span>)</span>;
    &#125;
    <span class="hljs-keyword">internal</span> <span class="hljs-keyword">class</span> <span class="hljs-title">DefaultComplexObjectValidationStrategy</span> : <span class="hljs-title">IValidationStrategy</span>
    &#123;

        <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">readonly</span> IValidationStrategy Instance = <span class="hljs-keyword">new</span> DefaultComplexObjectValidationStrategy();

        <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">DefaultComplexObjectValidationStrategy</span>(<span class="hljs-params"></span>)</span>
        &#123;
        &#125;

        <span class="hljs-comment"><span class="hljs-doctag">///</span> <span class="hljs-doctag"><inheritdoc /></span></span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> IEnumerator<ValidationEntry> <span class="hljs-title">GetChildren</span>(<span class="hljs-params">
            ModelMetadata metadata,
            <span class="hljs-built_in">string</span> key,
            <span class="hljs-built_in">object</span> model</span>)</span>
        &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Enumerator(metadata, key, model);
        &#125;

        
        &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>策略模式并不难理解，只要合适的场景就可以引入它。</p>
<h1 data-id="heading-2">🎏 03. dotnet 代理类实现</h1>
<p>这是一个例子，我们来按照uml图的设计实现一个策略类，接口定义如下：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">class</span> <span class="hljs-title">Strategy</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">AlgorithmInterface</span>(<span class="hljs-params"></span>)</span>;
    &#125;    
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">ConcreteStrategyA</span> : <span class="hljs-title">Strategy</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-keyword">void</span> <span class="hljs-title">AlgorithmInterface</span>(<span class="hljs-params"></span>)</span>
        &#123;
            Console.WriteLine(
                <span class="hljs-string">"Called ConcreteStrategyA.AlgorithmInterface()"</span>);
        &#125;
    &#125;   
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">ConcreteStrategyB</span> : <span class="hljs-title">Strategy</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> <span class="hljs-keyword">void</span> <span class="hljs-title">AlgorithmInterface</span>(<span class="hljs-params"></span>)</span>
        &#123;
            Console.WriteLine(
                <span class="hljs-string">"Called ConcreteStrategyB.AlgorithmInterface()"</span>);
        &#125;
    &#125;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">Client</span>
    &#123;
        Strategy strategy;
        <span class="hljs-comment">// Constructor</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Client</span>(<span class="hljs-params">Strategy strategy</span>)</span>
        &#123;
            <span class="hljs-keyword">this</span>.strategy = strategy;
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">ContextInterface</span>(<span class="hljs-params"></span>)</span>
        &#123;
            strategy.AlgorithmInterface();
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用方，可以按照下列方式直接使用。</p>
<pre><code class="copyable">Client context;
// Two contexts following different strategies
context = new Client(new ConcreteStrategyA());
context.ContextInterface();
context = new Client(new ConcreteStrategyB());
context.ContextInterface();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，通过上述的策略类，我们可以在客户端代码内，随意切换策略实现类，实现互换的目的，当然如果引入配置信息，还可以做到根据配置信息动态修改算法的功能。</p>
<p>你的项目内有无类似的场景，可以拿来练练手哦。</p>
<h1 data-id="heading-3">🎏 04. 小结</h1>
<p>策略模式侧重于通过不同的算法达到相同的目的，关注点主要在对行为的抽象上，所以策略模式一般都是基于接口的。</p>
<p>每篇的设计模式，都是看起来容易，往往写起来很费力气，这可能是我在编程中大部分场景并没有使用到他们，或者使用的比较少的缘故吧，甚至于没有排在前面写的模式，可能都从来没用过呢。</p>
<p>当然查找.net源码，试图从里面找到我们需要的设计模式也不是个轻松的活。</p>
<p>虽然设计模式已经有很多文章了，但我还是希望能写的不同，一方面增强自己的记忆，一方面也给.net 广大程序员打打气，看看支撑我们的.net core源码里有多少设计模式可供我们学习。</p>
<p>所以能翻看源码的程序员不会差到哪里去！😳</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            