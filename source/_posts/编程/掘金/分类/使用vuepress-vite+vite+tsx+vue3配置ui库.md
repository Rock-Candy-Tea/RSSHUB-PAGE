
---
title: '使用vuepress-vite+vite+tsx+vue3配置ui库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98e73a521c2842bf8dc0084ba0d8a741~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 02:01:42 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98e73a521c2842bf8dc0084ba0d8a741~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">背景</h3>
<p>最近跟朋友开发一个vue3的ui库，希望使用 <code>vite</code> <code>tsx</code> <code>vue3</code>等技术开发，并且可以边开发边通过vuepress文档查看到最新的组件，以下是环境搭建的一些总结</p>
<hr>
<h3 data-id="heading-1">使用技术</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv2.vuepress.vuejs.org%2Fzh%2Fguide%2Fbundler.html%23vite" target="_blank" rel="nofollow noopener noreferrer" title="https://v2.vuepress.vuejs.org/zh/guide/bundler.html#vite" ref="nofollow noopener noreferrer">vuepress-vite</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/" ref="nofollow noopener noreferrer">vite</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.cn.vuejs.org%2Fguide%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.cn.vuejs.org/guide/introduction.html" ref="nofollow noopener noreferrer">vue3</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fjsx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/jsx" ref="nofollow noopener noreferrer">tsx</a> - 待更新</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fesbuild.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://esbuild.github.io/" ref="nofollow noopener noreferrer">esbuild</a> - 待更新</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshelljs%2Fshelljs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shelljs/shelljs" ref="nofollow noopener noreferrer">shelljs</a> - 待更新</li>
</ul>
<hr>
<h3 data-id="heading-2">环境搭建</h3>
<h4 data-id="heading-3">1.  搭建浏览文档的模块</h4>
<p>我们都知道vue的官方文档是使用<code>vuepress</code>展示的，vuepress的展示风格因为经常查看vue文档的缘故，已经特别熟悉了，因此选择vuepress，但是既然都使用了vue3来开发组件了，那能不能使用vite来构建vuepress项目呢，答案可以的，官方vuepress的<code>2.0版本</code>也提供了此方式。</p>
<p>首先创建 my-ui 文件夹并进入</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># my-ui根目录</span>

<span class="hljs-comment"># 环境初始化</span>
yarn init
<span class="hljs-comment"># 安装vuepress、vuepress-vite</span>
yarn add -D vuepress@next vuepress-vite@next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vuepress在运行时会生成缓存目录<code>.cache</code>以及临时目录<code>.temp</code>，这些文件都不需要上传远端，所以都得添加进<code>.gitignore</code>文件中
创建.gitignore</p>
<pre><code class="hljs language-.gitignore copyable" lang=".gitignore">node_modules
docs/.vuepress/.cache
docs/.vuepress/.temp
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建<code>docs</code>目录以及docs中创建<code>.vuepress</code>目录以及<code>READMD.md</code>文件，并在<code>.vuepress</code>中创建vuepress的初始化文件<code>config.ts</code>
结构如下</p>
<pre><code class="copyable">|-- my-ui
    |-- docs
    |   |-- .vuepress
    |       |-- config.ts
    |   |-- README.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vuepress文档展示路由规则将 <code>docs</code> 目录作为你的 sourceDir ，例如你在运行 <code>vuepress docs:dev</code> 命令。此时，你的 Markdown 文件对应的路由路径为：</p>





















