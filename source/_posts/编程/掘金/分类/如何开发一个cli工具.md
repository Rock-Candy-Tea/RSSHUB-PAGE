
---
title: '如何开发一个cli工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88b67d8c0186474ca89f39b2c669b08b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:11:27 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88b67d8c0186474ca89f39b2c669b08b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">脚手架可以帮助我们通过简单的命令来快速构建内容，目前比较常见的脚手架有vue-cli、create-react-app等，它是团队提升效率的重要手段。我们可以结合公司的业务来开发自己的脚手架工具。下面我将一步一步的开发一个脚手架工具，跟着我一起吧！</h3>
<h2 data-id="heading-1">1. 准备</h2>
<p>首先，需要确保你已经安装了node，然后我们来初始化一个项目</p>
<pre><code class="hljs language-bash copyable" lang="bash">mkdir mycli-demo & <span class="hljs-built_in">cd</span> mycli-demo
npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88b67d8c0186474ca89f39b2c669b08b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210616162547762.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">2. 添加一个简单的命令</h2>
<p>在package.json中添加bin配置，<code>mycli</code>是我们cli工具提供的命令名称，对应的值是文件入口，我们这里指向<code>bin/cli.js</code>文件</p>
<pre><code class="hljs language-diff copyable" lang="diff">&#123;
  "name": "mycli-demo",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
<span class="hljs-addition">+ "bin":&#123;</span>
<span class="hljs-addition">+   "mycli": "./bin/cli.js"</span>
<span class="hljs-addition">+ &#125;,</span>
  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1"
  &#125;,
  "keywords": [],
  "author": "",
  "license": "ISC"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目中创建<code>bin/cli.js</code>，并打印一段文字</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">#!/usr/bin/env node</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"i'm a cli"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>第一行很重要，用来指明运行环境</strong></p>
</blockquote>
<p>此时我们可以再控制台运行<code>mycli</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62e4a612910e43669a4e3c489b0f8c0f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210616161849805.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可能会上述错误，控制台找不到我们的<code>cli</code>工具，这是因为我们在使用一个工具的时候必须安装它，例如你没有安装<code>npm</code>的时候去使用也会遇到同样的错误。</p>
<p>由于我们的<code>mycli</code>并没有发布，因此可以借助<code>npm link</code>或者<code>yarn link</code>选择本地安装，执行：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm link

yarn link
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果你觉得npm link 和 yarn link比较繁琐，你也可以使用<a href="https://www.npmjs.com/package/yalc" target="_blank" rel="nofollow noopener noreferrer">yalc</a> 进行本地调试</p>
</blockquote>
<p>然后再执行<code>mycli</code>,就可以看到控制台输出了<code>bin/cli.js</code>中打印的内容</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d678d16d659b434ea365b9beec2d711a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210616164824467.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，我们已经了解<code>cli</code>工具是如何作用的，下面我们在此基础上做一些改进，让他可以处理参数，彩色打印，显示加载中等等功能</p>
<h2 data-id="heading-3">3. 处理参数</h2>
<p>很多时候我们需要在运行<code>cli</code>工具时携带参数，那么如何获取到这个参数呢？</p>
<p>在<code>node</code>程序中，通过<code>process.argv</code>可获取到命令的参数，以数组返回</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77a0e84a690e421e8a9878685088aa33~tplv-k3u1fbpfcp-watermark.image" alt="image-20210616165851713.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到其实我们已经拿到各个参数，但是这样的获取方式不太直观，所以我们引入一个第三方npm包帮我们处理这部分功能：<code>commander</code>,参考文档：<a href="https://github.com/tj/commander.js/blob/HEAD/Readme_zh-CN.md" target="_blank" rel="nofollow noopener noreferrer">commander文档</a></p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i commander -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在<code>bin/cli.js</code>添加如下代码</p>
<pre><code class="hljs language-diff copyable" lang="diff">#!/usr/bin/env node
<span class="hljs-addition">+ const program = require('commander')</span>

console.log("i'm a cli")

// 打印参数
console.log(process.argv)

