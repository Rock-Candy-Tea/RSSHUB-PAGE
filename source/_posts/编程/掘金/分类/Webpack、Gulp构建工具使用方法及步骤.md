
---
title: 'Webpack、Gulp构建工具使用方法及步骤'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3344'
author: 掘金
comments: false
date: Fri, 05 Mar 2021 07:12:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=3344'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、Webpack的使用方法</h3>
<blockquote>
<p>在项目中安装和配置webpack</p>
</blockquote>
<ol>
<li>运行npm install <code>webpack</code> <code>webpack-cli</code> -D 命令，安装webpack相关的包</li>
<li>在项目根目录下，创建名为 <code>webpack.config.js</code> 的 webpack 配置文件</li>
<li>在 webpack 的配置文件中，初始化如下基本配置:</li>
</ol>
<pre><code class="copyable">module.exports = &#123;
    mode: 'development'  //mode用来初始化构建模式(development-------开发模式; production----产品发布模式)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><code>npm init -y</code> 生成 package.json 配置文件，在配置文件中的 scripts 节点下，新增 dev 脚本如下:</li>
</ol>
<pre><code class="copyable">"scripts": &#123;
    "dev": "webpack"    //script 节点下的脚本，可以通过 npm run 执行
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>在终端中运行 <code>npm run dev</code> 命令， 启动 webpack 进行项目打包</li>
</ol>
<h4 data-id="heading-1">webpack的基本使用</h4>
<h6 data-id="heading-2">1.  配置打包的入口与出口</h6>
<p>通过改变 webpack.config.js 来设置入口/出口的js文件，如下：</p>
<pre><code class="copyable">const path = require("path");
module.exports = &#123;
    mode:"development",
    //设置入口文件路径
    entry: path.join(__dirname,"./src/xx.js"),
    //设置出口文件
    output:&#123;
        //设置路径
        path:path.join(__dirname,"./dist"),
        //设置输出文件名称
        filename:"bundle.js"
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-3">2. webpack自动打包</h6>
<p>A.安装自动打包功能的包:  webpack-dev-server<br>
输入命令: <code>npm install webpack-dev-server -D</code></p>
<p>B.修改package.json中的dev指令如下：</p>
<pre><code class="copyable">"scripts":&#123;
   "dev":"webpack-dev-server"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>C.将引入的js文件路径更改为：<br>
D.运行 <code>npm run dev</code>，进行打包<br>
E.打开网址查看效果：<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080" ref="nofollow noopener noreferrer">http://localhost:8080</a></p>
<h6 data-id="heading-4">3.  配置生成预览页面</h6>
<p>A.安装默认预览功能的包: html-webpack-plugin<br>
输入命令：
<code>npm install html-webpack-plugin -D</code> <br>
<code>npm install clean-webpack-plugin</code></p>
<p>B.修改 webpack.config.js 文件，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//导入包</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);

<span class="hljs-comment">//导入清除dist插件 不用手动每次去删除dist文件夹</span>
<span class="hljs-keyword">const</span> clearWebpackPlugin= <span class="hljs-built_in">require</span>(<span class="hljs-string">"clean-webpack-plugin"</span>); 

<span class="hljs-comment">//创建对象</span>
<span class="hljs-keyword">const</span> htmlPlugin = <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
    <span class="hljs-comment">//设置生成预览页面的模板文件</span>
    <span class="hljs-attr">template</span>:<span class="hljs-string">"./src/index.html"</span>,
    <span class="hljs-comment">//设置生成的预览页面名称,该文件存在于内存中，在目录中不显示</span>
    <span class="hljs-attr">filename</span>:<span class="hljs-string">"index.html"</span>
&#125;)

<span class="hljs-keyword">const</span>  clearPlugin=<span class="hljs-keyword">new</span> clearWebpackPlugin() <span class="hljs-comment">//导入模块清除dist插件不用手动每次去删除dist文件夹</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>C.继续修改webpack.config.js文件，添加plugins信息：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    ...
    <span class="hljs-attr">plugins</span>:[ htmlPlugin,clearPlugin ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自动打包的参数</p>
<pre><code class="copyable">//package.json中的配置
//--open 打包完成后自动打开浏览器、
//--host 配置IP地址
//--post 配置端口
"dev": "webpack-dev-server --open --host 127.0.0.1 --port 8888"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意!</code>
修改了配置文件就要重新运行命令： <code>npm run dev</code></p>
<h4 data-id="heading-5">Webpack 加载器</h4>
<h6 data-id="heading-6">1.通过loader打包非js模块</h6>
<p>在实际开发中，webpack默认只能打包处理以 .js 后缀名结尾的模块，其他非 .js 后缀名结尾的模块，webpack默认处理不了，需要调用 loader 加载器才可以正常打包，否则会报错！</p>
<h5 data-id="heading-7">1. 打包处理 css 文件</h5>
<ul>
<li>运行 <code>npm i style-loader css-loader -D</code> 命令，安装处理 css 文件的loader</li>
<li>在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//所有第三方文件模块的匹配规则</span>
<span class="hljs-attr">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>,use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>] &#125;
    ]
