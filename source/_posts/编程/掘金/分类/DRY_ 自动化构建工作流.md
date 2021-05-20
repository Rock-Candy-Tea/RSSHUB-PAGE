
---
title: 'DRY_ 自动化构建工作流'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9646'
author: 掘金
comments: false
date: Wed, 19 May 2021 22:49:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=9646'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文章内容输出来源：拉勾大前端高薪训练营</p>
</blockquote>
<h2 data-id="heading-0">工程化概述</h2>
<h3 data-id="heading-1">工程化的定义和主要解决的问题</h3>
<ul>
<li>
<p>全副武装:通过工程化提升战斗力。</p>
</li>
<li>
<p>问题1: 想要使用ES6+新特性，但是兼容有问题。</p>
</li>
<li>
<p>问题2: 想要使用Less/Sass/PostCSS增强CSS的编程性但是运行环境不能直接支持。</p>
</li>
<li>
<p>问题3: 想要使用模块化的方式提高项目的可维护性但运行环境不能直接支持。</p>
</li>
<li>
<p>问题4: 部署上线前需要手动压缩代码和资源文件。</p>
</li>
<li>
<p>问题5: 部署过程需要手动上传代码到服务器。</p>
</li>
<li>
<p>问题6: 多人协作开发时，无法硬性统一大家的代码风格。</p>
</li>
<li>
<p>问题7: 从仓库中pull回来的代码质量无法保证。</p>
</li>
<li>
<p>问题8: 部分功能开发时需要等待后端服务接口提前完成。</p>
</li>
<li>
<p>问题归类</p>
<ul>
<li>传统语言或语法的弊端。</li>
<li>无法使用模块化/组件化。</li>
<li>重复的机械式工作。</li>
<li>代码风格统一、质量保证。</li>
<li>依赖后端服务接口支持。</li>
<li>整体依赖后端项目。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-2">一个项目过程中工程化的表现。</h3>
<ul>
<li>
<p>一切以降本增效、质量保证为目的的手段都属于☛工程化☚</p>
</li>
<li>
<p>一切重复的工作都应该被自动化。</p>
<ul>
<li>
<p>创建项目</p>
<ul>
<li>创建项目结构。</li>
<li>创建特定类型文件。</li>
</ul>
</li>
<li>
<p>编码</p>
<ul>
<li>格式化代码</li>
<li>检验代码风格</li>
<li>编译/构建/打包</li>
</ul>
</li>
<li>
<p>预览/测试</p>
<ul>
<li>Web Server/Mock</li>
<li>Live Reloading/HMR</li>
<li>Source Map</li>
</ul>
</li>
<li>
<p>提交</p>
<ul>
<li>Git Hooks</li>
<li>Lint-staged</li>
<li>持续集成</li>
</ul>
</li>
<li>
<p>部署</p>
<ul>
<li>CI/CD</li>
<li>自动发布</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-3">工程化  ≠  某个工具</h3>
<ul>
<li>工具不是工程化的核心</li>
<li>工程化的核心是对项目整体的规划或者说架构</li>
<li>工具只是落地规划或架构过程的一种手段。</li>
</ul>
<h3 data-id="heading-4">工程化与Node.js</h3>
<ul>
<li>
<p>工程化 Powered by Node.js</p>
</li>
<li>
<p>Node.js让前端有了一个新舞台。</p>
</li>
<li>
<p>前端工程化由Node.js强烈驱动的。</p>
</li>
<li>
<p>落实工程化</p>
<ul>
<li>脚手架工具开发</li>
<li>自动化构建系统</li>
<li>模块化打包</li>
<li>项目代码规范化</li>
<li>自动化部署</li>
</ul>
</li>
</ul>
<h2 data-id="heading-5">脚手架工具</h2>
<h3 data-id="heading-6">脚手架的作用</h3>
<ul>
<li>
<p>前端工程化的发起者</p>
</li>
<li>
<p>用于创建项目基础结构</p>
</li>
<li>
<p>提供项目规范和约定</p>
<ul>
<li>相同的文件组织结构</li>
<li>相同的开发范式</li>
<li>相同的模块依赖</li>
<li>相同的工具配置</li>
<li>相同的基础代码</li>
</ul>
</li>
<li>
<p>可以快速搭建特定类型的项目骨架</p>
</li>
<li>
<p>示例:IDE创建项目的过程就是一个脚手架的工作流程。</p>
</li>
<li>
<p>前端脚手架都是以一个独立的工具存在。</p>
</li>
<li>
<p>目标: 都是为了解决我们在创建项目过程当中那些复杂的工作。</p>
</li>
</ul>
<h3 data-id="heading-7">常用的脚手架工具</h3>
<ul>
<li>
<p>创建项目时才用到的脚手架工具</p>
<ul>
<li>
<p>服务于特定项目类型的脚手架工具</p>
<ul>
<li>React项目↝create-react-app</li>
<li>Vue.js项目↝vue-cli</li>
<li>Agular项目↝angular-cli</li>
<li>共同点:根据你提供的信息生成对应的项目基础结构。</li>
<li>不同处:一般只适用于自身所服务那个框架的项目。</li>
</ul>
</li>
<li>
<p>通用型项目脚手架工具</p>
<ul>
<li>以Yeomen为代表。</li>
<li>可以根据一套模板生成一个对应额额项目结构。</li>
<li>很灵活</li>
<li>很容易扩展</li>
</ul>
</li>
</ul>
</li>
<li>
<p>另一类脚手架</p>
<ul>
<li>用于在项目开发过程中去创建一些特定类型的文件</li>
<li>以Plop为代表</li>
<li>示例:创建一个组件/模块所需要的文件。</li>
</ul>
</li>
<li>
<p>重点关注几个有代表性的工具</p>
<ul>
<li>Yeoman</li>
<li>Plop</li>
</ul>
</li>
<li>
<p>脚手架的工作原理</p>
<ul>
<li>启动过后，会询问一些预设的问题，然后将回答的结果结合一些模板文件来生成项目结构。</li>
<li>脚手架实质上就是一个node cli 应用。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">通用脚手架工具剖析</h3>
<ul>
<li>
<p>Yeoman</p>
<ul>
<li>
<p>The web's scaffolding tool for modern webapps</p>
</li>
<li>
<p>作为最老牌最强大最通用的一款工具，有很多值得我们借鉴的地方。</p>
</li>
<li>
<p>更像一款脚手架运行平台</p>
</li>
<li>
<p>官方定义: 用于创建现代web应用的脚手架工具。</p>
</li>
<li>
<p>可以搭配Generator去创建任何类型的项目。</p>
</li>
<li>
<p>缺点:在很多专注基于框架的人眼中Yeoman过于通用，不够专注。他们更愿意使用像vue-cli等工具。</p>
</li>
<li>
<p>基本使用</p>
<ul>
<li>
<p>依赖Node环境</p>
</li>
<li>
<p>yarn global add yo</p>
</li>
<li>
<p>配合Generator:  yarn global add generator-node</p>
</li>
<li>
<p>新项目使用: yo node</p>
</li>
<li>
<p>总结</p>
<ul>
<li>
<p>在全局范围安装yo</p>
<ul>
<li>npm install yo --global</li>
<li>yarn global add yo</li>
</ul>
</li>
<li>
<p>安装对应的generator</p>
<ul>
<li>npm install generator-node --global</li>
<li>yarn global add generator-node</li>
</ul>
</li>
<li>
<p>通过yo运行generator</p>
<ul>
<li>cd path/to/project-dir</li>
<li>mkdir my-module</li>
<li>yo node</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Sub Generator</p>
<ul>
<li>子级生成器</li>
<li>使用: yo node:cli</li>
</ul>
</li>
<li>
<p>常规使用步骤</p>
<ul>
<li>1，明确你的需求</li>
<li>2，找到合适的Generator</li>
<li>3，全局范围安装找到的Generator</li>
<li>4，通过yo运行对应的Generator</li>
<li>5，通过命令行交互填写选项</li>
<li>6，生成你所需要的项目结构</li>
<li>示例: web应用生成器</li>
</ul>
<p>yarn global add generator-webapp
yo webapp</p>
</li>
<li>
<p>自定义Generator</p>
<ul>
<li>
<p>基于Yeoman搭建自己的脚手架。</p>
</li>
<li>
<p>创建Generator模块</p>
<ul>
<li>
<p>Generator本质上就是一个NPM模块。</p>
</li>
<li>
<p>Generator基本结构</p>
<ul>
<li>generator/app/index.js</li>
<li>generator/component/index.js</li>
<li>package.json</li>
<li>命名: generator-</li>
</ul>
</li>
<li>
<p>案例演示</p>
<ul>
<li>
<p>mkdir generator-sample</p>
</li>
<li>
<p>cd generator-sample</p>
</li>
<li>
<p>yarn init</p>
<ul>
<li>初始化package.json文件</li>
</ul>
</li>
<li>
<p>yarn add yeoman-generator</p>
</li>
<li>
<p>VSCode打开: code  .</p>
</li>
<li>
<p>创建文件: generator/app/index.js</p>
<ul>
<li>此文件为generator的核心入口</li>
<li>需要导出一个继承自Yeoman Generator 的类型</li>
<li>Yeoman Generator 在工作时会自动调用我们在此类型中定义的一些生命周期方法。</li>
<li>我们在这些方法中可以通过调用父类提供的一些工具方法实现一些功能，例如文件写入。</li>
<li>const Generator  =   require('yeoman-generator')</li>
<li>module.exports = class extends Generator &#123;</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>writing () &#123;
// Yeoman 自动在生成文件阶段调用此方法
//  我们这里尝试往项目目录中写入文件
this.fs.write(this.destinationPath('temp.txt'), Math.random().toString())
&#125;</p>
</li>
</ul>
<p>&#125;
- yarn link</p>
<pre><code class="copyable">- cd  ..
- mkdir my-proj
- cd my-proj
- yo sample

