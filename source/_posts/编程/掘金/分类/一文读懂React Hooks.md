
---
title: '一文读懂React Hooks'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3362'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 23:35:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=3362'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 4 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">什么是React Hooks？</h2>
<p>引自官网：</p>
<blockquote>
<p>Hook 是 React 16.8 的新增特性。它可以让你在不编写 class 的情况下使用 state 以及其他的 React 特性。</p>
</blockquote>
<p>其实react一直是很推崇使用无副作用的function来实现组件的，class的组件弊端有很多，比如使用的模式是组合，而不是继承，违背了class的初衷，class有一定的上手门槛，而且内部的this会让一些新手摸不着头脑。</p>
<p>但是使用function的形式实现组件的话，会完全依赖外部状态，自身无法实现状态管理，这对于一些业务场景显得有些棘手。在这之前，我们会用redux或者把状态写在class内部来进行管理。在Hook出现后，可以可以在函数内部管理状态了。</p>
<h2 data-id="heading-1">解决了什么问题？</h2>
<ol>
<li>在组件之间复用状态逻辑很难</li>
<li>复杂组件变得难以理解</li>
<li>难以理解的 class</li>
</ol>
<p>以上三点是官方提的，有兴趣的同学可以去看看官方怎么说的。我们可以这么看这个问题，一个视图的最终呈现需要UI+State，在传统的class组件中，UI和State是交织在一起的，想要抽离怎么办？一种是把一些状态提出来，封装成一个utils库，但是就进不了生命周期了，因为变成了静态方法。</p>
<p>Redux解决了这个问题，在引入Redux架构后，React Component负责UI的展示，Redux负责状态管理。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>
<span class="hljs-keyword">import</span> &#123; addTodo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../actions'</span>

<span class="hljs-keyword">let</span> AddTodo = <span class="hljs-function">(<span class="hljs-params">&#123; dispatch &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> input

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">form</span>
        <span class="hljs-attr">onSubmit</span>=<span class="hljs-string">&#123;e</span> =></span> &#123;
          e.preventDefault()
          if (!input.value.trim()) &#123;
            return
          &#125;
          dispatch(addTodo(input.value))
          input.value = ''
        &#125;&#125;
      >
        <span class="hljs-tag"><<span class="hljs-name">input</span>
          <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;node</span> =></span> &#123;
            input = node
          &#125;&#125;
        />
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>></span>
          Add Todo
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
AddTodo = connect()(AddTodo)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> AddTodo
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Hooks 实践</h2>
<h3 data-id="heading-3">useState</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> [state, setState] = useState(initialState);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个应该是我们用的最多的Hook了，在初始阶段，state的值会等于initialState，setState用于更新state的值，state发生改变，触发页面刷新。</p>
<h3 data-id="heading-4">useEffect</h3>
<p>类似于在class组件中的componentDidMount、componentDidUpdate、componentWillUnmount的结合体，有两个参数，第一个参数为函数，第二个参数为依赖项</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">useEffect(
  <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> subscription = props.source.subscribe();
    <span class="hljs-comment">// 返回一个函数，会在销毁前调用</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      subscription.unsubscribe();
    &#125;;
  &#125;,
  [props.source], <span class="hljs-comment">// 根据依赖项的变化而触发函数的调用，传[]表示只调用一次</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">useContext</h3>
<p>接收一个 context 对象（React.createContext 的返回值）并返回该 context 的当前值。一般我们会配合Context.Provider来使用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> themes = &#123;
  <span class="hljs-attr">light</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#000000"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#eeeeee"</span>
  &#125;,
  <span class="hljs-attr">dark</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#ffffff"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#222222"</span>
  &#125;
&#125;;

<span class="hljs-keyword">const</span> ThemeContext = React.createContext(themes.light);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ThemeContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;themes.dark&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Toolbar</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">ThemeContext.Provider</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Toolbar</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ThemedButton</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ThemedButton</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> theme = useContext(ThemeContext);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">background:</span> <span class="hljs-attr">theme.background</span>, <span class="hljs-attr">color:</span> <span class="hljs-attr">theme.foreground</span> &#125;&#125;></span>
      I am styled by theme context!
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">小结</h2>
<ul>
<li>React Hooks 的出现提供了我们更好的模块化代码的方式，我们从以前的抽离公共UI的方式，可以变为更小粒度的拆分，例如拆分某个公共的逻辑</li>
<li>React Hooks 能够大大的减少我们大代码量，不需要再去理解复杂的class Component，一切都变的更加简单了</li>
<li>在使用的过程中一定要注意到，Function Component 始终是函数，只要re-render，里面的代码都会重新执行，内联函数，内联对象都会被重新创建</li>
</ul></div>  
</div>
            