
---
title: 'git 常用操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669ff264c9cf461cb9a5031c5654c3c5~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 00:11:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669ff264c9cf461cb9a5031c5654c3c5~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>git 作为一个开源的分布式版本控制系统，在日常开发中占据了一定的地位，可以说，每一个开发者都需要掌握 git 的常用操作，本文将对 git 的常用操作进行说明并演示。</p>
<p>若对本文内容有所异议欢迎指正讨论，若感兴趣，欢迎点赞收藏。</p>
<h2 data-id="heading-0">git 简介</h2>
<p>Git 是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。Linus Torvalds，开源 linux 系统的发明人，这个人我相信大家都知道吧。如今，你看到的大部分服务器其实都是运行在 linux 系统上，令人感到称叹的是，这位大神级别的程序员不仅创造了 linux 系统。那 linux 的代码是如何管理的呢？2002 年之前，世界各地的志愿者把源代码文件通过 diff 的方式发给 Linus，然后由 Linus 本人通过手工方式合并代码！要知道，当时的 linux 的代码量已经很大了，通过人工管理的方式，一是容易出错，二是效率低。于是 Linus 选择了一个商业的版本控制系统 BitKeeper，BitKeeper 的东家 BitMover 公司出于人道主义精神，授权 Linux 社区免费使用这个版本控制系统。最后，出于某种原因，BitMover 公司收回了 linux 社区的免费使用权，于是 Linus 花了两周时间自己用 C 写了一个分布式版本控制系统，这就是 git 的由来了。</p>
<h2 data-id="heading-1">git 的工作区域及流程</h2>
<p>要想弄懂 git 是怎么对我们的代码进行管理的，那首当其冲的是了解 git 的工作区域是如何构成的。因为，只有彻底弄懂了 git 工作区域的构成，你才可以在适当的区域使用合适的命令。如下图所示，此图包含了 git 的 4 个工作区和一些常见的操作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669ff264c9cf461cb9a5031c5654c3c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>workspace</code>：工作区，就是平时进行开发改动的地方，是当前看到最新的内容，在开发的过程也就是对工作区的操作。</p>
<p><code>Index</code>：暂存区，当执行 <code>git add</code> 命令后，工作区的文件就会被移入暂存区，暂存区标记了当前工作区中那些内容是被 git 管理的，当完成某个需求或者功能后需要提交代码，第一步就是通过 <code>git add</code>命令先提交到暂存区。</p>
<p><code>Repository</code>：本地仓库，位于自己的电脑上，通过 <code>git commit</code>命令提交暂存区的内容，会进入本地仓库。</p>
<p><code>Remote</code>：远程仓库，用来托管代码的服务器，远程仓库的内容能够被分布在多个地点的处于协作关系的本地仓库修改，本地仓库修改完代码后通过 <code>git push</code>命令同步代码到远程仓库。</p>
<p>一般来说，git 的工作流程分为以下几步:</p>
<ul>
<li>
<p>0.拉取远程仓库的代码。</p>
</li>
<li>
<p>1.在工作区开发，添加、修改文件。</p>
</li>
<li>
<p>2.将修改后的文件放入暂存区。</p>
</li>
<li>
<p>3.将暂存区的文件提交到本地仓库。</p>
</li>
<li>
<p>4.将本地仓库的修改的文件推送到远程仓库。</p>
</li>
</ul>
<h2 data-id="heading-2">准备工作</h2>
<h3 data-id="heading-3">本地安装 git</h3>
<ul>
<li>git <a href="https://git-scm.com/downloads" target="_blank" rel="nofollow noopener noreferrer">下载地址</a>，根据自己的需要自行下载即可。</li>
</ul>
<h3 data-id="heading-4">配置 ssh 秘钥</h3>
<ul>
<li>
<p>如果不想配置 ssh 秘钥，可以使用 https 的方式关联远程仓库,但可能需要重复输入用户名和密码</p>
</li>
<li>
<p>配置 ssh 秘钥步骤如下：</p>
<ul>
<li>
<p>1.在自己的电脑上打开控制台(cmd 窗口)，然后执行命令<code>ssh-keygen -t rsa -C <你的邮箱地址></code>，待命令执行成功则继续执行下方操作。</p>
</li>
<li>
<p>2.切换到<code>~/.ssh</code>目录下，打开<code>id_rsa.pub</code>文件，并复制该文件下的全部内容。</p>
</li>
<li>
<p>3.在 github 上配置，将上一步复制的本地生成的公钥内容复制到 github 上托管，在 github 页面中依次点击<code>settings ==> SSH and GPG keys ==> add ssh key</code>。然后将上一步复制的<code>id_rsa.pub</code>文件中的内容粘贴进来，然后保存。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d682afef079b477292bdc6b6d0a49f75~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-5">配置用户名和邮箱</h3>
<pre><code class="copyable">//若想为某个项目单独设置用户名和邮箱，则可以执行下方命令，（与全局设置的区别就是不加 --global）
git config user.name "xxxxxxx"
git config user.email "gujunq1998@163.com"

