
---
title: 'webpack打包用Babel处理es6'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7633'
author: 掘金
comments: false
date: Sun, 30 May 2021 02:28:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=7633'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天来梳理下webpack中关于js打包的处理方式，首先我们都知道需要处理es6+的编译就要用到babel,那什么是babel呢？</p>
<p>Babel是JavaScript编译器，能将ES6代码转换成ES5代码，让我们开发过程中放⼼使⽤JS新特性⽽不⽤担
⼼兼容性问题。但是默认的Babel只⽀持let等⼀些基础的语法转换，<strong>Promise等特性无法转换，这时候需要借助@babel/polyfill</strong>，把es的新特性都装进来，来弥补低版本浏览器中缺失的特性。</p>
<p>1、安装babel</p>
<pre><code class="copyable">npm i babel-loader @babel/core @babel/preset-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、插件说明</p>
<p>这里我们先说明下babel-loader,他不是用来做es6转义的，它是babel与webpack的通信桥梁，我们需要转义需要用到@babel/preset-env，这里安装的@babel/core其实就是bable(目前的babel版本是7.X),下面是来自babel官网的关于不同类型的语法转移插件：</p>
<pre><code class="copyable">es6+ ----->@babel/presets-env --> es5
flow语法 ---->@babel/presets-flown -->es5
jsx语法 ---->@babel/preset-react -->es5
ts语法 ---->@babel/preset-ts -->es5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、一般我们会在webpack.config.js文件中做如下配置：</p>
<pre><code class="copyable">&#123;
    test: /\.js$/,
    exclude: /node_modules/,
    use: &#123;
        loader: "babel-loader",
        options: &#123;
            presets: ["@babel/preset-env"]
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、关于@babel/polyfill使用</p>
<p>上文提到了babel不能转义的es6+的特性，这里我们就需要一个垫片插件来辅助转义的实现。</p>
<p>4.1  安装（因为在生产环境也需要依赖使用）</p>
<pre><code class="copyable">npm install --save @babel/polyfill
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.2  使用</p>
<pre><code class="copyable">//index.js 顶部
import "@babel/polyfill";
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式打包会发现打包的体积增大了很多，因为polyfill默认会把所有的特性注入进来，那么能不能按需加载呢？这里我们就要使用到babel7的新功能，useBuiltIns,它有三个参数可选：</p>
<pre><code class="copyable">//需要在 webpack 的⼊⼝⽂件⾥ import "@babel/polyfill" ⼀次。 babel
会根据你的使⽤情况导⼊垫⽚，没有使⽤的功能不会被导⼊相应的垫⽚
useBuiltIns: "entry",  
// 按需注⼊,不需要 import ，全⾃动检测，但是要安装 @babel/polyfill 
useBuiltIns: "usage",  
 //如果你 import "@babel/polyfill" ，它不会排除掉没有使⽤的垫⽚，程序体积会庞⼤。(不推荐)
useBuiltIns: "false" 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这个特性要怎么配置呢，有以下两种方式：</p>
<pre><code class="copyable">// 第一种：在webpack.config.js中配置
options: &#123;
    presets: [
        [
            "@babel/preset-env",
            &#123;
                targets: &#123;
                    edge: "17",
                    firefox: "60",
                    chrome: "67",
                    safari: "11.1"
                &#125;,
            corejs: 2,//新版本需要指定核⼼库版本
            useBuiltIns: "usage"//按需注⼊
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 第二种: 新建.babelrc⽂件，把options部分移⼊到该⽂件中
&#123;
    presets: [
        [
            "@babel/preset-env",
            &#123;
                targets: &#123;
                    edge: "17",
                    firefox: "60",
                    chrome: "67",
                    safari: "11.1"
                &#125;,
                corejs: 2, //新版本需要指定核⼼库版本
                useBuiltIns: "usage" //按需注⼊
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：这里有个需要注意的问题是如果你使用了比较高版本的，比如es11这种特性，就需要使用corejs 3.x的版本了，他会比2多一些新特性。</p>
<p>5、既然上文提到了vue\react的语法转义，那下面就来解析下使用方式：</p>
<p>5.1  安装babel与react转换的插件</p>
<pre><code class="copyable">npm install --save-dev @babel/preset-react
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在babelrc⽂件⾥添加：</p>
<pre><code class="copyable">"@babel/preset-react"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.2 安装babel与vue转换的插件</p>
<pre><code class="copyable">npm install -D vue-loader vue-template-compiler
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// webpack.config.js
const &#123; VueLoaderPlugin &#125; = require('vue-loader')

module.exports = &#123;
  module: &#123;
    rules: [
      // ... 其它规则
      &#123;
        test: /\.vue$/,
        loader: 'vue-loader'
      &#125;
    ]
  &#125;,
  plugins: [
    // 请确保引入这个插件！
    new VueLoaderPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上仅为自己学习过程中的了解，欢迎指正！</p></div>  
</div>
            