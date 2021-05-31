
---
title: '全面总结Vue3.0的新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b0c296c6e7d4b0981d5414fc5aa2b5d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 06:46:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b0c296c6e7d4b0981d5414fc5aa2b5d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>　　Vue3.0从20年九月发布第一个One Piece版本，到现在一直在更新优化；中文版的官方文档也已经放出；那么作为终端用户的我们来看下Vue3新增了哪些功能和特性。</p>
<blockquote>
<p>本文首发于公众号<code>【前端壹读】</code>，更多精彩内容敬请关注公众号最新消息。</p>
</blockquote>
<p>　　尤大大在B站直播时分享了Vue3.0的几个亮点：</p>
<ul>
<li>Performance：性能优化</li>
<li>Tree-shaking support：支持摇树优化</li>
<li>Composition API：组合API</li>
<li>Fragment，Teleport，Suspense：新增的组件</li>
<li>Better TypeScript support：更好的TypeScript支持</li>
<li>Custom Renderer API：自定义渲染器</li>
</ul>
<p>　　在性能方面，对比Vue2.x，性能提升了1.3~2倍左右；打包后的体积也更小了，如果单单写一个HelloWorld进行打包，只有13.5kb；加上所有运行时特性，也不过22.5kb。</p>
<p>　　那么作为终端用户的我们，在开发时，和Vue2.x有什么不同呢？<code>Talk is cheap</code>，我们还是来看代码。</p>
<h1 data-id="heading-0">Tree-shaking</h1>
<p>　　Vue3最重要的变化之一就是引入了Tree-Shaking，Tree-Shaking带来的bundle体积更小是显而易见的。在2.x版本中，很多函数都挂载在全局Vue对象上，比如<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi><mi>e</mi><mi>x</mi><mi>t</mi><mi>T</mi><mi>i</mi><mi>c</mi><mi>k</mi><mtext>、</mtext></mrow><annotation encoding="application/x-tex">nextTick、</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">n</span><span class="mord mathnormal">e</span><span class="mord mathnormal">x</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.13889em;">T</span><span class="mord mathnormal">i</span><span class="mord mathnormal">c</span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mord cjk_fallback">、</span></span></span></span></span>set等函数，因此虽然我们可能用不到，但打包时只要引入了vue这些全局函数仍然会打包进bundle中。</p>
<p>　　而在Vue3中，所有的API都通过ES6模块化的方式引入，这样就能让webpack或rollup等打包工具在打包时对没有用到API进行剔除，最小化bundle体积；我们在main.js中就能发现这样的变化：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//src/main.js</span>
<span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;

