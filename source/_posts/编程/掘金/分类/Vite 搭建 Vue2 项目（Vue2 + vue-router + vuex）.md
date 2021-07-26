
---
title: 'Vite 搭建 Vue2 项目（Vue2 + vue-router + vuex）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6e70bc29ff2487a8a56e8c1ffd00c95~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 02:29:52 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6e70bc29ff2487a8a56e8c1ffd00c95~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先让我说几句废话。</p>
<p>在写本文时 <code>Vite</code> 没有提供 <code>Vue2</code> 的创建方式。</p>
<p>相信有些开发者还没开始学 <code>Vue3</code>，但又想尝尝 <code>Vite</code>。那可以参考本文的进食方式。</p>
<p>如果心急的话，<strong>“0、简介”</strong> 可以跳过。</p>
<p><br><br></p>
<h3 data-id="heading-0">0、简介</h3>
<p>在写本文时，<code>Vite</code> 默认不提供 <code>Vue2</code> 项目的创建方式。</p>
<p>使用 <code>Vite</code> 创建出来的 <code>Vue</code> 项目，暂时都是 <code>Vue3</code> 的。</p>
<p><code>Vite</code> 是构建工具的高阶封装。它的内部其实是 <code>Rollup</code> 。</p>
<p><code>Vite</code> 是尤雨溪随着 <code>Vue3</code> 正式版 一起发布的一个工具。</p>
<p>最开始 <code>Vite</code> 是为 <code>Vue3</code> 服务的一个工具，但随着 <code>Vite 2.0</code> 发布之后，<code>Vite</code> 就是一个独立的构建工具了。</p>
<p><code>Vite</code> 除了能搭建 <code>Vue3</code> 项目之外，还能搭建 <code>react</code> 等项目。</p>
<br>
<p>Vite 能搭建的项目包括：</p>
<ul>
<li><code>vanilla</code></li>
</ul>

<ul>
<li><code>vanilla-ts</code></li>
<li><code>vue</code></li>
<li><code>vue-ts</code></li>
<li><code>react</code></li>
<li><code>react-ts</code></li>
<li><code>preact</code></li>
<li><code>preact-ts</code></li>
<li><code>lit-element</code></li>
<li><code>lit-element-ts</code></li>
<li><code>svelte</code></li>
<li><code>svelte-ts</code></li>
</ul>
<br>
<p>更详细的介绍请看</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/" ref="nofollow noopener noreferrer">Vite官网（中文版）</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite" ref="nofollow noopener noreferrer">Vite GitHub地址</a></p>
<p><br><br><br><br></p>
<h3 data-id="heading-1">1、初始化 Vue2 项目</h3>
<p>在写本文时，<code>Vite</code> 默认没提供 <code>Vue2</code> 项目创建的选项。</p>
<p>我们可以使用 <code>Vite</code> 创建一个原生项目，然后再安装 <code>Vue2</code> 的生态进行开发。</p>
<h4 data-id="heading-2">1.1、初始化项目</h4>
<p>首先进入项目存放的地方，然后运行以下命令创建项目。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init vite@latest
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>如果是首次使用 <code>Vite</code> 的话，会询问你是否继续，这里回复 y 即可。</p>
<pre><code class="hljs language-bash copyable" lang="bash">Ok to proceed?(y)
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p>之后只需输入项目名称即可，我这里新建的项目名为：vite-vue2。</p>
<pre><code class="hljs language-bash copyable" lang="bash">Project name: vite-vue2
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6e70bc29ff2487a8a56e8c1ffd00c95~tplv-k3u1fbpfcp-watermark.image" alt="createViteVue2ProjectName.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<p>完成以上步骤后，再选择以下要新建的是什么项目即可。</p>
<p>这里选择 <code>vanilla</code> 即可，随后会追问选择 <code>原生</code> 的还是 <code>ts</code> 的，根据自己需求选择即可。</p>
<p>我这里会选择 原生 进行开发。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d7b844ad2a6408286cfcae1632bbb88~tplv-k3u1fbpfcp-watermark.image" alt="selectVanilla.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39db6e8b54704c04b5b5019453ca2135~tplv-k3u1fbpfcp-watermark.image" alt="VanillaNotTs.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<p>项目创建成功后，会出现 3 条提示命令。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 【1】进入项目</span>
<span class="hljs-built_in">cd</span> vite-vue2

