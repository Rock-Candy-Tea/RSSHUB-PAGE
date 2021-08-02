
---
title: '8x0 精读Vue官方文档 - Composition-API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe1b8350db804af09d5cc1f13a99fab7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 18:30:49 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe1b8350db804af09d5cc1f13a99fab7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/column/6976899977133948965" target="_blank" title="https://juejin.cn/column/6976899977133948965">精读 Vue 官方文档系列</a> 🎉</h2>
<hr>
<blockquote>
<p>注意：本篇内容更多是基于 <code>@vue/composition-api</code> 这个库上进行讲解的。</p>
</blockquote>
<h2 data-id="heading-1">What is the Composition-API ?</h2>
<p><code>Composition-API</code> 的核心目的在于代码的复用。
<code>Composition-API</code> 赋予了开发者访问 Vue 底层响应式系统的能力，对比于传统的 <code>Options API</code> 会自行处理 <code>data</code> 返回的对象，现在 <code>Composition-API</code> 则需要在开发者手动在 <code>setup</code> 中定义响应式数据。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe1b8350db804af09d5cc1f13a99fab7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>缺点是响应式数据的定义不再简单方便，优点则是响应式数据定义的时机、位置不再有严格的限制，可以更灵活的组装。</p>
</blockquote>
<p><code>Options API</code> 基于功能代码的不同选项（类别）进行拆分，例如将功能中的数据拆分到 <code>data</code> 选项中，将方法逻辑拆分到 <code>methods</code> 选项中，计算属性则拆分到 <code>computed</code> 选项中。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb1e1e534e2e4fc88f395f0b43538f3f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然这种排列条理清晰，但是一旦代码量增加，其可阅读性就会变差，并且也为组件逻辑的复用带来了挑战，例如，依然采用这一方式的 <code>mixins</code> 再实现代码复用时，就会都带来命名冲突、数据来源不清晰的隐患。</p>
<p>而 <code>Composition API</code> 则是将一个功能视为一个完整的整体。这个整体本身就囊括了<code>data</code>、<code>methods</code>、<code>computed</code>、<code>life-cycle</code> 等选项，每个功能都被视为一个独立的部分。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0376862fa3e747ccbc4b0eba99e77c93~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，通过 <code>Composition API</code> 我们可以像传统 JavaScript 编写函数的方式那样来编写我们的组件逻辑了，此时，你可以发现<strong>响应式数据</strong>必须要通过手动声明，但好处也随之浮现，这些响应式对象与功能可以从组件中抽离，实现跨组件共享和复用。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a95bcc2e264c1785777458178a2686~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>其中逻辑关注点按照颜色进行分组，额外的好处，代码量很大的场景下，再也不需要用鼠标滚来滚去，以在不同的选项之间浏览属于同一个功能的内容。</p>
</blockquote>
<p><strong><code>Composition-API</code> VS <code>Options API</code></strong></p>





































<table><thead><tr><th><strong>Options API</strong></th><th><strong>Composition-API</strong></th></tr></thead><tbody><tr><td>不利于复用</td><td>方便代码复用，关注点分离</td></tr><tr><td>潜在命名冲突，数据源来源不清晰</td><td>数据来源清晰</td></tr><tr><td>上下文丢失</td><td>提供更好的上下文</td></tr><tr><td>有限类型支持</td><td>更好的 <strong>TypeScript</strong> 支持</td></tr><tr><td>按 API 类型支持</td><td>按功能/逻辑组织</td></tr><tr><td>按功能/逻辑组织</td><td>方便代码复用</td></tr><tr><td>响应式数据必须在组件的 <code>data</code> 中定义</td><td>可独立 Vue 组件使用</td></tr></tbody></table>
<h2 data-id="heading-2">setup</h2>
<p><code>setup</code> 是一个新的组件选项，作为 <code>Composition-API</code> 的入口点，值是一个函数，且只会被执行一次，用于建立数据与逻辑的链接。</p>
<p><code>setup</code> 执行时机位于 <code>beforeCreated</code> 与 <code>created</code> 之间，此时无法访问 <code>this</code>，并且 <code>data</code>、<code>methods</code>、<code>computed</code> 等还未被解析所以也无法访问。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, context</span>)</span>&#123;
    
        context.attrs; <span class="hljs-comment">//Attributes</span>
        context.slots; <span class="hljs-comment">//slots</span>
        context.emit; <span class="hljs-comment">//tirgger event</span>
        context.listeners; <span class="hljs-comment">// events</span>
        context.root; <span class="hljs-comment">// root component instance</span>
        context.parent; <span class="hljs-comment">// parent component isntance</span>
        context.refs; <span class="hljs-comment">// all refs</span>
        
        <span class="hljs-keyword">return</span> &#123;&#125;;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>setup</code> 方法的返回值会合并到“模板”的上下文中参与数据的渲染。</p>
