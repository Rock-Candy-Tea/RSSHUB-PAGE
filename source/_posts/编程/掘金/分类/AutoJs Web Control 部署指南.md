
---
title: 'AutoJs Web Control 部署指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a80ea9ab238743b3bb2052b9a8e28086~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 19:43:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a80ea9ab238743b3bb2052b9a8e28086~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<p><code>AutoJs Web Control</code> 是基于<code>nodejs</code> <code>typescript</code> <code>vuejs</code> 等前端语言开发的,可以实现Android手机免root的群控控制系统,本篇文章详细介绍如何编译及部署<code>AutoJs Web Control</code> 。</p>
<h4 data-id="heading-1">开源文档</h4>
<ul>
<li>
<p><a href="https://hyb1996.github.io/AutoJs-Docs/#/%C2%A0" target="_blank" rel="nofollow noopener noreferrer">Autojs 官方文档</a></p>
</li>
<li>
<p><a href="https://github.com/hyb1996/Auto.js" target="_blank" rel="nofollow noopener noreferrer">Autojs 源码</a></p>
</li>
<li>
<p><a href="https://github.com/zrk1993/autojs-web-control" target="_blank" rel="nofollow noopener noreferrer">Autojs Web Control（本片文章重点）</a></p>
<blockquote>
<p>AutoJs Web Control分成两部分，web是用户操作界面，server是服务端，分别编译传输到服务器部署启动即可。</p>
</blockquote>
</li>
</ul>
<h4 data-id="heading-2">环境要求</h4>
<ol>
<li><a href="https://nodejs.org/en/download/" target="_blank" rel="nofollow noopener noreferrer">nodejs</a></li>
<li><a href="https://www.jetbrains.com/webstorm/download/" target="_blank" rel="nofollow noopener noreferrer">webstorm</a>【其他开发工具也可以，我这里使用的是webstorm】</li>
<li><a href="https://git-scm.com/downloads" target="_blank" rel="nofollow noopener noreferrer">git</a></li>
<li><a href="https://www.mysql.com/downloads/" target="_blank" rel="nofollow noopener noreferrer">mysql</a></li>
</ol>
<h4 data-id="heading-3">环境搭建</h4>
<h5 data-id="heading-4">数据库环境</h5>
<ol>
<li>
<p>新建数据库，库名随自己喜好，这里为<code>autojs_control</code></p>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a80ea9ab238743b3bb2052b9a8e28086~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
<li>
<p>导入数据库脚本</p>
<blockquote>
<p>文件位置：</p>
<p>autojs-web-control/cloud_auto.sql</p>
<p>autojs-web-control/update.sql</p>
</blockquote>
<img class="lazyload" src="https://s3.jpg.cm/2021/04/13/yOVjt.png" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
</ol>
<h5 data-id="heading-5">导入源码</h5>
<ol>
<li>
<p>使用<code>git</code>拉取源码</p>
<blockquote>
<p>git clone <a href="https://github.com/zrk1993/autojs-web-control.git" target="_blank" rel="nofollow noopener noreferrer">github.com/zrk1993/aut…</a></p>
</blockquote>
</li>
<li>
<p>导入<code>Webstorm</code></p>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a456aecf8f2495e9fd45e869b436e19~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
<li>
<p>修改数据库连接</p>
<blockquote>
<p>文件位置：</p>
<p>autojs-web-control\server\utils\db.ts</p>
</blockquote>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fec359a630684940b9b926bddccea896~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
</ol>
<h5 data-id="heading-6">部署服务端</h5>
<ol>
<li>
<p>进入<code>autojs-web-control/server/</code>目录</p>
</li>
<li>
<p>执行<code>npm install</code> 生成<code>node_modules</code> 目录</p>
</li>
<li>
<p>修改编译文件输出目录,</p>
<blockquote>
<p>autojs-web-control\server\tsconfig.json</p>
<pre><code class="copyable">"outDir": "./"调整为 "outDir": "./dest"
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</li>
<li>
<p>执行 <code>npm run build</code> 编译</p>
</li>
<li>
<p>增加<code>start</code> 命令脚本</p>
<blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-string">"scripts"</span>: &#123;
 <span class="hljs-string">"build"</span>: <span class="hljs-string">"tsc -p tsconfig.build.json"</span>,
 <span class="hljs-string">"clean"</span>: <span class="hljs-string">"ts-clean"</span>,
 <span class="hljs-string">"lint"</span>: <span class="hljs-string">"tslint --fix -p tsconfig.json -c tslint.json"</span>,
 <span class="hljs-string">"start"</span>: <span class="hljs-string">"node ./modules/default/main.js"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</li>
<li>
<p>部署并启动</p>
<ul>
<li>
<p>新建文件夹<code>autojs_server</code></p>
</li>
<li>
<p>将 <code>modules</code> <code>node_modules</code> <code>package.json</code> <code>dest</code>下的所有目录拷贝到<code>autojs_server</code>下</p>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1303f7e1d5df44729ca27f9df0cefc53~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
<li>
<p>执行<code>npm start</code>命令启动服务端</p>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f66c6d5950145fca758fe9206022de9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
</ul>
</li>
</ol>
<h5 data-id="heading-7">部署Web端</h5>
<ol>
<li>
<p>进入<code>autojs-web-control/web/</code>目录</p>
</li>
<li>
<p>运行 <code>npm install</code> 命令安装文件</p>
</li>
<li>
<p>安装<code>vue</code></p>
<blockquote>
<p>npm install -g @vue/cli</p>
<p>vue add unit-jest</p>
</blockquote>
</li>
<li>
<p>编辑<code>autojs-web-control\web\.env.staging</code>文件，修改服务器连接地址（同一台服务器可不修改）</p>
<blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript">NODE_ENV = production

# just a flag
ENV = <span class="hljs-string">'staging'</span>

# base api
VUE_APP_BASE_API = <span class="hljs-string">'http://localhost:9317'</span> # 调整为服务器IP地址
VUE_APP_WS_HOST = <span class="hljs-string">'ws://localhost:9317'</span>  # 调整为服务器IP地址
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</li>
<li>
<p>如本地启动直接执行 <code>npm run dev</code>即可启动web程序，后续步骤为发布到服务器可跳过</p>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/762fcbae04d246378fa6474cff77a526~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
<li>
<p>执行<code>npm run build:stage</code> 生成<code>dest</code> 目录</p>
<blockquote>
<p>此步骤发布到服务器可选，如本地启动直接执行 <code>npm run dev</code>即可启动web程序,后续步骤不需要执行 </p>
</blockquote>
</li>
<li>
<p>拷贝<code>dest</code> 目录文件到服务器，发布即可。</p>
</li>
</ol>
<h5 data-id="heading-8">验证发布</h5>
<ol>
<li>
<p>访问<code>http://localhost:9528</code>进入登陆页</p>
<blockquote>
<p>默认用户名：admin</p>
<p>默认密码：123456</p>
<p>用户名和密码都可以在数据库【autojs_control.t_admin】中修改</p>
</blockquote>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdbe18b0d4bb413c93fc1c32384e1b09~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
<li>
<p>可以选择设备，执行脚本</p>
<img class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cba78833ac5741099f6a400cfa11854e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</li>
</ol>
<h4 data-id="heading-9">总结</h4>
<p>以上为 <code>Autojs Web Control</code> 部署的全部过程，如有疑问或交流，欢迎大家评论@我。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            