&#125;
<span class="hljs-comment">//test 表示匹配的文件类型; use表示对应要调用的 loader</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意</code></p>
<ul>
<li>use 数组中指定的 loader 顺序是固定的</li>
<li>多个 loader 的调用顺序是: 从后往前调用</li>
</ul>
<h5 data-id="heading-8">2. 打包处理 less 文件</h5>
<ul>
<li>运行 npm i less-loader less -D 命令</li>
</ul>
<pre><code class="copyable">module:&#123;
    rules:[
        &#123; test:/\less$/,use:['style-loader','css-loader','less-loader'] &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">3. 打包处理 scss 文件</h5>
<ul>
<li>运行 npm i sass-loader node-sass -D 命令</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.scss$/</span>,use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'sass-loader'</span>] &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">4. 配置 postCSS 自动添加 CSS 的兼容前缀</h5>
<ul>
<li>运行 npm i postcss-loader autoprefixer -D 命令</li>
<li>在项目根目录中创建 postcss 的配置文件 postcss.config.js,并初始化以下配置:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> autoprefixer = requier(<span class="hljs-string">'autoprefixer'</span>)    <span class="hljs-comment">//导入自动添加前缀的插件</span>
<span class="hljs-built_in">module</span>.exports = &#123;
   <span class="hljs-attr">plugins</span>: [ autoprefixer ] <span class="hljs-comment">//挂载插件</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在webpack.config.js 的 module -> rules 数组中，修改 css 中的 loader 规则如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>,use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>，<span class="hljs-string">'postcss-loader'</span>] &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">5. 打包样式表中的图片和字体文件</h5>
<ul>
<li>运行 npm i url-loader file-loader -D 命令</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        &#123; 
            <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.jpg|png|gif|bmp|ttf|eot|svg|woff|woff2$/</span>,
            use:<span class="hljs-string">'url-loader?limit=xxxx'</span>
        &#125;
    ]
