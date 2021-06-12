
---
title: 'Webpack4从入门到入土'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8694'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 01:46:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=8694'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Webpack</h1>
<h2 data-id="heading-1">一、Webpack简介</h2>
<h3 data-id="heading-2">1.1 Webpack是什么</h3>
<p>Webpack是一种前端资源构建工具，一个静态模块打包器。在Webpack看来，前端的所有资源文件都会作为模块处理，它将根据模块的依赖关系进行静态分析，打包生成对应的静态资源(bundle)。</p>
<h3 data-id="heading-3">1.2 Webpack五个核心概念</h3>
<h4 data-id="heading-4">1.2.1 Entry</h4>
<p>​入口(Entry)指示Webpack以哪个文件为入口起点开始打包，分析构建内部依赖图。</p>
<h4 data-id="heading-5">1.2.2 Output</h4>
<p>​输出(Output)指示Webpack打包后的资源bundles输出到哪里去，以及如何命名。</p>
<h4 data-id="heading-6">1.2.3 Loader</h4>
<p>​Loader让Webpack能够去处理那些非JavaScript文件(webpack自身只理解JavaScript)</p>
<h4 data-id="heading-7">1.2.4 Plugins</h4>
<p>​插件(Plugins)可以用于执行范围更广的任务。插件的范围包括，从打包优化和压缩，一直到重新定义环境中的变量等。</p>
<h4 data-id="heading-8">1.2.5 Mode</h4>
<p>​模式(Mode)指示Webpack使用对应模式的配置。</p>




















<table><thead><tr><th>选项</th><th>描述</th><th>特点</th></tr></thead><tbody><tr><td>development</td><td>会将<code>process.env.NODE_ENV</code>的值设为<code>development</code>。启用<code>NamedChunksPlugin</code>和<code>NamedModulesPlugin</code>。</td><td>能让代码本地调试运行的环境</td></tr><tr><td>production</td><td>会将<code>process.env.NODE_ENV</code>的值设为<code>production</code>。启用<code>FlagDependencyUsagePlugin</code>, <code>FlagIncludedChunksPlugin</code>, <code>ModuleConcatenationPlugin</code>, <code>NoEmitOnErrorsPlugin</code>, <code>OccurrenceOrderPlugin</code>, <code>SideEffectsFlagPlugin</code>和<code>UglifyJsPlugin</code>。</td><td>能让代码优化上线运行的环境</td></tr></tbody></table>
<h2 data-id="heading-9">二、Webpack初体验</h2>
<h3 data-id="heading-10">2.1 运行指令</h3>
<p>​开发环境：<code>webpack ./src/index.js -o ./build/build.js --mode=development</code></p>
<p>​生产环境：<code>webpack ./src/index.js -o ./build/build.js --mode=production</code></p>
<p>​webpack会以<code>./src/index.js</code>为入口文件开始打包，打包后输出到<code>./build/build.js</code>，整体打包环境是开发/生产环境</p>
<p><strong>结论：</strong></p>
<ol>
<li>webpack能处理js/json资源，不能处理css/img等其他资源</li>
<li>生成环境和开发环境将ES6模块编译成浏览器能识别的模块化</li>
<li>生成环境比开发环境多一个压缩js代码</li>
</ol>
<h3 data-id="heading-11">2.2 webpack配置</h3>
<p>​<code>webpack.config.js</code>：webpack的配置文件。指示webpack干哪些活(当你运行webpack指令时，会加载里面的配置)；<br>
​所有构件工具都是基于nodejs平台运行的，模块化默认使用commonjs</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    loader：1. 下载2. 使用（配置loader）
    plugins：1.下载2. 引入3. 使用
*/</span>
<span class="hljs-comment">// resolve用来拼接绝对路径的方法</span>
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>);

<span class="hljs-comment">// 设置nodejs环境变量</span>
process.env.NODE_ENV = <span class="hljs-string">'development'</span>;

