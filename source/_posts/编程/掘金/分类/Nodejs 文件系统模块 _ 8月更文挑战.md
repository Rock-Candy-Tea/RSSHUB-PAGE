
---
title: 'Node.js 文件系统模块 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7349'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 07:03:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=7349'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>文件系统模块（简称 <code>fs</code>）允许我们访问计算机上的文件系统并与之交互。</p>
<p>使用 <code>fs</code> 模块，我们可以执行以下操作：</p>
<ul>
<li>创建文件和目录</li>
<li>修改文件和目录</li>
<li>删除文件和目录</li>
<li>读取文件和目录的内容</li>
<li>...</li>
</ul>
<blockquote>
<p><strong>建议</strong>：文件系统模块比较复杂，建议查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fdocs%2Flatest-v16.x%2Fapi%2Ffs.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/docs/latest-v16.x/api/fs.html" ref="nofollow noopener noreferrer">官方文档</a>，你可以看到所有的方法。</p>
</blockquote>
<p>本文将向您介绍最常见和最有用的 <code>fs</code> 方法。事不宜迟，让我们看看这些方法是什么。</p>
<h2 data-id="heading-0">如何使用 <code>fs</code></h2>
<p>文件系统模块是一个核心的 Node.js 模块。这意味着我们不必安装它。我们唯一需要做的就是将 <code>fs</code> 模块导入到自己的文件中。</p>
<p>因此，在文件顶部添加：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们可以使用前缀 <code>fs</code> 从文件系统模块调用任何方法。</p>
<p>或者，我们可以只从 <code>fs</code> API 导入所需的方法，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; writeFile, readFile &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意</strong>：为了方便起见，我们还需要导入 <code>path</code> 模块。它是另一个核心 Node.js 模块，它允许我们使用文件和目录路径。</p>
</blockquote>
<p>导入 <code>fs</code> 模块后，在文件中添加：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用文件系统模块时，<code>path</code> 模块不是必需的。但它对我们有很大的帮助！</p>
<h2 data-id="heading-1">同步与异步</h2>
<p><strong>需要注意的是</strong>，默认情况下，所有 <code>fs</code> 方法都是异步的。但是，我们可以通过在方法末尾添加 <code>Sync</code> 来使用同步版本。</p>
<p>例如，<code>writeFile</code> 方法的同步版本为 <code>writeFileSync</code>。同步方法将同步的完成代码，因此它们阻塞了主线程。阻塞 Node.js 中的主线程被认为是不好的做法，我们不应该这么做。</p>
<p>因此，以下我们都将使用文件系统模块中的异步方法。</p>
<h2 data-id="heading-2">写入文件</h2>
<p>要从 Node.js 应用程序写入文件，请使用 <code>writeFile</code> 方法。</p>
<p><code>writeFile</code> 方法至少接受以下参数：</p>
<ul>
<li>文件名</li>
<li>内容</li>
<li>回调</li>
</ul>
<p>如果指定的文件已经存在，它会将旧内容替换为您作为参数提供的内容。如果指定的文件不存在，则创建一个新文件。</p>
<p>导入 <code>fs</code> 和 <code>path</code> 模块后，在文件中编写以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">fs.writeFile(<span class="hljs-string">'content.txt'</span>, <span class="hljs-string">'All work and no play makes Jack a dull boy!'</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
​
  process.stdout.write(<span class="hljs-string">'创建成功!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码将创建了一个名为 <code>content.txt</code> 的新文件，并添加了文本 <code>All work and no play makes Jack a dull boy!</code> 作为内容。如果存在任何错误，回调函数将抛出该错误。否则，它将向控制台输出文件创建成功。</p>
<p><code>writeFile</code> 还有其他变体，例如：</p>
<ul>
<li><code>fs.writeFileSync</code> — 同步写入文件</li>
<li><code>fsPromises.writeFile</code> — 使用基于 Promise 的 API 写入文件</li>
</ul>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2F571ba06c06214b5c8744036c6500af92" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/571ba06c06214b5c8744036c6500af92" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote>
<h2 data-id="heading-3">从文件中读取</h2>
<p>在读取文件之前，需要创建并存储文件的路径。<code>path</code> 模块的路径在这里很方便。</p>
<p>使用 <code>join</code> 模块中的 <code>path</code> 方法，您可以创建文件路径，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> filePath = path.join(process.cwd(), <span class="hljs-string">'content.txt'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个参数 <code>process.cwd()</code> 返回当前工作目录。现在您已经有了文件路径，可以读取文件的内容了。</p>
<p>在文件中编写以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">fs.readFile(filePath, <span class="hljs-function">(<span class="hljs-params">error, content</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">throw</span> error
​
  process.stdout.write(content)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>readFile</code> 方法至少接受两个参数：</p>
<ul>
<li>文件的路径</li>
<li>回调</li>
</ul>
<p>如果有错误，它会抛出一个错误。否则，它会在终端中输出文件内容。</p>
<p><code>readFile</code> 还有其他变体，例如：</p>
<ul>
<li><code>fs.readFileSync</code> — 同步写入文件</li>
<li><code>fsPromises.readFile</code> — 使用基于 Promise 的 API 写入文件</li>
</ul>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2Fbadc2a539a44412892a0e05a9575d54d" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/badc2a539a44412892a0e05a9575d54d" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote>
<h2 data-id="heading-4">读取目录的内容</h2>
<p>在目录中显示文件与读取文件内容非常相似。但是，不是传递文件路径，而是传递当前工作目录（我们可以传递任何其他目录）。</p>
<p>然后，传递一个回调函数来处理响应。在文件中编写以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">fs.readdir(process.cwd(), <span class="hljs-function">(<span class="hljs-params">error, files</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">throw</span> error
​
  <span class="hljs-built_in">console</span>.log(files)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到目前为止，我们只使用 <code>process.stdout.write</code> 将内容输出到终端。但是，您可以简单地使用 <code>console.log</code>，就像上面的代码片段一样。</p>
<p>如果运行该应用程序，我们应该会得到一个包含目录中所有文件的数组。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2Ff82c4e6ae3acd5d97efdecb0bc67979e" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/f82c4e6ae3acd5d97efdecb0bc67979e" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote>
<h2 data-id="heading-5">删除文件</h2>
<p>文件系统模块有一种方法，允许您删除文件。但是，需要注意的是，它只适用于文件，不适用于目录。</p>
<p>当以文件路径作为参数调用 <code>unlink</code> 方法时，它将删除该文件。将以下代码段添加到文件中：</p>
<pre><code class="hljs language-js copyable" lang="js">fs.unlink(filePath, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">throw</span> error
​
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'文件已删除!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您重新运行代码，您的文件将被删除！</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2Fb1201434218c400f77e042109bfce99e" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/b1201434218c400f77e042109bfce99e" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote>
<h2 data-id="heading-6">创建目录</h2>
<p>我们可以使用 <code>mkdir</code> 方法异步创建目录。在文件中编写以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">fs.mkdir(<span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/myFolder/secondFolder`</span>, &#123; <span class="hljs-attr">recursive</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
​
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'已成功创建文件夹!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，要在当前工作目录中创建一个新文件夹。如前所述，您可以使用 <code>cwd()</code> 方法从 <code>process</code> 对象获取当前工作目录。</p>
<p>然后，传递要创建的一个或多个文件夹。但是，这并不意味着您必须在当前工作目录中创建新文件夹。你可以在任何地方创建它们。</p>
<p>现在，第二个参数是递归选项。如果未将其设置为 <code>true</code>，则无法创建多个文件夹。如果将 <code>recursive</code> 选项设置为 <code>false</code>，上述代码将给出一个错误。<strong>试试看！</strong></p>
<p>但是，如果您只想创建一个文件夹，则无需将 <code>recursive</code> 选项设置为 <code>true</code>。</p>
<p>以下代码可以正常工作！</p>
<pre><code class="hljs language-js copyable" lang="js">fs.mkdir(<span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/myFolder`</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
​
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'已成功创建文件夹!'</span>)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，我想强调使用 <code>recursive</code>。如果要在文件夹中创建文件夹，则需要将其设置为 <code>true</code>。它将创建所有文件夹，即使它们不存在。</p>
<p>另一方面，如果您只想创建一个文件夹，可以将其保留为 <code>false</code>。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2F09bad802541102c0cce2a2e4c3985066" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/09bad802541102c0cce2a2e4c3985066" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote>
<h2 data-id="heading-7">删除目录</h2>
<p>删除目录的逻辑类似于创建目录。如果您查看为创建目录而编写的代码和下面的代码，您会发现相似之处。</p>
<p>因此，在文件中编写以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">fs.rmdir(<span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/myFolder/`</span>, &#123; <span class="hljs-attr">recursive</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
​
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'已成功删除文件夹!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用文件系统模块中的 <code>rmdir</code> 方法，并传递以下参数：</p>
<ul>
<li>要删除的目录</li>
<li>递归属性</li>
<li>回调</li>
</ul>
<p>如果将 <code>recursive</code> 属性设置为 <code>true</code>，它将删除文件夹及其内容。请务必注意，如果文件夹中包含内容，则<strong>需要将其设置为 <code>true</code></strong>。否则，您将得到一个错误。</p>
<p>以下代码段仅在文件夹为空时有效：</p>
<pre><code class="hljs language-js copyable" lang="js">fs.rmdir(<span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/myFolder/`</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'已成功删除文件夹!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 <code>myFolder</code> 中有其他文件和/或文件夹，如果未传递 <code>&#123; recursive: true &#125;</code>，则会出现错误。</p>
<p>知道何时使用 <code>recursive</code> 选项以及何时不避免问题是很重要的。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2Fa8cb6aca75cef8d6ac5043eae9ba22ce" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/a8cb6aca75cef8d6ac5043eae9ba22ce" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote>
<h2 data-id="heading-8">目录/文件重命名</h2>
<p>使用 <code>fs</code> 模块，您可以重命名目录和文件。下面的代码片段显示了如何使用 <code>rename</code> 方法进行此操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 重命名一个目录</span>
fs.rename(<span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/myFolder/secondFolder`</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/myFolder/newFolder`</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'目录重命名!'</span>)
&#125;);

<span class="hljs-comment">// 重命名一个文件</span>
fs.rename(<span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/content.txt`</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;process.cwd()&#125;</span>/newFile.txt`</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'文件重命名!'</span>)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>rename</code> 方法包含三个参数：</p>
<ul>
<li>第一个参数是现有的文件夹/文件</li>
<li>第二个参数是新名称</li>
<li>回调</li>
</ul>
<p>因此，要重命名文件或目录，我们需要传递当前文件/目录的名称和新名称。运行应用程序后，应更新目录/文件的名称。</p>
<blockquote>
<p><strong>需要注意的是</strong>，如果新路径已经存在（例如，文件/文件夹的新名称），它将被覆盖。因此，请确保不要错误地覆盖现有文件/文件夹。</p>
</blockquote>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2F5c3e7c6ae39d09996ff67175a719122e" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/5c3e7c6ae39d09996ff67175a719122e" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote>
<h2 data-id="heading-9">向文件中添加内容</h2>
<p>我们还可以使用 <code>appendFile</code> 方法向现有文件添加新内容。</p>
<p>如果比较 <code>writeFile</code> 和 <code>appendFile</code> 这两种方法，我们可以发现它们是相似的。传递文件路径、内容和回调。</p>
<pre><code class="hljs language-js copyable" lang="js">fs.appendFile(filePath, <span class="hljs-string">'\nAll work and no play makes Jack a dull boy!'</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err
  
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'All work and no play makes Jack a dull boy!'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码片段演示了如何向现有文件添加新内容。如果运行应用程序并打开文件，您应该会看到其中的新内容。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fcatalinpit%2F7c8d40db53dea9e6831f9ee89d92475c" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/catalinpit/7c8d40db53dea9e6831f9ee89d92475c" ref="nofollow noopener noreferrer">点击此处查看此要点</a></p>
</blockquote></div>  
</div>
            