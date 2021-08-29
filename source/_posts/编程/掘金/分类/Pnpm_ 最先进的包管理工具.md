
---
title: 'Pnpm_ 最先进的包管理工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55ffcfd231524abb8f4b17c629409d84~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 02:20:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55ffcfd231524abb8f4b17c629409d84~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Hi~大家好，今天给大家介绍一个现代的包管理工具，名字叫做 pnpm，英文里面的意思叫做 <code>performant npm</code> ，意味“高性能的 npm”，官网地址可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2F%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/%E3%80%82" ref="nofollow noopener noreferrer">pnpm.io/。</a></p>
<p>目前 pnpm 在字节内部已经有很多项目中得到了实践和落地，例如下图中的 TikTok FE 团队，我们团队自研的 Monorepo 工具目前最新版本同样在底层默认了以 pnpm 作为依赖管理工具。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55ffcfd231524abb8f4b17c629409d84~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>pnpm 相比较于 yarn/npm 这两个常用的包管理工具在性能上也有了极大的提升，根据目前官方提供的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2Fbenchmarks" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/benchmarks" ref="nofollow noopener noreferrer">benchmark</a> 数据可以看出在一些综合场景下比 npm/yarn 快了大概两倍：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa38fc979f4f4ed6a5ec4af64a73c34e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这篇文章中，将会介绍一些关于 pnpm 在依赖管理方面的优化，在 monorepo 中相比较于 yarn workspace 的应用，以及也会介绍一些 pnpm 目前存在的一些缺陷，包括讨论一下未来 pnpm 会做的一些事情。</p>
<h2 data-id="heading-0">依赖管理</h2>
<p>这节会通过 pnpm 在依赖管理这一块的一些不同于正常包管理工具的一些优化技巧。</p>
<h3 data-id="heading-1">hard link 机制</h3>
<p>介绍 pnpm 一定离不开的就是关于 pnpm 在安装依赖方面做的一些优化，根据前面的 benchmark 图可以看到其明显的性能提升。</p>
<p>那么 pnpm 是怎么做到如此大的提升的呢？是因为计算机里面一个叫做 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHard_link" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Hard_link" ref="nofollow noopener noreferrer">Hard link</a></strong> 的机制，<code>hard link</code> 使得用户可以通过不同的路径引用方式去找到某个文件。pnpm 会在全局的 store 目录里存储项目 <code>node_modules</code> 文件的 <code>hard links</code> 。</p>
<p>举个例子，例如项目里面有个 1MB 的依赖 a，在 pnpm 中，看上去这个 a 依赖同时占用了 1MB 的 node_modules 目录以及全局 store 目录 1MB 的空间(加起来是 2MB)，但因为 <code>hard link</code> 的机制使得两个目录下相同的 1MB 空间能从两个不同位置进行寻址，因此实际上这个 a 依赖只用占用 1MB 的空间，而不是 2MB。</p>
<h3 data-id="heading-2">Store 目录</h3>
<p>上一节提到 store 目录用于存储依赖的 hard links，这一节简单介绍一下这个 sotre 目录。</p>
<p>一般 store 目录默认是设置在 <code>$&#123;os.homedir&#125;/.pnpm-store</code> 这个目录下，具体可以参考 <code>@pnpm/store-path</code> 这个 pnpm 子包中的代码:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> homedir = os.homedir()
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">await</span> canLinkToSubdir(tempFile, homedir)) &#123;
  <span class="hljs-keyword">await</span> fs.unlink(tempFile)
  <span class="hljs-comment">// If the project is on the drive on which the OS home directory</span>
  <span class="hljs-comment">// then the store is placed in the home directory</span>
  <span class="hljs-keyword">return</span> path.join(homedir, relStore, STORE_VERSION)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然用户也可以在 <code>.npmrc</code> 设置这个 store 目录位置，不过一般而言 store 目录对于用户来说感知程度是比较小的。</p>
