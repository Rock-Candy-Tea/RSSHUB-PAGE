
---
title: 'petite-vue源码分析：无虚拟DOM的极简版Vue'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eedf8fb517f34ca1acb049c58c7ea779~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 07:19:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eedf8fb517f34ca1acb049c58c7ea779~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文同步在个人博客<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.shymean.com%2Farticle%2Fpetite-vue%25E6%25BA%2590%25E7%25A0%2581%25E5%2588%2586%25E6%259E%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://www.shymean.com/article/petite-vue%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90" ref="nofollow noopener noreferrer">shymean.com</a>上，欢迎关注</p>
</blockquote>
<p>最近发现Vue增加了一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fpetite-vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/petite-vue" ref="nofollow noopener noreferrer">petite-vue</a>的仓库，大概看了一下，这是一个无虚拟DOM的mini版Vue，前身貌似是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyyx990803%2Fvue-lit" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yyx990803/vue-lit" ref="nofollow noopener noreferrer">vue-lite</a>(瞎猜的~)，主要用于在服务端渲染的HTML页面中上"sprinkling"(点缀)一些Vue式的交互。颇有意思，于是看了下源码(<code>v0.2.3</code>)，整理了本文。</p>

<h2 data-id="heading-0">起步</h2>
<h3 data-id="heading-1">开发调试环境</h3>
<p>整个项目的开发环境非常简单</p>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> git@github.com:vuejs/petite-vue.git

yarn 

<span class="hljs-comment"># 使用vite启动</span>
npm run dev

