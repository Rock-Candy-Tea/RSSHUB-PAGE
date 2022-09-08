
---
title: '如何在Java中使用Optional功能'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8134'
author: 掘金
comments: false
date: Mon, 05 Sep 2022 19:31:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=8134'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">尽管存在争议，但Optiont极大地改进了Java应用程序的设计。在本文中，我们将了解如何、何时以及在哪里最好地应用Optional。</h3>
<p><code>Optional</code>类的引入是Java语言设计的重大改进，但这一改进一直存在争议。在<code>Optional</code>类之前，许多开发人员使用<code>null</code>或异常来表示何时不存在所需的值；然而，使用<code>Optional</code>类可以让我们明确说明何时可能存在或不存在值。尽管有这种改进，但<code>Optional</code>类可能会不恰当地应用，弊大于利。</p>
<p>在本文中，我们将研究<code>Optional</code>类的基本原理，包括：</p>
<ul>
<li>其引入背后的目的和思维过程</li>
<li><code>Optional</code>课程中包含的基本方法</li>
<li>使用<code>Optional</code>课程的适当时间和地点</li>
<li>一些可以替代的技术</li>
</ul>
<p>Java，像大多数面向对象(OO)语言一样，对它的类型系统有一个秘密的后门。例如，假设我们有以下方法签名:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> Foo <span class="hljs-title function_">doSomething</span><span class="hljs-params">()</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然，此方法返回类型为<code>Foo</code>的对象，但它也可以返回另一个值：<code>null</code>。由于任何非原始类型都可以设置为<code>null</code>，因此没有什么可以阻止开发人员编写以下方法实现：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> Foo <span class="hljs-title function_">doSomething</span><span class="hljs-params">()</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">Nullity</h3>
<p>这为调用此方法的客户端造成了一个繁琐的情况。在使用从<code>doSomething</code>方法返回的<code>Foo</code>对象之前，客户端必须首先检查该对象是否为<code>null</code>：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> doSomething();
<span class="hljs-keyword">if</span> (foo == <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">// handle null case...</span>
&#125;
<span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// do something with the foo object...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法确保了Foo对象的使用不会导致<code>NullPointerException</code> (NPE)。然而，这又产生了另一个问题:任何非原语对象都可以隐式地设置为<code>null</code>。因此，在使用方法之前，我们必须彻底检查方法返回的每个对象是否为空。不用说，这不仅在大型应用程序中是不可行的，而且还会混淆代码的清晰度。例如，为<code>null</code>检查添加额外的行会在整个应用程序中引入样板代码，使Foo对象的使用变得不那么清晰(隐藏在<code>if-else</code>语句中)。</p>
<p>根本问题是，我们不知道方法何时打算返回<code>null</code>——例如当找不到所需的值时——或者可以根据要求保证永远不会返回<code>null</code>。由于我们不确定，我们被迫假设<em>任何</em>返回的对象都可以为<code>null</code>。</p>
<p>一个常用的解决方案是记录使用<code>JavaDocs</code>返回值可以为<code>null</code>。虽然这是对原始问题的改进，但这并不能确保客户端在使用对象之前检查空性（即Java编译器将毫无怨无故地编译代码，而无需进行这些<code>null</code>检查）。同样，像<code>@NotNull</code>注释也存在，但这些注释与文档方法存在相同的缺点。也就是说，可以规避执法。</p>
<h3 data-id="heading-2"><code>Optional</code> Class</h3>
<p>相反，我们需要一种机制，允许方法开发人员显式表示方法的返回值可能存在，也可能不存在。该机制以[<code>Optional</code>]类的形式在Java开发工具包（JDK）7中引入。该类充当可能不存在的对象的包装器。因此，如果我们知道我们的<code>doSomething</code>方法可能不会返回所需的<code>Foo</code>对象，我们可以将签名更改为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> Optional<Foo> <span class="hljs-title function_">doSomething</span><span class="hljs-params">()</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正如我们将在以下各节中看到的，<code>Optional</code>提供了一套方法——许多功能性——允许客户端在不存在所需值时决定该怎么做。例如，当找不到所需的值时，我们可以使用<code>orElse</code>方法返回默认值（在<code>Optional</code>词典中称为<em>空</em>的<code>Optional</code>）</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> doSomething().orElse(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Foo</span>());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，当<code>Optional</code>使用<code>orElseThrow</code>方法为空时，我们也可以抛出异常：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> doSomething().orElseThrow(SomeException::<span class="hljs-keyword">new</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重要的是要注意两件事：</p>
<ol>
<li>Java编译器迫使我们处理空<code>Optional</code>值的情况</li>
<li>客户负责处理缺失的期望值</li>
</ol>
<p>虽然文档和注释确实将我们推向了正确、更明确的方向，但它们不允许我们将检查缺失值的责任强加给客户。另一方面，<code>Optional</code>对象要求客户端决定如何处理缺失的值。</p>
<p>例如，以下内容不会编译：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> doSomething();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相反，我们将看到一个编译错误，提醒我们，类型为<code>Optional<Foo></code>的对象不能转换为<code>Foo</code>，因为<code>doSomething</code>的返回类型是<code>Optional<Foo></code>，而<code>foo</code>的类型是<code>Foo</code>。因此，我们必须调用<code>orElse</code>或<code>orElseThrow</code>等方法——或<code>get</code>，但我们稍后会看到为什么这不应该是首选——以便将<code>Optional<Foo></code>对象转换为<code>Foo</code>对象。由于这两种方法都需要一个参数，因此，它们要求我们明确决定使用什么默认值，或者如果<code>Optional</code>为空，则抛出什么异常。</p>
<h3 data-id="heading-3">客户责任</h3>
<p>这让我们注意到（2）：处理空的<code>Optional</code>的责任在于客户。从本质上讲，<code>doSomething</code>方法——本质上返回<code>Optional<Foo></code>而不是<code>Foo</code>——告诉客户端，可能无法找到结果。因此，当找不到结果时，客户端现在负责处理案件（即必须调用其中一种<code>Optional</code>方法，如<code>orElse</code>，才能从<code>Optional<Foo></code>到<code>Foo</code>）。</p>
<p>这种对客户端负责的方法意味着方法开发人员没有足够的信息来确定在缺少值的情况下应该做什么。当找不到值时，开发人员可以抛出异常，但缺失的值可能不是需要例外的情况（即它可能不是<em>例外</em>情况）。</p>
<p>例如，如果我们想检查一个对象是否已经存在，或者如果没有，创建一个，那么不存在的对象不会是一个错误，抛出异常是没有道理的。此外，抛出异常需要我们在调用代码中捕获异常，以创建默认值。例如，假设我们创建以下方法：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-function"><span class="hljs-keyword">public</span> Foo <span class="hljs-title">findIfExists</span>() throws FooNotFoundException</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要使用现有值，或者如果不存在，则创建默认值，我们必须执行以下操作：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> <span class="hljs-literal">null</span>;
<span class="hljs-keyword">try</span> &#123;
    foo = findIfExists();
&#125;
<span class="hljs-keyword">catch</span> (FooNotFoundException e) &#123;
    foo = <span class="hljs-comment">// create default value...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相反，我们可以从<code>findIfExists</code>返回<code>Optional</code>值：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-function"><span class="hljs-keyword">public</span> Optional<Foo> <span class="hljs-title">findIfExists</span>()</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们可以简单地使用<code>orElse</code>方法来提供默认值：</p>
<pre><code class="hljs language-ini copyable" lang="ini">Foo <span class="hljs-attr">foo</span> = findIfExists().orElse(/* create default value... */)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，后一种方法可读性更强。通过简单地阅读代码，我们知道这两行意味着查找是否存在或使用该值。在前一种情况下，当<code>findIfExists</code>无法找到现有值时，我们必须有意识地将<code>catch</code>子句的含义派生为默认值。因此，<code>Optional</code>词汇比异常方法更接近预期的含义。</p>
<p>了解这一点，当客户端负责处理丢失的对象<em>而</em>缺少对象不是错误时，<code>Optional</code>是一种有用的技术。有时，缺失的值可能是错误——例如，当我们假设一个值存在，而其缺失可能会给应用程序带来致命结果时——方法应该抛出一个选中或未检查的异常。然而，在某些情况下（例如<code>findIfExists</code>方法），缺席对象不是错误，使用<code>Optional</code>是确保客户端显式处理缺失对象的有效方法。</p>
<h3 data-id="heading-4"><code>null</code> <code>Optional</code> Objects</h3>
<p>必须解决一个警告：<code>Optional</code>对象可能是<code>null</code>的。由于<code>Optional</code>对象和<code>Foo</code>一样是非原始对象，因此它们也可以设置为<code>null</code>。例如，<code>doSomething</code>的以下实现将编译无错误：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-function"><span class="hljs-keyword">public</span> Optional<Foo> <span class="hljs-title">doSomething</span>()</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这将导致客户端必须同时处理<code>null</code>返回值<em>和</em>处理空<code>Optional</code>情况的奇怪情况：</p>
<pre><code class="hljs language-ini copyable" lang="ini">Optional<Foo> <span class="hljs-attr">possibleFoo</span> = doSomething()<span class="hljs-comment">;</span>
if (<span class="hljs-attr">possibleFoo</span> == null) &#123;
    // handle missing object case...
&#125;
else &#123;
    Foo <span class="hljs-attr">foo</span> = possibleFoo.orElse(/* handle missing object case... */)<span class="hljs-comment">; </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这不仅为丢失的对象情况带来了重复（即在两个位置处理丢失的对象的情况），而且还重新引入了清晰度降低的问题。相反，当从方法返回<code>Optional</code>值时，我们不应该检查<code>null</code>值。根据<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F14%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Futil%2FOptional.html%23of(T)" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/Optional.html#of(T)" ref="nofollow noopener noreferrer"><code>Optional</code>类文档</a>：</p>
<blockquote>
<p>类型为<code>Optional</code>的变量本身永远不应该<code>null</code>；它应该始终指向<code>Optional</code>实例。</p>
</blockquote>
<p>如果返回<code>null</code>值代替<code>Optional</code>对象，则方法开发人员违反了方法规定。通过声明方法将返回<code>Optional</code>对象，方法开发人员还声明返回<code>null</code>无效。由于<code>Optional</code>对象表示对象丢失的可能性，因此<code>null</code>值没有有效的用例（即方法在所有情况下都应该返回空的<code>Optional</code>而不是<code>null</code>）。</p>
<p>因此，每当我们处理<code>Optional</code>对象时，我们正确地假设<code>Optional</code>对象永远不会为<code>null</code>。虽然<code>Optional</code>对象在实践中可能是<code>null</code>的，但这个问题应该由方法开发人员而不是客户端解决。</p>
<h2 data-id="heading-5">重要方法</h2>
<p>通过了解<code>Optional</code>类背后的概念，我们现在可以看看如何在实践中使用<code>Optional</code>对象。<code>Optional</code>类包含大量方法，可以分为两类：创建方法和实例方法。</p>
<h3 data-id="heading-6">创建方法</h3>
<p><code>Optional</code>创建方法是静态方法，允许我们创建各种<code>Optional</code>对象来满足我们的需求。目前有三种这样的方法：一种用于创建填充的<code>Optional</code>（即包装值不是<code>null</code>的Optional），一种用于创建填充或空的<code>Optional</code>，一种用于创建空的<code>Optional</code>。</p>
<h4 data-id="heading-7"><code>of</code></h4>
<p>方法<code>of</code>静态允许我们用<code>Optional</code>对象包装现有对象。如果现有对象不是<code>null</code>，则返回填充的<code>Optional</code>：</p>
<pre><code class="hljs language-ini copyable" lang="ini">Optional<Foo> <span class="hljs-attr">foo</span> = Optional.of(new Foo())<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果现有对象为<code>null</code>，则抛出NPE：</p>
<pre><code class="hljs language-ini copyable" lang="ini">Optional<Foo> <span class="hljs-attr">foo</span> = Optional.of(null)<span class="hljs-comment">; // 抛出 NullPointerException</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8"><code>ofNullable</code></h4>
<p>当传递非<code>null</code>值时， <code>ofNullable</code>静态方法与方法相同（即生成填充的<code>Optional</code>），但在传递<code>null</code>时将生成空<code>Optional</code>（即不会抛出NPE）：</p>
<pre><code class="hljs language-vbnet copyable" lang="vbnet"><span class="hljs-keyword">Optional</span><Foo> foo1 = <span class="hljs-keyword">Optional</span>.ofNullable(<span class="hljs-built_in">new</span> Foo()); // populated <span class="hljs-keyword">Optional</span>
<span class="hljs-keyword">Optional</span><Foo> foo2 = <span class="hljs-keyword">Optional</span>.ofNullable(null); // null <span class="hljs-keyword">Optional</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当对象的空性未知时，通常使用这种方法。</p>
<h4 data-id="heading-9"><code>empty</code></h4>
<p><code>empty</code>静态方法只需创建一个空的<code>Optional</code>：</p>
<pre><code class="hljs language-ini copyable" lang="ini">Optional<Foo> <span class="hljs-attr">foo</span> = Optional.empty()<span class="hljs-comment">; // empty</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据定义，这种方法与以下方法相同：</p>
<pre><code class="hljs language-ini copyable" lang="ini">Optional<Foo> <span class="hljs-attr">foo</span> = Optional.ofNullable(null)<span class="hljs-comment">;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正如我们将在下面几节中看到的，<code>empty</code> 通常在已知没有值存在的情况下使用。</p>
<h3 data-id="heading-10">实例方法</h3>
<p>实例方法允许我们与现有的<code>Optional</code>对象交互，并主要专注于查询<code>Optional</code>对象的状态，从<code>Optional</code>对象获取包装对象，并操作<code>Optional</code>对象。</p>
<h4 data-id="heading-11"><code>isPresent</code>&<code>isEmpty</code></h4>
<p><code>Optional</code>类中包含两种查询方法，允许我们检查给定的<code>Optional</code>是填充的还是空的：</p>
<ol>
<li><code>isPresent</code>：如果填充了<code>Optional</code>，则返回<code>true</code>，否则返回<code>false</code></li>
<li><code>isEmpty</code>：如果<code>Optional</code>为<code>empty</code>，则返回<code>true</code>，否则返回<code>false</code></li>
</ol>
<p>因此，给定填充的<code>Optional</code>，查询方法将返回以下内容：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">Optional<Foo> populated = <span class="hljs-regexp">//</span> ...populated Optional...
populated.isPresent(); <span class="hljs-regexp">//</span> <span class="hljs-literal">true</span>
populated.isEmpty(); <span class="hljs-regexp">//</span> <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给定一个空的<code>Optional</code>，查询方法将返回以下内容：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">Optional<Foo> empty = <span class="hljs-regexp">//</span> ...empty Optional...
populated.isPresent();    <span class="hljs-regexp">//</span> <span class="hljs-literal">false</span>
populated.isEmpty();      <span class="hljs-regexp">//</span> <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><code>get</code></h4>
<p>如果<code>Optional</code>被填充，<code>get</code>方法将获得由<code>Optional</code>包装的值，如果<code>Optional</code>为空，则抛出NoSuchElementException。当我们可以保证填充Optional时，此方法可用于将现有<code>Optional</code>转换为其值（即从<code>Optional<Foo></code>转换为<code>Foo</code>），但我们应该谨慎使用此方法。</p>
<p>在实践中，保证填充<code>Optional</code>需要我们首先使用<code>isPresent</code>或<code>isEmpty</code>方法查询<code>Optional</code>，然后调用<code>get</code>：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
<span class="hljs-keyword">if</span> (possibleFoo.isPresent()) &#123;
    <span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> possibleFoo.get();
    <span class="hljs-comment">// ...use the foo object...</span>
&#125;
<span class="hljs-keyword">else</span> &#123;
<span class="hljs-comment">// ...handle case of missing Foo...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种模式的问题在于，这与我们在引入<code>Optional</code>之前执行的<code>null</code>检查非常相似。因此，这种方法消除了<code>Optional</code>类的固有好处。在大多数情况下，我们应该避免使用<code>get</code>方法，并使用其他方法之一（如<code>orElse</code>或<code>orElseThrow</code>）来获取与填充的<code>Optional</code>值相关联。</p>
<h4 data-id="heading-13"><code>orElse</code>系列</h4>
<p><code>orElse</code>系列方法允许我们获得由<code>Optional</code>包装的值（如果填充了<code>Optional</code>），或者如果<code>Optional</code>为空，则获取默认方法。这个系列中最简单的方法是<code>orElse</code>，它接受包装类型的对象，如果<code>Optional</code>是空的，则返回它。例如，给定anOptional<code>Optional<Foo></code>对象，<code>orElse</code>方法接受一个<code>Foo</code>对象。如果填充了<code>Optional</code>，它会返回填充值；如果<code>Optional</code>为空，则返回我们传递给<code>orElse</code>方法的<code>Foo</code>对象：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
<span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> possibleFoo.orElse(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Foo</span>());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，有时创建默认值可能是一项昂贵的操作，并且不太可能使用。例如，默认值可能需要建立到远程服务器的连接，或者可能需要从数据库进行扩展或大型查找。如果可能填充<code>Optional</code>，我们不太可能需要默认值。使用<code>orElse</code>方法，即使未使用，我们也被迫创建默认值，这可能会导致严重的性能影响。</p>
<p><code>Optional</code>类还包括<code>orElseGet</code>方法，该方法采用可以懒散创建默认对象的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F14%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Futil%2Ffunction%2FSupplier.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/function/Supplier.html" ref="nofollow noopener noreferrer"><code>Supplier</code></a>。这允许<code>Optional</code>类仅在需要时创建默认对象（即仅在<code>Optional</code>为空时创建默认对象）。例如：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
<span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> possibleFoo
    .orElseGet(() -> &#123; <span class="hljs-comment">/* ...lazily create a Foo object... */</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14"><code>orElseThrow</code>系列</h4>
<p>与<code>orElse</code>方法类似，<code>Optional</code>类提供了一个<code>orElseThrow</code>方法，如果<code>Optional</code>为空，则允许我们在获取包装值时抛出异常。然而，与<code>orElse</code>方法不同，<code>orElseThrow</code>方法有两种形式：</p>
<ol>
<li>无参数形式，如果<code>Optional</code>为空，则抛出<code>NoSuchElementException</code>，如果<code>Optional</code>填充，则返回包装值</li>
<li>一个接受<code>Supplier</code>的表单，该<code>Supplier</code>创建<code>Throwable</code>对象，并在<code>Optional</code>为空时抛出<code>Throwable</code>对象，或在<code>Optional</code>填充时返回包装好的值</li>
</ol>
<p>例如，我们可以从<code>Optional<Foo></code>对象中获取<code>Foo</code>对象，如下所示：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
<span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> possibleFoo
    .orElseThrow();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>Optional</code>是空的，将抛出<code>NoSuchElementException</code>。如果填充了<code>Optional</code>，则将返回包装值。因此，<code>orElseThrow</code>方法的功能与<code>get</code>方法相同，但它的名称更好地描述了其目的。因此，当<code>Optional</code>未填充时，<code>orElseThrow</code>方法应使用任何值的任何地方来抛出<code>NoSuchElementException</code>，而无需首先检查它是否已填充（即不使用<code>isPresent</code>或<code>isEmpty</code>查询方法）。</p>
<p><code>get</code>方法仅当在<code>Optional</code>查询方法之一中使用时才应保留用于（即首先选中<code>Optional</code>的填充或空状态）。请注意，此<code>orElseThrow</code>方法是在JDK 9中引入的，以减少围绕<code>get</code>方法使用的混乱，应该比get方法更喜欢。</p>
<blockquote>
<p>我们[在Java 8]中犯的少数错误之一是命名<code>Optional.get()</code>，因为这个名字只是邀请人们在不调用<code>isPresent()</code>用它，首先破坏了使用<code>Optional</code>的全部意义......</p>
</blockquote>
<blockquote>
<p>在Java 9时间范围内，我们建议弃用<code>Optional.get()</code>，但公众对此的反应是......比说冷。作为较小的一步，我们在[Java] 10中引入了<code>orElseThrow()</code>...作为当前<code>get()</code>有害行为的更透明的同义词。</p>
</blockquote>
<p><code>Optional</code>类还包括一个重载的<code>orElseThrow</code>方法，当<code>Optional</code>为空时，该方法会抛出自定义异常。此方法接受创建任何<code>Throwable</code>对象或<code>Throwable</code>子类的对象的<code>Suppler</code>并抛出它。例如：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
<span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> possibleFoo.orElseThrow(() -> &#123; <span class="hljs-comment">/* ...lazily create a Foo object... */</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当客户端认为丢失的对象是一个错误，并希望在访问空的<code>Optional</code>时抛出异常时，这非常有用。使用构造函数的功能形式抛出简单的异常也是一种常见的做法：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
<span class="hljs-type">Foo</span> <span class="hljs-variable">foo</span> <span class="hljs-operator">=</span> possibleFoo.orElseThrow(SomeException::<span class="hljs-keyword">new</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15"><code>ifPresent</code>系列</h4>
<p>如果Optional被填充，ifPresent方法接受一个Consumer，该Consumer使用包装的值执行操作。这是使用orElse或orElseThrow方法获得包装对象的函数替代，主要是当我们不希望在值不存在的情况下执行任何操作时。例如:</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
possibleFoo.ifPresent(foo -> &#123; <span class="hljs-comment">/* ...do something with foo... */</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Optional</code>类还包括类似的方法，<code>ifPresentOrElse</code>，允许我们在<code>Optional</code>也是空时处理案例。<code>ifPresentOrElse</code>方法接受的第一个参数是<code>Consumer</code>，如果填充了<code>Optional</code>，则使用包装值执行操作，而第二个参数是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F14%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Flang%2FRunnable.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/lang/Runnable.html" ref="nofollow noopener noreferrer"><code>Runnable</code></a>，如果<code>Optional</code>为空，则执行操作。因此，只有当<code>Optional</code>被填充时才会调用<code>Consumer</code>，而只有当<code>Optional</code>为空时，才会调用<code>Runnable</code>。例如：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Foo> possibleFoo = doSomething();
possibleFoo.ifPresentOrElse(
    foo -> &#123; <span class="hljs-comment">/* ...do something with foo... */</span> &#125;,
    () -> &#123; <span class="hljs-comment">/* ...do something when no foo found... */</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两种方法的好处是，如果<code>Optional</code>为空，则永远不会调用<code>Consumer</code>。同样，在<code>ifPresentOrElse</code>的情况下，如果填充了<code>Optional</code>，则永远不会调用<code>Runnable</code>。这使我们能够提供复杂或昂贵的操作，这些操作将根据<code>Optional</code>状态被懒惰地调用。</p>
<p>请注意，这种方法不应该仅仅用于昂贵的操作。每当对填充值执行操作时，都应使用此方法。例如，如果我们只想在对象存在的情况下更新它，我们可以做一些类似于以下内容的事情：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Bar</span> &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-type">boolean</span> <span class="hljs-variable">isUpdated</span> <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">update</span><span class="hljs-params">()</span> &#123;
        isUpdated = <span class="hljs-literal">true</span>;
    &#125;
&#125;
<span class="hljs-keyword">public</span> Optional<Bar> <span class="hljs-title function_">findBar</span><span class="hljs-params">()</span> &#123;
    <span class="hljs-comment">// ...return a populated Bar if it could be found...</span>
&#125;
findBar().ifPresent(bar -> bar.update());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，如果找不到<code>Bar</code>对象，我们不关心执行任何操作。如果我们是，我们可以改用<code>ifPresentOrElse</code>方法。</p>
<h4 data-id="heading-16"><code>map</code></h4>
<p>如果填充了<code>Optional</code>，<code>map</code>方法允许我们将包装值从一个对象转换为另一个对象。这种方法可以被认为是一种管道方法，其中包装的值沿着管道传递并转换为新值。此方法的工作原理是接受应用于包装值的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F14%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Futil%2Ffunction%2FFunction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/function/Function.html" ref="nofollow noopener noreferrer"><code>Function</code></a>对象，以生成映射值。如果<code>Optional</code>是空的，则永远不会调用<code>Function</code>对象，并且从<code>map</code>方法返回空的<code>Optional</code>。</p>
<p>当我们不知道是否存在一个值时，这种方法非常有用，但如果存在，它应该转换为另一个对象。这是从数据库读取时常见的用例，数据库通常存储数据传输对象（DTO）。在大多数应用程序中，DTO用于有效地将域对象存储在数据库中，但在应用程序的更高级别上，需要域对象本身。因此，我们必须从DTO转换为域对象。</p>
<p>如果我们对数据库对象进行查找，我们可能会找到也可能找不到该对象。因此，这是返回<code>Optional</code>包装DTO的好用例。为了转换为域对象，我们可以使用<code>map</code>方法。例如，假设我们有一个DTO（<code>PersonDto</code>），将<code>Person</code>对象的名称存储在一行中，而<code>Person</code>对象的名称分为名字和姓氏（即，该名称在<code>PersonDto</code>对象中存储为<code>"John Doe"</code>但它在<code>Person</code>对象中以<code>"John"</code>的名字和<code>"Joe"</code>的姓氏存储）。我们可以使用映射器对象从<code>PersonDto</code>转换为<code>Person</code>对象，并使用映射器将从数据库返回的<code>PersonDto</code>对象映射到<code>Person</code>对象：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Person</span> &#123;
    <span class="hljs-keyword">private</span> String firstName;
    <span class="hljs-keyword">private</span> String lastName;
    <span class="hljs-comment">// ...getters & setters...</span>
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">PersonDto</span> &#123;
    <span class="hljs-keyword">private</span> String name;
    <span class="hljs-comment">// ...getters & setters...</span>
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">PersonMapper</span> &#123;
    <span class="hljs-keyword">public</span> Person <span class="hljs-title function_">fromDto</span><span class="hljs-params">(PersonDto dto)</span> &#123;
        String[] names = dto.getName().split(<span class="hljs-string">"\s+"</span>);
        <span class="hljs-type">Person</span> <span class="hljs-variable">person</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Person</span>();
        person.setFirstName(names[<span class="hljs-number">0</span>]);
        person.setLastName(names[<span class="hljs-number">1</span>]);
        <span class="hljs-keyword">return</span> person;
    &#125;
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Database</span> &#123;
    <span class="hljs-keyword">public</span> Optional<PersonDto> <span class="hljs-title function_">findPerson</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-comment">// ...return populated DTO if DTO is found...</span>
    &#125;
&#125;
<span class="hljs-type">Database</span> <span class="hljs-variable">db</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Database</span>();
<span class="hljs-type">PersonMapper</span> <span class="hljs-variable">mapper</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">PersonMapper</span>();
Optional<Person> person = db.findPerson()
    .map(mapper::fromDto);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，可能有一个转换会导致一个空的<code>Optional</code>。例如，如果从给定对象到另一个对象的转换是不可能的，那么<code>map</code>方法应该返回一个空的<code>Optional</code>。执行这种技术的反模式是让<code>Function</code>对象返回<code>null</code>，然后用<code>map</code>方法(使用<code>ofNullable</code>，它允许我们的<code>null</code>对象在不抛出异常的情况下被包装)包装到空的可选对象中:</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Person> person = db.findPerson()
    .map(dto -> &#123;
        <span class="hljs-keyword">if</span> (dtoCanBeConverted()) &#123;
            <span class="hljs-keyword">return</span> mapper.fromDto(dto);
       &#125;
       <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果方法<code>dtoCanBeConverted</code>计算为<code>false</code>，则<code>Function</code>对象返回<code>null</code>，从而导致<code>person</code>为空的<code>Optional</code>。这种方法存在缺陷，因为它重新引入了<code>null</code>值的隐式使用，其替换是<code>Optional</code>类的原始目的。相反，我们应该使用<code>flatMap</code>方法，并显式返回一个空的<code>Optional</code>。</p>
<h4 data-id="heading-17"><code>flatMap</code></h4>
<p><code>flatMap</code>方法类似于<code>map</code>方法，但<code>flatMap</code>接受一个<code>Function</code>对象，该函数将包装值转换为新的<code>Optional</code>。与<code>map</code>方法不同，<code>flatMap</code>允许我们返回我们选择的<code>Optional</code>。因此，如果映射<code>Function</code>无法转换包装值，我们可以显式返回空的<code>Optional</code>值：</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Person> person = db.findPerson()
    .flatMap(dto -> &#123;
        <span class="hljs-keyword">if</span> (dtoCanBeConverted()) &#123;
            <span class="hljs-type">Person</span> <span class="hljs-variable">person</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">return</span> dao.fromDto(dto);
            <span class="hljs-keyword">return</span> Optional.ofNullable(person);
        &#125;
        <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> Optional.empty();
        &#125;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，我们不再能够像使用<code>map</code>方法那样简单地返回<code>Person</code>对象。相反，我们现在负责将转换后的对象包装成<code>Optional</code>。注意，如果<code>Function</code>对象返回<code>null Optional</code>，则抛出一个<code>NPE</code>。例如，以下代码在执行时会抛出一个<code>NPE</code>:</p>
<pre><code class="hljs language-java copyable" lang="java">Optional<Person> person = db.findPerson()
    .flatMap(dto -> <span class="hljs-literal">null</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18"><code>filter</code></h4>
<p>如果填充的<code>Optional</code>满足提供的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F14%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Futil%2Ffunction%2FPredicate.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/function/Predicate.html" ref="nofollow noopener noreferrer"><code>Predicate</code></a>，则<code>filter</code>方法允许我们返回填充的<code>Optional</code>。因此，如果<code>filter</code>方法应用于空的<code>Optional</code>，则不会调用<code>Predicate</code>。同样，如果<code>filter</code>方法应用于填充的<code>Optional</code>，但包装值不满足提供的<code>Predicate</code>（即<code>Predicate</code>对象的<code>test</code>方法计算<code>false</code>），则返回一个空的<code>Optional</code>。例如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Bar</span> &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-type">int</span> number;
    <span class="hljs-keyword">public</span> <span class="hljs-title function_">Bar</span><span class="hljs-params">(<span class="hljs-type">int</span> number)</span> &#123;
        <span class="hljs-built_in">this</span>.number = number;
    &#125;
    <span class="hljs-comment">// ...getters & setters...</span>
&#125;
Predicate<Bar> greaterThanZero = bar -> bar.getNumber() > <span class="hljs-number">0</span>;
Optional.of(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Bar</span>(<span class="hljs-number">1</span>))
    .filter(greaterThanZero)
    .isPresent();              <span class="hljs-comment">// true</span>
Optional.of(<span class="hljs-keyword">new</span> <span class="hljs-title class_">Bar</span>(-<span class="hljs-number">1</span>))
    .filter(greaterThanZero)
    .isPresent();              <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">何时使用</h2>
<p><code>Optional</code>类最具争议的方面之一是何时应该和不应该使用它。在本节中，我们将研究一些常见的用例，例如方法返回值、字段和参数，其中<code>Optional</code>可能非常适合也可能不合适。</p>
<h3 data-id="heading-20">返回值</h3>
<p>正如我们在本文中看到的那样，<code>Optional</code>值非常适合方法返回值，因为这是其预期目的。根据<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F14%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Futil%2FOptional.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/util/Optional.html" ref="nofollow noopener noreferrer"><code>Optional</code>类文档</a>：</p>
<blockquote>
<p><code>Optional</code>主要用于方法返回类型，其中明确需要表示“无结果”，并且使用<code>null</code>可能会导致错误。</p>
</blockquote>
<p>一般来说，在以下情况下，应使用<code>Optional</code>作为返回值：</p>
<ol>
<li>预计一个值可能存在，也可能不存在</li>
<li>如果缺少值，这不是错误</li>
<li>客户负责处理丢失价值的情况</li>
</ol>
<p><code>Optional</code>返回值通常用于可能找到或找不到所需对象的查询。例如，存储库通常将以以下方式定义：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">interface</span> <span class="hljs-title class_">BookRepository</span> &#123;
    <span class="hljs-keyword">public</span> Optional<Book> <span class="hljs-title function_">findById</span><span class="hljs-params">(<span class="hljs-type">long</span> id)</span>;
    <span class="hljs-keyword">public</span> Optional<Book> <span class="hljs-title function_">findByTitle</span><span class="hljs-params">(String title)</span>;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这允许客户端以适合调用方法的上下文的方式处理丢失的<code>Book</code>对象，例如忽略丢失的对象、创建默认对象或抛出异常。</p>
<h3 data-id="heading-21">字段</h3>
<p>虽然<code>Optional</code>对象非常适合返回类型，但它们不太适合例如字段。可以创建一个类似于以下内容的字段，但这是非常不可取的：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Bar</span> &#123;
    <span class="hljs-keyword">private</span> Optional<Foo> foo;
    <span class="hljs-comment">// ...getters & setters...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Optional</code>应避免字段，因为<code>Optional</code>类不可序列化（即没有实现<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.oracle.com%2Fen%2Fjava%2Fjavase%2F14%2Fdocs%2Fapi%2Fjava.base%2Fjava%2Fio%2FSerializable.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/io/Serializable.html" ref="nofollow noopener noreferrer"><code>Serializable</code></a>接口）。</p>
<blockquote>
<p>当然，人们会做他们想做的事。但我们添加此功能时确实有明确的意图，<em>这不是</em>一个通用的目的，也许类型，就像许多人希望我们这样做一样。我们的意图是为库方法返回类型提供有限的机制，其中需要一种明确的方法来表示“无结果”，因此使用<code>null</code>极有可能导致错误。</p>
</blockquote>
<p>因此，<code>Optional</code>类型仅适用于方法返回类型。由于字段构成类的内部状态，外部客户端不应可见，如果字段被认为是可选的，则可以创建一个getter，返回<code>Optional</code>对象：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Bar</span> &#123;
    <span class="hljs-keyword">private</span> Foo foo;
    <span class="hljs-keyword">public</span> Optional<Foo> <span class="hljs-title function_">getFoo</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-keyword">return</span> Optional.ofNullable(foo);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用这种技术，客户会明确被告知<code>foo</code>值可能存在，也可能不存在，同时保持<code>Bar</code>的可序列化性。</p>
<h3 data-id="heading-22">参数</h3>
<p>在有效的情况下，方法或构造函数的参数可能是可选的，但<code>Optional</code>的不应用于此目的。例如，应避免以下情况：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Bar</span> &#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">doSomething</span><span class="hljs-params">(Optional<Foo> foo)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不应将参数类型设置为<code>Optional</code>，而应使用方法重载：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Bar</span> &#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">doSomething</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">doSomething</span><span class="hljs-params">(Bar bar)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，具有不同方法名称的非过载方法也可以使用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Bar</span> &#123;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">doSomething</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">doSomethingWithBar</span><span class="hljs-params">(Bar bar)</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">替代方案</h2>
<p>虽然<code>Optional</code>类在正确的上下文中有效，但当可能找到或找不到所需的值时，它并不是可以使用的唯一方法。在本节中，我们涵盖了<code>Optional</code>类的三种替代方案，以及如何在适当的上下文中应用它们。</p>
<h3 data-id="heading-24"><code>null</code></h3>
<p>最简单的替代方案是使用<code>null</code>，正如我们在本文开头看到的那样。虽然这种方法确实实现了我们的目标，但在引入<code>Optional</code>类后，仅当<code>Optional</code>对象需要太多的开销时，才应使用<code>null</code>。此开销可以是<code>Optional</code>包装类的额外内存需求，也可以是执行<code>Optional</code>方法所需的额外周期。</p>
<p>在<code>Optional</code>更有效的情况下，人们很容易以性能为借口使用<code>null</code>，但是在大多数应用程序中，<code>Optional</code>类只增加了少量的开销。除非我们处理的是低级代码，就像来自网络或驱动程序的字节一样，或者我们处理的是极其大量的数据，否则对于方法返回类型来说，可选项应该总是优先于<code>null</code>。</p>
<h3 data-id="heading-25">空对象</h3>
<p>比<code>null</code>值更有效的替代方案是<a href="https://link.juejin.cn/?target=https%3A%2F%2Frefactoring.guru%2Fintroduce-null-object" target="_blank" rel="nofollow noopener noreferrer" title="https://refactoring.guru/introduce-null-object" ref="nofollow noopener noreferrer">引入空对象</a>。null对象是扩展所需类型的对象，但包含本应为<code>null</code>大小写执行的逻辑。例如，假设我们有以下代码：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Article</span> &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-type">long</span> id;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">submit</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-comment">// ...getters & setters...</span>
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">ArticleRepository</span> &#123;
    <span class="hljs-keyword">public</span> Article <span class="hljs-title function_">findById</span><span class="hljs-params">(<span class="hljs-type">long</span> id)</span> &#123;
        <span class="hljs-comment">// ...return the article if it can be found...</span>
    &#125;
&#125;
<span class="hljs-type">ArticleRepository</span> <span class="hljs-variable">repository</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">ArticleRepository</span>();
<span class="hljs-type">Article</span> <span class="hljs-variable">article</span> <span class="hljs-operator">=</span> repository.findById(<span class="hljs-number">1</span>);
<span class="hljs-keyword">if</span> (article == <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">ArticleNotFoundException</span>();
&#125;
<span class="hljs-keyword">else</span> &#123;
    article.submit();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以使用空对象重构此代码到以下内容：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Article</span> &#123;
    <span class="hljs-comment">// ...same as before...</span>
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">NullArticle</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_">Article</span> &#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title function_">submit</span><span class="hljs-params">()</span> &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">ArticleNotFoundException</span>();
    &#125;
&#125;
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">ArticleRepository</span> &#123;
    <span class="hljs-keyword">public</span> Article <span class="hljs-title function_">findById</span><span class="hljs-params">(<span class="hljs-type">long</span> id)</span> &#123;
        <span class="hljs-keyword">if</span> (articleIsFound()) &#123;
            <span class="hljs-comment">// return article...</span>
        &#125;
        <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">NullArticle</span>();
        &#125;
    &#125;
&#125;
<span class="hljs-type">ArticleRepository</span> <span class="hljs-variable">repository</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">ArticleRepository</span>();
<span class="hljs-type">Article</span> <span class="hljs-variable">article</span> <span class="hljs-operator">=</span> repository.findById(<span class="hljs-number">1</span>);
article.submit();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，引入空对象假设方法本身知道如何处理缺失值的情况。</p>
<h3 data-id="heading-26">例外情况</h3>
<p>我们在本文中看到的另一个替代方案是在找不到所需对象时抛出异常。如果方法知道未能找到所需的对象是一个错误，则此方法有效。例如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">ArticleRepository</span> &#123;
    <span class="hljs-keyword">public</span> Article <span class="hljs-title function_">findById</span><span class="hljs-params">(<span class="hljs-type">long</span> id)</span> &#123;
        <span class="hljs-keyword">if</span> (articleIsFound()) &#123;
            <span class="hljs-comment">// return article...</span>
        &#125;
        <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">ArticleNotFoundException</span>();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">结论</h2>
<p>在许多情况下，所需的值可能存在于也可能不存在于应用程序中，以可读和有效的方式处理这些情况是精心设计的软件的重要组成部分。从JDK 7开始，Java包括<code>Optional</code>类，该类允许开发人员返回可能存在也可能不存在的值，并允许客户端根据发生这些情况的上下文处理这些情况。虽然<code>Optional</code>类只能用于方法返回值，但了解其有用性以及如何使用简单技术应用它是掌握现代Java的重要组成部分。</p></div>  
</div>
            