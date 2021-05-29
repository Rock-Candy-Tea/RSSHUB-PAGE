
---
title: '一份工作4年前端的Git备忘指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8681'
author: 掘金
comments: false
date: Sat, 29 May 2021 01:01:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=8681'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>刚毕业的时候用过极短时间的SVN，后面就一直在用Git来做代码的版本控制了，前前后后差不多4年的时间，期间做了一些在使用Git过程中的记录和心得，在这里分享给大家，大家或许可以从中吸收到一些有用的东西。</p>
<p>无论是github，还是gitlab，还是其他的代码托管平台，代码管理都是用git去做的，git可以说是一名程序员的必备技能，对于工作和面试都是非常有帮助的。</p>
<ul>
<li>Git常用命令</li>
<li>优雅使用Git的一些实践</li>
<li>oh-my-zsh 常用命令</li>
</ul>
<h3 data-id="heading-0">Git常用命令</h3>
<ul>
<li>git克隆远程分支仓库：</li>
</ul>
<p><code>git clone -b 分支名称 远程地址</code>
git克隆远程仓库项目时如果不指定分支，只会克隆默认分支的内容。</p>
<ul>
<li>查看git用户名和密码</li>
</ul>
<p><code>git config user.name</code>
<code>git config user.email</code></p>
<ul>
<li>分支相关</li>
</ul>
<p><code>git branch（查看当前分支）</code>
<code>git branch -a（查看所有分支）</code>
<code>git checkout 分支名（切换到对应分支）</code> 会自动将代码更新为分支代码
<code>git branch 分支名</code>（创建一个分支）
<code>git branch -d 分支名</code>（删除一个分支）
<code>git branch -D 分支名</code>（强制删除一个未合并的分支）
<code>git checkout -b 分支名 [基于的分支名或commit值]</code>（切换分支并直接切换过去）</p>
<ul>
<li>查看git历史</li>
</ul>
<p><code>history</code></p>
<ul>
<li>按照关键词搜索git历史</li>
</ul>
<p><code>history | grep push</code></p>
<ul>
<li>查看commit历史</li>
</ul>
<p><code>git log</code>
<code>git log --summary</code></p>
<ul>
<li>设置git账号</li>
</ul>
<p><code>git config --global user.name "Frankkai"</code>
<code>git config --global user.email "gaokai20100801@gmail.com"</code>
<code>git config user.name "Frankkai"</code>
<code>git config user.email "gaokai20100801@gmail.com"</code></p>
<ul>
<li>查看git账号</li>
</ul>
<p><code>git config --global --list</code>
<code>git config --local --list</code></p>
<ul>
<li>仅仅查看某一项的配置</li>
</ul>
<p><code>git config --local user.name</code></p>
<ul>
<li>回滚本次修改</li>
</ul>
<p><code>git reset HEAD static/lib/js/constantsUrl.js</code>
<code>git checkout -- static/lib/js/constantsUrl.js</code></p>
<ul>
<li>查看本次修改的代码</li>
</ul>
<p><code>git diff</code>
<code>git diff HEAD</code>
<code>git diff --staged</code></p>
<ul>
<li>提交后发现丢了几个文件没有提交</li>
</ul>
<p>发现丢了修改记录，重新添加
<code>git add "*.html"</code>
重新提交，最终只有一个提交
<code>git commit --amend</code></p>
<ul>
<li>缓存某种后缀的文件</li>
</ul>
<p><code>git add "*.js"</code></p>
<ul>
<li>清除缓存区中的文件</li>
</ul>
<p><code>git reset octofamily/octodog.txt</code></p>
<ul>
<li>彻底删除某种后缀的文件</li>
</ul>
<p><code>git rm "*.txt"</code></p>
<ul>
<li>合并分支到master</li>
</ul>
<p><code>git merge 分支名</code></p>
<ul>
<li>add .之前取消提交某些文件</li>
</ul>
<p><code>git checkout -- <filename></code></p>
<ul>
<li>藏代码到脏目录（适用于其他成员修改了相同分支代码，但又不想提交）</li>
</ul>
<p><code>git stash</code></p>
<ul>
<li>释放脏目录代码</li>
</ul>
<p><code>git stash pop</code></p>
<ul>
<li>释放指定脏目录代码</li>
</ul>
<p><code>git stash pop stash@&#123;0&#125;</code></p>
<ul>
<li>删除远程分支(此分支必须是非默认分支)</li>
</ul>
<p><code>git push origin --delete branchname</code></p>
<ul>
<li>已经commit，强制回退到旧版本</li>
</ul>
<p><code>git log</code>//找到commit hash值
<code>git reset --hard hash值</code></p>
<ul>
<li>查看stash目录</li>
</ul>
<p><code>git stash list</code></p>
<ul>
<li>删除某一个stash</li>
</ul>
<p><code>git stash drop stash@&#123;0&#125;</code></p>
<ul>
<li>设置远程仓库地址</li>
</ul>
<p><code>git remote set-url origin git@foo.bar.com:baz/helloworld.git</code></p>
<ul>
<li>本地创建了新分支，但是orgin没有，push代码前</li>
</ul>
<p><code>git push --set-upstream origin preproduction</code></p>
<ul>
<li>指定tag到远程</li>
</ul>
<p><code>git push origin <tag_name></code></p>
<ul>
<li>将全部tag打到远程</li>
</ul>
<p><code>git push --tags</code></p>
<ul>
<li>查看当前tags</li>
</ul>
<p><code>git tag --list</code></p>
<ul>
<li>仅仅删除index不删除working tree上的.idea文件</li>
</ul>
<p><code>git rm --cached -r .idea</code> // --cached仅仅删除index，-r（recursive）递归删除.idea目录下的所有文件</p>
<ul>
<li>git主动track文件，控制文件，做好提交准备</li>
</ul>
<p><code>git add <file(s)>/.</code></p>
<ul>
<li>git unstage文件，释放文件，选择性控制</li>
</ul>
<p><code>git reset HEAD <file(s)>/.</code></p>
<ul>
<li>暂存区文件如何覆盖工作目录文件</li>
</ul>
<p><code>git reset HEAD <file(s)>/. && git checkout -- <file(s)>/.</code></p>
<ul>
<li>提交已经被git管理的，modified为红色的所有文件</li>
</ul>
<p><code>git add -u</code></p>
<ul>
<li>重置工作区和暂存区的所有文件为原始状态</li>
</ul>
<p><code>git reset --hard</code></p>
<ul>
<li>比较当前分支与某次提交的区别</li>
</ul>
<p><code>git diff HEAD [commit hash fragment]</code></p>
<ul>
<li>删除一个分支</li>
</ul>
<p><code>git branch -D [branch name]</code></p>
<ul>
<li>同步到remote后，合并多个commit 为1个</li>
</ul>
<pre><code class="copyable">git rebase -i HEAD~2/hash
pick && squash
:wq!
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>查看项目的origin代表的地址</li>
</ul>
<p><code>git remote -v</code></p>
<ul>
<li>pick中途误退出</li>
</ul>
<p><code>git rebase --abort</code></p>
<ul>
<li>未同步到remote，重新提交</li>
</ul>
<p><code>reset soft</code></p>
<ul>
<li>gitflow release 发布新版本</li>
</ul>
<pre><code class="copyable">git flow release start v0.5.0
npm version minor
git flow release finish -n
git push
git checkout master
git push
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>gitflow hotfix 修复一个master上的bug</li>
</ul>
<pre><code class="copyable">git flow hotfix start foo
npm version patch // 注意：一定要在修复bug代码之前新增版本号
git add .
git commit -m "version change message"
git flow hotfix finish -n
git push
git checkout master
git push
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>对比2个分支的日志</li>
</ul>
<pre><code class="copyable">git log develop..master
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>合并master代码到feature</li>
</ul>
<pre><code class="copyable">git checkout feature
git merge master
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">git merge master feature
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>git rebase冲突时怎么办</li>
</ul>
<pre><code class="copyable">resolve conficts
git add .
git rebase --continue
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>squash多个commits成一个怎么敲？</li>
</ul>
<p>假设merge feature到master。</p>
<pre><code class="copyable">git checkout master
git merge --squash feature
git commit -m "这是一次squash commit"
git push
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>查看当前分支的父分支</li>
</ul>
<pre><code class="copyable">git reflog show <childBranch>
32c3956 (HEAD -> currentBranch, origin/fatherBranch, fatherBranch, list) childBranch@&#123;0&#125;: branch: Created from fatherBranch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>childBranch 是你新建的分支。
fatherBranch 是它的父分支，也就是来源分支。</p>
<ul>
<li>撤销远程分支错误提交</li>
</ul>
<pre><code class="copyable">...reset
git push --force
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实使用本地分支的提交替代远程分支。</p>
<ul>
<li>误删除领先远程的本地分支如何恢复？</li>
</ul>
<pre><code class="copyable">git reflog // 找出最新的commit sha1值，HEAD@&#123;1&#125;比HEAD@&#123;2&#125;新
git branch branchName <sha1>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过git reflog找到一个commit，然后再cherry-pick也可以。</p>
<ul>
<li>删除由npm version patch/minor/major误添加的tag</li>
</ul>
<pre><code class="copyable">git tag | grep v1.1.38
git tag -d v1.1.38
git push origin :refs/tags/v1.1.38
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>git fetch与git pull的区别</li>
</ul>
<pre><code class="copyable">git fetch 更新origin/*下的所有分支，在发布git flow feature前很有用，用于更新remote分支。
git pull 主要用来更新多人合作的当前分支，多用于更新local分支。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://www.git-tower.com/learn/git/faq/difference-between-git-fetch-git-pull" target="_blank" rel="nofollow noopener noreferrer">www.git-tower.com/learn/git/f…</a></p>
<ul>
<li>远程分支删除，本地git fetch不能更新到最新分支</li>
</ul>
<pre><code class="copyable">git fetch --prune
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>--prune
Before fetching, remove any remote-tracking references that no longer exist on the remote.</p>
</blockquote>
<ul>
<li>及时查看本地所有分支的状态</li>
</ul>
<pre><code class="copyable">git remote show origin
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>假如远程已不存在这个分支，git fetch --prune也更新不到状态，该怎么办？</li>
</ul>
<pre><code class="copyable">git push origin --delete feature/fix-chat-unread-msg-async
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>删除单个脱离的远程分支</li>
</ul>
<pre><code class="copyable">git remote prune <name>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>取消一次合并（merge）</li>
</ul>
<p><code>git merge --abort</code></p>
<ul>
<li>回退一次commit</li>
</ul>
<p><code>git revert Head/[commit hash]</code></p>
<h3 data-id="heading-1">优雅使用Git的一些实践</h3>
<ul>
<li>windows下gitbash支持中文输入：</li>
</ul>
<p>1）鼠标左键点击左上角git的logo
2）找到options并且切换到text目录，将Character set设置为UTF-8</p>
<ul>
<li>生成ssh-key</li>
</ul>
<p><code>ssh-keygen -t rsa -C "gaokai20100801@qq.com"</code></p>
<ul>
<li>windows查看ssh-key</li>
</ul>
<p><code>/c/Users/frank/.ssh/id_rsa.pub</code></p>
<ul>
<li>mac/linux查看ssh-key</li>
</ul>
<p><code>cd ~/.ssh</code>
<code>ls</code>
<code>cat id_rsa.pub</code></p>
<ul>
<li>git flow</li>
</ul>
<p><a href="https://danielkummer.github.io/git-flow-cheatsheet/index.html" target="_blank" rel="nofollow noopener noreferrer">danielkummer.github.io/git-flow-ch…</a></p>
<ul>
<li>误删除stash，该怎么办？</li>
</ul>
<pre><code class="copyable">git fsck --unreachable |
grep commit | cut -d\  -f3 |
xargs git log --merges --no-walk --grep=WIP
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到对应的commit hash值</p>
<pre><code class="copyable">git stash apply 1f55da93d26cd51f15f9e93351dae6b75e25e36f
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>.idea修改总是会提醒，.gitignore不生效</li>
</ul>
<p><code>.idea/</code></p>
<pre><code class="copyable">git rm -r --cached .idea
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Git中的origin是什么？</li>
</ul>
<p>origin是一个变量，代表着一个git仓库地址。可以使用<code>git remote -v</code>查看origin代表的地址。</p>
<ul>
<li>Git的system，global和local参数分别代表什么？</li>
</ul>
<pre><code class="copyable">--system可以输出很多git的系统设置，其中最有用的是alias，例如git s代表了git status，系统所有登录用户有用。
--global输出了git的全局设置，主要包括全局的user.name和user.email，优先级低于单个仓库中设置的user.name和user.email，当前用户所有仓库有用。
--local输出了git的项目设置，主要包括remote.origin.url以及gitflow的很多配置，只对某个仓库有用。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Git工作区和暂存区的区别？</li>
</ul>
<pre><code class="copyable">       add           commit
工作目录---->暂存区---->版本历史
<span class="copy-code-btn">复制代码</span></code></pre>
<p>暂存区：git已经获得了对文件的管理权限，暂存区文件有状态：new file，deleted，modified等等。</p>
<p>版本历史：git log查看每一次commit记录。</p>
<p>意外收获：
若是想非常细粒度的控制commit记录，可以使用git add 指定文件，分开多次commit，每一次commit提交一个细粒度功能的变更文件集合，多次走文件目录 暂存区 版本历史这个流程。</p>
<ul>
<li>Git如何重命名文件？</li>
</ul>
<pre><code class="copyable">git mv README.md readme.md
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Git的working tree和index是什么意思？</li>
</ul>
<p>index指的是git索引，可以理解成git有文件的一个复制，仅删除index则仅删除存在于git中的文件。
working tree则是指操作系统的工作树，也就是操作系统的磁盘上存储的文件。
举两个常用的例子：</p>
<ol>
<li>仅删除git index中的文件，.idea等IDE隐藏的工作树文件是不能删除的：<strong>--cached</strong></li>
</ol>
<p><code>git rm --cached -r .idea // **--cached仅仅删除index**，-r（recursive）递归删除.idea目录下的所有文件</code></p>
<ol start="2">
<li>删除index和working tree上的文件，恩断义绝</li>
</ol>
<p><code>git rm </code>删除index上和working tree上的文件，</p>
<p>仅仅删除working tree不删除index的情况，不存在。</p>
<ul>
<li>nothing to commit 和 working tree clean?</li>
</ul>
<p>暂存区没有可以提交到版本历史的内容。
工作区也是干净的。</p>
<ul>
<li>如何一目了然地区分出工作区和暂存区？
<ul>
<li><strong>Your branch is ahead of 'origin/master' by 1 commit</strong> 版本历史</li>
<li><strong>Changes to be committed</strong> 暂存区</li>
<li><strong>Untracked files</strong> 工作区</li>
</ul>
</li>
</ul>
<pre><code class="copyable">// 版本历史
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
// 暂存区
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        renamed:    readme.md -> README.md
        new file:   helloman

// 工作区
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        hi
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如何更加优雅地查看日志？</li>
</ul>
<p><code>git log --oneline</code>简洁的commit记录
<code>git log -n2 --oneline</code>最近的2次简洁的commit记录
<code>git log --all</code>所有分支的历史版本信息
<code>git log --graph</code>图形化查看版本演进历史
<code>git log --oneline --all -n4 --graph</code>组合查看日志</p>
<ul>
<li>如何快速定位到git的命令文档？</li>
</ul>
<p><code>git help --web log</code> 浏览器查看<code>git log</code>的用法</p>
<ul>
<li>git自带的图形化界面怎么看？</li>
</ul>
<p><code>gitk</code> 无需安装第三方插件，在纯命令行下，无第三方软件情况下可用。</p>
<ul>
<li>git 里的作者和提交人不一样吗？</li>
</ul>
<p>作者是代码的生成者，是为了版权保护。</p>
<ul>
<li>神秘的.git目录</li>
</ul>
<p><code>HEAD</code>工作分支refs/heads/foo
<code>config</code>repo的配置信息
<code>refs</code> heads，分支；tags，标签或者里程碑
<code>refs/heads/master</code>存放了什么，最新的一个commit
<code>refs/tags/js01</code>存放了什么，最新的一个tag，包含一个object
<code>objects</code>文件夹，2个字符的和松散的pack文件夹，存放的是tree，tree下有blob文件
可以直接通过vim修改HEAD，config等信息，和命令的作用是相同的。</p>
<ul>
<li>如何判断git文件的类型？</li>
</ul>
<p><code>git cat-file -t/-p [hash fragment]</code> // -t 类型，-p 内容
只要任何文件的文件内容相同，在git眼里，它就是唯一的一个blob。</p>
<pre><code class="copyable">commit  
tree // 位于objects目录下
blob // 位于objects目录的二级目录下，具体的文件
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>tree, commit, blob的区别？</li>
</ul>
<p>commit：一个commit肯定会对应一棵树，包含了根tree，author，committer，parent等等一个commit对象的信息。</p>
<p>tree：取出一个commit，存放了一个快照，这个快照，对应了当前项目的所有的文件夹及其文件的快照，是特定时间的整个仓库的一个状态；树里可以有blob，也可以有树，因为树是文件夹；根树是最大的树。</p>
<p>blob:  与文件名是否相同无关，只要内容相同，就是唯一的blob。</p>
<ul>
<li>一个commit包含了哪些？</li>
</ul>
<pre><code class="copyable">git cat-file -p [commit hash fragment]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>包含tree，parent，author和commiter。</p>
<pre><code class="copyable">tree f06f7f36af17cb9098031c66d22a7910c0fa1bac
parent 92a55c8a5b1d38d224232ad84b9b728ae77189cb
parent eda632a1f2a3ea049c5f5268f6b2f064b71898ce
author FrankKai <gaokai20100801@gmail.com> 1548139120 +0800
committer FrankKai <gaokai20100801@gmail.com> 1548139120 +0800

Merge branch 'feature/chatBreakChange' into prerelease

# Conflicts:
#       src/api/chat.js
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>一个tree包含了哪些？</li>
</ul>
<pre><code class="copyable">git cat-file -p [tree hash fragment]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>包含tree，blob。</p>
<pre><code class="copyable">100644 blob 015aaf344153ed7822069b2a98898b7d7a215b0d    .babelrc
100644 blob 9d08a1a828a3bd2d60de3952744df29f9add27fa    .editorconfig
100644 blob 080140b833db5b758b1eb869a269f4bbb068a19e    .eslintignore
100644 blob 8f777c376c0314e480f9bbba273d4902810bcb11    .eslintrc.js
100644 blob 895e844218637929546ed2295ae90f991ceb5d38    .gitignore
100644 blob db7b635d23657349dbe4c33cc353ef4efd8ca960    .npmrc
100644 blob 797e871f4b8c0a3071e8b6ab2cc40b804cd2971c    .postcssrc.js
100644 blob d3983c1d6a5525aae58b823448723434ca83ceed    .prettierrc
100644 blob 93cc7473ab066204f3329221111a945e2dc83576    BUS.md
100644 blob defc3d9914d1af08e6670b96995261bfe1fb61a6    CHANGELOG.md
100644 blob bfd46fd4008cbe7103181fc5cd64392a74426e96    MQTT.md
100644 blob abdb55935d833dd4f4b79475aa7d63ffcb0cc9cd    README.md
040000 tree f1f80f844bb80389826198a15ec0f224a53525f8    build
100644 blob 2aefa3130f4ff753b5c3e538db53b9b186f12540    index.html
100644 blob 967b8f243420a9a8a07b8f429f0a7ba874a834ad    package-lock.json
100644 blob 35d9fa46f569395b25a87daef4820de42d071831    package.json
040000 tree f6bdc675a8f9af805867b5a19c263e5bbfe4c26c    src
040000 tree 09e231414b91779326447a0c8d5b3421aa2308c2    static
040000 tree ad94369cfdd2038a552e44fc0abbd1738113b5e6    test
100644 blob 0b96f21c27a3759cecde02fba1e050d86a8e9a54    yarn.lock
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>一个blob包含了哪些？</li>
</ul>
<pre><code class="copyable">git cat-file -p [tree hash fragment]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是一个具体的文件。</p>
<ul>
<li>detached HEAD是什么？</li>
</ul>
<p>分离头指针。
<code>git checkout [commit hash fragment]</code>，切换到分离头指针状态，不与任何branch或tag关联，git会认为这是不重要的，当成垃圾清理掉。</p>
<p>缺点：切换分支后，需要用<code>git branch [branch name] [commit hash fragment]</code>新建一个分支，否则会丢失原消息。</p>
<p>优点：可以基于某一次commit切出分支，然后新建一个commit，快速会退到想要的版本。</p>
<ul>
<li>HEAD可以指向什么？</li>
</ul>
<p>它位于.git/HEAD。</p>
<p>可以指向分支或者commit，<strong>但其实分支归根结底还是指向了commit</strong>。</p>
<p>git log 查看HEAD指针指向的分支名：<code>(HEAD->foo, bar, master)</code></p>
<p>可以快速diff，<code>git diff HEAD [commit hash fragment]</code>。</p>
<p>父亲的父亲diff：<code>git diff HEAD HEAD~2</code>，<code>git diff HEAD HEAD^^</code>。</p>
<ul>
<li>如何修改最新一次commit的message？</li>
</ul>
<p><code>git commit --amend</code>
注意：不能在团队的集成分支上，做这样的变更，仅适用于本地。</p>
<ul>
<li>如何修改老旧commit的message？</li>
</ul>
<pre><code class="copyable">git rebase -i [父 commit hash fragment]
reward
添加修改后的commit message
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：不能在团队的集成分支上，做这样的变更，仅适用于本地。</p>
<ul>
<li>git stash pop stash@&#123;n&#125;还能做什么操作？</li>
</ul>
<p>当前分支的本地代码未提交的情况下，pull了领先的远程分支代码，此时远程代码会覆盖本地代码。</p>
<p>git比较聪明，它不会完全将本地的代码扔掉，即使没有人为的生成一次commit记录，也会自动为我们在stash下生成一次记录，以免造成重大的代码丢失。</p>
<ul>
<li>gitflow模式下，如何规范版本发布？</li>
</ul>





















<table><thead><tr><th>版本号升级</th><th>gitflow对应</th></tr></thead><tbody><tr><td>bug -> patch</td><td>hotfix</td></tr><tr><td>feature->minor</td><td>release</td></tr><tr><td>系统重构->major</td><td>release</td></tr></tbody></table>
<p>但是在scrum的情况下，迭代非常快速，若所有feature都升级minor，会导致minor数字很大，该怎么处理这种情况？</p>
<p>只升级minor时，在commit提交信息中，添加以下信息：</p>

















<table><thead><tr><th>类型</th><th>提交信息</th></tr></thead><tbody><tr><td>bug patch</td><td>[bug patch]</td></tr><tr><td>feature patch</td><td>[feature patch</td></tr></tbody></table>
<ul>
<li>创建一个新的项目并上传到git</li>
</ul>
<pre><code class="copyable">git init
git ac
git remote add origin remote repository URL
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>git参数--decorate是什么？</p>
<ul>
<li>有short，full，auto，no几种值，--decorate=short</li>
<li>打印出commit的ref name。</li>
<li>short时，ref name 前缀refs/head,refs/tags/和refs/remotes不会打印</li>
<li>full时，完整前缀会被打印</li>
<li>auto时，如果输出是一个终端，会按照short的方式打印；非终端会显示全部</li>
<li>no时，会隐藏HEAD和tag等等refs信息</li>
<li>默认值是short</li>
</ul>
</li>
<li>
<p>cherry pick是什么？</p>
</li>
</ul>
<p><a href="https://github.com/FrankKai/FrankKai.github.io/issues/172" target="_blank" rel="nofollow noopener noreferrer">如何理解git cherry pick？</a></p>
<ul>
<li>清空所有本地git 缓存</li>
</ul>
<pre><code class="copyable">git rm -r --cache .
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>error Command "husky-run" not found</li>
</ul>
<p>rm -rf .git/hooks/</p>
<ul>
<li>一次完整的rebase流程</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> git checkout feature
<span class="hljs-number">2.</span> git rebase master
<span class="hljs-number">3.</span> resolve conflicts
<span class="hljs-number">4.</span> git add .
<span class="hljs-number">5.</span> git rebase --<span class="hljs-keyword">continue</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>git revert和git reset的区别</li>
</ul>
<p>git revert 生成一个新的commit的方式回滚到上一个或者指定commit版本的代码，原理是Head继续前进。有存在被回滚掉的commit分支代码合并过来时，代码正常被合并</p>
<p>git reset 删除某个commit之后的代码，原理是Head向后退。有存在被回滚掉的commit分支代码合并过来时，被reset掉的代码仍然会合并上来</p>
<h3 data-id="heading-2">oh-my-zsh 常用命令</h3>
<h4 data-id="heading-3">缩写全写对照表</h4>









































<table><thead><tr><th>缩写</th><th>全写</th></tr></thead><tbody><tr><td>gst</td><td>git status</td></tr><tr><td>gaa</td><td>git add .</td></tr><tr><td>gcmsg ""</td><td>git commit -m ""</td></tr><tr><td>gp</td><td>git push</td></tr><tr><td>glog</td><td>git log --oneline --decorate --graph</td></tr><tr><td>gl</td><td>git pull</td></tr><tr><td>gf</td><td>git fetch</td></tr><tr><td>gfa</td><td>git fetch --all --prune</td></tr></tbody></table>
<h4 data-id="heading-4">使用小技巧</h4>
<ul>
<li>如何修改默认指令的参数，比如，glog的decorate默认是short，我想指定glog的decorate为no，要怎么做？</li>
</ul>
<p><code>glog --decorate=no</code></p>
<blockquote>
<p>期待和大家交流，共同进步：</p>
<ul>
<li>微信公众号： 大大大前端 / excellent_developers</li>
<li>Github博客: <a href="https://github.com/FrankKai/FrankKai.github.io" target="_blank" rel="nofollow noopener noreferrer">趁你还年轻233的个人博客</a></li>
<li>SegmentFault专栏：<a href="https://segmentfault.com/blog/chennihainianqing" target="_blank" rel="nofollow noopener noreferrer">趁你还年轻，做个优秀的前端工程师</a></li>
</ul>
</blockquote>
<blockquote>
<p>努力成为优秀前端工程师！</p>
</blockquote></div>  
</div>
            