<p>因为这样一个机制，导致每次安装依赖的时候，如果是个相同的依赖，有好多项目都用到这个依赖，那么这个依赖实际上最优情况(即版本相同)只用安装一次。</p>
<p>如果是 npm 或 yarn，那么这个依赖在多个项目中使用，在每次安装的时候都会被重新下载一次。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ba60f4713bc46318ee139d3b8a9bc82~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图可以看到在使用 pnpm 对项目安装依赖的时候，如果某个依赖在 sotre 目录中存在了话，那么就会直接从 store 目录里面去 hard-link，避免了二次安装带来的时间消耗，如果依赖在 store 目录里面不存在的话，就会去下载一次。</p>
<p>当然这里你可能也会有问题：如果安装了很多很多不同的依赖，那么 store 目录会不会越来越大？</p>
<p>答案是当然会存在，针对这个问题，pnpm 提供了一个命令来解决这个问题: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2Fcli%2Fstore" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/cli/store" ref="nofollow noopener noreferrer">pnpm store | pnpm</a>。</p>
<p>同时该命令提供了一个选项，使用方法为 <code>pnpm store prune</code> ，它提供了一种用于删除一些不被全局项目所引用到的 packages 的功能，例如有个包 <code>axios@1.0.0</code> 被一个项目所引用了，但是某次修改使得项目里这个包被更新到了 <code>1.0.1</code> ，那么 store 里面的 1.0.0 的 axios 就就成了个不被引用的包，执行 <code>pnpm store prune</code> 就可以在 store 里面删掉它了。</p>
<p>该命令推荐偶尔进行使用，但不要频繁使用，因为可能某天这个不被引用的包又突然被哪个项目引用了，这样就可以不用再去重新下载这个包了。</p>
<h3 data-id="heading-3">node_modules 结构</h3>
<p>在 pnpm 官网有一篇很经典的文章，关于介绍 pnpm 项目的 node_modules 结构: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2Fblog%2F2020%2F05%2F27%2Fflat-node-modules-is-not-the-only-way" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/blog/2020/05/27/flat-node-modules-is-not-the-only-way" ref="nofollow noopener noreferrer">Flat node_modules is not the only way | pnpm</a>。</p>
<p>在这篇文章中介绍了 pnpm 目前的 node_modules 的一些文件结构，例如在项目中使用 pnpm 安装了一个叫做 <code>express</code> 的依赖，那么最后会在 node_modules 中形成这样两个目录结构:</p>
<pre><code class="copyable">node_modules/express/...
node_modules/.pnpm/express@4.17.1/node_modules/xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中第一个路径是 nodejs 正常寻找路径会去找的一个目录，如果去查看这个目录下的内容，会发现里面连个 <code>node_modules</code> 文件都没有：</p>
<pre><code class="hljs language-bash copyable" lang="bash">▾ express
    ▸ lib
      History.md
      index.js
      LICENSE
      package.json
      Readme.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上这个文件只是个软连接，它会形成一个到第二个目录的一个软连接(类似于软件的快捷方式)，这样 node 在找路径的时候，最终会找到 .pnpm 这个目录下的内容。</p>
<p>其中这个 <code>.pnpm</code> 是个虚拟磁盘目录，然后 express 这个依赖的一些依赖会被平铺到 <code>.pnpm/express@4.17.1/node_modules/</code> 这个目录下面，这样保证了依赖能够 require 到，同时也不会形成很深的依赖层级。</p>
<p>在保证了 nodejs 能找到依赖路径的基础上，同时也很大程度上保证了依赖能很好的被放在一起。</p>
<p><code>pnpm</code> 对于不同版本的依赖有着极其严格的区分要求，如果项目中某个依赖实际上依赖的 <code>peerDeps</code> 出现了具体版本上的不同，对于这样的依赖会在虚拟磁盘目录 <code>.pnpm</code> 有一个比较严格的区分，具体可以参考: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2Fhow-peers-are-resolved" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/how-peers-are-resolved" ref="nofollow noopener noreferrer">pnpm.io/how-peers-a…</a> 这篇文章。</p>
<p>综合而言，本质上 pnpm 的 <code>node_modules</code> 结构是个网状 + 平铺的目录结构。这种依赖结构主要基于软连接(即 symlink)的方式来完成。</p>
<h3 data-id="heading-4">symlink 和 hard link 机制</h3>
<p>在前面知道了 pnpm 是通过 hardlink 在全局里面搞个 store 目录来存储 node_modules 依赖里面的 hard link 地址，然后在引用依赖的时候则是通过 symlink 去找到对应虚拟磁盘目录下(.pnpm 目录)的依赖地址。</p>
<p>这两者结合在一起工作之后，假如有一个项目依赖了 <code>bar@1.0.0</code> 和 <code>foo@1.0.0</code> ，那么最后的 node_modules 结构呈现出来的依赖结构可能会是这样的:</p>
<pre><code class="hljs language-bash copyable" lang="bash">node_modules
└── bar // symlink to .pnpm/bar@1.0.0/node_modules/bar
└── foo // symlink to .pnpm/foo@1.0.0/node_modules/foo
└── .pnpm
    ├── bar@1.0.0
    │   └── node_modules
    │       └── bar -> <store>/bar
    │           ├── index.js
    │           └── package.json
    └── foo@1.0.0
        └── node_modules
            └── foo -> <store>/foo
                ├── index.js
                └── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>node_modules</code> 中的 bar 和 foo 两个目录会软连接到 .pnpm 这个目录下的真实依赖中，而这些真实依赖则是通过 hard link 存储到全局的 store 目录中。</p>
