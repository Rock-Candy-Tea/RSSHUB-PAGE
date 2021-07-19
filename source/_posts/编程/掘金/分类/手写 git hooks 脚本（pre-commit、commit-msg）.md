
---
title: '手写 git hooks 脚本（pre-commit、commit-msg）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53a3d639f75a4676802da639a3925c9b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 16:25:33 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53a3d639f75a4676802da639a3925c9b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<p>Git 能在特定的重要动作发生时触发自定义脚本，其中比较常用的有：<code>pre-commit</code>、<code>commit-msg</code>、<code>pre-push</code> 等钩子（hooks）。我们可以在 <code>pre-commit</code> 触发时进行代码格式验证，在 <code>commit-msg</code> 触发时对 commit 消息和提交用户进行验证，在 <code>pre-push</code> 触发时进行单元测试、e2e 测试等操作。</p>
<p>Git 在执行 <code>git init</code> 进行初始化时，会在 <code>.git/hooks</code> 目录生成一系列的 hooks 脚本：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53a3d639f75a4676802da639a3925c9b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图可以看到每个脚本的后缀都是以 <code>.sample</code> 结尾的，在这个时候，脚本是不会自动执行的。我们需要把后缀去掉之后才会生效，即将 <code>pre-commit.sample</code> 变成 <code>pre-commit</code> 才会起作用。</p>
<p>本文主要是想介绍一下如何编写 git hooks 脚本，并且会编写两个 <code>pre-commit</code>、<code>commit-msg</code> 脚本作为示例，帮助大家更好的理解 git hooks 脚本。当然，在工作中还是建议使用现成的、开源的解决方案 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftypicode%2Fhusky" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/typicode/husky" ref="nofollow noopener noreferrer">husky</a>。</p>
<h2 data-id="heading-1">正文</h2>
<p>用于编写 git hooks 的脚本语言是没有限制的，你可以用 <code>nodejs</code>、<code>shell</code>、<code>python</code>、<code>ruby</code>等脚本语言，非常的灵活方便。</p>
<p>下面我将用 shell 语言来演示一下如何编写 <code>pre-commit</code> 和 <code>commit-msg</code> 脚本。另外要注意的是，在执行这些脚本时，如果以非零的值退出程序，将会中断 git 的提交/推送流程。所以在 hooks 脚本中验证消息/代码不通过时，就可以用非零值进行退出，中断 git 流程。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">exit</span> 1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">pre-commit</h3>
<p>在 <code>pre-commit</code> 钩子中要做的事情特别简单，只对要提交的代码格式进行检查，因此脚本代码比较少：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/bin/sh</span>
npm run lint

<span class="hljs-comment"># 获取上面脚本的退出码</span>
exitCode=<span class="hljs-string">"$?"</span>
<span class="hljs-built_in">exit</span> <span class="hljs-variable">$exitCode</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我在项目中已经配置好了相关的 eslint 配置以及 npm 脚本，因此在 <code>pre-commit</code> 中执行相关的 lint 命令就可以了，并且判断一下是否正常退出。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在 package.json 文件中已配置好 lint 命令</span>
<span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"lint"</span>: <span class="hljs-string">"eslint --ext .js src/"</span>
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面看一个动图，当代码格式不正确的时候，进行 commit 就报错了：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4581be24ce441319deff389ddaf38d8~tplv-k3u1fbpfcp-watermark.image" alt="demo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在修改代码格式后再进行提交，这时就不报错了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67ae2c375ea6490e817d7e5130447c1a~tplv-k3u1fbpfcp-watermark.image" alt="demo2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从动图中可以看出，这次 commit 已正常提交了。</p>
<h3 data-id="heading-3">commit-msg</h3>
<p>在 <code>commit-msg</code> hooks 中，我们需要对 commit 消息和用户进行校验。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-meta">#!/bin/sh</span>

<span class="hljs-comment"># 用 `` 可以将命令的输出结果赋值给变量</span>
<span class="hljs-comment"># 获取当前提交的 commit msg</span>
commit_msg=`cat <span class="hljs-variable">$1</span>`

<span class="hljs-comment"># 获取用户 email</span>
email=`git config user.email`
msg_re=<span class="hljs-string">"^(feat|fix|docs|style|refactor|perf|test|workflow|build|ci|chore|release|workflow)(\(.+\))?: .&#123;1,100&#125;"</span>

<span class="hljs-keyword">if</span> [[ ! <span class="hljs-variable">$commit_msg</span> =~ <span class="hljs-variable">$msg_re</span> ]]
<span class="hljs-keyword">then</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"\n不合法的 commit 消息提交格式，请使用正确的格式：\
\nfeat: add comments\
\nfix: handle events on blur (close #28)\
\n详情请查看 git commit 提交规范：https://github.com/woai3c/Front-end-articles/blob/master/git%20commit%20style.md"</span>

