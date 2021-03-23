
---
title: '面试官叫我手写 Redux - 2'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 19:18:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3b055621b1c41d990052c800c967e16~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前篇 <a href="https://juejin.cn/post/6941973271210360845" target="_blank">juejin.cn/post/694197…</a></p>
<p>方：目前，我们需要整理一下我们的代码，把 appContext.js、connect.js 和 createNewState.js 的代码全整合到 redux.js 里来：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3b055621b1c41d990052c800c967e16~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如此一来，App.js 就只用到了两个 API 了：</p>
<pre><code class="copyable">import &#123; appContext, connect &#125; from "./redux";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>学生：接下来做什么呢？</p>
<p>方：优化一下 appContext，来看看它是被如何使用的：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ba5a4bccd4845aa97a3a561b4dede82~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到，appContext 主要是用来初始化 appState 和 setAppState 的。目前我们使用 App 的 state 当做全局 state，其实是有很大的性能问题的</p>
<p>学生：什么问题？</p>
<p>方：我给你演示一下这个 bug，首先，我在三个儿子组件的第一行都添加一个 log</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bab133c5c454f038e76f9231a944533~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后，你注意看控制台里的 log：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5e97b34dda240459cd36f6cdf879a28~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>发现什么问题没有？</p>
<p>学生：有什么问题吗？</p>
<p>方：你没发现有多余的 render 吗？我在「二儿子」里的 UserModifier 调用 dispatch，理论上应该只需要执行「大儿子」函数和「二儿子」函数即可（因为这两个组件的子组件都读取了 user），为什么要执行「幺儿子」函数呢？这属于多余的 render 对吧？</p>
<p>学生：哦，对哦……</p>
<p>方：你知道这意味着什么吗？这意味着我们每次对 state 的微小改动，都会渲染这个 App</p>
<p>学生：因为你调用了 App 的 setAppState 函数对吗？</p>
<p>方：是的，只要调用这个函数（并传给它了一个新的 appState），就必定会触发 App 重新执行，也就必定会导致 App 的所有子组件重新执行，除非给子组件加缓存：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daf106deea974e0389d3b2001ed9da44~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>显然，大部分人不会给每个后代组件都加缓存。</p>
<p>学生：那怎么办？</p>
<p>方：问题出在我们「使用 App 的 state 当做全局 state」，可以考虑将 appState 独立出来，于是我在 redux.js 里声明了一个 store，并将其导出：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2cb75291b5c40b49517d13b298f2a56~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后将 store 传给 context 的 value：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/311f6fc3ea4747a28b26868c61a77ddc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如此一来，就消除了对 App 的 state 的依赖了。</p>
<p>学生：那么所有用到 appState 的地方，就都要改成 store.state 了</p>
<p>方：没错，由于我们上节课让 User 和 UserModifier 组件都从 connect 那里获取 state 和 dispatch，所以我们只需要修改 connect 就行了：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9becb858a7df4178ba83b1cf006052a0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>学生：这样就可以了吗？</p>
<p>方：完全不行，运行页面你会发现「无法修改 user.name」。因为 store.state 的变化并不能触发任何一个组件更新，React 里想要触发组件更新一般需要调用 setState。</p>
<p>学生：这不有回到原点了吗？我们一开始就是用的 setState</p>
<p>方：我们一开始用的是 App 的 setState，这次我们可以使用 Wrapper 的 setState 呀</p>
<p>学生：可是 Wrapper 怎么知道 store.state 变化了呢？</p>
<p>方：Wrapper 可以订阅 store.state 的变化，我们只需要给 store 添加一个 subscribe 接口即可：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aae5ae0dd06243b6885b9eac9c73b35e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后，在 setState 运行完毕后，遍历调用所有 fn 即可：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99cb7e50014e4f2bb8335f44eae484fb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>学生：你就用这么几行代码就实现了一个发布订阅？</p>
<p>方：没错，只不过实现得比较简陋而已。接下来我们需要在 Wrapper 里面监听 store.state 的变化：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d30f42aa812c48f39fc9d98043312c20~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>学生：state 变化了就重新渲染 Wrapper？</p>
<p>方：对，但问题是如何重新渲染 Wrapper？函数组件并没有提供 forceUpdate 接口哦。这里我们要使用一个小技巧：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c5515bc69f24036a722d7441679402d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>26 行的 update(&#123;&#125;) 就相当于 forceUpdate()</p>
<p>学生：你利用了 <code>&#123;&#125; !== &#123;&#125;</code> 这一特性！</p>
<p>方：聪明，用 Symbol() 也能达到相同的效果。接下来看看我们的优化成果：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aecb975754184961ac04f5a3c50e9a0a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>看到没，修改 user.name 时，三个儿子组件全都没有重新执行，只有 User 和 UserModifier 重新执行了。</p>
<p>学生：那也就是说，每次修改 state，只有被 connect 过的组件会重新渲染？</p>
<p>方：对。</p>
<p>学生：诶？那我又有一个问题了，如果一个组件被 connect 过，但是它没有使用 user.name 也会在 user.name 被更新时重新渲染吗？</p>
<p>方：目前是</p>
<p>学生：能优化吗？</p>
<p>方：这还不简单吗？每个 Wrapper 对比一下自己依赖的值是否改变了（用 ref 来存储上一次的值），没变就不要 update(&#123;&#125;) 呗……</p>
<p>学生：那每个 Wrapper 怎么知道自己依赖的值是 state.user 还是 state.group 呢？</p>
<p>方：让 connect 接受一个 selector 即可，如果依赖 user，就给 connect 传一个 <code>state => (&#123;user: state.user&#125;)</code>；如果依赖 group，就传 <code>state => (&#123;group: state.group&#125;)</code></p>
<p>学生：原来 redux 的 connect 的第一个参数 mapStateToProps是干这个的啊</p>
<p>方：嗯，目前的代码先给你看看 <a href="https://codesandbox.io/s/damp-wave-1ufwd?file=/src/redux.js" target="_blank" rel="nofollow noopener noreferrer">damp-wave-1ufwd - CodeSandbox</a> ，具体怎么实现 selector 下节课再讲</p>
<p>学生：好的！</p>
<p>待续……</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            