<span class="hljs-comment">// 复用loader</span>
<span class="hljs-keyword">const</span> commonCssLoader = [
    <span class="hljs-comment">// use数组中loader执行顺序：从右到左，从下到上，依次执行。</span>
    <span class="hljs-comment">// 创建style标签，将js中的样式资源插入进行，添加到head中生效</span>
    <span class="hljs-comment">// 'style-loader',</span>
    <span class="hljs-comment">// 这个loader取代style-loader。作用：提取js中的css成单独文件</span>
    MiniCssExtractPlugin.loader,
    <span class="hljs-comment">// 将css文件变成commonjs模块加载js中，里面内容时样式字符串</span>
    <span class="hljs-string">'css-loader'</span>,
    <span class="hljs-comment">/*
      css兼容性处理：postcss --> postcss-loaderpost-preset-env
      帮postcss找到packet.json中browerslist里面的配置，通过配置加载指定的css兼容性样式
          "browserslist": &#123;
              // 开发环境 --> 设置node环境变量： process.env.NODE_ENV = 'development'
          "development": [
            "last 1 chrome version",
            "last 1 firefox version",
            "last 1 safari version",
           ],
           // 生产环境：默认是生产环境
           "production": [
                  ">0.2%",
                  "not dead",
                  "not op_mini all"
            ]
          &#125;
        */</span>
    <span class="hljs-comment">// 使用loader的默认配置</span>
    <span class="hljs-comment">// 'post-loader',</span>
    <span class="hljs-comment">// 修改loader配置</span>
    &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">ident</span>: <span class="hljs-string">'postcss'</span>,
            <span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> [
                <span class="hljs-comment">// postcss的插件</span>
                <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-preset-env'</span>)()
            ]
        &#125;
    &#125;
];

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// webpack配置</span>
    <span class="hljs-comment">// 入口起点</span>
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,

    <span class="hljs-comment">// 输出</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// 输出文件名</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/build.js'</span>,
        <span class="hljs-comment">// 输出路径</span>
        <span class="hljs-comment">// __dirname nodejs的变量，代表当前文件的目录的绝对路径</span>
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,

    <span class="hljs-comment">// loader的配置</span>
    <span class="hljs-attr">modules</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            <span class="hljs-comment">// 详细loader配置</span>
            <span class="hljs-comment">// 不同文件必须配置不同loader处理</span>
            &#123;
                <span class="hljs-comment">// 匹配哪些文件</span>
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                <span class="hljs-comment">// 使用哪些loader进行处理</span>
                use: [...commonCssLoader]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                use: [
                    ...commonCssLoader,
                    <span class="hljs-comment">// 将less文件编译成css文件</span>
                    <span class="hljs-comment">// 需要下载less-loader和less</span>
                    <span class="hljs-string">'less-loader'</span>
                ]
            &#125;,
            &#123;
                <span class="hljs-comment">// 处理样式中的图片资源 —— 默认处理不了html中的图片资源</span>
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpg|png|gif)$/</span>,
                <span class="hljs-comment">// 下载url-loader、file-loader</span>
                loader: <span class="hljs-string">'url-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-comment">// 图片大小小于8kb，就会被base64处理</span>
                    <span class="hljs-comment">// 优点：减少请求数量（减轻服务器压力）</span>
                    <span class="hljs-comment">// 缺点：图片提及会更大（文件请求速度更慢）</span>
                    <span class="hljs-attr">limit</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span>,
                    <span class="hljs-comment">// 问题：因为url-loader默认使用es6模块化解析，而html-loader引入图片是commonjs</span>
                    <span class="hljs-comment">// 解析时会出问题：【object Module】</span>
                    <span class="hljs-comment">// 解决： 关闭url-loader的es6模块化，使用commonjs解析</span>
                    <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>,
                    <span class="hljs-comment">// 给图片进行重命名</span>
                    <span class="hljs-comment">// [hash: 10]取图片的hash值前10位</span>
                    <span class="hljs-comment">// [ext]取文件原来扩展名</span>
                    <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
                    <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'imgs'</span>
                &#125;
            &#125;,
            <span class="hljs-comment">// 打包其他资源（除了html/js/css资源以外的资源）</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.html$/</span>,
                <span class="hljs-comment">// 处理html文件中的img图片（负责引入img，从而能被url-loader进行处理）</span>
                loader: <span class="hljs-string">'html-loader'</span>
            &#125;,
            &#123;
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/\.(html|css|js|less|jpg|png|gif)$/</span>,
                loader: <span class="hljs-string">'file-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
                    <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'media'</span>
                &#125;
            &#125;,
            <span class="hljs-comment">// 正常来讲，一个文件只能被一个loader处理，当被多个loader处理，一定要指定loader执行的先后顺序：先执行eslint再执行babel</span>
            &#123;
                <span class="hljs-comment">/*
                    语法检查： eslint-loader eslint
                        注意：只检查自己写的源代码，第三方的库是不用检查的
                        设置检查规则：
                            package.json中eslintConfig中设置：
                            “eslintConfig”: &#123;
                                "extend": "airbnb-base"
                            &#125;
                    airbnb --> eslint-config-airbnb-baseeslint-plugin-importeslint
                */</span>
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                exclude: <span class="hljs-regexp">/node_modules/</span>,
                <span class="hljs-comment">// 优先执行</span>
                enforce: <span class="hljs-string">'pre'</span>,
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'eslint-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-comment">// 自动修复eslint的错误</span>
                    <span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>
                &#125;
            &#125;,
            <span class="hljs-comment">/*
                  js兼容性处理：babel-loader @babel/core @babel/preset-env
                      1. 基本js兼容性处理==》 @babel/preset-env
                          问题：只能转换基本语法，如promise不能转换
                2. 全部js兼容性处理==》 @babel/polyfill
                      问题：我只要解决部分兼容性问题，但是所有兼容性代码全部引入，提及太大
                    3. 需要做兼容性处理的就做：按需加载==》 core-js 
            */</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                exclude: <span class="hljs-regexp">/node_modules/</span>,
                loader: <span class="hljs-string">'babel-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-comment">// 预设：指示babel做怎么样的兼容性处理</span>
                    <span class="hljs-attr">presets</span>: [
                        [
                            <span class="hljs-string">'@babel/preset-env'</span>,
                            &#123;
                                <span class="hljs-comment">// 按需加载</span>
                                <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
                                <span class="hljs-comment">// 指定core-js版本</span>
                                <span class="hljs-attr">corejs</span>: &#123; <span class="hljs-attr">version</span>: <span class="hljs-number">3</span> &#125;,
                                <span class="hljs-comment">// 指定兼容性做到哪个版本的浏览器</span>
                                <span class="hljs-attr">targets</span>: &#123;
                                    <span class="hljs-attr">chrome</span>: <span class="hljs-string">'60'</span>,
                                    <span class="hljs-attr">firefox</span>: <span class="hljs-string">'60'</span>,
                                    <span class="hljs-attr">ie</span>: <span class="hljs-string">'9'</span>,
                                    <span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>,
                                    <span class="hljs-attr">edge</span>: <span class="hljs-string">'17'</span>
                                &#125;
                            &#125;
                        ]]
                &#125;
            &#125;
        ]
    &#125;,

    <span class="hljs-comment">// plugins配置</span>
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// 详细plugins配置</span>
        <span class="hljs-comment">// html-webpack-plugin —— 默认会创建一个空的HTML，自动引入打包输出的所有资源（JS/CSS）</span>
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-comment">// 复制'./src/index.html'文件，并自动引入打包输出的所有资源（JS/CSS）</span>
            <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
            <span class="hljs-comment">// 压缩html</span>
            <span class="hljs-attr">minify</span>: &#123;
                <span class="hljs-comment">// 移除空格</span>
                <span class="hljs-attr">collapseWhitspace</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-comment">// 移除注释</span>
                <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>
            &#125;
        &#125;),
        <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
            <span class="hljs-comment">// 对输出的css文件重命名</span>
            <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/build.css'</span>
        &#125;),
        <span class="hljs-comment">// 压缩css</span>
        <span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin()
    ],

    <span class="hljs-comment">// 模式</span>
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-comment">// mode: 'production',</span>

    <span class="hljs-comment">// 开发服务器devServer：用来自动化（自动编译、自动打开浏览器、自动刷新浏览器）</span>
    <span class="hljs-comment">// 特点：只会在内存中编译打包，不会有任何输出</span>
    <span class="hljs-comment">// 启动devServer指令为：`npx webpack-dev-server`</span>
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-comment">// 项目构建后路径</span>
        <span class="hljs-attr">contentBase</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
        <span class="hljs-comment">// 启动gzip压缩</span>
        <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 端口号</span>
        <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
        <span class="hljs-comment">// 自动打开浏览器</span>
        <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">三、Webpack性能优化</h2>
