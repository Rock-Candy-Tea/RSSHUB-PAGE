
---
title: 'Google zx 源码浅析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0697e0287d314cb5a430b267a515a0e1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 02:19:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0697e0287d314cb5a430b267a515a0e1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">“Bash很好，所以我选择JavaScript”</h3>
<p>前端日常开发中我们大部分时间都是使用Javascript，在编写shell脚本时，写bash没有像js那般熟悉，如果能选择一种更方便的编程语言来写它，何乐而不为呢？
Google zx 工具实现了这种可能，官方用给base发“好人卡”的方式，成功介绍了它，作为一个更方便、更友好帮助开发者写脚本的工具 ，短短时间就在GitHub上火爆起来了，那我们一起来瞧一瞧它的庐山真面目。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0697e0287d314cb5a430b267a515a0e1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">它怎么使用呢？</h3>
<p>安装初始化（ <code>npm i -g zx</code> ），node版本限制（ <code>>= 14.8.0</code> ）
先看一个简单的例子，创建一个 demo.mjs 文件，内容如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// demo.mjs</span>
<span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all([
  $<span class="hljs-string">`sleep 1; echo 3`</span>,
  $<span class="hljs-string">`sleep 2; echo 2`</span>,
  $<span class="hljs-string">`sleep 3; echo 1`</span>,
])
<span class="hljs-keyword">let</span> tName = <span class="hljs-string">'google/zx'</span>
<span class="hljs-keyword">await</span> $<span class="hljs-string">`echo '/hello/<span class="hljs-subst">$&#123;tName&#125;</span>'`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命令行执行 <code>zx demo.mjs</code>
伴随着3秒倒计时，可以看到 /hello/google/zx</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1d952cfb98546eb8ea3eb19d241491b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是一个简单的使用例子，接下去我们进入正题</p>
<h3 data-id="heading-2">来看看提供了哪些能力？</h3>
<h4 data-id="heading-3">三种使用方式</h4>
<h5 data-id="heading-4">zx << 'EOF'</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> firstArg === <span class="hljs-string">'undefined'</span> || firstArg === <span class="hljs-string">'-'</span>) &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断输入命令没有firstArg则会通过 <code>scriptFromStdin</code> 函数处理逻辑：</p>
<ul>
<li>
<p>通过 <code>process.stdin.isTTY</code> 判断是否在终端条件下</p>
</li>
<li>
<p>如果不是的话设置utf8字符编码</p>
</li>
<li>
<p>根据输入的逐行内容循环并拼接</p>
</li>
<li>
<p>在临时文件夹创建一个随机命名的mjs文件</p>
</li>
</ul>
<p><code>Math.random().toString(36).substr(2) + '.mjs'</code>
举个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">zx <<<span class="hljs-string">'EOF'</span>
<span class="hljs-keyword">await</span> $<span class="hljs-string">`pwd`</span>
EOF
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">从远端拉取脚本执行</h5>
<pre><code class="hljs language-markdown copyable" lang="markdown">if (firstArg.startsWith('http://') || firstArg.startsWith('https://')) &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拉取数据主要是通过 <code>scriptFromHttp</code> 实现，主要有以下几步：</p>
<ul>
<li>
<p>使用node-fetch包拉取对应url的数据</p>
</li>
<li>
<p>拉取完数据后会通过url的pathname来命名</p>
</li>
<li>
<p>在临时文件夹中创建文件</p>
</li>
</ul>
<h5 data-id="heading-6">本地脚本文件执行</h5>
<p>如果没有进入到上面两个判断，则会执行下方逻辑，以 / 开头则直接使用该链接，file开头则调用url.fileURLToPath获取绝对路径字符串，其他逻辑的通过path.resolve获取路径</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (firstArg.startsWith(<span class="hljs-string">'/'</span>)) &#123;
  filepath = firstArg
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (firstArg.startsWith(<span class="hljs-string">'file:///'</span>)) &#123;
  filepath = url.fileURLToPath(firstArg)
