
---
title: '【webpack】webpack初体验 - 安装 - 配置 - 打包发布 - 实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92e2fbdc1be8496ca0d6ecb65f02cfe5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 19:59:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92e2fbdc1be8496ca0d6ecb65f02cfe5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>今天来学习前端打包构建工具webpack~</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/" ref="nofollow noopener noreferrer">官网 https://webpack.docschina.org/</a></p>
<h1 data-id="heading-0">0. 起步</h1>
<h2 data-id="heading-1">0.1 webpack 是什么</h2>
<ul>
<li>
<p>webpack 是一种前端资源构建工具，一个静态模块打包器(module bundler)</p>
</li>
<li>
<p>在webpack 看来, 前端的所有资源文件(js/json/css/img/less/...)都会作为模块处理</p>
</li>
<li>
<p>它将根据模块的依赖关系进行静态分析，打包生成对应的静态资源(bundle)</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92e2fbdc1be8496ca0d6ecb65f02cfe5~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">0.2 webpack 五个核心概念</h2>
<h3 data-id="heading-3">0.2.1 Entry 入口</h3>
<blockquote>
<p>指示 webpack 以哪个文件为入口起点开始打包，分析构建内部依赖图。</p>
</blockquote>
<h3 data-id="heading-4">0.2.2 Output 输出</h3>
<blockquote>
<p>指示 webpack 打包后的资源 bundles 输出到哪里去，以及如何命名。</p>
</blockquote>
<h3 data-id="heading-5">0.2.3 Loader</h3>
<blockquote>
<p>让 webpack 能够去处理那些非 JS 的文件，比如样式文件、图片文件(webpack 自身只理解JS)</p>
</blockquote>
<h3 data-id="heading-6">0.2.4 Plugins 插件</h3>
<blockquote>
<p>可以用于执行范围更广的任务。插件的范围包括，从打包优化和压缩，一直到重新定义环境中的变量等</p>
</blockquote>
<h3 data-id="heading-7">0.2.5 Mode 模式</h3>
<blockquote>
<p>指示 webpack 使用相应模式的配置</p>
</blockquote>




















