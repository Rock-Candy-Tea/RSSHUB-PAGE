
---
title: React脚手架跨域代理配置
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 17:21:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ea6f91b21a442fcb00f3698e983f346~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>    本文介绍关于在<strong>react脚手架</strong>开发过程中碰到<strong>跨域问题</strong>该如何进行处理，不进行跨域原因的阐述。</p>
<p>    <strong>react脚手架</strong>中可通过两种方式配置代理：</p>
<ol>
<li>在<strong>package.json</strong>文件中配置；</li>
<li>新建<strong>setupProxy.js</strong>文件进行配置</li>
</ol>
<h3 data-id="heading-0">package.json配置代理</h3>
<p>    假设我们要在<strong>本地3000端口</strong>向<strong>本地5000端口</strong>发起请求，完整的请求地址为：**<a href="http://localhost:5000/study**,%E7%94%B1%E4%BA%8E%E6%B5%8F%E8%A7%88%E5%99%A8%E7%9A%84**%E5%90%8C%E6%BA%90%E7%AD%96%E7%95%A5**%EF%BC%8C%E4%B8%8D%E5%90%8C%E7%9A%84%E7%AB%AF%E5%8F%A3%E4%BA%A4%E4%BA%92%E4%BC%9A%E4%BA%A7%E7%94%9F%E8%B7%A8%E5%9F%9F" target="_blank" rel="nofollow noopener noreferrer">http://localhost:5000/study**,由于浏览器的**同源策略**，不同的端口交互会产生跨域</a>:</p>
<p><img alt class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ea6f91b21a442fcb00f3698e983f346~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们可以通过在<strong>package.json</strong>文件中进行配置，打开这个文件，在最后添加一行代理的代码:</p>
<pre><code class="copyable">"proxy": "http://localhost:5000"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体代码内容如下：</p>
<pre><code class="copyable">&#123;  "name": "todolist",  "version": "0.1.0",  "private": true,  "dependencies": &#123;    "@testing-library/jest-dom": "^5.11.4",    "@testing-library/react": "^11.1.0",    "@testing-library/user-event": "^12.1.10",    "axios": "^0.21.1",    "react": "^17.0.1",    "react-dom": "^17.0.1",    "react-scripts": "4.0.3",    "web-vitals": "^1.0.1"  &#125;,  "scripts": &#123;    "start": "react-scripts start",    "build": "react-scripts build",    "test": "react-scripts test",    "eject": "react-scripts eject"  &#125;,  "eslintConfig": &#123;    "extends": [      "react-app",      "react-app/jest"    ]  &#125;,  "browserslist": &#123;    "production": [      ">0.2%",      "not dead",      "not op_mini all"    ],    "development": [      "last 1 chrome version",      "last 1 firefox version",      "last 1 safari version"    ]  &#125;,  "proxy": "http://localhost:5000"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    添加这行代码表示当客户端向端口为5000的服务端发起请求，会由代理转发这次请求，代理端和服务器不受浏览器同源策略的限制，不会产生跨域问题，返回结果如下图：</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcf341ad4c6a4ce1a53a29859244fb12~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>**问题：**但是这种方式配置代理有一定的局限性，当客户端需要向多个不同服务器发起请求时，<strong>proxy</strong>只能允许配置一个代理，因此便有了以下方式。</p>
<h3 data-id="heading-1">setupProxy文件配置代理</h3>
<p>    我们可以在<strong>src目录</strong>下新建一个名为**"setupProxy.js"<strong>的文件，<strong>react脚手架</strong>会自动识别该文件的配置并编译，在该文件中，只能使用</strong>Common JS，<strong>无法使用</strong>ES6**高级语法，否则会无法识别并报错，让我们看看如何配置。</p>
<p>    首页我们需要引入<code>**http-proxy-middleware**</code>这个模块，该模块不需要我们手动下载，项目中自带该模块，直译为：**http代理中间件，**具体代码如下:</p>
<pre><code class="copyable">const proxy = require('http-proxy-middleware')

module.exports = function(app) &#123;
  app.use(
    proxy('/api1', &#123;  //api1是需要转发的请求(所有带有/api1前缀的请求都会转发给5000)
      target: 'http://localhost:5000', //配置转发目标地址(能返回数据的服务器地址)
      changeOrigin: true, //控制服务器接收到的请求头中host字段的值
      /*
      changeOrigin设置为true时，服务器收到的请求头中的host为：localhost:5000
      changeOrigin设置为false时，服务器收到的请求头中的host为：localhost:3000
      changeOrigin默认值为false，但我们一般将changeOrigin值设为true
      */
      pathRewrite: &#123;'^/api1': ''&#125; //去除请求前缀，保证交给后台服务器的是正常请求地址(必须配置)
    &#125;),
    proxy('/api2', &#123; 
      target: 'http://localhost:5001',
      changeOrigin: true,
      pathRewrite: &#123;'^/api2': ''&#125;
    &#125;)
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 说明：</p>
<ol>
<li>
<p>优点：可以配置多个代理，可以灵活的控制请求是否走代理。</p>
</li>
<li>
<p>缺点：配置繁琐，前端请求资源时必须加前缀。</p>
</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            