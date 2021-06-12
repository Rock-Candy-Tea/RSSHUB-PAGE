
---
title: '_译_ Inside Fiber： 深入了解React的新协调算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb8bd8632f804939b0563ad8d1e876de~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:28:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb8bd8632f804939b0563ad8d1e876de~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文链接：<a href="https://indepth.dev/posts/1008/inside-fiber-in-depth-overview-of-the-new-reconciliation-algorithm-in-react" target="_blank" rel="nofollow noopener noreferrer">indepth.dev/posts/1008/…</a></li>
<li>原文标题：Inside Fiber: in-depth overview of the new reconciliation algorithm in React</li>
<li>原文作者：<a href="https://twitter.com/maxkoretskyi" target="_blank" rel="nofollow noopener noreferrer">Max Koretskyi</a></li>
</ul>
</blockquote>
<p><code>React</code>是一个用于构建用户界面的<code>JavaScript</code>库。它的核心机制是跟踪组件的<code>state</code>变化并将更新后的<code>state</code>显示到屏幕上。在React中这个过程叫做<strong>协调</strong>(<strong>reconciliation</strong>)。我们调用<code>setState</code>方法，React会检查<code>state</code>或<code>props</code>是否变化，然后重新渲染组件到UI上。</p>
<p>React文档为这个机制提供了<a href="https://reactjs.org/docs/reconciliation.html" target="_blank" rel="nofollow noopener noreferrer">很好的高级概述</a>：React元素的角色，生命周期方法和<code>render</code>方法，以及应用到组件<code>children</code>的<code>diffing</code>算法。由<code>render</code>方法返回的元素组成的树通常被认为是”虚拟DOM“。这个术语早期有助于理解<code>React</code>，但是它也引起了困惑并且在<code>React</code>文档里已经不再使用它了。在这篇文章里我称其为<code>React</code>元素树。</p>
<p>除了<code>React</code>元素树，还有一颗内部实例树（组件，DOM节点等等）用于保存状态。从版本16开始，React推出了内部树和管理内部树的算法的实现，称为Fiber。通过<a href="https://indepth.dev/the-how-and-why-on-reacts-usage-of-linked-list-in-fiber-to-walk-the-components-tree/" target="_blank" rel="nofollow noopener noreferrer">React如何以及为什么在Fiber中使用链表 </a>。</p>
<p>这是让你了解<code>React</code>内部架构系列的第一篇文章。在这篇文章中，我想提供关于这个算法的重要概念和数据结构的概述。一旦我们拥有足够的背景知识，我们就会探索该算法用于遍历和处理<code>fiber</code>树的主要函数。在这个系列接下来的文章中会展示React是如何使用这个算法进行首次渲染，处理<code>state</code>和<code>props</code>的更新。在那之前，我们先了解调度器、协调过程和构建<code>effects</code>列表的机制的细节。</p>
<p>我会教你一些相当高级的知识？我鼓励你阅读它来理解<code>Concurrent React</code>内部运作背后的魔法。如果你想为<code>React</code>贡献，这个系列的文章可以作为你很好的指南。我<a href="https://indepth.dev/level-up-your-reverse-engineering-skills/" target="_blank" rel="nofollow noopener noreferrer">坚信逆向工程</a>，所以会有很多版本16.6.0的源码链接。</p>
<p>这确实要花费大量时间和精力，所以不要气馁即使你不能马上理解。花费时间是值得的。<strong>注意，你无需知道这些也能使用<code>React</code>，这篇文章是关于<code>React</code>内部是如何运作的。</strong></p>
<h1 data-id="heading-0">背景设定</h1>
<p>这是一个我准备贯穿整个系列的简单程序。在屏幕上我们有个简单增加数字的按钮：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb8bd8632f804939b0563ad8d1e876de~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props);
        <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;;
        <span class="hljs-built_in">this</span>.handleClick = <span class="hljs-built_in">this</span>.handleClick.bind(<span class="hljs-built_in">this</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125;;
        &#125;);
    &#125;


    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> [
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>Update counter<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>,
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"2"</span>></span>&#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以在<a href="https://stackblitz.com/edit/react-t4rdmh" target="_blank" rel="nofollow noopener noreferrer">这</a>查看。如你所见，它是一个<code>render</code>方法中返回两个子元素<code>button</code>和<code>span</code>的简单组件。一旦你点击按钮，组件的<code>state</code>在处理函数中被更新。这样就会导致<code>span</code>元素的文本更新。</p>
<p>在<code>React</code>的<strong>协调</strong>过程中有很多活动，比如调用<a href="https://reactjs.org/docs/react-component.html#updating" target="_blank" rel="nofollow noopener noreferrer"> 生命周期方法 </a>、更新<a href="https://reactjs.org/docs/refs-and-the-dom.html" target="_blank" rel="nofollow noopener noreferrer">refs</a>。<strong>在<code>Fiber</code>架构中这些活动都称为”work“</strong>。work的类型通常依赖于<code>React</code>元素的类型。举个例子，对于类组件，<code>React</code>需要创建一个实例，而函数组件则不必这样。正如你所知道的，<code>React</code>中有很多种类的元素，如类组件和函数组件，原生组件（DOM节点），portals等等。<code>React</code>元素的类型是由<a href="https://github.com/facebook/react/blob/b87aabdfe1b7461e7331abb3601d9e6bb27544bc/packages/react/src/ReactElement.js#L171" target="_blank" rel="nofollow noopener noreferrer">createElement</a>函数的第一个参数确定的。这个函数通常用于<code>render</code>方法中用来创建一个元素。</p>
<p>在研究这些活动和<code>fiber</code>主要算法前，我们先来熟悉<code>React</code>内部使用的数据结构。</p>
<h1 data-id="heading-1">从<code>React</code>元素到<code>Fiber</code>节点</h1>
<p><code>React</code>的每个组件都有UI表示，我们可以称从<code>render</code>方法返回的为视图或模板。这是我们<code>ClickCounter</code>组件的模板：</p>
<pre><code class="hljs language-js copyable" lang="js"><button key=<span class="hljs-string">"1"</span> onClick=&#123;<span class="hljs-built_in">this</span>.onClick&#125;>Update counter</button>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"2"</span>></span>&#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">React元素</h2>
<p>一个模板经过JSX编译器编译后，就会得到一堆<code>React</code>元素。这才是真正从<code>render</code>中返回的东西，而不是<code>HTML</code>。如果不适用JSX，我们<code>ClickCounter</code>组件的<code>render</code>方法应该写成这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickCounter</span> </span>&#123;
    ...
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> [
            React.createElement(
                <span class="hljs-string">'button'</span>,
                &#123;
                    <span class="hljs-attr">key</span>: <span class="hljs-string">'1'</span>,
                    <span class="hljs-attr">onClick</span>: <span class="hljs-built_in">this</span>.onClick
                &#125;,
                <span class="hljs-string">'Update counter'</span>
            ),
            React.createElement(
                <span class="hljs-string">'span'</span>,
                &#123;
                    <span class="hljs-attr">key</span>: <span class="hljs-string">'2'</span>
                &#125;,
                <span class="hljs-built_in">this</span>.state.count
            )
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>render</code>方法中调用<code>React.createElement</code>会创建像这样的数据结构：</p>
<pre><code class="hljs language-js copyable" lang="js">[
    &#123;
        <span class="hljs-attr">$$typeof</span>: <span class="hljs-built_in">Symbol</span>(react.element),
        <span class="hljs-attr">type</span>: <span class="hljs-string">'button'</span>,
        <span class="hljs-attr">key</span>: <span class="hljs-string">"1"</span>,
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">children</span>: <span class="hljs-string">'Update counter'</span>,
            <span class="hljs-attr">onClick</span>: <span class="hljs-function">() =></span> &#123; ... &#125;
        &#125;
    &#125;,
    &#123;
        <span class="hljs-attr">$$typeof</span>: <span class="hljs-built_in">Symbol</span>(react.element),
        <span class="hljs-attr">type</span>: <span class="hljs-string">'span'</span>,
        <span class="hljs-attr">key</span>: <span class="hljs-string">"2"</span>,
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">children</span>: <span class="hljs-number">0</span>
        &#125;
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>React</code>为这些对象添加了<a href="https://overreacted.io/why-do-react-elements-have-typeof-property/" target="_blank" rel="nofollow noopener noreferrer">$$typeof</a>属性来表示它们是<code>React</code>元素。还有些属性<code>type</code>、<code>key</code>和<code>props</code>来描述元素。这些值是通过<code>React.createElement</code>函数传递进来的。注意<code>React</code>如何让文本内容作为<code>span</code>和<code>button</code>的<code>children</code>。以及点击事件如何作为<code>button</code>元素的<code>props</code>的一部分。<code>React</code>元素上还有其他一些超出本文讨论范围的字段比如<code>ref</code>。</p>
<p><code>ClickCounter</code>的<code>React</code>元素没有任何<code>props</code>或<code>ref</code></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">$$typeof</span>: <span class="hljs-built_in">Symbol</span>(react.element),
    <span class="hljs-attr">key</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">props</span>: &#123;&#125;,
    <span class="hljs-attr">ref</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">type</span>: ClickCounter
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Fiber节点</h2>
<p>在<strong>协调</strong>过程中，每个从<code>render</code>返回的<code>React</code>元素会被合并一颗<code>fiber</code>树。每个<code>React</code>元素都有相应的<code>fiber</code>节点。与<code>React</code>元素不同的是，<code>fiber</code>节点不会再每次渲染是从新创建。它们是可变的数据结构，保存了组件<code>state</code>和DOM。</p>
<p>我们之前讨论过<code>React</code>根据元素类型执行不同活动。在我们的实例程序中，对于类组件<code>ClickCounter</code>会调用生命周期方法和<code>render</code>方法，而对于<code>span</code>这样的原生组件（DOM节点）会执行DOM变化。所以每个React元素会被转换成<a href="https://github.com/facebook/react/blob/769b1f270e1251d9dbdce0fcbd9e92e502d059b8/packages/shared/ReactWorkTags.js" target="_blank" rel="nofollow noopener noreferrer">相应类型</a>的Fiber节点，这个节点描述了需要完成的work。</p>
<p><strong>你可以将<code>Fiber</code>理解为一种表示待做的一些work的数据结构，或者换句话说，一个work单元。Fiber架构也提供了一种方便的方式来追踪、调度、暂停和中止这些work。</strong></p>
<p>当一个<code>React</code>元素第一次转换成<code>fiber</code>节点时，<code>React</code>在<a href="https://github.com/facebook/react/blob/769b1f270e1251d9dbdce0fcbd9e92e502d059b8/packages/react-reconciler/src/ReactFiber.js#L414" target="_blank" rel="nofollow noopener noreferrer">createFiberFromTypeAndProps</a>函数中使用元素中的数据来创建一个<code>fiber</code>。在更新中<code>React</code>会复用fiber节点，根据相应的<code>React</code>元素仅更新必要的属性。React也可能根据<code>key</code>prop来移动节点，或者如果相应的的<code>React</code>不再从<code>render</code>方法中返回，那么就删除它。</p>
<blockquote>
<p>查看<a href="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactChildFiber.js#L239" target="_blank" rel="nofollow noopener noreferrer">ChildReconciler</a>函数来了解活动列表以及<code>React</code>对于已经存在的<code>fiber</code>节点执行的函数。</p>
</blockquote>
<p>因为<code>React</code>为每个<code>React</code>元素创建了fiber节点并且我们有一颗由这些元素组成的树，所以我们将有一个由<code>fiber</code>节点组成的树。在我们例子中看起来像这样：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26a024409d894c8580f6db69101d3eb4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有<code>fiber</code>节点都是通过<code>fiber</code>节点上的这几个属性形成链表：<code>child</code>，<code>subling</code>和<code>return</code>。要了解为什么这样做的更多细节，请阅读我的文章<a href="https://medium.com/dailyjs/the-how-and-why-on-reacts-usage-of-linked-list-in-fiber-67f1014d0eb7" target="_blank" rel="nofollow noopener noreferrer">React如何以及为什么在Fiber中使用链表</a>，如果你还没读过。</p>
<h2 data-id="heading-4">Current和work in process树</h2>
<p>首次渲染后，<code>React</code>中存在一颗保存了应用程序状态，用于渲染UI的<code>fiber</code>树。这颗树通常称为<strong>current</strong>。当React开始进行更新时，它创建一颗所谓的<code>workInProgress</code>树，这棵树保存着将来要刷新到屏幕上的状态。</p>
<p>所有的work都是在<code>workInProgress</code>树的fibers上执行的。当<code>React</code>遍历<code>current</code>树，对于每个现存的fiber节点，React会创建一个代替（alternate）节点，这些代替节点组成<code>workInProgress</code>树。代替节点是由<code>render</code>方法返回的<code>React</code>元素的数据创建的。一旦更新都被处理了、所有相关联的work完成了，<code>React</code>就会有一颗准备刷新到屏幕上的代替树。一旦<code>workInProgress</code>树渲染到屏幕上，它就变成<code>current</code>树。</p>
<p>React的核心原则之一就是连贯性。React总是一次性更新DOM，它不会显示部分结果。<code>workInProgress</code>树就像一份草稿，用户是看不见它的，所以React可以先处理所有组件，然后在将它们的变化更新到屏幕上。</p>
<p>在源码中你会看到很多使用<code>current</code>和<code>workInProgress</code>树节点的函数，这是其中一个函数的签名：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateHostComponent</span>(<span class="hljs-params">current, workInProgress, renderExpirationTime</span>) </span>&#123;...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个fiber节点在<strong>alternate</strong>字段上保存了另一颗树上相应节点的引用。<code>current</code>树上节点指向<code>workInProgress</code>树上相应的节点，反之亦然。</p>
<h2 data-id="heading-5">Side-effects（副作用）</h2>
<p>我们可以把React中的组件看成一个使用<code>state</code>和<code>props</code>来得到UI页面的函数。其他的每个活动比如DOM变化或调用生命周期方法都应该被认为是副作用或作用。Effects<a href="https://reactjs.org/docs/hooks-overview.html#%EF%B8%8F-effect-hook" target="_blank" rel="nofollow noopener noreferrer">在文档中</a>也有提及。</p>
<blockquote>
<p>你之前在React组件中可能执行过数据获取，订阅，或手动<strong>更改DOM</strong>。我们把这些操作称为副作用（或简称作用），因为它们可能影响其他组件，而且在渲染过程中无法完成。</p>
</blockquote>
<p>你可以看到大部分<code>state</code>和<code>props</code>更新如何产生副作用。由于标记effects是一种work，除了更新外，fiber节点是一种方便跟踪effects的机制。每个fiber节点都可以关联它的effects。它们保存在<code>effectTag</code>字段上。</p>
<p>因此，Fiber中的effects基本定义了更新被处理后实例需要完成的<a href="https://github.com/facebook/react/blob/b87aabdfe1b7461e7331abb3601d9e6bb27544bc/packages/shared/ReactSideEffectTags.js" target="_blank" rel="nofollow noopener noreferrer">work</a>。对于原生组件（DOM元素），work包含添加、更新或移除元素。对于类组件，React可能需要更新<code>refs</code>，调用<code>componentDidMount</code>和<code>componentDidUpdate</code>生命周期方法。其他类型的fibers有相应的其他effects。</p>
<h2 data-id="heading-6">Effects list</h2>
<p>React处理更新非常快，为了实现高性能它使用了一些有趣的技术。<strong>它们中的一个就是创建一个由包含effects的fiber节点组成的线性链表来实现快速迭代。</strong> 迭代线链列表比迭代一颗树快的多，而且无需在没有副作用的节点上浪费时间。</p>
<p>这个链表的目标是标记含有DOM更新或其他effects的节点并把它们关联起来。这个链表是<code>finishedWork</code>树的子集，节点之间使用<code>nextEffect</code>属性进行连接，而不是 <code>current</code>和<code>workInProgress</code>树中使用的 <code>child</code>属性。</p>
<p><a href="https://medium.com/u/a3a8af6addc1?source=post_page---------------------------" target="_blank" rel="nofollow noopener noreferrer">Dan Abramov</a>为effects list描述了一种比喻。他喜欢将它想象成挂在圣诞树上的”圣诞灯“，”圣诞灯“将所有有副作用的节点绑到一起。形象点说，把下面fiber树种高亮的节点想象成有些work要做的节点。比如，我们的更新导致<code>c2</code>插入DOM中，<code>d2</code>和<code>c1</code>改变了属性，<code>b2</code>触发了一个生命周期方法。effects list会把它们连接起来，如此，React在后面就可以跳过其他节点：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/416598ccecd54e41af27a5206999fe46~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以看到有副作用的节点是如何连接到一起的。遍历节点时，React使用<code>firstEffect</code>指针找出list从哪开始。所以上面的图可以看成这样的线性链表：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d793a5c04c2048b293baf7ee2ca820ee~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">Root of the fiber tree</h2>
<p>每个React程序都有一个或多个DOM元素作为容器。在我们的例子中它是ID为<code>container</code>的<code>div</code>元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> domContainer = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#container'</span>);
ReactDOM.render(React.createElement(ClickCounter), domContainer);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React为这些容器创建了一个<a href="https://github.com/facebook/react/blob/0dc0ddc1ef5f90fe48b58f1a1ba753757961fc74/packages/react-reconciler/src/ReactFiberRoot.js#L31" target="_blank" rel="nofollow noopener noreferrer">fiber root</a>对象。你可以使用DOM元素的引用来获取它。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fiberRoot = query(<span class="hljs-string">'#container'</span>)._reactRootContainer._internalRoot
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个fiber root就是React保存一颗fiber树引用的地方。它保存在fiber root的<code>current</code>属性中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> hostRootFiberNode = fiberRoot.current
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fiber树开始于<a href="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/shared/ReactWorkTags.js#L34" target="_blank" rel="nofollow noopener noreferrer">一个特殊类型</a>的fiber节点，它就是<code>HostRoot</code>。它在内部创建，作为你最顶层组件的父级。<code>HostRoot</code>fiber节点上有个指回<code>FiberRoot</code>的<code>stateNode</code>属性：</p>
<pre><code class="hljs language-js copyable" lang="js">fiberRoot.current.stateNode === fiberRoot; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以通过访问最顶层<code>HostRoot</code>fiber节点到达fiber root，接着探索fiber树。
或者你可以从组件实例中获取一个fibe节点，就像这样：</p>
<pre><code class="hljs language-js copyable" lang="js">compInstance._reactInternalFiber
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Fiber节点结构</h2>
<p>现在让我们来看看为<code>ClickCounter</code>组件创建的fiber节点的结构：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> ClickCounter,
    <span class="hljs-attr">type</span>: ClickCounter,
    <span class="hljs-attr">alternate</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">updateQueue</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">memoizedState</span>: &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;,
    <span class="hljs-attr">pendingProps</span>: &#123;&#125;,
    <span class="hljs-attr">memoizedProps</span>: &#123;&#125;,
    <span class="hljs-attr">tag</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">effectTag</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">nextEffect</span>: <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>span</code>DOM元素的fiber节点：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">stateNode</span>: <span class="hljs-keyword">new</span> HTMLSpanElement,
    <span class="hljs-attr">type</span>: <span class="hljs-string">"span"</span>,
    <span class="hljs-attr">alternate</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">"2"</span>,
    <span class="hljs-attr">updateQueue</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">memoizedState</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">pendingProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">0</span>&#125;,
    <span class="hljs-attr">memoizedProps</span>: &#123;<span class="hljs-attr">children</span>: <span class="hljs-number">0</span>&#125;,
    <span class="hljs-attr">tag</span>: <span class="hljs-number">5</span>,
    <span class="hljs-attr">effectTag</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">nextEffect</span>: <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fiber节点上有很多字段。在之前的部分中我已经描述过字段<code>alternate</code>，<code>effectTag</code>，<code>nextEffect</code>的作用。现在来看看为什么需要其他字段。</p>
<h2 data-id="heading-9">stateNode</h2>
<p>保存类组件实例，DOM节点，或其他与fiber节点关联的React元素类型。总的来说，我们可以说这个属性用于保存与fiber节点关联的本地状态。</p>
<h2 data-id="heading-10">type</h2>
<p>定义与这个fiber关联的函数或类。对于类组件，它指向构造函数，对于DOM元素，它代表HTML标签。我经常使用这个字段来理解与一个fiber节点关联的元素是什么。</p>
<h2 data-id="heading-11">tag</h2>
<p>定义<a href="https://github.com/facebook/react/blob/769b1f270e1251d9dbdce0fcbd9e92e502d059b8/packages/shared/ReactWorkTags.js" target="_blank" rel="nofollow noopener noreferrer">the type of the fiber</a>。它在协调算法中用于确定什么work要做。如前所述，React元素类型不同，work有所不同。<a href="https://github.com/facebook/react/blob/769b1f270e1251d9dbdce0fcbd9e92e502d059b8/packages/react-reconciler/src/ReactFiber.js#L414" target="_blank" rel="nofollow noopener noreferrer">createFiberFromTypeAndProps</a>函数将React元素映射成相应的fiber节点类型。在我们的程序中，<code>ClickCounter</code>组件的<code>tag</code>属性是1，表示它是一个<code>ClassComponent</code>，<code>span</code>元素的是5表示它是一个<code>HostComponent</code>。</p>
<h2 data-id="heading-12">updateQueue</h2>
<p>一条state更新，回调和DOM更新的队列。</p>
<h2 data-id="heading-13">memoizedState</h2>
<p>fiber中用于创建输出的state。当处理更新时，它表示当前渲染到屏幕上的state。</p>
<h2 data-id="heading-14">memoizedProps</h2>
<p>在之前渲染中fiber用于创建输出的props。</p>
<h2 data-id="heading-15">pendingProps</h2>
<p>React元素中从新数据中更新的props，需要传递给子组件或DOM元素。</p>
<h2 data-id="heading-16">key</h2>
<p>一组子元素中的唯一标识符，帮助React从列表中找出哪些项目已变化、添加或者删除。它与React文档<a href="https://reactjs.org/docs/lists-and-keys.html#keys" target="_blank" rel="nofollow noopener noreferrer">此处</a>描述的”列表和keys“功能有关。</p>
<p>你可以在<a href="https://github.com/facebook/react/blob/6e4f7c788603dac7fccd227a4852c110b072fe16/packages/react-reconciler/src/ReactFiber.js#L78" target="_blank" rel="nofollow noopener noreferrer">这</a>看到fiber节点完整的结构。我在上面的说明中删除了一堆字段。特别是我跳过了<a href="https://indepth.dev/the-how-and-why-on-reacts-usage-of-linked-list-in-fiber-to-walk-the-components-tree/" target="_blank" rel="nofollow noopener noreferrer">我在上篇文章中描述过了</a>的组成树结构的<code>child</code>，<code>sibling</code>和<code>return</code> 指针。还有一类字段像<code>expirationTime</code>，<code>childExpirationTime</code>和<code>mode</code>，它们是给调度器用的。</p>
<h1 data-id="heading-17">通用算法</h1>
<p>React在两个主要阶段中执行work：<strong>render</strong>和<strong>commit</strong>。</p>
<p>在<code>render</code>阶段中，React将更新应用到通过<code>setState</code>或<code>React.render</code>调度的组件，并且找出什么需要被更新到UI。如果是首次渲染，React为每个从<code>render</code>方法中返回的元素创建新的fiber节点。在接下来的更新中，现存的React元素的fiber会被复用和更新。<strong>这个阶段的结果是由标记了副作用的fiber节点组成的树。</strong> effects描述了在接下来的<code>commit</code>阶段需要完成的<code>work</code>。在这个阶段中，React拥有一颗标记了effects的fiber树，并将它们应用到实例上。它遍历effects链表执行DOM更新和其他用户可见的变化。</p>
<p><strong><code>render</code>阶段中的work是可以异步执行的，理解这一点很重要。</strong> React在可用时间内处理一个或多个fiber节点，然后停止运行并暂存完成的work，让步于其他事件。然后从它停止的地方继续。但有时，它可能需要放弃已完成的work，再次从顶部开始。正是因为这个阶段执行的work不会导致任何用户可见的变化，比如DOM更新，使得这些暂停成为可能。<strong>相反，后面的<code>commit</code>阶段总是同步的。</strong> 这是因为这个阶段执行的work会用户可见的变化，例如DOM更新。这就是为什么React需要一次性完成它们。</p>
<p>调用生命周期方式是React执行的一类work。一些方法在<code>render</code>阶段调用，其他的在<code>commit</code>阶段调用。下列生命周期函数在<code>render</code>阶段中调用：</p>
<ul>
<li>[UNSAFE_]componentWillMount (已废弃)</li>
<li>[UNSAFE_]componentWillReceiveProps (已废弃)</li>
<li>getDerivedStateFromProps</li>
<li>shouldComponentUpdate</li>
<li>[UNSAFE_]componentWillUpdate (已废弃)</li>
<li>render</li>
</ul>
<p>如你所见，一些在<code>render</code>阶段中执行的遗留的生命周期函数从版本16.3开始被标记为<code>UNSAFE</code>。现在再文档中它们被称为遗留的生命周期函数。它们将在16.x发行版中废弃，对应的没有<code>UNSAFE</code>前缀的将在17.0中移除。你可以在<a href="https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html" target="_blank" rel="nofollow noopener noreferrer">这</a>读到更多关于这些变化和建议的迁移路线。</p>
<p>你对这样做的原因感到好奇吗？</p>
<p>好的，我们刚刚学习了render阶段不会产生像DOM更新这样的副作用，React可以异步处理组件更新（甚至可以在多个线程中运行）。然而，这些被标记为<code>UNSAFE</code>被误解和误用。开发人员往往在这些生命周期方法中放入带有副作用的代码，这在新的异步渲染方式中可能引起问题。尽管只有没有<code>UNSAFE</code>前缀的会被移除，它们在即将到来的Concurrent模式（你可以选择退出）中仍然可能引起问题。</p>
<p>下列生命周期函数在<code>commit</code>阶段中执行：</p>
<ul>
<li>getSnapshotBeforeUpdate</li>
<li>componentDidMount</li>
<li>componentDidUpdate</li>
<li>componentWillUnmount</li>
</ul>
<p>因为执行在同步的<code>commit</code>阶段，所以它们可以包含副作用和访问DOM。</p>
<p>好的，现在我们了解了用于遍历树和执行work的算法的背景知识。让我们更深入些。</p>
<h2 data-id="heading-18">Render阶段</h2>
<p>协调算法总是从<a href="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L1132" target="_blank" rel="nofollow noopener noreferrer">renderRoot</a>函数使用的最顶层<code>HostRoot</code>fiber节点开始。然而，React会跳过已经处理了的fiber节点直到它遇到有未完成work的节点。例如，如果你在组件树深层调用<code>setState</code>，React将从顶层开始，但是会快速跳过父级直到它到达调用<code>setState</code>方法的组件。</p>
<h3 data-id="heading-19">work循环的主要步骤</h3>
<p>所有fiber节点在work循环中处理。这是循环的同步部分实现的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span>(<span class="hljs-params">isYieldy</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!isYieldy) &#123;
    <span class="hljs-keyword">while</span> (nextUnitOfWork !== <span class="hljs-literal">null</span>) &#123;
      nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;...&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，<code>nextUnitOfWork</code>保存了来自<code>workInProgress</code>树中有work待完成的fiber节点的引用。当React遍历Fiber树时，它使用这个变量来知道是否存在其他有未完成work的fiber节点。当前节点处理完后，这个变量将包含树中下一个fiber节点的引用或者为<code>null</code>。在这种情况下（译注：<code>nextUnitOfWork=null</code>的情况）React退出work循环并准备提交变化。</p>
<p>有四个主要函数用于遍历树，开始或结束work：</p>
<ul>
<li><a href="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L1056" target="_blank" rel="nofollow noopener noreferrer">performUnitOfWork</a></li>
<li><a href="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/react-reconciler/src/ReactFiberBeginWork.js#L1489" target="_blank" rel="nofollow noopener noreferrer">beginWork</a></li>
<li><a href="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L879" target="_blank" rel="nofollow noopener noreferrer">completeUnitOfWork</a></li>
<li><a href="https://github.com/facebook/react/blob/cbbc2b6c4d0d8519145560bd8183ecde55168b12/packages/react-reconciler/src/ReactFiberCompleteWork.js#L532" target="_blank" rel="nofollow noopener noreferrer">completeWork</a></li>
</ul>
<p>为了演示它们是如何使用的，看看下面遍历fiber树的动画。我在demo中使用这些函数的简化实现。每个函数都接收一个fiber节点来处理，随着React向下遍历树你会看到当前活动的fiber节点发生了变化。你可以在视频中清楚地看出算法是如何从一个分支到其他分支的。它在移动到父节点之前先完成子节点的work。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb197794ba7a4a32b339af08195f83cd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意，垂直向下连着的表示兄弟节点，弯着连接的表示子节点，例如<code>b1</code>没有子节点，而<code>b2</code>有一个<code>c1</code>子节点</p>
</blockquote>
<p><a href="https://vimeo.com/302222454" target="_blank" rel="nofollow noopener noreferrer">这是视频的链接</a>，你可以暂停播放，查看当前节点和函数的状态。从概念上讲，你可以把”开始“看作”进入“一个组件，把”完成“看作“退出它”。当我说明这些函数是做说明的时候，你可以<a href="https://stackblitz.com/edit/js-ntqfil?file=index.js" target="_blank" rel="nofollow noopener noreferrer">在这查看示例和实现</a>。</p>
<p>让我们从前面的两个函数<code>performUnitOfWork</code>和<code>beginWork</code>开始：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">performUnitOfWork</span>(<span class="hljs-params">workInProgress</span>) </span>&#123;
    <span class="hljs-keyword">let</span> next = beginWork(workInProgress);
    <span class="hljs-keyword">if</span> (next === <span class="hljs-literal">null</span>) &#123;
        next = completeUnitOfWork(workInProgress);
    &#125;
    <span class="hljs-keyword">return</span> next;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">beginWork</span>(<span class="hljs-params">workInProgress</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'work performed for '</span> + workInProgress.name);
    <span class="hljs-keyword">return</span> workInProgress.child;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>performUnitOfWork</code>函数接收一个<code>workInProgress</code>树中的fiber节点，通过调用<code>beginWork</code>函数开始工作。这个函数将开启一个fiber节点所有执行的活动。为了演示，我们简单的打印出fiber的name表示work已经完成。<strong><code>beginWork</code>函数总是返回一个指向循环中下一个待处理child的指针或者<code>null</code></strong>。</p>
<p>如果存在下一个child，它将在<code>workLoop</code>函数中赋值给<code>nextUnitOfWork</code>变量。 但是，如果不存在child，React知道它已经到达分支的末尾，所以它可以完成当前节点。<strong>一旦节点完成，它需要执行兄弟节点的work然后返回父节点</strong>。这是在<code>completeUnitOfWork</code>函数内完成的:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">completeUnitOfWork</span>(<span class="hljs-params">workInProgress</span>) </span>&#123;
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
        <span class="hljs-keyword">let</span> returnFiber = workInProgress.return;
        <span class="hljs-keyword">let</span> siblingFiber = workInProgress.sibling;

        nextUnitOfWork = completeWork(workInProgress);

        <span class="hljs-keyword">if</span> (siblingFiber !== <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-comment">// If there is a sibling, return it</span>
            <span class="hljs-comment">// to perform work for this sibling</span>
            <span class="hljs-keyword">return</span> siblingFiber;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (returnFiber !== <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-comment">// If there's no more work in this returnFiber,</span>
            <span class="hljs-comment">// continue the loop to complete the parent.</span>
            workInProgress = returnFiber;
            <span class="hljs-keyword">continue</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// We've reached the root.</span>
            <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">completeWork</span>(<span class="hljs-params">workInProgress</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'work completed for '</span> + workInProgress.name);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以看出这个函数主体就是一个大的<code>while</code>循环。当一个<code>workInProgress</code>节点没有子节点时React会进入这个函数。在当前fiber完成work后，会检查是否有兄弟节点。如果有，React退出这个函数并返回指向兄弟节点的指针。它将赋值给<code>nextUnitOfWork</code>变量，React将从这个兄弟节点开始为这个分支执行work。在这个时候，React只完成了之前兄弟节点的work，理解这点很重要。它没有完成父节点的work。<strong>只有当所有以子节点开始的分支都完成后，它才完成父节点的work并回到父节点。</strong></p>
<p>你可以从实现中看出，<code>performUnitOfWork</code>和<code>completeUnitOfWork</code>主要起到迭代的作用，而主要活动是在<code>beginWork</code>和<code>completeWork</code>函数中进行的。在这个系列接下来的文章中，我们将学到当React进入<code>beginWork</code>和<code>completeWork</code>函数中时<code>ClickCounter</code>组件和<code>span</code>节点发生了什么。</p>
<h2 data-id="heading-20">Commit阶段</h2>
<p>这个阶段开始于<a href="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L2306" target="_blank" rel="nofollow noopener noreferrer">completeRoot</a>函数.在这个阶段中React更新DOM，调用变更前后生命周期函数。</p>
<p>当React进入这个阶段，它有两颗树和effects链表。一颗树代表当前渲染在屏幕上的状态。然后有颗在<code>render</code>阶段创建的<code>alternate</code>树。在源码中它被称为<code>finishedWork</code>或<code>workInProgress</code>，代表需要被显示到屏幕上的状态。<code>alternate</code>树和<code>current</code>树类似，通过child和sibling指针连接。</p>
<p>然后，还有一条effects链 —— <code>finishedWork</code>树节点的子集，通过<code>nextEffect</code>指针连接的。记住effect链是<code>render</code>阶段的运行结果。render阶段的目标就是确定哪些节点需要插入、更新或删除 ，以及需要调用哪些组件的生命周期方法。<strong>这就是在commit阶段遍历的节点集。</strong></p>
<blockquote>
<p>为了调试，<code>current</code>树可通过<code>fiber root</code>的<code>current</code>属性访问。<code>finishedWork</code>树可以通过<code>current</code>树中<code>HostFiber</code>节点的<code>alternate</code>属性访问。</p>
</blockquote>
<p><code>commit</code>阶段的主要函数是<code>commitRoot</code>。 大体上，它做了下面这些事：</p>
<ul>
<li>在带有<code>Snapshot</code>effect标记的节点上调用 <code>getSnapshotBeforeUpdate</code>生命周期方法</li>
<li>在带有<code>Deletion</code>effect标记的节点上调用 <code>componentWillUnmount</code>生命周期方法</li>
<li>执行所有DOM的插入、更新、删除</li>
<li>设置<code>finishedWork</code>树作为<code>current</code>树</li>
<li>在带有<code>Placement</code>effect标记的节点上调用 <code>componentDidMount</code>生命周期方法</li>
<li>在带有<code>Update</code>effect标记的节点上调用 <code>componentDidUpdate</code>生命周期方法</li>
</ul>
<p>在调用变更前方法<code>getSnapshotBeforeUpdate</code>之后，React在树中提交所有副作用。分成两次完成。第一次执行所有DOM（host）的插入、更新、删除，和ref卸载。然后，React将<code>finishedWork</code>树分配给<code>FiberRoot</code>，标记<code>workInProgress</code>树作为<code>current</code>树。这是在commit阶段第一部分之后，第二个部分之前完成的。所以在<code>componentWillUnmount</code>中之前的树仍然是当前的。<code>componentDidMount/Update</code>中<code>finished</code>树是当前的。在第二部分中React调用其他生命周期方法和ref回调。这些方法作为独立部分执行，因此所有的插入、更新和删除在整颗树中都已被调用。</p>
<p>这是运行上述步骤的函数的大体结构：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params">root, finishedWork</span>) </span>&#123;
    commitBeforeMutationLifecycles()
    commitAllHostEffects();
    root.current = finishedWork;
    commitAllLifeCycles();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个子函数都实现循环遍历effects list并检查effects的类别。当发现effect和该函数作用有关时会应用它。</p>
<h3 data-id="heading-21">变更前生命周期方法</h3>
<p>例如，这是遍历effects树并检查节点是否有<code>Snapshot</code>effect的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitBeforeMutationLifecycles</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">while</span> (nextEffect !== <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">const</span> effectTag = nextEffect.effectTag;
        <span class="hljs-keyword">if</span> (effectTag & Snapshot) &#123;
            <span class="hljs-keyword">const</span> current = nextEffect.alternate;
            commitBeforeMutationLifeCycles(current, nextEffect);
        &#125;
        nextEffect = nextEffect.nextEffect;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于类组件，effect意味着调用<code>getSnapshotBeforeUpdate</code>生命周期方法。</p>
<h3 data-id="heading-22">DOM更新</h3>
<p><a href="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L376" target="_blank" rel="nofollow noopener noreferrer">commitAllHostEffects</a>是React执行更新DOM的函数。这个函数大体上定义了对节点要做的操作类型并执行它：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitAllHostEffects</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">switch</span> (primaryEffectTag) &#123;
        <span class="hljs-keyword">case</span> Placement: &#123;
            commitPlacement(nextEffect);
            ...
        &#125;
        <span class="hljs-keyword">case</span> PlacementAndUpdate: &#123;
            commitPlacement(nextEffect);
            commitWork(current, nextEffect);
            ...
        &#125;
        <span class="hljs-keyword">case</span> Update: &#123;
            commitWork(current, nextEffect);
            ...
        &#125;
        <span class="hljs-keyword">case</span> Deletion: &#123;
            commitDeletion(nextEffect);
            ...
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有趣的是，React在<code>commitDeletion</code>函数中调用<code>componentWillUnmount</code>方法作为删除过程的一部分。</p>
<h3 data-id="heading-23">变更后生命周期方法</h3>
<p><a href="https://github.com/facebook/react/blob/95a313ec0b957f71798a69d8e83408f40e76765b/packages/react-reconciler/src/ReactFiberScheduler.js#L465" target="_blank" rel="nofollow noopener noreferrer">commitAllLifecycles</a>是React调用剩下的<code>componentDidUpdate</code>和<code>componentDidMount</code>生命周期方法的函数。</p>
<p>终于结束了。在评论区中告诉我你觉得这篇文章怎么样或问我问题。查看这个系列的下一篇文章<a href="https://indepth.dev/in-depth-explanation-of-state-and-props-update-in-react/" target="_blank" rel="nofollow noopener noreferrer">深入理解React中的state和props更新</a>。我计划写更多的文章深入解释调度器，协调过程，以及effects list是如何创建的。我也计划创建个视频，使用这篇文章作基础展示如何调试程序。</p></div>  
</div>
            