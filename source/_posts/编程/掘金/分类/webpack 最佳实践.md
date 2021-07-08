
---
title: 'webpack 最佳实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 17:28:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image" alt="掘金引流终版.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://juejin.cn/post/6963056815420473357#heading-0" target="_blank" title="https://juejin.cn/post/6963056815420473357#heading-0">构建专栏系列目录入口</a></p>
</blockquote>
<blockquote>
<p>陆阳阳，微医前端技术部前端开发工程师，做一条安静的咸鱼。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>本文讲述的最佳实践是从日常业务中总结而出的，不一定适合所有项目。毕竟每个公司或个人的项目不同，最佳实践也会有所不同。但是可以从这篇文章借鉴吸收一点有用的东西，有问题的地方也欢迎大家积极<code>吐槽指正</code>。</p>
<p>为了避免出现 <code>我这明明可以，你那怎么不行</code> 的尴尬情况，这里列一下文章涉及到依赖的版本号。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">├── webpack           <span class="hljs-number">5.39</span><span class="hljs-number">.1</span>
├── webpack-cli       <span class="hljs-number">4.7</span><span class="hljs-number">.2</span>
├── node              <span class="hljs-number">12.8</span><span class="hljs-number">.0</span>
├── npm               <span class="hljs-number">6.10</span><span class="hljs-number">.2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">正文</h2>
<h3 data-id="heading-2">初始化项目</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">1.</span> mkdir test-app && cd test-app
<span class="hljs-number">2.</span> npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先添加一个入口文件 <code>/src/index.js</code> 和 webpack 配置文件 <code>webpack.config.js</code>，现在我们的目录结构如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test-app
    ├── src
    |    └── index.js
    ├── package.json
    ├── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 webpack</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install webpack webpack-cli -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">开始搞事情</h3>
<p>在 <code>src/index.js</code> 中随便写点东西</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">document</span>.writeTest(<span class="hljs-string">'hello world'</span>)
  &#125;
&#125;

<span class="hljs-keyword">new</span> Test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先来打个包看看啥效果， 执行命令 <code>npx webpack</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8236e6938cb54721aa291600a95fe51d~tplv-k3u1fbpfcp-zoom-1.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>等待一段时间后，看到目录有了变化, 新增了一个 <code>dist</code> 目录，该目录下有一个 <code>main.js</code> 文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test-app
  + ├── dist
  + |    └── main.js
    ├── src
    |    └── index.js
    ├── package.json
    ├── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让我们来看看 <code>main.js</code> 里有点啥</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>&#123;<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">document</span>.writeTest(<span class="hljs-string">"hello world"</span>)&#125;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这玩意都不用试，肯定不得行啊，得将 js 代码转成 es5 才行。首先安装下<code>babel-loader</code>及几个相关的依赖</p>
