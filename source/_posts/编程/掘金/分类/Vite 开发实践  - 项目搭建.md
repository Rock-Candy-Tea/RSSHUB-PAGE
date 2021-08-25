
---
title: 'Vite 开发实践  - 项目搭建'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b262659dfa3445cdb58819a1e0027d4a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 18:02:34 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b262659dfa3445cdb58819a1e0027d4a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在公司试着用<code>vite</code>搭建了项目，总体来说收获与坑并存吧。一方面<code>vite</code>确实给了我极好的开发体验，另一方面由于它本身出现的时间比较晚，社区生态并不是很完善，所以很多坑还是要自己去踩。不过幸运的是最后都找到了解决办法，后续也准备写几篇文章来细说一下<code>vite</code>里面的一些坑和实践，下面是第一篇文章，<code>vite</code>的相关<strong>环境搭建</strong>部分。</p>
<h2 data-id="heading-1">什么是 vite</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/" ref="nofollow noopener noreferrer"><code>vite</code></a>是一个新型的开发构建工具，开发环境使用<code>esbuild</code>预构建依赖过程，生产环境中使用<code>rollup</code>作为打包工具以适配更好的性能，并以 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FModules" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules" ref="nofollow noopener noreferrer">原生 ESM</a> 方式提供源码。</p>
<p>也就是说，让浏览器接管了打包程序的部分工作，<code>vite</code>只需要<strong>在浏览器请求源码时进行转换并按需提供源码</strong>。根据情景动态导入代码，即<strong>只在当前屏幕上实际使用时才会被处理</strong>。</p>
<p>附一张官方的图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b262659dfa3445cdb58819a1e0027d4a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>它的出现主要是为了解决以下现实问题：</p>
<ul>
<li><strong>缓慢的服务器启动</strong>：以前基于打包器的方式的构建工具（比如 webpack）冷启动开发服务器时，启动必须优先抓取并构建整个应用才能提供服务，当项目越来越大时会非常的耗时。</li>
<li><strong>缓慢的更新</strong>：基于打包器启动时，重建整个包的效率很低，原因同上。</li>
</ul>
<h2 data-id="heading-2">初始化 vite 项目</h2>
<blockquote>
<p>由于作者的技术栈是<code>React</code>，并且项目多以<code>typescript</code>为主，所以本文的示例暂且都以<code>React + TS</code>的方式组织，一些需要额外说明的地方会针对不同框架进行说明。</p>
</blockquote>
<pre><code class="hljs language-sh copyable" lang="sh">npm init vite@latest
<span class="hljs-comment"># or </span>
yarn create vite
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0263a598fb144abac29d2f58ebcf97a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>初始化完成后，可以<code>cd</code>进目录，项目的结构很简单：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d879cf0bccb49d29df481571e851c1c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建完项目后第一步看下<code>package.json</code>文件：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"vite-todo"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.0.0"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"vite"</span>,
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"tsc && vite build"</span>,
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"vite preview"</span>
  &#125;,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"react"</span>: <span class="hljs-string">"^17.0.0"</span>,
    <span class="hljs-attr">"react-dom"</span>: <span class="hljs-string">"^17.0.0"</span>
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@types/react"</span>: <span class="hljs-string">"^17.0.0"</span>,
    <span class="hljs-attr">"@types/react-dom"</span>: <span class="hljs-string">"^17.0.0"</span>,
    <span class="hljs-attr">"@vitejs/plugin-react-refresh"</span>: <span class="hljs-string">"^1.3.1"</span>,
    <span class="hljs-attr">"typescript"</span>: <span class="hljs-string">"^4.3.2"</span>,
    <span class="hljs-attr">"vite"</span>: <span class="hljs-string">"^2.4.4"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>vite</code>本身将启动命令单独抽离出来了，运行<code>npm run dev</code>即可进入开发模式。</p>
