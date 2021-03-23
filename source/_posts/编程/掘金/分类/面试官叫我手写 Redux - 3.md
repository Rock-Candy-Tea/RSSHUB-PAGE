
---
title: '面试官叫我手写 Redux - 3'
categories: 
 - 编程
 - 掘金
 - — 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18cdf89a5e904916bd3ad08e9ef19249~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 00:24:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18cdf89a5e904916bd3ad08e9ef19249~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前篇 <a href="https://juejin.cn/post/6942683673900613663" target="_blank">juejin.cn/post/694268…</a></p>
<hr>
<p>方：上回说到我们在 connect 里让每个 Wrapper 监听 store 的变化，以保证只有 connect 过的组件会在 store 变化时 render</p>
<p>学生：今天讲什么？</p>
<p>方：今天讲如何让组件「只在自己依赖的数据变化时重新 render」。</p>
<p>学生：上次说加 selector 可以搞定</p>
<p>方：没错，不过今天加的代码稍稍有点多</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18cdf89a5e904916bd3ad08e9ef19249~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这样一来，每个组件都可以在 connect 的时候，选择自己在什么数据变化的时候更新了。</p>
<p>学生：原来如此。</p>
<p>方：同样的思路，我们可以给 connect 加上 mapDispatchToProps 参数：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/397c64f1454f4302999126d3c781f418~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>学生：确实。</p>
<p>方：现在看看我们的 redux，还有什么没有封装：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2061b36399e4ae883b7414e66932328~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>学生：你的 appContext.Provider 跟 Redux 的 Provider 还不是完全一致</p>
<p>方：那我们就封装一下：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/741c5384428a43acbffb384eea537998~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后就看起来一样啦：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84cba964093e484ca39ff447e0fd8ca0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>学生：reducer 在哪定义的呢？</p>
<p>方：目前是写死在 redux.js 里的，我们需要让用户传入 reducer，所以我们提供一个 configureStore 给用户，用于传入 reducer 和初始 state：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0990691a0d243c2a062fd0800fc46ce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>configureStore 的用法如下：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1869a1a25b7640ca89153f5dbb8f4633~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>学生：哇，现在跟 Redux 就已经非常像了。</p>
<p>方：是的。我们来总结一下目前我们自己写的 Redux 的思路：</p>
<ol>
<li>提供 configureStore 让用户传入 store.reducer 和 store.state</li>
<li>提供 Provider 让用户划定全局 state 的作用范围</li>
<li>提供 connect 让组件被 Wrapper 接管</li>
<li>让 Wrapper 根据 selector 来获取局部的 state 并传给组件</li>
<li>让 Wrapper 根据 dispatchSelector 来获取对 dispatch 的封装，并传给组件</li>
<li>让 Wrapper 通过 store.subscribe 来监听 state 的变化，一旦自己依赖的 state 变化就强制 render 自己</li>
<li>组件可以从 props 里获取局部 state 以及 dispatch 的封装</li>
<li>组件调用 dispatch 后，会通过 reducer 获取 newState，以替换旧的 state</li>
</ol>
<p>大概就是这些。最终代码：<a href="https://codesandbox.io/s/determined-framework-gvhg1?file=/src/App.js" target="_blank" rel="nofollow noopener noreferrer">determined-framework-gvhg1 - CodeSandbox</a></p>
<p>学生：确实不难，但是面试官问我的时候我怎么想不到呢？</p>
<p>方：自己想不出来就先模仿，模仿多了就能自己想出来了。</p>
<p>学生：好的，谢谢你</p>
<p>本文告一段落，后续预告：</p>
<ol>
<li>Redux 的中间件怎么写？</li>
<li>Redux-thunk 是什么？</li>
<li>Redux-sage 是什么？</li>
<li>dva.js 是什么？</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            