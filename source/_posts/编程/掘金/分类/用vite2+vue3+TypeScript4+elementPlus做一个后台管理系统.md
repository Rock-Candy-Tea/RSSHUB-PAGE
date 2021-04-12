
---
title: '用vite2+vue3+TypeScript4+elementPlus做一个后台管理系统'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/375954691d064f50870272f400a8312d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 19:18:24 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/375954691d064f50870272f400a8312d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>祖师爷vite已经更新到2.0版本了，一直还没玩过，这几天自己用vite2.0、vue3.0、typescript搭建了一个简易后台管理系统</p>
</blockquote>
<p>直接上手操作搞一波</p>
<h1 data-id="heading-0">一、开始搭建基础的模板</h1>
<p>使用npm命令：npm init <code>@vitejs/app</code></p>
<p>输入项目名称</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/375954691d064f50870272f400a8312d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>选择vue-ts模板</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b9fa975f9b642f69b165d6e00edfbbd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">二、跳转到package.json目录下安装相关的包</h1>
<p>输入命令： yarn 或者 cnpm i 或者 npm i</p>
<h1 data-id="heading-2">三、项目文件夹一览</h1>
<blockquote>
<p>node_modules  ---依赖文件夹</p>
<p>public  ---公共文件夹</p>
<p>src  ---项目主要文件夹</p>
<p>.gitignore  ---排除git提交配置文件</p>
<p>index.html  ---入口文件</p>
<p>package.json  ---模块描述文件</p>
<p>tsconfig.json  ---ts配置文件</p>
<p>vite.config.ts  ---vite配置文件</p>
</blockquote>
<p>src文件夹一览</p>
<blockquote>
<p>assets  ---静态文件夹</p>
<p>components  ---组件文件夹</p>
<p>App.vue  ---页面文件</p>
<p>main.ts  ---项目入口文件</p>
<p>shims-vue.d.ts  ---类型定义文件（描述文件）</p>
</blockquote>
<h1 data-id="heading-3">四、为vite创建别名</h1>
<p>打开vite.config.ts文件，加入下面代码：</p>
<p><code>const &#123; resolve &#125; = require('path')</code></p>
<p><code>alias: &#123;'@': resolve(__dirname, 'src')&#125;</code></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbb596c8ff994a67a2006218259e5337~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>五、配置tsconfig.json</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-string">"target"</span>: <span class="hljs-string">"esnext"</span>,
    <span class="hljs-string">"module"</span>: <span class="hljs-string">"esnext"</span>,
    <span class="hljs-string">"strict"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"jsx"</span>: <span class="hljs-string">"preserve"</span>,
    <span class="hljs-string">"importHelpers"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"moduleResolution"</span>: <span class="hljs-string">"node"</span>,
    <span class="hljs-string">"experimentalDecorators"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"sourceMap"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"."</span>,
    <span class="hljs-string">"types"</span>: [<span class="hljs-string">"vite/client"</span>],
    <span class="hljs-string">"paths"</span>: &#123;
      <span class="hljs-string">"@/*"</span>: [
        <span class="hljs-string">"src/*"</span>
      ]
    &#125;,
    <span class="hljs-string">"lib"</span>: [
      <span class="hljs-string">"esnext"</span>,
      <span class="hljs-string">"dom"</span>,
      <span class="hljs-string">"dom.iterable"</span>,
      <span class="hljs-string">"scripthost"</span>
    ]
  &#125;,
  <span class="hljs-string">"include"</span>: [
    <span class="hljs-string">"src/**/*.ts"</span>,
    <span class="hljs-string">"src/**/*.tsx"</span>,
    <span class="hljs-string">"src/**/*.vue"</span>,
    <span class="hljs-string">"tests/**/*.ts"</span>,
    <span class="hljs-string">"tests/**/*.tsx"</span>
  ],
  <span class="hljs-string">"exclude"</span>: [
    <span class="hljs-string">"node_modules"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">五、改造App.vue</h1>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123; &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">font-family</span>: Avenir, Helvetica, Arial, sans-serif;
  -webkit-<span class="hljs-attribute">font</span>-smoothing: antialiased;
  -moz-osx-<span class="hljs-attribute">font</span>-smoothing: grayscale;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">六、安装vue-router4</h1>
<p>输入命令：<code>npm install vue-router@4 --save</code></p>
<p>在src下创建router文件夹，在里面创建index.ts文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHistory, RouteRecordRaw &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;

<span class="hljs-keyword">const</span> container = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/pages/container/container.vue'</span>);
<span class="hljs-keyword">const</span> login = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/pages/login/login.vue'</span>);

<span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><RouteRecordRaw> = [
&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/login'</span> &#125;,
&#123;
<span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
<span class="hljs-attr">component</span>: container,
<span class="hljs-attr">children</span>: []
&#125;,
&#123;
<span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
<span class="hljs-attr">name</span>: <span class="hljs-string">'登录'</span>,
<span class="hljs-attr">component</span>: login
&#125;
]

<span class="hljs-keyword">const</span> router = createRouter(&#123;
<span class="hljs-attr">history</span>: createWebHistory(),
routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.ts中引入</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/429893cca0974e8da05169a44688ae1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">七、安装vuex</h1>
<p>输入命令：<code>npm install vuex@next --save</code></p>
<p>在src下创建store文件夹，在里面创建index.ts、getters.ts、mutations.ts、actions.ts文件。</p>
<p>index.ts</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">import</span> getters <span class="hljs-keyword">from</span> <span class="hljs-string">"./getters"</span>;
<span class="hljs-keyword">import</span> mutations <span class="hljs-keyword">from</span> <span class="hljs-string">"./mutations"</span>;
<span class="hljs-keyword">import</span> actions <span class="hljs-keyword">from</span> <span class="hljs-string">"./actions"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(&#123;
<span class="hljs-attr">state</span>: &#123;
<span class="hljs-attr">userInfo</span>: <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">"userInfo"</span>) <span class="hljs-keyword">as</span> string) || &#123;&#125;
&#125;,
getters,
mutations,
actions,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.ts中引入</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862938d74cac46f895b784e8254bc13f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">八、安装element-plus</h1>
<p>输入命令：<code>npm install element-plus --save</code></p>
<p>我这里采用完全引入的方式：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4788564d76b24d549bd862b44f0a4fbe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>也可以根据项目需要按需引入：</p>
<p>首先输入命令：<code>npm install vite-plugin-style-import -D</code></p>
<p>然后，将 vite.config.js 修改为：</p>
<blockquote>
<p>引入 .scss 样式：</p>
<p><strong>请确保已经安装了 sass 依赖并将 element-plus/packages/theme-chalk/src/base.scss 文件在入口文件中引入</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>
<span class="hljs-keyword">import</span> styleImport <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-style-import'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    vue(),
    styleImport(&#123;
      <span class="hljs-attr">libs</span>: [&#123;
        <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'element-plus'</span>,
        <span class="hljs-attr">esModule</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">ensureStyleFile</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">resolveStyle</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          name = name.slice(<span class="hljs-number">3</span>)
          <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/packages/theme-chalk/src/<span class="hljs-subst">$&#123;name&#125;</span>.scss`</span>;
        &#125;,
        <span class="hljs-attr">resolveComponent</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/lib/<span class="hljs-subst">$&#123;name&#125;</span>`</span>;
        &#125;,
      &#125;]
    &#125;)
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入 .css 样式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>
<span class="hljs-keyword">import</span> styleImport <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-style-import'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    vue(),
    styleImport(&#123;
      <span class="hljs-attr">libs</span>: [
        &#123;
          <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'element-plus'</span>,
          <span class="hljs-attr">esModule</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">ensureStyleFile</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">resolveStyle</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/lib/theme-chalk/<span class="hljs-subst">$&#123;name&#125;</span>.css`</span>;
          &#125;,
          <span class="hljs-attr">resolveComponent</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/lib/<span class="hljs-subst">$&#123;name&#125;</span>`</span>;
          &#125;,
        &#125;
      ]
    &#125;)
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h1 data-id="heading-8">结论</h1>
<p>前期的准备工作就到这里结束了，后续就是搭建侧边栏和登录界面了。后台管理系统的基础架构我已初步搭建完毕，已放置我的GitHub仓库，欢迎兄弟们给个start。后续的功能还在开发中，敬请期待。</p>
<p>附上仓库地址：<a href="https://github.com/wuguanfei/vite2-vue3-TypeScript4" target="_blank" rel="nofollow noopener noreferrer">github.com/wuguanfei/v…</a></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/575c8fdca31a4c2c85ff4917ebeaa65c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            