<h4 data-id="heading-4">配置 babel</h4>
<ul>
<li>babel-loader</li>
<li>@babel/core</li>
<li>@babel/preset-env</li>
<li>@babel/plugin-transform-runtime</li>
<li>@babel/plugin-proposal-decorators</li>
<li>@babel/plugin-proposal-class-properties</li>
<li>@babel/plugin-proposal-private-methods</li>
<li>@babel/runtime</li>
<li>@babel/runtime-corejs3</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install babel-loader @babel/core @babel/preset-env @babel/plugin-transform-runtime  @babel/plugin-proposal-decorators  @babel/plugin-proposal-<span class="hljs-class"><span class="hljs-keyword">class</span>-<span class="hljs-title">properties</span> @<span class="hljs-title">babel</span>/<span class="hljs-title">plugin</span>-<span class="hljs-title">proposal</span>-<span class="hljs-title">private</span>-<span class="hljs-title">methods</span> -<span class="hljs-title">D</span>
<span class="hljs-title">npm</span> <span class="hljs-title">install</span> @<span class="hljs-title">babel</span>/<span class="hljs-title">runtime</span> @<span class="hljs-title">babel</span>/<span class="hljs-title">runtime</span>-<span class="hljs-title">corejs3</span> -<span class="hljs-title">s</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.config.js</code> 文件， 添加 <code>babel-loader</code> 配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.[contenthash:8].js'</span>,
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jsx|js)$/</span>,
        use: <span class="hljs-string">'babel-loader'</span>,
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,
      &#125;,
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根目录下添加相应的 <code>.babelrc</code> 配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"presets"</span>: [<span class="hljs-string">"@babel/preset-env"</span>],
    <span class="hljs-string">"plugins"</span>: [
        [<span class="hljs-string">"@babel/plugin-transform-runtime"</span>, &#123;<span class="hljs-string">"corejs"</span>: <span class="hljs-number">3</span>&#125;],
        [<span class="hljs-string">"@babel/plugin-proposal-decorators"</span>, &#123; <span class="hljs-string">"legacy"</span>: <span class="hljs-literal">true</span> &#125;],
        [<span class="hljs-string">"@babel/plugin-proposal-class-properties"</span>, &#123; <span class="hljs-string">"loose"</span>: <span class="hljs-literal">true</span> &#125;],
        [<span class="hljs-string">"@babel/plugin-proposal-private-methods"</span>, &#123; <span class="hljs-string">"loose"</span>: <span class="hljs-literal">true</span> &#125;]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行命令 <code>npx webpack</code> 来打个包。完成后查看目录结构</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test-app
    ├── dist
  + |    ├── bundle.b8ba1739.js
    |    ├── main.js
    ├── src
    |    └── index.js
  + ├── .babelrc
    ├── package.json
    ├── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看构建后的 <code>bundle.b8ba1739.js</code> 文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">(<span class="hljs-function">()=></span>&#123;<span class="hljs-string">"use strict"</span>;<span class="hljs-keyword">new</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">n</span>(<span class="hljs-params"></span>)</span>&#123;!<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n,t</span>)</span>&#123;<span class="hljs-keyword">if</span>(!(n <span class="hljs-keyword">instanceof</span> t))<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"Cannot call a class as a function"</span>)&#125;(<span class="hljs-built_in">this</span>,n),<span class="hljs-built_in">document</span>.writeTest(<span class="hljs-string">"hello world"</span>)&#125;&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构建产物看着没什么问题了，接下来看下在浏览器中的实际效果。要看效果，肯定离不开 <code>html</code> 文件。</p>
<h4 data-id="heading-5">浏览器中观看效果</h4>
<p>作为一个伸手党直接从社区嫖来一个插件 <code>html-webpack-plugin</code>，这个插件的作用是将打包产物引入到我们提前准备好的模板 <code>.html</code> 文件中，我们访问这个文件就能直观的看到效果了</p>
<p>先来安装下插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install html-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着创建一个 <code>public</code> 目录， 用来存放静态资源。新增一个 <code>index.html</code> 模板，放在 public 目录下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test-app
    ├── dist
    |    ├── bundle.b8ba1739.js
    |    ├── main.js
    ├── src
    |    └── index.js
  + ├── public
  + |    └── index.html
    ├── .babelrc
    ├── package.json
    ├── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>webpack.config.js</code> 中配置 <code>html-webpack-plugin</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略 ...</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略 ...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'./public/index.html'</span>),
      <span class="hljs-attr">inject</span>: <span class="hljs-string">'body'</span>,
      <span class="hljs-attr">scriptLoading</span>: <span class="hljs-string">'blocking'</span>,
    &#125;),
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行命令 <code>npx webpack</code> 来打个包。打完包发现 <code>dist</code> 目录下多了一个 <code>index.html</code> 文件。浏览器中打开 <code>index.html</code> 看看对不对</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77df1302bd1643f68d12eb8fa11968bb~tplv-k3u1fbpfcp-zoom-1.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作为一个 api 工程师，连 api 都能记错。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8ef3df937fa46a5b2d105eab56e9a8e~tplv-k3u1fbpfcp-zoom-1.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改下 <code>src/index.js</code> 代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">document</span>.write(<span class="hljs-string">'hello world'</span>)
  &#125;
&#125;

<span class="hljs-keyword">new</span> Test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行命令 <code>npx webpack</code> 来打个包。老步骤，先检查下打包产物对不对</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test-app
    ├── dist
    |    ├── bundle.b8ba1739.js
 +  |    ├── bundle.dc044571.js
    |    ├── index.html
    |    ├── main.js
    ├── src
    |    └── index.js
    ├── public
    |    └── index.html
    ├── .babelrc
    ├── package.json
    ├── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看样子应该没错，代码修改了，打包后多了个 <code>.js</code> 文件。再看看效果对不对</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e78ab547532d41d6ac7642744b4891ef~tplv-k3u1fbpfcp-zoom-1.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>界面上也出现了 <code>hello world</code>。到这里为止，算是利用 <code>webpack</code> 走通了一个最小流程。</p>
<p>为什么说是最小，因为到目前为止这个配置在实际工作中 <del>基本没卵用</del> <code>实用性不大</code>。细心一点的人已经看出来了，上面存在三个问题</p>
<ol>
<li>每修改一次代码，都要走一遍打包流程，然后自己手动打开 html 文件，预览效果</li>
<li>第一次调用错误 api 的时候，报错信息定位不精确</li>
<li>打包目录下面 <code>上次构建产物</code> 也仍旧存在，时间长了会存在越来越多的无用代码</li>
</ol>
<p>作为一个懒人，第三点可以忍，第一点和第二点忍不了。我们一个个来解决</p>
<h4 data-id="heading-6">实时更新并预览效果</h4>
<p>针对第一点，查阅 <code>webpack</code> 官网，发现官网就给指了一条明路</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84253637eb8b4cc3838d21e17dc5f607~tplv-k3u1fbpfcp-zoom-1.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照官网教程，首先安装下 <code>webpack-dev-server</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install webpack-dev-server -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再在 <code>webpack.config.js</code> 中添加相应的配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略 ...</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略 ...</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-string">'3001'</span>, <span class="hljs-comment">// 默认是 8080</span>
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">stats</span>: <span class="hljs-string">'errors-only'</span>, <span class="hljs-comment">// 终端仅打印 error</span>
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否启用 gzip 压缩</span>
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://0.0.0.0:80'</span>,
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">'/api'</span>: <span class="hljs-string">''</span>,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>package.json</code> > <code>script</code> 中添加一个命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack serve  --open"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run dev</code>，这个时候在动在浏览器中打开了 <code>http://localhost:3001/</code> 页面。光自动打开还不够啊，我们的目标是每次修改后<code>不用构建</code>就能在浏览器中<code>实时查看</code>。为了测试这个功能是否生效，我们任意修改 <code>src/index.js</code> 文件并保存。发现浏览器中内容自动刷新生效了。</p>
<p>想了解更多关于 <code>devServer</code> 的可以阅读以下两篇文章</p>
<ul>
<li><a href="https://juejin.cn/post/6971237797734645767" target="_blank" title="https://juejin.cn/post/6971237797734645767">【Webpack】devServer 实验报告</a></li>
<li><a href="https://juejin.cn/post/6973825927708934174" target="_blank" title="https://juejin.cn/post/6973825927708934174">120 行代码帮你了解 Webpack 下的 HMR 机制</a></li>
</ul>
<h4 data-id="heading-7">sourcemap 配置</h4>
<p>第一个问题好了，再来看看第二个问题 <code>报错信息定位不精确</code>。我们仍旧在官网找找看，有没有对应的解决方案。通过 1 小时的文档阅读和 7 小时的摸鱼，终于在一天后找到了解决方法。</p>
<p>我们在 <code>webpack.config.js</code> 中添加配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略 ...</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略 ...</span>
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval-cheap-module-source-map'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个配置什么意思呢，它会告诉我们错误是在<code>原始代码</code>的哪一行发生的。废话不多说，先来看看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/521a4ddfd82d4196a51f3591a8930dd4~tplv-k3u1fbpfcp-zoom-1.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点进去看看是什么情况</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad4eaad54c7c46ddac5332bdd96a0e6f~tplv-k3u1fbpfcp-zoom-1.image" alt="28.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6b7eaba3d0d4e5d9ec663dba3cf11cb~tplv-k3u1fbpfcp-zoom-1.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这么精准的定位，一天可以改<code>100</code>个 bug 了。</p>
<p>但是！！！ 这玩意好归好，生产环境可不能乱用。这里建议</p>
<p><code>开发环境</code> 最佳： eval-cheap-module-source-map
<code>生产环境</code> 最佳： hidden-source-map</p>
<p>什么？你上下嘴皮子吧嗒一合，说最佳就最佳？没有拿得出手的理由我们是不会信的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edc6cf1f844349e898b553d41b8cd331~tplv-k3u1fbpfcp-zoom-1.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>造谣是不可能造谣的，这辈子都不会。我也是吸收了这篇文章 <a href="https://juejin.cn/post/6969748500938489892" target="_blank" title="https://juejin.cn/post/6969748500938489892">万字长文：关于 sourcemap，这篇文章就够了</a> 的精华才总结出来的。</p>
<p>一万字的文章总结成两句话，10 秒钟吸收</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f21c3f3a7c5d4d23af15871e8ba9565c~tplv-k3u1fbpfcp-zoom-1.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>世事总是这么奇妙，按照上面的思路，在解决第二个问题的时候又带出了一个新的问题，某些配置可能需要区分环境来设置，不同的环境设置合适的配置。就像在解决一个<code>bug A</code>的过程中，发现了一个新<code>的 bug B</code>。看来在解决上面第三个问题之前，得先解决这个 <code>区分环境配置</code> 的问题了。</p>
<h4 data-id="heading-8">拆分环境</h4>
<p>按照一般惯例，我们会有 <code>开发</code>、<code>测试</code>、<code>预发</code>、<code>生产</code>几个环境。但是我个人很多情况下 <code>开发</code> 和 <code>测试</code> 环境是同一套配置，所以我这里直接省略 <code>测试</code> 这个环境。</p>
<p>修改下目录结构</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test-app
  + ├── build
  + |    ├── webpack.base.js
  + |    ├── webpack.dev.js
  + |    ├── webpack.pre.js
  + |    ├── webpack.pro.js
    ├── dist
    ├──  ├── bundle.b8ba1739.js
    ├──  ├── bundle.dc044571.js
    |    ├── index.html
    |    ├── main.js
    ├── src
    |    └── index.js
    ├── public
    |    └── index.html
    ├── .babelrc
    ├── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从目录中就可以看出一点东西，我们删除了原先根目录下的 <code>webpack.config.js</code> 文件。新增了一个 <code>build</code> 目录。在 <code>build</code> 目录下我们需要建一个 <code>webpack.base.js</code> 文件。用来存放各个环境公共的配置，毕竟不可能所有配置在各个环境中都不一样。然后按照我们各自项目实际的需求来建立不同环境的配置文件。</p>
<p>先修改公共配置文件 <code>webpack.base.js</code>。原先的 <code>devServe</code> 配置由于只有开发环境有；<code>devtool</code> 各个环境不一样，所以这两个配置从公共配置里移除了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-keyword">const</span> rootDir = process.cwd();

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: path.resolve(rootDir, <span class="hljs-string">'src/index.js'</span>),
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(rootDir, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.[contenthash:8].js'</span>,
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jsx|js)$/</span>,
        use: <span class="hljs-string">'babel-loader'</span>,
        <span class="hljs-attr">include</span>: path.resolve(rootDir, <span class="hljs-string">'src'</span>),
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,
      &#125;,
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: path.resolve(rootDir, <span class="hljs-string">'public/index.html'</span>),
      <span class="hljs-attr">inject</span>: <span class="hljs-string">'body'</span>,
      <span class="hljs-attr">scriptLoading</span>: <span class="hljs-string">'blocking'</span>,
    &#125;),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来配置各个环境的配置，这里主要用到一个 <code>webpack-merge</code> 插件，用来合并公共配置，执行 <code>npm install webpack-merge -D</code></p>
<p>修改 <code>webpack.dev.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>);
<span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.base'</span>);

<span class="hljs-built_in">module</span>.exports = merge(baseConfig, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval-cheap-module-source-map'</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-string">'3001'</span>, <span class="hljs-comment">// 默认是 8080</span>
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">stats</span>: <span class="hljs-string">'errors-only'</span>, <span class="hljs-comment">// 终端仅打印 error</span>
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否启用 gzip 压缩</span>
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://0.0.0.0:80'</span>,
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">'/api'</span>: <span class="hljs-string">''</span>,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为这里不涉及到实际的项目开发，所以这里<code>预发</code>和<code>生产</code>两个环境的文件先配置成一样的，大家可以根据自己的实际需要来进行不同的配置。</p>
<ul>
<li><code>webpack.pre.js</code></li>
<li><code>webpack.pro.js</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>);
<span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.base'</span>);

<span class="hljs-built_in">module</span>.exports = merge(baseConfig, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'hidden-source-map'</span>,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到仔细的人已经发现，配置中多了一个 <code>mode</code> 属性，这个会在后面解释一波，这里先不讲</p>
<p>修改 package.json 中的命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack serve --config build/webpack.dev.js --open"</span>,
    <span class="hljs-string">"build:pro"</span>: <span class="hljs-string">"npx webpack --config build/webpack.pro.js"</span>,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行 <code>npm run dev</code> 看看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32285bb9145d47cfb836dd6f5f95d656~tplv-k3u1fbpfcp-zoom-1.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看来是没问题了，现在已经成功把 <code>webpack.config.js</code> 文件根据环境进行拆分成了多个文件。</p>
<p>现在来回顾下之前提出的第三个问题</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b99b64a3754445af9c2d64a7a6727906~tplv-k3u1fbpfcp-zoom-1.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个项目小的时候其实问题不大，但是当项目大了之后，每次打包都增加几百上千的文件，还是有点恐怖的。所以还是把这个问题也顺带解决下好了。</p>
<h4 data-id="heading-9">打包时清除上次构建产物</h4>
<p>我们的目标是每次打包时删除上次打包的产物，保证打包目录下所有文件都是新的，社区查找一番后，找到一个插件<code>clean-webpack-plugin</code> ，来看下这个插件的介绍</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc46ca659b374edd8504ea60b107020b~tplv-k3u1fbpfcp-zoom-1.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比较懒，所以直接上截图了。老步骤，先安装 <code>npm install clean-webpack-plugin -D</code> 然后直接将文档中的示例代码<code>借鉴</code>到我们的项目中。 修改 <code>webpack.base.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: path.resolve(rootDir, <span class="hljs-string">'public/index.html'</span>),
      <span class="hljs-attr">inject</span>: <span class="hljs-string">'body'</span>,
      <span class="hljs-attr">scriptLoading</span>: <span class="hljs-string">'blocking'</span>,
    &#125;),
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>试下效果，执行 <code>npm run build:pro</code> 打个包。查看目录</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">test-app
    ├── build
    |    ├── webpack.base.js
    |    ├── webpack.dev.js
    |    ├── webpack.pre.js
    |    ├── webpack.pro.js
    ├── dist
    |    ├── bundle.fd44c2eb.js
    |    ├── bundle.fd44c2eb.js.map
    |    ├── index.html
    ├── src
    |    └── index.js
    ├── public
    |    └── index.html
    ├── .babelrc
    ├── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>dist</code> 目录下原先存在的 <code>main.js</code>、<code>bundle.b8ba1739.js</code> 等前几次打包产物已经自动清除了。到这里第三个问题也解决了</p>
<h3 data-id="heading-10">功能完善</h3>
<h4 data-id="heading-11">添加 css 和 less 支持</h4>
<p>为什么不添加 <code>sass</code> 支持？ 因为我不用 <code>sass</code></p>
<p>首先，在 <code>src</code> 目录下添加一个 <code>index.less</code> 文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.test &#123;
  <span class="hljs-attr">color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>src/index.js</code> 文件，在文件中引用刚才添加的 <code>less</code> 文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'./index.less'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.renderDiv()
  &#125;

  <span class="hljs-function"><span class="hljs-title">renderDiv</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
    div.className = <span class="hljs-string">'test'</span>
    div.innerHTML = <span class="hljs-string">'hello world'</span>
    <span class="hljs-built_in">document</span>.body.appendChild(div)
  &#125;
&#125;

<span class="hljs-keyword">new</span> Test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run dev</code></p>
<p>等待 10 分钟后，页面迟迟没有加载任何东西，打开控制台一看</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8c2458ad48744da9bef953b699bd24b~tplv-k3u1fbpfcp-zoom-1.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>英语 8 级的我立马读懂了报错："你 可能 需要 一个 什么什么 loader 来 处理 这个 文件 类型， 目前 没有 loaders 被配置 来 process 这个 文件"</p>
<p>再结合官网的说明</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b243bdcb42f401fad5b2ca67c49949a~tplv-k3u1fbpfcp-zoom-1.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到了这里，我好像隐约明白了 <code>webpack</code> 的真谛：<code>虽然很多时候我不行，但是很多大佬会让我行</code>。呸，什么叫不行？这叫 <code>灵活可插拔</code>，正是这种特性，让 webpack 可灵活支持各种复杂场景的自定义配置。</p>
<p>忘了正事儿，既然问题找到了，就好解决了，找到几个处理 <code>css</code> 和 <code>less</code> 的 loader 就行</p>
<p>首先安装 loader</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install less style-loader css-loader less-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再修改 <code>webpack.base.js</code> 文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// 省略...</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(le|c)ss$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'less-loader'</span>]
      &#125;,
    ]
  &#125;,
  <span class="hljs-comment">// 省略...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行 <code>npm run dev</code>，查看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2974c654e914834a5ab8fa43ec7b422~tplv-k3u1fbpfcp-zoom-1.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">css module</h4>
<p>这一块是基于上面的模块修改的，解决 <code>css</code> 命名混乱和冲突的。不需要的话可以直接跳过这一块。</p>
<p>修改 <code>webpack.base.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">//  省略...</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(le|c)ss$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: [
          <span class="hljs-string">'style-loader'</span>,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">modules</span>: &#123;
                <span class="hljs-attr">compileType</span>: <span class="hljs-string">'module'</span>,
                <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">"[local]__[hash:base64:5]"</span>,
              &#125;,
            &#125;,
          &#125;,
          <span class="hljs-string">'less-loader'</span>
        ]
      &#125;,
    ]
  &#125;,
  <span class="hljs-comment">// 省略...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run dev</code> 来看看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8c27e9eadf84046bd25c52070f32ff7~tplv-k3u1fbpfcp-zoom-1.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>给 <code>class</code> 样式名称后加上一个哈希串，具体的配置可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fcss-loader" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/css-loader" ref="nofollow noopener noreferrer">css-loader 官网</a></p>
<h4 data-id="heading-13">css 自动添加前缀</h4>
<p>首先安装插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install autoprefixer postcss postcss-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.base.js</code> 配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-keyword">const</span> autoprefixer = <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// 省略...</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(le|c)ss$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: [
          <span class="hljs-comment">// 省略...</span>
          <span class="hljs-string">'less-loader'</span>,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">postcssOptions</span>: &#123;
                <span class="hljs-attr">plugins</span>: [
                  [<span class="hljs-string">"autoprefixer"</span>],
                ],
              &#125;,
            &#125;,
          &#125;
        ]
      &#125;,
    ]
  &#125;,
  <span class="hljs-comment">// 省略...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">打包后抽离 css 文件</h4>
