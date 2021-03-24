
---
title: 'TypeError_ this.getOptions is not a function'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/bVcOBqz'
author: segmentfault
comments: false
date: 2021-03-24 12:18:23
thumbnail: 'https://segmentfault.com/img/bVcOBqz'
---

<div>   
<h2>一 背景</h2><p>在vue2项目上使用less,安装了 less 和 less-laoder之后，编译项目的时候提示下面问题：<br><strong>Module build failed (from ./node_modules/less-loader/dist/cjs.js): TypeError: this.getOptions is not a function</strong></p><h2>二 排查问题</h2><p>在网上搜索，有文章说是less-loader版本太高了，安装低版本的就没问题啦，比如5.0.0。看了下我当前安装的是less-loader@8.0.0,降级到less-loader@v5.0.0之后也确实好了。但是事情真的那么简单吗？为什么高版本不可以？为什么是5.0.0?</p><p>我去看之前跑的没有出问题的项目版本是v7.2.0，这个版本也没有问题，后来再仔细搜索发现是高版本的less-loader的配置变了。<br>之前使用less-loader <a href="https://www.webpackjs.com/loaders/less-loader/" rel="nofollow">建议配置</a>:</p><pre><code class="sh">// webpack.config.js
module.exports = &#123;
    ...
    module: &#123;
        rules: [&#123;
            test: /.less$/,
            use: [&#123;
                loader: "style-loader"
            &#125;, &#123;
                loader: "css-loader"
            &#125;, &#123;
                loader: "less-loader", 
                options: &#123;
                    strictMath: true,
                    noIeCompat: true
                &#125;
            &#125;]
        &#125;]
    &#125;
&#125;;</code></pre><p>注意用的是<code>options:&#123;&#125;</code>。<br> 但是在8版本，<a href="https://github.com/webpack-contrib/less-loader" rel="nofollow">官方给出</a>的是：</p><pre><code class="sh">module.exports = &#123;
 module: &#123;
   rules: [
     &#123;
       test: /.less$/i,
       use: [
         &#123;
           loader: "style-loader",
         &#125;,
         &#123;
           loader: "css-loader",
         &#125;,
         &#123;
           loader: "less-loader",
           options: &#123;
             lessOptions: &#123;
               strictMath: true,
             &#125;,
           &#125;,
         &#125;,
       ],
     &#125;,
   ],
 &#125;,
&#125;;</code></pre><p>注意这里的是<code>options: &#123;lessOptions:&#125;&#125;</code></p><p>发现8 版本有一次大的升级：<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVcOBqz" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>之前我们使用<code>~</code>来解决路径引用问题，现在8版本解决掉了这个bug,可以不再依赖<code>～</code>了，随之带来的是配置文件字段发生了改变。</p><h2>三 解决问题</h2><p>好了，既然已经知道是8版本配置发生了变化，那就好解决了。</p><h3>根本解决</h3><p>把之前的options稍加修改，加上<code>lessOptions</code>:</p><pre><code class="sh">module.exports = &#123;
    ...
    module: &#123;
        rules: [&#123;
            test: /.less$/,
            use: [
               ...
               &#123;
                loader: "less-loader", 
                options: &#123;
                    + lessOptions: &#123;
                        strictMath: true,
                        noIeCompat: true
                    + &#125;
                &#125;
            &#125;]
        &#125;]
    &#125;
&#125;;</code></pre><h3>vue-cli</h3><p>如果你是使用vue-cli创建的项目，可以在vue.config.js上自定义less-loader配置：</p><pre><code class="js">chainWebpack: config => &#123;
 config.module
 .rule('less')
 .use('less-loader')
 .loader('less-loader')
 .options(&#123;
    lessOptions: &#123;
    /**less-loader 配置 */
      strictMath: true,
      noIeCompat: true
    &#125;
 &#125;)</code></pre><h3>快速解决</h3><p>最简单的解决方法就是降低版本了，8的上一个版本是7.3.0，所以我们想在不改变配置的情况下解决问题，降级到7.3.0就OK：</p><pre><code class="sh">  npm install less-loader@7.3.0 --save-dev</code></pre>  
</div>
            