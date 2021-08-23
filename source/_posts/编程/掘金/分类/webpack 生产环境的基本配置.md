
---
title: 'webpack 生产环境的基本配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26bf8edadf094b04a7b54a1a452bc1a5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 20:36:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26bf8edadf094b04a7b54a1a452bc1a5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.提取css 成单独文件</h3>
<ol>
<li>下载安装包</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26bf8edadf094b04a7b54a1a452bc1a5~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.下载插件<br>
npm install --save-dev mini-css-extract-plugin<br>
3. 修改配置文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
&#125;,
<span class="hljs-attr">module</span>: &#123;
<span class="hljs-attr">rules</span>: [
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
use: [
<span class="hljs-comment">// 创建style 标签，将样式放入</span>
<span class="hljs-comment">// 'style-loader',</span>
<span class="hljs-comment">// 这个loader 取代style-loader。作用：提取js 中的css 成单独文件</span>
MiniCssExtractPlugin.loader,
<span class="hljs-comment">// 将css 文件整合到js 文件中</span>
<span class="hljs-string">'css-loader'</span>
]
&#125;
]
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
&#125;),
<span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
<span class="hljs-comment">// 对输出的css 文件进行重命名</span>
<span class="hljs-attr">filename</span>: <span class="hljs-string">'css/built.css'</span>
&#125;)
],
<span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>4 .运行指令: webpack</p>
<h3 data-id="heading-1">2. css 兼容性处理</h3>
<p>1.创建文件</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e2072d29a1848a8a604a353ca45aad1~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer">
2.下载loader<br>
npm install --save-dev postcss-loader postcss-preset-env
3.修改配置文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-comment">// 设置nodejs 环境变量</span>
<span class="hljs-comment">// process.env.NODE_ENV = 'development';</span>
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
&#125;,
<span class="hljs-attr">module</span>: &#123;
<span class="hljs-attr">rules</span>: [
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
use: [
MiniCssExtractPlugin.loader,
<span class="hljs-string">'css-loader'</span>,
&#123;
<span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-attr">ident</span>: <span class="hljs-string">'postcss'</span>,
<span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> [
<span class="hljs-comment">// postcss 的插件</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-preset-env'</span>)()
]
&#125;
&#125;
]
]
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
&#125;),
<span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'css/built.css'</span>
&#125;)
],
<span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>修改package.json</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"browserslist"</span>: &#123;
<span class="hljs-string">"development"</span>: [
<span class="hljs-string">"last 1 chrome version"</span>,
<span class="hljs-string">"last 1 firefox version"</span>,
<span class="hljs-string">"last 1 safari version"</span>
],
<span class="hljs-string">"production"</span>: [
<span class="hljs-string">">0.2%"</span>,
<span class="hljs-string">"not dead"</span>,
<span class="hljs-string">"not op_mini all"</span>
]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>运行指令: webpack</li>
</ol>
<h3 data-id="heading-2">3.压缩css</h3>
<p>1.创建文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d94f7f3adce499eaebf88df8834da1d~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>下载安装包</li>
</ol>
<p>npm install --save-dev optimize-css-assets-webpack-plugin</p>
<ol start="3">
<li>修改配置文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>
)
<span class="hljs-comment">// 设置nodejs 环境变量</span>
<span class="hljs-comment">// process.env.NODE_ENV = 'development';</span>
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
&#125;,
<span class="hljs-attr">module</span>: &#123;
<span class="hljs-attr">rules</span>: [
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
use: [
MiniCssExtractPlugin.loader,
<span class="hljs-string">'css-loader'</span>,
&#123;
<span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-attr">ident</span>: <span class="hljs-string">'postcss'</span>,
<span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> [
<span class="hljs-comment">// postcss 的插件</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-preset-env'</span>)()
]
&#125;
&#125;
]
&#125;
]
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
&#125;),
<span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'css/built.css'</span>
&#125;),
<span class="hljs-comment">// 压缩css</span>
<span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin()
],
<span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行指令: webpack</p>
<h3 data-id="heading-3">4. js 语法检查</h3>
<p>1.创建文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b48f120b0a374299a95d06b5fadf55e4~tplv-k3u1fbpfcp-watermark.image" alt="js.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>下载安装包</li>
</ol>
<p>npm install --save-dev eslint-loader eslint eslint-config-airbnb-base eslint-plugin-import</p>
<ol start="3">
<li>修改配置文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>
)
<span class="hljs-comment">// 设置nodejs 环境变量</span>
<span class="hljs-comment">// process.env.NODE_ENV = 'development';</span>
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
&#125;,
<span class="hljs-attr">module</span>: &#123;
<span class="hljs-attr">rules</span>: [
<span class="hljs-comment">/*
语法检查： eslint-loader eslint
注意：只检查自己写的源代码，第三方的库是不用检查的
设置检查规则：
package.json 中eslintConfig 中设置~
"eslintConfig": &#123;
"extends": "airbnb-base"
&#125;
airbnb --> eslint-config-airbnb-base eslint-plugin-import eslint
*/</span>
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
exclude: <span class="hljs-regexp">/node_modules/</span>,
loader: <span class="hljs-string">'eslint-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-comment">// 自动修复eslint 的错误</span>
<span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>
&#125;
&#125;
]
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
&#125;),
<span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'css/built.css'</span>
&#125;),
<span class="hljs-comment">// 压缩css</span>
<span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin()
],
<span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>配置package.json</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"eslintConfig"</span>: &#123;
<span class="hljs-string">"extends"</span>: <span class="hljs-string">"airbnb-base"</span>,
<span class="hljs-string">"env"</span>: &#123;
<span class="hljs-string">"browser"</span>: <span class="hljs-literal">true</span>
&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>运行指令: webpack</li>
</ol>
<h3 data-id="heading-4">5. js 兼容性处理</h3>
<p>1.创建文件</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a7f18f921a549529e4ffe659ea890dd~tplv-k3u1fbpfcp-watermark.image" alt="js1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>下载安装包</li>
</ol>
<p>npm install --save-dev babel-loader @babel/core @babel/preset-env @babel/polyfill core-js</p>
<ol start="3">
<li>修改配置文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
&#125;,
<span class="hljs-attr">module</span>: &#123;
<span class="hljs-attr">rules</span>: [
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
exclude: <span class="hljs-regexp">/node_modules/</span>,
loader: <span class="hljs-string">'babel-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-comment">// 预设：指示babel 做怎么样的兼容性处理</span>
<span class="hljs-attr">presets</span>: [
[
<span class="hljs-string">'@babel/preset-env'</span>,
&#123;
<span class="hljs-comment">// 按需加载</span>
<span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
<span class="hljs-comment">// 指定core-js 版本</span>
<span class="hljs-attr">corejs</span>: &#123;
<span class="hljs-attr">version</span>: <span class="hljs-number">3</span>
&#125;,
<span class="hljs-comment">// 指定兼容性做到哪个版本浏览器</span>
<span class="hljs-attr">targets</span>: &#123;
<span class="hljs-attr">chrome</span>: <span class="hljs-string">'60'</span>,
<span class="hljs-attr">firefox</span>: <span class="hljs-string">'60'</span>,
<span class="hljs-attr">ie</span>: <span class="hljs-string">'9'</span>,
<span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>,
<span class="hljs-attr">edge</span>: <span class="hljs-string">'17'</span>
&#125;
&#125;
]
]
&#125;
&#125;
]
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
&#125;)
],
<span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>运行指令: webpack</li>
</ol>
<h3 data-id="heading-5">6. js 压缩</h3>
<p>1.创建文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9f115b6746d474692393bb194ca7d68~tplv-k3u1fbpfcp-watermark.image" alt="js2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>修改配置文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>
&#125;)
],
<span class="hljs-comment">// 生产环境下会自动压缩js 代码</span>
<span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>
&#125;;


