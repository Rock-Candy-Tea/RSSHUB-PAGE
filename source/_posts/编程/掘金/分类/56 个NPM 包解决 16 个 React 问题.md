
---
title: '56 个NPM 包解决 16 个 React 问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b59ca044ffd4ac7b515d9bbf2524eab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 17:38:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b59ca044ffd4ac7b515d9bbf2524eab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>关于如何选择完美的 npm 包的深入指南。</p>
</blockquote>
<p>React 是用于构建用户界面的 JavaScript 库，它不仅是一个前端 UI 开发框架，更是一套完整的前端开发生态体系。</p>
<p>虽然 React 没有包含所有的解决方案，但是我们可以从繁荣的生态系统中找到应对不同场景的 NPM 包，来解决开发中遇到的问题。</p>
<p>今天，我们就从以下 16 个纬度着手，寻找最佳解决方案。</p>
<h2 data-id="heading-0">1. 全局状态管理</h2>
<p>在 99% 的应用程序中，组件之间共享状态是强制性的，并且有一些很好的本地和外部解决方案。</p>
<h3 data-id="heading-1">推荐</h3>
<p>如果你问我一种解决方案，我会说 <strong>Redux</strong>，不是因为他是最好的，而是因为它是最实用的。许多公司已经在使用它，意味着您也不得不在某个时刻使用它。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux-toolkit.js.org%2Fintroduction%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="https://redux-toolkit.js.org/introduction/getting-started" ref="nofollow noopener noreferrer">redux-toolkit</a>  +  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freact-redux" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/react-redux" ref="nofollow noopener noreferrer">react-redux</a></li>
</ul>
<p>以前我们使用 Redux，通常是指 Redux + React Redux 组合方案，但是现在有了更简化的方案：Redux Toolkit + React Redux，它帮助我们避免了 Redux 的三个常见问题：</p>
<ol>
<li>
<p>"配置一个 Redux 存储太复杂了"</p>
</li>
<li>
<p>"我必须添加很多包才能让 Redux 做任何有用的事情"</p>
</li>
<li>
<p>"Redux 需要太多样板代码"</p>
</li>
</ol>
<p>Redux Toolkit 简化了编写 Redux 逻辑和设置 store 的过程，允许我们编写更容易阅读的更短的逻辑，同时仍然遵循相同的 Redux 行为和数据流。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 react-toolkit（方式一）</span>
$ npm install @reduxjs/toolkit --save
<span class="hljs-comment"># or </span>
$ yarn add @reduxjs/toolkit

<span class="hljs-comment"># 还可以通过脚手架的 redux 模版安装使用（方式二）</span>
<span class="hljs-comment"># Redux + Plain JS template</span>
$ npx create-react-app my-app --template redux

<span class="hljs-comment"># Redux + TypeScript template</span>
$ npx create-react-app my-app --template redux-typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createSlice, configureStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@reduxjs/toolkit'</span>