<h3 data-id="heading-13">3.1 开发环境性能优化</h3>
<h4 data-id="heading-14">3.1.1 优化打包构建速度</h4>
<p>​HMR：hot module replacement热模块替换/模块热替换</p>
<p>​作用：一个模块发生变化，只会重新打包这一个模块（而不是打包所有模块），极大提升构建速度。</p>
<p>​样式文件：可以使用HMR功能：因为style-loader内部实现了</p>
<p>​js文件：默认不能使用HMR功能。 --> 需要修改js代码，添加支持HMR功能的代码</p>
<p>​注意：HMR功能对js的处理，只能处理非入口文件的其他文件。</p>
<p>​<code>if(module.hot)&#123;module.hot.accept('文件路径', function()&#123;...&#125;)&#125;</code></p>
<p>​html文件：默认不能使用HMR功能，同时会导致html文件不能热更新。(不用做HMR功能)</p>
<p>​解决：修改entry入口，将html文件引入</p>
<pre><code class="hljs language-js copyable" lang="js">entry: [<span class="hljs-string">'./src/index.html'</span>]
<span class="hljs-attr">devServer</span>: &#123;
<span class="hljs-comment">// 开启HMR功能</span>
<span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">3.1.2 优化代码调试</h4>
<p>​source-map：一种提供源代码到构建后代码映射的技术（如果构建后代码出错了，通过映射可以追踪源代码错误）</p>
<p><code>[inline-|hidden-|eval-][nosources-][cheap-[module-]]source-map</code></p>
<p><code>source-map</code>：外部</p>
<p>​---->错误代码准确信息 和 源代码的错误位置</p>
<p><code>inline-source-map</code>：内联；只生产一个内联source-map</p>
<p>​---->错误代码准确信息 和 源代码的错误位置</p>
<p><code>hidden-source-map</code>：外部;</p>
<p>​---->错误代码错误原因，但是没有错误位置；不能跟踪源代码错误，只能提示到构建后代码的错误位置</p>
<p><code>eval-source-map</code>：内联；每一个文件都生产对应的source-map，都在eval里</p>
<p>​---->错误代码准确信息 和 源代码的错误位置</p>
<p><code>nosources-source-map</code>： 外部</p>
<p>​---->错误代码准确信息但是没有任何源代码</p>
<p><code>cheap-source-map</code>：外部</p>
<p>​---->错误代码准确信息 和 源代码的错误位置；只能精确到行</p>
<p><code>cheap-module-source-map</code>：外部</p>
<p>​---->错误代码准确信息 和 源代码的错误位置；只能精确到行</p>
<p>​---->module会将loader的source map加入</p>
<p><strong>内联和外部的区别</strong>：1. 外部生成了文件，内联没有；2. 内联构建速度更快</p>
<p><strong>开发环境</strong>：速度快，调试更友好</p>
<p>​速度快：eval>inline>cheap>...</p>
<p>​eval-cheap-source-map</p>
<p>​eval-source-map</p>
<p>​调试更友好</p>
<p>​source-map</p>
<p>​cheap-module-source-map</p>
<p>​cheap-source-map</p>
<p>​--> <strong>eval-source-map/eval-cheap-module-source-map</strong></p>
<p><strong>生产环境</strong>：源代码要不要隐藏？调试要不要更友好？</p>
<p>​内联会让代码体积变大，所以在生产环境不用内联</p>
<p>​nosources-source-map全部隐藏</p>
<p>​hidden-source-map只隐藏源代码，会提示构建后代码错误信息</p>
<p>--> <strong>source-map/cheap-module-source-map</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  ...,
<span class="hljs-attr">devtool</span>: <span class="hljs-string">'source-map'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">3.2 生产环境性能优化</h3>
<h4 data-id="heading-17">3.2.1 优化打包构建速度</h4>
<h5 data-id="heading-18">3.2.1.1 <strong>oneof</strong></h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-keyword">const</span> commonCssLoader = [
    MiniCssExtractPlugin.loader,
    <span class="hljs-string">'css-loader'</span>,

    &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">ident</span>: <span class="hljs-string">'postcss'</span>,
            <span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> [
                <span class="hljs-comment">// postcss的插件</span>
                <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-preset-env'</span>)()
            ]
        &#125;
    &#125;
];

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,

    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/build.js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,

    <span class="hljs-attr">modules</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                exclude: <span class="hljs-regexp">/node_modules/</span>,
                enforce: <span class="hljs-string">'pre'</span>,
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'eslint-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>
                &#125;
            &#125;,
            &#123;
                <span class="hljs-comment">// 一个文件只会匹配一个loader，匹配到了不会向下继续匹配</span>
                <span class="hljs-attr">oneof</span>: [
                    &#123;
                        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                        use: [...commonCssLoader]
                    &#125;,
                    &#123;
                        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                        use: [
                            ...commonCssLoader,
                            <span class="hljs-string">'less-loader'</span>
                        ]
                    &#125;,
                    &#123;
                        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpg|png|gif)$/</span>,
                        loader: <span class="hljs-string">'url-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">limit</span>: <span class="hljs-number">8</span> * <span class="hljs-number">1024</span>,
                            <span class="hljs-attr">esModule</span>: <span class="hljs-literal">false</span>,
                            <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
                            <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'imgs'</span>
                        &#125;
                    &#125;,
                    &#123;
                        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.html$/</span>,
                        loader: <span class="hljs-string">'html-loader'</span>
                    &#125;,
                    &#123;
                        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/\.(html|css|js|less|jpg|png|gif)$/</span>,
                        loader: <span class="hljs-string">'file-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">name</span>: <span class="hljs-string">'[hash:10].[ext]'</span>,
                            <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'media'</span>
                        &#125;
                    &#125;,

                    &#123;
                        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                        exclude: <span class="hljs-regexp">/node_modules/</span>,
                        loader: <span class="hljs-string">'babel-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">presets</span>: [
                                [
                                    <span class="hljs-string">'@babel/preset-env'</span>,
                                    &#123;
                                        <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
                                        <span class="hljs-attr">corejs</span>: &#123; <span class="hljs-attr">version</span>: <span class="hljs-number">3</span> &#125;,
                                        <span class="hljs-attr">targets</span>: &#123;
                                            <span class="hljs-attr">chrome</span>: <span class="hljs-string">'60'</span>,
                                            <span class="hljs-attr">firefox</span>: <span class="hljs-string">'60'</span>,
                                            <span class="hljs-attr">ie</span>: <span class="hljs-string">'9'</span>,
                                            <span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>,
                                            <span class="hljs-attr">edge</span>: <span class="hljs-string">'17'</span>
                                        &#125;
                                    &#125;
                                ]]
                        &#125;
                    &#125;
                ]
            &#125;
        ]
    &#125;,
    <span class="hljs-comment">// mode: 'development',</span>
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">3.2.1.2 <strong>babel缓存</strong></h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    babel缓存 --> 第二次打包构建速度更快
        cacheDirectory: true