<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>运行指令: webpack</li>
</ol>
<h3 data-id="heading-6">7.压缩HTML</h3>
<p>1.创建文件</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecd3145300ad4ce3a840910432529cbc~tplv-k3u1fbpfcp-watermark.image" alt="html.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.修改配置文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
<span class="hljs-comment">// 压缩html 代码</span>
<span class="hljs-attr">minify</span>: &#123;
<span class="hljs-comment">// 移除空格</span>
<span class="hljs-attr">collapseWhitespace</span>: <span class="hljs-literal">true</span>,
<span class="hljs-comment">// 移除注释</span>
<span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>
&#125;
&#125;)
],
<span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">webpack 生产环境的基本配置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> MiniCssExtractorPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>)
<span class="hljs-keyword">const</span> OptimiziCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimizi-css-assets-webpack-plugin'</span>)
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)


<span class="hljs-comment">// 定义node.js的环境变量，决定使用browserslist的哪个环境</span>
process.env.NODE_ENV = <span class="hljs-string">'production'</span>


<span class="hljs-comment">// 复用loader的写法</span>
<span class="hljs-keyword">const</span> commonCssLoader = [
<span class="hljs-comment">// 这个loader取代style-loader。作用：提取js中的css成单独文件然后通过link加载</span>
MiniCssExtractPlugin.loader,
<span class="hljs-comment">// css-loader：将css文件整合到js文件中</span>
<span class="hljs-comment">// 经过css-loader处理后，样式文件是在js文件中的</span>
<span class="hljs-comment">// 问题：1.js文件体积会很大2.需要先加载js再动态创建style标签，样式渲染速度就慢，会出现闪屏现象</span>
<span class="hljs-comment">// 解决：用MiniCssExtractPlugin.loader替代style-loader</span>
<span class="hljs-string">'css-loader'</span>,
<span class="hljs-comment">/*
    postcss-loader：css兼容性处理：postcss --> 需要安装：postcss-loader postcss-preset-env
    postcss需要通过package.json中browserslist里面的配置加载指定的css兼容性样式
    在package.json中定义browserslist：
    "browserslist": &#123;
      // 开发环境 --> 设置node环境变量：process.env.NODE_ENV = development
      "development": [ // 只需要可以运行即可
        "last 1 chrome version",
        "last 1 firefox version",
        "last 1 safari version"
      ],
      // 生产环境。默认是生产环境
      "production": [ // 需要满足绝大多数浏览器的兼容
        ">0.2%",
        "not dead",
        "not op_mini all"
      ]
    &#125;,
  */</span>
&#123;
<span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-attr">ident</span>: <span class="hljs-string">'postcss'</span>, <span class="hljs-comment">// 基本写法</span>
<span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> [
<span class="hljs-comment">// postcss的插件</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-preset-env'</span>)(),
],
&#125;,
&#125;,
]


