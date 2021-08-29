
---
title: 'node中常用第三方工具库介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8047'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 08:46:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=8047'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一、minimist （命令行参数解析）</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsubstack%2Fminimist" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/substack/minimist" ref="nofollow noopener noreferrer">gitHub</a></p>
<p>先了解下<code>process.argv</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 假设有以下脚本：</span>
process.argv.forEach(<span class="hljs-function">(<span class="hljs-params">val, index</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;index&#125;</span>: <span class="hljs-subst">$&#123;val&#125;</span>`</span>)
&#125;)

<span class="hljs-comment">// 启动脚本：</span>
node process-argv.js one two=three four

<span class="hljs-comment">// 输出：</span>
<span class="hljs-number">0</span>: <span class="hljs-regexp">/usr/</span>local/bin/node <span class="hljs-comment">// process.execPath</span>
<span class="hljs-number">1</span>: <span class="hljs-regexp">/Users/m</span>jr/work/node/process-args.js <span class="hljs-comment">// 脚本文件的地址</span>
<span class="hljs-number">2</span>: one
<span class="hljs-number">3</span>: two=three
<span class="hljs-number">4</span>: four
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>process.argv</code>可以获取运行脚本时的命令行参数，而之所以常用<code>process.argv.slice(2)</code>，是因为一般第二个参数后才是我们需要的。
再来看<code>minimist</code>的用法及例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> args = <span class="hljs-built_in">require</span>(<span class="hljs-string">'minimist'</span>)(process.argv.slice(<span class="hljs-number">2</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举例：</p>
<pre><code class="hljs language-js copyable" lang="js">node test.js -a a -b b
<span class="hljs-comment">// args: &#123;_: [], a: 'a', b: 'b'&#125;</span>

node test.js -x <span class="hljs-number">3</span> -y <span class="hljs-number">4</span> -n5 -abc --beep=boop foo bar baz
<span class="hljs-comment">// &#123; _: [ 'foo', 'bar', 'baz' ],</span>
<span class="hljs-comment">// x: 3,</span>
<span class="hljs-comment">// y: 4,</span>
<span class="hljs-comment">// n: 5,</span>
<span class="hljs-comment">// a: true,</span>
<span class="hljs-comment">// b: true,</span>
<span class="hljs-comment">// c: true,</span>
<span class="hljs-comment">// beep: 'boop' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>minimist会解析参数，并放到一个对象中，方便在脚本中读取。特别要说明的是其中首个key是<code>_</code>，它的值是个数组，包含的是所有没有关联选项的参数。</p>
<h4 data-id="heading-1">二、chalk（终端多色彩输出）</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchalk%2Fchalk" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chalk/chalk" ref="nofollow noopener noreferrer">gitHub</a></p>
<p>用于终端显示多色彩输出</p>
<p>基本用法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>);

<span class="hljs-comment">// 基础用法</span>
<span class="hljs-built_in">console</span>.log(chalk.red(<span class="hljs-string">'red'</span>, <span class="hljs-string">'red2'</span>));
<span class="hljs-built_in">console</span>.log(chalk.red(<span class="hljs-string">'red'</span>));

<span class="hljs-comment">// 拼接</span>
<span class="hljs-built_in">console</span>.log(chalk.red(<span class="hljs-string">'red'</span>) + <span class="hljs-string">'middle'</span> + chalk.blue(<span class="hljs-string">'blue'</span>));

<span class="hljs-comment">// 多个样式</span>
<span class="hljs-built_in">console</span>.log(chalk.blue.bgRed.bold(<span class="hljs-string">'hello world'</span>));

<span class="hljs-comment">// 组合</span>
<span class="hljs-built_in">console</span>.log(chalk.red(<span class="hljs-string">'Hello'</span>, chalk.underline.bgBlue(<span class="hljs-string">'world'</span>) + <span class="hljs-string">'!'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">三、enquirer(终端交互)</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fenquirer%2Fenquirer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/enquirer/enquirer" ref="nofollow noopener noreferrer">gitHub</a></p>
<p>交互式询问用户输入</p>
<p>基本用法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; prompt &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'enquirer'</span>);

<span class="hljs-comment">// 1. 单次询问：</span>
<span class="hljs-keyword">const</span> options = &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'name'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">"What's your name?"</span>
&#125;

<span class="hljs-comment">// 2. 多次询问：</span>
<span class="hljs-keyword">const</span> options = [
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'username'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'What is your username?'</span>
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'password'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'password'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'What is your password?'</span>
    &#125;
  ]
  
<span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> prompt(options);
<span class="hljs-built_in">console</span>.log(res);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一种调用方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 比如input类型：</span>
<span class="hljs-keyword">const</span> &#123; Input &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'enquirer'</span>);
<span class="hljs-keyword">const</span> prompt = <span class="hljs-keyword">new</span> Input(&#123;
  <span class="hljs-attr">message</span>: <span class="hljs-string">'What is your username?'</span>,
  <span class="hljs-attr">initial</span>: <span class="hljs-string">'jonschlinkert'</span>
&#125;);

prompt.run()
  .then(<span class="hljs-function"><span class="hljs-params">answer</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Answer:'</span>, answer))
  .catch(<span class="hljs-built_in">console</span>.log);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次询问都需要指定一个类型<code>type</code>，或引入一个<code>Prompt类</code>。常见的有:</p>
<ol>
<li><code>Input</code>:  普通输入，返回<code>String</code>类型</li>
<li><code>Password</code>:  密码输入，返回<code>String</code>类型</li>
<li><code>Confirm</code>： 确认，返回<code>Boolean</code>类型</li>
<li><code>AutoComplete</code>: 自动补全</li>
<li><code>BasicAuth</code>：基本认证（用户名、密码）</li>
<li><code>Form</code>：表单</li>
<li><code>Invisible</code>：不可见信息</li>
<li><code>MultiSelect</code>: 选择多个</li>
<li><code>Numeral</code>: 数字</li>
</ol>
<h4 data-id="heading-3">四、execa(执行命令)</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fexeca" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/execa" ref="nofollow noopener noreferrer">gitHub</a></p>
<p>相当于我们在终端输入命令并执行</p>
<p>先看原生写法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> util = <span class="hljs-built_in">require</span>(<span class="hljs-string">'util'</span>);
<span class="hljs-keyword">const</span> exec = util.promisify(<span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>).exec);

<span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> exec(<span class="hljs-string">'ls'</span>);
<span class="hljs-comment">// 1. 可以传入cwd参数指定执行的目录</span>
<span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> exec(<span class="hljs-string">'ls'</span>, &#123;<span class="hljs-attr">cwd</span>: path.resolve(__dirname, <span class="hljs-string">'../../test'</span>)&#125;)
<span class="hljs-comment">// 2. 另一种指定执行目录的方法是 process.chdir()</span>
process.chdir(<span class="hljs-string">'../../test'</span>);
<span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> exec(<span class="hljs-string">'ls'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跟原生的<code>exec</code>的主要区别或优势：</p>
<ol>
<li>Promise支持</li>
<li>更高的最大缓冲区。100mb而不是200kb。</li>
<li>按名称执行本地安装的二进制文件。</li>
<li>在父进程终止时清除派生的进程。</li>
<li>更具描述性的错误。</li>
</ol>
<p>基本api及用法：</p>
<ol>
<li>execa(file, arguments?, options?)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; stdout &#125; = <span class="hljs-keyword">await</span> execa(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'status'</span>]);
<span class="hljs-comment">// 指定执行目录同样是传入cwd或者process.chdir()；</span>
<span class="hljs-keyword">const</span> &#123; stdout &#125; = <span class="hljs-keyword">await</span> execa(<span class="hljs-string">'git'</span>, [<span class="hljs-string">'status'</span>], &#123;<span class="hljs-attr">cwd</span>: resolve(<span class="hljs-string">'../demo'</span>)&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>execa.sync(file, arguments?, options?)：同步执行文件</li>
<li>execa.command(command, options?): 与<code>execa()</code>相同，只是文件和参数都在单个命令字符串中指定</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">execa.command(<span class="hljs-string">'git status'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>execa.commandSync(command, options?)：与 <code>execa.command()</code>相同，但是是同步的。</li>
</ol>
<h4 data-id="heading-4">五、fs-extra(操作文件)</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjprichardson%2Fnode-fs-extra" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jprichardson/node-fs-extra" ref="nofollow noopener noreferrer">gitHub</a></p>
<p><code>fs-extra</code>是原生<code>fs</code>的降级，<code>fs</code>中的所有方法都附加到了<code>fs-extra</code>中，并向<code>fs</code>添加了promise支持。如果没有传入回调，所有的fs方法都会返回promise 。</p>
<p>先回顾下原生<code>fs</code>的一些常用方法：</p>
<ol>
<li>获取文件类型：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">p</span> =></span> path.resolve(__dirname, p);

<span class="hljs-keyword">const</span> stat = fs.statSync(resolve(<span class="hljs-string">'../../README.txt'</span>));
<span class="hljs-built_in">console</span>.log(stat.isDirectory()); <span class="hljs-comment">// 是否是文件夹</span>
<span class="hljs-built_in">console</span>.log(stat.isFile()); <span class="hljs-comment">// 是否是文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>文件或目录是否存在：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(fs.existsSync(resolve(<span class="hljs-string">'../fs/fs.js'</span>)));
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>获取目录下的所有文件名</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">fs.readdirSync(path.resolve(__dirname, <span class="hljs-string">'../fs'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>读写(复制文件)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> source = fs.readFileSync(resolve(<span class="hljs-string">'./fs.js'</span>)); <span class="hljs-comment">// 返回的是一个Buffer对象</span>
fs.writeFileSync(resolve(<span class="hljs-string">'./test.js'</span>), source);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>流读写</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> readStream = fs.createReadStream(resolve(<span class="hljs-string">'./1.png'</span>);
readStream.on(<span class="hljs-string">'error'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123; <span class="hljs-comment">// 监听error</span>
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'流读取失败：'</span>, err);
&#125;)
 
<span class="hljs-keyword">const</span> writeStream = fs.createWriteStream(<span class="hljs-string">'./2.png'</span>);
writeStream.on(<span class="hljs-string">'error'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'流写入失败：'</span>, err);
    &#125;)
writeStream.on(<span class="hljs-string">'close'</span>, <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'流写入完成'</span>, data);
 &#125;)
readStream.pipe(writeStream);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>重命名</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">fs.renameSync(resolve(<span class="hljs-string">'./old.js'</span>),resolve(<span class="hljs-string">'./new.js'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>创建文件/目录</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">fs.mkdirSync(resolve(<span class="hljs-string">'./newDir'</span>);
<span class="hljs-comment">// 写入文件（会覆盖之前的内容），文件不存在就创建</span>
fs.writeFileSync(resolve(<span class="hljs-string">'./new.js'</span>, <span class="hljs-string">'console.log(1)'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>删除文件/目录</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">fs.unlinkSync(resolve(<span class="hljs-string">'./newDir/test.js'</span>)); <span class="hljs-comment">// 删除文件</span>
<span class="hljs-comment">// 只能删空目录，要删除非空文件夹，需要先把文件夹里的文件删除，再删除空文件夹</span>
fs.rmdirSync(resolve(<span class="hljs-string">'./newDir'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li>追加文件内容</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> context = <span class="hljs-string">`console.log(111)`</span>;
fs.appendFileSync(resolve(<span class="hljs-string">'./new.js'</span>), context);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来看下<code>fs-extra</code>的一些常用API：</p>
<ol>
<li>copy(src, dest[, options][, callback])：复制文件/文件夹</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fse = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs-extra'</span>);

<span class="hljs-comment">// With a callback:</span>
fs.copy(<span class="hljs-string">'/tmp/myfile'</span>, <span class="hljs-string">'/tmp/mynewfile'</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> <span class="hljs-built_in">console</span>.error(err)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success!'</span>)
&#125;) 

<span class="hljs-comment">// copies file</span>
fs.copy(<span class="hljs-string">'/tmp/mydir'</span>, <span class="hljs-string">'/tmp/mynewdir'</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> <span class="hljs-built_in">console</span>.error(err)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success!'</span>)
&#125;) <span class="hljs-comment">// copies directory, even if it has subdirectories or files</span>

<span class="hljs-comment">// With Promises:</span>
fs.copy(<span class="hljs-string">'/tmp/myfile'</span>, <span class="hljs-string">'/tmp/mynewfile'</span>)
.then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success!'</span>)
&#125;)
.catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.error(err)
&#125;)

<span class="hljs-comment">// With async/await:</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">example</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">await</span> fs.copy(<span class="hljs-string">'/tmp/myfile'</span>, <span class="hljs-string">'/tmp/mynewfile'</span>)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'success!'</span>)
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-built_in">console</span>.error(err)
  &#125;
&#125;

example()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>emptyDir(dir[, callback])：清空目录</li>
</ol>
<p>确保目录是空的。如果目录非空，删除目录下所有内容。如果目录不存在，创建一个空目录。</p>
<ol start="3">
<li>ensureFile(file[, callback])： 创建文件</li>
</ol>
<p>确保文件存在。如果被添加的文件所在的目录不存在,创建该目录。如果文件已经存在了,不进行操作。</p>
<ol start="4">
<li>ensureDir(dir[,options][,callback])： 创建目录</li>
</ol>
<p>确保目录存在。如果不存在，则创建。</p>
<ol start="5">
<li>remove(path[, callback])：删除文件/目录</li>
</ol>
<p>可以删除有内容的目录（这一点比<code>fs</code>优秀）。如果文件/目录存在，不进行任何操作。</p>
<p>本次只介绍几个常用的库的一些基本用法。这些工具库的用法还有很多，如果想更完整的了解，可以点击相应库的gitHub地址查看。</p></div>  
</div>
            