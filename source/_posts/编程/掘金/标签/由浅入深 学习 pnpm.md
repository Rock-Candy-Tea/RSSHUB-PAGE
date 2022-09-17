
---
title: '由浅入深 学习 pnpm'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4765779e50f6470b8a8403151506269c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 22:37:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4765779e50f6470b8a8403151506269c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Why pnpm</h1>
<blockquote>
<p>最近公司的项目迁移使用了<code>pnpm</code>这款包管理工具，正所谓知己知彼，百战不殆。就跟着这篇文章快速的学习一下<code>pnpm</code>吧</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/zh/" ref="nofollow noopener noreferrer">官网链接</a></p>
<h2 data-id="heading-1">指令快速学习</h2>
<pre><code class="hljs language-sh copyable" lang="sh">// 安装 pnpm
npm install -g pnpm
// or
yarn global add pnpm

// 查看版本
pnpm -v

// 查看帮助
pnpm -h

// 安装所有的包
pnpm install  // 别名  i

// 更新所有的包
pnpm update  // 别名  up

// 安装某一个包
pnpm add react      // dependencies
pnpm add eslint -D  // devDependencies

// 移除某一个包
pnpm remove react  // 别名  <span class="hljs-built_in">rm</span>、un、uninstall
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯嗯，已经学会了。这就去开发！</p>
<p>等等！这些和<code>yarn</code>，<code>npm</code>并没有什么区别呀，那我们为什么要使用 <code>pnpm</code>呢</p>
<h2 data-id="heading-2">Store</h2>
<h4 data-id="heading-3">介绍</h4>
<p>在 <code>pnpm</code>中有一个很重要的概念：<code>store</code>，这个单词我们很常见，在<code>pnpm</code>中，它的意思是一个全局的仓库，<code>pnpm</code>他会把包缓存到<code>store</code>中，我们要安装包的时候<strong>并不是</strong>优先联网下载的，是先读取的这个<code>store</code>。</p>
<p>我们安装包到 <code>node_modules</code>的过程如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4765779e50f6470b8a8403151506269c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917121328485" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装包的时候会同时的去看 <code>node_modules</code>以及<code>store</code></p>
<ul>
<li>两个都没有的时候会联网下载</li>
<li><code>store</code>有， <code>node_modules</code>没有，会从<code>store</code>中复制过去</li>
<li><code>store</code>没有， <code>node_modules</code>有，也会补充<code>store</code></li>
</ul>
<h4 data-id="heading-4">store有关的指令</h4>
<pre><code class="hljs language-arduino copyable" lang="arduino"><span class="hljs-comment">// 读取 store的位置</span>
pnpm config get store-dir   <span class="hljs-comment">// 默认是当前磁盘下的.pnpm-store的文件夹中</span>

<span class="hljs-comment">// 设置 store的位置</span>
pnpm config set store-dir <span class="hljs-string">"D:\env\.pnpm-store"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">store的体现</h4>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-comment">// 创建文件夹</span>
mkdir test-pnpm
<span class="hljs-comment">// 进入</span>
cd test-pnpm
<span class="hljs-comment">// 初始化文件夹为一个npm项目</span>
pnpm <span class="hljs-keyword">init</span>   Or   npm <span class="hljs-keyword">init</span> -y
<span class="hljs-comment">// 安装 express</span>
pnpm <span class="hljs-keyword">add</span> express
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行规程如图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9be1a121f3104ab7aabb93e2dbc177f8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917115538600" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们发现在 <code>pnpm add</code>完成的时候，他会告诉我们 <code>store</code>的地址，还有一个 <code>Virtual store</code> 的地址，这个就是当前目录下的<code>node_modules/.pnpm</code>，这里路径上有一个 <code>.pnpm</code>后面在讨论。</p>
<p>在最后输出了这样一句话</p>
<pre><code class="hljs language-sh copyable" lang="sh">// 这里和截图不同是因为我多次下载了请忽略~