<h3 data-id="heading-5">兼容问题</h3>
<p>读到这里，可能有用户会好奇: 像 hard link 和 symlink 这种方式在所有的系统上都是兼容的吗？</p>
<p>实际上 hard link 在主流系统上(<code>Unix/Win</code>)使用都是没有问题的，但是 symlink 即软连接的方式可能会在 windows 存在一些兼容的问题，但是针对这个问题，pnpm 也提供了对应的解决方案：</p>
<p>在 win 系统上使用一个叫做 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fwindows%2Fwin32%2Ffileio%2Fhard-links-and-junctions" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/en-us/windows/win32/fileio/hard-links-and-junctions" ref="nofollow noopener noreferrer">junctions</a> 的特性来替代软连接，这个方案在 win 上的兼容性要好于 symlink。</p>
<p>或许你也会好奇为啥 pnpm 要使用 hard links 而不是全都用 symlink 来去实现。</p>
<p>实际上存在 store 目录里面的依赖也是可以通过软连接去找到的，nodejs 本身有提供一个叫做 <code>--preserve-symlinks</code> 的参数来支持 symlink，但实际上这个参数实际上对于 symlink 的支持并不好导致作者放弃了该方案从而采用 hard links 的方式:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90ad9850716547d08bfbfea212d6d653~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode-eps%2Fissues%2F46" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node-eps/issues/46" ref="nofollow noopener noreferrer">github.com/nodejs/node…</a> 该issue 讨论。</p>
<h2 data-id="heading-6">Monorepo 支持</h2>
<p><code>pnpm</code> 在 monorepo 场景可以说算得上是个完美的解决方案了，因为其本身的设计机制，导致很多关键或者说致命的问题都得到了相当有效的解决。</p>
<h3 data-id="heading-7">workspace 支持</h3>
<p>对于 monorepo 类型的项目，pnpm 提供了 workspace 来支持，具体可以参考官网文档: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2Fworkspaces%2F%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/workspaces/%E3%80%82" ref="nofollow noopener noreferrer">pnpm.io/workspaces/…</a></p>
<h3 data-id="heading-8">痛点解决</h3>
<p>Monorepo 下被人诟病较多的问题，一般是依赖结构问题。常见的两个问题就是 <code>Phantom dependencies</code> 和 <code>NPM doppelgangers</code>，用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frushjs.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rushjs.io/" ref="nofollow noopener noreferrer">rush 官网</a> 的图片可以很贴切的展示着两个问题:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/977bd60346d04cc8a4565e3e398bd962~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面会针对两个问题一一介绍。</p>
<h4 data-id="heading-9">Phantom dependencies</h4>
<p>Phantom dependencies 被称之为幽灵依赖，解释起来很简单，即某个包没有被安装(<code>package.json</code> 中并没有，但是用户却能够引用到这个包)。</p>
<p>引发这个现象的原因一般是因为 node_modules 结构所导致的，例如使用 yarn 对项目安装依赖，依赖里面有个依赖叫做 foo，foo 这个依赖同时依赖了 bar，yarn 会对安装的 node_modules 做一个扁平化结构的处理(npm v3 之后也是这么做的)，会把依赖在 node_modules 下打平，这样相当于 foo 和 bar 出现在同一层级下面。那么根据 nodejs 的寻径原理，用户能 require 到 foo，同样也能 require 到 bar。</p>
<pre><code class="copyable">package.json -> foo(bar 为 foo 依赖)

