
---
title: 'Vue打包后页面出现空白解决办法（臻享版）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2984'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 03:13:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=2984'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、 vue-cli创建项打包后打开页面为空白的问题解决</h2>
<ol>
<li>命令行输入：<strong>npm run build</strong></li>
</ol>
<p>打包出来后项目中就会多了一个文件夹dist，这就是我们打包过后的项目。</p>
<h2 data-id="heading-1">二、打包完成后配置会自动生成vue.config.js文件，这个文件非常重要值得你收藏</h2>
<h2 data-id="heading-2">配置如下：</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">dir</span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.join(__dirname, dir);
&#125;;
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">publicPath</span>: process.env.NODE_ENV === <span class="hljs-string">"production"</span> ? <span class="hljs-string">"./"</span> : <span class="hljs-string">"./"</span>,
  <span class="hljs-attr">outputDir</span>: <span class="hljs-string">"dist"</span>,
  <span class="hljs-attr">assetsDir</span>: <span class="hljs-string">"static"</span>,
  <span class="hljs-attr">lintOnSave</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否开启eslint保存检测</span>
  <span class="hljs-attr">productionSourceMap</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否在构建生产包时生成sourcdeMap</span>
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    config.resolve.alias
      .set(<span class="hljs-string">"@"</span>, resolve(<span class="hljs-string">"src"</span>))
      .set(<span class="hljs-string">"@v"</span>, resolve(<span class="hljs-string">"src/views"</span>))
      .set(<span class="hljs-string">"@c"</span>, resolve(<span class="hljs-string">"src/components"</span>))
      .set(<span class="hljs-string">"@u"</span>, resolve(<span class="hljs-string">"src/utils"</span>))
      .set(<span class="hljs-string">"@s"</span>, resolve(<span class="hljs-string">"src/service"</span>)); <span class="hljs-comment">/* 别名配置 */</span>
    config.optimization.runtimeChunk(<span class="hljs-string">"single"</span>);
  &#125;,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">// host: "localhost",</span>
    <span class="hljs-comment">/* 本地ip地址 */</span>
    <span class="hljs-comment">//host: "192.168.1.107",</span>
    <span class="hljs-attr">host</span>: <span class="hljs-string">"0.0.0.0"</span>, <span class="hljs-comment">//局域网和本地访问</span>
    <span class="hljs-attr">port</span>: <span class="hljs-string">"8080"</span>,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">/* 自动打开浏览器 */</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">overlay</span>: &#123;
      <span class="hljs-attr">warning</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">error</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">/* 跨域代理 */</span>
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">"/api"</span>: &#123;
        <span class="hljs-comment">/* 目标代理服务器地址 */</span>
        <span class="hljs-attr">target</span>: <span class="hljs-string">"http://m260048y71.zicp.vip"</span>, <span class="hljs-comment">//</span>
        <span class="hljs-comment">// target: "http://192.168.1.102:8888", //</span>
        <span class="hljs-comment">/* 允许跨域 */</span>
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">ws</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">"^/api"</span>: <span class="hljs-string">""</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">第三个问题：router-view中的内容显示不出来。路由history模式</h2>
<p>这个坑是当你使用了路由之后，在没有后端配合的情况下就手贱打开路由history模式的时候，打包出来的文件也会是一片空白的情况，</p>
<p><strong>解决 ： 在 router.js 中将 mode: history注释掉</strong></p>
<h2 data-id="heading-4">非常珍贵的config.js文件值得你收藏</h2></div>  
</div>
            