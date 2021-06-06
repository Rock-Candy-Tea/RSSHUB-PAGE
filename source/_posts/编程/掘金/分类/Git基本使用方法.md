
---
title: 'Git基本使用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064f858082354fa6b01b71a47ffe202b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 23:52:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064f858082354fa6b01b71a47ffe202b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/post/6970585438876598279#Git%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5" title="Git基本概念"></a>Git 基本概念</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064f858082354fa6b01b71a47ffe202b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Workspace：工作区<br>
Index / Stage：暂存区<br>
Repository：仓库区（或本地仓库）<br>
Remote：远程仓库</p>
<h2 data-id="heading-1"><a href="https://juejin.cn/post/6970585438876598279#Git%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4" title="Git常用命令"></a>Git 常用命令</h2>
<p>初始化一个仓库：<code>git init</code><br>
添加文件：<code>git add 文件名</code><br>
添加所有文件：<code>git add *</code><br>
提交到本地仓库： <code>git commit -m "提交说明"</code><br>
查看仓库的状态：<code>git status</code><br>
查看发生更改的文件的具体改变位置：<code>git diff 文件名</code><br>
查看我们提交历史（以便确定要回退到哪个版本。）：<code>git log</code><br>
查看我们提交历史 (单行显示)：<code>git log--pretty=oneline</code><br>
回退到上一个版本：<code>git reset --hard HEAD^</code><br>
回退到上上一个版本：<code>git reset --hard HEAD^^</code><br>
回退到 100 个之前的版本：<code>git reset --hard HEAD~100</code><br>
回退到指定版本：<code>git reset --hard 版本号</code>（版本号也就是 git log–pretty=oneline 前面显示的 id，只需要记住前几位即可）<br>
查看命令历史（用来重返未来）：<code>git reflog</code><br>
用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以 “一键还原”：<code>git checkout</code><br>
删除一个文件：<code>git rm 文件名</code></p>
<p>提交到远程仓库：<br>
1、在远程创建一个与本地仓库名一致的仓库<br>
2、git remote add origin <a href="mailto:git@github.com">git@github.com</a>: 用户名 / 仓库名. git<br>
3、git push -u origin master</p>
<h2 data-id="heading-2"><a href="https://juejin.cn/post/6970585438876598279#%E5%88%9D%E6%AC%A1%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AEGit" title="初次使用配置Git"></a>初次使用配置 Git</h2>
<p>第一步：设置用户名和邮箱，并且生成秘钥<br>
不要密码的话直接一直 Enter 就行！</p>
<pre><code class="copyable">git config --global user.name "你的名字"
git config --global user.email "你的邮箱" 
ssh-keygen -t rsa -C "你的邮箱"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d29ab24490a74cdb96d508ad0227cb69~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二步：到 git 仓库，添加秘钥<br>
如果你没有改变秘钥的生成路径，那么通过家目录的<code>.ssh</code>下通过 cat 命令应该可以看到生成的秘钥，添加到 GitHub（这里以 Github 为例）的秘钥中！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afbb840663af4090972e4894a35515be~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8bf95abe37d4a809f3f38c9d1d3d37c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三步: <code>ssh -T git@github.com</code> 测试一下通不通，不通就是<code>ssh-agent -s</code> <code>ssh-add ~/.ssh/id_rsa</code>操作这两步</p>
<p>第四步：把代码 clone 下来，使用<code>git clone</code> 命令将仓库拷贝下来！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb8a5f2bf0f945419cc36b014b182557~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3"><a href="https://juejin.cn/post/6970585438876598279#%E5%88%86%E7%B1%BB%E6%93%8D%E4%BD%9C%E7%9A%84%E5%91%BD%E4%BB%A4" title="分类操作的命令"></a>分类操作的命令</h2>
<h3 data-id="heading-4"><a href="https://juejin.cn/post/6970585438876598279#%E6%96%B0%E5%BB%BA%E4%BB%A3%E7%A0%81%E5%BA%93" title="新建代码库"></a>新建代码库</h3>
<ul>
<li>在当前目录新建一个 Git 代码库<code>git init</code></li>
<li>新建一个目录，将其初始化为 Git 代码库<code>git init [project-name]</code></li>
<li>下载一个项目和它的整个代码历史<code>git clone [url]</code></li>
</ul>
<h3 data-id="heading-5"><a href="https://juejin.cn/post/6970585438876598279#%E9%85%8D%E7%BD%AE" title="配置"></a>配置</h3>
<ul>
<li>Git 的设置文件为 <strong>.gitconfig</strong> ，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）</li>
<li>显示当前的 Git 配置<code>git config --list</code></li>
<li>编辑 Git 配置文件<code>git config -e [--global]</code></li>
<li>设置提交代码时的用户信息
<ul>
<li><code>git config [--global] user.name "[name]"</code></li>
<li><code>git config [--global] user.email "[email address]"</code></li>
</ul>
</li>
</ul>
<h3 data-id="heading-6"><a href="https://juejin.cn/post/6970585438876598279#%E5%A2%9E%E5%8A%A0-%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6" title="增加/删除文件"></a>增加 / 删除文件</h3>
<ul>
<li>添加指定文件到暂存区<code>git add [file1] [file2] ...</code></li>
<li>添加指定目录到暂存区，包括子目录<code>git add [dir]</code></li>
<li>添加当前目录的所有文件到暂存区<code>git add .</code></li>
<li>删除工作区文件，并且将这次删除放入暂存区<code>git rm [file1] [file2] ...</code></li>
<li>停止追踪指定文件，但该文件会保留在工作区<code>git rm --cached [file]</code></li>
<li>改名文件，并且将这个改名放入暂存区<code>git mv [file-original] [file-renamed]</code></li>
</ul>
<h3 data-id="heading-7"><a href="https://juejin.cn/post/6970585438876598279#%E4%BB%A3%E7%A0%81%E6%8F%90%E4%BA%A4" title="代码提交"></a>代码提交</h3>
<ul>
<li>提交暂存区到仓库区<code>git commit -m [message]</code></li>
<li>提交暂存区的指定文件到仓库区<code>git commit [file1] [file2] ... -m [message]</code></li>
<li>提交工作区自上次 commit 之后的变化，直接到仓库区<code>git commit -a</code></li>
<li>提交时显示所有 diff 信息<code>git commit -v</code>
<ul>
<li>使用一次新的 commit，替代上一次提交如果代码没有任何新变化，则用来改写上一次 commit 的提交信息<code>git commit --amend -m [message]</code></li>
</ul>
</li>
<li>重做上一次 commit，并包括指定文件的新变化<code>git commit --amend ...</code></li>
</ul>
<h3 data-id="heading-8"><a href="https://juejin.cn/post/6970585438876598279#%E5%88%86%E6%94%AF" title="分支"></a>分支</h3>
<ul>
<li>列出所有本地分支<code>git branch</code></li>
<li>列出所有远程分支<code>git branch -r</code></li>
<li>列出所有本地分支和远程分支<code>git branch -a</code></li>
<li>新建一个分支，但依然停留在当前分支<code>git branch [branch-name]</code></li>
<li>新建一个分支，并切换到该分支<code>git checkout -b [branch]</code></li>
<li>新建一个分支，指向指定 commit<code>git branch [branch] [commit]</code></li>
<li>新建一个分支，与指定的远程分支建立追踪关系<code>git branch --track [branch] [remote-branch]</code></li>
<li>切换到指定分支，并更新工作区<code>git checkout [branch-name]</code></li>
<li>建立追踪关系，在现有分支与指定的远程分支之间<code>git branch --set-upstream [branch] [remote-branch]</code></li>
<li>合并指定分支到当前分支<code>git merge [branch]</code></li>
<li>选择一个 commit，合并进当前分支<code>git cherry-pick [commit]</code></li>
<li>删除分支<code>git branch -d [branch-name]</code></li>
<li>删除远程分支<code>git push origin --delete</code>、<code>git branch -dr</code></li>
</ul>
<h3 data-id="heading-9"><a href="https://juejin.cn/post/6970585438876598279#%E6%A0%87%E7%AD%BE" title="标签"></a>标签</h3>
<ul>
<li>列出所有 tag <code>git tag</code></li>
<li>新建一个 tag 在当前 commit<code>git tag [tag]</code></li>
<li>新建一个 tag 在指定 commit<code>git tag [tag] [commit]</code></li>
<li>查看 tag 信息<code>git show [tag]</code></li>
<li>提交指定 tag<code>git push [remote] [tag]</code></li>
<li>提交所有 tag<code>git push [remote] --tags</code></li>
<li>新建一个分支，指向某个 tag<code>git checkout -b [branch] [tag]</code></li>
</ul>
<h3 data-id="heading-10"><a href="https://juejin.cn/post/6970585438876598279#%E6%9F%A5%E7%9C%8B%E4%BF%A1%E6%81%AF" title="查看信息"></a>查看信息</h3>
<ul>
<li>
<p>显示有变更的文件<code>git status</code></p>
</li>
<li>
<p>显示当前分支的版本历史<code>git log</code></p>
</li>
<li>
<p>显示 commit 历史，以及每次 commit 发生变更的文件<code>git log --stat</code></p>
</li>
<li>
<p>显示某个文件的版本历史，包括文件改名<code>git log --follow [file]</code>、<code>git whatchanged [file]</code></p>
</li>
<li>
<p>显示指定文件相关的每一次 diff<code>git log -p [file]</code></p>
</li>
<li>
<p>显示指定文件是什么人在什么时间修改过<code>git blame [file]</code></p>
</li>
<li>
<p>显示暂存区和工作区的差异<code>git diff</code></p>
</li>
<li>
<p>显示暂存区和上一个 commit 的差异<code>git diff --cached []</code></p>
</li>
<li>
<p>显示工作区与当前分支最新 commit 之间的差异<code>git diff HEAD</code></p>
</li>
<li>
<p>显示两次提交之间的差异<code>git diff [first-branch]...[second-branch]</code></p>
</li>
<li>
<p>显示某次提交的元数据和内容变化<code>git show [commit]</code></p>
</li>
<li>
<p>显示某次提交发生变化的文件<code>git show --name-only [commit]</code></p>
</li>
<li>
<p>显示某次提交时，某个文件的内容<code>git show [commit]:[filename]</code></p>
</li>
<li>
<p>显示当前分支的最近几次提交<code>git reflog</code></p>
</li>
</ul>
<h3 data-id="heading-11"><a href="https://juejin.cn/post/6970585438876598279#%E8%BF%9C%E7%A8%8B%E5%90%8C%E6%AD%A5" title="远程同步"></a>远程同步</h3>
<ul>
<li>下载远程仓库的所有变动<code>git fetch [remote]</code></li>
<li>显示所有远程仓库<code>git remote -v</code></li>
<li>显示某个远程仓库的信息<code>git remote show [remote]</code></li>
<li>增加一个新的远程仓库，并命名<code>git remote add [shortname] [url]</code></li>
<li>取回远程仓库的变化，并与本地分支合并<code>git pull [remote] [branch]</code></li>
<li>上传本地指定分支到远程仓库<code>git push [remote] [branch]</code></li>
<li>强行推送当前分支到远程仓库，即使有冲突<code>git push [remote] --force</code></li>
<li>推送所有分支到远程仓库<code>git push [remote] --all</code></li>
</ul>
<h3 data-id="heading-12"><a href="https://juejin.cn/post/6970585438876598279#%E6%92%A4%E9%94%80" title="撤销"></a>撤销</h3>
<ul>
<li>恢复暂存区的指定文件到工作区<code>git checkout [file]</code></li>
<li>恢复某个 commit 的指定文件到工作区<code>git checkout [commit] [file]</code></li>
<li>恢复上一个 commit 的所有文件到工作区<code>git checkout .</code></li>
<li>重置暂存区的指定文件，与上一次 commit 保持一致，但工作区不变<code>git reset [file]</code></li>
<li>重置暂存区与工作区，与上一次 commit 保持一致<code>git reset --hard</code></li>
<li>重置当前分支的指针为指定 commit，同时重置暂存区，但工作区不变<code>git reset [commit]</code></li>
<li>重置当前分支的 HEAD 为指定 commit，同时重置暂存区和工作区，与指定 commit 一致<code>git reset --hard [commit]</code></li>
<li>重置当前 HEAD 为指定 commit，但保持暂存区和工作区不变<code>git reset --keep [commit]</code></li>
<li>新建一个 commit，用来撤销指定 commit 后者的所有变化都将被前者抵消，并且应用到当前分支<code>git revert [commit]</code></li>
</ul>
<h3 data-id="heading-13"><a href="https://juejin.cn/post/6970585438876598279#%E5%85%B6%E4%BB%96" title="其他"></a>其他</h3>
<ul>
<li>生成一个可供发布的压缩包<code>git archive</code></li>
<li>备份当前工作区的内容<code>git stash</code></li>
<li>从 Git 栈中读取最近一次保存的内容，恢复工作区的相关内容<code>git stash pop</code></li>
<li>显示 Git 栈内的所有备份<code>git stash list</code></li>
<li>清空 Git 栈<code>git stash clear</code></li>
</ul>
<h2 data-id="heading-14"><a href="https://juejin.cn/post/6970585438876598279#%E5%B8%B8%E7%94%A8%E7%9A%84%E5%91%BD%E4%BB%A4%E5%9B%BE" title="常用的命令图"></a>常用的命令图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c09653811c46411984612e09623af54f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            