Progress: resolved 57, reused 0, downloaded 57, added 57, <span class="hljs-keyword">done</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们解析一下</p>
<ul>
<li><code>resolved 57</code>，在下载 <code>express</code>这一个包的时候，<strong>解析</strong>出来这个包以及它的依赖，总共有57项。</li>
<li><code>reused 0</code>，<code>store</code>中的包<strong>重复使用</strong>了0次，毕竟我们这是第一次下载，重用是0没毛病。</li>
<li><code>downloaded 57</code>，<strong>联网下载</strong>了 57 个包</li>
<li><code>added 57</code>，<strong>添加到 store 中</strong>包有57项</li>
</ul>
<p>OK，具体这些怎么体现我们可以</p>
<ul>
<li>新建一个项目在安装 <code>express</code> 可以体现出 <code>reused</code></li>
<li>删掉 <code>node_modules</code>在下载可以体现 <code>reused</code></li>
<li>不删 <code>node_modules</code>，删掉 <code>store</code>文件夹可以体现 <code>added</code></li>
<li>删掉 <code>node_modules</code>，删掉 <code>store</code>文件夹可以体现 <code>downloaded</code></li>
</ul>
<h4 data-id="heading-6">小总结</h4>
<p>那么到这里，我们可以了解到，<code>pnpm</code>是使用了一个 <code>store</code> 机制，让我们下载包的速度极大的提升了</p>
<h2 data-id="heading-7">pnpm 的 node_modules解析</h2>
<p><code>pnpm</code>的优异之处不仅仅是使用了<code>store</code> 加快了下载数据，还有它的<code>node_modules</code>也很有意思</p>
<p>Tip: 我们安装包是安装到当前项目的 <code>node_modules</code> 下，写代码 <code>import/require</code> 找包是<code>node</code>的机制，它找依赖是一层层的向上找<code>node_modules</code>，这里我们只去了解<code>node_modules</code> 即可，与上面的 <code>store</code> 完全无关</p>
<h3 data-id="heading-8">node_modules历史</h3>
<h3 data-id="heading-9">npm2 的node_modules</h3>
<p>最早版本：npm2</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d2a0045cf404fbe872164a7a57571eb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917130244357" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个时候我们安装一下 express，node_modules是只有一个 express文件夹的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b48a84528f7043aab712d6b42092a4ea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917132521207" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是展开后我们就很容易发现问题了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c3a658837c47cb9865630dff0df39b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917130558986" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们安装的  <code>node_modules</code> 中有<code>express</code></p>
<p><code>express</code>有它自己的 <code>node_modules</code></p>
<p><code>express</code>依赖的包也有它的 <code>node_modules</code></p>
<p>依赖的包也有它依赖包的包。。。。反正就这样一直嵌套下去了</p>
<p>这里会有以下几个问题</p>
<ul>
<li>安装 <code>A</code> <code>B</code>两个包，这两个包都依赖了<code>C</code>，这个时候 <code>C</code>就会被安装两遍，即 公共依赖会被多次安装</li>
<li><code>windows</code> 的文件路径最长是 260 多个字符，嵌套的文件结构一直嵌套下去肯定是不行的</li>
</ul>
<p>当时 <code>npm</code> 还没解决，社区就出来新的解决方案了，就是 <code>yarn</code></p>
<h3 data-id="heading-10">yarn 的node_modules</h3>
<p><code>yarn</code> 解决嵌套的思路是将嵌套依赖<strong>打散</strong>到同一层，这样也就没有依赖重复多次的问题了，路径过长的问题了。</p>
<p>使用<code>yarn</code> 安装<code>express</code>的文件夹结构如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12a81b10c5c44f29aa7b53c16c7c654~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917131505232" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样的打散做法很好，但不是绝对的</p>
<p>比如</p>
<p>我们安装 <code>A</code> <code>B</code> 包</p>
<p><code>A</code>依赖 <code>1.0.0</code> 版本的<code>C</code>包</p>
<p><code>B</code>依赖 <code>2.0.0</code> 版本的<code>C</code>包</p>
<p>这个时候项目 <code>node_modules</code> 目录里面会有 <code>A</code> <code>B</code> <code>C</code> 包，<code>C</code> 包的版本是取决于安装过程先解析的是<code>A</code>还是<code>B</code></p>
<p>。如果先解析的是<code>A</code>，则项目<code>node_modules</code> 目录中的<code>C</code>包版本是<code>1.0.0</code>，在<code>B</code>包中依然会存在 <code>node_modules</code>文件夹 ，在<code>B</code>包的<code>node_modules</code> 中依赖  <code>2.0.0</code> 版本的<code>C</code>包</p>
<p>如果先解析的<code>B</code>，同理。</p>
<p>这样感觉也很合理，但是有一个致命的问题，叫幽灵依赖。</p>
<p>我们依赖的是 <code>A</code> <code>B</code>，但是我们在代码中是可以写 <code>require("C")</code>的，也就是打散的过程中，将不是我们的依赖也打散到<code>node_modules</code>中了，导致我们可以引入到<code>C</code>包</p>
<p>并且，并没有实质性的解决我们重复依赖导致包被多次安装，占用重复的空间。</p>
<p>还是上面的例子，打散的是<code>1.0.0</code>的<code>C</code>包，如果还有一个<code>D</code>包依赖<code>2.0.0</code>的<code>C</code>包，则 <code>2.0.0</code>的<code>C</code>包在 安装<code>B</code>包和<code>D</code> 包的过程中会被安装两次！</p>
<h3 data-id="heading-11">pnpm 的node_modules</h3>
<p>我们来看一下 pnpm 的做法</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6de8eff8094742ee91770b7067981a8b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917132821938" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先 <code>node_modules</code> 中只有一个 <code>express</code> 目录，但是我们发现后面多了一个链接符号，也就是说它真正的位置是不在这里的，这里只是一个软连接，保证我们在写  <code>require("express")</code> 的时候不会报错，这样的作法就解决了幽灵依赖的问题。</p>
<p>这个时候我们发现有一个 <code>.pnpm</code>的文件夹，这个文件夹的秘密就太多了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4161152c2da2435cb640853915e67368~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="image-20220917133226801" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们一点点来解密这个 <code>.pnpm</code> 目录</p>
<ol>
<li><code>pnpm</code>的思路是将所有包，以及包依赖的包，等嵌套依赖的包，全部打散到 <code>.pnpm</code>目录中，为了解决重复安装相同版本的包的问题，他将包的<strong>版本</strong>也写到了文件名中。</li>
<li>我们安装的<code>express</code>，在项目的<code>node_modules</code>目录中它是一个软连接，链接到了 <code>.pnpm</code> 目录中 <code>.pnpm/express@4.18.1/node_modules/express</code> 目录
<ol>
<li>注意一下这个文件结构， <code>.pnpm</code> 中 是带版本号的 文件夹，这个目录中会有一个 <code>node_modules</code>，在这里会有一个<strong>包名</strong>的文件夹，这个文件夹中才是<strong>真正源代码</strong>所在的目录</li>
</ol>
</li>
<li>那我们发现，<code>.pnpm/express@4.18.1/node_modules/</code>这个目录下，<code>express</code>目录是真实源代码所在地，跟他同级还有很多的软连接。这个软连接表示的是 <code>express</code>这个包依赖的包
<ol>
<li>那  <code>express</code>这个包依赖的包，现在是一个软连接，那他真实的路径在哪呢？</li>
<li>可以发现，他被打散到 <code>.pnpm</code> 中了，会有一个 <code>包名@版本号</code> 的文件夹，比如 <code>express</code>依赖的 <code>accepts</code>这个包，他真实的源代码是在<code>.pnpm/accepts@1.3.8/node_modules/accepts</code>文件夹下</li>
</ol>
</li>
</ol>
<p>那我们就发现了</p>
<ul>
<li><code>pnpm</code>会把所有的依赖打散到  <code>.pnpm</code>目录下，会带上版本号</li>
<li>在这个带版本号的文件夹下有一个 <code>node_modules</code></li>
<li>这个 <code>node_modules</code>中只有两种情况，一个是包名文件夹，这里是真实的源代码，包依赖的包会在当前<code>node_modules</code>下以软连接的方式，连接到 <code>.pnpm/包名@版本/node_modules/包名</code>这个目录中</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">test-pnpm\node_modules\express  // 这个是软连接，实际的地址如下

test-pnpm\node_modules\.pnpm\express@4.18.1\node_modules\express


// express 依赖的包 会在 下面这个目录里面生成 软连接
test-pnpm\node_modules\.pnpm\express@4.18.1\node_modules\依赖包名

// 对应的真实地址是
test-pnpm\node_modules\.pnpm\依赖包名@版本\node_modules\依赖包名
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">总结</h2>
<p><code>pnpm</code>的最大特点有两个</p>
<ol>
<li>使用 <code>store</code> 全局的缓存了包，能在安装包的时候联网下载也能从 项目的 <code>node_modules</code> 进行备份</li>
<li>在  <code>.pnpm</code> 文件夹，创建 <code>包名@版本号</code>文件夹，以及软连接的方式，杜绝了一个版本的包被多次安装的问题，<code>monoreport</code>类型的项目更加能体现出它的优势</li>
</ol></div>  
</div>
            