<table><thead><tr><th>选项</th><th>描述</th><th>特点</th></tr></thead><tbody><tr><td>development</td><td>会将 DefinePlugin 中 process.env.NODE_ENV 的值设置为 development。启用 NamedChunksPlugin 和 NamedModulesPlugin</td><td>能让代码本地调试运行的环境</td></tr><tr><td>production</td><td>会将 DefinePlugin 中 process.env.NODE_ENV 的值设置为 production。启用 FlagDependencyUsagePlugin, FlagIncludedChunksPlugin, ModuleConcatenationPlugin, NoEmitOnErrorsPlugin, OccurrenceOrderPlugin, SideEffectsFlagPlugin 和 TerserPlugin</td><td>能让代码优化上线运行的环境</td></tr></tbody></table>
<h1 data-id="heading-8">1. 初始化配置</h1>
<h2 data-id="heading-9">1.1 初始化package.json</h2>
<pre><code class="hljs language-shell copyable" lang="shell">npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">1.2 下载并安装webpack</h2>
<ul>
<li>webpack是核心模块</li>
<li>webpack-cli则是命令行工具</li>
</ul>
<pre><code class="hljs language-powershell copyable" lang="powershell">npm install webpack webpack<span class="hljs-literal">-cli</span> <span class="hljs-literal">-g</span>
npm install webpack webpack<span class="hljs-literal">-cli</span> <span class="hljs-literal">-D</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6110df7cd29145088549d9dbe3d25cab~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6d3039ee1e2445290f43342d7aed3cc~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
默认安装的都是最新的版本</p>
<h1 data-id="heading-11">2. 编译打包应用</h1>
<h2 data-id="heading-12">2.1 创建文件</h2>
<p>创建各种文件目录及文件</p>
<ul>
<li>build文件夹</li>
<li>src文件夹</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ce99dcab0374adebbf026187f87f79a~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
src中创建入口文件  index.js</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56b96ab339934119894f379df7f0bf90~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">2.2 运行指令</h2>
<h3 data-id="heading-14">2.2.1 开发环境：</h3>
<pre><code class="hljs language-powershell copyable" lang="powershell"> webpack ./src/index.js <span class="hljs-literal">-o</span> ./build/built.js -<span class="hljs-literal">-mode</span>=development
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>webpack会以  ./src/index.js 为<strong>入口</strong>文件开始打包</li>
<li>打包后<strong>输出</strong>到 ./build/built.js</li>
<li>整体打包环境是 <strong>开发环境</strong></li>
</ol>
<p>用这个指令因为版本原因会出错
<code>[webpack-cli] Unknown command './src/index.js'</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/916807bb5907426091769b693ad9e8e6~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
(新版本)</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">webpack -<span class="hljs-literal">-entry</span> ./src/index.js <span class="hljs-literal">-o</span> ./build -<span class="hljs-literal">-mode</span>=development
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包到 ./bulid/main.js</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec1e87eaa6d646538e8455e3cb84fef2~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
也可以用自动打包 打包到 ./dist/main.js<br>
默认打包src下的index到dist文件夹下的main.js</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">npx webpack -<span class="hljs-literal">-mode</span>=development
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8c661b960d94fd491ab8515330f7d81~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
注意这里如果没写 <code>--mode=development</code>会报错</p>
<p>The 'mode' option has not been set, webpack will fallback to 'production' for this value. Set 'mode' option to 'development' or 'production' to enable defaults for each environment.
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d577a9a53f264e9384aae53e3d486eae~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
最后得到的是这样的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43848ba75be34647a078ad246670f797~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
main.js
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d069e8babe747839ca4e4793013c1c7~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
可以直接用node运行
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d58bdcaf6c504d7ca9fffc7a04ff285b~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新建一个html在里面引入打包后的资源
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/811420b7f1ad4a01b751ccefb5fe1a92~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在浏览器运行得到的结果
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9269ccf5832d4865a6065f552d4a1694~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">2.2.2 生产环境</h3>
<pre><code class="hljs language-powershell copyable" lang="powershell">webpack ./src/index.js <span class="hljs-literal">-o</span> ./build/built.js -<span class="hljs-literal">-mode</span>=production
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新版本</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">webpack -<span class="hljs-literal">-entry</span> ./src/index.js <span class="hljs-literal">-o</span> ./build -<span class="hljs-literal">-mode</span>=production
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/933f5523253d45558a96643208c25c29~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-16">3. 结论</h1>
<ol>
<li>
<p>webpack 本身能处理 js/json 资源，不能处理 css/img 等其他资源</p>
</li>
<li>
<p>生产环境和开发环境将 ES6 模块化编译成浏览器能识别的模块化，但是不能处理 ES6 的基本语法转化为 ES5（需要借助 loader）</p>
</li>
<li>
<p>生产环境比开发环境多一个压缩 js 代码</p>
</li>
</ol>
<h1 data-id="heading-17">4. 问题</h1>
<ol>
<li>不能编译打包css、img 等文件</li>
<li>不能将js 的es6 基本语法转化为es5 以下语法</li>
</ol>
<p>最后，我们来实战使用webpack~</p>
<h1 data-id="heading-18"><em><strong>实战篇</strong></em></h1>
<h2 data-id="heading-19">创建项目</h2>
<p>① 初始化 <code>npm init -y</code> 初始化包管理配置文件package.json</p>
<p>② 新建src源代码目录</p>
<p>③ 新建 src/index.html 首页</p>
<p>④ 初始化首页的基本结构</p>
<p>⑤ <code>npm install</code> 安装需要的包</p>
<p>⑥ 通过模块化形式 创建src/index.js 写相关js代码</p>
<p>⑦ index.html通过script标签引入index.js 发现不能用，因为浏览器不支持ES6模块化语法</p>
<h2 data-id="heading-20">使用webpack</h2>
<p>① 运行</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">npm install webpack webpack<span class="hljs-literal">-cli</span> <span class="hljs-literal">-D</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装webpack相关包</p>
<p>② 项目根目录创建文件 webpack.config.js 的webpack配置文件</p>
<p>③ 在webpack配置文件中，初始化如下基本配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span> 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>④在package.json配置文件中的scrits节点下新增dev脚本</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>⑤ 终端中运行 <code>npm run dev</code> 命令，启动webpack进行项目打包</p>
<p>⑥ webpack会对src/index.js文件打包自动创建dist/main.js文件
⑦ 在src/index.html通过script标签引入dist/main.js文件，成功了！</p>
<h1 data-id="heading-21">1. 配置打包入口与出口</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 编译模式</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>, <span class="hljs-comment">// production</span>
  <span class="hljs-attr">entry</span>: path.join(__dirname, <span class="hljs-string">'./src/index.js'</span>), <span class="hljs-comment">// 入口文件</span>
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'./dist'</span>), <span class="hljs-comment">// 输出文件的存放路径</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span> <span class="hljs-comment">// 输出文件的名称</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-22">2. 配置自动打包功能</h1>
<p>① 运行 <code>npm install webpack-dev-server -D</code> 安装支持项目自动打包的工具</p>
<p>② 修改package.json -> scripts中的dev命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server"</span> <span class="hljs-comment">// script节点下的脚本，可以通过 npm run 执行</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>③ 将src/index.html中script引用路径改为'/buldle.js' （根目录中的js，在内存中，是虚拟看不见的）</p>
<p>④ 运行 <code>nmp run dev</code> 重新进行打包</p>
<p>⑤ 访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080" ref="nofollow noopener noreferrer">http://localhost:8080</a> 地址，查看自动打包效果</p>
<p>⑥ 访问<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080%2Fsrc" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080/src" ref="nofollow noopener noreferrer">http://localhost:8080/src</a> 查看首页，通过访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080%2Fbuldle.js" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080/buldle.js" ref="nofollow noopener noreferrer">http://localhost:8080/buldle.js</a> 查看js代码</p>
<h1 data-id="heading-23">3. 配置生成预览页面</h1>
<p>目的：将src中的index.html复制到根目录中</p>
<p>① 运行 <code>npm install html-webpack-plugin -D</code> 安装生成预览页面的插件</p>
<p>② 修改webpack.config.js文件头部区域，添加如下配置信息</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 导入生成预览页面的插件，得到一个构造函数</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-keyword">const</span> htmlPlugin = <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123; <span class="hljs-comment">// 创建插件的实例对象</span>
  <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>, <span class="hljs-comment">// 指定用到的模板文件</span>
  <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.html'</span> <span class="hljs-comment">// 指定生成的文件的名称，该文件存在于内存中，在目录中不显示</span>
