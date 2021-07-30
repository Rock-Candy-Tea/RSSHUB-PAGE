
---
title: '使用React+redux+Node.js+MongoDB开发后台管理系统【环境】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4627'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 23:32:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=4627'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">创建项目[名为back-table]</h2>
<pre><code class="hljs language-js copyable" lang="js">create-react-app back-table
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">进入项目根目录</h2>
<pre><code class="hljs language-js copyable" lang="js">cd back-table 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">ls命令查看目录下的文件列表</h3>
<pre><code class="hljs language-js copyable" lang="js">README.md  node_modules  package.json  public   src     yarn.lock
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">安装antd</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install antd --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">安装redux</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install redux --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">开发后台接口[express + mongodb]</h2>
<h3 data-id="heading-6">安装express</h3>
<pre><code class="hljs language-js copyable" lang="js">npm install express --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.根目录下创建server目录，存放服务端代码</p>
<p>2.server/下新建server.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*----- /server/server.js ------ */</span> 
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);

<span class="hljs-keyword">const</span> app = express();

<span class="hljs-comment">//开发get接口</span>
app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res</span>) </span>&#123;   
    res.send(<span class="hljs-string">'hello world'</span>)
&#125;)
<span class="hljs-comment">//开发post接口</span>
<span class="hljs-comment">// app.post('/', function(req, res) &#123;   </span>
<span class="hljs-comment">//     res.json('...')</span>
<span class="hljs-comment">// &#125;)</span>

app.listen(<span class="hljs-number">3000</span>,<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'node app start at port 3000'</span>)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">使用nodemon监听路由和相应内容，自动重启</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install -g nodemon <span class="hljs-comment">//全局安装nodemon</span>
<span class="hljs-comment">//运行服务端文件可使用 -- nodemon server.js</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">下载安装mongoDB</h2>
<h3 data-id="heading-9">安装homebrew[镜像]</h3>
<pre><code class="hljs language-js copyable" lang="js">/usr/bin/ruby -e <span class="hljs-string">"$(curl -fsSL https://cdn.jsdelivr.net/gh/ineo6/homebrew-install/install)"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我安装中报了如下错误</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Error</span>:   homebrew-core is a shallow clone.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方式：删除homebrew-core后更新即可</p>
<pre><code class="hljs language-js copyable" lang="js">cd /usr/local/Homebrew/Library/Taps/homebrew
rm -rf homebrew-core
brew upgrade
cd <span class="hljs-string">"$(brew --repo)/Library/Taps/"</span>
rm -rf homebrew
mkdir homebrew && cd homebrew
git clone git:<span class="hljs-comment">//mirrors.ustc.edu.cn/homebrew-core.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">配置homebrew</h5>
<p>Homebrew通常用来下载软件的，但它在安装软件时非常慢。为了提升安装速度，需要更改 Homebrew 的安装源，将其替换成国内镜像。</p>
<ol>
<li>必备设置</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//替换 brew.git</span>
git -C <span class="hljs-string">"$(brew --repo)"</span> remote set-url origin https:<span class="hljs-comment">//mirrors.ustc.edu.cn/brew.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//替换 homebrew-core.git</span>
git -C <span class="hljs-string">"$(brew --repo homebrew/core)"</span> remote set-url origin https:<span class="hljs-comment">//mirrors.ustc.edu.cn/homebrew-core.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>按需配置</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//替换 homebrew-cask.git</span>
git -C <span class="hljs-string">"$(brew --repo homebrew/cask)"</span> remote set-url origin https:<span class="hljs-comment">//mirrors.ustc.edu.cn/homebrew-cask.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//替换homebrew-bottles【终端是bash】</span>
echo <span class="hljs-string">'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles'</span> >> ~/.bash_profile
source ~/.bash_profile
<span class="hljs-comment">//替换homebrew-bottles【终端是zsh】</span>
echo <span class="hljs-string">'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles'</span> >> ~/.zshrc
source ~/.zshrc
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">Homebrew简介</h5>
<p>Homebrew 主要由四个部分组成: brew、homebrew-core 、homebrew-cask、homebrew-bottles，它们对应的功能如下：</p>
<ul>
<li>Homebrew 源代码仓库</li>
<li>homebrew-core  核心源</li>
<li>homebrew-cask 提供macos应用和大型二进制文件的安装</li>
<li>homebrew-bottles 预编译二进制软件包</li>
</ul>
<h5 data-id="heading-12">Homebrew常见用法</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 查询：</span>
brew search 软件名
<span class="hljs-comment">// 安装：</span>
brew install 软件名
<span class="hljs-comment">// 卸载：</span>
brew uninstall 软件名
<span class="hljs-comment">// 更新 Homebrew：</span>
brew update 
<span class="hljs-comment">// 查看 Homebrew 配置信息：</span>
brew config 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用官方脚本同样会遇到uninstall地址无法访问问题，可以替换为下面脚本：</p>
<pre><code class="hljs language-js copyable" lang="js">/usr/bin/ruby -e <span class="hljs-string">"$(curl -fsSL https://cdn.jsdelivr.net/gh/ineo6/homebrew-install/uninstall)"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">安装mongoDB到本地</h3>
<p>教程参考官网</p>
<blockquote>
<p>我的安装目录 /usr/local/var/mongodb</p>
</blockquote>
<ol>
<li>启动mongodb</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">mongod --config/usr/local/etc/mongod.conf　　
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>mongo启动服务</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm install mongoose --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">adminMongo 可视化工具</h3>
<pre><code class="hljs language-js copyable" lang="js">  $  git clone https:<span class="hljs-comment">//github.com/mrvautin/adminMongo</span>
  $  cd adminMongo
  $  npm install
  $  npm start
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            