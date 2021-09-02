
---
title: '「03」Git之add、branch、stash和checkout命令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afec26cadc5640b2a2133002b3d3dd0d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 22:12:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afec26cadc5640b2a2133002b3d3dd0d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a name="user-content-nnQZN" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-0">前言</h2>
<p>从本章开始，为了便于描述，我们做出如下约定。<br>凡是<code><></code>内的内容皆为自定义内容，部分名词含义如下<br>
<code><localBranch></code>           指本地已有分支<br>
<code><originBranch></code>         指远程分支<br>
<code><branchName></code>              指分支名称<br>
<code><repoAddress></code>           指仓库地址<br>
<code><commit></code>                     指某个commit记录<br>
<code>origin</code>                        指远程仓库<br>
本章节主要讲述 <code>add</code>、<code>branch</code>、<code>stash</code>和<code>checkout</code>命令
<a name="user-content-2wHiF" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-1">add命令</h2>
<p><a name="user-content-L0Wfa" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-2">作用</h3>
<p>用来确定将那些文件放在暂存区中，这些文件将包含在下一次提交中
<a name="user-content-wqdIL" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-3">用法</h3>
<ol>
<li>git add 文件路径+文件    例如：<code>git add foo.txt</code> <code>git add file/bar.txt</code></li>
<li><code>git add .</code>    或者 <code>git add --all</code>   将所有文件添加到暂存去中</li>
</ol>
<p><a name="user-content-OPK8M" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-4">branch命令</h2>
<p><a name="user-content-hrD3v" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-5">作用</h3>
<p>主要是用来查看、新建和删除分支
<a name="user-content-MdIGZ" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-6">用法</h3>
<ol>
<li><code>git branch</code> 查看本地分支，带有*的表示我们当前所在的分支</li>
<li><code>git branch <branchName></code>新建一个本地分支，但不会自动切换到信分支上</li>
<li><code>git branch <brancName> <commit></code>为某个commit记录创建一个分支</li>
<li><code>git branch <brancName> <localBranch></code>从某个分支新建一个分支</li>
<li><code>git branch -d <localBranch></code>删除本地该分支（不能删除当前所在的分支，不能删除没有合并到master上的分支）</li>
<li><code>git branch -D <localBranch></code> 删除本地该分支（不能删除当前所在的分支，可以删除没有合并到master上的分支）</li>
<li><code>git branch <branchName> <commit></code> 在已知commit的情形下，将某个被删除的分支进行复原</li>
</ol>
<p>这里说一下关于commit版本的问题，我们输入<code>git log</code> 会显示最近的一部分提交历史，在这里我们能查看我们的commit<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afec26cadc5640b2a2133002b3d3dd0d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>从图中我们可以看出，我们的commit是一个很长的16位的散列值，但其实我们在使用的时候，只需要截取前八位就行了，即<code>631a6b33</code>。之所以取前八位，是因为这里面已经包含了作者，以及提交的时间这一系列信息，<strong>作者+时间</strong>这两个信息生成的散列值会重复的概率以及微乎其微了。
<a name="user-content-oHkvA" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-7">stash命令</h2>
<p><a name="user-content-XRpMO" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-8">作用</h3>
<p>暂时贮存代码
<a name="user-content-UYUX2" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-9">用法</h3>
<ol>
<li><code>git stash</code>贮存当前改动</li>
<li><code>git stash list</code>查看贮存列表</li>
<li><code>git stash pop</code>应用某个贮存（默认第一个），即<code>git stash pop stash@&#123;0&#125;</code> 并删除该贮存，可修改最后的数字，来指定应用某个贮存</li>
<li><code>git stash apply</code>应用某个贮存（默认第一个），即 <code>git stash apply stash@&#123;0&#125;</code>，不会删除贮存，可修改最后的数字，来指定应用某个贮存</li>
<li><code>git stash drop</code>删除某个贮存（默认第一个），即<code>git stash drop stash@&#123;0&#125;</code> 可修改最后的数字，来指定删除某个贮存</li>
<li><code>git stash show</code>查看某个贮存（默认第一个）做了那些改动，即 <code>git stash show stash@&#123;0&#125;</code> 可修改最后的数字，来指定查看某个贮存</li>
<li><code>git stash clear</code>删除所有贮存</li>
</ol>
<blockquote>
<p>注意⚠️：<strong>没有在git 版本控制中的文件，是不能被git stash 存起来的</strong></p>
</blockquote>
<p>出现上述情形我们该怎么办呢？其实很简单，我们指需要使用<code>add</code>命令将它添加到暂存区中就可以对它使用<code>stash</code>命令了
<a name="user-content-xZ3Gt" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-10">checkout命令</h2>
<p><a name="user-content-BzKa2" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-11">作用</h3>
<p>切换分支
<a name="user-content-mqutu" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h3 data-id="heading-12">用法</h3>
<ol>
<li><code>git checkout <branchName></code>切换到某个分支</li>
<li><code>git checkout --force <branchName></code>强制切换到某个分支，会丢失当前已修改的内容</li>
<li><code>git checkout -b <branchName></code>创建并切换到新分支</li>
</ol>
<p>当我们本地存在修改时，切换分支这个操作很大可能是<strong>会被拒绝的</strong>，此时我们可以</p>
<ol>
<li>先提交修改</li>
<li>使用stash命令先暂存起来，之后在用stash pop来恢复他们</li>
</ol>
<p>什么时候<strong>不会被拒绝</strong>呢？只有当前两个分支处于同一个版本时，才不会拒绝checkout操作。也就是说如下操作是合法的。</p>
<ol>
<li>假设我们现在在a分支上，并在A分支上做出<strong>未提交的修改</strong></li>
<li>接下来做出如下操作 <code>git checkout -b B</code></li>
<li>此时我们是能切换成功的，并且我们所做出的修改也一并带了过来</li>
<li>此时我们在切换回A分支也是没有任何问题的，当然，我们所做出的修改也会跟着一起过来</li>
</ol>
<p><a name="user-content-lTdG5" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-13">总结</h2>
<p>本章节主要讲述 <code>add</code>、<code>branch</code>、<code>stash</code>和<code>checkout</code>命令的作用、用法以及一些注意事项，带大家对这些命令有一个更深入的理解。
<a name="user-content-ocIBB" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-14">往期文章</h2>
<p><a href="https://juejin.cn/post/6996833216720011300" target="_blank" title="https://juejin.cn/post/6996833216720011300">「02」Git之.gitignore文件配置</a><br><a href="https://juejin.cn/post/6993128865258274823" target="_blank" title="https://juejin.cn/post/6993128865258274823">「01」Git之版本控制</a>​</p></div>  
</div>
            