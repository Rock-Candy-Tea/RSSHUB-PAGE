
---
title: '「学习笔记」child_process'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f330b8a9ca74057a5035fd905e3a77c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 01:24:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f330b8a9ca74057a5035fd905e3a77c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">child_process</h2>
<p>child_process 用于创建衍生子进程。Node 和衍生的子进程建立 stdin(标准输入), stdout(标准输出), stderr(标准错误) 管道。child_process.spawn, child_process.fork, child_process.exec, child_process.execFile 都会返回 ChildProcess 实例。ChildProcess 实例实现了 EventEmitter API，可以在子进程实例上添加事件的回调函数。进程之间可以通过事件消息系统进行互相通信。</p>
<h3 data-id="heading-1">child_process.spawn</h3>
<p>启动一个子进程，执行命令。spawn 的接口定义: <code>spawn(command: string, args: ReadonlyArray<string>, options: SpawnOptions): ChildProcess</code></p>
<ul>
<li>command, 需要运行的命令</li>
<li>args, 运行命令的参数, 是一个字符串数组</li>
<li>options, 配置项
<ul>
<li>options.cwd 子进程的工作目录</li>
<li>options.env 环境变量, 使用 key, value 配置环境变量</li>
<li>等等</li>
</ul>
</li>
<li>返回值 ChildProcess, 返回 ChildProcess 的实例</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 例子</span>
<span class="hljs-keyword">const</span> &#123; spawn, spawnSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> cp = spawn(<span class="hljs-string">'ls'</span>, [<span class="hljs-string">'-a'</span>], &#123;
  <span class="hljs-attr">cwd</span>: path.resolve(__dirname, <span class="hljs-string">'../Movies'</span>)
&#125;)

cp.stdout.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`子进程输出:' <span class="hljs-subst">$&#123;data&#125;</span>`</span>)
&#125;)

