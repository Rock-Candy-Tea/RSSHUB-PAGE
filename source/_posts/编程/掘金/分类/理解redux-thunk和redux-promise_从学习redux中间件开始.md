
---
title: '理解redux-thunk和redux-promise_从学习redux中间件开始'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fa03ad9530c4a84a653c6902275c52d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 08:46:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fa03ad9530c4a84a653c6902275c52d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><a href="https://juejin.cn/post/6977992027459813407" target="_blank" title="https://juejin.cn/post/6977992027459813407">上一篇文章</a>写了关于<code>redux</code>的作用以及<code>redux</code>和<code>react-redux</code>两个插件的API，但<code>redux</code>中有一个API:<code>applyMiddleware</code>并没有说明，因为涉及到<code>redux</code>的中间件概念，需要比较多内容去说明，这次这篇文章就集中写一下这方面的知识。</p>
<h2 data-id="heading-1">何为<code>redux</code>中间件</h2>
<h3 data-id="heading-2">1. 中间件的作用</h3>
<p>之前我们说过，<code>redux</code>的工作流程图是下面这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fa03ad9530c4a84a653c6902275c52d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们看<code>express</code>有中间件机制，其实<code>redux</code>也有，<code>redux</code>的中间件<code>middleware</code>是用来增强<code>dispatch</code>方法的。有时候当我们想改变<code>dispatch</code>执行同时，也执行某些操作，例如<strong>日志记录</strong>，就可以用中间件实现该需求。如果我们把中间件也纳入到<code>redux</code>的工作流程图，那新的流程图如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f73e9b371b64bcebe4ef9de67b65ade~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2. 用到中间件的简单例子</h3>
<p>我们可以拿一个例子来说一下中间件，在<a href="https://juejin.cn/post/6977992027459813407" target="_blank" title="https://juejin.cn/post/6977992027459813407">上一篇文章</a>中，我们写了一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHitotsubashi%2Fredux-js-example%2Ftree%2Frelease_react-redux" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Hitotsubashi/redux-js-example/tree/release_react-redux" ref="nofollow noopener noreferrer">计数和单位切换的例子</a>，现在拿这个例子再添加一个需求，我希望可以从控制台里知道页面程序调用了哪些<code>action</code>。虽然可以在每个<code>action creator</code>都写打印输出语句，可是这不是最优解，我可以通过插入中间件来达到这个需求：</p>
<p>目录如下所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/406f327e1d63477686da64215cd5f877~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新增<strong>store/middleware/logger.js</strong>文件，内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 中间件用函数来定义</span>
<span class="hljs-keyword">const</span> logger = <span class="hljs-function"><span class="hljs-params">store</span> =></span> <span class="hljs-function"><span class="hljs-params">next</span> =></span> <span class="hljs-function"><span class="hljs-params">action</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'dispatching'</span>, action.type)
  next(action)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> logger
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore,applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">import</span> reducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducer'</span>
<span class="hljs-keyword">import</span> logger <span class="hljs-keyword">from</span> <span class="hljs-string">'./middleware/logger'</span>

