
---
title: '图解Git原理与日常实用指南'
categories: 
    - 编程
    - Dockone - 周报
author: Dockone - 周报
comments: false
date: 2021-03-22 03:42:44
thumbnail: 'http://dockone.io/uploads/article/20210318/56164b55297e0462c51d09ff0019c2af.png'
---

<div>   
<br><h3>缘起</h3>读了“扔物线”老师的小册《Git原理详解及实用指南》感觉收获良多，于是想写点东西做一个总结，即加深自己的印象也希望能给社区小伙伴一点帮助，写的不对的地方还请多多指导。身为一个初入前端半年的菜鸟，由伊始的只知道Git是用来托管代码的工具到逐步了解中央版本控制系统与分布式版本控制系统（Git）的原理与区别；从之前只会基本的add、commit、pull、push操作到使用stash、merge、reset方便得不亦乐乎，都得益于对Git原理的深入理解。<br>
<h3>从了解版本控制系统开始</h3>所谓版本控制，就是在文件修改的历程中保留修改历史，可以方便的撤销（如同文本编辑的撤销操作一般，只是版本控制会复杂的多）之前对文件的修改。一个版本控制系统的三个核心内容：版本控制（最基本的功能），主动提交（commit历史）和远程仓库（协同开发）。<br>
<h4>中央式版本控制系统（VCS）</h4>工作模型：<br>
<ul><li>主工程师搭好项目框架</li><li>在公司服务器创建一个远程仓库，并提交代码</li><li>其他人拉取代码，并行开发</li><li>每个人独立负责一个功能，开发完成提交代码</li><li>其他人随时拉取代码，保持同步</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/56164b55297e0462c51d09ff0019c2af.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/56164b55297e0462c51d09ff0019c2af.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>分布式版本控制系统（DVCS）</h4>分布式与中央式的区别主要在于，分布式除了远程仓库之外团队中每一个成员的机器上都有一份本地仓库，每个人在自己的机器上就可以进行提交代码，查看版本，切换分支等操作而不需要完全依赖网络环境。<br>
<br>工作模型：<br>
<ul><li>主工程师搭好项目框架 ，并提交代码到本地仓库</li><li>在公司服务器创建一个远程仓库，并将1的提交推送到远程仓库</li><li>其他人把远程仓库所有内容克隆到本地，拥有了各自的本地仓库，开始并行开发</li><li>每个人独立负责一个功能，可以把每一个小改动提交到本地（由于本地提交无需立即上传到远程仓库，所以每一步提交不必是一个完整功能，而可以是功能中的一个步骤或块）</li><li>功能开发完毕，将和这个功能相关的所有提交从本地推送到远程仓库</li><li>每次当有人把新的提交推送到远程仓库的时候，其他人就可以选择把这些提交同步到自己的机器上，并把它们和自己的本地代码合并</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/4c7e18682c4e1837caae54716c805569.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/4c7e18682c4e1837caae54716c805569.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
分布式版本管理系统的优缺点：<br>
<ul><li><br>优点：<br>
<ul><li>大多数操作本地进行，数度更快，不受网络与物理位置限制，不联网也可以提交代码、查看历史、切换分支等等</li><li>分布提交代码，提交更细利于review</li></ul></li><li><br>缺点：<br>
<ul><li>初次clone时间较长</li><li>本地占用存储高于中央式系统</li></ul></li></ul><br>
<br><h3>继续深入Git原理</h3>假设你已经安装好了Git并将代码clone到了本地，新手移步：<a href="https://blog.csdn.net/qq_36955622/article/details/72919314" rel="nofollow" target="_blank">https://blog.csdn.net/qq_36955 ... 19314</a><br>
<h4>Git最基本的工作模型</h4>首先理解三个基本概念：<br>
<ul><li>工作区：就是你在电脑里能看到的目录</li><li>版本库：工作区有一个隐藏目录.git，这个不算工作区，而是Git的本地版本库，你的所有版本信息都会存在这里</li><li>暂存区：英文叫stage或index。一般存放在“.git目录”下的index文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/9d7046daefd7aabd26473aa0fcf5c1be.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/9d7046daefd7aabd26473aa0fcf5c1be.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
工作模型：<br>
<br>首先新建一个test.txt文件并对其进行修改，通过status可以查看工作目录当前状态，此时test.txt对Git来说是不存在的（Untracked）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/ee7234c6a847df9da950ac35f9eeb1e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/ee7234c6a847df9da950ac35f9eeb1e7.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后通过add命令将修改放入暂存区（Git开始追踪它）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/397e9e57817fe2b73bc06ed6eb9d2b8e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/397e9e57817fe2b73bc06ed6eb9d2b8e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，test.txt 的文字变成了绿色，它的前面多了「new file:」的标记，而它的描述也从“Untracked files”变成了“Changes to be commited”。这些都说明一点：test.txt 这个文件的状态从“untracked”（未跟踪）变成了“staged”（已暂存），意思是这个文件中被改动的部分（也就是这整个文件）被记录进了 staging area（暂存区）。<br>
<br><blockquote><br>stage 这个词在 Git 里，是「集中收集改动以待提交」的意思；而 staging area ，就是一个「汇集待提交的文件改动的地方」。简称「暂存」和「暂存区」。至于 staged 表示「已暂存」，就不用再解释了吧？</blockquote>现在文件已经放入暂存区，可以用commit命令提交：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/6b3d8d61e7cabe71e9c4e59b0ebcf439.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/6b3d8d61e7cabe71e9c4e59b0ebcf439.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在这里你也可以直接commit提交会进入commit信息编辑页面，而加上-m参数可以快捷输入简短的提交备注信息，这样你就完成了一次提交（可以通过git log查看提交历史）。<br>
<br>接着对该文件再次进行修改，输入git status可以看到，该文件 又变红了，不过这次它左边的文字不是“New file:”而是“modified:”，而且上方显示它的状态也不是“Untracked”而是“not staged for commit”，意思很明确：Git 已经认识这个文件了，它不是个新文件，但它有了一些改动。所以虽然状态的显示有点不同，但处理方式还是一样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/57e3a33db00b6cc2e123292c502e3ab4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/57e3a33db00b6cc2e123292c502e3ab4.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
接下来再次将该文件add、commit，查看log可以看到已经存在两条提交记录：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/e339671994f0e7a20ea6a025430645c5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/e339671994f0e7a20ea6a025430645c5.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最后通过push把本地的所有commit上传到远程仓库：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/499cb220376c09602a4f537e81bbd932.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/499cb220376c09602a4f537e81bbd932.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>团队工作基本模型</h4>工作模型：<br>
<br>在上面基本操作的基础上，同事commit代码到他的本地，并push到远程仓库。<br>
<br>你把远程仓库新的提交通过pull指令拉取到你的本地。<br>
<br>通过这个流程，你和同事就可以简单地合作了：你写了代码，commit，push到远程仓库，然后他pull到他的本地；他再写代码，commit，push到远程仓库，然后你再pull到你的本地。你来我往，配合得不亦乐乎。（但是有时候push会失败）<br>
<br>为什么会失败？<br>
<br>因为Git的push其实是用本地仓库的commit记录去覆盖远程仓库的commit记录（注：这是简化概念后的说法，push的实质和这个说法略有不同），而如果在远程仓库含有本地没有的commit的时候，push（如果成功）将会导致远端的commit被擦掉。这种结果当然是不可行的，因此Git会在push的时候进行检查，如果出现这样的情况，push就会失败<br>
这时只需要先通过git pull（实为fetch和merge的组合操作）将本地仓库的提交和远程仓库的提交进行合并，然后再push就可以了。<br>
<h4>Feature Branching：最流行的工作流</h4>核心：<br>
<ul><li>任何新的功能（feature）或bug修复全都新建一个branch来写；</li><li>branch写完后，合并到master，然后删掉这个branch（可使用git origin -d分支名删除远程仓库的分支）。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/4b5017e4097fa4af1e16de3ae6f42b68.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/4b5017e4097fa4af1e16de3ae6f42b68.gif" class="img-polaroid" title="10.gif" alt="10.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
优势：<br>
<ul><li>代码分享：写完之后可以在开发分支review之后再merge到master分支</li><li>一人多任务：当正在开发接到更重要的新任务时，你只要稍微把目前未提交的代码简单收尾一下，然后做一个带有「未完成」标记的提交（例如，在提交信息里标上「TODO」），然后回到master去创建一个新的branch进行开发就好了。</li></ul><br>
<br><h3>HEAD、branch、引用的本质以及push的本质</h3><h4>HEAD：当前commit的引用</h4>当前commit在哪里，HEAD就在哪里，这是一个永远自动指向当前commit的引用，所以你永远可以用HEAD来操作当前commit。<br>
<h4>branch</h4>HEAD是Git中一个独特的引用，它是唯一的。而除了HEAD之外，Git还有一种引用，叫做branch（分支）。HEAD除了可以指向commit，还可以指向一个branch，当指向一个branch时，HEAD会通过branch间接指向当前commit，HEAD移动会带着branch一起移动：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/f8c857d090e43a009f409b7221ade31b.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/f8c857d090e43a009f409b7221ade31b.gif" class="img-polaroid" title="11.gif" alt="11.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
branch包含了从初始commit到它的所有路径，而不是一条路径。并且，这些路径之间也是彼此平等的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/efa70122a0a3a6b9b5ac60542bc76204.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/efa70122a0a3a6b9b5ac60542bc76204.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
像上图这样，master在合并了branch1之后，从初始commit到master有了两条路径。这时，master的串就包含了1 2 3 4 7和1 2 5 6 7这两条路径。而且，这两条路径是平等的，1 2 3 4 7这条路径并不会因为它是「原生路径」而拥有任何的特别之处。<br>
<br>创建branch：git branch名称<br>
<br>切换branch：git checkout名称（将HEAD指向该branch）<br>
<br>创建+切换：git checkout -b名称<br>
<br>在切换到新的branch后，再次commit时HEAD就会带着新的branch移动了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/0945464b402874b079d311c0fd55d54c.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/0945464b402874b079d311c0fd55d54c.gif" class="img-polaroid" title="13.gif" alt="13.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
而这个时候，如果你再切换到master去commit，就会真正地出现分叉了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/84f225af15f53043acc3381780de90e2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/84f225af15f53043acc3381780de90e2.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
删除branch：git branch -d名称<br>
<br>注意：<br>
<ul><li>HEAD指向的branch不能删除。如果要删除HEAD指向的branch，需要先用checkout把HEAD指向其他地方。</li><li>由于Git中的branch只是一个引用，所以删除branch的操作也只会删掉这个引用，并不会删除任何的commit。（不过如果一个commit不在任何一个branch的「路径」上，或者换句话说，如果没有任何一个branch可以回溯到这条commit（也许可以称为野生commit？），那么在一定时间后，它会被Git的回收机制删除掉）</li><li>出于安全考虑，没有被合并到master过的branch在删除时会失败（怕误删未完成branch）把-d换成-D可以强制删除</li></ul><br>
<br><h4>引用的本质</h4>所谓引用，其实就是一个个的字符串。这个字符串可以是一个commit的SHA-1码（例：c08de9a4d8771144cd23986f9f76c4ed729e69b0），也可以是一个branch（例：ref: refs/heads/feature3）。<br>
<br>Git中的HEAD和每一个branch以及其他的引用，都是以文本文件的形式存储在本地仓库.git目录中，而Git在工作的时候，就是通过这些文本文件的内容来判断这些所谓的「引用」是指向谁的。<br>
<h4>push的本质：把branch上传到远程仓库</h4><ul><li>把当前branch位置上传到远程仓库，并把它路径上的commits一并上传</li><li>git中（2.0及以后版本），git push不加参数只能上传到从远程仓库clone或者pull下来的分支，如需push在本地创建的分支则需使用git push origin 分支名的命令</li><li>远端仓库的HEAD并不随push与本地一致，远端仓库HEAD永远指向默认分支（master），并随之移动（可以使用git br -r查看远程分支的HEAD指向）。</li></ul><br>
<br><h3>开启Git操作之旅</h3><h3>merge：合并</h3>含义：从目标commit和当前commit（即HEAD所指向的commit）分叉的位置起，把目标commit的路径上的所有commit的内容一并应用到当前commit，然后自动生成一个新的commit。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/af2cfd945f151c524813dd3825f5735f.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/af2cfd945f151c524813dd3825f5735f.gif" class="img-polaroid" title="15.gif" alt="15.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
当执行git merge branch1操作，Git会把5和6这两个commit的内容一并应用到4上，然后生成一个新的提交7 。<br>
<br>merge的特殊情况：<br>
<br>merge冲突：你的两个分支改了相同的内容，Git不知道应该以哪个为准。如果在merge的时候发生了这种情况，Git就会把问题交给你来决定。具体地，它会告诉你merge失败，以及失败的原因；这时候你只需要手动解决掉冲突并重新add、commit（改动不同文件或同一文件的不同行都不会产生冲突）；或者使用git merge --abort放弃解决冲突，取消merge。<br>
<br>HEAD领先于目标commit：merge是一个空操作：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/d2b8b36a5a853801dd2bed7c1accbf97.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/d2b8b36a5a853801dd2bed7c1accbf97.jpg" class="img-polaroid" title="16.jpg" alt="16.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
此时merge不会有任何反应。<br>
<br>HEAD落后于目标commit且不存在分支（fast-forward）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/da6252ebfa0290085362984c193f92e8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/da6252ebfa0290085362984c193f92e8.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Git会直接把HEAD与其指向的branch（如果有的话）一起移动到目标commit。<br>
<h4>rebase：给commit序列重新设置基础点</h4>有些人不喜欢merge，因为在merge之后，commit历史就会出现分叉，这种分叉再汇合的结构会让有些人觉得混乱而难以管理。如果你不希望commit历史出现分叉，可以用rebase来代替merge。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/bdf7afe21bb33285ea23249adf3ab0e0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/bdf7afe21bb33285ea23249adf3ab0e0.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看出，通过rebase，5和6两条commits把基础点从2换成了4 。通过这样的方式，就让本来分叉了的提交历史重新回到了一条线。这种「重新设置基础点」的操作，就是rebase的含义。另外，在rebase之后，记得切回master再merge一下，把master移到最新的commit。<br>
<br>为什么要从branch1来rebase，然后再切回master再merge一下这么麻烦，而不是直接在master上执行rebase？<br>
<br>从图中可以看出，rebase后的每个commit虽然内容和rebase之前相同，但它们已经是不同的commit了（每个commit有唯一标志）。如果直接从master执行rebase的话，就会是下面这样：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/53733117a64d41d9b0064c6f65631f59.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/53733117a64d41d9b0064c6f65631f59.gif" class="img-polaroid" title="19.gif" alt="19.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
这就导致master上之前的两个最新commit（3和4）被剔除了。如果这两个commit之前已经在远程仓库存在，这就会导致没法push：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/ab54102f00038df1412fde678a0c4157.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/ab54102f00038df1412fde678a0c4157.jpg" class="img-polaroid" title="20.jpg" alt="20.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
所以，为了避免和远程仓库发生冲突，一般不要从master向其他branch执行rebase操作。而如果是master以外的branch之间的rebase（比如 branch1和branch2之间），就不必这么多费一步，直接rebase就好。<br>
需要说明的是，rebase是站在需要被rebase的commit上进行操作，这点和merge是不同的。<br>
<h4>stash：临时存放工作目录的改动</h4>stash指令可以帮你把工作目录的内容全部放在你本地的一个独立的地方，它不会被提交，也不会被删除，你把东西放起来之后就可以去做你的临时工作了，做完以后再来取走，就可以继续之前手头的事了。<br>
<br>操作步骤：<br>
<ul><li>git stash可以加上save参数后面带备注信息（git stash save '备注信息'）</li><li>此时工作目录已经清空，可以切换到其他分支干其他事情了</li><li>git stash pop弹出第一个stash（该stash从历史stash中移除）；或者使用git stash apply达到相同的效果（该stash仍存在stash list中），同时可以使用git stash list查看stash历史记录并在apply后面加上指定的stash返回到该stash。</li></ul><br>
<br>注意：没有被track的文件会被Git忽略而不被stash，如果想一起stash，加上-u参数。<br>
<h4>reflog：引用记录的log</h4>可以查看Git的引用记录，不指定参数，默认显示HEAD的引用记录；如果不小心把分支删掉了，可以使用该命令查看引用记录，然后使用checkout切到该记录处重建分支即可。<br>
<br>注意：不再被引用直接或间接指向的commits会在一定时间后被Git回收，所以使用reflog来找回被删除的branch的操作一定要及时，不然有可能会由于commit被回收而再也找不回来。<br>
<h4>看看我都改了什么</h4>log：查看已提交内容：<br>
<ul><li>git log -p可以查看每个commit的改动细节（到改动文件的每一行）</li><li>git log --stat查看简要统计（哪几个文件改动了）</li><li>git show 指定commit 指定文件名查看指定commit的指定文件改动细节</li></ul><br>
<br>diff：查看未提交内容<br>
<ul><li>git diff --staged可以显示暂存区和上一条提交之间的不同。换句话说，这条指令可以让你看到「如果你立即输入git commit，你将会提交什么」</li><li>git diff可以显示工作目录和暂存区之间的不同。换句话说，这条指令可以让你看到「如果你现在把所有文件都add，你会向暂存区中增加哪些内容」</li><li>git diff HEAD可以显示工作目录和上一条提交之间的不同，它是上面这二者的内容相加。换句话说，这条指令可以让你看到「如果你现在把所有文件都add然后git commit，你将会提交什么」（不过需要注意，没有被Git记录在案的文件（即从来没有被add过的文件，untracked files并不会显示出来。因为对Git来说它并不存在）实质上，如果你把HEAD换成别的commit，也可以显示当前工作目录和这条 commit 的区别。<br>
####刚刚提交的代码发现写错了怎么办？<br>
再提一个修复了错误的commit？可以是可以，不过还有一个更加优雅和简单的解决方法：commit --amend。</li></ul><br>
<br>具体做法：<br>
<ul><li>修改好问题</li><li>将修改add到暂存区</li><li>使用git commit --amend提交修改，结果如下图：</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/6ce716151c0259ddb4963cdfa2e4922e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/6ce716151c0259ddb4963cdfa2e4922e.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
减少了一次无谓的commit。<br>
<h4>错误不是最新的提交而是倒数第二个？</h4>使用rebase -i（交互式rebase）：<br>
<br>所谓「交互式 rebase」，就是在rebase的操作执行之前，你可以指定要rebase的commit链中的每一个commit是否需要进一步修改，那么你就可以利用这个特点，进行一次「原地rebase」。<br>
<br>操作过程：<br>
<br>1、git rebase -i HEAD^^<br>
<br>说明：在Git中，有两个「偏移符号」：^ 和 ~。<br>
<br>^的用法：在commit的后面加一个或多个^号，可以把commit往回偏移，偏移的数量是^的数量。例如：master^表示master指向的commit之前的那个commit；HEAD^^表示HEAD所指向的commit往前数两个commit。<br>
<br>~的用法：在commit的后面加上~号和一个数，可以把commit往回偏移，偏移的数量是~号后面的数。例如：HEAD~5表示HEAD指向的commit往前数5个commit。<br>
<br>上面这行代码表示，把当前commit（HEAD所指向的commit）rebase到HEAD之前2个的commit上：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/00b4136e7a1a701bfc42151530a55322.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/00b4136e7a1a701bfc42151530a55322.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
2、进入编辑页面，选择commit对应的操作，commit为正序排列，旧的在上，新的在下，前面黄色的为如何操作该commit，默认pick（直接应用该commit不做任何改变），修改第一个commit为edit（应用这个commit，然后停下来等待继续修正）然后:wq退出编辑页面，此时rebase停在第二个commit的位置，此时可以对内容进行修改：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/47e06accf0a872cafe7e5f1b5fb1fead.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/47e06accf0a872cafe7e5f1b5fb1fead.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/be723e14d69ddfc957cac843cfb0d813.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/be723e14d69ddfc957cac843cfb0d813.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
3、修改完后使用add，commit --amend将修改提交<br>
<br>4、git rebase --continue继续rebase过程，把后面的commit直接应用上去，这次交互式rebase的过程就完美结束了，你的那个倒数第二个写错的commit就也被修正了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/49f3ffa5d6b97c64cdaed4bbd5e719a9.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/49f3ffa5d6b97c64cdaed4bbd5e719a9.gif" class="img-polaroid" title="25.gif" alt="25.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>想直接丢弃某次提交？</h4><strong>reset --hard丢弃最新的提交</strong><br>
<br>git reset --hard HEAD^<br>
<br>HEAD^表示HEAD往回数一个位置的commit，上节刚说过，记得吧？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/0fb26c3763c74b9b1995a67e1fb84d3c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/0fb26c3763c74b9b1995a67e1fb84d3c.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>用交互式 rebase 撤销历史提交</strong><br>
<br>操作步骤与修改历史提交类似，第二步把需要撤销的commit修改为drop，其他步骤不再赘述。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/64d2218ddb32580eb278201499e1bf0c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/64d2218ddb32580eb278201499e1bf0c.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>用rebase --onto撤销提交</strong><br>
<br>git rebase --onto HEAD^^ HEAD^ branch1<br>
<br>上面这行代码的意思是：以倒数第二个commit为起点（起点不包含在rebase序列里），branch1为终点，rebase到倒数第三个commit上。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/2864d85c2e7b36888adb6c72ed79434b.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/2864d85c2e7b36888adb6c72ed79434b.gif" class="img-polaroid" title="28.gif" alt="28.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>错误代码已经push？</h4>有的时候，代码push到了远程仓库，才发现有个commit写错了。这种问题的处理分两种情况：<br>
<br><strong>出错内容在自己的分支</strong><br>
<br>假如是某个你自己独立开发的branch出错了，不会影响到其他人，那没关系用前面几节讲的方法把写错的commit修改或者删除掉，然后再push上去就好了。但是此时会push报错，因为远程仓库包含本地没有的commits（在本地已经被替换或被删除了），此时直接使用git push origin分支名-f强制push。<br>
<br><strong>问题内容已合并到master</strong><br>
<ul><li>增加新提交覆盖之前内容</li><li>使用git revert指定commit</li></ul><br>
<br>它的用法很简单，你希望撤销哪个commit，就把它填在后面。如：git revert HEAD^<br>
<br>上面这行代码就会增加一条新的commit，它的内容和倒数第二个commit是相反的，从而和倒数第二个commit相互抵消，达到撤销的效果。在revert完成之后，把新的commit再push上去，这个commit的内容就被撤销了。它和前面所介绍的撤销方式相比，最主要的区别是，这次改动只是被「反转」了，并没有在历史中消失掉，你的历史中会存在两条commit：一个原始commit，一个对它的反转commit。<br>
<h4>reset：不止可以撤销提交</h4>git reset --hard指定commit你的工作目录里的内容会被完全重置为和指定commit位置相同的内容。换句话说，就是你的未提交的修改会被全部擦掉。<br>
<br>git reset --soft指定commit会在重置HEAD和branch时，保留工作目录和暂存区中的内容，并把重置HEAD所带来的新的差异放进暂存区。<br>
<br>什么是「重置HEAD所带来的新的差异」？就是这里：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/b8c73f0d85ceaa67a1546c5a2f3ef7ea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/b8c73f0d85ceaa67a1546c5a2f3ef7ea.png" class="img-polaroid" title="29.png" alt="29.png" referrerpolicy="no-referrer"></a>
</div>
<br>
git reset --mixed（或者不加参数）指定commit保留工作目录，并且清空暂存区。也就是说，工作目录的修改、暂存区的内容以及由reset所导致的新的文件差异，都会被放进工作区。简而言之，就是「把所有差异都混合（mixed）放在工作区中」。<br>
<h4>checkout：签出指定commit</h4>checkout的本质是签出指定的commit，不止可以切换branch还可以指定commit作为参数，把HEAD移动到指定的commit上；与reset的区别在于只移动HEAD不改变绑定的branch；git checkout --detach可以把HEAD和branch脱离，直接指向当前commit。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210318/0681858cb1a1cc3d30e8258db6001f6b.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210318/0681858cb1a1cc3d30e8258db6001f6b.gif" class="img-polaroid" title="30.gif" alt="30.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>最后</h3>希望我的总结能给大家带来些许帮助，也希望和大家一起学以致用，一起成长。<br>
<br>原文链接：<a href="https://segmentfault.com/a/1190000018272902" rel="nofollow" target="_blank">https://segmentfault.com/a/1190000018272902</a>，作者：李某人
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            