cp.on(<span class="hljs-string">'exit'</span>, <span class="hljs-function">(<span class="hljs-params">code, signal</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'子进程退出:'</span>, <span class="hljs-string">`code <span class="hljs-subst">$&#123;code&#125;</span> and signal <span class="hljs-subst">$&#123;signal&#125;</span>`</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f330b8a9ca74057a5035fd905e3a77c~tplv-k3u1fbpfcp-watermark.image" alt="child_process.spawn1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>默认情况下，子进程的标准输入、标准输出和标准错误被重定向到 ChildProcess 对象上相应的 subprocess.stdin, subprocess.stdout 和 subprocess.stderr 流。可以设置 options.stdio: inherit, 传入父进程,</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; spawn, spawnSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> cp = spawn(<span class="hljs-string">'ls'</span>, [<span class="hljs-string">'-a'</span>], &#123;
  <span class="hljs-attr">cwd</span>: path.resolve(__dirname, <span class="hljs-string">'../Movies'</span>),
  <span class="hljs-attr">stdio</span>: <span class="hljs-string">'inherit'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">child_process.spawnSync</h4>
<blockquote>
<p>child_process.spawn 的同步版本。child_process.spawnSync 返回 Object。Object 包含了: pid(子进程pid), stdout(标准输出), stderr(标准错误) 等等。不同之处在于该函数在子进程完全关闭之前不会返回。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; spawnSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)


<span class="hljs-keyword">const</span> obj = spawnSync(<span class="hljs-string">'ls'</span>, [<span class="hljs-string">'-a'</span>],&#123; <span class="hljs-attr">cwd</span>: path.resolve(__dirname, <span class="hljs-string">'../Movies'</span>) &#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'pid'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;obj.pid&#125;</span>`</span>)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stdout'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;obj.stdout&#125;</span>`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">child_process.exec</h3>
<p>创建一个衍生的 shell, 然后可以在衍生的 shell 之中执行命令。exec 实现了函数重载。第二个参数可以是配置项，或者是 callback。如果第二个参数是配置项，那么第三个参数就是 callback。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; exec &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

exec(<span class="hljs-string">'ls'</span>, <span class="hljs-function">(<span class="hljs-params">error, stdout, stderr</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (error) &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'error:'</span>, error);
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stdout: '</span> + stdout);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stderr: '</span> + stderr);
&#125;)

<span class="hljs-comment">// 第二个参数可以是配置项</span>
exec(<span class="hljs-string">'ls -a'</span>, &#123; <span class="hljs-attr">cwd</span>: path.resolve(__dirname, <span class="hljs-string">'../Movies'</span>), &#125;, <span class="hljs-function">(<span class="hljs-params">error, stdout, stderr</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (error) &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'error:'</span>, error);
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stdout: '</span> + stdout);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stderr: '</span> + stderr);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>callback 的三个参数分别是错误实例（如果执行成功, error 等于 null）, stdout 标准输出, stderr 标准错误。</p>
<h4 data-id="heading-4">child_process.execSync</h4>
<blockquote>
<p>child_process.exec 的同步版本。child_process.execSync 方法返回标准输出，不同之处在于该方法在子进程完全关闭之前不会返回。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; execSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> stdout = execSync(<span class="hljs-string">'ls -a'</span>, &#123; <span class="hljs-attr">cwd</span>: path.resolve(__dirname, <span class="hljs-string">'../Movies'</span>) &#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stdout:'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;stdout&#125;</span>`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">child_process.exec 和 child_process.spawn 区别</h3>
<ul>
<li>spawn
<ol>
<li>不会创建衍生的 shell</li>
<li>流式的传输子进程产生的数据</li>
<li>没有数据大小的限制</li>
</ol>
</li>
<li>exec
<ol>
<li>会创建衍生的 shell</li>
<li>最大传输 200kb 的数据</li>
<li>会缓存数据, 进程关闭后传输数据</li>
</ol>
</li>
</ul>
<p>spawn 适合巨大长时间的传输数据。exec 适合需要多次，小量的情况。</p>
<h3 data-id="heading-6">child_process.fork</h3>
<p>child_process.fork, 用于在子进程中运行模块。child_process.fork(modulePath [, args] [, options])</p>
<ul>
<li>modulePath, 需要在子进程中运行的模块地址</li>
<li>args, 字符串参数列表</li>
<li>options 配置项
<ul>
<li>execPath, 用来创建子进程的可执行文件。我们可以通过配置这个参数，指定不同版本的 node 创建子进程。</li>
<li>execArgv, 传给可执行文件的字符串参数列表。</li>
<li>silent, 子进程的标准输出, 是否从父进程进行继承。默认是 false 进行继承。如果设置为 true 则直接 pipe 向子进程的 child.stdin, child.stdout 等。</li>
<li>stdio, 用于配置在父进程和子进程之间建立的管道</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子进程的代码</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是子进程'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; fork &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-comment">// 我是子进程</span>
fork(resolve(__dirname, <span class="hljs-string">'./cp.js'</span>), &#123;
  <span class="hljs-attr">silent</span>: <span class="hljs-literal">false</span>
&#125;)

<span class="hljs-comment">// 没有打印</span>
fork(resolve(__dirname, <span class="hljs-string">'./cp.js'</span>), &#123;
  <span class="hljs-attr">silent</span>: <span class="hljs-literal">true</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; fork &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> cp = fork(resolve(__dirname, <span class="hljs-string">'./cp.js'</span>), &#123;
  <span class="hljs-attr">silent</span>: <span class="hljs-literal">true</span>
&#125;)

cp.stdout.on(<span class="hljs-string">'data'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-comment">// stdout 中输出： 我是子进程</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'stdout 中输出：'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;data&#125;</span>`</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 stdout 属性，可以获取到子进程输出的内容</p>
<h3 data-id="heading-7">child_process.execFile</h3>
<p>child_process.execFile 不会创建衍生的 shell。效率要比 exec 要高。child_process.execFile(file[, args] [, options] [, callback])</p>
<ul>
<li>file, 可以是执行文件的名字，或者路径。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; execFile &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>)
<span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

execFile(<span class="hljs-string">'node'</span>, [resolve(__dirname, <span class="hljs-string">'./cp.js'</span>)], <span class="hljs-function">(<span class="hljs-params">err, stdout, stderr</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (err) &#123;
    <span class="hljs-keyword">throw</span> err
  &#125;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`stdout: <span class="hljs-subst">$&#123;stdout&#125;</span>`</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">child_process.exec 和 child_process.execFile 的区别</h3>
<p>exec 内部通过调用 execFile 来实现。而 execFile 内部通过调用 spawn 来实现。</p>
<h2 data-id="heading-9">事件</h2>
<p>ChildProcess 实例上可以监听很多事件</p>
<ul>
<li>close, 子进程的 stdio 流关闭时触发</li>
<li>disconnect, 父进程手动调用 child.disconnect 函数时触发</li>
<li>error, 产生错误时会触发</li>
<li>exit, 子进程退出时触发</li>
<li>message, 子进程使用 process.send 函数来传递消息时触发</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; fork &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);

<span class="hljs-keyword">const</span> cp = fork(<span class="hljs-string">'./cp.js'</span>)

cp.on(<span class="hljs-string">'close'</span>, <span class="hljs-function">(<span class="hljs-params">code, signal</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'close 事件：'</span>, code, signal);
&#125;)

cp.on(<span class="hljs-string">'disconnect'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'disconnect 事件...'</span>);
&#125;)

cp.on(<span class="hljs-string">'error'</span>, <span class="hljs-function">(<span class="hljs-params">code, signal</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'error 事件：'</span>, code, signal);
&#125;)

cp.on(<span class="hljs-string">'exit'</span>, <span class="hljs-function">(<span class="hljs-params">code, signal</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'exit 事件：'</span>, code, signal);
&#125;)

cp.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'message 事件：'</span>, val);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">进程之间的通信</h2>
<p>创建子进程后, 父进程与子进程之间将会创建 IPC 通道，父子进程之间通过 message 和 send 来通信。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父进程</span>
<span class="hljs-keyword">const</span> &#123; fork &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);

<span class="hljs-keyword">const</span> cp = fork(<span class="hljs-string">'./cp.js'</span>)

cp.on(<span class="hljs-string">'message'</span>, <span class="hljs-function">(<span class="hljs-params">msg</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'message: '</span> + <span class="hljs-built_in">JSON</span>.stringify(msg))
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子进程</span>
process.send(&#123;
  <span class="hljs-attr">msg</span>: <span class="hljs-string">'我是子进程'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父进程也可以向子进程发送消息使用 <code>cp.send</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父进程</span>
<span class="hljs-keyword">const</span> &#123; fork &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);

<span class="hljs-keyword">const</span> cp = fork(<span class="hljs-string">'./cp.js'</span>)

cp.send(&#123;
  <span class="hljs-attr">msg</span>: <span class="hljs-string">'我是父进程'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.cn%2Fapi%2Fchild_process.html%23child_process_child_process" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.cn/api/child_process.html#child_process_child_process" ref="nofollow noopener noreferrer">Node.js v16.8.0 文档</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fnode-js-child-processes-everything-you-need-to-know-e69498fe970a%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.freecodecamp.org/news/node-js-child-processes-everything-you-need-to-know-e69498fe970a/" ref="nofollow noopener noreferrer">Node.js Child Processes: Everything you need to know</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F46445805%2Fexec-vs-execfile-nodejs" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/46445805/exec-vs-execfile-nodejs" ref="nofollow noopener noreferrer">exec vs execFile nodeJs</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F48698234%2Fnode-js-spawn-vs-execute" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/48698234/node-js-spawn-vs-execute" ref="nofollow noopener noreferrer">Node.js Spawn vs. Execute</a></li>
<li><a href="https://juejin.cn/post/6844903456373735431#heading-28" target="_blank" title="https://juejin.cn/post/6844903456373735431#heading-28">Nodejs进阶：如何玩转子进程（child_process）</a></li>
<li><a href="https://juejin.cn/post/6844903908385488903" target="_blank" title="https://juejin.cn/post/6844903908385488903">深入理解Node.js 中的进程与线程</a></li>
<li><a href="https://juejin.cn/post/6913498911973834759" target="_blank" title="https://juejin.cn/post/6913498911973834759">Node.js process 模块学习指南</a></li>
<li><a href="https://juejin.cn/post/6882290865763680264#heading-5" target="_blank" title="https://juejin.cn/post/6882290865763680264#heading-5">玩转 node 子进程 — child_process</a></li>
</ul></div>  
</div>
            