<span class="hljs-addition">+ program</span>
<span class="hljs-addition">+  .command('create <projectName>')</span>
<span class="hljs-addition">+  .description('create a new project')</span>
<span class="hljs-addition">+  .alias('c')</span>
<span class="hljs-addition">+  .option('-r, --react', 'react template')</span>
<span class="hljs-addition">+  .option('-v, --vue', 'vue template')</span>
<span class="hljs-addition">+  .option('-v2, --vue2', 'vue2 template')</span>
<span class="hljs-addition">+  .option('-v3, --vue3', 'vue3 template')</span>
<span class="hljs-addition">+  .action((projectName, options) => &#123;</span>
<span class="hljs-addition">+    console.log(projectName, options)</span>
<span class="hljs-addition">+ &#125;)</span>
<span class="hljs-addition">+ program.version('1.0.0').parse(process.argv)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到目前为止，我们可以直观的获取到命令的参数，你可以在控制台尝试一下</p>
<h2 data-id="heading-4">4. 交互式命令</h2>
<p>有的时候我们可能需要在命令行工具中融入一些交互，根据用户的输入或者选择生成一些东西或者做相应的操作。我们可以引入一个<code>npm</code>包来帮我们实现：<a href="https://www.npmjs.com/package/inquirer" target="_blank" rel="nofollow noopener noreferrer">inquirer</a></p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i inquirer -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在<code>bin/cli.js</code>添加如下代码</p>
<pre><code class="hljs language-diff copyable" lang="diff">#!/usr/bin/env node
const program = require('commander')
<span class="hljs-addition">+ const inquirer = require('inquirer')</span>

console.log("i'm a cli")

// 打印参数
console.log(process.argv)

program
  .command('create <projectName>')
  .description('create a new project')
  .alias('c')
  .option('-r, --react', 'react template')
  .option('-v, --vue', 'vue template')
  .option('-v2, --vue2', 'vue2 template')
  .option('-v3, --vue3', 'vue3 template')
  .action((projectName, options) => &#123;
    console.log(projectName, options)
<span class="hljs-addition">+   inquirer</span>
<span class="hljs-addition">+     .prompt([</span>
<span class="hljs-addition">+       &#123;</span>
<span class="hljs-addition">+         type: 'list',</span>
<span class="hljs-addition">+         name: 'frameTemplate',</span>
<span class="hljs-addition">+         message: '请选择框架类型',</span>
<span class="hljs-addition">+         choices: ['Vue3', 'Vue2', 'React']</span>
<span class="hljs-addition">+       &#125;</span>
<span class="hljs-addition">+     ])</span>
<span class="hljs-addition">+     .then((answer) => &#123;</span>
<span class="hljs-addition">+       console.log(answer)</span>
<span class="hljs-addition">+     &#125;)</span>
  &#125;)
program.version('1.0.0').parse(process.argv)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在控制台运行</p>
<pre><code class="hljs language-bash copyable" lang="bash">mycli create <span class="hljs-built_in">test</span> -r
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa23d72dacb340d38f3fd611f4b09b6b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210616185522361.png" loading="lazy" referrerpolicy="no-referrer">
至此，我们完成了交互式命令，下面我将完成一个模板的下载，一起动手吧！</p>
<h2 data-id="heading-5">5. 完成一个模板下载</h2>
<p>在前面的步骤中，我们发现我们的日志打印不是很友好，我们可以通过<code>log-symblos</code> <code>chalk</code> <code>ora</code> 帮我们做一些提示信息的优化</p>





























<table><thead><tr><th align="left">npm包名称</th><th>作用</th><th>官网</th><th>备注</th></tr></thead><tbody><tr><td align="left">chalk</td><td>修改控制台中字符串的样式</td><td><a href="https://github.com/chalk/chalk#readme" target="_blank" rel="nofollow noopener noreferrer">chalk</a></td><td>字体样式、颜色、背景颜色</td></tr><tr><td align="left">log-symbols</td><td>各种日志级别的彩色符号</td><td><a href="https://github.com/sindresorhus/log-symbols#readme" target="_blank" rel="nofollow noopener noreferrer">log-symbols</a></td><td>从5版本开始使用ESM<a href="https://github.com/sindresorhus/log-symbols/releases/tag/v5.0.0" target="_blank" rel="nofollow noopener noreferrer">Release v5.0.0</a></td></tr><tr><td align="left">ora</td><td>终端加载效果</td><td><a href="https://github.com/sindresorhus/ora#readme" target="_blank" rel="nofollow noopener noreferrer">ora</a></td><td></td></tr></tbody></table>
<blockquote>
<p>由于log-symbols 从5版本开始使用ESM，所以我们这里使用4版本</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">npm i chalk log-symbols@4 ora -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要下载一个github仓库的代码，我们需要引入<code>download-git-repo</code>,  <a href="https://www.npmjs.com/package/download-git-repo" target="_blank" rel="nofollow noopener noreferrer">download-git-repo - npm</a></p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i download-git-repo -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来实现一个简单的下载功能</p>
<pre><code class="hljs language-diff copyable" lang="diff">#!/usr/bin/env node
const program = require('commander')
const inquirer = require('inquirer')
<span class="hljs-addition">+ const ora = require('ora')</span>
<span class="hljs-addition">+ const download = require('download-git-repo')</span>
<span class="hljs-addition">+ const &#123; errLog, successLog &#125; = require('../src/utils/log.js')</span>

console.log("i'm a cli")

// 打印参数
console.log(process.argv)

program
  .command('create <projectName>')
  .description('create a new project')
  .alias('c')
  .option('-r, --react', 'react template')
  .option('-v, --vue', 'vue template')
  .option('-v2, --vue2', 'vue2 template')
  .option('-v3, --vue3', 'vue3 template')
  .action((projectName, options) => &#123;
    console.log(projectName, options)
    inquirer
      .prompt([
        &#123;
          type: 'list',
          name: 'frameTemplate',
          message: '请选择框架类型',
          choices: ['Vue3', 'Vue2', 'React']
        &#125;
      ])
      .then((answer) => &#123;
        console.log(answer)
<span class="hljs-addition">+       const spinner = ora()</span>
<span class="hljs-addition">+       spinner.text = '正在下载模板...'</span>
<span class="hljs-addition">+       spinner.start()</span>
<span class="hljs-addition">+       download(</span>
<span class="hljs-addition">+         '',</span>
<span class="hljs-addition">+         projectName,</span>
<span class="hljs-addition">+         &#123; clone: true &#125;,</span>
<span class="hljs-addition">+         function (err) &#123;</span>
<span class="hljs-addition">+           if (err) &#123;</span>
<span class="hljs-addition">+             spinner.fail('模板下载失败')</span>
<span class="hljs-addition">+             errLog(err)</span>
<span class="hljs-addition">+           &#125; else &#123;</span>
<span class="hljs-addition">+             spinner.succeed('模板下载成功')</span>
<span class="hljs-addition">+             successLog('项目初始化完成')</span>
<span class="hljs-addition">+           &#125;</span>
<span class="hljs-addition">+         &#125;</span>
<span class="hljs-addition">+       )</span>
      &#125;)
  &#125;)
program.version('1.0.0').parse(process.argv)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台输入</p>
<pre><code class="hljs language-bash copyable" lang="bash"> mycli create <span class="hljs-built_in">test</span> -r
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到模板下载成功</p>
<blockquote>
<p>如果下载不成功，请详细查看<code>download-git-repo</code>的文档：<a href="https://www.npmjs.com/package/download-git-repo" target="_blank" rel="nofollow noopener noreferrer">download-git-repo - npm</a></p>
</blockquote>
<p>至此，我们已经实现了一个简单的模板仓库下载功能。更多的功能大家可以自行尝试。</p>
<p>如果我们想让其他小伙伴使用，我们需要把这个cli发布到npm，如何发布不在此篇文章展开叙述。</p>
<h2 data-id="heading-6">6. 项目优化</h2>
<p>如果我们有多个命令，那么我们就需要写多个</p>
<pre><code class="hljs language-js copyable" lang="js">program
  .command(<span class="hljs-string">''</span>)
  .description(<span class="hljs-string">''</span>)
  .alias(<span class="hljs-string">''</span>)
  .option(<span class="hljs-string">''</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 命令处理</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>因为这部分代码被重复使用，我们自然而然想到了遍历，首先声明一个list变量用来维护我们的命令配置，在src新建command-config.js文件，该文件导出配置</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> COMMAND_LIST = [
  &#123;
    <span class="hljs-attr">command</span>: <span class="hljs-string">'create <projectName>'</span>,
    <span class="hljs-attr">description</span>: <span class="hljs-string">'create a new project'</span>,
    <span class="hljs-attr">alias</span>: <span class="hljs-string">'c'</span>,
    <span class="hljs-attr">options</span>: [
      [<span class="hljs-string">'-r, --react'</span>, <span class="hljs-string">'react template'</span>],
      [<span class="hljs-string">'-v, --vue'</span>, <span class="hljs-string">'vue template'</span>],
      [<span class="hljs-string">'-v2, --vue2'</span>, <span class="hljs-string">'vue2 template'</span>],
      [<span class="hljs-string">'-v3, --vue3'</span>, <span class="hljs-string">'vue3 template'</span>]
    ],
    <span class="hljs-attr">action</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'./commandHandler/create'</span>),
    <span class="hljs-attr">examples</span>: [<span class="hljs-string">'-r'</span>, <span class="hljs-string">'--react'</span>, <span class="hljs-string">'-v'</span>, <span class="hljs-string">'--vue'</span>, <span class="hljs-string">'-v2'</span>, <span class="hljs-string">'--vue2'</span>, <span class="hljs-string">'-v3'</span>, <span class="hljs-string">'--vue3'</span>].map(<span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-string">`create projectName <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
  &#125;
]

<span class="hljs-built_in">module</span>.exports = COMMAND_LIST

<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>bin/cli.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 注册option
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>commander commander实例
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>option 每个命令配置对象
 * <span class="hljs-doctag">@returns <span class="hljs-variable">commander</span></span>
 */</span>
<span class="hljs-keyword">const</span> registerOption = <span class="hljs-function">(<span class="hljs-params">commander, option</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> option && option.length ? commander.option(...option) : commander
&#125;
<span class="hljs-comment">/**
 * 注册action
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>commander commander实例
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Object&#125;</span> </span>commandEle 每个命令配置对象
 * <span class="hljs-doctag">@returns <span class="hljs-variable">commander</span></span>
 */</span>
<span class="hljs-keyword">const</span> registerAction = <span class="hljs-function">(<span class="hljs-params">commander, commandEle</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; command, description, alias, options, action &#125; = commandEle
  <span class="hljs-keyword">const</span> c = commander
    .command(command) <span class="hljs-comment">// 命令的名称</span>
    .description(description) <span class="hljs-comment">// 命令的描述</span>
    .alias(alias)
  <span class="hljs-comment">// 循环options</span>
  options && options.reduce(registerOption, c)
  c.action(action)
  <span class="hljs-keyword">return</span> commander
&#125;

<span class="hljs-comment">// 循环创建命令</span>
COMMAND_LIST.reduce(registerAction, program)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>由于命令处理部分代码量较大，所以我们考虑把命令处理的函数提取在一个文件夹下，我们在src下新建commandHandler目录，并新建一个create.js，把create命令的处理代码放进create.js</p>
</li>
<li>
<p>为了更方便使用，我们改写mycli --help命令</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// help命令 把example显示出去</span>
<span class="hljs-keyword">const</span> help = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'\n'</span>)
  <span class="hljs-built_in">console</span>.log(chalk.green(<span class="hljs-string">'如何使用:'</span>))
  COMMAND_LIST.forEach(<span class="hljs-function">(<span class="hljs-params">command, index</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'  '</span>, chalk.keyword(<span class="hljs-string">'orange'</span>)(index + <span class="hljs-number">1</span>), <span class="hljs-string">`<span class="hljs-subst">$&#123;command.command&#125;</span>命令`</span>)
    command.examples.forEach(<span class="hljs-function">(<span class="hljs-params">example</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`     - mycli <span class="hljs-subst">$&#123;example&#125;</span>`</span>)
    &#125;)
  &#125;)
&#125;

program.on(<span class="hljs-string">'-h'</span>, help)
program.on(<span class="hljs-string">'--help'</span>, help)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们输入<code>mycli --help</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2030ff4a1844b63826f9cce5ffc9eff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>循环部分可自行再进行优化</p>
</blockquote>
<p>至此我们完成了一个简易版cli工具的开发</p>
<p>源码：<a href="https://github.com/enbrands/step-by-step-cli.git" target="_blank" rel="nofollow noopener noreferrer">github.com/enbrands/st…</a></p>
<p>main分支只git init该项目，其他分支每个分支完成一个步骤</p></div>  
</div>
            