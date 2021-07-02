
---
title: '👏  nodejs写bash脚本终极方案！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9360'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 08:09:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=9360'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>最近在学习<code>bash</code>脚本语法，但是如果对bash语法不是熟手的话，感觉非常容易出错，比如说：显示未定义的变量<code>shell</code>中变量没有定义，仍然是可以使用的，但是它的结果可能不是你所预期的。举个例子：</p>
<pre><code class="hljs language-BASH copyable" lang="BASH"><span class="hljs-comment">#！/bin/bash</span>

<span class="hljs-comment"># 这里是判断变量var是否等于字符串abc，但是var这个变量并没有声明</span>
<span class="hljs-keyword">if</span> [ <span class="hljs-string">"<span class="hljs-variable">$var</span>"</span> = <span class="hljs-string">"abc"</span> ] 
<span class="hljs-keyword">then</span>
   <span class="hljs-comment"># 如果if判断里是true就在控制台打印 “ not abc”</span>
   <span class="hljs-built_in">echo</span>  <span class="hljs-string">" not abc"</span> 
<span class="hljs-keyword">else</span>
   <span class="hljs-comment"># 如果if判断里是false就在控制台打印 “ abc”</span>
   <span class="hljs-built_in">echo</span> <span class="hljs-string">" abc "</span>
