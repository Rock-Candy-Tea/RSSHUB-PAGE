
---
title: '掘金一下 _ 从零开发一款基于 webview 的 vscode 扩展'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4970b4e627a04fb7a94ff53906b204f8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 20:21:55 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4970b4e627a04fb7a94ff53906b204f8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4970b4e627a04fb7a94ff53906b204f8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<blockquote>
<p>大家好，我是<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning" ref="nofollow noopener noreferrer">洛竹</a>🎋，一只住在杭城的木系前端 🧚🏻‍♀️，如果你喜欢我的文章 📚，可以通过点赞帮我聚集灵力 ⭐️。</p>
</blockquote>
<blockquote>
<p>温馨提示：结合本文配套<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fjuejin-me" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/juejin-me" ref="nofollow noopener noreferrer">源码</a>阅读体验更佳！</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在团队降本提效的基建中，洛竹开发了一款 vscode 插件，第一版我使用的是 vscode 内置 UI，虽说也能用，但是用户体验欠佳。由于 vscode 内置 UI 不够灵活，一番调研后我决定使用 webview 重构。</p>
<p>开发过 vscode 插件的同学可能对插件开发知识点多、文档阅读困难、参考资料少有所体会。基于 webview 开发插件更是如此，寻遍网络，虽然有优秀的项目，但却没有完整且优秀的教程。为了修炼 vscode 开发灵力，不妨和洛竹一起挑战从零到一开发一款基于 webview 的 vscode 插件。</p>
<h2 data-id="heading-1">Hello vscode</h2>
<p>英雄多起于市井，高楼皆起于平地。再伟大的软件也都是从 Hello World 开始的，本章尽量用最简洁的语言描述一个 vscode 插件 Hello World 的诞生。</p>
<h3 data-id="heading-2">初始化项目</h3>
<p>安装 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fyeoman.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://yeoman.io/" ref="nofollow noopener noreferrer">Yeoman</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fgenerator-code" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/generator-code" ref="nofollow noopener noreferrer">VS Code Extension Generator</a>：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ npm install -g yo generator-code
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个脚手架会生成一个可以立马开发的项目。运行生成器，然后填好下列字段：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yo code
<span class="hljs-comment">#     _-----_     ╭──────────────────────────╮</span>
<span class="hljs-comment">#    |       |    │   Welcome to the Visual  │</span>
<span class="hljs-comment">#    |--(o)--|    │   Studio Code Extension  │</span>
<span class="hljs-comment">#   `---------´   │        generator!        │</span>
<span class="hljs-comment">#    ( _´U`_ )    ╰──────────────────────────╯</span>
<span class="hljs-comment">#    /___A___\   /</span>
<span class="hljs-comment">#     |  ~  |</span>
<span class="hljs-comment">#   __'.___.'__</span>
<span class="hljs-comment"># ´   `  |° ´ Y `</span>

<span class="hljs-comment"># ? What type of extension do you want to create? New Extension (TypeScript)</span>
<span class="hljs-comment"># ? What's the name of your extension? Juejin Posts</span>
<span class="hljs-comment"># ? What's the identifier of your extension? juejin-posts</span>
<span class="hljs-comment"># ? What's the description of your extension? 掘金文章管理</span>
<span class="hljs-comment"># ? Initialize a git repository? Yes</span>
<span class="hljs-comment"># ? Bundle the source code with webpack? No</span>
<span class="hljs-comment"># ? Which package manager to use? yarn</span>

$ code ./juejin-posts
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提交记录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2FIaJdlW" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/IaJdlW" ref="nofollow noopener noreferrer">hello world</a></p>
</blockquote>
<h3 data-id="heading-3">代码规范</h3>
<p>默认的脚手架生成的也有 ESLint 配置，但是 Editor、Prettier 的配置都没有，并且 ESLint 配置也不符合我的习惯。洛竹关于前端工程化的包都在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fluozhu" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/luozhu" ref="nofollow noopener noreferrer">youngjuning/luozhu</a>， ESlint 配置的包是 <code>@luozhu/eslint-config-*</code>。由于我们开发插件使用的是 Typescript，所以我们选择 <code>@luozhu/eslint-config-typescript</code>。</p>
<p><strong>安装依赖：</strong></p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn add @luozhu/eslint-config-typescript @luozhu/prettier-config prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>具体配置：</strong></p>
<p>配置涉及文件较多，请参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fluozhu%23coding-style" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/luozhu#coding-style" ref="nofollow noopener noreferrer">coding-style</a>，不关心的同学也可以直接略过。</p>
<p><strong>提交检测：</strong></p>
<p>安装依赖：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn add lint-staged yorkie -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改配置：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;
  <span class="hljs-attr">"gitHooks"</span>: &#123;
    <span class="hljs-attr">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>
  &#125;,
  <span class="hljs-attr">"lint-staged"</span>: &#123;
    <span class="hljs-attr">"**/*.&#123;js,jsx,ts,tsx&#125;"</span>: [<span class="hljs-string">"eslint --fix"</span>],
    <span class="hljs-attr">"**/*.&#123;md,json&#125;"</span>: [<span class="hljs-string">"prettier --write"</span>]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>eslint --fis：</strong></p>