node_modules

  /foo

  /bar -> 👻依赖
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这里这个 bar 就成了一个幽灵依赖，如果某天某个版本的 foo 依赖不再依赖 bar 或者 foo 的版本发生了变化，那么 require bar 的模块部分就会抛错。</p>
<p>以上其实只是一个简单的例子，但是根据笔者在字节内部见到的一些 monorepo(主要为 <code>lerna + yarn</code> )项目中，这其实是个比较常见的现象，甚至有些包会直接去利用这种残缺的引入方式去减轻包体积。</p>
<p>还有一种场景就是在 lerna + yarn workspace 的项目里面，因为 yarn 中提供了 hoist 机制(即一些底层子项目的依赖会被提升到顶层的 <code>node_modules</code> 中)，这种 phantom dependencies 会更多，一些底层的子项目经常会去 require 一些在自己里面没有引入的依赖，而直接去找顶层 node_modules 的依赖(nodejs 这里的寻径是个递归上下的过程)并使用。</p>
<p>而根据前面提到的 pnpm 的 <code>node_modules</code> 依赖结构，这种现象是显然不会发生的，因为被打平的依赖会被放到 <code>.pnpm</code> 这个虚拟磁盘目录下面去，用户通过 require 是根本找不到的。</p>
<blockquote>
<p>值得一提的是，pnpm 本身其实也提供了将依赖提升并且按照 yarn 那种形式组织的 node_modules 结构的 Option，作者将其命名为 <code>--shamefully-hoist</code> ，即 "羞耻的 hoist".....</p>
</blockquote>
<h4 data-id="heading-10">NPM doppelgangers</h4>
<p>这个问题其实也可以说是 hoist 导致的，这个问题可能会导致有大量的依赖的被重复安装，举个例子:</p>
<p>例如有个 package，下面依赖有 lib_a、lib_b、lib_c、lib_d，其中 a 和 b 依赖 <a href="https://link.juejin.cn/?target=mailto%3Autil_e%401.0.0" target="_blank" title="mailto:util_e@1.0.0" ref="nofollow noopener noreferrer">util_e@1.0.0</a>，而 c 和 d 依赖 <a href="https://link.juejin.cn/?target=mailto%3Autil_e%402.0.0" target="_blank" title="mailto:util_e@2.0.0" ref="nofollow noopener noreferrer">util_e@2.0.0</a>。</p>
<p>那么早期 npm 的依赖结构应该是这样的:</p>
<pre><code class="hljs language-bash copyable" lang="bash">- package
- package.json
- node_modules
- lib_a
  - node_modules <- util_e@1.0.0
- lib_b
  - node_modules <- util_e@1.0.0
_ lib_c
  - node_modules <- util_e@2.0.0
- lib_d
  - node_modules <- util_e@2.0.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样必然会导致很多依赖被重复安装，于是就有了 hoist 和打平依赖的操作:</p>
<pre><code class="hljs language-bash copyable" lang="bash">- package
- package.json
- node_modules
- util_e@1.0.0
- lib_a
- lib_b
_ lib_c
  - node_modules <- util_e@2.0.0
- lib_d
  - node_modules <- util_e@2.0.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样也只能提升一个依赖，如果两个依赖都提升了会导致冲突，这样同样会导致一些不同版本的依赖被重复安装多次，这里就会导致使用 npm 和 yarn 的性能损失。</p>
