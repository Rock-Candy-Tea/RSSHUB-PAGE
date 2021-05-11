
---
title: 'vscode插件开发指南(一)-理论篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c935edf3608443b796602a8456f2ae19~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 03:49:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c935edf3608443b796602a8456f2ae19~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、vscode插件是什么，可以做什么</h3>
<p><code>VSCode</code> 全称 <code>Visual Studio Code</code>，是微软出的一款轻量级代码编辑器，免费、开源而且功能强大。它支持几乎所有主流的程序语言的语法高亮、智能代码补全、自定义热键、括号匹配、代码片段、代码对比 Diff、GIT 等特性，支持插件扩展，并针对网页开发和云端应用开发做了优化。软件跨平台支持 Win、Mac 以及 Linux。已经成了越来越多人会选择的代码编辑器。</p>
<p>而<code>vscode插件</code>其实就是类似于一个<code>npm</code>包的<code>vsix</code>文件，其可以实现的功能大概可以分为以下几类：</p>
<p>1）不受限的本地磁盘访问</p>
<p>2）自定义命令、快捷键、菜单</p>
<p>3）自定义跳转、自动补全、悬浮提示</p>
<p>4）自定义插件设置、自定义插件欢迎页</p>
<p>5）自定义WebView</p>
<p>6）自定义左侧功能面板</p>
<p>7）自定义颜色、图标主题</p>
<p>8）新增语言支持（代码高亮、语法解析、折叠、跳转、补全等）</p>
<p>9）Markdown增强</p>
<p>10）其他（比如状态栏修改、通知提示、编辑器控制、git源代码控制、任务定义、Language Server、Debug Adapter等等）</p>
<p>是不是感觉很有意思，当你了解其可以实现哪些功能后，说不定就会找到目前工作中可以提高效率的场景点，接下来我们就来看一下到底怎么来写一个插件。</p>
<h3 data-id="heading-1">二、手把手教你写一个插件</h3>
<h4 data-id="heading-2">2.1 搭建项目</h4>
<p>微软官方提供了脚手架，可以帮助你快速搭建一个项目</p>
<h5 data-id="heading-3">2.1.1 安装脚手架</h5>
<pre><code class="copyable">// 安装脚手架
npm install -g yo generator-code
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">2.2.2 使用脚手架创建项目</h5>
<pre><code class="copyable">// 创建项目
yo code
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.2.2.1 创建项目会开启一个交互命令行，会让你选择你想创建的插件类型，目前支持以下几种类型：</strong></p>
<p>1）<code>New Extension (TypeScript)</code> ：ts语法的项目，基础版，内置了hello world的命令</p>
<p>2） <code>New Extension (JavaScript) </code>: js语法的项目，基础版，内置了hello world的命令</p>
<p>3）<code>New Color Theme</code> ：主题项目，内置了主题，可用来自定义主题</p>
<p>4）<code>New Language Support</code>：语言支持项目，内置了语法支持配置，可用来支持特殊语言</p>
<p>5）<code>New Code Snippets</code>：代码片段项目，内置了代码片段配置，可用来配置代码片段，输入触发字符，快速生成代码片段</p>
<p>6）<code>New Keyma</code>p：快捷键项目，内置了快捷键配置，可用来自定义快捷键行为</p>
<p>7）<code>New Extension Pack</code>：插件集合项目，内置了插件集合配置，可用于定制插件集，达到快速安装一组插件</p>
<p>8）<code>New Language Pack (Localization)</code>：目前官方文档暂未查到localizations贡献的场景点，待补充</p>
<p><strong>2.2.2.2 接着依次录入插件名称、插件标识、插件描述、是否初始化为git仓库、是否需要webpack打包、使用包管理器（npm/yarn）</strong></p>
<p><strong>2.2.2.3 按照步骤配置后，则会创建好以插件标识(identifier)命名的项目文件夹，里面包含了初始化好的项目文件</strong></p>
<p><strong>2.2.3 以New Extension (TypeScript) 类型讲解一下项目架构</strong></p>
<pre><code class="hljs language-json copyable" lang="json">├── .eslintrc.json <span class="hljs-comment">// eslint配置</span>
├── .vscode <span class="hljs-comment">// vscode调试配置</span>
|  ├── extensions.json
|  ├── launch.json
|  ├── settings.json
|  └── tasks.json
├── .vscodeignore <span class="hljs-comment">// 发布忽略内容</span>
├── CHANGELOG.md <span class="hljs-comment">// 修改日志</span>
├── README.md <span class="hljs-comment">// 插件发布后，插件主页内容</span>
├── package-lock.json
├── package.json <span class="hljs-comment">// vscode从这里识别插件贡献点</span>
├── src <span class="hljs-comment">// 核心源码内容</span>
|  ├── extension.ts <span class="hljs-comment">// 入口文件</span>
|  └── test <span class="hljs-comment">//测试文件</span>
├── tsconfig.json <span class="hljs-comment">// ts配置文件</span>
├── vsc-extension-quickstart.md 
└── webpack.config.js <span class="hljs-comment">// wepack配置</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里面有几个核心的内容，重点展开讲一下</p>
<p><strong>1）<a href="https://code.visualstudio.com/api/references/extension-manifest" target="_blank" rel="nofollow noopener noreferrer">package.json</a></strong></p>
<blockquote>
<p>Every Visual Studio Code extension needs a manifest file package.json at the root of the extension directory structure</p>
</blockquote>
<p>其中最基本的字段：</p>





































