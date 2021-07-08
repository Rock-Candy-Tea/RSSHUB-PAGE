
---
title: '小白手把手教你封装Vue组件，并使用npm发布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a2b92e97a1044edb75caaaa419937ab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 02:39:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a2b92e97a1044edb75caaaa419937ab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">缘由</h1>
<p>作为giser使用到了给地图添加图例这个功能，图例的标准是固定的所以就想发布到npm上以后方便使用。
<strong>说明</strong>：前端新手+第一次发布npm包 一步一步都会说明
通过下午阅读很多大佬写的总结出来的 其中一些理解可能不对 欢迎指正</p>
<h1 data-id="heading-1">搭建模板 构建vue组件</h1>
<p>开发组件我们使用 webpack-simple ：（看大佬们的 还没开始学webpack）</p>
<p><code>vue init webpack-simple <project-name></code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a2b92e97a1044edb75caaaa419937ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">框架搭建</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9177d9dd1859438a859b29c0fed1d930~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1 中主要是需要发布的组件
2 是输出文件 输出发布的组件</p>
<p>这里代码就不详细说了 就说明一下这些index.js文件</p>
<h2 data-id="heading-3">文件说明</h2>
<h3 data-id="heading-4">package下的index.js</h3>
<pre><code class="hljs language-import copyable" lang="import">
//定义插件 插件有个install方法 传入两个参数
//SipLegend.name 组件名 SipLegend 组件
SipLegend.install = Vue => Vue.component(SipLegend.name, SipLegend);


//导出
export default SipLegend;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里重点说下问题<strong>我遇到的问题</strong></p>
<p>代码Vue.component(SipLegend.name, SipLegend); 中SipLegend.name 指的是需要在sip-legend.vue组件中 写上组件名 不然会报个错误</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19ed63b3304e4d4b989e7e21d7e7fdd2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">src目录下的index 主要是组件的输出口</h3>
<pre><code class="hljs language-import copyable" lang="import">// ...如果还有的话继续添加

const components = [
    SipLegend
  // ...如果还有的话继续添加
]

const install = function(Vue, opts = &#123;&#125;) &#123;
  components.map(component => &#123;
    Vue.component(component.name, component);
  &#125;)
&#125;

/* 支持使用标签的方式引入 */
if (typeof window !== 'undefined' && window.Vue) &#123;
  install(window.Vue);
&#125;

export default &#123;
  install,
  SipLegend
  // ...如果还有的话继续添加
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">引用组件</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/089ebe8b0de74b6180a6fecb6cc148d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dea7479c5a374eea884b533ec22f614d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>成功</p>
<h3 data-id="heading-7">有了输出 还要有入口</h3>
<p>入口在main.js中</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09ff7cba0cca4ddd8c50ea2b2886a3db~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
通过这样导出组件</p>
<h3 data-id="heading-8">webpack.config.js配置</h3>
<pre><code class="hljs language-var copyable" lang="var">var webpack = require('webpack')

// 执行环境
//process 当前node进程 process.env包含着关于系统环境的信息，但是process.env中并不存在NODE_ENV这个东西。
//NODE_ENV是一个用户自定义的变量 用于判断生产环境或开发环境
const NODE_ENV = process.env.NODE_ENV

module.exports = &#123;
  // 根据不同的执行环境配置不同的入口
  entry: NODE_ENV == 'development' ? './src/main.js' : './src/index.js',
  output: &#123;
    // 修改打包出口，在最外级目录打包出一个 index.js 文件，我们 import 默认会指向这个文件
    path: path.resolve(__dirname, './dist'),
    publicPath: '/dist/',
    filename: 'gis-ui.js',
    library: 'gis-ui', // 指定的就是你使用require时的模块名
    libraryTarget: 'umd', // libraryTarget会生成不同umd的代码,可以只是commonjs标准的，也可以是指amd标准的，也可以只是通过script标签引入的
    umdNamedDefine: true // 会对 UMD 的构建过程中的 AMD 模块进行命名。否则就使用匿名的 define
  &#125;,
  //主要是上面一块
  module: &#123;
    rules: [
      &#123;
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      &#125;,      &#123;
        test: /\.vue$/,
        loader: 'vue-loader',
        options: &#123;
          loaders: &#123;
          &#125;
          // other vue-loader options go here
        &#125;
      &#125;,
      &#123;
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      &#125;,
      &#123;
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: &#123;
          name: '[name].[ext]?[hash]'
        &#125;
      &#125;
    ]
  &#125;,
  resolve: &#123;
    alias: &#123;
      'vue$': 'vue/dist/vue.esm.js'
    &#125;,
    extensions: ['*', '.js', '.vue', '.json']
  &#125;,
  devServer: &#123;
    historyApiFallback: true,
    noInfo: true,
    overlay: true
  &#125;,
  performance: &#123;
    hints: false
  &#125;,
  devtool: '#eval-source-map'
&#125;

if (process.env.NODE_ENV === 'production') &#123;
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin(&#123;
      'process.env': &#123;
        NODE_ENV: '"production"'
      &#125;
    &#125;),
    new webpack.optimize.UglifyJsPlugin(&#123;
      sourceMap: true,
      compress: &#123;
        warnings: false
      &#125;
    &#125;),
    new webpack.LoaderOptionsPlugin(&#123;
      minimize: true
    &#125;)
  ])
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">package.js配置 文件打包</h3>
<pre><code class="copyable">  &#123;
      "name": "gisui", //npm包名
      "main": "dist/gis-ui.js",//build打包文件名
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">准备发布</h2>
<h3 data-id="heading-11">本地测试</h3>
<p><code>npm run build</code> 打包
使用<code>npm back</code>打包成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f623d0031ccd49c0a7b56f8bf6ff9287~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在所需要的项目中<code> npm i 地址/gisui-1.0.0.tgz</code>
之后就 像组件一样在main引入</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ce5b55be12449a49292484e594a8563~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
需要的地方使用</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68be6f2119c4417fb7f7c94fe3c6d85b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">发布</h3>
<p>需要到npm 官网注册
注册成功需要验证邮箱
之后</p>
<p>npm login   // 登陆</p>
<p>npm publish // 发布</p>
<p>就完成了！</p>
<h3 data-id="heading-13">一个小问题</h3>
<p>发布完成后 再到发布的vue组件中启动发现报错
最后发现是webpack.config.js配置的问题 这里面的配置是打包发布的配置 需要重新改成原来的配置才能正常启动。暂时不知道什么问题，毕竟webpack还没学，之后会学习一下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4eefc8c5f2d430e912b368a9e20b39b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>感谢：<a href="https://juejin.cn/post/6844903636808499214#heading-5" target="_blank" title="https://juejin.cn/post/6844903636808499214#heading-5">juejin.cn/post/684490…</a> 参考</p>
</blockquote></div>  
</div>
            