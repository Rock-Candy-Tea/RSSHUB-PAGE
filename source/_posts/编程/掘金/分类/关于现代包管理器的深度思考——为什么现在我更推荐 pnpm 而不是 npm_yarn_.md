
---
title: '关于现代包管理器的深度思考——为什么现在我更推荐 pnpm 而不是 npm_yarn_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27a9da5df7214075b0f02e9b93b596f0~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 22:26:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27a9da5df7214075b0f02e9b93b596f0~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这篇文章给大家分享一个业内一款出色的包管理器——<code>pnpm</code>。目前 GitHub 已经有 star 9.8k，现在已经相对成熟且稳定了。它由 npm/yarn 衍生而来，但却解决了 npm/yarn 内部潜在的 bug，并且极大了地优化了性能，扩展了使用场景。下面是本文的思维导图:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27a9da5df7214075b0f02e9b93b596f0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、什么是 pnpm ?</h2>
<p>pnpm 的<a href="https://pnpm.js.org/en/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>是这样说的:</p>
<blockquote>
<p>Fast, disk space efficient package manager</p>
</blockquote>
<p>因此，pnpm 本质上就是一个包管理器，这一点跟 npm/yarn 没有区别，但它作为杀手锏的两个优势在于:</p>
<ul>
<li>包安装速度极快；</li>
<li>磁盘空间利用非常高效。</li>
</ul>
<p>它的安装也非常简单。可以有多简单?</p>
<pre><code class="hljs language-js copyable" lang="js">npm i -g pnpm
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、特性概览</h2>
<h3 data-id="heading-2">1. 速度快</h3>
<p>pnpm 安装包的速度究竟有多快？先以 React 包为例来对比一下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c13ce7ad65e4345a2be7bd750187d51~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，作为黄色部分的 pnpm，在绝多大数场景下，包安装的速度都是明显优于 npm/yarn，速度会比 npm/yarn 快 2-3 倍。</p>
<p>对 yarn 比较熟悉的同学可能会说，yarn 不是有 <a href="https://classic.yarnpkg.com/en/docs/pnp/" target="_blank" rel="nofollow noopener noreferrer">PnP 安装模式</a>吗？直接去掉 node_modules，将依赖包内容写在磁盘，节省了 node 文件 I/O 的开销，这样也能提升安装速度。（具体原理见<a href="https://loveky.github.io/2019/02/11/yarn-pnp/" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a>）</p>
<p>接下来，我们以这样一个<a href="https://github.com/pnpm/benchmarks-of-javascript-package-managers" target="_blank" rel="nofollow noopener noreferrer">仓库</a>为例，我们来看一看 benchmark 数据，主要对比一下 <code>pnpm</code> 和 <code>yarn PnP</code>:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c63047cccdf74e5c82cc5d8c2aef995a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从中可以看到，总体而言，<code>pnpm</code> 的包安装速度还是明显优于 <code>yarn PnP</code>的。</p>
<h3 data-id="heading-3">2. 高效利用磁盘空间</h3>
<p>pnpm 内部使用<code>基于内容寻址</code>的文件系统来存储磁盘上所有的文件，这个文件系统出色的地方在于:</p>
<ul>
<li>
<p>不会重复安装同一个包。用 npm/yarn 的时候，如果 100 个项目都依赖 lodash，那么 lodash 很可能就被安装了 100 次，磁盘中就有 100 个地方写入了这部分代码。但在使用 pnpm 只会安装一次，磁盘中只有一个地方写入，后面再次使用都会直接使用 <code>hardlink</code>(硬链接，不清楚的同学详见<a href="https://www.cnblogs.com/itech/archive/2009/04/10/1433052.html" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a>)。</p>
</li>
<li>
<p>即使一个包的不同版本，pnpm 也会极大程度地复用之前版本的代码。举个例子，比如 lodash 有 100 个文件，更新版本之后多了一个文件，那么磁盘当中并不会重新写入 101 个文件，而是保留原来的 100 个文件的 <code>hardlink</code>，仅仅写入那<code>一个新增的文件</code>。</p>
</li>
</ul>
<h3 data-id="heading-4">3. 支持 monorepo</h3>
<p>随着前端工程的日益复杂，越来越多的项目开始使用 monorepo。之前对于多个项目的管理，我们一般都是使用多个 git 仓库，但 monorepo 的宗旨就是用一个 git 仓库来管理多个子项目，所有的子项目都存放在根目录的<code>packages</code>目录下，那么一个子项目就代表一个<code>package</code>。如果你之前没接触过 monorepo 的概念，建议仔细看看<a href="https://www.perforce.com/blog/vcs/what-monorepo" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a>以及开源的 monorepo 管理工具<a href="https://github.com/lerna/lerna#readme" target="_blank" rel="nofollow noopener noreferrer">lerna</a>，项目目录结构可以参考一下 <a href="https://github.com/babel/babel" target="_blank" rel="nofollow noopener noreferrer">babel 仓库</a>。</p>
<p>pnpm 与 npm/yarn 另外一个很大的不同就是支持了 monorepo，体现在各个子命令的功能上，比如在根目录下 <code>pnpm add A -r</code>, 那么所有的 package 中都会被添加 A 这个依赖，当然也支持 <code>--filter</code>字段来对 package 进行过滤。</p>
<h3 data-id="heading-5">4. 安全性高</h3>
<p>之前在使用 npm/yarn 的时候，由于 node_module 的扁平结构，如果 A 依赖 B， B 依赖 C，那么 A 当中是可以直接使用 C 的，但问题是 A 当中并没有声明 C 这个依赖。因此会出现这种非法访问的情况。但 pnpm 脑洞特别大，自创了一套依赖管理方式，很好地解决了这个问题，保证了安全性，具体怎么体现<code>安全</code>、规避非法访问依赖的<code>风险</code>的，后面再来详细说说。</p>
<h2 data-id="heading-6">三、依赖管理</h2>
<h3 data-id="heading-7">npm/yarn install 原理</h3>
<p>主要分为两个部分, 首先，执行 npm/yarn install 之后，<code>包如何到达项目 node_modules 当中</code>。其次，node_modules <code>内部如何管理依赖</code>。</p>
<p>执行命令后，首先会构建依赖树，然后针对每个节点下的包，会经历下面四个步骤:</p>
<ul>
<li>
<ol>
<li>将依赖包的版本区间解析为某个具体的版本号</li>
</ol>
</li>
<li>
<ol start="2">
<li>下载对应版本依赖的 tar 包到本地离线镜像</li>
</ol>
</li>
<li>
<ol start="3">
<li>将依赖从离线镜像解压到本地缓存</li>
</ol>
</li>
<li>
<ol start="4">
<li>将依赖从缓存拷贝到当前目录的 node_modules 目录</li>
</ol>
</li>
</ul>
<p>然后，对应的包就会到达项目的<code>node_modules</code>当中。</p>
<p>那么，这些依赖在<code>node_modules</code>内部是什么样的目录结构呢，换句话说，项目的依赖树是什么样的呢？</p>
<p>在 <code>npm1</code>、<code>npm2</code> 中呈现出的是嵌套结构，比如下面这样:</p>
<pre><code class="hljs language-js copyable" lang="js">node_modules
└─ foo
   ├─ index.js
   ├─ package.json
   └─ node_modules
      └─ bar
         ├─ index.js
         └─ package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 <code>bar</code> 当中又有依赖，那么又会继续嵌套下去。试想一下这样的设计存在什么问题:</p>