<span class="hljs-comment">// createStore的第三个参数是用来定义中间件的，如果initalState（即下面的第二个参数）省略，则可以放在第二个参数的位置传进去</span>
<span class="hljs-keyword">const</span> store = createStore(reducer,&#123;<span class="hljs-attr">number</span>:<span class="hljs-number">3</span>,<span class="hljs-attr">unit</span>:<span class="hljs-string">'mm'</span>&#125;,applyMiddleware(logger))
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>达到的效果如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/938c709a275846b68b467a8c17df7479~tplv-k3u1fbpfcp-watermark.image" alt="add&sub&unit&middleware.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHitotsubashi%2Fredux-js-example%2Ftree%2Frelease_middleware" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Hitotsubashi/redux-js-example/tree/release_middleware" ref="nofollow noopener noreferrer">项目代码</a></p>
<h3 data-id="heading-4">3. 中间件的使用方式</h3>
<p>从上面的例子可知，中间件以<strong>函数</strong>来定义，其格式为：</p>
<pre><code class="hljs language-js copyable" lang="js">store => <span class="hljs-function"><span class="hljs-params">next</span> =></span> <span class="hljs-function"><span class="hljs-params">action</span> =></span> &#123;
    <span class="hljs-comment">// do something</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>&#123;&#125;</code>里面需要调用<code>next(action)</code>，不然后面的<code>middleware</code>们不会处理该<code>action</code>以及真正触发<code>dispatch(action)</code>。</p>
<blockquote>
<p>派发给 redux Store 的 action 对象，会被 Store 上的多个中间件依次处理，如果把 action 和当前的 state 交给 reducer 处理的过程看做默认存在的中间件，那么其实所有的对 action 的处理都可以有中间件组成的。值得注意的是这些中间件会按照指定的顺序依次处理传入的 action，只有排在前面的中间件完成任务后，后面的中间件才有机会继续处理 action，同样的，每个中间件都有自己的“熔断”处理,当它认为这个 action 不需要后面的中间件进行处理时，后面的中间件就不能再对这个 action 进行处理了。</p>
</blockquote>
<p>最后在生成<code>Redux store</code>时作为第二或第三次参数传入到<code>createStore</code>中，传入之前要用<code>applyMiddleware</code>处理。下面来通过分析相关源码来了解下为什么要这么用：</p>
<h3 data-id="heading-5">4. Redux源码中是如何实现中间件的</h3>
<h4 data-id="heading-6">createStore</h4>
<p>我们先了解<code>createStore</code>方法：</p>
<p><em><strong>createStore(reducer, [preloadedState], enhancer)</strong></em></p>
<p>该方法传入2～3个参数，最后会返回一个<code>Redux store</code>。<code>applyMiddleware(middle)</code>是作为<code>enhancer</code>传入的，<code>enhancer</code>是什么？下面先引用官方的解释对其说明：</p>
<blockquote>
<p>Store enhancer 是一个组合 store creator 的高阶函数，返回一个新的强化过的 store creator。这与 middleware 相似，它也允许你通过复合函数改变 store 接口。</p>
</blockquote>
<p>总结以上的引用，其实<code>enhancer</code>是一个用于更改增强<code>Redux store</code>的函数，如何增强？我们先了解下<code>createStore</code>函数的部分代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params">
  reducer,
  preloadedState,
  enhancer
</span>) </span>&#123;
    <span class="hljs-comment">// ...无关代码不展示</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> enhancer !== <span class="hljs-string">'undefined'</span>) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> enhancer !== <span class="hljs-string">'function'</span>) &#123;
          <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(
            <span class="hljs-string">`Expected the enhancer to be a function. Instead, received: '<span class="hljs-subst">$&#123;kindOf(
              enhancer
            )&#125;</span>'`</span>
          )
        &#125;

        <span class="hljs-keyword">return</span> enhancer(createStore)(
          reducer,
          preloadedState
        )
    &#125;
    <span class="hljs-comment">//... 一堆定义store函数的逻辑不展示</span>
    <span class="hljs-keyword">const</span> store = &#123;
    <span class="hljs-attr">dispatch</span>: dispatch,
    subscribe,
    getState,
    replaceReducer,
    [$$observable]: observable
  &#125; 
  <span class="hljs-keyword">return</span> store
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从<code>createStore</code>函数的返回结果得知，<code>store</code>本质上是一个带<code>dispatch</code>,<code>subscribe</code>,<code>getState</code>,<code>replaceReducer</code>以及<code>$$observable</code>五个属性的普通<code>object</code>对象。而当调用<code>createStore</code>时有传入<code>enhancer</code>，他会直接返回<code>enhancer(createStore)(reducer,preloadedState)</code>，那其实<code>enhancer(createStore)(reducer,preloadedState)</code>执行完成后最终返回的也是一个<code>store</code>，我们可以推断<code>enhancer</code>的编写格式是这样的：
<em><strong>（createStore）=>(reducer,preloadedState)=>&#123;return store&#125;</strong></em>。接下来我们看一下生成<code>enhancer</code>的<code>applyMiddleware</code>函数是怎样子的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyMiddleware</span>(<span class="hljs-params">...middlewares</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">createStore</span>) =></span>
    <span class="hljs-function">(<span class="hljs-params">
      reducer,
      preloadedState
    </span>) =></span> &#123;
      <span class="hljs-keyword">const</span> store = createStore(reducer, preloadedState)
      <span class="hljs-comment">// 调用applyMiddleware时不允许middlewares为空</span>
      <span class="hljs-keyword">let</span> dispatch = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(
          <span class="hljs-string">'Dispatching while constructing your middleware is not allowed. '</span> +
            <span class="hljs-string">'Other middleware would not be applied to this dispatch.'</span>
        )
      &#125;

      <span class="hljs-keyword">const</span> middlewareAPI = &#123;
        <span class="hljs-attr">getState</span>: store.getState,
        <span class="hljs-attr">dispatch</span>: <span class="hljs-function">(<span class="hljs-params">action, ...args</span>) =></span> dispatch(action, ...args)
      &#125;
      <span class="hljs-comment">/**
       * 通过compose形成调用链
       * compose函数代码：
        function compose(...funcs: Function[]) &#123;
          if (funcs.length === 0) &#123;
            return (arg) => arg
          &#125;
       
          if (funcs.length === 1) &#123;
            return funcs[0]
          &#125;

          return funcs.reduce(
            (a, b) =>
              (...args: any) =>
                a(b(...args))
          )
        &#125;
       */</span>
      <span class="hljs-keyword">const</span> chain = middlewares.map(<span class="hljs-function"><span class="hljs-params">middleware</span> =></span> middleware(middlewareAPI))
      dispatch = compose(...chain)(store.dispatch)
      <span class="hljs-comment">// 通过扩展运算符拆开store后合并成新的对象以更改dispatch方法</span>
      <span class="hljs-keyword">return</span> &#123;
        ...store,
        dispatch
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重点说一下这两行代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> chain = middlewares.map(<span class="hljs-function"><span class="hljs-params">middleware</span> =></span> middleware(middlewareAPI))
dispatch = compose(...chain)(store.dispatch)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之前说过，中间件的<strong>编写格式</strong>为<em><strong>store => next => action => &#123;// do something&#125;</strong></em>，对照上面的代码来分析，假设我们按照以上的<strong>编写格式</strong>写了两个中间件分别是<code>middleware1</code>和<code>middleware2</code>如下所示：</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">const</span> middleware1 = <span class="hljs-function"><span class="hljs-params">store</span> =></span> <span class="hljs-function"><span class="hljs-params">next</span> =></span> <span class="hljs-keyword">async</span>(action) => &#123;
  <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'middleware1 start'</span>)
  <span class="hljs-keyword">await</span> next(action)
  <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'middleware1 end'</span>)
