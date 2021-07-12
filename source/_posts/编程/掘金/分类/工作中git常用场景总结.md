
---
title: '工作中git常用场景总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2543'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 22:44:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=2543'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">git常用流程命令</h2>
<pre><code class="hljs language-js copyable" lang="js">git clone <span class="hljs-string">'http://www.url'</span> <span class="hljs-comment">// 下载仓库代码到本地</span>
git branch -a <span class="hljs-comment">// 查看所有的分支</span>
git checkout -b 本地分支 远程分支 <span class="hljs-comment">// 远程代码分支下载到本地分支</span>
git pull
git add . || git add -A
git commit -m <span class="hljs-string">'commitMsg'</span>
git push
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">场景一：git误删的恢复操作</h2>
<h5 data-id="heading-2">前提是执行了git add 命令或者是 git statch</h5>
<pre><code class="hljs language-js copyable" lang="js">git log  <span class="hljs-comment">// 找到你提交代码的记录</span>
git reset 指定版本 <span class="hljs-comment">// 回退到删除的那个版本id</span>
git status <span class="hljs-comment">// 找到删除的记录 里面有删除的文件等相关信息</span>
git checkout 删除的文件或者文件夹 <span class="hljs-comment">// 恢复删除的文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">场景二：遇到pull有冲突的时候</h2>
<pre><code class="hljs language-js copyable" lang="js">git add . <span class="hljs-comment">// add本地修改的内容</span>
git statch save <span class="hljs-string">'暂存标识'</span> <span class="hljs-comment">// 暂存本地修改的内容</span>
git pull <span class="hljs-comment">// 更新远程代码到本地</span>
git stash pop stash@&#123;<span class="hljs-number">0</span>&#125; <span class="hljs-comment">// 恢复暂存代码</span>
<span class="hljs-comment">// 然后解决冲突，提交代码。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">场景三：合并分支</h2>
<p>想将dev分支合并到master分支，操作如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、首先切换到master分支上
   git checkout master
<span class="hljs-number">2</span>、保险起见，需要把远程master上的代码pull下来
   git pull origin master
<span class="hljs-number">3</span>、然后我们把dev分支的代码合并到master上
   git merge dev
<span class="hljs-number">4</span>、然后查看状态及执行提交命令
   git status
<span class="hljs-number">5</span>、最后执行下面提交命令
  git push origin master
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">其他常用命令</h2>
<pre><code class="hljs language-js copyable" lang="js">git config -e <span class="hljs-comment">// 查看当前项目配置的git配置文件 里面有当前项目的源地址</span>
git --amend -m <span class="hljs-string">'msg'</span> <span class="hljs-comment">// 修改上次提交的commit msg</span>
git stash list <span class="hljs-comment">// 可以查看git的暂存代码</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            