<table><thead><tr><th>字段名</th><th>含义</th></tr></thead><tbody><tr><td>name</td><td>插件名（要求全小写，无空格）</td></tr><tr><td>version</td><td>插件版本（使用这个控制插件版本，类似npm）</td></tr><tr><td>publisher</td><td>发布者</td></tr><tr><td>engines</td><td>对vscode或其他环境依赖版本的要求</td></tr><tr><td>main</td><td>插件入口文件</td></tr><tr><td><a href="https://code.visualstudio.com/api/references/contribution-points" target="_blank" rel="nofollow noopener noreferrer">contributes</a></td><td>插件贡献点，基本上我们增加的功能点，都需要在这里显示声明，如注册的命令、注册的菜单、注册的快捷键</td></tr><tr><td><a href="https://code.visualstudio.com/api/references/activation-events" target="_blank" rel="nofollow noopener noreferrer">activationEvents</a></td><td>插件触发动作，如在打开某种语言的文件时、当某个命令被触发时</td></tr></tbody></table>
<p>这里面比较复杂的就是<code>contributes</code>以及<code>activationEvents</code>的配置，后面实战内容我会重点再实例。</p>
<p>这里以脚手架创建的项目先简单说明一下</p>
<pre><code class="copyable">  "activationEvents": [
    "onCommand:TypeScript.helloWorld" // 当触发TypeScript.helloWorld命令时启动插件
  ],
  "main": "./dist/extension.js", // 入口文件
  "contributes": &#123;
      "commands": [ // 注册命令
        &#123;
          "command": "TypeScript.helloWorld", // 命令唯一标识，命令名
          "title": "Hello World" // 命令在vcode中的展示标题
        &#125;
      ]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2）入口文件</strong></p>
<pre><code class="copyable">// ./dist/extension.js"
import * as vscode from 'vscode';
​
// 当插件被激活触发
export function activate(context: vscode.ExtensionContext) &#123;
​
  console.log('Congratulations, your extension "TypeScript" is now active!');
