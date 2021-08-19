
---
title: '我的webpack进化史-构建篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2febefd59ded4d71a9a18e679c271ca1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 02:26:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2febefd59ded4d71a9a18e679c271ca1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">开篇还是我的一些碎碎念！</h4>
<p>前面我们刚刚把webpack最基础的加载css，加载图片，一些基本配置都写完啦！那么这次接着上周的代码，我们继续捣鼓！我之前用vue脚手架搭的项目写项目时就会很奇怪，为什么我每次一保存它就会自动帮我更新页面呀！为什么每次我启动项目都会自动帮我打开浏览器？由于当时的我脑子里充满了业务需求，这些东西通通被我抛到脑后，这次扫盲过程才发现之前经典webpack面试题目--<strong>热更新（HMR 全称 HotModuleReplacement)</strong> 就是讲这个的呀！唉，年少不知webpack。这次构建篇还是会和之前基础篇一样，我按我自己平常写项目的思路把我不明白不清楚的问题都会首先抛出来，期间碰到过的问题也全部贴出来，然后在贴详细代码。要是有大佬路过，请留步！请赐教！求指导！代码完整连接指路👉   <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiaoshanweb%2Fwebpack-test" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiaoshanweb/webpack-test" ref="nofollow noopener noreferrer">github.com/xiaoshanweb…</a></p>
<p>本篇主要讲三部分</p>
<h3 data-id="heading-1">I. webpack中加载vue，react文件</h3>
<p>在基础篇文章里，我们讲了些基本配置。但是在webpack中如何配置vue，react？</p>
<h5 data-id="heading-2">1: babel</h5>
<p>在实现加载vue，react文件之前，我们必须要先了解下babel这个插件。babel他其实就是将非ECMAScript 2015的语言，向后转化为兼容的javascript。将我们的vue语法，jsx转换成js，箭头函数转成function，const转成var等等。</p>
<pre><code class="copyable">npm install @babel/plugin-transform-arrow-functions -D 将箭头函数转换的插件
npm install @babel/plugin-transform-block-scoping -D 将const转成var
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一点要说的是，babel一个独立的工具，它不和和webpack等构建工具配置。如果要转化的内容很多，我们也不可能一个一个去安装插件，所以babel还有一个概念 <strong>预设preset</strong> ，我们可以直接给webpack提供一个预设，webpack会根据我们的预设去加载插件，并且将它传递给babel。我们比较常见的预设是 <strong>env react TypeScript</strong></p>
<pre><code class="copyable">npm install @babel/preset-env
npm install --save-dev @babel/core
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">2: 加载react文件</h5>
<pre><code class="copyable">npm i --save-dev react react-dom
npm install @babel/preset-react -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先把react的基本配置写好，index.html文件下新增一个id为root的标签，根目录下新建一个Babel.config.js文件</p>
<p>新建一个babel.config.js的文件，将我们需要加载的插件写入。如果不想新建一个文件也可以在webpack下配置去加载插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">presets</span>: [
    [<span class="hljs-string">"@babel/preset-env"</span>],
    [<span class="hljs-string">"@babel/preset-react"</span>],
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在webpack.config.js的rules里面配置babel-loader</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jsx?$/i</span>,
    exclude: <span class="hljs-regexp">/node_modeuls/</span>,
    use: &#123;
      <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
      <span class="hljs-comment">// options: &#123;</span>
      <span class="hljs-comment">//   presets: [</span>
      <span class="hljs-comment">//     ["@babel/preset-env", &#123;</span>
      <span class="hljs-comment">//       // targets: ["chrome 88"]</span>
      <span class="hljs-comment">//       // enmodules: true</span>
      <span class="hljs-comment">//     &#125;]</span>
      <span class="hljs-comment">//   ]</span>
      <span class="hljs-comment">//   // plugins: [</span>
      <span class="hljs-comment">//   //   "@babel/plugin-transform-arrow-functions",</span>
      <span class="hljs-comment">//   //   "@babel/plugin-transform-block-scoping"</span>
      <span class="hljs-comment">//   // ]</span>
      <span class="hljs-comment">// &#125;</span>
    &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建一个reactFile.jsx文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReactApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
 <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
   <span class="hljs-built_in">super</span>(props);

   <span class="hljs-built_in">this</span>.state = &#123;
     <span class="hljs-attr">message</span>: <span class="hljs-string">"Hello React"</span>
   &#125;
 &#125;

 <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-keyword">return</span> (
     <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.message&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
   )
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactApp <span class="hljs-keyword">from</span> <span class="hljs-string">'./reactFile.jsx'</span>
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ReactApp</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.html</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <meta charset=<span class="hljs-string">"UTF-8"</span> />
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"ie=edge"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">title</span>></span>
    <%= htmlWebpackPlugin.options.title %>
  <span class="hljs-tag"></<span class="hljs-name">title</span>></span></span>
