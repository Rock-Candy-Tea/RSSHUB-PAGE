
---
title: '简单实现Vuex'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ad50c52ffe4f76a993bceedf050e6c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 01:08:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ad50c52ffe4f76a993bceedf050e6c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><a href="https://github.com/OUDUIDUI/vue-source-code-study/tree/vuex" target="_blank" rel="nofollow noopener noreferrer">github</a>，<a href="https://ouduidui.cn/2021/04/27/simple_achieve_vuex/" target="_blank" rel="nofollow noopener noreferrer">blog</a></p>
</blockquote>
<p><a href="https://juejin.cn/post/6949158989368131621" target="_blank">简单实现VUE-Router</a></p>
<h1 data-id="heading-0">Vuex</h1>
<p><code>Vuex</code><strong>集中式</strong>存储管理应用的所有组件的状态，并以相应的规则保证状态以<strong>可预测</strong>的方式发生变化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ad50c52ffe4f76a993bceedf050e6c~tplv-k3u1fbpfcp-zoom-1.image" alt="vuex" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">安装Vuex</h2>
<pre><code class="hljs language-shell copyable" lang="shell">vue add vuex
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">核心概念</h2>
<ul>
<li><strong>state</strong>：状态、数据</li>
<li><strong>mutations</strong>：更改状态的函数</li>
<li><strong>action</strong>：异步操作</li>
<li><strong>store</strong>：包含以上概念的容器</li>
</ul>
<h3 data-id="heading-3">状态 - state</h3>
<p><code>state</code>保存应用状态</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue"><h1>
  &#123;&#123;$store.state.counter&#125;&#125;
</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">状态变更 - mutations</h3>
<p><code>mutations</code>用于修改状态</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">mutations</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">state</span>)</span>&#123;
      state.counter++
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue"><h1 @click="$store.commit('add')">
  &#123;&#123;$store.state.counter&#125;&#125;
</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">派生状态 - getters</h3>
<p>从<code>state</code>派生出来新状态，类似计算属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">getters</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">doubleCounter</span>(<span class="hljs-params">state</span>)</span>&#123;
      <span class="hljs-keyword">return</span> state.counter * <span class="hljs-number">2</span>;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue"><h1>
  &#123;&#123;$store.getters.doubleCounter&#125;&#125;
</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">动作 - actions</h3>
<p>添加业务逻辑，类似于<code>controller</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">actions</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">&#123;commit&#125;</span>)</span>&#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> commit(<span class="hljs-string">'add'</span>), <span class="hljs-number">1000</span>);
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-vue copyable" lang="vue"><h1 @tap="$store.dispatch('add')">
  &#123;&#123;$store.state.counter&#125;&#125;
</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">Vuex原理解析</h1>
<h2 data-id="heading-8">任务分析</h2>
<ul>
<li>实现插件
<ul>
<li>实现Store类
<ul>
<li>维持一个响应式状态state</li>
<li>实现commit()</li>
<li>实现dispatch()</li>
<li>实现getters</li>
</ul>
</li>
<li>挂载$store</li>
</ul>
</li>
</ul>
<h2 data-id="heading-9">创建新的插件</h2>
<p>在<code>Vue2.x</code>项目中的<code>src</code>路径下，复制一份<code>store</code>文件，重命名为<code>ou-store</code>。</p>
<p>然后在<code>ou-store</code>路径下新建一个<code>ou-vuex.js</code>文件，并将<code>index.js</code>文件中的<code>Vuex</code>引入改为<code>ou-vuex.js</code>。</p>
<pre><code class="copyable">import Vuex from './ou-vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时将<code>main.js</code>中的<code>router</code>引入也修改一下。</p>
<pre><code class="copyable">import router from './ou-vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">创建vue的插件</h2>
<p>回头看一下<code>store/index.js</code>，首先是使用<code>Vue.use()</code>注册了<code>Vuex</code>，然后再实例化了<code>Vuex.Store</code>这个类，因此<code>Vuex</code>这个对象里含有一个<code>install</code>方法以及一个<code>Store</code>的类。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    ...
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此我们来创建一个新的<code>Vuex</code>插件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Vue;    <span class="hljs-comment">// 保存Vue的构造函数，插件中需要用到</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">_Vue</span>) </span>&#123;
    Vue = _Vue;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;Store, install&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">挂载<code>$store</code></h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Vue;    <span class="hljs-comment">// 保存Vue的构造函数，插件中需要用到</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">_Vue</span>) </span>&#123;
    Vue = _Vue;

    Vue.mixin(&#123;
        <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-comment">// 挂载$store</span>
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$options.store)&#123;
                Vue.prototype.$store = <span class="hljs-built_in">this</span>.$options.store;     <span class="hljs-comment">// vm.$store</span>
            &#125;
        &#125;
    &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;Store, install&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">实现响应式保存<code>state</code>数据</h2>
