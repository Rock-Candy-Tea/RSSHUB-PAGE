
---
title: '从0开始配置Mac前端基本开发环境'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0910a72d7d3e44f3b07051c6e6d12b64~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 22:30:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0910a72d7d3e44f3b07051c6e6d12b64~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Mac前端环境搭建</h2>
<p>大家好，我又来了，之前在滴滴实习了几个月，这次换了个公司实习，又拿到了一台新的Mac，所以就记录了一下自己配置基本前端开发环境的过程，也可以给一些有需要的朋友做一下参考。希望可以帮助到大🏠</p>
<h3 data-id="heading-1">Homebrew</h3>
<p>拿到一台新的Mac，就是需要安装各种我们平时常用到的软件了。首先建议安装的就是Homebrew(Homebrew是Mac OSX下使用的包管理工具,用来安装OS系统中没有预装的东西)</p>
<p>地址<a href="https://brew.sh/" target="_blank" rel="nofollow noopener noreferrer">Homebrew官网</a></p>
<p>按<code>command + 空格</code>，然后输入<code>terminal</code>，控制台上输入<code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code>便可以进行安装</p>
<p>等到安装完成了，就会显示这个</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0910a72d7d3e44f3b07051c6e6d12b64~tplv-k3u1fbpfcp-watermark.image" alt="EB6343C7-A6DF-4F4F-AA6D-E05FE2165504.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>出现安装成功提示之后，就可以配置路径了。</p>
<p>控制台输入<code>echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/这里是电脑的用户名/.zprofile</code></p>
<p>然后再输入<code>eval "$(/opt/homebrew/bin/brew shellenv)"</code></p>
<p>完成上面两步之后，控制台输入<code>brew -v</code>出现版本号那就是配置成功了</p>
<h3 data-id="heading-2">Git环境</h3>
<p>安装完homebrew之后就可以使用homebrew来进行Git的安装了。<a href="https://git-scm.com/download/mac" target="_blank" rel="nofollow noopener noreferrer">Git安装官网</a></p>
<p>控制台输入<code>brew install git</code></p>
<p>如果安装成功了，最后输入<code>git --version</code>可以看到版本号</p>
<h4 data-id="heading-3">初始化</h4>
<p>安装好git之后就要进行初始化操作。第一次使用git的时候我们需要给git配置用户名和邮箱，用户和邮箱可以使用github的，也可以使用自己公司的gitlab仓库的账号</p>
<p>配置用户名</p>
<pre><code class="hljs language-bash copyable" lang="bash">git config --global user.name <span class="hljs-string">"用户名"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置邮箱</p>
<pre><code class="hljs language-bash copyable" lang="bash">git config --global user.email <span class="hljs-string">"邮箱地址"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置好这个以后我们输入便可以看到我们所有的配置信息了，然后可以看到user.name和user.email配置得对不对</p>
<pre><code class="hljs language-bash copyable" lang="bash">git config -l
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就可以配置ssh密钥了。ssh密钥允许系统和gitlab之间建立安全连接。在上传代码的时候使用https需要频繁的输入密码，而使用ssh的话可以省去这个步骤。</p>
<ul>
<li>检查SSH秘钥是否存在。控制台输入：<code>cat ~/.ssh/id_rsa.pub</code></li>
<li>若密钥不存在，就需要生成SSH 密钥 。执行命令<code>ssh-keygen -t rsa -C "邮箱地址"</code></li>
<li>在gitlab上添加SSH key。执行命令查看公钥：<code>cat ~/.ssh/id_rsa.pub</code>，然后将显示出来的一大串字符串复制下来</li>
<li>打开gitlab的找到Profile Settings下的SSH Keys，在Add an SSH key中，将刚刚复制的一大串字符串密钥粘贴到Key的框框里，在Title这里给这个key设置一个响当当的名字，点击Add key就大功告成。</li>
</ul>
<h3 data-id="heading-4">控制台优化</h3>
<h4 data-id="heading-5">zsh</h4>
<p>zsh（z-shell）是一款用于交互式使用的shell，也可以作为脚本解释器来使用。其包含了 bash，ksh，tcsh 等其他shell中许多优秀功能，也拥有诸多自身特色。 从 MacOS Catalina 版开始，其默认shell从bash改为zsh。)</p>
<p>如果机器上当前安装的zsh不是最新版本(<code>zsh --version</code>查看当前版本)，可以使用<code>brew install zsh</code>安装。</p>
<h4 data-id="heading-6">oh-my-zsh</h4>
<p><a href="https://ohmyz.sh/#install" target="_blank" rel="nofollow noopener noreferrer">下载官网</a></p>
<ul>
<li>
<p>兼容bash</p>
</li>
<li>
<p>自动cd：只需输入目录的名称即可</p>
</li>
<li>
<p>命令选项补齐：比如输入<code>git</code>，然后按<code>Tab</code>，即可显示出<code>git</code>都有哪些命令</p>
</li>
<li>
<p>目录一次性补全：比如输入<code>Doc/doc</code>按<code>Tab</code>键会自动变成<code>Documents/document/</code></p>
<p>各种提效插件和美化主题的支持</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee298794e57042189fc20799e041f725~tplv-k3u1fbpfcp-watermark.image" alt="Jietu20210514-142200.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这个的时候就表示安装成功了。</p>
<h4 data-id="heading-7">常用zsh提效插件</h4>
<p><strong>zsh-syntax-highlighting</strong> 语法高亮插件</p>
<p>依次输入以下的命令</p>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> https://github.com/zsh-users/zsh-syntax-highlighting.git 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">vim ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在文件里找到plugins=(git)，括号是插件列表，git是默认安装的插件。添加插件</p>
<pre><code class="copyable">plugins=(
  git
  zsh-syntax-highlighting
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让插件生效</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">source</span> ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>zsh-autosuggestions</strong> 自动路径补全</p>
<p>输入命令时可提示自动补全（会出现灰色的命令提示，你曾经访问过的命令），然后按键盘 → (右方向键)</p>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> git://github.com/zsh-users/zsh-autosuggestions <span class="hljs-variable">$ZSH_CUSTOM</span>/plugins/zsh-autosuggestions
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">vim ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在文件里找到plugins，添加</p>
<pre><code class="copyable">plugins=(
  git
  zsh-syntax-highlighting
  zsh-autosuggestions
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让插件生效</p>
<pre><code class="copyable">source ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>autojump</strong> 跳转插件</p>
<p>实现目录间快速跳转，想去哪个目录直接 <code>j + 目录名</code>，或者想在Finder打开哪个目录就直接<code>jo + 目录名</code>，不用频繁的 cd 了</p>
<p>安装</p>
<pre><code class="copyable">brew install autojump
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">vim ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在文件里找到plugins，添加</p>
<pre><code class="copyable">plugins=(
  git
  zsh-syntax-highlighting
  zsh-autosuggestions
  autojump
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在zshrc文件末尾(最后一行)添加</p>
<pre><code class="copyable">[[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && . $(brew --prefix)/etc/profile.d/autojump.sh
source $ZSH/oh-my-zsh.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让插件生效</p>
<pre><code class="copyable">source ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Node环境安装</h3>
<p>主要是node和常用的工具</p>
<pre><code class="copyable">brew install node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成后输入<code>node -v</code>显示版本号就安装成功了</p>
<p>node版本管理工具安装</p>
<pre><code class="copyable">brew install nvm
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后按照安装提示，创建 <code>.nvm</code> 目录</p>
<pre><code class="copyable">mkdir ~/.nvm
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编辑 <code>~/.zshrc</code> 配置文件</p>
<pre><code class="copyable">vim ~/.zshrc 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>~/.zshrc</code> 配置文件后添加如下内容，最后一行</p>
<pre><code class="copyable">export NVM_DIR="$HOME/.nvm"
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && . "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && . "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让配置生效</p>
<pre><code class="copyable">source ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后输入<code>nvm -v</code>查看版本号，显示版本号则安装成功</p></div>  
</div>
            