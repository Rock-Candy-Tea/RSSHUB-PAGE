
---
title: '代码版本控制用SVN还是Git好？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic1.zhimg.com/v2-70e1143c6ff4bc23fcff50ecb9a9f21c_1440w.jpg?source=b1748391'
author: 知乎
comments: false
date: Thu, 05 May 2022 09:00:05 GMT
thumbnail: 'https://pic1.zhimg.com/v2-70e1143c6ff4bc23fcff50ecb9a9f21c_1440w.jpg?source=b1748391'
---

<div>   
腾讯技术工程的回答<br><br><h2><b>来分享下鹅厂程序员 </b>@ronhu同学的一篇心得：《<b>从 SVN 到 Git 》</b></h2><blockquote data-pid="k10HUDWe"> 本文从 Git 与 SVN 的对比入手，介绍如何通过 Git-SVN 开始使用 Git，并总结平时工作高频率使用到的 Git 常用命令。</blockquote><h3><b>一、Git vs SVN</b></h3><blockquote data-pid="96zdKA6c"> Git 和 SVN 孰优孰好，每个人有不同的体验。</blockquote><h3><b>Git 是分布式的，SVN 是集中式的</b></h3><p data-pid="xiT-7Wpi">这是 Git 和 SVN 最大的区别。若能掌握这个概念，两者区别基本搞懂大半。因为 Git 是分布式的，所以 Git 支持离线工作，在本地可以进行很多操作，包括接下来将要重磅推出的分支功能。而 SVN 必须联网才能正常工作。</p><h3><b>Git 复杂概念多，SVN 简单易上手</b></h3><p data-pid="Yv_6iXIh">所有同时掌握 Git 和 SVN 的开发者都必须承认，Git 的命令实在太多了，日常工作需要掌握<code>add</code>,<code>commit</code>,<code>status</code>,<code>fetch</code>,<code>push</code>,<code>rebase</code>等，若要熟练掌握，还必须掌握<code>rebase</code>和<code>merge</code>的区别，<code>fetch</code>和<code>pull</code>的区别等，除此之外，还有<code>cherry-pick</code>，<code>submodule</code>，<code>stash</code>等功能，仅是这些名词听着都很绕。</p><p data-pid="wOJkUE0i">在易用性这方面，SVN 会好得多，简单易上手，对新手很友好。但是从另外一方面看，Git 命令多意味着功能多，若我们能掌握大部分 Git 的功能，体会到其中的奥妙，会发现再也回不去 SVN 的时代了。</p><h3><b>Git 分支廉价，SVN 分支昂贵</b></h3><p data-pid="7IwUh2SP">在版本管理里，分支是很常使用的功能。在发布版本前，需要发布分支，进行大需求开发，需要 feature 分支，大团队还会有开发分支，稳定分支等。在大团队开发过程中，常常存在创建分支，切换分支的需求。</p><p data-pid="qKxUjjWC">Git 分支是指针指向某次提交，而 SVN 分支是拷贝的目录。这个特性使 Git 的分支切换非常迅速，且创建成本非常低。</p><p data-pid="8Vh09WQP">而且 Git 有本地分支，SVN 无本地分支。在实际开发过程中，经常会遇到有些代码没写完，但是需紧急处理其他问题，若我们使用 Git，便可以创建本地分支存储没写完的代码，待问题处理完后，再回到本地分支继续完成代码。</p><h3><b>二、Git 核心概念</b></h3><p data-pid="f7Co5WId">Git 最核心的一个概念就是工作流。</p><ul><li data-pid="KQVrOhsP">工作区(Workspace)是电脑中实际的目录。</li><li data-pid="1EEwmGk5">暂存区(Index)类似于缓存区域，临时保存你的改动。</li><li data-pid="yZFEFZ-n">仓库区(Repository)，分为本地仓库和远程仓库。</li></ul><p data-pid="4B6uLn0f">从 SVN 切换到 Git，最难理解并且最不能理解的是暂存区和本地仓库。熟练使用 Git 后，会发现这简直是神设计，由于这两者的存在，使许多工作变得易管理。</p><p data-pid="364eqr6z">通常提交代码分为几步：</p><ol><li data-pid="7lKc7M57"><code>git add</code>从工作区提交到暂存区</li><li data-pid="TWuFCEHY"><code>git commit</code>从暂存区提交到本地仓库</li><li data-pid="xbvDi5lm"><code>git push</code>或<code>git svn dcommit</code>从本地仓库提交到远程仓库</li></ol><p data-pid="NCScE0V5">一般来说，记住以下命令，便可进行日常工作了（图片来源于网络）：</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-70e1143c6ff4bc23fcff50ecb9a9f21c_1440w.jpg?source=b1748391" data-size="normal" data-rawwidth="640" data-rawheight="428" data-default-watermark-src="https://pica.zhimg.com/v2-0a372f5bee8e9f0dba25b62d8109f200_720w.jpg?source=b1748391" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-70e1143c6ff4bc23fcff50ecb9a9f21c_r.jpg?source=b1748391" referrerpolicy="no-referrer"><figcaption>Git命令</figcaption></figure><h3><b>三、Git-SVN 常用命令</b></h3><blockquote data-pid="1G6x_o-5"> 本节命令针对使用 Git-SVN 的开发者，请务必掌握。<br> <br></blockquote><p data-pid="5zS6rI7v">若服务器使用的 SVN，但是本地想要体验 Git 的本地分支，离线操作等功能，可以使用 <code>Git-SVN</code>功能。</p><p data-pid="j_5gwkAH">常用操作如下（图片来源于网络）：</p><figure data-size="normal"><img src="https://pic2.zhimg.com/v2-449d32623e12bf22b99fd94f897163b0_1440w.jpg?source=b1748391" data-size="normal" data-rawwidth="716" data-rawheight="338" data-default-watermark-src="https://pica.zhimg.com/v2-90d110891843452c9ea8a24a50176ee1_720w.jpg?source=b1748391" class="origin_image zh-lightbox-thumb" data-original="https://pic2.zhimg.com/v2-449d32623e12bf22b99fd94f897163b0_r.jpg?source=b1748391" referrerpolicy="no-referrer"><figcaption>Git-SVN</figcaption></figure><div class="highlight"><pre><code class="language-text"><span># 下载一个 SVN 项目和它的整个代码历史，并初始化为 Git 代码库
$ git svn clone -s [repository]

