
---
title: 'Markdown转HTML的plugin插件【记录Plan】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/024db1ac3f904741945c110e72e5ab0c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 00:43:48 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/024db1ac3f904741945c110e72e5ab0c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>前段时间有在学习webpack的基础知识，但是无论是文档还是入门小视频，都没有直接在实践中学的好一点。</p>
<p>下面我会从我在这个完成Markdown转HTML的plugin插件中学到的一些知识点（相当于巩固自己之前的webpack入门吧），逐一理一理。（b站前端小野森森的视频，有兴趣可以看下）
包括但不限于：</p>
<ul>
<li>webpack的一些基础配置</li>
<li>一些正则表达式的书写</li>
<li>如何构建一颗DOM树</li>
<li>......</li>
</ul>
<p>整个的代码在这-> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjingdd-boop%2Fcode%2Ftree%2Fmaster%2Fwebpack%2F%25E5%25AD%25A6%25E4%25B9%25A0%2Fmd-html-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jingdd-boop/code/tree/master/webpack/%E5%AD%A6%E4%B9%A0/md-html-plugin" ref="nofollow noopener noreferrer">md-to-html-plugin</a></p>
<p>实现的效果时这样的：左边的markdowm渲染成右边的html
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/024db1ac3f904741945c110e72e5ab0c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>暂时先不去想具体怎么实现Markdown转HTML，首先来看看我们要怎么开始，先放出目录：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a81334dd938449a95a139571b38ec17~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>首先你得用webpack搭个项目吧(入门的webpack有了用武之地)</li>
<li>创建一个plugin文件夹，里面是我们的这个插件的灵魂</li>
<li>既然是md转html 那我们的有个 md文档吧, 我md文档要先转成像<code><h1>**</h1></code>类似的包裹了内容的字符串, 再插入到template.html模板中 再输出一个html文件</li>
</ol>
<h2 data-id="heading-1">1. 使用webpack搭建项目 （回顾篇）</h2>
<ol>
<li>创建一个md-to-html-plugin 的文件夹</li>
</ol>
<p>使用如下命令</p>
<ul>
<li>npm init -y</li>
<li>npm install webpack webpack-cli webpack-dev-server -D</li>
</ul>
<p>在根目录下创建</p>
<ul>
<li>webpack.config.js</li>
<li>src/app.js</li>
<li>plugin/md-to-html-plugin/ index.js</li>
<li>plugin/md-to-html-plugin/ compier.js</li>
</ul>
<p><code>(md文档要先转成像<h1>**</h1>类似的包裹了内容的字符串)</code></p>
<ul>
<li>plugin/md-to-html-plugin/template.html</li>
</ul>
<p>下面依次介绍一下：</p>
<h2 data-id="heading-2">2.webpack.config.js 配置</h2>
<p>包含：</p>
<ul>
<li>打包入口  entry</li>
<li>出口 output</li>
<li>模式   mode</li>
<li>plugin MdToHtmlPlugin (我们自己写的)</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> MdToHtmlPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./plugin/md-to-html-plugin'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>, 
    <span class="hljs-attr">entry</span>: resolve(__dirname, <span class="hljs-string">'src/app.js'</span>),
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>:<span class="hljs-string">'app.js'</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> MdToHtmlPlugin(&#123;
            <span class="hljs-attr">template</span>: resolve(__dirname, <span class="hljs-string">'text.md'</span>),
            <span class="hljs-attr">filename</span>: <span class="hljs-string">'text.html'</span>
        &#125;),
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3. md-to-html-plugin/ index.js 有关plugin</h2>
<h3 data-id="heading-4">3.1 插件的定义：</h3>
<blockquote>
<p>插件是由一个构造函数（此构造函数上的 prototype 对象具有 <code>apply</code> 方法）的所实例化出来的。这个 <code>apply</code> 方法在安装插件时，会被 webpack compiler 调用一次。<code>apply</code> 方法可以接收一个 webpack compiler 对象的引用，从而可以在回调函数中访问到 compiler 对象。</p>
</blockquote>
<h3 data-id="heading-5">3.2 MdToHtmlPlugin基础结构</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; readFileSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>) <span class="hljs-number">1.</span> 需要读取文件 md和模板
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>) 
<span class="hljs-keyword">const</span> INNER_MARK = <span class="hljs-string">'<!-- inner -->'</span> <span class="hljs-number">2.</span> template.html 中用来承载转换后的html标签
<span class="hljs-keyword">const</span> &#123;compileHTML&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./compiler'</span>) <span class="hljs-number">3.</span> md-html的转换
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MdToHtmlPlugin</span> </span>&#123; <span class="hljs-number">4.</span> 在webpack配置中我们使用的是<span class="hljs-keyword">new</span>的方式创建 这边，我们设置一个<span class="hljs-class"><span class="hljs-keyword">class</span>类，它接受两个参数，<span class="hljs-title">md</span>文档的文件名，和输出的文件名
    <span class="hljs-title">constructor</span>(</span>&#123; template, filename &#125;) &#123;
    <span class="hljs-number">5.</span> 如果md文件找不到，直接保错
        <span class="hljs-keyword">if</span> (!template) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'template 找不到'</span>)
        &#125;
        <span class="hljs-built_in">this</span>.template = template
    <span class="hljs-number">6.</span> 设置输出文件名，如果有文件名就配置，如果没有，就设置成<span class="hljs-string">'md.html'</span>
        <span class="hljs-built_in">this</span>.filename = filename ? filename : <span class="hljs-string">'md.html'</span>
    &#125;
    <span class="hljs-number">7.</span> apply()方法 
    <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
        compiler.hooks.emit.tap(<span class="hljs-string">'md-to-html-plugin'</span>, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
        <span class="hljs-comment">// 我把整个apply方法的内容放到下面去分析了</span>
           <span class="hljs-number">8.</span> 在这个方法里面，我们会将md文档读取处理，生成一颗dom树，再放回template.html里面
        &#125;)
    &#125;
&#125;
<span class="hljs-built_in">module</span>.exports =  MdToHtmlPlugin
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3.3 apply()方法</h3>
<ol>
<li>compiler</li>
</ol>
<ul>
<li>compiler.hooks.emit.tap</li>
<li>emit: 生成资源到 output 目录之前</li>
<li>参数：<code>compilation</code></li>
</ul>
<ol start="2">
<li>compilation</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123; 
        compiler.hooks.emit.tap(<span class="hljs-string">'md-to-html-plugin'</span>, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> _assets = compilation.assets;
            <span class="hljs-keyword">const</span> _mdContent = readFileSync(<span class="hljs-built_in">this</span>.template, <span class="hljs-string">'utf8'</span>);
            <span class="hljs-keyword">const</span> _templateHtml = readFileSync(resolve(__dirname, <span class="hljs-string">'template.html'</span>), <span class="hljs-string">'utf8'</span>)
            <span class="hljs-comment">// 将md文档 分行转换成数组 _mdContentArray</span>
            <span class="hljs-keyword">const</span> _mdContentArray = _mdContent.split(<span class="hljs-string">'\n'</span>) 
            <span class="hljs-comment">// 通过compileHTML方法将这个数组构建成dom树 _htmlStr</span>
            <span class="hljs-keyword">const</span> _htmlStr = compileHTML(_mdContentArray)
            <span class="hljs-comment">// 将dom插入到template.html中</span>
            <span class="hljs-keyword">const</span> _finalHTML = _templateHtml.replace(INNER_MARK,_htmlStr)
            _assets[<span class="hljs-built_in">this</span>.filename] = &#123;
                <span class="hljs-function"><span class="hljs-title">source</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-keyword">return</span> _finalHTML
                &#125;,
                <span class="hljs-function"><span class="hljs-title">size</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-keyword">return</span> _finalHTML.length
                &#125;
            &#125;
           
        &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官网：</p>
<blockquote>
<p>一个插件由以下构成</p>
</blockquote>
<ul>
<li>一个具名 JavaScript 函数。   <code>MdToHtmlPlugin </code></li>
<li>在它的原型上定义 <code>apply</code> 方法。 <code>apply(compiler)</code></li>
<li>指定一个触及到 webpack 本身的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.docschina.org%2Fapi%2Fcompiler-hooks%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.docschina.org/api/compiler-hooks/" ref="nofollow noopener noreferrer">事件钩子</a>。 <code>compiler.hooks.emit.tap</code></li>
<li>操作 webpack 内部的实例特定数据。</li>
<li>在实现功能后调用 webpack 提供的 callback</li>
</ul>
<h2 data-id="heading-7">4. md-to-html 字符串转换</h2>
<h3 data-id="heading-8">4.1 使用js对象创建树</h3>
<h4 data-id="heading-9">4.1.1 创建一颗怎样的树：</h4>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-string">'h1-1626856207419'</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'single'</span>, <span class="hljs-attr">tags</span>: [ <span class="hljs-string">'<h1>这是一个h1的标题\r</h1>'</span> ] &#125;,
    <span class="hljs-string">'ul-1626856207993'</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'wrap'</span>,
      <span class="hljs-attr">tags</span>: [
        <span class="hljs-string">'<li>这个一个ul 列表的第一项\r</li>'</span>,
        <span class="hljs-string">'<li>这个一个ul 列表的第一项\r</li>'</span>,
        <span class="hljs-string">'<li>这个一个ul 列表的第一项\r</li>'</span>,
        <span class="hljs-string">'<li>这个一个ul 列表的第一项\r</li>'</span>
      ]
    &#125;,
    <span class="hljs-string">'h2-1626856207560'</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'single'</span>, <span class="hljs-attr">tag</span>: [ <span class="hljs-string">'<h2>这是一个h2的标题\r</h2>'</span> ] &#125;,
    <span class="hljs-string">'ol-1626856207336'</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'wrap'</span>,
      <span class="hljs-attr">tags</span>: [
        <span class="hljs-string">'<li>. 这个一个ol 列表的第一项\r</li>'</span>,
        <span class="hljs-string">'<li>. 这个一个ol 列表的第一项\r</li>'</span>,
        <span class="hljs-string">'<li>. 这个一个ol 列表的第一项\r</li>'</span>,
        <span class="hljs-string">'<li>. 这个一个ol 列表的第一项</li>'</span>
      ]
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">4.1.2 详细步骤：</h4>
<p>首先之前在index.js里面有个compileHTML(_mdContentArray)，我们将一行行形成的数组作为参数传递给了 compileHTML，希望compileHTML这个函数可以先将md数组，再转换成一个dom树，再将这棵树插入到模板里面。</p>
<ul>
<li>md数组转换成dom树</li>
</ul>
<p>里面分成三种 分别是</p>
<ol>
<li><code># ## </code> 标题类 我们需要转换成h1 h2</li>
<li><code>-</code> 无序列表  我们需要转换成 ul li</li>
<li><code>1. 2.</code> 有序列表  我们需要转换成 ol li</li>
</ol>
<p>当然每个标签里面还有我们需要的内容。 <code>input = matched.input</code></p>
<ul>
<li>使用正则将这集中情况区分</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> reg_mark = <span class="hljs-regexp">/^(.+?)\s/</span>
<span class="hljs-comment">// 匹配 # 开头</span>
<span class="hljs-keyword">const</span> reg_sharp = <span class="hljs-regexp">/^\#/</span>
<span class="hljs-comment">// 匹配 无序列表 -</span>
<span class="hljs-keyword">const</span> reg_crossbar = <span class="hljs-regexp">/^\-/</span>
<span class="hljs-comment">// 匹配 有序列表 1. 2.</span>
<span class="hljs-keyword">const</span> reg_number = <span class="hljs-regexp">/^\d/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>还有一个需要注意的</li>
</ul>
<p>ul里面的li，和ol里面的li，他们都是一起放到ul或者是ol里面的，因此需要做判断上一次的开通标签和这次的是否是相同的</p>
<pre><code class="hljs language-js copyable" lang="js">_lastMark === mark
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">4.1.3 具体代码：</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTreel</span>(<span class="hljs-params">_mdArr</span>) </span>&#123;
    <span class="hljs-keyword">let</span> _htmlPool = &#123;&#125;
    <span class="hljs-keyword">let</span> _lastMark = <span class="hljs-string">''</span> <span class="hljs-comment">// 用于判断，是不是像li标签一样，需要一起放到ol或者ul里面</span>
    <span class="hljs-keyword">let</span> _key = <span class="hljs-number">0</span>

        _mdArr.forEach(<span class="hljs-function"><span class="hljs-params">mdFragment</span> =></span> &#123;
            <span class="hljs-comment">// console.log(mdFragment)</span>
            <span class="hljs-keyword">const</span> matched = mdFragment.match(reg_mark);
            <span class="hljs-keyword">if</span> (matched) &#123;
                <span class="hljs-keyword">const</span> mark = matched[<span class="hljs-number">1</span>]
                <span class="hljs-keyword">const</span> input = matched.input
                <span class="hljs-built_in">console</span>.log(matched,<span class="hljs-string">'matched'</span>) <span class="hljs-comment">// 我们可以看一下这里的matched 打印出的东西是什么</span>
                <span class="hljs-comment">// md-to-html 三种操作 标题 无序列表 有序列表</span>
            &#125;
        &#125;);
    <span class="hljs-keyword">return</span> _htmlPool
   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是matched 打印出来的东西</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mark = matched[<span class="hljs-number">1</span>]   md匹配的 # ##  - <span class="hljs-number">1.</span>等 
<span class="hljs-keyword">const</span> input = matched.input  内容
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">[ <span class="hljs-string">'# '</span>, <span class="hljs-string">'#'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">input</span>: <span class="hljs-string">'# 这是一个h1的标题\r'</span>, <span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span> ] matched
[ <span class="hljs-string">'- '</span>, <span class="hljs-string">'-'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">input</span>: <span class="hljs-string">'- 这个一个ul 列表的第一项\r'</span>, <span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span> ] matched
[ <span class="hljs-string">'- '</span>, <span class="hljs-string">'-'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">input</span>: <span class="hljs-string">'- 这个一个ul 列表的第一项\r'</span>, <span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span> ] matched
[ <span class="hljs-string">'- '</span>, <span class="hljs-string">'-'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">input</span>: <span class="hljs-string">'- 这个一个ul 列表的第一项\r'</span>, <span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span> ] matched
[ <span class="hljs-string">'- '</span>, <span class="hljs-string">'-'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">input</span>: <span class="hljs-string">'- 这个一个ul 列表的第一项\r'</span>, <span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span> ] matched
[ <span class="hljs-string">'## '</span>, <span class="hljs-string">'##'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">input</span>: <span class="hljs-string">'## 这是一个h2的标题\r'</span>, <span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span> ] matched
[<span class="hljs-string">'1. '</span>,<span class="hljs-string">'1.'</span>,<span class="hljs-attr">index</span>: <span class="hljs-number">0</span>,<span class="hljs-attr">input</span>: <span class="hljs-string">'1. 这个一个ol 列表的第一项\r'</span>,<span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span>] matched
[<span class="hljs-string">'2. '</span>,<span class="hljs-string">'2.'</span>,<span class="hljs-attr">index</span>: <span class="hljs-number">0</span>,<span class="hljs-attr">input</span>: <span class="hljs-string">'2. 这个一个ol 列表的第一项\r'</span>,<span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span>] matched
[<span class="hljs-string">'3. '</span>,<span class="hljs-string">'3.'</span>,<span class="hljs-attr">index</span>: <span class="hljs-number">0</span>,<span class="hljs-attr">input</span>: <span class="hljs-string">'3. 这个一个ol 列表的第一项\r'</span>,<span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span>] matched
[ <span class="hljs-string">'4. '</span>, <span class="hljs-string">'4.'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">input</span>: <span class="hljs-string">'4. 这个一个ol 列表的第一项'</span>, <span class="hljs-attr">groups</span>: <span class="hljs-literal">undefined</span> ] matched
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4.3 md-to-html字符串详细处理</h3>
<h4 data-id="heading-13">4.3.1 key 唯一值处理</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">randomNum</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() + <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">1000</span>);
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
    randomNum
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">4.3.2 对标题的处理 h1 h2</h4>
<ol>
<li>首先匹配这个标题 h1.h2...</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (reg_sharp.test(mark)) &#123; <span class="hljs-comment">// 匹配#开头的</span>
      <span class="hljs-keyword">const</span> tag = <span class="hljs-string">`h<span class="hljs-subst">$&#123;mark.length&#125;</span>`</span>; <span class="hljs-comment">// 转换成h1 h2等</span>
      <span class="hljs-keyword">const</span> tagContent = input.replace(reg_mark, <span class="hljs-string">''</span>)
     <span class="hljs-keyword">if</span> (_lastMark === mark) &#123;
     <span class="hljs-comment">// 如果前一次的标签和这次的标签是一样的，之前拼接</span>
         _htmlPool[<span class="hljs-string">`<span class="hljs-subst">$&#123;tag&#125;</span>-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>].tags = [..._htmlPool[<span class="hljs-string">`<span class="hljs-subst">$&#123;tag&#125;</span>-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>].tags,<span class="hljs-string">`<<span class="hljs-subst">$&#123;tag&#125;</span>><span class="hljs-subst">$&#123;tagContent&#125;</span></<span class="hljs-subst">$&#123;tag&#125;</span>>`</span>]
    &#125; <span class="hljs-keyword">else</span> &#123;
     <span class="hljs-comment">// 否则 创建一个新的标题标签</span>
         _lastMark = mark
          _key = randomNum();
          _htmlPool[<span class="hljs-string">`<span class="hljs-subst">$&#123;tag&#125;</span>-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>] = &#123;
              <span class="hljs-attr">type</span>: <span class="hljs-string">'single'</span>, <span class="hljs-comment">// 单个标识</span>
               <span class="hljs-attr">tags</span>: [<span class="hljs-string">`<<span class="hljs-subst">$&#123;tag&#125;</span>><span class="hljs-subst">$&#123;tagContent&#125;</span></<span class="hljs-subst">$&#123;tag&#125;</span>>`</span>]
           &#125;
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">4.3.3 对无序列表的处理</h4>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (reg_crossbar.test(mark)) &#123;
     <span class="hljs-comment">// console.log(matched)</span>
       <span class="hljs-keyword">const</span> tagContent = input.replace(reg_mark, <span class="hljs-string">''</span>);
       <span class="hljs-keyword">const</span> tag = <span class="hljs-string">'li'</span>;

       <span class="hljs-keyword">if</span> (reg_crossbar.test(_lastMark)) &#123;
           _htmlPool[<span class="hljs-string">`ul-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>].tags = [..._htmlPool[<span class="hljs-string">`ul-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>].tags ,<span class="hljs-string">`<<span class="hljs-subst">$&#123;tag&#125;</span>><span class="hljs-subst">$&#123;tagContent&#125;</span></<span class="hljs-subst">$&#123;tag&#125;</span>>`</span>]
          &#125; <span class="hljs-keyword">else</span> &#123;
            _lastMark = mark
            _key = randomNum();
             _htmlPool[<span class="hljs-string">`ul-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>] = &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'wrap'</span>,<span class="hljs-comment">// 多个标识</span>
            <span class="hljs-attr">tags</span>: [<span class="hljs-string">`<<span class="hljs-subst">$&#123;tag&#125;</span>><span class="hljs-subst">$&#123;tagContent&#125;</span></<span class="hljs-subst">$&#123;tag&#125;</span>>`</span>] 
          &#125;
       &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">4.3.4 对有序列表的处理</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (reg_number.test(mark)) &#123;
    <span class="hljs-keyword">const</span> tagContent = input.replace(reg_number, <span class="hljs-string">''</span>)
    <span class="hljs-keyword">const</span> tag = <span class="hljs-string">'li'</span>

    <span class="hljs-keyword">if</span> (reg_number.test(_lastMark)) &#123;
       _htmlPool[<span class="hljs-string">`ol-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>].tags = [..._htmlPool[<span class="hljs-string">`ol-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>].tags ,<span class="hljs-string">`<<span class="hljs-subst">$&#123;tag&#125;</span>><span class="hljs-subst">$&#123;tagContent&#125;</span></<span class="hljs-subst">$&#123;tag&#125;</span>>`</span>]
      &#125; <span class="hljs-keyword">else</span> &#123;
           _lastMark = mark;
           _key = randomNum();

            _htmlPool[<span class="hljs-string">`ol-<span class="hljs-subst">$&#123;_key&#125;</span>`</span>] = &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'wrap'</span>,
                <span class="hljs-attr">tags</span>: [<span class="hljs-string">`<<span class="hljs-subst">$&#123;tag&#125;</span>><span class="hljs-subst">$&#123;tagContent&#125;</span></<span class="hljs-subst">$&#123;tag&#125;</span>>`</span>] 
            &#125;
       &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">4.4 模板编译</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compileHTML</span>(<span class="hljs-params">_mdContentArray</span>) </span>&#123;
    <span class="hljs-keyword">const</span> _htmlPool = createTreel(_mdContentArray)
    <span class="hljs-comment">// sconsole.log(_htmlPool)</span>
    <span class="hljs-keyword">let</span> _htmlStr = <span class="hljs-string">''</span>
    <span class="hljs-keyword">let</span> item

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">in</span> _htmlPool) &#123;
        <span class="hljs-comment">// console.log(k, _htmlPool[k])</span>
        item = _htmlPool[k]
        <span class="hljs-keyword">if</span> (item.type === <span class="hljs-string">'single'</span>) &#123;
        <span class="hljs-comment">// 单个标题标签</span>
            item.tags.forEach(<span class="hljs-function">(<span class="hljs-params">tag</span>) =></span> &#123;
                _htmlStr += tag;
            &#125;)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (item.type === <span class="hljs-string">'wrap'</span>) &#123;
        <span class="hljs-comment">// 多个标签 列表</span>
            <span class="hljs-built_in">console</span>.log(item.tags,<span class="hljs-string">'2'</span>)
            <span class="hljs-keyword">let</span> _list = <span class="hljs-string">`<<span class="hljs-subst">$&#123;k.split(<span class="hljs-string">'-'</span>)[<span class="hljs-number">0</span>]&#125;</span>>`</span>

            item.tags.forEach(<span class="hljs-function">(<span class="hljs-params">tag</span>) =></span> &#123;
                _list += tag;
            &#125;)

            _list += <span class="hljs-string">`</<span class="hljs-subst">$&#123;k.split(<span class="hljs-string">'-'</span>)[<span class="hljs-number">0</span>]&#125;</span>>`</span>
            _htmlStr += _list
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> _htmlStr
    
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
    compileHTML
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">5. 放入模板编译</h2>
<p>再body里面有个注释<code><!-- inner --></code> 之后我们可以将处理好的html放到这里</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- inner -->
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考文档：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.docschina.org%2Fapi%2Fcompiler-hooks%2F%23emit" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.docschina.org/api/compiler-hooks/#emit" ref="nofollow noopener noreferrer">1.webpack compiler 钩子</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV15i4y1j7gk%3Ffrom%3Dsearch%26seid%3D8135852893377850875" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV15i4y1j7gk?from=search&seid=8135852893377850875" ref="nofollow noopener noreferrer">2.视频</a></p>
<p>还有很多不会不懂的地方，继续学习中。。。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f4636ac9b8f49a78756c7abb76c4e40~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            