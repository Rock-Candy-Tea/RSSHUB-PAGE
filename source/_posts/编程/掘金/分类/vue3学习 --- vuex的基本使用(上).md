
---
title: 'vue3学习 --- vuex的基本使用(上)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://s3.jpg.cm/2021/08/28/IHR8R4.png'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 02:29:52 GMT
thumbnail: 'https://s3.jpg.cm/2021/08/28/IHR8R4.png'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>在开发中，我们会的应用程序需要处理各种各样的数据，这些 数据需要保存在我们应用程序中的某一个位置，对于这些数据 的管理我们就称之为是 <strong>状态管理</strong></p>
<p>在Vue开发中，我们使用组件化的开发方式</p>
<p>在组件中我们定义data或者在setup中返回使用的数据， 这些数据我们称之为state</p>
<p>在模块template中我们可以使用这些数据，模块最终会被 渲染成DOM，我们称之为View</p>
<p>在模块中我们会产生一些行为事件，处理这些行为事件时， 有可能会修改state，这些行为事件我们称之为actions</p>
<p><img src="https://s3.jpg.cm/2021/08/28/IHR8R4.png" alt="IHR8R4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>JavaScript开发的应用程序，已经变得越来越复杂了，当我们的应用遇到<strong>多个组件共享状态</strong>时，单向数据流的简洁性很容易被破坏</p>
<ul>
<li>多个视图依赖于同一状态</li>
<li>来自不同视图的行为需要变更同一状态</li>
</ul>
<p>此时管理不断变化的state本身是非常困难的:</p>
<ul>
<li>状态之间相互会存在依赖，一个状态的变化会引起另一个状态的变化，View页面也有可能会引起状态的变化</li>
<li>当应用程序复杂时，state在什么时候，因为什么原因而发生了变化，发生了怎么样的变化，会变得非常难以控制和追踪</li>
</ul>
<p>此时， 我们是否可以考虑将组件的内部状态抽离出来，以一个全局单例对象的方式来管理，即将这些数据转变为全局对象来进行使用</p>
<ul>
<li>在这种模式下，我们的组件树构成了一个巨大的 “试图View”</li>
<li>不管在树的哪个位置，任何组件都能获取状态或者触发行为</li>
<li>通过定义和隔离状态管理中的各个概念，并通过强制性的规则来维护视图和状态间的独立性，我们的代码边会 变得更加结构化和易于维护、跟踪</li>
</ul>
<p><img src="https://s3.jpg.cm/2021/08/28/IHRbA6.png" alt="IHRbA6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">使用</h2>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 安装 --- 如果需要使用的是vuex4.x，安装的时候需要添加 next 指定版本</span>
npm i vuex@next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般我们会将我们书写的操作vuex的代码存放在<code>store</code>文件夹下</p>
<h2 data-id="heading-1">store</h2>
<h3 data-id="heading-2">创建Store</h3>
<p>每一个Vuex应用的核心就是store(仓库):</p>
<ul>
<li>store本质上是一个容器，它包含着你的应用中大部分的状态(state)</li>
</ul>
<p>Vuex和单纯的全局对象的区别：</p>
<ul>
<li><code>Vuex的状态存储是响应式的</code>
<ul>
<li>当Vue组件从store中读取状态的时候，若store中的状态发生变化，那么相应的组件也会被更新</li>
</ul>
</li>
<li>不推荐直接改变store中的状态
<ul>
<li>改变store中的状态的唯一途径就显示<strong>提交 (commit) mutation</strong></li>
<li>这样使得我们可以方便的跟踪每一个状态的变化，从而让我们能够通过一些工具(如devTool)帮助我们更好的管理应用的状态</li>
</ul>
</li>
</ul>
<p><code>main.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./routes'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