</head>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2febefd59ded4d71a9a18e679c271ca1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">3: 加载vue文件</h5>
<pre><code class="copyable">npm i --save-dev vue vue-loder vue-templete-compiler
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue文件的加载相对来说比较简单，先把vue文件建起来并挂载，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"vue"</span>></span>我是Vue文件<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-class">.vue</span> &#123;
 <span class="hljs-attribute">color</span>: red;
 <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'./index.less'</span>
<span class="hljs-keyword">import</span> Icon <span class="hljs-keyword">from</span> <span class="hljs-string">'./img.jpeg'</span>
<span class="hljs-keyword">import</span> printMe <span class="hljs-keyword">from</span> <span class="hljs-string">'./print'</span>

<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueApp <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactApp <span class="hljs-keyword">from</span> <span class="hljs-string">'./reactFile.jsx'</span>
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">component</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> element = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  element.innerHTML = <span class="hljs-string">'Hello Webpack'</span>
  element.classList.add(<span class="hljs-string">'color_red'</span>)

  <span class="hljs-keyword">var</span> img = <span class="hljs-keyword">new</span> Image(<span class="hljs-number">300</span>, <span class="hljs-number">300</span>)
  img.src = Icon
  element.appendChild(img)

  <span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'button'</span>)
  btn.innerHTML = <span class="hljs-string">'点击我'</span>
  btn.onclick = printMe
  element.appendChild(btn)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">222</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">333</span>)
  <span class="hljs-keyword">return</span> element
&#125;

<span class="hljs-built_in">document</span>.body.appendChild(component())

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ReactApp</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(VueApp)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.html</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <meta charset=<span class="hljs-string">"UTF-8"</span> />
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"ie=edge"</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">title</span>></span>
    <%= htmlWebpackPlugin.options.title %>
  <span class="hljs-tag"></<span class="hljs-name">title</span>></span></span>
</head>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次在webpack.config.js里配置，vue-loader会匹配所有.vue文件，VueLoaderPlugin会将所有匹配出来的vue文件进行处理。不过在下载vue-loader时要注意，<strong>vue-loader的版本不要太高</strong>，下载<strong>15.x.x</strong>版本就可以。引入VueLoaderPlugin的方法有两种，一种是直接require('vue-loader/lib/plugin')，也可以下载vue-loder-plugin直接引用。但两者相差不大，在vue-loder-plugin中他也是去引用vue-loader/lib/plugin</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// const VueLoaderPlugin = require('vue-loader/lib/plugin')</span>
<span class="hljs-keyword">const</span> VueLoaderPlugin = <span class="hljs-function"><span class="hljs-title">require</span>(<span class="hljs-params"><span class="hljs-string">'vue-loader-plugin'</span></span>)</span>

 &#123;
   <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/i</span>,
   use: <span class="hljs-string">'vue-loader'</span>
 &#125;,
 
 <span class="hljs-keyword">new</span> VueLoaderPlugin()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8394390699b4fceb19388305ec50db0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">II. 自动编译</h3>
