
---
title: 'React状态管理的一些思考（上篇）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7122'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 03:03:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=7122'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>众所周知，react可以抽象为一个函数： <code>UI = render(data)</code> 。这意味着我们可以专注于构建data，而不用考虑如何更新视图。
但随着SPA(single page application)单页面应用复杂度的提高，状态也会变大，管理状态的难度也会增加。
为了更好的管理应用的状态，或许会考虑状态使用react状态管理的库，但是该考虑和如何选择？</p>
<h1 data-id="heading-0">状态</h1>
<p>首先我们要知道什么是状态，举个例子：当我们和我们的应用交互的时候，比如我们点击了一个button，会弹一个对话框，或者UI会有变化，或者发送一个请求。
随着点击事件，我们的应用有对应的响应。可以肯定的是这个时刻的 <strong>状态</strong> 跟点击之前的不一样了，我们应用进入了一个新的状态。比如说标志是否打开弹窗的变量、AJAX请求的数据，这些变量我们都可以称之为状态。
广泛的讲，应用的状态就是这些变量。它可以是React中使用useState(函数组件)或者this.state(类组件)保存的数据，也可以保存第三方状态管理库里。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcdc.tencent.com%2F2020%2F05%2F22%2Ffrontend-state-management-research%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cdc.tencent.com/2020/05/22/frontend-state-management-research/" ref="nofollow noopener noreferrer">前端状态管理设计——优雅与妥协的艺术</a> 。</p>
</blockquote>
<h1 data-id="heading-1">抉择</h1>
<p>在React中如果我们需要储存状态，我们一般会选择以下三种途径方式：</p>
<ul>
<li>
<p>储存在当前组件里面，函数组件里面可以使用useState、useReducer这些hooks，类组件可以存在this.state里面。</p>
</li>
<li>
<p>储存在第三状态管理库的仓库(store)里，相关的库有：Redux、MobX、Recoil....</p>
</li>
<li>
<p>自己维护状态，例如我们可以直接存在window里。。。</p>
</li>
</ul>
<p>相应的如果改变状态，我们可以：</p>
<ul>
<li>
<p>当我们调用useState、useReducer、this.setState的时候，React将会自动重新渲染，这是React提供给我们的机制。</p>
</li>
<li>
<p>如果我们使用第三方库，例如Redux、MobX、Recoil等。。。他们会在适当的时机，然后调用Ract的API触发重新渲染。</p>
</li>
<li>
<p>如果自己维护了数据，例如保存在window里，就需要自己实现状态改变触发重新渲染的逻辑，但是不建议。 <strong>其实react并不在意你把数据放在哪，react处理的只是data -> UI的映射。</strong></p>
</li>
</ul>
<p><strong>在绝大多数情况下，我们使用React提供的组件级别的状态管理API就完全足够了。</strong></p>
<h2 data-id="heading-2">简单状态共享场景</h2>
<p>但是其实如果我们只用React提供的API，我们常常会遇到以下状态共享问题：</p>
<ol>
<li>
<p>prop drilling问题，即props传递的层级过深，我们需要手动传递props，比较麻烦。</p>
</li>
<li>
<p>树上距离较远的两个组件需要共享状态，在react中一个做法是，提取props到他们相邻最近的祖先节点中，回到第一种情况。</p>
</li>
<li>
<p>子组件向父组件传递数据，只能通过回调的方式。</p>
</li>
</ol>
<p>造成这些问题的根本原因还是React的 <strong>单向数据流</strong> 的设计思想，React恨不得把所有状态都保存在顶层。
当然单向数据流的设计有利有弊，好处就是每个组件的依赖（数据流入）都很清晰，坏处就是状态共享问题。
于是，React提出了Context API。但是我们需要明确的是 <strong>Context API解决的其实是依赖注入的问题</strong> ，它本身并不是状态管理工具，具体可以看看这篇 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.isquaredsoftware.com%2F2021%2F01%2Fcontext-redux-differences%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.isquaredsoftware.com/2021/01/context-redux-differences/" ref="nofollow noopener noreferrer"><strong>Blogged Answers: Why React Context is Not a "State Management" Tool</strong></a>
事实上有基于Context API + Hooks封装库。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Funstated-next" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/unstated-next" ref="nofollow noopener noreferrer">jamiebuilds/unstated-next</a> ， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Funstated-next%2Fblob%2Fmaster%2Fsrc%2Funstated-next.tsx%23L15" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/unstated-next/blob/master/src/unstated-next.tsx#L15" ref="nofollow noopener noreferrer">源码</a> 十分简单。
看过源码也就能发现，其实是会有性能问题的，更改状态后，所有使用context的组件都会重新渲染。所以他们只适用于需要快速上手、对性能要求不高的 <strong>简单场景</strong> 。</p>
<h2 data-id="heading-3">网络密集型的场景</h2>
<p>这种场景常见于中后台项目，需要频繁从服务端请求数据，请求后的数据需需要进行加载状态、缓存和过期管理，这种场景可以使用React-query或者SWR。
以React-query特性来说：</p>
<ul>
<li>
<p>使用hooks API</p>
</li>
<li>
<p>封装了许多前端异步请求的逻辑</p>
</li>
<li>
<p>数据缓存控制，自动更新数据</p>
</li>
<li>
<p>重复请求合并</p>
</li>
<li>
<p>分页和延迟加载</p>
</li>
<li>
<p>。。。</p>
</li>
</ul>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F351280149" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/351280149" ref="nofollow noopener noreferrer">用react-query解决你一半的状态管理问题</a></p>
</blockquote>
<h2 data-id="heading-4">复杂场景</h2>
<p>我觉得可能真正的 <strong>复杂场景</strong> 有：</p>
<ul>
<li>
<p>用户的使用方式复杂</p>
</li>
<li>
<p>不同身份的用户有不同的使用方式（比如普通用户和管理员）</p>
</li>
<li>
<p>多个用户之间可以协作</p>
</li>
<li>
<p>与服务器大量交互，或者使用了WebSocket</p>
</li>
<li>
<p>View要从多个来源获取数据</p>
</li>
<li>
<p>。。。</p>
</li>
</ul>
<p>总而言之，在多状态、多交互、多数据源、数据耦合等复杂场景中，就需要使用 <strong>复杂状态管理库</strong> 。
按照设计思想，可以大概把他们分为四类：</p>
<ul>
<li>
<p>单向数据流：Redux, Zustand</p>
</li>
<li>
<p>响应式数据流/Proxy：Mobx, Valtio</p>
</li>
<li>
<p>原子模式Atomic：Recoil, Jotai</p>
</li>
<li>
<p>Stream: rxjs(Reactive Extension JavaScript)</p>
</li>
</ul>
<p>这里要说一下Redux、Mobx等都是比较偏底层的并且是框架无关的，他们常常有框架关联的库如react-redux，mobx-react。</p>
<h1 data-id="heading-5">总结</h1>
<p>在React生态里面，状态管理的库有很多，我们需要根据自己的需求选择适合业务场景的状态管理库。
接下来的文章将会介绍React里使用的比较多的几个主流状态管理库的主要思想和原理。</p></div>  
</div>
            