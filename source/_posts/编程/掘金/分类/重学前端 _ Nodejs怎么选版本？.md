
---
title: '重学前端 _ Node.js怎么选版本？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2222aa3553b47658fd60dae61b33bf6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 00:53:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2222aa3553b47658fd60dae61b33bf6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>学习使用Node.js的第一步，就是下载安装，但是面对众多版本，应该怎么选，又为什么要这么选你都知道吗？</p>
<h1 data-id="heading-0">Node.js版本介绍</h1>
<h2 data-id="heading-1">安装</h2>
<p>Node.js是一个基于Google V8引擎的、跨平台的JavaScript运行环境</p>
<p>直接官网下载安装👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fzh-cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/zh-cn/" ref="nofollow noopener noreferrer">官网地址</a></p>
<h2 data-id="heading-2">版本介绍</h2>
<h3 data-id="heading-3">怎么选？</h3>
<p>在官网下载的时候会看到LTS和Current两个版本可以下载，怎么选？</p>
<p>简单的说就是【选LTS】</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2222aa3553b47658fd60dae61b33bf6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828152251539" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">为什么这么选？</h3>
<p><strong>LTS和Current的解释</strong></p>
<p>首先LTS和Current并不是版本，而是同一个主版本号的不同阶段（”主版本号“是指semver-major)。</p>
<p><strong>Current</strong>：</p>
<p>一个新主版本号release后，先进入Current阶段，该阶段持续6个月，目的是给各个库(library)的作者时间来支持新版。六个月之后，奇数版本（诸如 9、11 等）将变为不支持状态，只有偶数版本（诸如 10、12 等）变成 <em>Active LTS</em> 状态，并且准备投入使用（每年的 4 月发布偶数版本、10 月发布奇数版本）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a71f64d108df40b1afffb5f58a1ee6c2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828160925277" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>LTS（Long Term Support）</strong>：</p>
<p><em>LTS</em> 发布版的状态是“长期维护版”。它分为两个阶段：<em>Active LTS</em>和<em>Maintenance LTS</em>。<em>Active LTS</em>阶段持续18个月，到期后进入<em>Maintenance LTS</em>版本，持续18个月，到期后进入 <em>EOL</em>版本，正式退出历史舞台。</p>
<h3 data-id="heading-5"><strong>生命周期</strong></h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1a4b064cca4a4499099971d335900a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828161222795" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6"><strong>总结</strong></h3>
<ul>
<li>
<p>如果是测试环境想尝试一些新特性，可以下载Current；</p>
</li>
<li>
<p>如果是生产环境，为了保证稳定性，应该选择LTS，并且可以在每年发布 Active LTS 版本的时候进行跟进升级，最迟更新时间不要超过30 个月，因为30个月之后就进入EOL了。</p>
</li>
</ul>
<h3 data-id="heading-7"><strong>一些术语解释</strong></h3>
<p><code>Active</code>：指正在积极维护和升级的版本系列，包括向后移植非破坏性功能和改进，解决错误以及修补安全漏洞。</p>
<p><code>Maintenance</code>：这是一个维护的 LTS 版本系列，直到它的生命周期终止，只会在短时间内收到错误修复和安全补丁</p>
<p><code>EOL</code>：EOL 是 End of Life 的首字母缩写，进入到 EOL 时间线的版本，将不在维护。</p>
<br>
<p><strong>顺带解释一下semver-major</strong></p>
<p><code>Semver</code>指Semver规范，Github 起草了一个具有指导意义的，统一的版本号表示规则，称为 Semantic Versioning(语义化版本表示)。该规则规定了版本号如何表示，如何增加，如何进行比较，不同的版本号意味着什么。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsemver.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://semver.org/" ref="nofollow noopener noreferrer">Semver官网</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsemver.org%2Flang%2Fzh-CN%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://semver.org/lang/zh-CN/" ref="nofollow noopener noreferrer">Semver官网中文版</a></p>
<p><code>major</code>指主版本号，版本格式：<code>主版本号.次版本号.修订号</code>，版本号递增规则如下：</p>
<ul>
<li>主版本号(major)：当你做了不兼容的 API 修改，</li>
<li>次版本号(minor)：当你做了向下兼容的功能性新增，可以理解为Feature版本，</li>
<li>修订号(patch)：当你做了向下兼容的问题修正，可以理解为Bug fix版本。</li>
</ul>
<blockquote>
<p>参考资料：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2Fabout%2Freleases%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/about/releases/" ref="nofollow noopener noreferrer">node releases</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2FRelease%23release-phases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/Release#release-phases" ref="nofollow noopener noreferrer">Node.js Release Working Group</a></p>
</blockquote>
<h1 data-id="heading-8">Node.js版本管理</h1>
<h3 data-id="heading-9">如何快速切换Node.js版本?</h3>
<br>
<p>有以下面几种方式:</p>
<p><strong><code>n</code>：一个npm全局的开源包，是依赖npm来全局安装、使用的</strong></p>
<p>你看没错，node有一个模块就叫<code>n</code>（起的好随意...），是专门用来管理node.js的版本的（这个方式比较常用）。</p>
<p><em>安装n模块</em></p>
<pre><code class="copyable">npm install -g n
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>查看安装版本</em></p>
<pre><code class="copyable">n --version
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>升级node.js到最新稳定版</em></p>
<pre><code class="copyable">n stable
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>升级任意版本</em>，n后面跟随版本号【<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Ftree%2Fmaster%2Fdoc%2Fchangelogs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/tree/master/doc/changelogs" ref="nofollow noopener noreferrer">版本号大全</a>】</p>
<pre><code class="copyable">n v14.17.5 或者 n 14.17.5
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>常用命令</em></p>
<pre><code class="copyable">查看node版本
node --version

查看npm 版本,检查npm 是否正确安装。
npm -v

安装cnpm (国内淘宝镜像源),主要用于某些包或命令程序下载不下来的情况
npm install cnpm -g --registry=https://registry.npm.taobao.org

列出已安装模块
npm list
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<p><strong><code>fnm</code>:快速简单，兼容性支持.node-version和.nvmrc文件</strong></p>
<p>这是一个内置了 Rust，用于 Node.js 多发布版本的快速便捷管理工具;</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fzh-cn%2Fdownload%2Fpackage-manager%2F%23fnm" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/zh-cn/download/package-manager/#fnm" ref="nofollow noopener noreferrer">fnm</a> 有跨版本的支持（macOS、Windows 以及 Linux），以及一系列衍生命令（Bash, Zsh, Fish, PowerShell, Windows 命令行）</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSchniz%2Ffnm" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Schniz/fnm" ref="nofollow noopener noreferrer">github地址</a></p>
<br>
<p><strong><code>nvm</code>:独立的软件包, Node Version Manager</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fzh-cn%2Fdownload%2Fpackage-manager%2F%23nvm" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/zh-cn/download/package-manager/#nvm" ref="nofollow noopener noreferrer">nvm</a>是一个只适用于Mac/Linux用户的项目，而nvm-windows则是其在windows平台的一个替代方案，两者有联系，但是各自独立的项目;</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcoreybutler%2Fnvm-windows%2Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/coreybutler/nvm-windows/releases" ref="nofollow noopener noreferrer">nvm-windows下载</a></p>
<h1 data-id="heading-10">结语</h1>
<p>如以上有错误的地方，请在评论区中指出！</p>
<hr>
<p>如果有收获的话，就留个<strong>赞</strong>鼓励一下吧！🍜</p></div>  
</div>
            