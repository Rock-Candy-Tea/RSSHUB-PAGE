
---
title: 'Git学习笔记三'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17e78e0d86ed4dcfa7a0cfbea85477a4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 02:16:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17e78e0d86ed4dcfa7a0cfbea85477a4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>  前两篇Git笔记主要内容是Git的安装以及底层命令，但是在实际开发当中是几乎不涉及底层命令的，因为底层命令记忆麻烦而且容易出错。既然实际开发过程不用底层命令，那为啥还要学习呢？emmmm好问题，底层命令可以说是Git的灵魂高层命令是Git的身躯，单纯学Git的高层命令那是没有灵魂de~不是有一首歌的歌词是“得到你的人却得不到你的心，就是得到全世界也不开心~~~~”,Git也是如此的耶！既然我们已经有了Git的灵魂，那么我们是时候开始获得Git的身躯了。</p>
<h2 data-id="heading-1">一、高层命令</h2>
<h3 data-id="heading-2"><strong>初始化仓库</strong></h3>
<ul>
<li><strong>git init</strong></li>
</ul>
<p>这个命令在前面已经使用过，就是用来初始化Git仓库的。</p>
<h3 data-id="heading-3"><strong>将修改添加进暂存区</strong></h3>
<ul>
<li><strong>git add 文件路径</strong></li>
</ul>
<p>光说不练假把式，所以我们应该动手试一试。流程：创建一个文件，然后利用git add 命令将文件加入暂存区、 git ls-files -s 命令查看暂存区内容 和 find ./.git/objects/ -type f 命令查看版本库内容。</p>
<div align="center">
<p><a href="https://imgtu.com/i/2NDNnA" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17e78e0d86ed4dcfa7a0cfbea85477a4~tplv-k3u1fbpfcp-zoom-1.image" alt="2NDNnA.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
  我在Git学习笔记二中写道，Git的文件管理是从工作区到暂存区最好后在进入版本库，但是从上图就可以发现我以前说的是不对的,我们可以看见现在暂存区和版本库里面都有。所以，那么真正的流程应该是怎么样的呢？下面我用一个图来进行描述。
<div align="center">
<p><a href="https://imgtu.com/i/2N68UI" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ad35329349f4740b5c215e27cd0a079~tplv-k3u1fbpfcp-zoom-1.image" alt="2N68UI.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<p>  所以通过上面的我们可以分析出git add 命令应该就是 git hash-object -w 和 git updata-index的结合体，看到这里我相信大家的思路应该是异常的清晰吧哈哈。</p>
<h3 data-id="heading-4"><strong>将暂存区的内容提交到版本库</strong></h3>
<ul>
<li><strong>git commit -m    "infromation"</strong></li>
<li><strong>git commit "</strong> 可以在vim编辑器中写大量的信息</li>
<li><strong>git commit -a -m "infromation"</strong> 跳过暂存区直接进入版本库(其实是让Git自己执行了git add的命令)</li>
</ul>
<p>git commit 命令应该就是git write-tree 和 git commit-tree的结合体，废话不多说直接上图。(我肯定演示最简单的哈哈哈，剩下的给你们去实践)</p>
<div align="center">
<p><a href="https://imgtu.com/i/2NgV1K" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb0a4360999b4416ade5c4d2ab0f885d~tplv-k3u1fbpfcp-zoom-1.image" alt="2NgV1K.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<p>  没用使用git commit的命令时候版本库里面只有一个对象，当我们使用完命令之后就变成三个对象，这三个对象分别是git对象、树对象以及提交对象。</p>
<h3 data-id="heading-5"><strong>检测当前文件状态</strong></h3>
<ul>
<li><strong>git status</strong></li>
</ul>
<p>  首先，我们需要知道文件有两大状态分别是<strong>已跟踪和未跟踪</strong>，已跟踪又分为<strong>已暂存</strong>、<strong>已提交和已修改</strong>。</p>
<div align="center">
<p><a href="https://imgtu.com/i/2Nf0qU" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/399fc26bce6e46e8879754f0f8bfc745~tplv-k3u1fbpfcp-zoom-1.image" alt="2Nf0qU.png" loading="lazy" referrerpolicy="no-referrer"></a>
<a href="https://imgtu.com/i/2NfhqO" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e43505a9c8564e1bad01b5e59caf4330~tplv-k3u1fbpfcp-zoom-1.image" alt="2NfhqO.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<p>  文件的状态不同我们所采取的行动也不同，文件未跟踪那么我们需要跟踪一下，文件若处于已修改那么我们应该暂存一下，文件处于已暂存那么我们需要提交一下，提交完就可以安心睡大觉了(狗头保命哈哈)。上述情况是比较理想的，现在我们想一种情况：一个文件已经暂存了，但是我现在又修改了这个文件那么git status会提示什么信息呢？废话不多说直接上图！(希望初学Git可以自己尝试的哦！)</p>
<div align="center">
<p><a href="https://imgtu.com/i/2UdRCF" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27a5bf67583746bfa5f4ac1ced8f9a24~tplv-k3u1fbpfcp-zoom-1.image" alt="2UdRCF.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
  在图中的提示可以看见提示文件已暂存需要提交和已修改需要暂存，这样就由问题如果我们此时执行git commit -m 那我们刚才修改会被提交上去吗？答案肯定是不会的，所以我们需要先在次执行git add 命令将修改的内容进行暂存,因为进入暂存区的内容和原来的暂存区具有相同的文件名所以会出现覆盖(Ps:这个覆盖原来这个更加人性化，但是本质不会覆盖因为内容不同生成的hash值是不同的，如果忘记了记得翻一下我以前的笔记哦！)废话不多说上图咯！
