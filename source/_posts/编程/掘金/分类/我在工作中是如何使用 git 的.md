
---
title: '我在工作中是如何使用 git 的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65101a7d9d694e6fb4c72a020a80ab4c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 16:41:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65101a7d9d694e6fb4c72a020a80ab4c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65101a7d9d694e6fb4c72a020a80ab4c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 103 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://zoo.team/article/how-to-use-git" target="_blank" rel="nofollow noopener noreferrer">我在工作中是如何使用 git 的</a></p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c21fe17bec4446fcb90c68d271b958de~tplv-k3u1fbpfcp-watermark.image" alt="奕承.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10be51db41754da791aea92c067a95cd~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前言</h2>
<p>最近在网上有个真实发生的案例比较火，说的是一个新入职的员工，不会用 git 拉代码，第二天被开除。由此，可见 git 对我们工作的重要性，无论是前端后端，都是离不开 git 的，下面就让我们一探究竟吧。</p>
<p>上面的案例引申出一个问题，入职一家新公司，你的 leader 给你分配了仓库的权限后，如何配置本地的git环境并拉取代码？莫慌，按照下面我讲的四个步骤走，保证你可以顺利使用 git 进行拉取代码！</p>
<ol>
<li>
<p>下载 git  <a href="https://git-scm.com/downloads" target="_blank" rel="nofollow noopener noreferrer">下载地址</a> ，选择自己系统对应的版本下载即可。</p>
</li>
<li>
<p>在你的电脑上生成 ssh 秘钥,打开终端，执行 <code>ssh-keygen -t rsa -C "你公司内部邮箱地址" </code>，如果执行成功，切换到 <code>~/.ssh</code>目录下，此时目录应该如下所示。复制<code>id_rsa.pub</code>的内容。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b1368427af470ba95caefa7936b63c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519163921819.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>这里以 github 为例，如下图所示，进入 settings -> SSH and GPG keys 通过 <code>cat</code>命令查看文件<code>id_rsa.pub</code>的内容，然后复制过来，点击 add ssh key，这一步等于说把你的公钥放到了 github 上进行托管。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee11ec8f4efd4e62866bc09386dd4c08~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519164643069.png" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>全局配置 git 的用户名和邮箱</p>
</li>
</ol>
<pre><code class="copyable">git config --global user.name "xxx"
git config --global user.email "xxx@xx.com"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成以上四步，你就可以愉快的 pull 代码开发了，和 https 拉取方式不同的是，https 方式需要每次提交前都手动输入用户名和密码，ssh 的方式配置完毕后 git 都会使用你本地的私钥和远程仓库的公钥进行验证是否是一对秘钥，从而简化了操作流程。</p>
<h2 data-id="heading-1">git 简介</h2>
<p>在介绍 git 的相关操作前，我觉得非常有必要了解 git 的由来，以及 git 是用来解决什么问题的。Git（读音为/gɪt/）是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。Linus Torvalds，这个人我相信大家都知道吧，开源 linux 系统的发明人。如今，你看到的大部分服务器其实都是运行在linux系统上，令人感到称叹的是，这位大神级别的程序员不仅创造了 linux 系统。那 linux 的代码是如何管理的呢？2002年之前，世界各地的志愿者把源代码文件通过 diff 的方式发给 Linus，然后由 Linus本人通过手工方式合并代码！要知道，当时的 linux 的代码量已经很大了，通过人工管理的方式，一是容易出错，二是效率低。于是 Linus 选择了一个商业的版本控制系统 BitKeeper，BitKeeper 的东家 BitMover 公司出于人道主义精神，授权 Linux 社区免费使用这个版本控制系统。最后，出于某种原因，BitMover 公司收回了 linux 社区的免费使用权，于是 Linus 花了两周时间自己用 C 写了一个分布式版本控制系统，这就是 git 的由来了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/816c1e8add6641ef86c6e28530085226~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">git 的工作区域和流程</h2>
<p>要想弄懂 git 是怎么对我们的代码进行管理的，那首当其冲的是了解 git 的工作区域是如何构成的。因为，只有彻底弄懂了 git 工作区域的构成，你才可以在适当的区域使用合适的命令。如下图所示，此图包含了 git 的4个工作区和一些常见的操作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/487723f3c50945138a49628809587bbf~tplv-k3u1fbpfcp-zoom-1.image" alt="git" loading="lazy" referrerpolicy="no-referrer"></p>
<p>workspace：工作区，就是平时进行开发改动的地方，是当前看到最新的内容，在开发的过程也就是对工作区的操作</p>
<p>Index：暂存区，当执行<code>git add </code>的命令后，工作区的文件就会被移入暂存区，暂存区标记了当前工作区中那些内容是被 git 管理的，当完成某个需求或者功能后需要提交代码，第一步就是通过 git add 先提交到暂存区。</p>
<p>Repository：本地仓库，位于自己的电脑上，通过<code>git commit</code> 提交暂存区的内容，会进入本地仓库。</p>
<p>Remote：远程仓库，用来托管代码的服务器，远程仓库的内容能够被分布在多个地点的处于协作关系的本地仓库修改，本地仓库修改完代码后通过 <code>git push</code>命令同步代码到远程仓库。</p>
<p>一般来说，git 的工作流程分为以下几步</p>
<pre><code class="copyable">1.在工作区开发，添加，修改文件。
2.将修改后的文件放入暂存区。
3.将暂存区域的文件提交到本地仓库。
4.将本地仓库的修改推送到远程仓库。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">git 基本操作</h2>
<h3 data-id="heading-4">git add</h3>
<p>添加文件到暂存区</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 添加某个文件到暂存区，后面可以跟多个文件，以空格区分</span>
git add xxx
<span class="hljs-comment"># 添加当前更改的所有文件到暂存区。</span>
git add .
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">git commit</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 提交暂存的更改，会新开编辑器进行编辑</span>
git commit 
<span class="hljs-comment"># 提交暂存的更改，并记录下备注</span>
git commit -m <span class="hljs-string">"you message"</span>
<span class="hljs-comment"># 等同于 git add . && git commit -m</span>
git commit -am
<span class="hljs-comment"># 对最近一次的提交的信息进行修改,此操作会修改commit的hash值</span>
git commit --amend
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">git pull</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 从远程仓库拉取代码并合并到本地，可简写为 git pull 等同于 git fetch && git merge </span>
git pull <远程主机名> <远程分支名>:<本地分支名>
<span class="hljs-comment"># 使用rebase的模式进行合并</span>
git pull --rebase <远程主机名> <远程分支名>:<本地分支名>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">git fetch</h3>
<p>与 <code>git pull</code> 不同的是<code>git fetch</code>操作仅仅只会拉取远程的更改，不会自动进行merge操作。对你当前的代码没有影响</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 获取远程仓库特定分支的更新</span>
git fetch <远程主机名> <分支名>
<span class="hljs-comment"># 获取远程仓库所有分支的更新</span>
git fetch --all
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">git branch</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 新建本地分支，但不切换</span>
git branch <branch-name> 
<span class="hljs-comment"># 查看本地分支</span>
git branch
<span class="hljs-comment"># 查看远程分支</span>
git branch -r
<span class="hljs-comment"># 查看本地和远程分支</span>
git branch -a
<span class="hljs-comment"># 删除本地分支</span>
git branch -D <branch-nane>
<span class="hljs-comment"># 重新命名分支</span>
git branch -m <old-branch-name> <new-branch-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">工作中使用 git 解决问题的场景</h2>
<h3 data-id="heading-10">git rebase 让你的提交记录更加清晰可读</h3>
<h4 data-id="heading-11">git rebase 的使用</h4>
<p>rebase 翻译为变基，他的作用和 merge 很相似，用于把一个分支的修改合并到当前分支上。</p>
<p>如下图所示，下图介绍了经过 rebase 前后提交历史的变化情况。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8f7c01bf3df4485929f93e8415bbe09~tplv-k3u1fbpfcp-zoom-1.image" alt="WechatIMG2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们来用一个例子来解释一下上面的过程。</p>
<p>假设我们现在有2条分支，一个为 master ，一个为 feature/1，他们都基于初始的一个提交<code>add readme</code>进行检出分支，之后，master分支增加了<code>3.js</code>,和<code>4.js</code>的文件，分别进行了2次提交，feature/1也增加了<code>1.js</code>和<code>2.js</code>的文件，分别对应以下2条提交记录。</p>
<p>此时，对应分支的提交记录如下。</p>
<p>master 分支如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a39f7f2b2a8f48d5869aa79c886c3d18~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210531144909187.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>feature/1分支如下图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e2c9017b6fb482e8dcf983d995a2531~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210531145504071.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结合起来看是这样的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/359b096aa495413a923c44b7a06620da~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210531145553107.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，切换到 feature/1 分支下，执行 <code>git rebase master</code> ,成功之后，通过 log 查看记录。</p>
<p>如下图所示：可以看到先是逐个应用了 mater 分支的更改，然后以 master 分支最后的提交作为基点，再逐个应用 feature/1的每个更改。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c67d61591e1c4404ab72cdc097d93ae3~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210531150719965.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，我们的提交记录就会非常清晰，没有分叉，上面演示的是比较顺利的情况，但是大部分情况下，rebase 的过程中会产生冲突的，此时，就需要手动解决冲突，然后使用<code>git add</code> 、<code>git rebase --continue</code>的方式来处理冲突，完成 rebase，如果不想要某次 rebase 的结果，那么需要使用 <code>git rebase --skip</code>来跳过这次 rebase。</p>
<h4 data-id="heading-12">git merge 和 git rebase 的区别</h4>
<p>不同于 <code>git rebase</code>的是，<code>git merge</code> 在不是 <code>fast-forward</code>（快速合并）的情况下，会产生一条额外的合并记录，类似<code>Merge branch 'xxx' into 'xxx'</code>的一条提交信息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/229cb2713bb34cef85604eed7996e612~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210531151838328.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外，在解决冲突的时候，用 merge 只需要解决一次冲突即可，简单粗暴，而用 rebase 的时候 ，需要一次又一次的解决冲突。</p>
<h4 data-id="heading-13">git rebase 交互模式</h4>
<p>​在开发中，常会遇到在一个分支上产生了很多的无效的提交，这种情况下使用 rebase 的交互式模式可以把已经发生的多次提交压缩成一次提交，得到了一个干净的提交历史，例如某个分支的提交历史情况如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f1790df19d64a379d19a60606e3b701~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210518211345258.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>进入交互式模式的方式是执行：</p>
<pre><code class="copyable">git rebase -i <base-commit>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数<code>base-commit</code>就是指明操作的基点提交对象，基于这个基点进行 rebase 的操作，对于上述提交历史的例子，我们要把最后的一个提交对象（ac18084）之前的提交压缩成一次提交，我们需要执行的命令格式是：</p>
<pre><code class="hljs language-git copyable" lang="git">git rebase -i ac18084
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时会进入一个 vim 的交互式页面，编辑器列出的信息像下列这样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae4c6e5f5cc849fab17541bf450cd774~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210518212036198.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>想要合并这一堆更改，我们要使用 squash 策略进行合并，即把当前的 commit 和它的上一个 commit 内容进行合并， 大概可以表示为下面这样。</p>
<pre><code class="copyable">pick  ... ...
s     ... ... 
s     ... ... 
s     ... ... 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改文件后 按下<code>:</code>然后<code>wq</code>保存退出，此时又会弹出一个编辑页面，这个页面是用来编辑提交的信息，修改为<code>feat: 更正</code>,最后保存一下，接着使用<code>git branch</code>查看提交的 commit 信息，rebase 后的提交记录如下图所示，是不是清爽了很多？rebase 操作可以让我们的提交历史变得更加清晰。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2a0c44a207f4ffe8b817fda2df931e5~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210518212812000.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>特别注意，只能在自己使用的 feature 分支上进行 rebase 操作，不允许在集成分支上进行 rebase，因为这种操作会修改集成分支的历史记录。</p>
</blockquote>
<h3 data-id="heading-14">使用 git cherry-pick 获取指定的 commit</h3>
<p><code>git cherry-pick</code>可以理解为”挑拣”提交，和 merge 合并一个分支的所有提交不同的是，它会获取某一个分支的单笔提交，并作为一个新的提交引入到你当前分支上。当我们需要在本地合入其他分支的提交时，如果我们不想对整个分支进行合并，而是只想将某一次提交合入到本地当前分支上，那么就要使用<code>git cherry-pick</code>了。</p>
<p>如下场景，以下有三条分支，feature/cherry-pick1 和 feature/cherry-pick2 都是基于 master 拉出来的两条功能性分支，对应的分支 log 如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30b8ea10aca14d699d7a45c16405c07e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210518221001432.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43fcf4484b8647a7a04aff03a4235c28~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210518221010458.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>master 分支的提交如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6e50915b5734e5e8de925209468e782~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210518221051734.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在 master 只需要 feature/cherry-pick1 和 feature/cherry-pick2 有关 change 的修改，并不关心 fix 内容的修改。此时就可以用<code>cherry-pick</code>指令了。</p>
<p>语法： <code>git cherry-pick [commit-hash]</code></p>
<p><code>commit-hash</code> 表示的是某次 commit 的 hash 值。现在，依次执行以下两条指令 <code>git cherry-pick e0bb7f3</code>  <code>git cherry-pick c9a3101</code>, 过程中，如果出现冲突，解决冲突后 进行<code>git add </code>，接着执行 <code>git cherry-pick --continue</code>，最后，master 上的提交如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52a136df5fe34ee689ccd0089c320749~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210518235707190.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，master 分支上应用了需要的提交，就达到了我们想要的效果。如果需要多个<code>cherry-pick</code>需要同步到目标分支，可以简写为<code>git cherry-pick <first-commit-id>...<last-commit-id></code>，这是一个左开右闭的区间，也就时说 <code>first-commit-id</code>提交带来的代码的改动不会被合并过去，如果需要合并过去，可以使用<code>git cherry-pick <first-commit-id>^...<last-commit-id></code>，它表示包含<code>first-commit-id</code>到<code>last-commit-id</code>在内的提交都会被合并过去。</p>
<h3 data-id="heading-15">使用 git revert 回滚某次的提交</h3>
<p>想象这么一个场景，你的项目最近有2个版本要上线，这两个版本还伴随着之前遗留的 bug 的修复，一开始的时候，你将 bug 修复在了第一个版本的 release 分支上，突然在发版前一天，测试那边反馈，需要把第一个版本修复 bug 的内容改在第二个版本上，这个时候，第一个版本的集成分支的提交应该包括了第一个版本的功能内容，遗留 bug 修复的提交和其他同事提交的内容，想要通过 reset 的方式摘除之前的关于 bug 修复的 commit 肯定是不行的，同时，这种做法比较危险，此时，我们既不想破坏之前的提交记录，又想撤回我们遗留 bug 的 commit 记录应该怎么做呢？<code>git revert </code> 就派上了用场。</p>
<blockquote>
<p><code>git revert</code> 撤销某次操作，此操作不会修改原本的提交记录，而是会新增一条提交记录来抵消某次操作。</p>
</blockquote>
<p>语法： <code>git revert <commit-id></code>针对普通commit</p>
<p><code>git revert <commit-id> -m</code> 针对merge的commit</p>
<p>下面就用一个案例来理解一下这个命令，如下图所示，假设被红框框起来的地方是会引起 bug 的一次提交，在他的提交之后，又进行了2次提交，其中包含了其它同事的提交。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/904d984f27ab470b8c847c5ab50bb0e2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519142702752.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时想把引起提交的 bug 的干掉，执行<code>git revert 1121932</code>，执行操作后，再打开查看日志，如下图所示，可以看到是新增了一条 commit 记录，之前的 commit 记录并没有消失，此时也达到了代码回退的效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01fadf8b43de4fb3bfab24f633c256da~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519142824836.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此外 git revert 也可以回滚多次的提交</p>
<p>语法：<code>git revert [commit-id1] [commit-id2] ...</code>  注意这是一个前开后闭区间，即不包括 commit1，但包括 commit2。</p>
<p>回滚我们的提交有二种方式，一种是上文提到的<code>git revert</code>命令外，还可以使用<code>git reset</code>命令，那么它们两者有什么区别呢？</p>
<p><code>git revert</code>会新建一条 commit 信息，来撤回之前的修改。</p>
<p><code>git reset</code>会直接将提交记录退回到指定的 commit 上。</p>
<p>对于个人的 feature 分支而言，可以使用<code>git reset</code>来回退历史记录，之后使用<code>git push --force</code>进行推送到远程，但是如果是在多人协作的集成分支上，不推荐直接使用<code>git reset</code>命令，而是使用更加安全的<code>git revert</code>命令进行撤回提交。这样，提交的历史记录不会被抹去，可以安全的进行撤回。</p>
<h3 data-id="heading-16">使用 git stash 来暂存文件</h3>
<p>会有这么一个场景，现在你正在用你的 feature 分支上开发新功能。这时，生产环境上出现了一个 bug 需要紧急修复，但是你这部分代码还没开发完，不想提交，怎么办？这个时候可以用 <code>git stash</code>命令先把工作区已经修改的文件暂存起来，然后切换到 hotfix 分支上进行 bug 的修复，修复完成后，切换回 feature 分支，从堆栈中恢复刚刚保存的内容。</p>
<p>基本命令如下</p>
<pre><code class="copyable">git stash //把本地的改动暂存起来
git stash save "message" 执行存储时，添加备注，方便查找。
git stash pop // 应用最近一次暂存的修改，并删除暂存的记录
git stash apply  // 应用某个存储,但不会把存储从存储列表中删除，默认使用第一个存储,即stash@&#123;0&#125;，如果要使用其他个，git stash apply stash@&#123;$num&#125; 。
git stash list // 查看stash有哪些存储
git stash clear // 删除所有缓存的stash
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面通过几幅图对 <code>stash</code>的命令做进一步了解。</p>
<p>此时，我正在开发一个新功能，修改了<code>1.js</code> 文件里的内容</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16d276327e5740659873fec37e9ef3cf~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519175036869.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还没开发完成，这个时候，我想去 hotfix 分支上修复 bug，得暂停下开发切换到 hotfix 分支，但是现在工作区还有内容，此时如果切换分支，git 会报出下面的错误</p>
<pre><code class="hljs language-bash copyable" lang="bash">error: Your <span class="hljs-built_in">local</span> changes to the following files would be overwritten by checkout:
        1.js
