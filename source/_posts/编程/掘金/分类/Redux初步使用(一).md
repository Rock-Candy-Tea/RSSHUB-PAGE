
---
title: 'Redux初步使用(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f39777da5bd6409aaaef8cdfc59f0568~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 02:03:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f39777da5bd6409aaaef8cdfc59f0568~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<p>好久没有更新博客了，前段时间一直在准备春招，幸运的是能入职一家不错的公司，公司的技术栈是react，所以得转react，希望以后学习的过程中能多更新文章，学会知识最好的办法就是给别人讲懂。</p>
<h3 data-id="heading-1">一、Redux介绍</h3>
<blockquote>
<p>Redux 是针对 JavaScript 应用程序的可预测状态容器。</p>
<p>它可以帮助您编写性能一致、在不同环境（客户端、服务器和原生环境）中运行且易于测试的应用程序。最重要的是，它提供了出色的开发人员体验，例如 <a href="https://github.com/reduxjs/redux-devtools" target="_blank" rel="nofollow noopener noreferrer">带有时间旅行调试器的实时代码编辑</a>。</p>
<p>可以将 Redux 与 <a href="https://reactjs.org/" target="_blank" rel="nofollow noopener noreferrer">React</a> 或任何其他类似的工具库一起使用。 他的体积很小（算上依赖也只有 2kB），但是在其生态系统中有大量插件可用。</p>
</blockquote>
<p>以上是官网的解释，其实就和Vuex是一个状态管理器，用来在构建大型应用的时候组件之间可以共享全局数据。因为如果业务过于复杂组件之间数据传递可能会很麻烦。就像这样，左边是没有 redux，右边是有 redux。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f39777da5bd6409aaaef8cdfc59f0568~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">二、Redux工作流程</h3>
<p>首先放张图片感受一下</p>
<p><img alt="redux" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ba9b64e894942d186d46924fb798a66~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">2.1 redux 安装</h4>
<p>npm安装</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install --save redux
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2.2 redux基本使用</h4>
<p>我们可以看到 <code>React Components</code> 是从 <code>Store</code> 里面拿数据的，那么我们可以初步得出结论，<code>Store</code> 就是数据管理中心，所有的全局数据就是存在这里面的，下面我们来使用一下。</p>
<p>我们在 <code>react</code> 项目中 <code>src</code> 文件中新建 <code>store</code> 文件夹下面新建两个文件分别为 <code>index.js</code> <code>reducer.js</code></p>
<p>大致目录如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">--src
----store
------index.js
------reducer.js
----index.js
----TodoList.js
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// store/reducer.js</span>
<span class="hljs-keyword">const</span> defaultState = &#123;
    <span class="hljs-attr">inputValue</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">data</span>: [
        &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'吃饭'</span>, <span class="hljs-attr">compeled</span>: <span class="hljs-literal">false</span> &#125;,
        &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'睡觉'</span>, <span class="hljs-attr">compeled</span>: <span class="hljs-literal">false</span> &#125;,
        &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'打豆豆'</span>, <span class="hljs-attr">compeled</span>: <span class="hljs-literal">false</span> &#125;
    ]
&#125;

<span class="hljs-comment">//eslint-disable-next-line</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (state = defaultState, action) => &#123;

    <span class="hljs-comment">// console.log(action)</span>
    <span class="hljs-comment">// Reducer里面只能接收state 不能改变state</span>
    <span class="hljs-keyword">if</span>(action.type === <span class="hljs-string">'CHANGE_INPUT'</span>)&#123;
        <span class="hljs-keyword">let</span> newValue = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(state))
        newValue.inputValue = action.value
        <span class="hljs-keyword">return</span> newValue
    &#125;

    <span class="hljs-keyword">if</span>(action.type === <span class="hljs-string">'ADD_ITEM'</span>)&#123;
        <span class="hljs-keyword">let</span> newValue = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(state))
        <span class="hljs-keyword">if</span>(newValue.inputValue === <span class="hljs-string">''</span>) <span class="hljs-keyword">return</span> newValue
        <span class="hljs-keyword">let</span> item = &#123;
            <span class="hljs-attr">id</span>:<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime(),
            <span class="hljs-attr">title</span>:newValue.inputValue,
            <span class="hljs-attr">compeled</span>:<span class="hljs-literal">false</span>
        &#125;
        newValue.data.push(item)
        newValue.inputValue = <span class="hljs-string">''</span>
        <span class="hljs-keyword">return</span> newValue
    &#125;

    <span class="hljs-keyword">if</span>(action.type === <span class="hljs-string">'DELETE_ITEM'</span>)&#123;
        <span class="hljs-keyword">let</span> newValue = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(state))
        <span class="hljs-keyword">let</span> index = newValue.data.findIndex(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.id === action.id)
        newValue.data.splice(index,<span class="hljs-number">1</span>)
        <span class="hljs-keyword">return</span> newValue
    &#125;
    
    <span class="hljs-keyword">return</span> state
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// store/index.js</span>
<span class="hljs-keyword">import</span> &#123;createStore&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">import</span> reducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducer'</span>
<span class="hljs-comment">// reducer (state,action) => &#123;&#125;</span>
<span class="hljs-keyword">const</span> store = createStore(reducer)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们看到创建 <code>store</code> 对象其实调用了 <code>redux</code> 中的 <code> createStore</code> 方法，它的参数就是一个函数，就是我们的 <code>reducer</code> ，<code>reducer</code> 它里面有 <code>state</code> 和 <code>action</code> 两个参数。<code>state</code> 我们初始化了值。而我们的 <code>action</code> 这里是什么呢？</p>
<p>我们看看<code> TodoList.js</code> 的代码，我们通过引入创建的 <code>store</code> 通过 <code>store.getState()</code> 获取数据。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'antd/dist/antd.css'</span>
<span class="hljs-keyword">import</span> &#123; Button, Input, List &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>