<p>首先安装 <code>mini-css-extract-plugin</code> 插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install mini-css-extract-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.base.js</code> 配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// 省略...</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(le|c)ss$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: [
          MiniCssExtractPlugin.loader,
          <span class="hljs-comment">// 省略...</span>
        ]
      &#125;,
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 省略...</span>
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/[name].css'</span>,
    &#125;),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run build:pro</code> 打个包看看效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b449c33f789456bb2eaef214b3e06fa~tplv-k3u1fbpfcp-zoom-1.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 css 已经被抽离出来了</p>
<h4 data-id="heading-15">压缩打包后的 css 文件</h4>
<p>首先安装 <code>optimize-css-assets-webpack-plugin</code> 插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install optimize-css-assets-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.base.js</code> 配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-keyword">const</span> OptimizeCssPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 省略...</span>
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/[name].css'</span>,
    &#125;),
    <span class="hljs-keyword">new</span> OptimizeCssPlugin(),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run build:pro</code> 打个包看看效果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.test__1PSRs&#123;<span class="hljs-attr">color</span>:red;transition-duration:.4s&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出 css 已经被压缩了</p>
<h4 data-id="heading-16">复制静态资源到打包目录</h4>
<p>有些时候有些第三方的 js 插件没有提供 npm 包，只提供了一个 cdn 地址或者一份文件需要自己下载下来。通常我们下载下来之后放在我们的 <code>public/js</code> 目录下面，然后 <code>public/index.html</code> 文件里直接用 <code>script</code> 标签引入。这个时候不管是 <code>npm run dev</code> 开发时，还是 <code>npm run build:pro</code> 构建后，这个 js 文件都是找不到的。我们可以尝试下</p>
<p>在 <code>public/js</code> 新加一个 <code>test.js</code> 的空文件，啥内容都不用。然后在 <code>public/index.html</code> 中引入这个文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    // 省略
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./js/test.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run dev</code> 查看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fa8b1138ad9498cbbf1564bfcdf7540~tplv-k3u1fbpfcp-zoom-1.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们可以用 <code>copy-webpack-plugin</code> 这个插件，在构建的时候，将 <code>public/js</code> 的静态资源复制到 <code>dist</code> 目录下，这样文件就能找到了</p>
<p>安装插件 <code>npm install copy-webpack-plugin -D</code></p>
<p>修改 <code>webpack.base.js</code> 配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-keyword">const</span> CopyWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'copy-webpack-plugin'</span>);

