
---
title: 'Git 实用技巧记录'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/0d837f8d104bf1c79c4030784044cf09.png'
author: Dockone
comments: false
date: 2021-08-26 03:08:18
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/0d837f8d104bf1c79c4030784044cf09.png'
---

<div>   
<br><blockquote><br>只有在遇到问题的时候，才体会到技巧带来的好处！</blockquote>如果我们希望能够快速了解或体验一下 <code class="prettyprint">Git</code> 的操作的话，我这里推荐搭建前往这个网站进行学习，其不需要我们安装工具，而且我们的每一步操作都可以在右侧实时看到状态，对于我们学习和理解 <code class="prettyprint">Git</code> 工作方式和原理非常有帮助的。——  欢迎光临 => <a href="https://oschina.gitee.io/learn-git-branching/" rel="nofollow" target="_blank">https://oschina.gitee.io/learn-git-branching/</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/0d837f8d104bf1c79c4030784044cf09.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/0d837f8d104bf1c79c4030784044cf09.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>常见企业工作流程</h3><em>主要介绍，企业中常用的 Git 工作流程！</em><br>
<br>Git Flow：<br>
<ul><li>主干分支</li><li>稳定分支</li><li>开发分支</li><li>补丁分支</li><li>修改分支</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/578bc4491fa0a7e8b373afb67d2b59b6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/578bc4491fa0a7e8b373afb67d2b59b6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Github Flow：<br>
<ul><li>创建分支</li><li>添加提交</li><li>提交 PR 请求</li><li>讨论和评估代码</li><li>部署检测</li><li>合并代码</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/7d9ee386aad9de81b9537ca16f74d4af.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/7d9ee386aad9de81b9537ca16f74d4af.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Gitlab Flow：<br>
<ul><li>带生产分支</li><li>带环境分支</li><li>带发布分支</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/e900668c0a7718dfae44c2accb67283a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/e900668c0a7718dfae44c2accb67283a.png" class="img-polaroid" title="git-prue-use-pretty-03.png" alt="git-prue-use-pretty-03.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>日常使用最佳实践</h3><em>总结日常工作中应该遵循的 Git 使用方式和方法！</em><br>
<br>使用命令行代替图形化界面：<br>
<ul><li>使用命令行来操作，简洁且效率高</li></ul><br>
<br>提交应该尽可能的表述提交修改内容：<br>
<ul><li>区分 <code class="prettyprint">subject</code> 和 <code class="prettyprint">body</code> 内容，使用空行隔开</li><li><code class="prettyprint">subject</code> 一般不超过 <code class="prettyprint">50</code> 个字符</li><li><code class="prettyprint">body</code> 每一行的长度控制在 <code class="prettyprint">72</code> 个字符</li><li><code class="prettyprint">subject</code> 结尾不需要使用句号或者点号结尾</li><li><code class="prettyprint">body</code> 用来详细解释此次提交具体做了什么</li></ul><br>
<br>使用 <code class="prettyprint">.gitignore</code> 文件来排除无用文件：<br>
<ul><li>可使用模板文件，然后根据项目实际进行修改</li></ul><br>
<br>基于分支或 <code class="prettyprint">fork</code> 的开发模式：<br>
<ul><li>不要直接在主干分支上面进行开发</li><li>在新建的分支上进行功能的开发和问题的修复</li></ul><br>
<br>使用 <code class="prettyprint">release</code> 分支和 <code class="prettyprint">tag</code> 标记进行版本管理：<br>
<ul><li>使用 <code class="prettyprint">release</code> 分支发布代码和版本维护（<code class="prettyprint">release/1.32</code>）</li><li>使用 <code class="prettyprint">tag</code> 来标记版本（A-大 <code class="prettyprint">feature</code> 功能；B-小 <code class="prettyprint">feature</code> 功能；C-只修 <code class="prettyprint">bug</code>）</li></ul><br>
<br><h3>常用命令汇总整理</h3><em>日常使用只要记住 <code class="prettyprint">6</code> 个命令就可以了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/67129f65d815e87dc0e01fcd5216a46f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/67129f65d815e87dc0e01fcd5216a46f.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint"># 工作区 -> 暂存区<br>
$ git add <file/dir><br>
<br>
# 暂存区 -> 本地仓库<br>
$ git commit -m "some info"<br>
<br>
# 本地仓库 -> 远程仓库<br>
$ git push origin master  # 本地 master 分支推送到远程 origin 仓库<br>
</pre><br>
<pre class="prettyprint"># 工作区 <- 暂存区<br>
$ git checkout -- <file>  # 暂存区文件内容覆盖工作区文件内容<br>
<br>
# 暂存区 <- 本地仓库<br>
$ git reset HEAD <file>   # 本地仓库文件内容覆盖暂存区文件内容<br>
<br>
# 本地仓库 <- 远程仓库<br>
$ git clone <git_url>        # 克隆远程仓库<br>
$ git fetch upstream master  # 拉取远程代码到本地但不应用在当前分支<br>
$ git pull upstream master   # 拉取远程代码到本地但应用在当前分支<br>
$ git pull --rebase upstream master  # 如果平时使用 rebase 合并代码则加上<br>
</pre><br>
<pre class="prettyprint"># 工作区 <- 本地仓库<br>
$ git reset <commit>          # 本地仓库覆盖到工作区（保存回退文件内容修改）<br>
$ git reset --mixed <commit>  # 本地仓库覆盖到工作区（保存回退文件内容修改）<br>
$ git reset --soft <commit>   # 本地仓库覆盖到工作区（保留修改并加到暂存区）<br>
$ git reset --hard <commit>   # 本地仓库覆盖到工作区（不保留修改直接删除掉)<br>
</pre><br>
<h3>配置实用参数选项</h3></em>虽然配置比较简单，但是非常有用！*<br>
<h4>全局配置</h4><pre class="prettyprint"># 用户信息<br>
$ git config --global user.name "your_name"<br>
$ git config --global user.email "your_email"<br>
<br>
# 文本编辑器<br>
$ git config --global core.editor "nvim"<br>
<br>
# 分页器<br>
$ git config --global core.pager "more"<br>
<br>
# 别名<br>
$ git config --global alias.gs "git status"<br>
<br>
# 纠错<br>
$ git config --global help.autocorrect 1<br>
</pre><br>
<h4>个人配置</h4><pre class="prettyprint"># 不加 --global 参数的话，则为个人配置<br>
$ git config --list<br>
$ git config user.name<br>
$ git config user.name "your_name"<br>
<br>
# 如果在项目中设置，则保存在 .git/config文件里面<br>
$ cat .git/config<br>
[user]<br>
name = "your_name"<br>
......<br>
</pre><br>
<h3>合并和变基的选择</h3><em>到底什么时候使用 merge 操作，什么时候使用 rebase 操作呢？</em><br>
<h4>使用 merge 操作 - Python 中的 Requests 库在使用</h4>支持使用 <code class="prettyprint">merge</code> 的开发者，他们认为仓库的提交历史就是记录实际发生过什么，它是针对于历史的一个文档，本身其实是有价值的，我们不应该随意修改。我们改变历史的话，就相当于使用“谎言”来掩盖实际发生过的事情，而这些痕迹是应该被保留的。可能，这样并不是很好。<br>
<pre class="prettyprint"># 3rd 的两个分支的 commit 修改相同内容<br>
*   62a322d - (HEAD->master) Merge branch 'hotfix3' into master<br>
|\<br>
| * 6fa8f4a - (hotfix3) 3rd commit in hotfix3<br>
* | 548d681 - 3rd commit in master<br>
|/<br>
* 6ba4a08 - 2nd commit<br>
* 22afcc1 - 1st commit<br>
</pre><br>
<h4>使用 rebase 操作 - Python 中的 Django 库在使用</h4>支持使用 <code class="prettyprint">rebase</code> 的开发者，他们认为提交历史是项目过程中发生过的事情，需要项目的主干非常的干净。而使用 <code class="prettyprint">merge</code> 操作会生成一个 <code class="prettyprint">merge</code> 的 <code class="prettyprint">commit</code> 对象，让提交历史多了一些非常多余的内容。<br>
<br>当我们后期，使用 <code class="prettyprint">log</code> 命令参看提交历史的话，会发现主干的提交历史非常的尴尬。比如，同样的修改内容重复提交了两次，这显然是分支合并导致的问题。<br>
<pre class="prettyprint"># 3rd 的两个分支的 commit 修改相同内容<br>
* 697167e - (HEAD -> master, hotfix) 3rd commit<br>
* 6ba4a08 - 2nd commit (2 minutes ago)<br>
* 22afcc1 - 1st commit (3 minutes ago)<br>
</pre><br>
<h4>两者的使用原则</h4>总的原则就是，只对尚未推送或分享给其他人的本地修改执行变基操作清理历史，从不对已经推送到仓库的提交记录执行变基操作，这样，你才可能享受到两种方式带来的便利。<br>
<h3>更新仓库提交历史</h3><code class="prettyprint">Git</code> 提供了一些工具，可以帮助我们完善版本库中的提交内容，比如：<br>
<h4>合并多个 <code class="prettyprint">commit</code> 提交记录</h4>日常开发中，我们为了完成一个功能或者特性，提交很多个 <code class="prettyprint">commit</code> 记录。但是在最后，提交 <code class="prettyprint">PR</code> 之前，一般情况下，我们是应该整理下这些提交记录的。有些 <code class="prettyprint">commit</code> 需要合并起来，或者需要将其删除掉，等等。<br>
<pre class="prettyprint"># 调整最近五次的提交记录<br>
$ git rebase -i HEAD~5<br>
$ git rebase -i 5af4zd35  # 往前第六次的commit值<br>
reword c2aeb6e 3rd commit<br>
squash 25a3122 4th commit<br>
pick 5d36f1d 5th commit<br>
fixup bd5d32f 6th commit<br>
drop 581e96d 7th commit<br>
<br>
# 查看提交历史记录<br>
$ git log<br>
* ce813eb - (HEAD -> master) 5th commit<br>
* aa2f043 - 3rd commit -> modified<br>
* 6c5418f - 2nd commit<br>
* c8f7dea - 1st commit<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/251c3bd174918aed8257863e495b0579.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/251c3bd174918aed8257863e495b0579.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>删除意外调试的测试代码</h4>有时候提交之后，我们才发现提交的历史记录中存在这一些问题，而这个时候我们又不想新生成一个 <code class="prettyprint">commit</code> 记录，且达到一个修改的目录。即，修改之前的 <code class="prettyprint">commit</code> 提交记录。<br>
<pre class="prettyprint"># 不使用分页器<br>
$ git --no-pager log --oneline -1<br>
d5e96d9 (HEAD -> master) say file<br>
<br>
# 改变提交信息并加入暂存区<br>
$ echo "hello" > say.txt<br>
$ git add -u<br>
<br>
# 改变当前最新一次提交记录<br>
$ git commit --amend<br>
# 改变且息不改变提交信<br>
$ git commit --amend --no-edit<br>
# 改变当前最新一次提交记录并修改信息<br>
$ git commit --amend -m "some_info"<br>
<br>
# 不使用分页器<br>
$ git --no-pager log --oneline -1<br>
9e1e0eb (HEAD -> master) say file<br>
</pre><br>
<h4>取消多个 <code class="prettyprint">commit</code> 中的部分提交</h4>我们开发了一个功能，而在上线的时候，产品经理说这个功能的部分特性已经不需要了，即相关特性的提交记录和内容就可以忽略/删除掉了。<br>
<pre class="prettyprint"># 回滚操作(可多次执行回滚操作)<br>
# 彻底上次提交记录；也可是 PR 的提交记录<br>
# 默认会生成一个类型为 reverts 的新 commit 对象<br>
$ git revert 3zj5sldl<br>
</pre><br>
<h4>合并某些特定的 <code class="prettyprint">commit</code> 提交</h4>我们不希望合并整个分支，而是需要合并该分支的某些提交记录就可以了。<br>
<pre class="prettyprint"># 摘樱桃<br>
$ git cherry-pick -x z562e23d<br>
</pre><br>
<h3>使用引用日志记录</h3><em>如何找回我们丢失的内容和记录？</em><br>
<br>我们之前说过，使用下面命令回退内容、强制推送代码、删除本地分支，都是非常危险的操作，因为重置之后我们就没有办法在找到之前的修改内容了。<br>
<pre class="prettyprint"># 回退<br>
$ git reset --hard <commit><br>
<br>
# 推送<br>
$ git push origin master -f<br>
<br>
# 分支<br>
$ git branch -D <branch_name><br>
</pre><br>
其实 <code class="prettyprint">Git</code> 给我们留了一个后门，就是使用 <code class="prettyprint">relflog</code> 命令来找回之前的内容，只不过是相对来说麻烦一些。而原理也很简答，就是在我们使用 <code class="prettyprint">Git</code> 命令操作仓库的时候，<code class="prettyprint">Git</code> 偷偷地帮助我们把所有的操作记录了下来。<br>
<pre class="prettyprint"># 查看日志记录<br>
$ git --no-pager log --oneline -1<br>
4bc8703 (HEAD -> master) hhhh<br>
<br>
# 回退到上次提交<br>
$ git reset --hard HEAD~1<br>
<br>
# 查看引用日志记录<br>
$ git reflog<br>
6a89f1b (HEAD -> master) HEAD@&#123;0&#125;: reset: moving to HEAD~1<br>
4bc8703 HEAD@&#123;1&#125;: commit (amend): hhhh<br>
<br>
# 找回内容<br>
$ git cherry-pick 4bc8703<br>
</pre><br>
<h3>批量修改历史提交</h3><em>批量修改历史提交虽然不常用，但是理解的话可以省下很多时间！</em><br>
<br>之前我们学习到的命令都是针对于一个或者多个 <code class="prettyprint">commit</code> 提交信息进行修改的，如果我们需要全局修改历史提交呢？当然，<code class="prettyprint">Git</code> 中也是支持全局修改历史提交的，比如全局修改邮箱地址，或者将一个文件从全局历史中删除或修改。<br>
<ul><li>开源项目中使用了公司邮箱进行提交了</li><li>提交文件中包含隐私性的密码相关信息</li><li>提交时将大文件提交到了仓库代码中了</li></ul><br>
<br>这里我们可以使用 <code class="prettyprint">filter-brach</code> 的方式进行修改，但是建议在使用之前，新建一个分支，在上面进行测试没有问题之后，再在主干上操作，防止出现问题，背个大锅在身上。<br>
<pre class="prettyprint"># 创建分支<br>
$ git branch -b testing<br>
<br>
# 修改邮箱地址<br>
$ git filter-branch --commit-filter '<br>
if [ "$GIT_AUTHOR_EMAIL" == "escape@escapelife.site" ]; then<br>
    GIT_AUTHOR_NAME="escape";<br>
    GIT_AUTHOR_EMAIL="escape@gmail.com";<br>
    git commit-tree "$@"<br>