<span class="hljs-comment"># 【2】初始化项目</span>
npm install

<span class="hljs-comment"># 【3】运行项目</span>
npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><strong>注意：</strong> 第二步使用 <code>npm install</code> 初始化可能会出现一些小问题，这里建议使用 <code>yarn</code> 初始化项目。</p>
<p>项目目录如下所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fcc686786734278acb16654ebae92a2~tplv-k3u1fbpfcp-watermark.image" alt="projectCatalog.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h4 data-id="heading-3">1.2、安装 vite 对 vue2 支持的插件</h4>
<p>要在 <code>vite</code> 里运行 <code>vue2</code> 项目，需要安装一个 <code>vite</code> 的插件：<code>vite-plugin-vue2</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vite-plugin-vue2 --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 <code>npm</code> 安装不了，可以用 <code>cnpm</code> 或者 <code>yarn</code> 。</p>
<br>
<p>要使用 <code>vite</code> 插件，需要在项目的根目录创建 <code>vite.config.js</code> 文件。</p>
<p>在 <code>vite.config.js</code> 里输入以下代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-vue2'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">plugins</span>: [createVuePlugin()]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 <code>vite-plugin-vue2</code> 插件，并用 <code>Vite</code> 提供的插件注册方法来注册。</p>
<p>需要注意，<code>createVuePlugin()</code> 是跟着括号的，是要执行的！</p>
<br>
<h4 data-id="heading-4">1.3、安装 vue 依赖</h4>
<p>使用以下命令安装 vue2。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vue -S
npm install vue-template-compiler
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在写本文时，通过 <code>npm install vue</code> 安装 <code>vue</code> ，还是会装回 <code>2.x</code> 版本的。</p>
<p>如果后面 <code>vue3</code> 全面更新了，需要安装 <code>vue2</code> 的话，需要在以上命令加上版本号。</p>
<br>
<h4 data-id="heading-5">1.4、修改项目文件依赖关系</h4>
<h5 data-id="heading-6">1.4.1、创建 src 目录</h5>
<p>在项目根目录下创建 <code>src</code> 目录。</p>
<p>然后把 <code>main.js</code> 移到 <code>src</code> 目录里。</p>
<br>
<h5 data-id="heading-7">1.4.2、修改 index.html</h5>
<p>项目启动后，入口文件是 <code>index.html</code> ，而 <code>index.html</code> 原本引入了 <code>main.js</code> ，所以也要修改一下 <code>index.html</code> 文件的指向。</p>
<pre><code class="copyable"><script type="module" src="/src/main.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h5 data-id="heading-8">1.4.3、创建 App.vue 文件</h5>
<p>创建 <code>App.vue</code> 文件，并输入以下代码</p>
<pre><code class="copyable"><template>
  <div>Hello Vite Vue2</div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h5 data-id="heading-9">1.4.4、修改 src/main.js</h5>
<p>这一步的代码就有点像使用 <code>vue-cli</code> 创建的项目里的 <code>main.js</code> 的操作了。</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'

