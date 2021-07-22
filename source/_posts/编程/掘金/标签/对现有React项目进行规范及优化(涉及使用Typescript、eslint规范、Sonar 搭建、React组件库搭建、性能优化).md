
---
title: '对现有React项目进行规范及优化(涉及使用Typescript、eslint规范、Sonar 搭建、React组件库搭建、性能优化)'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cdf8a440c834c6493355056165312f7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:49:47 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cdf8a440c834c6493355056165312f7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近项目组不是很忙，也为了实践自己学习的知识，进行吸收优化，决定对项目组现有项目进行规范优化，也是对项目代码的负责，在此做个记录。</p>
<h1 data-id="heading-0">概论</h1>
<p>此文章记录的是基于线上项目代码的规范优化升级，也是自己对经手项目的代码的补救，针对所要优化的项目，涉及以下几点知识点：</p>
<ul>
<li>使用Typescript开发（都说ts很香，也看过一些相关文档，但一直没有结合具体项目去实践，确实体验不到他是怎么个香）</li>
<li>eslint（确实是我的责任，在项目初期，因为报错的eslint规范太多，很烦，就把eslint规范关了，现在想想，这不仅仅是对项目的不负责，也是对自己的不负责，对团队的不负责，对未来接受的猿们的不负责，所以，即使现在使用很痛苦，也一定要把这个规范建立起来）</li>
<li>编码规范及规范的文档说明、相关配置文件的文档说明</li>
<li>单元测试（核心业务模块）</li>
<li>Sentry报错收集平台接入（开源的 Sentry 平台）</li>
<li>Sonar 搭建（不管是对项目负责、还是为了团队成长，项目代码交付也好、自己的代码质量规范也好，确实需要一个代码质量分析工具，于是选择了sonarqube）</li>
<li>搭建前端公共组件库（一直以来，我们的项目针对本来可以复用的组件跟业务边界切割不清、可以复用的组件没有根据组件的功能分类清晰、在工程实践即项目工程目录构建中，没有清晰安排构建，这些等等的问题，早就在我心目中所嫌弃与诟病，但一直没有时间去重新规划整理，趁着这段闲暇时间，也趁着自己在这段提升时间段，把这块自己一直嫌弃的模块去重新规划与规范化）</li>
<li>对于高阶组件的使用（规范化与合理化，例如使用装饰器的写法、根据业务合理使用高阶组件）</li>
<li>针对渲染异常（组件渲染异常的处理）的“错误边界”的相关内容在项目中的应用（如果渲染异常，在没有任何降级保护措施的情况下，页面会直接显示白屏。在组件内部可以使用getDerivedStateFromError 与 componentDidCatch 两个函数，还有基于整体性考量，针对错误边界的预防与兜底）</li>
<li>使用mockjs</li>
<li>性能优化方向在项目中的实践</li>
</ul>
<p>以上几点相关知识点，就是我要针对我们项目的优化点，本文章会持续书写，毕竟项目会一直持续优化。
下图是我整个项目规范化与优化下来的大概实行步骤，如下：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cdf8a440c834c6493355056165312f7~tplv-k3u1fbpfcp-watermark.image" alt="未命名文件.png" loading="lazy" referrerpolicy="no-referrer">
废话少说，接下来开始表演：</p>
<h1 data-id="heading-1">一. 项目中引入Typescript</h1>
<p>引入Typescript借鉴相关文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6844904102355271694#heading-16" target="_blank" title="https://juejin.cn/post/6844904102355271694#heading-16">【开源】一个 React + TS 项目模板</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.tslang.cn%2Fdocs%2Fhandbook%2Ftypescript-in-5-minutes.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.tslang.cn/docs/handbook/typescript-in-5-minutes.html" ref="nofollow noopener noreferrer">5分钟上手TypeScript</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzr15829039341%2Farticle%2Fdetails%2F102844315" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zr15829039341/article/details/102844315" ref="nofollow noopener noreferrer">React项目 加入 TS</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F88615706" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/88615706" ref="nofollow noopener noreferrer">在React中使用TypeScript</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F102250469" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/102250469" ref="nofollow noopener noreferrer">Babel 7 下配置 TypeScript 支持</a></li>
<li>更多TS转译方案请看<a href="https://juejin.cn/post/6844904052094926855#heading-5" target="_blank" title="https://juejin.cn/post/6844904052094926855#heading-5">Webpack 转译 Typescript 现有方案</a></li>
</ul>
<h2 data-id="heading-2">1. 全局安装ts</h2>
<p>安装命令如下：</p>
<pre><code class="copyable">npm i -g typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2. 创建tsconfig.json</h2>
<p>命令如下：</p>
<pre><code class="copyable">tsc --init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0ee27d80bfc4b46928f61c9384419a4~tplv-k3u1fbpfcp-watermark.image" alt="1625710508(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>tsconfig.json的配置参数如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6e024b6a9a84004a229fe98c9a806aa~tplv-k3u1fbpfcp-watermark.image" alt="ULOT&#125;U$3UN9QZG6GGH9X@1A.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">3. 安装开发环境依赖</h2>
<h3 data-id="heading-5">1.  比较旧的开发环境</h3>
<h4 data-id="heading-6">1. 依赖如下：</h4>
<pre><code class="copyable">npm install --save-dev typescript @types/react @types/react-dom @types/react-router-dom ts-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2. webpack配置文件示例如下：</h4>
<pre><code class="copyable">module.exports = &#123;
    context: ...,
    entry: ...,
    output: ...,

    // 添加resolve
    resolve: &#123;
        extensions: ['.ts', '.tsx', '.js']
    &#125;,

    module: &#123;
        loaders: [

            // 增加新的loader
            &#123;
                test: /\.tsx?$/,
                loaders: ['babel-loader', 'ts-loader']
            &#125;,
            ...
        ]
    &#125;,
    plugins: ...
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目时发现会报如下错误：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913f2fd3520940948649b62718b3059a~tplv-k3u1fbpfcp-watermark.image" alt="1625750688(1).png" loading="lazy" referrerpolicy="no-referrer">
安装的相关依赖的版本如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c057feb483942f7987b5cef947b6a82~tplv-k3u1fbpfcp-watermark.image" alt="1625751055(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/334d2c912e7840bf90bc80507a0390bb~tplv-k3u1fbpfcp-watermark.image" alt="1625751002(1).png" loading="lazy" referrerpolicy="no-referrer">
推测是由于ts-loader的版本过高导致的这个报错，由于不使用ts-loader方案，所以没有继续探究。</p>
<h3 data-id="heading-8">2. 新的开发环境</h3>
<h4 data-id="heading-9">1. 依赖如下：</h4>
<pre><code class="copyable">npm install --save-dev typescript @types/react @types/react-dom @babel/preset-typescript @babel/plugin-proposal-class-properties @babel/plugin-proposal-object-rest-spread
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">2. package.json的项设置如下：</h4>
<pre><code class="copyable">&#123;
  "name": "inforserver",
  "version": "1.0.0",
  "description": "信息服务平台",
  "main": "index.js",
  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "webpack-dev-server --config ./config/webpack.dev.config.js --host 0.0.0.0",
    "build": "webpack -p --config ./config/webpack.prod.config.js"
  &#125;,
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": &#123;
    "antd": "^3.22.2",
    "axios": "^0.19.0",
    "crypto-js": "^4.0.0",
    "echarts": "4.9.0",
    "happypack": "^5.0.1",
    "hard-source-webpack-plugin": "^0.13.1",
    "immutable": "^4.0.0-rc.12",
    "js-cookie": "^2.2.1",
    "moment": "^2.24.0",
    "prop-types": "latest",
    "qs": "^6.8.0",
    "react": "^16.9.0",
    "react-cookies": "^0.1.1",
    "react-dom": "^16.9.0",
    "react-loadable": "^5.5.0",
    "react-redux": "^7.1.1",
    "react-router": "^5.0.1",
    "react-router-dom": "^5.0.1",
    "redux": "^4.0.4",
    "redux-persist": "^6.0.0",
    "redux-persist-transform-immutable": "^5.0.0",
    "redux-thunk": "^2.3.0"
  &#125;,
  "devDependencies": &#123;
    "@babel/core": "^7.14.6",
    "@babel/plugin-proposal-class-properties": "^7.14.5",
    "@babel/plugin-proposal-object-rest-spread": "^7.14.7",
    "@babel/plugin-syntax-dynamic-import": "^7.8.3",
    "@babel/plugin-transform-runtime": "^7.14.5",
    "@babel/preset-env": "^7.5.5",
    "@babel/preset-react": "^7.0.0",
    "@babel/preset-typescript": "^7.14.5",
    "@svgr/webpack": "^5.3.1",
    "@types/react": "16.9.23",
    "@types/react-dom": "16.9.7",
    "@types/react-router-dom": "5.1.3",
    "babel-loader": "^8.0.6",
    "babel-plugin-import": "^1.13.3",
    "babel-polyfill": "^6.26.0",
    "clean-webpack-plugin": "^3.0.0",
    "copy-webpack-plugin": "^6.0.2",
    "css-loader": "^3.2.0",
    "file-loader": "^4.2.0",
    "html-webpack-plugin": "^3.2.0",
    "less": "^3.10.3",
    "less-loader": "^5.0.0",
    "mini-css-extract-plugin": "^0.8.0",
    "node-sass": "^4.12.0",
    "react-countup": "^4.3.3",
    "sass-loader": "^8.0.0",
    "style-loader": "^1.0.0",
    "terser-webpack-plugin": "^4.2.0",
    "typescript": "^4.3.5",
    "uglifycss-loader": "^1.0.2",
    "url-loader": "^3.0.0",
    "webpack": "^4.39.3",
    "webpack-cli": "^3.3.7",
    "webpack-dev-server": "^3.8.0",
    "webpack-merge": "^4.2.2",
    "webpack-theme-color-replacer": "^1.3.7"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中：</p>
<p>基于Babel 7 下配置 TypeScript 支持，使用 @babel/preset-typescript 和 @babel/preset-env 配置TypeScript的编译环境，安装 Babel 基础如下：</p>
<p>有 5 个包需要下载安装，它们分别是：</p>
<ul>
<li>@babel/core</li>
<li>@babel/preset-env</li>
<li>@babel/preset-typescript</li>
<li>@babel/plugin-proposal-class-properties</li>
<li>@babel/plugin-proposal-object-rest-spread</li>
</ul>
<p>其中包含了 2 个插件 plugin-proposal-class-properties 和 plugin-proposal-object-rest-spread，分别用于转换语法特性“类属性”、“对象展开”。</p>
<ol start="3">
<li>配置 babel</li>
</ol>
<p><strong>注意</strong>：我们的项目没有创建文件 .babelrc</p>
<p>配置内容如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb499a56d18f4af98c4960441a9bb41a~tplv-k3u1fbpfcp-watermark.image" alt="1625755077(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们项目是使用HappyPack插件提升webpack构建时间的，所以webpack配置文件的具体内容如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b84fd069b96941fbafd6ca974f81a598~tplv-k3u1fbpfcp-watermark.image" alt="1625755906(1).png" loading="lazy" referrerpolicy="no-referrer">
HappyPack内的配置内容如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b731cd70a79648f0b1671b8f3ec0696d~tplv-k3u1fbpfcp-watermark.image" alt="1625755077(1).png" loading="lazy" referrerpolicy="no-referrer">
<strong>注意</strong>：完成后运行项目Typescript如果报如下错误：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efbe456996774a3792d7a1be6dcef851~tplv-k3u1fbpfcp-watermark.image" alt="1625729793(1).png" loading="lazy" referrerpolicy="no-referrer">
即报如下错误：</p>
<pre><code class="copyable">Typescript error “Cannot write file xxx because it would overwrite input file
<span class="copy-code-btn">复制代码</span></code></pre>
<p>出现这个问题基本是因为开启了allowJs。</p>
<ul>
<li>因为allowJs即允许Typescript编译器去编译js。而编译之后的输出文件也就是xxx.js与源文件是一样的。</li>
<li>所以就会报出“会覆盖输入文件”这样的错误。</li>
</ul>
<p>解决思路如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dee0ae96bba41f69804e9dfc5efeaed~tplv-k3u1fbpfcp-watermark.image" alt="11432478-e4fd00419e43a760.png" loading="lazy" referrerpolicy="no-referrer">
我是设定outDir参数，指向相关位置。</p>
<h1 data-id="heading-11">二. ESLint+Prettier统一代码风格</h1>
<h2 data-id="heading-12">1. 背景</h2>
<p>在一个多人协作的项目中，不同的开发人员写的代码的风格不太一样，比如是否需要在行末加分号，换行、空格、缩紧、项目中散落的console处理方法、单行代码最大长度等等，如果项目中没有统一的规范就会导致代码风格的五花八门，不利于代码的阅读和维护。</p>
<p>为了项目中有统一的编码规范，我们使用eslint + prettier 来进行约束。</p>
<ul>
<li>使用 eslint + prettier添加统一代码规范</li>
<li>格式化现有项目下的不符合规范的文件</li>
<li>配置编辑器，自动检测新增或修改的代码的规范合法性</li>
</ul>
<h2 data-id="heading-13">2. 配置相关配置依赖环境及配置文件</h2>
<h3 data-id="heading-14">1. 安装eslint</h3>
<p>ESLint 主要有以下特点：</p>
<ul>
<li>默认规则包含所有 JSLint、JSHint 中存在的规则，易迁移；</li>
<li>规则可配置性高：可设置「警告」(warning)、「错误」(error)两个 error 等级，或者直接禁用；</li>
<li>包含代码风格检测的规则（可以丢掉 JSCS 了）；</li>
<li>支持插件扩展、自定义规则。</li>
</ul>
<p>ESLint配置方式，可以通过以下三种方式配置 ESLint:</p>
<ul>
<li>使用 .eslintrc 文件（支持 JSON 和 YAML 两种语法）；</li>
<li>在 package.json 中添加 eslintConfig 配置块；</li>
<li>直接在代码文件中定义。</li>
</ul>
<p>我们选择使用 .eslintrc 文件方式！！！</p>
<p><strong>规则的严重性(rule severity)</strong></p>
<ul>
<li>"off"</li>
<li>or 0 - turn the rule off 不验证 "warn"</li>
<li>or 1 - turn the rule on as a warning(doesn’ t affect exit code) 警告 "error"</li>
<li>or 2 - turn the rule on as an error(exit code is 1 when triggered) 错误（ 如有） 规则的选项(additional options)  "quotes": [2, "double"]</li>
</ul>
<h4 data-id="heading-15">1. 安装依赖如下：</h4>
<pre><code class="copyable">npm i -D eslint babel-eslint eslint-plugin-import eslint-plugin-jsx-a11y eslint-plugin-react @typescript-eslint/parser @typescript-eslint/eslint-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，相关插件如下：</p>
<ul>
<li>eslint-plugin-jsx-a11y：检验jsx语法</li>
<li>eslint-plugin-react：设定react组件的相关规范</li>
<li>eslint-plugin-import：在使用 import 的时候，一些 rules 规范</li>
<li>@typescript-eslint/parser：eslint 默认使用 <code>Espree</code> 进行解析，无法识别 ts 的一些语法，所以需要安装一个 ts 的解析器 <code>@typescript-eslint/parser</code>，用它来代替默认的解析器</li>
<li>@typescript-eslint/eslint-plugin：来提供有关 ts 的规则补充</li>
</ul>
<h4 data-id="heading-16">2. 添加.eslintrc配置文件</h4>
<p>配置文件内容如下：</p>
<pre><code class="copyable">&#123;
  //  ESLint默认使用Espree作为其解析器
  //  此项是用来指定eslint解析器的，解析器必须符合规则
  //  官网没有对其他解析器进行说明，但是有提示，使用其他解析器的时候，注意确认它是不是和 ESLint 兼容。
  //  至于咋确认。。你指定一下这个解析器，看看 eslint 会不会对你想检查的代码正常报错，就行了。
  // 以下解析器与 ESLint 兼容：
  //  1、Esprima
  //  2、Babel-ESLint：一个对Babel解析器的包装，使其能够与 ESLint 兼容（如果你想使用一些 先进的语法，比如es6789...）。
  //  3、@typescript-eslint/parser：将 TypeScript 转换成与 estree 兼容的形式，以便在ESLint中使用（如果你想使用typescript）。
  "parser": "@typescript-eslint/parser",
  //  解析器选项，与parser同时使用
  //  在使用自定义解析器时，
  //  为了让 ESLint 在处理非 ECMAScript 5 特性时正常工作，
  //  配置属性 parserOptions 仍然是必须的
  //  解析器会被传入parserOptions，
  //  但是不一定会使用它们来决定功能特性的开关。
  "parserOptions": &#123;
    // 默认是 script。模块化的代码要写：module（当前最常见做法，如果你的代码是 ECMAScript 模块）
    "sourceType": "module",
    //emcaVersion用来指定你想要使用的 ECMAScript 版本
    //注意，使用对于 ES6 语法，使用"ecmaVersion": 6时，不自动启用es6全局变量
    //自动启用es6语法和全局变量，需要搭配env使用"env": &#123; "es6": true &#125;
    "ecmaVersion": 6,
    //想使用额外的语言特性，一个配置对象，可配置项如下（value 均为 true/false）
    "ecmaFeatures": &#123;
      "jsx": true,//启用jsx
      "globalReturn":true, //在全局作用域下使用return语句
      "impliedStrict":true, //启用全局strict mode (如果 ecmaVersion 是 5 或更高)
      "experimentalObjectRestSpread": false //启用实验性的object rest/spread properties支持(不建议开启)
    &#125;
  &#125;,
  //  要在配置文件中指定环境，请使用env键并通过将每个设置为来指定要启用的环境true。
  "env": &#123;
    "browser": true, //开启浏览器全局变量
    "es6": true, //启用除模块以外的所有ECMAScript 6功能（这会自动将ecmaVersion解析器选项设置为6）
    "node": true //Node.js全局变量和Node.js作用域
  &#125;,
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "plugins": [
    "react",
    "@typescript-eslint"
  ],
  "rules": &#123;
    "semi": 0, // 行末分号，根据编码习惯选择添加，这里配置的不加分号
    "no-console": 0,
    "comma-dangle": [2,"always-multiline"],
    "max-len": 0,
    "space-before-function-paren": [0,"always"],
    "no-unused-expressions": [
      0,
      &#123;
        "allowShortCircuit": true,
        "allowTernary": true
      &#125;
    ],
    "arrow-body-style": [0, "never"],
    "func-names": 0,
    "prefer-const": 0,
    "no-extend-native": 0,
    "no-param-reassign": 0,
    "no-restricted-syntax": 0,
    "no-eval": 0,
    "no-continue": 0,
    "no-unused-vars": [
      0,
      &#123;
        "ignoreRestSiblings": true
      &#125;
    ],
    "no-underscore-dangle": 0,
    "global-require": 0,
    "import/no-extraneous-dependencies": 0,
    "import/prefer-default-export": 0,
    "import/no-unresolved": 0,
    "import/extensions": 0,
    // react
    "react/jsx-first-prop-new-line": 0,
    "react/jsx-filename-extension": 0,
    "react/jsx-no-bind": 0,
    "react/no-array-index-key": 0,
    "react/require-default-props": 0,
    "react/forbid-prop-types": 0,
    "react/no-string-refs": 0,
    "react/no-find-dom-node": 0,
    "react/no-danger": 0,
    "react/prop-types": 0,
    "react/display-name": 0,
    "react/no-deprecated": 0,
    "react/no-direct-mutation-state": 0,
    "jsx-a11y/href-no-hash": 0,
    "jsx-a11y/no-static-element-interactions": 0
  &#125;,
  "settings": &#123;
    "import/resolver": "node"
  &#125;
&#125;

//环境定义了预定义的全局变量。可用环境为：
//browser -浏览器全局变量。
//node -Node.js全局变量和Node.js作用域。
//commonjs -CommonJS全局变量和CommonJS作用域（将其用于使用Browserify / WebPack的仅浏览器代码）。
//shared-node-browser -Node.js和浏览器通用的全局变量。
//es6-启用除模块以外的所有ECMAScript 6功能（这会自动将ecmaVersion解析器选项设置为6）。
//es2017-添加所有ECMAScript 2017全局变量并自动将ecmaVersion解析器选项设置为8。
//es2020-添加所有ECMAScript 2020全局变量并将ecmaVersion解析器选项自动设置为11。
//worker -网络工作者的全局变量。
//amd- 根据amd规范定义require()和define()作为全局变量。
//mocha -添加所有Mocha测试全局变量。
//jasmine -添加了版本1.3和2.0的所有Jasmine测试全局变量。
//jest -开玩笑的全局变量。
//phantomjs -PhantomJS全局变量。
//protractor -量角器全局变量。
//qunit -QUnit全局变量。
//jquery -jQuery全局变量。
//prototypejs -Prototype.js全局变量。
//shelljs -ShellJS全局变量。
//meteor -流星全局变量。
//mongo -MongoDB全局变量。
//applescript -AppleScript全局变量。
//nashorn -Java 8 Nashorn全局变量。
//serviceworker -服务人员全局变量。
//atomtest -Atom测试助手全局变量。
//embertest -灰烬测试助手全局变量。
//webextensions -WebExtensions全局变量。
//greasemonkey -GreaseMonkey全球。
//这些环境不是互斥的，因此您一次可以定义多个环境。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">3. 在package.json中添加脚本</h4>
<p>脚本内容如下：</p>
<pre><code class="copyable">&#123;
  scripts: &#123;
    "lint-fix": "eslint --fix .js src"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行这个命令，这个命令会检测src目录下的所有的js文件。</li>
<li>如果发现在src目录下有不需要检测的文件夹，比如vendors文件夹下有三方开源的代码，不需要做格式的校验，可以通过配置下.eslintignore，忽略此文件夹目录。</li>
<li>执行完lint-fix命令后，eslint会根据配置文件标注出不符合规范的地方，并且自动添加一些修改，比如去掉行末添加分号。</li>
<li>但是对于一些其它的代码格式的设置，比如缩进是使用空格还是tab，大括号是否要添加空格等等，而这些正是prettier插件擅长做的。</li>
</ul>
<p>注意：我上面scripts脚本写的有问题，如果按照上面写，执行后，会出现如下报错：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/082b7e8f64514a4d8c7ce454f2b90f24~tplv-k3u1fbpfcp-watermark.image" alt="111.png" loading="lazy" referrerpolicy="no-referrer">
所以脚本内容改为如下：</p>
<pre><code class="copyable">&#123;
  scripts: &#123;
    "lint-fix": "eslint --fix --ext .js --ext .tsx src"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在要检测的文件格式前加 <code>--ext</code>
但执行该脚本又会报如下错误：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/228bb453a1be43009fe45d41720a3c33~tplv-k3u1fbpfcp-watermark.image" alt="PT`O_N(7NPJ02(866V~TP.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>尝试把eslint相关的依赖都卸载，还是报这个错误，怀疑是<code>.eslintrc配置文件</code>配置有问题，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24ca0b420ca44a52bc4a6e035c531df4~tplv-k3u1fbpfcp-watermark.image" alt="23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>把内容改成如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b025be6837cd44e2bf178838f5c8dd1e~tplv-k3u1fbpfcp-watermark.image" alt="33.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以是配置书写错误，不应该像错误方式书写。</p>
<h3 data-id="heading-18">2. Prettier是什么？</h3>
<p>Prettier是一个能够完全统一团队代码风格的利器，支持jsx、css</p></div>  
</div>
            