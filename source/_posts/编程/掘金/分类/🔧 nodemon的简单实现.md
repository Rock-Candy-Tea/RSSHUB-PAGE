
---
title: '🔧 nodemon的简单实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6269'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 21:55:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=6269'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>nodemon</code>启动的node服务，在检测到目标文件发生变化后，会重新启动服务器</p>
<ul>
<li>监听目标文件的变化</li>
<li>重新启动服务器 -> 关闭服务器 + 启动服务器</li>
</ul>
<h4 data-id="heading-0">1. 监听文件的变化</h4>
<p>nodejs自带的<code>fs.watch || fs.watchFile</code>可以做到监听文件的变化，但是存在系统兼容和其他小问题，这里推荐使用<code>chokidar</code>去处理文件的监听</p>
<p>🔗   <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fchokidar" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/chokidar" ref="nofollow noopener noreferrer">chokidar</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> chokidar = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chokidar'</span>);

chokidar.watch([<span class="hljs-string">'index.js'</span>]).on(<span class="hljs-string">'all'</span>, <span class="hljs-function">(<span class="hljs-params">event, path</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(event, path);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2. 重新启动服务器</h4>
<p>重新启动服务器分为关闭服务器和重新打开服务器，在监听到文件变化后处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> chokidar = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chokidar'</span>);
<span class="hljs-keyword">const</span> &#123; spawn &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)

<span class="hljs-keyword">const</span> start = debounce(restart, <span class="hljs-number">500</span>);

<span class="hljs-keyword">let</span> childProcess = <span class="hljs-literal">null</span>;
chokidar.watch([<span class="hljs-string">'index.js'</span>]).on(<span class="hljs-string">'all'</span>, <span class="hljs-function">(<span class="hljs-params">event, path</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(event, path)
  start();
&#125;);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">restart</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 重启服务器前先杀掉之前的进程</span>
  childProcess && childProcess.kill();
  childProcess = spawn(<span class="hljs-string">'node'</span>, [<span class="hljs-string">'index.js'</span>], &#123;
    <span class="hljs-attr">stdio</span>: [process.stdin, process.stdout, process.stderr]
  &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">f, delay</span>) </span>&#123;
  <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    timer && <span class="hljs-built_in">clearTimeout</span>(timer);
    timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      f();
    &#125;, delay);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>🔗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxuyede%2Fnodemon-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xuyede/nodemon-demo" ref="nofollow noopener noreferrer">github.com/xuyede/node…</a></p></div>  
</div>
            