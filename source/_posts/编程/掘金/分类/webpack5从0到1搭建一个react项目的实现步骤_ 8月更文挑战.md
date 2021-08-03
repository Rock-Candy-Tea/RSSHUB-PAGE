
---
title: 'webpack5从0到1搭建一个react项目的实现步骤_ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2319'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 02:55:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=2319'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是webpack</h1>
<p><strong>webpack</strong> 是一个用于现代 JavaScript 应用程序的 <em>静态模块打包工具</em>。当 webpack 处理应用程序时，它会在内部构建一个依赖图，此依赖图对应映射到项目所需的每个模块，并生成一个或多个 <em>bundle</em></p>
<h1 data-id="heading-1">安装webpack</h1>
<p>在文件根目录下</p>
<ul>
<li>npm init 生成一个package.json 文件</li>
<li>npm i  webpack  --模块打包库</li>
<li>npm i -D webpack-cli --命令行工具</li>
<li>npm i -D webpack-dev-server --一个小型的静态文件服务器。使用它，可以为webpack打包生成的资源文件提供Web服务。</li>
</ul>
<p>npm i -D html-webpack-plugin -- 简化了 HTML 文件的创建，以便为你的 webpack 包提供服务。
生成的packsge.json 文件</p>
<pre><code class="copyable">&#123;
  "name": "zerotoone",
  "version": "1.0.0",
  "description": "git init \r 生成一个packjson",
  "main": "index.js",
  "dependencies": &#123;
    "@babel/core": "^7.14.8",
    "@babel/preset-react": "^7.14.5",
    "babel-loader": "^8.2.2",
    "init": "^0.1.2",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "webpack": "^5.47.1"
  &#125;,
  "devDependencies": &#123;
    "html-webpack-plugin": "^5.3.2",
    "webpack-cli": "^4.7.2",
    "webpack-dev-server": "^3.11.2",
    "webpack-server": "^0.1.2"
  &#125;,
  "scripts": &#123;
    "start": "webpack serve",
    "build": "rm -rf dist/ && webpack",
    "test": "echo \"Error: no test specified\" && exit 1"
  &#125;,
  "author": "",
  "license": "ISC"
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在根目录下创建webpack.config.js 文件</p>
<pre><code class="copyable">const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = &#123;
    mode: 'development',
    module: &#123;
        rules: [
            &#123;
                test: /\.(js|jsx)$/,
                use: ['babel-loader'],
                exclude: /node_modules/,
            &#125;,
        ],
    &#125;,
    plugins: [new HtmlWebpackPlugin(&#123; template: './src/index.html' &#125;)],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">安装相关babel</h1>
<p>Babel 是一个 JavaScript 编译器，能将 ES6 代码转为 ES5 代码，让你使用最新的语言特性而不用担心兼容性问题</p>
<ul>
<li>npm i @babel/core --转译ES2015+的代码</li>
<li>npm i @babel/preset-react</li>
</ul>
<p>在根目录下创建以一个.babelrc</p>
<pre><code class="copyable">&#123;
    "presets": [
        [
            "@babel/preset-react",
            &#123;
                "runtime": "automatic" 
                // 这一行可以在rect hook 版本里不引入import React from 'react'
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">安装react</h1>
<ul>
<li>npm i react</li>
<li>npm i react-dom</li>
</ul>
<p>在src 文件夹里
创建一个html 文件，创建一个index.js 文件，一个app.jsx 文件</p>
<h2 data-id="heading-4">html文件</h2>
<p>主要目的，写入一个入口</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div id='root'></div>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">index.js 文件</h2>
<pre><code class="copyable">import ReactDom from 'react-dom';
import App from './App.jsx';

ReactDom.render(<App />, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">app.jsx 自定义文件</h2>
<pre><code class="copyable">import React from 'react';
export default () => &#123;
    return <div>
        this is a page
    </div>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">总结</h1>
<p>以上就是从空文件到创建了一个基于react+webpack 开发的文件夹，你可以根据你的习惯开发你的项目啦</p></div>  
</div>
            