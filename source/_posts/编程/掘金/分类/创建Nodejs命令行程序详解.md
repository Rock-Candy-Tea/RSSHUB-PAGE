
---
title: '创建Nodejs命令行程序详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7851'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:38:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=7851'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>本文主要是探究Nodejs程序全局安装的原理以及如何用Nodejs开发命令行程序</p>
</blockquote>
<h2 data-id="heading-0">创建一个命令</h2>
<p>我们正常编写js文件，然后在js文件的顶部加上这行注释<code>#!/usr/bin/env node</code>，例如我们创建一个文件<code>hello.js</code>文件，内容如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/usr/bin/env node</span>

console.log(<span class="hljs-string">'你好'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后切换到<code>hello.js</code>文件所在的目录，执行<code>./hello.js</code>，会看到屏幕上打印了"你好"，表明我们成功的创建了一个命令脚本</p>
<p>但是该方法还有一个欠缺，就是每次运行的时候还需要输入完整的路径，不够自动化，我们希望达到的效果是输入<code>hello</code>命令，直接在屏幕上看到打印结果</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ hello 
>> 你好
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想要做到这个效果，我们需要在<code>package.json</code>文件中增加<code>bin</code>字段，注册一个命令（名称）和执行命令的脚本</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"bin"</span>: &#123;
        <span class="hljs-attr">"hello"</span>: <span class="hljs-string">"./bin/hello.js"</span>
    &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们将这个包通过<code>npm run publish</code>发布，然后我们安装这个包，如果是全局安装，则执行<code>hello</code>之后就会看到打印结果，如果是安装在某个项目里，则需要用<code>npx hello</code>命令查看效果</p>
<p>接下来我们探究下原理，以非全局安装为例，执行完<code>npm install</code>之后，会自动生成一个文件夹 <code>node_modules/.bin</code> ，并在里面自动生成三个文件<code>hello</code>、<code>hello.cmd</code>、<code>hello.ps1</code>，这三个文件的功能是一样的，都是执行对应的命令脚本，如<code>hello</code>文件的内容是：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/bin/sh</span>
basedir=$(dirname <span class="hljs-string">"<span class="hljs-subst">$(echo <span class="hljs-string">"<span class="hljs-variable">$0</span>"</span> | sed -e 's,\\,/,g')</span>"</span>)

<span class="hljs-keyword">case</span> `uname` <span class="hljs-keyword">in</span>
    *CYGWIN*|*MINGW*|*MSYS*) basedir=`cygpath -w <span class="hljs-string">"<span class="hljs-variable">$basedir</span>"</span>`;;
<span class="hljs-keyword">esac</span>

<span class="hljs-keyword">if</span> [ -x <span class="hljs-string">"<span class="hljs-variable">$basedir</span>/node"</span> ]; <span class="hljs-keyword">then</span>
  <span class="hljs-string">"<span class="hljs-variable">$basedir</span>/node"</span>  <span class="hljs-string">"<span class="hljs-variable">$basedir</span>/../hello/bin/hello.js"</span> <span class="hljs-string">"<span class="hljs-variable">$@</span>"</span>
  ret=$?
<span class="hljs-keyword">else</span> 
  node  <span class="hljs-string">"<span class="hljs-variable">$basedir</span>/../hello/bin/hello.js"</span> <span class="hljs-string">"<span class="hljs-variable">$@</span>"</span>
  ret=$?