<ol>
<li>依赖层级太深，会导致文件路径过长的问题，尤其在 window 系统下。</li>
<li>大量重复的包被安装，文件体积超级大。比如跟 <code>foo</code> 同级目录下有一个<code>baz</code>，两者都依赖于同一个版本的<code>lodash</code>，那么 lodash 会分别在两者的 node_modules 中被安装，也就是重复安装。</li>
<li>模块实例不能共享。比如 React 有一些内部变量，在两个不同包引入的 React 不是同一个模块实例，因此无法共享内部变量，导致一些不可预知的 bug。</li>
</ol>
<p>接着，从 npm3 开始，包括 yarn，都着手来通过<code>扁平化依赖</code>的方式来解决这个问题。相信大家都有这样的体验，我明明就装个 <code>express</code>，为什么 <code>node_modules</code>里面多了这么多东西？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eb0bebbcb544e5fadab18348a462035~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>没错，这就是<code>扁平化</code>依赖管理的结果。相比之前的<code>嵌套结构</code>，现在的目录结构类似下面这样:</p>
<pre><code class="hljs language-js copyable" lang="js">node_modules
├─ foo
|  ├─ index.js
|  └─ package.json
└─ bar
   ├─ index.js
   └─ package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有的依赖都被拍平到<code>node_modules</code>目录下，不再有很深层次的嵌套关系。这样在安装新的包时，根据 node require 机制，会不停往上级的<code>node_modules</code>当中去找，如果找到相同版本的包就不会重新安装，解决了大量包重复安装的问题，而且依赖层级也不会太深。</p>
