
---
title: 'webpack5 和 webpack4 的区别有哪些 ？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85782f62e154a2d9971cce084d61103~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 15:51:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85782f62e154a2d9971cce084d61103~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1、Tree Shaking</h4>
<p>作用： 如果我们的项目中引入了 lodash 包，但是我只有了其中的一个方法。其他没有用到的方法是不是冗余的？此时 tree-shaking 就可以把没有用的那些东西剔除掉，来减少最终的bundle体积。</p>
<blockquote>
<p>usedExports : true, 标记没有用的叶子</p>
</blockquote>
<blockquote>
<p>minimize: true, 摇掉那些没有用的叶子</p>
</blockquote>
<pre><code class="copyable">  // webpack.config.js中
  module.exports = &#123;
     optimization: &#123;
       usedExports: true, //只导出被使用的模块
       minimize : true // 启动压缩
     &#125;
  &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 tree shaking 只支持 esmodule ，如果你打包出来的是 commonjs，此时 tree-shaking 就失效了。不过当前大家都用的是 vue，react 等框架，他们都是用 babel-loader 编译，以下配置就能够保证他一定是 esmodule</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e85782f62e154a2d9971cce084d61103~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>webpack5的 mode=“production” 自动开启 tree-shaking。</p>
<h4 data-id="heading-1">2、压缩代码</h4>
<h5 data-id="heading-2">1.webpack4</h5>
<blockquote>
<p>webpack4 上需要下载安装 terser-webpack-plugin 插件，并且需要以下配置：</p>
</blockquote>
<pre><code class="copyable">const TerserPlugin = require('terser-webpack-plugin')

