
---
title: 'git规范操作从入门到精通'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf9db6a434c94a12b5d600a0d192cb87~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 23:49:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf9db6a434c94a12b5d600a0d192cb87~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">关于git,你知道多少</h1>
<h2 data-id="heading-1">规范</h2>
<p>开篇刚开始我们就要提一下规范的git习惯，并做持续更新。规范的习惯，让我们更加专业</p>
<ul>
<li>保持commit提交记录的有效率</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 当我们提交代码到本地仓库的时候，经常会遇到重复提交的情况。
场景： 
刚刚commit完毕，发现描述信息有误，需要修改一下描述信息再次提交；
commit信息没有错，但是修改了一下代码的格式，最后也需要重新提交。

这样无非在分析（仓库管理工具gitlab）提交记录增加了混淆度，
因此我们可以在提交到暂存区后使用git commit --amend ，这个命令的
作用是对上一次commit描述进行修改，因此就解决了重复commit的问题。

<span class="hljs-number">2.</span>如果git commit --amend后，你git pull origin daily/<span class="hljs-number">0.0</span><span class="hljs-number">.1</span>发现提示
<span class="hljs-string">`fatal: refusing to merge unrelated histories`</span>
解决： git pull origin daily/<span class="hljs-number">0.0</span><span class="hljs-number">.1</span> --allow-unrelated-histories
但是正常情况下，都是在自己的分支上开发的，也就不会出现远程仓库领先于自己仓库
的情况，所以也就没有必要再次执行命令：git pull origin daily/<span class="hljs-number">0.0</span><span class="hljs-number">.1</span>

<span class="hljs-number">3.</span>撤回commit的命令：
git reset --soft commitID   绿
git reset --mixed commitID  红
git reset --hard commitID  白
每一次的commitId肯定是不同的，所以再次commit然后git push时会报错：

<span class="hljs-attr">hint</span>: Updates were rejected because the tip <span class="hljs-keyword">of</span> your current branch is behind
<span class="hljs-attr">hint</span>: its remote counterpart. Integrate the remote changes (e.g.
<span class="hljs-attr">hint</span>: <span class="hljs-string">'git pull ...'</span>) before pushing again.
<span class="hljs-attr">hint</span>: See the <span class="hljs-string">'Note about fast-forwards'</span> <span class="hljs-keyword">in</span> <span class="hljs-string">'git push --help'</span> <span class="hljs-keyword">for</span> details.

解决： 可以 git push --force

stage/index > working/directory如下
git reset HEAD readme.txt暂存区》工作区
git checkout readme.txt 撤销工作区的更改
。。。。。。。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">准备工作</h2>
<p>当你领到一台新电脑或者已有电脑重装系统了，你需要做哪些，来使用git。</p>
<ol>
<li>生成ssh秘钥</li>
</ol>
<p>windows+R输入命令ssh-keygen -t rsa -C "<a href="mailto:asdf@163.com">asdf@163.com</a>"
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf9db6a434c94a12b5d600a0d192cb87~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
问题：我们需要的是公共秘钥,如果没有 .pub后缀的文件
原因：隐藏了已知文件类型的扩展名
解决：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/330c428045024b8fbfa0f40daabe4be4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9770a98ebfc4d78977dc593e956a4cd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>登录github新建ssh key</li>
</ol>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd64bac6d4cd466c802b030414263aad~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a7b3211891e4f4faab37009957d371b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>验证ssh</li>
</ol>
<pre><code class="copyable">>本地新建文件夹右键Git Bash Here
>git init
>git config user.name 'github名字'
>git config user.email 'github绑定的邮箱'
>本地仓库与远程仓库建立连接:
git remote add origin git@github.com:China_forrest/learngit.git     
git remote -v  查看连接情况
git remote  rm origin 断开与远程仓库的连接  
>把远程仓库源代码拉取到本地
git pull origin master   这里的master指的是远程仓库的分支名
>然后yes
>验证成功后，就会把远程分支master分支的代码拉取到我本地的文件夹，
同时在本地创建一个master分支
>建立本地分支与远程分支的连接
git branch --set-upstream-to=origin/master或
git branch  --set-upstream  dev origin/dev或
第一次推送的时候git push -u origin 分支名
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此新的电脑或新的系统：本地仓库重新建立了与远程仓库的连接</p>
<h4 data-id="heading-3">从远程库拉代码之git clone和git pull的区别</h4>
<p>1.是否是需要本地是一个仓库</p>
<pre><code class="copyable">git clone 不需要本地仓库（.git文件夹）    在本地仓库文件夹内生成一个新的文件夹alibaba
git pull  需要先初始化本地文件夹为一个本地仓库（有.git文件夹）         直接将远程仓库文件夹内的文件拷贝到本地仓库（文件夹）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>git clone
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77c2af1872404f39bd967a35b67f463f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
git pull</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16036195bec4bbe8d6a5cc227a3c084~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>2.切换分支（仅限于刚拉下代码的时候）
git clone   git远程仓库已有的分支可以直接进行切换
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4e70b6b824b469faeae8b72f26613e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
git pull   不能直接切换远程仓库 已有的分支
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae892f9fb940430d80a4c34a2ec95329~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
3.推送远程库</p>
<ul>
<li>git clone 直接指定分支可以推动到远端</li>
</ul>
<pre><code class="copyable">git chekcout -b dev
git push --set-upstream origin dev
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>git pull  先指定源</li>
</ul>
<pre><code class="copyable">git remote add origin git@github.com:rdmclin2/learngit.git,远程库的名字叫origin
git pull origin master   // 或者可以这样  git merge master  将master分支合并到当前分支

