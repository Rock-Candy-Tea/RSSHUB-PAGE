
---
title: '浅入vue脚手架 手把手教你撸一个简单脚手架'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8597bd65df374ae28c90a6412a75de2b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 18:39:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8597bd65df374ae28c90a6412a75de2b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>nodejs是个非常好用的工具，同时对我们前端同学来说学习成本低，非常友善，可以使用js来开发服务端，同时兼顾前端，实现了语言统一化，这里我不展开说了，主要展开说一下脚手架是怎么实现的。前端的同学想必都使用过vue脚手架（vue-cli），一条简单的命令vue init 就可以将一个简单的单页面应用包括webpack的简单配置全部搭建好并且你只用关注开发层面的东西（如果没有什么特殊的要求的话），他的实现原理其实也不难。先上vue脚手架的原理图：</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8597bd65df374ae28c90a6412a75de2b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
整个vue init大致流程如我上图所示，应该还是比较好理解的。这里我大致阐述一下大致的流程。</p>
<ol>
<li>vue-cli会先判断你的模板在远程github仓库上还是在你的本地某个文件里面，若是本地文件夹则会立即跳到第3步，反之则走第2步。</li>
<li>第2步会判断是否为官方模板，官方模板则会从官方github仓库中下载模板到本地的默认仓库下，即根目录下.vue-templates文件夹下。</li>
<li>第3步则读取模板目录下meta.js或者meta.json文件，根据里面的内容会询问开发者，根据开发者的回答，确定一些修改。</li>
<li>根据模板内容以及开发者的回答，渲染出项目结构并生成到指定目录。</li>
</ol>
<blockquote>
<p>引用：<a href="https://blog.csdn.net/sinat_17775997/article/details/84099731" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/sinat_17775…</a></p>
</blockquote>
<blockquote>
<p>脚手架的优势：
减少重复性的工作，不再需要复制其他项目再删除无关代码，或者从零创建一个项目和文件。你可以将常用的组件、工具类、样式等全部抽离出来放在git或者其他的模板库里，再用脚手架进行拉取，这样开发类似风格的新业务时候就不需要复制其他的代码。</p>
</blockquote>
<h2 data-id="heading-0">开始搭建我们的node脚手架</h2>
<p>首先新建文件夹，cd进该文件夹并且npm init 初始化一个node项目包括项目名称、版本、作者、依赖等相关信息。他会在当前目录下生成一个package.json文件。</p>
<blockquote>
<p>bin文件的作用： 很多包都有一个或多个可执行的文件，希望放在PATH中，（实际上，就是这个功能让npm可执行的）。
当你要用这个功能时，需要给package.json中的bin字段添加一个命令名，并指向需要执行的文件（即后文的入口文件）。初始化的时候npm会将他链接到prefix/bin（全局初始化）或者./node_modules/.bin/（本地初始化）。
引用：<a href="https://blog.csdn.net/weixin_34357436/article/details/88811435" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/weixin_3435…</a>
比如：我们在bin目录下新建一个index.js文件（当前目录也可以，随便你）</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-string">"bin"</span>: &#123;
    <span class="hljs-string">"cli"</span>: <span class="hljs-string">"./bin/index.js"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>实际上就是相当于一个入口文件，这个入口文件就是他的可执行文件，你可以将其他js引入该文件中然后通过入口文件暴露出去，上面代码指定，cli命令对应的可执行文件为 bin 子目录下的 index.js。npm会寻找这个文件，在node_modules/.bin/目录下建立符号链接。在上面的例子中，index.js会建立符号链接node_modules/.bin/index。由于node_modules/.bin/目录会在运行时加入系统的PATH变量，因此在运行npm时，就可以不带路径，直接通过命令来调用这些脚本。