&#125; <span class="hljs-keyword">else</span> &#123;
  filepath = resolve(firstArg)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">支持多种文件格式 importPath</h4>
<h5 data-id="heading-8">空后缀</h5>
<p>zx 遇到这样的情况会直接readFile读取文件信息，然后获取当前文件所在目录以及文件名，重新写一个mjs文件，再次进入 <code>importPath</code> 方法并import执行</p>
<h5 data-id="heading-9">Markdown文件</h5>
<p>zx 对于markdow编写的脚本同样可以执行，只有code包裹的部分会被解析，通过 <code>transformMarkdown</code> 方法用 \n 切割为数组后逐行扫描并用正则做匹配，匹配命中的信息会push到另一个数组，最后将数据通过换行符\n进行拼接转化成字符串作为script数据，生成文件的方式同上
Markdown格式举例：</p>
<pre><code class="hljs language-markdown copyable" lang="markdown"><span class="hljs-section"># Markdown Scripts</span>

It's possible to write scripts using markdown. Only code blocks will be executed
by zx. 

<span class="hljs-quote">> You can run this markdown file:</span>
<span class="hljs-quote">>
> ```</span>
<span class="hljs-quote">> zx docs/markdown.md</span>
<span class="hljs-quote">> ```</span>

<span class="hljs-code">```js
await $`whoami`
await $`echo $&#123;__dirname&#125;`
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>The <code>__filename</code> will be pointed to <strong>markdown.md</strong>:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(chalk.yellowBright(__filename))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>We can use imports here as well:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'chalk'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>A bash code (with <code>bash</code> or <code>sh</code> language tags) also will be executed:</p>
<pre><code class="hljs language-bash copyable" lang="bash">VAR=$(date)
<span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$VAR</span>"</span> | wc -c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Other code blocks are ignored:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.hero</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">42px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">##### Ts文件

核心部分是执行 `compile` 方法进行tsc编译出一个js，然后对js进行重命名为mjs
```javascript
let tsc = $`npm_config_yes=true npx -p typescript tsc --target esnext --lib esnext --module esnext --moduleResolution node $&#123;input&#125;`
await tsc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个loading，用的是setInterval实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> interval = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
process.stdout.write(<span class="hljs-string">'  '</span>
  + [<span class="hljs-string">'⠋'</span>, <span class="hljs-string">'⠙'</span>, <span class="hljs-string">'⠹'</span>, <span class="hljs-string">'⠸'</span>, <span class="hljs-string">'⠼'</span>, <span class="hljs-string">'⠴'</span>, <span class="hljs-string">'⠦'</span>, <span class="hljs-string">'⠧'</span>, <span class="hljs-string">'⠇'</span>, <span class="hljs-string">'⠏'</span>][i++ % <span class="hljs-number">10</span>]
  + <span class="hljs-string">'\r'</span>
)
&#125;, <span class="hljs-number">100</span>)

...

<span class="hljs-built_in">clearInterval</span>(interval)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">$函数</h4>
<p>首先是使用了标签函数的能力处理args</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6d7b7b2a7cf438782257db78c4877f6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果传入了数组，会对这个数组进行拼接，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> flags = [
  <span class="hljs-string">'--oneline'</span>,
  <span class="hljs-string">'--decorate'</span>,
  <span class="hljs-string">'--color'</span>,
]
<span class="hljs-keyword">await</span> $<span class="hljs-string">`git log <span class="hljs-subst">$&#123;flags&#125;</span>`</span>