else<br>
    git commit-tree "$@"<br>
fi' HEAD<br>
</pre><br>
<h3>灵活使用钩子函数</h3><em>主要介绍.git/hooks 目录下面的示例钩子函数！</em><br>
<br>在 <code class="prettyprint">Git</code> 里面有两类，分别对应客户端和服务端钩子函数。客户端的钩子函数，是在执行提交和合并之类的操作时调用的。而服务端钩子函数，就是当服务端收到代码提交之后，可以出发代码检查和持续集成的步骤。作为开发者我们并不会搭建 <code class="prettyprint">Git</code> 服务器，所以基本不会涉及。<br>
<br>下面就是 <code class="prettyprint">Git</code> 自带的钩子脚本，但是自带的都 <code class="prettyprint">.sample</code> 作为后缀，表示并没有启用，表示为一个示例。如果需要启用的话，将 <code class="prettyprint">.sample</code> 作为后缀删除掉，即可。而其钩子脚本的对应内容，都是使用 <code class="prettyprint">Shell</code> 语法进行编写的。<br>
<pre class="prettyprint">➜ ll .git/hooks<br>
total 112<br>
-rwxr-xr-x  applypatch-msg.sample<br>
-rwxr-xr-x  commit-msg.sample<br>
-rwxr-xr-x  fsmonitor-watchman.sample<br>
-rwxr-xr-x  post-update.sample<br>
-rwxr-xr-x  pre-applypatch.sample<br>
-rwxr-xr-x  pre-commit.sample<br>
-rwxr-xr-x  pre-merge-commit.sample<br>
-rwxr-xr-x  pre-push.sample  # 不会推送包含WIP的commit提交<br>
-rwxr-xr-x  pre-rebase.sample<br>
-rwxr-xr-x  pre-receive.sample<br>
-rwxr-xr-x  prepare-commit-msg.sample<br>
-rwxr-xr-x  update.sample<br>
</pre><br>
其实，钩子脚本使用任何语言编写都是可以的，只要你让程序返回对应的退出码就可以了。<br>
<br>正常的代码合入流程就是，我们本地修改之后，提一个 <code class="prettyprint">PR</code> 请求并通过 <code class="prettyprint">Github</code> 的 <code class="prettyprint">CI</code> 检查，接下来进行代码评审，最后被合并入主干。但是，好的一个习惯就是，在代码提交之前就应该保证代码不会出现语法错误等基础问题，比如通过 <code class="prettyprint">flake8</code> 和 <code class="prettyprint">PEP8</code> 标准等。<br>
<br>这个时候我们就可以使用 <a href="https://github.com/pre-commit/pre-commit"><code class="prettyprint">pre-commit</code></a> 这个 <code class="prettyprint">GitHub</code> 的开源项目了，其本质就是给项目添加钩子函数的一个脚本，可以保证我们在提交代码或者推送代码之前，先检查代码的质量。<br>
<br>而 <a href="https://github.com/pre-commit/pre-commit-hooks"><code class="prettyprint">pre-commit-hooks</code></a> 这个项目里面包含的就是，现在所支持的钩子脚本，即开箱即用的钩子脚本集合。而其钩子脚本的对应内容，都是使用 <code class="prettyprint">Python</code> 语法进行编写的。<br>
<pre class="prettyprint"># 安装方式<br>
$ pip install pre-commit<br>
<br>
# 指定 hook 类型（即在哪里检查）<br>
$ pre-commit install -f --hook-type pre-push<br>
<br>
# 配置需要执行的检查<br>
$ cat .pre-commit-config.yaml<br>
repos:<br>
- repo: https://github.com/pre-commit/pre-commit-hooks<br>
rev: v2.9.2<br>
hooks:<br>
- id: trailing-whitespace<br>
- id: flake8<br>
<br>
# 执行 push 操作时检查<br>
$ git push origin master<br>
</pre><br>
<h3>快速克隆大型项目</h3><em>在大项目中工作中，拉取代码非常占时间！</em><br>
<br>我们如果想为 <code class="prettyprint">Linux</code> 或 <code class="prettyprint">Python</code> 这样的大型项目贡献提交的时候，首先遇到的问题就是，如果快速的 <code class="prettyprint">clone</code> 该项目到本地。因为改项目提交历史超多且仓库巨大，加了国内网络的问题，可能等项目完全拉下来的时候，我们的热情都消减下去了。<br>
<br>好在 <code class="prettyprint">Git</code> 也帮我们想到了这样的问题，我们可以使用 <code class="prettyprint">--depth</code> 参数值拉取远程仓库上面最新一次的提交历史，并不包含项目历史记录，即 <code class="prettyprint">.git/objects/</code> 目录下的对象只是本地的，并不包含之前的多次修改产生的对象。<br>
<pre class="prettyprint"># 克隆不包含之前历史<br>
$ git clone http://xxx.xx.xxx/xxx --depth=1<br>
</pre><br>
但是，有时间我们可能会需要 <code class="prettyprint">clone</code> 仓库中的某个 <code class="prettyprint">tag</code> 版本对应下的内容。如果我们直接使用 <code class="prettyprint">clone</code> 命令是无法做到的，需要执行如下操作，即可完美解决。<br>
<pre class="prettyprint"># 克隆特定版本代码<br>
$ git init xxx-15-0-1<br>
$ git remote add origin http://xxx.xx.xxx/xxx<br>
$ git -c protocol.version=2 fetch origin 15.0.1 --depth=1<br>
$ git checkout FETCH_HEAD<br>
</pre><br>
上面的效果已经基本可以满足我们日常使用需求了，但是不幸的是，你现在接受了一个机器学习的项目，里面包含了大量的 <code class="prettyprint">lfs</code> 文件，现在 <code class="prettyprint">clone</code> 又会变得非常慢。可以使用如下操作来避免，<code class="prettyprint">Git</code> 工具主动拉去 <code class="prettyprint">lfs</code> 文件，来达到目录。<br>
<pre class="prettyprint"># 克隆不包含 LFS 数据<br>
$ GIT_LFS_SKIP_SMUDGE=1 git clone http://xxx.xx.xxx/xxx<br>
</pre><br>
<h3>如何处理工作中断</h3><em>如果在多路运转的时候，还能够高效的进行开发！</em><br>
<br>比如，我们现在正在一个分支为项目添加一个小的功能，此时，产品经理找到你说是线上环境现在有一个 <code class="prettyprint">bug</code> 需要让你来修复下。但是，此时我们添加的小功能并没有完成。<br>
<br>如果此时，我们直接切换到主干分支的话，会将之前分支没有来得及提交的内容全部都带到了主干分支上来，这是我们不想看到的情况。此时，我们需要保存上个分支的工作状态，在我们修改完成线上 <code class="prettyprint">bug</code> 之后，再继续工作。<br>
<br>好在 <code class="prettyprint">Git</code> 也帮我们想到了这样的问题，我们可以使用 <code class="prettyprint">stash</code> 子命令帮助我们将当前工作区、暂存区当中的修改都保存到堆栈之中。等到需要处理的时候，再弹出堆栈中的内容，我们再次进行开发。<br>
<pre class="prettyprint">➜ git stash -h<br>
usage: git stash list [<options>]<br>
or: git stash show [<options>] [<stash>]<br>
or: git stash drop [-q|--quiet] [<stash>]<br>
or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]<br>
or: git stash branch <branchname> [<stash>]<br>
or: git stash clear<br>
or: git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]<br>
      [-u|--include-untracked] [-a|--all] [-m|--message <message>]<br>
      [--pathspec-from-file=<file> [--pathspec-file-nul]]<br>
      [--] [<pathspec>...]]<br>
