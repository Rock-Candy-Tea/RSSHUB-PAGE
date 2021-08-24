
---
title: '让 Node.js 变_懒_的 COW 技术'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21158ca9a4134b0f9a66247c9245c492~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 21:44:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21158ca9a4134b0f9a66247c9245c492~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>COW 不是奶牛，是 Copy-On-Write 的缩写，这是一种是复制但也不完全是复制的技术。</p>
<p>一般来说复制就是创建出完全相同的两份，两份是独立的：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21158ca9a4134b0f9a66247c9245c492~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是，有的时候复制这件事没多大必要，完全可以复用之前的，这时候可以只是引用之前的那份，在写内容的时候才去复制对应的一部分内容。这样如果内容用于读的话，就免去了复制，而如果需要写，才会真正复制部分内容来做修改。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b8044ca487240e8892214997aff7025~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就叫做“写时复制”，也就是 Copy-On-Write。</p>
<p>原理很简单，但是在操作系统的内存管理和文件系统中却很常见，Node.js 里面也因为这种技术变“懒”了。</p>
<p>本文我们来探究下 Copy-On-Write 在 Node.js 的进程创建和文件复制的应用：</p>
<h2 data-id="heading-0">文件复制</h2>
<p>文件复制这件事最常见的思路就是完全写一份相同的文件内容到另一个位置，但是这样有两个问题：</p>
<ul>
<li>完全写一份相同的内容，如果同样的文件复制了几百次，那么也创建相同的内容几百次么？太浪费硬盘空间了</li>
<li>如果写到一半断电了怎么办？覆盖的内容如何恢复？</li>
</ul>
<p>怎么办呢？这时候操作系统设计者就想到了 COW 技术。</p>
<p>用 COW 技术实现文件复制以后完美解决了上面两个问题：</p>
<ul>
<li>复制只是添加一个引用到之前的内容，如果不修改并不会真正复制，只有到第一次修改内容的时候才去真正复制对应的数据块，这样就避免了大量硬盘空间的浪费。</li>
<li>写文件时会先在另一个空闲磁盘块做修改，等修改完之后才会复制到目标位置，这样就不会有断电无法回滚的问题</li>
</ul>
<p>在 Node.js 的 fs.copyFile 的 api  就可以使用 Copy-On-Write 模式：</p>
<p>默认情况下，copyFile 会写入目标文件，覆盖原内容</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fsPromises = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>).promises;

(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> fsPromises.copyFile(<span class="hljs-string">'source.txt'</span>, <span class="hljs-string">'destination.txt'</span>);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-built_in">console</span>.log(e.message);
  &#125;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是可以通过第三个参数指定复制的策略：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> fsPromises = fs.promises;
<span class="hljs-keyword">const</span> &#123; COPYFILE_EXCL, COPYFILE_FICLONE, COPYFILE_FICLONE_FORCE&#125; = fs.constants;

(<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> fsPromises.copyFile(<span class="hljs-string">'source.txt'</span>, <span class="hljs-string">'destination.txt'</span>, COPYFILE_FICLONE);
  &#125; <span class="hljs-keyword">catch</span>(e) &#123;
    <span class="hljs-built_in">console</span>.log(e.message);
  &#125;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>支持的 flag 有 3 个：</p>
<ul>
<li>COPYFILE_EXCL: 如果目标文件已存在，会报错（默认是覆盖）</li>
<li>COPYFILE_FICLONE: 以 copy-on-write 模式复制，如果操作系统不支持就转为真正的复制（默认是直接复制）</li>
<li>COPYFILE_FICLONE_FORCE：以 copy-on-write 模式复制，如果操作系统不支持就报错</li>
</ul>
<p>这3个常量分别是 1，2，4，可以通过按位或把它们合并之后传入：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> flags = COPYFILE_FICLONE | COPYFILE_EXCL;
fsPromises.copyFile(<span class="hljs-string">'source.txt'</span>, <span class="hljs-string">'destination.txt'</span>, flags);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Node.js 支持操作系统的 copy-on-write 技术，在一些场景下可以提升性能，建议使用 COPYFILE_FICLONE 的方式，会比默认的方式好一些。</p>
<h2 data-id="heading-1">进程创建</h2>
<p>fork 是常见的创建进程的方式，而它的实现就是一种 copy-on-write 技术。</p>
<p>我们知道，进程在内存中分为代码段、数据段、堆栈段这 3 部分：</p>
<ul>
<li>代码段：存放要执行的代码</li>
<li>数据段：存放一些全局数据</li>
<li>堆栈段：存放执行的状态</li>
</ul>
<p>如果基于该进程创建一个新的进程，那么要复制这 3 部分内存。而如果这三部分内存是一样的内容，那就浪费了内存空间。</p>
<p>所以 fork 并不会真正的复制内存，而是创建一个新的进程，引用父进程的内存，当做数据的修改的时候，才会真正复制该部分的内存。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b20d930ee8b4fab907f89e1d7336691~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这也是为什么把进程创建叫做 fork，也就是分叉，因为不完全是独立的，只是某部分做了分叉，成了两份，但是大部分还是一样的。</p>
<p>但如果要执行的代码不一样怎么办呢，这时候就要用 exec 了，它会创建新的代码段、数据段、堆栈段、执行新的代码。</p>
<p>Node.js 里面同样可以用 fork 和 exec 的 api：</p>
<p>fork:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> cluster = <span class="hljs-built_in">require</span>(<span class="hljs-string">'cluster'</span>);

<span class="hljs-keyword">if</span> (cluster.isMaster) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'I am master'</span>);
  cluster.fork();
  cluster.fork();
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (cluster.isWorker) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`I am worker #<span class="hljs-subst">$&#123;cluster.worker.id&#125;</span>`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exec:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; exec &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);
exec(<span class="hljs-string">'my.bat'</span>, <span class="hljs-function">(<span class="hljs-params">err, stdout, stderr</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (err) &#123;
    <span class="hljs-built_in">console</span>.error(err);
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-built_in">console</span>.log(stdout);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fork 是 linux 进程创建的基础，由此可见 copy-on-write 技术多么重要了。</p>
<h2 data-id="heading-2">总结</h2>
<p>复制同样的内容多份无疑比较浪费空间，所以操作系统在做文件复制、进程创建时的内存复制的时候都采用了 Copy-On-Write 技术，只有真正修改的时候才会去做复制。</p>
<p>Node.js 支持了 fs.copyFile 的 flags 的设置，可以指定 COPYFILE_FICLONE 来使用 Copy-On-Write 的方式做文件复制，也建议大家使用这种方式来节省硬盘空间，提高文件复制的性能。</p>
<p>进程的 fork 也是 Copy-On-Write 的实现，并不会直接复制进程的代码段、数据段、堆栈段到新的内容，而是引用之前的，只有在修改的时候才会做真正的内存复制。</p>
<p>除此以外，Copy-On-Write 在 Immutable 的实现，在分布式的读写分离等领域都有很多应用。</p>
<p>COW 让 Node.js 变“懒”了，但性能却更高了。</p></div>  
</div>
            