​
  // 调用vscode注册命令API，注册了一个名（命令唯一标识）为TypeScript.helloWorld的命令
  let disposable = vscode.commands.registerCommand('TypeScript.helloWorld', () => &#123;
    // 执行命令，会在右下角展示提示信息
    vscode.window.showInformationMessage('Hello World from TypeScript!');
  &#125;);
​
  context.subscriptions.push(disposable);
&#125;
​
// 当插件停用时触发
export function deactivate() &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3）效果</strong></p>
<p>按下<code>shift+command+p</code>，输入命令标题查询，并点击我们写的命令
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c935edf3608443b796602a8456f2ae19~tplv-k3u1fbpfcp-zoom-1.image" alt="命令效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>vscode右下角会展示提示信息
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51f82881a9004da5b184745cb3d0f976~tplv-k3u1fbpfcp-zoom-1.image" alt="展示效果" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">2.2 如何开发调试</h4>
<p>以上面<code>New Extension (TypeScript)</code> 类型举例，借由vscode自带的调试功能，脚手架已经自动为我们配置好了，也就是<code>.vscode</code>目录下的内容
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53a0a31fb9c349c68a904d4b9411f53c~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实际上，执行的<code>package.json</code>配置的<code>watch</code>命令</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"watch"</span>: <span class="hljs-string">"webpack --watch"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1）点击运行<code>Run Extension</code>后，会自动打开一个新的vscode界面，此时这个新打开的vscode，会自动安装我们开发的插件，vscode头部会展示<code>[Extension Development Host]</code></p>
<p>2）此时我们在这个界面调试插件功能，如果需要测试代码，我们可以在此vscode新建一个本地项目或者打开已有项目测试</p>
<p>3）我们写的console相关日志，可以在<code>DEBUG CONSOLE</code>面板中查看，也可以在运行过程中增删断点，如下：
<img src="https://raw.githubusercontent.com/tongyuchan/pub/master/img/809508710.png" alt="调试" loading="lazy" referrerpolicy="no-referrer"></p>
<p>4）如果修改了插件内容，<code>webpack</code>会自动监听并编译</p>
<p>5）打开的<code>[Extension Development Host]</code>的vscode调试页面如何更新修改呢？</p>
<ul>
<li>方法一：断开并重新执行</li>
<li>方法二：在此界面按住command+R，则会自动重启并应用，推荐</li>
</ul>
<h4 data-id="heading-6">2.3 如何发布、更新</h4>
<h5 data-id="heading-7">2.3.1 发布方式</h5>
<ul>
<li>方法一：直接把文件夹发给别人，让别人找到vscode的插件存放目录并放进去，然后重启vscode，一般不推荐；</li>
<li>方法二：打包成<code>vsix</code>插件，然后发送给别人安装，如果你的插件涉及机密不方便发布到应用市场，可以尝试采用这种方式；</li>
<li>方法三：注册开发者账号，发布到官网应用市场，这个发布和npm一样是不需要审核的。</li>
</ul>
<h5 data-id="heading-8">2.3.2 打包</h5>
<pre><code class="copyable">npm i vsce -g
// 打包成vsix文件，项目根目录下会生成一个vsix文件
vsce package
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">2.3.3 发布到应用市场</h5>
<p><strong>1）注册账号发布（这里可以详细阅读<a href="http://blog.haoji.me/vscode-plugin-publish.html" target="_blank" rel="nofollow noopener noreferrer">blog.haoji.me/vscode-plug…</a>）</strong></p>
<ul>
<li>首先访问 <a href="https://login.live.com/" target="_blank" rel="nofollow noopener noreferrer">login.live.com/</a>, 登录你的Microsoft账号，没有的先注册一个</li>
<li>然后访问： <a href="https://aka.ms/SignupAzureDevOps" target="_blank" rel="nofollow noopener noreferrer">aka.ms/SignupAzure…</a>， 点击继续，默认会创建一个以邮箱前缀为名的组织</li>
<li>创建令牌，这里需要注意的是创建令牌成功后你需要本地记下来，因为网站是不会帮你保存的</li>
<li>获得个人访问令牌后，使用<code>vsce</code>以下命令创建新的发布者</li>
</ul>
<pre><code class="copyable">vsce create-publisher your-publisher-name
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>发布</li>
</ul>
<pre><code class="copyable">// 发布
vsce publish
// 增量发布， 版本号：major.minor.patch
vsce publish patch
vsce publish minor
vsce publish major
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2）撤销发布</strong></p>
<p>需要注意的是，此操作并不会撤销某一版本的发布，而是直接删除插件，谨慎使用！</p>
<pre><code class="copyable">vsce unpublish (publisher name).(extension name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3）用户如何更新（从应用市场安装）</strong></p>
<p>vscode的插件是热更新的模式，用户安装过一次之后，会自动检测是否有新版本并安装，用户基本是无感知，这些检测时机包括：搜索插件、重启vscode等</p>
<p>如果插件发布更新后，vscode自动检测机制还未触发，可手动搜索插件一次或重启一下vscode，需要注意的是，插件更新之后如果想要生效，也是需要重启vscode的</p>
<h3 data-id="heading-10">三、参考资料</h3>
<ul>
<li><a href="https://code.visualstudio.com/api/references/vscode-api#commands" target="_blank" rel="nofollow noopener noreferrer">vscode官方API</a></li>
<li><a href="https://github.com/Liiked/VS-Code-Extension-Doc-ZH" target="_blank" rel="nofollow noopener noreferrer">翻译文档</a></li>
<li><a href="http://blog.haoji.me/vscode-plugin-overview.html" target="_blank" rel="nofollow noopener noreferrer">VSCode插件开发全攻略</a>: 这里重点推荐，小白入门神教程</li>
</ul></div>  
</div>
            