# 查看当前版本库情况
$ git svn info

# 取回远程仓库所有分支的变化
$ git svn fetch

# 取回远程仓库当前分支的变化，并与本地分支变基合并
$ git svn rebase

# 上传当前分支的本地仓库到远程仓库
$ git svn dcommit

# 拉取新分支，并提交到远程仓库
$ svn copy [remote_branch] [new_remote_branch] -m [message]

# 创建远程分支对应的本地分支
$ git checkout -b [local_branch] [remote_branch]
</span></code></pre></div><h3><b>四、初始化</b></h3><blockquote data-pid="tL-JPBvT"> 从本节开始，除特殊说明，以下命令均适用于 Git 与 <code>Git-SVN</code>。<br> <br></blockquote><div class="highlight"><pre><code class="language-text"><span># 在当前目录新建一个Git代码库
$ git init

# 下载一个项目和它的整个代码历史 [Git only]
$ git clone [url]
</span></code></pre></div><h3><b>五、配置</b></h3><div class="highlight"><pre><code class="language-text"><span># 列举所有配置
$ git config -l

# 为命令配置别名
$ git config --global alias.co checkout
$ git config --global alias.ci commit
$ git config --global alias.st status
$ git config --global alias.br branch

# 设置提交代码时的用户信息
$ git config [--global] user.name "[name]"
$ git config [--global] user.email "[email address]"
</span></code></pre></div><p data-pid="fVeYOc2c">Git 用户的配置文件位于 <code>~/.gitconfig</code></p><p data-pid="PqNQB3fQ">Git 单个仓库的配置文件位于 <code>~/$PROJECT_PATH/.git/config</code></p><h3><b>六、增删文件</b></h3><div class="highlight"><pre><code class="language-text"><span># 添加当前目录的所有文件到暂存区
$ git add .

# 添加指定文件到暂存区
$ git add <file1> <file2> ...

# 添加指定目录到暂存区，包括其子目录
$ git add <dir>

# 删除工作区文件，并且将这次删除放入暂存区
$ git rm [file1] [file2] ...

# 停止追踪指定文件，但该文件会保留在工作区
$ git rm --cached [file]

# 改名文件，并且将这个改名放入暂存区
$ git mv [file-original] [file-renamed]
</span></code></pre></div><p data-pid="KCBiiUjT">把文件名 file1 添加到 .gitignore 文件里，Git 会停止跟踪 file1 的状态。</p><h3><b>七、分支</b></h3><div class="highlight"><pre><code class="language-text"><span># 列出所有本地分支
$ git branch

# 列出所有本地分支和远程分支
$ git branch -a

# 新建一个分支，但依然停留在当前分支
$ git branch [branch-name]

# 新建一个分支，并切换到该分支
$ git checkout -b [new_branch] [remote-branch]

# 切换到指定分支，并更新工作区
$ git checkout [branch-name]

# 合并指定分支到当前分支
$ git merge [branch]

# 选择一个 commit，合并进当前分支
$ git cherry-pick [commit]

# 删除本地分支，-D 参数强制删除分支
$ git branch -d [branch-name]

# 删除远程分支
$ git push [remote] :[remote-branch]
</span></code></pre></div><h3><b>八、提交</b></h3><div class="highlight"><pre><code class="language-text"><span># 提交暂存区到仓库区
$ git commit -m [message]

# 提交工作区与暂存区的变化直接到仓库区
$ git commit -a

# 提交时显示所有 diff 信息
$ git commit -v

# 提交暂存区修改到仓库区，合并到上次修改，并修改上次的提交信息
$ git commit --amend -m [message]

