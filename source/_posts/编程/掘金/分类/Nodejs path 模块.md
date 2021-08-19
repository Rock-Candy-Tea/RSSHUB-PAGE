
---
title: 'Node.js path 模块'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6940'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 07:55:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=6940'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
</blockquote>
<p>Node.js <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fapi%2Fpath.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/api/path.html" ref="nofollow noopener noreferrer">path 模块</a>是一个内置模块，可帮助您以独立于操作系统的方式使用文件系统路径。如果要构建支持 OSX、Linux 和 Windows 的 CLI 工具，则 Path 模块是必不可少的。</p>
<p>即使您正在构建一个只在 Linux 上运行的后端服务，path 模块仍然有助于在操作路径时避免边缘情况。</p>
<p>下面我们将描述一些使用 path 模块的常见模式，以及为什么您应该使用 path 模块而不是将路径操纵成字符串。</p>
<h2 data-id="heading-0">在 Node 中使用 Path 模块</h2>
<p>path 模块中最常用的方法是 <code>path.join()</code>。该方法将一个或多个路径段合并为一个字符串，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
​
path.join(<span class="hljs-string">'/path'</span>, <span class="hljs-string">'to'</span>, <span class="hljs-string">'test.txt'</span>) <span class="hljs-comment">// '/path/to/test.txt'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>您可能想知道为什么要使用 <code>path.join()</code> 方法而不是字符串拼接。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">'/path'</span> + <span class="hljs-string">'/'</span> + <span class="hljs-string">'to'</span> + <span class="hljs-string">'/'</span> + <span class="hljs-string">'test.txt'</span> <span class="hljs-comment">// '/path/to/test.txt'</span>
​
[<span class="hljs-string">'/path'</span>, <span class="hljs-string">'to'</span>, <span class="hljs-string">'test.txt'</span>].join(<span class="hljs-string">'/'</span>) <span class="hljs-comment">// '/path/to/test.txt'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因主要有两个：</p>
<ul>
<li><strong>对于 Windows 支持</strong>。Windows 使用反斜杠（<code>\</code>）而不是正斜杠（<code>/</code>）作为路径分隔符。<code>path.join()</code> 会为我们处理此问题。因为 <code>path.join('data', 'test.txt')</code> 在 Linux 和 OSX 以及 Windows 上都会返回 <code>'data/test.txt'</code>。</li>
<li><strong>用于处理边缘情况</strong>。使用文件系统路径时，会弹出许多边缘情况。例如，如果您尝试手动连接两个路径，您可能会意外地得到重复的路径分隔符。<code>path.join()</code> 方法为我们处理开头和结尾的斜杠，如下所示：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">path.join(<span class="hljs-string">'data'</span>, <span class="hljs-string">'test.txt'</span>) <span class="hljs-comment">// 'data/test.txt'</span>
path.join(<span class="hljs-string">'data'</span>, <span class="hljs-string">'/test.txt'</span>) <span class="hljs-comment">// 'data/test.txt'</span>
path.join(<span class="hljs-string">'data/'</span>, <span class="hljs-string">'test.txt'</span>) <span class="hljs-comment">// 'data/test.txt'</span>
path.join(<span class="hljs-string">'data/'</span>, <span class="hljs-string">'/test.txt'</span>) <span class="hljs-comment">// 'data/test.txt'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">常用的 Path 方法</h2>
<p>path 模块还具有几个用于提取路径组件的方法，例如文件扩展名或目录。</p>
<p><code>path.extname()</code> 方法以字符串形式返回文件扩展名：</p>
<pre><code class="hljs language-js copyable" lang="js">path.extname(<span class="hljs-string">'/path/to/test.txt'</span>) <span class="hljs-comment">// '.test'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就像连接两条路径一样，获取文件扩展名比最初看起来要复杂。</p>
<p>如果 path 以 <code>.</code> 为结尾，将返回 <code>.</code>。如果文件无扩展名，又不以 <code>.</code> 结尾，或文件没有扩展名，将返回空值。</p>
<pre><code class="hljs language-js copyable" lang="js">path.extname(<span class="hljs-string">'/path/to/index.'</span>) <span class="hljs-comment">// '.'</span>

path.extname(<span class="hljs-string">'/path/to/README'</span>) <span class="hljs-comment">// ''</span>

path.extname(<span class="hljs-string">'/path/to/.gitignore'</span>) <span class="hljs-comment">// ''</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>path 模块还有 <code>path.basename()</code> 和 <code>path.dirname()</code> 方法，分别获取文件名（包括扩展名）和目录。</p>
<pre><code class="hljs language-js copyable" lang="js">path.basename(<span class="hljs-string">'/path/to/test.txt'</span>) <span class="hljs-comment">// 'test.txt'</span>
​
path.dirname(<span class="hljs-string">'/path/to/test.txt'</span>) <span class="hljs-comment">// '/path/to'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>path.parse()</code> 方法返回一个对象，该对象包含分为五个不同组件的路径，包括扩展名和目录。<code>path.parse()</code> 方法也是不带任何扩展名获取文件名的方法。</p>
<pre><code class="hljs language-js copyable" lang="js">path.parse(<span class="hljs-string">'/path/to/test.txt'</span>)

