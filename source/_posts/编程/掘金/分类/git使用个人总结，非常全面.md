
---
title: 'git使用个人总结，非常全面'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-gold-cdn.xitu.io/2018/4/25/162fcc0987bf1c0a?imageView2/2/w/1956/q/85/interlace/1'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 06:34:12 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2018/4/25/162fcc0987bf1c0a?imageView2/2/w/1956/q/85/interlace/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">git 的配置</h2>
<p>1.下载 Git <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fdownloads" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/downloads" ref="nofollow noopener noreferrer">下载地址</a> ，选择自己系统对应的版本下载即可。</p>
<p>2.生成 ssh 秘钥：打开终端，执行 ssh-keygen -t rsa -C "你公司内部邮箱地址"，此时文件会在 c 盘用户的.shh 文件夹中，复制 id_rsa.pub 的内容到你 gitlab/gitee 等的 ssh 中。</p>
<p>3.查询配置信息</p>
<pre><code class="copyable">列出当前配置：git config --list;
列出repository配置：git config --local --list;
列出全局配置：git config --global --list;
列出系统配置：git config --system --list;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.全局配置 git 的用户名和邮箱</p>
<pre><code class="copyable">git config --global user.name "xxx"
git config --global user.email "xxx@xx.com"
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">四个关键点</h2>
<p>git 的通用操作流程图
<img src="https://user-gold-cdn.xitu.io/2018/4/25/162fcc0987bf1c0a?imageView2/2/w/1956/q/85/interlace/1" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>1.<strong>工作区</strong>：就是你平时存放项目代码的地方</p>
<p>2.<strong>暂存区（Index/Stage）</strong>：数据暂时存放的区域，就是我们使用<strong>git add</strong>提交的区域</p>
<p>3.<strong>本地仓库</strong>：.git 文件夹里管理的本地仓库区域，里面可以包含很多本地分支，也就是通过<strong>git commit</strong>提交的区域</p>
<p>4.<strong>远程仓库</strong>：git 远程仓库，gitlab/gitee/github/svn 等等，通过<strong>git push</strong>提交远程仓库</p>
<p>总结：平时在工作去正常开发，通过 git add 提交代码到暂存区，通过 git commit 提交代码到本地仓库，通过 git push 提交代码到远程仓库</p>
<h2 data-id="heading-2">工作区的操作</h2>
<h3 data-id="heading-3">init(初始化)</h3>
<p>1.从 git 仓库克隆代码</p>
<blockquote>
<p>git 克隆远程仓库项目时如果不指定分支，只会克隆默认分支的内容</p>
</blockquote>
<pre><code class="copyable">git clone -b 分支名称 远程地址 指定的项目名
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.init 项目</p>
<pre><code class="copyable">cd 文件夹
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin 远程地址
git push -u origin 分支名称
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">add</h3>
<p>1.提交工作区所有文件到暂存区：git add .<br>
2.提交工作区中指定文件到暂存区：git add <文件名 1> <文件名 2> ...;<br>
3.提交工作区中某个文件夹中所有文件到暂存区：git add [文件夹名];<br></p>
<h3 data-id="heading-5">rm(删除)</h3>
<p>1.仅从暂存区中删除文件，但是工作区依然还有该文件:git rm --cached <文件名>;<br>
2.删除工作区文件，并且也从暂存区删除对应文件的记录：git rm <文件名 1> <文件名 2>;</p>
<h3 data-id="heading-6">reset/revert(撤销/回滚)</h3>
<p>1.取消暂存区所有暂存的文件：git reset;</p>
<p>2.取消暂存区已经暂存的文件：git reset HEAD <文件名>...;</p>
<p>3.撤销上一次对文件的操作：git checkout --<文件名>。要确定上一次对文件的修改不再需要，如果想保留上一次的修改以备以后继续工作，可以使用 stashing 和分支来处理；</p>
<p>4.使用 reset/revert 回滚代码，二选一</p>
<blockquote>
<p>二者区别(就是是否删除被回滚掉的 commit):</p>
</blockquote>
<blockquote>
<p>revert 是会生成一次新的提交，需要填写提交注释，以前的历史记录都在；</p>
</blockquote>
<blockquote>
<p>reset 是指将 HEAD 指针指到指定提交，历史记录中不会出现放弃的提交记录。</p>
</blockquote>
<p>1.将本地代码回滚到指定 commit:</p>
<pre><code class="copyable">git reset/revert --hard HEAD^ 回退到上个版本
git reset/revert --hard HEAD~3 回退到前3次提交之前，以此类推，回退到n次提交之前
git reset/revert --hard commit_id 退到/进到，指定commit的哈希码（这次提交之前或之后的提交都会回滚）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.回滚后强制提交本地代码上去：git push -f origin 远程分支名</p>
<h3 data-id="heading-7">stash(暂存)</h3>
<p>1.查看所有暂存的记录：git stash list 可用于恢复暂存时查看,会有 stash@&#123;0&#125;:信息，之后通过 0 作为 index 去应用暂存</p>
<p>2.查看暂存记录的详情，提交信息：git stash show 0</p>
<p>3.暂存当前修改：git stash / git stash save '说明信息'，如果经常使用暂存功能，请务必添加说明信息，避免忘记是哪条切换不回来</p>
<p>4.应用暂存（暂存记录仍在）：应用最新暂存 git stash apply 应用指定的暂存 git stash apply 0 如果是同一个文件使用时要先暂存再应用，不然要提交到本地仓库再操作</p>
<p>5.清除暂存：移除指定的储藏 git stash drop 0 应用暂存并将其清除 git stash pop 0</p>
<p>注：不加 stash&#123;0&#125; 都是操作最新的一次（栈顶）暂存,stash&#123;0&#125;就是数字而已，网上很多教程使用 stash@&#123;0&#125;，我在实际操作中都不生效，只需要在后直接加 index 即可。
在实际工作中用到最多的应该是：保存暂存 git stash save '信息'，然后切换分支去做别的事情，然后切回来把保存的暂存应用并删除 git stash pop，如果想要更多骚操作自行百度</p>
<h2 data-id="heading-8">暂存区的操作</h2>
<h3 data-id="heading-9">log(查看)</h3>
<blockquote>
<p>3628164fb26d48395383f8f31179f24e0882e1e0 长长的是 commit-id ea34578 短的是 HEAD 版本</p>
</blockquote>
<p>查看提交历史：git log 显示所有提交过的版本信息，不包括已经被删除的 commit 记录和 reset 的操作</p>
<pre><code class="copyable">commit 7b1e2c6bd3851732d0d3e1d01169cd31042b64bc
Author: libinbin <libinbin@ainirobot.com>
Date:   Sat May 19 17:26:33 2018 +0800
    第三次commit

