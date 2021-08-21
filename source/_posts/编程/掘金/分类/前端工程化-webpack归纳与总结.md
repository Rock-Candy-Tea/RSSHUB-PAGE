
---
title: '前端工程化-webpack归纳与总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ac62475008d4996b15deb7ad3dc6a5a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 01:21:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ac62475008d4996b15deb7ad3dc6a5a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>目前前端已经全面进入模块化和工程化的阶段,不仅有我们炒常用webpack项目构建工具,尤大又推出了更快的vite(下文讲解),本文主要对模块化和工程化以及webpack做以归纳总结</p>
<h1 data-id="heading-0">模块化</h1>
<p>在ES6模块化规范诞生之前，Javascript社区已经尝试并提出了AMD、CMD、CommonJS 等模块化规范。<br>
但是,这些社区提出的模块化标准,还是存在一定的差异性与局限性、并不是浏览器与服务器通用的模块化标准，例如:<br>
● AMD和CMD适用于浏览器端的Javascript模块化<br>
● CommonJS适用于服务器端的Javascript模块化<br>
因此，ES6语法规范中，在语言层面上定义了ES6模块化规范,是浏览器端与服务器端通用的模块化开发规范。<br>
ES6模块化规范中定义:<br>
● 每个js文件都是一个独立的模块<br>
● 导入模块成员使用import 关键字<br>
● 暴露模块成员使用export 关键字</p>
<h2 data-id="heading-1">1 默认导出与默认导入</h2>
<p>● 默认导出语法export default 默认导出的成员<br>
● 默认导入语法<code>import</code>接收名称<code>from</code>模块标识符’ 导入的名称可以自定义</p>
<h2 data-id="heading-2">2 需导出与按需导入</h2>
<p>● 按需导出语法<code>export let s1 = 10</code><br>
● 按需导入语法<code>import &#123; s1 &#125; from</code> ‘模块标识符’</p>
<h1 data-id="heading-3">webpack</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.webpackjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.webpackjs.com/" ref="nofollow noopener noreferrer">webpack官方文档</a></p>
<p>webpack是一个流行的前端项目构建工具 (打包工具) , 可以解决当前web开发中所面临的困境。webpack提供了友好的<code>模块化支持</code>,以及<code>代码压缩混淆</code>、<code>处理js兼容问题</code>、<code>性能优化</code>等强大的功能，从而让程序员把工作的重心放到具体的功能实现上，提高了开发效率和项目的可维护性。</p>
<h2 data-id="heading-4">1. 定义打包出去口</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>补充:</p>
<ol>
<li>join是把各个path片段连接在一起， resolve把‘／’当成根目录</li>
<li>join直接拼接字段，resolve解析路径并返回</li>
</ol>
<h2 data-id="heading-5">2. 配置自动打包</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ac62475008d4996b15deb7ad3dc6a5a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">3.配置首页预览页面</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c1f213a46fb468dba980e6dc1c96834~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">4. 自动打包相关参数</h2>
<p>打包完成后自动打开浏览器页面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --open --host 127.0.0.1 --port 8888"</span>
  &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">5. loader加载器的配置</h2>