&#125;
<span class="hljs-comment">// 其中 ? 之后的是 loader 的参数项</span>
limit 用来指定图片的大小，单位是字节(byte), 只有小于 limit 大小的图片，才会被转换为 base64 图片
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">6. 打包处理 js 文件中的高级语法</h5>
<ul>
<li>安装 beble 转换器相关的包: npm i babel-loader @babel/core @babel/runtime -D</li>
<li>安装 babel 语法插件相关的包: npm i @babel/preset-env @bable/plugin-transform-runtime @babel/plugin-proposal-class-properties -D</li>
<li>在项目根目录中，创建 babel 配置文件 babel.config.js,并初始化配置如下:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preser-env'</span>],
    <span class="hljs-attr">plugins</span>: [ <span class="hljs-string">'@bable/plugin-tranform-runtime'</span>,<span class="hljs-string">'@babel/plugin-proposal-class-properties'</span> ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        <span class="hljs-comment">//exclude 为排除项，表示 babel-loader 不需要处理 node_modules 中的 js 文件</span>
        &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.js$/</span>,use:<span class="hljs-string">'babel-loader'</span>,<span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span> &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">单文件组件 ----- 文件名.vue  (eg: App.vue)</h4>
<h5 data-id="heading-14">1. webpack 中配置 vue 组件的加载器</h5>
<ul>
<li>运行 npm i vue-loader vue-template-compiler -D 命令</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-keyword">const</span> VueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>)
    <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>:[
            &#123; <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.vue$/</span>,use:<span class="hljs-string">'vue-loader'</span> &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>:[ 
        <span class="hljs-comment">//其他插件</span>
        <span class="hljs-keyword">new</span> VueLoaderPlugin() 
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">2. webpack 项目中使用 vue</h5>
<ul>
<li>运行 npm i vue -S 安装 vue</li>
<li>在 src ->index.js 入口文件中，通过 import Vue from 'vue' 来导入 vue 构造函数</li>
<li>创建 vue 实例对象，并指定要控制的 el 区域</li>
<li>通过 render 函数 渲染 App 组件</li>
</ul>
<pre><code class="copyable">// 1. 导入 vue 构造函数
import Vue from 'vue'
// 2. 导入 App 根组件
import App from './App.vue'

const vm = new Vue(&#123;
    // 3. 指定 vm 实例要控制的页面区域
    el: '#app',
    // 4. 通过 render 函数，把指定的组件渲染到 el 区域中
    render: h=>h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h3 data-id="heading-16">Gulp的使用</h3>
<p>基于node平台开发的构建工具,步骤如下：</p>
<ol>
<li>使用npm install gulp下载gulp库文件</li>
<li>在项目根目录下建立gulpfile.js文件</li>
<li>重构项目下的文件结构，src目录存放源代码文件，dist目录存放构建后的文件</li>
<li>在gulpfile.js文件中编写任务</li>
<li>在命令工具中执行gulp任务</li>
</ol>
<h4 data-id="heading-17">二、Gulp提供的方法</h4>
<ol>
<li>gulp.task(): 建立gulp任务</li>
<li>gulp.src(): 获取要处理的文件</li>
<li>gulp.dest(): 输出文件</li>
<li>gulp.watch() :监控文件的变化</li>
</ol>
<pre><code class="copyable">// 引用gulp模块
const gulp = require('gulp');
/* 使用gulp.task()方法建立任务
1、任务的名称， 2、任务的回调函数 */
gulp.task('first', () => &#123;
    //获取要处理的文件
    gulp.src('./src/css/index.css')
        //将处理后的文件输出到dist目录
        .pipe(gulp.dest('dist/css'));
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命令窗口输入命令：<br>
npm install gulp-cli -g<br>
gulp first</p>
<h4 data-id="heading-18">Gulp插件</h4>
<p>(1)下载插件： npm install 插件名称;  (2)gulpfile.js文件中引入插件：require('插件名称');
(3)调用插件</p>
<ol>
<li>gulp-htmlmin: html文件压缩</li>
<li>gulp-less: less语法转换</li>
<li>gulp-csso: 压缩css</li>
<li>gulp-babel: JavaScript语法转换</li>
<li>gulp-uglify: 压缩混淆JavaScript</li>
<li>gulp-file-include: 公共文件包含</li>
<li>browsersync: 浏览器实时同步</li>
</ol>
<pre><code class="copyable"><!-- html文件压缩 -->
// 1.引入插件
const htmlmin = require('gulp-htmlmin');
//公共文件包含
const fileinclude = require('gulp-file-include');

//调用插件
gulp.task('htmlmin', () => &#123;
    gulp.src('./src/*.html')
        //抽取html文件中的公共代码  require('gulp-file-include');
        .pipe(fileinclude())
        //压缩html文件中的代码
        .pipe(htmlmin(&#123; collapseWhitespace: true &#125;))
        .pipe(gulp.dest('dist'))
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//css压缩 
//1、less语法转换 const less = require('gulp-less');
//2、css代码压缩 const csso = require('gulp-csso')
gulp.task('cssmin', () => &#123;
    // gulp.src('./src/css/*.less')
    //选择css目录下的所有less文件以及css文件
    gulp.src(['./src/css/*.less', './src/css/*.css'])
        //将less语法转换为css语法
        .pipe(less())
        //将css代码进行压缩
        .pipe(csso())
        //将处理的结果进行输出
        .pipe(gulp.dest('dist/css'))
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//js任务
//1、es6代码转换 const babel = require('gulp-babel');
//2、代码压缩 const uglify = require('gulp-uglify')
gulp.task('jsmin', () => &#123;
    gulp.src('./src/js/*.js')
        .pipe(babel(&#123;
            //他可以判断当前代码的运行环境 将代码转换成当前运行环境所支持的代码
            presets: ['@babel/env']
        &#125;))
        //压缩代码
        .pipe(uglify())
        .pipe(gulp.dest('dist/js'))
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//复制文件夹
gulp.task('copy', () => &#123;
    gulp.src('./src/images/*')
        .pipe(gulp.dest('dist/images'))

    gulp.src('./src/lib/*')
        .pipe(gulp.dest('dist/lib'))
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//构建任务                  
gulp.task('my-tasks', gulp.series('htmlmin', 'cssmin', 'jsmin', 'copy', () => &#123;

&#125;));
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            