<p>修改完配置之后需要执行 fix 对所有文件格式化一次。</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn lint --fix
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提交记录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2FxzFAVE" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/xzFAVE" ref="nofollow noopener noreferrer">chore: code style config</a></p>
</blockquote>
<h3 data-id="heading-4">约定式提交</h3>
<p>约定式提交我使用的是渐进式脚手架 <code>@luozhu/create-commitlint</code>，在项目中执行 <code>npx @luozhu/create-commitlint</code> 即可使项目符合规范化提交的配置。对规范化提交不了解的同学，强烈建议读一下 <a href="https://juejin.cn/post/6877462747631026190/" target="_blank" title="https://juejin.cn/post/6877462747631026190/">一文搞定 Conventional Commits </a>。</p>
<blockquote>
<p>提交记录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2FLd142y" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/Ld142y" ref="nofollow noopener noreferrer">chore: npx @luozhu/create-commitlint</a></p>
</blockquote>
<h3 data-id="heading-5">调试</h3>
<p>按下 <code>F5</code> 开启调试会出现[扩展开发宿主]窗口，然后按 <code>Command+Shift+P</code> 组件键输入 <code>Hello World</code> 命令。如下图所示 vscode 弹出了 <code>Hello World from Juejin Posts!</code> 的提示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc26d7d429f84564b88b55e9df60fcd7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时我们的开发窗口中，会出现一个 watch 任务的终端：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a15d0bd2cc4096af1a3f76173cbbe1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发窗口的调试控制台会输出插件运行日志（忽略红色的警告）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c31068ea0bca4d4793e35bdb16d70c0a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>调试执行的任务是在 <code>.vscode/tasks.json</code> 中配置的：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// See https://go.microsoft.com/fwlink/?LinkId=733558</span>
<span class="hljs-comment">// for the documentation about the tasks.json format</span>
&#123;
<span class="hljs-attr">"version"</span>: <span class="hljs-string">"2.0.0"</span>, <span class="hljs-comment">// 配置的版本号。</span>
<span class="hljs-attr">"tasks"</span>: [ <span class="hljs-comment">// 任务配置。通常是外部任务运行程序中已定义任务的扩充。</span>
&#123;
<span class="hljs-attr">"type"</span>: <span class="hljs-string">"npm"</span>, <span class="hljs-comment">// 要自定义的任务类型。</span>
<span class="hljs-attr">"script"</span>: <span class="hljs-string">"watch"</span>, <span class="hljs-comment">// 要自定义的 npm 脚本。</span>
<span class="hljs-attr">"problemMatcher"</span>: <span class="hljs-string">"$tsc-watch"</span>, <span class="hljs-comment">// 要使用的问题匹配程序。可以是一个字符串或一个问题匹配程序定义，也可以是一个字符串数组和多个问题匹配程序。</span>
<span class="hljs-attr">"isBackground"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 执行的任务是否保持活动状态并在后台运行。</span>
<span class="hljs-attr">"presentation"</span>: &#123; <span class="hljs-comment">// 配置用于显示任务输出并读取其输入的面板。</span>
<span class="hljs-attr">"reveal"</span>: <span class="hljs-string">"never"</span> <span class="hljs-comment">// 控制运行任务的终端是否显示。可按选项 "revealProblems" 进行替代。默认设置为“始终”。</span>
&#125;,
<span class="hljs-attr">"group"</span>: &#123; <span class="hljs-comment">// 定义此任务属于的执行组。它支持 "build" 以将其添加到生成组，也支持 "test" 以将其添加到测试组。</span>
<span class="hljs-attr">"kind"</span>: <span class="hljs-string">"build"</span>, <span class="hljs-comment">// 任务的执行组。</span>
<span class="hljs-attr">"isDefault"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 定义此任务是否为组中的默认任务。</span>
&#125;
&#125;
]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">打包</h2>
<p>我们的插件开发完成前，想要分享给小伙伴体验可以吗？答案是肯定的，vscode 为我们提供了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fvscode-vsce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/microsoft/vscode-vsce" ref="nofollow noopener noreferrer">vsce</a> 实现这个需求，我们将 vsce 模块安装到全局，然后使用 <code>vsce package</code> 命令尝试打包：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ vsce package
 ERROR  Missing publisher name. Learn more: https://code.visualstudio.com/api/working-with-extensions/publishing-extension<span class="hljs-comment">#publishing-extensions</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>啊，咋还报错了？<code>publisher</code> 是啥？？一脸懵逼。不慌，按<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2Fapi%2Fworking-with-extensions%2Fpublishing-extension%23create-a-publisher" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/api/working-with-extensions/publishing-extension#create-a-publisher" ref="nofollow noopener noreferrer">链接</a> 我知道了 publisher 是一个可以将扩展发布到Visual Studio Code Marketplace 的身份。每个扩展都需要在其 <code>package.json</code> 文件中包含一个发布者名称。如果注册发布者我们后面详说，这里我们把 <code>publisher</code> 设置为 <code>luozhu</code>。</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ vsce package
 INFO  Detected presence of yarn.lock. Using <span class="hljs-string">'yarn'</span> instead of <span class="hljs-string">'npm'</span> (to override this pass <span class="hljs-string">'--no-yarn'</span> on the <span class="hljs-built_in">command</span> line).
 ERROR  Make sure to edit the README.md file before you package or publish your extension.
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf561381232b4690a5d7cd0378c267d7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>额，裂开，这咋还报错，假装淡定，读一下提示原来是要我们编辑一下 README.md，没错，vscode 模板里有初始的 README，我们需要编辑一下才可以打包。修改后再次尝试 <code>vsce package</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acfe2e957c9545578c7b6990371a3f0b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>终于，打包成功！为了追求完美，最后我们再来做一些优化工作：</p>
<ol>
<li>执行 <code>vsce package</code> 的时候加上 <code>--no-yarn</code></li>
<li>在 <em>package.json</em> 中加上 <code>repository</code> 字段即可看不到任何警告。</li>
<li>为了便捷，我们将 vsce 安装到项目中，然后把 <code>vsce package --no-yarn</code> 添加到 npm scripts 中。</li>
<li><em>package.json</em> 加上 <code>license</code> 字段。</li>
</ol>
<p>然后再次尝试 <code>yarn package</code> 就完美了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a9a251834b945c8a882039020f56e4f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提示：vsce package 会先执行 <code>vscode:prepublish</code> 这个预发布脚本去编译项目。</p>
</blockquote>
<blockquote>
<p>提交记录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2FZCp4qU" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/ZCp4qU" ref="nofollow noopener noreferrer">chore: config vsce package</a></p>
</blockquote>
<h3 data-id="heading-7">打包原理</h3>
<p>如过你也跟着一路敲到了这里，此时你会在项目根目录发现 <code>vsix</code> 结尾的文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2c0846bd66747ceab0c09524a209b28~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就是 vscode 插件的安装包，我们先不急着安装，先一起来看一下这个文件是个什么东西。尝试用归档工具解压后得到如下目录文件夹：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/182c365a0690467cb0bd8b0d1490c175~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到编译后的文件夹 <code>out</code> 和其他一些文件是被直接压缩进安装包的，聪明的你肯定发现了 <code>.cz-config.js</code>、<code>.prettierrc.js</code> 和 <code>commitlint.config.js</code> 这种开发时文件也被压缩了，运行插件完全用不到，这明显不合理。其实和其他插件体系一样，vscode 也提供了 <code>.vscodeignore</code> 来实现打包忽略配置，我们将以上无关文件忽略重新打包即可。</p>
<p>原理就这？不存在的，我们打开 <code>extension.js</code> 会发现引用了 <code>vscode</code> 这个包：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb42881e49a94456aeac417f6b5cba71~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是我们的安装包中并没有 <em>node_modules</em>，那么 vscode 这个包存在在哪里呢？我猜的是挂在 node 环境上了，读了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2F33GTcH" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/33GTcH" ref="nofollow noopener noreferrer">源码</a>后我发现我竟然是对的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e796fcf81b64fd7a18d9c3e36fbefdf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>vscode 实现了拦截器在加载 Node 环境的时候将 vscode 给添加到了内置包中，这样的好处是减小插件的体积。</p>
<p>那么我们如果使用三方插件呢？以常用的 lodash 为例，安装 lodash 之后重新打包：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn package
yarn run v1.22.10
$ vsce package --no-yarn
Executing prepublish script <span class="hljs-string">'npm run vscode:prepublish'</span>...

> juejin-posts@0.0.1 vscode:prepublish
> yarn run compile

$ tsc -p ./
This extension consists of 1060 files, out of <span class="hljs-built_in">which</span> 1049 are JavaScript files. For performance reasons, you should bundle your extension: https://aka.ms/vscode-bundle-extension . You should also exclude unnecessary files by adding them to your .vscodeignore: https://aka.ms/vscode-vscodeignore
 DONE  Packaged: /Users/luozhu/Desktop/playground/juejin-posts/juejin-posts-0.0.1.vsix (1060 files, 644.72KB)
