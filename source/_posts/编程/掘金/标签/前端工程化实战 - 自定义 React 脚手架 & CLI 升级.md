
---
title: '前端工程化实战 - 自定义 React 脚手架 & CLI 升级'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/035452c09ff044b6b2df757c3e664a20~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 16:44:31 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/035452c09ff044b6b2df757c3e664a20~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️ 本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>上一篇<a href="https://juejin.cn/post/6982215543017193502" target="_blank" title="https://juejin.cn/post/6982215543017193502">企业级 CLI 开发</a>中，已经针对构建这块的流程做了一个初级的 CLI，但对于工程化体系的建设仅仅也只是迈出了第一步。</p>
<p>开发者平常最多的还是在开发业务代码，仅仅依靠 CLI 从 devops 末端去约束是远远不够的，所以一般的小团队也会从脚手架入手。</p>
<p>本篇将以 React 为例定制一套自定义脚手架以及对之前的 CLI 进行升级。</p>
<h2 data-id="heading-1">自定义 React 脚手架</h2>
<p>脚手架设计一般分为两块，一块是基础架构，一块是业务架构。</p>
<p>基础架构决定脚手架的技术选型、构建工具选型以及开发优化、构建优化、环境配置、代码约束、提交规范等。</p>
<p>业务架构则是针对业务模块划分、请求封装、权限设计等等于与业务耦合度更高的模块设计。</p>
<h3 data-id="heading-2">搭建基础架构</h3>
<p>跟 CLI 一样都是从 0 搭建这个脚手架，所以起手还是初始化项目与 ts 配置。</p>
<pre><code class="hljs language-js copyable" lang="js">npm init
tsx --init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上先将 <code>package.josn</code> 与 <code>tsconfig.json</code> 生成出来，<code>tsconfig.json</code> 的配置项可以直接使用下面的配置或者根据自己需求重新定义。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"include"</span>: [
    <span class="hljs-string">"src"</span>
  ],
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"module"</span>: <span class="hljs-string">"CommonJS"</span>,
    <span class="hljs-attr">"target"</span>: <span class="hljs-string">"es2018"</span>,
    <span class="hljs-attr">"outDir"</span>: <span class="hljs-string">"dist"</span>,
    <span class="hljs-attr">"noEmit"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"jsx"</span>: <span class="hljs-string">"react-jsx"</span>,
    <span class="hljs-attr">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"moduleResolution"</span>: <span class="hljs-string">"node"</span>,
    <span class="hljs-attr">"strict"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"noUnusedLocals"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">"noFallthroughCasesInSwitch"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"./"</span>,
    <span class="hljs-attr">"keyofStringsOnly"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"paths"</span>: &#123;
      <span class="hljs-attr">"@/*"</span>: [
        <span class="hljs-string">"./src/*"</span>
      ]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是 <code>package.josn</code> 的依赖与一些其他的配置，也一起附上，<strong>这里不再针对每个依赖包做单独说明，如果对哪个模块有不理解的地方，可以在留言区评论咨询。</strong></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"react-tpl"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"a react tpl"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-attr">"start"</span>: <span class="hljs-string">"cross-env NODE_ENV=development webpack-dev-server --config ./script/webpack.config.js"</span>,
  &#125;,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"cookieboty"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"@babel/cli"</span>: <span class="hljs-string">"^7.14.5"</span>,
    <span class="hljs-attr">"@babel/core"</span>: <span class="hljs-string">"^7.14.6"</span>,
    <span class="hljs-attr">"@babel/preset-env"</span>: <span class="hljs-string">"^7.14.7"</span>,
    <span class="hljs-attr">"@babel/preset-react"</span>: <span class="hljs-string">"^7.14.5"</span>,
    <span class="hljs-attr">"@babel/preset-typescript"</span>: <span class="hljs-string">"^7.14.5"</span>,
    <span class="hljs-attr">"babel-loader"</span>: <span class="hljs-string">"^8.2.2"</span>,
    <span class="hljs-attr">"clean-webpack-plugin"</span>: <span class="hljs-string">"^4.0.0-alpha.0"</span>,
    <span class="hljs-attr">"cross-env"</span>: <span class="hljs-string">"^7.0.3"</span>,
    <span class="hljs-attr">"css-loader"</span>: <span class="hljs-string">"^6.1.0"</span>,
    <span class="hljs-attr">"file-loader"</span>: <span class="hljs-string">"^6.2.0"</span>,
    <span class="hljs-attr">"html-webpack-plugin"</span>: <span class="hljs-string">"^5.3.2"</span>,
    <span class="hljs-attr">"less"</span>: <span class="hljs-string">"^4.1.1"</span>,
    <span class="hljs-attr">"less-loader"</span>: <span class="hljs-string">"^10.0.1"</span>,
    <span class="hljs-attr">"react"</span>: <span class="hljs-string">"^17.0.2"</span>,
    <span class="hljs-attr">"react-dom"</span>: <span class="hljs-string">"^17.0.2"</span>,
    <span class="hljs-attr">"style-loader"</span>: <span class="hljs-string">"^3.1.0"</span>,
    <span class="hljs-attr">"typescript"</span>: <span class="hljs-string">"^4.3.5"</span>,
    <span class="hljs-attr">"webpack"</span>: <span class="hljs-string">"^5.45.1"</span>,
    <span class="hljs-attr">"webpack-cli"</span>: <span class="hljs-string">"3.3.12"</span>,
    <span class="hljs-attr">"webpack-dev-server"</span>: <span class="hljs-string">"^3.11.2"</span>
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@types/react"</span>: <span class="hljs-string">"^17.0.14"</span>,
    <span class="hljs-attr">"@types/react-dom"</span>: <span class="hljs-string">"^17.0.9"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">配置 webpack</h4>
