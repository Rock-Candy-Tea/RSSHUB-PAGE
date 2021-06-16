
---
title: 'Git从放弃到入门(四)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9123e53cdd77446f84c9885ee8787b05~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 07:15:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9123e53cdd77446f84c9885ee8787b05~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>🎏 这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<h1 data-id="heading-0">0x00 📢 前言</h1>
<p>👇 Git入门系列文章链接如下，请按照顺序阅读文章 👇。</p>
<p><a href="https://juejin.cn/column/6969263852206686221" target="_blank">Git从放弃到入门专栏</a></p>
<p>本系列文章主要通过示例实践讲解快速掌握 Git 基础用法，实现快速入门。</p>
<p>本文是第四篇,介绍不同阶段的撤销操作。</p>
<h1 data-id="heading-1">0x01 放弃本地更改</h1>
<blockquote>
<p>📌有时候修改了本地工作目录（通常也叫工作区）的文件，如何放弃本地更改（尚未暂存）？</p>
</blockquote>
<p>首先将项目切换至master分支最新版本。</p>
<pre><code class="hljs language-js copyable" lang="js">$ git checkout master
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更改 <code>helloworld.html</code>，新增一条注释（错误内容）。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, World!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-comment"><!-- 新增一条注释，错误内容. 接下来将会重置它. --></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检查工作区的状态。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git st (git status)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示文件 <code>helloworld.html</code> 已修改，尚未暂存。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9123e53cdd77446f84c9885ee8787b05~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">git checkout</h2>
<p>使用 <code>git checkout <file></code> 命令来检出仓库中的版本文件，舍弃工作目录中的更改。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git checkout helloworld.html
$ git st
$ cat helloworld.html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示在工作目录中不存在更改。文件中的新增注释内容也被还原了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4fe3a7305e249eab61ab05cbdd889f1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">git restore</h2>
<p>根据提示也可以使用<code>git restore</code>，该命令还是实验性的，功能可以发生变化。<a href="https://git-scm.com/docs/git-restore" target="_blank" rel="nofollow noopener noreferrer">git-restore v2.32.0 doc </a></p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git st
$ git restore helloworld.html
$ git st
$ cat helloworld.html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参照上文更改文件，检查工作目录状态后，运行<code>git restore</code> 即可舍弃工作目录中的更改。与 <code>git checkout</code>效果一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec70112efb4e41fa8f3934812ca48c55~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">0x02 取消暂存的更改</h1>
<blockquote>
<p>📌 有时候暂存了更改，尚未提交至仓库，如何取消暂存的更改？</p>
</blockquote>
<p>更改 <code>helloworld.html</code>，新增一条注释（错误内容）。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, World!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-comment"><!-- 新增一条注释，错误内容. 接下来将会重置它. --></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>git add</code>暂存更改。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git add helloworld.html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检查工作目录状态，显示更改已被暂存且准备提交。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8a165c1af4f4fb19ee725bb082d26ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">git reset</h2>
<p>使用 <code>git reset</code> 命令重置 <code>HEAD</code> 中暂存区的内容，清除已经暂存的更改。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git reset HEAD helloworld.html
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42bc8ab16ddb4962a283a0f2eb986a17~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>git reset</code>命令默认不会更改工作目录。所以在工作目录中文件仍存在已更改。若要移除这些更改，可以使用之前示例中的 checkout 或 restore 命令。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git checkout helloworld.html  <span class="hljs-comment"># git restore helloworld.html</span>
$ git st
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在工作目录又变干净了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2182eb3728b44852891484e885e97b14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">0x03 撤销提交的更改</h1>
<blockquote>
<p>📌 有时候发现已经提交至本地仓库的更改不正确并想撤销该提交？</p>
</blockquote>
<p>更改 <code>helloworld.html</code> 文件并提交</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, World!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-comment"><!-- 我不想提交这个更改. --></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>暂存更改并提交。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git add helloworld.html
$ git commit -m <span class="hljs-string">"这个更改不想提交"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/371e5adc04ea45748a598812a1fc8170~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">git revert 还原提交</h2>
<p><code>git revert</code>命令还原操作就是Git会生成一个新提交的选项，提交将会撤消一个已存在提交的所有修改。</p>
<p>因为将撤销最后一次提交，所以使用 HEAD作为还原的参数。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git revert HEAD
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行命令将进入到编辑器中。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8219e62ea1284e56808c5740667a8a9b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>最新三次提交参数 (<code>HEAD</code>, <code>HEAD^</code>, <code>HEAD~2</code>)</p>
</blockquote>
<p>若不打开编辑器，命令中添加 --no-edit 。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git revert HEAD --no-edit
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a5ed6587a4d49d3a45d40c519218208~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看日志纪录，可以看到原始提交纪录和“撤销”还原操作提交纪录。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6011406622224f449179cb4e7f187067~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">0x04 移除分支提交纪录</h1>
<blockquote>
<p>📌 如何将提交纪录移除？</p>
<p>当使用<code>git revert</code>进行还原提交，移除错误操作，恢复代码，但是历史纪录中仍会显示还原提交纪录和错误提交纪录。若涉及敏感文件时，即使还原操作后，但是历史纪提交录中仍能看到文件内容，涉及数据安全问题。</p>
</blockquote>
<p>首先将最新的提交打上标签，查看项目提交历史。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git tag unwanted 
$ git hist 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fefa51244154154a81610e6ead2b5b3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">git reset --hard</h2>
<p>查看日志纪录，标签“v1”之后的提交都是错误提交纪录和原提交纪录。可以使用 <code>git reset</code> 命令重置当前分支到制定提交，可以使用标签名或提交hash。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git reset --hard v1
$ git hist  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行命令后 <code>master</code>分支指向标签为v1的提交，错误的提交还原纪录都看不到了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0062b362154847c18219f58bf24fc445~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>🚨 <code>--hard</code> 标记是 reset 命令唯一的危险用法。它强制覆盖了工作目录中的文件，会真正地销毁数据，无法撤销。</p>
</blockquote>
<p>错误的提交还原纪录并没有消失，仍然在仓库中，只能使用哈希值引用它们。使用<code>git log -all</code>查看全部纪录。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/485e7b1d4a714d898c044eb30ba224ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">移除标签</h2>
<p>仓库会保留未引用的提交会一段时间直到垃圾回收运行。通过移除标签释放引用，将<strong>错误提交还原提交纪录</strong>作为垃圾被回收。</p>
<pre><code class="hljs language-bash copyable" lang="bash">git tag -d unwanted
git hist --all     
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时历史纪录干干净净的，没留下一点痕迹。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4bc526fac444dcea21557e9bfb592e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">0x05 📚参考</h1>
<p><a href="https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E7%BD%AE%E6%8F%AD%E5%AF%86#_git_reset" target="_blank" rel="nofollow noopener noreferrer">“git_reset”, Pro_git_v2_zh ebook</a></p>
<h1 data-id="heading-12">0x06  关注专栏</h1>
<p>此文章已收录到专栏中 👇，可以直接关注。</p>
<p>更多文章继续阅读｜系列文章持续更新</p></div>  
</div>
            