
---
title: 'NVS —— js 实现的node版本管理工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a12dd9d85b444f6ebec2b21d0f0e41a1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 12 May 2021 23:57:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a12dd9d85b444f6ebec2b21d0f0e41a1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：未见</p>
<h2 data-id="heading-0">NVS (Node Version Switcher)</h2>
<p>NVS 是一个跨平台的 Node.js 的版本切换工具，并且 NVS 本身是用<a href="http://nodejs.org/" title="**Node.js**" target="_blank" rel="nofollow noopener noreferrer">Node.js</a>编写的。</p>
<p>这个工具显然是受到其他 Node.js 版本管理器工具的启发，特别是<a href="https://github.com/creationix/nvm" title="**nvm**" target="_blank" rel="nofollow noopener noreferrer">nvm</a>，它借鉴了很多思想和一些命令行语法。</p>
<p>以下是基本的设置说明。<a href="https://gitee.com/wsz7777/nvs/tree/gitee/doc/SETUP.md" title="有关设置 NVS 的更多细节和选项，请参阅设置页面。" target="_blank" rel="nofollow noopener noreferrer">有关设置 NVS 的更多细节和选项，请参阅设置页面。</a></p>
<h3 data-id="heading-1">Windows</h3>
<p>windows 的 MSI 安装包可以从<a href="https://github.com/wsz7777/nvs/releases" title="NVS releases page on GitHub" target="_blank" rel="nofollow noopener noreferrer">NVS releases page on GitHub</a>这里获得。<br>
你也可以通过<a href="https://chocolatey.org/" title="chocolatey" target="_blank" rel="nofollow noopener noreferrer">chocolatey</a>安装:</p>
<pre><code class="copyable">choco install nvs
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Mac, Linux</h3>
<p>指定安装路径，克隆 repo，并输入安装命令：</p>
<pre><code class="copyable">export NVS_HOME="$HOME/.nvs"
git clone https://gitee.com/wsz7777/nvs "$NVS_HOME"
. "$NVS_HOME/nvs.sh" install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个<code>nvs.sh</code>是向环境变量中添加<code>nvs</code>的 shell 方法. 执行这个脚本后，你就可以在命令行中直接使用<code>nvs</code>了。 请添加这个<code>install</code>命令至<code>~/.bashrc</code>,<code>~/.profile</code>, 或者<code>~/.zshrc</code>文件中。 以便该<code>nvs</code>功能在你的 shell 中可用.</p>
<p>对于 ksh, 这个脚本<code>nvs.sh</code>需要添加到<code>~/.kshrc</code>中，或者是<code>$ENV</code>的地方。</p>
<h3 data-id="heading-3">CI 支持</h3>
<p><a href="https://gitee.com/wsz7777/nvs/tree/gitee/doc/CI.md" title="NVS can be used in a CI environment" target="_blank" rel="nofollow noopener noreferrer">NVS can be used in a CI environment</a>可以在 Travis CI 中使用。 去使用 NVS 测试下载任何版本的 Node.js 环境。</p>
<h2 data-id="heading-4">基础使用</h2>
<p>下载最新版本的 Node.js：</p>
<pre><code class="copyable">$ nvs add latest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载 lts 版本的 Node.js：</p>
<pre><code class="copyable">$ nvs add lts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行<code>nvs use</code>去选择 Node.js 的版本</p>
<pre><code class="copyable">$ nvs use lts
PATH += ~/.nvs/node/6.9.1/x64
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>nvs link</code>添加默认的 Node.js 版本：</p>
<pre><code class="copyable">$ nvs link lts
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Command 介绍</h2>

























































































