
---
title: 'Vue.js 中使用defineAsyncComponent 延迟加载组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1538da82476b4a8e9480c67e43ed6eb0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 22:12:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1538da82476b4a8e9480c67e43ed6eb0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>使用 Vue 3 的 <code>defineAsyncComponent</code> 特性可以让我们延迟加载组件。这意味着它们仅在需要时从服务器加载。</p>
<p>这是改善初始页面加载的好方法，因为我们的应用程序将以较小的块加载，而不必在页面加载时加载每个组件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1538da82476b4a8e9480c67e43ed6eb0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在本教程中，我们将学习 <code>defineAsyncComponent</code> 的全部内容，并看一个例子，该例子将一个弹出窗口的加载推迟到我们的应用程序需要的时候。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ada1c3edc1c4089b84103d4ba626625~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，让我们开始吧。</p>
<h2 data-id="heading-0">什么是defineAsyncComponent</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// SOURCE: https://v3.vuejs.org/guide/component-dynamic-async.html</span>
<span class="hljs-keyword">const</span> AsyncComp = defineAsyncComponent(
  <span class="hljs-function">() =></span>
    <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      resolve(&#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>I am async!</div>'</span>
      &#125;)
    &#125;)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>defineAsyncComponent</code> 接受一个返回Promise的工厂函数。当我们成功地从服务器获取组件时，这个Promise应该会被 <code>resolve</code> ，如果出现错误则会被 <code>reject</code> 。</p>
<p>要使用它，我们必须从Vue中导入它，然后才能在脚本的其余部分中使用它。</p>
<p>我们也可以使用工厂函数中的 <code>import</code> ，轻松地从其他文件中添加Vue组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineAsyncComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span> 

<span class="hljs-comment">// 简单使用</span>
<span class="hljs-keyword">const</span> LoginPopup = defineAsyncComponent(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"./components/LoginPopup.vue"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是使用 <code>defineAsyncComponent</code> 的最简单方法，但我们也可以传入一个完整的选项对象，配置几个更高级的参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// with options </span>
<span class="hljs-keyword">const</span> AsyncPopup = defineAsyncComponent(&#123; 
  <span class="hljs-attr">loader</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"./LoginPopup.vue"</span>),
  <span class="hljs-attr">loadingComponent</span>: LoadingComponent, <span class="hljs-comment">/* 在加载时显示 */</span>
  <span class="hljs-attr">errorComponent</span>: ErrorComponent, <span class="hljs-comment">/* 显示是否有错误 */</span>
  <span class="hljs-attr">delay</span>: <span class="hljs-number">1000</span>, <span class="hljs-comment">/* 在显示加载组件之前延迟毫秒 */</span>
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">3000</span> <span class="hljs-comment">/* 这个毫秒之后的超时 */</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就我个人而言，我发现自己更经常使用第一种较短的语法，它对我的大多数使用情况都有效，但这完全取决于你。</p>
<p>就这么简单，让我们进入我们的例子。</p>
<h2 data-id="heading-1">使用defineAsyncComponent延迟加载弹出组件</h2>
<p>在本例中，我们将使用一个由单击按钮触发的登录弹出窗口。</p>
<p>每当我们的应用程序加载时，我们不需要我们的应用程序加载此组件，因为只有在用户执行特定操作时才需要它。</p>
<p>所以这就是我们的登录组件的样子，它只是通过用 <code>position: fixed</code> 将屏幕的其余部分涂黑来创建一个弹出窗口，并且有一些输入和一个提交按钮。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"popup"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h4</span>></span> Login to your account <span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"Email"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"Password"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>></span> Log in <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.popup</span> &#123;
  <span class="hljs-attribute">position</span>: fixed;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">top</span>: ; 
  <span class="hljs-attribute">left</span>: ;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(, , , <span class="hljs-number">0.2</span>);
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
&#125;
<span class="hljs-selector-class">.content</span> &#123;
   <span class="hljs-attribute">min-width</span>: <span class="hljs-number">200px</span>;
   <span class="hljs-attribute">width</span>: <span class="hljs-number">30%</span>;
   <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
   <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
   <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
   <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">5px</span>;
&#125;
<span class="hljs-selector-tag">input</span><span class="hljs-selector-attr">[type=<span class="hljs-string">"text"</span>]</span>, <span class="hljs-selector-tag">input</span><span class="hljs-selector-attr">[type=<span class="hljs-string">"password"</span>]</span> &#123;
  <span class="hljs-attribute">border</span>: ;
  <span class="hljs-attribute">outline</span>: ;
  <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#eee</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">80%</span>;
  <span class="hljs-attribute">margin</span>:  auto;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">0.5em</span>;
&#125;
<span class="hljs-selector-tag">button</span> &#123;
  <span class="hljs-attribute">border</span>: ;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-attribute">background-color</span>:<span class="hljs-number">#8e44ad</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">5px</span> <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">0.5em</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6b0830867ad4c4086983f37417f73b3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而不是像我们通常那样导入它并将其纳入我们的 <code>components</code> 选项中。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- "Standard" way of doing things --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"show = true"</span>></span> Login <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">login-popup</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> LoginPopup <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/LoginPopup.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123; LoginPopup &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以改为使用 <code>defineAsyncComponent</code> 仅在需要时加载它（意味着单击按钮并切换我们的 <code>v-if</code>）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- Use defineAsyncComponent  --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"show = true"</span>></span> Login <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">login-popup</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineAsyncComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123; 
    <span class="hljs-string">"LoginPopup"</span> : defineAsyncComponent(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./components/LoginPopup.vue'</span>))
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">show</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然这在我们使用我们的应用程序时可能看起来是一样的，但让我们检查元素 > 网络来理解这个小而重要的区别。</p>
<p>如果我们不使用 <code>defineAsyncComponent</code>，一旦我们的页面加载，我们就会看到我们的应用程序从服务器上获得<code>LoginPopup.vue</code>。虽然在这个例子中，这可能不是最大的性能问题，但它仍然会减慢加载速度，如果我们有几十个组件这样做，它真的会加起来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d10727639cc34bd488f10cd5ade0a194~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是，如果我们使用 <code>defineAsyncComponent</code> 查看同一个选项卡，我们会注意到当我们的页面加载时，<code>LoginPopup.vue</code> 不见了，这是因为它还没有加载。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63094b8127eb484d9023de25ff024461~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是一旦我们点击我们的按钮并告诉我们的应用程序显示我们的弹出窗口，这时它就会从服务器加载，我们可以在网络标签中看到它。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2578e3dba08a436eaec09ae46d62f7a0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这有助于我们实现最佳性能。我们只想在我们的页面初始加载时加载需要的组件。有条件渲染的组件在我们的页面加载时往往是不需要的，所以为什么要让我们的应用程序加载它们呢？</p>
<h2 data-id="heading-2">如何使用异步设置功能</h2>
<p>无论我们是否使用 <code>defineAsyncComponent</code> 延迟加载，任何具有异步设置功能的组件都必须用 <code><Suspense></code> 包装。</p>
<p>简而言之，创建一个异步设置函数是我们的一个选择，可以让我们的组件在渲染前等待一些API调用或其他异步动作。</p>
<p>这是我们具有异步设置的组件。它使用 <code>setTimeout()</code> 模拟 API 调用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"popup"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span> Loaded API: &#123;&#123; article &#125;&#125; <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h4</span>></span> Login to your account <span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"Email"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"Password"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>></span> Log in <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">const</span> getArticleInfo = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-comment">// wait 3 seconds to mimic API call</span>
  <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">1000</span>));
  <span class="hljs-keyword">const</span> article = &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'My Vue 3 Article'</span>,
    <span class="hljs-attr">author</span>: <span class="hljs-string">'Matt Maribojoc'</span>
  &#125;
  <span class="hljs-keyword">return</span> article
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> article = <span class="hljs-keyword">await</span> getArticleInfo()
    <span class="hljs-built_in">console</span>.log(article)
    <span class="hljs-keyword">return</span> &#123;
      article
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以在有或没有 <code>defineAsyncComponent</code> 的情况下将它导入到我们的组件中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> LoginPopup <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/LoginPopup.vue'</span>
<span class="hljs-comment">// OR </span>
<span class="hljs-keyword">const</span> LoginPopup = defineAsyncComponent(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"./components/LoginPopup.vue"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是如果我们想让它在我们的模板中渲染，我们需要将它包装在一个 <code>Suspense</code> 元素中。这将等待我们的 <code>setup</code> 函数在尝试渲染我们的组件之前解析。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"show = true"</span>></span> Login <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">default</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">login-popup</span>  /></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">fallback</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span> Loading... <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是结果。用户会看到 "正在加载......"，然后在3秒后（我们的setTimeout的硬编码值），我们的组件将渲染。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d2b9b96bac148cdbc27781697c6cc93~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>默认情况下，我们使用 defineAsyncComponent 定义的所有组件都是可暂停的。</strong></p>
<p>这意味着如果一个组件的父链中有 Suspense，它将被视为该 Suspense 的一个异步依赖。我们的组件的加载、错误、延迟和超时选项将被忽略，而是由 Suspense 来处理。</p>
<h2 data-id="heading-3">最后的想法</h2>
<p><code>defineAsyncComponent</code> 在创建有几十个组件的大型项目时是有好处的。当我们进入到懒惰加载组件时，我们可以有更快的页面加载时间，改善用户体验，并最终提高你的应用程序的保留率和转换率。</p>
<p>我想知道你对这个功能的看法。如果你已经在你的应用中使用它了，请在下面的评论中告诉我。</p>
<hr>
<p>翻译自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flearnvue.co%2F2021%2F06%2Flazy-load-components-in-vue-with-defineasynccomponent%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://learnvue.co/2021/06/lazy-load-components-in-vue-with-defineasynccomponent/" ref="nofollow noopener noreferrer">learnvue.co</a>，作者：Matt Maribojoc</p></div>  
</div>
            