✨  Done <span class="hljs-keyword">in</span> 5.54s.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候提示我们有 1000 多个文件，大概率 <em>node_modules</em> 文件夹被打包了，我们来解压下见证一下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/917b7742991640c9a0b03314cef24ce6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不出所料，vscode 默认的打包方式就是简单的编译拷贝，通过忽略文件减小体积也是杯水车薪。而且 vscode 扩展的规模往往增长很快。它们是在多个源文件中编写的，并依赖于 npm 的模块。分解和重用是开发的最佳实践，但在安装和运行扩展时，它们是有代价的。加载 100 个小文件要比加载一个大文件慢得多。这就是我们推荐捆绑的原因。捆绑是将多个小的源文件合并成一个文件的过程。</p>
<p>在 JavaScript 中，有不同的打包工具可以用，流行的有 rollup.js、Parcel、esbuild 和 webpack，官方脚手架默认只能选 webpack，我们这里推荐直接使用更快更强的 esbuild。</p>
<blockquote>
<p>提交记录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2FZCp4qU" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/ZCp4qU" ref="nofollow noopener noreferrer">chore: ignore config file when package</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2FggpQmv" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/ggpQmv" ref="nofollow noopener noreferrer">chore: add esModuleInterop to tsconfig</a></p>
</blockquote>
<h3 data-id="heading-8">使用 esbuild 优化打包</h3>
<p><strong>安装依赖：</strong></p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn add -D esbuild
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>npm scripts：</strong></p>
<pre><code class="hljs language-diff copyable" lang="diff">"scripts": &#123;
<span class="hljs-deletion">-    "vscode:prepublish": "yarn run compile",</span>
<span class="hljs-deletion">-    "compile": "tsc -p ./",</span>
<span class="hljs-deletion">-    "watch": "tsc -watch -p ./",</span>
<span class="hljs-deletion">-    "pretest": "yarn run compile && yarn run lint",</span>
<span class="hljs-addition">+    "vscode:prepublish": "yarn esbuild-base -- --minify",</span>
<span class="hljs-addition">+    "esbuild-base": "esbuild ./src/extension.ts --bundle --outfile=out/extension.js --external:vscode --format=cjs --platform=node",</span>
<span class="hljs-addition">+    "esbuild": "yarn esbuild-base --sourcemap",</span>
<span class="hljs-addition">+    "esbuild-watch": "yarn esbuild-base --sourcemap --watch",</span>
<span class="hljs-addition">+    "test-compile": "tsc -p ./",</span>
<span class="hljs-addition">+    "pretest": "yarn test-compile && yarn lint",</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：由于 watch 改成了 esbuild-watch，所以 <em>.vscode/tasks.json</em> 中的 scripts 子段也需要做相应修改。</p>
</blockquote>
<p><strong>vscode tasks：</strong></p>
<p>理论上我们把打包命令改成 esbuild 之后，应该将 vscode 任务中的问题匹配程序设置为 <code>$esbuild-watch</code>，但是 vscode 会提示我们无法识别的问题匹配程序：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b51c79ee1344b6f92a3f2efaf9ef7aa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>尝试搜索扩展，果然有一个 esbuild Problem Matchers 插件，我们将其安装并添加 <code>"connor4312.esbuild-problem-matchers"</code> 到 <em>.vscode/extensions.json</em> 文件的 <code>recommendations</code> 中。</p>
<p><strong>忽略文件：</strong></p>
<p>我们使用 esbuild 打包后会将使用到的代码都打包进 <code>out/extension.js</code>，但是 vsce 的打包机制是不管你有没有用到都会把 <code>dependencies</code> 中的包打进安装包中，所以我们需要将 <em><em>node_modules</em></em> 忽略掉。</p>
<p><strong>成果展示：</strong></p>
<p>从图中我们可以看到，安装包的体积大大减小了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba86286be7fc41f4b8325a3e0be0d2d2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提交记录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2FF12xNk" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/F12xNk" ref="nofollow noopener noreferrer">chore: config esbuild</a></p>
</blockquote>
<h2 data-id="heading-9">Hello Umijs</h2>
<h3 data-id="heading-10">初始化 umi 项目</h3>
<p>使用 umi 脚手架在根目录新建一个 <em>web</em> 目录。</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ mkdir web && <span class="hljs-built_in">cd</span> web
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过官方工具创建项目：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ yarn create @umijs/umi-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <em>.umirc.ts</em> 配置：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig, IConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'umi'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">nodeModulesTransform</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'none'</span>,
  &#125;,
  <span class="hljs-attr">routes</span>: [&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: <span class="hljs-string">'@/pages/index'</span> &#125;],
  <span class="hljs-attr">fastRefresh</span>: &#123;&#125;, <span class="hljs-comment">// 开发时可以保持组件状态，同时编辑提供即时反馈。</span>
  <span class="hljs-attr">history</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'memory'</span>, <span class="hljs-comment">// 默认的类型是 `browser`，但是由于 vscode webview 环境不存在浏览器路由，改成 `memory` 和 `hash` 都可以</span>
  &#125;,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">// 需要在 dev 时写文件到输出目录，这样保证开发阶段有 js/css 文件</span>
    <span class="hljs-attr">writeToDisk</span>: <span class="hljs-function"><span class="hljs-params">filePath</span> =></span>
      [<span class="hljs-string">'umi.js'</span>, <span class="hljs-string">'umi.css'</span>].some(<span class="hljs-function"><span class="hljs-params">name</span> =></span> filePath.endsWith(name)),
  &#125;,
&#125; <span class="hljs-keyword">as</span> IConfig);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>package.json</code> 加入 <code>name</code>、<code>version</code>、<code>description</code>：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"web"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"web for juejin-posts"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">忽略文件</h3>
<p><strong>.gitignore：</strong></p>
<p>将 vscode 扩展和 umijs 脚手架生成的 gitignore 合并为一下内容：</p>
<pre><code class="copyable"># See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# vscode
.vscode-test/
*.vsix

# dependencies
node_modules
npm-debug.log*
yarn-error.log
package-lock.json

# production
out
dist

# misc
.DS_Store

# umi
**/src/.umi
**/src/.umi-production
**/src/.umi-test
**/.env.local
web/yarn.lock
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>.vscodeignore：</strong></p>
<p>由于 vscode 打包的时候只需要获取 umijs 打包后的产物，所有加入 <code>web/**</code> 和 <code>!web/dist/**</code> 将无用的文件忽略掉。</p>
<pre><code class="copyable">.vscode/**
.vscode-test/**
out/test/**

src/**
.gitignore
.yarnrc
vsc-extension-quickstart.md
**/tsconfig.json
**/*.map
**/*.ts

.cz-config.js
.prettierrc.js
commitlint.config.js
**/node_modules/**
yarn-error.log
web/**
!web/dist/**
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">yarn workspace</h3>
<p>由于我们的项目是 vscode 扩展和 web 项目混合的项目。为了方便管理脚本和依赖，我们引入了 <code>yarn workspace</code> 来管理项目。在根目录的 <em>package.json</em> 中加入以下配置即可：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"private"</span>: <span class="hljs-string">"true"</span>,
  <span class="hljs-attr">"workspaces"</span>: [<span class="hljs-string">"web"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">调试</h3>
<p>由于我们的 web 项目也需要编译，所以我们需要修改一下 vscode <code>launch.json</code> 加入 web 项目的编译任务。配置参考了 <a href="https://link.juejin.cn/?target=http%3A%2F%2Ftny.im%2FbOqQT" target="_blank" rel="nofollow noopener noreferrer" title="http://tny.im/bOqQT" ref="nofollow noopener noreferrer">appworks</a>。</p>
<p>首先修改根目录的 <code>package.json</code> 的 scripts:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"vscode:prepublish"</span>: <span class="hljs-string">"yarn build:web && yarn esbuild-base --minify"</span>,
    <span class="hljs-attr">"preesbuild-base"</span>: <span class="hljs-string">"rimraf out"</span>,
    <span class="hljs-attr">"esbuild-base"</span>: <span class="hljs-string">"esbuild ./src/extension.ts --bundle --outfile=out/extension.js --external:vscode --format=cjs --platform=node"</span>,
    <span class="hljs-attr">"esbuild"</span>: <span class="hljs-string">"yarn esbuild-base --sourcemap"</span>,
    <span class="hljs-attr">"esbuild-watch"</span>: <span class="hljs-string">"yarn esbuild-base --sourcemap --watch"</span>,
    <span class="hljs-attr">"web-build"</span>: <span class="hljs-string">"yarn workspace web run build"</span>,
    <span class="hljs-attr">"web-watch"</span>: <span class="hljs-string">"yarn workspace web run start"</span>,
    <span class="hljs-attr">"test-compile"</span>: <span class="hljs-string">"tsc -p ./"</span>,
    <span class="hljs-attr">"lint"</span>: <span class="hljs-string">"eslint src --ext ts,tsx"</span>,
    <span class="hljs-attr">"pretest"</span>: <span class="hljs-string">"yarn test-compile && yarn lint"</span>,
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"node ./out/test/runTest.js"</span>,
    <span class="hljs-attr">"commit"</span>: <span class="hljs-string">"git cz"</span>,
    <span class="hljs-attr">"package"</span>: <span class="hljs-string">"vsce package --no-yarn"</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后修改 <em>.vscode/launch.json</em> 配置为：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// A launch configuration that compiles the extension and then opens it inside a new window</span>
<span class="hljs-comment">// Use IntelliSense to learn about possible attributes.</span>
<span class="hljs-comment">// Hover to view descriptions of existing attributes.</span>
<span class="hljs-comment">// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387</span>
&#123;
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.2.0"</span>,
  <span class="hljs-attr">"compounds"</span>: [
    <span class="hljs-comment">// 复合列表。每个复合可引用多个配置，这些配置将一起启动。</span>
    &#123;
      <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Debug Extension"</span>, <span class="hljs-comment">// 复合的名称。在启动配置下拉菜单中显示。</span>
      <span class="hljs-attr">"configurations"</span>: [
        <span class="hljs-comment">// 将作为此复合的一部分启动的配置名称。</span>
        <span class="hljs-string">"Run Extension"</span>,
        <span class="hljs-string">"Watch Webview"</span>
      ],
      <span class="hljs-attr">"presentation"</span>: &#123;
        <span class="hljs-attr">"order"</span>: <span class="hljs-number">0</span>
      &#125;
    &#125;
  ],
  <span class="hljs-attr">"configurations"</span>: [
    &#123;
      <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Watch Webview"</span>,
      <span class="hljs-attr">"request"</span>: <span class="hljs-string">"attach"</span>,
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"node"</span>,
      <span class="hljs-attr">"preLaunchTask"</span>: <span class="hljs-string">"npm: web-watch"</span>
    &#125;,
    &#123;
      <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Run Extension"</span>,
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"extensionHost"</span>,
      <span class="hljs-attr">"request"</span>: <span class="hljs-string">"launch"</span>,
      <span class="hljs-attr">"args"</span>: [<span class="hljs-string">"--extensionDevelopmentPath=$&#123;workspaceFolder&#125;"</span>],
      <span class="hljs-attr">"outFiles"</span>: [<span class="hljs-string">"$&#123;workspaceFolder&#125;/out/**/*.js"</span>],
      <span class="hljs-attr">"preLaunchTask"</span>: <span class="hljs-string">"$&#123;defaultBuildTask&#125;"</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成后进入 VS Code，按下<code>F5</code>，你会立即看到一个<strong>插件发开主机</strong>窗口，其中就运行着插件。这时候运行你会发现控制台报一下错误 ❌：</p>
<pre><code class="copyable">error TS6059: File '/Users/luozhu/Desktop/github/juejin-posts/web/src/pages/index.tsx' is not under 'rootDir' '/Users/luozhu/Desktop/github/juejin-posts/src'. 'rootDir' is expected to contain all source files.
  The file is in the program because:
    Matched by include pattern '**/*' in '/Users/luozhu/Desktop/github/juejin-posts/tsconfig.json'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因是因为 umi 的约定的项目结构和 vscode extension 都包含 <em>src</em> 目录。由于 vscode 插件和 umi 的编译是分开的，我们在根目录的 <em>tsconfig.json</em> 中将 <em>web</em> 目录忽略即可：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"exclude"</span>: [<span class="hljs-string">"web"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，你可以按下 <code>F5</code> 看到<strong>插件发开主机</strong>窗口的同时还会看到两个调试任务：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4b3b6f2522643fb9bc574e2f9982775~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">其他优化工作</h3>
<ol>
<li>由于基于 yarn workspace，我们把公用的依赖合并</li>
<li>eslint 配置使用 <code>@luozhu/eslint-config-react-typescrip</code></li>
</ol>
<blockquote>
<p>提交记录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2Fbt3WHr" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/bt3WHr" ref="nofollow noopener noreferrer">chore: config umijs</a></p>
</blockquote>
<h2 data-id="heading-15">vscode 插件开发核心概念</h2>
<p>在开始 webview 能力开发之前，我们有必要了解一下 vscode 插件开发的核心概念。为了有个全局的理解，我们先来看下我们现在项目的主要目录结构：</p>
<pre><code class="hljs language-sh copyable" lang="sh">.
├── CHANGELOG.md <span class="hljs-comment"># 基于 standard-version 生成的更新日志文件</span>
├── README.md
├── package.json <span class="hljs-comment"># vscode 包配置文件，诸如插件 LOGO、名字、描述、注册激活事件</span>
├── src
│   └── extension.ts <span class="hljs-comment"># 插件入口文件，暴露 activate 方法用于注册命令和初始化一些配置，暴露 deactivate 方法用于插件关闭前执行清理工作</span>
├── tsconfig.json <span class="hljs-comment"># vscode 的编译配置</span>
├── web <span class="hljs-comment"># 基于 umi 的 web，也是我们后边 webview 要承载的内容</span>
└── yarn.lock
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从目录结构可以看出，关键的文件是 <code>package.json</code> 和 <code>extension.ts</code>，我们以 helloWorld 命令为例介绍下 vscode 插件的三个核心概念。</p>
<h3 data-id="heading-16">1. 激活事件</h3>
<p><strong>激活事件</strong>是在 <code>package.json</code> 中的 <code>activationEvents</code> 字段声明的一个 JSON 数组对象。为了注册 helloWorld 这个命令，第一步就是注册激活事件，激活事件类型有很多，注册命令的激活事件是 <code>onCommand</code>:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"activationEvents"</span>: [<span class="hljs-string">"onCommand:juejin-posts.helloWorld"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">2. 发布内容配置</h3>
<p>发布内容配置（ 即 VS Code 为插件扩展提供的配置项）是 <code>package.json</code> 的 <code>contributes</code> 字段，你可以在其中注册各种配置项扩展 VS Code 的能力。上一步我们注册的 helloWorld 激活事件只是告诉了 vscode 可以通过 <code>juejin-posts.helloWorld</code> 命令触发。我们还需要再 <code>contributes.commands</code> 中注册我们的 <code>juejin-posts.helloWorld</code> 命令：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"commands"</span>: [
      &#123;
        <span class="hljs-attr">"command"</span>: <span class="hljs-string">"juejin-posts.helloWorld"</span>,
        <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Hello World"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">3. VS Code API</h3>
<p><strong>VS Code API</strong> 是 VS Code 提供给插件使用的一系列 Javascript API。通过前两个核心概念的能力，我们已经注册好了命令和事件，那么下一步必然就是注册事件回调。事件回调在 vscode 中是通过 <code>vscode.commands.registerCommand</code> 函数来注册的，下面 👇🏻 是我们在入口文件 <code>src/extension.ts</code> 中注册 <code>juejin-posts.helloWorld</code> 命令。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// vscode 这个模块包含了 VS Code 扩展的 API</span>
<span class="hljs-keyword">import</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;

<span class="hljs-comment">// 这个方法当你的扩展激活时调用，扩展会在命令首次执行时激活</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">context: vscode.ExtensionContext</span>) </span>&#123;
  <span class="hljs-comment">// 当你的扩展被激活时，这行代码将只被执行一次</span>
  <span class="hljs-comment">//</span>
  <span class="hljs-comment">// 使用 console.log 输出日志信息或使用 console.error 输出错误信息。</span>
  <span class="hljs-comment">//</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Congratulations, your extension "juejin-posts" is now active!'</span>);

  <span class="hljs-comment">// 入口命令已经在 package.json 文件中定义好了，现在调用 registerCommand 方法</span>
  <span class="hljs-comment">// registerCommand 中的参数必须与 package.json 中的 command 保持一致</span>
  <span class="hljs-keyword">const</span> disposable = vscode.commands.registerCommand(<span class="hljs-string">'juejin-posts.helloWorld'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 把你的代码写在这里，每次命令执行时都会调用这里的代码</span>
    <span class="hljs-comment">// 给用户显示一个消息提示</span>
    vscode.window.showInformationMessage(<span class="hljs-string">'Hello World from Juejin Posts!'</span>);
  &#125;);

  context.subscriptions.push(disposable);
&#125;

<span class="hljs-comment">// 当你的扩展被停用时，这个方法被调用。</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deactivate</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">集成 webview</h2>
<h3 data-id="heading-20">注册命令</h3>
<p>1、<em>package.json</em> 激活事件（<code>activationEvents</code>）中添加 <code>"onCommand:juejin-posts.start"</code></p>
<p>2、<em>package.json</em> 命令（<code>commands</code>）中添加：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"command"</span>: <span class="hljs-string">"juejin-posts.start"</span>,
  <span class="hljs-attr">"title"</span>: <span class="hljs-string">"start"</span>,
  <span class="hljs-attr">"category"</span>: <span class="hljs-string">"Juejin Posts"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、<em>src/extension.ts</em> 中注册命令</p>
<pre><code class="hljs language-ts copyable" lang="ts">context.subscriptions.push(
  vscode.commands.registerCommand(<span class="hljs-string">'juejin-posts.start'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// Truth is endless. Keep coding...</span>
  &#125;)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">创建 webview 面板</h3>
<h4 data-id="heading-22">创建一个空白的面板</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;

<span class="hljs-comment">// 创建并显示新的webview</span>
<span class="hljs-keyword">const</span> panel = vscode.window.createWebviewPanel(
  <span class="hljs-string">'juejin-posts'</span>, <span class="hljs-comment">// 只供内部使用，这个 webview 的标识</span>
  <span class="hljs-string">'Juejin Posts'</span>, <span class="hljs-comment">// 给用户显示的面板标题</span>
  vscode.vscode.ViewColumn.One, <span class="hljs-comment">// 给新的 webview 面板一个编辑器视图</span>
  &#123;
    <span class="hljs-attr">enableScripts</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启用 javascript 脚本</span>
    <span class="hljs-attr">retainContextWhenHidden</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 隐藏时保留上下文</span>
  &#125; <span class="hljs-comment">// webview 面板的内容配置</span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们使用了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api.js.org%2Fmodules%2Fwindow.html%23createWebviewPanel" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api.js.org/modules/window.html#createWebviewPanel" ref="nofollow noopener noreferrer">window.createWebviewPanel</a> API 创建了一个 webview 面板，现在我们尝试运行 <code>juejin-posts.start</code> 就可以打开一个 webview 面板：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d85ad985232542f587376e5073feb1a1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">给面板设置内容</h4>
<p>上面我们创建了一个空白的面板，那么我们如何给面板添加内容呢？我们可以使用 <code>panel.webview.html</code> 来设置 HTML 内容：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getWebviewContent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Juejin Posts</title>
        <style>
          html, body &#123;
            padding: 0px;
            height: 100vh;
            position: relative;
            margin: 0;
            padding: 0;
            overflow: hidden;
          &#125;
          #yoyo &#123;
            position: absolute;
            bottom: 50px;
            right: -90px;
            opacity: 0;
            transition: .25s ease-in-out
          &#125;
          #yoyo:hover &#123;
            opacity: 1;
            right: 0;
          &#125;
        </style>
    </head>
    <body>
      <a href="https://juejin.cn"><img id="yoyo" src="https://cdn.jsdelivr.net/gh/youngjuning/images/20210817163229.png" width="100" /></a>
    </body>
    </html>
  `</span>;
&#125;
...
<span class="hljs-comment">// 给 webview panel 设置 HTML 内容</span>
panel.webview.html = getWebviewContent();
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新使用 <code>juejin-posts.start</code> 命令就可以调戏悠悠船长了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5160d0c76536441b8d1ac3cfcedc0d0e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-24">限制 webview 视图为一个</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">context: vscode.ExtensionContext</span>) </span>&#123;
  <span class="hljs-comment">// 追踪当前 webview 面板</span>
  <span class="hljs-keyword">let</span> currentPanel: vscode.WebviewPanel | <span class="hljs-literal">undefined</span> = <span class="hljs-literal">undefined</span>;

  context.subscriptions.push(
    vscode.commands.registerCommand(<span class="hljs-string">'juejin-posts.start'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 获取当前活动的编辑器</span>
      <span class="hljs-keyword">const</span> columnToShowIn = vscode.window.activeTextEditor
        ? vscode.window.activeTextEditor.viewColumn
        : <span class="hljs-literal">undefined</span>;

      <span class="hljs-keyword">if</span> (currentPanel) &#123;
        <span class="hljs-comment">// 如果我们已经有了一个面板，那就把它显示到目标列布局中</span>
        currentPanel.reveal(columnToShowIn);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 不然，创建一个新面板</span>
        currentPanel = vscode.window.createWebviewPanel();
        <span class="hljs-comment">// 当前面板被关闭后重置</span>
        currentPanel.onDidDispose(
          <span class="hljs-function">() =></span> &#123;
            currentPanel = <span class="hljs-literal">undefined</span>;
          &#125;,
          <span class="hljs-literal">null</span>,
          context.subscriptions
        );
      &#125;
    &#125;)
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Fmodules%2Fwindow.html%23activeTextEditor" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/modules/window.html#activeTextEditor" ref="nofollow noopener noreferrer">vscode.window.activeTextEditor</a>：获取当前活动的文本编辑器</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Finterfaces%2FWebviewPanel.html%23reveal" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/interfaces/WebviewPanel.html#reveal" ref="nofollow noopener noreferrer">currentPanel.reveal()</a>：调用 <code>reveal()</code> 或者拖动 webview 面板到新的编辑布局中去。</li>
</ul>
<h4 data-id="heading-25">设置 Icon</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 设置 Logo</span>
panel.iconPath = vscode.Uri.file(
  path.join(context.extensionPath, <span class="hljs-string">'assets'</span>, <span class="hljs-string">'icon-juejin.png'</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 vscode 扩展中我们需要通过 <code>vscode.Uri.file</code> 方法获取磁盘上的资源路径。</p>
<h4 data-id="heading-26">webview 获取内容的 Uri</h4>
<p>你应该使用 <code>asWebviewUri</code> 管理插件资源。不要硬编码 <code>vscode-resource://</code>，而是使用 <code>asWebviewUri</code> 确保你的插件在云端环境也能正常运行。</p>
<p>在 <a href="https://link.juejin.cn/?target=http%3A%2F%2Ftny.im%2Fjb4go" target="_blank" rel="nofollow noopener noreferrer" title="http://tny.im/jb4go" ref="nofollow noopener noreferrer">@luozhu/vscode-utils</a> 中我们对获取本地资源路径做了封装：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 获取内容的 Uri</span>
<span class="hljs-keyword">const</span> getDiskPath = <span class="hljs-function">(<span class="hljs-params">fileName: <span class="hljs-built_in">string</span></span>) =></span> &#123;
  <span class="hljs-keyword">return</span> webviewPanel.webview.asWebviewUri(
    vscode.Uri.file(path.join(context.extensionPath, rootPath, <span class="hljs-string">'dist'</span>, fileName))
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">使用 umi 开发 webview</h3>
<p>上一节我们通过调戏悠悠船长熟悉了 webview 面板的创建，这一节我们来看下如何使用 umijs 来代替 HTML 的内容。</p>
<p><code>panel.webview.html</code> 中的内容其实就是正常的 HTML+JavaScript+CSS 代码。你可以使用任何前端技术去编写它的内容，比如 jquery、bootstrap、Vue 以及 React。虽然本文的例子是基于 umijs 开发 webview 的内容，但是其他技术原理是一样的，洛竹在后续也会提供多个技术的 vscode webview 开发脚手架。</p>
<h4 data-id="heading-28">封装获取 umijs 打包产物的方法</h4>
<p>我们知道 <code>umi build</code> 命令会在 <em>web/dist</em> 产生 index.html、umi.js、umi.css 三个文件，我们根据 index.html 改造前面的 getWebviewContent 方法如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-comment">/**
 * 获取基于 umijs 的 webview 内容
 * <span class="hljs-doctag">@param </span>context 扩展上下文
 * <span class="hljs-doctag">@param </span>webviewPanel webview 面板对象
 * <span class="hljs-doctag">@param </span>rootPath webview 所在路径，默认 web
 * <span class="hljs-doctag">@param </span>umiVersion umi 版本
 * <span class="hljs-doctag">@returns <span class="hljs-variable">string</span></span>
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getUmiContent = <span class="hljs-function">(<span class="hljs-params">
  context: vscode.ExtensionContext,
  webviewPanel: vscode.WebviewPanel,
  umiVersion?: <span class="hljs-built_in">string</span>,
  rootPath = <span class="hljs-string">'web'</span>
</span>) =></span> &#123;
  <span class="hljs-comment">// 获取磁盘上的资源路径</span>
  <span class="hljs-keyword">const</span> getDiskPath = <span class="hljs-function">(<span class="hljs-params">fileName: <span class="hljs-built_in">string</span></span>) =></span> &#123;
    <span class="hljs-keyword">return</span> webviewPanel.webview.asWebviewUri(
      vscode.Uri.file(path.join(context.extensionPath, rootPath, <span class="hljs-string">'dist'</span>, fileName))
    );
  &#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`
    <html>
      <head>
        <meta charset="utf-8" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no"
        />
        <link rel="stylesheet" href="<span class="hljs-subst">$&#123;getDiskPath(<span class="hljs-string">'umi.css'</span>)&#125;</span>" />
        <style>
          html, body, #root &#123;
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
          &#125;
        </style>
        <script>
          //! umi version: <span class="hljs-subst">$&#123;umiVersion&#125;</span>
        </script>
      </head>
      <body>
        <div id="root"></div>
        <script src="<span class="hljs-subst">$&#123;getDiskPath(<span class="hljs-string">'umi.js'</span>)&#125;</span>"></script>
      </body>
    </html>
  `</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：上面的方法我已经封装在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fluozhu%2Ftree%2Fmain%2Fpackages%2Fvscode-utils" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/luozhu/tree/main/packages/vscode-utils" ref="nofollow noopener noreferrer">@luozhu/vscode-utils</a> 的中。</p>
</blockquote>
<p>我们使用 getUmiContent 重新前面的代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; getUmiContent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@luozhu/vscode-utils'</span>;
...
panel.webview.html = getUmiContent(context, panel, <span class="hljs-string">'3.5.17'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">优化打包</h4>
<p>由于我们封装了 <code>getUmiContent</code> 方法，<code>umi build</code> 生成的 index.html 就没有用了，我们可以使用 <code>HTML=none umi build</code> 命令在打包的时候不生成 index.html 文件。</p>
<p>另外目前 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Fumi%2Fissues%2F7132" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/umi/issues/7132" ref="nofollow noopener noreferrer">umijs 的 mfsu 不支持 writeToDisk 方法</a>，如果后续支持了可以使用 mfsu 优化调试速度。</p>
<blockquote>
<p>创建 webview 面板的任务大部分都比较重复，为了沉淀最佳实践，我在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fluozhu%2Ftree%2Fmain%2Fpackages%2Fvscode-utils" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/luozhu/tree/main/packages/vscode-utils" ref="nofollow noopener noreferrer">@luozhu/vscode-utils</a> 封装了 <a href="https://link.juejin.cn/?target=http%3A%2F%2Ftny.im%2FbHLQx" target="_blank" rel="nofollow noopener noreferrer" title="http://tny.im/bHLQx" ref="nofollow noopener noreferrer">createUmiWebviewPanel</a> 方法。</p>
</blockquote>
<h3 data-id="heading-30">给 webview 内容加上主题</h3>
<p>webview 可以基于当前的 VS Code 主题和 CSS 改变自身的样式。VS Code 将主题分成 3 种类别，而且在 body 元素上加上了特殊类名以表明当前主题，我们在 umi 中全局加入下面的样式：</p>
<pre><code class="hljs language-ts copyable" lang="ts">body.vscode-light &#123;
  h1, h2, h3, h4, h5, h6 &#123;
    <span class="hljs-attr">color</span>: black;
  &#125;
  <span class="hljs-attr">color</span>: black;
  background-color: <span class="hljs-keyword">var</span>(--vscode-editor-background);
&#125;

body.vscode-dark &#123;
  h1, h2, h3, h4, h5, h6 &#123;
    <span class="hljs-attr">color</span>: white;
  &#125;
  <span class="hljs-attr">color</span>: white;
  background-color: <span class="hljs-keyword">var</span>(--vscode-editor-background);
&#125;

body.vscode-high-contrast &#123;
  h1, h2, h3, h4, h5, h6 &#123;
    <span class="hljs-attr">color</span>: red;
  &#125;
  <span class="hljs-attr">color</span>: red;
  background-color: <span class="hljs-keyword">var</span>(--vscode-editor-background);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于这部分适配大部分是通用的，所以我也将它封装进了 <code>@luozhu/vscode-utils</code> 的 <code>getUmiContent</code> 中了。</p>
<h2 data-id="heading-31">webview 与 vscode 交互</h2>
<h3 data-id="heading-32">webview 中执行脚本</h3>
<p>vscode 中的 webview 本质就是一个 iframe，因此我们是可以再 webview 中执行脚本的，只不过在 vscode 中 webview 默认禁用了 JavaScript，我们在调用 <code>createWebviewPanel</code> API 时传入 <code>enableScripts: true</code> 即可。</p>
<h3 data-id="heading-33">插件传递信息给 webview</h3>
<p>webview 的脚本能做到任何普通网页脚本能做到的事情，但是 webview 运行在自己的上下文中，脚本是不能访问 VS Code API 的。我们需要借助 postMessage 这种事件的方式传递信息。在 vscode 中，我们在 vscode 侧可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Finterfaces%2FWebview.html%23postMessage" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/interfaces/Webview.html#postMessage" ref="nofollow noopener noreferrer">Webview.postMessage</a> 发布事件并发送任何序列化的 JSON 数据，在 webview 侧则使用 <code>window.addEventListener('message' event => &#123; ... &#125;)</code> 来处理这些信息：</p>
<p><strong>vscode 侧</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 注册一个新的命令</span>
context.subscriptions.push(
  vscode.commands.registerCommand(<span class="hljs-string">'juejin-me.author'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!currentPanel) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;

    <span class="hljs-comment">// 把信息发送到 webview</span>
    <span class="hljs-comment">// 你可以发送任何序列化的 JSON 数据</span>
    currentPanel.webview.postMessage(&#123; <span class="hljs-attr">method</span>: <span class="hljs-string">'showAuthor'</span> &#125;);
  &#125;)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webview 侧</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Modal &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
...
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">const</span> message = event.data;
  <span class="hljs-keyword">switch</span> (message.method) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'showAuthor'</span>: &#123;
      Modal.info(&#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'洛竹'</span>,
        <span class="hljs-attr">content</span>: (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            大家好，我是洛竹🎋一只住在杭城的木系前端🧚🏻‍♀️，如果你喜欢我的文章📚，可以通过
            <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://juejin.cn/user/325111174662855/posts"</span>></span>点赞<span class="hljs-tag"></<span class="hljs-name">a</span>></span>帮我聚集灵力⭐️。
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        ),
        <span class="hljs-attr">okText</span>: <span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://juejin.cn/user/325111174662855/posts"</span>></span>点赞 o(￣▽￣)ｄ<span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>,
      &#125;);
      <span class="hljs-keyword">break</span>;
    &#125;
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dd7dd37db954d84925ac1c0f60cb965~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-34">webview 传递信息给插件</h3>
<p>webview 反向传递信息给插件的原理也是一样的，只不过由于 webview 的上下文限制，我们只能通过 <code>acquireVsCodeApi</code> 函数获取阉割版的 VS Code API 对象，这个阉割的对象上有一个 <code>postMessage</code> 函数可以供我们发送事件用。注意 <code>acquireVsCodeApi</code> 个会话中只能调用一次，重复调用会报错。而在插件侧则可以通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Finterfaces%2FWebview.html%23onDidReceiveMessage" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/interfaces/Webview.html#onDidReceiveMessage" ref="nofollow noopener noreferrer">Webview.onDidReceiveMessage</a> 处理 webview 传递的信息。我们来写一个在 webview 中调用 <code>vscode.window.showInformationMessage</code> 的例子：</p>
<p><strong>webview 侧</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> vscode = acquireVsCodeApi();
vscode.postMessage(&#123;
  <span class="hljs-attr">method</span>: <span class="hljs-string">'showMessage'</span>,
  <span class="hljs-attr">params</span>: &#123;
    <span class="hljs-attr">text</span>: <span class="hljs-string">`为人民服务`</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>插件侧</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 处理 webview 中的信息</span>
currentPanel.webview.onDidReceiveMessage(
  <span class="hljs-function"><span class="hljs-params">message</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (message.method === <span class="hljs-string">'showMessage'</span>) &#123;
      vscode.window.showInformationMessage(message.params.content);
    &#125;
  &#125;,
  <span class="hljs-literal">undefined</span>,
  context.subscriptions
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c32c8b374b534d6fac1cb552287de6ca~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-35">在 webview 中请求接口</h3>
<p>一开始，我以为这是个轻松的工作，直到遇到跨域半天解决不了后我绝望了，在 <a href="https://juejin.cn/post/6844903966799577101#heading-3" target="_blank" title="https://juejin.cn/post/6844903966799577101#heading-3">VSCode WebView插件（扩展）开发实战</a> 一文中我终于知道了 vscode webview 内部是不允许发送 ajax 请求，所有 ajax 请求都是跨域的，因为 webview 本身是没有 host 的。</p>
<p>人裂开了，这什么鬼呀，我们核心的需求就是请求掘金的接口获取我们的文章列表呀，那我们还有办法吗？答案是肯定的，其实还是借助上面我们提到的通信机制把请求接口的任务交给 vscode 去处理，完事再让 vscode 把数据通过 <code>postMessage</code> 返回给我们，多说无益，我们来看代码：</p>
<p><strong>webview 侧</strong>：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">React.useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// @ts-ignore</span>
  <span class="hljs-keyword">const</span> vscode = <span class="hljs-keyword">typeof</span> acquireVsCodeApi === <span class="hljs-string">'function'</span> ? acquireVsCodeApi() : <span class="hljs-literal">null</span>;
  vscode.postMessage(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'queryPosts'</span>,
  &#125;);
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (method === <span class="hljs-string">'queryPosts'</span>) &#123;
      <span class="hljs-keyword">const</span> message = event.data;
      <span class="hljs-built_in">console</span>.log(message);
    &#125;
  &#125;);
&#125;, []);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>vscode 侧</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 处理 webview 中的信息，并返回接口请求的数据</span>
currentPanel.webview.onDidReceiveMessage(
  <span class="hljs-keyword">async</span> message => &#123;
    <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> events(message);
    currentPanel?.webview.postMessage(&#123; data &#125;);
  &#125;,
  <span class="hljs-literal">undefined</span>,
  context.subscriptions
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">@luozhu/vscode-channel</h3>
<p>前面我们知道了使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Finterfaces%2FWebview.html%23postMessage" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/interfaces/Webview.html#postMessage" ref="nofollow noopener noreferrer">Webview.postMessage</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Finterfaces%2FWebview.html%23onDidReceiveMessage" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/interfaces/Webview.html#onDidReceiveMessage" ref="nofollow noopener noreferrer">Webview.onDidReceiveMessage</a>、<code>acquireVsCodeApi().postMessage</code> 和 <code>window.addEventListener</code> 就可以满足各种通信需求了，那 <code>@luozhu/vscode-channel</code> 又是什么呢？</p>
<p>受 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjs-channel" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/js-channel" ref="nofollow noopener noreferrer">js-channel</a> 启发，<code>@luozhu/vscode-channel</code> 主要是封装了 webview 与 vscode 交互流程，核心原理是通过暴露 <code>call</code>、<code>bind</code> 方法抹平 API 的差异，减少重复代码量。其中参考 appworks 和 cs-channel 使用 uuid 保证交互的可靠性。Talk is cheap, show you the code：</p>
<p><strong>webview 侧</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 创建 channel 对象</span>
<span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> Channel();
<span class="hljs-keyword">const</span> getData = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-comment">// 发起一个请求，并等待其返回数据</span>
  <span class="hljs-keyword">const</span> &#123; payload &#125; = <span class="hljs-keyword">await</span> channel.call(&#123; <span class="hljs-attr">method</span>: <span class="hljs-string">'queryPosts'</span> &#125;);
  <span class="hljs-built_in">console</span>.log(payload);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>webview 中由于 acquireVsCodeApi 只能调用一次，之后又需要在多个地方使用，所以我们在 <code>wev/src/layouts/index.ts</code> 中创建一次并挂载到 <code>window</code> 对象上比较合适。</p>
</blockquote>
<p><strong>vscode 侧</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// vscode 侧的 channel 需要依赖上下文和 WebviewPanel 实例</span>
<span class="hljs-keyword">const</span> channel = <span class="hljs-keyword">new</span> Channel(context, currentPanel);
<span class="hljs-comment">// 绑定一个回调函数，一般只需要创建一个，然后根据约定做分发即可</span>
channel.bind(<span class="hljs-keyword">async</span> message => &#123;
  <span class="hljs-keyword">const</span> &#123; eventType, method, params &#125; = message;
  <span class="hljs-comment">// 实际发起请求获取数据的地方</span>
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> events[eventType][method](params);
  <span class="hljs-comment">// 这里将获取的数据直接返回即可，channel 内部会进行消息合并和回传。</span>
  <span class="hljs-comment">// 如果只是执行一个功能，不写 return 语句即可，内部会进行判断降级成单工通信。</span>
  <span class="hljs-keyword">return</span> data;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">vscode 国际化</h2>
<p>我们都知道 vscode 中是可以切换语言环境的，一款优秀的 vscode 扩展至少要支持中英两种语言。而且支持国际化可以让你的插件受众直接突破国界限制。vscode 国际化分为三部分，一部分是配置的国际化，一部分是代码中的国际化，另一部分则是 webview 中 umijs 的国际化。本章我们就来具体看一下如何在 vscode 中实现国际化。</p>
<h3 data-id="heading-38">配置国际化</h3>
<p>我们已经知道 vscode 中的配置都是在 <em>package.json</em> 中，而配置的国际化是约定在 <code>package.nls.json</code> 和 <code>package.nls.zh-cn.json</code> 这种文件中编写。比如我们要在中英文环境下命令配置中英文版本，我们可以在 <code>package.nls.json</code> 中写：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes.category.juejin-me"</span>: <span class="hljs-string">"Juejin Me"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>package.nls.zh-cn.json</code> 写：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes.category.juejin-me"</span>: <span class="hljs-string">"掘金一下"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后 <code>package.json</code> 中写：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"commands"</span>: [
      &#123;
        ...
        <span class="hljs-attr">"category"</span>: <span class="hljs-string">"%contributes.category.juejin-me%"</span>
      &#125;,
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-39">代码中国际化</h3>
<p>推荐使用洛竹贡献过代码的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faxetroy%2Fvscode-nls-i18n" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/axetroy/vscode-nls-i18n" ref="nofollow noopener noreferrer">vscode-nls-i18n</a>，使用方法也很简单，配置的话和上一节一样，在 <code>src/extension.ts</code> 中使用 <code>init</code> 方法初始化，然后使用 <code>localize</code> 方法实现国际化：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; init, localize &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode-nls-i18n'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">context: vscode.ExtensionContext</span>) </span>&#123;
  init(context.extensionPath); <span class="hljs-comment">// 初始化国际化配置。只用在扩展激活时初始化一次</span>
  <span class="hljs-built_in">console</span>.log(localize(<span class="hljs-string">'extension.activeLog'</span>)); <span class="hljs-comment">// 之后就可以在各个文件中使用。</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">umijs 国际化</h3>
<p>umijs 的国际化需要使用 <code>@umijs/plugin-locale</code> 插件支持，这个插件封装了 <code>react-intl</code>，配置方式如下：</p>
<p>1、.umirc.ts 中配置 <code>local</code></p>
<pre><code class="hljs language-ts copyable" lang="ts">locale: &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、在 <em>src</em> 目录下创建 <code>locales</code> 并创建 <code>en.ts</code> 或 <code>zh-CN.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// src/locales/en.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">WELCOME_TO_UMI_WORLD</span>: <span class="hljs-string">"welcome to umi's world"</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// src/locales/zh-CN.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">WELCOME_TO_UMI_WORLD</span>: <span class="hljs-string">'欢迎光临  umi  的世界'</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、使用国际化</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; useIntl &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'umi'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>: React.FunctionComponent = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> intl = useIntl()
  <span class="hljs-keyword">return</span> (
     <div>
     &#123;intl.formatMessage(
        &#123;
          <span class="hljs-attr">id</span>: <span class="hljs-string">'WELCOME_TO_UMI_WORLD'</span>,
        &#125;
      )&#125;<div>
   )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、切换语言</p>
<p>切换语言，我们需要使用 <code>setLocale</code> 方法，需要注意的是我们给这个方法第二个参数传入 <code>false</code> 来实现无刷新动态切换。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; setLocale &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'umi'</span>;
<span class="hljs-comment">// 不刷新页面</span>
setLocale(<span class="hljs-string">'zh-CN'</span>, <span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过，切换语言的时机在什么时候呢？切换时机就是我们语言环境改变的时机。在 vscode webview 环境中，其实当使用 <code>Config display language</code> 方法切换语言环境后，会要求 vscode 重启。也就说我们只需要在 webview 创建时设置一次语言环境即可。由于 vscode 和 webview 传值太困难，我们选择在 <code>getUmiHTMLContent</code> 时传如 <code>vscode.env</code>：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">window</span>.vscodeEnv = $&#123;<span class="hljs-built_in">JSON</span>.stringify(vscode.env)&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们在 <code>web/src/layouts/index.ts</code> 中设置一下即可：</p>
<pre><code class="hljs language-ts copyable" lang="ts">setLocale(<span class="hljs-built_in">window</span>.vscodeEnv.language, <span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">“掘金一下” 扩展核心实现</h2>
<p>灵感来源于现实，作为掘金的重度使用者，几乎每篇文章和笔记都同步在这里。当有些知识忘记需要查阅或拷贝代码时，我就有在掘金搜索我的文章的需求。但是掘金的搜索是全站的，就算加上自己的名字搜索也会出现大量无关记录。“掘金一下” 这个名字就像插件功能一样，在你想搜索自己掘金文章的时候就可以打开插件“掘金一下” 进行搜索。</p>
<p>其实为了只搜索到自己的文章，我想到的还有开发 chrome 插件来实现。但是考虑到市场和便捷性，我最终还是决定开发 vscode 插件来落地这个灵感。本章就是综合前面的经验实现 “掘金一下” 的核心逻辑。</p>
<h3 data-id="heading-42"><code>juejin-me.start</code> 命令</h3>
<h4 data-id="heading-43">vscode 侧开启 channel 通信</h4>
<p>vscode 侧通过 <code>channel.bind</code> 绑定一个事件处理函数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> events <span class="hljs-keyword">from</span> <span class="hljs-string">'./events'</span>;
...
context.subscriptions.push(
  vscode.commands.registerCommand(<span class="hljs-string">'juejin-me.start'</span>, <span class="hljs-keyword">async</span> () => &#123;
    currentPanel = createUmiWebviewPanel(
      context,
      <span class="hljs-string">'juejin-me'</span>,
      localize(<span class="hljs-string">'extension.webview-panel.title'</span>),
      <span class="hljs-string">'assets/icon-luozhu.png'</span>,
      <span class="hljs-string">'3.5.17'</span>
    );
    <span class="hljs-comment">// 处理 webview 中的信息</span>
    channel = <span class="hljs-keyword">new</span> Channel(context, currentPanel);
    channel.bind(<span class="hljs-keyword">async</span> message => &#123;
      <span class="hljs-keyword">const</span> &#123; eventType, method, params &#125; = message;
      <span class="hljs-comment">// 根据事件类型、方法、参数来完成一次 api 调用，内置的 eventType 有 request、command 和 variable。</span>
      <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> events[eventType][method](params);
      <span class="hljs-keyword">return</span> data;
    &#125;, vscode);
  &#125;)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：我们不需要给定监听事件名，内部会根据 eventId 保证可靠性和全局唯一性</p>
</blockquote>
<h4 data-id="heading-44">注册 events</h4>
<p><strong>events/index.ts</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> requests <span class="hljs-keyword">from</span> <span class="hljs-string">'./requests'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">request</span>: requests,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>events/requests</strong>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;
<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">'../utils/request'</span>;

<span class="hljs-keyword">const</span> queryPosts = <span class="hljs-keyword">async</span> (params: &#123; <span class="hljs-attr">cursor</span>: <span class="hljs-built_in">string</span> &#125;): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">any</span>> => &#123;
  <span class="hljs-comment">// 这里我们根据 vscode 配置动态取的用户 id</span>
  <span class="hljs-keyword">const</span> &#123; userId &#125; = vscode.workspace.getConfiguration(<span class="hljs-string">'juejin-me'</span>);

  <span class="hljs-keyword">const</span> &#123; cursor &#125; = params;
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> request.post(<span class="hljs-string">'/article/query_list'</span>, &#123;
    <span class="hljs-attr">cursor</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;cursor&#125;</span>`</span>,
    <span class="hljs-attr">sort_type</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">user_id</span>: userId,
  &#125;);
  <span class="hljs-keyword">return</span> data;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  queryPosts,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>utils/request</strong>：</p>
<p>这里简单封装了基于 axios 的请求对象。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/* eslint-disable no-param-reassign */</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>;
<span class="hljs-keyword">import</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;
<span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;

<span class="hljs-comment">// 中文文档: http://t.cn/ROfXFuj</span>
<span class="hljs-comment">// 创建实例</span>
<span class="hljs-keyword">const</span> request = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'https://api.juejin.cn/content_api/v1/'</span>,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">10000</span>,
&#125;);

<span class="hljs-comment">// 添加请求拦截器</span>
request.interceptors.request.use(
  <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (config.method === <span class="hljs-string">'get'</span>) &#123;
      config.paramsSerializer = <span class="hljs-function"><span class="hljs-params">params</span> =></span> qs.stringify(params, &#123; <span class="hljs-attr">arrayFormat</span>: <span class="hljs-string">'repeat'</span> &#125;);
    &#125;
    <span class="hljs-keyword">return</span> config;
  &#125;,
  <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    vscode.window.showErrorMessage(error.message);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;
);

<span class="hljs-comment">// 添加响应拦截器</span>
request.interceptors.response.use(
  <span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; data &#125; = response;
    <span class="hljs-keyword">return</span> data;
  &#125;,
  <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    vscode.window.showErrorMessage(error.message);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
  &#125;
);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> request;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45">webview 中调用接口</h3>
<p>channel 是在 <code>web/src/layouts/index.tsx</code> 中初始化并挂载到 window 上的，我们在 <code>web/src/pages/index.tsx</code> 中调用 <code>window.channel.call</code> 即可调用指定接口。由于我们需要模糊搜索所有的文章，所以我们需要在初始化页面时一次请求完所有数据。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> Homepage = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> getData = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> &#123; payload &#125; = (<span class="hljs-keyword">await</span> <span class="hljs-built_in">window</span>.channel.call(&#123;
      <span class="hljs-attr">eventType</span>: <span class="hljs-string">'request'</span>,
      <span class="hljs-attr">method</span>: <span class="hljs-string">'queryPosts'</span>,
      <span class="hljs-attr">params</span>: &#123; cursor &#125;,
    &#125;)) <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>;
    tempData = tempData.concat(payload.data);
    setData(tempData);
    <span class="hljs-keyword">if</span> (!payload.has_more) &#123;
      setInitLoading(<span class="hljs-literal">false</span>);
      setCategories(_union([<span class="hljs-string">'全部'</span>, ...tempData.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.category.category_name)]));
      tempData = [];
    &#125; <span class="hljs-keyword">else</span> &#123;
      cursor += <span class="hljs-number">10</span>;
      getData();
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多具体实现细节就是一些页面编写逻辑，不是本文的重点，感兴趣的同学可以直接进查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyoungjuning%2Fjuejin-me%2Ftree%2Fmain%2Fweb" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/youngjuning/juejin-me/tree/main/web" ref="nofollow noopener noreferrer">源码</a>。</p>
<h3 data-id="heading-46">配置掘金 ID</h3>
<p><strong>声明配置</strong>：</p>
<p>vscode 的配置我们需要借助 package.json 的 <code>contributes.configuration</code> 属性，我们的掘金 ID 是 string，所以声明如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"configuration"</span>: &#123;
      <span class="hljs-attr">"title"</span>: <span class="hljs-string">"%configuration.title%"</span>,
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"object"</span>,
      <span class="hljs-attr">"properties"</span>: &#123;
        <span class="hljs-attr">"juejin-me.userId"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
          <span class="hljs-attr">"default"</span>: <span class="hljs-string">"325111174662855"</span>,
          <span class="hljs-attr">"description"</span>: <span class="hljs-string">"%configuration.properties.juejin-me.userId%"</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>修改配置的命令</strong>：</p>
<p>让用户打开设置去修改配置也可以，但是为了用户体验，我们提供了 <code>juejin-me.configUserId</code> 命令，我们来看下命令的实现：</p>
<pre><code class="hljs language-ts copyable" lang="ts">context.subscriptions.push(
  vscode.commands.registerCommand(<span class="hljs-string">'juejin-me.configUserId'</span>, <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> userId = <span class="hljs-keyword">await</span> vscode.window.showInputBox(&#123;
      <span class="hljs-attr">placeHolder</span>: localize(<span class="hljs-string">'extension.juejin-me.configUserId.placeHolder'</span>),
      <span class="hljs-attr">validateInput</span>: <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (value) &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;
        <span class="hljs-keyword">return</span> localize(<span class="hljs-string">'extension.juejin-me.configUserId.validateInput'</span>);
      &#125;,
    &#125;);
    <span class="hljs-keyword">const</span> config = vscode.workspace.getConfiguration(<span class="hljs-string">'juejin-me'</span>);

    config.update(<span class="hljs-string">'userId'</span>, userId, <span class="hljs-literal">true</span>);
  &#125;)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Fmodules%2Fwindow.html%23showInputBox" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/modules/window.html#showInputBox" ref="nofollow noopener noreferrer">vscode.window.showInputBox</a>：打开一个输入框，提示用户输入掘金用户 ID</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Fmodules%2Fworkspace.html%23getConfiguration" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/modules/workspace.html#getConfiguration" ref="nofollow noopener noreferrer">vscode.workspace.getConfiguration</a>：获取工作空间的配置对象</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Finterfaces%2FWorkspaceConfiguration.html%23update" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/interfaces/WorkspaceConfiguration.html#update" ref="nofollow noopener noreferrer">WorkspaceConfiguration.update</a>：更新一个配置值。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2Finterfaces%2FInputBoxOptions.html%23validateInput" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/interfaces/InputBoxOptions.html#validateInput" ref="nofollow noopener noreferrer">InputBoxOptions.validateInput</a>：一个可选的函数，被调用来验证输入信息并提示用户</li>
</ul>
<h3 data-id="heading-47">插件效果展示</h3>
<p>感兴趣的话你也可以直接在扩展中搜索“掘金一下”自行体验。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac7d2ab498b2469486e8f237fc3b7997~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91ae0fdbff7043db9513e539640fcc2e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-48">彩蛋</h2>
<h3 data-id="heading-49">@luozhu/create-vscode-webview</h3>
<p>本文中有很多最佳实践，为了方便之后创建新的项目时减少重复工作，洛竹抽离出了一个简单的模板。掘友直接使用 <code>yarn create @luozhu/vscode-webview  myvscode</code> 即可创建出一个属于自己的 vscode 扩展。参考本文的一些实践再加一些你的创意即可完成一个出色的基于 webview 的 vscode 扩展。</p>
<h3 data-id="heading-50">Word Count Juejin</h3>
<p>为了答谢掘金平台和掘友一直以来的支持，我编写了一款专为掘金适配的 Markdown 文件字数统计 VS Code 扩展，字数统计会实时显示在状态栏。比起来 vscode 官方的 Word Count，我们支持中文字数统计，比起来 Word Count CJK，我们支持中英文混排。如果你也喜欢使用 VS Code 的 Markdown 编辑能力，那么一定不要错过洛竹的这款插件，下载请认准：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08c060326c954849b3eb2d34f2e6b0e5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你还在犹豫要不要下载，那不妨看下三个插件的统计对比，我们拿 <code>i love juejin. 我爱掘金</code> 这个字符串测试一下三款插件的功能：</p>




















<table><thead><tr><th>Word Count</th><th>Word Count CJK</th><th>Word Count Juejin</th></tr></thead><tbody><tr><td>4 个字</td><td>4 个字</td><td>7 个字</td></tr><tr><td>中文算成了一个字</td><td>直接忽略了英文</td><td>中文4 个字加英文三个字，格局正好</td></tr></tbody></table>
<h3 data-id="heading-51">vscode api cn</h3>
<p>在学习和开发 vscode 插件的过程中，最大的痛点无过于 API 文档翻译的缺失。哪怕是硬着头皮看英文原版 API 文档，阅读体验也很差。为了方便自己、回馈社区，我和 <a href="https://juejin.cn/user/703340610597064" target="_blank" title="https://juejin.cn/user/703340610597064">寒草</a> 等小伙伴决定翻译 vscode api 类型声明并使用 Typedoc 承载，另外在完工后我们也会输出 <code>@types/vscode-cn</code> 类型包代替 <code>@types/vscode</code> 进一步方便 vscode 插件开发者。团队成员现状：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa80c1603b2e4482883fe39e1b44f62e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>翻译是一件带有侠义精神的事业，欢迎更多的小伙伴加入我们。你可以浏览<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvscode-cn%2Fvscode-api-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vscode-cn/vscode-api-cn" ref="nofollow noopener noreferrer">仓库</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvscode-api-cn.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vscode-api-cn.js.org/" ref="nofollow noopener noreferrer">官网</a>了解具体情况。</p>
<h2 data-id="heading-52">后记</h2>
<p>这是第一次尝试写这么长的文章，断断续续经历了有半个月，本着对读者负责任的态度，文中的实践都是经过反复测试以及和同事朋友的讨论。当然 vscode 插件开发的概念和 API 比较多，一篇文章也很难讲全，讲透彻。如果大家感兴趣，可以在评论区告诉洛竹，我可以继续更新这方面的教程。</p>
<h2 data-id="heading-53">近期好文</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fis.gd%2Fr8XEZQ" target="_blank" rel="nofollow noopener noreferrer" title="https://is.gd/r8XEZQ" ref="nofollow noopener noreferrer">vscode 插件发布</a></li>
<li><a href="https://juejin.cn/post/6990511054224621598" target="_blank" title="https://juejin.cn/post/6990511054224621598">前端组件化实战之 Button</a></li>
<li><a href="https://juejin.cn/post/6983854006124675108" target="_blank" title="https://juejin.cn/post/6983854006124675108">每个前端都值得拥有自己的组件库，就像每个夏天都拥有西瓜🍉</a></li>
<li><a href="https://juejin.cn/post/6969544464113074189" target="_blank" title="https://juejin.cn/post/6969544464113074189">基于 lerna 的多包 JavaScript 项目搭建维护</a></li>
<li><a href="https://juejin.cn/post/6877462747631026190" target="_blank" title="https://juejin.cn/post/6877462747631026190">一文搞定 Conventional Commits</a></li>
<li><a href="https://juejin.cn/post/6955402195311263751" target="_blank" title="https://juejin.cn/post/6955402195311263751">2021 年最值得使用的 Node.js 框架</a></li>
<li><a href="https://juejin.cn/column/6972556324022255624" target="_blank" title="https://juejin.cn/column/6972556324022255624">React 面试必知必会系列</a></li>
<li><a href="https://juejin.cn/column/6962102040684134436" target="_blank" title="https://juejin.cn/column/6962102040684134436">Go 语言教程系列</a></li>
</ul>
<blockquote>
<p>本文首发于「掘金专栏」，同步于公众号「程序人生」。</p>
</blockquote></div>  
</div>
            