<p>继续看项目目录，根目录下有一个<code>vite.config.ts</code>文件，该文件是<code>vite</code>的默认配置文件，<code>vite</code>启动时默认会读取它内部的相关配置。并且还有一个<code>index.html</code>文件，该文件官方也有解释，直接看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2F%23index-html-and-project-root" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/#index-html-and-project-root" ref="nofollow noopener noreferrer">这里</a>就行了。</p>
<p>ok，基本的使用方式我们知道了，不过官方给的目标默认的初始化信息太少了，代码格式和<code>eslint</code>配置等都没有，下面我们就来丰富一些官方的启动模板。</p>
<h2 data-id="heading-3">项目配置</h2>
<blockquote>
<p>项目配置其实大体同<code>webpack</code>的工程化配置，一般就是加入各种插件就行了，并不会有太多不同的写法，目前我这里写的都是<code>vite</code>文档中介绍比较少或者没有介绍的地方，其余包括开发服务的 proxy，css 预处理器的支持推荐看对应的官方文档就行了。</p>
</blockquote>
<h3 data-id="heading-4">添加项目别名</h3>
<p>不管你是<code>ts</code>还是<code>js</code>项目，我这边建议项目别名都添加在两个地方，<code>vite.config.ts</code>和<code>tsconfig.json</code>（或<code>vite.config.js</code>和<code>jsconfig.json</code>）。</p>
<p>前一个配置是为了<code>vite</code>解析时能识别别名，这是必须配置的。后一个配置是为了你的编译器能够识别别名，在我看来这也是不可或缺的，它能给我们带来非常好的开发体验。</p>
<p>具体配置如下：</p>
<p><strong>注意：</strong> 如果你使用的也是 typescript，需要先<code>npm install @types/node -D</code>下载<code>Node API</code>的相关类型提示。</p>
<ul>
<li>
<p><strong>vite.config.ts</strong></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> reactRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-react-refresh'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">relativePath: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.resolve(__dirname, relativePath)
&#125;

<span class="hljs-comment">// https://vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [reactRefresh()],
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: resolve(<span class="hljs-string">'./src'</span>)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>tsconfig.json（或 jsconfig.json）</strong></p>
<p>添加下面这段代码：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"."</span>,
    <span class="hljs-attr">"paths"</span>: &#123;
      <span class="hljs-attr">"@/*"</span>: [<span class="hljs-string">"./src/*"</span>]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>现在，我们的项目中就可以完美地支持别名了。</p>
