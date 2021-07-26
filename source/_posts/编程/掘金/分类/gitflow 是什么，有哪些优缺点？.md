
---
title: 'gitflow 是什么，有哪些优缺点？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761cdc2b87dd4da3b99132d94212c9f3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 00:12:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761cdc2b87dd4da3b99132d94212c9f3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 什么是git</h2>
<p>Git是一个分布式的版本管理工具，它分为远程仓库（云端仓库，存在后端服务器中）（仓库：repository简写repo：）和本地仓库。本地和云端的仓库的维护机制是类似的，它们都是使用一个类似一个树形结构的数据结构来维护的。每次的文件内容的改变都是一个节点(blob节点)，每个commit都是一个tree节点，节点中附带代码的操作信息和节点类型。详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F96631135" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/96631135" ref="nofollow noopener noreferrer">传送门</a>。</p>
<h2 data-id="heading-1">2. git的优点</h2>
<ol>
<li>git 是分布式的，有本地分支管理功能，所以，就算没有网络也可以进行本地的维护。</li>
<li>git的每个变动都是一个节点因此，每次的文件内容的变动都可以单独保存并且可以逐个的进行应用管理。在所有代码合并后也可以看到所有变更内容，而其他的版本管理工具则不可以。</li>
<li>由于git每次的变更都会生成一个完整的文件快照，所以它非常快。用空间来换取时间。</li>
<li>由于git会面临内存问题，它有自己的内存维护机制比如：删掉无用的节点，压缩打包历史记录等...</li>
<li>git有非常多的命令，可以灵活的使用。详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fgit%2Fgit-basic-operations.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/git/git-basic-operations.html" ref="nofollow noopener noreferrer">传送门</a></li>
</ol>
<h2 data-id="heading-2">3. GitFlow 协同工作流</h2>
<p>其实GitFlow并非什么技术，而是一种代码开发合并管理流程的思维模式或者是管理方法。大家一起开发的一种软约定。</p>
<h3 data-id="heading-3">3.1 GitFlow的由来</h3>
<p>我们为什么需要GitFlow这种git管理流程？原因有以下几点</p>
<ol>
<li>有一个稳定版本的代码分支，可以安心的用在线上发布。</li>
<li>在代码提测前或者说是代码达到预发状态时，在测试交付的过程中程序员们还可以继续进行下一个版本的开发工作（挤出每一秒去开发-_-''）。</li>
<li>有个一个分支可以让我们及时的对线上的bug进行修复，这个过程中我们不希望将正在开发中的代码提交到线上生产中去。</li>
</ol>
<p>由于上述开发过程中面临的需求，GitFlow协同国祚流应运而生。对应的点就是</p>
<ol>
<li>代码共享</li>
<li>不同环境下代码互不干扰</li>
<li>管理好代码与环境的一致性</li>
</ol>
<h3 data-id="heading-4">3.1 GitFlow中分支角色们</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761cdc2b87dd4da3b99132d94212c9f3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>Master 分支： 稳定版本代码分支，用作发布环境，上面的每次提交都是可以发布的。</li>
<li>Feture 分支： 功能分支，用于开发功能（需求），用于开发环境</li>
<li>Developer 分支: 开发分支， 一旦Feture分支内功能开发完成就将Feture中的代码合并到Developer分支中，合并完成后，删除该功能分支。这个分支对应的是集成测试环境。</li>
<li>Release 分支：预发分支，做发布前的准备工作，对应的是预发环境。这个分支可以确保们开发继续向前，不会因为要发布不而被停滞住。一旦Release分支达到了可发布的状态，我们需要把Release分支同时向Master，Developer分支上合并，保持代码的一致性，然后把Release分支删除。</li>
<li>Hotfix 分支： 线上bug修缮用的分支，每次修改线上代码的bug时都要用hotfix来维护，完成后向Developer和Master同时合并。完成后删除分支。</li>
</ol>
<p>以上就是GitFlow中所有角色分支，从中我们可以看到以下几点：</p>
<ol>
<li>Master和Developer需要我们长期维护，也是我们开发的主干线。</li>
<li>其中relesase和hotfix两个分支的操作会很零碎，操作起来会比较麻烦，在这个过程中很容易产生失误，导致代码不一致。所以我们需要一个号的工具或者脚本来完成此步骤。</li>
<li>这个套流程虽然麻烦，但是他可以应用到几乎所有的开发流程中：瀑布型，敏捷性（waterfall，agile）</li>
</ol>
<h3 data-id="heading-5">3.2 GitFlow的优点</h3>
<ol>
<li>适应场景多</li>
<li>不影响开发进度</li>
<li>分支使用相对有条理</li>
<li>确保线上的版本稳定</li>
</ol>
<h3 data-id="heading-6">3.3 GitFlow的缺点</h3>
<p>当然GitFlow并不是完美的，这只是种管理思维，一下是他的一些缺点：</p>
<ol>
<li>因为分支态度，所以会出现git log混乱的局面：主要是因为git-flow使用git merge --no-ff来合并分支，在git-flow这种多分支的环境下会让整个项目的log变的非常混乱。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7625b39030f14b48a20ebbc55e543825~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
对于整个中情况我们可以：只有feature合并到developer分支时， 使用-no-ff参数，其他的合并都不使用--no-ff
** <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fq%2F1010000002477106" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/q/1010000002477106" ref="nofollow noopener noreferrer">什么是 git merge --no-ff</a>：</p>
<pre><code class="copyable">--no-ff指的是强行关闭fast-forward方式。
fast-forward方式就是当条件允许的时候，git直接把HEAD指针指向合并分支的头，完成合并。属于“快进方式”，
不这种情况如果删除分支，则会丢失分支信息。因为在这个过程中没有创建commit
  
git merge --squash 是用来把一些不必要commit进行压缩，比如说，你的feature在开发的时候写的commit很乱，
那么我们合并的时候不希望把这些历史commit带过来，于是使用--squash进行合并，此时文件已经同合并后一样了,
但不移动HEAD，不提交。需要进行一次额外的commit来“总结”一下，然后完成最终的合并。

总结：
--no-ff：不使用fast-forward方式合并，保留分支的commit历史
--squash：使用squash方式合并，把多次分支commit历史压缩为一次
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>同时维护Master和Developer两个分支很多时候是没必要的，因为在很多场景下Master中的内容和Developer中的内容是差不多的。尤其当你想回滚某些人的提交时，你就会发现这事似乎有点儿不好干了。而且在工作过程中，你会来来回回地切换工作的分支，有时候一不小心没有切换，就提交到了不正确的分支上，你还要回滚和重新提交，等等。</li>
</ol>
<h2 data-id="heading-7">总结</h2>
<p>这么看下来GitFlow还是不错的，毕竟他的应用场景比较全面，确实解决了开发时分支混乱的问题，而且为我们提供了代码分支管理的策略和思维。但是它也并不是完美的。我感觉像这种分支管理的规范只是万千分支管理策略中的一种，我们完全可以自己去对它进行修改和调整找到适合自己团队的管理策略。在找寻自己策略时我们可以参考一下几点：</p>
<ol>
<li>
<p>不同团队保持并行开发</p>
</li>
<li>
<p>软件版本和代码的一致性</p>
</li>
<li>
<p>环境和代码的一致性</p>
</li>
<li>
<p>保证线上有个稳定的代码源</p>
</li>
<li>
<p>结合DevOps为主的开发流程（这个才是根本，才是未来）</p>
</li>
</ol>
<p>下面提供其他的一些策略，有兴趣的小伙伴可以自行查阅：
6. GitHub Flow
7. GitLab Flow</p></div>  
</div>
            