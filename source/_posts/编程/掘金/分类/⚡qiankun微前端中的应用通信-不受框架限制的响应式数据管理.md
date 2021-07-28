
---
title: '⚡qiankun微前端中的应用通信-不受框架限制的响应式数据管理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b0480c587c641428c1ca6ca145ccf5b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 23:25:52 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b0480c587c641428c1ca6ca145ccf5b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">引言</h2>
<p>对于微前端来说，应用间通信（主要为主应用-微应用）往往是架构设计之初就要考虑的核心需求，并且这种通信需求往往不是一个简单的传参就能满足的（如果是的话，<code>路由</code>、<code>localstorage</code>就可以满足），因此这就要求我们在进行技术选型，调研微前端解决方案时，通信方案也要一并考虑。</p>
<h2 data-id="heading-1">背景</h2>
<p>在调研了众多微前端解决方案后，我们初步选择了<code>qiankun</code>框架，但是qiankun自身在通信方面并不提供完整的解决方案，更多的是提供api，通过这些api可以快捷地实现通讯功能，但是对于更丰富、未来可能更复杂地业务需求，依照qiankun文档中的示例，恐怕难以满足。因此在横向对比了众多方案后（其中一篇文章给了我很大的启发-<a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">基于 qiankun 的微前端最佳实践（图文并茂） - 应用间通信篇</a>）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b0480c587c641428c1ca6ca145ccf5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终选择使用<code>redux</code>作为微前端的通信解决方案。</p>
<h2 data-id="heading-2">特点</h2>
<p>该方案以<code>redux</code>为核心，采用<code>发布-订阅模式</code>进行封装，实现应用间通信数据上的<code>响应式</code>，并在代码结构上实现<code>模块化</code>，api方面仿照vuex，降低上手难度, 并可<code>适用多框架</code>（如vue、react）.</p>
<h2 data-id="heading-3">实现</h2>
<h3 data-id="heading-4">设计思路</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a8d91a127c44b70a3d9030e195cd4cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p><code>Shared</code>实例基于<code>BaseShared</code>基类生成</p>
<ul>
<li>
<p>BaseShared基类接收两个构造参数: <code>Pool</code> 、 <code>Action</code></p>
</li>
<li>
<p>Pool由<code>redux</code>的<code>createStore</code>生成，所需参数为所有module的reducer, 也就是说Pool是所有reducer的合集</p>
</li>
<li>
<p>Action负责管理所有module的action</p>
</li>
</ul>
</li>
<li>
<p>每个Module均包含两个部分， <code>reducer</code> 与 <code>action</code></p>
<ul>
<li><code>reducer</code> 即为redux中的reducer类型，可实现对状态树的操作，并最终导出给Pool模块交由<code>redux</code>的<code>createStore</code>进行生成， 对<code>reducer</code>有疑问的，可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fredux.js.org%2Fapi%2Fcreatestore" target="_blank" rel="nofollow noopener noreferrer" title="https://redux.js.org/api/createstore" ref="nofollow noopener noreferrer">redux文档</a></li>
<li><code>action</code> 类似vuex的action, 用于提交<code>mutation</code>(即交由reducer来更改状态)，同时action中的api也将是暴露给使用者的接口（也就是使用过程中是无法直接操作reducer的，只能调用action）</li>
</ul>
</li>
</ol>
<blockquote>
<p>注意： Pool即为Redux文档中的store, 只是一般项目中的状态模块均命名为store， 因此为了避免混淆， 取名为Pool</p>
</blockquote>
<h3 data-id="heading-5">实际代码</h3>
<p>注意： 本次演示我创建了两个项目， 一个叫<b>plat</b>，一个叫<b>micro</b>， 顾名思义， plat项目即为主应用， micro为微应用</p>
<h4 data-id="heading-6">目录</h4>
<p>主应用项目代码里的shared目录  <code>@/shared</code></p>
<pre><code class="copyable">shared
 ├── action.ts
 ├── base.ts
 ├── index.ts
 ├── pool.ts
 └── modules
     ├── locale
     │   ├── action.ts
     │   └── reducer.ts
     └── user
         ├── action.ts
         └── reducer.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">开发流程</h4>