<span class="hljs-keyword">fi</span>
<span class="hljs-built_in">exit</span> <span class="hljs-variable">$ret</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上可知，如果我们想要创建一个命令，只需要两步：</p>
<ol>
<li>在命令的执行脚本顶部加上<code>#!/usr/bin/env node</code>标记</li>
<li>在<code>package.json</code>文件里加上 <code>bin</code> 字段，注册命令名称以及对应的命令脚本路径</li>
</ol>
<h2 data-id="heading-1">关于参数的获取</h2>
<p>命令行程序除了命令的注册外，命令参数的获取也是一个重要的环节，基本上关于命令行参数有这么几个基本的需求：</p>
<ul>
<li>定义参数的数据类型</li>
<li>定义参数的默认值</li>
<li>获取用户配置的参数</li>
<li>参数的使用方法（实现--help）</li>
<li>参数别名（-n --name）</li>
<li>实现显示当前版本号功能</li>
</ul>
<p>手动实现上述功能，主要是依赖对<code>process.argv</code>的处理，上述的工作 <a href="https://www.npmjs.com/package/commander" target="_blank" rel="nofollow noopener noreferrer">Commander.js</a> 已经帮我们做了实现，我们接下来介绍一下其用法</p>
<h3 data-id="heading-2">安装</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm install commander
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">配置version</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; program &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'commander'</span>);
program.version(<span class="hljs-string">'0.0.1'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; Command &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'commander'</span>);
<span class="hljs-keyword">const</span> program = <span class="hljs-keyword">new</span> Command();
program.version(<span class="hljs-string">'0.0.1'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">定义参数、获取参数</h3>
<p>涉及到数据类型，必填项，默认值，别名，变长参数</p>
<ul>
<li>
<p><strong>数据类型</strong>：有两种最常用的选项，一类是 boolean 型选项，选项无需配置参数，另一类选项则可以设置参数（使用尖括号声明在该选项后，如--expect ）。如果在命令行中不指定具体的选项及参数，则会被定义为undefined</p>
</li>
<li>
<p><strong>必填</strong>：通过.requiredOption方法可以设置选项为必填。必填选项要么设有默认值，要么必须在命令行中输入，对应的属性字段在解析时必定会有赋值。该方法其余参数与.option一致</p>
</li>
<li>
<p><strong>别名</strong>：每个选项可以定义一个简写名称（-后面接单个字符）和一个长选项名称（--后面接一个或多个单词），使用逗号、空格或|分隔，如 <code>option('-d, --debug', 'output extra debugging')</code></p>
</li>
<li>
<p><strong>变长参数</strong>：定义选项时，可以通过使用...来设置参数为可变长参数。在命令行中，用户可以输入多个参数，解析后会以数组形式存储在对应属性字段中，如<code>option('-l, --letter [letters...]', 'specify letters')</code></p>
</li>
</ul>
<p>完整示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">#!/usr/bin/env node</span>

<span class="hljs-keyword">const</span> commander = <span class="hljs-built_in">require</span>(<span class="hljs-string">'commander'</span>);
<span class="hljs-keyword">const</span> program = <span class="hljs-keyword">new</span> commander.Command();

program.version(<span class="hljs-string">'0.0.1'</span>);

program
    .option(<span class="hljs-string">'-d, --debug'</span>, <span class="hljs-string">'output extra debugging'</span>) <span class="hljs-comment">// --debug 別名 -d</span>
    .requiredOption(<span class="hljs-string">'-h, --hot'</span>, <span class="hljs-string">'hot must chose'</span>) <span class="hljs-comment">// 必填项</span>
    .option(<span class="hljs-string">'-ad, --adress [adress...]'</span>, <span class="hljs-string">'adress can mutl'</span>) <span class="hljs-comment">// 必填项</span>
    .option(<span class="hljs-string">'-s, --small'</span>, <span class="hljs-string">'small pizza size'</span>, <span class="hljs-literal">true</span>)
    .option(<span class="hljs-string">'-p, --pizza-type <type>'</span>, <span class="hljs-string">'flavour of pizza'</span>, <span class="hljs-string">'okok'</span>);

program.parse(process.argv);

<span class="hljs-keyword">const</span> options = program.opts();

<span class="hljs-built_in">console</span>.log(options);


<span class="hljs-comment">//</span>
<span class="hljs-comment">// $ ./cli-run.js -h -ad 123 32131 1321</span>
<span class="hljs-comment">// &#123;</span>
<span class="hljs-comment">//     small: true,</span>
<span class="hljs-comment">//     pizzaType: 'okok',</span>
<span class="hljs-comment">//     hot: true,</span>
<span class="hljs-comment">//     adress: ['123', '32131', '1321']</span>
<span class="hljs-comment">// &#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">业界常见实现方式</h2>
<p>通过上文可知，命令行的实际内容是个<code>js</code>文件，只不过在<code>package.json</code>里用<code>bin</code>字段做了指定，以便可以在命令行中调取这个命令。在很多致命的第三方库，如<code>webpack</code>、<code>ESLint</code>，它们除了会提供<code>API</code>调用方式外，还会提供命令行方式，基本上是在项目根目录添加一个<code>bin</code>文件夹，实现连接命令与<code>API</code>的脚本，向<code>API</code>传递从命令行获取到的参数。所以基本上就是命令在<code>API</code>的基础上做了一层获取参数的封装而已。</p>
<h2 data-id="heading-6">附录</h2>
<h3 data-id="heading-7">参考文章</h3>
<ul>
<li><a href="https://juejin.cn/post/6844904095065587725" target="_blank">手把手教你写Node.js命令行程序</a></li>
<li><a href="https://juejin.cn/post/6844904095065587725" target="_blank">Building a simple command line tool with npm</a> ：npm官方文章</li>
<li><a href="http://www.ruanyifeng.com/blog/2015/05/command-line-with-node.html" target="_blank" rel="nofollow noopener noreferrer">Node.js 命令行程序开发教程</a></li>
</ul>
<h3 data-id="heading-8">必备开发包</h3>
<ul>
<li><a href="https://github.com/tj/commander.js" target="_blank" rel="nofollow noopener noreferrer">Commander.js</a> ：完整的Nodejs命令行程序解决方案，<a href="https://github.com/tj/commander.js/blob/master/Readme_zh-CN.md" target="_blank" rel="nofollow noopener noreferrer">中文文档</a></li>
<li><a href="https://www.npmjs.com/package/yargs" target="_blank" rel="nofollow noopener noreferrer">yargs</a>：处理命令行参数</li>
</ul></div>  
</div>
            