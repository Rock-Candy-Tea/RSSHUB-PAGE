
---
title: 'Git基本使用及HEAD、fetch问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fec5e8e4122e4cdaba0f6d66d8824326~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 23:50:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fec5e8e4122e4cdaba0f6d66d8824326~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">---Git使用</h1>
<h2 data-id="heading-1">Git配置</h2>
<blockquote>
<p><strong>设置签名</strong></p>
<ul>
<li>
<p>项目(仓库)级别<code>仅在当前本地库有效</code></p>
<pre><code class="copyable">git config user.name tom  #设置用户名tom
git config user.email liu@qq.com #设置用户邮箱
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>系统用户级别<code>仅在当前登录的操作系统用户有效</code></p>
</li>
</ul>
<pre><code class="copyable">git config --global user.name tom
git config --global user.email liu@qq.com
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优先级别：<code>项目级别</code>  >  <code>系统级别</code></p>
<p>信息保存位置：<code>~/.gitconfig 文件</code></p>
</blockquote>
<blockquote>
<p><strong>忽略文件.gitignore</strong>
当我们有无需上传至线上仓库的文件，比如我们项目中的npm包(node_modules)，它在我们项目中是很重要的，但是它占的内存也是很大的，所以一般我们用Git管理的时候是不需要添加npm包的.此时我们只需在项目中新建一个.gitignore文件，并写入 <code>node_modules/</code>，git在之后的操作会自动忽略node_modules的所有文件
<a href="https://www.liaoxuefeng.com/wiki/896043488029600/900004590234208" target="_blank" rel="nofollow noopener noreferrer">.gitignore相应书写规则</a></p>
</blockquote>
<h2 data-id="heading-2">Git四个关键区域</h2>
<p>对于git操作流程，主要有一下四个关键区域：工作区（workspace），暂存区（Index），本地仓库（Repository）,远程仓库（Remote）</p>
<ol>
<li>工作区
本地电脑存放项目文件的地方</li>
<li>暂存区
就是将文件暂存的地方，通常使用add命令将工作区文件添加进暂存区内</li>
<li>本地仓库</li>
</ol>
<p>通常通过commit等命令将暂存区提交给master分支上，也就是意味打了一个版本，也可以说代码提交到了本地仓库中
4. 远程仓库
线上的git服务器，如gitlab，github，gitee上的项目就是一个远程仓库
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fec5e8e4122e4cdaba0f6d66d8824326~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">Git操作指令</h2>
<h3 data-id="heading-4">一.工作区</h3>
<blockquote>
<h5 data-id="heading-5"><strong>1.新建仓库</strong></h5>
</blockquote>
<p>将工作区中的项目配置git进行管理，将项目使用git初始化</p>
<pre><code class="copyable">git init
注意：生成的 .git 目录中存放的是本地库相关文件，不要删除
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从远程仓库拉取项目：</p>
<pre><code class="copyable">git clone <url>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h5 data-id="heading-6"><strong>2.向暂存区提交文件</strong></h5>
</blockquote>
<p>提交工作区所有文件至暂存区</p>
<pre><code class="copyable">git add .
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提交工作区指定文件至暂存区</p>
<pre><code class="copyable">git add <file 0> <file 1> .....<file n>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提交工作区指定文件夹至暂存区</p>
<pre><code class="copyable">git add [dir]
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h5 data-id="heading-7"><strong>3.撤销删除</strong></h5>
</blockquote>
<p>撤销、丢弃工作区的修改。也就是就是让这个文件回到最近一次git commit或git add时的状态。</p>
<pre><code class="copyable">git checkout --<file>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时删除工作区和暂存区文件</p>
<pre><code class="copyable">git rm <file1> <file2>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取消暂存区已经暂存的文件：</p>
<pre><code class="copyable">git reset HEAD <file>...
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h5 data-id="heading-8"><strong>3.查看信息</strong></h5>
</blockquote>
<p>查询当前工作区所有文件的状态</p>
<pre><code class="copyable">git status
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较工作区中当前文件和暂存区之间的差异</p>
<pre><code class="copyable">git diff
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">二.暂存区</h3>
<blockquote>
<h5 data-id="heading-10"><strong>1.向版本库提交文件</strong></h5>
</blockquote>
<p>提交更改</p>
<pre><code class="copyable">git commit -m [message]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把暂存区的指定文件提交到本地仓库中的当前所在分支</p>
<pre><code class="copyable">git commit [file1] [file2] ... -m [message]
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h5 data-id="heading-11"><strong>2.查看信息</strong></h5>
</blockquote>
<p>比较暂存区与上一版本的差异</p>
<pre><code class="copyable">git diff --cached
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较暂存区指定文件与上一版本的差异</p>
<pre><code class="copyable">git diff <file-name> --cached
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看历史记录</p>
<pre><code class="copyable">git log #可以显示所有提交过的版本信息
git reflog  #常用(可以查看所有分支的所有操作记录（包括已经被删除的 commit 记录和 reset 的操作）)
git log --greph #图形显示,更直观
git log --pretty=oneline #漂亮一行显示
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h5 data-id="heading-12"><strong>3.分支管理</strong></h5>
</blockquote>
<p>创建分支</p>
<pre><code class="copyable">git branch <branch-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从当前分支切换到其他分支</p>
<pre><code class="copyable">git checkout <branch-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除分支</p>
<pre><code class="copyable">git branch -d <branch-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>指定分支合并到当前分支</p>
<pre><code class="copyable">git merge <分支名>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示本地仓库的所有分支</p>
<pre><code class="copyable">git branch
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h5 data-id="heading-13"><strong>4.解决冲突</strong></h5>
</blockquote>
<ul>
<li>第一步：编辑，删除特殊标记<code><<<</code> <code>===</code></li>
<li>第二步：修改到满意位置，保存退出</li>
<li>第三步：添加到缓存区  <code>git  add 文件名</code></li>
<li>第四步：提交到本地库<code>git commit -m '日志信息' </code>  <code>注意：后面一定不能带文件名</code></li>
</ul>
<h3 data-id="heading-14">三.本地仓库</h3>
<p>获取远程仓库信息</p>
<pre><code class="copyable">git fetch <远程主机名> <分支名>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将本地仓库某分支推送到远程仓库上</p>
<pre><code class="copyable">git push [remote-name] [branch-name]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看远程仓库的详细信息</p>
<pre><code class="copyable">git remote show origin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取回远程主机某个分支的更新，再与本地的指定分支合并</p>
<pre><code class="copyable">git pull
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">Git中的分支</h2>
<h3 data-id="heading-16">一.Git中的HEAD和master</h3>
<p>在git中，我们可以把HEAD理解成一个指针，这个指针指向我们的开发分支。如下图所示，当我们当前处于master分支时，HEAD指向了master分支。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41e20ccd9c524f5a9e4ccb7bdc75546f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，当我们（checkout）检出到dev分支时，那么HEAD指针就会指向dev指针。</p>
<pre><code class="copyable">git checkout dev
git branch
* dev
  master
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8cf4b2c7e224f18acdf3e009d486df6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们在dev上进行开发提交，dev就会指向当前分支的最新提交，而master分支依旧保持master之前的提交状态
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f6c010a61124fe4810cf8574f9f034e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们把dev合并到master上,git将master指向dev 的当前提交,完成合并
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cab54e9bfc04059aae53f4cd76388fa~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">git checkout master
git merge dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">二.git fetch + git merge（git rebase） = git pull（大多数情况）</h3>
<blockquote>
<p>理解了以上HEAD、master和开发分支的关系是通过指针联系起来，我们可以借此思想顺便理解git fetch + git merge (git rebase) = git pull的原因</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8ab692362294456a32c7be41d376af1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当线上master的位置随着其他人的代码文件提交。线上的master将与本地orgin/master不再对应。本地master也与线上master所处的位置不在同一分支</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/799c0a432b32411b87322877a3de8791~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>目标</strong></p>
</blockquote>
<p><strong>解决这个问题，我们需要将本地开发分支改成如下情况</strong></p>
<blockquote>
<p>我们可以使用git pull一次性完成取回远程主机某个分支的更新，再与本地的指定分支合并，也就是直接把远程仓库版本迭代到本地仓库和远程仓库关联库上,也可以使用以下方法完成我们的目标。但问题是git pull的问题是它把过程的细节都隐藏了起来，以至于你不用去了解git中各种类型分支的区别和使用方法。当然，多数时候这是没问题的，但一旦代码有问题，会别急难找到出错的地方。同时本地工作目录在未经确认的情况下就会被远程分支更新，所以会比较推荐使用git fetch</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ec6d4a649ae48db80d6f575460c48f0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">git fetch + git merge（git rebase）</h4>
<p>git fetch后本地的工作区（workspace）不会自动生成一份可编辑的副本，抓取结果存储于版本库（Repository），也就是图中版本A1，A2
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa2972c75e27423daefc4c4bf2e8d9fc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d337e10ff3ba4caaaa8651e7983cfdbf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们把git merge 改变为 git rebase也会有大致相同的效果，并且此时开发分支master并没有合并过后的痕迹
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fee094d816774dd6b33847a867900858~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            