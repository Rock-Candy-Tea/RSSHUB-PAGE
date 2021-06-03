
---
title: '一个让 git clone 提速几十倍的小技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2000f3af00704c16a0647f4db6b55b2d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 06:43:08 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2000f3af00704c16a0647f4db6b55b2d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
<p>不知道大家有没有遇到比较大的项目，git clone 很慢很慢，甚至会失败的那种。大家会怎么处理的呢？</p>
<p>可能会考虑换一个下载源，可能会通过一些手段提高网速，但是如果这些都试过了还是比较慢呢？</p>
<p>今天我就遇到了这个问题，我需要把 typescript 代码从 gitlab 下载下来，但是速度特别慢：</p>
<pre><code class="hljs language-shell copyable" lang="shell">git clone https://github.com/microsoft/TypeScript ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等了很久还是没下载完，于是我加了一个参数：</p>
<pre><code class="hljs language-shell copyable" lang="shell">git clone https://github.com/microsoft/TypeScript --depth=1 ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样速度提高了几十倍，瞬间下载完了。</p>
<p>加上 --depth 会只下载一个 commit，所以内容少了很多，速度也就上去了。</p>
<p>而且下载下来的内容是可以继续提交新的 commit、创建新的分支的。不影响后续开发，只是不能切换到历史 commit 和历史分支。</p>
<p>我用我的一个项目测试过，我首先下载了一个 commit：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2000f3af00704c16a0647f4db6b55b2d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后做一下改动，之后 git add、commit、push，能够正常提交：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f2c0dcdcd014829b65efbe81a8a6291~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd2ec3ef478e480eaf06658ffc7a6ccd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建新分支也能正常提交。唯一的缺点就是不能切换到历史 commit 和历史分支。</p>
<p>在一些场景下还是比较有用的：当需要切换到历史分支的时候也可以计算需要几个 commit，然后再指定 depth，这样也可以提高速度。</p>
<p>大家有没有想过，这样能行的原理是什么？</p>
<h2 data-id="heading-0">git 原理</h2>
<p>git 是通过一些对象来保存信息的：</p>
<ul>
<li>glob 对象存储文件内容</li>
<li>tree 对象存储文件路径</li>
<li>commit 对象存储 commit 信息，关联 tree</li>
</ul>
<p>以一个 commit 为入口，关联的所有的 tree 和 blob，就是这个 commit 的内容。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b0dfd84fe0e416fb94250a44454cae5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>commit 之间相互关联，而 head、branch、tag 等是指向具体 commit 的指针。可以在 .git/refs 下看到。这样就基于 commit 实现了分支、tag 等概念。</p>
<p>git 就是通过这三个对象来实现的版本管理和分支切换的功能，所有 objects 可以在 .git/objects 下看到。</p>
<p>这就是 git 的原理。</p>
<p>主要理解 blob、tree、commit 这三个 object，还有 head、tag、branch、remote 等 ref。</p>
<h2 data-id="heading-1">能下载单个 commit 的原理</h2>
<p>我们知道了 git 是通过某一个 commit 做为入口来关联所有的 object，那如果我们不需要历史自然就可以只下载一个 commit。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3fa1b29536c404695b4abb484630802~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样依然基于那个 commit 创建新的 commit，关联新的 blob、tree 等。但是历史的 commit、tree、blob 因为都没有下载下来所以无法切回去，相应的 tag、branch 等指针也不行。这就是我们下载了单个 commit 却依然可以创建新的分支、commit 等的原理。</p>
<h2 data-id="heading-2">总结</h2>
<p>遇到大的 git 项目的时候，可以通过添加 --depth 参数使得速度极大提升，历史 commit 越多，下载速度提升越大。</p>
<p>而且下载下来的项目依然可以进行后续开发，可以创建新的 commit 和新的分支、tag，只是不能切换到历史 commit、分支、tag。</p>
<p>我们梳理了 git 的原理：通过 tree、blob、commit 这三个 object 来存储文件和提交信息，通过 commit 之间的关联来实现分支、标签等功能。commit 是入口，关联所有的 tree 和 blob。</p>
<p>我们下载了一个 commit，就是下载了他关联的所有 tree、blob，还有一些 refs （包括tag、branch 等），这就是 --depth 的原理。</p>
<p>希望大家在不需要切换到历史 commit 和分支的场景下可以用这个技巧来提升大项目的 git clone 速度。</p></div>  
</div>
            