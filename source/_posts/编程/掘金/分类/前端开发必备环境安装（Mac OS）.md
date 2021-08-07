
---
title: '前端开发必备环境安装（Mac OS）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6816'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 02:24:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=6816'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>发现自己一年多没更新博客了(<em>/ω＼</em>)，最近有学弟、学妹问作为<strong>前端使用Mac需要搭建哪些环境</strong>。问的次数多了，索性整理了一套较为通用和简洁的搭建流程，如果对你有帮助的话，欢迎<strong>点赞和收藏❤️</strong>~</p>
<h2 data-id="heading-1">Xcode</h2>
<p>必备的<strong>App</strong>端开发调试工具，<strong>App Store</strong>搜索下载即可</p>
<h2 data-id="heading-2">Homebrew</h2>
<p><strong>Homebrew</strong>是一款<strong>Mac OS</strong>平台下的软件包管理工具，拥有安装、卸载、更新、查看、搜索等很多实用的功能，简单来说就是装软件包的神器。</p>
<pre><code class="copyable"># 推荐使用清华源
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
​
# 安装完成后记得重启下终端
​
# 验证是否安装成功
brew --version
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">iTerm2</h2>
<h3 data-id="heading-4">下载</h3>
<p>相比于原生<strong>bash</strong>更为好用的终端</p>
<ol>
<li>官网下载，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iterm2.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iterm2.com/" ref="nofollow noopener noreferrer">www.iterm2.com/</a></li>
<li>使用<strong>brew</strong>进行安装</li>
</ol>
<pre><code class="copyable">brew cask install iterm2
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">切换shell</h3>
<pre><code class="copyable"># 查看系统当前的shell
cat /etc/shells
​
# 切换shell
chsh -s /bin/zsh
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Oh My Zsh</h2>
<p>让<strong>iTerm2</strong>的主题更加漂亮</p>
<h3 data-id="heading-7">下载</h3>
<pre><code class="copyable">sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">设置主题</h3>
<pre><code class="copyable">open ~/.zshrc
​
# 找到 ZSH_THEME
# robbyrussell 是默认的主题
ZSH_THEME="robbyrussell"
​
# ZSH_THEME="样式名称"
# 更多主题 https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
​
# 修改配置项后记得使其生效
source ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">升级自带的Git</h2>
<pre><code class="copyable"># 下载
brew install git
​
# 配置环境变量
vim ~/.zshrc  # 添加
export GIT=/usr/local/Cellar/git/2.1.3 #这里写你自己下载的git版本地址
export PATH=$GIT/bin:$PATH
​
# 保存
source ~./zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">Node</h2>
<h3 data-id="heading-11">下载nvm</h3>
<p><strong>nvm</strong>是用于管理node版本的（node version manager）</p>
<pre><code class="copyable"># 下载
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
​
# 配置环境变量
export NVM_DIR="$([ -z "$&#123;XDG_CONFIG_HOME-&#125;" ] && printf %s "$&#123;HOME&#125;/.nvm" || printf %s "$&#123;XDG_CONFIG_HOME&#125;/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
​
# 保存
~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">M1芯片使用nvm安装低版本node报错的解决方案</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.macdaxue.com%2Frosetta-2%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.macdaxue.com/rosetta-2/" ref="nofollow noopener noreferrer">M1芯片在过渡期间苹果给出的对应X86芯片的兼容性方案</a></p>
<pre><code class="copyable"># 安装
softwareupdate --install-rosetta
​
# 启动
arch -x86_64 zsh
​
# 指定node 版本
# nvm install 14.15.0
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">使用nvm控制node版本（npm会随着node进行安装）</h3>
<pre><code class="copyable"># 查看所有可用版本
nvm ls-remote
​
# 安装最新稳定版 node
nvm install stable  
​
# 安装指定版本
nvm install <version>
​
# 删除已安装的指定版本
nvm uninstall <version>
​
# 切换使用指定的版本
nvm use <version>  切换使用指定的版本node
​
# 指定默认版本
nvm alias default <version>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">使用yarn进行下载包</h3>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000021335004" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000021335004" ref="nofollow noopener noreferrer">yarn和npm的对比</a></strong></p>
<pre><code class="copyable">brew install yarn
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15"><strong>设置npm镜像源</strong></h3>
<pre><code class="copyable"> # npm
​
 # 获取镜像源地址
npm get registry
​
 # 设置镜像源
npm set registry https://registry.npm.taobao.org

​
 # yarn
​
 # 获取镜像源地址
yarn config get registry
​
 # 设置镜像源
yarn config  registry https://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16"><strong>vs code好用的插件</strong></h2>
<pre><code class="copyable"> # 中文简体
Chinese
​
 # 标签自闭和
Auto Close Tag
​
 # 标签字段重命名
Auto Rename Tag
​
 # 更好的注释
Better Comments
​
 # 打标签工具，查看源码必备
Bookmarks
​
 # 代码静态检查工具
Eslint
​
 # HTML & Css相关
CSScomb
HTML CSS Support
HTML Boilerplate
HTML Snippets
​
 # JS相关
ES7 React/Redux/React-Native/JS snippets
React-Native/React/Redux es6/es7
React/Redux/react-router Snippets
Typescript React code snippets
Vetur
​
 # 查看文件大小
filesize
​
 # 在浏览器中打开
Open in Browser
​
 # Git神器，可以查看每行代码的提交人，提交时间等信息
GitLens
​
 # SVG代码提示
svg
​
 # 主题
One Dark Pro
​
 # 文件图标主题
vscode-icons
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            