<span class="hljs-comment"># 访问http://localhost:3000/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(不得不说，用vite来搭开发环境还是挺爽的~</p>
<p>新建一个测试文件<code>exmaples/demo.html</code>，写点代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123; createApp, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../src'</span>

  createApp(&#123;
    <span class="hljs-attr">msg</span>: <span class="hljs-string">"hello"</span>
  &#125;).mount(<span class="hljs-string">"#app"</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123;msg&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后访问<code>http://localhost:3000/demo.html</code>即可</p>
<h3 data-id="heading-2">目录结构</h3>
<p>从readme可以看见项目与标准vue的一些差异</p>
<ul>
<li>Only ~5.8kb，体积很小</li>
<li>Vue-compatible template syntax，与Vue兼容的模板语法</li>
<li>DOM-based, mutates in place，基于DOM驱动，就地转换</li>
<li>Driven by @vue/reactivity，使用<code>@vue/reactivity</code>驱动</li>
</ul>
<p>目录结构也比较简单，使用ts编写，外部依赖基本上只有<code>@vue/reactivity</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eedf8fb517f34ca1acb049c58c7ea779~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">核心实现</h2>
<h3 data-id="heading-4">createContext</h3>
<p>从上面的demo代码可以看出，整个项目从<code>createApp</code>开始。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createApp = <span class="hljs-function">(<span class="hljs-params">initialData?: <span class="hljs-built_in">any</span></span>) =></span> &#123;
  <span class="hljs-comment">// root context</span>
  <span class="hljs-keyword">const</span> ctx = createContext()
  <span class="hljs-keyword">if</span> (initialData) &#123;
    ctx.scope = reactive(initialData) <span class="hljs-comment">// 将初始化数据代理成响应式</span>
  &#125;
  <span class="hljs-comment">// app的一些接口</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-function"><span class="hljs-title">directive</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, def?: Directive</span>)</span> &#123;&#125;,
    <span class="hljs-function"><span class="hljs-title">mount</span>(<span class="hljs-params">el?: <span class="hljs-built_in">string</span> | Element | <span class="hljs-literal">null</span></span>)</span> &#123;&#125;,
    <span class="hljs-function"><span class="hljs-title">unmount</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于Vue3中的reactive,可以参考之前整理的：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.shymean.com%2Farticle%2FVue3%25E6%25BA%2590%25E7%25A0%2581%25E5%2588%2586%25E6%259E%2590%25E2%2580%2594%25E2%2580%2594%25E6%2595%25B0%25E6%258D%25AE%25E4%25BE%25A6%25E6%25B5%258B" target="_blank" rel="nofollow noopener noreferrer" title="https://www.shymean.com/article/Vue3%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E6%95%B0%E6%8D%AE%E4%BE%A6%E6%B5%8B" ref="nofollow noopener noreferrer">Vue3中的数据侦测reactive</a>，这里就不再展开了。</p>
<p>createApp中主要是通过<code>createContext</code>创建根context，这个上下文现在基本不陌生了，来看看<code>createContext</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createContext = (parent?: Context): <span class="hljs-function"><span class="hljs-params">Context</span> =></span> &#123;
  <span class="hljs-keyword">const</span> ctx: Context = &#123;
    ...parent,
    <span class="hljs-attr">scope</span>: parent ? parent.scope : reactive(&#123;&#125;),
    <span class="hljs-attr">dirs</span>: parent ? parent.dirs : &#123;&#125;, <span class="hljs-comment">// 支持的指令</span>
    <span class="hljs-attr">effects</span>: [],
    <span class="hljs-attr">blocks</span>: [],
    <span class="hljs-attr">cleanups</span>: [],
    <span class="hljs-comment">// 提供注册effect回调的接口，主要使用调度器来控制什么时候调用</span>
    <span class="hljs-attr">effect</span>: <span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (inOnce) &#123;
        queueJob(fn)
        <span class="hljs-keyword">return</span> fn <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>
      &#125;
      <span class="hljs-comment">// @vue/reactivity中的effect方法</span>
      <span class="hljs-keyword">const</span> e: ReactiveEffect = rawEffect(fn, &#123;
        <span class="hljs-attr">scheduler</span>: <span class="hljs-function">() =></span> queueJob(e)
      &#125;)
      ctx.effects.push(e)
      <span class="hljs-keyword">return</span> e
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> ctx
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>稍微看一下<code>queueJob</code>就可以发现，还是Vue中熟悉的<code>nextTick</code>实现，</p>
<ul>
<li>通过一个全局变量queue队列保存回调</li>
<li>在下一个微任务处理阶段，依次执行queue中的每一个回调，然后清空queue</li>
</ul>
<h3 data-id="heading-5">mount</h3>
<p>基本使用</p>
<pre><code class="hljs language-ts copyable" lang="ts">createApp().mount(<span class="hljs-string">"#app"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mount方法最主要的作用就是处理el参数，找到应用挂载的根DOM节点，然后执行初始化流程</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-title">mount</span>(<span class="hljs-params">el?: <span class="hljs-built_in">string</span> | Element | <span class="hljs-literal">null</span></span>)</span> &#123;
    <span class="hljs-keyword">let</span> roots: Element[]
    <span class="hljs-comment">// ...根据el参数初始化roots</span>
    <span class="hljs-comment">// 根据el创建Block实例</span>
    rootBlocks = roots.map(<span class="hljs-function">(<span class="hljs-params">el</span>) =></span> <span class="hljs-keyword">new</span> Block(el, ctx, <span class="hljs-literal">true</span>))
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Block</code>是一个抽象的概念，用于统一DOM节点渲染、插入、移除和销毁等操作。</p>
<p>下图是依赖这个<code>Block</code>的地方，可以看见主要在初始化、<code>if</code>和<code>for</code>这三个地方使用</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9d920710fa04a35ba549b3441aa1da2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看一下<code>Block</code>的实现</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// src/block.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Block</span> </span>&#123;
  <span class="hljs-attr">template</span>: Element | DocumentFragment
  <span class="hljs-attr">ctx</span>: Context
  key?: <span class="hljs-built_in">any</span>
  parentCtx?: Context

  <span class="hljs-attr">isFragment</span>: <span class="hljs-built_in">boolean</span>
  start?: Text
  end?: Text

  <span class="hljs-keyword">get</span> <span class="hljs-title">el</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.start || (<span class="hljs-built_in">this</span>.template <span class="hljs-keyword">as</span> Element)
  &#125;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">template: Element, parentCtx: Context, isRoot = <span class="hljs-literal">false</span></span>)</span> &#123;
    <span class="hljs-comment">// 初始化this.template</span>
    <span class="hljs-comment">// 初始化this.ctx</span>
    
    <span class="hljs-comment">// 构建应用</span>
    walk(<span class="hljs-built_in">this</span>.template, <span class="hljs-built_in">this</span>.ctx)
  &#125;
  <span class="hljs-comment">// 主要在新增或移除时使用，可以先不用关心实现</span>
  <span class="hljs-function"><span class="hljs-title">insert</span>(<span class="hljs-params">parent: Element, anchor: Node | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">teardown</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个walk方法，主要的作用是递归节点和子节点，如果之前了解过递归diff，这里应该比较熟悉。但petite-vue中并没有虚拟DOM，因此在walk中会直接操作更新DOM。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> walk = (node: Node, <span class="hljs-attr">ctx</span>: Context): ChildNode | <span class="hljs-literal">null</span> | <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = node.nodeType
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">type</span> === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-comment">// 元素节点</span>
    <span class="hljs-keyword">const</span> el = node <span class="hljs-keyword">as</span> Element
    <span class="hljs-comment">// ...处理 如v-if、v-for</span>
    <span class="hljs-comment">// ...检测属性执行对应的指令处理 applyDirective，如v-scoped、ref等</span>

    <span class="hljs-comment">// 先处理子节点，在处理节点自身的属性</span>
    walkChildren(el, ctx)

    <span class="hljs-comment">// 处理节点属性相关的自定，包括内置指令和自定义指令</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">type</span> === <span class="hljs-number">3</span>) &#123;
    <span class="hljs-comment">// 文本节点</span>
    <span class="hljs-keyword">const</span> data = (node <span class="hljs-keyword">as</span> Text).data
    <span class="hljs-keyword">if</span> (data.includes(<span class="hljs-string">'&#123;&#123;'</span>)) &#123;
      <span class="hljs-comment">// 正则匹配需要替换的文本，然后 applyDirective(text)</span>
      applyDirective(node, text, segments.join(<span class="hljs-string">'+'</span>), ctx)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">type</span> === <span class="hljs-number">11</span>) &#123;
    walkChildren(node <span class="hljs-keyword">as</span> DocumentFragment, ctx)
  &#125;
&#125;

<span class="hljs-keyword">const</span> walkChildren = <span class="hljs-function">(<span class="hljs-params">node: Element | DocumentFragment, ctx: Context</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> child = node.firstChild
  <span class="hljs-keyword">while</span> (child) &#123;
    child = walk(child, ctx) || child.nextSibling
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看见会根据<code>node.nodeType</code>区分处理处理</p>
<ul>
<li>对于元素节点，先处理了节点上的一些指令，然后通过<code>walkChildren</code>处理子节点。
<ul>
<li>v-if，会根据表达式决定是否需要创建Block然后执行插入或移除</li>
<li>v-for，循环构建Block，然后执行插入</li>
</ul>
</li>
<li>对于文本节点，替换<code>&#123;&#123;&#125;&#125;</code>表达式，然后替换文本内容</li>
</ul>
<h3 data-id="heading-6">v-if</h3>
<p>来看看if的实现，通过<code>branches</code>保存所有的分支判断，<code>activeBranchIndex</code>通过闭包保存当前位于的分支索引值。</p>
<p>在初始化或更新时，如果某个分支表达式结算结果正确且与上一次的activeBranchIndex不一致，就会创建新的Block，然后走Block构造函数里面的walk。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> _if = <span class="hljs-function">(<span class="hljs-params">el: Element, exp: <span class="hljs-built_in">string</span>, ctx: Context</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> parent = el.parentElement!
  <span class="hljs-keyword">const</span> anchor = <span class="hljs-keyword">new</span> Comment(<span class="hljs-string">'v-if'</span>)
  parent.insertBefore(anchor, el)

  <span class="hljs-comment">// 存放条件判断的各种分支</span>
  <span class="hljs-keyword">const</span> branches: Branch[] = [&#123; exp,el &#125;]

  <span class="hljs-comment">// 定位if...else if ... else 等分支，放在branches数组中</span>

  <span class="hljs-keyword">let</span> block: Block | <span class="hljs-literal">undefined</span>
  <span class="hljs-keyword">let</span> activeBranchIndex: <span class="hljs-built_in">number</span> = -<span class="hljs-number">1</span> <span class="hljs-comment">// 通过闭包保存当前位于的分支索引值</span>

  <span class="hljs-keyword">const</span> removeActiveBlock = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (block) &#123;
      parent.insertBefore(anchor, block.el)
      block.remove()
      block = <span class="hljs-literal">undefined</span>
    &#125;
  &#125;

  <span class="hljs-comment">// 收集依赖</span>
  ctx.effect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < branches.length; i++) &#123;
      <span class="hljs-keyword">const</span> &#123; exp, el &#125; = branches[i]
      <span class="hljs-keyword">if</span> (!exp || evaluate(ctx.scope, exp)) &#123;
        <span class="hljs-comment">// 当判断分支切换时，会生成新的block</span>
        <span class="hljs-keyword">if</span> (i !== activeBranchIndex) &#123;
          removeActiveBlock()
          block = <span class="hljs-keyword">new</span> Block(el, ctx)
          block.insert(parent, anchor)
          parent.removeChild(anchor)
          activeBranchIndex = i
        &#125;
        <span class="hljs-keyword">return</span>
      &#125;
    &#125;
    <span class="hljs-comment">// no matched branch.</span>
    activeBranchIndex = -<span class="hljs-number">1</span>
    removeActiveBlock()
  &#125;)

  <span class="hljs-keyword">return</span> nextNode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">v-for</h3>
<p>for指令的主要作用是循环创建多个节点，这里还根据key实现了类似于diff算法来复用Block的功能</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> _for = <span class="hljs-function">(<span class="hljs-params">el: Element, exp: <span class="hljs-built_in">string</span>, ctx: Context</span>) =></span> &#123;
  <span class="hljs-comment">// ...一些工具方法如createChildContexts、mountBlock</span>

  ctx.effect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> source = evaluate(ctx.scope, sourceExp)
    <span class="hljs-keyword">const</span> prevKeyToIndexMap = keyToIndexMap
    <span class="hljs-comment">// 根据循环项创建多个子节点的context</span>
    ;[childCtxs, keyToIndexMap] = createChildContexts(source)
    <span class="hljs-keyword">if</span> (!mounted) &#123;
      <span class="hljs-comment">// 首次渲染，创建新的Block然后insert</span>
      blocks = childCtxs.map(<span class="hljs-function">(<span class="hljs-params">s</span>) =></span> mountBlock(s, anchor))
      mounted = <span class="hljs-literal">true</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 更新时</span>
      <span class="hljs-keyword">const</span> nextBlocks: Block[] = []
      <span class="hljs-comment">// 移除不存在的block</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < blocks.length; i++) &#123;
        <span class="hljs-keyword">if</span> (!keyToIndexMap.has(blocks[i].key)) &#123;
          blocks[i].remove()
        &#125;
      &#125;
      <span class="hljs-comment">// 根据key进行处理</span>
      <span class="hljs-keyword">let</span> i = childCtxs.length
      <span class="hljs-keyword">while</span> (i--) &#123;
        <span class="hljs-keyword">const</span> childCtx = childCtxs[i]
        <span class="hljs-keyword">const</span> oldIndex = prevKeyToIndexMap.get(childCtx.key)
        <span class="hljs-keyword">const</span> next = childCtxs[i + <span class="hljs-number">1</span>]
        <span class="hljs-keyword">const</span> nextBlockOldIndex = next && prevKeyToIndexMap.get(next.key)
        <span class="hljs-keyword">const</span> nextBlock =
          nextBlockOldIndex == <span class="hljs-literal">null</span> ? <span class="hljs-literal">undefined</span> : blocks[nextBlockOldIndex]
        <span class="hljs-comment">// 不存在旧的block，直接创建</span>
        <span class="hljs-keyword">if</span> (oldIndex == <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-comment">// new</span>
          nextBlocks[i] = mountBlock(
            childCtx,
            nextBlock ? nextBlock.el : anchor
          )
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 存在旧的block，复用，检测是否需要移动位置</span>
          <span class="hljs-keyword">const</span> block = (nextBlocks[i] = blocks[oldIndex])
          <span class="hljs-built_in">Object</span>.assign(block.ctx.scope, childCtx.scope)
          <span class="hljs-keyword">if</span> (oldIndex !== i) &#123;
            <span class="hljs-keyword">if</span> (blocks[oldIndex + <span class="hljs-number">1</span>] !== nextBlock) &#123;
              block.insert(parent, nextBlock ? nextBlock.el : anchor)
            &#125;
          &#125;
        &#125;
      &#125;
      blocks = nextBlocks
    &#125;
  &#125;)

  <span class="hljs-keyword">return</span> nextNode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">处理指令</h3>
<p>所有的指令都是通过<code>applyDirective</code>和<code>processDirective</code>来处理的，后者是基于前者的二次封装，主要处理一些内置的指令快捷方式<code>builtInDirectives</code>，</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> builtInDirectives: Record<<span class="hljs-built_in">string</span>, Directive<<span class="hljs-built_in">any</span>>> = &#123;
  bind,
  on,
  show,
  text,
  html,
  model,
  effect
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每种指令都是基于ctx和el等来实现快速实现某些逻辑，具体实现可以参考对应源码。</p>
<p>当调用<code>app.directive</code>注册自定义指令时，</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-title">directive</span>(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, def?: Directive</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (def) &#123;
        ctx.dirs[name] = def
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> ctx.dirs[name]
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上是向contenx的dirs添加一个属性，当调用<code>applyDirective</code>时，就可以得到对应的处理函数</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> applyDirective = <span class="hljs-function">(<span class="hljs-params">el: Node,dir: Directive<<span class="hljs-built_in">any</span>>,exp: <span class="hljs-built_in">string</span>,ctx: Context,arg?: <span class="hljs-built_in">string</span>,modifiers?: Record<<span class="hljs-built_in">string</span>, <span class="hljs-literal">true</span>></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> get = <span class="hljs-function">(<span class="hljs-params">e = exp</span>) =></span> evaluate(ctx.scope, e, el)
  <span class="hljs-comment">// 执行指令方法</span>
  <span class="hljs-keyword">const</span> cleanup = dir(&#123;
    el,
    get,
    <span class="hljs-attr">effect</span>: ctx.effect,
    ctx,
    exp,
    arg,
    modifiers
  &#125;)
  <span class="hljs-comment">// 收集那些需要在卸载时清除的副作用</span>
  <span class="hljs-keyword">if</span> (cleanup) &#123;
    ctx.cleanups.push(cleanup)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，可以利用上面传入的这些参数来构建自定义指令</p>
<pre><code class="hljs language-ts copyable" lang="ts">app.directive(<span class="hljs-string">"auto-focus"</span>, <span class="hljs-function">(<span class="hljs-params">&#123;el&#125;</span>)=></span>&#123;
    el.focus()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">小结</h2>
<p>整个代码看起来，确实非常精简</p>
<ul>
<li>没有虚拟DOM，就无需通过template构建render函数，直接递归遍历DOM节点，通过正则处理各种指令就行了</li>
<li>借助<code>@vue/reactivity</code>，整个响应式系统实现的十分自然，除了在解析指令的使用通过<code>ctx.effect()</code>收集依赖，基本无需再关心数据变化的逻辑</li>
</ul>
<p>文章开头提到，<code>petite-vue</code>的主要作用是：在服务端渲染的HTML页面中上"sprinkling"(点缀)一些Vue式的交互。</p>
<p>就我目前接触到的大部分服务端渲染HTML的项目，如果要实现一些DOM交互，一般使用</p>
<ul>
<li>jQuery操作DOM，yyds</li>
<li>当然Vue也是可以通过script + template的方式编写的，但为了一个div的交互接入Vue，又有点杀鸡焉用牛刀的感觉</li>
<li>其他如React框架等同上</li>
</ul>
<p><code>petite-vue</code>使用了与Vue基本一致的模板语法和响应式功能，开发体验上应该很不错。且其无需考虑虚拟DOM跨平台的功能，在源码中直接使用浏览器相关API操作DOM，减少了框架runtime运行时的成本，性能方面应该也不错。</p>
<p>总结一下，感觉<code>petite-vue</code>结合了Vue标准版本的开发体验，以非常小的代码体积、良好的开发体验和还不错的运行性能，也许可以用来替代<code>jQuery</code>，用更现代的方式来操作DOM。</p>
<p>该项目是6月30号提交的第一个版本，目前相关的功能和接口应该不是特别稳定，可能会有调整。但就exmples目录中的示例而言，应该能满足一些简单的需求场景了，也许可以尝试在一些比较小型的历史项目中使用。</p></div>  
</div>
            