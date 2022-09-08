
---
title: '服务器拒绝了我的ssh免密登录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1460'
author: 掘金
comments: false
date: Tue, 06 Sep 2022 17:40:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=1460'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>。</p>
<blockquote>
<p>众里寻他千百度，蓦然回首，答案就在眼皮子底下......</p>
</blockquote>
<p>正如标题所述，我遇到的问题是服务器拒绝了我的ssh免密登录，具体情况是我之前已经配置好了ssh免密登录，但是最近突发 PC ssh 登录云服务器报错，接连好些天都没找到原因。</p>
<p>ssh 免密码登录本身不是一个复杂的问题，百度 / google 上面随便都找得到教程。关键点在于：</p>
<ol>
<li>基于 RSA 密钥对保障通信的安全。</li>
<li>将公钥传递到目标服务器的 <code>~/.ssh/authorized_keys</code> 中。</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">// 生成密钥
ssh-keygen -t rsa -b 4096 -C "your comment"
// 将公钥发送到目标服务器
ssh-copy-id -i ~/.ssh/id_rsa.pub user@host
// 免密登录
ssh user@host
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我自己的一台个人服务器原本也配置好了 authorized_keys，免密登录一直用得挺好，在PC本地，remote CI/CD 中一直跑得通。</p>
<p>然而，最近我不知道在服务器上调整了什么，或者是我的 PC 发生了什么升级，不记得了，反正现象就是在 git bash 使用 ssh 免密登录上不去了，一直提示 Permission denied (publickey) 之类的报错信息，但是在 xshell 或者 CI/CD 中都是正常的。</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta prompt_">$ </span><span class="bash">ssh txcentos</span>
username@xxx.xx.xx.xx: Permission denied (publickey).
<span class="copy-code-btn">复制代码</span></code></pre>
<p>网上自然有各种类似问题，解决方案诸如修改 .ssh 目录权限，修改 sshd_config 配置等，或者是说你的密钥不对（然而重新生成了也一样，emm...）。</p>
<ul>
<li>调整了权限，发现不是权限的问题</li>
</ul>
<pre><code class="hljs language-shell copyable" lang="shell">chmod 700 ~/.ssh
chmod 600 .ssh/authorized_keys
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调整了 sshd_config 的几个关键配置，发现也不是这个问题。</li>
</ul>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-string">PermitRootLogin</span> <span class="hljs-literal">yes</span>
<span class="hljs-string">PubkeyAuthentication</span> <span class="hljs-literal">yes</span>
<span class="hljs-string">PasswordAuthentication</span> <span class="hljs-literal">no</span>

<span class="hljs-string">//</span> <span class="hljs-string">调整之后重启服务</span>
<span class="hljs-string">systemctl</span> <span class="hljs-string">restart</span> <span class="hljs-string">sshd.service</span>
<span class="hljs-string">//</span> <span class="hljs-string">或者</span>
<span class="hljs-string">service</span> <span class="hljs-string">sshd</span> <span class="hljs-string">restart</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实我心里很清楚，我的问题可能不是这些情况，即使从报错信息上看还是差不多的。我抱着试试的态度，改了一遍又一遍，还是不太行，要么是提示 denied，要么是 ssh 登录时让我输入密码（这还怎么免密），有点崩溃。</p>
<p>最终决定从 ssh 命令上 debug 看看报错信息（这是我之前忽略的，应该从这里开始查的），</p>
<pre><code class="hljs language-ruby copyable" lang="ruby"><span class="hljs-variable">$ </span>ssh txcentos -v
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到了这么一个关键信息。</p>
<pre><code class="hljs language-vbnet copyable" lang="vbnet"><span class="hljs-symbol">debug1:</span> send_pubkey_test: no mutual signature algorithm
<span class="hljs-symbol">debug1:</span> No more authentication methods <span class="hljs-keyword">to</span> <span class="hljs-keyword">try</span>.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顺着<code>no mutual signature algorithm</code>这个信息查到了一些资料，由于 OpenSSH 从 8.8 版本由于安全原因开始弃用了 rsa 加密的密钥，需要在 .ssh 的 config 配置中加入这么一行：</p>
<pre><code class="hljs copyable">PubkeyAcceptedKeyTypes +ssh-rsa
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经测试真的管用，免密登录成功！</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta prompt_">$ </span><span class="bash">ssh xxx</span>
Last login: Tue Sep  6 xx:xx:47 2022 from xxx.xx.xxx.xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>附上参考的博客链接 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fq274488181%2Farticle%2Fdetails%2F121673370" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/q274488181/article/details/121673370" ref="nofollow noopener noreferrer">blog.csdn.net/q274488181/…</a></p>
<p>同时我也检查了 PC 的 openssh 版本，确实是高于 8.8 版本的。</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta prompt_">$ </span><span class="bash">ssh -V</span>
OpenSSH_9.0p1, OpenSSL 1.1.1o  3 May 2022
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我还是去查阅 openssh 8.8 的发行日志核实了一下，确实有关于 security 的 incompatible changes，具体与 RSA/SHA-256/512 和 RSA/SHA1 有关。</p>
<p>详细资料可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.openssh.com%2Ftxt%2Frelease-8.8" target="_blank" rel="nofollow noopener noreferrer" title="https://www.openssh.com/txt/release-8.8" ref="nofollow noopener noreferrer">www.openssh.com/txt/release…</a></p>
<blockquote>
<p>总结下来就是，本次遇到问题时，我盲目自信认为可以凭自己之前的一些经验，找之前用过的一些方法去修改测试，浪费了很多时间，同时也打击了自己的信心。正确的做法是，对于一些命令行接口，可以优先确认是否能找到 debug 或者日志信息，优先从这些信息入手查问题，就比如这次的 ssh 命令，实际上是提供了 -v 选项，也就是 verbose，能看到比较详细的日志，往往会有事半功倍之效。</p>
</blockquote></div>  
</div>
            