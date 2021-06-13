
---
title: 'Git从放弃到入门(一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1c4af986b04f6cb9eaa371278b6dc3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 07:25:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1c4af986b04f6cb9eaa371278b6dc3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>🎏 这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<h1 data-id="heading-0">0x.00 前言</h1>
<p><strong>Git</strong> 是一个功能强大、复杂的分布式<code>VCS(version control system)</code>版本控制系统。Git 是针对开源项目的开发模式设计的，它的速度飞快，极其适合管理大项目，有着令人难以置信的非线性分支管理系统。它的出现改变了软件开发流程，大大地提高了开发流畅度。随着Git代码托管服务越来越流行(github、gitlab、gitee)，Git 成为了当今主流源代码管理首选，很多公司、个人将项目上传至 Git平台进行代码托管。</p>
<p>Git优缺点如此明显，爱它的人爱死，恨它的人恨死。它功能强大毋庸置疑，但是它概念繁多复杂且命名随意、命令行语法命名随意且不一致、命令行帮助提示晦涩难懂、缺乏良好的封装等等缺点让人无力吐槽。</p>
<p>虽然一般情况下只需要掌握git的几个常用命令即可满足日常开发，但是在使用的过程中难免会遇到各种复杂的情况，不得不面对底层实现的，这时候经常需要搜索命令参数，非常麻烦，让初学者头大。</p>
<p>每次代码合并提交时都是心跳加速的时候！我的代码哪里去了呢？ 咋没保存成功？！白忙活了！ 怎么办还能找回吗？ 返回的提示信息啥意思啊 我到底需要干什么啊？....</p>
<p>瑕不掩瑜，优秀的工具软件还是需要学习掌握的。通过接下来的Git常用命令学习，降低学习曲线，完成快速入门。</p>
<h1 data-id="heading-1">0x.01 环境安装</h1>
<p><a href="https://git-scm.com/" target="_blank" rel="nofollow noopener noreferrer">Git官网</a> 提供了下载、文档和其他资源：</p>
<ul>
<li><a href="https://git-scm.com/book/zh/v2" target="_blank" rel="nofollow noopener noreferrer">Pro Git 中文版</a></li>
<li><a href="https://git-scm.com/downloads/guis/" target="_blank" rel="nofollow noopener noreferrer">Git Gui 客户端</a></li>
</ul>
<h2 data-id="heading-2">Windows</h2>
<p>操作系统是 <code>Windows</code>，下载<a href="https://gitforwindows.org/" target="_blank" rel="nofollow noopener noreferrer">git for windows</a>进行安装。</p>
<h2 data-id="heading-3">Mac</h2>
<p>操作系统是 <code>Mac OS</code> , 使用 <code>brew</code> 命令来安装。<a href="https://git-scm.com/download/mac" target="_blank" rel="nofollow noopener noreferrer">git for MacOS </a></p>
<pre><code class="hljs language-bash copyable" lang="bash">$ brew install git 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">git --version 版本确认</h2>
<p>使用 <code>git --version</code> 命令查看环境是否成功安装，返回版本信息。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git --version

git version 2.28.0
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">0x.02  git config 配置</h1>
<h2 data-id="heading-6">用户信息</h2>
<p>安装完 Git 之后，要做的第一件事就是设置你的用户名和邮件地址。 这一点很重要，因为每一个 Git 提交都会使用这些信息，它们会写入到你的每一次提交中，不可更改。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ git config --global user.name <span class="hljs-string">"your name"</span>
$ git config --global user.email <span class="hljs-string">"your_email@xxx.com"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">检查配置信息</h2>
<p>使用 git config --list 命令来列出所有 Git 配置。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//查看所有配置项</span>
$ git config -l , --list  
...
user.name=Anduril
user.email=egger@outlook.com
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">core.autocrlf</h2>
<p>解决跨平台格式化不同导致的各种问题。Windows 使用回车（CR）和换行（LF）两个字符来结束一行，而 macOS 和 Linux 只使用换行（LF）一个字符,会极大地扰乱跨平台协作。</p>
<p><strong>Unix/Mac用户</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 提交时转换为LF,检出时不转换</span>
$ git config --global core.autocrlf input
<span class="hljs-comment"># 提交包含混合换行符的文件时给出警告</span>
$ git config --global core.safecrlf warn
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Windows 用户</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 提交时转换为LF,检出时转换CRLF</span>
$ git config --global core.autocrlf <span class="hljs-literal">true</span>
<span class="hljs-comment"># 提交包含混合换行符的文件时给出警告</span>
$ git config --global core.safecrlf warn
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">0x.03 创建项目</h1>
<p>接下来从头开始创建 git 仓库(repository)。</p>
<h2 data-id="heading-10">创建目录/文件</h2>
<p>创建一个名为<code>helloworld</code>的空目录，然后在该目录中创建一个包含以下内容的文件 <code>helloworld.html</code>。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ mkdir helloworld
$ <span class="hljs-built_in">cd</span> helloworld
 