<p>在上一篇文章，我们是通过build方法来查看代码的每次更新，webpack要实现自动编译到底是提供了什么方法？</p>
<h5 data-id="heading-6">1:watch</h5>
<pre><code class="copyable">watch是可以监听文件的变化，通过live-server插件（vs插件）提供本地服务在在每次修改文件后自动刷新页面
缺点：
    a：效率不是很高，我们还是要手动build之后再启动watch；
    b：它对所有的diamanté都重新进行编译，而且编译成功后，都会产生新的文件（比如文件操作，file等）
    c：虽然可以监听到文件变化，但实际上没有自动刷新浏览器的功能
  
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//package.json</span>
<span class="hljs-string">"watch"</span>: <span class="hljs-string">"webpack --watch"</span>,
<span class="hljs-comment">//或者webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports=&#123;
    <span class="hljs-attr">watch</span>:<span class="hljs-literal">true</span>,
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">2:webpack-dev-server</h5>
<p>在开发中，我们是希望在没有live-server的情况下，依然可以具备实施刷新加载的功能。webpack-dev-server在编译之后是不会向watch会产生一些新的输出文件，它生成文件的都是存在内存中。它让使用者可以配置一个地址，规定我们必须用过这个地址去调试，开发。</p>
<pre><code class="copyable">  npm install --save-dev-webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在package.json中写脚本命令，有一点要注意的是，我在查看webpack-dev-server的过程中看到有两种启动方式。第一种是直接用web-dev-server插件去启动，第二种是webpack有内置server服务，但是用第二种方式去启动就必须保证webpack的版本要兼容webpack-dev-server，最麻烦的事这两种启动方式不能并存。</p>
<pre><code class="copyable">"start": "webpack-dev-server",
要求的web-dev-server的版本

"start-other": "webpack serve",
要求的webpack和web-dev-server的版本
"webpack": "^5.48.0",
"webpack-cli": "^4.5.0",
"webpack-dev-server": "^3.11.2"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后在webpack.config.js中配置devServer，devServer的配置相对来还是很常见，</p>
<p><strong>contentBase：</strong> 这个属性其实接触并不多，但如果index.html里面有额外的使用某些存放在pubilc下的静态资源，在index.html里面这样引入，但是浏览器根本无法通过这个路径去引入的，所以可以通过设置contentBase来制定我们要从那里去取这个文件。contentBase和publicPath这两个概念我在刚开始看的时候就很容易搞混，而且在发布的时候，如果后端是在一台服务器上部署h5和pc端，那这个时候publicPath就需要区分h5是从那里进入，pc是从那里进入。publicPath这个比较重要，我们在下面再来细说。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">devServer: &#123;
   <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>,<span class="hljs-comment">//主机地址</span>
   <span class="hljs-attr">port</span>: <span class="hljs-number">8000</span>,<span class="hljs-comment">//端口号</span>
   <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span><span class="hljs-comment">//是否项目启动成功后自动打开浏览器</span>
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样直接启动命令，在修改文件后，就会发现浏览器自动刷新啦！webpack-dev-server的配置相对来说还是比较简单。大部分的处理webpack-dev-server它自己搞了，但是如果我需要自己配置热更新的过程怎么办？我不想要框架集成的怎么办？我之前写ssr（服务器渲染）的时候就碰到过这种问题，通过node启动项目，没有热更新，需要我自己去配置。</p>
<h5 data-id="heading-8">3: webpack-dev-middleware</h5>
<p>webpack-dev-middlewarek可以说是一个封装器，他可以把webpack处理过的文件发送到一个sever。webpack-dev-server在内部使用了它（对哦，没错哦，webpack-dev-server内部是使用的他来实现热更新哦)。然而webpack-dev-middleware也可以作为一个单独的package来使用，这样就方便使用者根据需求进行更多的自定义。</p>
<p>例子我实在官方网站看到的，我就直接用了。当然如果你对node比较熟悉，你用koa搭建也是可以的，官方的例子是express搭建的。先安装express，webpack-dev-middleware</p>
<pre><code class="copyable">npm install --save-dev express webpack-dev-middleware
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后新建一个server.js文件。先将我们需要用到的express，webpack，webpack-dev-middleware引入。创建一个app，并且监听3000的端口号。config拿到了所有的配置信息，再将config传递给webpack，webpack将所有的配置信息进行编译。将webpack编译成功之后会生成一个compiler对象传递给webpackDevMiddleware。处理完之后webpackDevMiddleware是会生成一个express的中间件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> webpackDevMiddleware = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-dev-middleware'</span>)
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)

<span class="hljs-keyword">const</span> app = express()
<span class="hljs-comment">// 加载配置信息</span>
<span class="hljs-keyword">const</span> config = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.config'</span>)
<span class="hljs-comment">// 将配置信息传递给webpack编译</span>
<span class="hljs-keyword">const</span> compiler = webpack(config)

