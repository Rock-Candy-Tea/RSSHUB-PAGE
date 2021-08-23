
---
title: 'TypeScript重写axios之项目诞生'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6095c0119e0a4c339fe013a311852f80~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 17:48:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6095c0119e0a4c339fe013a311852f80~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">TypeScript重写axios之项目诞生</h1>
<h2 data-id="heading-1">项目初始化</h2>
<blockquote>
<p>我们通过<code>TypeScript library starter</code>来创建一个TS项目，它是一个开源的<code>TypeScript</code>开发基础库的脚手架工具，可以帮助我们快速初始化一个<code>TypeScript</code>项目，我们可以去它的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falexjoverm%2Ftypescript-library-starter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alexjoverm/typescript-library-starter" ref="nofollow noopener noreferrer">官网</a>进行学习和使用它。</p>
</blockquote>
<h3 data-id="heading-2">一、使用方式</h3>
<pre><code class="copyable">git clone https://github.com/alexjoverm/typescript-library-starter.git 项目名称
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在这里初始化项目</p>
<pre><code class="copyable"># 拉下项目基础模板
git clone https://github.com/alexjoverm/typescript-library-starter.git ts-axios-pro
# 切换到项目目录下
cd ts-axios-pro
# 进行项目install安装相关插件
npm install 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">二、项目目录</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6095c0119e0a4c339fe013a311852f80~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> 在编写代码之前，我们先来了解下<code>axios</code>的工作流程，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d692afb6a3845cc976bdbaf61c9ee20~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> 我们大概知道了axios的工作流程，当然如果你把源码看了，并且理解那是更好的，接下来我们先来写测试的例子,我们在跟目录下建立一个<code>examples</code>目录，在<code>examples</code>目录下建立一个<code>webpack.config.js</code>配置文件，在编写<code>webpack.config.js</code>文件之前，我们先安装几个插件：</p>
<ul>
<li><code>npm install express -D</code> 安装express框架，编写服务端代码</li>
<li><code>npm install body-parser -D</code> 解决post请求</li>
<li><code>npm install webpack@4.17 webpack-cli@3 webpack-dev-server -D</code> 安装webpack</li>
<li><code>npm install ts-loader@5 tslint-loader -D</code>一个是解析以.ts结尾的文件，一个ts的eslint</li>
</ul>
<pre><code class="copyable">npm install express -D
npm install body-parser -D
npm install webpack@4.17 webpack-cli@3 webpack-dev-server -D 
npm install ts-loader@5 tslint-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装成功后，对<code>examples/webpack.config.js</code>进行配置</p>
<pre><code class="copyable"># webpack.config.js

const fs = require('fs');
const path = require('path');
const webpack = require('webpack');

module.exports = &#123;
    /**
     * 我们会在 examples 目录下建多个子目录
     * 我们会把不同章节的 demo 放到不同的子目录中
     * 每个子目录的下会创建一个 app.ts
     * app.ts 作为 webpack 构建的入口文件
     * entries 收集了多目录个入口文件，并且每个入口还引入了一个用于热更新的文件
     * entries 是一个对象，key 为目录名
     */
    entry: fs.readdirSync(__dirname).reduce((entries, dir) => &#123;
        const fullDir = path.join(__dirname, dir);
        const entry = path.join(fullDir, "app.ts");
        if (fs.statSync(fullDir).isDirectory() && fs.existsSync(entry)) &#123;
        entries[dir] = entry;
        &#125;
        return entries;
    &#125;, &#123;&#125;),
    /**
     * 根据不同的目录名称，打包生成目标 js，名称和目录名一致
    */
    output: &#123;
        path: path.join(__dirname, "__build__"),
        filename: "[name].js",
        publicPath: "/__build__/"
    &#125;,
    resolve: &#123;
        extensions: [".ts", ".tsx", ".js"]
    &#125;,
    module: &#123;
        rules: [
          &#123;
            test: /.ts$/,
            enforce: "pre",
            use: "tslint-loader",
            exclude: /node_modules/
          &#125;,
          &#123;
            test: /.tsx?$/,
            use: "ts-loader",
            exclude: /node_modules/
          &#125;
        ]
    &#125;,
    devServer: &#123;
        noInfo: true,
        overlay: true,
        open: true,
        proxy: &#123;
          // 配置跨域
          "/api/": &#123;
            target: "http://localhost:3000",
            ws: true,
            changOrigin: true
          &#125;
        &#125;
    &#125;,
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin()
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">服务端代码</h2>
<p>在根目录下建立<code>server</code>文件夹，在server文件下建立<code>server.js</code></p>
<pre><code class="copyable">const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const router = express.Router();

// 使用body-parser中间件
app.use(bodyParser.urlencoded(&#123; extended: false &#125;));
app.use(bodyParser.json());


router.get('/api/base/get', (req, res) => &#123;
    res.json(&#123;
        msg: 'hello world'
    &#125;)
&#125;)

app.use(router)

const port = process.env.PORT || 3000;
module.exports = app.listen(port, () => &#123;
    console.log(`Server listening on http://localhost:$&#123;port&#125;, Ctrl+C to stop`)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>examples</code>下建立第一个例子：我们取名为<code>base</code>，它是一个文件夹，它里面包含<code>index.html</code>和<code>app.ts</code></p>
<pre><code class="copyable"># app.ts
import axios from '../../src/axios'
axios(&#123;
    method: "get",
    url: "/api/base/get",
    params: &#123;
      a: 1,
      b: 2
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"># index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Base demo</title>
</head>
<body>
<script src="/__build__/base.js"></script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们在<code>package.json</code>设置相关命令：</p>
<pre><code class="copyable">// 在scripts里面加入两行命令
"scripts":&#123;
  "server": "node server/server.js",
  "dev": "webpack-dev-server --config './examples/webpack.config.js' --hot"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们执行<code>npm run dev</code>可以让demo跑起来，同时让服务端启动<code>npm run server</code>访问<code>http://localhost:8080/</code>,这样一个小的demo就成功了，下一篇文档我们开始编写<code>axios</code>的源码了。。</p></div>  
</div>
            