//全局设置用户名和邮箱
git config --global user.name "xxxxxxx"
git config --global user.email "gujunq1998@163.com"

// 删除全局的用户和邮箱
git config --global --unset user.name
git config --global --unset user.email
//设置之后的查看配置的用户名和邮箱
git config --list

//注意，全局配置用户名和邮箱之后再想为某个项目单独设置用户名和邮箱设置的可能不会生效。
//若想设置，则可以按照如下方式设置

//1.进入到该项目的.git目录，执行如下命令(建议在git bash中执行命令)
git config --local --unset user.name
git config --local --unset user.email

//2.设置局部的用户名和邮箱
git config user.name "xxxxxxx"
git config user.email "gujunq1998@163.com"

//3.通过下方命令查看设置是否成功
//注意是在.git这个隐藏文件夹下执行命令（此时的这个命令必须在git bash 中执行才会成功）
cat config

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">git 工作流程</h2>
<h3 data-id="heading-7">1.拉取远程仓库代码到本地仓库</h3>
<ul>
<li>若第一次拉取项目代码则使用<code>git clone</code>命令，具体使用请参考</li>
</ul>
<pre><code class="copyable">git clone -b <分支名> <远程仓库url>

// 从远程仓库中拉取当前项目下的 prod 分支下的代码

git clone -b prod https://github.com/gujunling/vue-template.git
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>更新远程仓库代码到本地(之前拉取过代码到本地,不是第一次拉取代码)</li>
</ul>
<pre><code class="copyable">//拉取更新远程仓库中的 pre 分支中的代码到本地，此时是在拉取过代码之后的操作
  git pull origin pre

// git pull 等同于 git fetch && git merge

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2. 初始化本地仓库（只有新项目且是第一次执行 git 操作才需要此步骤，其他情况不需要执行此步骤）</h3>
<pre><code class="copyable"> //在当前目录下新建一个git仓库，即初始化，会在当前文件夹下创建一个.git文件夹，该文件夹是隐藏文件夹，可以通过勾选查看中的隐藏的项目进行显示
git init
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.添加本地代码到暂存区</h3>
<p>注意:在提交代码之前请先查看一下所在分支是否是自己想要提交代码的分支</p>
<pre><code class="copyable">//会将所有分支列举出来，并在自己当前所处的分支之前标记 * 号
git branch
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 添加当前目录的所有文件到暂存区
git add .  或 git add *

// 添加指定文件到暂存区，如果需要添加多个文件，则多个文件之间使用空格隔开即可。
git add <filename1> <filename2> <filename3>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若某些文件或目录不想要提交，可以在根目录下新建一个 .gitignore 文件，在该文件中添加相关文件或目录即可。</p>
<p><strong>注意，.gitignore 文件只能忽略那些原来没有被 track 的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore 也是无效的，可以重新拉取代码或者手动去除不想提交文件的修改内容。</strong></p>
<p>若不小心把一个不需要的文件添加到暂存区中，想要从暂存区中删除该文件。</p>
<ul>
<li>
<p>方式一：</p>
<pre><code class="copyable">// 对特定的文件进行撤销,如果需要撤销多个文件，文件之间使用空格 隔开即可
git reset <filename1> <filename2> <filename3>

// 撤销所有存在于暂存区的文件
git reset
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>方式二：</p>
<pre><code class="copyable">// 只把文件从暂存区删除，不会修改文件的内容，也不会删除文件
 git rm --cache xxx.vue

// 直接把文件从暂存区删除，同时删除物理文件，回收站也找不到。(不建议这样操作，会造成自己的代码丢失)
git rm -f xxx.vue

//是否删除成功，可以通过下方命令查看git状态
git status