<span class="hljs-comment">// 将编译后的结果返回给webpackDevMiddleware，之后的请求webpackDevMiddleware()返回给中间件处理</span>
app.use(webpackDevMiddleware(compiler))

app.listen(<span class="hljs-number">4000</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"服务已经开启在3000端口上~"</span>);
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目结构如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8a2e3a4690e4aa78bfc666d0a3e64bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ok，代码写完后，我们来测试下。打开终端输入 <strong>node server.js</strong>，当控制台出现输出就代表运行成功了，接下来在浏览器中输入<a href="https://link.juejin.cn/?target=http%3A%2F%2F127.0.0.1%3A4000" target="_blank" rel="nofollow noopener noreferrer" title="http://127.0.0.1:4000" ref="nofollow noopener noreferrer">http://127.0.0.1:4000</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ca5f20412094c61bead35ae961640f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ed5a374699d4044b2c925d251cc425a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-9">4:HMR（HotModuleReplacement）</h5>
<p>HMR--热更替/热更新。专业点说就是指在程序运行过程中添加，删除，更替模块不需要重新刷新整个页面。在默认情况下，webpack-dev-server已经支持HMR，我们只需要开启就可以。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">devServer: &#123;
    <span class="hljs-comment">// contentBase: './dist',</span>
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">8000</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 开启HMR</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当浏览器出现这几个的时候代表已经连接成功。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90d714cd714541849f41c48883f698ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们说的三个热更新方法其实都是刷新的整个页面，如果我希望每次我修改之后，只刷新我更改过的页面，就可以用<strong>module.hot.accept</strong>这个方法，在每个页面上添加在进而控制当前页面是否要更新。但是大型项目根本不允许我们这样去配置，在vue，react中我们要如何配合热更新。vue-loader当前已经支持热更新了，所以无需我们再去配置。react官方提供了react-refresh。</p>
<pre><code class="copyable">npm install -D @pmmmwh/react-refresh-webpack-plugin react-refresh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改webpack.config.js和babel.config.js文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">const</span> ReactRefreshWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@pmmmwh/react-refresh-webpack-plugin'</span>)

<span class="hljs-attr">plugins</span>:[
  <span class="hljs-keyword">new</span> ReactRefreshWebpackPlugin()
]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">presets</span>: [
    [<span class="hljs-string">"@babel/preset-env"</span>],
    [<span class="hljs-string">"@babel/preset-react"</span>],
  ],
  <span class="hljs-attr">plugins</span>: [
    [<span class="hljs-string">'react-refresh/babel'</span>]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">HMR原理</h6>
<p>看下面这张图（把王红元老师的图搬来了，要是有不妥之处，立马删！）。我们可以知道浏览器是通过Socket与webpack-dev-server进行通信的。源代码在webpack中被打包编译到内存中，浏览器通过http请求向服务器请求资源。但是http请求是短链接，每次都需要浏览器主动发出请求，服务器才会响应结果。</p>
<p>而我们需要实现的状态是，在浏览器没有发出请求的情况下，服务器依然向浏览器推送数据或资源，但是短链接是不可能实现的这种需求。</p>
<p>socket是可以解决这个问题。他是服务器和浏览器端之间的桥梁。当我们启动devServer的时候，socket在服务器和浏览器之间建立了一个webSocket长连接。当我们某个文件修改保存后，webpack将改文件打包编译之后的json，js文件，通过socket告知浏览器。浏览器接收到后做出响应，刷新对应的文件。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9c5df092fac4ceb8872449eae6b9e19~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">bug集锦</h4>
<h5 data-id="heading-12">2021-08-06</h5>
<p>第一个bug，这种bug以我目前的智商无法解释为什么要这么改。我百度的原因是说webpack-dev-server的版本和webpack-cli版本不匹配所以报错，
原先的版本</p>
<blockquote>
<p>"webpack-cli": "^4.7.2","webpack-dev-server": "^3.11.2"</p>
</blockquote>
<p>修改之后的版本</p>
<blockquote>
<p>"webpack-cli": "^3.3.12", "webpack-dev-server": "^3.11.2"</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b24db968bf8f48ce8a2242ea47fb3b9d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            