<span class="hljs-keyword">const</span> counterSlice = createSlice(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'counter'</span>,
  <span class="hljs-attr">initialState</span>: &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-attr">incremented</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> &#123;
      state.value += <span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">decremented</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> &#123;
      state.value -= <span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; incremented, decremented &#125; = counterSlice.actions

<span class="hljs-keyword">const</span> store = configureStore(&#123;
  <span class="hljs-attr">reducer</span>: counterSlice.reducer
&#125;)

store.subscribe(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(store.getState()))
store.dispatch(incremented())
<span class="hljs-comment">// &#123;value: 1&#125;</span>
store.dispatch(incremented())
<span class="hljs-comment">// &#123;value: 2&#125;</span>
store.dispatch(decremented())
<span class="hljs-comment">// &#123;value: 1&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您还是使用 Redux + React Redux 组合方案，Redux 社区也还提供了很多中间件来简化各种场景。</p>
<ol>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Fredux-thunk" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/redux-thunk" ref="nofollow noopener noreferrer">redux-thunk</a> - 用于处理异步动作（与 redux 使用）；</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frt2zz%2Fredux-persist" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rt2zz/redux-persist" ref="nofollow noopener noreferrer">redux-persist</a> - 用于本地存储数据（离线支持）；</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freduxjs%2Freselect" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reduxjs/reselect" ref="nofollow noopener noreferrer">reselect</a> - 用于更快的查询存储；</p>
</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm install redux react-redux redux-thunk redux-persist reselect --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">备选方案</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Fcontext.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/context.html" ref="nofollow noopener noreferrer">context</a> - 内置与 React，适合简单使用，不利于性能，特别是如果您有大量变化的数据。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Frecoiljs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://recoiljs.org/" ref="nofollow noopener noreferrer">recoil</a> - 旨在解决特定问题，现在还是实验状态，精准更新、下一代状态管理方案。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpmndrs%2Fjotai" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pmndrs/jotai" ref="nofollow noopener noreferrer">jotai</a> - 简约的 API、没有字符串键、面向 TypeScript，与 <code>react-spring</code> 同属于 Poimandres 。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmobx.js.org%2FREADME.html" target="_blank" rel="nofollow noopener noreferrer" title="https://mobx.js.org/README.html" ref="nofollow noopener noreferrer">mobx</a> - 遵循观察者模式，适合响应式编程（reactive programming），推荐中小型项目使用。</li>
</ul>
<h2 data-id="heading-3">2. 服务器状态管理</h2>
<p>如果您的应用程序严重依赖某些外部数据源，那么管理该数据（缓存、更新等）对于性能至关重要。</p>
<h3 data-id="heading-4">推荐</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-query.tanstack.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react-query.tanstack.com/" ref="nofollow noopener noreferrer">react-query</a> - 适用于 <code>react hooks</code> 的请求库。</li>
</ul>
<p>React Query 将帮助你获取、同步、更新和缓存你的远程数据， 提供两个简单的 hooks，就能完成增删改查等操作。</p>
<p>它处理 <code>caching</code> 陈旧的数据，以及更多开箱即用的东西，它简单、强大且可配置。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm i react-query --save
<span class="hljs-comment"># or</span>
$ yarn add react-query
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本功能概览：</p>
<ol>
<li>
<p>传输/协议/后端不可知的数据获取（REST、GraphQL、promise等等）；</p>
</li>
<li>
<p>自动缓存+重新取回（过期时重新验证，窗口重新聚焦，轮询/实时）；</p>
</li>
<li>
<p>并行 + 依赖查询；</p>
</li>
<li>
<p>突变 + 反应式查询重取；</p>
</li>
<li>
<p>多层缓存 + 自动垃圾收集；</p>
</li>
<li>
<p>分页 + 基于游标的查询；</p>
</li>
<li>
<p>加载更多 + 无限滚动查询/滚动恢复；</p>
</li>
<li>
<p>请求取消；</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Fconcurrent-mode-suspense.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/concurrent-mode-suspense.html" ref="nofollow noopener noreferrer">React Suspense</a> + Fetch-As-You-Render 查询预取；</p>
</li>
<li>
<p>专用的 Devtools。</p>
</li>
</ol>
<p>简单示例（全局配置）：</p>
<pre><code class="hljs language-react copyable" lang="react">// main.js
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

import &#123; QueryClient, QueryClientProvider &#125; from 'react-query'

const queryClient = new QueryClient()

ReactDOM.render(
  <React.StrictMode>
    <QueryClientProvider client=&#123;queryClient&#125;>
      <App />
    </QueryClientProvider>
  </React.StrictMode>
  document.getElementById('root')
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-react copyable" lang="react">// QueryExample.jsx
import React from 'react'
import &#123; useQuery &#125; from 'react-query'
import &#123; ReactQueryDevtools &#125; from 'react-query/devtools'

function QueryExample() &#123;
  const &#123; isLoading, error, data, isFetching &#125; = useQuery('repoData', () =>
    fetch('https://api.github.com/repos/tannerlinsley/react-query').then((res) => res.json())
  )

  if (isLoading) return 'Loading...'

  if (error) return 'An error has occurred: ' + error.message

  return (
    <div>
      <h1>&#123;data.name&#125;</h1>
      <p>&#123;data.description&#125;</p>
      <strong>👀 &#123;data.subscribers_count&#125;</strong> <strong>✨ &#123;data.stargazers_count&#125;</strong> <strong>🍴 &#123;data.forks_count&#125;</strong>
      <div>&#123;isFetching ? 'Updating...' : ''&#125;</div>
      <ReactQueryDevtools initialIsOpen /> 
    </div>
  )
&#125;
export default QueryExample
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">备选方案</h3>
<p>还有一个类似于 React Query 的库。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fswr.vercel.app%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://swr.vercel.app/" ref="nofollow noopener noreferrer">swr</a></li>
</ul>
<p>“SWR” 这个名字来自于 <code>stale-while-revalidate</code>：一种由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc5861" target="_blank" rel="nofollow noopener noreferrer" title="https://tools.ietf.org/html/rfc5861" ref="nofollow noopener noreferrer">HTTP RFC 5861</a> 推广的 HTTP 缓存失效策略。这种策略首先从缓存中返回数据（过期的），同时发送 fetch 请求（重新验证），最后得到最新数据。</p>
<p>这个库的主要好处是它由 Vercel 构建的，他们是创建 Next.js 的人。因此，在使用 Next.js 时，您可以期待更好的性能。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm i swr --save
<span class="hljs-comment"># or</span>
$ yarn add swr
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SWR 涵盖了性能正确性和稳定性的各个方面，以帮你建立更好的体验：</p>
<ul>
<li>快速页面导航</li>
<li>间隔轮询</li>
<li>数据依赖</li>
<li>聚焦时重新验证</li>
<li>网络恢复时重新验证</li>
<li>本地缓存更新 (Optimistic UI)</li>
<li>智能错误重试</li>
<li>分页和滚动位置恢复</li>
<li>React Suspense</li>
<li>...</li>
</ul>
<h2 data-id="heading-6">3. 脚手架</h2>
<p>从头开始创建 React 应用程序很复杂，设置 webpack、babel 等会让人望而生畏。</p>
<h3 data-id="heading-7">推荐</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fcreate-react-app" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/create-react-app" ref="nofollow noopener noreferrer">create-react-app</a> - 官方脚手架工具。</li>
</ul>
<p>它将 webpack 和 babel 封装在一起，组成一个新的脚本工具 react-scripts 来管理整个应用。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 创建 React 项目</span>
$ npx create-react-app my-app
<span class="hljs-comment"># or</span>
$ npm init react-app my-app
<span class="hljs-comment"># or </span>
$ yarn create react-app my-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b59ca044ffd4ac7b515d9bbf2524eab~tplv-k3u1fbpfcp-watermark.image" alt="Easy to get started in seconds" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite" ref="nofollow noopener noreferrer">vite</a> - 使用原生 ESM 文件，无需打包，下一代前端开发与构建工具。</li>
</ul>
<p><strong>Vite 充分利用了「操作系统的原生能力」，缩短了链路，省去了繁杂的打包步骤，规避了很多在在构建上时的性能问题，Vite具有「跨时代」的意义。</strong></p>
<p>目前来看，虽然 Vite 生态没有 Webpack 繁荣，但随着时间的推移， Vite 必将会替代 Webpack。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 创建 react 项目</span>
<span class="hljs-comment"># npm 6.x</span>
$ npm init vite@latest my-react-app --template react 

<span class="hljs-comment"># npm 7+, 需要额外的双横线：</span>
$ npm init vite@latest my-react-app -- --template react

<span class="hljs-comment"># yarn</span>
$ yarn create vite my-react-app --template react
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/next.js" ref="nofollow noopener noreferrer">next.js</a> - 构建 React 应用的框架。</li>
</ul>
<p><strong>Next.js</strong> 开箱即用，提供服务器端渲染、静态站点生成、无服务器功能等等。</p>
<p>它是一个工具箱，最重要的功能是开箱即用的 SEO 支持，为您提供创建高性能 web 应用程序所需的一切。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 创建 next.js 程序</span>
$ npx create-next-app my-next-app
<span class="hljs-comment"># or</span>
$ yarn create next-app my-next-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Next.js 是围绕着 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.nextjs.cn%2Fdocs%2Fbasic-features%2Fpages" target="_blank" rel="nofollow noopener noreferrer" title="https://www.nextjs.cn/docs/basic-features/pages" ref="nofollow noopener noreferrer">页面（pages）</a> 的概念构造的。一个页面（page）就是一个从 <code>pages</code> 目录下的 <code>.js</code>、<code>.jsx</code>、<code>.ts</code> 或 <code>.tsx</code> 文件导出的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Fcomponents-and-props.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/components-and-props.html" ref="nofollow noopener noreferrer">React 组件</a>。</p>
<p>页面（page） 根据其文件名与路由关联。例如，<code>pages/about.js</code> 被映射到 <code>/about</code>。甚至可以在文件名中添加动态路由参数。</p>
<h3 data-id="heading-8">备选方案</h3>
<p>如果您开始使用 React 构建一些基本项目，那么您还有其他选择。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.gatsbyjs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.gatsbyjs.org/" ref="nofollow noopener noreferrer">gatsby</a> - 构建面向内容的静态网站，不适用于其他项目。</li>
</ul>
<h2 data-id="heading-9">4. UI 组件库</h2>
<p>一套通用完善的 UI 库不仅能帮助我们解决重复的应用场景，也能节省开发成本，经社区锤炼后的库性能也有所保障。</p>
<h3 data-id="heading-10">推荐</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fant.design%2Findex-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://ant.design/index-cn" ref="nofollow noopener noreferrer">antd</a> - 文档全面，成熟的设计体系，生态丰富，国人首选。</li>
</ul>
<p>antd 是基于 Ant Design 设计体系的 React UI 组件库，主要用于研发企业级中后台产品。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ yarn add antd
<span class="hljs-comment"># or</span>
$ npm i antd --save

<span class="hljs-comment"># 基于 Umi 搭建项目</span>
$ yarn create @umijs/umi-app
<span class="hljs-comment"># or </span>
$ npx @umijs/create-umi-app
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpalantir%2Fblueprint" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/palantir/blueprint" ref="nofollow noopener noreferrer">blueprint</a> - 一个基于 React 的 Web UI 工具包。</li>
</ul>
<p>Blueprint 基于 TypeScript 和 Scss 开发，功能强大，并且有自己的色彩和排版规范，推荐使用。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d58be801778e45b6bfc4a4a4ba0bf657~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>它是一个模块化组件库，分为多个包（可以单独安装）：</p>
<ol>
<li><code>core</code> - 30+ 组件，300多个 icons。</li>
<li><code>datetime</code> - 关于日期和时间的 6 个组件。</li>
<li><code>icons</code> - 300+ 图标，支持 svg 和 fonts 两种格式。</li>
<li><code>select</code> - 下拉选择相关的 6 个组件。</li>
<li><code>table</code> - 高度交互的表格组件（个人感觉性能不咋地）。</li>
<li><code>timezone</code> - 处理时区相关的组件。</li>
<li><code>popover</code>- 强大的弹出框组件，基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpopper.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://popper.js.org/" ref="nofollow noopener noreferrer"><strong>Popper.js</strong></a> 。</li>
<li><code>tooltip</code> - 由 <code>popover</code> 提供。</li>
<li><code>contextMenu2</code> - 由 <code>popover</code> 提供。</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ yarn add @blueprintjs/core 
<span class="hljs-comment"># 使用 datetime</span>
$ yarn add @blueprintjs/datetime
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Blueprint 支持 Chrome、Firefox、Safari、IE 11 和 Microsoft Edge。</strong></p>
<p>Blueprint 在其公共 API 中严格遵守 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsemver.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://semver.org/" ref="nofollow noopener noreferrer">semver</a>：</p>
<ul>
<li>从 <code>blueprint</code> 的 <code>root/main</code> 模块导出的 JS API；</li>
<li>组件的 HTML 结构；</li>
<li>渲染组件的 CSS 样式；</li>
</ul>
<h3 data-id="heading-11">备选方案</h3>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmaterial-ui.com%2Fzh%2Fgetting-started%2Finstallation%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://material-ui.com/zh/getting-started/installation/" ref="nofollow noopener noreferrer">Material UI</a> - Google‘s Material Design 风格，定制相对困难。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fmaterial-ui.com" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fmaterial-ui.com" ref="nofollow noopener noreferrer">Semantic UI</a> - 语义化、代码可读性与可理解性很强，与 bootstrap 风格接近。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freact-bootstrap%2Freact-bootstrap%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/react-bootstrap/react-bootstrap/" ref="nofollow noopener noreferrer">React Bootstrap</a> -  用 React 构建的 Bootstrap 组件。</p>
</li>
</ul>
<h2 data-id="heading-12">5. 表单处理</h2>
<p>90% 的 Web 应用程序都有这种情形 - 处理表单输入是一个很大的痛苦。但我们有一些好的方案。</p>
<h3 data-id="heading-13">推荐</h3>
<p>React Hook Form 是用于处理表单最新最好的库（个人认为），它非常高效且灵活。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-hook-form.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react-hook-form.com/" ref="nofollow noopener noreferrer">react-hook-form</a></li>
</ul>
<p>它对一些外部设计库有很好的支持，比如 <code>material-ui</code> 和 <code>ant-design</code>。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm i react-hook-form --save
<span class="hljs-comment"># or</span>
$ yarn add react-hook-form
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="hljs language-react copyable" lang="react">import React from 'react'
import &#123; useForm &#125; from 'react-hook-form'

export default function HookForm() &#123;
  const &#123;
    register,
    handleSubmit,
    watch,
    formState: &#123; errors &#125;,
  &#125; = useForm()
  const onSubmit = (data) => console.log(data)

  // 通过 watch 可以监听 inupt 的变化
  console.log(watch('username')) 
  return (
    // handleSubmit 会在调用 onSubmit 之前验证用户输入
    <form onSubmit=&#123;handleSubmit(onSubmit)&#125;>
      &#123;/*通过 register 函数将输入注册到钩子中 */&#125;
      <input defaultValue="test" &#123;...register('username')&#125; />
      
      &#123;/* 通过 register 可以配置验证规则 */&#125;
      <input &#123;...register('password', &#123; required: true &#125;)&#125; />
      
      &#123;/* 验证规则不通过时，将会显示如下内容  */&#125;
      &#123;errors.exampleRequired && <span>This field is required</span>&#125;
      <input type="submit" />
    </form>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">备选方案</h3>
<p>这个领域有一些很好的选择。</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fformik.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://formik.org/" ref="nofollow noopener noreferrer">formik</a> - Formik 为输入验证、格式化、屏蔽、数组和错误处理提供了久经考验的解决方案。</p>
</li>
<li>
<p><em>redux-form - 不建议使用 ，它真的会损害性能。</em></p>
</li>
</ul>
<h2 data-id="heading-15">6. HTTP 调用</h2>
<p>在现代世界中，几乎所有网站都依赖于一些外部数据源，所以进行 HTTP 调用非常简单。</p>
<h3 data-id="heading-16">推荐</h3>
<p>Axios 是进行 HTTP 调用的推荐方式。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faxios%2Faxios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/axios/axios" ref="nofollow noopener noreferrer">axios</a> - 一个基于Promise 用于浏览器和 nodejs 的 HTTP 客户端。</li>
</ul>
<p>Axios 具有如下特征：</p>
<ol>
<li>
<p>从浏览器中创建 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest" ref="nofollow noopener noreferrer">XMLHttpRequest</a>；</p>
</li>
<li>
<p>从 node.js 发出 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.org%2Fapi%2Fhttp.html" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.org/api/http.html" ref="nofollow noopener noreferrer">http</a> 请求；</p>
</li>
<li>
<p>支持 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise" ref="nofollow noopener noreferrer">Promise</a> API；</p>
</li>
<li>
<p>拦截请求和响应；</p>
</li>
<li>
<p>转换请求和响应数据；</p>
</li>
<li>
<p>取消请求；</p>
</li>
<li>
<p>自动转换 JSON 数据；</p>
</li>
<li>
<p>客户端支持防止 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCross-site_request_forgery" target="_blank" rel="nofollow noopener noreferrer" title="http://en.wikipedia.org/wiki/Cross-site_request_forgery" ref="nofollow noopener noreferrer">CSRF/XSRF</a>。</p>
</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm i axios --save
<span class="hljs-comment"># or </span>
$ yarn add axios
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// axios</span>
axios.get(url)
  .then(<span class="hljs-function">(<span class="hljs-params">response</span>) =></span> <span class="hljs-built_in">console</span>.log(response))
  .catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> <span class="hljs-built_in">console</span>.log(error))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">备选方案</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFetch_API" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API" ref="nofollow noopener noreferrer">Fetch</a> - 浏览器原生 API，有别与 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest" ref="nofollow noopener noreferrer">xhr</a>。</li>
</ul>
<p>小型项目的情况下，只需要几个简单的 API 调用，Fetch 是一个不错的解决方案。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// fetch</span>
fetch(url)
  .then(<span class="hljs-function">(<span class="hljs-params">response</span>) =></span> response.json())
  .then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> <span class="hljs-built_in">console</span>.log(data))
  .catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> <span class="hljs-built_in">console</span>.log(error))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">7. 样式</h2>