<table><thead><tr><th>命令</th><th>描述</th></tr></thead><tbody><tr><td><code>nvs help <command></code></td><td>获取命令的详细帮助</td></tr><tr><td><code>nvs install</code></td><td>初始化并使用 NVS</td></tr><tr><td><code>nvs uninstall</code></td><td>从 profile 和 environment 中移除 NVS</td></tr><tr><td><code>nvs --version</code></td><td>展示 NVS 版本</td></tr><tr><td><code>nvs add [version]</code></td><td>下载某个版本的 Node.js</td></tr><tr><td><code>nvs rm <version></code></td><td>移除某个版本的 Node.js</td></tr><tr><td><code>nvs migrate <fromver> [tover]</code></td><td>迁移全局的 node_modules</td></tr><tr><td><code>nvs upgrade [fromver]</code></td><td>更新当前环境的 Node.js 至最新版本</td></tr><tr><td><code>nvs use [version]</code></td><td>选择使用某个版本的 Node.js</td></tr><tr><td><code>nvs auto [on/off]</code></td><td>使用 cwd 自动切换</td></tr><tr><td><code>nvs run <ver> <js> [args...]</code></td><td>使用 Node.js 的某个版本的去执行 js 应用</td></tr><tr><td><code>nvs exec <ver> <exe> [args...]</code></td><td>使用 Node.js 的某个版本的去执行 可执行文件</td></tr><tr><td><code>nvs which [version]</code></td><td>显示 Node.js 的某个版本的二进制文件的路径</td></tr><tr><td><code>nvs ls [filter]</code></td><td>展示本地下载的 Node.js 版本列表</td></tr><tr><td><code>nvs ls-remote [filter]</code></td><td>列出可下载的 Node.js 版本</td></tr><tr><td><code>nvs lsr [filter]</code></td><td>同上</td></tr><tr><td><code>nvs link [version]</code></td><td>设置一个软连接指向一个版本，作为默认使用的版本</td></tr><tr><td><code>nvs unlink [version]</code></td><td>删除指向默认版本的链接</td></tr><tr><td><code>nvs alias [name] [value]</code></td><td>给某个版本设置一个别名</td></tr><tr><td><code>nvs remote [name] [value]</code></td><td>设置下载 node 的仓库</td></tr></tbody></table>
<p><code>[version]</code>和<code>[filter]</code>是用来描述版本的，有以下一些情况</p>





























