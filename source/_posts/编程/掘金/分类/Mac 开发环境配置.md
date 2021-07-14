
---
title: 'Mac 开发环境配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/678cafa7048f49b59aa1e5ea69c4ac97~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 18:02:36 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/678cafa7048f49b59aa1e5ea69c4ac97~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>萌新报道,简单记录一下在mac上便于开发的一些环境配置及安装方法</p>
<h2 data-id="heading-0">配置<code>code .</code>打开vscode项目</h2>
<ul>
<li>在vscode中按下 <code>shift+command+p</code>,输入<code>path</code>,回车即可</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/678cafa7048f49b59aa1e5ea69c4ac97~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">推荐使用终端软件 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iterm2.com%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iterm2.com/index.html" ref="nofollow noopener noreferrer">iTerm2</a></h2>
<h2 data-id="heading-2">使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fohmyz.sh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ohmyz.sh/" ref="nofollow noopener noreferrer">zsh</a>来优化终端</h2>
<p><code>sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"</code></p>
<p>注意：需要配全局参数</p>
<ul>
<li>which yarn  查找bin路径，到bin为止</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e291a31500214f4f927ff276c0e7435d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>打开～/.zshrc 文件，加入文字<code>export PATH="$PATH:上面找的到bin路径:$HOME/.config/yarn/global/node_modules/.bin"</code></li>
<li>在zsh中运行<code>source ./zshrc</code>使其生效</li>
</ul>
<h2 data-id="heading-3">内网穿透软件</h2>
<p>开发时可能需要远程提供给***去验收,这时候就需要用的内网穿透</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdashboard.ngrok.com%2Fget-started%2Ftutorials" target="_blank" rel="nofollow noopener noreferrer" title="https://dashboard.ngrok.com/get-started/tutorials" ref="nofollow noopener noreferrer">ngrok</a>
<ul>
<li>解压包<code>unzip /path/to/ngrok.zip</code></li>
<li>当前目录下,设置用户<code>./ngrok authtoken 你的token</code></li>
<li>使用 <code>./ngrok http 你开发环境的端口号</code></li>
<li>遇上“Invalid Host header”时</li>
</ul>
<code>ngrok http --host-header=rewrite 端口号</code> 使用</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnatapp.cn%2Farticle" target="_blank" rel="nofollow noopener noreferrer" title="https://natapp.cn/article" ref="nofollow noopener noreferrer">natapp</a></li>
</ul>
<h2 data-id="heading-4">mac聚焦软件 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.alfredapp.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.alfredapp.com/" ref="nofollow noopener noreferrer">Alfred</a></h2>
<h2 data-id="heading-5">使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvm-sh%2Fnvm" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nvm-sh/nvm" ref="nofollow noopener noreferrer">nvm</a>来管理node版本</h2>
<ul>
<li>
<p>先卸载<code>node</code>,可以通过<code>node -v</code>来验证</p>
<ul>
<li>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 依次执行</span>
sudo npm uninstall npm -g
sudo rm -rf /usr/local/lib/node /usr/local/lib/node_modules /var/db/receipts/org.nodejs.*
sudo rm -rf /usr/local/include/node /Users/$USER/.npm
sudo rm /usr/local/bin/node
sudo rm /usr/local/share/man/man1/node.1
sudo rm /usr/local/lib/dtrace/node.d
<span class="hljs-meta">#</span><span class="bash"> 验证</span>
node -v
npm -v
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>安装<code>git</code></p>
<ul>
<li>
<p>如果没有安装<code>git</code>可以先通过<code>homebrew</code>来进行安装</p>
<pre><code class="hljs language-shell copyable" lang="shell">/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装git   <code>brew install git</code></p>
</li>
</ul>
</li>
<li>
<p>安装<code>nvm</code></p>
<ul>
<li>打开<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnvm-sh%2Fnvm" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nvm-sh/nvm" ref="nofollow noopener noreferrer">nvm</a>的github仓库,查看readme,找到<code>Installing and Updataing</code></li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73798a52e6d4467dba109b6681505d83~tplv-k3u1fbpfcp-watermark.image" alt="image-20210714094157015.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>先用curl 安装，使用下面的代码对全局变量进行修改</p>
</li>
<li>
<p>终端输入<code>nvm</code>查看是否安装完成</p>
</li>
<li>
<p>如遇问题，可继续往下查看nvm的readme解决</p>
</li>
<li>
<p>nvm常用命令</p>
<pre><code class="hljs language-shell copyable" lang="shell">nvm version 查看nvm版本
nvm install 安装最新版本的nvm
nvm install <version>  安装对应node版本
nvm use <version>  切换使用指定的node版本
nvm ls 列出所有node版本
nvm current 显示当前node版本
nvm uninstall <version> 卸载指定的node版本
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-6">使用yrm来管理npm源</h2>
<ul>
<li>使用npm安装
<code>npm install -g yrm</code></li>
<li><code>yrm ls</code> 查看所有的源</li>
<li><code>yrm use taobao</code> 指定淘宝源，<code>taobao</code>是<code>yrm ls</code>中显示的</li>
</ul></div>  
</div>
            