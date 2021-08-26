
---
title: '深入 Git 和开发规范（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2583eacd46e45ca91036d633e627660~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 13:18:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2583eacd46e45ca91036d633e627660~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">除了 Git 三连，实际工作中还有哪些常用操作</h2>
<h3 data-id="heading-1">git checkout--创建、切换分支，放弃本地修改</h3>
<p>checkout 命令在分支操作上经常使用，同时支持本地文件的操作
创建并切换到新分支：</p>
<pre><code class="hljs language-git copyable" lang="git">git checkout <branch> // 切换到分支

git chekcout - // 切换到上一次使用的分支

git checkout -b <branch> // 创建并切换
<span class="copy-code-btn">复制代码</span></code></pre>
<p>放弃某个文件的修改：</p>
<pre><code class="hljs language-git copyable" lang="git">git checkout <file>

git checkout . // 放弃所有文件修改
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">git reset--回退历史版本</h3>
<p>Git 的另一特征便是可以灵活操作历史版本。借助分散仓库的优势，可以在不影响其他仓库的前提下对历史版本进行操作。
回退到某个历史提交：</p>
<pre><code class="hljs language-git copyable" lang="git">git reset <commit> // 回退到某个版本，不回退文件
git reset --hard <commit> // 回退到某个版本，并回退文件
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">git merge--合并分支</h3>
<p>当开发到一定程度后，需要将开发分支的代码合并到测试或者主干分支，这时候，需要用到 merge 命令。</p>
<pre><code class="hljs language-git copyable" lang="git">git merge <branch> // 合并某个分支到当前分支
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">git pull 的时候，发生了什么？</h3>
<p>很多人不理解 Git 的拉取<code>pull</code>和获取<code>fetch</code>的区别，其实当执行 <code>git pull</code> 的时候，经历了两个步骤，一个是获取<code>fetch</code>，并自动合并<code>merge</code>
而获取则支持单纯的执行<code>fetch</code>，并不会自动合并。
如下例子：</p>
<pre><code class="hljs language-git copyable" lang="git">git fetch origin master:temp //从远程仓库 master 获取，并建立本地分支 temp

git diff temp //对比修改

git merge temp //合并tmp
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">修改了文件，突然发现分支不对，怎么办？</h3>
<p>有时候当我们修改了文件后发现，分支忘了切回开发分支了，除了笨笨的复制文件，然后切换回正确分支，再恢复代码，还有更好的操作吗？
执行 git stash 暂存修改到缓存后，切换到正确分支，并将修改出栈：</p>
<pre><code class="hljs language-git copyable" lang="git">git stash // 暂存修改

git checkout <branch> // 切换分支

git stash pop // 将修改出栈（恢复）
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Git分支管理规范</h2>
<h3 data-id="heading-7">master 主分支</h3>
<blockquote>
<p>作为正式环境分支（稳定版），只读，不可修改，可被merge
正式服务器应当切换为此分支</p>
</blockquote>
<h3 data-id="heading-8">release 预发布分支</h3>
<blockquote>
<p>作为验收环境分支，不可修改，可被merge
验收或正式服务器上线前应当切换为此分支</p>
</blockquote>
<h3 data-id="heading-9">develop 测试分支</h3>
<blockquote>
<p>作为测试环境分支，可修改，可被merge
测试服务器应当切换为此分支</p>
</blockquote>
<h3 data-id="heading-10">feature/ 开发（功能）分支</h3>
<blockquote>
<p>作为开发环境分支，本地开发和开发服务器应当切换为此分支</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2583eacd46e45ca91036d633e627660~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">hotfix/ 修复BUG分支</h3>
<blockquote>
<p>作为修复BUG分支，应从线上或测试分支拉取一个hotfix分支，BUG解决后merge到测试或线上分支</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13a8948133144e67b0fc469db541eab2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">Git工作流模型推荐</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc4b2d780b5f49e3823645ae6cebfa53~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">欢迎阅读其它文章</h4>
<ul>
<li><a href="https://juejin.cn/post/6991566044674392078" target="_blank" title="https://juejin.cn/post/6991566044674392078">使用 Vite2+Vue3 实现网站国际化｜8月更文挑战</a></li>
<li><a href="https://juejin.cn/post/6991204669573824520" target="_blank" title="https://juejin.cn/post/6991204669573824520">实战：前端接口请求参数混淆</a></li>
<li><a href="https://juejin.cn/post/6975770170413776926" target="_blank" title="https://juejin.cn/post/6975770170413776926">实战：用 Vue3 实现一个 Message 消息组件</a></li>
<li><a href="https://juejin.cn/post/6981232153233195039" target="_blank" title="https://juejin.cn/post/6981232153233195039">实战：用 Vue3 实现 Image 组件，顺便支持懒加载</a></li>
<li><a href="https://juejin.cn/post/6968352814858764296" target="_blank" title="https://juejin.cn/post/6968352814858764296">One Piece，Vue.js 3.0 带来了哪些更新</a></li>
<li><a href="https://juejin.cn/post/6983625803271503886/" target="_blank" title="https://juejin.cn/post/6983625803271503886/">一篇文章消化 ES7、ES8、ES9 主要新特性</a></li>
<li><a href="https://juejin.cn/post/6979053938087723021" target="_blank" title="https://juejin.cn/post/6979053938087723021">技术团队普遍存在的问题和解决方案</a></li>
<li><a href="https://juejin.cn/post/6844903618810757128" target="_blank" title="https://juejin.cn/post/6844903618810757128">ES6中常用的10个新特性讲解</a></li>
<li><a href="https://juejin.cn/post/6983626263327932429" target="_blank" title="https://juejin.cn/post/6983626263327932429">上手后才知道 ，Vue3 的 script setup 语法糖是真的爽</a></li>
</ul></div>  
</div>
            