commit 004ff75d9ccf27b6721f6b6ea86efa92319f4102
Author: libinbin <libinbin@ainirobot.com>
Date:   Sat May 19 17:08:15 2018 +0800
    第一次commit
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fm0_50668851%2Farticle%2Fdetails%2F108651417" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/m0_50668851/article/details/108651417" ref="nofollow noopener noreferrer">gitlog 的具体参数</a></p>
<p>查看所有分支的操作记录：git reflog 包括 reset 掉的记录，使用 cherry-pick 的时候需要执行这句话，查看曾经的提交历史以及被 reset 掉想要重新找回的历史</p>
<pre><code class="copyable">2e39ab1 HEAD@&#123;15&#125;: commit (merge): feat: d
750cf0d HEAD@&#123;16&#125;: commit: feat: f
c5af345 HEAD@&#123;17&#125;: commit (merge): feat: update
062055c HEAD@&#123;18&#125;: checkout: moving from main to test
fb2af28 HEAD@&#123;19&#125;: commit: feat: update
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fchaiyu2002%2Farticle%2Fdetails%2F81773041" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/chaiyu2002/article/details/81773041" ref="nofollow noopener noreferrer">gitlog 的具体参数</a></p>
<h3 data-id="heading-10">commit(提交)</h3>
<p>1.正常提交需要有 add 的内容，若无则无法 commit：git commit -m "提交信息"</p>
<p>2.跳过 add 将暂存区提交：git commit -a -m "提交信息"</p>
<p>3.撤销上一次的提交：git commit --amend</p>
<h3 data-id="heading-11">tag(标签)</h3>
<blockquote>
<p>Git 可以给仓库历史中的某一个提交打上标签，以示重要。 比较有代表性的是人们会使用这个功能来标记发布结点（ v1.0 、 v2.0 等等）</p>
</blockquote>
<p><strong>轻量标签</strong>：就是简单输个标签名即可，不会有任何附带信息 git tag v1.0</p>
<p><strong>附注标签</strong>：需要强制附带备注信息，git tag -a v1.0 -m 第一次发版</p>
<p>查看标签信息与对应的提交信息：git show /git show v1.0</p>
<p>给指定的提交历史打标签：git tag -a v1.0 9fceb02</p>
<p>推送标签到远程：git push origin v1.0 不需要指定分支，它会在远程仓库共享，在仓库中可以找到 tag 并查看</p>
<p>删除本地标签：git tag -d v1.0</p>
<p>删除远程标签：git push origin -d v1.0</p>
<h3 data-id="heading-12">branch(分支)</h3>
<p>创建本地分支：git branch 分支名</p>
<p>切换到本地分支：git checkout 分支名</p>
<p>上面二合一，创建分支并切换到分支：git branch -b 分支名</p>
<p>删除本地分支：git branch -d 分支名</p>
<p>删除远程分支：git push origin --d 远程分支名</p>
<p>合并分支：git merge 分支名 合并远程分支 git merge origin/master</p>
<p>在远程分支的基础上创建本地分支：git checkout -b test origin/master 如果这个记不住：也可以用比较简单容易记的方法就是先创建本地分支，再强制拉取，其实就是拆分</p>
<pre><code class="copyable">git branch test
git checkout test        //这两个又可以合并为git branch -b test
git fetch --all
git reset --hard origin/master  //这四个可以合并为git checkout -b test origin/maset
这个时候远程是没有这个分支的，在提交时要指定提交到远程，会自动创建远程分支，git push origin test
<span class="copy-code-btn">复制代码</span></code></pre>
<p>强制拉取远程分支内容到本地分支：</p>
<ol>
<li>
<p>git fetch --all //拉取远程仓库上所有分支的最新内容，但不合并</p>
</li>
<li>
<p>git reset --hard origin/master //将工作区的代码重置成远程分支的内容</p>
</li>
</ol>
<p>切换到远程分支，并且在本地切换到该分支：</p>
<ol>
<li>
<p>git fetch origin master</p>
</li>
<li>
<p>git checkout master</p>
</li>
</ol>
<h4 data-id="heading-13">git fetch 与 git pull 的区别</h4>
<p>这两个都是从远程分支拉取代码，它们的区别是 fetch 不会进行 merge,而 pull 会进行合并。fetch+merge === git pull。fetch 没有真正把内容合并到本地库，只是把更新下载下来，让你知道你本地版本和远端有什么差异，是否会有冲突等</p>
<p>git fetch origin 分支名 可以指定当前的 fetch-head 指针，之后可以直接 git fetch,</p>
<p>在 fetch 后，可以看到工作区不会有任何变化，但是我们可以在暂存区看到拉取代码跟本地的对比，然后去选择是否要进行合并,而 pull 就是直接合并了</p>
<p><strong>git pull 拉取不到最新代码</strong>： 很大可能是本地分支并未与远程分支建立过连接，你只是把远程代码 fetch 下来了，并且 checkout 过去，并未建立连接。</p>
<p>使用 git pull origin 分支名 这样可以拉取到最新的，但是下次使用 git pull 仍然拉取不到最新的。所以使用 git branch -u origin/分支名</p>
<h3 data-id="heading-14">rebase(变基)</h3>
<blockquote>
<p>1.在开发时，我们可能会有多个 commit，这个时候 push 的时候会产生多个 commit 信息，使用 rebase 可以将多个 commit 合并成一个</p>
</blockquote>
<blockquote>
<p>2.当我们从远程主分支拉取代码并新建分支进行操作时，此时主分支可能已经被别人修改了很多遍，这个时候我们一般会通过 merge 去合并代码并提交，但这时会产生一条 merge 的 commit 信息。使用 rebase 可以拉取主分支最新代码并且不会产生 merge 的 commit 信息</p>
</blockquote>
<blockquote>
<p>3.使用 rebase 可以把一个分支的改动复制到另一个分支上，使用--onto</p>
</blockquote>
<blockquote>
<p>每次使用 git rebase 前，问自己"有没有人也正在基于这个 branch 写代码？"若是的话，就老老实实用 merge，不要尝试 rebase。</p>
</blockquote>
<blockquote>
<p>该功能可能会导致一些问题，不熟悉的同学还是老老实实使用 merge 吧，在确保自己的分支只有自己改动的前提下，可以使用合并 commit 的功能，其它不熟就算了</p>
</blockquote>
<p><img src="https://user-gold-cdn.xitu.io/2020/6/1/1726e09219fa46fe?imageView2/2/w/1956/q/85/interlace/1" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">pick：保留该commit（缩写:p）
reword：保留该commit，但我需要修改该commit的注释（缩写:r）
edit：保留该commit, 但我要停下来修改该提交(不仅仅修改注释)（缩写:e）
squash：将该commit和前一个commit合并（缩写:s）
fixup：将该commit和前一个commit合并，但我不要保留该提交的注释信息（缩写:f）
exec：执行shell命令（缩写:x）
drop：我要丢弃该commit（缩写:d）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如说现在在自己的分支中你提交了三个 commit:commit1、commit2、commit3</p>
<pre><code class="copyable">git rebase -i  //-i是使用编辑界面，此时可以输入i进入编辑修改操作指令，修改提交信息，比如将commit1 跟 commit2 drop掉，然后将最后一条commit3给reword修改注释，然后esc退出编辑，wq保存
git rebase --continue  //如果有冲突先解决冲突,如果rebase中途出现问题，可以使用git rebase --abort恢复。
git push //提交，这个时候就只有一条commit信息
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 rebase 可以把一个分支的改动复制到另一个分支上</p>
<pre><code class="copyable">git rebase   [startpoint]   [endpoint]  --onto  [branchName]  //[startpoint] [endpoint]指定的是一个前开后闭的区间,所以起点要后退一步
git  rebase   90bc0045b^   5de0da9f2   --onto master
git checkout master
git reset --hard  0c72e64  //将master所指向的提交id设置为当前HEAD所指向的提交id
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">cherry-pick</h3>
<blockquote>
<p>使用场景:当一个 bug 在一个分支中被解决后，这时其它分支也需要解决这个 bug，那么可以使用 cherry-pick 将这个 commit 复制到其它分支中</p>
</blockquote>
<blockquote>
<p>我们代码库中的一个个 commit 可以看做一个个 cherry。同一个代码库中的 commit-id 往往是唯一的，当你在分支 B 上也需要在分支 A 上的提交内容时，就可以将它们 cherry-pick 过来！</p>
</blockquote>
<p>假设仓库中有三个分支：master、feature-a、feature-b。现在需要将 feature-a 中的两次 commit 合并到 feature-b 中</p>
<pre><code class="copyable">1.git checkout feature-b //切换到feature-b 分支
2.git reflog //查看所有的操作记录，拿到需要的HEAd值
3.git cherry-pick 6b95b5 b09a488 //挑选commit
这时候，如果没有冲突的话， git log 就可以看到 feature-b 分支上会多出 2 次新的提交
这个时候它是自动提交的，如果想不自动提交，执行：git cherry-pick 6b95b5 b09a488 -n
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发生冲突：</p>
<pre><code class="copyable">1.自己手动解决完所有冲突
2.git add -u 标记有冲突的文件已经解决好冲突
3.git cherry-pick --ontinue
除此以外，如果你过程中不想 cherry-pick了，只需执行：git cherry-pick --abort
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意点：虽然表面上看似是将那两次提交拿过来再用一遍，但其实 Git 只是拿到修改生成了新的提交，因此，这里会看到这 2 个新的提交，commit-id 和我们挑选 commit-id 并不一致。</p>
</blockquote>
<p>从 feature-a 分支选择连续的提交合入到 feature-b:</p>
<pre><code class="copyable">git cherry-pick d3113d5...b09a488c01  //左开右闭，开头应该后退一步
git cherry-pick 6b95b58^...b09a488c01 //左闭右闭
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他有用的选项：</p>
<pre><code class="copyable">-e/--edit：进行 cherry-pick 时，会在进行新的提交之前，重新编辑提交的信息
x：在记录提交时，会在原始提交消息后添加一行cherry picked from commit …，以表明此更改是从哪个提交中挑选出来的。 这仅适用于没有冲突的 cherry-pick
-s/--signoff：在提交信息的末尾追加一行操作者的签名，表示是谁进行了这个操作
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">本地仓库的操作</h2>
<p>查看本地仓库关联的远程仓库： git remote -v</p>
<p>查看远程仓库的详细信息：git remote show origin</p>
<p>将本地仓库某分支推送到远程仓库上:git push origin 远程分支名</p>
<p>将本地分支推送到远程仓库的不同名分支:git push origin 本地分支名:远程分支名</p>
<p>删除远程分支：git push origin --d 远程分支名 //删除本地分支：git branch -d 分支名</p>
<p>删除远程仓库：git remote rm 远程仓库名</p>
<h2 data-id="heading-17">.gitignore</h2>
<blockquote>
<p>一般我们总会有些文件无需纳入 Git 的管理，也不希望它们总出现在未跟踪文件列表。通常都是些自动生成的文件，比如日志文件，或者编译过程中创建的临时文件等。我们可以创建一个名为 .gitignore 的文件，列出要忽略的文件模式。</p>
</blockquote>
<pre><code class="copyable"># 此为注释 – 将被 Git 忽略
# 忽略所有 .a 结尾的文件
*.a
# 但 lib.a 除外
!lib.a
# 仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO
/TODO
# 忽略 build/ 目录下的所有文件
build/
# 会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
doc/*.txt
# 忽略 doc/ 目录下所有扩展名为 txt 的文件
doc/**/*.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">.gitkeep</h2>
<blockquote>
<p>.gitkeep是一个占位文件。</p>
</blockquote>
<p>Git是不会把一个完全空的文件夹添加到版本控制里，为了让空文件夹被跟踪，常规做法是在空文件夹里添加.gitkeep。</p></div>  
</div>
            