Please commit your changes or stash them before you switch branches.
Aborting
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面那句话的意思就是说工作区有文件修改，不能提交，需要先进行 commit 或者 stash 操作，执行<code>git stash</code>,结果如下</p>
<pre><code class="hljs language-bash copyable" lang="bash">Saved working directory and index state WIP on stash: 22e561c feat: add 1.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，我们的工作区已经干净了，可以切换到 hotfix 分支进行 bug 修复的工作，假设我们现在 bug 修复完成了，继续切回 feature 分支进行原本功能的开发，此时只需要执行 <code>git stash pop</code>，之前我们暂存的修改就会恢复到工作区，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6890327cc50049f4a80e373fb327e2b9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519185011012.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们想要暂存文件，切换分支做某些事的时候，可以用<code>git stash</code>这种机制帮助开发。</p>
<p>推荐在使用 stash 的相关命令时，每一次暂存的时候，不要直接使用 <code>git stash</code>命令进行暂存下来，而是使用<code>git stash save "message..."</code>这种方式给本次的提交做一个信息的记录，这样，想应用更改的时候，先通过<code>git stash list</code>查看一下所有的暂存列表。之后，推荐使用<code>git stash apply stash@$&#123;num&#125;</code>的方式进行应用对应的 stash，这样不会清空已有的 stash 的列表项，并且能应用到当前的工作区，不需要这个暂存的话，再手动清除就可以了。</p>
<h3 data-id="heading-17">不同的工作区域撤销更改</h3>
<p>开发中，我们经常需要回退代码的操作，在不同的工作区域中，回退代码的方式也是不相同的。如下图所示，假设现在要在 feature/revoke 分支上进行开发,</p>
<p>首先通过 <code>git status</code>查看下现在的状态。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/704c2633fadd42658c757b36d1eeda20~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210520115802579.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前我们的工作区是很干净的，没有任何修改的操作，此时，修改一下代码再次查看状态，可以看到，<code>1.js</code>这个文件被修改了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fbd05028d0e4f888f42be99aec426fc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210520115934693.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在我们想把<code>1.js</code>这个文件恢复到修改前的状态，即撤回工作区的修改，就可以使用 <code>git checkout -- <filename></code>的命令，如果要撤回多个文件的修改，文件之间使用空格隔开，如下图所示，我们撤回了<code>1.js</code>文件的修改，工作区也恢复干净了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/213400cc055a4f7e82c9e6b0a3fa1982~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210520120242475.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果说现在我们对文件进行了修改，并且已经提交到暂存区了，这部分文件我们不想要的话，那么就可以通过 <code>git reset <filename></code>的命令来对特定的文件进行撤销，<code>git reset</code>会撤回所有存在暂存区的文件，如下图所示，查看前后的状态可知，文件最后成功撤回到工作区了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/049081f0bac649e49d1335ddab4ff460~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210520141538130.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">配置 git alias提升工作效率</h3>
<p>一般我们在工作中，接到开发任务后，需要新创建一个分支进行开发  此时需要 用到 <code>git branch</code> 、<code>git checkout </code>、 <code>git pull</code>等命令，在我们一顿操作后，开发完成，到了提交代码的阶段，又要诸如此类 <code>git add</code> 、 <code>git commit</code>、<code>git push</code> 等命令，虽然简单，但是输入起来也是不够简洁，作为一个程序员，开发程序就是为了提高我们的效率的，懒是人类进步的源泉，所以我们可以通过配置别名的方式，简化这些命令。</p>
<p>它的基本用法是 <code>git config --global alias.<简化的字符> 原始命令</code></p>
<p>如下面的例子：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git config --global alias.co checkout
$ git config --global alias.ci commit
$ git config --global alias.br branch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里将 <code>co</code>表示<code>checkout</code>， <code>ci</code>表示<code>commit</code> ，<code>br</code> 表示<code>branch</code>,  以后提交就可以简写成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3aad9af59c954391a7c652262f0877a9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519152804390.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>--global</code> 是全局参数，也就是配置一次后，这些命令可以在这台电脑下的所有仓库都适用。这些命令其实是更新你全局的 .gitconfig 文件，该文件用来保存全局的 git 配置，<code>vim ~/.gitconfig</code>，执行这段命令后，显示如下，下图展示了刚才通过 <code>git config --global alias</code> 添加的 alias</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b737b7f04ca54e2399e5853c6195f851~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519153624712.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也可以通过修改这个文件的 alias 项来设置别名。</p>
<p>这里分享一个我自己常用的别名设置，把以下配置替换到 <code>.gitconfig</code>文件里的<code>[alias]</code>所属的区域，然后就可以愉快的使用了~</p>
<pre><code class="hljs language-bash copyable" lang="bash">[<span class="hljs-built_in">alias</span>]
st = status -sb
co = checkout
br = branch
mg = merge
ci = commit
ds = diff --staged
dt = difftool
mt = mergetool
last = <span class="hljs-built_in">log</span> -1 HEAD
latest = for-each-ref --sort=-committerdate --format=\"%(committername)@%(refname:short) [%(committerdate:short)] %(contents)\"
ls = <span class="hljs-built_in">log</span> --pretty=format:\"%C(yellow)%h %C(blue)%ad %C(red)%d %C(reset)%s %C(green)[%cn]\" --decorate --date=short
hist = <span class="hljs-built_in">log</span> --pretty=format:\"%C(yellow)%h %C(red)%d %C(reset)%s %C(green)[%an] %C(blue)%ad\" --topo-order --graph --date=short
<span class="hljs-built_in">type</span> = cat-file -t
dump = cat-file -p
lg = <span class="hljs-built_in">log</span> --color --graph --pretty=format:<span class="hljs-string">'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'</span> --abbrev-commit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们每次想查看 git 的历史记录,就不用输入那么一长串命令 直接使用 <code>git lg</code> ，下图是 axios 源码里的提交记录,使用封装后的<code>git lg</code>查看的效果图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11f48b0432d648979304aade8dbf4f01~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519162327693.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分支之间的关系一眼就很明了，在哪个 commit 上进行的 merge 操作也很清晰，可以帮助我们很好的追溯历史的提交和解决问题。</p>
<h2 data-id="heading-19">总结</h2>
<p>本文由浅入深的的讲解了 git 的环境搭建，基本用法，以及工作中使用较为高频的git命令的用法，无论你是前端后端还是其它端的开发，日常工作中少不了对 git 的使用，我们不仅要会用，还要用的漂亮，用的灵活，用的稳健。这样才能在和同事协作项目的时候更加得心应手，学会了本文这些 git 的使用技巧后，在日常工作中多多练习，相信会给你带来很大的收获！</p>
<h2 data-id="heading-20">参考文献</h2>
<p><a href="https://www.ruanyifeng.com/blog/2014/06/git_remote.html" target="_blank" rel="nofollow noopener noreferrer">阮一峰的git教程</a></p>
<p><a href="https://juejin.cn/post/6844903603694469134#heading-3" target="_blank">Git merge和rebase分支合并命令的区别</a></p>
<h2 data-id="heading-21">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6971586506011967519" target="_blank">v8 执行 js 的过程</a></p>
<p><a href="https://juejin.cn/post/6968988552075952141" target="_blank">手把手带你入门Webpack Plugin</a></p>
<h2 data-id="heading-22">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://www.zoo.team/openweekly/" target="_blank" rel="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-23">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2cd4a6446934dbc9144a60ee4f82e59~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            