git push -u origin '分支名’
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">知道</h2>
<p>关于git命令我们仅仅知道，git add,git commit, git push，是不能满足团队协作开发的。本文将对git命令作出系统的总结。</p>
<h2 data-id="heading-5">团队协作</h2>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/103d0f0453024a56a4915dd16656be82~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>首先，可以试图使用git push origin branch-name  推送自己的修改</li>
<li>如果推送失败，则因为远程分支比你的本地分支更新，需要用git pull试图合并</li>
<li>如果合并有冲突，则解决冲突，并在本地提交；</li>
<li>没有冲突或者解决冲突后，再用git push origin branch-name 推送就能够成功</li>
<li>如果git pull 提示 "no tracking information",则说明本地分支和远程分支的链接关系没有创建，用git branch --set-upstream branch-name origin/branch-name</li>
</ul>
<p>注意：不要直接在迭代分支上写代码：比如我们这次的迭代分支是dev,那么在dev上checkout出自己的开发分支，一个功能完成后提交MR到dev上，有其他同学来review,有问题的地方进行整改，全部ok后合并入dev。等dev也稳定之后合并入master.</p>
<h2 data-id="heading-6">关联本地和远程分支</h2>
<ul>
<li>
<p>第一种，远程分支如dev,本地分支如dev，
用git branch  --set-upstream  dev origin/dev</p>
</li>
<li>
<p>第二种，本地分支创建分支如dev，用git push -u origin dev，将本地分支上传到远程仓库，并关联起来，如果远程分支没有dev分支，会自动创建。</p>
</li>
<li>
<p>第三种，抓取远程分支并在本地建立关联的分支，</p>
</li>
</ul>
<p>用git chekcout -b local-branchname  origin/remote_branchname</p>
<h2 data-id="heading-7">Commit提交规范</h2>
<p>根据<a href="https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#commit-message-format" target="_blank" rel="nofollow noopener noreferrer">angular规范</a>提交commit，这样history看起来更加清晰，还可以自动生成changelog。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><type>(<scope>:<subject>)
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(1)type
提交commit 的类型，包括以下几种</p>
<ul>
<li>feat:新功能</li>
<li>fix:修复问题</li>
<li>docs:修改文档</li>
<li>style:修改代码格式，不影响代码逻辑</li>
<li>refactor:重构代码，理论上不影响现有功能</li>
<li>pref:提升性能</li>
<li>test:增加修改测试用例</li>
<li>chore:修改工具相关（包括但不限于文档、代码生成等）</li>
<li>deps:升级依赖</li>
</ul>
<p>(2)scope
修改文件的范围（包括但不限于doc,middleware,proxy,core,config）
(3)subject
用一句话清楚的描述这次提交做了什么
（4）body
补充subject,适当增加原因、目的等相关因素，也可以不写
（5）footer</p>
<ul>
<li>当有非兼容修改时可以在这里描述清楚</li>
<li>关联issue,如Close  #1,  Close  #2  ,#3</li>
<li>如果功能点有新增或这修改的，还需要关联 chair-handbook和chair-init的MR，如chair/doc!123</li>
</ul>
<p>示例：</p>
<pre><code class="copyable">1  fix($compile) : couple of unit test for IE9
2 
3 Older IEs serialize html html uppercased, but IE9 does not ...
4 Would be better to expect case insensitive,unfortunately jasmine does
5 not allow to user regexps for throw expectations.
6
7 Document change on chair/doc!123
8
9 Cloes #392
10  Breaks foo.bar api, foo.baz should be used instead
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体查看文档点<a href="https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit" target="_blank" rel="nofollow noopener noreferrer">这里</a></p>
<p>提交Merge Request
如果你有仓库的开发者权限，而且希望贡献代码，那么你可以创建分支修改代码提交MR，让负责人review代码合并到主干。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//先创建开发分支开发，分支名应该有含义，避免使用update、tmp之类的</span>
$ git checkout -b branch-name

