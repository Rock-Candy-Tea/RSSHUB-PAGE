
---
title: '如何用 git 折磨同事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ac70a6053de4965a2ab234d5850d1eb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 07:42:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ac70a6053de4965a2ab234d5850d1eb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>merge  代码的正确姿势</strong></p>
<h2 data-id="heading-0">前情铺垫</h2>
<p>这里就不讲 gitflow 的问题了，最最简单的场景，同事A 和 B，协同开发，假设分支名是 feature。两人共同在 feature  上提交代码。</p>
<h3 data-id="heading-1">初始化</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ac70a6053de4965a2ab234d5850d1eb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">B 君开了个分支，写了一行B代码</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d60da6925e24625b1ccb398b32da645~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">B 君告知A，请求代码合并到公共分支上</h3>
<p>A 一堆操作猛如虎</p>
<pre><code class="hljs language-bash copyable" lang="bash">git checkout feature
git merge -s ours func_b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通知B君，我合并你代码了。</p>
<h3 data-id="heading-4"><strong>这时候 B 君一看，我代码咋没了</strong></h3>
<pre><code class="hljs language-bash copyable" lang="bash">😠 demo git:(feature) cat code
😠 demo git:(feature) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看一下 <code>git log</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">😠 demo git:(feature) git <span class="hljs-built_in">log</span> --oneline --decorate --graph
*   846f001 (HEAD -> feature) Merge branch <span class="hljs-string">'func_b'</span> into feature
|\\
| * 93972fb (func_b) code by b
|/
* 1c2b405 init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没毛病，提交已经合并了。</p>
<h3 data-id="heading-5"><strong>要不自己再合一下？</strong></h3>
<pre><code class="hljs language-bash copyable" lang="bash">😡 demo git:(feature) git merge func_b
Already up to date.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完犊子，git 认为已经合并过了 ，不做处理。🤬</p>
<h2 data-id="heading-6">原理</h2>
<p>我们合并代码时候，是可以指定合并策略的。<code>recursive</code> 是默认的。</p>
<ul>
<li>resolve</li>
<li>recursive</li>
<li>octopus</li>
<li>ours</li>
<li>subtree</li>
</ul>
<p>划重点，<code>ours</code>  策略，即合并时候，不管别人做了什么，以我分支上的提交为主，丢弃掉别人的变动。</p>
<p>对此 ，我们可以有很多操作坑队友</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git merge --strategy=ours origin/master  <span class="hljs-comment"># 合并主干代码，但丢弃主干变动</span>
$ git pull -s ours <span class="hljs-comment"># 拉取远程代码，并丢弃队友push的代码</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">结尾</h3>
<p>为啥我会看这些？因为我特么是被坑的那个🤬。不晓得同事的git GUI工具咋配置的能干出这种事🤬</p>
<p>由于太气了，所以不能好好介绍上述其他策略了，详见大佬文章</p>
<p><a href="https://blog.walterlv.com/post/git-merge-strategy.html#resolve" target="_blank" rel="nofollow noopener noreferrer">git 合并策略</a></p>
<blockquote>
<p><a href="https://eoyohe.cn/2021/07/02/%E5%A6%82%E4%BD%95%E7%94%A8-git-%E6%8A%98%E7%A3%A8%E5%90%8C%E4%BA%8B/" target="_blank" rel="nofollow noopener noreferrer">个人博客原文地址</a></p>
</blockquote></div>  
</div>
            