<span class="hljs-keyword">const</span> app = createApp(App);
app.use(router).mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　创建app实例方式从原来的<code>new Vue()</code>变为通过createApp函数进行创建；不过一些核心的功能比如virtualDOM更新算法和响应式系统无论如何都是会被打包的；这样带来的变化就是以前在全局配置的组件（Vue.component）、指令（Vue.directive）、混入（Vue.mixin）和插件（Vue.use）等变为直接挂载在实例上的方法；我们通过创建的实例来调用，带来的好处就是一个应用可以有多个Vue实例，不同实例之间的配置也不会相互影响：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app = createApp(App)
app.use(<span class="hljs-comment">/* ... */</span>)
app.mixin(<span class="hljs-comment">/* ... */</span>)
app.component(<span class="hljs-comment">/* ... */</span>)
app.directive(<span class="hljs-comment">/* ... */</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　因此Vue2.x的以下全局API也需要改为ES6模块化引入：</p>
<ul>
<li>Vue.nextTick</li>
<li>Vue.observable不再支持，改为<code>reactive</code></li>
<li>Vue.version</li>
<li>Vue.compile (仅全构建)</li>
<li>Vue.set (仅兼容构建)</li>
<li>Vue.delete (仅兼容构建)</li>
</ul>
<p>　　除此之外，vuex和vue-router也都使用了Tree-Shaking进行了改进，不过api的语法改动不大：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//src/store/index.js</span>
<span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(&#123;
  <span class="hljs-attr">state</span>: &#123;&#125;,
  <span class="hljs-attr">mutations</span>: &#123;&#125;,
  <span class="hljs-attr">actions</span>: &#123;&#125;,
  <span class="hljs-attr">modules</span>: &#123;&#125;,
&#125;);
<span class="hljs-comment">//src/router/index.js</span>
<span class="hljs-keyword">import</span> &#123; createRouter, createWebHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHistory(process.env.BASE_URL),
  routes,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　更多关于Tree-Shaking的使用可以在<a href="https://xieyufei.com.com/2020/07/30/Webpack-Optimize.html" target="_blank" rel="nofollow noopener noreferrer">Webpack配置全解析</a>中查看。</p>
<h1 data-id="heading-1">生命周期函数</h1>
<p>　　我们都知道，在Vue2.x中有8个生命周期函数：</p>
<ul>
<li>beforeCreate</li>
<li>created</li>
<li>beforeMount</li>
<li>mounted</li>
<li>beforeUpdate</li>
<li>updated</li>
<li>beforeDestroy</li>
<li>destroyed</li>
</ul>
<p>　　在vue3中，新增了一个<code>setup</code>生命周期函数，setup执行的时机是在<code>beforeCreate</code>生命函数之前执行，因此在这个函数中是不能通过<code>this</code>来获取实例的；同时为了命名的统一，将<code>beforeDestroy</code>改名为<code>beforeUnmount</code>，<code>destroyed</code>改名为<code>unmounted</code>，因此vue3有以下生命周期函数：</p>
<ul>
<li>beforeCreate（建议使用setup代替）</li>
<li>created（建议使用setup代替）</li>
<li>setup</li>
<li>beforeMount</li>
<li>mounted</li>
<li>beforeUpdate</li>
<li>updated</li>
<li>beforeUnmount</li>
<li>unmounted</li>
</ul>
<p>　　同时，vue3新增了生命周期钩子，我们可以通过在生命周期函数前加<code>on</code>来访问组件的生命周期，我们可以使用以下生命周期钩子：</p>
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
<p>　　那么这些钩子函数如何来进行调用呢？我们在setup中挂载生命周期钩子，当执行到对应的生命周期时，就调用对应的钩子函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; onBeforeMount, onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"----setup----"</span>);
    onBeforeMount(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// beforeMount代码执行</span>
    &#125;);
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// mounted代码执行</span>
    &#125;);
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">新增的功能</h1>
<p>　　说完生命周期，下面就是我们期待的Vue3新增加的那些功能。</p>
<h2 data-id="heading-3">响应式API</h2>
<p>　　我们在<a href="https://xieyufei.com.com/2020/12/16/DefineProperty-Proxy.html" target="_blank" rel="nofollow noopener noreferrer">深入学习Object.defineProperty和Proxy</a>讲解过Proxy优点以及Vue3为什么改用Proxy实现响应式，同时Vue3也将一些响应式的API进行抽离，以便代码更好的复用。</p>
<p>　　我们可以使用<code>reactive</code>来为JS对象创建响应式状态：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive, toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">const</span> user = reactive(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Vue2'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;);
user.name = <span class="hljs-string">'Vue3'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　reactive相当于Vue2.x中的<code>Vue.observable</code>。</p>
<blockquote>
<p>reactive函数只接收object和array等复杂数据类型。</p>
</blockquote>
<p>　　对于一些基本数据类型，比如字符串和数值等，我们想要让它变成响应式，我们当然也可以通过reactive函数创建对象的方式，但是Vue3提供了另一个函数<code>ref</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">const</span> num = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> str = ref(<span class="hljs-string">""</span>);
<span class="hljs-keyword">const</span> male = ref(<span class="hljs-literal">true</span>);

num.value++;
<span class="hljs-built_in">console</span>.log(num.value);

str.value = <span class="hljs-string">"new val"</span>;
<span class="hljs-built_in">console</span>.log(str.value);

male.value = <span class="hljs-literal">false</span>;
<span class="hljs-built_in">console</span>.log(male.value);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　ref返回的响应式对象是只包含一个名为value参数的RefImpl对象，在js中获取和修改都是通过它的value属性；但是在模板中被渲染时，自动展开内部的值，因此不需要在模板中追加<code>.value</code>。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <span>&#123;&#123; count &#125;&#125;</span>
    <button @click="count ++">Increment count</button>
  </div>
</template>

<script>
  import &#123; ref &#125; from 'vue'
  export default &#123;
    setup() &#123;
      const count = ref(0)
      return &#123;
        count
      &#125;
    &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　reactive主要负责复杂数据结构，而ref主要处理基本数据结构；但是很多童鞋就会误解ref只能处理基本数据，ref本身也是能处理对象和数组的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">const</span> obj = ref(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"qwe"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">1</span>,
&#125;);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  obj.value.name = <span class="hljs-string">"asd"</span>;
&#125;, <span class="hljs-number">1000</span>);

<span class="hljs-keyword">const</span> list = ref([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>]);
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  list.value.push(<span class="hljs-number">7</span>);
&#125;, <span class="hljs-number">2000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　当我们处理一些大型响应式对象的property时，我们很希望使用ES6的解构来获取我们想要的值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> book = reactive(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Learn Vue'</span>,
  <span class="hljs-attr">year</span>: <span class="hljs-number">2020</span>,
  <span class="hljs-attr">title</span>: <span class="hljs-string">'Chapter one'</span>
&#125;)
<span class="hljs-keyword">let</span> &#123;
  name,
&#125; = book

name = <span class="hljs-string">'new Learn'</span>
<span class="hljs-comment">// Learn Vue</span>
<span class="hljs-built_in">console</span>.log(book.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　但是很遗憾，这样会消除它的响应式；对于这种情况，我们可以将响应式对象转换为一组ref，这些ref将保留与源对象的响应式关联：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> book = reactive(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Learn Vue'</span>,
  <span class="hljs-attr">year</span>: <span class="hljs-number">2020</span>,
  <span class="hljs-attr">title</span>: <span class="hljs-string">'Chapter one'</span>
&#125;)
<span class="hljs-keyword">let</span> &#123;
  name,
&#125; = toRefs(book)

<span class="hljs-comment">// 注意这里解构出来的name是ref对象</span>
<span class="hljs-comment">// 需要通过value来取值赋值</span>
name.value = <span class="hljs-string">'new Learn'</span>
<span class="hljs-comment">// new Learn</span>
<span class="hljs-built_in">console</span>.log(book.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　对于一些只读数据，我们希望防止它发生任何改变，可以通过<code>readonly</code>来创建一个只读的对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive, readonly &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">let</span> book = reactive(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Learn Vue'</span>,
  <span class="hljs-attr">year</span>: <span class="hljs-number">2020</span>,
  <span class="hljs-attr">title</span>: <span class="hljs-string">'Chapter one'</span>
&#125;)

<span class="hljs-keyword">const</span> copy = readonly(book);
<span class="hljs-comment">//Set operation on key "name" failed: target is readonly.</span>
copy.name = <span class="hljs-string">"new copy"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　有时我们需要的值依赖于其他值的状态，在vue2.x中我们使用<code>computed函数</code>来进行计算属性，在vue3中将computed功能进行了抽离，它接受一个getter函数，并为getter返回的值创建了一个<strong>不可变</strong>的响应式ref对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> num = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> double = computed(<span class="hljs-function">() =></span> num.value * <span class="hljs-number">2</span>);
num.value++;
<span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(double.value);
<span class="hljs-comment">// Warning: computed value is readonly</span>
double.value = <span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　或者我们也可以使用get和set函数创建一个可读写的ref对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> num = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> double = computed(&#123;
  <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> num.value * <span class="hljs-number">2</span>,
  <span class="hljs-attr">set</span>: <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> (num.value = val / <span class="hljs-number">2</span>),
&#125;);

num.value++;
<span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(double.value);

double.value = <span class="hljs-number">8</span>
<span class="hljs-comment">// 4</span>
<span class="hljs-built_in">console</span>.log(num.value);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">响应式侦听</h2>
<p>　　和computed相对应的就是watch，computed是多对一的关系，而watch则是一对多的关系；vue3也提供了两个函数来侦听数据源的变化：watch和watchEffect。</p>
<p>　　我们先来看下watch，它的用法和组件的watch选项用法完全相同，它需要监听某个数据源，然后执行具体的回调函数，我们首先看下它监听单个数据源的用法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive, ref, watch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">const</span> state = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
&#125;);

<span class="hljs-comment">//侦听时返回值得getter函数</span>
watch(
  <span class="hljs-function">() =></span> state.count,
  <span class="hljs-function">(<span class="hljs-params">count, prevCount</span>) =></span> &#123;
    <span class="hljs-comment">// 1 0</span>
    <span class="hljs-built_in">console</span>.log(count, prevCount);
  &#125;
);
state.count++;

<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
<span class="hljs-comment">//直接侦听ref</span>
watch(count, <span class="hljs-function">(<span class="hljs-params">count, prevCount</span>) =></span> &#123;
  <span class="hljs-comment">// 2 0</span>
  <span class="hljs-built_in">console</span>.log(count, prevCount, <span class="hljs-string">"watch"</span>);
&#125;);
count.value = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们也可以把多个值放在一个数组中进行侦听，最后的值也以数组形式返回：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> state = reactive(&#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">1</span>,
&#125;);
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">2</span>);
watch([<span class="hljs-function">() =></span> state.count, count], <span class="hljs-function">(<span class="hljs-params">newVal, oldVal</span>) =></span> &#123;
  <span class="hljs-comment">//[3, 2]  [1, 2]</span>
  <span class="hljs-comment">//[3, 4]  [3, 2]</span>
  <span class="hljs-built_in">console</span>.log(newVal, oldVal);
&#125;);
state.count = <span class="hljs-number">3</span>;

count.value = <span class="hljs-number">4</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　如果我们来侦听一个深度嵌套的对象属性变化时，需要设置<code>deep:true</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> deepObj = reactive(&#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: &#123;
      <span class="hljs-attr">c</span>: <span class="hljs-string">"hello"</span>,
    &#125;,
  &#125;,
&#125;);

watch(
  <span class="hljs-function">() =></span> deepObj,
  <span class="hljs-function">(<span class="hljs-params">val, old</span>) =></span> &#123;
    <span class="hljs-comment">// new hello new hello</span>
    <span class="hljs-built_in">console</span>.log(val.a.b.c, old.a.b.c);
  &#125;,
  &#123; <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span> &#125;
);

deepObj.a.b.c = <span class="hljs-string">"new hello"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　最后的打印结果可以发现都是改变后的值，这是因为侦听一个响应式对象始终返回该对象的引用，因此我们需要对值进行深拷贝：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> _ <span class="hljs-keyword">from</span> <span class="hljs-string">"lodash"</span>;
<span class="hljs-keyword">const</span> deepObj = reactive(&#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: &#123;
      <span class="hljs-attr">c</span>: <span class="hljs-string">"hello"</span>,
    &#125;,
  &#125;,
&#125;);

watch(
  <span class="hljs-function">() =></span> _.cloneDeep(deepObj),
  <span class="hljs-function">(<span class="hljs-params">val, old</span>) =></span> &#123;
    <span class="hljs-comment">// new hello new hello</span>
    <span class="hljs-built_in">console</span>.log(val.a.b.c, old.a.b.c);
  &#125;,
  &#123; <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span> &#125;
);

deepObj.a.b.c = <span class="hljs-string">"new hello"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　一般侦听都会在组件销毁时自动停止，但是有时候我们想在组件销毁前手动的方式进行停止，可以调用watch返回的stop函数进行停止：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);

<span class="hljs-keyword">const</span> stop = watch(count, <span class="hljs-function">(<span class="hljs-params">count, prevCount</span>) =></span> &#123;
  <span class="hljs-comment">// 不执行</span>
  <span class="hljs-built_in">console</span>.log(count, prevCount);
&#125;);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
  count.value = <span class="hljs-number">2</span>;
&#125;, <span class="hljs-number">1000</span>);
<span class="hljs-comment">// 停止watch</span>
stop();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　还有一个函数watchEffect也可以用来进行侦听，但是都已经有watch了，这个watchEffect和watch有什么区别呢？他们的用法主要有以下几点不同：</p>
<ol>
<li>watchEffect不需要手动传入依赖</li>
<li>每次初始化时watchEffect都会执行一次回调函数来自动获取依赖</li>
<li>watchEffect无法获取到原值，只能得到变化后的值</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; reactive, ref, watch, watchEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>);
<span class="hljs-keyword">const</span> state = reactive(&#123;
  <span class="hljs-attr">year</span>: <span class="hljs-number">2021</span>,
&#125;);

watchEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(count.value);
  <span class="hljs-built_in">console</span>.log(state.year);
&#125;);
<span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
  count.value++;
  state.year++;
&#125;, <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　watchEffect会在页面加载时自动执行一次，追踪响应式依赖；在加载后定时器每隔1s执行时，watchEffect都会监听到数据的变化自动执行，每次执行都是获取到变化后的值。</p>
<h2 data-id="heading-5">组合API</h2>
<p>　　Composition API（组合API）也是Vue3中最重要的一个功能了，之前的2.x版本采用的是<code>Options API</code>（选项API），即官方定义好了写法：data、computed、methods，需要在哪里写就在哪里写，这样带来的问题就是随着功能增加，代码也越来复杂，我们看代码需要上下反复横跳：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b0c296c6e7d4b0981d5414fc5aa2b5d~tplv-k3u1fbpfcp-zoom-1.image" alt="Composition API对比" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>上图中，一种颜色代表一个功能，我们可以看到<code>Options API</code>的功能代码比较分散；<code>Composition API</code>则可以将同一个功能的逻辑，组织在一个函数内部，利于维护。</p>
</blockquote>
<p>　　我们首先来看下之前Options API的写法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  <span class="hljs-attr">computed</span>: &#123;&#125;,
  <span class="hljs-attr">watch</span>: &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　<code>Options API</code>就是将同一类型的东西放在同一个选项中，当我们的数据比较少的时候，这样的组织方式是比较清晰的；但是随着数据增多，我们维护的功能点会涉及到多个data和methods，但是我们无法感知哪些data和methods是需要涉及到的，经常需要来回切换查找，甚至是需要理解其他功能的逻辑，这也导致了组件难以理解和阅读。</p>
<p>　　而<code>Composition API</code>做的就是把同一功能的代码放到一起维护，这样我们需要维护一个功能点的时候，不用去关心其他的逻辑，只关注当前的功能；<code>Composition API</code>通过<code>setup</code>选项来组织代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, context</span>)</span> &#123;&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们看到这里它接收了两个参数props和context，props就是父组件传入的一些数据，context是一个上下文对象，是从2.x暴露出来的一些属性：</p>
<ul>
<li>attrs</li>
<li>slots</li>
<li>emit</li>
</ul>
<blockquote>
<p>注：props的数据也需要通过toRefs解构，否则响应式数据会失效。</p>
</blockquote>
<p>　　我们通过一个Button按钮来看下setup具体的用法：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f08aee40329431a892e6c91554b1ecf~tplv-k3u1fbpfcp-zoom-1.image" alt="举个栗子" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>&#123;&#123; state.count &#125;&#125; * 2 = &#123;&#123; double &#125;&#125;</div>
  <div>&#123;&#123; num &#125;&#125;</div>
  <div @click="add">Add</div>
</template>
<script>
import &#123; reactive, computed, ref &#125; from "vue";
export default &#123;
  name: "Button",
  setup() &#123;
    const state = reactive(&#123;
      count: 1,
    &#125;);
    const num = ref(2);
    function add() &#123;
      state.count++;
      num.value += 10;
    &#125;
    const double = computed(() => state.count * 2);
    return &#123;
      state,
      double,
      num,
      add,
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　很多童鞋可能就有疑惑了，这跟我在data和methods中写没什么区别么，不就是把他们放到一起么？我们可以将<code>setup</code>中的功能进行提取分割成一个一个独立函数，每个函数还可以在不同的组件中进行逻辑复用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; networkState &#125; = useNetworkState();
    <span class="hljs-keyword">const</span> &#123; user &#125; = userDeatil();
    <span class="hljs-keyword">const</span> &#123; list &#125; = tableData();
    <span class="hljs-keyword">return</span> &#123;
      networkState,
      user,
      list,
    &#125;;
  &#125;,
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useNetworkState</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">userDeatil</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tableData</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Fragment</h2>
<p>　　所谓的Fragment，就是片段；在vue2.x中，要求每个模板必须有一个根节点，所以我们代码要这样写：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　或者在Vue2.x中还可以引入<code>vue-fragments</code>库，用一个虚拟的fragment代替div；在React中，解决方法是通过的一个<code>React.Fragment</code>标签创建一个虚拟元素；在Vue3中我们可以直接不需要根节点：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>hello<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>world<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样就少了很多没有意义的div元素。</p>
<h2 data-id="heading-7">Teleport</h2>
<p>　　Teleport翻译过来就是传送、远距离传送的意思；顾名思义，它可以将插槽中的元素或者组件传送到页面的其他位置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e93713df2044b1195a1c810284ff963~tplv-k3u1fbpfcp-zoom-1.image" alt="传送门游戏" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　在React中可以通过<code>createPortal</code>函数来创建需要传送的节点；本来尤大大想起名叫<code>Portal</code>，但是H5原生的<code>Portal标签</code>也在计划中，虽然有一些安全问题，但是为了避免重名，因此改成<code>Teleport</code>。</p>
<p>　　Teleport一个常见的使用场景，就是在一些嵌套比较深的组件来转移模态框的位置。虽然在逻辑上模态框是属于该组件的，但是在样式和DOM结构上，嵌套层级后较深后不利于进行维护（z-index等问题）；因此我们需要将其进行剥离出来：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <button @click="showDialog = true">打开模态框</button>

  <teleport to="body">
    <div class="modal" v-if="showDialog" style="position: fixed">
      我是一个模态框
      <button @click="showDialog = false">关闭</button>
      <child-component :msg="msg"></child-component>
    </div>
  </teleport>
</template>
<script>
export default &#123;
  data() &#123;
    return &#123;
      showDialog: false,
      msg: "hello"
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这里的Teleport中的modal div就被传送到了body的底部；虽然在不同的地方进行渲染，但是Teleport中的元素和组件还是属于父组件的逻辑子组件，还是可以和父组件进行数据通信。Teleport接收两个参数<code>to</code>和<code>disabled</code>：</p>
<ul>
<li>to - string：必须是有效的查询选择器或 HTMLElement，可以id或者class选择器等。</li>
<li>disabled - boolean：如果是true表示禁用teleport的功能，其插槽内容将不会移动到任何位置，默认false不禁用。</li>
</ul>
<h2 data-id="heading-8">Suspense</h2>
<p>　　Suspense是Vue3推出的一个内置组件，它允许我们的程序在等待异步组件时渲染一些后备的内容，可以让我们创建一个平滑的用户体验；Vue中加载异步组件其实在Vue2.x中已经有了，我们用的vue-router中加载的路由组件其实也是一个异步组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-attr">AsyncButton</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/AsyncButton"</span>),
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在Vue3中重新定义，异步组件需要通过<code>defineAsyncComponent</code>来进行显示的定义：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 全局定义异步组件</span>
<span class="hljs-comment">//src/main.js</span>
<span class="hljs-keyword">import</span> &#123; defineAsyncComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">const</span> AsyncButton = defineAsyncComponent(<span class="hljs-function">() =></span>
  <span class="hljs-keyword">import</span>(<span class="hljs-string">"./components/AsyncButton.vue"</span>)
);
app.component(<span class="hljs-string">"AsyncButton"</span>, AsyncButton);


<span class="hljs-comment">// 组件内定义异步组件</span>
<span class="hljs-comment">// src/views/Home.vue</span>
<span class="hljs-keyword">import</span> &#123; defineAsyncComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-attr">AsyncButton</span>: defineAsyncComponent(<span class="hljs-function">() =></span>
      <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/AsyncButton"</span>)
    ),
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　同时对异步组件的可以进行更精细的管理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-attr">AsyncButton</span>: defineAsyncComponent(&#123;
      <span class="hljs-attr">delay</span>: <span class="hljs-number">100</span>,
      <span class="hljs-attr">timeout</span>: <span class="hljs-number">3000</span>,
      <span class="hljs-attr">loader</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/AsyncButton"</span>),
      <span class="hljs-attr">errorComponent</span>: ErrorComponent,
      <span class="hljs-function"><span class="hljs-title">onError</span>(<span class="hljs-params">error, retry, fail, attempts</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (attempts <= <span class="hljs-number">3</span>) &#123;
          retry();
        &#125; <span class="hljs-keyword">else</span> &#123;
          fail();
        &#125;
      &#125;,
    &#125;),
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　这样我们对异步组件加载情况就能掌控，在加载失败也能重新加载或者展示异常的状态：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a38e1df163db4516b1b97c2d2fa40245~tplv-k3u1fbpfcp-zoom-1.image" alt="异步组件加载失败" loading="lazy" referrerpolicy="no-referrer"></p>
<p>　　我们回到Suspense，上面说到它主要是在组件加载时渲染一些后备的内容，它提供了两个slot插槽，一个<code>default</code>默认，一个<code>fallback</code>加载中的状态：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <button @click="showButton">展示异步组件</button>
    <template v-if="isShowButton">
      <Suspense>
        <template #default>
          <AsyncButton></AsyncButton>
        </template>
        <template #fallback>
          <div>组件加载中...</div>
        </template>
      </Suspense>
    </template>
  </div>
</template>
<script>
export default &#123;
  setup() &#123;
    const isShowButton = ref(false);
    function showButton() &#123;
      isShowButton.value = true;
    &#125;
    return &#123;
      isShowButton,
      showButton,
    &#125;;
  &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7285f570cb94cb6b304be55df9f1128~tplv-k3u1fbpfcp-zoom-1.image" alt="异步组件加载显示占位" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">非兼容的功能</h1>
<p>　　非兼容的功能主要是一些和Vue2.x版本改动较大的语法，已经在Vue3上可能存在兼容问题了。</p>
<h2 data-id="heading-10">data、mixin和filter</h2>
<p>　　在Vue2.x中，我们可以定义data为<code>object</code>或者<code>function</code>，但是我们知道在组件中如果data是object的话会出现数据互相影响，因为object是引用数据类型；</p>
<p>　　在Vue3中，data只接受<code>function</code>类型，通过<code>function</code>返回对象；同时<code>Mixin</code>的合并行为也发生了改变，当mixin和基类中data合并时，会执行浅拷贝合并：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Mixin = &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">user</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Jack'</span>,
        <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">address</span>: &#123;
          <span class="hljs-attr">prov</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">city</span>: <span class="hljs-number">3</span>,
        &#125;,
      &#125;
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">const</span> Component = &#123;
  <span class="hljs-attr">mixins</span>: [Mixin],
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">user</span>: &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">address</span>: &#123;
          <span class="hljs-attr">prov</span>: <span class="hljs-number">4</span>,
        &#125;,
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// vue2结果：</span>
&#123;
  <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Jack'</span>,
  <span class="hljs-attr">address</span>: &#123;
    <span class="hljs-attr">prov</span>: <span class="hljs-number">4</span>,
    <span class="hljs-attr">city</span>: <span class="hljs-number">3</span>
  &#125;
&#125;

<span class="hljs-comment">// vue3结果：</span>
<span class="hljs-attr">user</span>: &#123;
  <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">address</span>: &#123;
    <span class="hljs-attr">prov</span>: <span class="hljs-number">4</span>,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　我们看到最后合并的结果，vue2.x会进行深拷贝，对data中的数据向下深入合并拷贝；而vue3只进行浅层拷贝，对data中数据发现已存在就不合并拷贝。</p>
<p>　　在vue2.x中，我们还可以通过<code>过滤器filter</code>来处理一些文本内容的展示：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>&#123;&#123; status | statusText &#125;&#125;</div>
</template>
<script>
  export default &#123;
    props: &#123;
      status: &#123;
        type: Number,
        default: 1
      &#125;
    &#125;,
    filters: &#123;
      statusText(value)&#123;
        if(value === 1)&#123;
          return '订单未下单'
        &#125; else if(value === 2)&#123;
          return '订单待支付'
        &#125; else if(value === 3)&#123;
          return '订单已完成'
        &#125;
      &#125;
    &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　最常见的就是处理一些订单的文案展示等；然而在vue3中，过滤器filter已经删除，不再支持了，官方建议使用方法调用或者<code>计算属性computed</code>来进行代替。</p>
<h2 data-id="heading-11">v-model</h2>
<p>　　在Vue2.x中，<code>v-model</code>相当于绑定<code>value</code>属性和<code>input</code>事件，它本质也是一个语法糖：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">child-component</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"msg"</span>></span><span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>
<span class="hljs-comment"><!-- 相当于 --></span>
<span class="hljs-tag"><<span class="hljs-name">child-component</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"msg"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"msg=$event"</span>></span><span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在某些情况下，我们需要对多个值进行双向绑定，其他的值就需要显示的使用回调函数来改变了：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">child-component</span> 
    <span class="hljs-attr">v-model</span>=<span class="hljs-string">"msg"</span> 
    <span class="hljs-attr">:msg1</span>=<span class="hljs-string">"msg1"</span> 
    @<span class="hljs-attr">change1</span>=<span class="hljs-string">"msg1=$event"</span>
    <span class="hljs-attr">:msg2</span>=<span class="hljs-string">"msg2"</span> 
    @<span class="hljs-attr">change2</span>=<span class="hljs-string">"msg2=$event"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　在vue2.3.0+版本引入了<code>.sync</code>修饰符，其本质也是语法糖，是在组件上绑定<code>@update:propName</code>回调，语法更简洁：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">child-component</span> 
    <span class="hljs-attr">:msg1.sync</span>=<span class="hljs-string">"msg1"</span> 
    <span class="hljs-attr">:msg2.sync</span>=<span class="hljs-string">"msg2"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>

<span class="hljs-comment"><!-- 相当于 --></span>

<span class="hljs-tag"><<span class="hljs-name">child-component</span> 
    <span class="hljs-attr">:msg1</span>=<span class="hljs-string">"msg1"</span> 
    @<span class="hljs-attr">update:msg1</span>=<span class="hljs-string">"msg1=$event"</span>
    <span class="hljs-attr">:msg2</span>=<span class="hljs-string">"msg2"</span>
    @<span class="hljs-attr">update:msg2</span>=<span class="hljs-string">"msg2=$event"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　Vue3中将<code>v-model</code>和<code>.sync</code>进行了功能的整合，抛弃了.sync，表示：多个双向绑定value值直接用多个v-model传就好了；同时也将v-model默认传的prop名称由value改成了modelValue：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">child-component</span> 
    <span class="hljs-attr">v-model</span>=<span class="hljs-string">"msg"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>

<span class="hljs-comment"><!-- 相当于 --></span>
<span class="hljs-tag"><<span class="hljs-name">child-component</span> 
  <span class="hljs-attr">:modelValue</span>=<span class="hljs-string">"msg"</span>
  @<span class="hljs-attr">update:modelValue</span>=<span class="hljs-string">"msg = $event"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　如果我们想通过v-model传递多个值，可以将一个<code>argument</code>传递给v-model：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">child-component</span> 
    <span class="hljs-attr">v-model.msg1</span>=<span class="hljs-string">"msg1"</span>
    <span class="hljs-attr">v-model.msg2</span>=<span class="hljs-string">"msg2"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>

<span class="hljs-comment"><!-- 相当于 --></span>
<span class="hljs-tag"><<span class="hljs-name">child-component</span> 
    <span class="hljs-attr">:msg1</span>=<span class="hljs-string">"msg1"</span> 
    @<span class="hljs-attr">update:msg1</span>=<span class="hljs-string">"msg1=$event"</span>
    <span class="hljs-attr">:msg2</span>=<span class="hljs-string">"msg2"</span>
    @<span class="hljs-attr">update:msg2</span>=<span class="hljs-string">"msg2=$event"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">child-component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">v-for和key</h2>
<p>　　在Vue2.x中，我们都知道v-for每次循环都需要给每个子节点一个唯一的key，还不能绑定在template标签上，</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in list"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.id"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.id"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　而在Vue3中，key值应该被放置在template标签上，这样我们就不用为每个子节点设一遍：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in list"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.id"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>...<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">v-bind合并</h2>
<p>　　在vue2.x中，如果一个元素同时定义了<code>v-bind="object"</code>和一个相同的单独的属性，那么这个单独的属性会覆盖<code>object</code>中的绑定：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"&#123; id: 'blue' &#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"&#123; id: 'blue' &#125;"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-comment"><!-- 最后结果都相同 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　然而在vue3中，如果一个元素同时定义了<code>v-bind="object"</code>和一个相同的单独的属性，那么声明绑定的顺序决定了最后的结果（后者覆盖前者）：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- template --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"&#123; id: 'blue' &#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- result --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"blue"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-comment"><!-- template --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"&#123; id: 'blue' &#125;"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- result --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">v-for中ref</h2>
<p>　　vue2.x中，在v-for上使用<code>ref</code>属性，通过<code>this.$refs</code>会得到一个数组：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template
  <div v-for="item in list" :ref="setItemRef"></div>
</template>
<script>
export default &#123;
  data()&#123;
    list: [1, 2]
  &#125;,
  mounted () &#123;
    // [div, div]
    console.log(this.$refs.setItemRef) 
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>　　但是这样可能不是我们想要的结果；因此vue3不再自动创建数组，而是将ref的处理方式变为了函数，该函数默认传入该节点：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template
  <div v-for="item in 3" :ref="setItemRef"></div>
</template>
<script>
import &#123; reactive, onUpdated &#125; from 'vue'
export default &#123;
  setup() &#123;
    let itemRefs = reactive([])

    const setItemRef = el => &#123;
      itemRefs.push(el)
    &#125;

    onUpdated(() => &#123;
      console.log(itemRefs)
    &#125;)

    return &#123;
      itemRefs,
      setItemRef
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">v-for和v-if优先级</h2>
<p>　　在vue2.x中，在一个元素上同时使用v-for和v-if，<code>v-for</code>有更高的优先级，因此在vue2.x中做性能优化，有一个重要的点就是v-for和v-if不能放在同一个元素上。</p>
<p>　　而在vue3中，<code>v-if</code>比<code>v-for</code>有更高的优先级。因此下面的代码，在vue2.x中能正常运行，但是在vue3中v-if生效时并没有<code>item</code>变量，因此会报错：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div v-for="item in list" v-if="item % 2 === 0" :key="item">&#123;&#123; item &#125;&#125;</div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;
      list: [1, 2, 3, 4, 5],
    &#125;;
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">总结</h1>
<p>　　以上就是Vue3.0作为终端用的我们可能会涉及到的一些新特性和新功能，其实Vue3.0还有很多的改动，这里由于篇幅原因就不一一展开了，大家可以自行查阅官方文档，期待Vue3能带给我们更便利更友好的开发体验。</p>
<p>更多前端资料请关注公众号<code>【前端壹读】</code>。</p>
<p>如果觉得写得还不错，请关注我的<a href="https://juejin.im/user/580038cebf22ec0064bd0b2d">掘金主页</a>。更多文章请访问<a href="http://xieyufei.com/" target="_blank" rel="nofollow noopener noreferrer">谢小飞的博客</a></p></div>  
</div>
            