<span class="hljs-comment">//开发完成后跑下测试是否通过，必要时需要新增或修改测试用例</span>
$ npm run test

<span class="hljs-comment">//测试通过后提交代码，message建下面的规范</span>

$ git add . <span class="hljs-comment">//git add -u 删除文件</span>
$ git commit -m <span class="hljs-string">"fix(role):role.use must xxx"</span>
$ git push origin branch-name
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提交后就可以在gitlab创建MR了。
由于谁也无法保证过了多久之后还记得多少，为了后期回溯历史的方便，请在MR时确保提供一下信息。</p>
<pre><code class="copyable">需求点（一般关联issue或者注释都算）
升级原因（不同于issue，可以简述一下为什么要处理）
框架测试点（可以关联到测试文件，不用详细描述，关键点即可）
关注点(针对用户而言，可以没有，一般是不兼容更新等，需要额外提示)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">指令集合</h2>
<pre><code class="copyable">设置
git config --global user.name  'Your Name'
全局设置用户名   "--global"代表所有仓库使用这一配置

全局设置邮箱
git config  --global  user.email "email@example.com"

.gitignore 编写
git config --global alias.  <new order> order为命令设置别名
$ git config --global alias.st status 告诉Git，以后st就表示status,下面列一些常用设置
 $ git config --global alias.co checkout
 $ git config --global alias.ci commit
 $ git config --global alias.br branch
 $ git config --global alias.unstage 'reset HEAD' 撤销暂存区修改
 $ git config --global alias.last 'log -1' 显示最近一次提交
 $ git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"  简直丧心病狂!
如果要修改别名，当前用户的Git配置文件放在用户主目录下的一个隐藏文件.gitconfig中，可以直接修改
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">基本操作</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript">
 - git init   初始化一个git 仓库 
 - git add <file>  添加文件到仓库，可以多次add 如：git add readme.txt 
   git reset HEAD <file>  从暂存区撤销一个add 
   git reset  HEAD test.tsx
   git commit -m <span class="hljs-string">""</span>   快速提交代码，多次add 一次commit
   git rm <file> 从版本库删除某文件
   git checkout --<file>


丢弃工作区的修改
git checkout --readme.txt
git checkout .   丢弃所有本地修改
如果已经add,可以用git reset HEAD <file> 先撤销add,再丢弃更改
如果你已经commit了，可以用 git reset --hard  HEAD^  进行回退上一个版本
如果你已经推送远程分支了，也就凉凉了......
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">git status  仓库状态
git diff  <file>
git diff readme.txt  可以看到当前文件的改动
git diff 列出所有文件的改动
注意git diff会比较仓库中的文件和不在仓库中的同一文件的差异，也就是
git add的文件A，以及git add后改动的文件A，

如果没有改动的话，git diff 甚至智能地不自动匹配文件

git log  查看提交历史
 $ 从最近到最远 可以加 --pretty=oneline 让git 显示得更清楚些
 $ git log --graph --pretty=oneline --abbrev-commit  用--graph查看分支合并图
$ 版本回退
 $ 如 git reset --hard HEAD^, HEAD代表当前版本，HEAD^代表上个版本,Head^^代表上上版本，HEAD-100代表往上100个版本
 $ 不过过去了回不来怎么办, 只要命令行窗口没关闭，就可以找到你要回去的commit id，然后再用如 git reset --hard 3628164 回到该版本.
 $ 如果第二天后悔了怎么办？用 git reflog 查看所有命令，再找到相应的commit id即可
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">分支管理</h2>
<pre><code class="copyable">git branch   查看分支
git branch  <branch name>
git branch dev  创建分支
git branch -d dev  删除分支
git push origin : <branch name>  删除远程分支
git branch -D <branch name>强行删除分支
如git branch -D feature-vulcan 没有进行合并的分支用 -d参数会销毁失败
如果实在要丢弃一个没有合并过的分支，用-D进行强行销毁

修改本地分支名称 git branch -m <old_branch_name><new_branch_name>
     git branch -m feature-a  feature-b

git checkout <branch name> 切换分支
git checkout -b issue-101  创建分支并切换
git merge <branch name>  合并分支（branch name)到当前所在分支
git merge --no-ff -m <message><branch name>

$ 禁用fast forward
 $ 如 git merge --no-ff -m "merge with no-ff" dev
 $ --no-ff表示禁用fast forward,在ff模式下删除分支后会丢掉分支信息，所以用--no-ff后
 $ git就会在merge的时候生成一个新的commit，因为要有一个新的commit所以要加上－m参数