更多package.json配置：<a href="https://javascript.ruanyifeng.com/nodejs/packagejson.html#toc4" target="_blank" rel="nofollow noopener noreferrer">javascript.ruanyifeng.com/nodejs/pack…</a></p>
</blockquote>
<p>到现在代码是这样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"ljh"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">"nodejs"</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-string">"bin"</span>: &#123;
    <span class="hljs-string">"ljh-cli"</span>:<span class="hljs-string">"./index.js"</span>
  &#125;,
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>然后我们在安装一些npm包给我们提供一些方便好用的api。</p>
<p>commander.js：可以自动的解析命令和参数，用于处理用户输入的命令。</p>
<p>download-git-repo：下载并提取 git 仓库，用于下载项目模板。</p>
<p>Inquirer.js：通用的命令行用户界面集合，用于和用户进行交互。</p>
<p>handlebars.js：模板引擎，将用户提交的信息动态填充到文件中。</p>
<p>ora：下载过程久的话，可以用于显示下载中的动画效果。</p>
<p>chalk：可以给终端的字体加上颜色。</p>
<p>log-symbols：可以在终端上显示出 √ 或 × 等的图标。</p>
<p>fs：node内置的文件处理模块。</p>
<p>path：node内置的路径处理、解析模块。</p>
<p>child_process：node中创建子进程模块。</p>
<p>除此之外，还使用了nodejs的几个内置模块：fs、path、child_process</p>
</blockquote>
<p>直接一条命令解决：</p>
<pre><code class="hljs language-js copyable" lang="js">npm install commander download-git-repo inquirer handlebars ora chalk log-symbols shelljs -S
或
在package.json 锁死版本 直接 npm i

<span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"chalk"</span>: <span class="hljs-string">"^4.1.0"</span>,
    <span class="hljs-string">"commander"</span>: <span class="hljs-string">"^6.0.0"</span>,
    <span class="hljs-string">"download-git-repo"</span>: <span class="hljs-string">"^3.0.2"</span>,
    <span class="hljs-string">"handlebars"</span>: <span class="hljs-string">"^4.7.6"</span>,
    <span class="hljs-string">"inquirer"</span>: <span class="hljs-string">"^7.3.3"</span>,
    <span class="hljs-string">"log-symbols"</span>: <span class="hljs-string">"^4.0.0"</span>,
    <span class="hljs-string">"ora"</span>: <span class="hljs-string">"^4.0.5"</span>,
    <span class="hljs-string">"shelljs"</span>: <span class="hljs-string">"^0.8.4"</span>
&#125;<span class="hljs-string">`


