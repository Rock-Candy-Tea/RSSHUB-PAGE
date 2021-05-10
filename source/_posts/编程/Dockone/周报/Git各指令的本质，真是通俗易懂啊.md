
---
title: 'Git各指令的本质，真是通俗易懂啊'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/dbccfa9b4aa37f3fcdc1fe3cd376002f.jpg'
author: Dockone
comments: false
date: 2021-05-10 12:02:42
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/dbccfa9b4aa37f3fcdc1fe3cd376002f.jpg'
---

<div>   
<br>作为当前世界上最强大的代码管理工具<code class="prettyprint">Git</code>相信大家都很熟悉，但据我所知有很大一批人停留在<code class="prettyprint">clone、commit、pull、push……</code>的阶段，是不是对<code class="prettyprint">rebase</code>心里没底只敢用<code class="prettyprint">merge</code>？碰见版本回退就抓瞎？别问我怎么知道的，问就是：<code class="prettyprint">“我曾经就是这样啊～～”</code>。针对这些问题，今天我就将这几年对<code class="prettyprint">Git</code>的认知和理解分享出来，尽可能的从本质去讲解<code class="prettyprint">Git</code>，帮助你一步一步去了解<code class="prettyprint">Git</code>的底层原理，相信读完本篇文章你便可以换种姿态，更加风骚得使用<code class="prettyprint">Git</code>各种指令。<br>
<h3>基本概念</h3><h4>Git的优势</h4><code class="prettyprint">Git</code>是一个<code class="prettyprint">分布式</code>代码管理工具，在讨论分布式之前避免不了提及一下什么是<code class="prettyprint">中央式</code>代码管理仓库：<br>
<ul><li>中央式：所有的代码保存在中央服务器，所以提交必须依赖网络，并且每次提交都会带入到中央仓库，如果是协同开发可能频繁触发代码合并，进而增加提交的成本和代价。最典型的就是SVN。</li><li>分布式：可以在本地提交，不需要依赖网络，并且会将每次提交自动备份到本地。每个开发者都可以把远程仓库clone一份到本地，并会把提交历史一并拿过来。代表就是Git。</li></ul><br>
<br>那<code class="prettyprint">Git</code>相比于<code class="prettyprint">SVN</code>有什么优势呢？打个比方：“巴拉巴拉写了一大堆代码，突然发现写的有问题，我想回到一个小时之前”，对于这种情况<code class="prettyprint">Git</code>的优势就很明显了，因为commit的成本比较小并且本地会保存所有的提交记录，随时随刻可以进行回退。在这并不是说<code class="prettyprint">SVN</code>的不能完成这种操作，只是<code class="prettyprint">Git</code>的回退会显得更加的优雅。<code class="prettyprint">Git</code>相比于<code class="prettyprint">中央式</code>工具还有很多优点，就不一一列举了，感兴趣的可自行了解。<br>
<h4>文件状态</h4>在Git中文件大概分为三种状态：<code class="prettyprint">已修改（modified）、已暂存（staged）、已提交（committed）</code><br>
<ul><li>修改：Git可以感知到工作目录中哪些文件被修改了，然后把修改的文件加入到modified区域</li><li>暂存：通过add命令将工作目录中修改的文件提交到暂存区，等候被commit</li><li>提交：将暂存区文件commit至Git目录中永久保存</li></ul><br>
<br><h4>commit节点</h4>为了便于表述，本篇文章我会通过<code class="prettyprint">节点</code>代称<code class="prettyprint">commit提交</code>。<br>
<br>在Git中每次提交都会生成一个<code class="prettyprint">节点</code>，而每个节点都会有一个哈希值作为唯一标示，多次提交会形成一个<code class="prettyprint">线性</code>节点链（不考虑merge的情况），如图1。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210509/dbccfa9b4aa37f3fcdc1fe3cd376002f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/dbccfa9b4aa37f3fcdc1fe3cd376002f.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1</em><br>
<br>节点上方是通过SHA1计算的哈希值。<br>
<br><code class="prettyprint">C2</code>节点包含<code class="prettyprint">C1</code>提交内容,同样<code class="prettyprint">C3</code>节点包含<code class="prettyprint">C1、C2</code>提交内容。<br>
<h4>HEAD</h4><code class="prettyprint">HEAD</code>是Git中非常重要的一个概念，你可以称它为<code class="prettyprint">指针</code>或者<code class="prettyprint">引用</code>，它可以指向任意一个<code class="prettyprint">节点</code>，并且指向的节点始终为当前工作目录，换句话说就是当前工作目录(也就是你所看到的代码)就是<code class="prettyprint">HEAD</code>指向的节点。<br>
<br>还以图1举例，如果<code class="prettyprint">HEAD</code>指向<code class="prettyprint">C2</code>那工作目录对应的就是<code class="prettyprint">C2</code>节点。具体如何移动<code class="prettyprint">HEAD</code>指向后面会讲到，此处不要纠结。<br>
<br>同时<code class="prettyprint">HEAD</code>也可以指向一个<code class="prettyprint">分支</code>，间接指向<code class="prettyprint">分支</code>所指向的<code class="prettyprint">节点</code><br>
<h4>远程仓库</h4>虽然Git会把代码以及历史保存在本地，但最终还是要提交到服务器上的远程仓库。通过<code class="prettyprint">clone</code>命令可以把远程仓库的代码下载到本地，同时也会将<code class="prettyprint">提交历史</code>、<code class="prettyprint">分支</code>、<code class="prettyprint">HEAD</code>等状态一并同步到本地，但这些状态并不会实时更新，需要手动从远程仓库去拉取，至于何时拉、怎么拉后面章节会讲到。<br>
<br>通过远程仓库为中介，你可以和你的同事进行协同开发，开发完新功能后可以申请提交至远程仓库，同时也可以从远程仓库拉取你同事的代码。<br>
<br>注意点：因为你和你的同事都会以远程仓库的代码为基准，所以要时刻保证远程仓库的代码质量，切记不要将未经检验测试的代码提交至远程仓库。<br>
<h3>分支</h3><h4>什么是分支？</h4><code class="prettyprint">分支</code>也是Git中相当重要的一个概念，当一个<code class="prettyprint">分支</code>指向一个<code class="prettyprint">节点</code>时，当前<code class="prettyprint">节点</code>的内容即是该<code class="prettyprint">分支</code>的内容，它的概念和<code class="prettyprint">HEAD</code>非常接近同样也可以视为<code class="prettyprint">指针</code>或<code class="prettyprint">引用</code>，不同的是<code class="prettyprint">分支</code>可以存在多个，而<code class="prettyprint">HEAD</code>只有一个。通常会根据<code class="prettyprint">功能</code>或<code class="prettyprint">版本</code>建立不同的分支。<br>
<br>那分支有什么用呢？<br>
<br>举个例子：你们的App经历了千辛万苦终于发布了<code class="prettyprint">v1.0</code>版本，由于需求紧急<code class="prettyprint">v1.0</code>上线之后便马不停蹄的开始<code class="prettyprint">v1.1</code>，正当你开发的兴起时，QA同学说用户反馈了一些bug，需要修复然后重新发版，修复<code class="prettyprint">v1.0</code>肯定要基于<code class="prettyprint">v1.0</code>的代码，可是你已经开发了一部分<code class="prettyprint">v1.1</code>了，此时怎么搞？<br>
<br>面对上面的问题通过引入<code class="prettyprint">分支</code>概念便可优雅的解决，如图2：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210509/814f11b4f222e911041c6a77afec6d25.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/814f11b4f222e911041c6a77afec6d25.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2</em><br>
<ul><li>先看左边示意图，假设<code class="prettyprint">C2</code>节点既是<code class="prettyprint">v1.0</code>版本代码，上线后在<code class="prettyprint">C2</code>的基础上新建一个分支<code class="prettyprint">ft-1.0</code></li><li>再看右边示意图，在<code class="prettyprint">v1.0</code>上线后可在<code class="prettyprint">master</code>分支开发<code class="prettyprint">v1.1</code>内容，收到QA同学反馈后提交<code class="prettyprint">v1.1</code>代码生成节点<code class="prettyprint">C3</code>，随后切换到<code class="prettyprint">ft-1.0</code>分支做bug修复，修复完成后提交代码生成节点<code class="prettyprint">C4</code>，然后再切换到<code class="prettyprint">master</code>分支并合并<code class="prettyprint">ft-1.0</code>分支，到此我们就解决了上面提出的问题</li></ul><br>
<br>除此之外利用分支还可以做很多事情，比如现在有一个需求不确定要不要上线，但是得先做，此时可以单独创建一个分支开发该功能，等到啥时候需要上线直接合并到主分支即可。分支适用的场景很多就不一一列举了。<br>
<br>注意点：当在某个节点创建一个分支后，并不会把该节点对应的代码复制一份出来，只是将新分支指向该节点，因此可以很大程度减少空间上的开销。一定要记着不管是<code class="prettyprint">HEAD</code>还是<code class="prettyprint">分支</code>它们都只是引用而已，量级非常轻。<br>
<h3>命令详解</h3><h4>提交相关</h4>前面我们提到过，想要对代码进行提交必须得先加入到暂存区，Git中是通过命令 <code class="prettyprint">add</code> 实现。<br>
<br>添加某个文件到暂存区：<br>
<pre class="prettyprint">git add 文件路径<br>
</pre><br>
添加所有文件到暂存区：<br>
<pre class="prettyprint">git add .<br>
</pre><br>
同时Git也提供了撤销<code class="prettyprint">工作区</code>和<code class="prettyprint">暂存区</code>命令。<br>
<br>撤销工作区改动：<br>
<pre class="prettyprint">git checkout -- 文件名<br>
</pre><br>
清空暂存区：<br>
<pre class="prettyprint">git reset HEAD 文件名<br>
</pre><br>
提交：<br>
<br>将改动文件加入到暂存区后就可以进行提交了，提交后会生成一个新的提交节点，具体命令如下：<br>
<pre class="prettyprint">git commit -m "该节点的描述信息"<br>
</pre><br>
<h4>分支相关</h4>创建分支：<br>
<br>创建一个分支后该分支会与<code class="prettyprint">HEAD</code>指向同一节点，说通俗点就是<code class="prettyprint">HEAD</code>指向哪创建的新分支就指向哪，命令如下：<br>
<pre class="prettyprint">git branch 分支名<br>
</pre><br>
切换分支：<br>
<br>当切换分支后，默认情况下<code class="prettyprint">HEAD</code>会指向当前分支，即<code class="prettyprint">HEAD</code>间接指向当前分支指向的节点。<br>
<pre class="prettyprint">git checkout 分支名<br>
</pre><br>
同时也可以创建一个分支后立即切换，命令如下：<br>
<pre class="prettyprint">git checkout -b 分支名<br>
</pre><br>
删除分支：<br>
<br>为了保证仓库分支的简洁，当某个分支完成了它的使命后应该被删除。比如前面所说的单独开一个分支完成某个功能，当这个功能被合并到主分支后应该将这个分支及时删除。<br>
<br>删除命令如下：<br>
<pre class="prettyprint">git branch -d 分支名<br>
</pre><br>
<h4>合并相关</h4>关于合并的命令是最难掌握同时也是最重要的。我们常用的合并命令大概有三个<code class="prettyprint">merge</code>、<code class="prettyprint">rebase</code>、<code class="prettyprint">cherry-pick</code>。<br>
<br>merge：<br>
<br><code class="prettyprint">merge</code>是最常用的合并命令，它可以将某个分支或者某个节点的代码合并至当前分支。具体命令如下：<br>
<pre class="prettyprint">git merge 分支名/节点哈希值<br>
</pre><br>
如果需要合并的分支完全领先于当前分支，如图3所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210509/192555b85f839832279f459671fc5654.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/192555b85f839832279f459671fc5654.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图3</em><br>
<br>由于分支<code class="prettyprint">ft-1</code>完全领先分支<code class="prettyprint">ft-2</code>即<code class="prettyprint">ft-1</code>完全包含<code class="prettyprint">ft-2</code>，所以<code class="prettyprint">ft-2</code>执行了<code class="prettyprint">“git merge ft-1”</code>后会触发<code class="prettyprint">fast forward(快速合并)</code>，此时两个分支指向同一节点，这是最理想的状态。但是实际开发中我们往往碰到的是下面这种情况：如图4（左）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210509/c1b2a56f1fcd9925f6e8aeb49e78f1d8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/c1b2a56f1fcd9925f6e8aeb49e78f1d8.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4</em><br>
<br>这种情况就不能直接合了，当<code class="prettyprint">ft-2</code>执行了<code class="prettyprint">“git merge ft-1”</code>后Git会将节点<code class="prettyprint">C3</code>、<code class="prettyprint">C4</code>合并随后生成一个新节点<code class="prettyprint">C5</code>，最后将<code class="prettyprint">ft-2</code>指向<code class="prettyprint">C5</code> 如图4（右）。<br>
<br>注意点：如果<code class="prettyprint">C3</code>、<code class="prettyprint">C4</code>同时修改了同一个文件中的同一句代码，这个时候合并会出错，因为Git不知道该以哪个节点为标准，所以这个时候需要我们自己手动合并代码。<br>
<br>rebase：<br>
<br><code class="prettyprint">rebase</code>也是一种合并指令，命令行如下：<br>
<pre class="prettyprint">git rebase 分支名/节点哈希值<br>
</pre><br>
与<code class="prettyprint">merge</code>不同的是<code class="prettyprint">rebase</code>合并看起来不会产生新的节点（实际上是会产生的，只是做了一次复制），而是将需要合并的节点直接累加，如图5。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210509/9c2a83e38242dc21a854d82776b7cc56.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/9c2a83e38242dc21a854d82776b7cc56.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5</em><br>
<br>当左边示意图的<code class="prettyprint">ft-1.0</code>执行了<code class="prettyprint">git rebase master</code>后会将<code class="prettyprint">C4</code>节点复制一份到<code class="prettyprint">C3</code>后面，也就是<code class="prettyprint">C4'</code>，<code class="prettyprint">C4</code>与<code class="prettyprint">C4'</code>相对应，但是哈希值却不一样。<br>
<br><code class="prettyprint">rebase</code>相比于<code class="prettyprint">merge</code>提交历史更加线性、干净，使并行的开发流程看起来像串行，更符合我们的直觉。既然<code class="prettyprint">rebase</code>这么好用是不是可以抛弃<code class="prettyprint">merge</code>了？其实也不是了，下面我罗列一些<code class="prettyprint">merge</code>和<code class="prettyprint">rebase</code>的优缺点：<br>
<br>merge优缺点：<br>
<ul><li>优点：每个节点都是严格按照时间排列。当合并发生冲突时，只需要解决两个分支所指向的节点的冲突即可</li><li>缺点：合并两个分支时大概率会生成新的节点并<code class="prettyprint">分叉</code>，久而久之提交历史会变成一团乱麻</li></ul><br>
<br>rebase优缺点：<br>
<ul><li>优点：会使提交历史看起来更加线性、干净</li><li>缺点：虽然提交看起来像是线性的，但并不是真正的按时间排序，比如图3-3中，不管<code class="prettyprint">C4</code>早于或者晚于<code class="prettyprint">C3</code>提交它最终都会放在<code class="prettyprint">C3</code>后面。并且当合并发生冲突时，理论上来讲有几个节点<code class="prettyprint">rebase</code>到目标分支就可能处理几次冲突</li></ul><br>
<br>对于网络上一些<code class="prettyprint">只用rebase</code>的观点，作者表示不太认同，如果不同分支的合并使用<code class="prettyprint">rebase</code>可能需要重复解决冲突，这样就得不偿失了。但如果是本地推到远程并对应的是同一条分支可以优先考虑<code class="prettyprint">rebase</code>。所以我的观点是 根据不同场景合理搭配使用<code class="prettyprint">merge</code>和<code class="prettyprint">rebase</code>，如果觉得都行那优先使用<code class="prettyprint">rebase</code><br>
<br>cherry-pick：<br>
<br><code class="prettyprint">cherry-pick</code>的合并不同于<code class="prettyprint">merge</code>和<code class="prettyprint">rebase</code>，它可以选择某几个节点进行合并，如图6。<br>
<br>命令行：<br>
<pre class="prettyprint">git cherry-pick 节点哈希值<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210509/a0de71471ba2742d8d44a19b8daae7f3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/a0de71471ba2742d8d44a19b8daae7f3.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6</em><br>
<br>假设当前分支是<code class="prettyprint">master</code>，执行了<code class="prettyprint">git cherry-pick C3(哈希值)，C4(哈希值)</code>命令后会直接将<code class="prettyprint">C3</code>、<code class="prettyprint">C4</code>节点抓过来放在后面，对应<code class="prettyprint">C3'</code>和<code class="prettyprint">C4'</code>。<br>
<br><h4>回退相关</h4>分离HEAD：<br>
<br>在默认情况下HEAD是指向分支的，但也可以将HEAD从分支上取下来直接指向某个节点，此过程就是<code class="prettyprint">分离HEAD</code>，具体命令如下：<br>
<pre class="prettyprint">git checkout 节点哈希值<br>
//也可以直接脱离分支指向当前节点<br>
git checkout --detach<br>
</pre><br>
由于哈希值是一串很长很长的乱码，在实际操作中使用哈希值分离HEAD很麻烦，所以Git也提供了HEAD基于某一特殊位置（分支/HEAD）直接指向<code class="prettyprint">前一个</code>或<code class="prettyprint">前N个</code>节点的命令，也即相对引用，如下：<br>
<pre class="prettyprint">//HEAD分离并指向前一个节点<br>
git checkout 分支名/HEAD^<br>
</pre><br>
<pre class="prettyprint">//HEAD分离并指向前N个节点<br>
git checkout 分支名～N<br>
</pre><br>
将<code class="prettyprint">HEAD分离</code>出来指向节点有什么用呢？举个例子：如果开发过程发现之前的提交有问题，此时可以将HEAD指向对应的节点，修改完毕后再提交，此时你肯定不希望再生成一个新的节点，而你只需在提交时加上<code class="prettyprint">--amend</code>即可，具体命令如下：<br>
<pre class="prettyprint">git commit --amend<br>
</pre><br>
回退：<br>
<br>回退场景在平时开发中还是比较常见的，比如你巴拉巴拉写了一大堆代码然后提交，后面发现写的有问题，于是你想将代码回到前一个提交，这种场景可以通过<code class="prettyprint">reset</code>解决，具体命令如下：<br>
<pre class="prettyprint">//回退N个提交<br>
git reset HEAD~N<br>
</pre><br>
<code class="prettyprint">reset</code>和<code class="prettyprint">相对引用</code>很像，区别是<code class="prettyprint">reset</code>会使<code class="prettyprint">分支</code>和<code class="prettyprint">HEAD</code>一并回退。<br>
<h4>远程相关</h4>当我们接触一个新项目时，第一件事情肯定是要把它的代码拿下来，在Git中可以通过<code class="prettyprint">clone</code>从远程仓库复制一份代码到本地，具体命令如下：<br>
<pre class="prettyprint">git clone 仓库地址<br>
</pre><br>
前面的章节我也有提到过，<code class="prettyprint">clone</code>不仅仅是复制代码，它还会把远程仓库的<code class="prettyprint">引用（分支/HEAD）</code>一并取下保存在本地，如图7所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210509/950455ba60d89ca23cbd10e5f57486f0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210509/950455ba60d89ca23cbd10e5f57486f0.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图7</em><br>
<br>其中<code class="prettyprint">origin/master</code>和<code class="prettyprint">origin/ft-1</code>为远程仓库的分支，而远程的这些引用状态是不会实时更新到本地的，比如远程仓库<code class="prettyprint">origin/master</code>分支增加了一次提交，此时本地是感知不到的，所以本地的<code class="prettyprint">origin/master</code>分支依旧指向<code class="prettyprint">C4</code>节点。我们可以通过<code class="prettyprint">fetch</code>命令来手动更新远程仓库状态。<br>
<br>小提示：并不是存在服务器上的才能称作是远程仓库，你也可以<code class="prettyprint">clone</code>本地仓库作为远程，当然实际开发中我们不可能把本地仓库当作公有仓库，说这个只是单纯的帮助你更清晰的理解<code class="prettyprint">分布式</code>。<br>
<br>fetch：<br>
<br>说的通俗一点，<code class="prettyprint">fetch</code>命令就是一次<code class="prettyprint">下载</code>操作，它会将远程新增加的节点以及<code class="prettyprint">引用(分支/HEAD)</code>的状态下载到本地，具体命令如下：<br>
<pre class="prettyprint">git fetch 远程仓库地址/分支名<br>
</pre><br>
pull：<br>
<br><code class="prettyprint">pull</code>命令可以从远程仓库的某个引用拉取代码，具体命令如下：<br>
<pre class="prettyprint">git pull 远程分支名<br>
</pre><br>
其实<code class="prettyprint">pull</code>的本质就是<code class="prettyprint">fetch</code>+<code class="prettyprint">merge</code>，首先更新远程仓库<code class="prettyprint">所有状态</code>到本地，随后再进行合并。合并完成后本地分支会指向<code class="prettyprint">最新节点</code>。<br>
<br>另外<code class="prettyprint">pull</code>命令也可以通过<code class="prettyprint">rebase</code>进行合并，具体命令如下：<br>
<pre class="prettyprint">git pull --rebase 远程分支名<br>
</pre><br>
push：<br>
<br><code class="prettyprint">push</code>命令可以将本地提交推送至远程，具体命令如下：<br>
<pre class="prettyprint">git push 远程分支名<br>
</pre><br>
如果直接<code class="prettyprint">push</code>可能会失败，因为可能存在冲突，所以在<code class="prettyprint">push</code>之前往往会先<code class="prettyprint">pull</code>一下，如果存在冲突本地解决。<code class="prettyprint">push</code>成功后本地的远程分支引用会更新，与本地分支指向同一节点。<br>
<h3>综上所述</h3><ul><li>不管是<code class="prettyprint">HEAD</code>还是<code class="prettyprint">分支</code>，它们都只是<code class="prettyprint">引用</code>而已，<code class="prettyprint">引用</code>+<code class="prettyprint">节点</code>是 Git 构成分布式的关键</li><li><code class="prettyprint">merge</code>相比于<code class="prettyprint">rebase</code>有更明确的时间历史，而<code class="prettyprint">rebase</code>会使提交更加线性应当优先使用</li><li>通过移动<code class="prettyprint">HEAD</code>可以查看每个提交对应的代码</li><li><code class="prettyprint">clone</code>或<code class="prettyprint">fetch</code>都会将远程仓库的所有<code class="prettyprint">提交</code>、<code class="prettyprint">引用</code>保存在本地一份</li><li><code class="prettyprint">pull</code>的本质其实就是<code class="prettyprint">fetch</code>+<code class="prettyprint">merge</code>，也可以加入<code class="prettyprint">--rebase</code>通过rebase方式合并</li></ul><br>
<br>原文链接：<a href="https://juejin.cn/post/6895246702614806542" rel="nofollow" target="_blank">https://juejin.cn/post/6895246702614806542</a>，作者：Bezier  
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            