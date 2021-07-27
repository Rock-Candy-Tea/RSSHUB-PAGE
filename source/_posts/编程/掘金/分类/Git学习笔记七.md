
---
title: 'Git学习笔记七'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a49517fcd34f4e8d0cbd27d5aa0293~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 02:03:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a49517fcd34f4e8d0cbd27d5aa0293~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>  我们知道一个提交对象就是一个版本，那么我们在某一次版本中具有历史性的突破所以我们需要进行记录一下，在Git中可以利用tag(标签)来进行记录。我们工作的时候是需要伙伴的也就是说我们需要进行远程协作的啦！下面就分别讲述他们的功能以及一些简易操作。</p>
<h2 data-id="heading-1">一、Tag</h2>
<p>  Git可以使用给一个提交对象进行打标签或者说是标记。类似于游戏的版本~</p>
<ul>
<li>
<p>列出标签<br>
命令：git tag</p>
</li>
<li>
<p>创建标签<br>
<strong>轻量标签:</strong> 这个标签的功能和分支有点类似，只不过这个标签不能移动。</p>
<p>命令：git tag v1.0 [commitHash]</p>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FR2aRbD" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/R2aRbD" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a49517fcd34f4e8d0cbd27d5aa0293~tplv-k3u1fbpfcp-zoom-1.image" alt="R2aRbD.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<p><strong>附注标签:</strong> 这个标签是存储在Git数据库中的一个完整对象。他们是被检验的；标签会包含打标签的者的名字、电子邮件地址和日期时间；我们通常是创建附注标签，如果你因为某些原因不想保存信息那么是可以选择轻量标签的。</p>
<p>命令：git tag -a v1.1</p>
</li>
</ul>
<p>     git tag -a v1.1 commitHash</p>
<p>     git tag -a v1.1 commitHash -m "version v1.1"</p>
<p>  <strong>查看标签:</strong> 这个标签的功能和分支有点类似，只不过这个标签不能移动。</p>
<p>  命令：git show tagname</p>
<p>  <strong>删除标签:</strong> 这个标签的功能和分支有点类似，只不过这个标签不能移动。</p>
  <div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FRoOXpq" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/RoOXpq" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c67f5ca99194e0285be872a8a67a612~tplv-k3u1fbpfcp-zoom-1.image" alt="RoOXpq.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
  </div>
<p>  命令：git tag -d tagname</p>
<p>  <strong>检出标签:</strong> 这个标签的功能和分支有点类似，只不过这个标签不能移动。</p>
<p>  命令：git checkout tagname</p>
  <div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FRojAaQ" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/RojAaQ" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d78eddf78a9d437fa39286591c1c8254~tplv-k3u1fbpfcp-zoom-1.image" alt="RojAaQ.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
  </div>
<p>  到这里一些基本的操作就大体上结束了，下面将结合远程仓库(GitHub)进行讲解团队协作。</p>
<h2 data-id="heading-2">二、远程仓库</h2>
<p>  为了可以使用Git项目上的团队协作，我们需要知道如何管理自己的远程仓库。远程仓库的内容就是我项目的版本库，一般来言我们可以又很多远程仓库。与他人协作完成共同任务需要我们掌握管理远程仓库以及根据需求推送或拉取数据。下面就为远程仓库开个头~<br>
首先我们需要打开<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/" ref="nofollow noopener noreferrer">GitHub的网址</a>进行注册账号以及创建一个新的仓库。</p>
<h3 data-id="heading-3">1.创建远程仓库</h3>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FW9gdDP" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/W9gdDP" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02ff15529f3f4cd89ac388f2cf4750f9~tplv-k3u1fbpfcp-zoom-1.image" alt="W9gdDP.png" loading="lazy" referrerpolicy="no-referrer"></a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FW9gwHf" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/W9gwHf" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf89f1f91b3348b591a58b9e2442d9ed~tplv-k3u1fbpfcp-zoom-1.image" alt="W9gwHf.png" loading="lazy" referrerpolicy="no-referrer"></a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FW9gBE8" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/W9gBE8" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ee5cfe8b0694dacad350ff3a5b3d337~tplv-k3u1fbpfcp-zoom-1.image" alt="W9gBE8.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<h3 data-id="heading-4">2.为远程仓库配置简单的名字</h3>
<ul>
<li>
<p>命令：git remote add name url</p>
</li>
<li>
<p>作用：添加一个新的远程Git仓库，同时指定一个我们自己容易记得简写。</p>
</li>
<li>
<p>命令：git remote -v</p>
</li>
<li>
<p>作用：显示远程仓库使用的Git别名和与之对应的url。</p>
</li>
</ul>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWeYY4g" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/WeYY4g" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7287dde89b04906ab2c2842c4a89188~tplv-k3u1fbpfcp-zoom-1.image" alt="WeYY4g.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<ul>
<li>
<p>命令：git remote rename pb paul</p>
</li>
<li>
<p>作用：重命名。</p>
</li>
<li>
<p>命令：git remote rm name</p>
</li>
<li>
<p>作用：移除远程仓库。</p>
</li>
</ul>
<h3 data-id="heading-5">3.将本地项目推送到远程仓库</h3>
<ul>
<li>命令：git push remote-name branch-name</li>
<li>作用：将提交对象推送到远程仓库里面。(push的时候会生成远程跟踪分支，后边会深入的解释这个分支)</li>
</ul>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWeDjMD" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/WeDjMD" ref="nofollow noopener noreferrer"><img src="https://z3.ax1x.com/2021/07/14/WeDjMD.png" alt="WeDjMD.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<h3 data-id="heading-6">4.克隆远程仓库</h3>
<ul>
<li>命令：git clone url</li>
<li>作用：克隆远程仓库。</li>
</ul>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWersyD" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/WersyD" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1346fd26b53438b951935d308b330de~tplv-k3u1fbpfcp-zoom-1.image" alt="WersyD.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
  单纯的克隆是无法进行提交，需要接收到邀请才可以进行提交克隆的仓库已经帮我起好了别名，当然我们也可以修改掉哈。