</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>之后再index.js中我们要在第一行（必须在第一行）加入：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  #!<span class="hljs-regexp">/usr/</span>bin/env node
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>!/usr/bin/node是告诉操作系统执行这个脚本的时候，调用/usr/bin下的node解释器；
!/usr/bin/env node这种用法是为了防止操作系统用户没有将node装在默认的/usr/bin路径里。当系统看到这一行的时候，首先会到env设置里查找node的安装路径，再调用对应路径下的解释器程序完成操作。
!/usr/bin/node相当于写死了node路径;</p>
</blockquote>
<p>接下来开始编写我们的Index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> program = <span class="hljs-built_in">require</span>(<span class="hljs-string">'commander'</span>);
program.version(<span class="hljs-string">'1.0.0'</span>, <span class="hljs-string">'-v, --version'</span>)
  .command(<span class="hljs-string">'init <name>'</span>)
  .action(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(name);
  &#125;);
  program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用program.version('1.0.0', '-v, --version')会将-v和--version添加到命令行中，调用时可通过带上该参数获取该脚手架的版本号（命令 -v/--version），调用comand('init ')定义初始化命令，name参数必传，作为项目的文件夹名，如 cli init Name
action是执行command命令时发生的回调，参数为命令行中输入的name，即init 中的name，项目生成过程便发生在回调函数中。
现在可以通过调用node index.js init test，可以看到控制台中已经打印了输入的项目名，也就是test。
其中：program.parse(process.argv)解析命令行中的参数，解析出name,并传入action回调。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> inquirer.prompt([
   &#123;
     <span class="hljs-attr">name</span>: <span class="hljs-string">'description'</span>,
     <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入项目描述'</span>
   &#125;,
   &#123;
     <span class="hljs-attr">name</span>: <span class="hljs-string">'author'</span>,
     <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入作者名称'</span>
   &#125;
 ]).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
     <span class="hljs-built_in">console</span>.log(res)
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过inquirer模块的 prompt() 中，可以实现与用户的交互，并且有回调可以进行后续的处理。问题的类型为 input 就是输入类型（不填默认input），name 就是作为答案对象中的 key，message 就是问题了，用户输入的答案就在后面的回调返回的参数中。</p>
<blockquote>
<p>后续还有一些美化处理和动画效果就不一一讲解，上完整代码：</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">#!/usr/bin/env node</span>
<span class="hljs-keyword">const</span> program = <span class="hljs-built_in">require</span>(<span class="hljs-string">'commander'</span>);<span class="hljs-comment">// commander.js，可以自动的解析命令和参数，用于处理用户输入的命令。</span>
<span class="hljs-keyword">const</span> inquirer = <span class="hljs-built_in">require</span>(<span class="hljs-string">'inquirer'</span>);<span class="hljs-comment">// Inquirer.js，通用的命令行用户界面集合，用于和用户进行交互。</span>
<span class="hljs-keyword">const</span> symbols = <span class="hljs-built_in">require</span>(<span class="hljs-string">'log-symbols'</span>);<span class="hljs-comment">// log-symbols，可以在终端上显示出 √ 或 × 等的图标。</span>
<span class="hljs-comment">// const download = require('download-git-repo');// download-git-repo，下载并提取 git 仓库，用于下载项目模板。</span>
<span class="hljs-keyword">const</span> handlebars = <span class="hljs-built_in">require</span>(<span class="hljs-string">'handlebars'</span>);<span class="hljs-comment">// handlebars.js，模板引擎，将用户提交的信息动态填充到文件中。</span>
<span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>);<span class="hljs-comment">// chalk，可以给终端的字体加上颜色。</span>
<span class="hljs-keyword">const</span> ora = <span class="hljs-built_in">require</span>(<span class="hljs-string">'ora'</span>);<span class="hljs-comment">// ora，下载过程久的话，可以用于显示下载中的动画效果</span>
<span class="hljs-keyword">const</span> shell = <span class="hljs-built_in">require</span>(<span class="hljs-string">'shelljs'</span>);<span class="hljs-comment">// shelljs 做的事就是自动化，从耗时的重复性常规动作里解放出来</span>
<span class="hljs-keyword">const</span> child_process = <span class="hljs-built_in">require</span>(<span class="hljs-string">'child_process'</span>);<span class="hljs-comment">// child_process 创建异步进程(子进程)  exec传递的是 command 或 可执行文件</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-comment">// const path = require('path');</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: program.version 调用该命令时（如 ljh-cli -v） 会携带出'1.0.0'
 * <span class="hljs-doctag">@description</span>: program.command 定义初始化命令（如 ljh-cli init <项目名>）
 * <span class="hljs-doctag">@description</span>: program.action action是执行command命令时发生的回调 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;type&#125;</span> </span>node index.js init test == ljh-cli init ljh
 * <span class="hljs-doctag">@return</span>: program.parse(process.argv)解析命令行中的参数，解析出name,并传入action回调。
 */</span>
