
---
title: '【译】你真的应该使用useMomo 吗_ 让我们一起来看看'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53fd3f899ffc4564bbb3f39555ccd5c2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 01:54:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53fd3f899ffc4564bbb3f39555ccd5c2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>原文：<a href="https://medium.com/swlh/should-you-use-usememo-in-react-a-benchmarked-analysis-159faf6609b7" target="_blank" rel="nofollow noopener noreferrer">medium.com/swlh/should…</a></p>
</blockquote>
<p>我们的一些开发人员最近提出了一个问题，什么时候我应该在 React 中使用 usemo？这是一个非常好的问题。在本文中，我们将使用一种科学的方法，定义一个假设，并在 React 中使用现实生活中的基准对其进行测试。</p>
<p>请继续阅读，了解 useMomo 对性能的影响。</p>
<h2 data-id="heading-0">什么是 useMomo？</h2>
<p>useMomo 是 React 提供的一个hook 函数。这个钩子允许开发人员缓存变量的值和依赖列表。如果此依赖项列表中的任何变量发生更改，React 将重新运行此数据的处理并重新缓存它。如果依赖项列表中的变量值之前已经缓存过，则 React 将从缓存中获取值。</p>
<p>这主要是对组件的重新呈现有影响。一旦组件重新呈现，它将从缓存中提取值，而不必一次又一次地循环数组或处理数据。</p>
<h2 data-id="heading-1">react 官方是怎么介绍useMenu的？</h2>
<p>我们咋一看一下 的 React 文档，关于 usemo，它在应该使用它的时候并没有被提及。他们只是简单地提到它的作用和使用方法。</p>
<blockquote>
<p>You may rely on useMemo as a performance optimization</p>
</blockquote>
<blockquote>
<p>您可以依赖 useMomo 作为性能优化工具</p>
</blockquote>
<p>这里的探讨关于 useMomo 的使用问题是是有趣的！</p>
<p>在我们看到使用 useMomo 的性能优势之前，数据应该有多复杂或大？开发者应该什么时候使用 usemo？</p>
<h2 data-id="heading-2">实验</h2>
<p>在我们开始实验之前，让我们先定义一个假设。</p>
<p>让我们首先定义要执行的对象和处理的复杂性为 n。如果 n = 100，那么我们需要循环遍历一个由100个条目组成的数组，以获得 memo-ed 变量的最终值。</p>
<p>然后，我们还需要将两个操作分开。第一个动作是组件的初始呈现。在这种情况下，如果一个变量使用 useMomo 或不使用 usemo，它们都必须计算初始值。一旦完成了第一次渲染，随后用 useMomo 重新渲染(我们需要测量的第二个操作) ，可以从缓存中检索值，其中的性能优势应该与非备注版本相比可见。</p>
<p>在所有情况下，为了建立备忘缓存并存储值，我预计在初始呈现期间会有大约5-10% 的开销。当 n < 1000时，我期望看到 useMomo 的性能下降。对于 n > 1000，我希望看到类似或更好的性能与 useMomo 重新渲染，但初始渲染应该仍然略慢，由于额外的缓存算法。你的猜测是什么？</p>
<h3 data-id="heading-3">基准测试设置</h3>
<p>我们设置了一个小的 React 组件如下，它将生成一个复杂度为 n 的对象，复杂度定义在props level 。</p>
<ul>
<li>BenchmarkNormal.jsx</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> BenchmarkNormal = <span class="hljs-function">(<span class="hljs-params">&#123;level&#125;</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> complexObject = &#123;
        <span class="hljs-attr">values</span>: []
    &#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= level; i++) &#123;
        complexObject.values.push(&#123; <span class="hljs-string">'mytest'</span> &#125;);
    &#125;
    <span class="hljs-keyword">return</span> ( <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Benchmark level: &#123;level&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> BenchmarkNormal;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是我们正常的基准组件，我们还将为 useMomo 做一个基准组件 BenchmarkMemo。</p>
<ul>
<li>BenchmarkMemo.jsx</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123;useMemo&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">const</span> BenchmarkMemo = <span class="hljs-function">(<span class="hljs-params">&#123;level&#125;</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> complexObject = useMemo(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> result = &#123;
            <span class="hljs-attr">values</span>: []
        &#125;;
        
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <= level; i++) &#123;
            result.values.push(&#123;<span class="hljs-string">'mytest'</span>&#125;);
        &#125;;
        <span class="hljs-keyword">return</span> result;
    &#125;, [level]);
    <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Benchmark with memo level: &#123;level&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> BenchmarkMemo;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们在 App.js 中设置这些组件，以便在按下按钮时显示。我们还使用 React 的  来提供渲染时间</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [showBenchmarkNormal, setShowBenchmarkNormal] = useState(<span class="hljs-literal">false</span>);
    <span class="hljs-comment">// Choose how many times this component needs to be rendered</span>
    <span class="hljs-comment">// We will then calculate the average render time for all of these renders</span>
    <span class="hljs-keyword">const</span> timesToRender = <span class="hljs-number">10000</span>;
    <span class="hljs-comment">// Callback for our profiler</span>
    <span class="hljs-keyword">const</span> renderProfiler = <span class="hljs-function">(<span class="hljs-params">type</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
            <span class="hljs-comment">// Keep our render time in an array</span>
            <span class="hljs-comment">// Later on, calculate the average time</span>
            <span class="hljs-comment">// store args[3] which is the render time ...</span>
        &#125;;
    &#125;;
    <span class="hljs-comment">// Render our component </span>
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span> &#123;showBenchmarkNormal && [...Array(timesToRender)].map((index) => &#123;
        return <span class="hljs-tag"><<span class="hljs-name">Profiler</span> <span class="hljs-attr">id</span>=<span class="hljs-string">&#123;</span>`<span class="hljs-attr">normal-</span>$&#123;<span class="hljs-attr">index</span>&#125;`&#125; <span class="hljs-attr">onRender</span>=<span class="hljs-string">&#123;renderProfiler(</span>'<span class="hljs-attr">normal</span>')&#125;></span>
            <span class="hljs-tag"><<span class="hljs-name">BenchmarkNormal</span> <span class="hljs-attr">level</span>=<span class="hljs-string">&#123;1&#125;</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">Profiler</span>></span>;
    &#125;)&#125;
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如您所见，我们渲染组件10000次，并获取这些组件的平均渲染时间。现在我们需要一种机制来触发组件的按需重新呈现，同时不必重新计算 usemo，因此我们不希望修改 useMemo 的依赖列表中的任何值。</p>
<h3 data-id="heading-4">重新渲染触发机制</h3>
<p>为了保持结果的清晰，我们总是在开始测试之前从一个新的浏览器页面开始(除了重新渲染) ，以清除任何可能仍然在页面上并影响我们的结果的缓存。</p>
<h2 data-id="heading-5">结果</h2>
<h3 data-id="heading-6">复杂度 n = 1的结果</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53fd3f899ffc4564bbb3f39555ccd5c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46bb80811b804b45985ce9de50a27802~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>复杂度在左列显示，第一个测试是初始渲染，第二个测试是第一次重新渲染，最后一个测试是第二次重新渲染。第二列显示了普通基准测试的结果，不包括 useMomo。最后一列显示了使用 useMomo 的基准测试的结果。这些值是我们的基准组件渲染时间超过10000次的平均值。</p>
<p>当使用 useMomo 时，初始渲染会慢19% ，这比预期的5-10% 要高得多。随后的渲染仍然很慢，因为通过 useMomo 缓存的开销比重新计算实际值的开销更大。</p>
<p>总之，对于复杂度 n = 1，不使用 useMomo 总是更快，因为开销总是比性能增益更昂贵。</p>
<h3 data-id="heading-7">复杂度 n = 100的结果</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/682c807200bf4dee8805e7f087bad7d5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在复杂度为100的情况下，使用 useMomo 的初始渲染变慢了62% ，这是一个相当大的数量。后续的重新投票似乎平均要稍微快一点或者差不多。</p>
<p>总之，复杂度为100的初始渲染显著地慢，而随后的重新渲染相当类似，最多只是稍微快一点。在这一点上，useMomo 似乎还没有什么意思。</p>
<h3 data-id="heading-8">复杂度 n = 1000的结果</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00fd811185414b86b1ebf18e8e8c01bc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于复杂度为1000，我们注意到使用 useMomo 的初始渲染变慢了183% ，因此可以推测，useMomo 缓存更难存储这些值。后续渲染大约快37% ！</p>
<p>在这一点上，我们可以看到一些性能提高在重新呈现，但它不是没有成本来。最初的渲染速度要慢得多，损失了183% 的时间。</p>
<p>总之，在复杂度为1000的情况下，我们可以看到在初始渲染时性能损失更大(183%) ，然而，随后的渲染速度要快37% 。</p>
<p>这是否已经很有用将在很大程度上取决于您的用例。一个183% 的性能损失在初始渲染是一个艰难的销售，但可能是合理的情况下，很多重新呈现的组件。</p>
<h3 data-id="heading-9">复杂度 n = 5000的结果</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44885dea1ba34e3491e98ccd61f99dc4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在复杂度为5000的情况下，我们注意到 useMomo 的初始渲染速度要慢545% 。看起来数据和处理的复杂度越高，初始渲染的速度就越慢。</p>
<p>有趣的部分来自于再次的渲染。在这里，我们注意到在每个后续渲染中 useMomo 的性能提高了437% 到609% 。</p>
<p>总之，使用 useMomo 的初始渲染更加昂贵，但是随后的重新渲染会有更大的性能提升。如果您的应用程序的数据/处理复杂度大于5000并且有一些重新渲染，我们可以看到使用 useMomo 的好处。</p>
<h3 data-id="heading-10">结果说明</h3>
<p>友好的读者社区已经指出了一些可能的原因，比如为什么初始渲染会慢很多，比如运行生产模式等等。我们重新测试了所有的实验，发现结果是相似的。这些比率相似，但实际值可能更低。所有的结论都是一样的。</p>
<h2 data-id="heading-11">总结</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a7da26becc4493caa84b24313cd2573~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这些是组件的复杂度为 n 的结果，其中应用程序将循环并向数组中添加值 n 次。请注意，结果将根据您处理数据的具体方式以及数据量而有所不同。但是，这应该能够让您了解不同大小的数据集的性能差异。</p>
<p>是否应该使用 useMemo 将在很大程度上取决于您的用例，但是由于复杂度小于100，useMemo 似乎没什么意思。</p>
<p>值得注意的是，useMemo 最初的渲染在性能方面遭受了相当大的挫折。我们预计初始性能损失大约为5-10% ，但发现这在很大程度上取决于数据/处理的复杂性，甚至可能导致500% 的性能损失，这比预期的性能损失多100倍。</p>
<p>我们已经重新运行了几次测试，甚至在得到结果之后，我们可以说后续的结果是非常一致的，类似于我们已经记录下来的最初结果。</p>
<h2 data-id="heading-12">关键点</h2>
<p>我们都同意，通过保持变量的相同对象引用，useMemo 可以有效地避免不必要的重复渲染。</p>
<p>对于使用 useMemo 缓存实际计算的情况，其主要目标不是避免在子组件中重新渲染:</p>
<ul>
<li>当处理量很大时，应该使用 useMemo</li>
<li>从什么时候 useMemo 变得有用以避免额外处理，阈值在很大程度上取决于您的应用程序</li>
<li>数据在处理非常低的情况下使用 useMemo，可能会有额外的使用开销</li>
</ul>
<p>你什么时候使用 useMemo？
这些发现会改变你何时使用 useMemo 的想法吗？请在评论中告诉我们！</p></div>  
</div>
            