&#125;

<span class="hljs-keyword">const</span> middleware2 = <span class="hljs-function"><span class="hljs-params">store</span> =></span> <span class="hljs-function"><span class="hljs-params">next</span> =></span> <span class="hljs-keyword">async</span>(action) => &#123;
  <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'middleware2 start'</span>)
  <span class="hljs-keyword">await</span> next(action)
  <span class="hljs-built_in">console</span>.info(<span class="hljs-string">'middleware2 end'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当调用<code>applyMiddleware(middleware1,middleware2)</code>传入这两个中间件，<code>applyMiddleware</code>内部执行到<code>const chain = middlewares.map(middleware => middleware(middlewareAPI))</code>这一条语句时，<code>middlewareAPI</code>对应<strong>编写格式</strong>中的<code>store</code>形参，返回的<code>chain</code>是一个数组，其中的元素为 <em><strong>next => action => &#123;// do something&#125;</strong></em> 格式的函数，即是一个描述如何调用<code>dispatch</code>的函数（<code>next</code>是一个经包装或者原始的<code>dispatch</code>，通过<code>next(action)</code>可以派发<code>action</code>）。</p>
<p>轮到下一条语句<code>dispatch = compose(...chain)(store.dispatch)</code>，当执行<code>compose(...chain)</code>时，根据注释中<code>compose</code>函数的源码我们可以推断该语句执行后返回的结果为：<code> (...args: any) =>chain1(chain2(...args))</code>，最终把<code>store.dispatch</code>作为形参传入该函数时，相当于执行<code>chain1(chain2(store.dispatch))</code>，会有下图的执行过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c12c32f27dfc4dcf96c12f82029c6cb0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先执行<code>chain2</code>函数，<code>store.dispatch</code>作为<code>chain2</code>中的<code>next</code>新参传入，<code>chain2</code>立即返回一个格式为<em><strong>action=>&#123;&#125;</strong></em> 的函数，该函数作为<code>chain1</code>中的<code>next</code>新参传入<code>chain1</code>中，而<code>chain1</code>也会返回一个格式一样为<em><strong>action=>&#123;&#125;</strong></em> 的函数赋值给<code>dispatch</code>。该<code>dispatch</code>会在<code>applyMiddleware</code>函数中最后的语句<code>return &#123;...store,dispatch&#125;</code>与<code>store</code>合并返回出去。<strong>以上过程中，<code>chain1</code>和<code>chain2</code>返回的<code>action=>&#123;&#125;</code>的函数都以闭包的方式记录着<code>next</code>变量。</strong></p>
<p>当在开发代码中<code>dispatch(action)</code>被调用时，会呈现以下的调用流程：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32b20da6896d4bcb82acf48d428c1cfe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因<code>dispatch</code>指向<code>chain1</code>，故先执行<code>chain1</code>，执行到<code>next(action)</code>语句时，其<code>next</code>指向<code>chain2</code>，故开始执行<code>chain2</code>，执行到<code>next(action)</code>语句时，<code>next</code>指向<code>store</code>原始的<code>dispatch</code>方法，从而实现了增强<code>dispatch</code>方法。上面的调用流程中控制台的输出会是以下的结果：</p>
<pre><code class="hljs language-js copyable" lang="js">middleware1 start
middleware2 start
middleware2 end
middleware1 end
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">关于异步action</h2>
<p>存在以下需求，我需要把<code>github</code>中的表情包数据放到<code>Redux store</code>中供项目里的多个模块使用，而这些数据需要异步请求获取，这时候我们遇到一个难题，因<code>reducer</code>原则上是<strong>纯函数</strong>，因此，异步操作这类不纯的行为不能出现在<code>reducer</code>中，针对此问题，我们可以绕个弯子，写个如下的公共函数，获取响应后调用<code>dispatch</code>设置状态，下面我来写一个例子来实践一下上述思路：</p>
<p><strong>utils\index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'../store'</span>
<span class="hljs-keyword">import</span> &#123;SET_EMOJIS&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../store/action'</span>

<span class="hljs-comment">// 公共函数，用于请求或更新表情图数据</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">requestEmojis</span>(<span class="hljs-params"></span>)</span>&#123;
  fetch(<span class="hljs-string">'https://api.github.com/emojis'</span>) <span class="hljs-comment">// 数据从github的公共开放接口获取</span>
    .then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>res.json())
    .then(<span class="hljs-function"><span class="hljs-params">emojis</span>=></span>store.dispatch(SET_EMOJIS(emojis)))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是<code>store</code>的代码：</p>
