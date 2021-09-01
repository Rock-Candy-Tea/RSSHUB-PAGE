
---
title: 'git add && git stash 的巧用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17120f28794d44b5b39c7f14a8596a49~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 16:46:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17120f28794d44b5b39c7f14a8596a49~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>首发于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fblueju%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/blueju/" ref="nofollow noopener noreferrer">语雀文档@blueju</a></p>
</blockquote>
<p><a name="user-content-rEjdm" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-0">git stash & git add</h2>
<p>git add 和 git stash 的用法不多说，详情请看</p>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fdocs%2Fgit-stash" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/docs/git-stash" ref="nofollow noopener noreferrer">git-scm.com/docs/git-st…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgit-scm.com%2Fdocs%2Fgit-add" target="_blank" rel="nofollow noopener noreferrer" title="https://git-scm.com/docs/git-add" ref="nofollow noopener noreferrer">git-scm.com/docs/git-ad…</a></li>
</ol>
<p>​<br>
<a name="user-content-d94Ve" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-1">契机</h2>
<p>发现该巧用的契机是有一次需要使用 git stash 将修改内容藏匿（stash）起来，但使用后发现 git stash 只能将修改项藏匿，并能将新增项藏匿，那可怎么办？<br>​</p>
<p>查阅了下文档，确实如此，诚不起我。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17120f28794d44b5b39c7f14a8596a49~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-SXJuf" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-2">实践</h2>
<p>我既修改了又新增了。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d414c748892540819bdbc34507fbd28d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>直接 git stash，导致只成功藏匿了修改，未成功藏匿新增。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/008b4f95656f4df596a32d474387e880~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>先 git add，在 git stash，成功藏匿了新增和修改。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d00c6c5eabc54c339cb3a69065506b58~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-EE4Lp" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a></p>
<h2 data-id="heading-3">收获</h2>
<p>纠正了我对 git add 和 git stash 在描述 & 用法上的偏差</p>
<blockquote>
<p>之前我以为 git stash 能将工作区（其实不止工作区，还包括索引区）的新增、修改（其实在工作区中不包括新增，但在索引区包括）暂存（其实应该是叫藏匿）起来</p>
</blockquote></div>  
</div>
            