- 根据模板创建文件

- 创建模板文件: app/templates/foo.txt

- 模板遵循ejs模板语法

- <%=  name  %>
- <%  if(success) &#123; %>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成文件内容
<%  &#125; %></p>
<pre><code class="copyable">- 通过模板方式写入文件到目标
- 模板文件路径获取:  const temp1=this.templatePath('foo.txt')
- 输出目标路径: const output= this.destinationPath('foo')
- 模板数据上下文: const context = &#123; name: 'sjz' &#125;
- this.fs.copyTpl(temp1, output, context)
- yo sample
- 相对于手动创建每一个文件，模板的方式大大提高了效率。

- 接收用户输入数据

- module.exports = class extends Generator &#123;
prompting () &#123;
    // Yeoman 在询问用户环节会自动调用此方法。
    //  在此方法中可以调用父类的prompt() 方法发出对用户的命令行询问。
    return this.prompt([
          &#123;
               type:'input',
               name: 'name',
               message: 'sjz',
               default: this.appname
          &#125;
    ])
    .then(answers ⥤ &#123;
          console.log(answers)
          this.answers = answers
     &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- Vue Generator 案例

- mkdir generator-sjz-vue
- cd generator-sjz-vue
- yarn init
- yarn add yeoman-generator
- code  .
- 创建主入口文件: generator/app/index.js

- const Generator = require('yeoman-generator')
- module.exports =  class extends Generator &#123;
prompting () &#123;
   return this.prompt([
       &#123;
          type: 'input',
          name: 'name',
          message: 'your project name',
          default: this.appname
       &#125;
   ])
   .then(answers ⥤ &#123;
       this.answers = answers
   &#125;)
&#125;
writing () &#123;
    // 把每一个文件都通过模板转换到目标路径
    const templates = []
    templates.forEach(item ⥤ &#123;
       // item ⥤每个文件路径
       this.fs.copyTpl(
           this.templatePath(item),
           this.destinationPath(item),
           this.answers
       )
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
- 创建templates目录，并把准备好的文件及目录结构拷贝到templates目录中。
- yarn link</p>
<pre><code class="copyable">- cd  ..
- mkdir my-proj
- cd my-proj
- yo sjz-vue

- 发布Generator

- 将项目源代码托管到公开的源代码仓库上面。
- 先创建本地仓库

- echo node-modules >.gitignore
- git init

- 初始化本地空仓库

- git status
- git add  .
- git commit -m "feat: initial commit"
- 创建远端仓库
- git remote add origin 远端仓库地址
- git push -u origin master
- npm publish/yarn publish

- yarn publish --registry=https://registry.yarnpkg.com

- 问题:淘宝镜像是只读镜像
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>Plop</p>
<ul>
<li>
<p>一个小而美的脚手架工具</p>
</li>
<li>
<p>是一款主要用于创建项目中特定类型文件的小工具，有些类似Yeoman中的子生成器Sub Generator。</p>
</li>
<li>
<p>一般不会独立使用</p>
<ul>
<li>
<p>一般集成到项目中用来自动化创建同类型的文件</p>
</li>
<li>
<p>使用场景: 需要重复创建相同类型的文件，例如react中创建组件都要重复创建3个文件(css/js/html)</p>
</li>
<li>
<p>Plop的具体使用</p>
<ul>
<li>
<p>1，yarn add plop --dev</p>
</li>
<li>
<p>2，新建plopfile.js文件</p>
<ul>
<li>
<p>plop工作的入口文件</p>
</li>
<li>
<p>需要导出一个函数</p>
</li>
<li>
<p>函数中接收一个plop的对象参数</p>
</li>
<li>
<p>参数plop对象中提供了一系列的工具函数</p>
</li>
<li>
<p>这些工具函数用于创建生成器任务。</p>
</li>
<li>
<p>上代码</p>
<ul>
<li>module.exports = plop ⥤ &#123;</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>plop.setGenerator('generatorName',  &#123;
description: '生成器描述',
prompts: [
&#123;
type: 'input',
name: 'name',
message: '屏幕提示',
default: '默认答案',
&#125;
],
actions: [
&#123;
type: 'add', // 添加一个全新的文件
path: 'src/components/&#123;&#123;name&#125;&#125;/&#123;&#123;name&#125;&#125;.js',
templateFile: 'plop-templates/component.hbs',
&#125;,
&#123;
type: 'add', // 添加一个全新的文件
path: 'src/components/&#123;&#123;name&#125;&#125;/&#123;&#123;name&#125;&#125;.css',
templateFile: 'plop-templates/component.css.hbs',
&#125;,
&#123;
type: 'add', // 添加一个全新的文件
path: 'src/components/&#123;&#123;name&#125;&#125;/&#123;&#123;name&#125;&#125;.test',
templateFile: 'plop-templates/component.test.hbs',
&#125;,
]
&#125;)</p>
</li>
</ul>
<p>&#125;</p>
<pre><code class="copyable">- 运行

- yarn plop generatorName

- 总结

- 1，将plop模块作为项目开发依赖安装
- 2，在项目根目录下创建一个plopfile.js文件
- 3，在plopfile.js文件中定义脚手架任务
- 4，编写用于生成特定类型文件的模板
- 5，通过plop提供的CLI运行脚手架任务
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">开发一款脚手架</h3>
<ul>
<li>
<p>mkdir sample-scaffolding</p>
</li>
<li>
<p>cd sample-scaffolding</p>
</li>
<li>
<p>yarn init</p>
<ul>
<li>初始化package.json文件。</li>
</ul>
</li>
<li>
<p>VsCode打开: code  .</p>
</li>
<li>
<p>在package.json中添加bin属性</p>
<ul>
<li>值为'cli.js'</li>
</ul>
</li>
<li>
<p>根目录新建文件: cli.js</p>
<ul>
<li>
<p>此文件必须要有特定文件头: #!/usr/bin/env node</p>
<ul>
<li>
<p>Linux/macOS系统下</p>
<ul>
<li>还需要修改此文件的读写权限为 755</li>
<li>具体就是通过 chmod 755 cli.js 实现修改</li>
</ul>
</li>
</ul>
</li>
<li>
<p>内容:console.log('sjz')</p>
</li>
</ul>
</li>
<li>
<p>yarn link</p>
<ul>
<li>将脚手架link到全局</li>
</ul>
</li>
<li>
<p>然后就可以在命令行执行:  sample-scaffolding</p>
<ul>
<li>运行结果: sjz</li>
</ul>
</li>
<li>
<p>实现脚手架的具体过程</p>
<ul>
<li>
<p>1，通过命令行交互询问用户问题</p>
<ul>
<li>
<p>安装询问模块inquirer</p>
<ul>
<li>yarn add inquirer</li>
</ul>
</li>
</ul>
</li>
<li>
<p>2，根据用户回答的结果生成文件</p>
</li>
<li>
<p>cli.js中代码实现</p>
<ul>
<li>const fs = require('fs')</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>const path = require('path')
const inquirer = require('inquirer')
const ejs = require('ejs')</p>
<pre><code class="copyable">- 

- inquirer.prompt([
&#123;
    type: 'input',
    name: 'name',
    message: 'Project name?',
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>])
.then(answers ⥤ &#123;
// 根据用户回答的结果生成文件
// 模板目录
const tmplDir = path.join(__dirname, 'templates')
// 目标目录
const destDir = process.cwd()
// 将模板下的文件全部转换到目标目录
fs.readdir(tmplDir, (err, files) ⥤ &#123;
if(err) throw err
files.forEach(file ⥤ &#123;
// 通过模板引擎渲染文件
ejs.renderFile(path.join(tmplDir,file), answers, (err, result) ⥤ &#123;
if(err) throw err
fs.writeFileSync(path.join(destDir, file), result)
&#125;)
&#125;)
&#125;
&#125;)</p>
<pre><code class="copyable">- 创建模板文件

- templates/index.html
- templates/style.css

- 安装模板引擎

- yarn add ejs
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">自动化构建</h2>
<h3 data-id="heading-11">简介</h3>
<ul>
<li>
<p>一切重复工作本应自动化</p>
</li>
<li>
<p>名字解释</p>
<ul>
<li>
<p>自动化</p>
<ul>
<li>机器代替手工完成一些工作</li>
</ul>
</li>
<li>
<p>构建</p>
<ul>
<li>可以理解为转换</li>
<li>把一个东西转换为另一些东西。</li>
</ul>
</li>
</ul>
</li>
<li>
<p>就是把源代码自动化构建或转换为生产代码</p>
<ul>
<li>这个转换或构建过程称为自动化构建工作流。</li>
</ul>
</li>
<li>
<p>作用</p>
<ul>
<li>
<p>可以脱离运行环境兼容带来的问题</p>
</li>
<li>
<p>允许使用提高效率的语法、规范和标准</p>
<ul>
<li>
<p>ECMAScript Next</p>
</li>
<li>
<p>Sass</p>
</li>
<li>
<p>模板引擎</p>
<ul>
<li>抽象源码文件中重复的代码</li>
</ul>
</li>
<li>
<p>以上这些用法大都不被浏览器直接支持</p>
</li>
<li>
<p>可以使用自动化构建工具构建转换那些不被支持的☞特性。</p>
</li>
</ul>
</li>
<li>
<p>可以提高开发效率</p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-12">自动化构建初体验</h3>
<ul>
<li>
<p>新建sass文件: scss/main.scss</p>
<ul>
<li>
<p>内容</p>
<ul>
<li>$body-bg: #f8f9fb</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>$body-color: #333</p>
<p>body &#123;
margin: 0 auto;
padding: 20px;
max-width: 800px;
background-color: <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>b</mi><mi>o</mi><mi>d</mi><mi>y</mi><mo>−</mo><mi>b</mi><mi>g</mi><mo separator="true">;</mo><mi>c</mi><mi>o</mi><mi>l</mi><mi>o</mi><mi>r</mi><mo>:</mo></mrow><annotation encoding="application/x-tex">body-bg;  color: </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">b</span><span class="mord mathnormal">o</span><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">b</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mpunct">;</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span></span></span></span>body-color;
&#125;</p>
<ul>
<li>
<p>yarn add sass  --dev</p>
</li>
<li>
<p>运行:
./node_modules/.bin/sass   scss/main.scss  css/style.css</p>
<ul>
<li>style.css</li>
<li>style.css.map</li>
</ul>
</li>
<li>
<p>NPM Scripts</p>
<ul>
<li>
<p>包装构建命令</p>
</li>
<li>
<p>package.json中增加scripts配置</p>
<ul>
<li>"scripts": &#123;</li>
</ul>
</li>
</ul>
<p>"build": "sass   scss/main.scss  css/style.css  --watch",
// "preserve": "yarn build", // NPM Scripts 的钩子机制
"serve": "browser-sync  .  --files "css/*.css"",
"start": "run-p  build  serve",</p>
</li>
</ul>
<p>&#125;</p>
<pre><code class="copyable">- yarn  build
- yarn  serve
- yarn start

- 是实现自动化构建工作流的最简方式
- yarn add browser-sync  --dev

- 用于启动一个测试服务器来运行项目。

- yarn add npm-run-all  --dev

- 同时运行多个任务

- 面对相对复杂的构建过程，就显得有些吃力了。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">常用的自动化构建工具</h3>
<ul>
<li>
<p>Grunt</p>
<ul>
<li>
<p>简介</p>
<ul>
<li>
<p>最早的前端构建系统</p>
</li>
<li>
<p>插件生态非常完善</p>
<ul>
<li>其插件几乎可以帮你自动化完成任何你想完成的事情。</li>
</ul>
</li>
<li>
<p>缺点</p>
<ul>
<li>
<p>工作过程是基于临时文件去实现的，所以说构建速度相应较慢。</p>
</li>
<li>
<p>例如去完成sass文件的构建</p>
<ul>
<li>先对sass文件做编译操作</li>
<li>再自动添加一些私有属性的前缀。</li>
<li>之后再压缩代码</li>
<li>在这些过程中Grunt每一步都有磁盘操作。</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>基本使用</p>
<ul>
<li>
<p>初始化package.json文件</p>
<ul>
<li>yarn  init --yes</li>
</ul>
</li>
<li>
<p>添加grunt模块</p>
<ul>
<li>yarn  add  grunt</li>
</ul>
</li>
<li>
<p>添加gruntfile.js的文件</p>
<ul>
<li>
<p>code  gruntfile.js</p>
<ul>
<li>
<p>Grunt的入口文件</p>
</li>
<li>
<p>用于定义一些需要 Grunt  自动执行的任务</p>
</li>
<li>
<p>需要导出一个函数</p>
</li>
<li>
<p>此函数接收一个 grunt 的形参</p>
</li>
<li>
<p>grunt是一个对象，内部提供一些创建任务时用到的 API</p>
</li>
<li>
<p>上代码</p>
<ul>
<li>module.exports  =  grunt ⥤  &#123;</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>grunt.registerTask('taskName', () ⥤ &#123;
console.log('sjz')
&#125;)</p>
<p>grunt.registerTask('taskName1', '任务描述', () ⥤ &#123;
console.log('sjz515')
&#125;)</p>
<p>// grunt.registerTask('default', '默认任务描述', () ⥤ &#123;
// console.log('sjz515')
// &#125;)</p>
<p>grunt.registerTask('default', ['taskName', 'taskName1'])</p>
<p>grunt.registerTask('async-task', () ⥤ &#123;
setTimeout(()⥤&#123;
console.log('sjz515')
&#125;, 1000)
&#125;)</p>
<p>grunt.registerTask('async-task1', function () &#123;
const done = this.async()
setTimeout(()⥤&#123;
console.log('sjz515')
done()
&#125;, 1000)
&#125;)</p>
</li>
</ul>
<p>&#125;</p>
<pre><code class="copyable">- yarn grunt taskName
- yarn grunt taskName1
- 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>yarn grunt</p>
<pre><code class="copyable">- 默认任务不需要指定

- yarn grunt async-task

- grunt默认支持同步模式
- 异步任务中console.log未执行。

- yarn grunt async-task1

- 可以成功执行

- 标记任务失败

- module.exports  =  grunt ⥤  &#123;
 grunt.registerTask('bad', () ⥤ &#123;
     console.log('sjz')
     return false
 &#125;)

 grunt.registerTask('async-task1', function () &#123;
     const done = this.async()
     setTimeout(()⥤&#123;
          console.log('sjz515')
          done(false)
      &#125;, 1000)
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- 一旦任务失败，后续任务将不会执行
- 可以通过指定--force参数控制即使某个任务执行失败，后续任务依然会保证执行

- Grunt 配置选项方法

- module.exports  =  grunt ⥤  &#123;
 grunt.initConfig(&#123;
     taskName: 'sjz',
     foo: &#123;
         bar: 'sjz'
     &#125;
 &#125;)
 grunt.registerTask('taskName', () ⥤ &#123;
     console.log(grunt.config('taskName'))
 &#125;)
 grunt.registerTask('foo', () ⥤ &#123;
     console.log(grunt.config('foo.bar'))
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- yarn grunt taskName
- yarn grunt foo

- Grunt多目标任务

- 多目标模式，可以任务根据配置形成多个子任务。
- module.exports  =  grunt ⥤  &#123;
 grunt.initConfig(&#123;
     build: &#123;
         options: &#123;
             foo: 'bar'
         &#125;,
         css: &#123;
            options: &#123;
                foo: 'baz'
            &#125;
         &#125;,
         js: '2'
     &#125;
 &#125;)
 grunt.registerMultiTask('build', function() &#123;
     console.log('multi task~')
     console.log(`target: $&#123;this.target&#125;, data:$&#123;this.data&#125;, options: $&#123;this.options()&#125;`)
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- yarn grunt build
- yarn grunt build:css

- Grunt插件的使用

- module.exports  =  grunt ⥤  &#123;
 grunt.initConfig(&#123;
     clean: &#123;
         temp: 'temp/*.js',
         temp1: 'temp/**',
     &#125;
 &#125;)
grunt.loadNpmTasks('grunt-contrib-clean')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- yarn grunt clean

- yarn add grunt-contrib-clean

- 实现常用的构建任务

- yarn add grunt-sass sass  --dev
- const sass = require('sass')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const loadGruntTask = require('load-grunt-tasks')
module.exports  =  grunt ⥤  &#123;
grunt.initConfig(&#123;
sass: &#123;
options: &#123;
sourceMap: true,
implementation: sass
&#125;,
main: &#123;
files: &#123;
'dist/css/main.css': 'src/scss/main.scss'
&#125;
&#125;
&#125;,
babel: &#123;
options: &#123;
sourceMap: true,
presets: ['@babel/preset-env']
&#125;,
main: &#123;
files: &#123;
'dist/js/app.js': 'src/js/app.js'
&#125;
&#125;
&#125;,
watch: &#123;
js: &#123;
files: [''src/is/<em>.js],
tasks: ['babel']
&#125;, &#123;
css: &#123;
files: [''src/scss/</em>.scss],
tasks: ['sass']
&#125;
&#125;
&#125;)
//   grunt.loadNpmTasks('grunt-sass')
loadGruntTasks(grunt) // 自动加载所有的grunt插件中的任务</p>
<pre><code class="copyable"> grunt.registerTask('default', ['sass', 'babel', 'watch'])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- yarn grunt sass
- yarn grunt babel
- yarn grunt watch
- yarn grunt

- yarn add grunt-babel  @babel/core @babel/preset-env   --dev
- yarn add load-grunt-tasks  --dev
- yarn add grunt-contrib-watch   --dev

- 基本已经退出历史舞台
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>Gulp</p>
<ul>
<li>
<p>简介</p>
<ul>
<li>推荐使用</li>
<li>很好的解决了Grunt构建慢的问题</li>
<li>每个环节都是在内存中完成。</li>
<li>默认支持同时执行多个任务。</li>
<li>使用方式相对于Grunt更加直观易懂。</li>
<li>插件生态也非常完善。</li>
<li>后来居上</li>
<li>目前市面上最流行的前端构建系统</li>
</ul>
</li>
<li>
<p>基本使用</p>
<ul>
<li>
<p>核心特点: 高效、易用</p>
</li>
<li>
<p>yarn init --yes</p>
<ul>
<li>初始化package.json文件</li>
</ul>
</li>
<li>
<p>安装Gulp模块</p>
<ul>
<li>
<p>yarn add gulp --dev</p>
<ul>
<li>会同时安装gulp-cli模块</li>
</ul>
</li>
</ul>
</li>
<li>
<p>创建gulpfile.js文件</p>
<ul>
<li>
<p>code gulpfile.js</p>
<ul>
<li>gulp的入口文件</li>
<li>通过导出成员函数的方式定义任务</li>
</ul>
</li>
</ul>
</li>
<li>
<p>在最新的Gulp中去掉了同步代码模式，约定每个任务都必须是异步任务。</p>
</li>
</ul>
</li>
<li>
<p>上代码</p>
<ul>
<li>
<p>gulpfile.js</p>
<ul>
<li>exports.foo = done ⥤ &#123;</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>console.log('sjz')
done() // 标识任务完成</p>
</li>
</ul>
<p>&#125;</p>
<pre><code class="copyable">- yarn gulp foo

- exports.default = done ⥤ &#123;
console.log('default sjz')
done() // 标识任务完成
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- yarn  gulp

- gulp4.0以前

- const gulp =  require('gulp')
- gulp.task('bar',  done ⥤&#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>console.log('bar')
done()
&#125;)</p>
<pre><code class="copyable">- yarn gulp bar

- Gulp创建组合任务

- const &#123;series, parallel&#125; = require ('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.task1 = done ⥤ &#123;
setTimeout(()⥤&#123;
console.log('sjz1')
done() // 标识任务完成
&#125;, 1000)</p>
<p>exports.task2 = done ⥤ &#123;
setTimeout(()⥤&#123;
console.log('sjz2')
done() // 标识任务完成
&#125;, 1000)</p>
<p>exports.task3 = done ⥤ &#123;
setTimeout(()⥤&#123;
console.log('sjz3')
done() // 标识任务完成
&#125;, 1000)
&#125;</p>
<p>exports.foo = series(task1, task2, task3)
exports.bar = parallel(task1, task2, task3)</p>
<pre><code class="copyable">- yarn gulp foo
- yarn gulp bar

- Gulp异步任务的三种方式

- exports.callback = done ⥤ &#123;
console.log('sjz callback')
done() // 标识任务完成
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>exports.callback_error = done ⥤ &#123;
console.log('sjz callback_error')
done(new Error('task failed')) // 标识任务完成
&#125;</p>
<pre><code class="copyable">- yarn gulp callback
- yarn gulp callback_error

- exports.promise = done ⥤ &#123;
console.log('sjz promise')
return Promise.resolve()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>exports.promise_error = done ⥤ &#123;
console.log('sjz Promise error')
return Promise.reject(new Error('task failed'))
&#125;</p>
<pre><code class="copyable">- yarn gulp promise
- yarn gulp promise_error

- const timeout = time ⥤ &#123;
return new Promise(resolve ⥤ &#123;
     setTimeout(resolve, time)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
exports.async = async () ⥤ &#123;
console.log('async task')
await timeout(1000)
&#125;</p>
<pre><code class="copyable">- yarn gulp async

- const fs = require('fs')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.stream = () ⥤ &#123;
console.log('sjz stream')
const readStream = fs.createReadStream('package.json')
const writeStream = fs.createReadStream('package.json')
return
&#125;
exports.stream1 = done ⥤ &#123;
console.log('sjz stream1')
const readStream = fs.createReadStream('package.json')
const writeStream = fs.createWriteStream('temp.txt')
readStream.pipe(writeStream)
readStream.on('end', () ⥤ &#123;
done()
&#125;)
&#125;</p>
<pre><code class="copyable">- yarn gulp stream

- Gulp构建过程核心工作原理

- const fs = require('fs')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const &#123;&#125; = require('stream')</p>
<p>exports.default = () ⥤ &#123;
// 文件读取流
const read = fs.createReadStream('normalize.css')
// 文件写入流
const write = fs.createWriteStream('normalize.min.css')
// 转换流
const transform = new Transform(&#123;
transform: (chunk, encoding, callback) ⥤ &#123;
// 核心转换过程实现
// chunk ⥤ 读取流中读取到的内容 (Buffer)
const input = chunk.toString()
input.replace(/\s+/g, '').replace(//*.+?*//g, '')
callback(null, input)
&#125;
&#125;)
// 把读取出来的文件流导入写入文件流
read
.pipe(transform) // 转换
.pipe(write) // 写入
return read
&#125;</p>
<pre><code class="copyable">- yarn gulp

- the streaming build system

- Gulp希望实现构建管道的概念

- Gulp文件操作API + 插件的使用

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const cleanCss = require('gulp-clean-css')
const rename = require('gulp-rename')
exports.default = () ⥤&#123;
return src('src/*.css')
.pipe(cleanCss())
.pipe(rename(&#123; extname: '.min.css' &#125;))
.pipe(dest('dist'))
&#125;</p>
<pre><code class="copyable">- yarn gulp

- yarn add gulp-clean-css --dev
- yarn add gulp-rename --dev

- Gulp自动化构建案例

- 准备需要构建工作流的网页应用案例

- git clone https://github.com/zce/zce-gulp-demo

- 用vscode打开目录

- code zce-gulp-demo/

- 网页应用案例目录剖析

- public目录

- 存放那些不需要被加工且会被直接拷贝到生成文件夹的文件

- src目录

- 存放开发阶段所编写代码的
- 此文件夹目录下所有文件都将被构建。
- 此目录下文件都会被转换生成到生成文件夹中

- yarn add gulp --dev
- 新建gulpfile.js文件作为入口文件

- 样式编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const sass = require('gulp-sass')
exports.style =() ⥤ &#123;
return src('src/assets/styles/*.scss', &#123; base: 'src' &#125; )
.pipe(sass(&#123; outputStyle: 'expanded' &#125;))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
style
&#125;</p>
<pre><code class="copyable">- yarn gulp style

- yarn add gulp-sass --dev

- 脚本文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const babel = require('gulp-babel')
exports.script = () ⥤ &#123;
return src('src/assets/scripts/*.js', &#123; base: 'src' &#125; )
.pipe(babel(&#123; presets: ['@babel/preset-env'] &#125;))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
script
&#125;</p>
<pre><code class="copyable">- yarn gulp script

- yarn add gulp-babel --dev
- yarn add @babel/core @babel/preset-env --dev

- 页面文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const swig = require('gulp-swig')</p>
<p>const data = &#123;
menus: [],
pkg: require('package.json'),
date: new Date()
&#125;</p>
<p>exports.page = () ⥤ &#123;
return src('src/*.html', &#123; base: 'src' &#125; )
.pipe(swig(&#123; data &#125;))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
page
&#125;</p>
<pre><code class="copyable">- yarn gulp page

- 安装模板引擎

- yarn add gulp-swig --dev

- 图片和字体文件的转换

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const imagemin = require('gulp-imagemin')
exports.image = () ⥤ &#123;
return src('src/assets/images/<strong>', &#123; base: 'src' &#125; )
.pipe(imagemin())
.pipe(dest('dist'))
&#125;
exports.font = () ⥤ &#123;
return src('src/assets/fonts/</strong>', &#123; base: 'src' &#125; )
.pipe(imagemin())
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
image,
font
&#125;</p>
<pre><code class="copyable">- yarn gulp image
- yarn gulp font

- yarn add gulp-imagemin --dev

- 其他文件及文件清除

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.extra = () ⥤ &#123;
return src('public/**', &#123; base: 'public' &#125; )
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
extra
&#125;</p>
<pre><code class="copyable">- 自动加载插件

- yarn add gulp-load-plugins --dev
- const loadPlugins = require('gulp-load-plugins')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const plugins = loadPlugins()
- 替换</p>
<pre><code class="copyable">- 样式编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.style =() ⥤ &#123;
return src('src/assets/styles/*.scss', &#123; base: 'src' &#125; )
.pipe(plugins.sass(&#123; outputStyle: 'expanded' &#125;))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
style
&#125;</p>
<pre><code class="copyable">- yarn gulp style

- yarn add gulp-sass --dev

- 脚本文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.script = () ⥤ &#123;
return src('src/assets/scripts/*.js', &#123; base: 'src' &#125; )
.pipe(plugins.babel(&#123; presets: ['@babel/preset-env'] &#125;))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
script
&#125;</p>
<pre><code class="copyable">- yarn gulp script

- yarn add gulp-babel --dev
- yarn add @babel/core @babel/preset-env --dev

- 页面文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const data = &#123;
menus: [],
pkg: require('package.json'),
date: new Date()
&#125;</p>
<p>exports.page = () ⥤ &#123;
return src('src/*.html', &#123; base: 'src' &#125; )
.pipe(plugins.swig(&#123; data &#125;))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
page
&#125;</p>
<pre><code class="copyable">- yarn gulp page

- 安装模板引擎

- yarn add gulp-swig --dev

- 图片和字体文件的转换

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.image = () ⥤ &#123;
return src('src/assets/images/<strong>', &#123; base: 'src' &#125; )
.pipe(plugins.imagemin())
.pipe(dest('dist'))
&#125;
exports.font = () ⥤ &#123;
return src('src/assets/fonts/</strong>', &#123; base: 'src' &#125; )
.pipe(plugins.imagemin())
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
image,
font
&#125;</p>
<pre><code class="copyable">- yarn gulp image
- yarn gulp font

- yarn add gulp-imagemin --dev

- 热更新开发服务器

- yarn add browser-sync --dev
- const browserSync = require('browser-sync')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const bs = browserSync.create()
exports.serve = () ⥤ &#123;
bs.init(&#123;
notify: false,
port: 2080,
files: 'dist/**',
open: true,
server: &#123;
baseDir: 'dist',
routes: &#123;
'/node_modules': 'node_modules'
&#125;
&#125;
&#125;)
&#125;</p>
<p>module.exports = &#123;
serve
&#125;</p>
<pre><code class="copyable">- yarn gulp serve

- 监视变化以及构建过程变化

- const &#123; src, dest, parallel, series, watch &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const browserSync = require('browser-sync')
const bs = browserSync.create()
exports.serve = () ⥤ &#123;
watch('src/assets/styles/<em>.scss', style)
watch('src/assets/scripts/</em>.js', script)
watch('src/*.html', page)</p>
<pre><code class="copyable">// 以下监听开发时无意义，需注释掉
// watch('src/assets/images/**', image)
// watch('src/assets/fonts/**', font)
// watch('public/**', extra)
watch([
     'src/assets/images/**',
     'src/assets/fonts/**',
     'public/**'
], bs.reload)
bs.init(&#123;
    notify: false,
    port: 2080,
    files: 'dist/**',
    open: true,
    server: &#123;
        baseDir: ['dist', 'src', 'public'],
        routes: &#123;
           '/node_modules': 'node_modules'
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>module.exports = &#123;
clean,
serve
&#125;</p>
<pre><code class="copyable">- yarn gulp clean
- yarn gulp serve

- 问题

- 这里可能会因为swig模板引擎缓存的机制导致页面不会变化，此时需要额外将swig选项中的cache设置为false, 具体参考源代码72行

- 组合任务

- 编译任务

- const &#123; src, dest, parallel &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const compile = parallel(style, script, page, image, font)
module.exports = &#123;
compile
&#125;</p>
<pre><code class="copyable">- yarn gulp compile

- 构建任务

- 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const &#123; src, dest, parallel, series &#125; = require('gulp')
const del = require('del')
const clean = () ⥤ &#123;
return del(['dist'])
&#125;
const compile = parallel(style, script, page)
// 上线之前执行的任务
const build = series(clean, parallel(compile, image, font, extra))
module.exports = &#123;
build,
clean,
develop
&#125;</p>
<pre><code class="copyable">- yarn gulp build
- yarn gulp clean

- yarn add del --dev

- 开发任务

- const develop = series(compile, serve)

- yarn gulp develop

- be.reload

- 样式编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.style =() ⥤ &#123;
return src('src/assets/styles/*.scss', &#123; base: 'src' &#125; )
.pipe(plugins.sass(&#123; outputStyle: 'expanded' &#125;))
.pipe(dest('dist'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
style
&#125;</p>
<pre><code class="copyable">- yarn gulp style

- yarn add gulp-sass --dev

- 脚本文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.script = () ⥤ &#123;
return src('src/assets/scripts/*.js', &#123; base: 'src' &#125; )
.pipe(plugins.babel(&#123; presets: ['@babel/preset-env'] &#125;))
.pipe(dest('dist'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
script
&#125;</p>
<pre><code class="copyable">- yarn gulp script

- yarn add gulp-babel --dev
- yarn add @babel/core @babel/preset-env --dev

- 页面文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const data = &#123;
menus: [],
pkg: require('package.json'),
date: new Date()
&#125;</p>
<p>exports.page = () ⥤ &#123;
return src('src/*.html', &#123; base: 'src' &#125; )
.pipe(plugins.swig(&#123; data &#125;))
.pipe(dest('dist'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
page
&#125;</p>
<pre><code class="copyable">- yarn gulp page

- 安装模板引擎

- yarn add gulp-swig --dev

- const &#123; src, dest, parallel, series, watch &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const browserSync = require('browser-sync')
const bs = browserSync.create()
exports.serve = () ⥤ &#123;
watch('src/assets/styles/<em>.scss', style)
watch('src/assets/scripts/</em>.js', script)
watch('src/*.html', page)</p>
<pre><code class="copyable">// 以下监听开发时无意义，需注释掉
// watch('src/assets/images/**', image)
// watch('src/assets/fonts/**', font)
// watch('public/**', extra)
watch([
     'src/assets/images/**',
     'src/assets/fonts/**',
     'public/**'
], bs.reload)
bs.init(&#123;
    notify: false,
    port: 2080,
    // files: 'dist/**',
    open: true,
    server: &#123;
        baseDir: ['dist', 'src', 'public'],
        routes: &#123;
           '/node_modules': 'node_modules'
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>const develop = series(compile, serve)</p>
<p>module.exports = &#123;
clean,
serve,
develop
&#125;</p>
<pre><code class="copyable">- yarn gulp develop

- useref文件引用处理

- yarn gulp build
- yarn add gulp-useref --dev
- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.useref = () ⥤ &#123;
return src('dist/*.html', &#123; base: 'dist' &#125; )
.pipe(plugins.useref(&#123; searchPath: ['dist', '.'] &#125;))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
useref
&#125;</p>
<pre><code class="copyable">- yarn gulp useref

- 分别压缩HTML、CSS、JS

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.useref = () ⥤ &#123;
return src('dist/*.html', &#123; base: 'dist' &#125; )
.pipe(plugins.useref(&#123; searchPath: ['dist', '.'] &#125;))
// html,js,css
.pipe(plugins.if(/.js<span class="math math-inline"><span class="katex-error" title="ParseError: KaTeX parse error: Can't use function '\.' in math mode at position 42: …pe(plugins.if(/\̲.̲css" style="color:#cc0000">/, plugins.uglify()))  .pipe(plugins.if(/\.css</span></span>/, plugins.cleanCss()))
.pipe(plugins.if(/.html$/, plugins.htmlmin(&#123;
collapseWhitespace: true,
minifyCSS: true,
minifyJS: true,
&#125;)))
.pipe(dest('release'))
&#125;</p>
<p>module.exports = &#123;
useref
&#125;</p>
<pre><code class="copyable">- yarn gulp compile
- yarn gulp useref

- yarn add gulp-htmlmin gulp-uglify gulp-clean-css --dev
- yarn add gulp-if --dev

- 重新规划构建过程

- clean

- 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const &#123; src, dest, parallel, series &#125; = require('gulp')
const del = require('del')
const clean = () ⥤ &#123;
return del(['dist', 'temp'])
&#125;
const compile = parallel(style, script, page)
// 上线之前执行的任务
const build = series(clean, parallel(compile, image, font, extra))
module.exports = &#123;
build,
clean,
develop
&#125;</p>
<pre><code class="copyable">- 样式编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.style =() ⥤ &#123;
return src('src/assets/styles/*.scss', &#123; base: 'src' &#125; )
.pipe(plugins.sass(&#123; outputStyle: 'expanded' &#125;))
.pipe(dest('temp'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
style
&#125;</p>
<pre><code class="copyable">- yarn gulp style

- yarn add gulp-sass --dev

- 脚本文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.script = () ⥤ &#123;
return src('src/assets/scripts/*.js', &#123; base: 'src' &#125; )
.pipe(plugins.babel(&#123; presets: ['@babel/preset-env'] &#125;))
.pipe(dest('temp'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
script
&#125;</p>
<pre><code class="copyable">- yarn gulp script

- yarn add gulp-babel --dev
- yarn add @babel/core @babel/preset-env --dev

- 页面文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const data = &#123;
menus: [],
pkg: require('package.json'),
date: new Date()
&#125;</p>
<p>exports.page = () ⥤ &#123;
return src('src/*.html', &#123; base: 'src' &#125; )
.pipe(plugins.swig(&#123; data &#125;))
.pipe(dest('temp'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
page
&#125;</p>
<pre><code class="copyable">- yarn gulp page

- 安装模板引擎

- yarn add gulp-swig --dev

- serve

- const &#123; src, dest, parallel, series, watch &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const browserSync = require('browser-sync')
const bs = browserSync.create()
exports.serve = () ⥤ &#123;
watch('src/assets/styles/<em>.scss', style)
watch('src/assets/scripts/</em>.js', script)
watch('src/*.html', page)</p>
<pre><code class="copyable">// 以下监听开发时无意义，需注释掉
// watch('src/assets/images/**', image)
// watch('src/assets/fonts/**', font)
// watch('public/**', extra)
watch([
     'src/assets/images/**',
     'src/assets/fonts/**',
     'public/**'
], bs.reload)
bs.init(&#123;
    notify: false,
    port: 2080,
    // files: 'dist/**',
    open: true,
    server: &#123;
        baseDir: ['temp', 'src', 'public'],
        routes: &#123;
           '/node_modules': 'node_modules'
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>const develop = series(compile, serve)</p>
<p>module.exports = &#123;
clean,
serve,
develop
&#125;</p>
<pre><code class="copyable">- useref

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.useref = () ⥤ &#123;
return src('temp/*.html', &#123; base: 'temp' &#125; )
.pipe(plugins.useref(&#123; searchPath: ['temp', '.'] &#125;))
// html,js,css
.pipe(plugins.if(/.js<span class="math math-inline"><span class="katex-error" title="ParseError: KaTeX parse error: Can't use function '\.' in math mode at position 42: …pe(plugins.if(/\̲.̲css" style="color:#cc0000">/, plugins.uglify()))  .pipe(plugins.if(/\.css</span></span>/, plugins.cleanCss()))
.pipe(plugins.if(/.html$/, plugins.htmlmin(&#123;
collapseWhitespace: true,
minifyCSS: true,
minifyJS: true,
&#125;)))
.pipe(dest('dist'))
&#125;</p>
<p>module.exports = &#123;
useref
&#125;</p>
<pre><code class="copyable">- 组合任务

- const build = series(clean, parallel(series(compile, useref), image, font, extra)

- yarn gulp build
- yarn gulp develop

- 补充

- 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module.exports = &#123;
clean,
build,
develop
&#125;
- package.json中添加scripts属性</p>
<pre><code class="copyable">- "scripts": &#123;
"clean": "gulp clean",
"build": "gulp build",
"develop": "gulp develop",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- yarn clean
- yarn build
- yarn develop

- .gitignore中忽略文件

- dist
- temp

- 如何提取多个项目中共同的自动化构建过程？

- 封装自动化构建工作流

- 准备

- 思路: Gulpfile + Gulp = 构建工作流
- Gulpfile + Gulp CLI ⥤  zce-pages
- 新建仓库zce-pages
- cd  ..
- 安装应用脚手架

- yarn global add zce-cli
- 使用

- zce init nm zce-pages

- cd zce-pages
- git init
- git remote add origin 远程仓库地址
- git status
- git add  .
- git commit -m "feat: initial commit"
- git push -u origin master

- 提取Gulpfile到模块

- code  .  -a
- 把zce-gulp-demo下gulpfile.js中内容全部拷贝到zce-pages目录下的lib/index.js中。
- 把zce-gulp-demo下package.json中的开发依赖全部拷贝到zce-pages目录下的package.json中作为项目依赖。
- zce-pages目录下安装依赖

- yarn

- 删除zce-gulp-demo下gulpfile.js中内容
- 删除zce-gulp-demo下package.json中的开发依赖
- 删除zce-gulp-demo下node_modules文件夹
- 在zce-gulp-demo中使用zce-pages

- 在zce-pages中使用yarn link
- yarn link "zce-pages"
- 修改gulpfile.js文件

- 删除所有内容
- 添加: module.exports = require ('zce-pages')

- yarn
- yarn build

- 报错: gulp不是内部命令

- yarn add gulp-cli --dev
- yarn build

- 报错: Local gulp not found

- yarn add gulp --dev
- yarn build

- 报错: Cannot find module './package.json'

- 解决模块中的问题

- 在zce-gulp-demo中新建pages.config.js文件

- module.exports = &#123;
 data: &#123;
     menus: [],
     pkg: require('package.json'),
     date: new Date()
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- 修改lib/index.js文件

- 页面文件编译任务

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const cwd = process.cwd()
let config = &#123;
// default config
&#125;</p>
<p>try &#123;
const loadConfg = require(<code>$&#123;cwd&#125;/pages.config.js</code>)
config = Object.assign(&#123;&#125;, config, loadConfig)
&#125; catch(e) &#123;&#125;</p>
<p>exports.page = () ⥤ &#123;
return src('src/*.html', &#123; base: 'src' &#125; )
.pipe(plugins.swig(&#123; data: config.data &#125;))
.pipe(dest('temp'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
page
&#125;</p>
<pre><code class="copyable">- yarn gulp page
- yarn build

- Cannot find module '@babel/preset-env'
- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.script = () ⥤ &#123;
return src('src/assets/scripts/*.js', &#123; base: 'src' &#125; )
.pipe(plugins.babel(&#123; presets: [require('@babel/preset-env')] &#125;))
.pipe(dest('temp'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
script
&#125;</p>
<pre><code class="copyable">- yarn build

- 抽象路径配置

- 修改lib/index.js

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const cwd = process.cwd()
let config = &#123;
// default config
build: &#123;
src: 'src',
dist: 'dist',
temp: 'temp',
public: 'public',
paths: &#123;
styles: 'assets/styles/<em>.scss',
scripts: 'assets/scripts/</em>.js',
pages: '<em>.html',
images: 'assets/images/<strong>',
fonts: 'assets/fonts/</strong>',
styles: 'assets/styles/</em>.scss',
&#125;,
&#125;
&#125;</p>
<p>try &#123;
const loadConfg = require(<code>$&#123;cwd&#125;/pages.config.js</code>)
config = Object.assign(&#123;&#125;, config, loadConfig)
&#125; catch(e) &#123;&#125;</p>
<p>exports.page = () ⥤ &#123;
return src('src/*.html', &#123; base: 'src' &#125; )
.pipe(plugins.swig(&#123; data: config.data &#125;))
.pipe(dest('temp'))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
page
&#125;
- 更换写死的常量</p>
<pre><code class="copyable">- clean

- 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const &#123; src, dest, parallel, series &#125; = require('gulp')
const del = require('del')
const clean = () ⥤ &#123;
return del(config.build.dist, config.build.temp])
&#125;
const compile = parallel(style, script, page)
// 上线之前执行的任务
const build = series(clean, parallel(compile, image, font, extra))
module.exports = &#123;
build,
clean,
develop
&#125;</p>
<pre><code class="copyable">- style

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.style =() ⥤ &#123;
return src(config.build.paths.styles, &#123; base: config.build.src, cwd: config.build.src &#125; )
.pipe(plugins.sass(&#123; outputStyle: 'expanded' &#125;))
.pipe(dest(config.build.temp))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
style
&#125;</p>
<pre><code class="copyable">- script

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.script = () ⥤ &#123;
return src(config.build.paths.scripts, &#123; base: config.build.src, cwd: config.build.src &#125;)
.pipe(plugins.babel(&#123; presets: [require('@babel/preset-env')] &#125;))
.pipe(dest(config.build.temp))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
script
&#125;</p>
<pre><code class="copyable">- page

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const cwd = process.cwd()
let config = &#123;
// default config
&#125;</p>
<p>try &#123;
const loadConfg = require(<code>$&#123;cwd&#125;/pages.config.js</code>)
config = Object.assign(&#123;&#125;, config, loadConfig)
&#125; catch(e) &#123;&#125;</p>
<p>exports.page = () ⥤ &#123;
return src(config.build.paths.pages, &#123; base: config.build.src, cwd: config.build.src &#125; )
.pipe(plugins.swig(&#123; data: config.data &#125;))
.pipe(dest(config.build.temp))
.pipe(bs.reload(&#123; stream: true &#125;))
&#125;</p>
<p>module.exports = &#123;
page
&#125;</p>
<pre><code class="copyable">- image/font

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const imagemin = require('gulp-imagemin')
exports.image = () ⥤ &#123;
return src(config.build.paths.images, &#123; base: config.build.src, cwd: config.build.src &#125;  )
.pipe(imagemin())
.pipe(dest(config.build.dist))
&#125;
exports.font = () ⥤ &#123;
return src(config.build.paths.fonts, &#123; base: config.build.src, cwd: config.build.src &#125;  )
.pipe(imagemin())
.pipe(dest(config.build.dist))
&#125;</p>
<p>module.exports = &#123;
image,
font
&#125;</p>
<pre><code class="copyable">- extra

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.extra = () ⥤ &#123;
return src('**', &#123; base: config.build.public &#125; )
.pipe(dest(config.build.dist))
&#125;</p>
<p>module.exports = &#123;
extra
&#125;</p>
<pre><code class="copyable">- serve

- const &#123; src, dest, parallel, series, watch &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const browserSync = require('browser-sync')
const bs = browserSync.create()
exports.serve = () ⥤ &#123;
watch(config.build.paths.styles, &#123; cwd: config.build.src &#125;, style)
watch(config.build.paths.scripts, &#123; cwd: config.build.src &#125;, script)
watch(config.build.paths.pages, &#123; cwd: config.build.src &#125;, page)</p>
<pre><code class="copyable">// 以下监听开发时无意义，需注释掉
// watch('src/assets/images/**', image)
// watch('src/assets/fonts/**', font)
// watch('public/**', extra)
watch([
     config.build.paths.images,
     config.build.paths.fonts,
     // 'public/**'
], &#123; cwd: config.build.src &#125;, bs.reload)

watch([
     '**'
], &#123; cwd: config.build.public &#125;, bs.reload)
bs.init(&#123;
    notify: false,
    port: 2080,
    // files: 'dist/**',
    open: true,
    server: &#123;
        baseDir: [config.build.temp, config.build.src, config.build.public],
        routes: &#123;
           '/node_modules': 'node_modules'
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>const develop = series(compile, serve)</p>
<p>module.exports = &#123;
clean,
serve,
develop
&#125;</p>
<pre><code class="copyable">- useref

- const &#123; src, dest &#125; = require('gulp')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>exports.useref = () ⥤ &#123;
return src(config.build.paths.pages, &#123; base: config.build.temp, cwd: config.build.temp &#125; )
.pipe(plugins.useref(&#123; searchPath: [config.build.temp, '.'] &#125;))
// html,js,css
.pipe(plugins.if(/.js<span class="math math-inline"><span class="katex-error" title="ParseError: KaTeX parse error: Can't use function '\.' in math mode at position 42: …pe(plugins.if(/\̲.̲css" style="color:#cc0000">/, plugins.uglify()))  .pipe(plugins.if(/\.css</span></span>/, plugins.cleanCss()))
.pipe(plugins.if(/.html$/, plugins.htmlmin(&#123;
collapseWhitespace: true,
minifyCSS: true,
minifyJS: true,
&#125;)))
.pipe(dest(config.build.dist))
&#125;</p>
<p>module.exports = &#123;
useref
&#125;</p>
<pre><code class="copyable">- yarn build

- zce-gulp-demo下pages.config.js中增加配置

- module.exports = &#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>build: &#123;
src: 'src',
dist: 'release',
temp: '.tmp',
public: 'public',
paths: &#123;
styles: 'assets/styles/<em>.scss',
scripts: 'assets/scripts/</em>.js',
pages: '<em>.html',
images: 'assets/images/<strong>',
fonts: 'assets/fonts/</strong>',
styles: 'assets/styles/</em>.scss',
&#125;,
&#125;
data: &#123;
menus: [],
pkg: require('package.json'),
date: new Date()
&#125;
&#125;</p>
<pre><code class="copyable">- 包装Gulp CLI

- 删除zce-gulp-demo中的gulpfile.js文件

- yarn gulp

- No gulpfile found

- yarn gulp --gulpfile  ./node_modules/zce-pages/lib/index.js

- 问题: Task never defined: default

- yarn gulp build --gulpfile  ./node_modules/zce-pages/lib/index.js

- 问题: Working directory change to D:\zce\Desktop\zce-gulp-demo\node_modules\zce-pages\lib

- yarn gulp build --gulpfile  ./node_modules/zce-pages/lib/index.js  --cwd   .

- 可以正常运行，但传参复杂

- 在zce-pages目录下新建文件bin/zce-pages.js文件作为cli入口文件。

- 在zce-pages目录下的package.json文件中添加bin属性

- "bin": "bin/zce-pages.js"
- "bin": &#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>zp: "zce-pages"
&#125;</p>
<pre><code class="copyable">- 容易产生冲突

- 内容

- #!/usr/bin/env node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>console.log("zce/pages")
- 使用</p>
<pre><code class="copyable">- 1，yarn unlink
- 2，yarn link
- 可以直接zce-pages运行命令行文件bin/zce-pages.js。控制台输出: zce/pages

- 内容

- #!/usr/bin/env node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>require('gulp/bin/gulp')
- 使用</p>
<pre><code class="copyable">- 命令行运行: zce-pages

- 问题: No gulpfile found

- 内容

- #!/usr/bin/env node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>console.log(process.agv)
require('gulp/bin/gulp')
- 使用</p>
<pre><code class="copyable">- 命令行运行: zce-pages --sdfs  sdfs

- 结果: [
<span class="copy-code-btn">复制代码</span></code></pre>
<p>'C:\Develop\node\node',
'C:\Users\zce\AppData\Local\Yarn\Data\link\zce-pages\bin\zce-pages.js',
'--sdfs',
'sdfs'
]
- 问题: No gulpfile found</p>
<pre><code class="copyable">- 内容

- #!/usr/bin/env node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>process.agv.push('--cwd')
process.agv.push(process.cwd())
process.agv.push('--gulpfile')
process.agv.push(require.resolve('..'))
require('gulp/bin/gulp')
- 使用</p>
<pre><code class="copyable">- cd  ..
- cd  zce-gulp-demo
- zce-pages build

- Ok~

- 发布并使用模块

- 修改zce-pages目录下的package.json中的files属性

- "files": [
"bin",
"lib"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>]</p>
<pre><code class="copyable">- cd   ../
- cd zce-pages
- git add  .
- git commit -m "feat: update package"
- git push 
- yarn publish

- 问题: 淘宝镜像是只读镜像，直接发布会失败。

- yarn publish --registry https://registry.yranpkg.com
- 使用

- cd  ..
- mkdir zce-pages-demo
- cd zce-pages-demo
- Vscode打开

- code  .

- 拷贝zce-gulp-demo中的目录public/src/pages.config.js到zce-demo目录中
- 初始化package.json

- yarn init --yes

- yarn add zce-pages  --dev
- yarn zce-pages build
- 在package.json中添加scripts

- "scripts": &#123;
 "clean": "zce-pages clean",
 "build": "zce-pages build",
 "develop": "zce-pages develop",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<ul>
<li>
<p>FIS</p>
<ul>
<li>
<p>简介</p>
<ul>
<li>
<p>前端团队推出的一款构建系统。</p>
</li>
<li>
<p>最早只在他们内部项目中使用。</p>
</li>
<li>
<p>后来开源过后，在国内快速流行。</p>
</li>
<li>
<p>相对于Grunt/Gulp这种微内核特点的构建系统，FIS更像是一种捆绑套餐，它把在我们系统中一些典型的需求尽可能都集成到内部了。</p>
<ul>
<li>例如我们在FIS当中可以很轻松的处理像资源加载、模块化开发、代码部署，甚至是性能优化</li>
</ul>
</li>
<li>
<p>正因为大而全，所以在国内很多项目中就流行开了。</p>
</li>
</ul>
</li>
<li>
<p>FIS基本使用</p>
<ul>
<li>
<p>FIS的核心特点是高度集成</p>
<ul>
<li>把前端日常开发过程当中常见的构建任务和调试任务都集成到了内部。</li>
<li>开发者可以通过简单的配置文件的方式去配置我们构建过程中需要完成的工作</li>
<li>存在很多内置任务</li>
<li>内置了用于调试的web server，可以很方便的调试构建结果</li>
</ul>
</li>
<li>
<p>yarn global  add  fis3</p>
</li>
<li>
<p>用Vscode打开提前准备好的web应用</p>
<ul>
<li>code  fis-sample -r</li>
</ul>
</li>
<li>
<p>fis3 release</p>
<ul>
<li>自动构建项目到操作系统当前登录用户所在目录下的临时目录:.fis3-temp</li>
</ul>
</li>
<li>
<p>将构建结果放入当前目录</p>
<ul>
<li>
<p>fis3 release -d output</p>
<ul>
<li>只做了资源定位</li>
<li>未做代码转换</li>
</ul>
</li>
</ul>
</li>
<li>
<p>添加fis-conf.js文件</p>
<ul>
<li>
<p>内容</p>
<ul>
<li>fis.match('*.&#123;js, scss, png&#125;', &#123;</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>release: '/assets/$0'</p>
</li>
</ul>
<p>&#125;)</p>
<pre><code class="copyable">- fis

- 特殊的全局对象

- $0

- 表示当前文件的原始目录结构

- 编译与压缩

- fis.match('*.&#123;js, scss, png&#125;', &#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>release: '/assets/$0'
&#125;)</p>
<p>fis.match('**/*.scss', &#123;
rExt: '.css',
parser: fis.plugin('node-sass'),
optimized: fis.plugin('clean-css')
&#125;)</p>
<p>fis.match('**/*.js', &#123;
parser: fis.plugin('babel-6.x') ,
optimized: fis.plugin('uglify-js')
&#125;)</p>
<pre><code class="copyable">- fis3 release -d output
- fis3 inspect

- yarn global add fis-parser-node-sass
- yarn global add fis-parser-babel-6.x
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>小结</p>
<ul>
<li>
<p>如果你是初学者，FIS更适合</p>
<ul>
<li>但是如果你的要求灵活多变的话，Gulp/Grunt应该是你更好的选择。</li>
</ul>
</li>
<li>
<p>新手是需要规则的，而老手呢一般都渴望自由。</p>
<ul>
<li>也是因为这个原因，像Grunt/Gulp这些小而美的工具才得以流行。</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><em>XMind - Trial Version</em></p></div>  
</div>
            