<span class="hljs-comment">/*
&#123;
  root: '/',
  dir: '/path/to',
  base: 'test.txt',
  ext: '.txt',
  name: 'test'
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">使用 <code>path.relative()</code></h2>
<p>像 <code>path.join()</code> 和 <code>path.extname()</code> 这样的方法涵盖了大多数使用文件路径的用例。但是 path 模块有几个更高级的方法，例如 <code>path.relative()</code>。</p>
<p><code>path.relative(from, to)</code> 方法根据当前工作目录返回从 <code>from</code> 到 <code>to</code> 的相对路径。 如果 <code>from</code> 和 <code>to</code> 都解析为相同的路径（在分别调用 <code>path.resolve()</code> 之后），则返回零长度字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 返回相对于第一条路径的第二条路径的路径</span>
path.relative(<span class="hljs-string">'/app/views/home.html'</span>, <span class="hljs-string">'/app/layout/index.html'</span>) <span class="hljs-comment">// '../../layout/index.html'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果给定了相对于一个目录的路径，但需要相对于另一个目录的路径，则 <code>path.relative()</code> 方法非常有用。例如，流行的文件系统监视库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fchokidar" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/chokidar" ref="nofollow noopener noreferrer">Chokidar</a> 提供了相对于监视目录的路径。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> watcher = chokidar.watch(<span class="hljs-string">'mydir'</span>)
​
<span class="hljs-comment">// 如果用户添加 mydir/path/to/test.txt，则会打印 mydir/path/to/test.txt</span>
watcher.on(<span class="hljs-string">'add'</span>, <span class="hljs-function"><span class="hljs-params">path</span> =></span> <span class="hljs-built_in">console</span>.log(path))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是为什么大量的使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpaulmillr%2Fchokidar" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/paulmillr/chokidar" ref="nofollow noopener noreferrer">Chokidar</a> 工具。如常见的 Gatsby 或 webpack，其在内部也大量使用 <code>path.relative()</code> 方法。</p>
<p>例如，Gatsby 使用 <code>path.relative()</code> 方法帮助同步静态文件目录。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> syncStaticDir = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-keyword">const</span> staticDir = nodePath.join(process.cwd(), <span class="hljs-string">`static`</span>)
  chokidar
    .watch(staticDir)
    .on(<span class="hljs-string">`add`</span>, <span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
      <span class="hljs-keyword">const</span> relativePath = nodePath.relative(staticDir, path)
      fs.copy(path, <span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/public/<span class="hljs-subst">$&#123;relativePath&#125;</span>`</span>)
    &#125;)
    .on(<span class="hljs-string">`change`</span>, <span class="hljs-function"><span class="hljs-params">path</span> =></span> &#123;
      <span class="hljs-keyword">const</span> relativePath = nodePath.relative(staticDir, path)
      fs.copy(path, <span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/public/<span class="hljs-subst">$&#123;relativePath&#125;</span>`</span>)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，假设用户向 <code>static</code> 目录添加了一个新文件 <code>main.js</code>。Chokidar 调用 <code>on('add')</code> 事件处理程序，路径设置为 <code>static/main.js</code>。但是，当您将文件复制到 <code>/public</code> 时，不需要额外的 <code>static/</code>。</p>
<p>调用 <code>path.relative('static', 'static/main.js')</code> 返回 <code>static/main.js</code> 相对于 <code>static</code> 的路径，这正是您想要将 <code>static</code> 的内容复制到 <code>public</code> 的路径。</p>
<h2 data-id="heading-3">跨操作系统路径和 URL</h2>
<p>默认情况下，path 模块会根据 Node 进程运行的操作系统自动在 POSIX（OSX、Linux）和 Windows 模式之间切换。</p>
<p>但是，path 模块确实可以在 POSIX 上使用 Windows path 模块，反之亦然。<code>path.posix</code> 和 <code>path.win32</code> 属性分别包含 path 模块的 Posix 和 Windows 版本。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 返回 'path\to\test.txt'，与操作系统无关</span>
path.win32.join(<span class="hljs-string">'path'</span>, <span class="hljs-string">'to'</span>, <span class="hljs-string">'test.txt'</span>)
​
<span class="hljs-comment">// 返回 'path/to/test.txt'，与操作系统无关</span>
path.posix.join(<span class="hljs-string">'path'</span>, <span class="hljs-string">'to'</span>, <span class="hljs-string">'test.txt'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在大多数情况下，根据检测到的操作系统自动切换 path 模块是正确的行为。但是，使用 <code>path.posix</code> 和 <code>path.win32</code> 属性对于总是希望输出 Windows 或 Linux 样式路径的测试或应用程序可能会有所帮助。</p>
<p>例如，一些应用程序使用 <code>path.join()</code> 和 <code>path.extname()</code> 等方法处理 URL 路径。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 'https://api.mydomain.app/api/v2/me'</span>
<span class="hljs-string">'https://api.mydomain.app/'</span> + path.join(<span class="hljs-string">'api'</span>, <span class="hljs-string">'v2'</span>, <span class="hljs-string">'me'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法适用于 Linux 和 OSX，但如果有人试图将您的应用程序部署到一些无服务器上会发生什么？</p>
<p>你最终会得到 <code>https://api.mydomain.app/api\v2\me</code>，这不是有效的 URL！如果使用 path 模块操作 URL，则应使用 <code>path.posix</code>。</p></div>  
</div>
            