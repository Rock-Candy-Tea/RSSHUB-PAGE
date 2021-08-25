
---
title: '【万字实战长文】手把手教你赋予Vuex 4.x 更好的 TypeScript体验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8de16069c4fa4b5f84ddf28e0397ba2f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 22:56:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8de16069c4fa4b5f84ddf28e0397ba2f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>Vue 3.x</code> 已经问世很长时间了，但由于我工作技术栈全是 <code>React</code>，所以一直没怎么关注，最近觉着 <code>Vue 3.x</code> 差不多也稳定下来了，抽空学习了一下，不得不说，<code>Vue 3.x</code>对于 <code>TypeScript</code> 的支持性真的不错，配合上 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Djohnsoncodehk.volar" target="_blank" rel="nofollow noopener noreferrer" title="https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar" ref="nofollow noopener noreferrer">Volar</a> 插件，代码写得行云流水</p>
<p>顺便又将 <code>vue-router</code>、<code>vuex</code> 啥的相关生态库也都学习了一下，并且写了个 <code>Demo</code>进行测试，因为既然已经对于 <code>TypeScript</code>有了很好的支持，再加上本人也比较推崇使用 <code>ts</code>，所以就尽量避免写 <code>any</code> 类型，在引入 <code>vuex</code>的时候，看了一下其对于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.vuex.vuejs.org%2Fzh%2Fguide%2Ftypescript-support.html" target="_blank" rel="nofollow noopener noreferrer" title="https://next.vuex.vuejs.org/zh/guide/typescript-support.html" ref="nofollow noopener noreferrer">ts 的支持介绍</a>，看完之后发现这介绍得也太简单了吧，正好最近学习 <code>TypeScript</code> 体操有所心得，遂决定对 <code>vuex</code>这枚钉子挥舞起手中的锤子</p>
<p>直观起见，对 <code>vuex</code> 放在 <code>github</code> 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvuex%2Ftree%2F4.0%2Fexamples%2Fclassic%2Fshopping-cart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vuex/tree/4.0/examples/classic/shopping-cart" ref="nofollow noopener noreferrer">购物车例子</a> 进行改造，主要以 <code>cart</code>模块为例，<code>products</code> 模块类似</p>
<p>本文将要实现的效果</p>
<ol>
<li>能够提示 <code>getters</code>/<code>rootGetters</code> 里所有的可用属性及其类型</li>
<li>能够提示 <code>dispatch</code> 所有的可用 <code>type</code> 及其对应 <code>payload</code> 的类型</li>
<li>能够提示 <code>commit</code> 所有的可用 <code>type</code> 及其对应 <code>payload</code> 的类型</li>
<li>以上效果无论在 <code>module</code>、全局(<code>this.$store</code>)还是 <code>useStore</code> 都有效</li>
</ol>
<p>作为 <code>TypeScript</code> <em>上道</em> 没多久的新手，在撰写本文的时候也遇到了很多问题，但最终都一一解决，本文在写的时候也会将一些我遇到的认为比较有价值的问题提出来以供参考</p>
<p>本文写法循序渐进，并且贴近实际工作场景，可以认为是一个小小的实战体验了，就算你对于 <code>TypeScript</code> 的类型编程不太明白，但看完之后相信也会有所收获</p>
<blockquote>
<ol>
<li>本文完整实例代码已上传到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faccforgit%2Fblog-data%2Ftree%2Fmaster%2Fshopping-cart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/accforgit/blog-data/tree/master/shopping-cart" ref="nofollow noopener noreferrer">github</a>，可以直接拿来主义当做样板代码用在自己的项目里</li>
<li>文中代码的编写环境为 <code>TypeScript 4.3.5</code>，由于使用到了一些高级特性，所以低于此版本可能无法正确编译</li>
</ol>
</blockquote>
<h2 data-id="heading-0">改造 Getters</h2>
<p>根据代码的业务逻辑，先把 <code>state</code> 的类型补充好</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> IProductItem = &#123; <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>, <span class="hljs-attr">inventory</span>: <span class="hljs-built_in">number</span>; quantity: <span class="hljs-built_in">number</span> &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TState = &#123;
  <span class="hljs-attr">items</span>: <span class="hljs-built_in">Array</span><&#123; <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span>, <span class="hljs-attr">quantity</span>: <span class="hljs-built_in">number</span> &#125;>;
  checkoutStatus: <span class="hljs-literal">null</span> | <span class="hljs-string">'successful'</span> | <span class="hljs-string">'failed'</span>
&#125;