<p>如果是 pnpm 的话，这里因为依赖始终都是存在 store 目录下的 hard links ，一份不同的依赖始终都只会被安装一次，因此这个是能够被彻彻底底的消除的。</p>
<h2 data-id="heading-11">目前不适用的场景</h2>
<p>前面有提到关于 pnpm 的主要问题在于 symlink(软链接)在一些场景下会存在兼容的问题，可以参考作者在 nodejs 那边开的一个 discussion：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fdiscussions%2F37509" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/discussions/37509" ref="nofollow noopener noreferrer">github.com/nodejs/node…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fb3e4b6b5ef43dc9e8437389d2cb46e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在里面作者提到了目前 nodejs 软连接不能适用的一些场景，希望 nodejs 能提供一种 link 方式而不是使用软连接，同时也提到了 pnpm 目前因为软连接而不能使用的场景:</p>
<ul>
<li>Electron 应用无法使用 pnpm</li>
<li>部署在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.aws.amazon.com%2Flambda%2Flatest%2Fdg%2Fgettingstarted-package.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html" ref="nofollow noopener noreferrer">lambda</a> 上的应用无法使用 pnpm</li>
</ul>
<p>笔者在字节内部使用 pnpm 时也遇到过一些 nodejs 基础库不支持 symlink 的情况导致使用 pnpm 无法正常工作，不过这些库在迭代更新之后也会支持这一特性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b702b38ff6704651976c4c3eab540566~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">未来会做的一些事情</h2>
<h3 data-id="heading-13">脱离 nodejs</h3>
<p>具体可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fdiscussions%2F3434" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pnpm/pnpm/discussions/3434" ref="nofollow noopener noreferrer">github.com/pnpm/pnpm/d…</a></p>
<ul>
<li>安装 pnpm 的， 可以基本上脱离掉 nodejs 这个 runtime 去进行安装使用。</li>
<li>可以通过 pnpm 来使用不同版本的 nodejs 来去做依赖安装，类似于 nvm 提供的功能。</li>
</ul>
<p>目前该特性其实已经到了 beta 版本，可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40pnpm%2Fbeta" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@pnpm/beta" ref="nofollow noopener noreferrer">www.npmjs.com/package/@pn…</a> 这个包。管理不同版本的 nodejs 功能可以参考 env 这个子命令: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpnpm.io%2Fcli%2Fenv" target="_blank" rel="nofollow noopener noreferrer" title="https://pnpm.io/cli/env" ref="nofollow noopener noreferrer">pnpm.io/cli/env</a></p>
<h3 data-id="heading-14">使用 rust 写一些模块</h3>
<p>具体可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fdiscussions%2F3419" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pnpm/pnpm/discussions/3419" ref="nofollow noopener noreferrer">github.com/pnpm/pnpm/d…</a> 这个 discussion 讨论的内容，大概就是作者希望给 pnpm 的一些子命令提供一些 rust 的 cli wrapper 来做提升性能使用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/815599c082fd4c2085282cdd1f22b04d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前这个目前还没有特别大的进展，但还是为作者的想法点赞，作者本人对于这个的回应是“如果这个 pnpm 不去做，那么会有其他工具去做，最后 pnpm 就会被淘汰”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03fe9287edbe4d87af627f8a62288621~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前作者本人也还在学习 rust 的过程中，具体的 cli rust wrapper 的仓库地址可以参考: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpn%25EF%25BC%258C%25E7%259B%25AE%25E5%2589%258D%25E8%25BF%2598%25E5%258F%25AA%25E6%2598%25AF%25E5%25A4%2584%25E4%25BA%258E%25E4%25B8%2580%25E4%25B8%25AA%25E8%25B5%25B7%25E6%25AD%25A5%25E7%259A%2584%25E9%2598%25B6%25E6%25AE%25B5%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pnpm/pn%EF%BC%8C%E7%9B%AE%E5%89%8D%E8%BF%98%E5%8F%AA%E6%98%AF%E5%A4%84%E4%BA%8E%E4%B8%80%E4%B8%AA%E8%B5%B7%E6%AD%A5%E7%9A%84%E9%98%B6%E6%AE%B5%E3%80%82" ref="nofollow noopener noreferrer">github.com/pnpm/pn，目前还…</a></p>
<h2 data-id="heading-15">总结</h2>
<p>目前基于 pnpm 为依赖管理的 monorepo 工具例如 rush 在开源社区得到了广泛的实践，在字节内部的我们组自研的 Monorepo 工具中同样基于 pnpm 作为依赖管理工具，目前已经落地了大量的项目。</p>
<p>pnpm 作为包管理器里面的“后起之秀”，通过作者别出心裁的设计方案，完美解决了许多了现有的包管理工具 npm、yarn 以及 node_modules 本身设计原因留下的痛点。同时作者本人也十分有进取心，努力的在完善 pnpm 的 feature 以及规划未来的发展方向，期待未来能越来越好吧~</p></div>  
</div>
            