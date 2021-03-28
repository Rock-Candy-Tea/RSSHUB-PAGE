
---
title: 'Node.js学习（一）——简介'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6327c1f5c72456584d8bbea98cd96c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 00:30:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6327c1f5c72456584d8bbea98cd96c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Node.js是一个基于chrome V8引擎的JavaScript运行环境</h3>
<p>node.js不是语言，不是服务器，不是数据库。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6327c1f5c72456584d8bbea98cd96c6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h3 data-id="heading-1">优点</h3>
<p>1)异步非阻塞的I/O (I/O线程池)：</p>
<p>        异步非阻塞是能不能在做一件是的时候不影响其他人，异步肯定非阻塞</p>
<p>        I:input        O：output         文件的读写，数据库的读写叫做I/O</p>
<p>2)特别适用于 I/O密集型应用。</p>
<p>3)事件循环机制。</p>
<p>4)单线程。</p>
<p>5)跨平台：一处编写，随处可用。  Windows上写的代码，放在Linux上也可用。</p>
<p> </p>
<h3 data-id="heading-2">不足之处</h3>
<ul>
<li>1) 问调函数嵌套太多、太深(俗称回调地狱)</li>
<li>2) 单线程,处理不好CPU密集型任务。</li>
<li>3）不支持多核处理器</li>
</ul>
<p>Java服务器对CPU密集型友好，对I/O密集型友好。</p>
<p> </p>
<h3 data-id="heading-3">Node.js的应用场景</h3>
<ul>
<li>web服务API</li>
<li>服务器渲染页面，提升速度</li>
<li>后端的web服务，例如跨域，服务器端的请求</li>
</ul>
<p> </p>
<h3 data-id="heading-4">Node中任意一个模块（js文件）都被一个外层文件函数所包裹</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.callee.toString())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>function (exports, require, module, __filename, __dirname) &#123;</p>
<p>console.log(arguments.callee.toString())</p>
<p>exports：用于暴露模块</p>
<p>require：用于引入模块</p>
<p>module：用于暴露模块</p>
<p>__filename：这个文件所在的绝对路径</p>
<p>__dirname：当前文件所在的文件夹的绝对路径<br>
&#125;</p>
<p><strong>为什么要有这个外层函数（这个外层函数有什么作用）</strong></p>
<ol>
<li>隐藏内部实现</li>
<li>支持CommonJS的模块化</li>
</ol>
<p> </p>
<p><strong>对于浏览器端而言，js由哪几部分组?</strong></p>
<p>      1.BOM浏览器对象模型-------很多的API (location, history)</p>
<p>2.DOM文档对象模型........很多的API (对DOM的增删改查)</p>
<p>3.ES规范-------------- ES6. ES5.....</p>
<p> </p>
<p><strong>Node端js由几部分组成?</strong></p>
<p>1.没有了BOM ----因为服务器不需要 (服务端没有海览器对象)</p>
<p>2.没有了DON ----因为没有浏览器窗口</p>
<p>3.几乎包含了所有ES规范，没有alert</p>
<p>4.没有了window，但是取而代之的是一个叫global的全局变量。<br>
</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6d94f357f34443aa789465b278964f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h2 data-id="heading-5">包和包管理器</h2>
<p> </p>
<h3 data-id="heading-6">package包</h3>
<p>Nodejs的包基本遵循CommonuS规范，包将一组 相关的模块组合在一起，形成一组完整的工具。<br>
包由包结构和包描述文件两个部分组成。</p>
<ul>
<li>1)包结构: 用于组织包中的各种文件。</li>
<li>2)包描述文件: 描述包的相关信息，以供外部读取分析。</li>
</ul>
<p> </p>
<h3 data-id="heading-7">什么是包</h3>
<p>我们电脑上的文件夹，包含了某些特定的文件，符合了某些特定的结构，就是一个包。</p>
<p> </p>
<h3 data-id="heading-8">一个标准的包应该包含哪些内容</h3>
<ol>
<li>package.json——描述文件（包的说明书，必须要有！！！）</li>
<li>bin——可执行二进制文件</li>
<li>lib——经过编译后的js代码</li>
<li>doc——文档（说明文档、bug修复文档、版本变更记录文档）</li>
<li>test——一些测试报告</li>
</ol>
<p> </p>
<h3 data-id="heading-9">如何让一个普通文件变成包</h3>
<p>让这个文件夹拥有一个：package.json文件即可，且package.json里面的内容要合法。</p>
<p>执行命令：npm init</p>
<p>包名的要求：不能有中文，不能有大写字母，不能与npm仓库上其他包同名</p>
<p> </p>
<h3 data-id="heading-10">npm与node的关系</h3>
<p><strong>npm 是 JavaScript 世界的包管理工具,并且是 Node.js 平台的默认包管理工具，也是世界上最大的软件注册表</strong></p>
<p><strong>现在很多人是为了使用npm才去安装node</strong></p>
<p>pnm官网：www.npmjs.com</p>
<p>在官网中搜索可以找到某个包</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/becec5e937db4a4b975c38e86e183451~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<p>安装了node自动就有了npm（npm是node官方出的包管理器）</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4c35c604801475ca3a8149716d213f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>回到文件夹里，package.json已经生成了</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7032798c1ea24a37a65e9873361982a2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h3 data-id="heading-11">获取npm全局安装地址</h3>
<p>npm root -g</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a889a136a12f4c838f707e5f57f9a958~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<h3 data-id="heading-12">开发依赖和生产依赖</h3>
<ol>
<li>只有在开发时（写代码）需要依赖的库，就是开发依赖——例如：语法检查，压缩代码，扩展CSS前缀的包</li>
<li>在生产环境中必不可少的包，就是生产依赖——例如：jQuery，axios等等。所谓的生产环境就是指：项目开发完毕，要部署到服务器上运行</li>
<li>某些包即属于开发依赖，又属于生产依赖——例如：jQuery</li>
</ol>
<p>这两个依赖是为了有时候区分包在什么时候才产生的</p>
<p> </p>
<h3 data-id="heading-13">删除依赖包</h3>
<p>npm remove 依赖包名</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7c7c010d06a4431ae51d44a0a1c1ae4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac9882e4376f489d9e3019d7b3694cce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h3 data-id="heading-14">npm一些其他命令</h3>
<ol>
<li>npm aduit fix：检测项目依赖中的一些问题，并且尝试修复</li>
<li>npm view xxxxx versions：查看npm仓库中xxxx包的所有版本信息</li>
<li>npm view xxxxx version：查看npm仓库中xxxx包的最新版本</li>
<li>npm ls xxxx：查看我们所安装的xxxx包的版本</li>
</ol>
<p> </p>
<p>例子：安装某一个jQuery版本号</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65787eadaf594ca7ac8abe80c33437f8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> </p>
<h3 data-id="heading-15">关于版本号的说明</h3>
<p>"^3.x.x"：锁定最大版本，以后安装包的时候，保证包必须是3.x.x版本，x默认取最新的</p>
<p>"~3.1.x" ：锁定最小版本，以后安装包的时候，保证包必须是3.1.x版本，x默认取最新的</p>
<p>"3.1.1" ：锁定完整版本，以后安装包的时候，保证包必须是3.1.1版本</p>
<p> </p>
<h3 data-id="heading-16">node.js创建一个js文件后导入包</h3>
<p>使用import语句</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 入口文件</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">// 1.1 导入路由的包</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h2 data-id="heading-17">webpack</h2>
<p>Webpack 是一个前端资源加载/打包工具。它将根据模块的依赖关系进行静态分析，然后将这些模块按照指定的规则生成对应的静态资源。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65d4cbcf46324410a68b5ac41078d4a1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>中文文档：<a href="https://www.webpackjs.com/" target="_blank" rel="nofollow noopener noreferrer">www.webpackjs.com/</a></p>
<h3 data-id="heading-18">安装 Webpack</h3>
<p>在安装 Webpack 前，你本地环境需要支持 <a href="https://www.runoob.com/nodejs/nodejs-install-setup.html" target="_blank" rel="nofollow noopener noreferrer">node.js</a>。</p>
<pre><code class="copyable">npm install webpack -g
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 本身只能处理 JavaScript 模块，如果要处理其他类型的文件，就需要使用 loader 进行转换。</p>
<p>所以如果我们需要在应用中添加 css 文件，就需要使用到 css-loader 和 style-loader，他们做两件不同的事情，css-loader 会遍历 CSS 文件，然后找到 url() 表达式然后处理他们，style-loader 会把原来的 CSS 代码插入页面中的一个 style 标签中。</p>
<pre><code class="copyable">//当在控制台直接输入webpack命令执行的时候，webpack做了以下几步：
//1.首先，webpack发现，并没有通过命令的形式，给其指定入口和出口
//2.webpack会去项目根目录中，查找一个叫做‘webpack.config.js’的配置文件
//3.当找到配置文件后，webpack会去解析执行这个配置文件，当解析执行完，就得到了配置文件导出的配置对象
//4.当webpack拿到配置对象后，就拿到了配置对象中指定的入口和出口，然后进行打包构建
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p> </p>
<p>一起学习，一起进步 -.- ，如有错误，可以发评论</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            