//若列举出的文件中不包含删除的文件则表示从暂存区中删除成功。

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-10">4.提交代码到本地仓库</h3>
<p>代码的提交规范是<code>约定式提交规范</code>（<code>Conventional Commits</code>），可以使用命令**<code>git cz</code>**或者 vscode 的插件（<code>vsc-commitizen</code>）等将代码提交到本地仓库的，使用命令操作见下文 git 提交代码到本地，拉取代码和解决冲突等根据自己的个人习惯，使用命令、插件、图形化界面均可。</p>
<pre><code class="copyable">// git commit '提交文件的描述'   //但这样提交代码会显得代码提交太乱，毕竟不同人提交代码习惯不同，这种行为是不好的。

//推荐使用下方命令来提交代码（遵循 约定式提交规范 ，是目前使用最广的写法，比较合理和系统化，并有配套的工具）
git cz    //会打开提交代码的描述，通过方向键控制上下移动，选中后通过敲击回车键执行下一步，如果在这个过程中选择错误或者想撤销提交代码到本地仓库，可以按Ctrl+C结束

//如果不小心将代码提交到本地仓库却发现提交错分支或者想要重新修改之后再提交到本地仓库可以执行下方命令（将提交到本地仓库的代码从本地仓库中撤销）

 git reset HEAD~

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">注意</h3>
<p>若项目还不支持使用<code>git cz</code>命令，则可以使用如下命令安装。</p>
<pre><code class="copyable">// 安装 commitizen

npm install -g commitizen

//在项目的目录下执行如下命令，使其支持 Angular 的 Commit message 格式。

commitizen init cz-conventional-changelog --save --save-exact
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><code>git cz</code> 命令执行后会进入 interactive 模式，具体的 type 类型的选择参考如下</h4>
<table><thead><tr><th>值</th><th>描述</th></tr></thead><tbody><tr><td>feat</td><td>新增一个功能</td></tr><tr><td>fix</td><td>修复一个Bug</td></tr><tr><td>docs</td><td>文档变更</td></tr><tr><td>style</td><td>代码格式（不影响功能，例如空格、分号等格式修正）</td></tr><tr><td>refactor</td><td>代码重构</td></tr><tr><td>perf</td><td>改善性能</td></tr><tr><td>test</td><td>测试</td></tr><tr><td>build</td><td>变更项目构建或外部依赖（例如scopes: webpack、gulp、npm等）</td></tr><tr><td>ci</td><td>更改持续集成软件的配置文件和package中的scripts命令，例如scopes: Travis, Circle等</td></tr><tr><td>chore</td><td>变更构建流程或辅助工具</td></tr><tr><td>revert</td><td>代码回退</td></tr></tbody></table>
<h4 data-id="heading-13">注意</h4>
<p>选择自己提交的类型后回车，依次填写改动范围、精简描述、长描述、是否是破坏性修改、修复了什么问题等，填写完毕后，<code>husky</code>会调用<code>commitlint</code>对 message 进行格式校验，默认规定<code>type</code>及<code>subject</code>为必填项。</p>
<pre><code class="copyable">1.Select the type of change that you're committing 选择改动类型 (<type>)

2.What is the scope of this change (e.g. component or file name)? 填写改动范围 (<scope>)

3.Write a short, imperative tense description of the change: 写一个精简的描述 (<subject>)

4.Provide a longer description of the change: (press enter to skip) 对于改动写一段长描述 (<body>)

5.Are there any breaking changes? (y/n) 是破坏性修改吗？默认n (<footer>)

