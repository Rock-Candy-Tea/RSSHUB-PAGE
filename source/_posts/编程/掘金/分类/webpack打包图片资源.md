
---
title: 'webpack打包图片资源'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: ''
author: 掘金
comments: false
date: Fri, 02 Apr 2021 01:49:33 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">图片加载</h2>
<h3 data-id="heading-1">in Javascript</h3>
<p>webpack只能处理js模块，在js中加载图片模块时需要借助file-loader。如</p>
<pre><code class="copyable">//index.js
import photo from './../static/image/Chrome.png';
const image = new Image()
image.src = photo
document.body.appendChild(image)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack配置file-loader</p>
<pre><code class="copyable">module.exports = &#123;
  mode: 'production',
  module: &#123;
    rules: [
      &#123;
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          &#123;
            loader: 'file-loader',
            options: &#123;
              name: '[path][name].[ext]',
              publicPath: 'www.txx.com',
            &#125;,
          &#125;,
          // 'image-webpack-loader'
        ],
      &#125;,
    ],
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">file-loader 和 url-loader 的区别</h4>
<p>url-loader内部继承了file-loader，与file-loader不同的是：</p>
<ol>
<li>url-loader可以把较小的图片转化成base64数据，从而减少对图片资源的http请求。同时打包文件也会变大；</li>
<li>当图片大小超过设置的限制（limit）时，默认采用file-loader进行加载。fallback默认值“file-loader”；</li>
<li>所有file-loader的属性，url-loader均可以使用。例如publicPath设置图片公共地址（图片部署到CDN服务器）</li>
</ol>
<h3 data-id="heading-3">in CSS</h3>
<p>在css中使用图片时，如background直接指定图片路径即可。</p>
<pre><code class="copyable">.root&#123;
  width: 200px;
  height: 200px;
  background: url("./../static/image/webpack.jpg") 100%;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为css-loader对css中引用的图片进行了处理</p>
<h3 data-id="heading-4">in html</h3>
<p>html中通过 <img src=""> 标签直接使用图片时，需要借助html-withimg-loader。如</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="root"></div>
  <img src="./../static/image/eslint.jpeg" alt="eslint">
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack配置loader</p>
<pre><code class="copyable">module.exports = &#123;
  mode: 'production',
  module: &#123;
    rules: [
      &#123;
        test: /\.(htm|html)$/,
        exclude: /node_modules/,
        use: 'html-withimg-loader',
      &#125;
    ],
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，file-loader/url-laoder 的 esModule设置为false。自webpack2开始，内部就集成了tree shaking代码优化，只会加载引用了的模块，html的图片会被视作未引用的模块资源</p>
<h2 data-id="heading-5">图片压缩</h2>
<p>进过以上配置，我们已经可以成功地打包图片资源了，接下来我们要对图片资源进行压缩，在页面加载时减少响应时间。</p>
<p>目前主流的webpack图片压缩无非就是 image-webpack-loader 和 imagemin-webpack-plugin。一种是配置loader，一种是配置插件，参数配置也大同小异。个人倾向使用前者，下面就 image-webpack-loader 配置举例</p>
<pre><code class="copyable">module.exports = &#123;
  mode: 'production',
  module: &#123;
    rules: [
      &#123;
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          &#123;
            loader: 'file-loader',
            options: &#123;
              name: '[path][name].[ext]',
              publicPath: 'www.txx.com',
            &#125;,
          &#125;,
          &#123;
            loader: 'image-webpack-loader',
            options: &#123;
                disable: process.env.NODE_ENV !== 'production', //仅生产环境对图片进行压缩
                pngquant: &#123;
                  quality: [0.65, 0.90],
                  speed: 4
                &#125;,
            &#125;
          &#125;
        ],
      &#125;,
    ],
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>image-webpack-loader <a href="https://www.npmjs.com/package/image-webpack-loader" target="_blank" rel="nofollow noopener noreferrer">参数配置参考</a></p>
<h2 data-id="heading-6">雪碧图</h2>
<p>“雪碧图”又叫css精灵（css sprite），css图片合成技术。</p>
<p>当我们在开发中需要用到很多小图片的时候，比如菜单icon，悬浮icon等，相信大部分开发者直观的做法是直接下载UI稿中的切图，在项目中引入使用。是，这样做没错，但是作为一个直接面向客户的开发者，我们对自己的产品必须严格要求，做到性能最优。</p>
<p>假如我们的应用首屏需要加载很多小图片，也就是说除了html，js，css等请求外，还需要发送很多次http请求去下载图片资源，这显然会降低首屏加载速度，用户体验很差。那么，我们是否可以考虑把这些小图合并成一张大图，然后用css去定位截取使用呢？显然是可以的，这里我只提一下技术方案，不做具体实现demo了</p>
<h4 data-id="heading-7">图片合成</h4>
<p>首先我们要把这些小图合成一张大图，然后写css样式去扣。听起来很复杂，哈哈哈别怕，社区很强大，牛逼的人也很多，早就有大佬写了一套完整的工具去帮我们完成这些操作。</p>
<ul>
<li><a href="https://www.npmjs.com/package/webpack-spritesmith" target="_blank" rel="nofollow noopener noreferrer">webpack-spritesmith</a>完成图片合并和对应css样式导出；</li>
<li><a href="https://www.npmjs.com/package/image-webpack-loader" target="_blank" rel="nofollow noopener noreferrer">image-webpack-loader</a>压缩图片</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            