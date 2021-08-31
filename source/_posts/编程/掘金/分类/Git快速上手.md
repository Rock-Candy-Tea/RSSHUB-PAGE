
---
title: 'Git快速上手'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4344'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 19:20:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=4344'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>git作为一个先进的版本管理工具，已经被广泛应用在大量项目中。近来发现了一个非常不错的git学习网站，虽然比较基础，但是可视化的界面能够帮助新人快速理解git每项指令的功能，同时也可以一定程度上的查漏补缺。
网站地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flearngitbranching.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://learngitbranching.js.org/" ref="nofollow noopener noreferrer">learngitbranching.js.org/</a>
而本文也记录了一些常用的git指令和使用技巧</p>
<h2 data-id="heading-1">常用git指令</h2>
<h3 data-id="heading-2">新建仓库</h3>
<p>在当前目录初始化一个git仓库
<code>git init</code>
新建一个目录，初始化一个git仓库
<code>git init [projectName]</code>
用于从远程仓库进行克隆，一般可以选择通过https或者ssh方式
<code>git clone [url]</code></p>
<h3 data-id="heading-3">配置</h3>
<p>对于刚安装git的新人，一般需要配置邮箱和用户名，建议使用全局方式配置
<code>git conifg [--global] user.name "[username]"</code>
<code>git conifg [--global] user.email "[email]"</code>
可以查看当前的git配置
<code>git config --list</code>
可以直接编辑git配置文件，之前通过命令行配置的在此也可以看到
<code>git config -e [--global]</code></p>
<h3 data-id="heading-4">增加、删除文件</h3>
<p>这里需要简单介绍一下git中工作区和暂存区的概念</p>
<ul>
<li>工作区可以简单理解为你在当前仓库的种种改动，git可以检测到但是并未将之准备为下次提交的内容。需要用户将之添加到暂存区。</li>
<li>暂存区可以简单理解为，下次执行提交中会被提交上去的文件。</li>
<li>整个工作流为： 你修改了某个文件 -> 该文件变为工作区文件 -> 你添加该文件进入暂存区 -> 提交暂存区文件，该文件被提交</li>
</ul>
<p>添加指定文件到暂存区
<code>git add [file1] [file2] ...</code>
添加指定目录到暂存区（包含该目录下所有文件）
<code>git add [dir]</code>
添加当前目录下所有文件到暂存区
<code>git add .</code>
删除工作区文件，并将“删除”这个操作放入暂存区
<code>git rm [file1] [file2] ...</code>
停止追踪文件，但是该文件会保留在工作区，类似gitignore的作用
<code>git rm --cached [file]</code>
改名文件，并将“改名”这个操作放入暂存区
<code>git mv [origin-name] [target-name]</code></p>
<h3 data-id="heading-5">代码提交</h3>
<p>把暂存区内容提交到仓库， 最常用的提交指令
<code>git commit -m "message"</code>
提交暂存区中的指定文件到仓库
<code>git commit [file1] [file2] ... -m "message"</code>
直接将工作区自从上次commit之后的变化，提交到仓库（跳过暂存区）
<code>git commit -a</code>
使用一次新的commit，替代上一次提交,常用于简单修复
如果代码没有任何新变化，则用来改写上一次commit的提交信息
<code>git commit --amend -m [message]</code></p>
<h3 data-id="heading-6">分支操作</h3>
<p>git中的分支是一个非常强大的功能，新建、删除、切换分支速度极快，可以多多使用</p>
<p>列出所有本地分支
<code>git branch</code>
列出所有远程分支
<code>git branch -r</code>
列出所有本地和远程分支
<code>git branch -a</code>
新建一个分支，并且留在当前分支
<code>git branch [branch-name]</code>
新建一个分支，并切换到新的分支上
<code>git checkout -b [branch-name]</code>
从某一个commit记录为起点，新建一个分支；其中commit中填入commit的hash或者tag（如果有标签）（下同）
<code>git branch [branch-name] [commit] </code>
新建一个分支，并于远程的一个分支建立追踪关系
<code>git branch --track [branch-name] [remote-branch]</code>
切换分支
<code>git checkout [branch-name]</code>
合并指定分支到当前分支
<code>git merge [branch-name]</code>
合并指定分支到当前分支，并生成线性的记录
<code>git rebase [branch-name]</code>
交互式的rebase
<code>git rebase [branch] -i</code>
选择某一次提交（任意分支上的），合并到当前分支
<code>git cherry-pick [commit]</code>
删除分支
<code>git branch -d [branch-name]</code>
删除远程分支
<code>git branch -dr [origin/branch]</code>
<code>git push origin --delete [branch-name]</code></p>
<h3 data-id="heading-7">标签</h3>
<p>标签可以用来给某一次提交添加一个可以追踪的标记，该标记不受分支影响，不会变化，可以在任何情况下被追踪。对于某一次重大提交，常常可以用标签予以标记（如某一次版本发布）</p>
<p>列出所有tag
<code>git tag</code>
在当前的commit上新建一个标签
<code>git tag [tag-name]</code>
给指定的commit上新建一个标签
<code>git tag [tag-name] [commit]</code>
删除本地的一个标签
<code>git tag -d [tag-name]</code>
删除远程的一个标签
<code>git push origin :refs/tags/[tag-name]</code>
查看某个标签对应的提交信息
<code>git show [tag-name]</code>
提交指定tag, remote指远程仓库的名字，一般为origin
<code>git push [remote] [tag]</code>
提交所有tag
<code>git push [remote] --tags</code>
以某个标签指定的commit为基点，新建一个分支
<code>git branch [branch-name] [tag-name]</code></p>
<h3 data-id="heading-8">查看信息</h3>
<p>显示有变更的文件
<code>git status</code>
显示当前分支的版本历史
<code>git log</code>
显示commit历史，以及每次commit发生变化的文件
<code>git log --stat</code>
显示指定文件的每一次改动
<code>git log -p [file]</code>
显示指定文件是什么时间被什么人修改的
<code>git blame [file]</code>
显示暂存区与工作区的差异
<code>git diff</code>
显示暂存区与上一次commit之间的差异 （可指定文件）
<code>git diff --cached [file]</code>
显示工作区与当前分支最新commit之间的差异
<code>git diff HEAD</code>
显示你今天写了多少行代码
<code>git diff --shortstat "@&#123;0 day ago&#125;"</code>
显示当前分支最近的几次提交记录（常用来进行恢复）
<code>git reflog</code></p>
<h3 data-id="heading-9">远程同步</h3>
<p>下载远程仓库的所有变动
<code>git fetch [remote]</code>
显示所有远程仓库
<code>git remote -v</code>
显示某个远程仓库的信息
<code>git remote show [remote]</code>
新增一个远程仓库，并命名
<code>git remote add [name] [url]</code>
拉取远程仓库的变化，并与本地分支合并
<code>git pull [remote] [branch]</code>
上传本地分支到远程仓库
<code>git push [remote] [branch]</code>
强行推送当前分支到远程仓库，即使有冲突
<code>git push [remote] --force</code>
推送所有分支到远程仓库
<code>git push [remote] --all</code></p>
<h3 data-id="heading-10">撤销</h3>
<p>恢复暂存区的指定文件到工作区
<code>git checkout [file]</code>
恢复某个commit的指定文件到暂存区与工作区
<code>git checkout [commit] [file]</code>
恢复暂存区的所有文件到工作区
<code>git checkout .</code>
重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
<code>git reset [file]</code>
重置工作区与暂存区，与上一次commit保持一致
<code>git reset --hard</code>
重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
<code>git reset [commit]</code>
重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
<code>git reset --hard [commit]</code>
新建一个commit，用来撤销指定commit
后者的所有变化都将被前者抵消，并且应用到当前分支
常用来对远程仓库进行恢复
<code>git revert [commit]</code>
暂时将未提交的变化移除，稍后再移入
<code>git stash</code>
<code>git stash pop</code></p>
<p>关于git reset指令，其实有 --soft --hard --mixed三种参数，默认为 --mixed参数。
具体详细用法可以参考这篇文章 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000009658888" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000009658888" ref="nofollow noopener noreferrer">git reset详解</a></p>
<h3 data-id="heading-11">HEAD移动</h3>
<p>HEAD在git中是一个非常重要的概念，因此在这里把这部分单独列出来。
HEAD是git中用来标记当前位置的一个指针。
形象的说法就是：你现在在哪，HEAD就指向哪，因为HEAD，git才知道你在哪。</p>
<p>一般情况下，HEAD指向当前分支（上最近的提交），但是在有些时候，我们可以让HEAD指向某一次具体的提交，这也叫做分离HEAD。比如创建分支时，如果不指定commit，那么会在当前HEAD的位置创建分支。</p>
<p>移动HEAD的方法是使用checkout指令，指定一个commid的hash值进行绝对定位
<code>git checkout [commit-id]</code>
我们也可以使用相对定位，以当前HEAD或分支名等可以追踪位置的标记为基准。 ^代表当前位置的前一个提交
<code>git checkout HEAD^</code>
<code>git checkout master^</code>
我们也可以用 ~[number] 来一次移动多次提交
<code>git checkout HEAD~3</code>
<code>git checkout master~5</code></p>
<p>关于HEAD的更多用法可以进一步去搜集资料</p>
<h2 data-id="heading-12">后记</h2>
<p>以上仅仅为git 入门常用的一些指令，熟练之后可以应对一般git的使用场景。
在这里依然十分推荐<a href="https://link.juejin.cn/?target=https%3A%2F%2Flearngitbranching.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://learngitbranching.js.org/" ref="nofollow noopener noreferrer">learngitbranching.js.org/</a>进行实际操作一次，相信对git的使用有很大帮助。</p></div>  
</div>
            