<span class="hljs-keyword">const</span> rootDir = process.cwd();

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 省略...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: path.resolve(rootDir, <span class="hljs-string">'public/index.html'</span>),
      <span class="hljs-attr">inject</span>: <span class="hljs-string">'body'</span>,
      <span class="hljs-attr">scriptLoading</span>: <span class="hljs-string">'blocking'</span>,
    &#125;),
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
    <span class="hljs-keyword">new</span> CopyWebpackPlugin(&#123;
      <span class="hljs-attr">patterns</span>: [
        &#123;
          <span class="hljs-attr">from</span>: <span class="hljs-string">'*.js'</span>,
          <span class="hljs-attr">context</span>: path.resolve(rootDir, <span class="hljs-string">"public/js"</span>),
          <span class="hljs-attr">to</span>: path.resolve(rootDir, <span class="hljs-string">'dist/js'</span>),
        &#125;,
      ],
    &#125;)
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/[name].css'</span>,
    &#125;),
    <span class="hljs-keyword">new</span> OptimizeCssPlugin(),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run dev</code> 查看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/608e15682e494ba19d051ba91094b2b9~tplv-k3u1fbpfcp-zoom-1.image" alt="19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>静态文件已经可以正常加载了。</p>
<h4 data-id="heading-17">资源加载器</h4>
<p>项目中难免要引入一些图标、图片等资源，在不做任何处理的情况下，我们尝试下在代码中引用图片，修改 <code>src/index.js</code> 文件如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> wuhanjiayou <span class="hljs-keyword">from</span> <span class="hljs-string">'../public/asset/a.jpeg'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.renderImg()
  &#125;

  <span class="hljs-function"><span class="hljs-title">renderImg</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> img = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'img'</span>)
    img.src = wuhanjiayou
    <span class="hljs-built_in">document</span>.body.appendChild(img)
  &#125;
