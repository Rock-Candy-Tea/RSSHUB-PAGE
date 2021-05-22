
---
title: 'React 你知道 useMemo，useCallback 和 useEffect，useLayoutEffect 的依赖数组，含义不同么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/582e339314f24468a1ce9f285bbb7226~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 05:22:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/582e339314f24468a1ce9f285bbb7226~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>任何逻辑，都可以拆分成这样的模型：</p>
<blockquote>
<p>事件 -> 状态 -> 事件 -> 状态 -> 事件 -> 状态 ...</p>
</blockquote>
<p>事件引起状态的变化，状态的变化又发起新的事件</p>
<p>“当 xxxx 发生时，xxxx 的数据会发生改变”，事件在前，状态在后，它是什么样的形式呢？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/582e339314f24468a1ce9f285bbb7226~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-21 下午7.56.47.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>引用 cycle.js 的说明文档，<strong>事件到状态的依赖箭头，在事件那里</strong></p>
<p>即 <strong>事件主动发起，状态被动承受</strong>，注意这个主被动关系</p>
<p>但是，我们换个描述</p>
<p>“监听到 xxxx 数据变化时，执行 xxxx”，状态在前，事件在后，它就会变成这种形式：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffad730247854e91a27ff7b4cee163ee~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-21 下午7.59.31.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图，依赖关系在 Bar，状态所有者，可以 <strong>主动控制</strong> 流程的执行</p>
<p>这种主被动的转换，就是 <strong>响应式编程</strong> 的核心</p>
<blockquote>
<p>而响应式编程的挑战就是这种编程思想的转变。转变你的思想为“响应式优先”，这会使你学习曲线变得平坦，大部分任务也变得简单明了</p>
</blockquote>
<p>那么我们来看看 React 那些带依赖数组的 api，哪些是主动的？而哪些又是被动的呢？</p>
<h3 data-id="heading-0">useEffect，useLayoutEffect 是主动 API</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript">useEffect(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">if</span>(a)&#123;
     <span class="hljs-comment">// ...</span>
    &#125;