<p>因为<code>state</code>是一个对象，我们可以使用<code>new Vue()</code>将<code>state</code>转换为一个响应式数据进行保存起来。</p>
<p>其次，我们不能显式去保存这个<code>state</code>，暴露给外面，因此我们可以使用<code>get</code>和<code>set</code>去保存。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;
    <span class="hljs-comment">/*
    * options:
    *   state
    *   mutations
    *   actions
    *   modules
    *   getters
    * */</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-comment">// data响应式处理</span>
        <span class="hljs-built_in">this</span>._vm = <span class="hljs-keyword">new</span> Vue(&#123;   
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">$$state</span>: options.state    <span class="hljs-comment">// 通过this._vm._data.$$state 或 this._vm.$data.$$state 获取</span>
            &#125;
        &#125;);
    &#125;

    <span class="hljs-comment">// 获取state</span>
    <span class="hljs-keyword">get</span> <span class="hljs-title">state</span>() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._vm._data.$$state;
    &#125;

    <span class="hljs-comment">// 不可设置state</span>
    <span class="hljs-keyword">set</span> <span class="hljs-title">state</span>(<span class="hljs-params">v</span>) &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'please use replaceState to reset state'</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">实现<code>commit</code>方法</h2>
<p>当我们使用<code>commit</code>方法时，都是<code>$store.commit(type,payload)</code>，第一个参数即<code>mutations</code>的<code>type</code>值，第二个是<code>payload</code>负载，而对应<code>mutation</code>方法的参数为<code>state</code>和<code>payload</code>，因此我们来实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">$$state</span>: options.state
            &#125;
        &#125;);

        <span class="hljs-comment">// 保存用户配置的mutations选项</span>
        <span class="hljs-built_in">this</span>._mutations = options.mutations;
    &#125;

    <span class="hljs-keyword">get</span> <span class="hljs-title">state</span>() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._vm._data.$$state;
    &#125;

    <span class="hljs-keyword">set</span> <span class="hljs-title">state</span>(<span class="hljs-params">v</span>) &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'please use replaceState to reset state'</span>);
    &#125;


    <span class="hljs-function"><span class="hljs-title">commit</span>(<span class="hljs-params">type, payload</span>)</span> &#123;
        <span class="hljs-comment">// 获取type对应的mutation</span>
        <span class="hljs-keyword">const</span> entry = <span class="hljs-built_in">this</span>._mutations[type]
        <span class="hljs-keyword">if</span>(!entry) &#123;
            <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`unknown mutation type : <span class="hljs-subst">$&#123;type&#125;</span>`</span>);
            <span class="hljs-keyword">return</span> ;
        &#125;

        <span class="hljs-comment">// 传递state和payload给mutation</span>
        entry(<span class="hljs-built_in">this</span>.state, payload)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">实现<code>dispatch</code>方法</h2>