git stash 储藏工作现场，可以把当前的工作现场储藏起来，等以后恢复现场后继续工作
git stash list 列出储藏的工作现场
git stash apply 恢复现场，但stash内容不删除
git stash drop 删除现场
git stash pop 恢复现场的同时删除现场
git stash apply <stash id>多个现场时指定恢复某一现场（先用git stash list查看)
git rebase <branch name> 整合分支 变基 、 高危操作请清楚了解原理和后果后再操作
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">远程仓库</h2>
<pre><code class="copyable">ssh-keygen -t rsa -C "youremail@email"
创建ssh-key,将公钥添加到github等网站上
git  remote add origin <remote git repo>将本地仓库和远程仓库相关联，在本地仓库执行
如 git remote add origin git@github.com:rdmclin2/learngit.git,远程库的名字叫origin
可以添加多个远程仓库如git remote add rdmclin2 git@...  origin rdmclin2都是我们为远程仓库取的别名。
git remote set-url  origin <remote git repo>
修改origin 的地址，如：git remote set-url origin git@gitlab.artemisprojects.org:menchenglin/fcws.git

git push origin <branch name>
将本地内容推送到远程
如git push origin master,如果是第一次推送的话:git push -u origin master,
也就是第一次加上-u参数，可以吧本地分支和远程分支关联起来，以后就不要添加-u参数了

git clone <remote git repo>
从远程仓库克隆
如： git clone git@github.com:michaelliao/gitskills.git,非常常用的操作
clone时可以指定深度，git clone git://xx00  --depth  1

git remote
常看远程库信息，加上-v参数可以显示更加详细的信息

git pull
抓取远程分支最新提交并合并分支
如git tag v0.9 6224937,可以先用git log --pretty=oneline  --abbrev-commit 查看历史提交

git fetch
抓取远程分支最新提交（与pull的区别是fetch不直接合并）

git branch  ---set-upstream <local branch> <remote branch>
指定本地分支和远程分支的链接
如git branch --set-upstream dev origin/dev  指定本地div分支与远程origin/dev分支的链接

git tab <name>
打标签  如 git tag v1.0

git tag
查看所有标签，按字母排序

gitshow <tagname>
查看标签信息

git tag <name> <commit id>
给某次提交打上标签
如 git tag v0.9 6224937,可以先用git log  --pretty=oneline  --abbrev-commit 查看历史提交

git tag -a  <tagname> -m  <message> <commit id>
创建带有说明的标签
如 git tag -a v0.1 -m  "version 0.1 released"  3628164  , -a 指定标签名， -m 指定说明文字

git tag -s <tagname> -m <message> <commit id>
采用PGP签名一个标签
如git tag -s v0.2 -m "signed version 0.2 released "  fec145a ,  -s 用私钥签名一个标签
看这里http://www.ruanyifeng.com/blog/2013/07/gpg.html 了解如何安装gnupg

git tag -d <tagname>
删除标签 git tag -d v0.1

git push origin <tagname>
推送标签到远程
git push origin v1.0

git push origin --tags
一次性推送全部尚未推送到远程的本地标签

git push origin  :refs/tags/<tagname>
如： git push origin  :refs/tags/v0.9


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">现有工程中删除  .DS_Store</h2>
<p>$ find . -name .DS_Store  - print0  |  xargs -0  git  rm -f  --ignore-unmatch</p>
<p>向顶层的.gitignore文件中增加 .DS_Store然后
<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>g</mi><mi>i</mi><mi>t</mi><mi>a</mi><mi>d</mi><mi>d</mi><mi mathvariant="normal">.</mi><mi>g</mi><mi>i</mi><mi>t</mi><mi>i</mi><mi>g</mi><mi>n</mi><mi>o</mi><mi>r</mi><mi>e</mi></mrow><annotation encoding="application/x-tex"> git add .gitignore</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal">a</span><span class="mord mathnormal">d</span><span class="mord mathnormal">d</span><span class="mord">.</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord mathnormal">n</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span></span></span></span></span>   git commit -m '.DS_Store banished'</p>
<h2 data-id="heading-13">下载github上单个文件夹</h2>
<p>将 /tree/master换成/trunk/, 然后用svn  checkout,例如：
svn checkout <a href="https://github.com/Mooophy/Cpp-Primer/trunk/ch03" target="_blank" rel="nofollow noopener noreferrer">github.com/Mooophy/Cpp…</a></p>
<p>gists介绍：</p>
<p><a href="https://www.zhihu.com/question/21343711" target="_blank" rel="nofollow noopener noreferrer">www.zhihu.com/question/21…</a>
<a href="http://www.worldhello.net/gotgithub/06-side-projects/gist.html" target="_blank" rel="nofollow noopener noreferrer">www.worldhello.net/gotgithub/0…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            