&#125;,[a,b,c,d])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制结构在 useEffect 中，所以 useEffect 是主动的，是 <strong>响应式 API</strong></p>
<p>这就意味着，无论这个结构在哪里，它都能实现独立自主，也就是实现了 <strong>低耦合</strong>，同时融合了 React 的调度机制，在处理异步方面也有天然的优势</p>
<h3 data-id="heading-1">useMemo，useCallback，甚至 useState 是 被动 API</h3>
<p>useCallback 无法决定何事变化， useMemo 只是跟随 state，而 useState 也无法决定自己如何变化</p>
<p>useMemo 无所谓，因为数据不会自发地触发事件</p>
<p>但是，当你在 useEffect 中使用 useCallback 的返回值时，巨大的陷阱就出现了：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> cb = useCallback(<span class="hljs-function">()=></span>&#123;<span class="hljs-comment">/* ... */</span>&#125;,[<span class="hljs-comment">/* ... */</span>])
useEffect(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-comment">// 耦合 cb，如果 cb 不在本作用域内声明，你将很难确定依赖，控制调度</span>
&#125;,[cb])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是会有很多神奇的死循环 effect 诞生，既 effect(主动)->callback(被动？主动？)</p>
<p>useEffect 中的依赖数组，是主动的，在 effect 中作为事件发起者，应该作用于 useState 的 setter，而这里却写入了一个 被动控制的 useCallback，一旦 callback 的依赖与 effect 耦合，就会出现回环，死循环诞生</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> cb = useCallback(<span class="hljs-function">()=></span>&#123; 
   setA(<span class="hljs-string">''</span>) <span class="hljs-comment">// 这里写入 a</span>
&#125;,[a,b,c,d])
useEffect(<span class="hljs-function">()=></span>&#123;
&#125;,[cb,a]) <span class="hljs-comment">// 这里传入 a</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要避免出现回环，很简单 ——</p>
<h4 data-id="heading-2">尽量不要在 useEffect 中调用 带依赖callback</h4>
<blockquote>
<p>无依赖 callback 只是一个值，不存在主被动</p>
</blockquote>
<p>如何保证无依赖 callback 呢？</p>
<p>很简单，我们将所有这些 <code>事件->状态->事件->状态</code> 的流程，都找出来，然后将它变换成：</p>
<blockquote>
<p>事件(useCallback) -> 状态 -> effect -> 状态</p>
</blockquote>
<p>不就可以了么？</p>
<h2 data-id="heading-3">MVI 模型</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ae2e6e9cd9f4fa789b8e41b8e745641~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-21 下午8.19.21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将 IO 进行高度抽象，不难发现，只是一个如此的流程：</p>
<blockquote>
<p>操作(输入) -> 计算 -> 输出（感知）-> 人 -> 操作（输入） ...</p>
</blockquote>
<p>而其中，处理输入部分，设计为 事件，而输出部分，设计为 状态，计算部分，设计为 state + effect 集合</p>
<p>则可以轻松实现建模，而这个模式，被称作 MVI 模型：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5243a9e275d346dcb7d9aba384582670~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-21 下午8.21.42.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中 intent 部分，就是 useCallback 发力的地方，既 ——</p>
<p>我们用 useCallback 将 <strong>事件转化为状态</strong></p>
<p>那你需要为 useCallback 添加依赖么？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> [a,setA] = useState()
<span class="hljs-keyword">const</span> [b,setB] = useState()

<span class="hljs-keyword">const</span> intentCb = useCallback(<span class="hljs-function">()=></span>&#123;
  setA(<span class="hljs-string">''</span>)
  setB(<span class="hljs-string">''</span>)
&#125;,[])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于这个目的的 useCallback 使用，不会带有任何依赖，可以放心地进行传递，组合：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> refresh = useCallback(<span class="hljs-function">()=></span>&#123;&#125;,[])

useEffect(
  <span class="hljs-function">()=></span>&#123;
      refresh()
  &#125;
,[refresh,a,b,c,d,e])

<span class="copy-code-btn">复制代码</span></code></pre>
<p>既：</p>
<blockquote>
<p>DOM SOURCE -> callback -> state -> effect -> state+memo -> DOM SINK</p>
</blockquote>
<p>容易被人忽略的一点，是 view 层</p>
<p>MVI 中，用 DOM SINK 描述 view 层，即从调度上来讲，不是每个用户操作，都会让每个数据进行变化，因此，需要做一次类似过滤一样的工作</p>
<p>但是，开发者们总是忘记这一部分，比如代码中很容易习惯性直接 return 一个 element</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SomeCompo</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">return</span> <div>
    &#123;<span class="hljs-comment">/* state 好说，变换容易控制，callback 的变化很难控制，因为 function 总是新值 */</span>&#125;
    <SomeExpenssiveCompo value=&#123;[state,someCb]&#125;/>
  <div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React 官方解法是 用 useReducer 向下传递回调，并分开写 context</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> [state,dispatch] = useReducer(<span class="hljs-function">()=></span>&#123;&#125;,&#123;&#125;)
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">State.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;state&#125;</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">Dispatcher.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;dispatch&#125;</span>></span>
    &#123;/* ... */&#125;
  <span class="hljs-tag"></<span class="hljs-name">Dispatch.Provider</span>></span>
<span class="hljs-tag"></<span class="hljs-name">State.Provider</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我认为这很蠢！且不说原本属于同一上下文逻辑的的部分需要拆开，写成嵌套的上下文，让依赖注入结构更加复杂</p>
<p>最主要的是, useReducer 很难用上各种第三方 Hooks 生态，比如 react-use，swr 等，本身异步支持也不够</p>
<p>当然，有模块能力的 useReducer 都如此，更不要说全局统一上下文，无拆分初始化能力的 Redux 等统一状态管理库了</p>
<p>这里的问题，我认为真正的解法是 —— 头疼医头脚疼医脚</p>
<ol>
<li>
<p>无依赖的 callback 替代 dispatch (本来就是无依赖，不会变化)</p>
</li>
<li>
<p>为 jsx 加上 useMemo</p>
</li>
</ol>
<p>是的，你的目的就是对组件调度进行控制，既 DOM sink（沉降）</p>
<p>你应该直接作用于消费阶段（JSX Element）(将这个逻辑提前到 model 阶段，是个非常傻的做法)</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SomeCompo</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <div>
    &#123;<span class="hljs-comment">/* 只在 a,b,c 变化时，刷新这个 component */</span>&#125;
    useMemo(<span class="hljs-function">()=></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">SomeExpenssiveCompo</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;[state,someCb]&#125;/</span>></span></span>, [a,b,c])
  <div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很简单就能解决的问题，为何要上 useReducer 呢？</p>
<blockquote>
<p>useReducer 是逆变类型函数式状态机 （类似 class 的封装结构），但是，js 甚至 ts 不是函数式语言，ts 的逆变类型支持也不好，用 ts 更多应该考虑协变类型，和 利用 类的自解释性进行辅助开发</p>
</blockquote>
<p>我个人非常反对在 js/ts 中使用 reducer 这种状态机制，js/ts 没有模式识别，没有完善的协变类型，很多时候是靠开发者自己来控制代码行文，用字符串模拟协变类型，用if/switch 语句强行模式识别，这样的函数式状态机，真的没有存在的必要</p>
<p>当然，我反对在 js/ts 中使用 reducer，并不影响我认为它在 reasonml 中很美~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/785b9ab4d93c4d30b58e81d6f79ee45f~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-21 下午8.42.20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过我没有 flow + react 的开发经历，或许校验类型系统能够给这种开发方式带来更好的体验，但是基于 js/ts 的环境，还是不报太大希望</p>
<p>没错，大家注意到，我在说明 主被动/响应式编程 和 MVI 模型的时候，都是用的 cycle.js 的文档，而 cycle.js 又是基于或者借鉴 Rxjs 的</p>
<p>没错，这种基于 MVI 模型 + 主被动响应式开发的思想，就是 ——</p>
<blockquote>
<p>响应式流</p>
</blockquote>
<ol>
<li>
<p>流程上，将一次 IO 抽象为 intent，model，view，intent 发起，model 处理，view 沉降</p>
</li>
<li>
<p>逻辑上，区分主被动响应模式，如果全部更改为主动模式，即是 <strong>事件驱动流 （rx,xstream）</strong>,如果全部切换为被动模式，即是 <strong>数据驱动流（react主要模式）</strong></p>
</li>
</ol>
<p>既 <code>事件 -> 事件 -> 事件</code> 和 <code>数据 -> 数据 -> 数据</code></p>
<p>换句话说，如果你的应用逻辑部分主要采用 useCallback + state 的模式，就是事件驱动模型（全员被动），如果你的应用逻辑部分主要采用 useEffect + state 的模式，就是数据驱动模型（全员主动）</p>
<p>React 更加适合 数据驱动模型，为何？</p>
<p>哈哈哈，因为 React 没有将事件进行完全代理啊（用过 ng zone 的同学，可以站出来，科普一下何为完全暴力事件代理）</p>
<p>换言之，并非所有的事件，react 都能够感知到，合成事件处，你可以直接调用 useCallback，非合成事件呢？（setTimeout，promise，socket，web worker，media stream？）</p>
<p>你可能需要在 useEffect 中 调用 useCallback 了吧？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> handleTimeout = useCallback(<span class="hljs-function">()=></span>&#123;
   <span class="hljs-comment">// timeout</span>
&#125;,[])
useEffect(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">setTimeout</span>(handleTimeout)
&#125;,[handleTimeout])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次这些事件的处理，都必须小心翼翼，胆战新机</p>
<p>不过，有一种特殊的模式，可以用在这些地方：</p>
<h3 data-id="heading-4">action 模式 - 按照 React 调度执行函数</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> [action,disaptch] = useState(<span class="hljs-function">()=></span><span class="hljs-function">()=></span><span class="hljs-string">''</span>)

useEffect(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-comment">// 函数参数</span>
    <span class="hljs-keyword">const</span> params = action()
    <span class="hljs-comment">// 函数逻辑</span>
&#125;,[action])

<span class="hljs-comment">// 在某一处</span>
dispatch(<span class="hljs-function">()=></span><span class="hljs-string">'new param'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理很简单，只是用 useEffect 的写法，来写一个 useCallback，不过，这个所谓函数的调度，完全是由 react 控制，即：</p>
<ol>
<li>异步进行调用</li>
<li>同一事件循环，只会调用一次</li>
</ol>
<p>第二个问题可以使用参数集合的形式解决，而第一个问题，基本误解（useCallback 的话，你也无解，useEffect 处理逻辑必须按照 react 调度进行，毕竟这也是没有办法的事）</p>
<p>这样的话，setTimout 等异步事件，就非常好解决了</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> [action,dispatch] = useState(<span class="hljs-function">()=></span><span class="hljs-function">()=></span>&#123;&#125;)

useEffect(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timeout'</span>)
&#125;,[action])

useEffect(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123; dispatch(<span class="hljs-function">()=></span>&#123;&#125;) &#125;)
&#125;,[])
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">数据驱动 - 笨办法，解决复杂问题</h3>
<p>数据驱动没有像事件驱动那样，有那么多的超高度抽象的工具，比如 switchMap，merge，combine，debounce（是的，数据驱动你甚至不用 debounce，一个 timer + 另一个标识即可），但是他却高效稳定得可怕</p>
<blockquote>
<p>甚至 数据驱动 的思想来看，不存在异步，而且异步的基本实现（共享内存通讯）本身也是数据驱动的</p>
</blockquote>
<blockquote>
<p>比如 setTimeout ，触发被看做空函数（或map） action，等待被看做状态 waiting，回调执行被看做状态 over， 异步并不存在</p>
</blockquote>
<p>不难理解为何很多 hooks 工具，会这样封装：</p>
<p><code>/* swr */  const &#123;data,error,loading&#125; = useSwr(key,fetcher)</code>
`/* react-use */ const [state, doFetch] = useAsyncFn(async ()=>&#123;&#125;,[])</p>
<blockquote>
<p>当然，纯粹一点应该是 const [state,waiting,dispatch] = useAsyncFn, 可能为了易用，以及<strong>同步触发</strong>的角度考虑如此封装吧</p>
</blockquote>
<p>但是，这里就不得不说 React 的一大缺点了，即 ——</p>
<h3 data-id="heading-6">数据驱动，并不适合函数式</h3>
<p>没错，数据驱动并不适合函数式</p>
<ul>
<li>一个函数调用有调用和返回值两个状态，还有调用次数和错误，同步多次调用的话，还有参数集合等数据</li>
<li>一个异步函数调用，除了函数都有的状态，还有loading，为了方便调度控制，还有历史 loading 时间，被调用时间，发起时间以及他们的列表 等</li>
<li>一个不断触发的事件，更是有数不清的数据和相关的描述信息</li>
</ul>
<p>这让状态数量极具扩张，因此，如何管理状态，就是一个非常棘手的问题</p>
<p>用函数加返回值？既函数模拟类（无继承，继承本身应该被抛弃），效果非常差 —— 没有附加描述信息，没有自解释性</p>
<p><strong>应该用类似 Golang interface 或者 直接使用 贫血类 的方式，来管理封装状态</strong></p>
<blockquote>
<p>没错，Go 也是数据驱动进行异步开发，开发者可以通过 select，for range 一个 channel，轻易实现无锁异步开发，也正因如此，Go 并不需要函数式，支持泛型（逆变类型）的动力也不足</p>
</blockquote>
<p>而 React 这方面的支持，不能说没有，只能说很差（要知道 class 有自解释性，对于庞大的 state 集合，没有自动生成文档，自动生成图形统计，这些 state 只能让你的开发体验直线下降）</p>
<p>再加上 React 并没有完整的事件驱动支持（即没有代理全部事件，保证用户代码在 model - view 范畴内，实现全被动），你如果采用 事件驱动 Rxjs 等工具辅助开发，体验也不会好（思维负担加重）</p>
<p>这算是 React 最大的缺点吧，不过原因也很正常，reason react 才是 react 嘛，哈哈哈</p></div>  
</div>
            