<p>之前的问题是解决了，但仔细想想这种<code>扁平化</code>的处理方式，它真的就是无懈可击吗？并不是。它照样存在诸多问题，梳理一下:</p>
<ul>
<li>
<ol>
<li>依赖结构的<strong>不确定性</strong>。</li>
</ol>
</li>
<li>
<ol start="2">
<li>扁平化算法本身的<strong>复杂性</strong>很高，耗时较长。</li>
</ol>
</li>
<li>
<ol start="3">
<li>项目中仍然可以<strong>非法访问</strong>没有声明过依赖的包</li>
</ol>
</li>
</ul>
<p>后面两个都好理解，那第一点中的<code>不确定性</code>是什么意思？这里来详细解释一下。</p>
<p>假如现在项目依赖两个包 foo 和 bar，这两个包的依赖又是这样的:
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/211c86c7838b48bead2a4ee7faee25b1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么 npm/yarn install 的时候，通过扁平化处理之后，究竟是这样
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2368d74f8b341f0b1b545198683af59~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还是这样？</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/198d6c12f0e045ce8c0867b44b3aaeb1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>答案是: 都有可能。取决于 foo 和 bar 在 <code>package.json</code>中的位置，如果 foo 声明在前面，那么就是前面的结构，否则是后面的结构。</p>
<p>这就是为什么会产生依赖结构的<code>不确定</code>问题，也是 <code>lock 文件</code>诞生的原因，无论是<code>package-lock.json</code>(npm 5.x 才出现)还是<code>yarn.lock</code>，都是为了保证 install 之后都产生确定的<code>node_modules</code>结构。</p>
<p>尽管如此，npm/yarn 本身还是存在<code>扁平化算法复杂</code>和<code>package 非法访问</code>的问题，影响性能和安全。</p>
<h3 data-id="heading-8">pnpm 依赖管理</h3>
<p>pnpm 的作者<code>Zoltan Kochan</code>发现 yarn 并没有打算去解决上述的这些问题，于是另起炉灶，写了全新的包管理器，开创了一套新的依赖管理机制，现在就让我们去一探究竟。</p>
<p>还是以安装 <code>express</code> 为例，我们新建一个目录，执行:</p>
<pre><code class="copyable">pnpm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行:</p>
<pre><code class="copyable">pnpm install express
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再去看看<code>node_modules</code>:</p>
<pre><code class="copyable">.pnpm
.modules.yaml
express
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们直接就看到了<code>express</code>，但值得注意的是，这里仅仅只是一个<code>软链接</code>，不信你打开看看，里面并没有 node_modules 目录，如果是真正的文件位置，那么根据 node 的包加载机制，它是找不到依赖的。那么它真正的位置在哪呢？</p>
<p>我们继续在 .pnpm 当中寻找:</p>
<pre><code class="copyable">▾ node_modules
  ▾ .pnpm
    ▸ accepts@1.3.7
    ▸ array-flatten@1.1.1
    ...
    ▾ express@4.17.1
      ▾ node_modules
        ▸ accepts
        ▸ array-flatten
        ▸ body-parser
        ▸ content-disposition
        ...
        ▸ etag
        ▾ express
          ▸ lib
            History.md
            index.js
            LICENSE
            package.json
            Readme.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好家伙！竟然在 <code>.pnpm/express@4.17.1/node_modules/express</code>下面找到了!</p>
