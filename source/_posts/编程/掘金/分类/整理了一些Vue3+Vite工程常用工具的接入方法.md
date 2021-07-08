
---
title: '整理了一些Vue3+Vite工程常用工具的接入方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9135'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 00:57:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=9135'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p><code>Vue3</code> 正式版已经发布一段时间了，和 <code>Vue3</code> 更配的工具 <code>Vite</code> 也已经投入使用了，本文整理了如何将一些常用的工具整合到项目中。</p>
<p>包括 <strong>vue-router</strong> , <strong>vuex</strong> , <strong>typescript</strong> , <strong>sass</strong> , <strong>axios</strong> , <strong>elementUI</strong> , <strong>vant</strong>。以及配置 <strong>环境变量</strong>，假数据 <strong>mock</strong> 等。</p>
<h2 data-id="heading-0">新建项目目录</h2>
<p>输入命令，然后会让你填写工程名称，选择你要使用的技术栈，按照提示操作即可！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn</span>
yarn create @vitejs/app
<span class="hljs-comment">//npm</span>
npm init @vitejs/app
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">配置文件</h2>
<p><code>Vite</code> 的配置文件就是 <strong>根目录</strong> 下的 <code>vite.config.js</code> 。</p>
<p>在 <code>vite</code> 中 <code>vue</code> 需要以插件的形式引入,但是脚手架已经给写好了,了解一下就行。</p>
<p>如果使用 <code>TS</code> ，则需要先安装类型声明文件。</p>
<pre><code class="hljs language-js copyable" lang="js">npm install --save-dev @types/node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入了 <code>defineConfig</code> 插件以后，书写配置文件就可以有代码提示了。</p>
<p>在 <code>vite</code> 中，定义别名不再需要添加 <code>'/'</code> 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vite.config.js</span>

<span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite"</span>;
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">"@vitejs/plugin-vue"</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">"path"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-comment">//定义别名</span>
  <span class="hljs-attr">alias</span>: &#123;
    <span class="hljs-string">"@"</span>: path.resolve(__dirname, <span class="hljs-string">"src"</span>),
    <span class="hljs-attr">coms</span>: path.resolve(__dirname, <span class="hljs-string">"src/components"</span>),
  &#125;,
  <span class="hljs-attr">css</span>: &#123;&#125;,
  <span class="hljs-attr">plugins</span>: [
    vue(),
  ],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">整合axios</h2>
