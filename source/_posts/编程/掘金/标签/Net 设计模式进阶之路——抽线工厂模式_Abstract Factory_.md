
---
title: '.Net 设计模式进阶之路——抽线工厂模式_Abstract Factory_'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dd896a41e524f0bba19df70bb0021d5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 06:44:07 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dd896a41e524f0bba19df70bb0021d5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 01.抽象工厂模式</h1>
<p><strong>意图：</strong> 把生产一系列关联产品部件的工厂进行更抽象，比如把生产不同枪支部件的厂抽象为枪支抽象工厂，而具体的实体工厂可能是手枪，也可能是步枪等等。</p>
<p><strong>问题领域：</strong> 它一般用来解决下列问题。</p>
<ul>
<li>产品和系统独立，</li>
<li>产品包含一系列的部件需要构建，</li>
<li>产品本身还有不同的类型</li>
<li>产品仅提供接口，而非具体的类</li>
</ul>
<p><strong>解决方案</strong>： 我们使用UML图来描述它。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dd896a41e524f0bba19df70bb0021d5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
图中可以看出，每个抽线工厂的子类，均负责不同部分产品的生成，合并在一起构成了对整体产品的构造。</p>
<p>当然如果采用了生成器设计模式，那我们一般按照 <code>XXXAbstractFactory</code>来定义接口或实现类，这样其他童鞋看到这些类时，可以很快的Get到XXX点。</p>
<p><strong>效果：</strong></p>
<ul>
<li>好处：</li>
</ul>
<ol>
<li>抽象工厂封装了具体的类，其一般对外供调用的接口返回抽象产品类，这样对客户端隐藏了实现的细节；</li>
<li>可以方便的替换产品生成的工厂，以便产生另外的系列部件；</li>
<li>可以方便的控制产品各个部件生成的一致性。</li>
</ol>
<ul>
<li>限定:</li>
</ul>
<ol>
<li>难以支持扩展产品的部件；因为扩展产品部件，意味着所有的实现类均需要修改，工作量繁重。</li>
</ol>
<h1 data-id="heading-1">🎏 02. dotnet core 源码赏析</h1>
<p>在 <code>EF Core</code>源代码内有一个表达式构建的工厂<code>ISqlExpressionFactory</code>构建时采用了抽象工厂模式。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">public</span> <span class="hljs-keyword">interface</span> <span class="hljs-title">ISqlExpressionFactory</span>
&#123;
<span class="hljs-function">SqlBinaryExpression <span class="hljs-title">IsNotNull</span>(<span class="hljs-params">SqlExpression operand</span>)</span>;

    <span class="hljs-function">SqlUnaryExpression <span class="hljs-title">Convert</span>(<span class="hljs-params">
        SqlExpression operand,
        Type type,
        CoreTypeMapping? typeMapping = <span class="hljs-literal">null</span></span>)</span>;

    <span class="hljs-function">SqlUnaryExpression <span class="hljs-title">Not</span>(<span class="hljs-params">SqlExpression operand</span>)</span>;

    <span class="hljs-function">SqlUnaryExpression <span class="hljs-title">Negate</span>(<span class="hljs-params">SqlExpression operand</span>)</span>;

    <span class="hljs-function">SqlFunctionExpression <span class="hljs-title">Function</span>(<span class="hljs-params">
        <span class="hljs-built_in">string</span> functionName,
        IEnumerable<SqlExpression> arguments,
        Type returnType,
        CoreTypeMapping? typeMapping = <span class="hljs-literal">null</span></span>)</span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其生成器接口了不同的表达式构建接口，有SqlUnaryExpression表达式的构建，有SqlFunctionExpression表达式的构建，还有更多的其他类型的表达式构建，这里不一一列举了。</p>
<p>大家有兴趣的可以参看源代码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdotnet%2Fefcore%2Fblob%2F9ac01d6035c76626d89aa1a3cd8d200db2c3c0e1%2Fsrc%2FEFCore.Cosmos%2FQuery%2FInternal%2FISqlExpressionFactory.cs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dotnet/efcore/blob/9ac01d6035c76626d89aa1a3cd8d200db2c3c0e1/src/EFCore.Cosmos/Query/Internal/ISqlExpressionFactory.cs" ref="nofollow noopener noreferrer">github</a>.</p>
<p>通过这个抽象工厂，我们可以构建不同的表达式，最后生成出整体的sql表达式预制件。</p>
<p>有时候比较混淆简单工厂模式，工厂方法模式，还是抽象工厂模式，因为他们都属于工厂模式，在形式上也是极为相似的。</p>
<p>记住他们的最终目的都是为了解耦。</p>
<p>所以，在使用工厂模式时，只需要关心降低耦合度的目的是否达到了，需求可扩展性是否达到了即可。</p>
<h1 data-id="heading-2">🎏 03. dotnet 抽象工厂实现</h1>
<p>这是一个例子，我们来实现一个抽象工厂，接口定义如下：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">abstract</span> <span class="hljs-keyword">class</span> <span class="hljs-title">AbstractFactory</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> AbstractProductA <span class="hljs-title">CreateProductA</span>(<span class="hljs-params"></span>)</span>;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> AbstractProductB <span class="hljs-title">CreateProductB</span>(<span class="hljs-params"></span>)</span>;
    &#125;  
    <span class="hljs-keyword">class</span> <span class="hljs-title">ConcreteFactory1</span> : <span class="hljs-title">AbstractFactory</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> AbstractProductA <span class="hljs-title">CreateProductA</span>(<span class="hljs-params"></span>)</span>
        &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ProductA1();
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> AbstractProductB <span class="hljs-title">CreateProductB</span>(<span class="hljs-params"></span>)</span>
        &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ProductB1();
        &#125;
    &#125;   
    <span class="hljs-keyword">class</span> <span class="hljs-title">ConcreteFactory2</span> : <span class="hljs-title">AbstractFactory</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> AbstractProductA <span class="hljs-title">CreateProductA</span>(<span class="hljs-params"></span>)</span>
        &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ProductA2();
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">override</span> AbstractProductB <span class="hljs-title">CreateProductB</span>(<span class="hljs-params"></span>)</span>
        &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> ProductB2();
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现比较简单，在这里不列出了，等后续一块放在github上。</p>
<p>调用方，可以按照下列方式直接使用。</p>
<pre><code class="copyable">AbstractFactory factory1 = new ConcreteFactory1();
Client client1 = new Client(factory1);
client1.Run();

AbstractFactory factory2 = new ConcreteFactory2();
Client client2 = new Client(factory2);
client2.Run();

<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，相对来说，抽线工厂是为了让创建工厂和一组产品与使用相分离，并可以随时切换到另一个工厂以及另一组产品，因此涉及到的类相对比较多，而我们的应用场景应该不会太多。</p>
<p>大部分产品的构建，使用简单工程或工厂方法即可完成。</p>
<h1 data-id="heading-3">🎏 04. 小结</h1>
<p>是的，写文章好累，输出和输入是不一样啊，有这事件，可以刷好多抖音了，哈！</p>
<p>养成一个好习惯，需要不停的激励和鼓励，写作的能力也许就是不断的写中提升的，当然还有自身的额能力，在不断的输出过程中，发现自己的不足以及巩固自己的知识。</p>
<p>30天不停更，目标很远大，今天是第四天，加油吧，兄弟们！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            