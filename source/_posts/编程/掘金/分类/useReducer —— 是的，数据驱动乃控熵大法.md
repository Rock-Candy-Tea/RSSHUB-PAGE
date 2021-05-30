
---
title: 'useReducer —— 是的，数据驱动乃控熵大法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dee126a0ebfe4cdab500f5c905ab3e0c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 06:08:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dee126a0ebfe4cdab500f5c905ab3e0c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>（但是，只在封闭系统生效！）</strong></p>
<p>早些时候，我对 hooks 下使用 useReducer 或者一众状态管理库是非常方案的，带上在结合项目仔细思考之下，发现了这一方案的优点，或许结合使用才是最优解</p>
<p>对 useReducer 的产生误解的原因也很简单：</p>
<ol>
<li><strong>类型支持</strong>非常差（js/ts 没有很好的逆变类型支持，没有模式识别，对比 reasonml 下的 useReducer 可知）</li>
<li><strong>无模式识别</strong>（同上）</li>
<li>无法在 useReducer 内部，利用<strong>第三方 hooks 生态</strong>（即封装状态逻辑视图的全功能第三方库）</li>
</ol>
<p>很简单一个例子，<code>const &#123;data,error&#125; = useSwr(key,fetcher)</code>,这段代码将请求过程，全部转化为数据驱动的 data，error 状态，同时响应式支持了请求，延迟，屏幕聚焦，轮训，防抖等等功能</p>
<p>开发过程中使用这样的 第三方 api 能够得到事半功倍的效果</p>
<p>但是，如果你在这样的逻辑上，使用了 useReducer ，那么，这个叫做 useSwr 的 api，你无法再使用了，因为 reducer 内部代码（<strong>脱离了 react 调度</strong>）</p>
<blockquote>
<p>当然，这里说的是 useReducer 的劣势，redux，mobx 等工具不在讨论范围内，，因为缺乏 module 功能，没有初始化的控制能力（<strong>即状态管理功能无法随着组件的初始化而初始化，迭代，异步渲染中失去了可编程性</strong>），导致大部分场景下已经缺乏使用价值（除了跨平台，又想要省略 dsl 编译过程，不过这种需求非常罕见，不是正道，比如 rn 和 flutter 方案，flutter 原理上更胜一筹）</p>
</blockquote>
<blockquote>
<p>不过，如果缺乏专业产品经理或者业务专家，没有设计，叠加新版本相关生态不够完善的情况下（比如 antd 的 useForm 不是无视图依赖的逻辑api，导致 <code>@testing-library/react-hooks</code> 无法使用），redux 等工具的调试方式可能更适合不稳定项目（生态完善的情况下，依然优先 TDD，即便缺乏顶层设计，因为逻辑本身是抽象的，靠打印进行的调试隔着一层 dom，一层 vm，绝对不是好的选择，直接调试逻辑才是标准流程）</p>
</blockquote>
<p>这么说来，useReducer 在 hooks 环境下，就毫无作用可言了么？</p>
<p>前文有提过，至少 react 所举的例子，并不能说明 useReducer 的意义：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dee126a0ebfe4cdab500f5c905ab3e0c~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-29 下午9.16.36.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仅仅是因为 useCallback 有变化？就需要用 useReducer dispatch？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> [todos,dispatch] = useReducer(todosReducer)
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">TodosState</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;todos&#125;</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">DeepTreeWithState</span>/></span>
  <span class="hljs-tag"><<span class="hljs-name">TodosDispatch.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;dispatch&#125;</span>></span> 
    <span class="hljs-tag"><<span class="hljs-name">DeepTreeWithDispatch</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">TodosDispatch.Provider</span>></span>
