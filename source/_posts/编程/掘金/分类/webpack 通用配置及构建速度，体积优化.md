
---
title: 'webpack 通用配置及构建速度，体积优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62de46a14d424e789727358d48651953~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 23:22:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62de46a14d424e789727358d48651953~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近在学习webpack，记录一下学习的基础东西，以及项目构建的速度和体积的优化。</p>
<h1 data-id="heading-1">webpack基本配置</h1>
<p>基本配置之前写过一遍文章，不重新写啦，不了解请转<a href="https://juejin.cn/post/6904476635559362567" target="_blank" title="https://juejin.cn/post/6904476635559362567">webpack之小白篇</a>。</p>
<h2 data-id="heading-2">修改代码，自动编译</h2>
<ul>
<li>webpack --watch 不会刷新浏览器，开发环境打包后的js是存在磁盘中。</li>
</ul>
<p>package.json文件
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62de46a14d424e789727358d48651953~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
webpack.dev.js文件
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8226e13281e4df586627149ad829a1f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
注：webpack.dev.js // 开发环境配置  webpack.prod.js // 生成环境配置</p>
<ul>
<li>webpack-dev-server --open 会自动打开浏览器，需要与webpack.HotModuleReplacementPlugin()配合使用，代码变动，可以自动刷新浏览器。</li>
</ul>
<p>package.json文件
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a3b560ad9f1475b9923935a91297267~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
webpack.dev.js文件
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4eb7b72ac1e04eb0b71f90d2a495fe64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">热更新（HMR:Hot Module Replacement）原理</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7d6656b578c4fdabcfd918ec7ff7e0e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Webpack Complier将代码转化为bundle.js文件。</li>
<li>将bound.js文件传输Bounle Server，提供浏览器Browser访问。</li>
<li>当代码更新时，会出发HMR Server 将代码传入到HMR Runtime（通常以json形式）</li>
<li>HMR Runtime接受会更新代码，刷新浏览器。</li>
</ul>
<h2 data-id="heading-4">文件指纹</h2>
<p>打包输出的文件名的后缀，通常作为版本的管理，没有修改的文件，可以使用浏览器缓存，加速访问。</p>
<ul>
<li>hash：和整个项目有关，只要文件修改，整个项目构建的hash都会改变，通常图片和字体使用。</li>
<li>chunkhash:不同的entry有不同的chunkhash值，通常js文件使用。</li>
<li>contenthash：根据文件内容生成hash值，通常css使用。</li>
</ul>
<p>style-loader：是将css插入style标签，插入到头部，没有单独的css文件。
MiniCssExtractPlugin(filename:'[name][conetnthash:8].css').loader 将css提出单独的文件，link到头部。
webpack.prod.js
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8284eb5f0604f55962f54b472202484~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">代码压缩</h2>
<ul>
<li>js，webpack4使用了terser-webpack-plugin插件默认以及打包过了，uglifyjs-webpack-plugin打包es6会报错。</li>
<li>html，使用html-webpack-plugin（一个html模板对应一个html-webpack-plugin）</li>
<li>css，使用optimize-css-assets-webpack-plugin插件，与cssnano配合使用</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f70fd73035d4316bad5d6ac978f3ce5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">css3:自动添加浏览器前缀（aotuperfixer）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a67c47f5bf6344819dbe409526a8a7ee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">移动端css中的px转化为rem</h2>
<ul>
<li>rem：相对单位，（相对于根元素html的font-size）</li>
<li>px：绝对单元</li>
<li>px2rem:将px转为rem</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf5eb05e35a7419f9951c4dab47e50ad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>lib-flexible：动态的计算根元素的font-size</li>
</ul>
<p>在入口文件引入<code>import 'lib-flexible'</code></p>
<h2 data-id="heading-8">多页面应用（entry+html-webpack-plugin）</h2>
<p>动态的设置entry，html-plugin-webpack，使用glob库，glob.sync()可以同步的获取正则匹配的目录信息。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/763e5e9ab2fe45819030a7f0a679c41d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">source map 定位源代码</h2>
<p>开发环境中开启，生产环境上关闭。
webpack.prod.js
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4cfe67d0e6e432ab12e262fa38bfd93~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">优化构建时命令行日志显示</h2>
<p>webpack中stats：统计信息
使用friendly-errors-webpack-plugin插件，将stats设置为'error-only'
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cc589097ba1463b83faad05a9aad131~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bc49924a7114f6faa732286bd4f4b1a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">webpack进阶用法</h1>
<h2 data-id="heading-12">提取公共资源</h2>
<ul>
<li>将react，react-dom 等公用的库，通过cdn的方式引入，不打包进入到bounld.js,使用html-webpack-externals-plugin引入</li>
</ul>
<pre><code class="copyable">new HtmlWebpackExternalsPlugin(&#123;
 externals: [
    &#123;
      module: 'react',
      entry: 'https://unpkg.com/react@17/umd/react.production.min.js',
      global: 'react',
    &#125;,
  ],
&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过webpack4自带的splitchunk属性进行公共脚本分离，splitchunk也可以提取公共使用的自己封装的函数，但是需要多个打包入库同时使用，一个项目使用多次是不可以的。</li>
</ul>
<pre><code class="copyable">    optimization:&#123;
        splitChunk:&#123;
           minSize:0,
           cacheGroups:&#123;
                vendor:&#123; // 提取node_modules的公共资源
                    test:/[\\/]node_modules[\\/](react|react-dom)[\\/]/,
                    name:'vendor',
                    chunks:'all'
                &#125;,
                commons:&#123; // 提取node_modules以及自己写的公告函数。（需要多个打包入口引用了依赖和公共函数）
                    chunks:'all',
                    name:'commons',
                    minChunks:'2'
                &#125;
           &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">tree shaking （摇树优化）</h2>
<p>只支持es6语法。webpack4的production默认打开。
原因：对代码进行静态分析，而不是在代码运行的时候在分析哪些是没有用到的，在tree shaking阶段把无用的代码注释，在代码压缩的阶段删除无用代码。</p>
<p>利用es6模块的特点：</p>
<ul>
<li>import只能最为模块的顶层出现</li>
<li>import的模块名称只能是字符串常量（导入之后不能修改）</li>
<li>import binding 是immutable的（不能动态引入的）</li>
</ul>
<p>注：不能在代码中动态的require导入</p>
<p>DCE(dead code elimination)</p>
<ul>
<li>代码不可达</li>
<li>代码执行结果不会被用到</li>
<li>代码只会影响死变量（只写不读）</li>
</ul>
<h2 data-id="heading-14">Scope Hositing(/ˈhɔɪstɪŋ/)</h2>
<p>webpack4的production默认打开，必须使用es6语法，不支持cjs。</p>
<p>不开启Scope Hoisting会导致什么问题：</p>
<ul>
<li>大量的闭包函数代码，会导致构建之后代码体积变大</li>
<li>运行代码时创建的函数作用域变多，内存开销变大</li>
</ul>
<p>scope hoisting的原理：</p>
<p>对所有模块的代码按照引用顺序放在一个函数作用域里，适当的重命名一些变量放置变量名冲突。</p>
<p>对比：通过scope hositing处理代码之后，会减少函数声明代码和内存开销。</p>
<p>注：如果模块只是用一次，会直接内联在函数作用域里，吐过使用多次，将会重新创建一个新的函数作用域。</p>
<h2 data-id="heading-15">代码分割</h2>
<p>将所有的代码打包到一个文件中是不够有效的，特别是有些代码在某种特殊情况下才会用到，webpack可以将打包过的代码分割成多个chunks，当代码运行我们在进行加载。</p>
<h2 data-id="heading-16">webpack打包组件库</h2>
<p>简单的组件库rollup更适合</p>
<h3 data-id="heading-17">发布npm包</h3>
<ul>
<li>需要打包压缩版和非压缩版</li>
<li>需要支持AMD/CJS/ESM模块导入，把output的library设置为'umd'。</li>
</ul>
<h3 data-id="heading-18">webpack.config.js 配置</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ce8027157dc41eb8d6206def32bc6a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">npm发布步骤</h3>
<ul>
<li><code>npm login</code> // 登录</li>
<li><code>npm publish</code> // 发布包</li>
<li><code>npm version path</code> // 改bug打补丁</li>
<li><code>npm version minjor</code> // 做一个feature，升级一个小的版本号</li>
<li><code>npm version major</code>// 升级一个大版本</li>
</ul>
<h3 data-id="heading-20">语义化版本（Semantic Versioning）格式规范</h3>
<ul>
<li>主版本号：当做了不兼容的API的修改</li>
<li>此版本号：当做了向下兼容的功能性新增</li>
<li>修订号：当做了向下兼容的问题修正</li>
</ul>
<h3 data-id="heading-21">先行版本号</h3>
<ul>
<li>alpha：是内部测试版，一般不向外发布，会有很多bug，一般只是测试人用。</li>
<li>beta：也是测试版，这个阶段的版本相对于alpha版的改进，消除了严重的错误，但是还存在着缺陷，这个版本也会一直加入新的功能，在alpha版之后推出。</li>
<li>rc：系统平台上发行的候选版本，rc版不会再加入新的功能了，主要着重于排错。</li>
</ul>
<h2 data-id="heading-22">webpack构建速度</h2>
<p>speep-measure-webpack-plugin速度分析
作用：可以查看每个loader和插件的执行耗时时间，整个打包耗时。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43f098e8878c414986045dc41add68f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">项目速度提升</h3>
<p>1.使用高版本的webpack和node</p>
<p>2.多进程多实例构建</p>
<p>thread-loader(webpack4推荐使用)，每次webpack解析一个模块，thread-loader将会将它及它的依赖分配给worker线程中。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed90ae3d710a4888bba4f931be61948c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3. 多进程实例压缩</p>
<p>terser-webpack-plugin 设置paralled参数
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbe2430f259146edb62d6c7a0106086f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
4. 分包：预编译资源模块</p>
<p>使用dllPlugin，dllReferencePlugin插件，使用script引入打包好的dll文件。
创建webpack.dll.js文件
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1f10547b0c049248320acaa06fed19a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在package.json文件中
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c42e24213da404690d3ae38c9e41fa1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
执行<code>npm run dll</code>,就会生成公共包的文件。</p>
<p>在webpack.dev.js,webpack.prod.js配置即可（当打出多个文件时，每个文件都需要添加一个插件，文中只打包了一个文件）
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fb9febec77341e9bd7e5f925b438ac2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>5.利用缓存提升二次构建</p>
<ul>
<li>babel-laoader开启缓存</li>
<li>terser-webpack-plugin 开启缓存</li>
<li>使用hard-source-webpack-plugin</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/056bab01d98f41f297c01a8e7d62a47c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
6. 减少文件搜索范围
resolve.modules,resve.mainFields,resolve.extensions,resolve.alias配置。</p>
<h2 data-id="heading-24">webpack构建体积</h2>
<p>webpack-bundle-analyzer分析体积
作用：第三方依赖包大小，我们自己组件代码大小</p>
<h3 data-id="heading-25">项目体积优化</h3>
<p>1.图片压缩</p>
<p>使用image-webpack-loader</p>
<p>2.删除无用的css</p>
<ul>
<li>PurifyCSS:遍历代码，识别已经用到的css，使用purgecss-webpack-plugin（css不可以使用）</li>
<li>uncss:需要html使用jsdom加载，样式使用postcss解析，通过document.querySelect来识别html文件里面不存在的选择器。</li>
</ul>
<p>3.提取公共的资源模块</p>
<p>详见webpack速度提升的分包：预编译资源模块</p>
<h1 data-id="heading-26">总结</h1>
<p>webpack的实践及优化，整理知识点，后期学习继续添加。</p></div>  
</div>
            