<p>随便打开一个别的包:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/163b08df949944fea45012bc0c6bfa9c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好像也都是一样的规律，都是<code><package-name>@version/node_modules/<package-name></code>这种目录结构。并且 express 的依赖都在<code>.pnpm/express@4.17.1/node_modules</code>下面，这些依赖也全都是<strong>软链接</strong>。</p>
<p>再看看<code>.pnpm</code>，<code>.pnpm</code>目录下虽然呈现的是扁平的目录结构，但仔细想想，顺着<code>软链接</code>慢慢展开，其实就是嵌套的结构！</p>
<pre><code class="copyable">▾ node_modules
  ▾ .pnpm
    ▸ accepts@1.3.7
    ▸ array-flatten@1.1.1
    ...
    ▾ express@4.17.1
      ▾ node_modules
        ▸ accepts  -> ../accepts@1.3.7/node_modules/accepts
        ▸ array-flatten -> ../array-flatten@1.1.1/node_modules/array-flatten
        ...
        ▾ express
          ▸ lib
            History.md
            index.js
            LICENSE
            package.json
            Readme.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将<code>包本身</code>和<code>依赖</code>放在同一个<code>node_module</code>下面，与原生 Node 完全兼容，又能将 package 与相关的依赖很好地组织到一起，设计十分精妙。</p>