<p>你将需要样式，这是毫无疑问的，有多种方法可以设置应用程序的样式。</p>
<h3 data-id="heading-19">推荐</h3>
<p>许多人可能不同意我的看法，但我认为 Styled Components 是 React 应用程序中样式化的最佳选择方案。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstyled-components.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://styled-components.com/" ref="nofollow noopener noreferrer">styled-components</a></li>
</ul>
<p>Styled Components 是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fspeakerdeck.com%2Fvjeux%2Freact-css-in-js" target="_blank" rel="nofollow noopener noreferrer" title="https://speakerdeck.com/vjeux/react-css-in-js" ref="nofollow noopener noreferrer"><strong>CSS in JS</strong></a> 一种实现方式，其他实现方式还有：<a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer">radium</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcssinjs%2Fjss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cssinjs/jss" ref="nofollow noopener noreferrer">react-jss</a> 等。</p>
<p>它有助于创建具有明确关注点分离的干净组件，此外，它可以通过 props 轻松管理和配置。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm i styled-components --save
<span class="hljs-comment"># or</span>
$ yarn add styled-components 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="hljs language-react copyable" lang="react">import React from "react";
import styled from "styled-components";

const Container = styled.div`
padding: 12px;
background: red;
&:hover &#123;
background: blue;
&#125;
`
const Homepage = () => &#123;
  return (
  <Container>
    <h1>Welcome to React<h1>
    </Container>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">备选方案</h3>
<p>但是，正如我所说，还有其他很棒的选择！</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FStyle%2FCSS%2FOverview.en.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/Style/CSS/Overview.en.html" ref="nofollow noopener noreferrer">Cascading Style Sheets (CSS) </a> - W3C 标准，对于较小的项目应该没问题。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsass-lang.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://sass-lang.com/" ref="nofollow noopener noreferrer">sass</a> - CSS 预处理，它为管理 CSS 提供了很好的功能，使用于中型甚至更大的项目。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fstyled-jsx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/styled-jsx" ref="nofollow noopener noreferrer">styled-jsx</a> - 与 <code>styled-compomnents</code> 功能很相似的库。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FFormidableLabs%2Fradium" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/FormidableLabs/radium" ref="nofollow noopener noreferrer">radium</a> -  CSS in JS 的一种实现。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcssinjs%2Fjss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cssinjs/jss" ref="nofollow noopener noreferrer">react-jss</a> -  CSS in JS 的一种实现。</li>
</ul>
<h2 data-id="heading-21">8. 文档</h2>
<p>好的文档可以在未来节省 100 多个小时，因此，在项目的早期就积极主动的采用文档库。</p>
<h3 data-id="heading-22">推荐</h3>
<p>推荐创建文档的方式是 <code>react-styleguidist</code>。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-styleguidist.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react-styleguidist.js.org/" ref="nofollow noopener noreferrer">react-styleguidist</a></li>
</ul>
<p>React Styleguidist 基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactjs%2Freact-docgen" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactjs/react-docgen" ref="nofollow noopener noreferrer">react-docgen</a> ，可以帮助 react 项目快速构建项目文档的库。</p>
<p>其原理是使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactjs%2Freact-docgen" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactjs/react-docgen" ref="nofollow noopener noreferrer">react-docgen</a> 来解析源文件（未转译）。react-docgen 查找导出的 React 组件并根据 PropTypes 或 Flow 注释生成文档。</p>
<p>React Styleguidist 使用 <strong>Markdown</strong> 文档：每个 JavaScript 代码块都被渲染为带有 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsatya164%2Freact-simple-code-editor" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/satya164/react-simple-code-editor" ref="nofollow noopener noreferrer">react-simple-code-editor</a> 的交互式演示（使用 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fremark.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://remark.js.org/" ref="nofollow noopener noreferrer">Remark</a> 提取所有这些代码块）。</p>
<p>Webpack loaders 生成包含所有用户组件、文档和示例的 JavaScript 模块，并将其传递给 React 应用程序，该应用程序渲染样式指南。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 （node >= 14.0.0）</span>
npm install react-styleguidist --save-dev
yarn add react-styleguidist --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用 React Styleguidist 时，需要在项目根目录下建立 <code>styleguide.config.js</code> 文件，基本配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// styleguide.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">title</span>: <span class="hljs-string">'React Style Guide Example'</span>,
  <span class="hljs-attr">defaultExample</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">webpackConfig</span>: &#123;
    <span class="hljs-attr">module</span>: &#123;
      <span class="hljs-attr">rules</span>: [
        &#123;
          <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jsx?$/</span>,
          exclude: <span class="hljs-regexp">/node_modules/</span>,
          loader: <span class="hljs-string">'babel-loader'</span>,
        &#125;,
        ...
      ],
    &#125;,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用的是 <strong>vite2</strong> 构建的 React 项目，则需要手动安装 <strong>babel</strong> 相关依赖：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># babel 7</span>
$ yarn add babel-loader @babel/core @babel/preset-env babel/preset-react --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后添加 <strong>babel</strong> 配置 <code>.babelrl</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// .babelrc</span>
&#123;
<span class="hljs-attr">"presets"</span>: [
<span class="hljs-string">"@babel/preset-env"</span>,
<span class="hljs-string">"@babel/preset-react"</span>
]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，React Styleguidist 搜索组件的位置使用的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fisaacs%2Fnode-glob%23glob-primer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/isaacs/node-glob#glob-primer" ref="nofollow noopener noreferrer">glob模式</a>：<code>src/components/**/*.&#123;js,jsx,ts,tsx&#125;</code>，也就是说位于这个路径下的组件才会生成文档。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f006ea81e7e48b1b77a7dd9a69fce64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是 React Styleguidist 的文档界面（编写文档需要提供与组建同名的 <code>.md</code> 文件） 。</p>
<h3 data-id="heading-23">备选方案</h3>
<p>还有一些其他选择。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjsdoc.app%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://jsdoc.app/index.html" ref="nofollow noopener noreferrer">js-docs</a> - JavaScript 的通用文档工具。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.docz.site%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.docz.site/" ref="nofollow noopener noreferrer">react-docz</a> - 非常易于使用的文档指南，值得一试。</li>
</ul>
<h2 data-id="heading-24">9. 多语言支持</h2>
<p>如果您正在全球范围内构建产品，那么您可能希望在 React 应用程序中添加多语言支持。</p>
<h3 data-id="heading-25">推荐</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact.i18next.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react.i18next.com/" ref="nofollow noopener noreferrer">react-i18next</a></li>
</ul>
<p>支持 React 应用程序国际化，使用 i18next、i18n 生态系统。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fi18next.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://i18next.com/" ref="nofollow noopener noreferrer">i18next</a></li>
</ul>
<h3 data-id="heading-26">备选方案</h3>
<p>还有其他一些不错的选择。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Freact-intl" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/react-intl" ref="nofollow noopener noreferrer">react-intl</a></li>
</ul>
<p>它也支持其他框架，如 VueJS 和 Angular。</p>
<h2 data-id="heading-27">10. 动画</h2>
<p>动画使您的应用程序栩栩如生。在 React 中使用动画有一些不错的选择。</p>
<h3 data-id="heading-28">推荐</h3>
<p>纯 CSS 是制作 React 应用程序动画的最佳方式，它简单快捷，性能也有保障。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3schools.com%2Fcss%2Fcss3_animations.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3schools.com/css/css3_animations.asp" ref="nofollow noopener noreferrer">CSS Animations</a> - W3C 标准的 CSS 动画。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [name, setName] = useState(<span class="hljs-string">''</span>)
...
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;[</span>'<span class="hljs-attr">example</span>', <span class="hljs-attr">name</span>]<span class="hljs-attr">.join</span>(' ')&#125;></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setName('example-animation')&#125;>点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.example</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">background-color</span>: red;
  <span class="hljs-attribute">animation-duration</span>: <span class="hljs-number">4s</span>;
&#125;

<span class="hljs-selector-class">.example-animation</span> &#123;
  <span class="hljs-attribute">animation-name</span>: example;
&#125;

<span class="hljs-keyword">@keyframes</span> example &#123;
  <span class="hljs-number">0%</span>   &#123;<span class="hljs-attribute">background-color</span>: red;&#125;
  <span class="hljs-number">25%</span>  &#123;<span class="hljs-attribute">background-color</span>: yellow;&#125;
  <span class="hljs-number">50%</span>  &#123;<span class="hljs-attribute">background-color</span>: blue;&#125;
  <span class="hljs-number">100%</span> &#123;<span class="hljs-attribute">background-color</span>: green;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56d394ad4f634fb6be62d8df54594632~tplv-k3u1fbpfcp-watermark.image" alt="794236914-61250337e4b7c.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-29">备选方案</h3>
<p>如果您想要现成的东西。那么这里有一些建议给您。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchenglou%2Freact-motion" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chenglou/react-motion" ref="nofollow noopener noreferrer">react-motion</a> - 官方推荐库之一，跨平台， 作者是 FB 大神 Cheng Lou。</li>
</ul>
<p>该库融合了一些物理学的东西，还为 React 的 <code>TransitionGroup</code> （V2 之前的版本）提供了一些更强大的 API。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-spring.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react-spring.io/" ref="nofollow noopener noreferrer">react-spring</a> - 官方推荐库之一。</li>
</ul>
<p>基于弹簧物理学的动画库，基本上能满足大多数与 UI 相关的动画需求。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactjs%2Freact-transition-group" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactjs/react-transition-group" ref="nofollow noopener noreferrer">react-transition-group</a> - 官方推荐库之一。</li>
</ul>
<p>一组组件，用于随时间管理组件状态（包括装载和卸载），专门针对动画设计。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.framer.com%2Fmotion%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.framer.com/motion/" ref="nofollow noopener noreferrer">framer-motion</a> - 生产就绪动画、手势库。</li>
</ul>
<h2 data-id="heading-30">11. 长列表渲染</h2>
<p>渲染一个长列表会严重影响应用程序的性能，在这种情况下使用库可能是一个好主意。</p>
<h3 data-id="heading-31">推荐</h3>
<p>如果你有某种无限滚动的应用程序， 那么你应该考虑 <strong>React Window</strong>。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-window.vercel.app%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://react-window.vercel.app/" ref="nofollow noopener noreferrer">react-window</a> -  antd 虚拟列表的解决方案。</li>
</ul>
<p><code>react-window</code>是是更轻量级的 <code> react-virtualized</code>， 同出一个作者（React 核心团队成员）。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm install react-window --save
<span class="hljs-comment"># or</span>
$ yarn add react-window
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">备选方案</h3>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbvaughn%2Freact-virtualized" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/bvaughn/react-virtualized" ref="nofollow noopener noreferrer">react-virtualized</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Freact-paginate" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/react-paginate" ref="nofollow noopener noreferrer">react-paginate</a> - 如果您不需要无限滚动列表，那么您可以对数据进行分页。</p>
</li>
</ul>
<h2 data-id="heading-33">12. 代码质量工具</h2>
<p>Linters 可以静态地发现代码中的任何错误，使用某种 linter 是个好主意。</p>
<h3 data-id="heading-34">推荐</h3>
<p>首选解决方案是 <strong>Eslint</strong>。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.org/" ref="nofollow noopener noreferrer">eslint</a></li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 （ Node.js (^10.12.0, or >=12.0.0) ）</span>
$ npm install eslint --save-dev
<span class="hljs-comment"># or</span>
$ yarn add eslint --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Eslint 需要进行配置，通过 <code>eslint --init</code> 可以在项目根目录下自动生成配置文件 <code>eslintrc.js</code>。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npx eslint --init
<span class="hljs-comment"># or </span>
$ yarn run eslint --init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Eslint 配置文件支持多种格式，优先级顺序如下：</p>
<ol>
<li><code>.eslintrc.js</code></li>
<li><code>.eslintrc.cjs</code></li>
<li><code>.eslintrc.yaml</code></li>
<li><code>.eslintrc.yml</code></li>
<li><code>.eslintrc.json</code></li>
<li><code>package.json</code></li>
</ol>
<h3 data-id="heading-35">备选方案</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjshint.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jshint.com/" ref="nofollow noopener noreferrer">jshint</a> - 比较旧的库。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpalantir.github.io%2Ftslint%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://palantir.github.io/tslint/" ref="nofollow noopener noreferrer">tslint</a> - TypeScript 的 linter，现在不推荐。</li>
</ul>
<h2 data-id="heading-36">13. 格式化</h2>
<p>具有一致的视觉样式对于任何应用程序都非常重要，代码格式化程序可以为您完成这项工作！</p>
<h3 data-id="heading-37">推荐</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fprettier.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://prettier.io/" ref="nofollow noopener noreferrer">prettier</a></li>
</ul>
<p>这对您来说是最好的解决方案，您不需要其他任何东西！</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 prettier</span>
$ npm install prettier --save-dev --save-exact 
<span class="hljs-comment"># or </span>
$ yarn add prettier --dev --exact
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Prettier 时需要提供配置文件，<code>prettier</code> 遵循 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdavidtheclark%2Fcosmiconfig" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/davidtheclark/cosmiconfig" ref="nofollow noopener noreferrer">cosmiconfig</a> ，所以您可以通过（按优先顺序）进行配置配置。</p>
<ul>
<li>在 <code>package.json</code> 中，提供 <code>prettier</code> 字段。</li>
<li>可以是一个 <code>.prettierrc</code>文件，使用  JSON 或 YAML 格式编写。</li>
<li>也可以是<code>.prettierrc.json</code>，<code>.prettierrc.yml</code>，<code>.prettierrc.yaml</code>，或<code>.prettierrc.json5</code>文件。</li>
<li>还可以使用 <code>.prettierrc.js</code>、<code>.prettierrc.cjs</code>、<code>prettier.config.js</code> 或 <code>prettier.config.cjs</code> 通过 <code>module.exports</code> 导出。</li>
<li>一个<code>.prettierrc.toml</code>文件。</li>
</ul>
<p>例如通过使用 <code>.prettierrc</code> 文件进行配置：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"trailingComma"</span>: <span class="hljs-string">"es5"</span>,
  <span class="hljs-attr">"tabWidth"</span>: <span class="hljs-number">4</span>,
  <span class="hljs-attr">"semi"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"singleQuote"</span>: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后可以通过命令行指令对所有文件进行格式化操作。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npx prettier --write .
<span class="hljs-comment"># or </span>
$ yarn prettier --write .
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Prettier 还可以与编辑器进行集成，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fprettier.io%2Fdocs%2Fen%2Feditors.html" target="_blank" rel="nofollow noopener noreferrer" title="https://prettier.io/docs/en/editors.html" ref="nofollow noopener noreferrer">详见</a> 。</p>
<h2 data-id="heading-38">14. 分析</h2>
<p>数据分析就是未来，今天的大多数企业都是数据驱动的，因此，为您的应用程序拥有一个好的分析工具非常重要！</p>
<h3 data-id="heading-39">推荐</h3>
<p>最流行和最强大的工具是 <strong>React Ga</strong>。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freact-ga%2Freact-ga" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/react-ga/react-ga" ref="nofollow noopener noreferrer">react-ga</a></li>
</ul>
<p>我认为您不需要其他任何东西。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm install react-ga --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用 <code>ReactGA.initialize</code> 初始化参数（谷歌分析生成的 id）后，React 项目会自动在 header 中引入 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmarketingplatform.google.com%2Fabout%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://marketingplatform.google.com/about/" ref="nofollow noopener noreferrer">Google Analytics</a> 脚本。</p>
<h2 data-id="heading-40">15. 测试</h2>
<p>我不需要重申测试对于任何应用程序的重要性。所以请往下看！</p>
<h3 data-id="heading-41">推荐</h3>
<p>推荐的是 React Testing Library（也是官方推荐的测试库），是 Airbnb 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fenzymejs.github.io%2Fenzyme%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://enzymejs.github.io/enzyme/" ref="nofollow noopener noreferrer"> Enzyme</a> 测试库的替代方案。</p>
<p><em>React Testing Library 和 Jest 是截然不同的，它是其中一个可以测试 React 组件的库（还有 Enzyme 等）。</em></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftesting-library.com%2Freact" target="_blank" rel="nofollow noopener noreferrer" title="https://testing-library.com/react" ref="nofollow noopener noreferrer">react-testing-library</a></li>
</ul>
<blockquote>
<p>它非常易于使用，并且旨在遵循真实环境中的使用情况。</p>
</blockquote>
<p><strong>React Testing Library 不直接测试组件的实现细节，而是从一个 React 应用的角度去测试。</strong> 更加符合我们对于单元测试的原本诉求，以及最佳实践。</p>
<p>它让您的测试库从长远来看是可维护的，让重构工作变得轻而易举，组件的重构（更改实现但不是功能）不会破坏您的测试。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm install --save-dev @testing-library/react
<span class="hljs-comment"># or</span>
yarn add @testing-library/react --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// hidden-message.js</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-comment">// <span class="hljs-doctag">NOTE:</span> React Testing Library works well with React Hooks and classes.</span>
<span class="hljs-comment">// Your tests will be the same regardless of how you write your components.</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HiddenMessage</span>(<span class="hljs-params">&#123;children&#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [showMessage, setShowMessage] = React.useState(<span class="hljs-literal">false</span>)
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">htmlFor</span>=<span class="hljs-string">"toggle"</span>></span>Show Message<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span>
        <span class="hljs-attr">id</span>=<span class="hljs-string">"toggle"</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span>
        <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;e</span> =></span> setShowMessage(e.target.checked)&#125;
        checked=&#123;showMessage&#125;
      />
      &#123;showMessage ? children : null&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> HiddenMessage
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// __tests__/hidden-message.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@testing-library/jest-dom'</span> <span class="hljs-comment">// jest-dom 更方便的为测试添加断言，建议使用，但不是必需的</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123;render, fireEvent, screen&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@testing-library/react'</span>
<span class="hljs-keyword">import</span> HiddenMessage <span class="hljs-keyword">from</span> <span class="hljs-string">'../hidden-message'</span>

test(<span class="hljs-string">'shows the children when the checkbox is checked'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> testMessage = <span class="hljs-string">'Test Message'</span>
  render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">HiddenMessage</span>></span>&#123;testMessage&#125;<span class="hljs-tag"></<span class="hljs-name">HiddenMessage</span>></span></span>)
  <span class="hljs-comment">//query* 函数将返回元素，如果找不到，则返回 null</span>
  <span class="hljs-comment">//get* 函数将返回元素，如果找不到，则抛出错误</span>
         
  expect(screen.queryByText(testMessage)).toBeNull()
  <span class="hljs-comment">//查询可以接受正则表达式，使选择器对内容调整和更改更具弹性</span>
  fireEvent.click(screen.getByLabelText(<span class="hljs-regexp">/show/i</span>))

  <span class="hljs-comment">// .toBeInTheDocument() 是一个来着jest-dom 的断言</span>
  <span class="hljs-comment">// 还可以使用 .toBeDefined()</span>
  expect(screen.getByText(testMessage)).toBeInTheDocument()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjestjs.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jestjs.io/" ref="nofollow noopener noreferrer">jest</a> - 最受欢迎的 JS 测试框架。</li>
</ul>
<p>Jest 是 Facebook 推出的老牌测试框架，也是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh-hans.reactjs.org%2Fdocs%2Fcreate-a-new-react-app.html%23create-react-app" target="_blank" rel="nofollow noopener noreferrer" title="https://zh-hans.reactjs.org/docs/create-a-new-react-app.html#create-react-app" ref="nofollow noopener noreferrer"> create-react-app</a> 默认安装的测试库。</p>
<p>Jest 和 React Testing Library 的职责是不同的，React Testing Library 是跟 react 打交道，Jest 是跟测试用例打交道。</p>
<p>Jest 给予我们运行测试的能力，除此之外，Jest 还提供了一系列 API，例如 test suites、test cases、assertions，当然 Jest 提供的还不止这些，还有 spies、mocks、stubs 等等。</p>
<p>如果是使用 CRA 创建的 React 程序，则只需要安装 <code>react-test-renderer</code> 来呈现快照。 快照测试是 Jest 的一部分。 您可以使用测试渲染器快速呈现虚拟 DOM 的可序列化 HTML 输出，而不是呈现整个应用程序的UI。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add react-test-renderer --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">备选方案</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cypress.io" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cypress.io" ref="nofollow noopener noreferrer">cypress</a></li>
</ul>
<p>Cypress 通常被比作 Selenium；然而，Cypress 在根本上和架构上都不同。Cypress 不受与 Selenium 相同的限制。</p>
<p>它能够进行端到端测试、单元测试、集成测试，可以测试在浏览器中运行的任何东西。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装</span>
$ npm install cypress --save-dev
<span class="hljs-comment"># or</span>
$ yarn add cypress --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-43">16. 构建可共享的组件</h2>
<p>如果您在一个大型团队中，那么轻松共享组件可能会成为一个大问题。</p>
<h3 data-id="heading-44">推荐</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstorybook.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://storybook.js.org/" ref="nofollow noopener noreferrer">storybook</a></li>
</ul>
<p>如果您正在寻找最完整的解决方案，Storybook 是您的最佳选择。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ab6c11a980341a3b136082c2b3a2b5c~tplv-k3u1fbpfcp-watermark.image" alt="Storybook welcome screen" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Storybook 是 UI 组件的快速开发环境。它允许你浏览组件库，查看每个组件的不同状态，以及交互式开发和测试组件。StoryBook 可帮助你独立于应用程序开发组件，这也有助于提高组件的可重用性和可测试性。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 storybook</span>
$ npx sb init
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Storybook 需要安装到已经设置了框架的项目中，它不适用于空项目。</strong> 有很多方法可以在给定的框架中引导应用程序，包括：</p>
<ul>
<li>
<p>📦 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fangular.io%2Fcli%2Fnew" target="_blank" rel="nofollow noopener noreferrer" title="https://angular.io/cli/new" ref="nofollow noopener noreferrer">Create an Angular Workspace</a></p>
</li>
<li>
<p>📦 <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Fcreate-a-new-react-app.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/create-a-new-react-app.html" ref="nofollow noopener noreferrer">Create React App</a></p>
</li>
<li>
<p>📦 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/" ref="nofollow noopener noreferrer">Vue CLI</a></p>
</li>
<li>
<p>📦 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fguides.emberjs.com%2Frelease%2Fgetting-started%2Fquick-start%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://guides.emberjs.com/release/getting-started/quick-start/" ref="nofollow noopener noreferrer">Ember CLI</a></p>
</li>
<li>
<p>其他构建工具（如：Vite 等）。</p>
</li>
</ul>
<p>最后，我想现在您对何时选择哪个库有了很好的了解，如果您有任何不同的想法，请留言告诉我。</p>
<p>本文启发于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjavascript.plainenglish.io%2F45-npm-packages-to-solve-16-react-problems-a9ab18946224" target="_blank" rel="nofollow noopener noreferrer" title="https://javascript.plainenglish.io/45-npm-packages-to-solve-16-react-problems-a9ab18946224" ref="nofollow noopener noreferrer">45-npm-packages-to-solve-16-react-problems</a>。</p></div>  
</div>
            