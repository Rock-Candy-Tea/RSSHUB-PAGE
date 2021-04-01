
---
title: '玩转 WSL'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f1a924232bc4a34baf65ef4403d362e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 31 Mar 2021 19:20:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f1a924232bc4a34baf65ef4403d362e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">玩转 WSL</h1>
<p>很早就听说WSL了，作为一名前端一般来说是不需要跟<code>linux</code>打交道的毕竟各种<code>ci</code>都已经可以自动化运行了，但是作为一名程序员我觉得还是有需要了解下我们的代码的运行环境而<code>WSL</code>作为初次接触<code>linux</code>的介质再好不过了。</p>
<h2 data-id="heading-1">一：什么是WSL？</h2>
<p>适用于 Linux 的 Windows 子系统可让开发人员按原样运行 GNU/Linux 环境 - 包括大多数命令行工具、实用工具和应用程序 - 且不会产生传统虚拟机或双启动设置开销。</p>
<p>您可以：</p>
<ul>
<li><a href="https://aka.ms/wslstore" target="_blank" rel="nofollow noopener noreferrer">在 Microsoft Store</a> 中选择你偏好的 GNU/Linux 分发版。</li>
<li>运行常用的命令行软件工具（例如 <code>grep</code>、<code>sed</code>、<code>awk</code>）或其他 ELF-64 二进制文件。</li>
<li>运行 Bash shell 脚本和 GNU/Linux 命令行应用程序，包括：
<ul>
<li>工具：vim、emacs、tmux</li>
<li>语言：<a href="https://docs.microsoft.com/zh-cn/windows/nodejs/setup-on-wsl2" target="_blank" rel="nofollow noopener noreferrer">NodeJS</a>、Javascript、<a href="https://docs.microsoft.com/zh-cn/windows/python/web-frameworks" target="_blank" rel="nofollow noopener noreferrer">Python</a>、Ruby、C/ C++、C# 与 F#、Rust、Go 等。</li>
<li>服务：SSHD、<a href="https://docs.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-database" target="_blank" rel="nofollow noopener noreferrer">MySQL</a>、Apache、lighttpd、<a href="https://docs.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-database" target="_blank" rel="nofollow noopener noreferrer">MongoDB</a>、<a href="https://docs.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-database" target="_blank" rel="nofollow noopener noreferrer">PostgreSQL</a>。</li>
</ul>
</li>
<li>使用自己的 GNU/Linux 分发包管理器安装其他软件。</li>
<li>使用类似于 Unix 的命令行 shell 调用 Windows 应用程序。</li>
<li>在 Windows 上调用 GNU/Linux 应用程序。</li>
</ul>
<p>官方文档：<a href="https://docs.microsoft.com/zh-cn/windows/wsl/install-win10" target="_blank" rel="nofollow noopener noreferrer">docs.microsoft.com/zh-cn/windo…</a></p>
<h2 data-id="heading-2">二：安装</h2>
<h3 data-id="heading-3">1. 启用<code>WSL</code></h3>
<p>以管理员权限打开<code>powershell</code>运行以下命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们用的是命令开启也可以在应用中开启<code>适用于 Linux 的 Windows 子系统</code></p>
<p>如果你希望使用<code>WSL1</code>这样就可以了，这里我们需要更新<code>WSL2</code></p>
<h3 data-id="heading-4">2. 更新<code>WSL2</code></h3>
<p>以管理员身份打开 PowerShell 并运行：</p>
<pre><code class="hljs language-bash copyable" lang="bash">dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是开启虚拟机功能的命令</p>
<p>重新启动计算机，以完成 WSL 安装并更新到 WSL 2</p>
<p>**注：**如果你的<code>cpu</code>没有开启虚拟机功能，那么你需要去<code>bios</code>开启</p>
<h3 data-id="heading-5">3. 下载 Linux 内核更新包</h3>
<p>下载Linux更新包并安装</p>
<p><code>x64</code>构架：</p>
<p><a href="https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi" target="_blank" rel="nofollow noopener noreferrer">wslstorestorage.blob.core.windows.net/wslblob/wsl…</a></p>
<p><code>ARM64</code>构架：</p>
<p><a href="https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_arm64.msi" target="_blank" rel="nofollow noopener noreferrer">wslstorestorage.blob.core.windows.net/wslblob/wsl…</a></p>
<h3 data-id="heading-6">4. 设置<code>WSL2</code>为默认版本</h3>
<pre><code class="hljs language-bash copyable" lang="bash">wsl --set-default-version 2
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">5. 安装Linux发行版</h3>
<p>前往<code>Microsoft Store</code>下载</p>
<p>安装后打开首次需要设置<code>root</code>账户名和密码</p>
<h2 data-id="heading-8">三：设置图形桌面</h2>
<p>安装WSL之后，我们所能看到的Linux 实际上只是个黑框框, 微软并没有为其配置图形界面。</p>
<p>习惯了Window系统的我们可能不太适应。有没办法实现图形桌面环境呢？</p>
<p>当然，主要途径有如下两种：</p>
<blockquote>
<p>1.通过 在win10中安装<code>X server</code>， 及在WSL中安装<code>ubuntu的图形桌面组件</code>直接在win10桌面上显示ubuntu的图形桌面。
2.在WSL中安装并启动<code>xrdp</code>和<code>Xubuntu-desktop</code>等，通过SSH如远程连接服务器一般连接到WSL。</p>
</blockquote>
<p>这里采用第二种方式。</p>
<h3 data-id="heading-9">1. 修改apt源</h3>
<p>自带的软件源在国内连接网速会比较吃力，所以换成国内源，类似镜像站点。</p>
<pre><code class="hljs language-bash copyable" lang="bash">sudo vi /etc/apt/sources.list
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在最上方加入：</p>
<pre><code class="hljs language-bash copyable" lang="bash">deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2. 更新<code>apt</code></h3>
<pre><code class="hljs language-bash copyable" lang="bash">sudo apt update
sudo apt upgrade
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3. 安装<code>xrdp</code></h3>
<pre><code class="hljs language-bash copyable" lang="bash">sudo apt install -y xfce4 xrdp
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>xrdp</code>是一个轻量级ubuntu桌面，里面的应用只能满足基本需求。就好像 ie 于windows一样</p>
<p>安装<code>xfce4</code>过程中会出现选择显示管理DM选择的提示,建议用<code>lightdm</code></p>
<p>如果错过了安装过程中出现的这个向导,那么可以在安装完成后执行下面的命令重新设置DM</p>
<pre><code class="hljs language-bash copyable" lang="bash">sudo dpkg-reconfigure lightdm
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4. 修改<code>xrdp</code>默认端口</h3>
<pre><code class="hljs language-bash copyable" lang="bash">sudo vim /etc/xrdp/xrdp.ini
<span class="hljs-comment"># 修改下面这一行,将默认的3389改成其他端口即可</span>
port=3390
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">5. 为当前用户指定登录session类型</h3>
<pre><code class="hljs language-bash copyable" lang="bash">$ vim ~/.xsession