6.Does this change affect any openreve issues? (y/n) 改动修复了哪个问题？默认n (<footer>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提交到本地仓库的描述示例如下：</p>
<ul>
<li>
<p>fix(xxx): 修复了 xxx bug</p>
</li>
<li>
<p>feat(组件): 新增组件的 xxx 功能</p>
</li>
<li>
<p>chore(配置): git 隐藏文件配置修改</p>
</li>
<li>
<p>。。。。。。</p>
</li>
</ul>
<h3 data-id="heading-14">5. 提交本地仓库中的代码到远程仓库</h3>
<pre><code class="copyable">//注意，一般在提交代码到远程仓库前都需要先将远程仓库的代码拉取下来，防止自己改动的代码影响到协作开发的其他人员的代码
//即先执行 git pull 在执行 git push

git pull origin <分支名>   //拉取远程仓库中xxx分支的代码到本地仓库

git push origin <分支名>   //提交本地仓库的代码到远程仓库中的xxx分支

//例如：
//拉取远程仓库中master分支下的代码，但最近GitHub上新建项目的主分支名称全部改为main分支，因为个别人认为master分支不尊重人。
git pull origin master

//将本地仓库中的代码提交到远程仓库中的main分支上
git push origin main

//将本地分支的代码强制覆盖远程分支(如果存在冲突，则直接覆盖，一般不建议这样使用)
git push origin main --force
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">注意</h4>
<p>若提交代码时出现错误，查看是否是初次提交，没有将本地仓库与远程仓库进行绑定。</p>
<p>若需要绑定远程仓库货解除与远程仓库之间的关联请参考下文。</p>
<h2 data-id="heading-16">其他常用命令</h2>
<h3 data-id="heading-17">git remote</h3>
<pre><code class="copyable">// 本地代码关联远程仓库
git remote add origin  <远程仓库url>

// 例如：
git remote add origin https://github.com/gujunling/vue-template.git


 //查看当前仓库绑定的远程仓库信息
 git remote -v

// 解除本地代码与远程仓库之间的绑定
git remote remove origin
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">git fetch</h3>
<p>此操作仅仅只会拉取远程的更改，不会自动进行 merge 操作。对当前的代码没有影响</p>
<pre><code class="copyable">// 获取远程仓库特定分支的更新
    git fetch <远程主机名> <分支名>

// 获取远程仓库所有分支的更新
    git fetch --all
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">git rebase</h3>
<p>rebase 翻译为变基，它的作用和 merge 很相似，用于把一个分支的修改合并到当前分支上。</p>
<p>假设我们现在有 2 条分支，一个为 master ，一个为 feature/1，他们都基于初始的一个提交 <code>add readme</code> 进行检出分支，之后，<code>master 分支增加了 3.js,和 4.js 的文件</code>，分别进行了 2 次提交，<code>feature/1 也增加了 1.js 和 2.js 的文件</code>，分别对应以下 2 条提交记录。</p>
<p><code>master</code> 分支提交记录如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fd22731905547fca0056a020aa85c1f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>feature/1</code>分支提交记录如下图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e00be658e4644f9180fe7042f7f37740~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>结合起来看是这样的:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d77b1a0f6b64a29ad479e63fe86abc6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，切换到 feature/1 分支下，执行 <code>git rebase master</code>命令 ,成功之后，通过 <code>git log</code>命令 查看记录。</p>
<p>如下图所示：可以看到先是逐个应用了 mater 分支的更改，然后以 master 分支最后的提交作为基点，再逐个应用 feature/1 的每个更改。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d57ac32c70ac423baf99e9bf8ddaf92e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，我们的提交记录就会非常清晰，没有分叉，上面演示的是比较顺利的情况，但是大部分情况下，rebase 的过程中会产生冲突的，此时，就需要手动解决冲突，然后使用 <code>git add</code> 、<code>git rebase --continue</code> 的方式来处理冲突，完成 rebase，如果不想要某次 rebase 的结果，那么需要使用 <code>git rebase --skip</code>来跳过这次 rebase。</p>
<h3 data-id="heading-20">git merge 和 git rebase 的区别</h3>
<p>不同于 <code>git rebase</code>的是，<code>git merge</code> 在不是 <code>fast-forward</code>（快速合并）的情况下，会产生一条额外的合并记录，类似 <code>Merge branch 'xxx' into 'xxx'</code>的一条提交信息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70d70fd81cbd456abc107cf03c6ec47c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在解决冲突的时候，用 merge 只需要解决一次冲突即可，简单粗暴，而用 rebase 的时候 ，需要一次又一次的解决冲突，但习惯了之后就会发现 rebase 使用起来更舒服(也并不是说这个就是最合适的，需要根据实际情况选择)。</p>
<h3 data-id="heading-21">git rebase 交互模式</h3>
<p>在开发中，经常会遇到在一个分支上产生了很多的无效的提交，这种情况下使用 rebase 的交互式模式可以把已经发生的多次提交压缩成一次提交，得到了一个干净的提交历史，例如某个分支的提交历史情况如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64bb201e4c6149f18a480ecd1a36d210~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>进入交互式模式的方式是执行如下命令：</p>
<pre><code class="copyable">git rebase -i <base-commit>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数 <code>base-commit</code> 就是指明操作的基点提交对象，基于这个基点进行 rebase 的操作，对于上述提交历史的例子，我们要把多个需要合并提交的的第一个提交对象（ac18084）之后的提交压缩成一次提交，我们需要执行的命令是：</p>
<pre><code class="copyable">git rebase -i ac18084
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时会进入一个 vim 的交互式页面，编辑器列出的信息像下列这样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dde4bce2e0449c28d086855b7e527ca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这些信息表示从 ac18084 对象 commit 操作后有 4 个提交。每个提交都用一行来表示，按时间顺序展示，首行是最早的提交，末行是最新的提交。</p>
<p>当修改这个文件后，git 会依次把这些 commit 按照 action 重新执行。action 有很多种，默认都是 pick，就是说使用该 commit，不作任何修改。</p>
<p>我们现在想把后三个提交合并到第一个中去，这里需要用到 squash，该 action 表示 使用该提交，但是把它与前一提交合并，所以只需把后四个的 action 改为 squash 即可。</p>
<pre><code class="copyable">pick       7751df4 feat:更正1
squash     cd94601 feat:更正2
squash     0a137a8 feat:更正3
squash     ff6349f feat:更正4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存( 按下:然后 wq 保存)之后，会唤出编辑器提示基于历史的提交信息创建一个新的提交信息，也就是需要用户编辑一下合并之后的 commit 信息，更改提示信息并保存即可。接着使用<code>git log</code> 查看提交的 commit 信息，rebase 后的提交记录如下图所示，rebase 操作可以让我们的提交历史变得更加清晰。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15f9de9ff7cf4230b35d17e11793f906~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意：只能在自己使用的 feature 分支上进行 rebase 操作，不允许在集成分支上进行 rebase，因为这种操作会修改集成分支的历史记录</strong></p>
<ul>
<li><a href="https://segmentfault.com/a/1190000012897755" target="_blank" rel="nofollow noopener noreferrer">git rebase 交互式 参考</a></li>
</ul>
<h3 data-id="heading-22">git revert 回滚某次的提交</h3>
<p>想象这么一个场景，你的项目最近有 2 个版本要上线，这两个版本还伴随着之前遗留的 bug 的修复，一开始的时候，你将 bug 修复在了第一个版本的 release 分支上，突然在发版前一天，测试那边反馈，需要把第一个版本修复 bug 的内容改在第二个版本上，这个时候，第一个版本的集成分支的提交应该包括了第一个版本的功能内容，遗留 bug 修复的提交和其他同事提交的内容，<code>想要通过 reset 的方式摘除之前的关于 bug 修复的 commit 肯定是不行的</code>，同时，这种做法比较危险，此时，我们<code>既不想破坏之前的提交记录，又想撤回我们遗留 bug 的 commit 记录</code>应该怎么做呢？<code>git revert</code> 就派上了用场。</p>
<pre><code class="copyable">git revert 撤销某次操作，此操作不会修改原本的提交记录，而是会新增一条提交记录来抵消某次操作。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语法：</p>
<ul>
<li>
<p>git revert 针对普通 commit</p>
</li>
<li>
<p>git revert  -m 针对 merge 的 commit</p>
</li>
</ul>
<p>案例演示如下：</p>
<p>如下图所示，假设被红框框起来的地方是会引起 bug 的一次提交，在他的提交之后，又进行了 2 次提交，其中包含了其它同事的提交。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67d38e746b5541fe802eecb6c7572c4d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时想把不必要提交的代码从远程仓库撤销掉，执行 <code>git revert 1121932</code>命令，执行操作后，再打开查看日志，如下图所示，可以看到是<code>新增了一条 commit 记录，之前的 commit 记录并没有消失</code>，此时也达到了代码回退的效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81a939cba154418a84f83331219fd91b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此外， <code>git revert</code> 也可以回滚多次的提交。</p>
<p>语法：<code>git revert [commit1] [commit2] ...</code>,注意这是一个前开后闭区间，即不包括 commit1，但包括 commit2。</p>
<p>回滚提交的代码有两种方式，一种是<code>git revert</code>命令，另一种是<code>git reset</code>命令，两者的区别如下：</p>
<p><code>git revert</code>会新建一条 commit 信息，来撤回之前的修改。</p>
<p><code>git reset</code> 会直接将提交记录退回到指定的 commit 上。(当后面还有新的提交记录时，采用此种方式回滚代码会导致代码丢失，不建议使用)</p>
<p>对于个人的 <code>feature</code>分支而言，可以使用<code>git reset</code>来回退历史记录，之后使用<code>git push --force</code>进行推送到远程，但是如果是在多人协作的集成分支上，不推荐直接使用<code>git reset</code>命令，而是使用更加安全的<code>git revert</code>命令进行撤回提交。这样，提交的历史记录并不会被抹去，可以安全的进行撤回。</p>
<h3 data-id="heading-23">git stash 来暂存文件</h3>
<p>会有这么一个场景，现在你正在用你的 <code>feature</code>分支上开发新功能。这时，生产环境上出现了一个 bug 需要紧急修复，但是你这部分代码还没开发完，不想提交，怎么办？这个时候可以用 <code>git stash</code> 命令先把工作区已经修改的文件<code>暂存</code>起来，然后切换到 <code>prod</code> 分支上进行 bug 的修复，修复完成后，<code>切换回 feature 分支，从堆栈中恢复刚刚保存的内容</code>。</p>
<p>具体步骤示例如下：</p>
<ul>
<li>
<p>1.此时，我正在<code>feature</code>分支开发一个新功能，修改了 1.js 文件里的内容</p>
</li>
<li>
<p>2.还没开发完成，这个时候，我想去 <code>prod</code> 分支上修复 bug，得暂停下开发切换到 prod 分支，但是现在工作区还有内容，此时如果切换分支，git 会报出下面的错误:</p>
</li>
</ul>
<pre><code class="copyable">error: Your local changes to the following files would be overwritten by checkout:
        1.js
Please commit your changes or stash them before you switch branches.
Aborting

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.上面那句话的意思就是说工作区有文件修改，不能提交，需要先进行 <code>commit</code>或者 <code>stash</code> 操作，执行 <code>git stash</code>操作之后,结果如下</li>
</ul>
<pre><code class="copyable">Saved working directory and index state WIP on stash: 22e561c feat: add 1.js
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>4.此时，我们的<strong>工作区已经干净了</strong>，可以<code>切换到 prod 分支进行 bug 修复的工作</code>，假设我们现在 bug 修复完成了，继续切回 <code>feature</code> 分支进行原本功能的开发，此时只需要执行 <code>git stash pop</code>命令，之前我们暂存的修改就会恢复到工作区，如下图所示。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/729bce825c754c79a9b4515a0d904347~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>提示：</strong> 当我们想要暂存文件，切换分支做某些事的时候，可以用<code>git stash</code>这种机制帮助开发。</li>
</ul>
<p>推荐在使用 stash 的相关命令时，每一次暂存的时候，<code>不要直接使用 git stash命令进行暂存下来</code>，而是使用<code>git stash save "message..."</code>这种方式给本次的提交<code>做一个信息的记录</code>，这样，想应用更改的时候，先通过<code>git stash list</code>查看一下所有的暂存列表。之后，推荐使用<code>git stash apply stash@$&#123;num&#125;</code>的方式进行应用对应的 stash，这样<code>不会清空已有的 stash 的列表项，并且能应用到当前的工作区</code>，不需要这个暂存的话，再手动清除就可以了。</p>
<h3 data-id="heading-24">git status 查看 git 状态</h3>
<pre><code class="copyable">// 查看git状态
    git  status
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">git log 查看日志</h3>
<pre><code class="copyable">// 查看当前分支下的版本历史，即日志,（查看提交记录）
    git log
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">git help 查看帮助</h3>
<pre><code class="copyable">// git 帮助命令
     git help
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">git 分支命令</h3>
<pre><code class="copyable">git checkout test  //切换到指定的test分支

git branch xxx    //新建一个xxx分支

git checkout -b xxx  //新建一个xxx分支，并切换到xxx分支，相当于上面两个的结合

git branch -a        //列出所有的本地分支和远程分支

git branch        //列出所有的本地分支

git branch -r     //列出所有的远程分支

git branch -d xxx    //删除xxx分支

git merge <分支名>   //合并本地的分支，是将指定分支合并到当前分支，并非当前分支合并到指定分支。

git merge <远程仓库名>/<分支名>  // 合并远程的分支
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">参考文档</h2>
<ul>
<li>
<p><a href="https://juejin.cn/post/6974184935804534815" target="_blank">juejin.cn/post/697418…</a></p>
</li>
<li>
<p><a href="https://www.liaoxuefeng.com/wiki/896043488029600" target="_blank" rel="nofollow noopener noreferrer">www.liaoxuefeng.com/wiki/896043…</a></p>
</li>
<li>
<p><a href="https://my.oschina.net/javazhiyin/blog/4597064" target="_blank" rel="nofollow noopener noreferrer">my.oschina.net/javazhiyin/…</a></p>
</li>
<li>
<p><a href="https://www.jianshu.com/p/36d970a2b4da" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/36d970a2b…</a></p>
</li>
</ul></div>  
</div>
            