<p><strong>store\index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">import</span> reducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducer'</span>

<span class="hljs-comment">// 把数据初始值设为对象</span>
<span class="hljs-keyword">const</span> store = createStore(reducer,&#123;&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>store\action\index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 用于生成设置表情图数据的action的action creator</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SET_EMOJIS=<span class="hljs-function">(<span class="hljs-params">emojis</span>)=></span>(&#123;
  <span class="hljs-attr">type</span>:<span class="hljs-string">'SET_EMOJIS'</span>,
  emojis
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>store\reducer\index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state,action</span>)=></span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'SET_EMOJIS'</span>:
      <span class="hljs-keyword">return</span> action.emojis
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> reducer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们来通过以下组件查看效果：</p>
<p><strong>App.jsx</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span>  React  <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>
<span class="hljs-keyword">import</span> &#123;requestEmojis&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../utils'</span>

<span class="hljs-keyword">const</span> App = <span class="hljs-function">(<span class="hljs-params">props</span>)=></span>&#123;
  <span class="hljs-keyword">const</span> &#123;emojis&#125; = props
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>emojis<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    // 点击该按钮后通过调用公共方法requestEmojis获取表情图并存到Redux store中
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;requestEmojis&#125;</span>></span>获取emojis<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
    &#123;
      Object.entries(emojis)
        .slice(0,50) // 数据有点多，所以只显示50个表情图
        .map(([key,value])=>
          <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">&#123;key&#125;</span> <span class="hljs-attr">title</span>=<span class="hljs-string">&#123;key&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;key&#125;/</span>></span>
        )
    &#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> (&#123;
  <span class="hljs-attr">emojis</span>:state
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  connect(mapStateToProps,<span class="hljs-literal">null</span>)(App)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们来看一下效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51b94e1af31543f3948650cc26778b27~tplv-k3u1fbpfcp-watermark.image" alt="async emojis.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHitotsubashi%2F02-redux-test%2Ftree%2Ffeature_without_thunk" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Hitotsubashi/02-redux-test/tree/feature_without_thunk" ref="nofollow noopener noreferrer">项目地址</a></p>
<p>但在实际开发中，这种做法并不常用，原因可以等我介绍了<code>redux-thunk</code>的用法后，再拿这两种用法分析对比。</p>
<p>我们更偏向于利用第三方插件实现<strong>异步action</strong>，<strong>异步action</strong>指指向异步操作的<code>action</code>。下面我们来依次看一下上面所说到的常用的第三方插件<code>redux-thunk</code>和<code>redux-promise</code>：</p>
<h2 data-id="heading-8">redux-thunk</h2>
<h3 data-id="heading-9">使用方法</h3>
<p>我们在上面的例子引入<code>redux-thunk</code>进行改造，在调用<code>createStore</code>创建<code>Redux store</code>时，就要通过<code>applyMiddleware</code>加载<code>redux-thunk</code>，如下所示：</p>
<p><strong>store\index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore,applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">import</span> reducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducer'</span>
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-thunk'</span>