module.exports = &#123; 
// ...other config
optimization: &#123;
  minimize: !isDev,
  minimizer: [
    new TerserPlugin(&#123;
      extractComments: false, 
      terserOptions: &#123; 
        compress: &#123; 
          pure_funcs: ['console.log'] 
        &#125;
      &#125;
    &#125;) ]
 &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">2.webpack5</h5>
<p>内部本身就自带 js 压缩功能，他内置了 terser-webpack-plugin 插件，我们不用再下载安装。而且在 mode=“production” 的时候会自动开启 js 压缩功能。</p>
<blockquote>
<p>如果你要在开发环境使用，就用下面：</p>
</blockquote>
<pre><code class="copyable">  // webpack.config.js中
  module.exports = &#123;
     optimization: &#123;
       usedExports: true, //只导出被使用的模块
       minimize : true // 启动压缩
     &#125;
  &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">3.js 压缩失效问题</h5>
<p>当你下载 optimize-css-assets-webpack-plugin ，执行 css 压缩以后，你会发现 webpack5 默认的 js 压缩功能失效了。先说 optimize-css-assets-webpack-plugin 的配置：</p>
<blockquote>
<p>npm install optimize-css-assets-webpack-plugin -D</p>
</blockquote>
<pre><code class="copyable">module.exports = &#123; 
  optimization: &#123; 
    minimizer: [ 
      new OptimizeCssAssetsPlugin() 
    ]
  &#125;,
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>此时的压缩插件 optimize-css-assets-webpack-plugin 可以配置到 plugins 里面去，也可以如图配置到到 optimization 里面。区别如下：</p>
</blockquote>
<p>配置到 plugins 中，那么这个插件在任何情况下都会工作。 而配置在 optimization 表示只有 minimize 为 true 的时候才能工作。</p>
<blockquote>
<p>当安装 optimize-css-assets-webpack-plugin 以后你去打包会发现原来可以压缩的 js 文件，现在不能压缩了。原因是你指定的压缩器是</p>
</blockquote>
<p>optimize-css-assets-webpack-plugin 导致默认的 terser-webpack-plugin 就会失效。解决办法如下：</p>
<blockquote>
<p>npm install terser-webpack-plugin -D</p>
</blockquote>
<pre><code class="copyable"> optimization: &#123;
    minimizer: [
      new TerserPlugin(&#123;
        extractComments: false,
        terserOptions: &#123;
          compress: &#123; pure_funcs: ['console.log'] &#125;,
        &#125;,
      &#125;),
      new OptimiazeCssAssetPlugin(),
    ]
  &#125;,
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即便在 webpack5 中，你也要像 webpack4 中一样使用 js 压缩。</p>
<h5 data-id="heading-5">4.注意事项</h5>
<p>在webpack5里面使用 optimize-css-assets-webpack-plugin 又是会报错，因为官方已经打算要废除了，请使用替换方案：</p>
<blockquote>
<p>npm i css-assets-webpack-plugin -D</p>
</blockquote>
<h4 data-id="heading-6">3、合并模块</h4>
<blockquote>
<p>普通打包只是将一个模块最终放到一个单独的立即执行函数中，如果你有很多模块，那么就有很多立即执行函数。concatenateModules 可以要所有的模块都合并到一个函数里面去。</p>
</blockquote>
<p>optimization.concatenateModules = true</p>
<p>配置如下：</p>
<pre><code class="copyable">module.exports = &#123;
  optimization: &#123;
    usedExports: true,
    concatenateModules: true,
    minimize: true
  &#125;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时配合 tree-shaking 你会发现打包的体积会减小很多。</p>
<h4 data-id="heading-7">4、副作用 sideEffects</h4>
<blockquote>
<p>webpack4 新增了一个 sideEffects 的功能，容许我们通过配置来标识我们的代码是否有副作用。</p>
</blockquote>
<blockquote>
<p>这个特性只有在开发 npm 包的时候用到</p>
</blockquote>
<p>副作用的解释： 在utils文件夹下面有index.js文件，用于系统导出utils里面其他文件，作用就是写的少， 不管 utils 里面有多少方法，我都只需要引入 utils 即可。</p>
<pre><code class="copyable">// utils/index.js
  export * from './getXXX.js';
  export * from './getAAA.js';
  export * from './getBBB.js';
  export * from './getCCC.js';
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> // 在其他文件使用 getXXX 引入
  import &#123;getXX&#125; from '../utils'
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，如果文件 getBBB 在外界没有用到，而 tree-shaking 又不能把它摇掉咋办？这个 getBBB 就是副作用。你或许要问 tree-shaking 为什么不能奈何他？原因就是：他在 utils/index.js 里面使用了。只能开启副作用特性。如下：</p>
<pre><code class="copyable">// package.json中
&#123;
  name：“项目名称”,
  ....
  sideEffects: false
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// webpack.config.js

module.exports = &#123;
  mode: 'none',
  ....
  optimization: &#123;
    sideEffects: true
  &#125;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>副作用开启：</p>
<blockquote>
<p>(1)optimization.sideEffects = true 开启副作用功能</p>
</blockquote>
<blockquote>
<p>(2)package.json 中设置 sideEffects : false 标记所有模块无副作用</p>
</blockquote>
<p>说明： webpack 打包前都会检查项目所属的 package.json 文件中的 sideEffects 标识，如果没有副作用，那些没有用到的模块就不需要打包，反之亦然。此时，在webpack.config.js 里面开启 sideEffects。</p>
<h4 data-id="heading-8">5、webpack 缓存</h4>
<h6 data-id="heading-9">1.webpack4 缓存配置</h6>
<p>支持缓存在内存中</p>
<blockquote>
<p>npm install hard-source-webpack-plugin -D</p>
</blockquote>
<pre><code class="copyable">const HardSourceWebpackPlugin = require('hard-source-webpack-plugin') 

module.exports = &#123; 
plugins: [
  // 其它 plugin... 
  new HardSourceWebpackPlugin(), 
] &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">2. webpack5 缓存配置</h6>
<p>webpack5 内部内置了 cache 缓存机制。直接配置即可。</p>
<blockquote>
<p>cache 会在开发模式下被设置成 type： memory 而且会在生产模式把cache 给禁用掉。</p>
</blockquote>
<pre><code class="copyable">// webpack.config.js
module.exports= &#123;
  // 使用持久化缓存
  cache: &#123;
    type: 'filesystem'，
    cacheDirectory: path.join(__dirname, 'node_modules/.cac/webpack')
  &#125;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>type 的可选值为： memory 使用内容缓存，filesystem 使用文件缓存。</p>
</blockquote>
<blockquote>
<p>当 type=filesystem的时候设置cacheDirectory才生效。用于设置你需要的东西缓存放在哪里？</p>
</blockquote>
<h4 data-id="heading-11">6、对loader的优化</h4>
<blockquote>
<p>webpack 4 加载资源需要用不同的 loader</p>
</blockquote>
<ul>
<li>raw-loader 将文件导入为字符串</li>
<li>url-loader 将文件作为 data url 内联到 bundle文件中</li>
<li>file-loader 将文件发送到输出目录中</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6abf7458ff1649fc81bbe2943887e539~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>webpack5 的资源模块类型替换 loader</p>
</blockquote>
<ul>
<li>asset/resource 替换 file-loader(发送单独文件)</li>
<li>asset/inline 替换 url-loader （导出 url）</li>
<li>asset/source 替换 raw-loader（导出源代码）</li>
<li>asset</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/280823192f3e4348af944c3f6a3ec4fc~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fguides%2Fasset-modules%2F" title="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fguides%2Fasset-modules%2F" target="_blank">webpack5</a></p>
<h4 data-id="heading-12">7、启动服务的差别</h4>
<h6 data-id="heading-13">1.webpack4 启动服务</h6>
<p>通过 webpack-dev-server 启动服务</p>
<h6 data-id="heading-14">2.webpack5 启动服务</h6>
<p>内置使用 webpack serve 启动，但是他的日志不是很好，所以一般都加都喜欢用 webpack-dev-server 优化。</p>
<h4 data-id="heading-15">8. 模块联邦（微前端）</h4>
<blockquote>
<p>webpack 可以实现 应用程序和应用程序之间的引用。</p>
</blockquote>
<h4 data-id="heading-16">9.devtool的差别</h4>
<p>sourceMap需要在 webpack.config.js里面直接配置 devtool 就可以实现了。而 devtool有很多个选项值，不同的选项值，不同的选项产生的 .map 文件不同，打包速度不同。</p>
<p>一般情况下，我们一般在开发环境配置用“cheap-eval-module-source-map”，在生产环境用‘none’。</p>
<p>devtool在webpack4和webpack5上也是有区别的</p>
<blockquote>
<p>v4: devtool: 'cheap-eval-module-source-map'</p>
</blockquote>
<blockquote>
<p>v5: devtool: 'eval-cheap-module-source-map'</p>
</blockquote>
<h4 data-id="heading-17">10.热更新差别</h4>
<blockquote>
<p>webpack4设置</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/171d53563efd40439c8f61969ca1d12d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>webpack5 设置</p>
</blockquote>
<p>如果你使用的是bable6，按照上述设置，你会发现热更新无效，需要添加配置：</p>
<pre><code class="copyable">  module.hot.accept('需要热启动的文件',(source)=>&#123;
     //自定义热启动
  &#125;)
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前最新版的babel里面的 babel-loader已经帮我们处理的热更新失效的问题。所以不必担心，直接使用即可。</p>
<p>如果你引入 mini-css-extract-plugin 以后你会发现 样式的热更新也会失效。</p>
<p>只能在开发环境使用style-loader，而在生产环境用MinicssExtractPlugin.loader。 如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/944a741135ea41478f335d1a9cd2ba5d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">11、使用 webpack-merge 的差别</h4>
<blockquote>
<p>webpack4 导入</p>
</blockquote>
<p>const merge = require('webpack-merge);</p>
<blockquote>
<p>webpack 5 导入</p>
</blockquote>
<p>const &#123;merge&#125; = require('webpack-merge');</p>
<p>12、 使用 copy-webpack-plugin 的差别</p>
<pre><code class="copyable">//webpack.config.js
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = &#123;
  plugins: [
    // webpack 4
    new CopyWebpackPlugin(['public']),
    
    // webpack 5
    new CopyWebpackPlugin(&#123;
      patterns: [&#123;
        from: './public',
        to: './dist/public'
      &#125;]
    &#125;)
  ]
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack5 支持的新版本里面需要配置的更加清楚。</p></div>  
</div>
            