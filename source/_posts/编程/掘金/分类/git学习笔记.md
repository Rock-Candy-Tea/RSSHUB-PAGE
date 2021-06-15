
---
title: 'git学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37dfbd58b12c4c0b8c0d24110dc83e0c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 20:29:56 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37dfbd58b12c4c0b8c0d24110dc83e0c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近公司项目只能在Linux环境提交代码，所以不得不又学习了一下git命令和git。<br>
相关内容大致可分为3个部分：认识git--git的一些概念；上手git--git的一些命令；了解git--git的一些原理。</p>
<h3 data-id="heading-0">认识git</h3>
<p>什么是git？<br>
git是一个分布式的版本控制系统，“分布式”指的是每个开发者本地都存储了一个版本仓库(.git目录)，可基于这个本地版本仓库与远程服务器仓库进行交互。与“分布式”对应的是集中化版本控制系统，如SVN，其中”集中化”是指所有版本记录都存储在中央服务器，客户端本地是基于中央服务器进行版本控制。<br>
<br>
git的优缺点：<br>
git(分布式版本控制系统)的优点：每个人可以独立进行版本控制，与远程服务器无关；哪怕服务器挂了每个人本地也有所有历史记录。<br>
git的缺点：<strong>几乎无</strong>，除了学习成本高一点。<br>
svn(集中化版本控制系统)的优点：便于集中管理，可以看到每个成员的操作，管理员可以轻松掌握每个开发者的权限。<br>
svn缺点：服务器宕机了开发者本地就失去了版本控制的功能，并且万一服务器损坏了就会失去所有的历史版本记录。<br>
<br>
学习git命令之前必须要知道哪些概念？
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37dfbd58b12c4c0b8c0d24110dc83e0c~tplv-k3u1fbpfcp-watermark.image" alt="space.png" loading="lazy" referrerpolicy="no-referrer">
如图，git有几个区域，从右至左依次是：<br>
workspace：工作区<br>
Index/Stage：暂存区 <br>
Repository：版本库(或本地仓库)<br>
Remote：远程仓库<br>
<br>
一个工程被git管理，会有一个.git文件夹，工作区就是指除了.git文件夹外这个工程的所有目录，而暂存区和版本库则存储在.git文件夹内，远程仓库是指远程服务器仓库。</p>
<h3 data-id="heading-1">上手git</h3>
<p>因为git在每个本地都有一个版本库，协同工作是本地版本库与远程版本库之间进行交互，所以git命令大致可分为2大块，本地操作相关的和远程操作相关的<br></p>
<h5 data-id="heading-2">本地操作</h5>
<p>一. 常用提交代码的命令<br>
<strong>git status</strong>；查看工作区文件状态<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7baa4b1118a43f890e96f6faef9b659~tplv-k3u1fbpfcp-watermark.image" alt="status.png" loading="lazy" referrerpolicy="no-referrer">
如图，工作区文件有3种状态：<br>
1.Changes to be committed  文件添加到暂存区未被提交到版本库<br>
2. Changes not staged for commit  文件被修改还未被添加到暂存区<br>
3. Untracked files  文件未被跟踪，也就是未被git管理，一般是新建的文件<br>
<br>
<strong>git add</strong>；将文件从工作区添加到暂存区(git add . 或 git add 文件路径)<br>
<br>
<strong>git commit -m “提交信息”</strong>；将文件从暂存区添加到版本库<br>
<br>
<strong>git commit -a -m “提交信息”</strong>；前2个命令的组合(不能是还未被跟踪的文件)<br>
<br>
说明：每次提交后都会生成一个唯一的提交哈希值，对应这次提交的版本，如下图：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84762b9b7c4e44d89a3ffc9aee0a83b4~tplv-k3u1fbpfcp-watermark.image" alt="commitHash.png" loading="lazy" referrerpolicy="no-referrer">
<br>
除了这几个常用的提交命令外，有时候还需要有其他的操作...<br>
<br>
二. 分支<br>
很多时候都需要用到分支，各分支之间可以是独立的，互不影响。<br>
分支，是一个个版本最终存储的位置。<br>
分支，就是一条时间线，每次git commit形成一个个版本，一个个版本依次存储在分支的一个个提交点上。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46e35dcbcd634eac903d4106f4646499~tplv-k3u1fbpfcp-watermark.image" alt="branch_1.png" loading="lazy" referrerpolicy="no-referrer">
仓库中默认有且仅有一个master分支。<br>
新建一个分支，首先是新建一个指针，新分支的指针和当前分支指向同一个提交点，新分支包含的提交点就是从第一个提交点到分支指针指向的提交点。<br>
在git中有一个名为 HEAD 的特别指针，它指向你正在工作中的本地分支的指针，可以将 HEAD 想象为当前分支的别名。<br>
<br>
在master分支上新建一个dev分支，如下图：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e099bef8d5574535b6b93968492be81c~tplv-k3u1fbpfcp-watermark.image" alt="branch_2.png" loading="lazy" referrerpolicy="no-referrer">
<br>
<strong>git branch</strong>；查看当前仓库的分支，*是当前所在的分支<br>
<strong>git branch 分支名</strong>；新建一个分支<br>
<strong>git checkout 分支名</strong>；切换分支(有坑：本分支的修改有可能被带到切换后的分支，从而产生分支污染)<br>
<strong>git checkout -b 分支名</strong>；新建并切换到这个分支<br>
<strong>git branch -d 分支名</strong>；删除分支<br>
<strong>git branch -D 分支名</strong>；强制删除分支(暂存区未清空或未被合并)<br>
<strong>git merge 分支名</strong>；把分支合并到当前分支<br>
<br>
合并分支有2种情况：<br>
1, 快速合并Fast-forward，不会产生冲突
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a47ebab7d804bb79f790be8dea6d0fc~tplv-k3u1fbpfcp-watermark.image" alt="branch_3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19c5de4e8cc747ce8862cd6679da1361~tplv-k3u1fbpfcp-watermark.image" alt="branch_4.png" loading="lazy" referrerpolicy="no-referrer">
2. 三方合并，有可能产生冲突</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abee1899ef504a50adbd281f975000eb~tplv-k3u1fbpfcp-watermark.image" alt="branch_5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15bb4b12bdd94d2194b0764f05d8e44e~tplv-k3u1fbpfcp-watermark.image" alt="branch_6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决冲突：保留对应的内容并删除掉<<<< ==== >>>>，之后重新add
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73a3517698a1443892f5b4041274f52b~tplv-k3u1fbpfcp-watermark.image" alt="branch_7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>三. 存储<br>
上面提到在切换分支时有坑，避免这个坑有2种方法：一是提交当前的修改，二是可以使用存储stash：将未提交的修改保存到一个栈上，然后在任何时候重新应用这些修改。<br>
<strong>git stash</strong>；将修改保存到一个栈<br>
<strong>git stash list</strong>；查看存储<br>
<strong>git stash apply</strong>；应用最近的存储<br>
<strong>git stash drop 存储名</strong>；移除存储<br>
<strong>git stash pop</strong>; 前2个命令的组合，应用并且移除掉最近的存储<br>
<br>
四. 撤销<br>
很多时候都需要撤销修改，或者回退版本。<br>
<strong>git checkout 文件名</strong>；撤销工作区的修改<br>
<strong>git reset 文件名</strong>；将文件从暂存区撤回<br>
<strong>git commit --amend</strong>；修改上一次的提交(会将暂存区的文件重新提交，并且覆盖上一次的提交信息)<br>
<br>
“reset三部曲”<br>
假设目前的提交是这样：<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe5204553a5d464882ceeac62b5b7e3b~tplv-k3u1fbpfcp-watermark.image" alt="reset_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>git reset --soft HEAD~数字</strong>；只回退HEAD的指向，数字是几就回退几个版本（本质是撤销git commit）<br>
如图：<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd5d50fb52224a5b89c86a19f5336dca~tplv-k3u1fbpfcp-watermark.image" alt="reset_2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>git reset --mixed HEAD~数字</strong>；回退HEAD指向和暂存区<br>
如图：<br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd8734e7be3c486c8f95da88c5663201~tplv-k3u1fbpfcp-watermark.image" alt="reset_3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>git reset --hard HEAD~数字</strong>；回退HEAD，暂存区，和工作目录。(<strong>慎用，会覆盖工作目录</strong>)<br>
如图：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28336250b5db4cf0bdddfdf616210951~tplv-k3u1fbpfcp-watermark.image" alt="reset_4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>说明：以上三个命令中”HEAD~数字”都可替换成提交哈希值<br>
<br>
<strong>git branch 分支名 提交哈希值</strong>；新建一个分支并且指向对应的提交对象(回退版本，<strong>比git reset --hard更安全</strong>)<br>
<br>
五. 打tag<br>
打tag是给历史中的某一个提交打上标签，常用标记发布节点(v1.0 等)<br>
<strong>git tag</strong>；列出所有tag<br>
<strong>git tag 标签名</strong>；新建tag<br>
<strong>git show 标签名</strong>；查看特定tag的提交信息<br>
<strong>git tag -d 标签名</strong>；删除tag<br>
<strong>git checkout 标签名</strong>；检出标签所指向的文件版本(此时处于分离头指针detached HEAD状态，要修改内容必须新建分支)<br>
<br>
六. 其他<br>
<strong>git config -–list</strong>；查看配置信息<br>
<strong>git init</strong>；初始化一个git库<br>
<strong>git diff</strong>；查看文件修改(<strong>git diff 文件名</strong>；)<br>
<strong>git diff --cached</strong>；查看已加入暂存的修改<br>
<strong>git show 提交哈希值</strong>；查看指定的提交内容<br>
<strong>git log</strong>；查看历史记录<br>
<strong>git log --online</strong>； 简化版的提交记录<br>
<strong>git reflog</strong>;  HEAD每次改变时的日志<br>
<strong>git log --oneline --decorate --graph --all</strong>；查看项目分叉历史<br>
<strong>git config --global alias.新命令 旧命令</strong>；为命令配别名（如git config --global alias.lol “log --oneline --decorate --graph --all”就将上一条命令配置成git lol）<br>
<br></p>
<h5 data-id="heading-3">远程操作</h5>
<p>多人协同开发时，往往需要与远程仓库之间推送或获取代码
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e46ac4017004e82a340fb4db4fd7d0e~tplv-k3u1fbpfcp-watermark.image" alt="remote1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>git remote add origin 远程仓库地址</strong>；关联远程仓库(origin为远程仓库的别名，也可叫主机名。需要git init)<br>
<strong>git clone 远程仓库地址</strong>；将远程仓库克隆到本地(不需要git init)<br>
<strong>git remote -v</strong>；查看远程仓库地址<br>
<strong>git push origin 本地分支名:远程分支名</strong>；将本地分支推送到远程分支(本地分支和远程分支一般是同名，可简写为git push origin 本地分支名)<br>
<strong>git push -u origin 本地分支名</strong>；将本地分支推送到同名远程分支，同时指定origin为默认主机，以后就可以不加任何参数执行git push<br>
<strong>git push</strong>；推送代码 <br>
<strong>git fetch origin</strong>；拉取远端所有的提交分支到本地(clone或者fetch时，并不会直接在本地生成一个与远程分支同名的分支，而是生成一个<strong>远程跟踪分支</strong>，它们以(remote)/(branch)形式命名，<strong>指向远端该分支的引用</strong>，远程跟踪分支不可修改，除了master分支会自动跟踪origin/master外，如需跟踪其他远程跟踪分支则要进行下面一个命令的操作)<br>
<strong>git checkout -b 本地分支名 远程跟踪分支名</strong>；创建一个本地分支并且跟踪远程跟踪分支(也可直接将远程跟踪分支merge到当前分支)<br>
<strong>git pull</strong>；拉取代码并且合并 (git fetch和git merge的组合命令)<br>
<strong>git pull origin 远程分支名:本地分支名</strong>；<br>
<strong>git push origin --delete 远程分支名</strong>；删除远程分支<br>
<strong>git branch -u 远程跟踪分支名</strong>；将当前分支跟踪远程跟踪分支(本地分支只有跟踪到远程跟踪分支才能对应到远程仓库的分支)<br>
<strong>git branch -a</strong>； 查看拉取到本地的分支列表<br>
<strong>git branch -vv</strong>； 查看设置的所有跟踪分支<br>
<br></p>
<h3 data-id="heading-4">了解git</h3>
<p>未完......
<br>
<br>
参考链接：<br>
<a href="https://juejin.cn/post/url">www.bilibili.com/video/BV15J…</a><br>
<a href="https://juejin.cn/post/url">www.bilibili.com/video/BV1Mf…</a><br>
<a href="https://juejin.cn/post/url">www.ruanyifeng.com/blog/2014/0…</a><br></p></div>  
</div>
            