*/</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,

    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/build.js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,

    <span class="hljs-attr">modules</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                exclude: <span class="hljs-regexp">/node_modules/</span>,
                loader: <span class="hljs-string">'babel-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">presets</span>: [[
                        <span class="hljs-string">'@babel/preset-env'</span>,
                        &#123;
                            <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
                            <span class="hljs-attr">corejs</span>: &#123; <span class="hljs-attr">version</span>: <span class="hljs-number">3</span> &#125;,
                            <span class="hljs-attr">targets</span>: &#123;
                                <span class="hljs-attr">chrome</span>: <span class="hljs-string">'60'</span>,
                                <span class="hljs-attr">firefox</span>: <span class="hljs-string">'60'</span>,
                                <span class="hljs-attr">ie</span>: <span class="hljs-string">'9'</span>,
                                <span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>,
                                <span class="hljs-attr">edge</span>: <span class="hljs-string">'17'</span>
                            &#125;
                        &#125;
                    ]],
                    <span class="hljs-comment">// 开启babel缓存</span>
                    <span class="hljs-comment">// 第二次构建时，会读取之前的缓存</span>
                    <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-literal">true</span>
                &#125;
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">3.2.1.3 多进程</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,

    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/build.[contenthash:10].js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,

    <span class="hljs-attr">modules</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                exclude: <span class="hljs-regexp">/node_modules/</span>,
                use: [
                    <span class="hljs-comment">/*
                        开启多进程打包
                        进程启动大概为600ms，进程通信也有开销
                        只有工作消耗时间比较长，才需要多进程打包
                    */</span>
                    &#123;
                        <span class="hljs-attr">loader</span>: <span class="hljs-string">'thread-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">workers</span>: <span class="hljs-number">2</span><span class="hljs-comment">// 开启2个进程</span>
                        &#125;
                    &#125;,
                    &#123;
                        <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">presets</span>: [[
                                <span class="hljs-string">'@babel/preset-env'</span>,
                                &#123;
                                    <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
                                    <span class="hljs-attr">corejs</span>: &#123; <span class="hljs-attr">version</span>: <span class="hljs-number">3</span> &#125;,
                                    <span class="hljs-attr">targets</span>: &#123;
                                        <span class="hljs-attr">chrome</span>: <span class="hljs-string">'60'</span>,
                                        <span class="hljs-attr">firefox</span>: <span class="hljs-string">'60'</span>,
                                        <span class="hljs-attr">ie</span>: <span class="hljs-string">'9'</span>,
                                        <span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>,
                                        <span class="hljs-attr">edge</span>: <span class="hljs-string">'17'</span>
                                    &#125;
                                &#125;
                            ]],
                            <span class="hljs-comment">// 开启babel缓存</span>
                            <span class="hljs-comment">// 第二次构建时，会读取之前的缓存</span>
                            <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-literal">true</span>
                        &#125;
                    &#125;
                ]
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">3.2.1.4 externals</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// [name] 取文件名</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[contenthash:10].js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    ...
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">externals</span>: &#123;
        <span class="hljs-comment">// 拒绝jQuery被打包 -- npm包名</span>
        <span class="hljs-comment">// 需要手动引入cdn - jQuery</span>
        <span class="hljs-attr">jquery</span>: <span class="hljs-string">'jQuery'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">3.2.1.5 dll</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    使用dll技术，对某些库（第三方库：jquery、react、vue...）进行单独打包
        当你运行webpack时，默认查找webpack.comfig.js配置文件
        需要运行：webpack.dll.js文件
        --> webpack --config webpack.dll.js
