
---
title: '梳理 React 中与 Ref 相关的一些知识点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=921'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 18:11:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=921'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">梳理 React 中与 Ref 相关的一些知识点</h1>
<p>在 <code>React</code> 的官方文档中，分别对 <code>Refs转发</code> 、 <code>Refs & DOM</code> 以及 <code>Hooks</code> 中的 <code>UseRef()</code> 和 <code>useImperativeHandle()</code> 做了详细的介绍。</p>
<p>因为这些章节比较分散，对于想要系统学习 <code>Ref</code> 的同学来说，可能阅读成本比较高昂。加上这些知识之间的贯通性，放在一起做比较可以加深对它的理解。</p>
<p>接下来我会按照自己的理解组织文章脉络，有兴趣的小伙伴直接按顺序阅读即可，相信到最后会对 <code>Ref</code> 有新的认识。</p>
<p>先来看下 <code>ref</code> 出现的背景。</p>
<h2 data-id="heading-1">背景</h2>
<p>在典型的 <code>React</code> 数据流中（自上而下），在父组件中想要更改子组件，则必须更改父组件的 <code>state</code> , 从而更改子组件接收到的 <code>props</code> ,触发子组件重新渲染。</p>
<p>但是在某些特殊情况下，我们想在父组件中直接更改子组件。被修改的子组件可以是一个 <code>react 组件</code> 也可以直接是一个 <code>DOM</code> 元素。如以下例子中，我想在页面初次渲染的时候，自动聚焦输入框：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改DOM元素</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改子组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> /></span></span>;
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然，我们需要拿到 <code>input</code> 元素，并执行其 <code>focus()</code> 方法。</p>
<p><code>ref</code> 便是这一情况的一剂良方。</p>
<p>想要使用 <code>ref</code>,首先我们需要创建它。在 <code>React</code> 中，创建 <code>ref</code> 有三种方式：<code>React.createRef()</code>，<code>回调ref</code> 和 <code>Hook API: useRef()</code>。我们先看第一种。</p>
<h2 data-id="heading-2">React.createRef()</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">const</span> myRef = React.createRef();
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;myref&#125;</span> /></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>React.createRef()</code> 创建 <code>ref</code>。并通过 <code>ref</code> 属性，附加到 <code>React元素</code>.</p>
<blockquote>
<p><code>React</code> 会在组件挂载时给 <code>current</code> 属性传入 <code>DOM</code> 元素，并在组件卸载时传入 <code>null</code> 值。<code>ref</code> 会在 <code>componentDidMount</code> 或 <code>componentDidUpdate</code> 生命周期钩子触发前更新。</p>
</blockquote>
<p><strong>现在通过 <code>myRef.current</code> 便可以拿到 <code>input</code> 元素</strong></p>
<p><code>current</code> 是 <code>ref</code> 的一个属性，其值根据节点的类型而有所不同：</p>
<ol>
<li>当 <code>ref</code> 属性用于 <code>HTML</code> 元素时，其值就是这个元素。</li>
<li>当 <code>ref</code> 属性用于自定义的 <code>class</code> 组件时，其值为组件实例。</li>
</ol>
<p>好了，我们来实现上面说到的聚焦输入框吧～</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改DOM元素</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = React.createRef();
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myRef.current.focus();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改子组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = React.createRef();
    <span class="hljs-function"><span class="hljs-title">focusInput</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myRef.current.focus();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = React.createRef();
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myRef.current.focusInput();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，函数组件因为没有实例，所以不能将 <code>ref</code> 属性作用于函数组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这段代码将不会生效，并且会报错</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">const</span> myRef = React.createRef();
    <span class="hljs-keyword">const</span> focusInput = <span class="hljs-function">() =></span> &#123;
        myRef.current.focus();
    &#125;;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;myRef&#125;</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;focusInput&#125;</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = React.createRef();
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 报错</span>
        <span class="hljs-built_in">this</span>.myRef.focusInput();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="hljs-comment">// Child因为不是class组件，所以ref不会生效</span>
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> /></span></span>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过有变通的方法，后面会有。我们继续看第二种方法 <code>回调ref</code>👀 ～</p>
<h2 data-id="heading-3">回调 ref</h2>
<p><code>回调ref</code> 使用函数的形式。这给函数可以接收 <code>React组件实例</code> 或者 <code>HTML DOM</code> 作为参数。所以它和 <code>React.createRef()</code> 一样，也可以作用于 <code>class组件</code> 和 <code>DOM</code>。</p>
<p>我们将上面的例子改成用 <code>回调ref</code> 的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改DOM元素</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = <span class="hljs-literal">null</span>;
    setInputRef = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.myRef = element;
    &#125;;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 注意这里的myRef就是DOM对象，不再有myRef.current</span>
        <span class="hljs-built_in">this</span>.myRef && <span class="hljs-built_in">this</span>.myRef.focus();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.setInputRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改子组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = <span class="hljs-literal">null</span>;
    setInputRef = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.myRef = element;
    &#125;;
    <span class="hljs-function"><span class="hljs-title">focusInput</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myRef.focus();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.setInputRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = <span class="hljs-literal">null</span>;
    setInputRef = <span class="hljs-function">(<span class="hljs-params">component</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.myRef = component;
    &#125;;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myRef && <span class="hljs-built_in">this</span>.myRef.focusInput();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.setInputRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在修改子组件的例子中，我们在 <code>Parent</code> 中调用 <code>Child</code> 的方法，实现功能。这是因为我们通过 <code>ref</code> 获取到了子组件实例。但是，其实 <code>回调ref</code> 可以直接 <code>获取子组件中的DOM节点</code>.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改子组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;props.inputRef&#125;</span> /></span></span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = <span class="hljs-literal">null</span>;
    setInputRef = <span class="hljs-function">(<span class="hljs-params">element</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.myRef = element;
    &#125;;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myRef && <span class="hljs-built_in">this</span>.myRef.focusInput();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">inputRef</span>=<span class="hljs-string">&#123;this.setInputRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中,将函数作为 <code>props</code> 传递给了子组件。现在 <code>this.myRef</code> 将直接是 <code>input</code> 元素。</p>
<p>那既然这样，思考如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 修改子组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;props.inputRef&#125;</span> /></span></span>;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = React.createRef();
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.myRef.current.focusInput();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">inputRef</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然，会报错的～</p>
<p>那如何在使用 <code>React.createRef()</code> 的情况下，也能够在父组件中直接获取子组件的 <code>DOM</code> 元素而不是组件实例呢？</p>
<p>这就要说到前面卖的关子了。前面说过，有方法将 <code>ref</code> 作用于函数组件。同样是这个方法，可以获取到子组件里的 <code>DOM</code> 元素。这个方法就是 <code>React.forwardRef()</code>。</p>
<h2 data-id="heading-4">React.forwardRef()</h2>
<p><code>forward</code>顾名思义，就是将我们创建的 <code>ref</code> 转发到子组件中的任意位置。来看一下它的用法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Child</span>
<span class="hljs-keyword">const</span> Child = React.forwardRef(<span class="hljs-function">(<span class="hljs-params">props, ref</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span> /></span></span>);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Child;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Parent</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    myRef = React.createRef();
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> /></span></span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Child</code> 的 <code>ref</code> 是我们创建的 <code>ref</code>。这个 <code>ref</code> 将作为 <code>React.forwardRef</code> 的函数参数的第二个参数传递给 <code>input</code> , 作为其 <code>ref</code> 属性的值。这就是其透传的作用。</p>
<p>上面说了两种创建 <code>ref</code> 的方法，以及直接获取子组件的 <code>DOM</code> 元素的方法。最后还有一种创建 <code>ref</code> 的方法属于 <code>React Hook API: useRef()</code>。</p>
<h2 data-id="heading-5">useRef()</h2>
<p><code>useRef</code> 和 <code>React.createRef</code> 大同小异。都是用来创建 <code>ref</code> 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">const</span> myRef = useRef(<span class="hljs-literal">null</span>);
    useEffect(<span class="hljs-function">() =></span> &#123;
        myRef.current.focus();
    &#125;, []);
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;myRef&#125;</span> /></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，<code>useRef</code> 强大之处在于，其可以很方便的保存任何值。因为它本质上就是一个普通的 JS 对象。并且，无论组件如何重新渲染，<code>useRef</code> 都会返回同一个对象。</p>
<p>我们来看一下它的巧用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Test</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">const</span> ref = useRef(<span class="hljs-literal">null</span>);
    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> id = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;&#125;);
        ref.current = id;
        <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">clearInterval</span>(ref.current);
        &#125;;
    &#125;);
    <span class="hljs-keyword">const</span> clear = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">clearInterval</span>(ref.current);
    &#125;;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clear&#125;</span>></span>clear<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上基本以及介绍完了关于 <code>React Ref</code> 的知识。还有一些不常用的没有介绍。我将官网链接按照逻辑顺序依次放在下面。想再系统地跟着官网过一遍的同学请可以按照这个顺序学习。</p>
<p><a href="https://zh-hans.reactjs.org/docs/refs-and-the-dom.html" target="_blank" rel="nofollow noopener noreferrer">1. React.createref</a></p>
<p>这一章说明的 <code>ref</code> 出现的背景，为什么需要使用它。如何创建，以及在 <code>DOM、class组件</code>中使用。</p>
<p><a href="https://zh-hans.reactjs.org/docs/forwarding-refs.html" target="_blank" rel="nofollow noopener noreferrer">2. React.forwardRef</a></p>
<p>这一章节主要介绍了 <code>React.createRef()</code> 的使用。如何利用它将我们创建的 <code>ref</code> 绑定到我们想要的任何子组件的任何<code>DOM</code> 元素上。</p>
<p><a href="https://zh-hans.reactjs.org/docs/hooks-reference.html#useref" target="_blank" rel="nofollow noopener noreferrer">3. Hook 中的 ref</a></p>
<p>这里主要介绍了 <code>useRef 和 useImperativeHandle</code> 的用法。</p>
<p>以上便是全部内容了，希望对你有所帮助，谢谢阅读～</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            