new Vue(&#123;
  render: h => h(App)
&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h4 data-id="heading-10">1.5、运行项目</h4>
<p>经过之前几步的配置，运行以下命令就可以把项目跑起来了。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dea3a23d7d6460cb1bdb930ad97c672~tplv-k3u1fbpfcp-watermark.image" alt="npmrundev.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<h4 data-id="heading-11">1.6、打包</h4>
<p>运行一下命令可以打包项目。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包出来的项目目录名是：<code>dist</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a1217e0b2b244dc81b551234aeb02eb~tplv-k3u1fbpfcp-watermark.image" alt="npmrunbuild.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><br><br><br><br></p>
<h3 data-id="heading-12">2、安装 vue-router</h3>
<h4 data-id="heading-13">2.1、安装</h4>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vue-router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在写本文时，使用以上命令安装的 <code>vue-router</code> 是支持 <code>Vue2</code> 项目的。</p>
<p>如果以后该命令安装的 <code>vue-router</code> 是支持 <code>Vue3</code> 的话，需要自行加一个版本号来约束。</p>
<br>
<h4 data-id="heading-14">2.2 新建路由目录</h4>
<h5 data-id="heading-15">2.2.1、创建路由表</h5>
<p>在 <code>src</code> 目录下创建 <code>router</code> 目录，并在 <code>router</code> 目录下创建 <code>index.js</code> 文件。</p>
<p>在 <code>src/router/index.js</code> 输入以下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../views/Home.vue'</span> <span class="hljs-comment">// 引入 Home页面组件</span>

<span class="hljs-comment">// 注册路由插件</span>
Vue.use(VueRouter)

<span class="hljs-comment">// </span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/About.vue'</span>)
  &#125;
]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h5 data-id="heading-16">2.2.2、创建路由指向的页面组件</h5>
<p>在 <code>src</code> 目录下创建 <code>views</code> 目录，用来存放页面组件。</p>
<p>在 <code>src/views</code> 目录下创建2个页面：<code>Home.vue</code> 和 <code>About.vue</code></p>
<p><code>Home.vue</code> 内容</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    Home
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>About.vue</code> 内容</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    About
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h4 data-id="heading-17">2.3 全局注册</h4>
<h5 data-id="heading-18">2.3.1、在 main.js 里注册</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router/index.js'</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 <code>router</code> ，并且在 <code>new Vue</code> 时注册一下。</p>
<br>
<h5 data-id="heading-19">2.3.2 创建路由跳转标签 并 展示</h5>
<p>修改 <code>App.vue</code> 文件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">nav</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code><router-link></code> 标签定义跳转地址。</p>
<p>使用 <code><router-view></code> 标签展示内容。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcff6478fef9464faa331fac1eb95054~tplv-k3u1fbpfcp-watermark.image" alt="showRouter.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><br><br><br><br></p>
<h3 data-id="heading-20">3、安装 vuex</h3>
<h4 data-id="heading-21">3.1 安装</h4>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vuex --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在写本文时，使用以上命令安装的 <code>vuex</code> 是支持 <code>Vue2</code> 项目的。</p>
<p>如果以后该命令安装的 <code>vuex</code> 是支持 <code>Vue3</code> 的话，需要自行加一个版本号来约束。</p>
<br>
<h4 data-id="heading-22">3.2 新建vuex目录</h4>
<p>在 <code>src</code> 目录下创建 <code>store</code> 目录，并在 <code>store</code> 目录下创建 <code>index.js</code>。</p>
<p>在 <code>index.js</code> 文件输入以下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">count</span>(<span class="hljs-params">state</span>)</span> &#123;
      <span class="hljs-keyword">return</span> state.count
    &#125;
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">addCount</span>(<span class="hljs-params">state, num</span>)</span> &#123;
      state.count += num
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码，在 <code>state</code> 里创建一个变量 <code>count</code> 用作计数器。</p>
<p>在 <code>getters</code> 里提供一个方法获取 <code>count</code>。</p>
<p>在 <code>mutations</code> 里提供一个方法修改 <code>count</code>。</p>
<br>
<h4 data-id="heading-23">3.3 全局注册</h4>
<h5 data-id="heading-24">3.3.1 在 main.js 里注册</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router/index.js'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 <code>store</code> 并在 <code>new Vue</code> 时注册。</p>
<br>
<h5 data-id="heading-25">3.3.2 在 Home.vue 里使用</h5>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>count: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addCount"</span>></span>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">count</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.getters.count;
    &#125;,
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">addCount</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">"addCount"</span>, <span class="hljs-number">1</span>);
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a50726f3003c4869b8f571aef4f02282~tplv-k3u1fbpfcp-watermark.image" alt="showVuex.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><br><br><br><br></p>
<h3 data-id="heading-26">4、参考</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/" ref="nofollow noopener noreferrer">Vite 官方文档</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Funderfin%2Fvite-plugin-vue2" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/underfin/vite-plugin-vue2" ref="nofollow noopener noreferrer">Vite 支持 Vue2 的插件：vite-plugin-vue2 文档</a></p></div>  
</div>
            