<h3 data-id="heading-7">5.邀请成员加入该项目</h3>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWe2yOf" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/We2yOf" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa119048f91643039005e03f4349efc8~tplv-k3u1fbpfcp-zoom-1.image" alt="We2yOf.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWe2cm8" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/We2cm8" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3f6ad63029f44849a1a57b18dff3d7b~tplv-k3u1fbpfcp-zoom-1.image" alt="We2cm8.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<p>  在我们注册GitHub的时候有填写的邮箱，被邀请者会收到一封邮件打开邮件根据操作即可成为该项目的成员。</p>
<h3 data-id="heading-8">6.项目负责人来更新成员所提交的内容</h3>
<ul>
<li>命令：git fetch [remote-name]</li>
<li>作用：克隆远程仓库。</li>
</ul>
<p>  这个命令会访问远程仓库，从中获取本地仓库还没有的数据。需要注意，这个命令并不会将数据自动合并或者修改到当前工作，我们需要进行收到合并才可以。</p>
<h2 data-id="heading-9">三、远程跟踪分支</h2>
<p>  远程跟踪分支是远程分支状态的引用。他们是你不能移动的本地分支，当你做任何网络通信操作时候，它们会自动移动。<br>
当克隆一个仓库时，会自动生成一个master本地分支并且已经跟踪了对应的远程跟踪分支。<br>
当我们新创建一个分支的时候，可以指定该分支跟踪哪一个远程跟踪分支,通过下面的命令:1.git checkout -b 本地分支名 远程跟踪分支名 2.git checkout --track 远程跟踪分支名。</p>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWhJW5t" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/WhJW5t" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6de3b9e2e5ea41c098899cc81d9986bb~tplv-k3u1fbpfcp-zoom-1.image" alt="WhJW5t.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWhJRUI" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/WhJRUI" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd585b88d861476a997007675a6f3899~tplv-k3u1fbpfcp-zoom-1.image" alt="WhJRUI.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FWhJ2VA" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/WhJ2VA" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cc93d181f094afe927086dcfa71f284~tplv-k3u1fbpfcp-zoom-1.image" alt="WhJ2VA.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<p>  上图我们发现使用git push 的命令很长,需要加上远程分支和本地分支名这样太麻烦了，我们需要进行优化一下。如果可以将本地分支和这个远程分支进行绑定起来那么我们就可以直接使用git push命令了。</p>
<p>  通过<strong>git branch -u 远程跟踪分支名</strong> 即可将当前所在本地分支与远程分支进行跟踪起来,之后就可以通过git push来进行操作啦！！</p>
<h2 data-id="heading-10">四、解决冲突</h2>
<p>  我们再本地仓库写代码会用冲突，那我们将我代码存放再远程仓库和同事一起合作来完成项目，这样也会有冲突我们使用git push(推送代码到远程仓库)、git pull(从远程仓库获取代码) 这都会产出冲突，那么下面就来看看是怎么产生冲突以及如果进行解决冲突。</p>
<ul>
<li>git push 造成的冲突</li>
</ul>
<p>  如果两个人再某一个文件动了同一个地方，然后再进行git push 那么这样肯定会产生冲突的。通过下面的图可以更好的理解。</p>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FW5EX8A" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/W5EX8A" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecd02c92ac53444ab4be86d69fc82cdf~tplv-k3u1fbpfcp-zoom-1.image" alt="W5EX8A.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FW5EOCd" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/W5EOCd" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c484ada16a1d4f41985e755cafc7928b~tplv-k3u1fbpfcp-zoom-1.image" alt="W5EOCd.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FW5Eq4H" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/W5Eq4H" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/924c36e575b349dbb20eedb705e7e1a7~tplv-k3u1fbpfcp-zoom-1.image" alt="W5Eq4H.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<ul>
<li>git pull 造成的冲突</li>
</ul>
<p>  如果远程库的一个文件的第6行有内容，并且你本地代码也刚好写到第六行，然后去执行git pull 那么此时就是出现冲突，但是我们一般不会去pull 因为本地都没没提交呢但是这个也是存在的一种可能性。(是不是感觉这个和上面的很熟悉哈哈,其实是一样的哈哈)</p>
<div align="center">
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fimgtu.com%2Fi%2FW51efK" target="_blank" rel="nofollow noopener noreferrer" title="https://imgtu.com/i/W51efK" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59a63aa7a7d24f0e89a66768dfdec4af~tplv-k3u1fbpfcp-zoom-1.image" alt="W51efK.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
</div>
<h2 data-id="heading-11">五、 结尾</h2>
<p>  至此呢Git就完结撒花，仅此记录一下学习过程，如果有错误还请指出来,感谢观众老爷的赏脸。<br>
若想获得上述内容的PDF版本移步到GitHub下载。</p>
<p>  <strong>地址: </strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FQianquanChina%2FStudy-Notes" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/QianquanChina/Study-Notes" ref="nofollow noopener noreferrer">Git 学习笔记专区</a></p></div>  
</div>
            