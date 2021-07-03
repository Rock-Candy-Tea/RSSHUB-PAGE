
---
title: '搭建一个NodeJS脚手架'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3598'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 00:33:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=3598'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前端脚手架搭建分享</h1>
<hr>
<p>最近团队需要统一脚手架，花了点时间了解了一下如何去进行搭建
其实原理并不复杂，</p>
<blockquote>
<p>第一步，首先我们要知道需要哪些东西，然后我们要创建什么东西</p>
</blockquote>
<ol>
<li>
<p>我们首先需要一个可被 node 执行入口文件</p>
</li>
<li>
<p>需要生成文件的模板</p>
</li>
<li>
<p>使用 node fs 模块把模板写入我们指定的目录</p>
</li>
</ol>
<blockquote>
<p>这是最简单的思路，那么我们就可以动手了</p>
</blockquote>
<ol>
<li>
<p>首先创建一个文件夹，然后在文件夹执行 npm init 初始化一个 package.json 文件</p>
</li>
<li>
<p>然后创建一个入口文件 index.js，然后写入</p>
<pre><code class="copyable">#!/usr/bin/env node

console.log('hello,cli!');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候执行 node index.js 就能够在控制台打印 hello,cil!</p>
</li>
<li>
<p>再创建一个模板文件 template.js, 添加字符串</p>
<pre><code class="copyable">hello,template!
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>然后我们在 index.js 进行修改，通过 process.cwd()获取 node 当前执行路径，我们可以读取一个文件，并写入到一个目录下</p>
<pre><code class="copyable">#!/usr/bin/env node

console.log('hello,cli!');

const fs = require("fs");
const path = require("path");

const folderName = path.join(process.cwd(), "/cli");

// 判断文件夹是否存在
const mkdirFile = (name) => &#123;
try &#123;
    if (!fs.existsSync(name)) &#123;
    fs.mkdirSync(name);
    &#125;
&#125; catch (err) &#123;
    console.error(err);
&#125;
&#125;;

fs.readFile("./template.js", "utf-8", (err, data) => &#123;
if (err) &#123;
    console.log(err);
    return;
&#125; else &#123;
    console.log(data);
    mkdirFile(folderName);
    fs.writeFileSync(`$&#123;folderName&#125;/template.js`, data);
&#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>第一步基础就完成了。下面我们进行思考</p>
<blockquote>
<p>如何在创建脚手架时，需要在控制台进行交互，这时候需要引入安装第三方库</p>
</blockquote>
<ul>
<li>commander 可以自动的解析命令和参数，用于处理用户输入的命令</li>
<li>inquirer 用户输入/选择交互</li>
<li>ora 控制台进度动画提示</li>
</ul>
<p>好了，这时候我们修改 index.js，执行 node index.js 就会提示，使用 create 参数，执行 node index.js create 项目名，然后进入项目类型选择，选择完成，就会创建对应名称的项目文件夹，并在里面创建 template.js</p>
</li>
</ol>
<pre><code class="copyable">#!/usr/bin/env node

// console.log("hello,cli!");

const fs = require("fs");
const path = require("path");
const ora = require("ora");
const inquirer = require("inquirer");
const program = require("commander");

// 判断文件夹是否存在
const mkdirFile = (name) => &#123;
  try &#123;
    if (!fs.existsSync(name)) &#123;
      fs.mkdirSync(name);
    &#125;
  &#125; catch (err) &#123;
    console.error(err);
  &#125;
&#125;;

const doFs = (name) => &#123;
  fs.readFile("./template.js", "utf-8", (err, data) => &#123;
    if (err) &#123;
      console.log(err);
      return;
    &#125; else &#123;
      mkdirFile(name);
      fs.writeFileSync(`$&#123;name&#125;/template.js`, data);
    &#125;
  &#125;);
&#125;;

program
  //   .version('1.0.0')
  .command("create <app-name>")
  .description("create a new project")
  .action(async (name) => &#123;
    const cwd = process.cwd();

    const questions = [
      &#123;
        type: "list",
        message: "请选择项目类型: ",
        name: "type",
        choices: [&#123; name: "web项目", value: "web" &#125;],
      &#125;,
    ];
    const &#123; type &#125; = await inquirer.prompt(questions);

    const proce = ora("Start creating...");
    proce.start();
    const folderName = path.join(cwd, name);
    doFs(folderName);
    proce.succeed("succeed done!");
  &#125;);

program.parse(process.argv);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么到此，我们的基本思路已经完成，我们需要重新整理一下。</p>
<ul>
<li>
<p>首先，我们创建一个 bin 文件夹，添加 tara.js 文件，作为我们的入口，在其中引入 index.js</p>
</li>
<li>
<p>创建一个 src 文件夹，里面存放我们所有的源码，添加 src/core 文件夹</p>
</li>
<li>
<p>因为后续的模板定义，类定义会用到，我们需要可直接执行 ts 文件，所以需要添加一个第三方组件，npm i -S ts-node @types/node，具体使用可以参照官方文档，然后将 tara.js 改造</p>
</li>
</ul>
<pre><code class="copyable">#!/usr/bin/env node

const tsNode = require("ts-node/dist/bin");
const path = require("path");

(async () => &#123;
    const argv = process.argv.slice(2);
    const dir = path.join(__dirname, "../src");
    tsNode.main(["index.ts", ...argv], &#123; "--dir": dir &#125;);
&#125;)();

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>修改 index.js 为 index.ts，并给所有方法参数添加类型定义，然后直接执行 node bin/tara，这时候会抛 Cannot find module 'typescript'错误，需要安装 ts 库 npm i -S typescript</p>
</li>
<li>
<p>这时候我们也可以使用远程模板 download-git-repo 支持从 Github 下载仓库，详细了解可以参考官方文档。</p>
</li>
</ul>
<pre><code class="copyable">npm install --save download-git-repo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>download() 第一个参数就是仓库地址,详细了解可以看官方文档</p>
<ul>
<li>
<p>使用本地模板，那我们的思路是，可以生成一个统一的模板配置对象，然后根据配置，一个一个的生成文件，从而生成完整的项目目录</p>
<ul>
<li>
<p>那第一步就是先创建一个模板类 Project.ts，定义生成 package.json 文件的属性</p>
<blockquote>
<p>_init_方法是一个抽象方法，用于子类进行自定义一些操作</p>
</blockquote>
</li>
</ul>
<pre><code class="copyable">    import Package from "./Package";

    abstract class Project &#123;
        name: string;
        private package: Package;

        constructor(parameters) &#123;&#125;


        init() &#123;&#125;

        protected abstract _init_: void;
    &#125;

    export default Project;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建一个 Package 类</li>
</ul>
<pre><code class="copyable">class Package &#123;
    constructor(parameters) &#123;&#125;
&#125;

export default Package;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>// TODO</p></div>  
</div>
            