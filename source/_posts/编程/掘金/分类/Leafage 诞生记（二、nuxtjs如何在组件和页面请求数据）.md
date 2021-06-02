
---
title: 'Leafage 诞生记（二、nuxt.js如何在组件和页面请求数据）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5614'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 16:33:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=5614'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文个人博客地址：<a href="https://www.abeille.top/posts/detail/213489UI" target="_blank" rel="nofollow noopener noreferrer">www.abeille.top/posts/detai…</a></p>
<p>在开发Leafage网站的过程中，我试用过viewui(原来叫iview)、element-ui、ant design vue、vuetify这几个组件库，但是约到后面会发现，使用组件库是比较容易开发界面，但是限制很多，而且很多文档写的不好，稍微复杂点的组合或者配置，很难实现，还有最重要的一点，除了vuetify之外的几个组件库， 都不是默认支持响应式的，需要自己适配，后来发现了nuxtjs的官网用的是css样式库<a href="https://tailwindcss.com/" target="_blank" rel="nofollow noopener noreferrer">tailwindcss</a>，与它同样类似的还有bulma，bulma和tailwindcss都是css开发的，不包含任何框架依赖，但是bulma更类似于bootstrap，区别是不依赖jquery等任何Javascript，参考nuxtjs官网的开发，选择使用tailwindcss。</p>
<p>作为一个java开发的程序员，从零开始写前端，还不用组件库，是很难肯痛苦的事情，那找一个好看的模板来模仿，总是容易的吧，然后就开始网罗各大模板网站，有的模板可能需要花几块钱，买一个自己满意的，然后参照来写或者直接进行修改。</p>
<p>页面开发完成之后，需要请求服务接口，由于现在还没有开发后台服务，所以需要使用mock.js来进行api的模拟。</p>
<p><strong>首先安装mock.js依赖：</strong></p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add mock.js -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成后，打开plugins目录，添加 mock.ts 文件（如果使用的是javascript，则创建mock.js），配置mock接口，示例如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Mock <span class="hljs-keyword">from</span> <span class="hljs-string">'mockjs'</span>