<span class="hljs-comment"># 异常退出</span>
<span class="hljs-built_in">exit</span> 1
<span class="hljs-keyword">fi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>commit-msg</code> 钩子触发时，对应的脚本会接收到一个参数，这个参数就是 commit 消息，通过 <code>cat $1</code> 获取，并赋值给 <code>commit_msg</code> 变量。</p>
<p>验证 commit 消息的正则比较简单，看代码即可。如果对 commit 提交规范有兴趣，可以看看我另一篇<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwoai3c%2FFront-end-articles%2Fblob%2Fmaster%2Fgit%2520commit%2520style.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/woai3c/Front-end-articles/blob/master/git%20commit%20style.md" ref="nofollow noopener noreferrer">文章</a>。</p>
<p>对用户权限做判断则比较简单，只需要检查用户的邮箱或用户名就可以了（假设现在只有 abc 公司的员工才有权限提交代码）。</p>
<pre><code class="hljs language-bash copyable" lang="bash">email_re=<span class="hljs-string">"@abc\.com"</span>
<span class="hljs-keyword">if</span> [[ ! <span class="hljs-variable">$email</span> =~ <span class="hljs-variable">$email_re</span> ]]
<span class="hljs-keyword">then</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"此用户没有权限，具有权限的用户为： xxx@abc.com"</span>

<span class="hljs-comment"># 异常退出</span>
<span class="hljs-built_in">exit</span> 1
<span class="hljs-keyword">fi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面用两个动图来分别演示一下校验 commit 消息和判断用户权限的过程：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09cfba88825c42f4b10d788c5e8060c0~tplv-k3u1fbpfcp-watermark.image" alt="demo3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4ee905eb3814fde86c6e80752a52bd4~tplv-k3u1fbpfcp-watermark.image" alt="demo4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">设置 git hooks 默认位置</h3>
<p>脚本可以正常执行只是第一步，还有一个问题是必须要解决的，那就是如何和同一项目的其他开发人员共享 git hooks 配置。因为 <code>.git/hooks</code> 目录不会随着提交一起推送到远程仓库。对于这个问题有两种解决方案：第一种是模仿 husky 做一个 npm 插件，在安装的时候自动在 <code>.git/hooks</code> 目录添加 hooks 脚本；第二种是将 hooks 脚本单独写在项目中的某个目录，然后在该项目安装依赖时，自动将该目录设置为 git 的 hooks 目录。</p>
<p>接下来详细说说第二种方法的实现过程：</p>
<ol>
<li>在 <code>npm install</code> 执行完成后，自动执行 <code>git config core.hooksPath hooks</code> 命令。</li>
<li><code>git config core.hooksPath hooks</code> 命令将 git hooks 目录设置为项目根目录下的 hooks 目录。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"lint"</span>: <span class="hljs-string">"eslint --ext .js src/"</span>,
    <span class="hljs-string">"postinstall"</span>: <span class="hljs-string">"git config core.hooksPath hooks"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">总结</h2>
<p>其实本文适用的范围不仅仅局限于前端，而是适用所有使用了 git 作为版本控制的项目。例如安卓、ios、Java 等等。只是本文选择了前端项目作为示例。</p>
<p>最近附上项目源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwoai3c%2Fgit-hooks-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/woai3c/git-hooks-demo" ref="nofollow noopener noreferrer">github.com/woai3c/git-…</a></p>
<h3 data-id="heading-6">参考资料</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fbook%2Fzh%2Fv2%2F%25E8%2587%25AA%25E5%25AE%259A%25E4%25B9%2589-Git-%25E4%25BD%25BF%25E7%2594%25A8%25E5%25BC%25BA%25E5%2588%25B6%25E7%25AD%2596%25E7%2595%25A5%25E7%259A%2584%25E4%25B8%2580%25E4%25B8%25AA%25E4%25BE%258B%25E5%25AD%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/book/zh/v2/%E8%87%AA%E5%AE%9A%E4%B9%89-Git-%E4%BD%BF%E7%94%A8%E5%BC%BA%E5%88%B6%E7%AD%96%E7%95%A5%E7%9A%84%E4%B8%80%E4%B8%AA%E4%BE%8B%E5%AD%90" ref="nofollow noopener noreferrer">自定义 Git - 使用强制策略的一个例子</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Flinux%2Flinux-shell.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/linux/linux-shell.html" ref="nofollow noopener noreferrer">Shell 教程</a></li>
</ul></div>  
</div>
            