<span class="hljs-keyword">const</span> store = createStore(reducer,&#123;&#125;, applyMiddleware(thunk))
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在 <strong>store\action\index.js</strong> 中加一个异步<code>action</code>如下所示： <strong>（注意此处的<code>action</code>是一个函数，而并非是以往的带<code>type</code>属性的纯对象）</strong>：</p>
<p><strong>store\action\index.js</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SET_EMOJIS=<span class="hljs-function">(<span class="hljs-params">emojis</span>)=></span>(&#123;
  <span class="hljs-attr">type</span>:<span class="hljs-string">'SET_EMOJIS'</span>,
  emojis
&#125;)

<span class="hljs-comment">// 此处的异步action为一个高阶函数，返回结果也是一个函数</span>
<span class="hljs-comment">// 此处的REQUEST_EMOJIS也是一个Action Creator，所谓Action Creator指创建异步action或同步action的函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> REQUEST_EMOJIS = <span class="hljs-function">()=></span><span class="hljs-function"><span class="hljs-params">dispatch</span> =></span> (
  fetch(<span class="hljs-string">'https://api.github.com/emojis'</span>)
    .then(<span class="hljs-function">(<span class="hljs-params">res</span>)=></span>res.json())
    .then(<span class="hljs-function"><span class="hljs-params">emojis</span> =></span> dispatch(SET_EMOJIS(emojis)))
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后更改一下<strong>App.jsx</strong></p>
<p><strong>App.jsx</strong></p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">import</span>  React  <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>
<span class="hljs-keyword">import</span> &#123;REQUEST_EMOJIS&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../store/action/index'</span>

<span class="hljs-keyword">const</span> App = <span class="hljs-function">(<span class="hljs-params">props</span>)=></span>&#123;
  <span class="hljs-keyword">const</span> &#123;emojis&#125; = props
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>emojis<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;props.requestEmojis&#125;</span>></span>获取表情图<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
    &#123;
      Object.entries(emojis).slice(0,50).map(([key,value])=>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">&#123;key&#125;</span> <span class="hljs-attr">title</span>=<span class="hljs-string">&#123;key&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;key&#125;/</span>></span>
      )
    &#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> (&#123;
  <span class="hljs-attr">emojis</span>:state
&#125;)

<span class="hljs-keyword">const</span> mapDispatchToProps = <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> (&#123;
  <span class="hljs-attr">requestEmojis</span>: <span class="hljs-function">() =></span> dispatch(REQUEST_EMOJIS()),
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  connect(mapStateToProps,mapDispatchToProps)(App)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样子就可以不调用异步请求的公共函数的同时也实现上面的效果，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHitotsubashi%2F02-redux-test%2Ftree%2Ffeature_redux_thunk" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Hitotsubashi/02-redux-test/tree/feature_redux_thunk" ref="nofollow noopener noreferrer">项目地址</a>。</p>
<p>值得注意的是，被<code>dispatch</code>派发的 <strong>异步<code>action</code></strong> 是一个函数，格式是<code>(dispatch, getState, extraArgument)=>&#123;&#125; </code>。</p>
<h3 data-id="heading-10">源码分析</h3>
<p>现在来分析一下<code>redux-thunk</code>的源码，源码非常简洁，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createThunkMiddleware</span>(<span class="hljs-params">extraArgument</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">&#123; dispatch, getState &#125;</span>) =></span> <span class="hljs-function">(<span class="hljs-params">next</span>) =></span> <span class="hljs-function">(<span class="hljs-params">action</span>) =></span> &#123;
    <span class="hljs-comment">// 如果传入的action是一个函数，则代表该action为异步action，则把dispatch, getState, extraArgument作为形参传入该异步action执行</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> action === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">return</span> action(dispatch, getState, extraArgument);
    &#125;

    <span class="hljs-keyword">return</span> next(action);
  &#125;;
&#125;

<span class="hljs-keyword">const</span> thunk = createThunkMiddleware();
thunk.withExtraArgument = createThunkMiddleware;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> thunk;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码太精简了，我觉得我都不用解释什么了，不过从源码中我们可以看出一点，在使用<code>redux-thunk</code>时，<strong>异步<code>action</code></strong> 必须写成<code>(dispatch, getState, extraArgument)=>&#123;&#125; </code>格式，然后在执行过程中需要调用<code>dispatch(action)</code>派发。</p>
<h3 data-id="heading-11">拓展：为什么要用redux-thunk（此章节可跳过）</h3>
<p><strong>此章节可能跟文章无关，我是兴趣之余写的，可以直接跳过</strong></p>
<p>为什么目前大多数用的是<code>redux-thunk</code>而不是像开头的<strong>异步公共函数的方式</strong>去解决异步操作。我从<strong>stackoverflow</strong>中的问题<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F35411423%2Fhow-to-dispatch-a-redux-action-with-a-timeout%2F35415559%2335415559" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/35411423/how-to-dispatch-a-redux-action-with-a-timeout/35415559#35415559" ref="nofollow noopener noreferrer">how-to-dispatch-a-redux-action-with-a-timeout</a>其中<strong>Dan Abramov（Redux作者）</strong> 的回答中得出了主要的答案：</p>
<p>对比于<code>redux-thunk</code>，使用<strong>异步公共函数的方式</strong>会导致：</p>
<ol>
<li>
<p><strong>不利于服务端渲染</strong></p>
<p>答案中是这么写的：</p>
<blockquote>
<p>The main reason we dislike it is because it forces store to be a singleton. This makes it very hard to implement server rendering. On the server, you will want each request to have its own store, so that different users get different preloaded data.</p>
</blockquote>
<p>在Redux关于服务端渲染的链接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux.js.org%2Fusage%2Fserver-rendering" target="_blank" rel="nofollow noopener noreferrer" title="https://redux.js.org/usage/server-rendering" ref="nofollow noopener noreferrer">Redux Server Rendering</a>中，这里 我们可以知道，每一次请求经服务端渲染的页面时，后端都会：</p>
<ol>
<li>创建一个新的<code>Redux store</code>，选择性地派发部分<code>action</code>，</li>
<li>然后模板页面可能某些占位符用<code>Redux store</code>中<code>state</code>的数据填充</li>
<li>从<code>Redux store</code>获取<code>state</code>，然后在和已渲染的<code>HTML</code>放到响应信息中一并传到客户端。客户端会根据响应的<code>state</code>创建<code>Redux store</code>。</li>
</ol>
<p>在上面采用<strong>异步公共函数的方式</strong>方案的例子中，<code>store</code>出现在两个地方，一处是<code><Provider store=&#123;store&#125;></code>中，一处是 <code>requestEmojis</code>公共函数中，在服务端渲染中如果调用到 <code>requestEmojis</code>，那需要保证两个地方的<code>store</code>是同一个实例。这样子会增加后端代码的复杂度。但是如果使用<code>redux-thunk</code>，那<code>store</code>只出现在<code><Provider store=&#123;store&#125;></code>中，我们不需要考虑保证单例的问题。</p>
</li>
<li>
<p><strong>不利于测试代码的编写</strong></p>
<p>引用答案中的描述：</p>
<blockquote>
<p>A singleton store also makes testing harder. You can no longer mock a store when testing action creators because they reference a specific real store exported from a specific module. You can’t even reset its state from outside.</p>
</blockquote>
<p>在保证上述所说的单例时，我们会很难编写测试用例，因为对于<code>requestEmojis</code>公共函数的测试中，其调用的<code>store</code>是一个真正的<code>Redux store</code>，其<code>duspatch</code>的调用会影响到页面的显示，因此，我们不能通过<code>jest</code>里<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjestjs.io%2Fzh-Hans%2Fdocs%2Fbypassing-module-mocks" target="_blank" rel="nofollow noopener noreferrer" title="https://jestjs.io/zh-Hans/docs/bypassing-module-mocks" ref="nofollow noopener noreferrer">bypassing-module-mocks</a>中的<code>jest.mock</code>去取替这个<code>store</code>。</p>
<p><code>Redux</code>不推荐手写<code>Action Creator</code>，他们更推荐使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux-toolkit.js.org%2Fintroduction%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="https://redux-toolkit.js.org/introduction/getting-started" ref="nofollow noopener noreferrer">@reduxjs/toolkit</a>去生成<code>Action Creator</code>。更详细的资料可参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux.js.org%2Fusage%2Fwriting-tests%23action-creators--thunks" target="_blank" rel="nofollow noopener noreferrer" title="https://redux.js.org/usage/writing-tests#action-creators--thunks" ref="nofollow noopener noreferrer">action-creators--thunks</a>。</p>
</li>
<li>
<p><strong>难以区分容器组件和展示组件</strong></p>
<blockquote>
<p>This makes it trickier to separate container and presentational components because any component that dispatches Redux actions asynchronously in the manner above has to accept dispatch as a prop so it can pass it further.</p>
</blockquote>
<p>什么是<strong>容器组件(container components)</strong> 和 <strong>展示组件(presentational components)</strong>，我引用别的文章的一张图来解释：</p>
 <img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edd9e3d97e374befb584a7dcd010b3b0~tplv-k3u1fbpfcp-watermark.image" width="70%" loading="lazy" referrerpolicy="no-referrer">
 <div>图片来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_46042722%2Farticle%2Fdetails%2F104891137" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_46042722/article/details/104891137" ref="nofollow noopener noreferrer">blog.csdn.net/weixin_4604…</a></div>
<p><code>Redux</code>把接受来自<code>Redux store</code>数据和行为的组件称为<strong>容器组件</strong>，与<code>Redux store</code>数据和行为无任何关系的组件称为<strong>展示容器</strong>。一般通过<code>connect</code>把<code>Redux store</code>数据和行为注入到<strong>展示容器</strong>后会成为<strong>容器组件</strong>。如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2768180110ab42bcb72fb8b9d6929b18~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>写代码时区分这两种组件会让我们的编写组件逻辑更加清晰，通常严格规范的项目都会把<strong>展示组件</strong>和<strong>容器组件</strong>写在不同的文件夹下，如<code>Redux</code>官网的例子<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fgithub%2Freactjs%2Fredux%2Ftree%2Fmaster%2Fexamples%2Ftodos" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/github/reactjs/redux/tree/master/examples/todos" ref="nofollow noopener noreferrer">Todo 列表</a>。</p>
<p>但如果用<strong>异步公共函数的方式</strong>，则不利于区分这两种组件，就拿开头例子中的<strong>App.jsx</strong>来说明：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a026da4a5f9c48f59cfcae6e560e42c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面代码中的<code>App</code>变量里<code><button onClick=&#123;requestEmojis&#125;>获取emojis</button></code>已经注入了<code>requestEmojis</code>方法，而该方法里面已经包含了<code>Redux store</code>行为。所以在此已经不能区分<strong>容器组件</strong> 和 <strong>展示组件</strong> 了。</p>
</li>
</ol>
<p>综上，我们更推荐使用<code>Redux-thunk</code>取替<strong>异步公共函数的方式</strong>的方案。</p>
<h2 data-id="heading-12">redux-promise</h2>
<h3 data-id="heading-13">使用方法</h3>
<p>我们继续用上面表情图的例子，只是这次把<code>redux-thunk</code>换成<code>redux-promise</code>。首先在用<code>createStore</code>创建<code>store</code>时，和<code>redux-thunk</code>的配置一样，用<code>applyMiddleware</code>加载从<code>redux-promise</code>引入的插件，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore,applyMiddleware &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">import</span> reducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducer'</span>
<span class="hljs-keyword">import</span> promiseMiddleware <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-promise'</span>;

<span class="hljs-keyword">const</span> store = createStore(reducer,&#123;&#125;, applyMiddleware(promiseMiddleware))
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就是根据<code>redux-promise</code>规定的格式编写<code>action creator</code>了，此处的<code>action creator</code>有两种写法：</p>
<p><strong>1. <code>action creator</code>是一个函数，其返回值必须是一个<code>promise</code>，<code>promise</code>最后<code>resolve</code>的是一个同步的<code>action</code>，该<code>action</code>会直接设置<code>Redux store</code>中的<code>state</code>值。如下所示：</strong></p>
<p><strong>reducer</strong></p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state,action</span>)=></span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-comment">// 处理第一种action creator</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'SET_EMOJIS'</span>:
      <span class="hljs-keyword">return</span> action.emojis
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>action</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SET_EMOJIS=<span class="hljs-function">(<span class="hljs-params">emojis</span>)=></span>(&#123;
  <span class="hljs-attr">type</span>:<span class="hljs-string">'SET_EMOJIS'</span>,
  emojis
&#125;)

<span class="hljs-comment">// 第一种action creator写法：</span>
<span class="hljs-comment">// 此action creator执行后返回一个promise，promise.resolve的同步action会直接被Redux store的dispatch执行，而不是经过下一个中间件middleware的处理</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> REQUEST_EMOJIS=<span class="hljs-keyword">async</span>()=>&#123;
  <span class="hljs-keyword">const</span> emojis = <span class="hljs-keyword">await</span> fetch(<span class="hljs-string">'https://api.github.com/emojis'</span>)
    .then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>res.json())
  <span class="hljs-keyword">return</span> SET_EMOJIS(emojis)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. <code>action creator</code>也是一个函数，其返回值必须是一个<code>payload</code>为<code>promise</code>的<code>FSA</code>,<code>FSA</code>全称flux standard action，意指符合<code>flux</code>标准的action，该<code>action</code>的判断函数如下：</strong></p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isFSA</span>(<span class="hljs-params">action</span>) </span>&#123;
    <span class="hljs-comment">//1. action必须是一个平面对象 plain-object</span>
    <span class="hljs-comment">//2. action.type必须是一个字符串</span>
    <span class="hljs-comment">//3. action的属性中不能出现["type", "payload", "error", "meta"]以外的属性</span>
    <span class="hljs-keyword">return</span> isPlainObject(action)&&
        isString(action.type)&&
        <span class="hljs-built_in">Object</span>.keys(action).every(<span class="hljs-function"><span class="hljs-params">key</span> =></span> [<span class="hljs-string">"type"</span>, <span class="hljs-string">"payload"</span>, <span class="hljs-string">"error"</span>, <span class="hljs-string">"meta"</span>].includes(key));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>action</strong></p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-comment">// 第二种action creator写法：</span>
<span class="hljs-comment">// payload必须是一个promise，中间件会先处理这个promise，等promise.resolve后把resolve的值替换这个promise放payload里，然后把action传给reducer处理</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SET_EMOJIS1=<span class="hljs-function">()=></span>(&#123;
  <span class="hljs-attr">type</span>:<span class="hljs-string">'SET_EMOJIS1'</span>,
  <span class="hljs-attr">payload</span>:fetch(<span class="hljs-string">'https://api.github.com/emojis'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>res.json())
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>reducer</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state,action</span>)=></span>&#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-comment">// 处理第二种action creator</span>
    <span class="hljs-comment">// 其promise.resolve的值会放在payload上，即fecth请求的数据就放在payload上</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'SET_EMOJIS1'</span>:
      <span class="hljs-keyword">return</span> action.payload
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHitotsubashi%2F02-redux-test%2Ftree%2Ffeature_redux_promise" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Hitotsubashi/02-redux-test/tree/feature_redux_promise" ref="nofollow noopener noreferrer">项目代码</a>中查看。</p>
<h3 data-id="heading-14">源码分析</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> isPromise <span class="hljs-keyword">from</span> <span class="hljs-string">'is-promise'</span>;
<span class="hljs-keyword">import</span> &#123; isFSA &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'flux-standard-action'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promiseMiddleware</span>(<span class="hljs-params">&#123; dispatch &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-params">next</span> =></span> <span class="hljs-function"><span class="hljs-params">action</span> =></span> &#123;
    <span class="hljs-comment">// 判断action是否为FSA</span>
    <span class="hljs-keyword">if</span> (!isFSA(action)) &#123;
      <span class="hljs-comment">// 判断action是否为promise，若是则按上述第一种action处理，如果不是则传递给下一个middleware处理</span>
      <span class="hljs-comment">// 注意如果action以reject的形式结束，则不会执行下去</span>
      <span class="hljs-keyword">return</span> isPromise(action) ? action.then(dispatch) : next(action);
    &#125;

    <span class="hljs-comment">// 如果action为FSA且action.payload是一个promise，则按上述第二种action处理：</span>
    <span class="hljs-comment">// 即等其resolve后，把resolve的值替换当前action的payload，然后跳过接下来的中间件直接让store.dispatch派发action</span>
    <span class="hljs-comment">// 如果promise是catch，我就不说了，下面写的很清楚了</span>
    <span class="hljs-keyword">return</span> isPromise(action.payload)
      ? action.payload
          .then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> dispatch(&#123; ...action, <span class="hljs-attr">payload</span>: result &#125;))
          .catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
            dispatch(&#123; ...action, <span class="hljs-attr">payload</span>: error, <span class="hljs-attr">error</span>: <span class="hljs-literal">true</span> &#125;);
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
          &#125;)
      : next(action);
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">后记</h2>
<p>之后会继续写关于<code>dva</code>用法的文章，再次立个<strong>FLAG</strong>鼓励自己再接再厉。</p></div>  
</div>
            