<p>现在我们回过头来看，根目录下的 node_modules 下面不再是眼花缭乱的依赖，而是跟 package.json 声明的依赖基本保持一致。即使 pnpm 内部会有一些包会设置依赖提升，会被提升到根目录 node_modules 当中，但整体上，根目录的<code>node_modules</code>比以前还是清晰和规范了许多。</p>
<h2 data-id="heading-9">再谈安全</h2>
<p>不知道你发现没有，pnpm 这种依赖管理的方式也很巧妙地规避了<code>非法访问依赖</code>的问题，也就是只要一个包未在 package.json 中声明依赖，那么在项目中是无法访问的。</p>
<p>但在 npm/yarn 当中是做不到的，那你可能会问了，如果 A 依赖 B， B 依赖 C，那么 A 就算没有声明 C 的依赖，由于有依赖提升的存在，C 被装到了 A 的<code>node_modules</code>里面，那我在 A 里面用 C，跑起来没有问题呀，我上线了之后，也能正常运行啊。不是挺安全的吗？</p>
<p>还真不是。</p>
<p>第一，你要知道 B 的版本是可能随时变化的，假如之前依赖的是<code>C@1.0.1</code>，现在发了新版，新版本的 B 依赖 <code>C@2.0.1</code>，那么在项目 A 当中 npm/yarn install 之后，装上的是 2.0.1 版本的 C，而 A 当中用的还是 C 当中旧版的 API，可能就直接报错了。</p>
<p>第二，如果 B 更新之后，可能不需要 C 了，那么安装依赖的时候，C 都不会装到<code>node_modules</code>里面，A 当中引用 C 的代码直接报错。</p>
<p>还有一种情况，在 monorepo 项目中，如果 A 依赖 X，B 依赖 X，还有一个 C，它不依赖 X，但它代码里面用到了 X。由于依赖提升的存在，npm/yarn 会把 X 放到根目录的 node_modules 中，这样 C 在本地是能够跑起来的，因为根据 node 的包加载机制，它能够加载到 monorepo 项目根目录下的 node_modules 中的 X。但试想一下，一旦 C 单独发包出去，用户单独安装 C，那么就找不到 X 了，执行到引用 X 的代码时就直接报错了。</p>
<p>这些，都是依赖提升潜在的 bug。如果是自己的业务代码还好，试想一下如果是给很多开发者用的工具包，那危害就非常严重了。</p>
<p>npm 也有想过去解决这个问题，指定<code>--global-style</code>参数即可禁止变量提升，但这样做相当于回到了当年嵌套依赖的时代，一夜回到解放前，前面提到的嵌套依赖的缺点仍然暴露无遗。</p>
<p>npm/yarn 本身去解决依赖提升的问题貌似很难完成，不过社区针对这个问题也已经有特定的解决方案: <strong>dependency-check</strong>，地址: <a href="https://github.com/dependency-check-team/dependency-check" target="_blank" rel="nofollow noopener noreferrer">github.com/dependency-…</a></p>
<p>但不可否认的是，pnpm 做的更加彻底，独创的一套依赖管理方式不仅解决了依赖提升的安全问题，还大大优化了时间和空间上的性能。</p>
<h2 data-id="heading-10">日常使用</h2>
<p>说了这么多，估计你会觉得 <code>pnpm</code> 挺复杂的，是不是用起来成本很高呢？</p>
<p>恰好相反，pnpm 使用起来十分简单，如果你之前有 npm/yarn 的使用经验，甚至可以无缝迁移到 pnpm 上来。不信我们来举几个日常使用的例子。</p>
<h3 data-id="heading-11">pnpm install</h3>
<p>跟 npm install 类似，安装项目下所有的依赖。但对于 monorepo 项目，会安装 workspace 下面所有 packages 的所有依赖。不过可以通过 --filter 参数来指定 package，只对满足条件的 package 进行依赖安装。</p>
<p>当然，也可以这样使用，来进行单个包的安装:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 安装 axios</span>
pnpm install axios
<span class="hljs-comment">// 安装 axios 并将 axios 添加至 devDependencies</span>
pnpm install axios -D
<span class="hljs-comment">// 安装 axios 并将 axios 添加至 dependencies</span>
pnpm install axios -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，也可以通过 --filter 来指定 package。</p>
<h3 data-id="heading-12">pnpm update</h3>
<p>根据指定的范围将包更新到最新版本，monorepo 项目中可以通过 --filter 来指定 package。</p>
<h3 data-id="heading-13">pnpm uninstall</h3>
<p>在 node_modules 和 package.json 中移除指定的依赖。monorepo 项目同上。举例如下:</p>
<pre><code class="copyable">// 移除 axios
pnpm uninstall axios --filter package-a
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">pnpm link</h3>
<p>将本地项目连接到另一个项目。注意，使用的是硬链接，而不是软链接。如:</p>
<pre><code class="copyable">pnpm link ../../axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，对于我们经常用到<code>npm run/start/test/publish</code>，这些直接换成 pnpm 也是一样的，不再赘述。更多的使用姿势可参考官方文档: <a href="https://pnpm.js.org/en/" target="_blank" rel="nofollow noopener noreferrer">pnpm.js.org/en/</a></p>
<p>可以看到，虽然 pnpm 内部做了非常多复杂的设计，但实际上对于用户来说是无感知的，使用起来非常友好。并且，现在作者现在还一直在维护，目前 npm 上周下载量已经有 10w +，经历了大规模用户的考验，稳定性也能有所保障。</p>
<p>因此，我觉得无论是从背后的安全和性能角度，还是从使用上的心智成本来考虑，pnpm 都是一个相比 npm/yarn 更优的方案。</p>
<p><em>参考资料</em>:</p>
<p>[1] pnpm 官方文档: <a href="https://pnpm.js.org/en/" target="_blank" rel="nofollow noopener noreferrer">pnpm.js.org/en/</a></p>
<p>[2] benchmark 仓库: <a href="https://github.com/dependency-check-team/dependency-check" target="_blank" rel="nofollow noopener noreferrer">github.com/dependency-…</a></p>
<p>[3] Zoltan Kochan
《Why should we use pnpm?》：<a href="https://www.kochan.io/nodejs/why-should-we-use-pnpm.html" target="_blank" rel="nofollow noopener noreferrer">www.kochan.io/nodejs/why-…</a></p>
<p>[4] Zoltan Kochan
《pnpm's strictness helps to avoid silly bugs》: <a href="https://www.kochan.io/nodejs/pnpms-strictness-helps-to-avoid-silly-bugs.html" target="_blank" rel="nofollow noopener noreferrer">www.kochan.io/nodejs/pnpm…</a></p>
<p>[5] Conarli《npm install 原理分析》: <a href="https://cloud.tencent.com/developer/article/1555982" target="_blank" rel="nofollow noopener noreferrer">cloud.tencent.com/developer/a…</a></p>
<p>[6] yarn 官方文档: <a href="https://classic.yarnpkg.com/en/docs" target="_blank" rel="nofollow noopener noreferrer">classic.yarnpkg.com/en/docs</a></p>
<p>[7] 《Yarn 的 Plug'n'Play 特性》: <a href="https://loveky.github.io/2019/02/11/yarn-pnp/" target="_blank" rel="nofollow noopener noreferrer">loveky.github.io/2019/02/11/…</a></p>
<p>[8] 《Guide to Monorepos for Front-end Code》: <a href="https://www.toptal.com/front-end/guide-to-monorepos" target="_blank" rel="nofollow noopener noreferrer">www.toptal.com/front-end/g…</a></p></div>  
</div>
            