&#125;）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>③ 修改webpack.config.js文件向外暴露的配置对象，新增如下配置节点</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">moudle.exports = &#123;
  <span class="hljs-attr">plugins</span>: [ htmlPlugin ] <span class="hljs-comment">// plugins数组是 webpack打包期间会用到的一些插件列表</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-24">4. 配置自动打包相关参数</h1>
<p>目的：打包后自动打开浏览器</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// package.json中配置</span>
<span class="hljs-comment">// --open 打包完成自动打开浏览器页面</span>
<span class="hljs-comment">// --host 配置ip地址</span>
<span class="hljs-comment">// --port 配置端口</span>
<span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --open --host 127.0.0.1 --port 8888"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-25">5. 通过loader打包非js模块</h1>
<p>实际开发中，webpack只能默认打包处理以.js后缀名结尾的模块，其他文件处理默认不了，需要调用loader加载器才可以正常打包，否则会报错</p>
<p>loader加载器可以协助webpack打包处理特定的文件模块，比如</p>
<ul>
<li>less-loader 可以打包处理  .less相关的文件</li>
<li>sass-loader 可以打包处理 .scss相关的文件</li>
<li>url-loader 可以打包处理 css中与 url路径相关的文件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04dbe866637d412cbfcd8b362aecef51~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-26">1. 打包处理css文件</h2>
<p>① 运行 <code>npm i style-loader css-loader -D</code> 安装处理css文件的loader</p>
<p>② 在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 所有第三方文件模块的匹配规则 </span>
<span class="hljs-attr">module</span>: &#123; 
  <span class="hljs-attr">rules</span>: [ 
    &#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>, use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>] &#125; 
  ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，test 表示匹配的文件类型， use 表示对应要调用的 loader</p>
<p>注意：</p>
<ul>
<li>use 数组中指定的 loader 顺序是固定的</li>
<li>多个 loader 的调用顺序是：从后往前调用</li>
</ul>
<h2 data-id="heading-27">2. 打包处理less文件</h2>
<p>① 运行 <code>npm i less-loader less -D</code> 命令</p>
<p>② 在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 所有第三方文件模块的匹配规则 </span>
<span class="hljs-attr">module</span>: &#123; 
  <span class="hljs-attr">rules</span>: [ 
    &#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>, use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'less-loader'</span>] &#125; 
  ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">3. 打包处理 scss 文件</h2>
<p>① 运行 <code>npm i sass-loader node-sass -D</code> 命令</p>
<p>② 在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 所有第三方文件模块的匹配规则 </span>
<span class="hljs-attr">module</span>: &#123; 
  <span class="hljs-attr">rules</span>: [ 
    &#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.scss$/</span>, use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'sass-loader'</span>] &#125; 
  ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">4. 配置 postCSS 自动添加 css 的兼容前缀</h2>
<p>① 运行 <code>npm i postcss-loader autoprefixer -D</code> 命令</p>
<p>② 在项目根目录中创建 postcss 的配置文件 postcss.config.js，并初始化如下配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> autoprefixer = <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>) <span class="hljs-comment">// 导入自动添加前缀的插件 </span>
<span class="hljs-built_in">module</span>.exports = &#123; 
  <span class="hljs-attr">plugins</span>: [ autoprefixer ] <span class="hljs-comment">// 挂载插件 </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>③ 在 webpack.config.js 的 module -> rules 数组中，修改 css 的 loader 规则如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>: &#123; 
  <span class="hljs-attr">rules</span>: [ 
    &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>, use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>] &#125; 
  ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">5. 打包样式表中的图片和字体文件</h2>
<p>① 运行 <code>npm i url-loader file-loader -D</code> 命令</p>
<p>② 在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>: &#123; 
  <span class="hljs-attr">rules</span>: [ 
    &#123; 
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jpg|png|gif|bmp|ttf|eot|svg|woff|woff2$/</span>, 
      use: <span class="hljs-string">'url-loader?limit=16940'</span> 
    &#125; 
  ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>?</code> 之后的是 loader 的参数项。</p>
<p>limit 用来指定图片的大小，单位是字节(byte), 只有小于 limit 大小的图片，才会被转为 base64 图片</p>
<h2 data-id="heading-31">6. 打包处理 js 文件中的高级语法babel</h2>
<p>① 安装babel转换器相关的包：<code>npm i babel-loader @babel/core @babel/runtime -D</code></p>
<p>② 安装babel语法插件相关的包：<code>npm i @babel/preset-env @babel/plugin-transform-runtime @babel/plugin-proposal-class-properties –D</code></p>
<p>③ 在项目根目录中，创建 babel 配置文件 babel.config.js 并初始化基本配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123; 
  <span class="hljs-attr">presets</span>: [ <span class="hljs-string">'@babel/preset-env'</span> ], 
  <span class="hljs-attr">plugins</span>: [ <span class="hljs-string">'@babel/plugin-transform-runtime'</span>, <span class="hljs-string">'@babel/plugin-proposal-class-properties’ ] 
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>④  在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// exclude 为排除项，表示 babel-loader 不需要处理 node_modules 中的 js 文件 </span>
&#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>, use: <span class="hljs-string">'babel-loader'</span>, <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-32">6. Vue单文件组件</h1>
<h2 data-id="heading-33">1. 传统组件的问题和解决方案</h2>
<h3 data-id="heading-34">问题</h3>
<ol>
<li>全局定义的组件必须保证组件的名称不重复</li>
<li>字符串模板缺乏语法高亮，在 HTML 有多行的时候，需要用到丑陋的 <code>\</code></li>
<li>不支持 CSS 意味着当 HTML 和 JavaScript 组件化时，CSS 明显被遗漏</li>
<li>没有构建步骤限制，只能使用 HTML 和 ES5 JavaScript, 而不能使用预处理器（如：Babel）</li>
</ol>
<h3 data-id="heading-35">解决方案</h3>
<p>针对传统组件的问题，Vue 提供了一个解决方案 —— 使用 Vue 单文件组件。</p>
<h2 data-id="heading-36">2. Vue 单文件组件的基本用法</h2>
<p>单文件组件的组成结构</p>
<ul>
<li>template 组件的模板区域</li>
<li>script 业务逻辑区域</li>
<li>style 样式区域</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span> 
  <span class="hljs-comment"><!-- 这里用于定义Vue组件的模板内容 --></span> 
<span class="hljs-tag"></<span class="hljs-name">template</span>></span> 

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"> 
  <span class="hljs-comment">// 这里用于定义Vue组件的业务逻辑 </span>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; <span class="hljs-attr">data</span>: () &#123; <span class="hljs-keyword">return</span> &#123;&#125; &#125;, <span class="hljs-comment">// 私有数据 </span>
  <span class="hljs-attr">methods</span>: &#123;&#125; <span class="hljs-comment">// 处理函数 </span>
  <span class="hljs-comment">// ... 其它业务逻辑 </span>
&#125; 
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span> 

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  <span class="hljs-comment">/* 这里用于定义组件的样式 */</span> 
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">3. webpack 中配置 vue 组件的加载器</h2>
<p>①运行 <code>npm i vue-loader vue-template-compiler -D</code> 命令</p>
<p>②在 webpack.config.js 配置文件中，添加 vue-loader 的配置项如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> VueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// ... 其它规则</span>
      &#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>, loader: <span class="hljs-string">'vue-loader'</span> &#125;
    ]
&#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// ... 其它插件</span>
    <span class="hljs-keyword">new</span> VueLoaderPlugin() <span class="hljs-comment">// 请确保引入这个插件！</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">4. 在 webpack 项目中使用 vue</h2>
<p>①运行 <code>npm i vue –S</code> 安装 vue</p>
<p>②在 src -> index.js 入口文件中，通过 <code>import Vue from 'vue'</code> 来导入 vue 构造函数</p>
<p>③创建 vue 的实例对象，并指定要控制的 el 区域</p>
<p>④通过 render 函数渲染 App 根组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 导入 Vue 构造函数 </span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span> 
<span class="hljs-comment">// 2. 导入 App 根组件 </span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/App.vue'</span> 

<span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123; 
  <span class="hljs-comment">// 3. 指定 vm 实例要控制的页面区域 </span>
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>, 
  <span class="hljs-comment">// 4. 通过 render 函数，把指定的组件渲染到 el 区域中 </span>
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App) 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.html 页面中使用</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">5. webpack 打包发布</h2>
<p>上线之前需要通过webpack将应用进行整体打包，可以通过 package.json 文件配置打包命令：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在package.json文件中配置 webpack 打包命令</span>
<span class="hljs-comment">// 该命令默认加载项目根目录中的 webpack.config.js 配置文件</span>
<span class="hljs-string">"scripts"</span>: &#123;
<span class="hljs-comment">// 用于打包的命令</span>
<span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack -p"</span>,
<span class="hljs-comment">// 用于开发调试的命令</span>
<span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --open --host 127.0.0.1 --port 3000"</span>,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-powershell copyable" lang="powershell">npm run build
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            