<h3 data-id="heading-5">修改 tsconfig.json</h3>
<p>vite 原本的<code>tsconfig.json</code>打包时可能会报错，并且在本项目中的文件匹配可能也会出错，所以这边简单改一下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"target"</span>: <span class="hljs-string">"ESNext"</span>,
    <span class="hljs-attr">"lib"</span>: [<span class="hljs-string">"DOM"</span>, <span class="hljs-string">"DOM.Iterable"</span>, <span class="hljs-string">"ESNext"</span>],
    <span class="hljs-attr">"allowJs"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"checkJs"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 填过 lib 检查</span>
    <span class="hljs-attr">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"esModuleInterop"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"strict"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"forceConsistentCasingInFileNames"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"module"</span>: <span class="hljs-string">"ESNext"</span>,
    <span class="hljs-attr">"moduleResolution"</span>: <span class="hljs-string">"Node"</span>,
    <span class="hljs-attr">"resolveJsonModule"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"isolatedModules"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"noEmit"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"jsx"</span>: <span class="hljs-string">"react"</span>,
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"."</span>,
    <span class="hljs-attr">"paths"</span>: &#123;
      <span class="hljs-attr">"@/*"</span>: [<span class="hljs-string">"./src/*"</span>]
    &#125;
  &#125;,
  <span class="hljs-comment">// 只手动排除不检测的目录</span>
  <span class="hljs-attr">"exclude"</span>: [<span class="hljs-string">"node_modules"</span>, <span class="hljs-string">"dist"</span>, <span class="hljs-string">"public"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">添加 eslint 检查 js 代码</h3>
<blockquote>
<p>这里所有配置文件我都建议能用<code>js</code>书写就用<code>js</code>书写，可以很方便地进行代码扩展。</p>
</blockquote>
<ul>
<li>下载<code>eslint</code>相关配置：
<ul>
<li>添加<code>prettier</code>风格
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># 我这边使用的是 prettier 风格，具体可自行选择</span>
npm install eslint eslint-plugin-prettier eslint-config-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加<code>typescript</code>相关 lint
<pre><code class="hljs language-sh copyable" lang="sh">npm install @typescript-eslint/parser @typescript-eslint/eslint-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加<code>ES6</code>模块导入相关 lint
<pre><code class="hljs language-sh copyable" lang="sh">npm install eslint-plugin-import -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加<code>React</code>相关 lint
<pre><code class="hljs language-sh copyable" lang="sh">npm install eslint-plugin-react eslint-plugin-react-hooks eslint-plugin-jsx-a11y -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>一些其他的插件（可选）：如果要用可以自己去查看文档进行配置。
<ul>
<li><code>eslint-plugin-eslint-comments</code>用于指令注释<code>eslint</code>规则应用的最佳实践。</li>
<li><code>eslint-plugin-jest</code>用于使用<code>jest</code>的特定 lint</li>
</ul>
</li>
</ul>
</li>
<li>项目中新增<code>.eslintrc.js</code>文件，相关配置如下：
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> __DEV__ = process.env.NODE_ENV === <span class="hljs-string">'development'</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es2021</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">parser</span>: <span class="hljs-string">'@typescript-eslint/parser'</span>,
  <span class="hljs-comment">// 开启静态检查</span>
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">tsconfigRootDir</span>: __dirname,
    <span class="hljs-attr">project</span>: [<span class="hljs-string">'./tsconfig.json'</span>],
  &#125;,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'@typescript-eslint'</span>],
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">'eslint:recommended'</span>,
    <span class="hljs-string">'plugin:@typescript-eslint/recommended'</span>,
    <span class="hljs-string">'plugin:@typescript-eslint/recommended-requiring-type-checking'</span>,
    <span class="hljs-string">'plugin:import/recommended'</span>,
    <span class="hljs-comment">// ts 支持</span>
    <span class="hljs-string">'plugin:import/typescript'</span>,
    <span class="hljs-string">'plugin:react/recommended'</span>,
    <span class="hljs-string">'plugin:react-hooks/recommended'</span>,
    <span class="hljs-string">'plugin:jsx-a11y/recommended'</span>,
    <span class="hljs-comment">// plugin:prettier/recommended 需要为最后一个扩展</span>
    <span class="hljs-string">'plugin:prettier/recommended'</span>,
  ],
  <span class="hljs-comment">// rules 可根据条件自行配置</span>
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-comment">// prettier</span>
    <span class="hljs-string">'prettier/prettier'</span>: <span class="hljs-string">'warn'</span>,
    <span class="hljs-comment">// ts</span>
    <span class="hljs-string">'@typescript-eslint/no-var-requires'</span>: <span class="hljs-string">'warn'</span>,
    <span class="hljs-string">'@typescript-eslint/no-shadow'</span>: <span class="hljs-string">'error'</span>,
    <span class="hljs-comment">// js</span>
    <span class="hljs-string">'no-shadow'</span>: <span class="hljs-string">'error'</span>,
    <span class="hljs-string">'no-unused-vars'</span>: <span class="hljs-string">'warn'</span>,
    <span class="hljs-string">'no-debugger'</span>: __DEV__ ? <span class="hljs-string">'off'</span> : <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 调试</span>
    <span class="hljs-string">'no-console'</span>: __DEV__ ? <span class="hljs-string">'off'</span> : <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 日志打印</span>
    <span class="hljs-string">'require-yield'</span>: <span class="hljs-string">'warn'</span>, <span class="hljs-comment">// 不允许 generate 函数中没有 yield</span>

    <span class="hljs-comment">// react</span>
    <span class="hljs-string">'react/self-closing-comp'</span>: <span class="hljs-string">'error'</span>,
  &#125;,
  <span class="hljs-comment">// ts 规则单独覆盖</span>
  <span class="hljs-attr">overrides</span>: [
    &#123;
      <span class="hljs-attr">files</span>: [<span class="hljs-string">'*.ts'</span>, <span class="hljs-string">'*.tsx'</span>],
      <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-comment">// use @typescript-eslint/no-shadow</span>
        <span class="hljs-string">'no-shadow'</span>: <span class="hljs-string">'off'</span>,
        <span class="hljs-comment">// use @typescript-eslint/no-unused-vars</span>
        <span class="hljs-string">'no-unused-vars'</span>: <span class="hljs-string">'off'</span>,
      &#125;,
    &#125;,
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>项目中添加忽略文件<code>.eslintignore</code>:
<pre><code class="hljs language-text copyable" lang="text"># 忽略 node_modules、打包目录和公共资源目录
node_modules
dist
public
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>下载<code>vscode</code>的<code>eslint</code>插件</li>
<li>下载<code>vite</code>运行时插件：
<pre><code class="hljs language-sh copyable" lang="sh">npm install vite-plugin-eslint
<span class="copy-code-btn">复制代码</span></code></pre>
加入<code>vite.config.ts</code>中：
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> eslintPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-eslint'</span>
<span class="hljs-keyword">import</span> reactRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-react-refresh'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">relativePath: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.resolve(__dirname, relativePath)
&#125;

<span class="hljs-comment">// https://vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    reactRefresh(),
    eslintPlugin(&#123;
      <span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">include</span>: [<span class="hljs-string">'./src/**/*.[tj]s?(x)'</span>],
    &#125;),
  ],
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: resolve(<span class="hljs-string">'./src'</span>),
    &#125;,
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-7">添加 stylelint 检查 css 代码</h3>
<ul>
<li>下载<code>stylelint</code>相关配置：
<ul>
<li>添加官方推荐配置：
<pre><code class="hljs language-sh copyable" lang="sh">npm install stylelint stylelint-config-standard -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加<code>prettier</code>风格
<pre><code class="hljs language-sh copyable" lang="sh">npm install stylelint-prettier stylelint-config-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加用于排序的规则：
<pre><code class="hljs language-sh copyable" lang="sh">npm install stylelint-order stylelint-config-rational-order -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加提醒样式冲突的规则：
<pre><code class="hljs language-sh copyable" lang="sh">npm install stylelint-declaration-block-no-ignored-properties -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>一些其他插件（可选）：
<ul>
<li><code>stylelint-scss</code>：用于<code>scss</code>文件的规则校验</li>
<li><code>stylelint-less</code>：用于<code>less</code>文件的规则校验</li>
</ul>
</li>
</ul>
</li>
<li>项目中新增<code>.stylelintrc.js</code>文件：
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> prettierConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./prettier.config'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-comment">// 标准配置</span>
    <span class="hljs-string">'stylelint-config-standard'</span>,
    <span class="hljs-comment">// 用于排序</span>
    <span class="hljs-string">'stylelint-config-rational-order'</span>,
    <span class="hljs-comment">// 放在最后</span>
    <span class="hljs-string">'stylelint-prettier/recommended'</span>,
  ],
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 提示书写矛盾的样式</span>
    <span class="hljs-string">'stylelint-declaration-block-no-ignored-properties'</span>,
  ],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'plugin/declaration-block-no-ignored-properties'</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">'prettier/prettier'</span>: [<span class="hljs-literal">true</span>, prettierConfig],
    <span class="hljs-string">'rule-empty-line-before'</span>: [
      <span class="hljs-string">'always'</span>,
      &#123;
        <span class="hljs-comment">// 防止和 prettier 冲突</span>
        <span class="hljs-attr">except</span>: [<span class="hljs-string">'first-nested'</span>],
      &#125;,
    ],
    <span class="hljs-string">'selector-pseudo-class-no-unknown'</span>: [
      <span class="hljs-literal">true</span>,
      &#123;
        <span class="hljs-attr">ignorePseudoClasses</span>: [<span class="hljs-string">'global'</span>],
      &#125;,
    ],
  &#125;,
  <span class="hljs-comment">// stylelint 支持直接配置忽略文件</span>
  <span class="hljs-attr">ignoreFiles</span>: [<span class="hljs-string">'node_modules/**/*'</span>, <span class="hljs-string">'dist/**/*'</span>, <span class="hljs-string">'public/**/*'</span>],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>下载<code>vscode</code>的<code>prettier</code>插件</li>
