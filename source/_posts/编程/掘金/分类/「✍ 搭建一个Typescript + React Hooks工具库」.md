
---
title: '「✍ 搭建一个Typescript + React Hooks工具库」'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5342'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 02:26:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=5342'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近项目用到了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2Fhooks" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/hooks" ref="nofollow noopener noreferrer">ahooks</a>，也顺便试试搭建一个hooks库，ahooks用的是dumi(基于umi)来搭建，本文先尝试从0搭建</p>
<h1 data-id="heading-0">从0搭建</h1>
<p>这里使用webpack构建</p>
<p>先看看必要的包(不包含eslint, 测试等包)</p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-attr">"@babel/core"</span>: <span class="hljs-string">"^7.14.8"</span>,
    <span class="hljs-attr">"@babel/preset-env"</span>: <span class="hljs-string">"^7.14.8"</span>,                 <span class="hljs-comment">// es语法转换</span>
    <span class="hljs-attr">"@babel/preset-react"</span>: <span class="hljs-string">"^7.14.5"</span>,               <span class="hljs-comment">// react语法转换</span>
    <span class="hljs-attr">"@babel/preset-typescript"</span>: <span class="hljs-string">"^7.14.5"</span>,          <span class="hljs-comment">// typescript语法转换，这次用ts-loader代替</span>
    <span class="hljs-attr">"babel-loader"</span>: <span class="hljs-string">"^8.2.2"</span>,                       <span class="hljs-comment">// babel-loader for webpack    </span>
    
    <span class="hljs-attr">"@types/node"</span>: <span class="hljs-string">"^12.19.12"</span>,
    <span class="hljs-attr">"@types/react"</span>: <span class="hljs-string">"^16.14.2"</span>,
    <span class="hljs-attr">"@types/react-dom"</span>: <span class="hljs-string">"^16.9.10"</span>,
   
    <span class="hljs-attr">"react"</span>: <span class="hljs-string">"^17.0.1"</span>,
    <span class="hljs-attr">"react-dom"</span>: <span class="hljs-string">"^17.0.1"</span>,
    
    <span class="hljs-attr">"rimraf"</span>: <span class="hljs-string">"^3.0.2"</span>,                            <span class="hljs-comment">// 打包前删除文件</span>
    <span class="hljs-attr">"ts-loader"</span>: <span class="hljs-string">"^9.2.4"</span>,                         <span class="hljs-comment">// typescript语法转换</span>
    <span class="hljs-attr">"typescript"</span>: <span class="hljs-string">"^4.1.3"</span>,                        <span class="hljs-comment">// typescript包</span>
    <span class="hljs-attr">"uglifyjs-webpack-plugin"</span>: <span class="hljs-string">"^2.2.0"</span>            <span class="hljs-comment">// 压缩js文件</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>webpack.config.js</code></p>
<p>这里主要是loader配置，注意loader是从左到右执行的，因此这里是先用ts-loader将ts解析为js，再用babel解析react和es语法</p>
<pre><code class="copyable">  module: &#123;
    rules: [
      &#123;
        test: /\.tsx?$/,
        exclude: /node_modules/,
        use: ['babel-loader','ts-loader'],
        include: [path.resolve('src')]
      &#125;
    ],
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，babel-loader要搭配preset，在.babelrc中设置preset</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"presets"</span>: [
    [
      <span class="hljs-string">"@babel/preset-env"</span>,&#123; <span class="hljs-comment">// 再转化 ES6 语法</span>
        <span class="hljs-attr">"targets"</span>: &#123;
          <span class="hljs-attr">"chrome"</span>: <span class="hljs-string">"67"</span>
        &#125;,
        <span class="hljs-attr">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>
      &#125;
    ],
    <span class="hljs-string">"@babel/preset-react"</span> <span class="hljs-comment">// 先转化 react 语法</span>
    <span class="hljs-comment">// "@babel/preset-typescript"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>打包</code></p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-attr">"clean"</span>: <span class="hljs-string">"rimraf ./lib"</span>,
  <span class="hljs-attr">"build"</span>: <span class="hljs-string">"npm run clean  && webpack"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">使用dumi</h1>
<p>todo..</p></div>  
</div>
            