<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TodoList</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props);
      <span class="hljs-comment">//获取数据</span>
        <span class="hljs-built_in">this</span>.state = store.getState()
      <span class="hljs-comment">// 监听数据改变 更新state</span>
        store.subscribe(<span class="hljs-built_in">this</span>.storeChange)
    &#125;

    deleteItem = <span class="hljs-function">(<span class="hljs-params">id</span>) =></span> &#123;
        <span class="hljs-comment">// console.log(id)</span>
        <span class="hljs-keyword">const</span> action = &#123;
            <span class="hljs-attr">type</span>:<span class="hljs-string">'DELETE_ITEM'</span>,
            id
        &#125;
        <span class="hljs-comment">// 删除item</span>
        store.dispatch(action)
    &#125;

    handleInputValue = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> action = &#123;
            <span class="hljs-attr">type</span>:<span class="hljs-string">'CHANGE_INPUT'</span>,
            <span class="hljs-attr">value</span>:e.target.value
        &#125;
        <span class="hljs-comment">//改变inputvalue</span>
        store.dispatch(action)
    &#125;

    clickBtn = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> action = &#123;
            <span class="hljs-attr">type</span>:<span class="hljs-string">'ADD_ITEM'</span>
        &#125;
        <span class="hljs-comment">// 添加item</span>
        store.dispatch(action)
    &#125;

    storeChange = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(store.getState())
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;margin:</span>'<span class="hljs-attr">15px</span>'&#125;&#125;></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">Input</span>
                        <span class="hljs-attr">placeholder</span>=<span class="hljs-string">'Write Something'</span> 
                        <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;width:</span>'<span class="hljs-attr">250px</span>',<span class="hljs-attr">marginRight:</span>'<span class="hljs-attr">15px</span>'&#125;&#125; 
                        <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;this.handleInputValue&#125;</span>
                        <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.inputValue&#125;</span>
                    /></span>
                    <span class="hljs-tag"><<span class="hljs-name">Button</span> 
                        <span class="hljs-attr">type</span>=<span class="hljs-string">'primary'</span>
                        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.clickBtn&#125;</span>
                    ></span>Add<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;marginTop:</span>'<span class="hljs-attr">15px</span>',<span class="hljs-attr">width:</span>'<span class="hljs-attr">250px</span>'&#125;&#125;></span>
                    <span class="hljs-tag"><<span class="hljs-name">List</span>
                        <span class="hljs-attr">bordered</span>
                        <span class="hljs-attr">dataSource</span>=<span class="hljs-string">&#123;this.state.data&#125;</span>
                        <span class="hljs-attr">renderItem</span>=<span class="hljs-string">&#123;item</span> =></span> (<span class="hljs-tag"><<span class="hljs-name">List.Item</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.deleteItem.bind(this,item.id)&#125;</span>></span>&#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">List.Item</span>></span>)&#125;
                        />
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        );
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> TodoList;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 <code>action</code> 就是我们通过 <code>store.dispatch(action)</code> 方法派发的一个个事件，这里 <code>action</code> 对象必须有一个 <code>type</code> 属性, 用来告诉 redux 你要做哪一类操作，也就是我们 <code>case</code> 到那个 <code>type</code> 就做执行相应的逻辑。然后我们通过 <code>reducer</code> 回调来更新相应数据。这里注意一下: <code>reducer里面只能接收 state 不能改变state,所以我们可以看到上面是先拷贝数据，更新之后再返回，并不是直接更新 state 的数据</code></p>
<p>那么我们可以根据上面的流程图初步了解redux的执行流程，首先通过 <code>redux</code> 的 <code>createStore</code> 函数创建一个 <code>store</code> 对象，注意<code>createStore</code>的参数是个函数 <code>reducer</code> 。我们 <code>react components</code> 通过 <code>store.getState()</code> 获取数据，如果需要操作 <code>store</code>，我们需要通过 <code>store.dispatch(action)</code> 来派发事件。 去告知 <code>store</code> 做出相应的改变，怎么做出改变呢？我们看到数据通过 <code>React Components</code> 出发到 <code>Action Creators</code> 再到 <code>Store</code> 最终到 <code>Reducers</code> 才进行理的，也就是 <code>reducer</code> 来处理数据。那么我们上面的代码也可以清楚的展示 reducer 函数里根据不同type处理各种 <code>dispatch(action)</code> 派发的事件。处理之后的 <code>newState</code> 更新到 <code>Store</code> 数据仓库供 <code>React Components</code> 使用</p>
<p>为了阅读方便，再次放送此图。</p>
<p><img alt="redux" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ff8a1157ddd4af494d40bd31779ed68~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>为了demo完整性，这里将 src/index.js 代码贴上</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDom <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> TodoList <span class="hljs-keyword">from</span> <span class="hljs-string">'./TodoList'</span>

ReactDom.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">TodoList</span> /></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里redux最简单的使用就差不多了介绍完了。后面会持续更新一些高级的用法，喜欢记得点点关注。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            