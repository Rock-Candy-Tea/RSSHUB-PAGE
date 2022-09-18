
---
title: '藏在 Vue2 中的 composition API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fd96482db284d55bde5ba09ecd66a71~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sun, 18 Sep 2022 01:40:09 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fd96482db284d55bde5ba09ecd66a71~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>熟悉 <strong>Vue2</strong> 的小伙伴们都清楚，<strong>Vue2</strong> 推崇 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv2.cn.vuejs.org%2Fv2%2Fapi%2F%23%25E9%2580%2589%25E9%25A1%25B9-%25E6%2595%25B0%25E6%258D%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://v2.cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E6%95%B0%E6%8D%AE" ref="nofollow noopener noreferrer">options API</a>，这对新人来说上手很简单，但也伴随而来了一些小问题，比如<strong>逻辑服用很困难</strong>，<strong>this黑盒</strong>、<strong>mixins命名冲突</strong>等等。后来 <strong>Vue3</strong> 通过 <a href="https://link.juejin.cn/?target=..." target="_blank" title="..." ref="nofollow noopener noreferrer">composition API</a> 解决了这些痛点。</p>
<p>但也因为采用了过于前卫的 <a href="https://link.juejin.cn/?target=..." target="_blank" title="..." ref="nofollow noopener noreferrer">Proxy</a> ，让一些必须考虑兼容性的应用无法立刻升级。所以历史问题依旧存在。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fd96482db284d55bde5ba09ecd66a71~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="你是个好框架.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所幸，近期笔者也遇到了类似的苦恼，最终发现了属于 <strong>Vue2</strong> 的 <a href="https://link.juejin.cn/?target=..." target="_blank" title="..." ref="nofollow noopener noreferrer">composition API</a>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa482d15546e46eab6baf412e3a8f18d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="20220917101234.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>嚯～这不仔细看还真以为是 <strong>Vue3</strong> 哈，但我们可是额外保留了 <strong>Vue2</strong> 良好的 <strong>兼容性</strong> 哦～</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/103a556663c24fc6963735b5661a3d88~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="真滴嘛你真好.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于是如何实现的，让我们一起来看一下吧～</p>
<h1 data-id="heading-1">Vue2的祖训</h1>
<p>首先大家都清楚，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv2.cn.vuejs.org%2Fv2%2Fapi%2F%23%25E9%2580%2589%25E9%25A1%25B9-%25E6%2595%25B0%25E6%258D%25AE" target="_blank" rel="nofollow noopener noreferrer" title="https://v2.cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E6%95%B0%E6%8D%AE" ref="nofollow noopener noreferrer">options API</a> 推荐我们通过 <code>data</code> 创建 <strong>响应式对象</strong> ；在 <code>methods</code> 中声明方法；而且还有一套完整的 <a href="https://link.juejin.cn/?target=..." target="_blank" title="..." ref="nofollow noopener noreferrer">生命周期函数</a> 可供使用。</p>
<p>除此之外，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv2.cn.vuejs.org%2Fv2%2Fguide%2Finstance.html%23%25E7%2594%259F%25E5%2591%25BD%25E5%2591%25A8%25E6%259C%259F%25E5%259B%25BE%25E7%25A4%25BA" target="_blank" rel="nofollow noopener noreferrer" title="https://v2.cn.vuejs.org/v2/guide/instance.html#%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%9B%BE%E7%A4%BA" ref="nofollow noopener noreferrer">官网</a> 还贴心地告诉大家在各个 <strong>生命周期函数</strong> 中应该做那些事情，这样一来新手很快就能上手写代码了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a354a515dc5b47bf8bbe46a5eaf997ec~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="面向文档编程，so easy.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中关于 <code>beforeCreate</code> 是这样讲的，</p>
<blockquote>
<p>在实例初始化之后,进行数据侦听和事件/侦听器的配置之前同步调用</p>
</blockquote>
<p>也就是说在 <code>beforeCreate</code> 阶段没有完成 <strong>数据响应式</strong> ，因此很多教程会告诉大家不要在这个阶段操作 <code>this.data</code> ，大部分行为最好在 <code>mounted</code> 阶段编写。</p>
<p>久而久之这便形成了一个公认的规则：尽量不要在 <code>beforeCreate</code> 中操作 <code>this.data</code>。</p>
<h1 data-id="heading-2">在规则的边缘试探</h1>
<p>对 <strong>Vue</strong> 有一定研究的同学可能尝试过在 <strong>实例</strong> 之外的地方，用 <code>Vue.util.defineReactive</code> 或 <code>Vue.observable</code> 创建 <strong>响应式对象</strong>。</p>
<p>像这样：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/172a41cd6d76407cbff6615602f5a71f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>于是乎现我们发现，好像 <strong>定义响应式变量</strong> 也可以不定义在 <code>data</code> 、<strong>方法</strong> 也可以不放在 <code>methods</code>。</p>
<p>但是绑定在 <strong>原型链</strong> 上有点不妥，而且变量的作用域也不合适，</p>
<p>所以我们尝试在 <code>beforeCreate</code> 阶段做这些事情，顺便绑定到 <strong>this</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/709df84d290f4fb494cd6326dc658f89~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现这种方式也不错，逻辑比较集中，不用像之前那样上下来回翻文件了。</p>
<p>于是我们做了一个更大胆的尝试～</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/754a382a907e451294a8a0cfe8cd6696~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="住手吧.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">我做了一个违背祖训的决定</h1>
<p>很快我们发现这种写法像极了 <strong>Vue3</strong> 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fguide%2Fintroduction.html%23api-styles" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/guide/introduction.html#api-styles" ref="nofollow noopener noreferrer">composition API</a> ，只是没有我们重写 <strong>响应式原理</strong> ，一切改造都是基于 <strong>Vue2</strong> 现有的 <strong>API</strong>，所以也不存在兼容性问题。</p>
<p>既然如此，何不借助 <strong>Vue2</strong> 的现有逻辑创造一个新的 <a href="https://link.juejin.cn/?target=..." target="_blank" title="..." ref="nofollow noopener noreferrer">composition API</a> 呢，既不用担心兼容性问题，将来迁移 <strong>Vue3</strong> 时还无需做过多改动。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4ad586075f249cdb8b67597250da1db~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="惊讶.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们以常用的几个API为例，用 <strong>Vue2</strong> 来实现一下</p>
<h2 data-id="heading-4">defineComponent</h2>
<p>在 <strong>Vue3</strong> 中，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fapi%2Fgeneral.html%23definecomponent" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/api/general.html#definecomponent" ref="nofollow noopener noreferrer">defineComponent</a> 仅仅是在定义 <strong>组件</strong> 时提供类型推导的辅助函数，并没有额外其他功能</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">defineComponent</span>(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App,
  setup (props) &#123;
    // ...
  &#125;
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>但我们可以借助这个方法实现一个很重要的事情：让 <code>options</code> 支持 <code>setup</code>。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fapi%2Fcomposition-api-setup.html%23composition-api-setup" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/api/composition-api-setup.html#composition-api-setup" ref="nofollow noopener noreferrer">setup</a> 的核心作用便是将 <strong>返回值</strong> 挂载到 <code>this</code> 上。</p>
<p>所以我们先将 <code>setup</code> 函数执行，再把返回值绑定至 <code>this</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> defineComponent = <span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) &#123;
  <span class="hljs-keyword">const</span> &#123; beforeCreate, setup, ...restOptions &#125; = options

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">beforeCreate</span>: setup
      ? <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
        beforeCreate && <span class="hljs-title function_">beforeCreate</span>()

        <span class="hljs-keyword">const</span> options = <span class="hljs-title function_">setup</span>(<span class="hljs-variable language_">this</span>)

        <span class="hljs-comment">// 代理到this</span>
        proxyToThis.<span class="hljs-title function_">call</span>(<span class="hljs-variable language_">this</span>, options)
      &#125; : <span class="hljs-literal">undefined</span>,
    ...restOptions
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但问题在于如何绑定到 <code>this</code> 呢？</p>
<p>经过思考我们想到两个可行性方案:</p>
<ol>
<li>
<p><code>Object.defineProperty</code></p>
<p>这方案老熟悉了哈～，在大部分场景下也确实好用，但 <code>Object.defineProperty</code> 不允许重复设置 <code>key</code> ，否则报错 <code>Cannot redefine property: xxx</code>。</p>
<p>为什么会出现重复设置呢？</p>
<p>大部分 <strong>Vue2</strong> 项目在 <strong>逻辑复用</strong> 时避免不了 <code>mixins</code> 或 <code>extends</code> ，这种情况下允许覆盖相同属性，所以该方案难以兼容此场景。</p>
</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9afa6962818f4432be2e5531899da9f6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="有点伤心.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>
<p><code>this.$options</code></p>
<p>看过源码的小伙伴或许知道，<strong>Vue</strong> 在组件初始化阶段会将 <strong>组件配置</strong> 绑定到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv2.cn.vuejs.org%2Fv2%2Fapi%2F%23vm-options" target="_blank" rel="nofollow noopener noreferrer" title="https://v2.cn.vuejs.org/v2/api/#vm-options" ref="nofollow noopener noreferrer">this.$options</a> 上。</p>
<p>所以 【修改 <code>this.$options</code> === 修改组件配置】</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18c8ef198f264e0eab91ea902b712860~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="完全等同.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么问题又来了，我们怎么知道返回的内容是 <code>data</code> ，还是 <code>methods</code> ，还是 <code>computed</code> 呢？</p>
<p>仅依靠 <strong>数据类型</strong> 是不严谨的，因为 <code>computed</code> 和 <code>methods</code> 都是函数，而 <code>data</code> 可以是任意值。</p>
<p>所以我们需要对这几类数据打上特殊标识</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isComputed = <span class="hljs-title class_">Symbol</span>(<span class="hljs-string">'isComputed'</span>)
<span class="hljs-keyword">const</span> isRef = <span class="hljs-title class_">Symbol</span>(<span class="hljs-string">'isRef'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以帮助我们在将目标绑定至 <code>this</code> 时能放到正确位置，说白了就是做搬运🤣。</p>
</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01a65534e9c042bfb1a35e670edfbcc2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="我什么都不会，只会搬运.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">reactive、ref 等基本API</h2>
<p>上文有介绍，可以用 <code>Vue.util.defineReactive</code> 或 <code>Vue.observable</code> 创建响应式对象，</p>
<p><code>Vue.observable</code> 方法的返回值即是响应式对象，而且可以一次设置多个 <strong>key-value</strong>，所以在这里最适合。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> reactive = <span class="hljs-title class_">Vue</span>.<span class="hljs-property">observable</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ref</code> 也类似，这里就不赘述啦～</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/560f35d9f6904c879fab314cfac3aa26~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="搬运工.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>别急别急，这只是最基础的API，我们无需重复造轮子，所以直接复用即可。</p>
<h2 data-id="heading-6">toRef、toRefs</h2>
<p>这两个 <strong>API</strong> 一直备受争议，因为方法返回的结构会被包装在 <code>value</code> 中，
像这样<code>&#123; value: xxx &#125;</code>，
但在 <code>template</code> 引用时却无需获取 <code>value</code>，直接引用即可。</p>
<p>其实在 <strong>Vue3源码</strong> 中，绑定至 <code>this</code> 时会经过特殊处理：将 <code>this.[key]</code> 转发给 <code>this.[key].value</code>，</p>
<p>像这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title function_">proxy</span>(target, key, &#123;
  <span class="hljs-attr">get</span>: <span class="hljs-keyword">function</span> <span class="hljs-title function_">getterHandler</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">var</span> value = getter ? getter.<span class="hljs-title function_">call</span>(target) : val;
    <span class="hljs-comment">// 如果是 ref ，则直接获取到 value</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-title function_">isRef</span>(value)) &#123;
      <span class="hljs-keyword">return</span> value.<span class="hljs-property">value</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> value;
    &#125;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以通过 <code>this</code> 访问时不需要读取 <code>value</code>，而直接访问则需要。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9169eb24dfd45cf88ee93e724b95f8c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="恍然大悟.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以呢，我们要先在对象身上打上 <code>isRef</code> 标识，以便将来代理到 <code>this</code> 时直接获取到他们的 <code>value</code>。</p>
<pre><code class="hljs language-diff copyable" lang="diff"><span class="hljs-addition">+ const isRef = Symbol('isRef')</span>

<span class="hljs-addition">+ export const toRef = function (obj, key) &#123;</span>
<span class="hljs-addition">+   const ObjectRefImpl = &#123;</span>
<span class="hljs-addition">+     get value () &#123;</span>
<span class="hljs-addition">+       return obj[key]</span>
<span class="hljs-addition">+     &#125;,</span>
<span class="hljs-addition">+     set value (val) &#123;</span>
<span class="hljs-addition">+       obj[key] = val</span>
<span class="hljs-addition">+     &#125;</span>
<span class="hljs-addition">+   &#125;</span>
<span class="hljs-addition">+   // 1. 打上特殊标识</span>
<span class="hljs-addition">+   ObjectRefImpl[isRef] = true</span>
<span class="hljs-addition">+   return ObjectRefImpl</span>
<span class="hljs-addition">+ &#125;</span>

const proxyToThis = function (obj) &#123;
  for (const key in obj) &#123;
    if (key in this) &#123;
      continue
    &#125;

    const value = obj[key]
    if (typeof value <span class="hljs-comment">=== 'function' && value[isComputed]) &#123;</span>
      // ...
<span class="hljs-addition">+   &#125; else if (value[isRef]) &#123;</span>
<span class="hljs-addition">+     // 2. 如果是 ref ，则直接获取到 value</span>
<span class="hljs-addition">+     Object.defineProperty(this, key, &#123;</span>
<span class="hljs-addition">+       get () &#123;</span>
<span class="hljs-addition">+         return value.value</span>
<span class="hljs-addition">+       &#125;,</span>
<span class="hljs-addition">+       set (val) &#123;</span>
<span class="hljs-addition">+         value.value = val</span>
<span class="hljs-addition">+       &#125;</span>
<span class="hljs-addition">+     &#125;)</span>
<span class="hljs-addition">+   &#125; else &#123;</span>
      // ...
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">computed</h2>
<p>关于 <strong>computed</strong> ，有一种方案是直接代理给 <code>this</code>，像这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> <span class="hljs-title function_">double</span> = (<span class="hljs-params"></span>) => state.<span class="hljs-property">count</span> * <span class="hljs-number">2</span>

<span class="hljs-title class_">Object</span>.<span class="hljs-title function_">defineProperty</span>(<span class="hljs-variable language_">this</span>, <span class="hljs-string">'double'</span>, &#123;
  get () &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title function_">double</span>()
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但 <strong>computed</strong> 在 <strong>Vue原理</strong> 中可不仅如此，而是一种特殊的 <a href="https://juejin.cn/post/6921589536233390093#heading-24" target="_blank" title="https://juejin.cn/post/6921589536233390093#heading-24">观察者</a>，内部包含了 <strong>脏检查</strong> 等优化处理。</p>
<blockquote>
<p>ps：本文对于 <strong>观察者</strong> 暂不展开细说，感兴趣的小伙伴可以查看 <a href="https://juejin.cn/post/6921589536233390093" target="_blank" title="https://juejin.cn/post/6921589536233390093">这篇文章</a></p>
</blockquote>
<p>所以我们干脆把 <strong>computed</strong> 放入 <code>this.$options</code> 交给 <strong>Vue</strong> 处理好了。</p>
<pre><code class="hljs language-diff copyable" lang="diff"><span class="hljs-addition">+ const isComputed = Symbol('isComputed')</span>
<span class="hljs-addition">+ export const computed = function (getter) &#123;</span>
<span class="hljs-addition">+   getter[isComputed] = true</span>
<span class="hljs-addition">+   return getter</span>
<span class="hljs-addition">+ &#125;</span>

const proxyToThis = function (obj) &#123;
  for (const key in obj) &#123;
    if (key in this) &#123;
      continue
    &#125;

    const value = obj[key]
<span class="hljs-addition">+   if (typeof value === 'function' && value[isComputed]) &#123;</span>
<span class="hljs-addition">+     // 如果是getter，则放到 options 中交给 Vue 处理</span>
<span class="hljs-addition">+     this.$options.computed[key] = value</span>
<span class="hljs-addition">+   &#125; else if (value[isRef]) &#123;</span>
      // ...
    &#125; else &#123;
      // ...
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7dd8a6adcac4863acd1c577821309ec~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="交给你.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">onMounted 等生命周期函数</h2>
<p>这里和前面会有所区别，因为 <strong>生命周期函数</strong> 不需要 <code>return</code> ，所以现有方案无法和 <code>this</code> 绑定</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3429f85dc0ca4aa99a0ec1b320dda09b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="那怎么办.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不怕不怕，看看 <strong>源码</strong> 是如何实现的。</p>
<p><strong>源码</strong> 的思路是专门获取到当前组件的 <code>this</code> ，然后把 <strong>回调函数</strong> 添加到 <code>this</code> 上，由于考虑的情况比较全面，所以代码比较复杂。</p>
<p>但我们不需要考虑那么多，只需要保证在 <code>setup</code> 中使用 <strong>composition API</strong> 正常即可，毕竟太灵活了也不好嘛，还是要做一点限制的。</p>
<p>所以我们可以在 <code>const options = setup(this)</code> 之前 <strong>保存</strong> 组件实例，在其之后 <strong>取消绑定</strong>。</p>
<p>核心改动如下：</p>
<pre><code class="hljs language-diff copyable" lang="diff">let currentInstance = null

export const defineComponent = function (options) &#123;
  const &#123; beforeCreate, setup, ...restOptions &#125; = options

  return &#123;
    beforeCreate: setup
      ? function () &#123;
        beforeCreate && beforeCreate()

<span class="hljs-addition">+       // 保存 this</span>
<span class="hljs-addition">+       currentInstance = this</span>

<span class="hljs-addition">+       // 使用 this</span>
<span class="hljs-addition">+       const options = setup(currentInstance)</span>

        proxyToThis(options)

<span class="hljs-addition">+       // 取消 this 的绑定</span>
<span class="hljs-addition">+       currentInstance = null</span>
      &#125; : undefined,
    ...restOptions
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 <strong>生命周期函数</strong> 中使用即可：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> onMounted = <span class="hljs-keyword">function</span> (<span class="hljs-params">cb</span>) &#123;
  <span class="hljs-keyword">if</span> (!currentInstance) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Error</span>(<span class="hljs-string">'onMounted只能在 setup 中使用哦'</span>)

  <span class="hljs-keyword">if</span> (currentInstance.<span class="hljs-property">$options</span>.<span class="hljs-property">mounted</span>) &#123;
    currentInstance.<span class="hljs-property">$options</span>.<span class="hljs-property">mounted</span>.<span class="hljs-title function_">push</span>(cb)
  &#125; <span class="hljs-keyword">else</span> &#123;
    currentInstance.<span class="hljs-property">$options</span>.<span class="hljs-property">mounted</span> = cb
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他 <strong>生命周期函数</strong> 同理～</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28a48905991c4bf88f8b5ce1a23cb8ca~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="bingo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">小试锋芒</h1>
<p>现在可以放心地在 <strong>历史债项目</strong> 中使用 <strong>composition API</strong> 啦！</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; defineComponent, reactive, toRefs, onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue2-composition-api'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">defineComponent</span>(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  setup (props) &#123;
    <span class="hljs-keyword">const</span> state = <span class="hljs-title function_">reactive</span>(&#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'1'</span>,
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
    &#125;)

    <span class="hljs-keyword">const</span> <span class="hljs-title function_">add</span> = (<span class="hljs-params"></span>) => state.<span class="hljs-property">count</span>++

    <span class="hljs-keyword">const</span> double = <span class="hljs-title function_">computed</span>(<span class="hljs-function">() =></span> state.<span class="hljs-property">count</span> * <span class="hljs-number">2</span>)
    
    <span class="hljs-title function_">onMounted</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'onMounted'</span>, state.<span class="hljs-property">count</span>);
    &#125;)

    <span class="hljs-keyword">return</span> &#123;
      double,
      add,
      ...<span class="hljs-title function_">toRefs</span>(state)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到体验和 <strong>Vue3</strong> 一模一样！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31b23718d5a64f4f90dbe61d90808f4a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="成了.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">思考与总结</h1>
<p>本篇文章的意义有两点</p>
<ol>
<li>
<p>为 <strong>因兼容性而无法升级到Vue3的项目</strong> 提供良好的过渡方案，以便将来可以顺滑地过渡。毕竟历史的车轮不会因为浏览器的版本问题而停滞不前，相信有朝一日我们一定可以全面拥抱 <strong>Vue3</strong> ！</p>
<p>但也仅局限于对 <a href="https://link.juejin.cn/?target=..." target="_blank" title="..." ref="nofollow noopener noreferrer">响应式API</a> 的改造，诸如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fapi%2Fsfc-script-setup.html%23script-setup" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/api/sfc-script-setup.html#script-setup" ref="nofollow noopener noreferrer">setup script</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fapi%2Fcustom-renderer.html%23create-renderer" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/api/custom-renderer.html#create-renderer" ref="nofollow noopener noreferrer">自定义渲染器</a> 这一类依赖 <strong>Vue3 编译器</strong> 的特性依然只能望而却步。</p>
</li>
<li>
<p>打破限制，寻求更多的可能，与其抱怨现阶段的不足，不如尝试着改变现状！</p>
</li>
</ol>
<p>代码已发布至 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvue2-composition-api" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vue2-composition-api" ref="nofollow noopener noreferrer">npm</a>，欢迎小伙伴们拍砖～</p>
<p>感谢读到这里的小伙伴，希望这篇文章能够给你带来帮助，蟹蟹～</p></div>  
</div>
            