<span class="hljs-comment"># 写入下面内容(就一行)</span>
xfce4-session
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">6. 启动<code>xrdp</code></h3>
<pre><code class="hljs language-bash copyable" lang="bash">sudo /etc/init.d/xrdp start <span class="hljs-comment"># stop restart</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">7. 远程访问</h3>
<p>在Windows系统中运行<code>mstsc</code>命令打开远程桌面连接,地址输入<code>localhost:3390</code></p>
<p><img alt="image-20210401104550965.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f1a924232bc4a34baf65ef4403d362e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>ok~</p>
<p>大功告成~</p>
<h2 data-id="heading-16">四：<code>Windows Terminal</code></h2>
<p>在<code>Microsoft Store</code>下载后里面自动配置有<code>WSL</code></p>
<p><img alt="image-20210401104719799.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbee9e94262b48c0b6a8757b7c4fd02e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>新命令行和<code>WSL</code>更配哦~</p>
<h2 data-id="heading-17">五：<code>vscode</code>连接<code>WSL</code></h2>
<p>微软全家桶怎么能少得了<code>vscode</code>呢？</p>
<p>其实主要是最近更新的<code>vscode</code>上出现了<code>WSL</code>的标志，才使我对此兴趣大增的。</p>
<p><img alt="image-20210401105340523.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc2bbe8bdefe42bcbdb2bf8ccf3d99f3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>连接也很简单，点击红框中的位置</p>
<p><img alt="image-20210401105437878.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c09896b28942476ba0e999a78addbed4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>选择一项，即可进入了<code>WSL</code>的文件</p>
<p><img alt="image-20210401105613058.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15fa225cd3144e46bf6c14865b28b752~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">六：安装最新版<code>Node</code></h2>
<p>作为前端我们第一世家肯定是安装<code>Node</code>了，可是<code>apt</code>里的版本都是比较低的，我们可以用以下方式来安装最新版<code>Node</code></p>
<h3 data-id="heading-19">1. 安装<code>npm</code></h3>
<pre><code class="hljs language-bash copyable" lang="bash">sudo apt install npm
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">2. 安装<code>n</code>模块</h3>
<blockquote>
<p>注：n 模块是用来安装各种版本的 node 的一个工具。参数 -g 表示全局安装</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">sudo npm install n -g
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">3. 安装长期支持版<code>Node</code></h3>
<pre><code class="hljs language-bash copyable" lang="bash">sudo n lts
<span class="hljs-comment"># 检查版本</span>
node -v
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">4. <code>n</code>模块简介</h3>
<p><code>n</code> 模块可以安装各种版本的 <code>node</code>，非常方便。</p>
<ul>
<li><code>latest</code> – 最新版，但不一定稳定</li>
<li><code>stable</code> – 最新的稳定版，比 <code>latest</code> 老一点，优点是稳定，但不是长期支持版（api 可能会变动）</li>
<li><code>lts</code> – 最新的长期支持版，这是最推荐使用的版本。虽然比 <code>stable</code> 老，但是是长期支持的版本（当然也是稳定版本）。是 long term support 的缩写。</li>
</ul>
<p>可以直接通过版本号，安装制定版本的 node</p>
<pre><code class="hljs language-bash copyable" lang="bash">sudo n [版本号]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过 n 模块的 use 命令，切换版本</p>
<pre><code class="hljs language-bash copyable" lang="bash">sudo n use [版本] <span class="hljs-comment"># 比如 sudo n use lts</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是就可以使用 <code>lts</code> 版本了。</p>
<h2 data-id="heading-23">七：来写代码吧~</h2>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">cd</span> ~ && mkdir web && <span class="hljs-built_in">cd</span> web && mkdir <span class="hljs-built_in">test</span> && <span class="hljs-built_in">cd</span> <span class="hljs-built_in">test</span> && touch index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建完<code>index.js</code>后，初始化<code>npm</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化<code>git</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">git init
touch .gitignore
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把<code>node_modules</code>加入<code>.gitignore</code></p>
<h3 data-id="heading-24">编写代码</h3>
<p>在<code>vscode</code>打开当前<code>wsl</code>目录</p>
<p><img alt="image-20210401110353529.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af5f72d6ee8445a9866c0ccea6f159e7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>先来写一份简单的问答吧~</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image-20210401110523053.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1403cdeca6c84375a6e481521e890608~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>nice~</p>
<p>运行成功~</p>
<h2 data-id="heading-25">结束语</h2>
<p>就笔者而言体验很流畅，不需要使用第三方工具就能在<code>windows</code>上体验<code>linux</code>这是很不错的，在里面乱搞搞坏了也没事直接傻瓜式的卸载重装即可。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            