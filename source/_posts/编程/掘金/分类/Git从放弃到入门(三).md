
---
title: 'Git从放弃到入门(三)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd0695d0c8848c2b0a3471b38c6c69d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 07:26:08 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd0695d0c8848c2b0a3471b38c6c69d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>🎏 这是我参与更文挑战的第9天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<h1 data-id="heading-0">0x00 📢 前言</h1>
<p>👇 Git入门系列文章链接如下，请按照顺序阅读文章 👇。</p>
<p><a href="https://juejin.cn/column/6969263852206686221" target="_blank">Git从放弃到入门专栏</a></p>
<p>本系列文章主要通过示例讲解快速掌握各命令的功能和操作流程，完成Git快速入门。</p>
<p>本文是第三篇,介绍下git命令别名设置，如何获取历史版本，打标签。</p>
<h1 data-id="heading-1">0x01 别名</h1>
<p>通过设置别名让频繁使用的Git命令更简单、容易、熟悉。</p>
<p>接下来对常用的命令<code> git status</code>、<code>git add</code>、<code>git commit</code>、<code>git checkout</code>、<code>git log</code> 进行缩写设置别名，将复杂的命令变为简单的单词。命令简单容易记忆，输入更简单便捷，避免输入很长的参数选项内容。</p>
<h2 data-id="heading-2">Windows 用户</h2>
<p>使用命令 <code>git config</code> 设置别名：</p>
<pre><code class="hljs language-bash copyable" lang="bash">git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.br branch
git config --global alias.hist <span class="hljs-string">"log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"</span>
git config --global alias.type <span class="hljs-string">'cat-file -t'</span>
git config --global alias.dump <span class="hljs-string">'cat-file -p'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Unix/Mac用户</h2>
<p>将设置内容到更新至的 <code>$HOME</code> 目录的 <code>.gitconfig</code> 文件中：</p>
<pre><code class="hljs language-bash copyable" lang="bash">...
...
[<span class="hljs-built_in">alias</span>]
    co = checkout
    ci = commit
    st = status
    br = branch
    hist = <span class="hljs-built_in">log</span> --pretty=format:<span class="hljs-string">'%h %ad | %s%d [%an]'</span> --graph --date=short
    <span class="hljs-built_in">type</span> = cat-file -t
    dump = cat-file -p
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dd0695d0c8848c2b0a3471b38c6c69d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前文介绍 <code>git log </code>查看日志时会改变默认格式，设置格式化选型。命令很长，不便记忆输入。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git <span class="hljs-built_in">log</span> --pretty=format:<span class="hljs-string">'%h %ad | %s%d [%an]'</span> --graph --date=short
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过设置别名后，只要输入 <code>git hist</code>即可实现同样功能 👇。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/598aa4d784144e3ba352c9c7e86e0cd0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">0x02 git checkout  获取旧版本</h1>
<p>使用 <code>git hist</code>（git log） 命令展示提交项目历史记录，查看各版本提交快照的哈希。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/598aa4d784144e3ba352c9c7e86e0cd0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过命令 <code>git checkout <hash></code> 将指定版本检出至工作区（Working Directory）。</p>
<p>接下来检出最早版本，查看提交历史纪录获取最早的提交hash值 <code>63120ae</code>,查看切换后文件内容。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git checkout 63120ae
$ cat helloworld.html 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>helloworld.html</code>内容已经改变成最初的。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47257a8c22b542009a09c348273920d2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>git checkout</code> 使仓库处于“分离头指针”（detached HEAD）的状态，这意味着 HEAD (Git 跟踪当前目录应当匹配的那部分)是直接指向提交而非分支。在“分离头指针”状态下，如果你做了某些更改然后提交它们，标签不会发生变化，但你的新提交将不属于任 何分支，并且将无法访问，除非通过确切的提交哈希才能访问。 因此，如果你需要进行更改，比如你要修复旧版本中的错误，那么通常需要创建一个新分支。</p>
<h2 data-id="heading-5">切换至master分支最新版本</h2>
<pre><code class="hljs language-bash copyable" lang="bash">$ git checkout master
$ cat helloworld.html 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>git checkout master</code>命令做了两件事。 一是使 HEAD 指回 master 分支，二是将工作目录恢复成 master 分支所指向的快照内容。此时文件内容已经变更至最后一次提交时。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e1ff280ba3040bebc8337d83087cde1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">0x03 git tag 打标签</h1>
<p>Git 可以给仓库历史中的某一个提交打上标签，以示重要。 使用这个功能来标记发布结点。</p>
<p>为程序的当前版本打一个 <code>v1</code> 的标签。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git tag v1
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">先前版本切换</h2>
<p>如果需要检出先前版本。可以使用 <code>v1^</code> 代替hash查询 , <code>v1^</code> 来表示“<strong>v1版本的上次提交</strong>”。也可以使用 <code>v1~1</code>，效果一样。该表示法意为“<strong>v1版本之前的最近一次提交</strong>”,格式为<code>tag~n</code>,1可以替换成n任意数值 。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git checkout v1^
$ cat helloworld.html 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf7c948038e449ba75bbd9e0b63f5de~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>检出后，为当前的版本打一个标记 <code>v1-rc</code>。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git tag v1-rc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需要输入命令 <code>git tag</code>,列出已有的标签。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git tag 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40c37219d9747d2920c88f6072cc92d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">检出标签</h2>
<p>尝试在多个标记版本之间切换。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git checkout v1
$ git checkout v1-rc
$ git checkout v1
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06470958d67345c2bb56520161789e7f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">日志中查看标签</h2>
<p>使用命令查看提交纪录中标签信息。</p>
<pre><code class="hljs language-js copyable" lang="js">$ git hist master --all
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在日志中看到多了两个标签 <code>tag:v1</code>  <code>tag:v1-rc</code> 。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38dbc93efac2494c80880b7ff56f3591~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">0x04 📚参考</h1>
<p><a href="https://git-scm.com/book/zh/v2" target="_blank" rel="nofollow noopener noreferrer">Pro Git Online</a></p>
<h1 data-id="heading-11">0x05  关注专栏</h1>
<p>此文章已收录到专栏中 👇，可以直接关注。</p>
<p>更多文章继续阅读｜系列文章持续更新</p></div>  
</div>
            