<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/js/index.js'</span>,
<span class="hljs-attr">output</span>: &#123;
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
<span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
&#125;,
<span class="hljs-attr">module</span>: &#123;
<span class="hljs-attr">rules</span>: [
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
use: [...commonCssLoader],
&#125;,
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
use: [...commonCssLoader, <span class="hljs-string">'less-loader'</span>],
&#125;,
<span class="hljs-comment">/*
        正常来讲，一个文件只能被一个loader处理
        当一个文件要被多个loader处理，那么一定要指定loader执行的先后顺序
        先执行eslint再执行babel（用enforce）
      */</span>
&#123;
<span class="hljs-comment">/*
          js的语法检查： 需要下载 eslint-loader eslint
          注意：只检查自己写的源代码，第三方的库是不用检查的
          airbnb(一个流行的js风格) --> 需要下载 eslint-config-airbnb-base eslint-plugin-import
          设置检查规则：
            package.json中eslintConfig中设置
              "eslintConfig": &#123;
                "extends": "airbnb-base"， // 继承airbnb的风格规范
                "env": &#123;
                  "browser": true // 可以使用浏览器中的全局变量(使用window不会报错)
                &#125;
              &#125;
        */</span>
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
exclude: <span class="hljs-regexp">/node_modules/</span>, <span class="hljs-comment">// 忽略node_modules</span>
enforce: <span class="hljs-string">'pre'</span>, <span class="hljs-comment">// 优先执行</span>
<span class="hljs-attr">loader</span>: <span class="hljs-string">'eslint-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-comment">// 自动修复</span>
<span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>,
&#125;,
      &#125;,
      <span class="hljs-comment">/*
        js兼容性处理：需要下载 babel-loader @babel/core
          1. 基本js兼容性处理 --> @babel/preset-env
            问题：只能转换基本语法，如promise高级语法不能转换
          2. 全部js兼容性处理 --> @babel/polyfill
            问题：只要解决部分兼容性问题，但是将所有兼容性代码全部引入，体积太大了
          3. 需要做兼容性处理的就做：按需加载  --> core-js
      */</span>
&#123;
<span class="hljs-comment">// 第三种方式：按需加载</span>
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
exclude: <span class="hljs-regexp">/node_modules/</span>,
loader: <span class="hljs-string">'babel-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
          <span class="hljs-comment">// 预设：指示babel做怎样的兼容性处理</span>
<span class="hljs-attr">presets</span>: [
<span class="hljs-string">'@babel/preset-env'</span>, <span class="hljs-comment">// 基本预设</span>
&#123;
<span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>, <span class="hljs-comment">//按需加载</span>
<span class="hljs-attr">corejs</span>: &#123; <span class="hljs-attr">version</span>: <span class="hljs-number">3</span> &#125;, <span class="hljs-comment">// 指定core-js版本</span>
<span class="hljs-attr">targets</span>: &#123; <span class="hljs-comment">// 指定兼容到什么版本的浏览器</span>
<span class="hljs-attr">chrome</span>: <span class="hljs-string">'60'</span>,
                <span class="hljs-attr">firefox</span>: <span class="hljs-string">'50'</span>,
                <span class="hljs-attr">ie</span>: <span class="hljs-string">'9'</span>,
                <span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>,
                <span class="hljs-attr">edge</span>: <span class="hljs-string">'17'</span>
&#125;,
&#125;,
],
&#125;,
&#125;,
&#123;
<span class="hljs-comment">// 图片处理</span>
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpg|png|gif)/</span>,
loader: <span class="hljs-string">'url-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-attr">limit</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span>,
<span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
<span class="hljs-attr">outputPath</span>: <span class="hljs-string">'imgs'</span>,
<span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 关闭url-loader默认使用的es6模块化解析</span>
&#125;,
&#125;,
<span class="hljs-comment">// html中的图片处理</span>
&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.html$/</span>,
loader: <span class="hljs-string">'html-loader'</span>,
&#125;,
<span class="hljs-comment">// 处理其他文件</span>
&#123;
<span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/\.(js|css|less|html|jpg|png|gif)/</span>,
loader: <span class="hljs-string">'file-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-attr">outputPath</span>: <span class="hljs-string">'media'</span>,
&#125;,
&#125;,
],
&#125;,
<span class="hljs-attr">plugins</span>: [
<span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
<span class="hljs-comment">// 对输出的css文件进行重命名</span>
<span class="hljs-attr">filename</span>: <span class="hljs-string">'css/built.css'</span>,
&#125;),
<span class="hljs-comment">// 压缩css</span>
<span class="hljs-keyword">new</span> OptimiziCssAssetsWebpackPlugin(),
<span class="hljs-comment">// HtmlWebpackPlugin：html文件的打包和压缩处理</span>
<span class="hljs-comment">// 通过这个插件会自动将单独打包的样式文件通过link标签引入</span>
<span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
<span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
      <span class="hljs-comment">// 压缩html代码</span>
<span class="hljs-attr">minify</span>: &#123;
        <span class="hljs-comment">// 移除空格</span>
        <span class="hljs-attr">collapseWhitespace</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 移除注释</span>
<span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>,
&#125;,
&#125;),
  ],
  <span class="hljs-comment">// 生产环境下会自动压缩js代码</span>
<span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            