<li>下载<code>vite</code>运行时插件：
<pre><code class="hljs language-sh copyable" lang="sh">npm install @amatlash/vite-plugin-stylelint
<span class="copy-code-btn">复制代码</span></code></pre>
加入<code>vite.config.ts</code>中：
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> eslintPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-eslint'</span>
<span class="hljs-keyword">import</span> viteStylelint <span class="hljs-keyword">from</span> <span class="hljs-string">'@amatlash/vite-plugin-stylelint'</span>
<span class="hljs-keyword">import</span> reactRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-react-refresh'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">relativePath: <span class="hljs-built_in">string</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.resolve(__dirname, relativePath)
&#125;

<span class="hljs-comment">// https://vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    reactRefresh(),
    eslintPlugin(&#123;
      <span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">include</span>: [<span class="hljs-string">'./src/**/*.[tj]s?(x)'</span>],
    &#125;),
    viteStylelint(&#123;
      <span class="hljs-attr">include</span>: <span class="hljs-string">'./src/**/*.(less|scss|css)'</span>,
    &#125;),
  ],
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: resolve(<span class="hljs-string">'./src'</span>),
    &#125;,
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-8">添加 prettier 格式化代码样式</h3>
<ul>
<li>下载<code>prettier</code>：
<pre><code class="hljs language-sh copyable" lang="sh">npm install prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>项目中新增<code>prettier.config.js</code>文件：
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">printWidth</span>: <span class="hljs-number">80</span>,
  <span class="hljs-attr">tabWidth</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">useTabs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">semi</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">singleQuote</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">quoteProps</span>: <span class="hljs-string">'as-needed'</span>,
  <span class="hljs-attr">jsxSingleQuote</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">trailingComma</span>: <span class="hljs-string">'es5'</span>,
  <span class="hljs-attr">bracketSpacing</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">jsxBracketSameLine</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">arrowParens</span>: <span class="hljs-string">'always'</span>,
  <span class="hljs-attr">htmlWhitespaceSensitivity</span>: <span class="hljs-string">'ignore'</span>,
  <span class="hljs-attr">vueIndentScriptAndStyle</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">endOfLine</span>: <span class="hljs-string">'lf'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>项目中添加忽略文件<code>.prettierignore</code>:
<pre><code class="hljs language-text copyable" lang="text">node_modules
dist
public
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>下载<code>vscode</code>的<code>prettier</code>插件</li>
</ul>
<h4 data-id="heading-9">解决 eslint、stylelint 与 prettier 的冲突</h4>
<p>因为我们的<code>eslint</code>和<code>stylelint</code>都是使用的<code>prettier</code>格式的 lint，一般来说都是可以识别项目中的<code>prettier</code>配置的，如果识别不了，一个简单的方法是直接在<code>eslint</code>或<code>stylelint</code>的<code>prettier/prettier</code>中手动同步<code>prettier</code>中的配置（这也是我为什么推荐使用<code>js</code>书写命名文件的原因）。</p>
<p>在<code>.eslintrc.js</code>和<code>.stylelintrc.js</code>中添加下面这句即可：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> prettierConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./prettier.config'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应引入：</p>
<ul>
<li><strong>.eslintrc.js</strong>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// eslint-disable-next-line @typescript-eslint/no-var-requires</span>
<span class="hljs-keyword">const</span> prettierConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./prettier.config'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-string">'prettier/prettier'</span>: [<span class="hljs-string">'warn'</span>, prettierConfig]
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li><strong>.stylelintrc.js</strong>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> prettierConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./prettier.config'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">rules</span>: &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-string">'prettier/prettier'</span>: [<span class="hljs-literal">true</span>, prettierConfig]
        <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-10">添加工作区配置统一格式化风格</h3>
<p>为了统一格式化风格，我们可以直接在项目中添加工作区配置。在根目录下新建一个<code>.vscode</code>目录，在里面创建一个<code>settings.json</code>文件，配置如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
 <span class="hljs-comment">// svg 当做 html 解析</span>
  <span class="hljs-attr">"files.associations"</span>: &#123;
    <span class="hljs-attr">"*.svg"</span>: <span class="hljs-string">"html"</span>,
    <span class="hljs-comment">// 识别所有 rc 配置文件</span>
    <span class="hljs-attr">"*rc"</span>: <span class="hljs-string">"json"</span>
  &#125;,
  <span class="hljs-comment">// 保存时 eslint 自动 fix</span>
  <span class="hljs-attr">"editor.codeActionsOnSave"</span>: &#123;
    <span class="hljs-attr">"source.fixAll"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-comment">// 保存自动格式化</span>
  <span class="hljs-attr">"editor.formatOnSave"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// 文件保存最后空一行</span>
  <span class="hljs-attr">"files.insertFinalNewline"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// eslint 校验文件</span>
  <span class="hljs-attr">"eslint.validate"</span>: [
    <span class="hljs-string">"javascript"</span>,
    <span class="hljs-string">"javascriptreact"</span>,
    <span class="hljs-string">"typescript"</span>,
    <span class="hljs-string">"typescriptreact"</span>
  ],
  <span class="hljs-comment">// 配置默认的格式化工具</span>
  <span class="hljs-attr">"[html]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-attr">"[json]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-attr">"[vue]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-attr">"[typescript]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-attr">"[typescriptreact]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-attr">"[javascript]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
   <span class="hljs-attr">"[javascriptreact]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-attr">"[jsonc]"</span>: &#123;
    <span class="hljs-attr">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">添加 commitlint 检验 git 提交信息</h3>
<p>git 的提交信息校验也是项目中比较重要的一环，一般比较正规的提交信息格式如下：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><<span class="hljs-built_in">type</span>>(<scope>): <subject>
<span class="hljs-comment"># 这里空了一行</span>
(<body>)
<span class="hljs-comment"># 这里空了一行</span>
(<footer>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>scope</code>、<code>body</code>、<code>footer</code>都是可选的，比如：</p>
<pre><code class="hljs language-sh copyable" lang="sh">git commit -m <span class="hljs-string">"feat: init"</span>
<span class="hljs-comment"># or</span>
git commit -m <span class="hljs-string">"feat(project): init"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>规范了信息之后，我们还可以 commit 的内容生成更新日志，非常的方便。下面就是通过 git commit message 自动生成的日志：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bce459d0f474316ab3b4ca8af3ba439~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们需要在每次提交的时候将不符合要求的提交信息拦截，保留正确格式的提交信息。我这边使用<code>commitlint</code>配合<code>husky</code>进行 git 提交校验。</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm install @commitlint/cli @commitlint/config-angular  -D <span class="hljs-comment"># angular的提交格式</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在项目中新建一个<code>commitlint.config.js</code>文件，添加相应规则：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * build : 改变了 build 工具 如 webpack
 * ci : 持续集成新增
 * chore : 构建过程或辅助工具的变动
 * feat : 新功能
 * docs : 文档改变
 * fix : 修复bug
 * perf : 性能优化
 * refactor : 某个已有功能重构
 * revert : 撤销上一次的 commit
 * style : 代码格式改变
 * test : 增加测试
 * anno: 增加注释
 */</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 扩展 angular 的提交配置</span>
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'@commitlint/config-angular'</span>],
  <span class="hljs-comment">// 添加自定义规则</span>
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'type-enum'</span>: [
      <span class="hljs-number">2</span>,
      <span class="hljs-string">'always'</span>,
      [
        <span class="hljs-string">'build'</span>,
        <span class="hljs-string">'ci'</span>,
        <span class="hljs-string">'chore'</span>,
        <span class="hljs-string">'docs'</span>,
        <span class="hljs-string">'feat'</span>,
        <span class="hljs-string">'fix'</span>,
        <span class="hljs-string">'perf'</span>,
        <span class="hljs-string">'refactor'</span>,
        <span class="hljs-string">'revert'</span>,
        <span class="hljs-string">'style'</span>,
        <span class="hljs-string">'test'</span>,
        <span class="hljs-string">'anno'</span>,
      ],
    ],
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后在<code>package.json</code>中添加 git hooks 执行的脚本（可以省略这一步，直接在 git hooks 里执行，但是为了拓展方便还是直接暴露出来吧）</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"scripts"</span>: &#123;
        <span class="hljs-attr">"commit-msg:commitlint"</span>: <span class="hljs-string">"commitlint --config commitlint.config.js -e $HUSKY_GIT_PARAMS"</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为不是为了手动执行，所以尽量语义化一点。</p>
<h4 data-id="heading-12">使用 commitizen 代替 git commit 提交信息</h4>
<p>在上面我们其实只是对提交信息做了约束，让<strong>用户必须手动提交符合要求的 commit message</strong>，事实上我们还可以<strong>依靠可视化的操作自动生成对应的提交信息</strong>，并且附加一些额外信息时也会更方便（比如 breaking changes、issue 的相关信息）。</p>
<p>我这边使用<code>commitizen</code>替代<code>git commit</code>提交信息，<code>commitizen</code>主要有两种使用方式：</p>
<ul>
<li>全局使用
<pre><code class="hljs language-sh copyable" lang="sh">npm install commitizen -g
<span class="copy-code-btn">复制代码</span></code></pre>
然后使用<code>git cz</code>代替<code>git commit</code>执行<code>git</code>命令</li>
<li>局部使用
<pre><code class="hljs language-sh copyable" lang="sh">npm install commitizen -D
<span class="copy-code-btn">复制代码</span></code></pre>
然后使用<code>npx cz</code>执行<code>git</code>命令，当然也可以直接写在<code>package.json</code>的<code>scripts</code>脚本里面：
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
      <span class="hljs-attr">"commit"</span>: <span class="hljs-string">"cz"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>当然，还是加入<code>angular</code>的提交格式（全局和局部使用都是安装在本项目中）：</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm install cz-conventional-changelog -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目中新建一个<code>.czrc</code>文件：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"path"</span>: <span class="hljs-string">"cz-conventional-changelog"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以愉快的使用了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/268e63aa7c154d60b993e51657870c6b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">生成提交日志</h4>
<p>最后，如果我们还想要生成<code>git</code>的提交日志，也可以下载对应的工具，我这里使用<code>conventional-changelog-cli</code>：</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm install conventional-changelog-cli -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>package.json</code>中加入一行命令：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"scripts"</span>: &#123;
        <span class="hljs-attr">"changelog"</span>: <span class="hljs-string">"conventional-changelog -p angular -i CHANGELOG.md -s"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok，现在我们运行<code>npm run changelog</code>就能生成对应日志了。</p>
<h3 data-id="heading-14">添加 lint-staged 检验代码质量</h3>
<p><code>lint-staged</code>一般都需要配合其他工具使用，如果你跟着我们的步骤走，那么现在配套工具也已经准备好了。</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm install lint-staged -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在项目中新建一个<code>.lintstagedrc</code>文件（也可以写在<code>package.json</code>中，但是我个人比较喜欢把配置单独分文件管理），加入下面的代码：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"*.&#123;js,jsx,ts,tsx,css,scss,less,html,md,json&#125;"</span>: [
    <span class="hljs-string">"npm run lint"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后在<code>package.json</code>中加入一行<code>script</code>：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"scripts"</span>: &#123;
        <span class="hljs-attr">"pre-commit:lint-staged"</span>: <span class="hljs-string">"lint-staged"</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，<code>lint-staged</code>我们也不是为了手动运行，它的检验我们一般当做是在其他 action 的附带行为，我在这里也主要是配合 git hooks 操作（<strong>当然我们其实也是能手动运行的</strong>）。</p>
<h3 data-id="heading-15">添加 husky 提供 git hooks 服务</h3>
<p>git hooks 同样也是工程化项目中不可缺少的一环，它可以帮助我们在代码提交时做一系列排错操作，并且还可以检验我们提交的规范性。</p>
<p>在前端项目中我们一般使用<code>husky</code>来提供 git hooks 服务：</p>
<ul>
<li>下载<code>husky</code>
<pre><code class="hljs language-sh copyable" lang="sh">npm install husky -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>启用<code>git</code>钩子
<pre><code class="hljs language-sh copyable" lang="sh">npx husky install
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>在安装依赖后自动启用 git hooks：
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json </span>
&#123; 
    <span class="hljs-attr">"scripts"</span>: &#123; 
        <span class="hljs-attr">"prepare"</span>: <span class="hljs-string">"husky install"</span> 
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>执行完毕后，我们可以看到项目中会多出一个<code>.husky</code>目录，现在里面还没有任何钩子，现在我们来把我们需要的两个钩子加进去：</p>
<ul>
<li>添加<code>pre-commit</code>钩子：
<pre><code class="hljs language-sh copyable" lang="sh">npx husky add .husky/pre-commit <span class="hljs-string">"npm run pre-commit:lint-staged"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>添加<code>commit-msg</code>钩子
<pre><code class="hljs language-sh copyable" lang="sh">npx husky add .husky/pre-commit <span class="hljs-string">"npm run commit-msg:commitlint"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>现在就可以享受到 git hooks 了
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e491db19f98410e9a85eab73c90ed9c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">总结</h2>
<p>本文为 <a href="https://juejin.cn/column/6999905262991573023" target="_blank" title="https://juejin.cn/column/6999905262991573023"><strong>Vite 开发实践</strong></a> 的第一篇文章，从初始化项目开始完整的搭建了一个配置详细的工程化项目，目前本文的相关配置也已经发布到了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCol0ring%2Fvite-react-start-template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Col0ring/vite-react-start-template" ref="nofollow noopener noreferrer"><code>github</code></a>的相关启动模板上，感兴趣的小伙伴可以直接使用。</p>
<p><strong>注意：</strong> 本文的相关配置并不只是适用于<code>vite</code>项目，其余项目都可以引入相关配置项，只需要改变一下运行时的相关插件就可以了。</p>
<blockquote>
<p>另外，官方为我们提供了对应的社区插件仓库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fawesome-vite" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/awesome-vite" ref="nofollow noopener noreferrer">awesome-vite</a>，可以根据自己的需求看看是否有适合的插件。</p>
</blockquote>
<h2 data-id="heading-17">后续</h2>
<p>后续也会加入包括 Vite 插件编写（如何实现 mock 服务等），打包上线、持续集成服务等操作的文章，感兴趣的小伙伴也可以关注一下专栏，顺便给个👍🏻再走呗~~。</p></div>  
</div>
            