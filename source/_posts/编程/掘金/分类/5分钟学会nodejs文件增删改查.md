
---
title: '5分钟学会nodejs文件增删改查'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4913'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 17:51:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=4913'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这篇文章主要是写给初学node.js的同学，本篇文章主要姐介绍nodejs的文件模块，通过nodejs的文件模块，我们可以创建、读取、修改、删除我们操作系统上的文件或文件夹，同理在Linux服务器上也是可以运行的。因为nodejs是跨平台运行的javascript运行环境。</p>
<p>Nodejs File System官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fdist%2Flatest-v14.x%2Fdocs%2Fapi%2Ffs.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/dist/latest-v14.x/docs/api/fs.html" ref="nofollow noopener noreferrer">nodejs.org/dist/latest…</a></p>
<p>源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcmdfas%2Fnodejs-file-system" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cmdfas/nodejs-file-system" ref="nofollow noopener noreferrer">github.com/cmdfas/node…</a></p>
<h2 data-id="heading-0">项目结构：</h2>
<pre><code class="copyable">├── files
│   ├── file1
│   └── file2
├── dir.js
├── index-callback.js
├── index-promise.js
└── stream.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">常规文件操作</h2>
<h3 data-id="heading-2">回调函数式操作</h3>
<p>创建<code>index-callback.js</code>，代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-comment">// 读取文件</span>
fs.readFile(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file1'</span>), <span class="hljs-function">(<span class="hljs-params">err, buf</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
    <span class="hljs-built_in">console</span>.log(buf.toString()) 
&#125;)

<span class="hljs-comment">// 写入文件</span>
fs.writeFile(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file3'</span>), <span class="hljs-string">'欢迎光临'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'写入完成'</span>) 

  <span class="hljs-comment">// 在文件末尾追加</span>
    fs.appendFile(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file3'</span>), <span class="hljs-string">'\n\n男宾三位'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'追加完成'</span>) 

      <span class="hljs-comment">// 修改文件名称</span>
        fs.rename(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file3'</span>), path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file3-rename'</span>), <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'改名完成'</span>) 
    
        &#125;)
    &#125;)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li><code>readFile</code>用来读取文件的内容，在读取成功后在回调函数返回的是buffer格式，所以需要调用toString()方法</li>
<li><code>writeFile</code>写入内容进文件，如果文件不存在会自动创建文件</li>
<li><code>appendFile</code>在文件末尾追加内容，如果文件不存在会自动创建文件</li>
<li><code>rename</code>可以用来修改文件名称</li>
<li><code>path.join</code>用来拼接文件路径，可以避免不同操作系统路径格式不同的问题</li>
<li><code>__dirname</code>是node.js全局变量，默认是当前项目目录</li>
</ul>
<h3 data-id="heading-3">promise async await式操作</h3>
<p>创建<code>index-promise.js</code>，代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fsPromises = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>).promises
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> fileFunc = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> fsPromises.readFile(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file1'</span>))
        <span class="hljs-built_in">console</span>.log(data.toString())
        <span class="hljs-keyword">await</span> fsPromises.unlink(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file1'</span>))
      
        <span class="hljs-keyword">await</span> fsPromises.writeFile(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file5'</span>), data)
        <span class="hljs-keyword">await</span> fsPromises.appendFile(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file5'</span>), <span class="hljs-string">'\n\n欢迎光临'</span>)
        <span class="hljs-keyword">await</span> fsPromises.rename(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file5'</span>), path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file5-rename'</span>))
        <span class="hljs-keyword">const</span> newData = <span class="hljs-keyword">await</span> fsPromises.readFile(path.join(__dirname, <span class="hljs-string">'files'</span>, <span class="hljs-string">'file5-rename'</span>))
        <span class="hljs-built_in">console</span>.log(newData.toString())
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-built_in">console</span>.log(error)
    &#125;
&#125;

fileFunc()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li>相比回调式操作，使用async await操作会更加优雅，不会出现回调地狱</li>
<li><code>unlink</code>用来删除文件</li>
</ul>
<h2 data-id="heading-4">文件流操作</h2>
<p>创建<code>stream.js</code>，代码如下</p>
<h3 data-id="heading-5">方式一</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)

<span class="hljs-comment">// 读取文件流</span>
<span class="hljs-keyword">const</span> rs = fs.createReadStream(<span class="hljs-string">'./files/file2'</span>, &#123; <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf8'</span> &#125;)
<span class="hljs-comment">// 写入文件流</span>
<span class="hljs-keyword">const</span> ws = fs.createWriteStream(<span class="hljs-string">'./files/new-file2'</span>)

<span class="hljs-comment">// 监听读取并写入</span>
rs.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">chunk</span>) =></span> &#123;
ws.write(chunk)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在读取大文件时或者处理网络文件时，文件流操作很有用，在操作大文件时，我们可以设置每次读取的数据量大小，默认是64kb</p>
<h3 data-id="heading-6">方式二</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)

<span class="hljs-comment">// 读取文件流</span>
<span class="hljs-keyword">const</span> rs = fs.createReadStream(<span class="hljs-string">'./files/file2'</span>, &#123; <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf8'</span> &#125;)
<span class="hljs-comment">// 写入文件流</span>
<span class="hljs-keyword">const</span> ws = fs.createWriteStream(<span class="hljs-string">'./files/new-file2'</span>)

rs.pipe(ws)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>pipe</code>方法自动将读取文件流导入到写入流，相当于一个便捷操作。</p>
<h2 data-id="heading-7">操作文件夹</h2>
<p>创建<code>dir.js</code>，代码如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)

<span class="hljs-comment">// 判断文件夹是否存在</span>
<span class="hljs-keyword">if</span> (!fs.existsSync(<span class="hljs-string">'./new'</span>)) &#123;
  <span class="hljs-comment">// 创建文件夹</span>
    fs.mkdir(<span class="hljs-string">'./new'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'文件夹创建成功'</span>)
    &#125;)
&#125;

<span class="hljs-keyword">if</span> (fs.existsSync(<span class="hljs-string">'./new'</span>)) &#123;
  <span class="hljs-comment">// 删除文件夹</span>
    fs.rmdir(<span class="hljs-string">'./new'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'文件夹删除成功'</span>)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li><code>existsSync</code>是同步方法，用来判断文件夹是否存在</li>
<li><code>mkdir</code>创建文件夹</li>
<li><code>rmdir</code>删除文件夹</li>
</ul>
<p>这3个操作文件夹的方法非常常用，就像每天吃饭一样。</p></div>  
</div>
            