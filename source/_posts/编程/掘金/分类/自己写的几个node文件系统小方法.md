
---
title: '自己写的几个node文件系统小方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3988'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 23:53:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=3988'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 遍历入参中对应文件夹下的所有文件，并返回对应文件完整路径</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">travel</span>(<span class="hljs-params">basePath, callback</span>) </span>&#123;
  fs
    .readdirSync(basePath)
    .forEach(<span class="hljs-function">(<span class="hljs-params">file</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> filePath = path.join(basePath, file)
      <span class="hljs-keyword">if</span> (fs.statSync(filePath).isDirectory()) &#123;
        <span class="hljs-comment">// 如果是文件夹则递归继续</span>
        travel(filePath, callback)
      &#125; <span class="hljs-keyword">else</span> &#123;
        callback(filePath)
      &#125;
    &#125;)
&#125;

<span class="hljs-comment">// 使用</span>
<span class="hljs-keyword">let</span> basePath = <span class="hljs-string">'./server'</span> <span class="hljs-comment">// 可以是以盘名开头的绝对路径：'F:/server'</span>

travel(basePath, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">filePath</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(filePath)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 根据入参路径创建对应目录和文件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>)
<span class="hljs-comment">// 生成可识别的完整路径</span>
<span class="hljs-keyword">const</span> toResolvePath = <span class="hljs-function">(<span class="hljs-params">...file</span>) =></span> path.resolve(process.cwd(), ...file);
<span class="hljs-comment">// 创建目录</span>
<span class="hljs-keyword">const</span> dirCreate = <span class="hljs-function">(<span class="hljs-params">targetPath, cb</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (fs.existsSync(targetPath)) &#123;
        cb()
    &#125; <span class="hljs-keyword">else</span> &#123;
        dirCreate(path.dirname(targetPath), <span class="hljs-function">() =></span> &#123;
            fs.mkdirSync(targetPath)
            cb()
        &#125;)
    &#125;
&#125;
<span class="hljs-keyword">const</span> generateDirectoryCreate = <span class="hljs-keyword">async</span> (dirPath) => &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        dirCreate(dirPath, resolve)
    &#125;)
&#125;

<span class="hljs-comment">// 创建文件</span>
<span class="hljs-keyword">const</span> generateFileCreate = <span class="hljs-keyword">async</span> (filePath, content) => &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        fs.writeFile(filePath, content, <span class="hljs-string">'utf8'</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (err) &#123;
                <span class="hljs-built_in">console</span>.log(err.message);
                reject(err)
            &#125; <span class="hljs-keyword">else</span> &#123;
                resolve()
            &#125;
        &#125;)
    &#125;)
&#125;

<span class="hljs-comment">// 使用</span>
<span class="hljs-keyword">const</span> basePath = <span class="hljs-string">'./aaa/bbb'</span>
<span class="hljs-keyword">const</span> resolvedPath = toResolvePath(basePath);
<span class="hljs-comment">// 根据path创建目录</span>
generateDirectoryCreate(resolvedPath);
<span class="hljs-comment">// 根据path创建文件</span>
generateFileCreate(toResolvePath(basePath, <span class="hljs-string">'index.js'</span>), <span class="hljs-string">'aaabbb\ncccddd'</span>);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            