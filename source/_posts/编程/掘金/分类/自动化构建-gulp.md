
---
title: '自动化构建-gulp'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4552'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 21:18:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=4552'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1. 基本使用</h4>
<ul>
<li>yarn init -y</li>
<li>yarn add gulp --dev(gulp是作为开发依赖安装的，grunt是以生产环境依赖安装的)</li>
<li>根目录下新建gulpfile.js</li>
<li>gulp4.0之前的写法（如下），被保留，但不推荐这种写法</li>
</ul>
<pre><code class="copyable">const gulp = require('gulp')

gulp.task('bar', done => &#123;
    console.log('bar working~')
    done() // 标记任务结束
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>gulp4.0之后的写法（直接导出任务的形式），推荐</li>
</ul>
<pre><code class="copyable">exports.foo = done => &#123;
    console.log('aaa')
    done() // 标记任务结束
&#125;
exports.default = done => &#123;
    console.log('tag')
    done()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>运行命令：yarn gulp bar/yarn gulp foo/yarn gulp</li>
</ul>
<h4 data-id="heading-1">2. gulp的组合任务</h4>
<ul>
<li>除了创建普通任务以外，gulp还提供了series和paralled两个用来创建组合任务的api</li>
<li>series用来创建串行任务，parallel用来创建并行任务</li>
<li>执行命令：yarn gulp foo/yarn gulp bar</li>
<li>series和parallel在实际创建工作流中非常有用，例如，我们编译css任务和编译js任务是互不干扰的，那这两个任务就可以通过并行的任务去执行，可以提高构建效率；部署的时候，需要先执行编译任务，这时候可以通过series这种串行的api去执行任务</li>
</ul>
<pre><code class="copyable">const &#123; series, parallel &#125; = require('gulp')
// 未被导出的函数可以认为是私有任务
const task1 = done => &#123;
    setTimeout(() => &#123;
        console.log('task1 working~')
        done()
    &#125;, 1000)
&#125;

const task2 = done => &#123;
    setTimeout(() => &#123;
        console.log('task2 working')
        done()
    &#125;, 1000)
&#125;

const task3 = done => &#123;
    setTimeout(() => &#123;
        console.log('tag', 'task3 working~')
        done()
    &#125;, 1000)
&#125;

exports.foo = series(task1, task2, task3)
exports.bar = parallel(task1, task2, task3)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3. gulp的异步任务</h4>
<ul>
<li>异步任务的实现方式：回调、promise、async、文件流</li>
</ul>
<pre><code class="copyable">const fs = require('fs')
// 回调
exports.callback = done => &#123;
    console.log('callback task~', '')
    done()
&#125;
exports.callback_error = done => &#123;
    console.log('callback task error~')
    // 标记任务发生错误
    done(new Error('error'))
&#125;
// promise
exports.promise = () => &#123;
    console.log('promise task finished~')
    return Promise.resolve()
&#125;
exports.promise_error = () => &#123;
    console.log('promise task error~')
    return Promise.reject(new Error('promsie error'))
&#125;
// async
exports.async = async () => &#123;
    await timeout(1000)
    console.log('tag', 'async task~')
&#125;
// 文件流（常用）
exports.stream = () => &#123;
    const readStream = fs.createReadStream('package.json')
    const writeSteam = fs.createWriteStream('temp.txt')
    readStream.pipe(writeSteam)
    return readStream
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4. gulp构建过程核心工作原理</h4>
<ul>
<li>构建过程大多数都是将文件读出来，然后进行转换操作，最后写入到另外一个位置</li>
<li>通过 读取流--》转换流 --》写入流 的流程实现</li>
<li>接下来通过node底层api来实现压缩css的过程(以下有css代码展现)</li>
</ul>
<pre><code class="hljs language-js--gulpfile.js copyable" lang="js--gulpfile.js">const fs = require('fs')
const &#123;Transform&#125; = require('stream')

exports.default = () => &#123;
    // 读取流
    const readStream = fs.createReadStream('normalize.css')
    // 转换流
    const transform = new Transform(&#123;
        transform: (chunk, encoding, callback) => &#123;
            console.log('chunk', chunk)
            const input = chunk.toString()
            console.log('chunked', input)
            const output = input.replace(/\s+/g, '').replace(/\/\*.+?\*\//g, '')
            callback(null, output)
        &#125;
    &#125;)
    // 写入流
    const writeStream = fs.createWriteStream('normalize.min.csss')
    readStream
      .pipe(transform)  
      .pipe(writeStream)
    return readStream
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */</span>

<span class="hljs-comment">/**
 * Restore the focus styles unset by the previous rule.
 */</span>

<span class="hljs-selector-tag">button</span>:-moz-focusring,
[type=<span class="hljs-string">"button"</span>]:-moz-focusring,
[type=<span class="hljs-string">"reset"</span>]:-moz-focusring,
[type=<span class="hljs-string">"submit"</span>]:-moz-focusring &#123;
  outline: <span class="hljs-number">1px</span> dotted ButtonText;
&#125;

<span class="hljs-comment">/**
 * Correct the padding in Firefox.
 */</span>

<span class="hljs-selector-tag">fieldset</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0.35em</span> <span class="hljs-number">0.75em</span> <span class="hljs-number">0.625em</span>;
&#125;

<span class="hljs-comment">/**
 * 1. Correct the text wrapping in Edge and IE.
 * 2. Correct the color inheritance from `fieldset` elements in IE.
 * 3. Remove the padding so developers are not caught out when they zero out
 *    `fieldset` elements in all browsers.
 */</span>

<span class="hljs-selector-tag">legend</span> &#123;
  <span class="hljs-attribute">box-sizing</span>: border-box; <span class="hljs-comment">/* 1 */</span>
  <span class="hljs-attribute">color</span>: inherit; <span class="hljs-comment">/* 2 */</span>
  <span class="hljs-attribute">display</span>: table; <span class="hljs-comment">/* 1 */</span>
  <span class="hljs-attribute">max-width</span>: <span class="hljs-number">100%</span>; <span class="hljs-comment">/* 1 */</span>
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>; <span class="hljs-comment">/* 3 */</span>
  <span class="hljs-attribute">white-space</span>: normal; <span class="hljs-comment">/* 1 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5. gulp文件操作api</h4>
<ul>
<li>gulp中提供了专用去创建读取流和写入流的api，相比于底层node的api更强大也更容易使用。至于负责文件加工的转换流，绝大多数都是使用独立的插件来实现</li>
<li>gulp 通过src方法创建读取流，再借助插件提供的转换流实现文件加工，最后提供gulp提供的dest方法实现一个写入流，从而写入到目标文件</li>
<li>yarn add gulp-clean-css --dev 安装此依赖作用：压缩css</li>
<li>yarn add gulp-rename --dev 此依赖作用：重命名扩展名</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; src, dest &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp'</span>)
<span class="hljs-keyword">const</span> cleanCss = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-clean-css'</span>)
<span class="hljs-keyword">const</span> rename = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-rename'</span>)

<span class="hljs-built_in">exports</span>.default = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> src(<span class="hljs-string">'*.css'</span>)
      .pipe(cleanCss())
      .pipe(rename(&#123; <span class="hljs-attr">extname</span>: <span class="hljs-string">'.min.css'</span> &#125;))
      .pipe(dest(<span class="hljs-string">'dist'</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">6. gulp案例（02-01-03-12-zce-gulp-demo）- 样式编译</h4>
<ul>
<li>根目录下的public,就是我们在开发网页应用当中那些不需要被加工的直接去拷贝到我们最终生成的文件夹的一些文件</li>
<li>图片和字体文件压缩：图片中是有一些二进制的原数据信息，那些信息在生产环境是没有必要的，这些信息都可以通过自动化构建的过程给删除掉，从而压缩文件的体积</li>
<li>js 将es6转换成es5</li>
<li>yarn add gulp --dev</li>
<li>yarn add gulp-sass --dev 安装gulp-sass的时候，内部会去安装node-sass,node-sass是C++的模块，内部会有对C++程序集的依赖，所以一些二进制的包需要通过外国的站点去下载，所以有的时候会下载不下来，可以单独为node-sass配置一个镜像</li>
<li>gulp-sass五版本以上需要手动安装sass,用法与4不同</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; src, dest &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp'</span>)
<span class="hljs-keyword">const</span> sass = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-sass'</span>)(<span class="hljs-built_in">require</span>(<span class="hljs-string">'sass'</span>))
<span class="hljs-comment">// 4.xx版本这么写就可以const sass = require('gulp-sass')</span>

<span class="hljs-keyword">const</span> style = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> src(<span class="hljs-string">'src/assets/styles/**'</span>, &#123; <span class="hljs-attr">base</span>: <span class="hljs-string">'src'</span>&#125;)
  .pipe(sass(&#123; <span class="hljs-attr">outputStyle</span>: <span class="hljs-string">'expanded'</span>&#125;)) <span class="hljs-comment">// outputStyle用于展开css</span>
  .pipe(dest(<span class="hljs-string">'dist'</span>))
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  style
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">7. gulp案例 - 脚本编译</h4>
<ul>
<li>yarn add gulp-babel --dev</li>
<li>yarn add @babel/core @babel/preset-env --dev</li>
<li>preset-env默认会把es6模块的新特性都会做转换</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; src, dest &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp'</span>)
<span class="hljs-keyword">const</span> sass = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-sass'</span>)
<span class="hljs-keyword">const</span> babel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'gulp-babel'</span>)

<span class="hljs-keyword">const</span> style = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> src(<span class="hljs-string">'src/assets/styles/*.scss'</span>, &#123; <span class="hljs-attr">base</span>: <span class="hljs-string">'src'</span>&#125;)
  .pipe(sass(&#123; <span class="hljs-attr">outputStyle</span>: <span class="hljs-string">'expanded'</span>&#125;))
  .pipe(dest(<span class="hljs-string">'dist'</span>))
&#125;

<span class="hljs-keyword">const</span> script = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> src(<span class="hljs-string">'src/assets/scripts/*.js'</span>, &#123;<span class="hljs-attr">base</span>: <span class="hljs-string">'src'</span>&#125;)
  .pipe(babel(&#123; <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>]&#125;))
  .pipe(dest(<span class="hljs-string">'dist'</span>))
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  style,
  script
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">8. gulp案例 - 页面模板编译</h4>
<ul>
<li>模板引擎插件 yarn add gulp-swig --dev</li>
<li>可以自定义data放到swig配置项里，实现全局动态渲染模板</li>
</ul>
<pre><code class="copyable">const &#123; src, dest, series, parallel &#125; = require('gulp')
const sass = require('gulp-sass')
const babel = require('gulp-babel')
const swig = require('gulp-swig')

const style = () => &#123;
  return src('src/assets/styles/*.scss', &#123; base: 'src'&#125;)
  .pipe(sass(&#123; outputStyle: 'expanded'&#125;))
  .pipe(dest('dist'))
&#125;

const script = () => &#123;
  return src('src/assets/scripts/*.js', &#123;base: 'src'&#125;)
  .pipe(babel(&#123; presets: ['@babel/preset-env']&#125;))
  .pipe(dest('dist'))
&#125;

const page = () => &#123;
  return src('src/*.html', &#123;base: 'src'&#125;)
  .pipe(swig(&#123; data &#125;))
  .pipe(dest('dist'))
&#125;

const compile = parallel(style, script, page)

module.exports = &#123;
  compile
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">9. gulp案例 - 图片和字体文件转换、其他文清除</h4>
<ul>
<li>yarn add gulp-imagemin --dev 图片是无损压缩，也就是说看到的结果是不会受影响的，只是删除了一些原数据的信息</li>
<li>yarn add del --dev 清除文件</li>
<li>yarn add gulp-load-plugins --dev 自动加载插件</li>
</ul>
<pre><code class="copyable">const &#123; src, dest, series, parallel &#125; = require('gulp')
const del = require('del')

const loadPlugins = require('gulp-load-plugins')
const plugins = loadPlugins()

// const plugins.sass = require('gulp-sass')
// const plugins.babel = require('gulp-babel')
// const plugins.swig = require('gulp-swig')
// const plugins.imagemin = require('gulp-imagemin')
const data = &#123;&#125;

// 不只可以返回pipe的形式，还支持返回promise,del方法本身返回的就是promise
const clean = () => &#123;
  return del(['dist'])
&#125;

const style = () => &#123;
  return src('src/assets/styles/*.scss', &#123; base: 'src'&#125;)
  .pipe(plugins.sass(&#123; outputStyle: 'expanded'&#125;))
  .pipe(dest('dist'))
&#125;

const script = () => &#123;
  return src('src/assets/scripts/*.js', &#123;base: 'src'&#125;)
  .pipe(plugins.babel(&#123; presets: ['@babel/preset-env']&#125;))
  .pipe(dest('dist'))
&#125;

const page = () => &#123;
  return src('src/*.html', &#123;base: 'src'&#125;)
  .pipe(plugins.swig(&#123; data &#125;))
  .pipe(dest('dist'))
&#125;

const image = () => &#123;
  return src('src/assets/images/**', &#123; base: 'src' &#125;)
  .pipe(plugins.imagemin())
  .pipe(dest('dist'))
&#125;
const font = () => &#123;
  return src('src/assets/fonts/**', &#123; base: 'src'&#125;)
  .pipe(plugins.imagemin())
  .pipe(dest('dist'))
&#125;

const extra = () => &#123;
  return src('public/**', &#123; base: 'public'&#125;)
  .pipe(dest('dist'))
&#125;

const compile = parallel(style, script, page, image, font)
const build = series(clean, parallel(compile, extra))

module.exports = &#123;
  clean,
  compile,
  build
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">10. gulp案例 - 开发服务器</h4>
<ul>
<li>yarn add browser-sync --dev 此模块可以提供给我们一个开发服务器，相对于我们普通使用express创建的web服务器,browser-sync有更强大的一些功能，它支持我们修改代码过后自动热更新到浏览器当中</li>
<li>打包好的html文件中，可能会有一些node_modules里文件的引用，本地开发的时候可以找到是因为在serve里做了一个路由的映射。但是这些文件不会拷贝到dist目录，导致上线的时候文件找不到。解决方案：使用useref插件，useref会自动处理html里的构建注释（自动将构建注释的开始标签和结束标签中间引入的文件最终打包到一个文件当中）
<ul>
<li>使用方法：yarn add gulp-useref --dev</li>
</ul>
<pre><code class="copyable">const useref = () => &#123;
    return src('dist/*.html', &#123;base: 'dist'&#125;)
    .pipe(plugins.useref(&#123;searchPath: ['dist', '.']&#125;)) // 从dist目录和根目录查找
    .pipe(dest('dist'))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>build的时候已经把image和font压缩了，还有html css js需要压缩
<ul>
<li>yarn add gulp-htmlmin --dev 压缩html</li>
<li>yarn add gulp-uglify --dev 压缩js</li>
<li>yarn add gulp-clean-css --dev 压缩css</li>
<li>yarn add gulp-if --dev 判断读取流是哪种类型的文件</li>
</ul>
</li>
<li>vscode 折叠到最高层级 ctrl+k ctrl+1</li>
</ul>
<pre><code class="copyable">const &#123; src, dest, parallel, series, watch &#125; = require('gulp')

const del = require('del')
const browserSync = require('browser-sync')

const loadPlugins = require('gulp-load-plugins')

const plugins = loadPlugins()
const bs = browserSync.create()

const data = &#123;
  menus: [
    &#123;
      name: 'Home',
      icon: 'aperture',
      link: 'index.html'
    &#125;,
    &#123;
      name: 'Features',
      link: 'features.html'
    &#125;,
    &#123;
      name: 'About',
      link: 'about.html'
    &#125;,
    &#123;
      name: 'Contact',
      link: '#',
      children: [
        &#123;
          name: 'Twitter',
          link: 'https://twitter.com/w_zce'
        &#125;,
        &#123;
          name: 'About',
          link: 'https://weibo.com/zceme'
        &#125;,
        &#123;
          name: 'divider'
        &#125;,
        &#123;
          name: 'About',
          link: 'https://github.com/zce'
        &#125;
      ]
    &#125;
  ],
  pkg: require('./package.json'),
  date: new Date()
&#125;

const clean = () => &#123;
  return del(['dist', 'temp'])
&#125;

const style = () => &#123;
  return src('src/assets/styles/*.scss', &#123; base: 'src' &#125;)
    .pipe(plugins.sass(&#123; outputStyle: 'expanded' &#125;))
    .pipe(dest('temp'))
    .pipe(bs.reload(&#123; stream: true &#125;))
&#125;

const script = () => &#123;
  return src('src/assets/scripts/*.js', &#123; base: 'src' &#125;)
    .pipe(plugins.babel(&#123; presets: ['@babel/preset-env'] &#125;))
    .pipe(dest('temp'))
    .pipe(bs.reload(&#123; stream: true &#125;))
&#125;

const page = () => &#123;
  return src('src/*.html', &#123; base: 'src' &#125;)
    .pipe(plugins.swig(&#123; data, defaults: &#123; cache: false &#125; &#125;)) // 防止模板缓存导致页面不能及时更新
    .pipe(dest('temp'))
    .pipe(bs.reload(&#123; stream: true &#125;))
&#125;

const image = () => &#123;
  return src('src/assets/images/**', &#123; base: 'src' &#125;)
    .pipe(plugins.imagemin())
    .pipe(dest('dist'))
&#125;

const font = () => &#123;
  return src('src/assets/fonts/**', &#123; base: 'src' &#125;)
    .pipe(plugins.imagemin())
    .pipe(dest('dist'))
&#125;

const extra = () => &#123;
  return src('public/**', &#123; base: 'public' &#125;)
    .pipe(dest('dist'))
&#125;

const serve = () => &#123;
  watch('src/assets/styles/*.scss', style)
  watch('src/assets/scripts/*.js', script)
  watch('src/*.html', page)
  // watch('src/assets/images/**', image)
  // watch('src/assets/fonts/**', font)
  // watch('public/**', extra)
  watch([
    'src/assets/images/**',
    'src/assets/fonts/**',
    'public/**'
  ], bs.reload)

  bs.init(&#123;
    notify: false,
    port: 2080,
    // open: false,
    // files: 'dist/**',
    server: &#123;
      baseDir: ['temp', 'src', 'public'],
      routes: &#123;
        '/node_modules': 'node_modules'
      &#125;
    &#125;
  &#125;)
&#125;

const useref = () => &#123;
  return src('temp/*.html', &#123; base: 'temp' &#125;)
    .pipe(plugins.useref(&#123; searchPath: ['temp', '.'] &#125;))
    // html js css
    .pipe(plugins.if(/\.js$/, plugins.uglify()))
    .pipe(plugins.if(/\.css$/, plugins.cleanCss()))
    .pipe(plugins.if(/\.html$/, plugins.htmlmin(&#123;
      collapseWhitespace: true,
      minifyCSS: true,
      minifyJS: true
    &#125;)))
    .pipe(dest('dist'))
&#125;

const compile = parallel(style, script, page)

// 上线之前执行的任务
const build =  series(
  clean,
  parallel(
    series(compile, useref),
    image,
    font,
    extra
  )
)

const develop = series(compile, serve)

module.exports = &#123;
  clean,
  build,
  develop
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            