&#125;

<span class="hljs-keyword">new</span> Test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run dev</code> 看下效果，报了个熟悉的错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6074d3f20ad463e88e4d2530a01ea45~tplv-k3u1fbpfcp-zoom-1.image" alt="20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照以往的套路，直接引用社区的三件套 <code>raw-loader</code>、<code>url-loader</code>、<code>file-loader</code>，安装依赖，配置依赖，一通操作下来就解决了问题。现在我们使用 <code>webpack5</code>就方便多了，不用安装任何依赖，直接修改 <code>webpack.base.js</code> 配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-attr">rules</span>: [
    &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif|jpeg|webp|svg|eot|ttf|woff|woff2)$/</span>,
        type: <span class="hljs-string">'asset'</span>,
    &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没错，就是这么简单。<code>type</code> 属性还有其他几个值，具体可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fguides%2Fasset-modules%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/guides/asset-modules/" ref="nofollow noopener noreferrer">官方文档</a></p>
<p>配置已经修改好了，执行 <code>npm run dev</code> 再来看下效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/040decb24cbd4aadaeee9eb644fb9a1d~tplv-k3u1fbpfcp-zoom-1.image" alt="21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>搞定！</p>
<p>上面讲到的东西基本够小项目的日常开发需求了，常用的 loader 和 plugin 都已经有所涉及。但是，如果你的项目特别复杂，需求又比较小众，社区没有现成的 loader 和 plugin 可以借鉴，那么只能<code>自己动手实现</code>一个了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4084e953669c43fa8ee60afa78a6c588~tplv-k3u1fbpfcp-zoom-1.image" alt="22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可能在一部分人眼中，loader 和 plugin 是比较神秘的，也不可能想着自己去造一个轮子。但是当碰到问题又没有现成的解决方案的时候，那就不得不自己造了。</p>
<p>看了这篇文章 <a href="https://juejin.cn/post/6976052326947618853" target="_blank" title="https://juejin.cn/post/6976052326947618853">Webpack - 手把手教你写一个 loader / plugin</a> 应该能很快上手</p>
<h3 data-id="heading-18">项目优化</h3>
<p>刚才也讲到了，上面的一通操作基本够小项目开发使用了。为什么是小项目？大项目不行吗？当一个项目大到路由都有<code>几百个</code>的时候，一次热更新就需要十几二十多秒，一次打包要半个小时。开发时，一次代码改动保存就要等 <code>20 秒</code>，这搁谁谁都忍不了啊。这个时候就需要想点办法来优化。</p>
<h4 data-id="heading-19">loader 配置优化</h4>
<p>这个其实上面已经做了。明确告诉 loader，哪些文件不用做处理(exclude)，或者只处理哪些文件(include)。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jsx|js)$/</span>,
    use: <span class="hljs-string">'babel-loader'</span>,
    <span class="hljs-comment">// include: [path.resolve(rootDir, 'src')]</span>
    <span class="hljs-comment">// exclude: /node_modules/,</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般倾向于使用 <code>include</code>，但是如果怕漏处理一些文件的话，粗暴点，使用 <code>exclude: /node_modules/</code> 也可以。</p>
