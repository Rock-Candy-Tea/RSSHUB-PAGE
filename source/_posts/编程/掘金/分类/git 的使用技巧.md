
---
title: 'git 的使用技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2472'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 20:50:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=2472'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.现在的工作空间太乱了，工作到一半，临时插需求。<strong>如何获得一个干净的工作空间？</strong></h2>
<p><code>git reset --hard HEAD</code> 使用这条命了，会使你的工作区和缓冲区和HEAD保持一致，原来的工作区的修改和缓存区的修改都不会保留，虽然能得到一个干净空间，但是一条<strong>很危险</strong>的命令。</p>
<p>应该使用<code>git stash</code>命令将工作区和缓存区的内容储藏起来，当完成临时的需求后，再使用<code>git stash apply</code>或<code>git stash pop</code>恢复。</p>
<h3 data-id="heading-1">2.从Git历史中删除一个文件，比如有敏感信息（私钥，内网ip等）或者不需要版本控制的超大文件</h3>
<p><code>git filter-branch --tree-filter 'rm -f passwords.txt' HEAD</code></p>
<h3 data-id="heading-2">3.上一个的commit的message打错字了，怎么修改</h3>
<p><code>git commit --amend -m ”Fix bug #42“</code></p>
<p>如果需要修改更早的commit的信息，怎么做？</p>
<p><code>git rebase -i [需要更改的commit的父SHA]</code>在交互式环境下修改。</p>
<h3 data-id="heading-3">4.追溯一个指定文件的历史修改记录</h3>
<p><code>git blame [filename]</code></p>
<h3 data-id="heading-4">5.代码有bug，commit很多次了，到底是哪一次修改把bug引入了？</h3>
<p><code>git bisect start [终点SHA] [起点SHA]</code></p>
<p><code>git bisect good</code>标记正确，<code>git bisect bad</code>标记错误，直到成功找到出问题的那一次提交为止。这时，Git 会给出如下的提示。</p>
<blockquote>
<p>XXXX is the first bad commit</p>
</blockquote>
<h3 data-id="heading-5">6.提交的版本有bug，怎么回退版本。</h3>
<p>方法一：使用<code>git revert HEAD</code>，前提是工作区和暂存区是干净的，新增一次提交，抵消上一次的变化，不会改变历史，首选方式，没有任何丢失代码的风险。</p>
<p>方法二：<code>git reset [SHA]</code>，丢弃部分提交，默认暂存区清空，工作区不变动，使用了<code>git reset --hard[SHA]</code>使工作区的文件回到以前的状态。</p>
<h3 data-id="heading-6">7.改写代码，发现还是原来的好，还没有commit时，撤销工作区的修改</h3>
<p><code>git checkout -- [filename]</code></p>
<p>两种情况：</p>
<p>1.修改后还没有被放到暂存区，撤销修改就回到和版本库一模一样的状态。</p>
<p>2.已经添加到暂存区后，撤销修改就回到添加到暂存区后的状态。</p>
<h3 data-id="heading-7">8.撤销暂存区已经add的文件</h3>
<p>有以下三种方法：</p>
<ol>
<li><code>git reset HEAD [filename]</code></li>
<li><code>git rm --cached [filename]</code></li>
<li><code>git reset [filename]</code></li>
</ol>
<h2 data-id="heading-8">9.本地有A_branch分支，远程没有A_branch分支</h2>
<p>当你在A分支push的时候会报错，同时会有提示：git push --set-upstream origin A_branch，即可以完成远程新建一个A_branch分支，同时也会push上去。</p>
<h2 data-id="heading-9">10.远程有B_branch分支，本地没有B_branch分支</h2>
<p>第一步：git fetch，获取远程新建的分支；</p>
<p>第二步：git checkout -b B_branch origin/B_branch 本地新建分支并和远程分支关联。</p></div>  
</div>
            