<table><thead><tr><th>情况</th><th>例子</th></tr></thead><tbody><tr><td>完整的版本号</td><td>15.14.0、0.6.11</td></tr><tr><td>不完整版本号</td><td>14、15、8</td></tr><tr><td>标签</td><td>lts, latest, Argon</td></tr><tr><td>远程安装仓库名</td><td>node、node/15.12.0 。 如果使用 nvs remote 添加了远程仓库名为 taobao 那就可以使用 taobao、taobao/15.13.0</td></tr><tr><td>远程仓库名斜线后的部分</td><td>lts, 4.6.0, 6/x86, node/6.7/x64</td></tr></tbody></table>
<p>大概是这样，可以自行发掘更多用法有关每个命令的更多详细信息<a href="https://gitee.com/wsz7777/nvs/tree/gitee/doc" title="请参阅文档" target="_blank" rel="nofollow noopener noreferrer">请参阅文档</a></p>
<h2 data-id="heading-6">互动菜单</h2>
<p>不带参数调用时，将<code>nvs</code>显示一个交互式菜单，用于切换和下载 Node.js 版本。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a12dd9d85b444f6ebec2b21d0f0e41a1~tplv-k3u1fbpfcp-zoom-1.image" alt="nvs-menu.gif" loading="lazy" referrerpolicy="no-referrer"><em>NVS 使用<a href="https://gitee.com/wsz7777/console-menu" title="**console-menu**" target="_blank" rel="nofollow noopener noreferrer">console-menu</a>, 最初 console-menu 是为该项目编写的，然后单独发布。</em></p>
<h2 data-id="heading-7">VS Code 支持</h2>
<p>Visual Studio Code 可以使用 NVS 选择启动或调试时要使用的 Node.js 版本。在<code>launch.json</code>（<code>.vscode</code>位于项目根文件夹中的文件夹中）中，添加<code>"runtimeArgs"</code>带有 NVS 版本字符串的<code>"runtimeExecutable"</code>属性 ，以及指向<code>nvs.cmd</code>（Windows）或<code>nvs</code>（Mac, Linux）。 (如果 NVS 不在 VS Code 的 PATH 环境变量中，您可能需要指定一个绝对路径，例如<code>"$&#123;env:HOME&#125;/.nvs/nvs"</code>)</p>
<p>配置示例：<code>launch.json</code>使用 VS Code 使用 NVS 启动 Node.js 版本 6.10:</p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"configurations"</span>: [
    &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"node"</span>,
      <span class="hljs-attr">"request"</span>: <span class="hljs-string">"launch"</span>,
      <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Launch Program"</span>,
      <span class="hljs-attr">"program"</span>: <span class="hljs-string">"$&#123;file&#125;"</span>,
      <span class="hljs-attr">"args"</span>: [ ],
      <span class="hljs-attr">"runtimeArgs"</span>: [ <span class="hljs-string">"6.10"</span> ],
      <span class="hljs-attr">"windows"</span>: &#123; <span class="hljs-attr">"runtimeExecutable"</span>: <span class="hljs-string">"nvs.cmd"</span> &#125;,
      <span class="hljs-attr">"osx"</span>: &#123; <span class="hljs-attr">"runtimeExecutable"</span>: <span class="hljs-string">"nvs"</span> &#125;,
      <span class="hljs-attr">"linux"</span>: &#123; <span class="hljs-attr">"runtimeExecutable"</span>: <span class="hljs-string">"nvs"</span> &#125;
    &#125;,
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，从中删除版本字符串，<code>"runtimeArgs"</code>从<code>.node-version</code>文件或文件夹中获取版本。 有关更多详细信息，请参见<a href="https://gitee.com/wsz7777/nvs/tree/gitee/doc/VSCODE.md" title="NVS VS Code 文档" target="_blank" rel="nofollow noopener noreferrer">NVS VS Code 文档</a>或者执行命令<code>nvs help vscode</code>.</p>
<h2 data-id="heading-8">配置 remotes</h2>
<p><code>nvs remote</code>命令允许配置多个命名的下载位置。NVS 分别管理来自不同远程位置的版本，因此没有版本冲突的风险。默认情况下，只有一个远程指向 Node.js 官方版本：</p>
<pre><code class="copyable">$ nvs remote
default  node
node     https://npm.taobao.org/mirrors/node/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以从其他来源获得构建。以下命令序列为 nightly 添加了一个远程 remote，列出了 nightly ，并添加了一个构建：</p>
<pre><code class="copyable">$ nvs remote add nightly https://nodejs.org/download/nightly/
$ nvs lsr nightly/13
nightly/13.1.1-nightly20191120c7c566023f
...
$ nvs add nightly/13
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加其他 remote:</p>
<pre><code class="copyable">nvs remote add iojs https://iojs.org/dist/
nvs remote add chakracore https://nodejs.org/download/chakracore-release/
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">别名</h2>
<p>别名是指远程名称和语义版本的组合。（不对处理器体系结构进行别名。）设置别名时，可以省略远程名称，在这种情况下，别名是指默认的远程。在其他任何命令中，都可以使用别名代替版本字符串。</p>
<pre><code class="copyable">$ nvs alias myalias 6.7.0
$ nvs alias
myalias default/6.7.0
$ nvs run myalias --version
v6.7.0
$ nvs which myalias
~/.nvs/node/6.7.0/x64/bin/node
$ nvs which myalias/32
~/.nvs/node/6.7.0/x86/bin/node
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://gitee.com/wsz7777/nvs/tree/gitee/doc/ALIAS.md#aliasing-directories" title="别名也可以引用本地目录" target="_blank" rel="nofollow noopener noreferrer">别名也可以引用本地目录</a>，从而使 NVS 可以切换到 Node.js 的本地私有版本。</p>
<h2 data-id="heading-10">根据目录自动切换版本</h2>
<p>在 Bash 或 PowerShell 中，NVS 可以在更改目录时自动切换当前 Shell 中的 Node.js 版本。默认情况下，此功能处于禁用状态。使它运行<code>nvs auto on</code>。之后，无论何时<code>cd</code>或<code>pushd</code>在包含<code>.node-version</code>或<a href="https://github.com/nvm-sh/nvm#nvmrc" title="`.nvmrc`" target="_blank" rel="nofollow noopener noreferrer">.nvmrc</a>文件的目录下，NVS 都会相应地自动切换 Node.js 版本，并在必要时下载新版本。当您<code>cd</code>到达目录上方没有目录<code>.node-version</code>或<code>.nvmrc</code>文件的目录时，将还原默认（链接）版本（如果有）。</p>
<pre><code class="copyable">~$ nvs link 6.9.1
~/.nvs/default -> ~/.nvs/node/6.9.1/x64
~$ nvs use
PATH += ~/.nvs/default/bin
~$ nvs auto on
~$ cd myproject
PATH -= ~/.nvs/default/bin
PATH += ~/.nvs/node/4.6.1/x64/bin
~/myproject$ cd ..
PATH -= ~/.nvs/node/4.6.1/x64/bin
PATH += ~/.nvs/default/bin
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>Windows 命令提示符中不提供此功能。请用 PowerShell。</em></p>
<h2 data-id="heading-11">手动切换使用<code>.node-version</code></h2>
<p>如果您的外壳与自动切换不兼容，或者您 ​​ 希望手动切换但仍利用其中的任何一个<code>.node-version</code>or<code>.nvmrc</code>文件，则可以<code>nvs use</code>使用该版本运行，也可以<code>auto</code>直接运行<code>nvs auto</code>.</p>
<pre><code class="copyable">$ nvs use auto
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于</p>
<pre><code class="copyable">$ nvs auto
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">如何运行的</h1>
<h2 data-id="heading-13">Bootstrapping node</h2>
<p>NVS 使用特定于平台的<code>shell</code>程序代码是比较少的，这些代码通过自动下载 Node.js 的私有副本来引导工具。引导代码仅是 Windows 命令脚本，Windows powershell 脚本和几十行的 POSIX shell 脚本。除引导程序外，shell 脚本还用于将 PATH 更改导出到调用 shell（单独的 Node.js 进程无法执行）。但是，所有用于查询可用版本，下载和安装 Node.js 以及匹配 npm ，切换版本/体系结构/引擎，卸载，解析和更新 PATH 等的代码都可以用 JavaScript 编写，并且大多数都是以跨平台的方式编写的。</p>
<h2 data-id="heading-14">版本切换</h2>
<p>NVS 下载 Node.js 版本在<code>NVS_HOME</code>环境变量指定的目录下，或者在<code>NVS_HOME</code>未设置的 NVS 工具目录下。例如，每个构建都位于基于远程名称，语义版本和体系结构的子目录中<code>node/6.7.0/x64</code>.</p>
<p>当您使用<code>nvs use</code>一个版本时， 当前<code>shell</code>的会更新<code>PATH</code>为包括该版本的<code>bin</code>目录.</p>
<h2 data-id="heading-15">全局模块</h2>
<p>与 NVS 安装的 Node.js 一起使用<code>npm install -g</code>or<code>npm link</code>与之配合使用时，将安装全局模块或将其链接到特定于版本的目录中。（NVS 清除<code>NPM_CONFIG_PREFIX</code>可能已设置的任何环境变量。）这意味着，在 NVS 切换版本时，它也在切换可用的全局模块集。该<code>nvs migrate</code>命令可以将这些全局模块从一个 Node.js 版本迁移到另一 Node.js 版本。</p>
<h2 data-id="heading-16">Symbolic 链接</h2>
<p><code>nvs link</code>命令在<code>$NVS_HOME/default</code>指向指定版本（或命令时的当前版本）的位置创建符号目录链接<code>PATH</code>。当需要在其他地方配置固定路径时，这很有用。</p>
<p>在非 Windows 平台上，如果存在链接，则提供<code>nvs.sh</code>脚本来源的新外壳程序也将设置<code>PATH</code>为包括默认版本。在 Windows 上，<code>PATH</code>环境变量在用户配置文件中更新，因此新的 Shell 将使用默认版本。</p>
<p><code>nvs ls</code>命令列出所有本地 Node.js 版本，并使用标记当前路径中的版本<code>></code>，并使用标记默认（链接的）版本（如果有）<code>#</code>。这些可以相同或不同。例如：</p>
<pre><code class="copyable">  node/4.5.0/x64
 #node/4.6.0/x64
 >node/6.7.0/x64
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">系统 linking</h2>
<p>如果<code>$NVS_HOME</code>在诸如<code>/usr/local</code>or<code>%ProgramFiles%</code>,<code>nvs link</code>命令还会链接到众所周知的 Node.js 系统位置。（仅当尚无系统安装的 Node.js 时才允许这样做。）</p>
<ul>
<li>
<p>在非 Windows 平台上，为<code>node</code>创建符号链接<code>/usr/local/bin</code>,<code>npm</code>以及具有可执行任何全球安装的 Node.js 模块。请注意，在安装或卸载包含可执行文件的全局模块之后，可能需要再次运行<code>nvs link</code>以更新全局链接。使用 NVS 链接不同版本的 Node.js（具有不同的全局模块）会相应地更新所有链接。</p>
</li>
<li>
<p>在 Windows 上，在创建符号目录链接<code>%ProgramFiles%\Nodejs</code>，并将该目录添加到系统<code>PATH</code>中。</p>
</li>
</ul>
<p>当<code>$NVS_HOME</code>指向非系统目录时，将跳过此系统链接功能，因为在系统目录中创建到用户文件的符号链接是错误的。</p>
<h2 data-id="heading-18">依赖关系</h2>
<p>除了自动下载的节点的私有副本之外，NVS 没有任何外部依赖关系。运行时 JS 软件包的相关性很小，并且已在存储库中签入，以避免<code>npm install</code>在引导时需要。</p></div>  
</div>
            