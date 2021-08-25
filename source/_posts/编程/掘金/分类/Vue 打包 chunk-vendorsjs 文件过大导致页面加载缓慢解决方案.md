
---
title: 'Vue 打包 chunk-vendors.js 文件过大导致页面加载缓慢解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5586647501f1485a8e80c7226de3dcaa~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 00:38:10 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5586647501f1485a8e80c7226de3dcaa~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一、<code>chunk-vendors.js</code> 简介</h4>
<ul>
<li>
<p>顾名思义，<code>chunk-vendors.js</code> 是捆绑所有不是自己的模块，而是来自其他方的模块的捆绑包，它们称为第三方模块或供应商模块。</p>
</li>
<li>
<p>通常，它意味着（仅和）来自项目 <code>/node_modules</code> 目录的所有模块，会将所有 <code>/node_modules</code> 中的第三方包打包到 <code>chunk-vendors.js</code> 中。</p>
</li>
<li>
<p>将所有的第三方包集中到一个文件，自然也会出现文件过大的问题。</p>
</li>
</ul>
<h4 data-id="heading-1">二、<code>chunk-vendors.js</code> 文件大小分析</h4>
<ul>
<li>
<p>新创建一个 <code>vue</code> 项目，通过打包之后运行到服务器，然后访问得到 <code>chunk-vendors.js</code> 为 <code>182 B</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5586647501f1485a8e80c7226de3dcaa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>通过安装第三方组件，将 <code>chunk-vendors.js</code> 文件增大，安装第三方组件之后需要在 <code>main.js</code> 中导入，重新运行 <code>npm run build</code> 进行打包。</p>
<ul>
<li>
<p><code>npm i --save ant-design-vue</code>，安装完打包后瞬间到了 <code>1.9 MB</code>！</p>
<pre><code class="copyable">import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';
Vue.use(Antd);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52dee162cb7445cd9dd81a329618cc25~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><code>npm i element-ui -S</code>，安装完打包后瞬间到了 <code>2.6 MB</code>！</p>
<pre><code class="copyable">import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6069ad765c4344faab8d2fe6b1c0d81e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>不要看后面的 <code>Time</code> 时间那么短，因为这是内网本机访问快，如果到了外网就跟服务器带宽、性能有关了，但是文件这么大，加载慢，那就需要拆开来进行分块加载，不是一味升级服务器解决问题，毕竟要钱的！</p>
</li>
<li>
<p>附带还未进行分块分包加载时，打包得到的文件目录(<code>js</code>、<code>css</code>)</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b76518446dbb40669a8e356a785aba5a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/036ef5bff1a044ff899177a7b249f9e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/695ba30ecadf4a8c802346144a40022e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h4 data-id="heading-2">三、方式一：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fzz00008888%2Farticle%2Fdetails%2F119893222" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/zz00008888/article/details/119893222" ref="nofollow noopener noreferrer">compression-webpack-plugin 插件解决方案</a></h4>
<h4 data-id="heading-3">四、方式二</h4>
<ul>
<li>
<p>还有种是通过 <code>webpack</code> 前端配置，将第三方包分开打包，这样不会将所有第三方包都打包到 <code>chunk-vendors.js</code> 文件，如果第三方包中存在过大的文件，那也会很大。</p>
</li>
<li>
<p>所以可以两者一起使用也是可以的，选择其中一种使用也可以，下面是两种一起使用，可以根据情况剔除选一种，或者都使用。</p>
<pre><code class="copyable">const path = require('path');

const webpack = require('webpack')
const CompressionWebpackPlugin = require('compression-webpack-plugin')
const productionGzipExtensions = ['js', 'css']
const isProduction = process.env.NODE_ENV === 'production'

module.exports = &#123;
  devServer: &#123;
    disableHostCheck: true
  &#125;,
  configureWebpack: &#123;
    resolve: &#123;
      alias: &#123;
        '@': path.resolve(__dirname, './src'),
        '@i': path.resolve(__dirname, './src/assets'),
      &#125;
    &#125;,
    plugins: [
      new webpack.IgnorePlugin(/^\.\/locale$/, /moment$/),
      // compression-webpack-plugin 插件配置，需要服务器配合配置
      new CompressionWebpackPlugin(&#123;
        algorithm: 'gzip',
        test: new RegExp('\\.(' + productionGzipExtensions.join('|') + ')$'),
        threshold: 10240,
        minRatio: 0.8
      &#125;),
      new webpack.optimize.LimitChunkCountPlugin(&#123;
        maxChunks: 5,
        minChunkSize: 100
      &#125;)
    ],
    // 开启分离 js
    optimization: &#123;
      runtimeChunk: 'single',
      splitChunks: &#123;
        chunks: 'all',
        maxInitialRequests: Infinity,
        minSize: 20000,
        cacheGroups: &#123;
          vendor: &#123;
            test: /[\\/]node_modules[\\/]/,
            name (module) &#123;
              // get the name. E.g. node_modules/packageName/not/this/part.js
              // or node_modules/packageName
              const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1]
              // npm package names are URL-safe, but some servers don't like @ symbols
              return `npm.$&#123;packageName.replace('@', '')&#125;`
            &#125;
          &#125;
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-4">五、其他方式</h4>
<ul>
<li>
<p>比如将有些大的 <code>js</code>、<code>css</code> 通过 <code>cdn</code> 的方式链接，可以多种方案配合一起使用的。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Flove314159%2Fp%2F14275666.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/love314159/p/14275666.html" ref="nofollow noopener noreferrer">其他参考方案</a></p>
</li>
</ul></div>  
</div>
            