<table><thead><tr><th>相对路径</th><th>路由路径</th></tr></thead><tbody><tr><td>/README.md</td><td>/</td></tr><tr><td>/guide/README.MD</td><td>/guide/</td></tr><tr><td>/guide/page.md</td><td>/guide/page.html</td></tr></tbody></table>
<blockquote>
<p>因此，我们在<code>docs/README.md</code>文件中写内容，理论项目启动首页就是该内容</p>
</blockquote>
<p>vuepress要想使用vite打包，官方提供了方式，需要修改配置文件，如下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// docs/.vuepress/config.ts</span>
<span class="hljs-keyword">import</span> &#123; defineUserConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuepress-vite'</span>
<span class="hljs-keyword">import</span> <span class="hljs-keyword">type</span> &#123; DefaultThemeOptions, ViteBundlerOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuepress-vite'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineUserConfig<DefaultThemeOptions, ViteBundlerOptions>(&#123;
  <span class="hljs-comment">// 使用vite模式打包</span>
  <span class="hljs-attr">bundler</span>: <span class="hljs-string">'@vuepress/vite'</span>,
  <span class="hljs-attr">bundlerConfig</span>: &#123;
    <span class="hljs-comment">// vite 打包工具的选项</span>
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>package.json</code>中新增vuepress脚本命令</p>
<pre><code class="hljs language-package.json copyable" lang="package.json">&#123;
  "scripts": &#123;
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，文档浏览模块初始化完毕，运行<code>yarn docs:dev</code>看看效果吧</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98e73a521c2842bf8dc0084ba0d8a741~tplv-k3u1fbpfcp-watermark.image" alt="home.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">2. 通过vite搭建vue3</h4>
<p>或许有的人会疑惑vue3和vuepress之间该怎么共存，是在vuepress中写vue3还是vue3中写vuepress呢？答案是共存关系，举个例子其实就是一个项目中有react和vue两种框架，两种框架运用互相独立，互不影响，只是之间<strong>通过打包</strong>，让其中一个项目能够直接访问另外一个项目的内容</p>
<p>vite提供了vue-ts模板安装的方式<code>demo</code>为项目文件夹名称</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># my-ui 根目录</span>
yarn create @vitejs/app demo --template vue-ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ui库一般是由文档展示模块<code>docs</code>、组件展示模块<code>example</code>、组件包模块<code>packages</code>构成。流程也就是：<strong>在packages中开发，在example中查看，在docs中展示</strong>。所以我们需要修改刚刚创建的vite项目结构</p>
<pre><code class="hljs language-md copyable" lang="md">|-- my-ui                                                                    |-- my-ui
<span class="hljs-code">    |-- package.json                                                             |-- package.json
    |-- yarn.lock                                                                |-- yarn.lock
    |-- docs                                                                     |-- docs
    |   |-- README.md                                                            |   |-- README.md
    |   |-- .vuepress                                                            |   |-- .vuepress
    |       |-- config.ts                                                        |       |-- config.ts
    |-- demo                                                                     |-- example
        |-- .gitignore                                                               |-- assets     
        |-- index.html                                                               |-- components 
        |-- package.json                                                             |-- App.vue
        |-- README.md                                             =>                 |-- main.ts
        |-- tsconfig.json                                                            |-- shims-vue.d.ts     
        |-- vite.config.ts                                                           |-- vite-env.d.ts
        |-- public                                                               |-- favicon.ico
        |   |-- favicon.ico                                                      |-- index.html
        |-- src                                                                  |-- tsconfig.json
            |-- App.vue                                                          |-- vite.config.ts
            |-- main.ts                                                          |-- .gitignore
            |-- shims-vue.d.ts                                                   |-- README.md
            |-- vite-env.d.ts                                                  
            |-- assets                                                  
            |-- components                                                  
</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单来说，就是将vite项目demo中的所有文件移动到根目录中，<code>favicon.icon</code>移动到根目录，删除<code>public</code>，<code>src</code>移动到根目录，改名为<code>example</code>，修改<code>index.html</code>中对<code>main.ts</code>和<code>favicon.icon</code>的引用路径，最后删除demo目录</p>
<blockquote>
<p>注意修改移动项目过后的引用路径，以及将vite的<code>package.json</code> <code>.gitignore</code>和vuepress的<code>package.json</code> <code>.gitignore</code>等需要公用的文件整合</p>
</blockquote>
<p>修改过后的package.json如下</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"my-ui"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"MIT"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"vite:vue"</span>: <span class="hljs-string">"vite"</span>,
    <span class="hljs-attr">"vite:build"</span>: <span class="hljs-string">"vue-tsc --noEmit && vite build"</span>,
    <span class="hljs-attr">"vite:serve"</span>: <span class="hljs-string">"vite preview"</span>,
    <span class="hljs-attr">"docs:dev"</span>: <span class="hljs-string">"vuepress dev docs"</span>,
    <span class="hljs-attr">"docs:build"</span>: <span class="hljs-string">"vuepress build docs"</span>
  &#125;,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"vue"</span>: <span class="hljs-string">"^3.0.5"</span>
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"vuepress"</span>: <span class="hljs-string">"^2.0.0-beta.21"</span>,
    <span class="hljs-attr">"vuepress-vite"</span>: <span class="hljs-string">"^2.0.0-beta.21"</span>,
    <span class="hljs-attr">"@vitejs/plugin-vue"</span>: <span class="hljs-string">"^1.2.4"</span>,
    <span class="hljs-attr">"@vue/compiler-sfc"</span>: <span class="hljs-string">"^3.0.5"</span>,
    <span class="hljs-attr">"typescript"</span>: <span class="hljs-string">"^4.3.2"</span>,
    <span class="hljs-attr">"vite"</span>: <span class="hljs-string">"^2.4.0"</span>,
    <span class="hljs-attr">"vue-tsc"</span>: <span class="hljs-string">"^0.0.24"</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上，vite环境搭建完毕，运行<code>yarn vite:vue</code>查看吧（ps:都看烂了的vue初始项目的首页就不展示啦）</p></div>  
</div>
            