program.version(chalk.green(<span class="hljs-string">'♫ ===== Dark，ljh-cli ===== \n  version: 1.0.0'</span>), <span class="hljs-string">'-v, --version'</span>).
  command(<span class="hljs-string">'init <name>'</span>).
  action(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(name);
    <span class="hljs-comment">// fs.existsSync 如果路径存在，则返回 true，否则返回 false</span>
    <span class="hljs-keyword">if</span> (!fs.existsSync(name)) &#123;
      <span class="hljs-built_in">console</span>.log(chalk.magentaBright(<span class="hljs-string">'正在创建项目...'</span>));
      inquirer.prompt([
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'description'</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入项目描述'</span>
        &#125;,
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">'author'</span>,
          <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入作者名称'</span>
        &#125;
      ]).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res)
        <span class="hljs-comment">//ora、chalk模块也进行了一些视觉美化</span>
        <span class="hljs-keyword">const</span> spinner = ora(<span class="hljs-string">'正在下载模板...\n'</span>);
        spinner.start();
        <span class="hljs-comment">// 可以使用download 或 child_process</span>
        url = <span class="hljs-string">'http://xxx.git'</span>
        child_process.exec(<span class="hljs-string">'git clone '</span> + url, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">err</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (err) &#123;
            spinner.fail();
            <span class="hljs-built_in">console</span>.log(symbols.error, chalk.red(<span class="hljs-string">'模板下载失败\n'</span>,err))
          &#125; <span class="hljs-keyword">else</span> &#123;
            spinner.succeed();
            <span class="hljs-comment">// 将要移动的文件 移动到目标文件  xxx -> __dirname/<projectName></span>
            <span class="hljs-comment">// __dirname 当前模块的目录名 </span>
            <span class="hljs-comment">// shell你可以理解为一个cmd</span>
            shell.mv(__dirname + <span class="hljs-string">'/xxx'</span>, __dirname + <span class="hljs-string">'/'</span> + name)
            <span class="hljs-keyword">const</span> filename = <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>/package.json`</span>;
            <span class="hljs-keyword">const</span> meta = &#123;
              name,
              <span class="hljs-attr">description</span>: res.description,
              <span class="hljs-attr">author</span>: res.author
            &#125;
            <span class="hljs-keyword">if</span> (fs.existsSync(filename)) &#123;
              <span class="hljs-comment">// 读取目标文件的package文件</span>
              <span class="hljs-keyword">const</span> content = fs.readFileSync(filename).toString();
              <span class="hljs-keyword">let</span> dt = <span class="hljs-built_in">JSON</span>.parse(content);
              dt.name = meta.name;
              dt.author = meta.author;
              dt.description = meta.description
              <span class="hljs-comment">//改写package.json </span>
              fs.writeFile(filename,<span class="hljs-built_in">JSON</span>.stringify(dt),<span class="hljs-string">'utf8'</span>,<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
                <span class="hljs-keyword">if</span>(err)
              <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'写入失败,原因：'</span>,err);
                <span class="hljs-keyword">else</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'写入成功'</span>)
              &#125;)
              <span class="hljs-built_in">console</span>.log(symbols.success, chalk.green(<span class="hljs-string">'项目初始化完成'</span>));
            &#125; <span class="hljs-keyword">else</span> &#123;
              <span class="hljs-built_in">console</span>.log(symbols.error, chalk.red(<span class="hljs-string">'package不存在'</span>))
            &#125;
          &#125;
        &#125;)
      &#125;)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(symbols.error, chalk.red(<span class="hljs-string">'项目已存在'</span>));
    &#125;
  &#125;)
program.parse(process.argv);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，在当前目录下执行 npm link 将你的包链接到全局环境这条命令实际上就是npm的本地调试。你就可以愉快的使用脚手架了，之后可以在npm上发布，下载到全局就可以使用了。</p>
<p>参考文章：
<a href="https://blog.csdn.net/weixin_34357436/article/details/88811435" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/weixin_3435…</a>
<a href="https://blog.csdn.net/sinat_17775997/article/details/84099731" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/sinat_17775…</a></p>
<blockquote>
<p>最后附上运行效果图：</p>
</blockquote>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3800a55b3ce4458fbd178afd77dde1b1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc65b37c40e74707952e04bfdfdbfc47~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote></div>  
</div>
            