<p><code>dispatch</code>方法跟<code>commit</code>方法大同小异，不同之处在于<code>dispatch</code>调用的是<code>action</code>异步函数，而<code>action</code>的参数为<code>context</code>和<code>payload</code>，<code>payload</code>我们可以通过<code>dispatch</code>的参数获取到，而<code>context</code>执行上下文其实就是实例中的<code>this</code>。</p>
<p>但<code>action</code>是用来处理异步函数的，因此我们需要对<code>dispatch</code>方法进行<code>this</code>绑定；同时，<code>action</code>方法中有可能会调用到<code>commit</code>方法，因此我们也需要对<code>commit</code>方法进行<code>this</code>绑定。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">$$state</span>: options.state 
            &#125;
        &#125;);

        <span class="hljs-comment">// 保存用户配置的mutations选项和actions选项</span>
        <span class="hljs-built_in">this</span>._mutations = options.mutations;
        <span class="hljs-built_in">this</span>._actions = options.actions;

        <span class="hljs-comment">// 将commit和dispatch绑定this，</span>
        <span class="hljs-built_in">this</span>.commit = <span class="hljs-built_in">this</span>.commit.bind(<span class="hljs-built_in">this</span>);
        <span class="hljs-built_in">this</span>.dispatch = <span class="hljs-built_in">this</span>.dispatch.bind(<span class="hljs-built_in">this</span>);
    &#125;

    <span class="hljs-keyword">get</span> <span class="hljs-title">state</span>() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._vm._data.$$state;
    &#125;

    <span class="hljs-keyword">set</span> <span class="hljs-title">state</span>(<span class="hljs-params">v</span>) &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'please use replaceState to reset state'</span>);
    &#125;


    <span class="hljs-function"><span class="hljs-title">commit</span>(<span class="hljs-params">type, payload</span>)</span> &#123;
        <span class="hljs-keyword">const</span> entry = <span class="hljs-built_in">this</span>._mutations[type]
        <span class="hljs-keyword">if</span>(!entry) &#123;
            <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`unknown mutation type : <span class="hljs-subst">$&#123;type&#125;</span>`</span>);
            <span class="hljs-keyword">return</span> ;
        &#125;

        entry(<span class="hljs-built_in">this</span>.state, payload)
    &#125;

    <span class="hljs-function"><span class="hljs-title">dispatch</span>(<span class="hljs-params">type, payload</span>)</span> &#123;
        <span class="hljs-comment">// 获取用户编写的type对应的action</span>
        <span class="hljs-keyword">const</span> entry = <span class="hljs-built_in">this</span>._actions[type];
        <span class="hljs-keyword">if</span>(!entry) &#123;
            <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`unknown action type : <span class="hljs-subst">$&#123;type&#125;</span>`</span>)
        &#125;
        <span class="hljs-comment">// 异步结果处理常常需要返回Promise</span>
        <span class="hljs-keyword">return</span> entry(<span class="hljs-built_in">this</span>, payload)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">实现<code>getters</code>派生状态</h2>
<p>当我们定义<code>getters</code>状态时，实际上是定义了一个<code>function</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">getters: &#123;
   <span class="hljs-function"><span class="hljs-title">doubleCounter</span>(<span class="hljs-params">state</span>)</span> &#123;
     <span class="hljs-keyword">return</span> state.counter * <span class="hljs-number">2</span>;
   &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而使用<code>getters</code>中某一个派生状态时，实际上是得到一个值，也就是这个<code>function</code>的返回值。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><h4>double count: &#123;&#123;$store.getters.doubleCounter&#125;&#125;</h4>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这其实就有点像对象中的<code>get</code>属性，因此我们可以使用<code>Object.defineProperty()</code>来实现<code>getters</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options = &#123;&#125;</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">$$state</span>: options.state   
            &#125;
        &#125;);

        <span class="hljs-built_in">this</span>._mutations = options.mutations;
        <span class="hljs-built_in">this</span>._actions = options.actions;

        <span class="hljs-built_in">this</span>.commit = <span class="hljs-built_in">this</span>.commit.bind(<span class="hljs-built_in">this</span>);
        <span class="hljs-built_in">this</span>.dispatch = <span class="hljs-built_in">this</span>.dispatch.bind(<span class="hljs-built_in">this</span>);

        <span class="hljs-comment">// 初始化getters，默认为一个空对象</span>
        <span class="hljs-built_in">this</span>.getters = &#123;&#125;;

        <span class="hljs-comment">// 遍历options.getters</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> options.getters) &#123;
            <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>;
            <span class="hljs-built_in">Object</span>.defineProperty(
                <span class="hljs-built_in">this</span>.getters,
                key,   <span class="hljs-comment">// key名</span>
                &#123;
                    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
                      <span class="hljs-comment">// 调用对应的函数，第一个参数为state，将结果返回</span>
                        <span class="hljs-keyword">return</span> options.getters[key](self._vm._data.$$state)   
                    &#125;
                &#125;
            )
        &#125;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            