// 新建 helloworld.html，内容如下
Hello, World!
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">git init 初始化仓库</h2>
<p>运行<code>git init</code>初始化仓库。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1c4af986b04f6cb9eaa371278b6dc3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加页面到仓库中并提交。</p>
<pre><code class="hljs language-bash copyable" lang="bash">git add helloworld.html
git commit -m <span class="hljs-string">"首次提交"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a629523ede454489935fbf75f83830c0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-12">0x.04 git status 检查存储库的状态</h1>
<p>运行 <code>git status</code>  检查存储库的当前状态。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb1b0b82537942cbbf16b270ed5c191a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-13">0x.05 进行更改</h1>
<p>更改<code>helloworld.html</code>页面内容。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, World!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>git status </code>检查工作目录的状态。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731e135e8c164cf7b0f0bea12f34a591~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>返回结果内容</p>
<ol>
<li><code>helloworld.html</code>文件已更改，但尚未提交到存储库 。</li>
<li>提示下一步操作。提交 <code>git add <file></code> 或者撤销 <code>git restore <file></code> 更改。</li>
</ol>
<h1 data-id="heading-14">0x.06 暂存更改</h1>
<p>暂存更改，然后检查状态</p>
<pre><code class="copyable">git add helloworld.html
git status
<span class="copy-code-btn">复制代码</span></code></pre>
<p>helloworld.html 已暂存。 它在存储库中不是永久性的。 可以使用  <code>git reset HEAD <file>...</code> 取消暂存这些更改。</p>
<h1 data-id="heading-15">0x.07  暂存提交</h1>
<p>分离暂存和提交，可以轻松自定义提交内容。暂存步骤允许您继续对工作目录进行更改，当您需要与版本控制交互时，可以在提交中记录更改。</p>
<p>假设您已编辑了三个文件。你可以一次提交所有更改，也可以分开单独提交。</p>
<pre><code class="copyable">git add a.html
git add b.html
git commit -m "a和b的更改"
git add c.html
git commit -m "c单独更改"
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">0x.08 提交更改</h1>
<p>提交到仓库中
<code>git commit</code>  增加 -m 标识可以提交描述信息。
直接输入<code>git commit</code> 默认编辑器会打开 <code>COMMIT_EDITMSG</code> 文件，输入提交信息,关闭文件后提交成功(如果空信息则终止提交).
编辑器打开顺序</p>
<ul>
<li>GIT_EDITOR environment variable</li>
<li>core.editor configuration setting</li>
<li>VISUAL environment variable</li>
<li>EDITOR environment variable</li>
</ul>
<h1 data-id="heading-17">0x.09 更改而不是文件</h1>
<p>git处理更改，而不是文件。
大多数版本控制系统处理文件。您将文件添加到源代码控制中，系统将从那一刻起跟踪更改。
Git关注的是对文件的更改，而不是文件本身。git add file 命令并没有告诉git将文件添加到存储库中，而是记录文件的当前状态，以便稍后提交。</p>
<p>更改 helloworld.html 内容</p>
<pre><code class="copyable"><html>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>git add hello.html</code>  暂存下更改。</p>
<p>再次修改 helloworld.html 内容</p>
<pre><code class="copyable"><html>
  <head>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>git status</code>  查看当前状态</p>
<p>hello.html 在状态中列出了两次。第一个更改已经暂存并准备提交。第二个更改未暂存。如果您现在进行提交，则不会将头文件保存到存储库中</p>
<p>我们做下验证</p>
<pre><code class="copyable">git commit -m "添加HTML tags"
git status
<span class="copy-code-btn">复制代码</span></code></pre>
<p>仍提示由更改尚未暂存。</p>
<pre><code class="copyable"># 将当前目录所有更改暂存最便捷方法。 
git add .    
# 检查状态 确保不会添加任何不应添加的文件
git status
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提交更改</p>
<pre><code class="copyable">git commit -m "添加 HTML header"
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-18">0x.10  提交历史</h1>
<pre><code class="copyable">git log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不传入任何参数的默认情况下，<code>git log</code> 会按时间先后顺序列出所有的提交，最近的更新排在最上面。</p>
<p>参数<code> --pretty</code>可以使用不同于默认格式的方式展示提交历史。 <code>oneline</code> 会将每个提交放在一行显示，在浏览大量的提交时非常有用。 另外还有 short，full 和 fuller 选项，它们展示信息的格式基本一致，但是详尽程度不一。</p>
<pre><code class="copyable">git log --pretty=oneline
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有许多选项参数可以控制日志展示结果</p>
<pre><code class="copyable">git log --pretty=oneline --max-count=2
git log --pretty=oneline --since='5 minutes ago'
git log --pretty=oneline --until='5 minutes ago'
git log --pretty=oneline --author=<your name>
git log --pretty=oneline --all
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制输输出日志格式化</p>
<pre><code class="copyable">git log --all --pretty=format:"%h %cd %s (%an)" --since='7 days ago' --author=anduril
# 最合适的日志格式  
git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>git log --pretty=format </code>常用的选项</p>
<ul>
<li>%H 提交的完整哈希值</li>
<li>%h 提交的简写哈希值</li>
<li>%d 提交装饰（例如 (HEAD -> master)）</li>
<li>%T 树的完整哈希值</li>
<li>%t 树的简写哈希值</li>
<li>%P 父提交的完整哈希值</li>
<li>%p 父提交的简写哈希值</li>
<li>%an 作者名字</li>
<li>%ae 作者的电子邮件地址</li>
<li>%ad 作者修订日期（可以用 --date=选项 来定制格式）</li>
<li>%ar 作者修订日期，按多久以前的方式显示</li>
<li>%cn 提交者的名字</li>
<li>%ce 提交者的电子邮件地址</li>
<li>%cd 提交日期</li>
<li>%cr 提交日期（距今多长时间）</li>
<li>%s 提交说明</li>
<li>--graph告诉 git 以 ASCII 图形布局的形式显示提交树</li>
<li>--date=short 保持日期格式简短美观</li>
</ul>
<p>👋 本文到此就结束了！后续文章将会继续学习Git命令操作。</p>
<h1 data-id="heading-19">0x.11 📚 参考</h1>
<p><a href="https://git-scm.com/book/zh/v2" target="_blank" rel="nofollow noopener noreferrer">Pro Git Online</a></p></div>  
</div>
            