<span class="hljs-keyword">fi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果是打印了abc，但问题是，这个脚本应该报错啊，变量并没有赋值算是错误吧。</p>
<p>为了弥补这些错误，我们学会在脚本开头加入：<code>set -u</code>
这句命令的意思是脚本在头部加上它，遇到不存在的变量就会报错，并停止执行。</p>
<p>再次运行就会提示：test.sh: 3: test.sh: num: parameter not set</p>
<p>再想象一下，你本来想删除：<code>rm -rf $dir/*</code>然后dir是空的时候，变成了什么？<code>rm -rf</code>是删除命令，<code>$dir</code>是空的话，相当于执行 <code>rm -rf /*</code>,这是删除所有文件和文件夹。。。然后，你的系统就没了，这就是传说中的删库跑路吗~~~~</p>
<p>如果是<code>node</code>或者浏览器环境，我们直接<code>var === 'abc'</code> 肯定是会报错的,也就是说很多javascript编程经验无法复用到<code>bash</code>来，如果能复用的话，该多好啊。</p>
<p>后来就开始探索，如果用<code>node</code>脚本代替<code>bash</code>该多好啊，经过一天折腾逐渐发现一个神器，<code>Google</code>旗下的<code>zx</code>库，先别着急，我先不介绍这个库，我们先看看目前主流用<code>node</code>如何编写<code>bash</code>脚本，就知道为啥它是神器了。</p>
<h4 data-id="heading-1">node执行bash脚本: 勉强解决方案：child_process API</h4>
<p>例如 <code>child_process</code>的API里面<code>exec</code>命令</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; exec &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"child_process"</span>);

exec(<span class="hljs-string">"ls -la"</span>, <span class="hljs-function">(<span class="hljs-params">error, stdout, stderr</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (error) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`error: <span class="hljs-subst">$&#123;error.message&#125;</span>`</span>);
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-keyword">if</span> (stderr) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`stderr: <span class="hljs-subst">$&#123;stderr&#125;</span>`</span>);
        <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`stdout: <span class="hljs-subst">$&#123;stdout&#125;</span>`</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是，首先<code>exec</code>是异步的，但是我们<code>bash</code>脚本命令很多都是同步的。</p>
<p>而且注意：<code>error</code>对象不同于<code>stderr</code>. <code>error</code>当<code>child_process</code>模块无法执行命令时，该对象不为空。例如，查找一个文件找不到该文件，则error对象不为空。但是，如果命令成功运行并将消息写入标准错误流，则该<code>stderr</code>对象不会为空。</p>
<p>当然我们可以使用同步的<code>exec</code>命令，<code>execSync</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 引入 exec 命令 from child_process 模块</span>
<span class="hljs-keyword">const</span> &#123; execSync &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"child_process"</span>);

<span class="hljs-comment">// 同步创建了一个hello的文件夹</span>
execSync(<span class="hljs-string">"mkdir hello"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再简单介绍一下child_process的其它能够执行bash命令的api</p>
<ul>
<li>spawn： 启动一个子进程来执行命令</li>
<li>exec：启动一个子进程来执行命令，与spawn不同的是，它有一个回调函数能知道子进程的情况</li>
<li>execFile：启动一子进程来执行可执行文件</li>
<li>fork：与spawn类似，不同点是它需要指定子进程需要需执行的javascript文件</li>
</ul>
<p>exec跟ececFile不同的是，exec适合执行命令，eexecFile适合执行文件。</p>
<h4 data-id="heading-2">node执行bash脚本: 进阶方案 shelljs</h4>
<pre><code class="hljs language-bash copyable" lang="bash">const shell = require(<span class="hljs-string">'shelljs'</span>);
 
<span class="hljs-comment"># 删除文件命令</span>
shell.rm(<span class="hljs-string">'-rf'</span>, <span class="hljs-string">'out/Release'</span>);
// 拷贝文件命令
shell.cp(<span class="hljs-string">'-R'</span>, <span class="hljs-string">'stuff/'</span>, <span class="hljs-string">'out/Release'</span>);
 
<span class="hljs-comment"># 切换到lib目录，并且列出目录下到.js结尾到文件，并替换文件内容（sed -i 是替换文字命令）</span>
shell.cd(<span class="hljs-string">'lib'</span>);
shell.ls(<span class="hljs-string">'*.js'</span>).forEach(<span class="hljs-keyword">function</span> (file) &#123;
  shell.sed(<span class="hljs-string">'-i'</span>, <span class="hljs-string">'BUILD_VERSION'</span>, <span class="hljs-string">'v0.1.2'</span>, file);
  shell.sed(<span class="hljs-string">'-i'</span>, /^.*REMOVE_THIS_LINE.*$/, <span class="hljs-string">''</span>, file);
  shell.sed(<span class="hljs-string">'-i'</span>, /.*REPLACE_LINE_WITH_MACRO.*\n/, shell.cat(<span class="hljs-string">'macro.js'</span>), file);
&#125;);
shell.cd(<span class="hljs-string">'..'</span>);
 
<span class="hljs-comment"># 除非另有说明，否则同步执行给定的命令。 在同步模式下，这将返回一个 ShellString</span>
<span class="hljs-comment">#（与 ShellJS v0.6.x 兼容，它返回一个形式为 &#123; code:..., stdout:..., stderr:... &#125; 的对象）。</span>
<span class="hljs-comment"># 否则，这将返回子进程对象，并且回调接收参数（代码、标准输出、标准错误）。</span>
<span class="hljs-keyword">if</span> (shell.exec(<span class="hljs-string">'git commit -am "Auto-commit"'</span>).code !== 0) &#123;
  shell.echo(<span class="hljs-string">'Error: Git commit failed'</span>);
  shell.exit(1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码上看来，shelljs真的已经算是非常棒的nodejs写bash脚本的方案了，如果你们那边的node环境不能随便升级，我觉得shelljs确实够用了。</p>
<p>接着我们看看今天的主角zx，start已经17.4k了。</p>
<h3 data-id="heading-3">zx库</h3>
<p>官方网址：<a href="https://www.npmjs.com/package/zx" target="_blank" rel="nofollow noopener noreferrer">www.npmjs.com/package/zx</a></p>
<p>我们先看看怎么用</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/usr/bin/env zx</span>

await $`cat package.json | grep name`

<span class="hljs-built_in">let</span> branch = await $`git branch --show-current`
await $`dep deploy --branch=<span class="hljs-variable">$&#123;branch&#125;</span>`

await Promise.all([
  $`sleep 1; <span class="hljs-built_in">echo</span> 1`,
  $`sleep 2; <span class="hljs-built_in">echo</span> 2`,
  $`sleep 3; <span class="hljs-built_in">echo</span> 3`,
])

<span class="hljs-built_in">let</span> name = <span class="hljs-string">'foo bar'</span>
await $`mkdir /tmp/<span class="hljs-variable">$&#123;name&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>各位看官觉得咋样，是不是就是在写linux命令而已，bash语法可以忽略很多，直接上js就行，而且它的优点还不止这些，有一些特点挺有意思的：</p>
<p>1、支持ts，自动编译.ts为.mjs文件，.mjs文件是node高版本自带的支持es6 module的文件结尾，也就是这个文件直接import模块就行，不用其它工具转义</p>
<p>2、自带支持管道操作pipe方法</p>
<p>3、自带fetch库，可以进行网络请求，自带chalk库，可以打印有颜色的字体，自带错误处理nothrow方法，如果bash命令出错，可以包裹在这个方法里忽略错误</p>
<h4 data-id="heading-4">完整中文文档（在下翻译水平一般，请见谅）</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/usr/bin/env zx</span>

await $`cat package.json | grep name`

<span class="hljs-built_in">let</span> branch = await $`git branch --show-current`
await $`dep deploy --branch=<span class="hljs-variable">$&#123;branch&#125;</span>`

await Promise.all([
  $`sleep 1; <span class="hljs-built_in">echo</span> 1`,
  $`sleep 2; <span class="hljs-built_in">echo</span> 2`,
  $`sleep 3; <span class="hljs-built_in">echo</span> 3`,
])

<span class="hljs-built_in">let</span> name = <span class="hljs-string">'foo bar'</span>
await $`mkdir /tmp/<span class="hljs-variable">$&#123;name&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Bash 很棒，但是在编写脚本时，人们通常会选择更方便的编程语言。 JavaScript 是一个完美的选择，但标准的 Node.js 库在使用之前需要额外的做一些事情。 zx 基于 child_process ，转义参数并提供合理的默认值。</p>
<p>安装</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm i -g zx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要的环境</p>
<pre><code class="copyable">Node.js >= 14.8.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将脚本写入扩展名为 <code>.mjs</code> 的文件中，以便能够在顶层使用<code>await</code>。</p>
<p>将以下 <code>shebang</code>添加到 <code>zx</code> 脚本的开头：</p>
<pre><code class="copyable">#!/usr/bin/env zx
现在您将能够像这样运行您的脚本：

chmod +x ./script.mjs
./script.mjs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者通过 <code>zx</code>可执行文件：</p>
<pre><code class="copyable">zx ./script.mjs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有函数<code>（$、cd、fetch 等）</code>都可以直接使用，无需任何导入。</p>
<h4 data-id="heading-5">$`command`</h4>
<p>使用 <code>child_process</code> 包中的 spawn 函数执行给定的字符串, 并返回 ProcessPromise.</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">let</span> count = parseInt(await $`ls -1 | wc -l`)
console.log(`Files count: <span class="hljs-variable">$&#123;count&#125;</span>`)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如，要并行上传文件：</p>
<p>如果执行的程序返回非零退出代码，<code>ProcessOutput</code> 将被抛出</p>
<pre><code class="hljs language-bash copyable" lang="bash">try &#123;
  await $`<span class="hljs-built_in">exit</span> 1`
&#125; catch (p) &#123;
  console.log(`Exit code: <span class="hljs-variable">$&#123;p.exitCode&#125;</span>`)
  console.log(`Error: <span class="hljs-variable">$&#123;p.stderr&#125;</span>`)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ProcessPromise，以下是promise typescript的接口定义</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ProcessPromise</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Promise</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">readonly</span> stdin: Writable
  <span class="hljs-keyword">readonly</span> stdout: Readable
  <span class="hljs-keyword">readonly</span> stderr: Readable
  <span class="hljs-keyword">readonly</span> exitCode: <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">number</span>>
  pipe(dest): ProcessPromise<T>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>pipe()</code> 方法可用于重定向标准输出：</p>
<pre><code class="hljs language-bash copyable" lang="bash">await $`cat file.txt`.pipe(process.stdout)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>阅读更多的关于管道的信息 <a href="https://github.com/google/zx/blob/HEAD/examples/pipelines.md" target="_blank" rel="nofollow noopener noreferrer">github.com/google/zx/b…</a></p>
<p><code>ProcessOutput</code>的<code>typescript</code>接口定义</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ProcessOutput</span> </span>&#123;
  <span class="hljs-keyword">readonly</span> stdout: <span class="hljs-built_in">string</span>
  <span class="hljs-keyword">readonly</span> stderr: <span class="hljs-built_in">string</span>
  <span class="hljs-keyword">readonly</span> exitCode: <span class="hljs-built_in">number</span>
  toString(): <span class="hljs-built_in">string</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数：</p>
<h4 data-id="heading-6">cd()</h4>
<p>更改当前工作目录</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">cd</span>(<span class="hljs-string">'/tmp'</span>)
await $`<span class="hljs-built_in">pwd</span>` // outputs /tmp
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">fetch()</h4>
<p>node-fetch 包。</p>
<pre><code class="copyable">let resp = await fetch('http://wttr.in')
if (resp.ok) &#123;
  console.log(await resp.text())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">question()</h4>
<p>readline包</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">let</span> bear = await question(<span class="hljs-string">'What kind of bear is best? '</span>)
<span class="hljs-built_in">let</span> token = await question(<span class="hljs-string">'Choose env variable: '</span>, &#123;
  choices: Object.keys(process.env)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在第二个参数中，可以指定选项卡自动完成的选项数组</p>
<p>以下是接口定义</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">question</span>(<span class="hljs-params">query?: <span class="hljs-built_in">string</span>, options?: QuestionOptions</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">string</span>>
<span class="hljs-title">type</span> <span class="hljs-title">QuestionOptions</span> = </span>&#123; choices: <span class="hljs-built_in">string</span>[] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">sleep()</h4>
<p>基于setTimeout 函数</p>
<pre><code class="hljs language-bash copyable" lang="bash">await sleep(1000)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">nothrow()</h4>
<p>将 $ 的行为更改, 如果退出码不是0，不跑出异常.</p>
<p>ts接口定义</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nothrow</span><<span class="hljs-title">P</span>>(<span class="hljs-params">p: P</span>): <span class="hljs-title">P</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">await nothrow($`grep something from-file`)
// 在管道内:

await $`find ./examples -<span class="hljs-built_in">type</span> f -print0`
  .pipe(nothrow($`xargs -0 grep something`))
  .pipe($`wc -l`)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下的包，无需导入，直接使用</p>
<h4 data-id="heading-11">chalk</h4>
<pre><code class="hljs language-BASH copyable" lang="BASH">console.log(chalk.blue(<span class="hljs-string">'Hello world!'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">fs</h4>
<p>类似于如下的使用方式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;promises <span class="hljs-keyword">as</span> fs&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>
<span class="hljs-keyword">let</span> content = <span class="hljs-keyword">await</span> fs.readFile(<span class="hljs-string">'./package.json'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">os</h4>
<pre><code class="copyable">await $`cd $&#123;os.homedir()&#125; && mkdir example`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置：</p>
<h4 data-id="heading-14">$.shell</h4>
<p>指定要用的bash.</p>
<pre><code class="copyable">$.shell = '/usr/bin/bash'
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">$.quote</h4>
<p>指定用于在命令替换期间转义特殊字符的函数</p>
<p>默认用的是 shq 包.</p>
<p>注意：</p>
<p><code>__filename & __dirname</code>这两个变量是在<code>commonjs</code>中的。我们用的是<code>.mjs</code>结尾的<code>es6</code> 模块。</p>
<p>在<code>ESM</code>模块中，<code>Node.js</code> 不提供<code>__filename</code>和<code> __dirname</code> 全局变量。 由于此类全局变量在脚本中非常方便，因此<code> zx</code> 提供了这些以在 <code>.mjs</code> 文件中使用（当使用 <code>zx</code> 可执行文件时）</p>
<p><code>require</code>也是<code>commonjs</code>中的导入模块方法，
在 <code>ESM</code> 模块中，没有定义 <code>require()</code> 函数。<code>zx</code>提供了 <code>require()</code> 函数，因此它可以与 <code>.mjs</code> 文件中的导入一起使用（当使用 <code>zx </code>可执行文件时）</p>
<h4 data-id="heading-16">传递环境变量</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">process.env.FOO = <span class="hljs-string">'bar'</span>
<span class="hljs-keyword">await</span> $<span class="hljs-string">`echo $FOO`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">传递数组</h4>
<p>如果值数组作为参数传递给 $，数组的项目将被单独转义并通过空格连接
Example:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> files = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]
<span class="hljs-keyword">await</span> $<span class="hljs-string">`tar cz <span class="hljs-subst">$&#123;files&#125;</span>`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过显式导入来使用 $ 和其他函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">#!/usr/bin/env node</span>
<span class="hljs-keyword">import</span> &#123;$&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'zx'</span>
<span class="hljs-keyword">await</span> $<span class="hljs-string">`date`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>zx 可以将 .ts 脚本编译为 .mjs 并执行它们</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">zx examples/typescript.ts
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            