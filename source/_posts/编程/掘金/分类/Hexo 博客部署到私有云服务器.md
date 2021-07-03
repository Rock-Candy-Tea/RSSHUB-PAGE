
---
title: 'Hexo 博客部署到私有云服务器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0952da28e7414808977fbd2f8839fe6e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 01:50:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0952da28e7414808977fbd2f8839fe6e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>喜欢分享是程序员的天性，所以大部分的程序员都会有一个自己的博客，里面的内容可以是一些工作中遇到的问题和解决思路，也可以是最近学习到的新技术的总结，也可以是对生活的思考和感悟。搭建个人博客的方式也有很多，可以直接在第三方博客平台上写作，如掘金、博客园、CSDN 等等，也可以使用 hexo 搭建博客部署到 github pages，当然如果拥有私有云服务器的还可以在上面借助 wordpress 博客系统搭建一个博客。本文要介绍的是使用 hexo 搭建博客，但是部署到私有云服务器。</p>
<h3 data-id="heading-1">准备工作</h3>
<p>本文重点介绍的是将博客部署到私有云服务器上，所以一些准备工作默认是已经做好了。具体包括以下几点：</p>
<ul>
<li>一台已经安装Nginx的私有云服务器，安装 Nginx 推荐使用军哥的<a href="https://lnmp.org/" target="_blank" rel="nofollow noopener noreferrer">LNMP一键安装包</a></li>
<li>一个博客域名：如果服务器是国外购买的，域名就不需要工信部备案，如果服务器是在阿里云/腾讯云等平台购买的，则域名需要工信部备案。并将域名解析到私有云服务器。</li>
<li>本地已经安装node.js、hexo博客环境、git</li>
</ul>
<h3 data-id="heading-2">部署步骤</h3>
<h4 data-id="heading-3">搭建git仓库</h4>
<h5 data-id="heading-4">新建git用户并设置密码</h5>
<pre><code class="hljs language-js copyable" lang="js">adduser git
passwd git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改权限</p>
<pre><code class="hljs language-js copyable" lang="js">chmod <span class="hljs-number">740</span> /etc/sudoers
vim /etc/sudoers
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到root ALL=(ALL) ALL并在其下面添加</p>
<pre><code class="hljs language-js copyable" lang="js">git     ALL=(ALL)       ALL
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存后改回sudoer权限：</p>
<pre><code class="hljs language-js copyable" lang="js">chmod <span class="hljs-number">400</span> /etc/sudoers
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">创建免密登陆证书</h5>
<p>在服务器中打开RSA认证</p>
<pre><code class="hljs language-js copyable" lang="js">vim /etc/ssh/sshd_config
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到以下三项并开启，若没有找到则添加</p>
<pre><code class="copyable">RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile  .ssh/authorized_keys
<span class="copy-code-btn">复制代码</span></code></pre>
<p>切换到git用户并开始配置ssh</p>
<pre><code class="hljs language-js copyable" lang="js">su git
cd ~
mkdir .ssh && chmod <span class="hljs-number">700</span> .ssh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，要为git用户里的.ssh添加开发者公钥，以便免密向git仓库推送数据。</p>
<p>在本地电脑通过 C盘用户目录/.ssh/id_rsa.pub找到ssh的公钥,在服务端.ssh里新建authorized_keys文件并将其复制到里面。</p>
<p>注意:公钥在authorized_keys文件中是一行添加一个</p>
<pre><code class="hljs language-js copyable" lang="js">touch /home/git/.ssh/authorized_keys
sudo chmod <span class="hljs-number">600</span> /home/git/.ssh/authorized_keys
vim /home/git/.ssh/authorized_keys
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若之前未有上传文件至github等仓库的经历，本地客户端无ssh的keys，则要先生成一下。</p>
<h5 data-id="heading-6">修改git用户权限</h5>
<p>给git用户设置权限，限制其只能使用git-shell向git仓库push或pull等，而不能登陆机器并取得普通shell命令控制系统。</p>
<p>使用which git-shell判断是否安装了git-shell。如果未安装，则yum install git
判断shells文件路径是否存在：cat /etc/shells，如果shells文件不存在或者文件中没有/usr/bin/git-shell，则</p>
<pre><code class="hljs language-js copyable" lang="js">sudo vim /etc/shells
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在最下面添加</p>
<pre><code class="hljs language-js copyable" lang="js">/usr/bin/git-shell
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">创建仓库</h5>
<p>在/var/repo创建空仓库(切换为root用户)</p>
<pre><code class="hljs language-js copyable" lang="js">mkdir /<span class="hljs-keyword">var</span>/repo
cd /<span class="hljs-keyword">var</span>/repo
git init --bare blog.git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置git hooks使得在仓库更新的时候，nginx配置文件中root指向的目录同步更新(这里root指向的是/home/wwwroot/<a href="http://www.blogdomain.com/" target="_blank" rel="nofollow noopener noreferrer">www.blogdomain.com/</a>)</p>
<pre><code class="hljs language-js copyable" lang="js">vim /<span class="hljs-keyword">var</span>/repo/blog.git/hooks/post-receive
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加</p>
<pre><code class="hljs language-js copyable" lang="js">#!<span class="hljs-regexp">/bin/</span>sh
git --work-tree=<span class="hljs-regexp">/home/</span>wwwroot/www.blogdomain.com/ --git-dir=<span class="hljs-regexp">/var/</span>repo/blog.git checkout -f
/home/wwwroot/www.blogdomain.com/
chmod -R <span class="hljs-number">777</span> *
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存退出并设置权限</p>
<pre><code class="hljs language-js copyable" lang="js">chmod +x /<span class="hljs-keyword">var</span>/repo/blog.git/hooks/post-receive
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更改blog.git拥有者</p>
<pre><code class="hljs language-js copyable" lang="js">sudo chown -R git:git blog.git
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">使用chsh命令修改任意系统用户的shell权限</h6>
<pre><code class="hljs language-js copyable" lang="js">sudo chsh git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Login Shell [/bin/bash]后输入:</p>
<pre><code class="hljs language-js copyable" lang="js">/usr/bin/git-shell
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改完后验证cat /etc/passwd是否以git-shell结尾，例如：</p>
<pre><code class="hljs language-js copyable" lang="js">git:x:<span class="hljs-number">1003</span>:<span class="hljs-number">1003</span>:,,,:<span class="hljs-regexp">/home/gi</span>t:<span class="hljs-regexp">/usr/</span>bin/git-shell
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改后，在本地客户端使用ssh git@serverip登陆将被拒绝(第一次登陆该网址会提示continue connecting，输入yes)：</p>
<pre><code class="hljs language-js copyable" lang="js">$ ssh git@gitserver
<span class="hljs-attr">fatal</span>: Interactive git shell is not enabled.
<span class="hljs-attr">hint</span>: ~/git-shell-commands should exist and have read and execute access.
Connection to gitserver closed.
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">git测试</h5>
<p>完成上述步骤后，通过测试判断git服务器是否部署成功,在本地客户端执行</p>
<pre><code class="hljs language-js copyable" lang="js">git clone git@serverip:<span class="hljs-regexp">/var/</span>repo/blog.git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果远程服务器禁用22端口登陆，则可以使用如下语句：</p>
<pre><code class="hljs language-js copyable" lang="js">git clone ssh:<span class="hljs-comment">//git@serverip:port/var/repo/blog.git</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输入密码后(如果秘钥配置成功则不用输入密码)若blog.git中没有内容将会提示:</p>
<pre><code class="hljs language-js copyable" lang="js">···
git@serverip<span class="hljs-string">`s password:
warning: You appear to have cloned an empty repository
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">Nginx 配置</h4>
<p>本文假定你是使用了 lnmp 一键安装包，可使用以下命令将博客域名添加到虚拟主机：</p>
<pre><code class="hljs language-js copyable" lang="js">lnmp vhost add
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体选项可按需要选择配置：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0952da28e7414808977fbd2f8839fe6e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后回车，即可完成虚拟主机的添加。</p>
<h4 data-id="heading-11">hexo 本地配置</h4>
<p>在本地hexo博客根目录修改_config.yml文件</p>
<pre><code class="hljs language-js copyable" lang="js"># Deployment
## Docs: https:<span class="hljs-comment">//hexo.io/docs/deployment.html</span>
deploy:
  type: git
  <span class="hljs-attr">repo</span>:
        vps:    git@serverip:<span class="hljs-regexp">/var/</span>repo/blog.git
  <span class="hljs-attr">branch</span>: master
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">将博客部署到私有云服务器</h4>
<p>在 hexo 博客根目录依次执行以下命令即可：</p>
<pre><code class="hljs language-js copyable" lang="js">hexo clean
hexo g
hexo d
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里就完成了hexo博客的配置和部署了，在浏览器输入域名（文章中示例用的是 <a href="http://www.blogdomain.com/" target="_blank" rel="nofollow noopener noreferrer">www.blogdomain.com</a> ） 即可访问博客了。</p></div>  
</div>
            