<span class="hljs-comment">// vuex本质上也是vue的一个插件 --- 挂载到vue上以后会在所有的实例上生产一个$store对象来帮助我们访问vuex</span>
createApp(App).use(router).use(store).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>v1</code></p>
<p><code>store.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> store = createStore(&#123;
 <span class="hljs-comment">// state是一个返回对象的函数</span>
 <span class="hljs-comment">// 所有的vuex数据存放在state函数返回的对象中</span>
 <span class="hljs-function"><span class="hljs-title">state</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> &#123;
     <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
   &#125;
 &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>App.vue</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.state.counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 虽然这么做并不会报错，但是这样做vuex并不推荐</span>
      <span class="hljs-built_in">this</span>.$store.state.counter++
    &#125;,

    <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.state.counter--
    &#125;,
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>v2</code></p>
<p><code>store.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> store = createStore(&#123;
 <span class="hljs-function"><span class="hljs-title">state</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> &#123;
     <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
   &#125;
 &#125;,

 <span class="hljs-comment">// 通过mutations函数来修改state</span>
 <span class="hljs-attr">mutations</span>: &#123;
   <span class="hljs-comment">// mutations中的函数会被vuex在合适的时间进行回调</span>
   <span class="hljs-comment">// 会将当前vuex实例的state对象作为参数进行传入  </span>
   <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">state</span>)</span> &#123;
     state.counter++
   &#125;,
   <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params">state</span>)</span> &#123;
    state.counter--
  &#125;
 &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>App.vue</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.state.counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 使用commit函数，触发mutations中的对应函数</span>
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'increment'</span>)
    &#125;,

    <span class="hljs-function"><span class="hljs-title">decrement</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'decrement'</span>)
    &#125;,
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">单一状态树</h3>
<p>Vuex 使用<strong>单一状态树</strong>:</p>
<ul>
<li>用一个对象就包含了全部的应用层级别的状态</li>
<li>采用的是SSOT，Single Source of Truth，也可以翻译成单一数据源</li>
<li>这也意味着，每个应用将仅仅包含一个 store 实例</li>
<li>我们可以使用module来对store进行进一步的拆分</li>
</ul>
<p>单一状态树的优势:</p>
<ul>
<li>如果你的状态信息是保存到多个Store对象中的，那么之后的管理和维护等等都会变得特别困难</li>
<li>单一状态树能够让我们最直接的方式找到某个状态的片段，而且在之后的维护和调试过程中，也可以非常方便 的管理和维护</li>
</ul>
<h3 data-id="heading-4">mapState</h3>
<p>如果我们在模板中每次都需要通过<code>$store.state.xxx</code>的方式来访问store属性的话，会比较繁琐，所以vuex提供了mapState的辅助函数</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; age &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-comment">// 1. 使用方式1，使用数组作为参数进行传递</span>
    ...mapState([<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>, <span class="hljs-string">'counter'</span>])
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; sName &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; sAge &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; sCounter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-comment">// 使用方式2： 传递对象</span>
    <span class="hljs-comment">// 1. 可以自定义需要使用的store成员的名称</span>
    <span class="hljs-comment">// 2. 可以对获取到的数据进行二次加工</span>
    ...mapState(&#123;
      <span class="hljs-attr">sName</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.name,
      <span class="hljs-attr">sAge</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.age,
      <span class="hljs-attr">sCounter</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.counter * <span class="hljs-number">2</span>,
    &#125;)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mapState一般需要和computed一起结合使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// mapState返回的是对象，key是属性名，value是一个get函数，这个get函数会通过this.$store去取对应的属性值</span>
...mapState([<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>, <span class="hljs-string">'counter'</span>])

<span class="hljs-comment">// 实际编译后的结果是类似如下的对象（伪代码）</span>
&#123;
  <span class="hljs-function"><span class="hljs-title">name</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>,$store.name
  &#125;,
    
  <span class="hljs-function"><span class="hljs-title">age</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>,$store.age
  &#125;,
    
  <span class="hljs-function"><span class="hljs-title">counter</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>,$store.counter
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">setup中使用mapState</h4>
<p><code>hooks/useMapState.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapState, useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> &#123; computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">mapper</span>) </span>&#123;
    <span class="hljs-comment">// 在setup函数中可以通过useStore这个hook函数来获取store对象</span>
    <span class="hljs-keyword">const</span> store = useStore()

    <span class="hljs-comment">// mapState的参数无论是对象还是数组，他们的返回值结构都是一致的</span>
    <span class="hljs-comment">// &#123; key: get函数， key： get函数 &#125;</span>
    <span class="hljs-comment">// 所以我们导出的方法的参数即支持对象，也支持函数</span>
    <span class="hljs-keyword">const</span> mapStateFns = mapState(mapper)
    <span class="hljs-keyword">const</span> storeState = &#123;&#125;


    <span class="hljs-built_in">Object</span>.keys(mapStateFns).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      <span class="hljs-comment">// 之所以需要使用computed函数进行包裹的目的是为了导出对象的value</span>
      <span class="hljs-comment">// 使用通过computed函数导出的ref对象，这样才可以在store中数据发生改变的时候</span>
      <span class="hljs-comment">// 自动进行监听，并自动更新所有的依赖</span>
      storeState[key] = computed(mapStateFns[key].bind(&#123; <span class="hljs-attr">$store</span>: store &#125;))
    &#125;)

    <span class="hljs-keyword">return</span> storeState
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>hook使用者</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; age &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> useMapState <span class="hljs-keyword">from</span> <span class="hljs-string">'./hooks/useMapState'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;


    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 自定义的hook函数的参数即支持数组，也支持对象</span>
      ...useMapState([<span class="hljs-string">'name'</span>]),
      ...useMapState(&#123;
        <span class="hljs-attr">age</span>: <span class="hljs-function"><span class="hljs-params">store</span> =></span> store.age
      &#125;)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">getters</h2>
<p>某些属性我们可能需要经过变化后来使用，这个时候可以使用getters</p>
<p>getters类似于store中的computed</p>
<p><code>基本使用</code></p>
<p><code>store.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> store = createStore(&#123;
 <span class="hljs-function"><span class="hljs-title">state</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> &#123;
     <span class="hljs-attr">books</span>: [
       &#123;
         <span class="hljs-attr">name</span>: <span class="hljs-string">'book1'</span>,
         <span class="hljs-attr">price</span>: <span class="hljs-number">32</span>,
         <span class="hljs-attr">count</span>: <span class="hljs-number">3</span>
       &#125;,

       &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'book2'</span>,
        <span class="hljs-attr">price</span>: <span class="hljs-number">45</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">5</span>
      &#125;,

      &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'book3'</span>,
        <span class="hljs-attr">price</span>: <span class="hljs-number">54</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">2</span>
      &#125;
     ]
   &#125;
 &#125;,

 <span class="hljs-attr">getters</span>: &#123;
   <span class="hljs-comment">// getters中定义的是函数</span>
   <span class="hljs-comment">/*
    1. 参数1： state对象
    2. 参数2： getters对象，用于在getters中进行计算的时候可以使用其它的'计算值'
   */</span>
   <span class="hljs-function"><span class="hljs-title">totalPrice</span>(<span class="hljs-params">state, getters</span>)</span> &#123;
    <span class="hljs-keyword">return</span> (state.books.reduce(<span class="hljs-function">(<span class="hljs-params">total, book</span>) =></span> total + book.price * book.count, <span class="hljs-number">0</span>) * getters.discount).toFixed(<span class="hljs-number">2</span>)
   &#125;,

   <span class="hljs-function"><span class="hljs-title">discount</span>(<span class="hljs-params"></span>)</span> &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-number">0.95</span>
   &#125;
 &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>使用者</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!--
      和计算属性一样，虽然totalPrice是一个函数，
      但是使用的时候，像一个属性一样去使用即可
    --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.getters.totalPrice &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很多时候我们可能需要在进行计算的时候，需要添加限制条件，</p>
<p>此时我们可以让getters返回一个函数，通过返回的函数来接收我们需要的参数</p>
<p><code>store.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> store = createStore(&#123;
 <span class="hljs-function"><span class="hljs-title">state</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> &#123;
     <span class="hljs-attr">books</span>: [
       &#123;
         <span class="hljs-attr">name</span>: <span class="hljs-string">'book1'</span>,
         <span class="hljs-attr">price</span>: <span class="hljs-number">32</span>,
         <span class="hljs-attr">count</span>: <span class="hljs-number">3</span>
       &#125;,

       &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'book2'</span>,
        <span class="hljs-attr">price</span>: <span class="hljs-number">45</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">5</span>
      &#125;,

      &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'book3'</span>,
        <span class="hljs-attr">price</span>: <span class="hljs-number">54</span>,
        <span class="hljs-attr">count</span>: <span class="hljs-number">2</span>
      &#125;
     ]
   &#125;
 &#125;,

 <span class="hljs-attr">getters</span>: &#123;
   <span class="hljs-function"><span class="hljs-title">totalPrice</span>(<span class="hljs-params">state</span>)</span> &#123;
    <span class="hljs-comment">//  返回函数，让getter函数可以接收外界传入的参数</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-params">v</span> =></span> &#123;
      <span class="hljs-keyword">return</span> (state.books.reduce(<span class="hljs-function">(<span class="hljs-params">total, book</span>) =></span> book.count < v ? total + book.price * book.count : <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)).toFixed(<span class="hljs-number">2</span>)
    &#125;
   &#125;
 &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>使用者</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 进行参数传递 --></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.getters.totalPrice(5) &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">mapGetters</h4>
<p>和mapStore一样，vuex提供了mapGetters函数来便于我们进行使用</p>
<p><code>数组写法</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">computed</span>: &#123;
    ...mapGetters([<span class="hljs-string">'totalPrice'</span>])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>对象语法</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">computed</span>: &#123;
    ...mapGetters(&#123;
      <span class="hljs-comment">// 这里的vlaue直接给key的name即可</span>
      <span class="hljs-comment">// 不需要传递一个函数，这和mapStore函数的对象写法是不一致的</span>
      <span class="hljs-attr">totalPrice</span>: <span class="hljs-string">'totalPrice'</span>
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和之前mapStore封装的hook函数一样的思路</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetters, useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> &#123; computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">mapper</span>) </span>&#123;
    <span class="hljs-keyword">const</span> store = useStore()

    <span class="hljs-keyword">const</span> mapStateFns = mapGetters(mapper)
    <span class="hljs-keyword">const</span> storeState = &#123;&#125;


    <span class="hljs-built_in">Object</span>.keys(mapStateFns).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      storeState[key] = computed(mapStateFns[key].bind(&#123; <span class="hljs-attr">$store</span>: store &#125;))
    &#125;)

    <span class="hljs-keyword">return</span> storeState
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将useGetters和useStore进行整合</p>
<p><code>useMapper.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetters, mapState, useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> &#123; computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">mapper, mapFn</span>) </span>&#123;
    <span class="hljs-keyword">const</span> store = useStore()

    <span class="hljs-keyword">const</span> mapStateFns = mapFn === <span class="hljs-string">'state'</span> ? mapState(mapper) : mapGetters(mapper)
    <span class="hljs-keyword">const</span> storeState = &#123;&#125;


    <span class="hljs-built_in">Object</span>.keys(mapStateFns).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      storeState[key] = computed(mapStateFns[key].bind(&#123; <span class="hljs-attr">$store</span>: store &#125;))
    &#125;)

    <span class="hljs-keyword">return</span> storeState
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useState.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> useMapper <span class="hljs-keyword">from</span> <span class="hljs-string">'./useMapper'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">mapper</span>) </span>&#123;
   <span class="hljs-keyword">return</span> useMapper(mapper, <span class="hljs-string">'state'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useGetters.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> useMapper <span class="hljs-keyword">from</span> <span class="hljs-string">'./useMapper'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">mapper</span>) </span>&#123;
   <span class="hljs-keyword">return</span> useMapper(mapper, <span class="hljs-string">'getter'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>index.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> useGetters <span class="hljs-keyword">from</span> <span class="hljs-string">'./useMapper'</span>
<span class="hljs-keyword">import</span> useState <span class="hljs-keyword">from</span> <span class="hljs-string">'./useState'</span>

<span class="hljs-keyword">export</span> &#123;
  useGetters,
  useState
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>使用者</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; totalPrice(5) &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; useGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./hooks'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      ...useGetters([<span class="hljs-string">'totalPrice'</span>])
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">mutations</h2>
<h4 data-id="heading-9">参数传递</h4>
<p><code>store.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> store = createStore(&#123;
 <span class="hljs-function"><span class="hljs-title">state</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> &#123;
     <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
   &#125;
 &#125;,
 <span class="hljs-attr">mutations</span>: &#123;
   <span class="hljs-function"><span class="hljs-title">incrementN</span>(<span class="hljs-params">store, payload</span>)</span> &#123;
     store.counter += payload.step
   &#125;,
   <span class="hljs-function"><span class="hljs-title">decrementN</span>(<span class="hljs-params">store, payload</span>)</span> &#123;
    store.counter -= payload.step
   &#125;
 &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>使用者</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.state.counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>+10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement"</span>></span>-10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; useStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> store = useStore()

    <span class="hljs-keyword">const</span> increment = <span class="hljs-function">() =></span> store.commit(<span class="hljs-string">'incrementN'</span>, &#123; <span class="hljs-attr">step</span>: <span class="hljs-number">10</span> &#125;)

    <span class="hljs-comment">// 这是另一个提交方式</span>
    <span class="hljs-keyword">const</span> decrement = <span class="hljs-function">() =></span> store.commit(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'decrementN'</span>,
      <span class="hljs-attr">step</span>: <span class="hljs-number">10</span>
    &#125;)

    <span class="hljs-keyword">return</span> &#123;
      increment,
      decrement
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">mapMutations</h4>
<p>和mapGetters和mapStore一样，vuex为mutation提供了辅助函数<code>mapMutations</code></p>
<p><code>options api中的使用</code></p>
<p><code>数组写法</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.state.counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"incrementN(&#123;step: 10&#125;)"</span>></span>+10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrementN(&#123;step: 10&#125;)"</span>></span>-10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 注意: mapMutations解构出来的函数是不需要交给computed的</span>
    <span class="hljs-comment">// 因为mapMutations返回的是类似于 &#123;key: 事件处理函数， key: 事件处理函数&#125; 格式的对象</span>
    <span class="hljs-comment">// 所以mapMutations返回的函数，可以直接合并到methods中直接使用</span>
    ...mapMutations([<span class="hljs-string">'incrementN'</span>, <span class="hljs-string">'decrementN'</span>])
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>对象写法</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.state.counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment(&#123;step: 10&#125;)"</span>></span>+10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement(&#123;step: 10&#125;)"</span>></span>-10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-attr">methods</span>: &#123;
    ...mapMutations(&#123;
      <span class="hljs-attr">increment</span>: <span class="hljs-string">'incrementN'</span>,
      <span class="hljs-attr">decrement</span>: <span class="hljs-string">'decrementN'</span>
    &#125;)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>composition api中的使用</code></p>
<p><code>数组语法</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.state.counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"incrementN(&#123;step: 10&#125;)"</span>></span>+10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrementN(&#123;step: 10&#125;)"</span>></span>-10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> mutations = mapMutations([<span class="hljs-string">'incrementN'</span>, <span class="hljs-string">'decrementN'</span>])

    <span class="hljs-keyword">return</span> &#123;
      ...mutations
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>对象语法</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;&#123; $store.state.counter &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment(&#123;step: 10&#125;)"</span>></span>+10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"decrement(&#123;step: 10&#125;)"</span>></span>-10<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> mutations = mapMutations(&#123;
      <span class="hljs-attr">increment</span>: <span class="hljs-string">'incrementN'</span>,
      <span class="hljs-attr">decrement</span>: <span class="hljs-string">'decrementN'</span>
    &#125;)

    <span class="hljs-keyword">return</span> &#123;
      ...mutations
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            