
---
title: 'Node.js的安装与配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c061cac49d274ec7a12a85e2c92aa390~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 04:13:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c061cac49d274ec7a12a85e2c92aa390~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是Node.js？</h1>
<blockquote>
<p>简单的说 Node.js 就是运行在服务端的 JavaScript。 Node.js 是一个基于Chrome JavaScript
运行时建立的一个平台。
Node.js是一个事件驱动I/O服务端JavaScript环境，基于Google的V8引擎，V8引擎执行Javascript的速度非常快，性能非常好。</p>
</blockquote>
<p>Node.js 官方网站：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/" ref="nofollow noopener noreferrer">nodejs.org/en/</a>
<br></p>
<h2 data-id="heading-1">一、下载</h2>
<hr>
<p>官方下载地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fzh-cn%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/zh-cn/download/" ref="nofollow noopener noreferrer">nodejs.org/zh-cn/downl…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c061cac49d274ec7a12a85e2c92aa390~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h2 data-id="heading-2">二、安装</h2>
<hr>
<p>一直点击<code>next</code>就行了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45041904a2124a0582802857374ceced~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择安装位置</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0810680e6244ca68d0aeccb6fbee954~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加node.js到系统环境变量</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c2d3a62e1db446e9c04d1e02bff6a27~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装完成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03a04971a7854a19826e9999c4c53402~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结束</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eef3159c5bf5453ea2cc90c4eca156b3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装位置目录</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90af2470864e4c2e939b71e4d1eff2b1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h2 data-id="heading-3">三、测试</h2>
<hr>
<p>在Windows运行<code>cmd</code>命令：
<code>node -v</code>：查看node.js版本号；
<code>npm -v</code>：查看npm版本号；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/565d5884ef014eca92ca1e818c731885~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<br></p>
<h2 data-id="heading-4">四、修改全局依赖包下载路径</h2>
<hr>
<p>默认情况下，我们在执行<code>npm install -g XXXX</code>下载全局包时，这个包的默认存放路径位<code>C:\Users\用户名\AppData\Roaming\npm\node_modules</code>下，可以通过CMD指令<code>npm root -g</code>查看</p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> npm root <span class="hljs-literal">-g</span>
C:\Users\Bealei\AppData\Roaming\npm\node_modules
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是有时候我们不想让全局包放在这里，我们可以自定义存放目录，在<code>cmd</code>窗口执行以下两条命令修改默认路径：</p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> npm config <span class="hljs-built_in">set</span> prefix <span class="hljs-string">"D:\Code\npm"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> npm config <span class="hljs-built_in">set</span> cache <span class="hljs-string">"D:\Code\npm\node_cache"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h2 data-id="heading-5">五、配置path环境</h2>
<hr>
<p>因为我们修改了全局包的下载路径，那么自然而然，我们下载的全局包就会存放在 <code>D:\Code\npm\node_modules</code>，而其对应的 <code>cmd</code> 指令会存放在 <code>D:\Code\npm</code></p>
<p>我全局安装一个<code>vue-cli</code>脚手架：</p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> npm install @vue/<span class="hljs-built_in">cli</span> <span class="hljs-literal">-g</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我使用 <code>CMD</code> 命令 <code>vue create myproject</code> 指令创建一个项目，显示如下：</p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> vue create myproject
<span class="hljs-string">'vue'</span> 不是内部或外部命令，也不是可运行的程序
或批处理文件。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为我们在执行指令时，它会默认在<code>node</code>安装根目录下查找指令文件，在这里就是<code>vue.cmd</code>,然后还会在<code>node</code>安装根目录下的<code>node_modules</code>下查找依赖包文件夹，在这里就是<code>@vue</code>文件夹，因为我们修改了全局包的存放路径，所以自然找不到了。</p>
<p>所以我们需要把我们指定的全局包存放路径添加到系统环境变量，这样就可以找到了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef1c5630875d4adabf5f6bfd6883a16f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再次测试一下，就成功啦</p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> vue create myproject
?  Your connection to the default npm registry seems to be slow.
   Use https://registry.npm.taobao.org <span class="hljs-keyword">for</span> faster installation? (Y/n)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            