<span class="hljs-comment">// zx 处理逻辑，先格式化，再用一个空格拼接</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(args[i])) &#123;
  s = args[i].map(<span class="hljs-function"><span class="hljs-params">x</span> =></span> $.quote(substitute(x))).join(<span class="hljs-string">' '</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>cmd与将转译后的args拼接，然后创建一个ProcessPromise类的实例
调用then的时候会触发_fun方法</p>
<pre><code class="hljs language-http copyable" lang="http"> then(onfulfilled, onrejected) &#123;
    if (this._run) this._run()
    return super.then(onfulfilled, onrejected)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>_run方法里核心是使用child_process.spawn</p>
<blockquote>
<p>简单介绍一下child_process的其它能够执行bash命令的api
spawn：启动一个子进程来执行命令
exec：启动一个子进程来执行命令，与spawn不同的是，它有一个回调函数能知道子进程的情况
execFile：启动一子进程来执行可执行文件
fork：与spawn类似，不同点是它需要指定子进程需要需执行的模块</p>
</blockquote>
<p>child_process监听exit和close事件，然后输出一个output，code为0即成功，失败则会通过code码在 <code>exitCodeInfo</code> 方法中返回对应的错误信息</p>
<pre><code class="hljs language-ada copyable" lang="ada">
<span class="hljs-keyword">function</span> <span class="hljs-title">exitCodeInfo</span>(exitCode) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-type">&#123;</span>
    <span class="hljs-number">2</span>: <span class="hljs-symbol">'Misuse</span> <span class="hljs-keyword">of</span> shell builtins',
    <span class="hljs-number">126</span>: <span class="hljs-symbol">'Invoked</span> command cannot execute',
    <span class="hljs-number">127</span>: <span class="hljs-symbol">'Command</span> <span class="hljs-keyword">not</span> found',
    <span class="hljs-number">128</span>: <span class="hljs-symbol">'Invalid</span> <span class="hljs-keyword">exit</span> argument',
    <span class="hljs-number">129</span>: <span class="hljs-symbol">'Hangup</span>',
    <span class="hljs-number">130</span>: <span class="hljs-symbol">'Interrupt</span>',
    <span class="hljs-number">131</span>: <span class="hljs-symbol">'Quit</span> <span class="hljs-keyword">and</span> dump core',
    <span class="hljs-number">132</span>: <span class="hljs-symbol">'Illegal</span> instruction',
    <span class="hljs-number">133</span>: <span class="hljs-symbol">'Trace</span>/breakpoint trap',
    <span class="hljs-number">134</span>: <span class="hljs-symbol">'Process</span> aborted',
    <span class="hljs-number">135</span>: <span class="hljs-symbol">'Bus</span> error: <span class="hljs-string">"access to undefined portion of memory object"</span>',
    <span class="hljs-number">136</span>: <span class="hljs-symbol">'Floating</span> point <span class="hljs-keyword">exception</span>: <span class="hljs-string">"erroneous arithmetic operation"</span>',
    <span class="hljs-number">137</span>: <span class="hljs-symbol">'Kill</span> (<span class="hljs-keyword">terminate</span> immediately)',
    <span class="hljs-number">138</span>: <span class="hljs-symbol">'User</span>-defined <span class="hljs-number">1</span>',
    <span class="hljs-number">139</span>: <span class="hljs-symbol">'Segmentation</span> violation',
    <span class="hljs-number">140</span>: <span class="hljs-symbol">'User</span>-defined <span class="hljs-number">2</span>',
    <span class="hljs-number">141</span>: <span class="hljs-symbol">'Write</span> to pipe <span class="hljs-keyword">with</span> no one reading',
    <span class="hljs-number">142</span>: <span class="hljs-symbol">'Signal</span> raised by alarm',
    <span class="hljs-number">143</span>: <span class="hljs-symbol">'Termination</span> (request to <span class="hljs-keyword">terminate</span>)',
    <span class="hljs-number">145</span>: <span class="hljs-symbol">'Child</span> process terminated, stopped (<span class="hljs-keyword">or</span> continued*)',
    <span class="hljs-number">146</span>: <span class="hljs-symbol">'Continue</span> <span class="hljs-keyword">if</span> stopped',
    <span class="hljs-number">147</span>: <span class="hljs-symbol">'Stop</span> executing temporarily',
    <span class="hljs-number">148</span>: <span class="hljs-symbol">'Terminal</span> stop signal',
    <span class="hljs-number">149</span>: <span class="hljs-symbol">'Background</span> process attempting to read from tty (<span class="hljs-string">"in"</span>)',
    <span class="hljs-number">150</span>: <span class="hljs-symbol">'Background</span> process attempting to write to tty (<span class="hljs-string">"out"</span>)',
    <span class="hljs-number">151</span>: <span class="hljs-symbol">'Urgent</span> data available on socket',
    <span class="hljs-number">152</span>: <span class="hljs-symbol">'CPU</span> time limit exceeded',
    <span class="hljs-number">153</span>: <span class="hljs-symbol">'File</span> size limit exceeded',
    <span class="hljs-number">154</span>: <span class="hljs-symbol">'Signal</span> raised by timer counting virtual time: <span class="hljs-string">"virtual timer expired"</span>',
    <span class="hljs-number">155</span>: <span class="hljs-symbol">'Profiling</span> timer expired',
    <span class="hljs-number">157</span>: <span class="hljs-symbol">'Pollable</span> event',
    <span class="hljs-number">159</span>: <span class="hljs-symbol">'Bad</span> syscall',
  &#125;[exitCode]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">其他Funtions</h4>
<h5 data-id="heading-12"><strong>cd()</strong></h5>
<p>更改当前工作目录，同时会设置$.cwd</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (!fs.existsSync(path)) &#123;
    <span class="hljs-keyword">let</span> __from = (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>().stack.split(<span class="hljs-regexp">/^\s*at\s/m</span>)[<span class="hljs-number">2</span>]).trim()
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`cd: <span class="hljs-subst">$&#123;path&#125;</span>: No such directory`</span>)
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`    at <span class="hljs-subst">$&#123;__from&#125;</span>`</span>)
    process.exit(<span class="hljs-number">1</span>)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13"><strong>fetch()</strong></h5>
