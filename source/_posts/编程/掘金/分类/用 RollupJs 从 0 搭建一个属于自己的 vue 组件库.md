
---
title: '用 RollupJs 从 0 搭建一个属于自己的 vue 组件库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b8eccb88a1f43edb0d0705c3341db9d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 02:22:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b8eccb88a1f43edb0d0705c3341db9d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>现在前端的打包工具主要有 <strong>webpack</strong>、 <strong>rollup</strong>、 <strong>gulp</strong>等。</p>
<p><a href="https://www.gulpjs.com.cn/docs/getting-started/quick-start/" target="_blank" rel="nofollow noopener noreferrer"><strong>Gulp</strong></a> 是一个基于任务驱动的自动化构建工具。</p>
<p><a href="https://webpack.docschina.org/guides/getting-started/" target="_blank" rel="nofollow noopener noreferrer"><strong>Webpack</strong></a> 是当下最热门的前端资源模块化 管理和打包工具。它可以将许多松散的模块按照依赖和规则打包成符合生产环境部署的前端资源。还可以将按需加载的模块进行代码分割，等到实际需要的时候再异步加载。</p>
<p><a href="https://www.rollupjs.com/guide/introduction" target="_blank" rel="nofollow noopener noreferrer"><strong>Rollup</strong></a> 是一个 JavaScript 模块打包器，可以将小块代码编译成大块复杂的代码，例如 library 或应用程序。</p>
<p>Rollup 对代码模块使用新的标准化格式，这些标准都包含在 JavaScript 的 ES6 版本中，而不是以前的特殊解决方案，如 CommonJS 和 AMD。ES6 模块可以使你自由、无缝地使用你最喜爱的 library 中那些最有用独立函数，而你的项目不必携带其他未使用的代码。ES6 模块最终还是要由浏览器原生实现，但当前 Rollup 可以使你提前体验。</p>
<p>简单点来说，就是 gulp 适合小项目，基于流程构建；webpack 适用于大型的应用项目，以模块划分，按需加载；而 rollup 适用于工具库的构建，优化代码。现在前端的 vue、 react 框架都是用 rollup 来打包的，也有一些 ui 框架的打包也是用的 rollup。</p>
<p><strong>本文思路参考了 <a href="https://github.com/hug-sun/element3" target="_blank" rel="nofollow noopener noreferrer">Element3</a> 的构建，以 vue3 + rollup + ts + gulp 结合</strong></p>
<h3 data-id="heading-1">初始化工作</h3>
<p>用 npm init 初始化一个项目，然后安装一些必要的 npm 包：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始化</span>
npm init

<span class="hljs-comment">// 安装必要的 rollup 的 npm 包</span>
yarn add -D
    rollup-plugin-vue                <span class="hljs-comment">// 类似于 webpack 的vue-loader，vue 组件的加载器</span>
    rollup-plugin-scss               <span class="hljs-comment">// scss 解析插件</span>
    rollup-plugin-peer-deps-external <span class="hljs-comment">// 打包的时候用来排除 package.json 内 peerDependencies 字段内的包</span>
    @rollup/plugin-node-resolve      <span class="hljs-comment">// 使用Node解析算法定位模块</span>
    @rollup/plugin-commonjs          <span class="hljs-comment">// CommonJS模块转换</span>
    @rollup/plugin-json              <span class="hljs-comment">// json 文件解析</span>
    @rollup/plugin-replace           <span class="hljs-comment">// 在打包文件时替换文件中的字符串</span>
    @rollup/plugin-babel             <span class="hljs-comment">// 转译 JavaScript 新特性</span>
    rollup-plugin-typescript2        <span class="hljs-comment">// 用于解析ts文件，并生成 x.d.ts 类型文件</span>
    rollup-plugin-terser             <span class="hljs-comment">// 包最小化生成，也就是压缩</span>
    
<span class="hljs-comment">// 还需要安装 @vue/compiler-sfc @babel/core typescript rollup </span>
    
