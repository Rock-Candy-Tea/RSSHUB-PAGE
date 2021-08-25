
---
title: 'Vue CLI 简易教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef6b160770294266a495f9d57155bc53~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 23:32:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef6b160770294266a495f9d57155bc53~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue CLI 是一个基于 Vue.js 进行快速开发的完整系统，称为脚手架工具。</p>
<p>使用 Vue CLI 具有以下优点：</p>
<ul>
<li>统一项目的架构风格</li>
<li>初始化配置项目依赖</li>
<li>提供单文件组件</li>
</ul>
<p>和 webpack 一样，Vue CLI 也是使用命令行进行操作的。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/" ref="nofollow noopener noreferrer">官方文档</a> 不那么容易看明白，所以让我们简化下吧！</p>
<h1 data-id="heading-0">安装</h1>
<p>安装之前需要确保安装了 node ，没有安装的可参考 <a href="https://juejin.cn/post/6939556120956502053#heading-5" target="_blank" title="https://juejin.cn/post/6939556120956502053#heading-5">node安装</a>，</p>
<p>然后使用命令行安装命令，我们这里使用 VS Code 终端输入命令操作，</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 安装</span>
npm install –g @vue/cli
<span class="hljs-meta">#</span><span class="bash"> 如果安装报错<span class="hljs-string">'源文本中存在无法识别的标记'</span>，则需要加引号</span>
npm install –g '@vue/cli'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为是全局安装，所以只需安装一次，后续直接使用即可。</p>
<p>查看版本</p>
<pre><code class="hljs language-shell copyable" lang="shell">vue --version
<span class="hljs-meta">#</span><span class="bash"> 升级版本</span>
npm update –g @vue/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">项目搭建</h1>
<p>创建项目：</p>
<pre><code class="hljs language-shell copyable" lang="shell">vue create project-demo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择Preset：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef6b160770294266a495f9d57155bc53~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择 Manually, 上下选择，按空格键选定自己需要的插件功能，</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a173dd4761644b09a31d00153be7036c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成后回车，后面是一系列你选择的插件的相关设置选择，</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ade032d0a1c464f80fefed09fb8c1cd~tplv-k3u1fbpfcp-watermark.image" alt="ScreenGif.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面最后一步是保存当前设置，我的命名为demo-preset1，默认保存位置在当前系统用户文件夹的<code>.vuerc</code>文件，比如<code>C:\Users\Administrator\.vuerc</code>，删除或修改文件即可对插件配置进行操作。</p>
<p>设置完成后就是一系列自动化安装，等待许久后，项目创建完成：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93f891aa08f44a768c4398c46c2a4482~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行项目：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 进入项目目录</span>
cd project-demo
<span class="hljs-meta">#</span><span class="bash"> 运行</span>
npm run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按住 Ctrl ，点击链接进行项目访问了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd788724c1414fc78882410d78790fd4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">目录与文件</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfffb73cb88c483596ed28d34b77fd45~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>单文件组件可以将组件的功能统一保存在以 .vue 为扩展名的文件中，统一存储在 components 文件夹中。</p>
<h1 data-id="heading-3">打包与部署</h1>
<h2 data-id="heading-4">打包</h2>
<p>打包就是将 Vue CLI 项目编译为浏览器可识别的文件。</p>
<p>在 VS Code 终端窗口按 Ctrl + C 退出项目运行，输入命令行命令,</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包完成，生成 dist 目录。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e68fc2c4f6342f59c0e1a82cd4c73e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">部署</h2>
<p>部署指的是将 Vue 项目 dist 目录部署到服务器上。</p>
<p>安装静态文件服务器：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install –g serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 dist 下通过 serve 命令部署</p>
<pre><code class="hljs language-shell copyable" lang="shell">cd dist

serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功部署。按住 Ctrl ，点击链接进行打包后的项目访问了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd7369ca00404b14b93a4f8de5f1ff2a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            