<p>这部分测试了下，提升速度不是很明显，应该算锦上添花吧</p>
<h4 data-id="heading-20">缓存</h4>
<p>先说下 <code>webpack5</code> 之前是怎么做的。</p>
<p>利用 <code>cache-loader</code> 将结果缓存中磁盘中；利用 <code>hard-source-webpack-plugin</code> 将结果缓存在 <code>node_modules/.cache</code> 下提升二次打包速度；利用 <code>DllReferencePlugin</code> 将变化不频繁的第三方库<code>提前单独</code>打包成动态链接库，提升真正业务代码的打包速度</p>
<p>webpack5 自带了持久化缓存，配置如下</p>
<p>开发环境 <code>webpack.dev.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cache: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'memory'</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生产环境 <code>webpack.pro.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cache: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'filesystem'</span>,
    <span class="hljs-attr">buildDependencies</span>: &#123;
      <span class="hljs-attr">config</span>: [__filename]
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个测试了下前后的打包时间</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8492af7ccd9344cf845aa60e6ad424e0~tplv-k3u1fbpfcp-zoom-1.image" alt="23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e25ef03911a847f7927ff540e7e25a5c~tplv-k3u1fbpfcp-zoom-1.image" alt="24.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>数据是这个数据：</p>
<ul>
<li>第一次: <code>12592 ms</code></li>
<li>第二次: <code>920 ms</code></li>
</ul>
<p>但是我心里默数了下，二次打包大概在 3 秒左右，咱也不知道控制台的计时逻辑是什么</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37c36605be7f44a28de692bcc7607157~tplv-k3u1fbpfcp-zoom-1.image" alt="25.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果在构建时，你主动确定要放弃旧的缓存的话，可以传一个新的 <code>version</code> 参数来放弃使用缓存</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cache: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'filesystem'</span>,
    <span class="hljs-attr">buildDependencies</span>: &#123;
      <span class="hljs-attr">config</span>: [__filename]
    &#125;,
    <span class="hljs-attr">version</span>: <span class="hljs-string">'new_version'</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">代码拆分</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">optimization: &#123;
    <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个在 <code>mode: production</code> 时是默认开启的，但是默认情况下只会对按需加载的代码进行分割。如果我们要对一开始就加载的代码也做分割处理，就要进行如上配置。</p>