<span class="hljs-tag"></<span class="hljs-name">TodosState</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>甚至标准做法还应该做的这么丑陋？</p>
<p>拜托，这个实在误人子弟了，控制 view 永远靠 useMemo，调度逻辑也是业务逻辑的一部分，哪能就这么回避掉的？</p>
<p><strong>直接返回未拆分的 jsx</strong> 本身的含义就是 —— <strong>视图跟随所有 state，props，context 变化</strong>，逻辑即如此，反而 dispatch 虽不说不伦不类，也有点反直觉</p>
<p>useReducer 该用么？现在告诉大家，某些情况下的确该用，但是不是 react 文档提到的这种情况（至少绝不会像他说的那么简单）</p>
<p>什么情况下需要用到 useReducer ？</p>
<h2 data-id="heading-0">封闭系统下的 <strong>控熵</strong></h2>
<blockquote>
<p>熵：泛指某些物质系统状态的一种量度，某些物质系统状态可能出现的程度</p>
</blockquote>
<p>可以近似理解为，同一时刻，物体可能状态的数量，其中既包含状态的 <strong>数量</strong>，也包含状态的 <strong>可能性</strong></p>
<p>还记得前文总结的么？React 虽然在 hooks 这一次更新，做了很大的函数式改进，但是数据驱动原则始终未变</p>
<p>毕竟直接由具象转化为抽象编程，跨度太大，前端又多是处在视图开发层次，<strong>状态或许比事件更加重要？</strong></p>
<p>然而函数式是不应该有太多状态，无共享状态甚至是无状态的，因为函数本身是对变化的抽象，用状态模拟概念编程，补足函数式顶层设计短板的做法，其实是有很大牺牲的（比如缺乏概念编程的自解释性，类型无协变，即类型无法自顶向下等）</p>
<p>但是，现实是，前端必须两者兼得，必须尊重状态，因为前端开发本身就是<strong>中介</strong>，本身就是视图和一致性数据的中间件，状态绕不过去</p>
<p>同样，即便是事件驱动（zone）著称的 angular，也没有像 cyclejs 那样无状态流一撸到底，cyclejs 的不温不火也能反过来证明这一点</p>
<p>那么， 状态，以及背后代表的意义，就耐人寻味了</p>
<p>因为</p>
<h3 data-id="heading-1">状态就是熵</h3>
<p>下面这段表述我相信对 react 程序员来说，都是入门经典：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235b89f54bee416e82006fa1281b724f~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-29 下午9.36.59.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没错！曼妥思糖和可乐！</p>
<p>曼妥思碰到了可乐，双方产生剧烈反应，一方的不确定性和状态数量会直接灌入另一方中，这就是个剧烈的熵增反应</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61cbe3292f3e4e3d973548f98491e30d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>左侧是你的应用中的状态，右侧是你收到的数据请求的状态，一旦两者想触碰，会发生什么？</p>
<blockquote>
<p>注意，将数据和数据变化的可能性，都要作为状态统一看待，熵本身就是状态可能性集合，因此，除了请求返回数据，还有请求返回时间，错误，多个请求的关系，race 还是更加复杂的调度？</p>
</blockquote>
<p>一边，是确定调度，确定结构的 react 应用，另一边，是不确定数据，不确定调度的异步</p>
<p><strong>将两者看做一个系统，怎么解决这个问题？</strong></p>
<p>没错！麦克斯韦妖！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0e93035421643ddbb57b12349138452~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设出现一个有选择能力的主体 —— 麦克斯韦妖，它选择性地将结果放入另一个结构（react 应用/store）中，就可以解决这个问题</p>
<p>一边是确定性（低熵）的 state，通过这个 麦克斯韦妖（dispatch）选择 （reducer），很好地保证了 store
的低熵环境</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> [state,dispatch] = useReducer(<span class="hljs-function">(<span class="hljs-params">state,action</span>)=></span>&#123;
  <span class="hljs-keyword">if</span>(action.name === <span class="hljs-string">'xxx'</span>)&#123;
    <span class="hljs-comment">// 麦克斯韦妖/reducer 正在进行选择</span>
  &#125;
  
  <span class="hljs-comment">// 麦克斯韦妖/reducer 正在放入另一侧的 state </span>
  <span class="hljs-keyword">return</span> &#123;...state&#125;
&#125;,&#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，前文提到的某个情景 —— 即应对非合成事件 的时候，callback 调用烧脑的问题（区分内外，区分调度源），useReducer 是个非常好的解决方案</p>
<p>这个时候，dispatch 的不变性，才有了很好的使用场景：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> ws = useRef()
<span class="hljs-keyword">const</span> [state,dispatch] = useReducer(<span class="hljs-function">(<span class="hljs-params">state,action</span>)=></span>&#123;
  <span class="hljs-keyword">if</span>(action.payload === <span class="hljs-string">'init'</span>)&#123;
    ws.current = <span class="hljs-keyword">new</span> WebSocker(<span class="hljs-string">'...'</span>)
  &#125;
  <span class="hljs-keyword">if</span>(action.payload === <span class="hljs-string">'read'</span>)&#123;
    ws.current.send(<span class="hljs-string">'read'</span>)
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;,&#123;<span class="hljs-attr">data</span>:<span class="hljs-string">''</span>,<span class="hljs-attr">error</span>:<span class="hljs-literal">null</span>&#125;)

<span class="hljs-comment">// 这样，应用本身的结构，可以很容易（effect,合成事件）与另一部分（非合成事件）进行交流</span>

useEffect(<span class="hljs-function">()=></span>&#123;
  <span class="hljs-keyword">if</span>(ready)&#123;
    dispatch(<span class="hljs-string">'init'</span>)
  &#125;
&#125;,[ready])


<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch('init')&#125;>init<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的话，不确定性会比纯粹使用 useCallback 低得多（因为依赖很难得到处理，至少很烧脑）</p>
<p>整个应用的熵得到了非常好的控制</p>
<h2 data-id="heading-2">useReducer，系统对接的神器</h2>
<p>是的，当我们想要将一个封闭系统，与另一个系统对接，形成更大的封闭系统时，useReducer 就非常有用了，因为它控制住了不确定性</p>
<p>将 dispatch 想象成麦克斯韦妖，你就能很轻松实现多个系统之间的隔离，并且有可预知的结果</p>
<p>那么，除了异步以外，还有哪些地方可以用到呢？</p>
<p>跨模块通讯！</p>
<p>这部分以后可以继续分享，因为涉及一个笔者仍没有彻底弄懂的架构技术</p>
<h2 data-id="heading-3">那全用 useReducer 可以么？</h2>
<p>本来是可以的，除非你不想要哪些全封装的第三方hooks api，以及不想要更简单明了的<code>流</code></p>
<p>但是效率和质量是可以做权衡的，这部分看你怎么看，不过一旦你全使用 useReducer 进行开发，就是默认了，有 useReducer 处，就是个单独的模块</p>
<p>也就是说，要么全用 useReducer，要么只用 useReducer 做模块通讯（其他调度系统的通讯也可以看做模块通讯）</p></div>  
</div>
            