or: git stash save [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]<br>
      [-u|--include-untracked] [-a|--all] [<message>]<br>
</pre><br>
<pre class="prettyprint"># 存储当前的修改但不用提交 commit<br>
$ git stash<br>
<br>
# 保存当前状态包括 untracked 的文件<br>
$ git stash -u<br>
<br>
# 展示所有 stashes 信息<br>
$ git stash list<br>
<br>
# 回到某个 stash 状态<br>
$ git stash apply <stash@&#123;n&#125;><br>
<br>
# 删除储藏区<br>
$ git stash drop <stash@&#123;n&#125;><br>
<br>
# 回到最后一个 stash 的状态并删除这个 stash 信息<br>
$ git stash pop<br>
<br>
# 删除所有的 stash 信息<br>
$ git stash clear<br>
<br>
# 从 stash 中拿出某个文件的修改<br>
$ git checkout <stash@&#123;n&#125;> -- <file-path><br>
</pre><br>
其实比较保险的做法就是，将当前的所有修改进行 <code class="prettyprint">push</code> 并保存到远程仓库里面。这样的好处在于，可以远端备份我们的修改，不会害怕本地文件丢失等问题。等到我们需要继续开发的时候，拉下对应内容，再想办法进行补救，比如使用 <code class="prettyprint">--amend</code> 或者 <code class="prettyprint">reset</code> 命令。<br>
<pre class="prettyprint"># 将工作区和暂存区覆盖最近一次提交<br>
$ git commit --amend<br>
$ git commit --amend -m "some_info"<br>
<br>
# 回退到指定版本并记录修改内容（--mixed）<br>
# 本地仓库覆盖到工作区（保存回退文件内容修改）<br>
$ git reset a87f328<br>
$ git reset HEAD~<br>
$ git reset HEAD~2<br>
$ git reset <tag>~2<br>
$ git reset --mixed <commit/reference><br>
<br>
# 本地仓库覆盖到工作区（不保留修改直接删除掉）<br>
$ git reset --soft <commit/reference><br>
# 本地仓库覆盖到工作区（保留修改并加到暂存区）<br>
$ git reset --hard <commit/reference><br>
</pre><br>
<br>原文链接：<a href="https://www.escapelife.site/posts/f6ffe82b.html" rel="nofollow" target="_blank">https://www.escapelife.site/posts/f6ffe82b.html</a>，作者：Escape
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            