<p>从官网截了一张图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e361de8e87a4abea47e3ceeaa87a7b6~tplv-k3u1fbpfcp-zoom-1.image" alt="26.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家的项目可能都有所不同，相对应的最佳的配置可能也有所不同，所以这里就补贴具体的配置了，大家有需要的可以看官网的文档对自己的项目进行配置 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fplugins%2Fsplit-chunks-plugin%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/plugins/split-chunks-plugin/" ref="nofollow noopener noreferrer">官网 optimization.splitChunks 更多配置</a>、<a href="https://juejin.cn/post/6979769284612325406" target="_blank" title="https://juejin.cn/post/6979769284612325406">「Webpack」从 0 到 1 学会 code splitting</a></p>
<h4 data-id="heading-22">mode</h4>
<p><code>mode: production</code> 在上面出现了这么多次，也没有具体说有哪些功能。其实当设置 <code>mode: production</code> 时，<code>webpack</code> 已经默认开启了一些优化措施。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9b8a0f09937436c8c88a4cee7418290~tplv-k3u1fbpfcp-zoom-1.image" alt="27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里面的一些东西由于篇幅较大也不做一一说明了，反正只要记得 <code>mode: production</code> 已经给我们做了一系列优化，真的想知道有哪些优化的，我找了篇文章，有兴趣的可以看看 <a href="https://juejin.cn/post/6844903695033843726" target="_blank" title="https://juejin.cn/post/6844903695033843726">mode 详解</a>
​</p>
<h4 data-id="heading-23">happypack</h4>
<p>利用 <code>happypack</code> 插件进行多线程打包，按照官网文档进行配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-keyword">const</span> Happypack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'happypack'</span>);
<span class="hljs-keyword">const</span> os = <span class="hljs-built_in">require</span>(<span class="hljs-string">'os'</span>)
<span class="hljs-keyword">const</span> happyThreadPool = Happypack.ThreadPool(&#123; <span class="hljs-attr">size</span>: os.cpus().length &#125;)

<span class="hljs-comment">// 省略...</span>
<span class="hljs-attr">rules</span>: [
  &#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jsx|js)$/</span>,
    <span class="hljs-comment">// use: 'babel-loader',</span>
    use: <span class="hljs-string">'Happypack/loader?id=js'</span>,
    <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,
  &#125;,
]

<span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> Happypack(&#123;
      <span class="hljs-attr">id</span>: <span class="hljs-string">'js'</span>, <span class="hljs-comment">// 这个 id 值为上面 Happypack/loader?id=js 问号后跟的参数</span>
      <span class="hljs-attr">use</span>: [<span class="hljs-string">'babel-loader'</span>],
      <span class="hljs-attr">threadPool</span>: happyThreadPool
    &#125;),
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于本篇文章写的是个 demo，没有业务代码，所以这个打包出来的时间基本没变化<code>甚至还多了 1 秒</code>，这里就不贴效果图了。 这是因为<code>happypack</code>执行也需要时间，如果项目比较小的话，就不需要配置了。 <code>js</code> 处理完之后那就是要处理<code>css</code>了， 按照处理<code>js</code>的方式，<code>ctrl+c/ctrl+v</code> 处理<code>css</code>。</p>
<p>执行 <code>npm run build:pro</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ERROR <span class="hljs-keyword">in</span> ./src/index.less
Module build failed (<span class="hljs-keyword">from</span> ./node_modules/Happypack/loader.js):
<span class="hljs-built_in">Error</span>: You forgot to add <span class="hljs-string">'mini-css-extract-plugin'</span> plugin (i.e. <span class="hljs-string">`&#123; plugins: [new MiniCssExtractPlugin()] &#125;`</span>), please read https:<span class="hljs-comment">//github.com/webpack-contrib/mini-css-extract-plugin#getting-started</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错说忘记添加了<code>mini-css-extract-plugin</code>插件，但是明明已经添加了，经过试验，发现是 <code>mini-css-extract-plugin</code> 这个插件引起 <code>happypack</code> 报错的。终于，在经过 <code>百度</code>、<code>谷歌</code> 等一系列骚操作后，我放弃了，没找到解决方法</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62deea3238ce4cc3b0eb5f01eb7a3aa5~tplv-k3u1fbpfcp-zoom-1.image" alt="尴尬.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在摆在面前的就三条路：</p>
<ul>
<li>放弃使用 <code>happypack</code></li>
<li>使用 <code>happypack</code> 优化<code>js</code>和<code>css</code>，放弃使用 <code>mini-css-extract-plugin</code></li>
<li>使用 <code>happypack</code> 优化 <code>js</code>，放弃优化 <code>css</code>，保留 <code>mini-css-extract-plugin</code></li>
</ul>
<p>知道咋解决的或有更好的方式的可以在下方留言，让我<del>白嫖</del> 借鉴下。</p>
<h4 data-id="heading-24">thread-loader</h4>
<p>如果采用上面第一种，放弃使用 <code>happypack</code>，可以用 <code>thread-loader</code> 代替下。而且这个配置非常简单。</p>
<p>先安装: <code>npm install thread-loader -D</code>，再修改配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略...</span>
<span class="hljs-attr">rules</span>: [
  &#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jsx|js)$/</span>,
    use: [<span class="hljs-string">'thread-loader'</span>, <span class="hljs-string">'babel-loader'</span>],
    <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(le|c)ss$/</span>,
    exclude: <span class="hljs-regexp">/node_modules/</span>,
    use: [
      MiniCssExtractPlugin.loader,
      <span class="hljs-string">'thread-loader'</span>,
      &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">modules</span>: &#123;
            <span class="hljs-attr">compileType</span>: <span class="hljs-string">'module'</span>,
            <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">"[local]__[hash:base64:5]"</span>,
          &#125;,
        &#125;,
      &#125;,
      <span class="hljs-string">'less-loader'</span>,
      &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">postcssOptions</span>: &#123;
            <span class="hljs-attr">plugins</span>: [
              [<span class="hljs-string">"autoprefixer"</span>],
            ],
          &#125;,
        &#125;,
      &#125;
    ],
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里应该可以应付一般的项目了。由于这篇文章主要讲述 webpack 的应用，所以很多知识点没有细讲，也没有精力细讲，但是很多涉及到的知识点都推荐了相应的文章，有兴趣的朋友可以看一下。</p>
<p>参考文献:</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fblog%2F2020-10-10-webpack-5-release%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/blog/2020-10-10-webpack-5-release/" ref="nofollow noopener noreferrer">webpack5</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fmigrate%2F5%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/migrate/5/" ref="nofollow noopener noreferrer">webpack4 升级到 5</a></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d58d4e21fa5a46ca85b05bebb55b01cf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            