<ol>
<li>以开发user模块开始</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/shared/modules/user/reducer.ts</span>
<span class="hljs-keyword">interface</span> UserInfo &#123;
    <span class="hljs-attr">username</span>: <span class="hljs-built_in">string</span>,
&#125;

<span class="hljs-keyword">interface</span> State &#123;
    userinfo?: UserInfo | Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">never</span>>
&#125;

<span class="hljs-keyword">const</span> state:State = &#123;
    <span class="hljs-attr">userinfo</span>: &#123;&#125;,
&#125;;

<span class="hljs-keyword">type</span> Mutation = &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">string</span>;
    payload: <span class="hljs-built_in">any</span>;
&#125;

<span class="hljs-keyword">const</span> reducer = (userState: State = state, <span class="hljs-attr">mutation</span>: Mutation): <span class="hljs-function"><span class="hljs-params">State</span> =></span> &#123;
    <span class="hljs-keyword">switch</span> (mutation.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'SET_USERINFO'</span>: <span class="hljs-keyword">return</span> &#123;
        ...userState,
        <span class="hljs-attr">userinfo</span>: mutation.payload,
    &#125;; <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">default</span>: <span class="hljs-keyword">return</span> userState;
    &#125;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> reducer;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/shared/modules/user/action.ts</span>
<span class="hljs-keyword">import</span> pool <span class="hljs-keyword">from</span> <span class="hljs-string">'../../pool'</span>;

<span class="hljs-keyword">interface</span> UserInfo &#123;
    <span class="hljs-attr">username</span>: <span class="hljs-built_in">string</span>,
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> userAction = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>,<span class="hljs-comment">// 模块名称，shared将根据名称区分不同模块的action</span>
    <span class="hljs-attr">getUserinfo</span>: (): UserInfo | Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">never</span>> => &#123;
        <span class="hljs-keyword">const</span> state = pool.getState();
        <span class="hljs-keyword">return</span> state.user.userinfo || &#123;&#125;;
    &#125;,
    <span class="hljs-attr">setUserinfo</span>: (userinfo: UserInfo): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
        pool.dispatch(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'SET_USERINFO'</span>,
            <span class="hljs-attr">payload</span>: userinfo,
        &#125;);
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>将user模块的reducer 和 action 分别导入到pool模块和action模块</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/shared/pool.ts</span>
<span class="hljs-keyword">import</span> &#123; combineReducers, createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>;
<span class="hljs-keyword">import</span> userReducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules/user/reducer'</span>;
<span class="hljs-keyword">import</span> localeReducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules/locale/reducer'</span>;

<span class="hljs-keyword">const</span> staticReducers = combineReducers(&#123;
    <span class="hljs-attr">user</span>: userReducer,
    <span class="hljs-attr">locale</span>: localeReducer,
&#125;);

<span class="hljs-keyword">const</span> pool = createStore(staticReducers);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> pool;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/shared/action.ts</span>
<span class="hljs-keyword">import</span> &#123; localeAction &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules/locale/action'</span>;
<span class="hljs-keyword">import</span> &#123; userAction &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules/user/action'</span>;

<span class="hljs-keyword">const</span> actionList = [
    localeAction,
    userAction,
];

<span class="hljs-keyword">const</span> actions = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

actionList.forEach(<span class="hljs-function">(<span class="hljs-params">obj: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; name &#125; = obj;
    <span class="hljs-built_in">Object</span>.keys(obj).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (key !== <span class="hljs-string">'name'</span>) actions.set(<span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>/<span class="hljs-subst">$&#123;key&#125;</span>`</span>, obj[key]);
    &#125;);
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> actions;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>将pool模块和action模块导入到index.ts中，由BaseShared基类构造为shared实例</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/shared/index.ts</span>
<span class="hljs-keyword">import</span> BaseShared <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>;
<span class="hljs-keyword">import</span> pool <span class="hljs-keyword">from</span> <span class="hljs-string">'./pool'</span>;
<span class="hljs-keyword">import</span> actions <span class="hljs-keyword">from</span> <span class="hljs-string">'./action'</span>;

<span class="hljs-keyword">const</span> shared = <span class="hljs-keyword">new</span> BaseShared(pool <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>, actions);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> shared;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/shared/base.ts</span>
<span class="hljs-keyword">import</span> &#123; Store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseShared</span> </span>&#123;
    <span class="hljs-keyword">static</span> pool: Store;

    <span class="hljs-keyword">static</span> actions = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">Pool: Store, action = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()</span>)</span> &#123;
        BaseShared.pool = Pool;
        BaseShared.actions = action;
    &#125;

    <span class="hljs-keyword">public</span> init(listener: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">void</span> &#123;
        BaseShared.pool.subscribe(listener);
    &#125;

    <span class="hljs-keyword">public</span> dispatch(target: <span class="hljs-built_in">string</span>, <span class="hljs-attr">param</span>: <span class="hljs-built_in">any</span> = <span class="hljs-string">''</span>):<span class="hljs-built_in">any</span> &#123;
        <span class="hljs-keyword">const</span> res:<span class="hljs-built_in">any</span> = BaseShared.actions.get(target)(param);
        <span class="hljs-keyword">return</span> res;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>BaseShared基类是整个shared模块的核心，实现action的分发(<b>dispatch</b>), redux订阅事件的初始化(<b>init</b>)</p>
</blockquote>
<p>到这里为止，shared核心内容已经完成，接下来要做的，就是将shared对接qiankun，并在子应用中接收该实例了</p>
<ol start="4">
<li>在主应用项目中，进行qiankun的微应用注册的地方</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; registerMicroApps, start &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;
<span class="hljs-keyword">import</span> shared <span class="hljs-keyword">from</span> <span class="hljs-string">'@/shared'</span>;

registerMicroApps([
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'micro'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8888'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#nav'</span>,
    <span class="hljs-attr">activeRule</span>: <span class="hljs-string">'/micro'</span>,
    <span class="hljs-attr">props</span>: &#123;
        shared
    &#125;,
  &#125;,
]);

start();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>在微应用中，接收shared实例</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/main.ts 已隐藏无关代码</span>
<span class="hljs-keyword">import</span> SharedModule <span class="hljs-keyword">from</span> <span class="hljs-string">'@/shared'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">props: <span class="hljs-built_in">any</span> = &#123;&#125;</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; container, shared = SharedModule.getShared() &#125; = props;
    SharedModule.overloadShared(shared);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SharedModule是什么？ 是微应用用于管理shared实例的模块</p>
<p>微应用中的SharedModule目录如下</p>
<pre><code class="copyable">shared
 ├── index.ts
 └── shared.ts // 当微应用独立运行时（即不存在主应用的传参）， 替代主应用的shared
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/shared/index.ts</span>
<span class="hljs-keyword">import</span> &#123; Shared &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./shared'</span>;<span class="hljs-comment">// 若不需要微应用独立运行，那么此处可以忽视</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SharedModule</span> </span>&#123;
    <span class="hljs-keyword">static</span> shared = <span class="hljs-keyword">new</span> Shared();<span class="hljs-comment">// shared实例</span>

    <span class="hljs-keyword">static</span> listener: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">any</span>> = [];<span class="hljs-comment">// 监听事件列表</span>

    <span class="hljs-comment">/**
     * 重载 shared
     */</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">overloadShared</span>(<span class="hljs-params">shared</span>)</span> &#123;
        SharedModule.shared = shared;
        shared.init(<span class="hljs-function">() =></span> &#123;
            SharedModule.listener.forEach(<span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> &#123;
                fn();
            &#125;);
        &#125;);
    &#125;

    <span class="hljs-comment">/**
     * 初始化监听事件列表
     */</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">subscribe</span>(<span class="hljs-params">fn: <span class="hljs-built_in">any</span></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (!fn) <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'缺少参数'</span>);
        <span class="hljs-keyword">if</span> (fn.length) &#123;
            SharedModule.listener.push(...fn);
        &#125; <span class="hljs-keyword">else</span> &#123;
            SharedModule.listener.push(fn);
        &#125;
    &#125;

    <span class="hljs-comment">/**
     * 获取 shared 实例
     */</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getShared</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> SharedModule.shared;
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> SharedModule;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>在微应用的store中，使用shared实例</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// @/store/index.ts</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;
<span class="hljs-keyword">import</span> SharedModule <span class="hljs-keyword">from</span> <span class="hljs-string">'@/shared'</span>;

Vue.use(Vuex);

<span class="hljs-keyword">let</span> shared:<span class="hljs-built_in">any</span> = <span class="hljs-literal">null</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> UserInfo &#123;
    <span class="hljs-attr">username</span>: <span class="hljs-built_in">string</span>,
&#125;

<span class="hljs-keyword">interface</span> State &#123;
    <span class="hljs-attr">locale</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">userinfo</span>: UserInfo | Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">never</span>>,
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">state</span>: &#123;
        <span class="hljs-attr">locale</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">userinfo</span>: &#123;&#125;,
    &#125;,
    <span class="hljs-attr">mutations</span>: &#123;
        <span class="hljs-attr">SET_LOCALE</span>: <span class="hljs-function">(<span class="hljs-params">state: State, locale: <span class="hljs-built_in">string</span></span>) =></span> &#123;
            state.locale = locale;
        &#125;,
        <span class="hljs-attr">SET_USERINFO</span>: <span class="hljs-function">(<span class="hljs-params">state: State, userinfo: UserInfo</span>) =></span> &#123;
            state.userinfo = userinfo;
        &#125;,
    &#125;,
    <span class="hljs-attr">actions</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">initShared</span>(<span class="hljs-params"></span>)</span> &#123;
            shared = SharedModule.getShared();
            <span class="hljs-comment">// 通过 SharedModule.subscribe 传入回调函数进行订阅， 可以数组形式批量传入</span>
            <span class="hljs-comment">// 当pool内数据有变化时（监听到redux提供的set方法执行了），会通过回调函数统一发布</span>
            <span class="hljs-built_in">this</span>.dispatch(<span class="hljs-string">'setLocale'</span>);
            <span class="hljs-built_in">this</span>.dispatch(<span class="hljs-string">'setUserinfo'</span>);
            SharedModule.subscribe([
                <span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">this</span>.dispatch(<span class="hljs-string">'setLocale'</span>);
                &#125;,
                <span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">this</span>.dispatch(<span class="hljs-string">'setUserinfo'</span>);
                &#125;,
            ]);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">setLocale</span>(<span class="hljs-params">&#123; commit &#125;</span>)</span> &#123;
            <span class="hljs-keyword">const</span> locale = shared.dispatch(<span class="hljs-string">'locale/getLocale'</span>);
            commit(<span class="hljs-string">'SET_LOCALE'</span>, locale);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">setUserinfo</span>(<span class="hljs-params">&#123; commit &#125;</span>)</span> &#123;
            <span class="hljs-keyword">const</span> userinfo = shared.dispatch(<span class="hljs-string">'user/getUserinfo'</span>);
            commit(<span class="hljs-string">'SET_USERINFO'</span>, userinfo);
        &#125;,
    &#125;,
    <span class="hljs-attr">getters</span>: &#123;
        <span class="hljs-attr">locale</span>: <span class="hljs-function">(<span class="hljs-params">state: State</span>) =></span> state.locale,
        <span class="hljs-attr">userinfo</span>: <span class="hljs-function">(<span class="hljs-params">state: State</span>) =></span> state.userinfo,
    &#125;,
    <span class="hljs-attr">modules</span>: &#123;
    &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此已通过shared实例，完成主、微应用之间的通信</p>
<ol start="7">
<li>在页面中实际使用</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 主应用的App.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>plat<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span>></span>username:<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"username"</span>/></span>
          <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleSubmit"</span>></span>submit<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
          userinfo: &#123;&#123; userinfo &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
          language: &#123;&#123; locale &#125;&#125;
          <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleChange"</span>></span>change<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">username</span>: <span class="hljs-string">''</span>,
        &#125;;
    &#125;,
    <span class="hljs-attr">computed</span>: &#123;
        ...mapGetters([<span class="hljs-string">'userinfo'</span>, <span class="hljs-string">'locale'</span>]),
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">handleSubmit</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">const</span> userinfo = &#123;
                <span class="hljs-attr">username</span>: <span class="hljs-built_in">this</span>.username,
            &#125;;
            <span class="hljs-built_in">this</span>.$store.dispatch(<span class="hljs-string">'getInfo'</span>, userinfo);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">handleChange</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">let</span> locale = <span class="hljs-string">''</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.locale === <span class="hljs-string">'zh'</span>) &#123;
                locale = <span class="hljs-string">'en'</span>;
            &#125; <span class="hljs-keyword">else</span> &#123;
                locale = <span class="hljs-string">'zh'</span>;
            &#125;
            <span class="hljs-built_in">this</span>.$store.dispatch(<span class="hljs-string">'setLocale'</span>, locale);
        &#125;
    &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 微应用的HelloWorld.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"hello"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>micro<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>userinfo: &#123;&#123; userinfo &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>language: &#123;&#123; locale &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">computed</span>: &#123;
        ...mapGetters([<span class="hljs-string">'userinfo'</span>, <span class="hljs-string">'locale'</span>]),
    &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f83e2450bc954fe4bc3ed46467c1e65d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">api介绍</h4>

























<table><thead><tr><th>api</th><th>说明</th></tr></thead><tbody><tr><td>SharedModule.overloadShared</td><td>用于重载SharedModule内的shared实例</td></tr><tr><td>SharedModule.getShared()</td><td>获取SharedModule内部的shared实例</td></tr><tr><td>SharedModule.subscribe()</td><td>注册订阅事件（可传数组），在state发生改变后会触发此处订阅的事件</td></tr><tr><td>shared.dispatch()</td><td>类似vuex的store.dispatch,用于调用不同模块的action</td></tr></tbody></table>
<p>api的设计思路：</p>
<p>该shared通信模块，依据redux本身的(state + action => reducer)结合vuex的(state + mutation + action)， 最终设计结构为（state + mutation => reducer + action）。</p>
<p>即：只有mutation能够操作state, 而mutation需要action调用，微应用只能使用主应用暴露出来的action，而主应用可自行决定要暴露的action。</p>
<h2 data-id="heading-9">总结&Todo</h2>
<ol>
<li>这个设计还有个问题，由于该响应式是通过发布-订阅模式实现的， 而该模式依赖于redux提供的subscribe这个api， 但仅凭这个api，我们无法精确地得知究竟哪个属性发生改变， 也就是说只要是state任何属性发生改变， 都会触发subscribe, 当state变得庞大时，该通信模块地性能将不可避免地下降（当然，要非常庞大），因此按模块发布，将会是后续改良的重点</li>
<li>目前在使用或者说上手难度上来说，还有点复杂， 后续看看能不能更高度的抽象， 暴露更简洁的api</li>
<li>目前演示demo已经上传至gitee:  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fsuqingyao%2Fplat" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/suqingyao/plat" ref="nofollow noopener noreferrer">主应用</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fsuqingyao%2Fmicro" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/suqingyao/micro" ref="nofollow noopener noreferrer">微应用</a></li>
</ol></div>  
</div>
            