<p>实际上是使用node-fetch拉取数据</p>
<pre><code class="hljs language-c# copyable" lang="c#">nodeFetch(url: RequestInfo, <span class="hljs-keyword">init</span>?: RequestInit): Promise<Response>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14"><strong>question()</strong></h5>
<p>readline的语法糖
通过设置options.choices传入一个数组可以支持select模式</p>
<h5 data-id="heading-15"><strong>sleep()</strong></h5>
<p>使用 <code>util.promisify</code> 对setTimeout包了一层，返回一个promise，例如await sleep(1000) 这样的回调风格更优美一些</p>
<h5 data-id="heading-16"><strong>nothrow()</strong></h5>
<p>设置_nothrow的值为true，child process监听close事件，返回的code !== 0 也能 resolve</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/178b14e3149b431a975d80256706f0cb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用举例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">await</span> nothrow($<span class="hljs-string">`grep something from-file`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">可以直接使用的Packages</h4>
<h5 data-id="heading-18"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fchalk" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/chalk" ref="nofollow noopener noreferrer">chalk</a> package</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(chalk.blue(<span class="hljs-string">'Hello world!'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">fs package ( <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Ffs-extra" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/fs-extra" ref="nofollow noopener noreferrer">fs-extra</a> )</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> content = <span class="hljs-keyword">await</span> fs.readFile(<span class="hljs-string">'./package.json'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fglobby" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/globby" ref="nofollow noopener noreferrer">globby</a> package</h5>
<p>这个包提供了一些方法，用于遍历文件系统，并根据UnixBashshell使用的规则返回与已定义的指定模式集匹配的路径名，同时以任意顺序返回结果，使用起来快速、简单、有效。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> packages = <span class="hljs-keyword">await</span> globby([<span class="hljs-string">'package.json'</span>, <span class="hljs-string">'packages/*/package.json'</span>])
<span class="hljs-keyword">let</span> pictures = globby.globbySync(<span class="hljs-string">'content/*.(jpg|png)'</span>)
<span class="hljs-comment">// Also, globby available via the glob shortcut:</span>
<span class="hljs-keyword">await</span> $<span class="hljs-string">`svgo <span class="hljs-subst">$&#123;<span class="hljs-keyword">await</span> glob(<span class="hljs-string">'*.svg'</span>)&#125;</span>`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fapi%2Fos.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/api/os.html" ref="nofollow noopener noreferrer">os</a> package</h5>
<p>提供了与操作系统相关的方法和属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">await</span> $<span class="hljs-string">`cd <span class="hljs-subst">$&#123;os.homedir()&#125;</span> && mkdir example`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fminimist" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/minimist" ref="nofollow noopener noreferrer">minimist</a> package</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用举例</span>
$ node example/parse.js -x <span class="hljs-number">3</span> -y <span class="hljs-number">4</span> -n5 -abc --beep=boop foo bar baz
&#123; <span class="hljs-attr">_</span>: [ <span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-string">'baz'</span> ],
  <span class="hljs-attr">x</span>: <span class="hljs-number">3</span>,
  <span class="hljs-attr">y</span>: <span class="hljs-number">4</span>,
  <span class="hljs-attr">n</span>: <span class="hljs-number">5</span>,
  <span class="hljs-attr">a</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">c</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">beep</span>: <span class="hljs-string">'boop'</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">参数配置</h4>
<h5 data-id="heading-24">$.quote</h5>
<p>这里主要是实现了一个quote方法，主要用于特殊字符转译</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">quote</span>(<span class="hljs-params">arg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^[a-z0-9/_.-]+$/i</span>.test(arg) || arg === <span class="hljs-string">''</span>) &#123;
    <span class="hljs-keyword">return</span> arg
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`$'`</span>
    + arg
      .replace(<span class="hljs-regexp">/\\/g</span>, <span class="hljs-string">'\\\\'</span>)
      .replace(<span class="hljs-regexp">/'/g</span>, <span class="hljs-string">'\\\''</span>)
      .replace(<span class="hljs-regexp">/\f/g</span>, <span class="hljs-string">'\\f'</span>)
      .replace(<span class="hljs-regexp">/\n/g</span>, <span class="hljs-string">'\\n'</span>)
      .replace(<span class="hljs-regexp">/\r/g</span>, <span class="hljs-string">'\\r'</span>)
      .replace(<span class="hljs-regexp">/\t/g</span>, <span class="hljs-string">'\\t'</span>)
      .replace(<span class="hljs-regexp">/\v/g</span>, <span class="hljs-string">'\\v'</span>)
      .replace(<span class="hljs-regexp">/\0/g</span>, <span class="hljs-string">'\\0'</span>)
    + <span class="hljs-string">`'`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-25">$.verbose（--quiet）</h5>
<p>设置静默模式，默认为true会打印出log，通过参数 --quiet可以设置$.verbose = false
目前会打印的位置有：</p>
<ul>
<li>
<p>cd命令，提示当前路径</p>
</li>
<li>
<p>远程拉取脚本，提示当前fetch的url</p>
</li>
</ul>
<h5 data-id="heading-26">$.cwd</h5>
<p>默认为undefined，$.cwd可以通过cd方法来设置，拿到当前的工作目录</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9f805482f7148ec87be3d9771aa8942~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-27">$.shell（--shell）</h5>
<p>指定使用的shell
例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">$.shell = <span class="hljs-string">'/usr/bin/bash'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-28">$.prefix</h5>
<p>设置所有运行命令的前缀的命令
默认设置为-euo pipefail
或者使用 --prefix 来设置，例如：--prefix='set -e;'</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/716e9524722e47f494851f9983900cb7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-29">Polyfills</h4>
<p>Nodejs 在 ESM 中不提供 __dirname 和 __filename，以及没有定义require()函数，所以zx在global挂了这几个变量，方便使用者自取</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">let</span> __filename = resolve(origin)
  <span class="hljs-keyword">let</span> __dirname = dirname(__filename)
  <span class="hljs-keyword">let</span> <span class="hljs-built_in">require</span> = createRequire(origin)
  <span class="hljs-built_in">Object</span>.assign(<span class="hljs-built_in">global</span>, &#123;__filename, __dirname, <span class="hljs-built_in">require</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次的介绍就到这里了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c54a61634e646eeaf6899f33c702084~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            