Mock.mock(<span class="hljs-regexp">/posts\.json/</span>, &#123;
  <span class="hljs-string">'list|1-10'</span>: [&#123;
    <span class="hljs-string">'id|+1'</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">'title'</span>: <span class="hljs-string">'my title'</span>
  &#125;]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完成之后，需要在nuxt.config.ts文件中进行配置，才会生效，否则，会执行默认的配置；</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-comment">// Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-string">'~/plugins/mock'</span>
  ],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就使用axios请求接口，获取数据了。</p>
<h2 data-id="heading-0">1、配置axios</h2>
<p>因为初始化项目时，安装了axios工具，现在就可以在页面（pages目录下的.vue）或者组件（components目录下的.vue）中使用axios来请求数据。nuxtjs默认会配置axios的一些配置，如果想要进行自己的一些配置，那么在plugins目录下创建axios.ts文件，然后进行相关设置，参考如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@nuxt/types'</span>
<span class="hljs-keyword">import</span> &#123; AxiosRequestConfig, AxiosError &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">const</span> statusCode: <span class="hljs-built_in">any</span> = &#123;
  <span class="hljs-number">400</span>: <span class="hljs-string">'请求参数错误'</span>,
  <span class="hljs-number">401</span>: <span class="hljs-string">'权限不足, 请重新登录'</span>,
  <span class="hljs-number">403</span>: <span class="hljs-string">'服务器拒绝本次访问'</span>,
  <span class="hljs-number">500</span>: <span class="hljs-string">'内部服务器错误'</span>,
  <span class="hljs-number">501</span>: <span class="hljs-string">'服务器不支持该请求中使用的方法'</span>,
  <span class="hljs-number">502</span>: <span class="hljs-string">'网关错误'</span>,
  <span class="hljs-number">504</span>: <span class="hljs-string">'网关超时'</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> accessor: Plugin = <span class="hljs-function">(<span class="hljs-params">&#123; error, app: &#123; $axios &#125;, redirect &#125;</span>) =></span> &#123;

  $axios.onRequest(<span class="hljs-function">(<span class="hljs-params">config: AxiosRequestConfig</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> config
  &#125;)

  $axios.onError(<span class="hljs-function">(<span class="hljs-params">err: AxiosError<<span class="hljs-built_in">any</span>></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> status: <span class="hljs-built_in">any</span> = err.response?.status
    <span class="hljs-keyword">if</span> (status === <span class="hljs-number">404</span>) &#123;
      redirect(<span class="hljs-string">'/error'</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
      error(&#123; <span class="hljs-attr">message</span>: statusCode[status] &#125;)
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(err)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要<strong>注意</strong>的是，当使用typescript时，引入axios的时候，不是</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> axios form <span class="hljs-string">'axios'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而是需要通过@nuxt/types引入Plugin，然后引入axios的AxiosRequestConfig和 AxiosError如果用到axios更多属性，则同样需要引入；</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@nuxt/types'</span>
<span class="hljs-keyword">import</span> &#123; AxiosRequestConfig, AxiosError &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'axios
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>和mockjs同样的，配置完成后，需要在nuxt.config.ts中的plugins项下加入此配置文件；</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-comment">// Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-string">'~/plugins/mock'</span>,
    <span class="hljs-string">'~/plugins/axios'</span>
  ],
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2、使用axios</h2>
<p>基础的使用方法参考<a href="https://www.axios.com/" title="axios" target="_blank" rel="nofollow noopener noreferrer">axios</a>官方文档（中文文档：<a href="http://axios-js.com/zh-cn/docs/" target="_blank" rel="nofollow noopener noreferrer">axios-js.com/zh-cn/docs/</a> ），包括同步请求、异步请求、并发请求等。</p>
<p>在nuxtjs中除了在vue勾子（Hook）中使用axios的一般场景，针对渲染的时机，它还提供了另外两种请求请求数据的函数，fetch() 和 asyncData()。</p>
<p>两个函数的共同点是，都是异步函数，所以在使用时需要await关键字，两者的区别是：</p>
<p>asyncData()：</p>
<ul>
<li>
<p>只能在页面中使用，即pages目录下的.vue文件中，他会阻塞页面的加载，所以不能请求很大的数据量或者很多同步接口；</p>
</li>
<li>
<p>不能使用this关键字；</p>
</li>
<li>
<p>不能被调用，只在页面加载时，自动执行；</p>
</li>
</ul>
<p>fetch()：</p>
<ul>
<li>
<p>可以在组件中使用，也可以在页面中使用，即在components目录和pages目录下的.vue文件中都可以；</p>
</li>
<li>
<p>可以使用this关键字；</p>
</li>
<li>
<p>可以重复调用，即在组件中直接调用fetch()来重新获取数据；</p>
</li>
</ul>
<p>针对两个函数的使用，我们通过一下示例来看看如何使用：</p>
<h4 data-id="heading-2">fetch()示例：</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/composition-api"</span>;
<span class="hljs-keyword">import</span> &#123; SERVER_URL &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"~/assets/request"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Main"</span>,

  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">fetch</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.datas = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$axios
      .get(SERVER_URL.posts.concat(<span class="hljs-string">"?page=0&size=10&order="</span>, <span class="hljs-built_in">this</span>.order))
      .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> res.data);
  &#125;,

  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">datas</span>: [],
      <span class="hljs-attr">order</span>: <span class="hljs-string">"likes"</span>,
    &#125;;
  &#125;,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">retrieve</span>(<span class="hljs-params">order: <span class="hljs-built_in">string</span></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.order = order;
      <span class="hljs-built_in">this</span>.$fetch(); <span class="hljs-comment">// 这里调用fetch()函数，复用接口请求</span>
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例中展示了，fetch()请求接口的使用以及在其他函数中如何被调用执行；</p>
<p>另外，使用fetch()会有一个$fetchState来判断fetch()执行情况，可以根据不同情况处理不同的页面逻辑，示例如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"$fetchState.pending"</span>></span>Fetching mountains...<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"$fetchState.error"</span>></span>An error occurred :(<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mb-12"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">asyncData示例：</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@vue/composition-api"</span>;
<span class="hljs-keyword">import</span> &#123; SERVER_URL &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"~/assets/request"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Portfolio"</span>,

  <span class="hljs-attr">scrollToTop</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 这个配置会在加载页面是自动滚动到页面顶部</span>

  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">asyncData</span>(<span class="hljs-params">&#123; app: &#123; $axios &#125; &#125;</span>)</span> &#123; <span class="hljs-comment">// asyncData()函数中不能使用this关键字，所以这里通过入参方式引入全局配置的一些参数，这里需要axios</span>
    <span class="hljs-keyword">let</span> [datas, categories] = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all([
      <span class="hljs-keyword">await</span> $axios.$get(SERVER_URL.portfolio.concat(<span class="hljs-string">"?page=0&size=10"</span>)),
      <span class="hljs-keyword">await</span> $axios.$get(SERVER_URL.category.concat(<span class="hljs-string">"?page=0&size=5"</span>)),
    ]);
    <span class="hljs-keyword">return</span> &#123; datas, categories &#125;;
  &#125;,

  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">code</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">datas</span>: [],
    &#125;;
  &#125;,

  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">retrieve</span>(<span class="hljs-params">code: <span class="hljs-built_in">string</span></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.code = code;
      <span class="hljs-built_in">this</span>.$axios
        .get(SERVER_URL.portfolio.concat(<span class="hljs-string">"?page=0&size=12&category="</span>, code))
        .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> (<span class="hljs-built_in">this</span>.datas = res.data));
    &#125;,
  &#125;,

  <span class="hljs-function"><span class="hljs-title">head</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> title = <span class="hljs-string">"Portfolio - Leafage"</span>;
    <span class="hljs-keyword">const</span> description =
      <span class="hljs-string">"Leafage的作品集，包含旅行记录、生活分享等资源信息，提供原创、优质、完整内容"</span>;
    <span class="hljs-keyword">return</span> &#123;
      title,
      <span class="hljs-attr">meta</span>: [
        &#123; <span class="hljs-attr">hid</span>: <span class="hljs-string">"description"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"description"</span>, <span class="hljs-attr">content</span>: description &#125;,
        <span class="hljs-comment">// Open Graph</span>
        &#123; <span class="hljs-attr">hid</span>: <span class="hljs-string">"og:title"</span>, <span class="hljs-attr">property</span>: <span class="hljs-string">"og:title"</span>, <span class="hljs-attr">content</span>: title &#125;,
        &#123;
          <span class="hljs-attr">hid</span>: <span class="hljs-string">"og:description"</span>,
          <span class="hljs-attr">property</span>: <span class="hljs-string">"og:description"</span>,
          <span class="hljs-attr">content</span>: description,
        &#125;,
        <span class="hljs-comment">// Twitter Card</span>
        &#123; <span class="hljs-attr">hid</span>: <span class="hljs-string">"twitter:title"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"twitter:title"</span>, <span class="hljs-attr">content</span>: title &#125;,
        &#123;
          <span class="hljs-attr">hid</span>: <span class="hljs-string">"twitter:description"</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">"twitter:description"</span>,
          <span class="hljs-attr">content</span>: description,
        &#125;,
      ],
    &#125;;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过代码可以看到，在asyncData()函数使用时，传入了对象参数 app: &#123; <span class="math math-inline"><span class="katex-error" title="ParseError: KaTeX parse error: Expected 'EOF', got '&#125;' at position 7: axios &#125;̲，因为asyncData()执…" style="color:#cc0000">axios &#125;，因为asyncData()执行的时候，组件还没有初始化完成，因此只能通过引入全局挂在的配置来使用一些工具，同样可以传入 </span></span>store, <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mo separator="true">,</mo></mrow><annotation encoding="application/x-tex">route, </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.80952em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mpunct">,</span></span></span></span></span>router等；</p>
<p>推荐几个模板站：</p>
<ol>
<li><a href="http://www.bootstrapmb.com/" target="_blank" rel="nofollow noopener noreferrer">www.bootstrapmb.com/</a></li>
<li><a href="https://tailwindcomponents.com/" target="_blank" rel="nofollow noopener noreferrer">tailwindcomponents.com/</a></li>
<li><a href="https://www.mobantu.com/6548.html" target="_blank" rel="nofollow noopener noreferrer">www.mobantu.com/6548.html</a></li>
</ol></div>  
</div>
            