<div align="center">
<p><a href="https://imgtu.com/i/2U04Tx" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0be9d53111442b9838eb7b6b4769422~tplv-k3u1fbpfcp-zoom-1.image" alt="2U04Tx.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<h3 data-id="heading-6"><strong>检测已暂存和未暂存的更新</strong></h3>
<ul>
<li><strong>git diff</strong></li>
<li><strong>git diff --cached</strong></li>
</ul>
<p>  对于git status来言，git diff可以让我们看到更多细节可以帮助我们查看具体修改那些内容。git diff 命令：当前的操作是不是修改了但是没有保存；gif diff --cached 命令那些东西暂存了但是没有提交。(Ps:记得自己尝试哦！)</p>
<div align="center">
<p><a href="https://imgtu.com/i/2Uyrz8" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da6711066b446b797a0e48d65690c81~tplv-k3u1fbpfcp-zoom-1.image" alt="2Uyrz8.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<h3 data-id="heading-7"><strong>删除文件</strong></h3>
<ul>
<li><strong>rm 文件路径</strong></li>
<li><strong>git rm 文件路径</strong>(省去了我们再出输入git add命令)</li>
</ul>
<p>  从Git移除文件，那肯定要在已跟踪的文件清单进行删除，通过上面的实验我们知道当执行了git add之后文件就会被跟踪所以我们需要在暂存区将其删除。Git肯定是不会给我们删除的，删除只是表面时看起来删除了本质上还是增加操作，直接上图(图中演示时用的rm)。</p>
<div align="center">
<p><a href="https://imgtu.com/i/2U2ThR" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7854b24fd9b4f1d8bec86a99231c32e~tplv-k3u1fbpfcp-zoom-1.image" alt="2U2ThR.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<p>  捋一下思路，删除操作也就是把工作目录中的new.txt
删除,暂存区中new.txt的快照移除，然后将此时暂存区的快照生成一个树对象,然后再通过git commit 生成提交对象。所以我们的版本库里面会增加两个对象一个树对象和一个提交对象。</p>
<h3 data-id="heading-8"><strong>文件重命名</strong></h3>
<ul>
<li><strong>mv fileName newFileName</strong></li>
<li><strong>git mv fileName newFileName</strong>(省去了我们再出输入git add命令)</li>
</ul>
<p>  git mv 将其分解其实是三个命令 mv name newName;git rm name;git add newName;直接上图(图中演示的时mv)</p>
<div align="center">
<p><a href="https://imgtu.com/i/2UXfRf" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a5b5aba4144b219ac44af6230cc799~tplv-k3u1fbpfcp-zoom-1.image" alt="2UXfRf.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<h3 data-id="heading-9"><strong>查看日志</strong></h3>
<ul>
<li><strong>git log --oneline</strong></li>
</ul>
<p>  这个没啥好说的就是看相关日志，这个大家自己尝试一下就ok啦SO~~easy！</p>
<h2 data-id="heading-10">二、 结尾</h2>
<p>  至此呢Git的经常使用的高层命令就讲述完了下一次就是讲述Git最最最最牛皮的分支功能哈哈哈，如果感觉有用可以点个赞的哦！我会持续更新，如果有错误还请指出来,感谢观众老爷的赏脸。</p>
<p>  若想获得上述内容的PDF版本移步到GitHub下载。</p>
<p>  <strong>地址: </strong><a href="https://github.com/QianquanChina/Study-Notes" target="_blank" rel="nofollow noopener noreferrer">Git 学习笔记专区</a>。</p>
<p align="right">-----缱绻</p>  </div>  
</div>
            