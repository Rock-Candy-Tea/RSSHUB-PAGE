
---
title: '从0搭建webpack5+vue3开发环境'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9710ae25ee224c2e9f5d3f48d406e478~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 06:08:52 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9710ae25ee224c2e9f5d3f48d406e478~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>一直以来都在使用基于各种脚手架创建的项目进行开发，很多webpack的配置这些脚手架都已经帮我们封装好了。一般情况下，脚手架提供的能力已经足够我们使用了，有些不适用的地方看看文档改一下配置也能满足。最近一直挺好奇脚手架这个“黑盒”内部的webpack配置是怎么做的，于是就想自己搭一套相关的配置，学习一下。<br>
文章不会过多介绍webpack相关的各种配置原理，只是简单记录整个过程，希望能对大家有所帮助。<br>
话不多说，我们开始吧。</p>
<h1 data-id="heading-1">正式开始</h1>
<blockquote>
<p>在开始之前请确保我们已经安装了node和npm。推荐使用<code>nvm</code>来安装和管理node版本，本次我使用的node版本是<code>14.20.0</code></p>
</blockquote>
<h2 data-id="heading-2">一、初始化空项目</h2>
<p>新建一个空白文件夹，然后执行<code>yarn</code>的初始化命令。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">mkdir</span> vue3
<span class="hljs-built_in">cd</span> vue3
yarn init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完我们就得到了一个只有<code>package.json</code>文件的空项目。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9710ae25ee224c2e9f5d3f48d406e478~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">二、安装<code>webpack</code>依赖</h2>
<p>接下来我们就要安装webpack相关的依赖了。在终端执行</p>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add webpack webpack-cli -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装的时候发现速度非常慢，我们可以在项目下新增一个<code>.npmrc</code>文件，指定下npm镜像源</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4f99212d70d4d17af2e9881e3e4144e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
安装好以后，<code>package.json</code>文件的<code>devDependencies</code>下就会有我们刚刚安装好的依赖和对应的版本号</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d79b0bc806f40e3b8d08687c1dd40ed~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">三、增加<code>webpack</code>配置文件，完善基本配置</h2>
<p>在项目根目录下新建一个<code>webpack.config.js</code>文件，写一点基本的配置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">main</span>: <span class="hljs-string">'./src/index.js'</span>,
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.<span class="hljs-title function_">resolve</span>(__dirname, <span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[contenthash:8].js'</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在根目录下新建<code>src</code>文件夹，新建一个<code>index.js</code>文件，写点基本的代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'hello world'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>package.json</code>文件增加<code>scripts</code>字段，配置<code>build</code>命令</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"vue3"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"1.0.0"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"main"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"index.js"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"license"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"MIT"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"build"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"webpack"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"devDependencies"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"webpack"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"^5.74.0"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"webpack-cli"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"^4.10.0"</span>
  <span class="hljs-punctuation">&#125;</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在终端执行<code>yarn build</code>，然后就能看到生成的打包好的文件啦</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f72c91116eef40fca7b400e0cffbebf7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个时候我们发现生成的文件里面有很多注释之类的代码，文件体积很大，我们需要修改webpack配置的<code>mode</code>为<code>production</code>。<br>
这个<code>mode</code>我们在开发的时候希望是<code>development</code>，在打包的时候是<code>production</code>，我们可以在<code>scripts</code>里指定，这样就不需要每次手动修改了<br>
修改<code>package.json</code>文件</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"build"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"NODE_ENV=production webpack"</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，修改<code>webpack.config.js</code>文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-attr">mode</span>: process.<span class="hljs-property">env</span>.<span class="hljs-property">NODE_ENV</span>,
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行<code>yarn build</code>，这个时候生成的代码就很干净了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/286e2daa75a94090a4ac90c2c9a029bb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">四、使用<code>clean-webpack-plugin</code>，清理旧的打包文件</h2>
<p>上一步最后，我们发现<code>dist</code>目录下有两个<code>main.xxx.js</code>文件，这是因为我们打包了两次，所以生成了两个。我们希望每次打包都自动删掉上次生成的文件，不要有额外的文件干扰我们。<br>
要实现这个功能，我们只需要安装一个webpack的插件即可。<br>
在终端下执行<code>yarn add clean-webpack-plugin -D</code>，然后在<code>webpack.config.js</code>文件里引入这个插件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> &#123; <span class="hljs-title class_">CleanWebpackPlugin</span> &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>);

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> <span class="hljs-title class_">CleanWebpackPlugin</span>(),
    ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行<code>yarn build</code>，这个时候我们发现<code>dist</code>目录下就只有刚刚打包好的这个文件了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a165ed87a8d4497e9e40a66e8cee265d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bca95420179c474c994a6ce9ea07b5e2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">五、增加<code>index.html</code>入口文件</h2>
<p>经过上面的步骤，我们已经可以打包基本的js文件了。接下来，我们需要新增一个index.html文件，让它引入我们的js文件，在浏览器里显示我们需要的内容。<br>
在项目根目录下新增一个<code>template</code>目录，新增一个html文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d61b5a95a9f142399facd184a3ff183e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
安装<code>html-webpack-plugin</code>插件，它能帮助我们自动引入打包生成好的js、css等文件到html文件中。
在终端执行<code>yarn add html-webpack-plugin -D</code>，然后在<code>webpack.config.js</code>文件里引入它</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">const</span> <span class="hljs-title class_">HTMLWebpackPlugin</span> = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> <span class="hljs-title class_">CleanWebpackPlugin</span>(),
        <span class="hljs-keyword">new</span> <span class="hljs-title class_">HTMLWebpackPlugin</span>(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">'./template/index.html'</span>,
        &#125;),
    ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行<code>yarn build</code>，我们发现<code>dist</code>目录下多了个<code>index.html</code>文件，在浏览器打开它，发现控制台输出了<code>hello world</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c96cfaa8d5e14db5b4bdaa5238542b3a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bbe99d35f694d619f9ae0db92d6cf73~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>注意</strong>：这里的<code>在浏览器打开html文件</code>需要以<code>web server</code>的方式打开，而不是以<code>file</code>的方式打开。以<code>file</code>的方式打开，使用的是文件协议，在浏览器里的url是以<code>file</code>开头的</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/665609521f2f4316a9e5861f3716e90b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
如果是以<code>web server</code>的方式打开，浏览器里的url应该是以<code>http(s)</code>开头的。</p>
<h2 data-id="heading-7">六、使用<code>webpack-dev-server</code>进行本地调试</h2>
<p>上面提到我们需要以<code>http server</code>的方式打开我们的html文件，为了更好的本地开发体验，我们可以使用<code>webpack-dev-server</code>来进行本地的开发调试。<br>
打开终端，执行<code>yarn add webpack-dev-server -D</code>，安装所需依赖。<br>
修改<code>package.json</code>文件，增加<code>dev</code>命令</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"dev"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"NODE_ENV=development webpack serve"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"build"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"NODE_ENV=production webpack"</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以修改下<code>webpack-dev-server</code>的配置，让它自动帮我们打开浏览器，并且增加<code>source map</code>的配置，提升本地开发体验。打开<code>webpack.config.js</code>文件，配置<code>devtool</code>和<code>devServer</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval-source-map'</span>,
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>yarn dev</code>，在浏览器里自动打开了<code>http://localhost:8080</code>这个页面，打开控制台，我们发现他输出了<code>hello world</code>，这就是我们在<code>index.js</code>里写的代码</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c68c91c0dd92411e9071e2af2eb50cbb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">七、使用<code>vue</code>来编写前端代码</h2>
<p>经过上面的几步，我们的项目已经有了一个基本的雏形了，可以本地开发，也可以打包。接下来我们就要使用<code>vue</code>来编写前端代码，实现各种炫酷的界面和功能了。<br>
打开终端，依次执行<code>yarn add vue</code>，<code>yarn add vue-loader -D</code><br>
在<code>src</code>目录下新建一个<code>app.vue</code>文件，写一点基础的代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"app"</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>index.js</code>里引入<code>vue</code>来渲染这个组件。（别忘了在<code>index.html</code>里加上<code>id</code>为<code>root</code>的元素）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./app'</span>;

<span class="hljs-keyword">const</span> app = <span class="hljs-title function_">createApp</span>(<span class="hljs-title class_">App</span>);

app.<span class="hljs-title function_">mount</span>(<span class="hljs-string">'#root'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们需要在<code>webpack.config.js</code>里增加<code>module.rules</code>来支持解析<code>vue</code>文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'vue-loader'</span>,
            &#125;
        ],
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行<code>yarn dev</code>，我们发现页面报错了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fedccb76049648ea91e6db838ba8b596~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
根据报错信息，我们发现是<code>webpack</code>没找到<code>app.vue</code>这个文件，这是因为我们没写文件的后缀，而webpack默认只会以<code>.js .json .wasm</code>这三个后缀来找，所以找不到<code>app.vue</code>这个文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae56e79966364ca3aa7f765043cd776d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
要解决这个问题，我们需要修改下<code>resolve.extensions</code>的配置<br>
打开<code>webpack.config.js</code>文件，新增<code>resolve</code>相关的配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">resolve</span>: &#123;
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'...'</span>, <span class="hljs-string">'.vue'</span>],
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行<code>yarn dev</code>，还是报错</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca831774ebdd4410b88a249807a7fd37~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里报了两个错误，我们先看第二个错误，他的意思很明显，我们需要在<code>webpack.config.js</code>里引入<code>VueLoaderPlugin</code>，我们在<code>vue-loader</code>的官方文档查找<code>VueLoaderPlugin</code>这个关键词，可以找到相关的说明。因为我们的<code>vue-loader</code>版本高于<code>14</code>，所以我们要手动引入这个插件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dcce61993a1407a949a6c0ba4c7d69d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
按照官方文档的说明进行配置，修改完配置后，我们重新执行<code>yarn dev</code>，发现项目启动成功了。页面上显示出了<code>hello vue</code>，但是浏览器的控制台报了一个<code>warning</code>（第一个warning是我安装的浏览器插件导致的，可以忽略）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7dcd70c16294be1b44c8a57887935fb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
点进去这个链接，我们发现需要通过<code>webpack</code>的<code>DefinePlugin</code>来注入这两个变量</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a8e69861a804fd5abbd81a9189b2ebf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
修改<code>webpack.config.js</code>，增加<code>DefinePlugin</code>配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">const</span> &#123; <span class="hljs-title class_">DefinePlugin</span> &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>);

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// ...</span>
        <span class="hljs-keyword">new</span> <span class="hljs-title class_">DefinePlugin</span>(&#123;
            <span class="hljs-attr">__VUE_OPTIONS_API__</span>: <span class="hljs-string">'true'</span>,
            <span class="hljs-attr">__VUE_PROD_DEVTOOLS__</span>: <span class="hljs-string">'false'</span>,
        &#125;),
    ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次<code>yarn dev</code>启动项目，warning就消失啦</p>
<h2 data-id="heading-9">八、编写样式美化界面</h2>
<p>前端的世界必然离不开css，我们的项目已经可以使用<code>vue</code>来编写界面了，接下来就要用<code>css</code>来美化它们了，让我们编写css的配置来实现一个五彩斑斓的黑的效果吧。<br>
安装相关<code>loader</code>，在终端执行<code>yarn add css-loader style-loader -D</code>；修改<code>webpack.config.js</code>的<code>module.rules</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.vue$/</span>,
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'vue-loader'</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.css$/</span>,
                <span class="hljs-attr">use</span>: [
                    <span class="hljs-string">'style-loader'</span>,
                    <span class="hljs-string">'css-loader'</span>,
                ],
            &#125;,
        ],
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>app.vue</code>里随便写点样式</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>hello vue<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"app"</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.container</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#38f</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新<code>yarn dev</code>，页面上就有了样式效果了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deb98b637f994d2a8568b51c3b7a5175~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
一般情况下，我们都会用<code>sass</code>或者<code>less</code>这样的语言来写样式，这里以<code>sass</code>为例<br>
执行<code>yarn add sass sass-loader -D</code>安装相应的依赖，再改下<code>webpack.config.js</code>配置
<code>module.rules</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.vue$/</span>,
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'vue-loader'</span>,
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.s?css$/</span>,
                <span class="hljs-attr">use</span>: [
                    <span class="hljs-string">'style-loader'</span>,
                    <span class="hljs-string">'css-loader'</span>,
                    <span class="hljs-string">'sass-loader'</span>,
                ],
            &#125;,
        ],
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把<code>app.vue</code>的<code>style</code>标签的<code>lang</code>属性设置成<code>scss</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.container</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#38f</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新<code>yarn dev</code>，页面显示正常，完美！</p>
<h2 data-id="heading-10">九、使用<code>mini-css-extract-plugin</code>抽离css代码</h2>
<p>上一步我们成功完成了<code>css</code>相关的配置，我们使用了<code>style-loader</code>来帮助我们引入我们编写的样式，它会把我们的<code>css</code>代码以<code>style</code>标签的方式插入到<code>index.html</code>文件的<code>head</code>里</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58aa49e24bd2434195eb43cd1e6f12ed~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当我们的代码越来越多的时候，所有的<code>css</code>代码全部在<code>index.html</code>里会让这个文件非常大，很臃肿。这个时候我们可以用<code>mini-css-extract-plugin</code>来帮我们把这些<code>css</code>代码抽离成单独的文件。<br>
打开终端，执行<code>yarn add mini-css-extract-plugin -D</code>，修改<code>webpack.config.js</code>，用<code>MiniCssExtractPlugin.loader</code>替换掉<code>style-loader</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ...</span>
<span class="hljs-keyword">const</span> <span class="hljs-title class_">MiniCssExtractPlugin</span> = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            <span class="hljs-comment">// ...</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.s?css$/</span>,
                <span class="hljs-attr">use</span>: [
                    <span class="hljs-title class_">MiniCssExtractPlugin</span>.<span class="hljs-property">loader</span>,
                    <span class="hljs-string">'css-loader'</span>,
                    <span class="hljs-string">'sass-loader'</span>,
                ],
            &#125;,
        ],
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> <span class="hljs-title class_">MiniCssExtractPlugin</span>(&#123;
            <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/[name].[contenthash:8].css'</span>
        &#125;),
    ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行<code>yarn dev</code>，打开浏览器控制台，这个时候我们的<code>css</code>代码就是通过单独的<code>css</code>文件来引入的了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04568c582b9d4f2db7427e8d2a64f1c2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">十、引入<code>ant-design-vue</code>组件库</h2>
<p>一般我们都会引入一些业界成熟的组件库，具体使用哪一个就凭大家的喜好，这里我们来引入<code>ant-design-vue</code>，具体的引入方式大家参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.antdv.com%2Fdocs%2Fvue%2Fintroduce-cn%23%25E6%258C%2589%25E9%259C%2580%25E5%258A%25A0%25E8%25BD%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://www.antdv.com/docs/vue/introduce-cn#%E6%8C%89%E9%9C%80%E5%8A%A0%E8%BD%BD" ref="nofollow noopener noreferrer">官方文档</a>，这里就不再赘述了。</p>
<h2 data-id="heading-12">十一、使用<code>webpack asset module</code>处理静态资源</h2>
<p>除了代码以外，我们的项目里还会需要引入各种静态资源，例如图片、字体等，接下来我们就编写对应的配置来处理这类资源。<br>
在<code>webpack v4</code>版本我们通常需要借助<code>file-loader</code>、<code>url-loader</code>来实现，而<code>webpack v5</code>已经内置了这些能力，不再需要借助第三方的<code>loader</code>了，具体可以查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fguides%2Fasset-modules%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/guides/asset-modules/" ref="nofollow noopener noreferrer">官方文档</a></p>
<p>修改<code>webpack.config.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// ...</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.jpe?g|png|gif|webp$/</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'asset'</span>,
        <span class="hljs-attr">generator</span>: &#123;
          <span class="hljs-attr">filename</span>: <span class="hljs-string">'assets/image/[hash:8][ext]'</span>
        &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.eot|woff|woff2|ttf|svg|otf$/</span>,
        <span class="hljs-attr">type</span>: <span class="hljs-string">'asset'</span>,
        <span class="hljs-attr">generator</span>: &#123;
          <span class="hljs-attr">filename</span>: <span class="hljs-string">'assets/font/[hash:8][ext]'</span>,
        &#125;
      &#125;,
    ]
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">十二、编写<code>splitChunks</code>配置，合理拆分代码</h2>
<p>经过上面的步骤，我们的项目已经具备基本的开发、调试、打包能力了，但是还有一点小小的问题可以优化一下。<br>
打开浏览器的控制台，切换到<code>network</code>，我们可以发现，现在生成的产物只有一个<code>js</code>文件和一个<code>css</code>文件，而且这个<code>js</code>文件的体积非常大，这是因为我们项目里引用的依赖例如<code>vue</code>、<code>ant-design-vue</code>的代码也在这个文件里。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4743ace720fe4f0fa984a945355fff8b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
一般而言，我们引用的第三方依赖的版本都是不会经常变化的，而我们如果把第三方依赖和我们的业务代码生成到一个文件里，那么每次业务代码改变，生成的<code>hash</code>就变了，浏览器会重新加载整个文件，对这些第三方依赖而言，其实是被重复加载了。<br>
所以，为了不重复加载这些依赖，提高网页性能，常见的做法是把它们单独拆出来，生成单独的文件，这样就能利用浏览器缓存的能力<br>
为了实现上面的功能，我们只需修改<code>webpack</code>的<code>splitChunks</code>的配置即可</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ...</span>

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
        <span class="hljs-attr">cacheGroups</span>: &#123;
          <span class="hljs-attr">vendor</span>: &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\/]node_modules[\/]/</span>,
            <span class="hljs-comment">// filename: 'chunks/vendor.js',</span>
            <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-function">(<span class="hljs-params"><span class="hljs-variable language_">module</span></span>) =></span> &#123;
              <span class="hljs-keyword">const</span> regExp = <span class="hljs-regexp">/[\/]node_modules[\/](.*?)[\/]/g</span>;
              <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/javascript/ig</span>.<span class="hljs-title function_">test</span>(<span class="hljs-variable language_">module</span>.<span class="hljs-property">type</span>)) &#123;
                <span class="hljs-keyword">const</span> packageName = <span class="hljs-variable language_">module</span>.<span class="hljs-property">context</span>.<span class="hljs-title function_">match</span>(<span class="hljs-regexp">/[\/]node_modules[\/](.*?)([\/]|$)/</span>)[<span class="hljs-number">1</span>];
                <span class="hljs-keyword">return</span> <span class="hljs-string">`npm.<span class="hljs-subst">$&#123;packageName.replace(<span class="hljs-string">'@'</span>, <span class="hljs-string">''</span>)&#125;</span>`</span>;
              &#125;
              <span class="hljs-keyword">const</span> identifier = <span class="hljs-variable language_">module</span>.<span class="hljs-title function_">identifier</span>();
              <span class="hljs-keyword">const</span> packageName = identifier.<span class="hljs-title function_">match</span>(regExp).<span class="hljs-title function_">pop</span>().<span class="hljs-title function_">replace</span>(<span class="hljs-regexp">/node_modules|[\/]/ig</span>, <span class="hljs-string">''</span>);
              <span class="hljs-keyword">return</span> <span class="hljs-string">`npm.<span class="hljs-subst">$&#123;packageName.replace(<span class="hljs-string">'@'</span>, <span class="hljs-string">''</span>)&#125;</span>`</span>;
            &#125;
          &#125;
        &#125;
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的大致意思就是对于<code>node_modules</code>下面的模块，我们会拿到它的包名，然后加上<code>npm.</code>的前缀，例如<code>ant-design-vue</code>，最后的名字就是<code>npm.ant-design-vue.[contenthash:8].js</code>这样的格式。通过这样的方式，我们就能把它们分离出来。想要进一步了解<code>splitChunks</code>的内容，大家可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Foptimization%2F%23optimizationsplitchunks" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/optimization/#optimizationsplitchunks" ref="nofollow noopener noreferrer">官方文档</a><br>
再次执行<code>yarn dev</code>，打开浏览器控制台的<code>network</code>部分，看看我们配置的效果吧</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f240db227b434c63a6d28ca66a623896~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">结尾</h1>
<p>以上就是本文的全部内容了，其实还有很多可以完善的地方，例如<code>eslint</code>、<code>unit test</code>、<code>commitlint</code>、<code>mock</code>等，本次就先讲到这里，预知后事如何，请听下回分解～<br>
喜欢的话，就点赞收藏吧～<br>
大家觉得有不对的地方也欢迎在评论区留言～</p></div>  
</div>
            