# 上传本地指定分支到远程仓库
$ git push [remote] [remote-branch]
</span></code></pre></div><h3><b>九、拉取</b></h3><div class="highlight"><pre><code class="language-text"><span># 下载远程仓库的所有变动 (Git only)
$ git fetch [remote]

# 显示所有远程仓库 (Git only)
$ git remote -v

# 显示某个远程仓库的信息 (Git only)
$ git remote show [remote]

# 增加一个新的远程仓库，并命名 (Git only)
$ git remote add [remote-name] [url]

# 取回远程仓库的变化，并与本地分支合并，(Git only), 若使用 Git-SVN，请查看第三节
$ git pull [remote] [branch]

# 取回远程仓库的变化，并与本地分支变基合并，(Git only), 若使用 Git-SVN，请查看第三节
$ git pull --rebase [remote] [branch]
</span></code></pre></div><h3><b>十、撤销</b></h3><div class="highlight"><pre><code class="language-text"><span># 恢复暂存区的指定文件到工作区
$ git checkout [file]

# 恢复暂存区当前目录的所有文件到工作区
$ git checkout .

# 恢复工作区到指定 commit
$ git checkout [commit]

# 重置暂存区的指定文件，与上一次 commit 保持一致，但工作区不变
$ git reset [file]

# 重置暂存区与工作区，与上一次 commit 保持一致
$ git reset --hard

# 重置当前分支的指针为指定 commit，同时重置暂存区，但工作区不变
$ git reset [commit]

# 重置当前分支的HEAD为指定 commit，同时重置暂存区和工作区，与指定 commit 一致
$ git reset --hard [commit]

# 新建一个 commit，用于撤销指定 commit
$ git revert [commit]

# 将未提交的变化放在储藏区
$ git stash

# 将储藏区的内容恢复到当前工作区
$ git stash pop
</span></code></pre></div><h3><b>十一、查询</b></h3><div class="highlight"><pre><code class="language-text"><span># 查看工作区文件修改状态
$ git status

# 查看工作区文件修改具体内容
$ git diff [file]

# 查看暂存区文件修改内容
$ git diff --cached [file]

# 查看版本库修改记录
$ git log

# 查看某人提交记录
$ git log --author=someone

# 查看某个文件的历史具体修改内容
$ git log -p [file]

# 查看某次提交具体修改内容
$ git show [commit]
</span></code></pre></div><h3><b>写在后面</b></h3><p data-pid="hJjSY04c">从 SVN 到 Git，除本文列举的基础概念和常用命令，包括但不限于<code>如何从 SVN 服务器切换到 Git 服务器</code>，<code>分支模型管理</code>等也非常重要。本文篇幅有限，针对没有介绍到但很重要的知识点会列举到参考资料里，希望作为本文的延伸阅读。</p><p data-pid="hRBmLptV"><b>参考资料</b></p><ol><li data-pid="BKu1B43J"><b><a href="http://link.zhihu.com/?target=https%3A//git-scm.com/book/zh/v2" class=" wrap external" target="_blank" rel="nofollow noreferrer">Git Pro Books</a></b> Git 权威指南</li><li data-pid="u5czv2R6"><b><a href="http://link.zhihu.com/?target=http%3A//www.worldhello.net/gotgit/04-git-model/070-git-svn.html" class=" wrap external" target="_blank" rel="nofollow noreferrer">Git 和 SVN 协同模型</a></b> 详细介绍 Git-SVN 协同模型的使用原理与注意点</li><li data-pid="d42Ii_VI"><b><a href="http://link.zhihu.com/?target=http%3A//www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html" class=" wrap external" target="_blank" rel="nofollow noreferrer">常用 Git 命令清单</a></b> 总结得非常详细的清单，与本文部分内容重合并互补</li><li data-pid="1xS7R5Fh"><b><a href="http://link.zhihu.com/?target=https%3A//github.com/xirong/my-git/blob/master/why-git.md" class=" wrap external" target="_blank" rel="nofollow noreferrer">SVN 和 Git 在日常使用中的明显差异</a></b> 介绍了 Git 和 SVN 的区别，可作为本文的延伸阅读</li><li data-pid="7iQcehFZ"><b><a href="http://link.zhihu.com/?target=https%3A//www.git-tower.com/learn/git/ebook/cn/command-line/advanced-topics/git-flow" class=" wrap external" target="_blank" rel="nofollow noreferrer">git-flow 的工作流程</a></b> 通俗易懂的介绍了 git-flow 的基础工作流程</li><li data-pid="sU14VgWU"><b><a href="http://link.zhihu.com/?target=https%3A//git-scm.com/book/zh/v2/Git-%25E4%25B8%258E%25E5%2585%25B6%25E4%25BB%2596%25E7%25B3%25BB%25E7%25BB%259F-%25E8%25BF%2581%25E7%25A7%25BB%25E5%2588%25B0-Git" class=" wrap external" target="_blank" rel="nofollow noreferrer">SVN 迁移到 Git</a></b> 服务器从 SVN 迁移到 Git 的具体操作方法</li></ol>  
</div>
            