<p>新建 <code>script/webpack.config.js</code> 复制下述配置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">"./src/index.tsx"</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: path.resolve(__dirname, <span class="hljs-string">"dist"</span>),
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: path.resolve(<span class="hljs-string">'src'</span>)
    &#125;,
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.json'</span>]
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx|ts|tsx)$/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-built_in">require</span>.resolve(<span class="hljs-string">'babel-loader'</span>)
        &#125;,
        <span class="hljs-attr">exclude</span>: [<span class="hljs-regexp">/node_modules/</span>],
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(css|less)$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"style-loader"</span>,
          &#125;,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"css-loader"</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">importLoaders</span>: <span class="hljs-number">1</span>,
            &#125;,
          &#125;,
        ],
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif|jpeg)$/</span>,
        loader: <span class="hljs-string">'file-loader'</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(woff|woff2|eot|ttf|otf)$/</span>,
        loader: <span class="hljs-string">'file-loader'</span>
      &#125;
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'tpl/index.html'</span>
    &#125;),
  ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个需要注意的点是 <code>webpack-cli</code> 与 <code>webpack-dev-server</code> 的<strong>版本需要保持一致</strong>，都是用 3.0 的版本即可，如果版本不一致的话，会导致报错。</p>
<h4 data-id="heading-4">配置 React 相关</h4>
<p>新建 <code>tpl/index.html</code> 文件（html 模板），复制下述代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建 <code>src/index.tsx</code> 文件（入口文件），复制下述代码</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App"</span>;

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建 <code>.babelrc</code> 文件（babel 解析配置），复制下述代码</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"presets"</span>: [
    <span class="hljs-string">"@babel/preset-env"</span>,
    <span class="hljs-string">"@babel/preset-react"</span>,
    [
      <span class="hljs-string">"@babel/preset-typescript"</span>,
      &#123;
        <span class="hljs-attr">"isTSX"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">"allExtensions"</span>: <span class="hljs-literal">true</span>
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成上述一系列配置之后，同时安装完依赖之后，运行 yarn start，此时应该是能够正常运行项目如下图所示</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/035452c09ff044b6b2df757c3e664a20~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>浏览器打开 <code>http://localhost:8081/</code>，即可看到写出来的展示的页面</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f64ceae796e4453af069149bbe759aa~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，已经完成了一个初步的脚手架搭建，但是针对于业务来说，还是有很多的细节需要完善。接下来，我们一起针对平常开发需要使用到的模块对项目进行进一步的配置。</p>
<blockquote>
<p>篇幅所致，本文并不会对 Webpack、Babel、React 的配置项做过多的说明，仅仅提供一个完整实例，可以根据步骤完成一个基础框架的搭建，如果有同学想了解更多相关的细节，建议直接搭建完毕之后阅读文档，然后根据文档说明来配置自己想要的功能，多思考、多动手。</p>
</blockquote>
<h3 data-id="heading-5">优化 Webpck Dev 配置</h3>
<h4 data-id="heading-6">简化 server 信息输出</h4>
<p>前面的配图可以看出 <code>webpack-dev-server</code> 输出的信息很乱，可以使用 Stats 配置字段对输出信息进行过滤。</p>
<p>一般我们只需要看到 error 信息即可，可以添加如下参数：</p>
<pre><code class="hljs language-js copyable" lang="js">devServer: &#123;
    <span class="hljs-attr">stats</span>: <span class="hljs-string">'errors-only'</span>, <span class="hljs-comment">// 过滤信息输出</span>
    <span class="hljs-attr">contentBase</span>: path.resolve(__dirname, <span class="hljs-string">"dist"</span>),
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">添加构建信息输出</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/540b02ae93024b65bafbea9ec109fb0e~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ProgressPlugin 可以监控各个 hook 执行的进度 percentage，输出各个 hook 的名称和描述。</p>
<p>使用也非常简单，按照如下引用之后，就可以正常输出如图标红的构建进度。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; ProgressPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-attr">plugins</span>: [
    ...
    <span class="hljs-keyword">new</span> ProgressPlugin(),
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">优化业务模块</h3>
<p>先将项目目录划分好，约定好每个目录的文件的作用与功能。</p>
<p>这里的规范并不是一定的，具体要看各个团队自己的开发规范来定制，例如有的团队喜欢将公共的资源放在 <code>public</code> 目录等。</p>
<pre><code class="hljs language-js copyable" lang="js">├── dist/                          <span class="hljs-comment">// 默认的 build 输出目录</span>
└── src/                           <span class="hljs-comment">// 源码目录</span>
    ├── assets/                    <span class="hljs-comment">// 静态资源目录</span>
    ├── config                     
        ├── config.js              <span class="hljs-comment">// 项目内部业务相关基础配置</span>
    ├── components/                <span class="hljs-comment">// 公共组件目录</span>
    ├── service/                   <span class="hljs-comment">// 业务请求管理</span>
    ├── store/                     <span class="hljs-comment">// 共享 store 管理目录</span>
    ├── util/                      <span class="hljs-comment">// 工具函数目录</span>
    ├── pages/                     <span class="hljs-comment">// 页面目录</span>
    ├── router/                    <span class="hljs-comment">// 路由配置目录</span>
    ├── .index.tsx                 <span class="hljs-comment">// 依赖主入口</span>
└── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">配置路由</h4>
<p>收敛路由的好处是可以在一个路由配置文件查看到当前项目的一个大概情况，便于维护管理，当然也可以使用约定式路由，即读取 pages 下文件名，根据文件命名规则来自动生成路由。但这种约束性我感觉还是不太方便，个人还是习惯自己配置路由规则。</p>
<p>首先改造 <code>index.tsx</code> 入口文件，代码如下：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> &#123; HashRouter, Route, Switch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="hljs-keyword">import</span> routerConfig <span class="hljs-keyword">from</span> <span class="hljs-string">'./router/index'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./base.less'</span>

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">HashRouter</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
        &#123;
          routerConfig.routes.map((route) => &#123;
            return (
              <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;route.path&#125;</span> &#123;<span class="hljs-attr">...route</span>&#125; /></span>
            )
          &#125;)
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">HashRouter</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>router/index.ts 文件配置，代码如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> BlogsList <span class="hljs-keyword">from</span> <span class="hljs-string">'@/pages/blogs/index'</span>
<span class="hljs-keyword">import</span> BlogsDetail <span class="hljs-keyword">from</span> <span class="hljs-string">'@/pages/blogs/detail'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">routes</span>: [
    &#123; <span class="hljs-attr">exact</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: BlogsList &#125;,
    &#123; <span class="hljs-attr">exact</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">path</span>: <span class="hljs-string">'/blogs/detail/:article_id'</span>, <span class="hljs-attr">component</span>: BlogsDetail &#125;,
  ],
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">Service 管理</h4>
<p>跟收敛路由是一样的意思，收敛接口也可以统一修改、管理这些请求，如果有复用接口修改可以从源头处理。</p>
<p>所有项目请求都放入 service 目录，建议每个模块都有对应的文件管理，如下所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> information <span class="hljs-keyword">from</span> <span class="hljs-string">'./information'</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> base <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>

<span class="hljs-keyword">export</span> &#123;
  information,
  base
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样可以方便管理请求，base.ts 作为业务请求类，可以在这里处理一些业务特殊处理。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; request &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../until/request'</span>

<span class="hljs-keyword">const</span> prefix = <span class="hljs-string">'/api'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getAllInfoGzip = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> request(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;prefix&#125;</span>/apis/random`</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>util/request 作为统一引入的请求方法，可以自行替换成 fetch、axios 等请求库，同时可以在此方法内封装通用拦截逻辑。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;

<span class="hljs-keyword">interface</span> IRequest &#123;
    <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>
    params?: SVGForeignObjectElement
    query?: <span class="hljs-built_in">object</span>
    header?: <span class="hljs-built_in">object</span>
    method?: <span class="hljs-string">"POST"</span> | <span class="hljs-string">"OPTIONS"</span> | <span class="hljs-string">"GET"</span> | <span class="hljs-string">"HEAD"</span> | <span class="hljs-string">"PUT"</span> | <span class="hljs-string">"DELETE"</span> | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-keyword">interface</span> IResponse &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">errorMsg</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">classify</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">data</span>: <span class="hljs-built_in">any</span>
    detail?: <span class="hljs-built_in">any</span>
    img?: <span class="hljs-built_in">object</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> request = (&#123; url, params, query, header, method = <span class="hljs-string">'POST'</span> &#125;: IRequest): <span class="hljs-built_in">Promise</span><IResponse> => &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        axios(query ? <span class="hljs-string">`<span class="hljs-subst">$&#123;url&#125;</span>/?<span class="hljs-subst">$&#123;qs.stringify(query)&#125;</span>`</span> : url, &#123;
            <span class="hljs-attr">data</span>: params,
            <span class="hljs-attr">headers</span>: header,
            <span class="hljs-attr">method</span>: method,
        &#125;)
            .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                resolve(res.data)
            &#125;)
            .catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
                reject(error)
            &#125;)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体通用拦截，请参考 axios 配置，或者自己改写即可，需要符合自身的业务需求。</p>
<p>在具体业务开发使用的时候可以按照模块名引入，容易查找对应的接口模块。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; information &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@/service/index"</span>;

<span class="hljs-keyword">const</span> &#123; data &#125; = <span class="hljs-keyword">await</span> information.getAllInfoGzip(&#123; id &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这套规则同样可以适用于 store、router、utils 等可以拆开模块的地方，有利于项目维护。</p>
</blockquote>
<p>上述是针对项目做了一些业务开发上的配置与约定，各位同学可以根据自己团队中的规定与喜好行修改。</p>
<h2 data-id="heading-11">CLI 升级改造</h2>
<p>在上述自定义 React 脚手架搭建完毕之后，我们如果直接用使用上一篇搭建出来的 CLI 来构建项目是不会构建成功的，还有印象的同学，应该记得之前的 CLI 的入口文件是 <code>src/index.js</code>，html 模板使用的是 <code>public/index.html</code>。</p>
<p>很明显可以看出，此时的 CLI 是远远达不到要求的，我们并不能在每一次开发的时候都需要对 CLI 进行更新，这样是违背 CLI 的通用性原则。</p>
<p>那么该如何解决这个问题呢？</p>
<h3 data-id="heading-12">自定义配置文件</h3>
<p>根目录新建 <code>cli.config.json</code> 文件，此文件将是需要读取配置的文件。</p>
<p>将此项目的自义定配置写入文件，供给 CLI 读取。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"entry"</span>: &#123;
    <span class="hljs-attr">"app"</span>: <span class="hljs-string">"./src/index.tsx"</span>
  &#125;,
  <span class="hljs-attr">"output"</span>: &#123;
    <span class="hljs-attr">"filename"</span>: <span class="hljs-string">"build.js"</span>,
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./dist"</span>
  &#125;,
  <span class="hljs-attr">"template"</span>: <span class="hljs-string">"tpl/index.html"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CLI 同步进行改造，代码如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">require</span>(<span class="hljs-string">'module-alias/register'</span>)
<span class="hljs-keyword">import</span> webpack <span class="hljs-keyword">from</span> <span class="hljs-string">'webpack'</span>;
<span class="hljs-keyword">import</span> &#123; getCwdPath, loggerTiming, loggerError &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/util'</span>
<span class="hljs-keyword">import</span> &#123; loadFile &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/util/file'</span>
<span class="hljs-keyword">import</span> &#123; getProConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./webpack.pro.config'</span>
<span class="hljs-keyword">import</span> ora <span class="hljs-keyword">from</span> <span class="hljs-string">"ora"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> buildWebpack = <span class="hljs-function">() =></span> &#123;

  <span class="hljs-keyword">const</span> spinner = ora(<span class="hljs-string">'Webpack building...'</span>)

  <span class="hljs-keyword">const</span> rewriteConfig = loadFile(getCwdPath(<span class="hljs-string">'./cli.config.json'</span>)) <span class="hljs-comment">// 读取脚手架配置文件</span>

  <span class="hljs-keyword">const</span> compiler = webpack(getProConfig(rewriteConfig));

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    loggerTiming(<span class="hljs-string">'WEBPACK BUILD'</span>);
    spinner.start();
    compiler.run(<span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">any</span>, stats: <span class="hljs-built_in">any</span></span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(err)
      <span class="hljs-keyword">if</span> (err) &#123;
        <span class="hljs-keyword">if</span> (!err.message) &#123;
          spinner.fail(<span class="hljs-string">'WEBPACK BUILD FAILED!'</span>);
          loggerError(err);
          <span class="hljs-keyword">return</span> reject(err);
        &#125;
      &#125;
    &#125;);

    spinner.succeed(<span class="hljs-string">'WEBPACK BUILD Successful!'</span>);
    loggerTiming(<span class="hljs-string">'WEBPACK BUILD'</span>, <span class="hljs-literal">false</span>);
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>webpack.pro.config.ts</code> 代码如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> getBaseConfig <span class="hljs-keyword">from</span> <span class="hljs-string">'./webpack.base.config'</span>
<span class="hljs-keyword">import</span> &#123; getCwdPath, &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/util'</span>

<span class="hljs-keyword">interface</span> IWebpackConfig &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">app</span>: <span class="hljs-built_in">string</span>
  &#125;
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">path</span>: <span class="hljs-built_in">string</span>
  &#125;
  <span class="hljs-attr">template</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getProConfig = <span class="hljs-function">(<span class="hljs-params">config: IWebpackConfig</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">entry</span>: &#123; app &#125;, template, <span class="hljs-attr">output</span>: &#123; filename, path &#125;, ...rest &#125; = config

  <span class="hljs-keyword">return</span> &#123;
    ...getBaseConfig(&#123;
      <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
      <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">app</span>: getCwdPath(app || <span class="hljs-string">'./src/index.js'</span>)
      &#125;,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: filename || <span class="hljs-string">'build.js'</span>,
        <span class="hljs-attr">path</span>: getCwdPath(path || <span class="hljs-string">'./dist'</span>), <span class="hljs-comment">// 打包好之后的输出路径</span>
      &#125;,
      <span class="hljs-attr">template</span>: getCwdPath(template || <span class="hljs-string">'public/index.html'</span>)
    &#125;),
    ...rest
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>loadFile</code> 函数，读取脚手架自定义配置项，替换初始值，再进行项目构建，构建结果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7fbc58df3814a25906b6709c952f1c2~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这个自定义配置只是初步的，后期可以自定义添加更多的内容，例如自定义的 babel 插件、webpack 插件、公共路径、反向代理请求等等。</p>
</blockquote>
<h3 data-id="heading-13">接管 dev 流程</h3>
<p>与接管构建流程类似，在我们进行自定义脚手架构建之后，可以以此为基础将项目的 dev 流程也接管，避免项目因为开发与构建的依赖不同而导致构建失败，从源头管理项目的规范与质量。</p>
<p>在前面脚手架中配置的 webpack-dev-server 是基于 webpack-cli 来使用的。</p>
<p>既然使用 CLI 接管 dev 环境，那么也就不需要将 <code>webpack-dev-server</code> 作为 <code>webpack</code> 的插件使用，而是直接调用 <code>webpack-dev-server</code> 的 <code>Node Api</code>。</p>
<p>将刚刚的脚手架的 webpack-dev-server 配置抽离，相关配置放入 CLI 中。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> WebpackDevServer = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-dev-server/lib/Server'</span>)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> devWebpack = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> spinner = ora(<span class="hljs-string">'Webpack running dev ...'</span>)

  <span class="hljs-keyword">const</span> rewriteConfig = loadFile(getCwdPath(<span class="hljs-string">'./cli.config.json'</span>))
  <span class="hljs-keyword">const</span> webpackConfig = getDevConfig(rewriteConfig)

  <span class="hljs-keyword">const</span> compiler = webpack(webpackConfig);

  <span class="hljs-keyword">const</span> devServerOptions = &#123;
    <span class="hljs-attr">contentBase</span>: <span class="hljs-string">'dist'</span>,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>
  &#125;;
  
  <span class="hljs-keyword">const</span> server = <span class="hljs-keyword">new</span> WebpackDevServer(compiler, devServerOptions);

  server.listen(<span class="hljs-number">8000</span>, <span class="hljs-string">'127.0.0.1'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Starting server on http://localhost:8000'</span>);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在脚手架的 package.json scripts 添加对应的命令就可以完成对 dev 环境的接管，命令如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
     <span class="hljs-string">"dev"</span>: <span class="hljs-string">"cross-env NODE_ENV=development fe-cli webpack"</span>,
     <span class="hljs-string">"build"</span>: <span class="hljs-string">"cross-env NODE_ENV=production fe-cli webpack"</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行对应的命令即可运行或者打包当前脚手架内容。</p>
<h3 data-id="heading-14">优化 webpack 构建配置</h3>
<p>上一篇就已经介绍过了，目前的构建产物结果很明显并不是我们想要的，也不符合普通的项目规范，所以需要将构建的配置再优化一下。</p>
<h4 data-id="heading-15">mini-css-extract-plugin</h4>
<p><code>mini-css-extract-plugin</code> 是一款样式抽离插件，可以将 css 单独抽离，单独打包成一个文件，它为每个包含 css 的 js 文件都创建一个 css 文件。也支持 css 和 sourceMaps 的按需加载。配置代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">rules</span>: [
        test: <span class="hljs-regexp">/\.(css|less)$/</span>,
            use: [MiniCssExtractPlugin.loader],
          &#125;
    ]
&#125;
  
<span class="hljs-attr">plugins</span>: [
      <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[contenthash].css'</span>,
        <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'[id].[contenthash].css'</span>,
        <span class="hljs-attr">ignoreOrder</span>: <span class="hljs-literal">true</span>,
      &#125;)
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">提取公共模块</h4>
<p>我们可以使用 webpack 提供的 <code>splitChunks</code> 功能，提取 <code>node_modules</code> 的公共模块出来，在 webpack 配置项中添加如下配置即可。</p>
<pre><code class="hljs language-js copyable" lang="js"> optimization: &#123;
      <span class="hljs-attr">splitChunks</span>: &#123;
        <span class="hljs-attr">cacheGroups</span>: &#123;
          <span class="hljs-attr">commons</span>: &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>,
            name: <span class="hljs-string">'vendors'</span>,
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
          &#125;,
        &#125;,
      &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e7b76708dc84b958fb1f5e787521537~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图，现在构建出来的产物是不是瞬间清晰多了。</p>
<h4 data-id="heading-17">优化构建产物路径</h4>
<p>上述的构建产物虽然已经优化过了，但是目录依然还不够清晰，我们可以对比下图的 cra 构建产物，然后进行引用路径的优化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7ead23ea1c941d79ee57b8a6634f87a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实很简单，将所有构建产物的路径前面统一添加 <code>static/js</code>，这样在进行构建得到的产物就如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91399fc924a645ef98cc6317da4e014b~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">配置增量构建（持久化缓存）</h4>
<p>这是 webpack 5 的新特性，在 webpack 4 的时候，我们常用优化构建的手段是使用 <code>hard-source-webpack-plugin</code> 这个插件将<strong>模块依赖</strong>缓存起来，再第二次构建的时候会直接读取缓存，加快构建速度。</p>
<p>这个过程在 webpack 5 里面被 cache 替代了，官方直接内置了持久化缓存的功能，配置起来也非常方便，添加如下代码即可：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; getCwdPath &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/util'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">cache</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'filesystem'</span>,  <span class="hljs-comment">//  'memory' | 'filesystem'</span>
    <span class="hljs-attr">cacheDirectory</span>: getCwdPath(<span class="hljs-string">'./temp_cache'</span>), <span class="hljs-comment">// 默认将缓存存储在 当前运行路径/.cache/webpack</span>
    <span class="hljs-comment">// 缓存依赖，当缓存依赖修改时，缓存失效</span>
    <span class="hljs-attr">buildDependencies</span>: &#123;
      <span class="hljs-comment">// 将你的配置添加依赖，更改配置时，使得缓存失效</span>
      <span class="hljs-attr">config</span>: [__filename]
    &#125;,
    <span class="hljs-attr">allowCollectingMemory</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">profile</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在运行构建或者开发的时候，会在当前运行目录生产缓存文件如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ddaabc27473412daecc11b9d3ffdf80~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在让我们一起来看看，构建速度的提升有多少：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3cae97c787b4dd7bc5a9f338e27f110~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以很明显看出，第一构建速度比之前要慢 2s 左右，但是第二次构建速度明显提升，毕竟脚手架目前的内容太少了，初次构建使用增量的时候会比普通编译多了存储缓存的过程。</p>
<p>这里有个需要注意的点，因为我们是调用 webpack 的 Node Api 来构建，所以需要显示关闭 compiler 才能正常生产缓存文件。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> compiler = webpack(webpackConfig);

  <span class="hljs-keyword">try</span> &#123;
    compiler.run(<span class="hljs-function">(<span class="hljs-params">err: <span class="hljs-built_in">any</span>, stats: <span class="hljs-built_in">any</span></span>) =></span> &#123;

      <span class="hljs-keyword">if</span> (err) &#123;
        loggerError(err);
      &#125; <span class="hljs-keyword">else</span> &#123;
        loggerSuccess(<span class="hljs-string">'WEBPACK SUCCESS!'</span>);
      &#125;
      compiler.close(<span class="hljs-function">() =></span> &#123;
        loggerInfo(<span class="hljs-string">'WEBPACK GENERATE CACHE'</span>); <span class="hljs-comment">// 显示调用 compiler 关闭，生成缓存</span>
      &#125;);
      loggerTiming(<span class="hljs-string">'WEBPACK BUILD'</span>, <span class="hljs-literal">false</span>);
    &#125;);
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    loggerError(error)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>有兴趣的同学可以试试 dev 环境，启动速度一样会缩短到秒开级别。</p>
</blockquote>
<h2 data-id="heading-19">特别鸣谢</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa0737df6fdc4e4fb524ca5ec252c7ce~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是上一篇的读者留言，此处<a href="https://juejin.cn/user/2928754705303415/posts" target="_blank" title="https://juejin.cn/user/2928754705303415/posts">@琦玉</a>，感谢这位同学的建议，后面的系列博文除了介绍思路之外，coding 与步骤会更加详细，也会及时提供项目 demo 供给参考，其他同学更好的建议也可以在评论区反馈。希望除了能将这个系列写完之外，还能写得更好，让我能和更多的同学一起互相学习、共同成长。</p>
<h2 data-id="heading-20">写在最后</h2>
<p>CLI 工具到此为止，总算是有个大概可用的雏形了，但是作为企业级的 CLI 目标，我们还差很长的一段路要走，仅仅构建这块能优化的点就非常多，包括但不限于构建配置的约束、拓展、提交约束等等细节性的优化。</p>
<p>所有的项目代码已经上传至<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fboty-design%2Ffe-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/boty-design/fe-cli" ref="nofollow noopener noreferrer">项目地址</a>，有兴趣的同学可以拉取参考，后续所有专栏的相关的代码都会统一放在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fboty-design" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/boty-design" ref="nofollow noopener noreferrer">BOTY DESIGN</a> 中。</p></div>  
</div>
            