*/</span>
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-comment">// 最终打包生成的[name] --> jquery</span>
        <span class="hljs-comment">// ['jquery'] --> 要打包的库是jquery</span>
        <span class="hljs-attr">jquery</span>: [<span class="hljs-string">'jquery'</span>]
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'dll'</span>),
        <span class="hljs-attr">library</span>: <span class="hljs-string">'[name]_[hash]'</span>,<span class="hljs-comment">// 打包库里面向外暴露出去的内容叫什么名字</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// 打包生成一个manifest.json --> 提供和jquery映射</span>
        <span class="hljs-keyword">new</span> webpack.DllPlugin(&#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'[name]_[hash]'</span>,<span class="hljs-comment">// 映射库的暴露的内容名称</span>
            <span class="hljs-attr">path</span>: resolver(__dirname, <span class="hljs-string">'dll/manifest.json'</span>)<span class="hljs-comment">// 输出文件路径</span>
        &#125;)
    ],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>
&#125;


<span class="hljs-comment">// webpack.config.js</span>

<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>);
<span class="hljs-keyword">const</span> AddAssetHtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'add-asset-html-webpack-plugin'</span>);
plugins: [
    ...
    <span class="hljs-keyword">new</span> webpack.DllReferencePlugin(&#123;
        <span class="hljs-comment">//告诉webpack哪些库不参与打包，同时使用时的名称也得变</span>
        <span class="hljs-attr">manifest</span>: resolve(__dirname, <span class="hljs-string">'dll/manifest.json'</span>)
    &#125;),
    <span class="hljs-comment">// 将某个文件打包输出去，并在html中自动引入该资源</span>
    <span class="hljs-keyword">new</span> AddAssetHtmlWebpackPlugin(&#123;
        <span class="hljs-attr">filepath</span>: resolve(__dirname, <span class="hljs-string">'dll/jquery.js'</span>)
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">3.2.2 优化代码运行的性能</h4>
<h5 data-id="heading-24">3.2.2.1 文件缓存</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    文件资源缓存 --> 让代码上线运行缓存更好使用
        问题：强缓存命中，无法获取最新资源
        hash：每次webpack构建时会生产唯一的hash值
            问题：因为js和css同时使用一个hash值，如果重新打包，会导致所有缓存失效（无论改动几个文件）
        chunkhash：根据chunk生产的hash值，如果打包来源于同一个chunk，那么hash值就一样
            问题：js和css的hash值还是一样的，因为css时在js中被引入的，所以同属于一个chunk
        contenthash：根据文件内容生产hash值，不同文件hash值一定不一样
*/</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,

    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// filename: 'js/build.[hash:10].js',</span>
        <span class="hljs-comment">// filename: 'js/build.[chunkhash:10].js',</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/build.[contenthash:10].js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-25">3.2.2.2 <strong>tree shaking</strong></h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
tree shaking：去除无用代码
前提：1. 必须使用ES6模块化
 2. 开启production环境
作用：减少代码体积

在package.json中配置
"sideEffects": false所有代码都没有副作用（都可以进行tree shaking）
问题：可能会把css、/@babel/polyfill文件干掉
"sideEffects": ["*.css", "*.less"]
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-26">3.2.2.3 code split</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// demo1</span>
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// 单入口</span>
    <span class="hljs-comment">// entry: './src/index.js',</span>
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-comment">// 多入口：输出多个bundle</span>
        <span class="hljs-attr">index</span>: <span class="hljs-string">'./src/index.js'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-string">'./src/test.js'</span>
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// [name] 取文件名</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[contenthash:10].js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// demo2</span>
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// 单入口</span>
    <span class="hljs-comment">//entry: './src/index.js',</span>
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-comment">// 多入口：输出多个bundle</span>
        <span class="hljs-attr">index</span>: <span class="hljs-string">'./src/index.js'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-string">'./src/test.js'</span>
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// [name] 取文件名</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[contenthash:10].js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    <span class="hljs-comment">/*
          1. 可以将node_modules中代码单独打包一个chunk最终输出
          2. 自动分析，多入口文件中有没有公共的文件，如果有会打包成一个单独的chunk
    */</span>
    <span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">splitChunks</span>: &#123;
            <span class="hljs-attr">chunks</span>: all
        &#125;
    &#125;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// demo3</span>
<span class="hljs-comment">/*
    基于webpack配置optimization，通过js代码，让某个文件被单独打包成一个chunk
    import动态导入语法：能将某个文件单独打包
*/</span>
<span class="hljs-comment">// 限定名字</span>
<span class="hljs-keyword">import</span>(<span class="hljs-comment">/*webpackChunkName: 'test'*/</span><span class="hljs-string">'./test'</span>)
    .then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123; &#125;)
    .catch(<span class="hljs-function">() =></span> &#123; &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-27">3.2.2.4 lazy loading</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 基于3.2.1.4代码分割实现懒加载</span>
<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>).onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// 懒加载：当文件需要使用时才加载</span>
  <span class="hljs-comment">// 预加载 prefetch：会在使用之前，提前加载js文件</span>
  <span class="hljs-comment">// 正常加载可以认为是并行加载（同一时间加载多个文件）</span>
  <span class="hljs-comment">// 预加载会等其他资源加载完毕，浏览器空闲了，再偷偷加载资源</span>
  <span class="hljs-keyword">import</span>(<span class="hljs-comment">/*webpackChunkName: 'test', webpackPrefetch: true*/</span><span class="hljs-string">'./test'</span>)
    .then(<span class="hljs-function">(<span class="hljs-params">&#123;mul&#125;</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(mul(<span class="hljs-number">4</span>,<span class="hljs-number">5</span>))
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-28">3.2.2.5 PWA</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    PWA：渐进式网络开发应用程序（离线可访问）
        workbox -->workbox-webpack-plugin
*/</span>

<span class="hljs-keyword">const</span> WorkboxWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'workbox-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    ...
    <span class="hljs-attr">plugins</span>: [
...
    <span class="hljs-comment">/*
        1. 帮助serviceworker快速启动
        2. 删除旧的serviceworker
    
        生成一个serviceworker配置文件
    */</span>
    <span class="hljs-keyword">new</span> WorkboxWebpackPlugin.GenerateSW(&#123;
        <span class="hljs-attr">clientsClaim</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">skipWaiting</span>: <span class="hljs-literal">true</span>
    &#125;)
  ]
&#125;

<span class="hljs-comment">/*
    1. eslint不认识window、navigator全局变量
        解决：需要修改package.json中eslintConfig配置
            "env": &#123;
                "brower": true// 支持浏览器端全局变量
            &#125;
   2. sw代码必须运行在服务器上
          --> nodejs
          --> npm i serve -g
                    serve -s build启动服务器，将build目录下的所有资源作为静态资源暴露出去
*/</span>
<span class="hljs-comment">// index.js 入口文件</span>
<span class="hljs-keyword">if</span> (<span class="hljs-string">'serviceWorker'</span> <span class="hljs-keyword">in</span> navigator) &#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function">() =></span> &#123;
        navigator.serviceWorker
            .register(<span class="hljs-string">'/service-worker.js'</span>)
            .then(<span class="hljs-function">() =></span> &#123; &#125;)
            .catch(<span class="hljs-function">() =></span> &#123; &#125;)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">四、webpack配置详解</h2>
<h3 data-id="heading-30">4.1 entry</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    entry: 入口起点
        1. string --> './src/index.js'
            打包形成一个chunk，输出一个bundle文件。
            此时chunk的默认名称是main
    2. array-->['./src/js', './src/add.js']
        多入口
        所有入口文件最终只会形成一个chunk，输出一个bundle文件
            --> 一般用于HMR功能中让html热更新生效
    3. object
        多入口
        有几个入口文件就形成几个chunk，输出几个bundle文件
        此时chunk的名称是key
        --> 特殊用法3里面包含1+2两种形式
*/</span>
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// entry: './src/index.js',</span>
    <span class="hljs-comment">// entry: ['./src/index.js', './src/add.js'],</span>
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-comment">// index: './src/index.js',</span>
        <span class="hljs-attr">index</span>: [<span class="hljs-string">'./src/index.js'</span>, <span class="hljs-string">'./src/add.js'</span>],
        <span class="hljs-attr">add</span>: <span class="hljs-string">'./src/add.js'</span>
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">4.2 output</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// 文件名称（指定名称+目录）</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].js'</span>
    <span class="hljs-comment">// 输出文件目录（将来所有资源输出的公共目录）</span>
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
  <span class="hljs-comment">// 所有资源引入公共路径前缀:'imgs/a.jpg' --> '/imgs/a.jpg'</span>
  <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'[name]_chunk.js'</span>,<span class="hljs-comment">// 非入口chunk的名称</span>
        <span class="hljs-comment">// library: '[name]',// 整个库向外暴露的变量名 + 一般结合dll一起使用</span>
        <span class="hljs-comment">// libraryTarget: 'window'// 变量名添加到哪个上 browser</span>
        <span class="hljs-comment">// libraryTarget: 'global'// 变量名添加到哪个上 node</span>
        <span class="hljs-comment">// libraryTarget: 'commonjs'// 模块化语法</span>

    &#125;,
    <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">4.3 module</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].js'</span>
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            <span class="hljs-comment">// loader的配置</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                <span class="hljs-comment">// 排除node_modules下的js文件</span>
                exclude: <span class="hljs-regexp">/node_modules/</span>,
                <span class="hljs-comment">// 只检查src下的js文件</span>
                include: resolve(__dirname, <span class="hljs-string">'src'</span>),
                <span class="hljs-comment">// 优先执行</span>
                <span class="hljs-attr">enfore</span>: <span class="hljs-string">'pre'</span>,
                <span class="hljs-comment">// 延后执行</span>
                <span class="hljs-comment">// enfore: 'post',</span>
                <span class="hljs-comment">// 单个loader使用loader</span>
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'eslint-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;&#125;
            &#125;,
            &#123;
                <span class="hljs-comment">// 一下配置只会生效一个</span>
                <span class="hljs-attr">oneof</span>: []
            &#125;

        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">4.4 resolve</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].js'</span>
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            <span class="hljs-comment">// loader的配置</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
            &#125;,
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-comment">// 解析模块的规则</span>
    <span class="hljs-attr">resolve</span>: &#123;
        <span class="hljs-comment">// 配置解析模块路径别名: 简写路径</span>
        <span class="hljs-attr">alias</span>: &#123;
            <span class="hljs-attr">$css</span>: resovle(__dirname, <span class="hljs-string">'src/css'</span>)
        &#125;,
        <span class="hljs-comment">// 配置省略文件路径的后缀名</span>
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'js'</span>, <span class="hljs-string">'json'</span>, <span class="hljs-string">'css'</span>, <span class="hljs-string">'jsx'</span>],
        <span class="hljs-comment">// 告诉webpack解析模块是去找哪个目录</span>
        <span class="hljs-attr">modules</span>: [resolve(__dirname, <span class="hljs-string">'../../node_modules'</span>), <span class="hljs-string">'node_modules'</span>]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">4.5 devServer</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].js'</span>
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            <span class="hljs-comment">// loader的配置</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
            &#125;,
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-comment">// 运行代码的目录</span>
        <span class="hljs-attr">contentBase</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
        <span class="hljs-comment">// 见识contenBase目录下的所有文件，一旦文件变化就会reload</span>
        <span class="hljs-attr">watchContentBase</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">watchOptions</span>: &#123;
            <span class="hljs-comment">// 忽略文件</span>
            <span class="hljs-attr">ignored</span>: <span class="hljs-regexp">/node_modules/</span>
        &#125;,
        <span class="hljs-comment">// 启动gzip压缩</span>
        <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 端口号</span>
        <span class="hljs-attr">port</span>: <span class="hljs-number">5000</span>,
        <span class="hljs-comment">// 域名</span>
        <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
        <span class="hljs-comment">// 自动打开浏览器</span>
        <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 开启HMR功能</span>
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 不要显示启动服务器日志信息</span>
        <span class="hljs-attr">clientLogLevel</span>: <span class="hljs-string">'none'</span>,
        <span class="hljs-comment">// 除了一些基本启动信息以外，其他内容都不要显示  </span>
        <span class="hljs-attr">quiet</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 如果出错了，不要全屏提示</span>
        <span class="hljs-attr">overlay</span>: <span class="hljs-literal">false</span>，
        <span class="hljs-comment">// 服务器代理 --> 解决开发环境跨域问题</span>
        <span class="hljs-attr">proxy</span>: &#123;
            <span class="hljs-comment">// 一旦devServer(5000)服务器接收到/api/xxx的请求，就会把请求转发到另一个服务器</span>
            <span class="hljs-string">'/api'</span>: &#123;
                <span class="hljs-attr">target</span>: <span class="hljs-string">'http://localhost:3000'</span>,
                <span class="hljs-comment">// 发送请求时，请求路径重写：将/api/xx-->/xxx；（去掉/api）</span>
                <span class="hljs-attr">pathRewrite</span>: &#123;
                    <span class="hljs-string">'^/api'</span>: <span class="hljs-string">''</span>
                &#125;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">4.6 optimization</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> TerserWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'terser-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].js'</span>
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>)
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            <span class="hljs-comment">// loader的配置</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
            &#125;,
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">splitChunks</span>: &#123;
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
            <span class="hljs-comment">// 以下为默认值</span>
            <span class="hljs-comment">/*
             minSize: 30 * 1024,// 分割的chunk最小为30kb
             maxSize: 0,// 最大没有限制
             minChunks: 1,// 要提取的chunk最少被引用1次
             maxAsyncRequests: 5,// 按需加载时并行加载的文件最大数量
             maxInitialRequests: 3,// 入口js文件最大并行请求数量
             automaticNameDelimiter: '～',// 名称链接符
             name: true,// 可以使用命名规则
             cacheGroups: &#123;
               // 分割chunk的组
               // node_modules文件会被打包到wendors组的chunk中。--> vendors～xxx.js
               // 满足上面的公共规则，如：大小超过30kb，至少被引用一次
               vendors: &#123;
                 test: /[\\/]node_modules[\\/]/,
                 // 优先级
                 priority: -10
               &#125;,
               default: &#123;
                   // 要提取的chunk最少被引用2次
                 minChunks: 2,
                 // 优先级
                 priority: -20,
                 // 如果当前要打包的模块，和之前已经被提取的模块是同一个，就会复用
                 reuseExistingChunk: true
               &#125;
             &#125;
             */</span>
        &#125;,
        <span class="hljs-comment">// 将当前模块的记录其他模块的hash单独打包为一个文件runtime</span>
        <span class="hljs-comment">// 解决：修改a文件导致b文件的contenthash变化</span>
        <span class="hljs-attr">runtimeChunk</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-function"><span class="hljs-params">entrypoint</span> =></span> <span class="hljs-string">`runtime-<span class="hljs-subst">$&#123;entrypoint.name&#125;</span>`</span>
        &#125;,
        <span class="hljs-attr">minimizer</span>: &#123;
            <span class="hljs-comment">// 配置生成环境的压缩方案：js和css</span>
            <span class="hljs-keyword">new</span> TerserWebpackPlugin(&#123;
                <span class="hljs-comment">// 开启缓存</span>
                <span class="hljs-attr">cache</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-comment">// 开启多线程打包</span>
                <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span>
        <span class="hljs-comment">// 启动source-map</span>
        <span class="hljs-attr">sourceMap</span>: <span class="hljs-literal">true</span>
            &#125;)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            