<span class="hljs-keyword">const</span> state: <span class="hljs-function">() =></span> TState = <span class="hljs-function">() =></span> (&#123;
  <span class="hljs-attr">items</span>: [],
  <span class="hljs-attr">checkoutStatus</span>: <span class="hljs-literal">null</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后开始给 <code>getters</code> 加类型，先去 <code>vuex</code> 的 <code>types</code> 文件夹下看看有没有已经定义好的类型，发现有个叫 <code>GetterTree</code> 的，先加上</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; GetterTree &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> getters: GetterTree<TState, TRootState> = &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TState</code>就是当前模块的 <code>state</code> 类型，<code>TRootState</code> 则是全局 <code>state</code> 类型，比如这个例子里包含 <code>cart</code> 和 <code>products</code> 两个模块，那么 <code>TRootState</code> 的类型就是：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">import</span> &#123; TState <span class="hljs-keyword">as</span> TCartState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/cart'</span>
<span class="hljs-keyword">import</span> &#123; TState <span class="hljs-keyword">as</span> TProductState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/products'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootState = &#123;
  <span class="hljs-attr">cart</span>: TCartState;
  products: TProductState;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>TRootState</code>的属性 <code>cart</code> 和 <code>products</code> 分别是 <code>cart</code> 模块和 <code>products</code>模块的命名空间名称，后续肯定还会经常遇到的，所以最好统一定义一下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> moduleName = <span class="hljs-string">'cart'</span>
<span class="hljs-comment">// store/modules/products.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> moduleName = <span class="hljs-string">'products'</span>

<span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">import</span> &#123; moduleName <span class="hljs-keyword">as</span> cartModuleName &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/cart'</span>
<span class="hljs-keyword">import</span> &#123; moduleName <span class="hljs-keyword">as</span> productsModuleName &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/products'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootState = &#123;
  [cartModuleName]: TCartState;
  [productsModuleName]: TProductState;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加上 <code>GetterTree</code> 之后，<code>getters</code> 下方法（例如 <code>cartProducts</code>）的第一个参数 <code>state</code> 和第三个参数 <code>rootState</code> 的类型就能自动推导出来了</p>
<p>但是第二个参数 <code>getter</code> 和 第四个参数 <code>rootGetters</code> 的类型依旧是 <code>any</code>，因为 <code>GetterTree</code> 方法给这两个参数的默认类型就是 <code>any</code>，所以需要我们手动改造下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">import</span> &#123; TRootState, TRootGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/index'</span>
<span class="hljs-keyword">import</span> &#123; GettersReturnType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/type'</span>

<span class="hljs-keyword">const</span> GettersTypes = &#123;
  <span class="hljs-attr">cartProducts</span>: <span class="hljs-string">'cartProducts'</span>,
  <span class="hljs-attr">cartTotalPrice</span>: <span class="hljs-string">'cartTotalPrice'</span>
&#125; <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>
<span class="hljs-keyword">type</span> VGettersTypes = (<span class="hljs-keyword">typeof</span> GettersTypes)[keyof <span class="hljs-keyword">typeof</span> GettersTypes]

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TGetters = &#123;
  <span class="hljs-keyword">readonly</span> [key <span class="hljs-keyword">in</span> VGettersTypes]: <span class="hljs-function">(<span class="hljs-params">
    state: TState, getters: GettersReturnType<TGetters, key>, rootState: TRootState, rootGetters: TRootGetters
  </span>) =></span> key <span class="hljs-keyword">extends</span> <span class="hljs-keyword">typeof</span> GettersTypes.cartProducts ? <span class="hljs-built_in">Array</span><&#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    price: <span class="hljs-built_in">number</span>;
    quantity: <span class="hljs-built_in">number</span>;
  &#125;> : <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">// getters</span>
<span class="hljs-keyword">const</span> getters: GetterTree<TState, TRootState> & TGetters = &#123;
  [GettersTypes.cartProducts]: <span class="hljs-function">(<span class="hljs-params">state, getters, rootState, rootGetters</span>) =></span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新增 <code>GettersTypes</code> 对象，用于明确枚举 <code>getters</code> 的 <code>key</code>，新增 <code>TGetters</code> 类型用于覆盖 <code>GetterTree</code></p>
<p>主要看用于定义 <code>getters</code> 的类型 <code>GettersReturnType<TGetters, key></code>，用于获取 <code>getters</code> 的返回类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/type.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> GettersReturnType<T, K <span class="hljs-keyword">extends</span> keyof T> = &#123;
  [key <span class="hljs-keyword">in</span> Exclude<keyof T, K>]: T[key] <span class="hljs-keyword">extends</span> (...args: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">any</span> ? ReturnType<T[key]> : <span class="hljs-built_in">never</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><code>Exclude</code> 用于将 <code>K</code> 从联合类型 <code>keyof T</code> 里排除出去</li>
<li><code>ReturnType</code> 用于返回函数的返回类型，这里就是获取到 <code>getters</code> 的返回类型</li>
</ol>
</blockquote>
<p><code>TRootGetters</code> 就是全局 <code>getters</code>，其 <code>key</code> 就是模块 <code>getters</code>的命名空间 + <code>key</code>，值还是模块 <code>getters</code>对应的值，利用 <code>ts</code> 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-4-1.html%23template-literal-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-1.html#template-literal-types" ref="nofollow noopener noreferrer">模板字符串</a> 能力，将命名空间与 <code>getters</code> 的 <code>key</code> 进行组合，得到 <code>TRootGetters</code> 的 <code>key</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/type.ts</span>
<span class="hljs-keyword">type</span> RootGettersReturnType<T <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>, TModuleName <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>> = &#123;
  <span class="hljs-keyword">readonly</span> [key <span class="hljs-keyword">in</span> keyof T <span class="hljs-keyword">as</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;TModuleName&#125;</span>/<span class="hljs-subst">$&#123;Extract<key, <span class="hljs-built_in">string</span>>&#125;</span>`</span>]: T[key] <span class="hljs-keyword">extends</span> (<span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>) ? ReturnType<T[key]> : <span class="hljs-built_in">never</span>
&#125;

<span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootGetters = RootGettersReturnType<TCartGetters, <span class="hljs-keyword">typeof</span> cartModuleName>
  & RootGettersReturnType<TProductsGetters, <span class="hljs-keyword">typeof</span> productsModuleName>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ol>
<li><code>GettersTypes</code> 设计成一个 <code>js</code>对象而不是 <code>enum</code>，首先是考虑到这里并不是一个枚举的适用场景，其次是为了明确 <code>getter</code> 的 <code>key</code>，以及 <code>key</code> 对应的方法及其返回值，如果使用 <code>enum</code>，会因为类型模糊导致丢失 <code>key</code> 与 对应的方法及其返回值之间的联系丢失</li>
<li><code>GettersTypes</code> 必须使用 <code>as const</code> 进行修饰，详细可见我之前 <a href="https://juejin.cn/post/6995786330533806117" target="_blank" title="https://juejin.cn/post/6995786330533806117">发过的一篇文章</a>，里面有关于 <code>Const Assertions</code> 的描述</li>
<li><code>Extract<key, string></code>写法是由于 <code>TypeScript</code> 存在的一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMicrosoft%2FTypeScript%2Fissues%2F25260" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Microsoft/TypeScript/issues/25260" ref="nofollow noopener noreferrer">feature</a></li>
<li><code>[key in keyof T as </code> <code>$&#123;TModuleName&#125;/$&#123;Extract<key, string>&#125;]</code> 的写法可见于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-4-1.html%23key-remapping-in-mapped-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-1.html#key-remapping-in-mapped-types" ref="nofollow noopener noreferrer">Key Remapping in Mapped Types</a></li>
</ol>
</blockquote>
<p>经过上述改造后，现在就可以在编辑器里<code>点</code>出 <code>getters</code> 和 <code>rootGetters</code> 上所有的属性了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8de16069c4fa4b5f84ddf28e0397ba2f~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff39d24b66994ea68473a9f5b7f4d684~tplv-k3u1fbpfcp-watermark.image" alt="2.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">改造 Mutions</h2>
<p>先去 <code>vuex</code> 里看下有没有定义好的类型，发现有个叫 <code>ActionTree</code>，先写上去</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">import</span> &#123; MutationTree &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">const</span> mutations: MutationTree<TState> = &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为这个 <code>MutationTree</code> 的 <code>key</code> 的类型是 <code>string</code>，所以是没法直接 <code>点</code> 出来的，需要手动再写个类型进行覆盖，为了明确 <code>mutation</code> 的 <code>key</code>，还是和 <code>getters</code>一样，先定义好对应的对象变量 <code>MutationTypes</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">import</span> &#123; MutationTree &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> MutationTypes = &#123;
  <span class="hljs-attr">pushProductToCart</span>: <span class="hljs-string">'pushProductToCart'</span>,
  <span class="hljs-attr">incrementItemQuantity</span>: <span class="hljs-string">'incrementItemQuantity'</span>,
  <span class="hljs-attr">setCartItems</span>: <span class="hljs-string">'setCartItems'</span>,
  <span class="hljs-attr">setCheckoutStatus</span>: <span class="hljs-string">'setCheckoutStatus'</span>
&#125; <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>
<span class="hljs-keyword">type</span> TMutations = &#123;
  [MutationTypes.pushProductToCart]<T <span class="hljs-keyword">extends</span> &#123; <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span> &#125;>(state: TState, <span class="hljs-attr">payload</span>: T): <span class="hljs-built_in">void</span>;
  [MutationTypes.incrementItemQuantity]<T <span class="hljs-keyword">extends</span> &#123; <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span> &#125;>(state: TState, <span class="hljs-attr">payload</span>: T): <span class="hljs-built_in">void</span>;
  [MutationTypes.setCartItems]<T <span class="hljs-keyword">extends</span> &#123; <span class="hljs-attr">items</span>: TState[<span class="hljs-string">"items"</span>] &#125;>(state: TState, <span class="hljs-attr">payload</span>: T): <span class="hljs-built_in">void</span>;
  [MutationTypes.setCheckoutStatus](state: TState, <span class="hljs-attr">payload</span>: TState[<span class="hljs-string">"checkoutStatus"</span>]): <span class="hljs-built_in">void</span>;
&#125;
<span class="hljs-comment">// mutations</span>
<span class="hljs-keyword">const</span> mutations: MutationTree<TState> & TMutations = &#123;
  [MutationTypes.pushProductToCart] (state, &#123; id &#125;) &#123;
    state.items.push(&#123; id, <span class="hljs-attr">quantity</span>: <span class="hljs-number">1</span> &#125;)
  &#125;,
  [MutationTypes.incrementItemQuantity] (state, &#123; id &#125;) &#123;
    <span class="hljs-keyword">const</span> cartItem = state.items.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.id === id)
    cartItem && cartItem.quantity++
  &#125;,
  [MutationTypes.setCartItems] (state, &#123; items &#125;) &#123;
    state.items = items
  &#125;,
  [MutationTypes.setCheckoutStatus] (state, status) &#123;
    state.checkoutStatus = status
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37961ce125864161a8a5627a35be7272~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer">
<code>Mutions</code> 的改造还是比较简单的，这就完事了</p>
<h2 data-id="heading-2">改造 Actions</h2>
<p>先定义好对应的枚举对象变量</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ActionTypes = &#123;
  <span class="hljs-attr">checkout</span>: <span class="hljs-string">'checkout'</span>,
  <span class="hljs-attr">addProductToCart</span>: <span class="hljs-string">'addProductToCart'</span>,
&#125; <span class="hljs-keyword">as</span> <span class="hljs-keyword">const</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再找到预先定义好的类型，加上去</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">const</span> actions: ActionTree<TState, TRootState> &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后照例写个类型 <code>TActions</code> 进行覆盖</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">type</span> TActions = &#123;
  [ActionTypes.checkout](context: <span class="hljs-built_in">any</span>, <span class="hljs-attr">payload</span>: TState[<span class="hljs-string">"items"</span>]): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">void</span>>
  [ActionTypes.addProductToCart](context: <span class="hljs-built_in">any</span>, <span class="hljs-attr">payload</span>: IProductItem): <span class="hljs-built_in">void</span>
&#125;
<span class="hljs-keyword">const</span> actions: ActionTree<TState, TRootState> & TActions &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>context</code> 还是个 <code>any</code>类型，这肯定是不行的，从 <code>vuex</code> 已经给定的类型定义来看，<code>context</code> 是一个对象，其具有5个属性：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> ActionContext<S, R> &#123;
  <span class="hljs-attr">dispatch</span>: Dispatch;
  commit: Commit;
  state: S;
  getters: <span class="hljs-built_in">any</span>;
  rootState: R;
  rootGetters: <span class="hljs-built_in">any</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>state</code>、<code>getters</code>、<code>rootState</code>、<code>rootGetters</code> 的类型都已经确定了，至于 <code>dispatch</code> 和 <code>commit</code>，类型签名的 <code>key</code> 都是 <code>string</code>，所以 <code>点</code> 不出来，需要对着这两个进行改造</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/type.ts</span>
<span class="hljs-keyword">import</span> &#123; ActionContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">type</span> TObjFn = Record<<span class="hljs-built_in">string</span>, <span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TActionContext<
  TState, TRootState,
  TActions <span class="hljs-keyword">extends</span> TObjFn, TRootActions <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, TObjFn>,
  TMutations <span class="hljs-keyword">extends</span> TObjFn, TRootMutations <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, TObjFn>,
  TGetters <span class="hljs-keyword">extends</span> TObjFn, TRootGetters <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>
> = Omit<ActionContext<TState, TRootState>, <span class="hljs-string">'commit'</span> | <span class="hljs-string">'dispatch'</span> | <span class="hljs-string">'getters'</span> | <span class="hljs-string">'rootGetters'</span>>
  & TCommit<TMutations, TRootMutations, <span class="hljs-literal">false</span>>
  & TDispatch<TActions, TRootActions, <span class="hljs-literal">false</span>>
  & &#123;
    <span class="hljs-attr">getters</span>: &#123;
      [key <span class="hljs-keyword">in</span> keyof TGetters]: ReturnType<TGetters[key]>
    &#125;
  &#125;
  & &#123; <span class="hljs-attr">rootGetters</span>: TRootGetters &#125;

<span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">type</span> TUserActionContext = TActionContext<TState, TRootState, TActions, TRootActions, TMutations, TRootMutations, TGetters, TRootGetters>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TActions = &#123;
  [ActionTypes.checkout]: <span class="hljs-function">(<span class="hljs-params">context: TUserActionContext, payload: TState[<span class="hljs-string">"items"</span>]</span>) =></span> <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">void</span>>
  [ActionTypes.addProductToCart]: <span class="hljs-function">(<span class="hljs-params">context: TUserActionContext, payload: IProductItem</span>) =></span> <span class="hljs-built_in">void</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给 <code>context</code> 定义了类型 <code>TUserActionContext</code>，底层是 <code>TActionContext</code>，<code>TActionContext</code>依旧借助了 <code>vuex</code> 提供的类型 <code>ActionContext</code>的能力，沿用对 <code>state</code>、<code>rootState</code> 类型的支持，需要手动重写的是 <code>dispatch</code>、<code>commit</code>、<code>getters</code>、<code>rootGetters</code> ，那么使用 <code>Omit</code> 将这几个类型挑出来另行定义</p>
<p>由于可以在<code>module</code>之间相互调用 <code>dispatch</code>、<code>commit</code>，所以给 <code>TCommit</code>、<code>TDispatch</code>传入第三个参数用于标识是位于当前模块内还是位于其他模块或者全局环境内，主要用于决定是否添加模块命名空间，例如 <code>cart/checkout</code></p>
<p><code>commit</code>依赖于 <code>mutation</code>，所以给 <code>TCommit</code> 再传入 <code>TMutations</code>、<code>TRootMutations</code>；同理，给 <code>TDispatch</code> 传入 <code>TActions</code>、<code>TRootActions</code></p>
<p>和 <code>TRootState</code>、<code>TRootActions</code> 类似，<code>TRootMutations</code>、<code>TRootActions</code> 也即是所有 <code>module</code>下 <code>mutaions</code> 和 <code>actions</code> 的集合</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">import</span> &#123;
  moduleName <span class="hljs-keyword">as</span> cartModuleName,
  TActions <span class="hljs-keyword">as</span> TCartActions, TMutations <span class="hljs-keyword">as</span> TCartMutations, TCartStore
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/cart'</span>
<span class="hljs-keyword">import</span> &#123;
  moduleName <span class="hljs-keyword">as</span> productsModuleName,
  TActions <span class="hljs-keyword">as</span> TProductsActions, TMutations <span class="hljs-keyword">as</span> TProductsMutations, TProductsStore
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/products'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootActions = &#123;
  [cartModuleName]: TCartActions;
  [productsModuleName]: TProductsActions;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootMutations = &#123;
  [cartModuleName]: TCartMutations;
  [productsModuleName]: TProductsMutations;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">getters & rootGetters</h3>
<pre><code class="hljs language-ts copyable" lang="ts">&#123;
  <span class="hljs-attr">getters</span>: &#123;
    [key <span class="hljs-keyword">in</span> keyof TGetters]: ReturnType<TGetters[key]>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>覆盖原有的 <code>getters</code>，主要就是给明确定义属性的 <code>key</code>，以及 <code>key</code> 对应的类型，即 <code>getter</code> 的类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootGetters = RootGettersReturnType<TCartGetters, <span class="hljs-keyword">typeof</span> cartModuleName>
  & RootGettersReturnType<TProductsGetters, <span class="hljs-keyword">typeof</span> productsModuleName>

<span class="hljs-comment">// store/type.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> RootGettersReturnType<T <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>, TModuleName <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>> = &#123;
  <span class="hljs-keyword">readonly</span> [key <span class="hljs-keyword">in</span> keyof T <span class="hljs-keyword">as</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;TModuleName&#125;</span>/<span class="hljs-subst">$&#123;Extract<key, <span class="hljs-built_in">string</span>>&#125;</span>`</span>]: T[key] <span class="hljs-keyword">extends</span> (<span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>)
    ? ReturnType<T[key]>
    : <span class="hljs-built_in">never</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>rootGetters</code> 即是在全局范围内可访问的 <code>getters</code>，带有命名空间</p>
<p>这一步做完之后就可以在 <code>getters</code>、<code>rootGetters</code> 上 <code>点</code> 出所有的可用属性了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3d12dc8213542c4b9e9b502e5e5a30c~tplv-k3u1fbpfcp-watermark.image" alt="11.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bacb389c4d554bcba4887235b0b78918~tplv-k3u1fbpfcp-watermark.image" alt="12.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">TCommit</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/type.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TCommit<
  TMutations <span class="hljs-keyword">extends</span> TObjFn, TRootMutations <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, TObjFn>, UseInGlobal <span class="hljs-keyword">extends</span> <span class="hljs-built_in">boolean</span>
> = &#123;
  commit<
    M = UseInGlobal <span class="hljs-keyword">extends</span> <span class="hljs-literal">true</span>
      ? UnionToIntersection<FlatRootObj<TRootMutations>>
      : (UnionToIntersection<FlatRootObj<TRootMutations>> & TMutations),
    K <span class="hljs-keyword">extends</span> keyof M = keyof M
  >(
    key: K,
    <span class="hljs-attr">payload</span>: Parameters<Extract<M[K], <span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>>>[<span class="hljs-number">1</span>],
    options?: CommitOptions
  ): <span class="hljs-built_in">void</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>commit</code>是一个方法，接收三个参数，最后一个参数 <code>options</code> 依旧是使用 <code>vuex</code> 提供的，返回值固定是 <code>void</code></p>
<p><code>commit</code>第一个参数为提交的 <code>type</code>，存在两种情况，在 <code>module</code> 内部使用（<code>UseInGlobal</code> 为 <code>false</code>）和在其他<code>module</code>或者全局使用（<code>UseInGlobal</code> 为 <code>false</code>）,前者的<code>type</code>不需要命名空间前缀，而后者需要，所以使用 <code>UseInGlobal</code> 区分开这两种情况，方便后续判断</p>
<p><code>TRootMutations</code> 是所有 <code>module</code> 下 <code>mutations</code>总的集合，所以需要借助 <code>FlatRootObj</code> 进行拍平</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> FlatRootObj<T <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, TObjFn>> = T <span class="hljs-keyword">extends</span> Record<infer U, TObjFn>
  ? U <span class="hljs-keyword">extends</span> keyof T ? &#123;
    [key <span class="hljs-keyword">in</span> keyof T[U] <span class="hljs-keyword">as</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;Extract<U, <span class="hljs-built_in">string</span>>&#125;</span>/<span class="hljs-subst">$&#123;Extract<key, <span class="hljs-built_in">string</span>>&#125;</span>`</span>]: T[U][key]
  &#125; : <span class="hljs-built_in">never</span> : <span class="hljs-built_in">never</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>FlatRootObj</code> 拍平之后的结果是一个联合类型，拍平出来的对象的 <code>key</code> 已经添加了命名空间，但这是一个联合类型，我们希望结果是一个交叉类型，所以再借助 <code>UnionToIntersection</code> 将联合类型转为交叉类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> UnionToIntersection<U <span class="hljs-keyword">extends</span> TObjFn> =
  (U <span class="hljs-keyword">extends</span> TObjFn ? <span class="hljs-function">(<span class="hljs-params">k: U</span>) =></span> <span class="hljs-built_in">void</span> : <span class="hljs-built_in">never</span>) <span class="hljs-keyword">extends</span> (<span class="hljs-function">(<span class="hljs-params">k: infer I</span>) =></span> <span class="hljs-built_in">void</span>) ? I : <span class="hljs-built_in">never</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>UnionToIntersection</code> 用于将联合类型转为交叉类型，即 <code>A | B | C</code> => <code>A & B & C</code>，原理可见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-2-8.html%23type-inference-in-conditional-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-8.html#type-inference-in-conditional-types" ref="nofollow noopener noreferrer">type-inference-in-conditional-types</a></p>
</blockquote>
<p>逻辑比较饶，可能看得不是太清楚，大概解释下 <code>FlatRootObj</code> 和 <code>UnionToIntersection</code> 所起的作用</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> A = &#123; <span class="hljs-attr">q</span>: <span class="hljs-number">1</span>; w: <span class="hljs-string">'2'</span> &#125;
<span class="hljs-keyword">type</span> B = &#123; <span class="hljs-attr">e</span>: []; r: <span class="hljs-literal">true</span>; &#125;
<span class="hljs-keyword">type</span> C = &#123; <span class="hljs-attr">a</span>: A; b: B; &#125;

<span class="hljs-keyword">type</span> D = FlatRootObj<C>
<span class="hljs-comment">// => &#123; "a/q": 1; "a/w": '2'; &#125; | &#123; "b/e": []; "b/r": true; &#125;</span>
<span class="hljs-keyword">type</span> E = UnionToIntersection<D>
<span class="hljs-comment">// => &#123; "a/q": 1; "a/w": '2'; &#125; & &#123; "b/e": []; "b/r": true; &#125;</span>
<span class="hljs-comment">// 也即 &#123; "a/q": 1; "a/w": '2'; "b/e": []; "b/r": true; &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个参数 <code>payload</code> 是提交的值，也就是 <code>TMutations</code>类型方法签名的第一个参数，借助 <code>Parameters</code> 内置方法可以取出函数的参数</p>
<p>到了这一步，就可以在 <code>commit</code> 后面 <code>点</code> 出所有可用属性了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f81e6d980f104512958bd30e18ea902a~tplv-k3u1fbpfcp-watermark.image" alt="15.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>甚至可以自动根据第一个选中的 <code>key</code>，自动提示第二个 <code>payload</code> 的参数类型</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbad70bf0b1d47a8b0e2ca9417b9c0a6~tplv-k3u1fbpfcp-watermark.image" alt="16.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">TDispatch</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TDispatch<
  TActions <span class="hljs-keyword">extends</span> TObjFn, TRootActions <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, TObjFn>, UseInGlobal <span class="hljs-keyword">extends</span> <span class="hljs-built_in">boolean</span>,
> = &#123;
  dispatch<
    M = UseInGlobal <span class="hljs-keyword">extends</span> <span class="hljs-literal">true</span>
      ? UnionToIntersection<FlatRootObj<TRootActions>>
      : (UnionToIntersection<FlatRootObj<TRootActions>> & TActions),
    K <span class="hljs-keyword">extends</span> keyof M = keyof M
  >(
    key: K,
    <span class="hljs-attr">payload</span>: Parameters<Extract<M[K], <span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>>>[<span class="hljs-number">1</span>],
    options?: DispatchOptions
  ): <span class="hljs-built_in">Promise</span><ReturnType<Extract<M[K], <span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>>>>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实和 <code>TCommit</code> 差不多，只不过它们的数据来源不一样，并且 <code>dispatch</code> 返回的是一个 <code>Promise</code>，就不多说了</p>
<p>上述类型写完之后，就可以愉快地看到编辑器会智能地给出包括自身 <code>module</code> 内以及其他 <code>module</code>内所有可<code>dispatch</code>、<code>commit</code> 方法的参数签名了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f827cefbb847f0a483b1c54cbc8b05~tplv-k3u1fbpfcp-watermark.image" alt="13.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样的，当你写完 <code>dispatch</code>、<code>commit</code> 的第一个<code>type</code>参数之后，还能正确地给出第二个参数 <code>payload</code> 的准确类型</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/078155b251164ae095880f09107cf6aa~tplv-k3u1fbpfcp-watermark.image" alt="14.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">$store</h2>
<p>事情还没完，除了在 <code>module</code> 内获取 <code>getters</code>、<code>state</code>，调用 <code>dispatch</code>、<code>commit</code> 之外，我还可以全局使用，比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">this</span>.$store.dispatch(...)
<span class="hljs-built_in">this</span>.$store.commit(...)
<span class="hljs-built_in">this</span>.$store.getters.xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了上面的基础，这个就简单了，只需要把类型映射到全局即可</p>
<p>首先在 <code>shims-vue.d</code> 增加 <code>$store</code> 的签名</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// shims-vue.d</span>
<span class="hljs-keyword">import</span> &#123; TRootStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/index'</span>

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'@vue/runtime-core'</span> &#123;
  <span class="hljs-keyword">interface</span> ComponentCustomProperties &#123;
    <span class="hljs-attr">$store</span>: TRootStore
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 <code>TRootStore</code> 就是所有 <code>module</code> 的 <code>store</code> 的集合，和 <code>TRootState</code>、<code>TRootActions</code> 差不多</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">import</span> &#123; TCartStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/cart'</span>
<span class="hljs-keyword">import</span> &#123; TProductsStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/modules/products'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootStore = TCartStore & TProductsStore
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么看下 <code>TCartStore</code> 是怎么得到的</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/modules/cart.ts</span>
<span class="hljs-keyword">import</span> &#123; TStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/type'</span>
<span class="hljs-keyword">import</span> &#123; TRootActions, TRootMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/index'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> moduleName = <span class="hljs-string">'cart'</span>
<span class="hljs-keyword">type</span> TModuleName = <span class="hljs-keyword">typeof</span> moduleName

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TCartStore = TStore<
  &#123; [moduleName]: TState &#125;,
  TCommit<TMutations, TRootMutations, <span class="hljs-literal">true</span>>,
  TDispatch<TActions, TRootActions, <span class="hljs-literal">true</span>>,
  &#123;
    [key <span class="hljs-keyword">in</span> keyof TGetters <span class="hljs-keyword">as</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;TModuleName&#125;</span>/<span class="hljs-subst">$&#123;key&#125;</span>`</span>]: ReturnType<TGetters[key]>
  &#125;
>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>借助了 <code>TStore</code> 类型，接收四个参数，分别是当前 <code>module</code> 的 <code>TState</code>、<code>TCommit</code>、<code>TDispatch</code> 以及 <code>getters</code></p>
<p>最后一个 <code>getters</code> 额外处理了一下，因为在全局调用 <code>getters</code> 的时候，肯定需要加命名空间的，所以这里使用模板字符串先把 <code>TModuleName</code> 给拼接上</p>
<p>再看 <code>TStore</code> 的实现</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/type.ts</span>
<span class="hljs-keyword">import</span> &#123; Store <span class="hljs-keyword">as</span> VuexStore, CommitOptions, DispatchOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TStore<
  TState <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>,
  TCommit <span class="hljs-keyword">extends</span> &#123; commit(<span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>, payload?: <span class="hljs-built_in">any</span>, options?: CommitOptions | <span class="hljs-literal">undefined</span>): <span class="hljs-built_in">void</span> &#125;,
  TDispatch <span class="hljs-keyword">extends</span> &#123; dispatch(<span class="hljs-keyword">type</span>: <span class="hljs-built_in">string</span>, payload?: <span class="hljs-built_in">any</span>, options?: DispatchOptions | <span class="hljs-literal">undefined</span>): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">any</span>> &#125;,
  TGetters
> = Omit<VuexStore<TState>, <span class="hljs-string">'commit'</span> | <span class="hljs-string">'dispatch'</span> | <span class="hljs-string">'getters'</span>> & TCommit & TDispatch & &#123;
  <span class="hljs-attr">getters</span>: TGetters
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>借助了 <code>vuex</code> 提供好的类型 <code>VuexStore</code>，然后因为 <code>commit</code>、<code>dispatch</code>、<code>getters</code> 是自定义的，所以把这三个剔除出来，换成自己定义的 <code>TCommit</code>、<code>TDispatch</code>、<code>TGetters</code></p>
<p>这里再次对 <code>TGetters</code> 进行了额外处理，因为全局使用 <code>$store</code> 调用 <code>getters</code>的时候不是直接调用的，而是需要通过 <code>getters</code> 属性，即：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">this</span>.$store.getters[<span class="hljs-string">'cart/cartProducts'</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后 <code>useStore</code> 同样也需要赋予相同的类型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// store/index.ts</span>
<span class="hljs-keyword">import</span> &#123; InjectionKey &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; Store <span class="hljs-keyword">as</span> VuexStore, useStore <span class="hljs-keyword">as</span> baseUseStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> TRootStore = TCartStore & TProductsStore

<span class="hljs-keyword">const</span> key: InjectionKey<VuexStore<TRootState>> = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'store'</span>)

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useStore</span> (<span class="hljs-params"></span>): <span class="hljs-title">TRootStore</span> </span>&#123;
  <span class="hljs-keyword">return</span> baseUseStore(key)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以愉快地在全局使用 <code>$store</code>了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48e6bd7bdbf5498b9501fe066c536619~tplv-k3u1fbpfcp-watermark.image" alt="7.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d31a45fbdb6b4784ab67f6cefe34454d~tplv-k3u1fbpfcp-watermark.image" alt="8.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db5bcb10c09544148895488c95ad83bb~tplv-k3u1fbpfcp-watermark.image" alt="9.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>包括 <code>useStore</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/130d52e8f09548b08c19da9610492c00~tplv-k3u1fbpfcp-watermark.image" alt="10.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">小结</h2>
<p>寻找资料的过程中，发现了一个第三方支持 <code>vuex</code> 的 <code>TypeScript</code> 库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FClickerMonkey%2Fvuex-typescript-interface" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ClickerMonkey/vuex-typescript-interface" ref="nofollow noopener noreferrer">vuex-typescript-interface</a>，但感觉支持性还不是那么好</p>
<p>当然了，本文对于 <code>vuex</code> 的 <code>TypeScript</code> 支持也远没有达到完美的地步，比如 <code>mapState</code>、<code>mapActions</code>、多级嵌套 <code>module</code> 等都没有支持，但相对于官方给的 <code>TypeScript</code>支持，显然又好了很多</p>
<p>为了获得良好的类型体验，类型体操的代码量必然不会少到哪里去，甚至比肩真正的业务代码，但这也只是在项目初期，随着项目逐渐复杂化，类型代码占比肯定越来越少，但作用却可以不减当初</p>
<p>对于 <code>javascript</code> 这种弱类型语言而言，能在庞大臃肿的多人协作项目代码里正确地 <code>点</code> 出一个变量的所有属性，我愿称之为 <strong>第二注释</strong></p>
<h2 data-id="heading-8">招个聘</h2>
<p>最后，打个广告吧~</p>
<p><strong>字节商业产品-客户增长团队急聘优秀前后端同学~</strong></p>
<p>跨端、商业智能BI、交易变现、CRM 等多款商业化产品规划清晰、资金充足，现在就差个程序员了（手动狗头）</p>
<p>什么，你问我到底是不是真的有 <code>hc</code> 是不是找人刷 <code>kpi</code>的？内推系统上一溜职位后面的内推加急标签难道是逗人玩的吗？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fd60111e59448c4b2f37e0eaa5c256b~tplv-k3u1fbpfcp-watermark.image" alt="z1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有发我简历的同学，我保证亲自跟进 <strong>从简历进入系统到面试结束全流程，随时可询问我面试进度</strong>，心动你就行动，简历发我邮箱 <strong><a href="https://link.juejin.cn/?target=mailto%3Akother%40foxmail.com" target="_blank" title="mailto:kother@foxmail.com" ref="nofollow noopener noreferrer">kother@foxmail.com</a></strong></p></div>  
</div>
            