<p>安装依赖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn</span>
yarn add  axios  -S    
<span class="hljs-comment">//npm</span>
npm i axios  -S 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <strong>src目录</strong> 下创建 <code>utils</code> 文件夹，并在 <strong>utils目录</strong> 下创建 <code>request.js</code></p>
<p>大家也可以根据自身需求对 <code>axios</code> 进行二次封装。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//request.ts</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">const</span> baseURL = <span class="hljs-string">''</span>;
<span class="hljs-keyword">const</span> service = axios.create(&#123;
  baseURL,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>, <span class="hljs-comment">// request timeout</span>
&#125;);
<span class="hljs-comment">// 发起请求之前的拦截器</span>
service.interceptors.request.use(
  <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
    <span class="hljs-comment">// 如果有token 就携带tokon</span>
    <span class="hljs-keyword">const</span> token = <span class="hljs-built_in">window</span>.localStorage.getItem(<span class="hljs-string">'accessToken'</span>);
    <span class="hljs-keyword">if</span> (token) &#123;
      config.headers.common.Authorization = token;
    &#125;
    <span class="hljs-keyword">return</span> config;
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> <span class="hljs-built_in">Promise</span>.reject(error)
);
<span class="hljs-comment">// 响应拦截器</span>
service.interceptors.response.use(
  <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> res = response.data;

    <span class="hljs-keyword">if</span> (response.status !== <span class="hljs-number">200</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(res.message || <span class="hljs-string">'Error'</span>));
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> res;
    &#125;
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;
);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> service;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">"../utils/request"</span>;

request(&#123;<span class="hljs-attr">url</span>: <span class="hljs-string">"/profile "</span>,<span class="hljs-attr">method</span>: <span class="hljs-string">"get"</span>&#125;)
.then(<span class="hljs-function">(<span class="hljs-params">res</span>)=></span>&#123;
  <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">整合mock数据</h2>
<p>通过 <code>yarn</code> 或 <code>npm</code> 进行安装</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">//yarn</span>
yarn add mockjs -S   
yarn add vite-plugin-mock -D
yarn add cross-env -D
<span class="hljs-comment">//npm</span>
npm i mockjs -S   
npm i vite-plugin-mock -D
npm i cross-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完之后需要配置 <code>vite.config.js</code> ,如果使用 <code>js</code>发开，则需要配置 <code>supportTs</code> 为 <code>false</code>。其它默认即可。</p>
<p>如果是 <code>ts</code> ,则不需要配置 <code>supportTs</code> 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//导入</span>
<span class="hljs-keyword">import</span> &#123; viteMockServe &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vite-plugin-mock"</span>;
<span class="hljs-comment">//plugins</span>
 plugins: [vue(), viteMockServe(&#123; <span class="hljs-attr">supportTs</span>: <span class="hljs-literal">false</span> &#125;)],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置环境变量，这里要设置为开发环境，下面会讲怎么整合环境变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//package.json  </span>
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"cross-env NODE_ENV=development vite"</span>,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们建一个测试接口进行测试</p>
<p>在 <strong>根目录</strong> 下新建 <code>mock</code> 文件夹， <code>mock</code> 文件夹下新建 <code>users.js</code> 。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//user.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
  &#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">"/api/getUsers"</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">"get"</span>,
    <span class="hljs-attr">response</span>: <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">code</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">"ok"</span>,
        <span class="hljs-attr">data</span>: [<span class="hljs-string">"tom"</span>, <span class="hljs-string">"jerry"</span>],
      &#125;;
    &#125;,
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中发起请求</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//app.vue</span>
<span class="hljs-comment">//此处是封装好的axios请求</span>
request(&#123; <span class="hljs-attr">url</span>: <span class="hljs-string">'/api/getUsers'</span>, <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span> &#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">整合环境变量</h2>
<p>在 <strong>根目录</strong> 下创建 <code>.env.development</code> 和 <code>.env.production</code> 文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .env.development</span>
VITE_APP_ENV = <span class="hljs-string">'development'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .env.production</span>
VITE_APP_ENV = <span class="hljs-string">'production'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>package.json</code>，对环境变量进行配置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//package.json  </span>
<span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-string">"dev"</span>: <span class="hljs-string">"cross-env NODE_ENV=development vite"</span>,
  <span class="hljs-string">"build:dev"</span>: <span class="hljs-string">"vite build --mode development"</span>,
  <span class="hljs-string">"build:pro"</span>: <span class="hljs-string">"vite build --mode production"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">整合vue-router</h2>
<p>通过 <code>yarn</code> 或 <code>npm</code> 进行安装，由于 <code>vue-router4</code> 还没有转成正式版，所以需要加 <code>next</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn</span>
yarn add  vue-router@next -S    
<span class="hljs-comment">//npm</span>
npm i  vue-router@next -S   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>src目录</strong> 下新建 <code>router</code> 文件夹</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//router/index.js</span>
<span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;
<span class="hljs-comment">// hash模式  createWebHashHistory</span>
<span class="hljs-comment">// history模式  createWebHistory</span>

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHashHistory(),
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../views/Home.vue"</span>),
    &#125;,
  ],
&#125;);
    
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在入口文件中引入</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//main.js</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;
createApp(App).use(router).mount(<span class="hljs-string">"#app"</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中使用，<code>vue-router</code> 的使用和新特性不属于本文的内容。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//App.vue</span>
<span class="hljs-comment">//在根节点上添加router-view</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">整合vuex</h2>
<p>通过 <code>yarn</code> 或 <code>npm</code> 进行安装，由于 <code>vuex</code> 还没有转成正式版，所以需要加 <code>next</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn</span>
yarn add vuex@next -S    
<span class="hljs-comment">//npm</span>
npm i vuex@next  -S   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>src目录</strong> 下新建 <code>store</code> 文件夹</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//store/index.js</span>
<span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">couter</span>: <span class="hljs-number">109</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在入口文件中引入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//main.js</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./store"</span>;
createApp(App).use(router).use(store).mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">整合SASS</h2>
<p>通过 <code>yarn</code> 或 <code>npm</code> 进行安装。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn</span>
yarn add sass -D  
<span class="hljs-comment">//npm</span>
npm i sass -D  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>src目录</strong> 下新建 <code>styles</code> 文件夹， <code>index.scss</code> 来存放全局样式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//styles/index.scss</span>
a &#123;
  <span class="hljs-attr">color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以分成多个文件,在 <code>index.scss</code> 中导入即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//styles/index.scss</span>
@<span class="hljs-keyword">import</span> <span class="hljs-string">'./element-ui.scss'</span> <span class="hljs-comment">//组件库的样式覆盖</span>
@<span class="hljs-keyword">import</span> <span class="hljs-string">'./variables.scss'</span> <span class="hljs-comment">//全局变量</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">整合typescript</h2>
<p>只需要在创建项目的时候选择 <code>vue-ts</code> 选项,然后脚手架就会生成 <code>shims-vue.d.ts</code> 文件来支持 <code>ts</code></p>
<p>然后只需要在 <code>script</code> 标签中添加 <code>lang='ts'</code> 即可</p>
<pre><code class="hljs language-js copyable" lang="js"><script lang=<span class="hljs-string">"ts"</span>>
    <span class="hljs-comment">//do something</span>
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">整合element组件库</h2>
<p>首先安装</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn</span>
yarn add  element-plus  -S    
<span class="hljs-comment">//npm</span>
npm i element-plus  -S 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <strong>src目录</strong> 下新建 <code>plugins</code> 文件夹, <strong>plugins目录下</strong> 新建 <code>elementPlus.js </code>文件</p>
<h3 data-id="heading-10">整体引入</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//elementPlus.js</span>

<span class="hljs-keyword">import</span> ElementPlus <span class="hljs-keyword">from</span> <span class="hljs-string">"element-plus"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"element-plus/lib/theme-chalk/index.css"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">app</span>) </span>&#123;
  <span class="hljs-comment">//整体引入</span>
  app.use(ElementPlus);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">按需引入</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ElButton &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"element-plus"</span>;
<span class="hljs-keyword">import</span> &#123; ElInput &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"element-plus"</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">"element-plus/lib/theme-chalk/index.css"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">app</span>) </span>&#123;
  <span class="hljs-comment">//按需引入</span>
  app.use(ElButton);
  app.use(ElInput);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>main.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> ElementPlus <span class="hljs-keyword">from</span> <span class="hljs-string">"plugins/elementPlus"</span>;

createApp(App).use(ElementPlus).mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">移动端适配</h2>
<p>安装依赖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//yarn</span>
yarn add postcss-pxtorem -D
yarn add autoprefixer -D
<span class="hljs-comment">//npm</span>
npm install postcss-pxtorem -D
npm install autoprefixer -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <strong>根目录</strong> 下创建 <code>postcss.config.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-string">"plugins"</span>: &#123;
    <span class="hljs-comment">// 兼容浏览器，添加前缀</span>
    <span class="hljs-attr">autoprefixer</span>: &#123;
      <span class="hljs-attr">overrideBrowserslist</span>: [
        <span class="hljs-string">"Android 4.1"</span>,
        <span class="hljs-string">"iOS 7.1"</span>,
        <span class="hljs-string">"Chrome > 31"</span>,
        <span class="hljs-string">"ff > 31"</span>,
        <span class="hljs-string">"ie >= 8"</span>,
        <span class="hljs-string">"last 10 versions"</span>, <span class="hljs-comment">// 所有主流浏览器最近10版本用</span>
      ],
      <span class="hljs-attr">grid</span>: <span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-string">"postcss-pxtorem"</span>: &#123;
      <span class="hljs-comment">// Vant 官方根字体大小是 37.5</span>
      <span class="hljs-attr">rootValue</span>: <span class="hljs-number">37.5</span>, 
      <span class="hljs-comment">//是一个存储哪些将被转换的属性列表，这里设置为['*']全部，假设需要仅对边框进行设置，可以写['*', '!border*']</span>
      <span class="hljs-attr">propList</span>: [<span class="hljs-string">'*'</span>],
      <span class="hljs-comment">// 过滤掉.norem-开头的class，不进行rem转换</span>
      <span class="hljs-attr">selectorBlackList</span>: [<span class="hljs-string">'.norem'</span>],
      <span class="hljs-attr">unitPrecision</span>: <span class="hljs-number">5</span>, <span class="hljs-comment">//保留rem小数点多少位</span>
      <span class="hljs-attr">mediaQuery</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 媒体查询( @media screen 之类的)中不生效</span>
      <span class="hljs-attr">minPixelValue</span>: <span class="hljs-number">12</span>, <span class="hljs-comment">// px小于12的不会被转换</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <strong>src目录下</strong> 中新建 <code>util</code> 文件夹, <strong>util目录</strong> 下新建 <code>rem.js</code> 等比适配文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// rem.js</span>
<span class="hljs-comment">// rem等比适配配置文件</span>
<span class="hljs-comment">// 基准大小</span>
<span class="hljs-keyword">const</span> baseSize = <span class="hljs-number">37.5</span> 
<span class="hljs-comment">// 注意此值要与 postcss.config.js 文件中的 rootValue保持一致</span>
<span class="hljs-comment">// 设置 rem 函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setRem</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 当前页面宽度相对于 375宽的缩放比例，可根据自己需要修改,一般设计稿都是宽750(图方便可以拿到设计图后改过来)。</span>
  <span class="hljs-keyword">const</span> scale = <span class="hljs-built_in">document</span>.documentElement.clientWidth / <span class="hljs-number">375</span>
  <span class="hljs-comment">// 设置页面根节点字体大小（“Math.min(scale, 2)” 指最高放大比例为2，可根据实际业务需求调整）</span>
  <span class="hljs-built_in">document</span>.documentElement.style.fontSize = baseSize * <span class="hljs-built_in">Math</span>.min(scale, <span class="hljs-number">2</span>) + <span class="hljs-string">'px'</span>
&#125;
<span class="hljs-comment">// 初始化</span>
setRem()
<span class="hljs-comment">// 改变窗口大小时重新设置 rem</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'resize'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我执行了'</span>);
  setRem();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>mian.ts</code> 中引入</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">"./utils/rem"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">整合vant组件库</h2>
<p>安装依赖</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add vant@next -S
npm i vant@next -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意: <code>vite</code> 版本不需要配置组件的按需加载，因为 <code>Vant 3.0</code> 内部所有模块都是基于 <code>ESM</code> 编写的，天然具备按需引入的能力，但是样式必须全部引入。</p>
<p><strong>plugins文件夹</strong> 下新建 <code>vant.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vant <span class="hljs-keyword">from</span> <span class="hljs-string">'vant'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'vant/lib/index.css'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">app</span>) </span>&#123;
  app.use(Vant);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>main.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//main.js</span>
<span class="hljs-keyword">import</span> Vant <span class="hljs-keyword">from</span> <span class="hljs-string">'plugins/vant'</span>;
createApp(App).use(Vant).mount(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">整合代码规范插件eslint,prettier</h2>
<p>安装依赖</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add babel-eslint -D
yarn add @vue/eslint-config-prettier -D
yarn add eslint -D
yarn add eslint-plugin-prettier -D
yarn add eslint-plugin-vue -D
yarn add prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>根目录</strong> 下新建 <code>.eslintrc.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//.eslintrc.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'plugin:vue/vue3-essential'</span>, <span class="hljs-string">'eslint:recommended'</span>],
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">parser</span>: <span class="hljs-string">'babel-eslint'</span>,
  &#125;,
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-comment">//在此处写规则</span>
    <span class="hljs-string">'no-unused-vars'</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 定义未使用的变量</span>
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>根目录</strong> 下新建 <code>.prettierrc.json</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//.prettierrc.json</span>
&#123;
  <span class="hljs-comment">//此处填写规则</span>
  <span class="hljs-string">"singleQuote"</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//单引号</span>
  <span class="hljs-string">"seme"</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//分号</span>
  <span class="hljs-string">"tabWidth"</span>: <span class="hljs-number">2</span>,<span class="hljs-comment">//缩进</span>
  <span class="hljs-string">"TrailingCooma"</span>: <span class="hljs-string">"all"</span>,<span class="hljs-comment">//尾部元素有逗号</span>
  <span class="hljs-string">"bracketSpacing"</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//对象中的空格</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再结合 <code>vscode</code> 的保存自动格式化</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">//settings.json</span>
<span class="hljs-string">"editor.formatOnSave"</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//保存时格式化</span>
<span class="hljs-string">"files.autoSave"</span>: <span class="hljs-string">"onFocusChange"</span>, <span class="hljs-comment">//失去焦点时保存</span>
<span class="hljs-string">"editor.codeActionsOnSave"</span>: &#123;
  <span class="hljs-string">"source.fixAll.eslint"</span>: <span class="hljs-literal">true</span>
&#125;,
<span class="hljs-string">"eslint.validate"</span>: [
  <span class="hljs-string">"javascript"</span>,
  <span class="hljs-string">"javascriptreact"</span>,
  <span class="hljs-string">"typescript"</span>
],  
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">配置GZIP压缩</h2>
<p>安装依赖</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add vite-plugin-compression -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>vite.config.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vite.config.js</span>

<span class="hljs-keyword">import</span> viteCompression <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-compression'</span>
<span class="hljs-attr">plugins</span>:[
  ...
  viteCompression(&#123;
      <span class="hljs-attr">verbose</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">disable</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">threshold</span>: <span class="hljs-number">10240</span>,
      <span class="hljs-attr">algorithm</span>: <span class="hljs-string">'gzip'</span>,
      <span class="hljs-attr">ext</span>: <span class="hljs-string">'.gz'</span>
  &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">部署发布</h2>
<p>执行对应命令即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"dev"</span>: <span class="hljs-string">"cross-env NODE_ENV=development vite"</span>,
<span class="hljs-string">"serve"</span>: <span class="hljs-string">"vite preview"</span>,
<span class="hljs-string">"build:dev"</span>: <span class="hljs-string">"vite build --mode development"</span>,
<span class="hljs-string">"build:pro"</span>: <span class="hljs-string">"vite build --mode production"</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            