<h2 data-id="heading-3">API 详解</h2>
<h3 data-id="heading-4">getCurrentInstance</h3>
<p>获取当前执行 <code>setup</code> 函数的组件实例。
需要注意的是，<code>getCurrentInstance</code> 只能在 <code>setup</code> 中执行或者在生命周期钩子中执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;getCurrentInstance&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span>&#123;
  <span class="hljs-keyword">const</span> vm = getCurrentInstace();
  onMounted(<span class="hljs-function">()=></span>&#123;
   vm =  getCurrentInstance();
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">ref && Ref</h3>
<p>定义响应式的 ref 对象，ref 对象内部只有单个名为 <code>value</code> 的 property。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span>&#123;
    <span class="hljs-keyword">const</span> title = ref(<span class="hljs-string">'this is a title!'</span>);
    
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
       title.value = <span class="hljs-string">'change title text'</span>;
    &#125;,<span class="hljs-number">1000</span>);

    <span class="hljs-keyword">return</span> &#123;title&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型声明</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// ref值的类型结构</span>
<span class="hljs-keyword">interface</span> Ref<T>&#123;
   <span class="hljs-attr">value</span>:T 
&#125;

<span class="hljs-comment">//ref 函数的类型结构</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span><<span class="hljs-title">T</span>>(<span class="hljs-params">value:T</span>):<span class="hljs-title">Ref</span><<span class="hljs-title">T</span>></span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体使用，我们可以在调用 <code>ref()</code> 方法时传入泛型的值来覆盖默认的推断时传递的泛型参数，也可以直接使用 <code>as Ref<state extends string></code> 的方式进行断言声明。</p>
<blockquote>
<p>ref 在 <code>setup</code> 方法中需要解包使用，但是在模板中无需解包。</p>
</blockquote>
<h3 data-id="heading-6">isRef</h3>
<p>检查一个值是否是 <code>Ref</code> 类型的对象。默认 <code>ref()</code> 函数已经自带了此功能，当接受的值已经是一个 <code>Ref</code> 类型，则什么都不会处理，否则将其转为为 <code>Ref</code> 类型的值。</p>
<h3 data-id="heading-7">unRef</h3>
<p>语法糖，其功能类似于 <code>isRef(val) ? val.value : val</code>。</p>
<h3 data-id="heading-8">toRef / toRefs</h3>
<p>基于源响应式对象上的某个 Property 映射出一个对应的 <code>ref</code> 对象。这个 <code>ref</code> 对象依然保持着与源响应式对象上对应的 property 的响应式链接。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;reactive, toRef&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span>&#123;
    <span class="hljs-keyword">const</span> state = reactive(&#123;<span class="hljs-attr">foo</span>:<span class="hljs-number">1</span>, <span class="hljs-attr">bar</span>:<span class="hljs-number">2</span>&#125;);
    
    <span class="hljs-comment">//从源响应式对象的property上映射出一个ref对象。</span>
    <span class="hljs-keyword">const</span> fooRef = toRef(state, <span class="hljs-string">'foo'</span>);
    
    <span class="hljs-comment">//依然保留对源响应式对象的响应式链接</span>
    fooRef.value = <span class="hljs-number">2</span>;
    <span class="hljs-built_in">console</span>.log(state.foo);
    
    state.foo++;
    <span class="hljs-built_in">console</span>.log(fooRef)；
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>就算要映射的源响应式上的 property 不存在，<code>toRef</code> 也不会报错，而是完全建立一个没有链接关系的新 <code>ref</code> 对象。</p>
</blockquote>
<p><code>toRefs()</code> 是 <code>toRef()</code> 的快捷操作，用于将源响应式对象上的所有 property 都转换为 <code>ref</code> 对象。</p>
<h3 data-id="heading-9">reactive</h3>
<p>创建响应式对象，可以使用 <code>toRefs</code> 方法进行解构为多个 <code>Ref</code> 对象的引用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span>&#123;
    <span class="hljs-keyword">const</span> userInfo = reactive(&#123;
        <span class="hljs-attr">firstName</span>:<span class="hljs-string">'shen'</span>,
        <span class="hljs-attr">lastName</span>:<span class="hljs-string">'guotao'</span>
    &#125;);
    
    <span class="hljs-keyword">return</span> &#123;...toRefs(userInfo)&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型声明：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>>(<span class="hljs-params">target: T</span>) : <span class="hljs-title">UnwrapNestedRefs</span><<span class="hljs-title">T</span>>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这说明 <code>reactive</code> 方法接受的泛型必须是继承 object 对象，然后用作传参的类型约束，其返回值则用 <code>UnwrapNestedRefs</code> 的泛型再包裹 <code>T</code>。</p>
<p>需要注意一点的是，如果将 <code>ref</code> 与 <code>reactive</code> 结合使用，可以通过 <code>reactvie</code> 方法重新定义 <code>ref</code> 对象，会自动展开 <code>ref</code> 对象的原始值，类似与自动解包无需再通过 <code>.value</code> 方式访问其值。当然，这并不会解构原始 <code>ref</code> 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> foo = ref(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> r = reactive(&#123;foo&#125;);

r.foo === foo.value;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是不能通过字面量的形式将一个 <code>ref</code> 添加到一个响应式对象中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> foo = ref(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> r = reactive(&#123;&#125;);

r.foo = foo; <span class="hljs-comment">//bad</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">readonly</h3>
<p>接受一个响应式对象或普通对象，返回一个它们的只读代理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; readonly, toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span>&#123;
    <span class="hljs-keyword">const</span> originalUserInfo = readonly(userInfo);
    
    <span class="hljs-comment">//覆盖响应式对象</span>
    userInfo = originalUserInfo ;
    
    <span class="hljs-keyword">return</span> &#123;
        ...toRefs(userInfo)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">isProxy</h3>
<p>检查对象是否是由 <code>reactive</code> 或 <code>readonly</code> 创建的 proxy。</p>
<h3 data-id="heading-12">isReactive</h3>
<p>检查对象是否是由 <code>reactive</code> 创建的响应式代理。</p>
<blockquote>
<p>注意：经过 <code>readonly</code> 包裹的 <code>reactive</code> 对象依然为true。</p>
</blockquote>
<h3 data-id="heading-13">isReadonly</h3>
<p>检查对象是否是由 <code>readonly</code> 创建的只读代理。</p>
<h3 data-id="heading-14">toRaw</h3>
<p>返回 <code>reactive</code> 或 <code>readonly</code> 代理的原始对象。这是一个“逃生舱”，可用于临时读取数据而无需承担代理访问/跟踪的开销，也可用于写入数据而避免触发更改。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//原始对象</span>
<span class="hljs-keyword">const</span> foo = &#123;&#125;;
<span class="hljs-comment">//readonlyFoo</span>
<span class="hljs-keyword">const</span> readonyFoo = readonly(foo);

<span class="hljs-comment">//reactiveFoo</span>
<span class="hljs-keyword">const</span> reactiveFoo = reactive(foo);

<span class="hljs-comment">//再次获得原始对象</span>

<span class="hljs-keyword">let</span> orignal = toRaw(reactiveFoo);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>不建议保留对原始对象的持久引用。请谨慎使用。</p>
</blockquote>
<h3 data-id="heading-15">markRaw</h3>
<p>标记一个对象，使其永远不会转换为 <code>proxy</code>。返回对象本身。</p>
<h3 data-id="heading-16">computed</h3>
<p><code>Composition-API</code> 中提供的计算属性功能，与 <code>OptionsAPI</code> 中提供的 <code>computed</code> 选项相同。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;computed&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span>&#123;
    <span class="hljs-keyword">const</span> fullName = computed(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">return</span> userInfo.firstName + userInfo.lastName;
    &#125;);
    
    <span class="hljs-keyword">const</span> pass = computed(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">if</span>(userInfo.score >= <span class="hljs-number">60</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">'及格'</span>;
        <span class="hljs-keyword">if</span>(userInfo.score < <span class="hljs-number">60</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">'不及格'</span>
    &#125;)
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>computed</code> 存在计算缓存。但是当计算属性被使用时（在模板中），那么就必然会执行一次 <code>computed</code> 函数，然后如果当 <code>computed </code>中的计算属性发生改变，也会重新执行 <code>computed</code> 函数，返回最新的计算属性的值。</p>
<h3 data-id="heading-17">watchEffect && watch</h3>
<p><strong>watchEffect</strong></p>
<ul>
<li>会立即执行副作用方法。并且当内部所依赖的响应式值发生改变时也会重新执行。</li>
<li>不需要指定监听属性，可以自动收集依赖。</li>
<li>可以通过 <code>onInvalidate</code> 取消监听。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;reactive, watchEffect, toRefs&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span> &#123;
    <span class="hljs-keyword">const</span> data = reactive(&#123;
        <span class="hljs-attr">num</span>:<span class="hljs-number">0</span>,
        <span class="hljs-attr">count</span>:<span class="hljs-number">0</span>,
    &#125;);
    
    <span class="hljs-keyword">const</span> stop = watchEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">//立即执行，输出0</span>
        <span class="hljs-comment">//每隔1秒钟值发生改变是，重新执行watchEffect。</span>
        <span class="hljs-comment">//count虽然是每2秒更新一次，但并不会触发当前的 watchEffect，因为它不属于当前 watchEffect 的依赖项。</span>
        <span class="hljs-built_in">console</span>.log(data.num);
        
        <span class="hljs-comment">//nInvalidate(fn)传入的回调会在watchEffect重新运行或者watchEffect停止的时候执行。</span>
        onInvalidate(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 取消异步api的调用。</span>
            apiCall.cancel()
        &#125;)
    &#125;);
    
    <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
        data.num++;
    &#125;,<span class="hljs-number">1000</span>);
    
    <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
        data.count++;
    &#125;,<span class="hljs-number">2000</span>);
    
    <span class="hljs-keyword">return</span> &#123;
        ...toRefs(data),
        <span class="hljs-function"><span class="hljs-title">onStop</span>(<span class="hljs-params"></span>)</span>&#123;stop()&#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要注意，当副作用函数中执行的函数，若该函数又改变了响应式的数据，可能会造成死循环问题。</p>
</blockquote>
<p><strong>watch</strong></p>
<ul>
<li>具有懒执行的特性，并不会立即执行。</li>
<li>要明确哪些依赖项的状态改变，触发侦听器的重新执行，支持监听多个依赖。</li>
<li>能够获得状态变更前后的值。</li>
<li>可以手动停止监听</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">//只能对响应式对象进行监听，而不能对响应式对象的属性进行监听。</span>
watch(data, <span class="hljs-function">(<span class="hljs-params">newValue, oldValue</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(newValue,oldValue)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听多个数据源：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; watch, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    setup () &#123;
        <span class="hljs-keyword">const</span> state = reactive(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
            <span class="hljs-attr">msg</span>: <span class="hljs-string">'hello'</span>
        &#125;)

       <span class="hljs-keyword">const</span> stop =  watch([<span class="hljs-function">()=></span> state.count, <span class="hljs-function">()=></span> state.msg],<span class="hljs-function">(<span class="hljs-params">[count, msg], [prevCount, prevMsg]</span>)=></span>&#123;
            <span class="hljs-built_in">console</span>.log(count, msg);
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'---------------------'</span>);
            <span class="hljs-built_in">console</span>.log(prevCount, prevMsg);
        &#125;)

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            state.count++;
            state.msg = <span class="hljs-string">'hello world'</span>;
        &#125;,<span class="hljs-number">1000</span>);

        <span class="hljs-keyword">return</span> &#123;
           state
        &#125;;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">provide && inject</h3>
<p><code>Composition-API</code> 风格的依赖注入：</p>
<p><strong>Parent:</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; provide, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> title = ref(<span class="hljs-string">'learn vue'</span>);
    
    <span class="hljs-keyword">const</span> changeTitle = <span class="hljs-function">()=></span>&#123; title.value = <span class="hljs-string">'learn vue and typescript!'</span> &#125;;
    
    provide(<span class="hljs-string">"title"</span>, title);
    
    <span class="hljs-keyword">return</span> &#123;changeTitle&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Son</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; inject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">const</span> title = inject(<span class="hljs-string">'title'</span>);
  
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;title.value =<span class="hljs-string">'learn success!'</span>&#125;,<span class="hljs-number">1000</span>);
  
  <span class="hljs-keyword">return</span> &#123;title&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">shallowReactive</h3>
<p>只处理对象最外层属性的响应式(也就是浅响应式)，所以最外层属性发生改变，更新视图，其他层属性改变，视图不会更新.</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> obj = &#123;
            <span class="hljs-attr">x</span>:&#123;
                <span class="hljs-attr">y</span>:&#123;
                    <span class="hljs-attr">z</span>:<span class="hljs-number">0</span>
                &#125;
            &#125;
        &#125;;
        
        <span class="hljs-keyword">const</span> shallowObj = shallowReactive(obj);

        shallowObj.x.y.z=<span class="hljs-number">1</span>; <span class="hljs-comment">//不会触发更新</span>

        <span class="hljs-keyword">return</span> &#123;shallowObj&#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">shallowRef</h3>
<p>只处理了 <code>value</code> 的响应式，对于引用类型的值，不会对引用值进行 <code>reactive</code> 处理。</p>
<h3 data-id="heading-21">customRef</h3>
<p><code>customRef</code> 用于创建自定义 <code>ref</code>，可以显式地控制依赖追踪和触发响应，接受一个工厂函数，两个参数分别是用于追踪的 <code>track</code> 和用于触发响应的 <code>trigger</code>，并返回一个一个带有 <code>get</code> 和 <code>set</code> 属性的对象。</p>
<p>使用自定义 <code>ref</code> 实现带防抖功能的 <code>v-model</code> ：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"text"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useDebouncedRef</span>(<span class="hljs-params">value, delay = <span class="hljs-number">200</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> timeout
  <span class="hljs-keyword">return</span> customRef(<span class="hljs-function">(<span class="hljs-params">track, trigger</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        track()
        <span class="hljs-keyword">return</span> value
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newValue</span>)</span> &#123;
        <span class="hljs-built_in">clearTimeout</span>(timeout)
        timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          value = newValue
          trigger()
        &#125;, delay)
      &#125;,
    &#125;
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">text</span>: useDebouncedRef(<span class="hljs-string">'hello'</span>),
    &#125;
  &#125;,
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">LifeCycle Hooks</h2>
<p>由于 <code>setup()</code> 是在 <code>beforeCreate</code>, <code>created</code> 之前执行，因此：</p>
<ul>
<li>不能在 <code>setup()</code> 函数中使用 <code>this</code>，因为此时组件并没有完全实例化。</li>
<li>不能在 <code>setup()</code> 函数中使用 <code>beforeCreate</code> 与 <code>created</code> 两个组合生命周期。</li>
</ul>
<p>但是可以使用以下生命周期方法：</p>
<ul>
<li>onBeforeMount</li>
<li>onMounted</li>
<li>onBeforeUpdate</li>
<li>onUpdated</li>
<li>onBeforeUnmount</li>
<li>onUnmounted</li>
<li>onErrorCaptured</li>
<li>onRenderTracked</li>
<li>onRenderTriggered</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;onMounted&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'composition-api'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span>&#123;
    onMounted(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mounted'</span>);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">最佳实践</h2>
<h3 data-id="heading-24">ref && reactive</h3>
<ol>
<li>能够使用 <code>ref</code> 的尽可能使用 <code>ref</code>，<code>ref</code> 因为有 <code>.value</code> 所以能更直观表明一个 <code>ref</code> 对象。</li>
<li>基本类型值使用 <code>ref</code> 定义。</li>
<li>对象类型有多个成员的情况，建议使用 <code>reactive</code>。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> n = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> data = ref([]);
<span class="hljs-keyword">const</span> mouse = reactive(&#123;
    <span class="hljs-attr">x</span>:<span class="hljs-number">0</span>,
    <span class="hljs-attr">y</span>:<span class="hljs-number">0</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">ref 自动解包</h3>
<ol>
<li>模板中自动解包。</li>
<li><code>watch</code> 监听的值会自动解包。</li>
<li>使用 <code>reactive</code> 包装 <code>ref</code> 对象，自动解包</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> counter = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> rc = reactive(&#123;
    <span class="hljs-attr">foo</span>:<span class="hljs-number">1</span>,
    counter
&#125;);

rc.counter; <span class="hljs-comment">//无需解包，自动解包</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><code>unref</code> 解包方法。</li>
</ol>
<blockquote>
<p>当我们不能确定接收的值是否为一个 <code>Ref</code> 类型，但是期望最终的结果是一个非  <code>Ref</code> 类型时，该方法会场有用</p>
</blockquote>
<h3 data-id="heading-26">接受 <code>Ref</code> 参数返回一个响应式结果。</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span> (<span class="hljs-params">a: Ref<number>, b: Ref<number></span>) </span>&#123;
    <span class="hljs-keyword">return</span> computer(<span class="hljs-function">()=></span>a.value + b.value);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>兼容非响应式场景</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span> (<span class="hljs-params">a: Ref<number> | number, b: Ref<number> | number</span>) </span>&#123;
    <span class="hljs-keyword">return</span> computer(<span class="hljs-function">()=></span> unref(a) + unref(b));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">isRef() && ref()</h3>
<p><code>ref</code> 函数自带了判断功能，这在编写不确定类型的时候非常有用。</p>
<pre><code class="hljs language-js copyable" lang="js">isRef(foo) ? foo : ref(foo) ==== ref(foo);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">返回一个 ref 成员构成的对象更加有用</h3>
<p>返回一个 ref 成员构成的对象更加有用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = &#123;
    <span class="hljs-attr">x</span>: ref(<span class="hljs-number">0</span>),
    <span class="hljs-attr">y</span>: ref(<span class="hljs-number">1</span>),
    <span class="hljs-attr">z</span>: ref(<span class="hljs-number">2</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Es6 解构使用时：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123;x, y ,z&#125; = data;
x.value = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过对象引用的方式使用，再通过 <code>reactive()</code> 进行包装一层。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rcData = reactive(data);
rcData.x = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">自动清除副作用</h3>
<p>自我们封装的 <code>use</code> 方法中使用 <code>onUnmounted</code> 钩子自动清理依赖，例如事件解绑、依赖清除。</p>
<h3 data-id="heading-30">类型安全的 provide / inject</h3>
<p>在一个共享的模块中，为 <code>provide</code> 与 <code>inject</code> 声明具有类型安全的 key。
例如在一个共享的 <code>context.ts</code> 模块中声明 key。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//context.ts</span>
<span class="hljs-keyword">import</span> &#123;InjectionKey&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/composition-api'</span>

interface UserInfo &#123;
  <span class="hljs-attr">name</span>:string;
  id:number;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">const</span> InjectionKeyUser : InjectionKey<UserInfo>  = <span class="hljs-built_in">Symbol</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Used：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;InjectionKeyUser&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./context'</span>;
&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
        provide(InjectionKeyUser, &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'zhangsan'</span>, <span class="hljs-attr">id</span>:<span class="hljs-number">10001</span>&#125;)
    &#125;
&#125;

&#123;

    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> user = inject(InjectionKeyUser);

        <span class="hljs-keyword">if</span>(user)&#123;
            <span class="hljs-built_in">console</span>.log(user.name);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">状态共享</h3>
<p>状态可以独立于组件被创建并使用。
但是最普通的方式并不支持 SSR，为了支持 SSR 我们应该基于 provide/inject 进行状态共享。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//context.ts</span>

<span class="hljs-comment">//....</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">const</span> InjectionKeyState : InjectionKey<State> = <span class="hljs-built_in">Symbol</span>();

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// useState.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createState</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> state = &#123; <span class="hljs-comment">/**/</span> &#125;;

    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">app:App</span>)</span>&#123;
            app.provide(InjectionKeyState, state);
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useState</span> (<span class="hljs-params"></span>) :<span class="hljs-title">State</span>  </span>&#123;
    <span class="hljs-keyword">const</span> &#123;inject&#125; = <span class="hljs-string">'@vue/composition-api'</span>;
    <span class="hljs-keyword">return</span> inject(InjectionKeyState)!;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">通过 ref 获取 DOM 节点</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"demo.jpg"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"domRef"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> domRef = ref(<span class="hljs-literal">null</span>);
        onMounted(<span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">console</span>.log(domRef.value)
        &#125;)
        <span class="hljs-keyword">return</span> &#123;domRef&#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">mayBeRef</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> type mayBeRef<T> = Ref<T> | T;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">安全解构 reactive 对象。</h3>
<p>如果使用 ES6 解构一个 <code>reactive()</code> 方法定义的响应式对象，会破坏其响应式特征。
一个好的方法就是使用 <code>toRefs()</code> 进行结构。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rc = reactive(&#123;
    <span class="hljs-attr">x</span>:<span class="hljs-number">0</span>,
    <span class="hljs-attr">y</span>:<span class="hljs-number">1</span>
&#125;);

<span class="hljs-comment">//bad</span>
<span class="hljs-keyword">const</span> &#123;x, y&#125; = rc;
isRef(x); <span class="hljs-comment">//false</span>

<span class="hljs-comment">//good;</span>
<span class="hljs-keyword">const</span> &#123;x, y&#125; = toRefs(rc);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">props 不能使用 ES6 解构</h3>
<p><code>setup(props)</code> 的方法 <code>props</code> 是一个 proxy 对象，所以不能直接使用 ES6 解构。</p>
<h3 data-id="heading-36">在 setup 中使用 $nextTick 等</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; root &#125;</span>)</span> &#123;
    
    <span class="hljs-keyword">const</span> &#123; $nextTick &#125; = root;
    <span class="hljs-built_in">console</span>.log($nextTick);
    
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">参考</h2>
<blockquote>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fvueconf%2Fmkwv0c%2Fsqffko" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/vueconf/mkwv0c/sqffko" ref="nofollow noopener noreferrer">www.yuque.com/vueconf/mkw…</a></li>
<li><a href="https://juejin.cn/post/6850418114111537159" target="_blank" title="https://juejin.cn/post/6850418114111537159">juejin.cn/post/685041…</a></li>
<li><a href="https://juejin.cn/post/6890545920883032071" target="_blank" title="https://juejin.cn/post/6890545920883032071">juejin.cn/post/689054…</a></li>
</ul>
</blockquote></div>  
</div>
            