<span class="hljs-comment">// package.json</span>
&#123;
  <span class="hljs-string">"peerDependencies"</span>: &#123; <span class="hljs-comment">// 打包将排除vue</span>
    <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^3.0.11"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在根目录新建 tsconfig.json</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"target"</span>: <span class="hljs-string">"esnext"</span>,
    <span class="hljs-attr">"module"</span>: <span class="hljs-string">"esnext"</span>,
    <span class="hljs-attr">"jsx"</span>: <span class="hljs-string">"preserve"</span>,
    <span class="hljs-attr">"declaration"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"importHelpers"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"moduleResolution"</span>: <span class="hljs-string">"node"</span>,
    <span class="hljs-attr">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"sourceMap"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"."</span>,
    <span class="hljs-attr">"allowJs"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"lib"</span>: [<span class="hljs-string">"esnext"</span>, <span class="hljs-string">"dom"</span>, <span class="hljs-string">"dom.iterable"</span>, <span class="hljs-string">"scripthost"</span>],
    <span class="hljs-attr">"outDir"</span>: <span class="hljs-string">"./"</span>,
    <span class="hljs-attr">"resolveJsonModule"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-attr">"include"</span>: [<span class="hljs-string">"src"</span>, <span class="hljs-string">"packages"</span>],
  <span class="hljs-attr">"exclude"</span>: [<span class="hljs-string">"node_modules"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">rollup.config.js</h3>
<p>然后再在根目录新建 rollup.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 引入 rollup 相关的包</span>
<span class="hljs-keyword">import</span> pkg <span class="hljs-keyword">from</span> <span class="hljs-string">'./package.json'</span>
<span class="hljs-keyword">import</span> vuePlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-vue'</span>
<span class="hljs-keyword">import</span> scss <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-scss'</span>
<span class="hljs-keyword">import</span> peerDepsExternal <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-peer-deps-external'</span>
<span class="hljs-keyword">import</span> resolve <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-node-resolve'</span>
<span class="hljs-keyword">import</span> commonjs <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-commonjs'</span>
<span class="hljs-keyword">import</span> json <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-json'</span>
<span class="hljs-keyword">import</span> replace <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-replace'</span>
<span class="hljs-keyword">import</span> babel <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-babel'</span>
<span class="hljs-keyword">import</span> ts <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-typescript2'</span>
<span class="hljs-keyword">import</span> &#123; terser &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-terser'</span>

<span class="hljs-comment">// 先定义一个 base 配置</span>
<span class="hljs-comment">// 创建打包文件的头部信息</span>
<span class="hljs-keyword">const</span> createBanner = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`/*!
  * <span class="hljs-subst">$&#123;pkg.name&#125;</span> v<span class="hljs-subst">$&#123;pkg.version&#125;</span>
  * (c) <span class="hljs-subst">$&#123;<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear()&#125;</span> test
  * @license ISC
  */`</span>
&#125;

<span class="hljs-comment">// 创建基础配置</span>
<span class="hljs-keyword">const</span> createBaseConfig = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">input</span>: <span class="hljs-string">'src/index.ts'</span>, <span class="hljs-comment">// 加载入口</span>
    <span class="hljs-attr">external</span>: [<span class="hljs-string">'vue'</span>],
    <span class="hljs-attr">plugins</span>: [ <span class="hljs-comment">// 插件加载</span>
      peerDepsExternal(),
      vuePlugin(&#123;
        <span class="hljs-attr">css</span>: <span class="hljs-literal">true</span>
      &#125;),
      ts(),
      babel(&#123;
        <span class="hljs-attr">exclude</span>: <span class="hljs-string">'node_modules/**'</span>,
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.vue'</span>],
        <span class="hljs-attr">babelHelpers</span>: <span class="hljs-string">'bundled'</span>
      &#125;),
      resolve(&#123;
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.vue'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.js'</span>]
      &#125;),
      commonjs(),
      json(),
      scss()
    ],
    <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-attr">sourcemap</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">banner</span>: createBanner(),
      <span class="hljs-attr">externalLiveBindings</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">globals</span>: &#123;
        <span class="hljs-attr">vue</span>: <span class="hljs-string">'Vue'</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后定义不同格式的输出及其它配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 生成文件名</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createFileName</span>(<span class="hljs-params">formatName</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`dist/taxreview.<span class="hljs-subst">$&#123;formatName&#125;</span>.js`</span>
&#125;

<span class="hljs-comment">// es-bundle</span>
<span class="hljs-keyword">const</span> esBundleConfig = &#123;
  <span class="hljs-attr">plugins</span>: [
    replace(&#123;
      <span class="hljs-attr">preventAssignment</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">__DEV__</span>: <span class="hljs-string">`(process.env.NODE_ENV !== 'production')`</span>
    &#125;)
  ],
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">file</span>: createFileName(<span class="hljs-string">'esm-bundler'</span>),
    <span class="hljs-attr">format</span>: <span class="hljs-string">'es'</span>
  &#125;
&#125;

<span class="hljs-comment">// cjs</span>
<span class="hljs-keyword">const</span> cjsConfig = &#123;
  <span class="hljs-attr">plugins</span>: [
    replace(&#123;
      <span class="hljs-attr">preventAssignment</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">__DEV__</span>: <span class="hljs-literal">true</span>
    &#125;)
  ],
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">file</span>: createFileName(<span class="hljs-string">'cjs'</span>),
    <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>
  &#125;
&#125;
<span class="hljs-comment">// cjs.prod</span>
<span class="hljs-keyword">const</span> cjsProdConfig = &#123;
  <span class="hljs-attr">plugins</span>: [
    terser(),
    replace(&#123;
      <span class="hljs-attr">preventAssignment</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">__DEV__</span>: <span class="hljs-literal">false</span>
    &#125;)
  ],
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">file</span>: createFileName(<span class="hljs-string">'cjs.prod'</span>),
    <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>
  &#125;
&#125;
<span class="hljs-comment">// 其它的格式还有 es-browser global 等</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于不同的环境打不同的包</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 生产</span>
<span class="hljs-keyword">const</span> prodFormatConfigs = [
  esBundleConfig,
  cjsConfig,
  cjsProdConfig
]
<span class="hljs-keyword">const</span> devFormatConfigs = [esBundleConfig] <span class="hljs-comment">// 开发</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后执行打包程序</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeConfig</span>(<span class="hljs-params">baseConfig, configB</span>) </span>&#123;
  <span class="hljs-keyword">const</span> config = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, baseConfig)
  <span class="hljs-comment">// plugin</span>
  <span class="hljs-keyword">if</span> (configB.plugins) &#123;
    baseConfig.plugins.push(...configB.plugins)
  &#125;

  <span class="hljs-comment">// output</span>
  config.output = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, baseConfig.output, configB.output)

  <span class="hljs-keyword">return</span> config
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createPackageConfigs</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> getFormatConfigs().map(<span class="hljs-function">(<span class="hljs-params">formatConfig</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> mergeConfig(createBaseConfig(), formatConfig)
  &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFormatConfigs</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> process.env.NODE_ENV === <span class="hljs-string">'development'</span>
    ? devFormatConfigs
    : prodFormatConfigs
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createPackageConfigs()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">vue 组件的处理</h3>
<p>在根目录新建一个 packages 文件夹用来存放所有组件，在 packages 内部新建一个 theme-chalk 文件夹用来存放 scss 文件，不要在 vue 文件内直接写 scss，之后 theme-chalk 内的 scss 文件用 gulp 来打包。</p>
<pre><code class="hljs language-html copyable" lang="html">// packages/Test/src/Test.vue
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    &#123;&#123;msg&#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'test'</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> msg = ref(<span class="hljs-string">'test'</span>)

    <span class="hljs-keyword">return</span> &#123; msg &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// packages/Test/index.ts</span>
<span class="hljs-keyword">import</span> Test <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/Test.vue'</span>

<span class="hljs-comment">/* istanbul ignore next */</span>
Test.install = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">app</span>) </span>&#123;
  app.component(Test.name, Test)
&#125;

<span class="hljs-keyword">export</span> &#123; Test &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在根目录下 src/index.ts 执行整个程序的启动</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// src/index.ts</span>
<span class="hljs-keyword">import</span> &#123; Test &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../packages/Test'</span>

<span class="hljs-keyword">import</span> &#123; version &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../package.json'</span>
<span class="hljs-keyword">import</span> &#123; setupGlobalOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./globalConfig'</span> <span class="hljs-comment">// 这个文件用来设置这个ui库的一些全局属性</span>

<span class="hljs-keyword">const</span> components = [
  Test
]

<span class="hljs-comment">// 这个是用 vue.use 用来注册全局组件的</span>
<span class="hljs-keyword">const</span> install = <span class="hljs-function">(<span class="hljs-params">app, opts = &#123;&#125;</span>) =></span> &#123;
  app.use(setupGlobalOptions(opts))

  components.forEach(<span class="hljs-function">(<span class="hljs-params">component</span>) =></span> &#123;
    app.use(component)
  &#125;)

  applyOptions(app)
&#125;

<span class="hljs-comment">// 这个是用来挂载像 Message 这样用 js 来调用的组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyOptions</span>(<span class="hljs-params">app</span>) </span>&#123;
  app.config.globalProperties.$test = Test
&#125;

<span class="hljs-keyword">const</span> taxreview = &#123;
  version,
  install
&#125;

<span class="hljs-comment">// 这个是用来单独引用的</span>
<span class="hljs-keyword">export</span> &#123;
  Test,
  install
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> taxreview
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/globalConfig.ts  用来设置ui库的一些全局属性</span>
<span class="hljs-keyword">import</span> &#123; getCurrentInstance &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-comment">/**
 * get globalOptions $TAXREVIEW config object
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useGlobalOptions</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> instance = getCurrentInstance()

  <span class="hljs-keyword">if</span> (!instance) &#123;
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'useGlobalOptions must be call in setup function'</span>)
    <span class="hljs-keyword">return</span>
  &#125;

  <span class="hljs-keyword">return</span> instance.appContext.config.globalProperties.$TAXREVIEW || &#123;&#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupGlobalOptions</span>(<span class="hljs-params">opts: any = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">app</span>) =></span> &#123;
    app.config.globalProperties.$TAXREVIEW = &#123;
      <span class="hljs-attr">size</span>: opts.size || <span class="hljs-string">''</span>,
      <span class="hljs-attr">zIndex</span>: opts.zIndex || <span class="hljs-number">2000</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还需要修改下 package.json</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"dist/taxreview.cjs.js"</span>, <span class="hljs-comment">// 引入包的主入口文件</span>
  <span class="hljs-attr">"types"</span>: <span class="hljs-string">"dist/src/index.d.ts"</span>, <span class="hljs-comment">// 指定类型声明文件</span>
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"rollup -c"</span> <span class="hljs-comment">// 启动打包</span>
  &#125;
  <span class="hljs-comment">// 其它配置</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里用 yarn build 就可以打包 vue 组件了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b8eccb88a1f43edb0d0705c3341db9d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">css 处理</h3>
<p>我们的全部 css 都放入了 packages/theme-chalk/src 下面，所以我们可以在 packages/theme-chalk 构建 gulp 打包</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// packages/theme-chalk/gulpfile.js</span>
<span class="hljs-meta">'use strict'</span>

<span class="hljs-keyword">const</span> &#123; series, src, dest &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp'</span>)
<span class="hljs-keyword">const</span> sass = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-sass'</span>)
<span class="hljs-keyword">const</span> autoprefixer = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-autoprefixer'</span>)
<span class="hljs-keyword">const</span> cssmin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-cssmin'</span>)

<span class="hljs-comment">// 将 scss 文件转译成 css 文件并压缩放入同级的 lib 文件夹内</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compile</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> src(<span class="hljs-string">'./src/*.scss'</span>)
    .pipe(sass.sync())
    .pipe(
      autoprefixer(&#123;
        <span class="hljs-attr">overrideBrowserslist</span>: [<span class="hljs-string">'ie > 9'</span>, <span class="hljs-string">'last 2 versions'</span>],
        <span class="hljs-attr">cascade</span>: <span class="hljs-literal">false</span>
      &#125;)
    )
    .pipe(cssmin())
    .pipe(dest(<span class="hljs-string">'./lib'</span>))
&#125;

<span class="hljs-comment">// 用来拷贝字体文件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copyfont</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> src(<span class="hljs-string">'./src/fonts/**'</span>).pipe(cssmin()).pipe(dest(<span class="hljs-string">'./lib/fonts'</span>))
&#125;

<span class="hljs-built_in">exports</span>.build = series(compile, copyfont)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在根目录的 package.json 再添加一个处理 scss 的命令</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// cp-cli A B： 命令是将路径 A 的文件全部拷贝到路径 B</span>
&#123;
  <span class="hljs-attr">"build:theme"</span>: <span class="hljs-string">"node scripts/generateCssFile.js && gulp build --gulpfile packages/theme-chalk/gulpfile.js && cp-cli packages/theme-chalk/lib lib/theme-chalk"</span>
&#125;

<span class="hljs-comment">// yarn build:theme</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">最后</h3>
<p>最后我们将包用 npm publish 发布到npm，然后就可以用 yarn add xxx 来应用于项目了。</p>
<p>GitHub: <a href="https://github.com/554246839/rollup-vue" target="_blank" rel="nofollow noopener noreferrer">github.com/554246839/r…</a> master 分支</p></div>  
</div>
            