<p>在实际开发过程中，webpack默认只能打包处理以. js后缀名结尾的模块，其他非.js 后缀名结<br>
尾的模块，webpack默认处理不了，需要调用loader加载器才可以正常打包，否则会报错!</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ac2f7b9b1274527b94c5dbc2c2dbe18~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">5.1 打包处理css文件</h3>
<ol>
<li>运行<code>npm i style-loader css-loader -D</code> 暗转处理css文件的loader</li>
<li>在webpack.config.js中module->rules数组中添加loader规则  :</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//所有第三方文件的匹配规则</span>
<span class="hljs-attr">module</span>:&#123;
    <span class="hljs-attr">rules</span>: [
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>, use: [ <span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span> ]  &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意:<br>
use数组中的loader顺序是固定的<br>
多个loader的调用顺序是从后往前调用</p>
<h3 data-id="heading-10">5.2 打包less相关文件</h3>
<ol>
<li>运行 <code>npm i less-loader less -D</code> 命令</li>
<li>在webpack.config.js 的 module -> rules数组汇总,添加laoder规则:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//所有第三方文件的匹配规则</span>
<span class="hljs-attr">module</span>:&#123;
    <span class="hljs-attr">rules</span>: [
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>, use: [ <span class="hljs-string">'style-loader'</span>,  <span class="hljs-string">'css-loader'</span> , <span class="hljs-string">'less-loader'</span> ] &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">5.3 打包scss相关文件</h3>
<ol>
<li>运行 <code>npm i sass-loader sass -D</code> 命令</li>
<li>在webpack.config.js 的 module -> rules数组汇总,添加laoder规则:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//所有第三方文件的匹配规则</span>
<span class="hljs-attr">module</span>:&#123;
    <span class="hljs-attr">rules</span>: [
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.sass$/</span>, use: [ <span class="hljs-string">'style-loader'</span>,  <span class="hljs-string">'css-loader'</span> , <span class="hljs-string">'sass-loader'</span> ] &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">5.4配置postCSS自动添加css的兼容前缀</h3>
<ol>
<li>运行 <code>npm i postcss-loader autoprefixer -D</code> 命令</li>
<li>在项目根目录中创建postcss的配置文件 postcss.config.js,并初始化如下配置:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//所有第三方文件的匹配规则</span>
<span class="hljs-keyword">const</span> autoperfixer = requier(<span class="hljs-string">'autoperfixer'</span>) <span class="hljs-comment">//导入自动添加前缀的插件</span>
<span class="hljs-attr">module</span>:&#123;
   <span class="hljs-attr">polugins</span>:[autoperfixer] <span class="hljs-comment">// 挂载插件</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在webpack.config.js 的 module -> rules数组汇总,添加laoder规则:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//所有第三方文件的匹配规则</span>
<span class="hljs-attr">module</span>:&#123;
    <span class="hljs-attr">rules</span>: [
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.sass$/</span>, use: [ <span class="hljs-string">'style-loader'</span>,  <span class="hljs-string">'css-loader'</span> , <span class="hljs-string">'postcss-loader'</span> ] &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">5.5 打包样式的中图片和字体文件</h3>
<ol>
<li>运行 <code>npm i url-loader file-loader -D</code> 命令</li>
<li>在webpack.config.js 的 module -> rules数组汇总,添加laoder规则:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">//所有第三方文件的匹配规则</span>
<span class="hljs-attr">module</span>:&#123;
    <span class="hljs-attr">rules</span>: [
        &#123; 
            <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.jpg|png|gif|bmp|ttf|eot|svg|woff$/</span>, 
            use: <span class="hljs-string">'url-loader?limit=16940'</span> 
        &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中?之后的是loader的参数项
limit 用来指定图片的大小,单位是字节(byte),只有小于limit大小的图片,才会被装维base64图片</p>
<h3 data-id="heading-14">5.6 打包处理js中的高级语法</h3>
<ol>
<li>安装babel转换器相关的包:npm i babel-loader @bable/core @babel/runtime -D</li>
<li>在装babel语法插件相关的包:npm i  @bable/procet-env @babel/plugin-transform-runtime @babel/plugin-proposal-class-properties -D</li>
<li>在项目根目录中,创建babel配置文件babel.config.js并初始化基本配置如下</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>],
    <span class="hljs-attr">plugins</span>: [@babel/plugin-transform-runtime<span class="hljs-string">','</span> @babel/plugin-proposal-<span class="hljs-class"><span class="hljs-keyword">class</span>-<span class="hljs-title">properties</span>']
    &#125;

</span><span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>在webpack.config.js的module->rules数组中,添加loader规则:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//exclude为排除项,表示babel-loader 不需要处理node_modules中的js文件</span>
&#123;<span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.js$/</span>, use: <span class="hljs-string">'babel-loader'</span>, <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>]&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">5.7配置vue-loader</h3>
<ol>
<li>运行npm i vue-laoder vue-template-compiler -D</li>
<li>在项目根目录中,创建babel配置文件babel.config.js并初始化基本配置如下</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> VueLoaderPlugin = requier(<span class="hljs-string">'vue-laoder/lib/plugin'</span>)
<span class="hljs-attr">module</span>:&#123;
    <span class="hljs-attr">rules</span>: [
        ...<span class="hljs-comment">//其他规则</span>
        &#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>, laoder: <span class="hljs-string">'vue-laoder'</span> &#125;
    ],
    
 &#125;
<span class="hljs-attr">plugins</span>: [
          ... <span class="hljs-comment">//其他</span>
          <span class="hljs-keyword">new</span> VueLoaderPlugin() <span class="hljs-comment">//确保引入这个插件</span>
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">6.webpack打包发布</h2>
<p>上线之前需要通过webpack将应用进行整体打包,可以通过package.json 文件配置打包命令</p>
<p>在package.json文件中配置webpack打包命令,该命令默认加载项目目录中的webpack.config.js配置文件</p>
<pre><code class="hljs language-js copyable" lang="js"> 
     <span class="hljs-string">"script "</span>: &#123;
         <span class="hljs-comment">// 用于打包的命令</span>
         <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack -p"</span>,
         <span class="hljs-comment">// 用于开发调试的命令</span>
         <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --open --host 127.0.0.1 --post 3000"</span>,
     &#125;
     
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            