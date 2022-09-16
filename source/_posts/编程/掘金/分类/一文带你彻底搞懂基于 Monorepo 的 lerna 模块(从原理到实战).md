
---
title: '一文带你彻底搞懂基于 Monorepo 的 lerna 模块(从原理到实战)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/248352fb287743dc8353fc3333e5f187~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Wed, 14 Sep 2022 20:59:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/248352fb287743dc8353fc3333e5f187~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://juejin.cn/post/7138637426922094605" target="_blank" title="https://juejin.cn/post/7138637426922094605">点击查看活动详情</a></p>
<h2 data-id="heading-0">本文你能学到什么？</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/248352fb287743dc8353fc3333e5f187~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看完本文后希望可以检查一下图中的内容是否都掌握了，文中的例子最好实际操作一下，下面开始正文。</p>
<blockquote>
<p>本文是<strong>前端工程化系列</strong>中的一篇，会不断更新，下篇更新内容可看文末的<strong>下期预告</strong>！ <strong>宗旨：工程化的最终目的是让业务开发可以 100% 聚焦在业务逻辑上</strong></p>
</blockquote>
<h2 data-id="heading-1">lerna是什么？有什么优势？</h2>
<h3 data-id="heading-2">lerna 基础概念</h3>
<blockquote>
<p>A tool for managing JavaScript projects with multiple packages. Lerna is a tool that optimizes the workflow around managing multi-package repositories with git and npm.</p>
</blockquote>
<p>翻译：<code>Lerna</code>
是一个用来优化托管在 <code>git\npm</code> 上的多 <code>package</code> 代码库的工作流的一个管理工具,可以让你在主项目下管理多个子项目，从而解决了多个包互相依赖，且发布时需要手动维护多个包的问题。</p>
<p>关键词：多仓库管理，多包管理，自动管理包依赖</p>
<h3 data-id="heading-3">lerna 解决了哪些痛点</h3>
<h4 data-id="heading-4">资源浪费</h4>
<p>通常情况下，一个公司的业务项目只有一个主干，多 <code>git repo</code> 的方式，这样 <code>node_module</code> 会出现大量的冗余，比如它们可能都会安装 <code>React</code>、<code>React-dom</code> 等包，浪费了大量存储空间。</p>
<h4 data-id="heading-5">调试繁琐</h4>
<p>很多公共的包通过 <code>npm</code> 安装，想要调试依赖的包时，需要通过 <code>npm link</code> 的方式进行调试。</p>
<h4 data-id="heading-6">资源包升级问题</h4>
<p>一个项目依赖了多个 <code>npm</code> 包，当某一个子 <code>npm</code> 包代码修改升级时，都要对主干项目包进行升级修改。 (这个问题感觉是最烦的，可能一个版本号就要去更新一下代码并发布)</p>
<h2 data-id="heading-7">lerna的核心原理</h2>
<h3 data-id="heading-8">monorepo 和 multrepo 对比</h3>
<p><code>monorepo</code>：是将所有的模块统一的放在一个主干分支之中管理。
<code>multrepo</code>：将项目分化为多个模块，并针对每一个模块单独的开辟一个 <code>reporsitory</code>来进行管理。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3c2cafdc4d447eab56c59fe1cd54534~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">lerna 软链实现(如何动态创建软链)</h3>
<p>未使用 <code>lerna</code> 之前，想要调试一个本地的 <code>npm</code> 模块包，需要使用 <code>npm link</code> 来进行调试，但是在 <code>lerna</code> 中可以直接进行模块的引入和调试，这种动态创建软链是如何实现的？</p>
<h4 data-id="heading-10">软链是什么？</h4>
<h4 data-id="heading-11">Node.js 中如何实现软链</h4>
<p><code>lerna</code>  中也是通过这种方式来实现软链的</p>
<p><code>fs.symlinkSync(target,path,type)</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">fs.<span class="hljs-title function_">symlinkSync</span>(target,path,type)
target <string> | <<span class="hljs-title class_">Buffer</span>> | <<span class="hljs-variable constant_">URL</span>>   <span class="hljs-comment">// 目标文件</span>
path <string> | <<span class="hljs-title class_">Buffer</span>> | <<span class="hljs-variable constant_">URL</span>>  <span class="hljs-comment">// 创建软链对应的地址</span>
type <string>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它会创建名为 <code>path</code> 的链接，该链接指向 <code>target</code>。<code>type</code> 参数仅在 <code>Windows</code> 上可用，在其他平台上则会被忽略。 它可以被设置为 <code>'dir'</code>、 <code>'file'</code> 或 <code>'junction'</code>。 如果未设置 <code>type</code> 参数，则 <code>Node.js</code> 将会自动检测 <code>target</code> 的类型并使用 <code>'file'</code> 或 <code>'dir'</code>。 如果 <code>target</code> 不存在，则将会使用 <code>'file'</code>。 <code>Windows</code> 上的连接点要求目标路径是绝对路径。 当使用 <code>'junction'</code> 时， <code>target</code> 参数将会自动地标准化为绝对路径。</p>
<ul>
<li>基本使用</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> res = fs.<span class="hljs-title function_">symlinkSync</span>(<span class="hljs-string">'./target/a.js'</span>,<span class="hljs-string">'./b.js'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2dbe30e801b54369af127de01035c4a7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这段代码的意思是为  创建一个软链接 <code>b.js</code> 指向了文件 <code>./targert/a.js</code>,当 <code>a.js</code> 中的内容发生变化时，<code>b.js</code> 文件也会发生相同的改变。</p>
<p>在 <code>Node.js</code> 文档中，<code>fs.symlinkSync()</code>
<code>lerna</code> 的源码中动态链接也是通过 <code>symlinkSync</code> 来实现的。
源码对应地址：软链实现源码地址<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%2Ftree%2Fmain%2Futils%2Fcreate-symlink" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna/tree/main/utils/create-symlink" ref="nofollow noopener noreferrer">参考1</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">createSymbolicLink</span>(<span class="hljs-params">src, dest, type</span>) &#123;
  log.<span class="hljs-title function_">silly</span>(<span class="hljs-string">"createSymbolicLink"</span>, [src, dest, type]);

  <span class="hljs-keyword">return</span> fs
    .<span class="hljs-title function_">lstat</span>(dest)
    .<span class="hljs-title function_">then</span>(<span class="hljs-function">() =></span> fs.<span class="hljs-title function_">unlink</span>(dest))
    .<span class="hljs-title function_">catch</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">/* nothing exists at destination */</span>
    &#125;)
    .<span class="hljs-title function_">then</span>(<span class="hljs-function">() =></span> fs.<span class="hljs-title function_">symlink</span>(src, dest, type));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>更多关于软链的文章,我后面会单独写一篇文章介绍软硬链接，这里知道 <code>lerna 链接部分</code> 的实现就可以了。
Node fs 官网 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.cn%2Fapi%2Ffs.html%23fs_fs_unlink_path_callback" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.cn/api/fs.html#fs_fs_unlink_path_callback" ref="nofollow noopener noreferrer">参考2</a></p>
</blockquote>
<h2 data-id="heading-12">lerna 基本使用</h2>
<h3 data-id="heading-13">lerna 环境配置</h3>
<p><code>lerna</code> 在使用之前需要全局安装 <code>lerna</code> 工具。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install lerna -g
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">初始化一个lerna 项目</h4>
<p><code>mkdir lerna-demo</code>,在当前目录下创建文件夹<code>lerna-demo</code>,然后使用命令 <code>lerna init</code>
执行成功后，目录下将会生成这样的目录结构。，一个 <code>hello world</code>级别的 <code>lerna</code> 项目就完成了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6147f0af259b401f89a9f4de0bdac3df~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> - <span class="hljs-title function_">packages</span>(目录)
 - lerna.<span class="hljs-title function_">json</span>(配置文件)
 - package.<span class="hljs-title function_">json</span>(工程描述文件)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">lerna 常用命令</h3>
<p>介绍一些 <code>lerna</code> 常用的命令,常用命令这部分可以简单过一遍，当作一个工具集收藏就行，需要的时候来找下，用着用着就熟练了，主要可以实操下下面的实战小练习，这个过程会遇到一些坑的。</p>
<ol>
<li>初始化 <code>lerna</code> 项目</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna init 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建一个新的由 <code>lerna</code> 管理的包。</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna create <name>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>安装所有·依赖项并连接所有的交叉依赖</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna bootstrap
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>增加模块包到最外层的公共 <code>node_modules</code>中</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna add axios
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>增加模块包到 <code>packages</code> 中指定项目
下面是将 <code>ui-web</code> 模块增加到 <code>example-web</code> 项目中</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna add ui-web --scope=example-web
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>在 <code>packages</code> 中对应包下的执行任意命令
下面的命令，是对 <code>packages</code> 下的 <code>example-web</code> 项目执行 <code>yarn start</code> 命令 ，比较常用，可以把它配置到最外层的 <code>package.json</code> 中。</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna exec --scope example-web -- yarn start
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果命令中不增加 <code>--scope example-web</code>
直接使用下面的命令，这会在 <code>packages</code> 下所有包执行命令<code>rm -rf ./node_modules</code></p>
<pre><code class="hljs language-shell copyable" lang="shell">lerna exec -- rm -rf ./node_modules
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>显示所有的安装的包</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna list // 等同于 lerna ls
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里再提一个命令也比较常用,可以通过<code>json</code>的方式查看 <code>lerna</code> 安装了哪些包,<code>json</code> 中还包括包的<strong>路径</strong>，有时候可以用于查找包是否生效。</p>
<pre><code class="hljs language-shell copyable" lang="shell">lerna list --json
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>从所有包中删除 <code>node_modules</code> 目录</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna clean
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>⚠️注意下 <code>lerna clean</code> 不会删除项目最外层的根 <code>node_modules</code></p>
</blockquote>
<ol start="9">
<li>在当前项目中发布包</li>
</ol>
<pre><code class="hljs language-shell copyable" lang="shell">lerna publish
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个命令可以结合 <code>lerna.json</code> 中的  <code>"version": "independent"</code> 配置一起使用，可以完成统一发布版本号和<code>packages</code> 下每个模版发布的效果，具体会在下面的实战讲解。</p>
<blockquote>
<p><code>lerna publish</code> 永远不会发布标记为 <code>private</code> 的包（<code>package.json中的”private“: true</code>）</p>
</blockquote>
<p>以上命令基本够日常开发使用了，如果需要更详细内命令内容，可以查看下面的详细文档
lerna 命令详细文档<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.febeacon.com%2Flerna-docs-zh-cn" target="_blank" rel="nofollow noopener noreferrer" title="http://www.febeacon.com/lerna-docs-zh-cn" ref="nofollow noopener noreferrer">参考3</a></p>
<h2 data-id="heading-16">lerna 应用(适用场景)</h2>
<h3 data-id="heading-17">从零搭建一个 平台基础组件库项目</h3>
<p>lerna 比较适合的场景：基础框架，基础工具类，<code>ui-component</code> 中会存在 <code>h5</code> 组件库，<code>web</code> 组件库，<code>mobile</code> 组件库，以及对应的 <code>doc</code> 项目，三个项目通用的 <code>common</code> 代码。为了方便多个项目的联调，以及分别打包，这里采用了<code>lerna</code> 的管理方式。</p>
<p>接下来会讲解使用 <code>leran</code> 搭建 <code>ui-component</code> 基础组件库的过程。</p>
<h4 data-id="heading-18">1. 项目初始化</h4>
<p>创建一个文件夹 <code>ui-component</code> ,</p>
<p>切换到目录 <code>ui-component</code>目录下。
执行 <code>lerna init</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9d54b3d7b254114867df842eafea257~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>lerna</code> 会自动创建一个 <code>packages</code> 目录夹，我们以后的项目都新建在这里面。同时还会在根目录新建一个 <code>lerna.json</code>配置文件</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"packages"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-string">"packages/*"</span>
  <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"0.0.0"</span> <span class="hljs-comment">// 共用的版本，由lerna管理</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意``lerna<code>默认使用的是集中版本，所有的</code>package<code>共用一个</code>version<code>,如果需要 </code>packages<code>下不同的模块 使用不同的版本号，需要配置</code>Independent<code>模式。命令行介绍时有提到这里 在</code>json` 中增加属性配置</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"independent"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>package.json</code> 中有一点需要注意，他的 <code>private</code> 必须设置为 <code>true</code> ，因为 <code>mono-repo</code> 本身的这个 <code>Git</code>仓库并不是一个项目，他是多个项目，所以一般不进行直接发布，发布的应该是 <code>packages/</code> 下面的各个子项目。</p>
<h4 data-id="heading-19">子项目创建</h4>
<p>现在 <code>package</code> 目录下是空的，我们需要创建一下组件库内部相关内容。使用 <code>leran create</code> 命令创建子 <code>package</code> 项目。</p>
<pre><code class="hljs language-shell copyable" lang="shell">lerna create ui-common
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>lerna create ui-common</code>会在 <code>packages</code> 中创建 <code>ui-common</code> 项目，另外创建两个基于 <code>TypeScript</code> 的 <code>react</code> 项目 <code>ui-web</code> 和 <code>example-web</code>，
在 <code>package</code> 目录下运行</p>
<pre><code class="hljs language-shell copyable" lang="shell">npx create-react-app ui-web --typescript
npx create-react-app example-web --typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里补充一个小插曲吧，初始化 <code>typescript</code> 项目后如何进行配置，可以直接用 <code>typescript</code> 编写组件?
安装 typescript需要的模块包</p>
</blockquote>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta prompt_">$ </span><span class="bash">npm install --save typescript @types/node @types/react @types/react-dom @types/jest</span>
<span class="hljs-meta prompt_">$ </span><span class="bash"><span class="hljs-comment"># 或者</span></span>
<span class="hljs-meta prompt_">$ </span><span class="bash">yarn add typescript @types/node @types/react @types/react-dom @types/jest</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在项目根目录创建 <code>tsconfig.json</code> 和 <code>webpack.config.js</code> 文件：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"compilerOptions"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"target"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"es5"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"module"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"commonjs"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"lib"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"dom"</span><span class="hljs-punctuation">,</span><span class="hljs-string">"es2015"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"jsx"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"react"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"sourceMap"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"strict"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"noImplicitAny"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"baseUrl"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"src"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"paths"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
      <span class="hljs-attr">"@/*"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"./*"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
    <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"esModuleInterop"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"experimentalDecorators"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"include"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-string">"./src/**/*"</span>
  <span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>jsx</code> 选择 <code>react</code></li>
<li><code>lib</code> 开启 <code>dom</code> 和 <code>es2015</code></li>
<li><code>include</code> 选择我们创建的 <code>src</code> 目录</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">var</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">var</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-keyword">const</span> &#123; <span class="hljs-title class_">CheckerPlugin</span> &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'awesome-typescript-loader'</span>);
<span class="hljs-keyword">var</span> <span class="hljs-variable constant_">ROOT</span> = path.<span class="hljs-title function_">resolve</span>(__dirname);

<span class="hljs-keyword">var</span> entry = <span class="hljs-string">'./src/index.tsx'</span>;
<span class="hljs-keyword">const</span> <span class="hljs-variable constant_">MODE</span> = process.<span class="hljs-property">env</span>.<span class="hljs-property">MODE</span>;
<span class="hljs-keyword">const</span> plugins = [];
<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-attr">entry</span>: entry,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-variable constant_">ROOT</span> + <span class="hljs-string">'/dist'</span>,
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].bundle.js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ts[x]?$/</span>,
        <span class="hljs-attr">loader</span>: [
          <span class="hljs-string">'awesome-typescript-loader'</span>
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">enforce</span>: <span class="hljs-string">'pre'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ts[x]$/</span>,
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'source-map-loader'</span>
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.json'</span>],
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: <span class="hljs-variable constant_">ROOT</span> + <span class="hljs-string">'/src'</span>
    &#125;
  &#125;,
&#125;

<span class="hljs-keyword">if</span> (<span class="hljs-variable constant_">MODE</span> === <span class="hljs-string">'production'</span>) &#123;
  config.<span class="hljs-property">plugins</span> = [
    <span class="hljs-keyword">new</span> <span class="hljs-title class_">CheckerPlugin</span>(),
    ...plugins
  ];
&#125;

<span class="hljs-keyword">if</span> (<span class="hljs-variable constant_">MODE</span> === <span class="hljs-string">'development'</span>) &#123;
  config.<span class="hljs-property">devtool</span> = <span class="hljs-string">'inline-source-map'</span>;
  config.<span class="hljs-property">plugins</span> = [
    <span class="hljs-keyword">new</span> <span class="hljs-title class_">CheckerPlugin</span>(),
    ...plugins
  ];
&#125;
<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = config;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建完两个项目后， <code>ui-web</code> 和 <code>example-web</code> 中同时出现 <code>node_modules</code>,二者会有很多重复部分，并且会占用大量的硬盘空间</p>
<h5 data-id="heading-20">lerna bootstrap</h5>
<p><code>lerna</code> 提供了可以<strong>将子项目的依赖包提升到最顶层</strong>的方式 ，我们可以执行 <code>lerna clean</code>先删除每个子项目的 <code>node_modules</code> , 然后执行命令  <code>lerna bootstrop --hoist</code>。</p>
<p><code>lerna bootstrop --hoist</code> 会将 <code>packages</code> 目录下的公共模块包抽离到最顶层，但是这种方式会有一个问题，<strong>不同版本号只会保留使用最多的版本</strong>，这种配置不太好，当项目中有些功能需要依赖老版本时，就会出现问题。</p>
<h5 data-id="heading-21">yarn workspaces</h5>
<p>有没有更优雅的方式？再介绍一个命令 <code>yarn workspaces</code> ，可以解决前面说的当不同的项目依赖不同的版本号问题， <code>yarn workspaces</code>会检查每个子项目里面依赖及其版本，如果版本不一致都会保留到自己的 <code>node_modules</code> 中，只有依赖版本号一致的时候才会提升到顶层。
注意：
这种需要在 <code>lerna.json</code> 中增加配置。</p>
<pre><code class="hljs language-javasript copyable" lang="javasript">  "npmClient": "yarn",  // 指定 npmClent 为 yarn
  "useWorkspaces": true // 将 useWorkspaces 设置为 true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且在<strong>顶层</strong>的 <code>package.json</code> 中增加配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 顶层的 package.json</span>
&#123;
    <span class="hljs-string">"workspaces"</span>:[
        <span class="hljs-string">"packages/*"</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>增加了这个配置后 不再需要 <code>lerna bootstrap</code> 来安装依赖了，可以直接使用 <code>yarn install</code> 进行依赖的安装。 注意：<code>yarn install</code> 无论在顶层运行还是在任意一个子项目运行效果都是可以。</p>
<h4 data-id="heading-22">启动子项目</h4>
<p>配置完成后，我们启动 <code>packages</code> 目录下的子项目 <code>example-web</code>,原有情况下我们可能需要频繁切换到 <code>example-web</code> 文件夹，在这个目录执行 <code>yarn start</code>。</p>
<p>使用了 <code>lerna</code> 进行项目管理之后,可以在顶层的 <code>package.json</code> 文件中进行配置，在 <code>scripts</code> 中增加配置。</p>
<pre><code class="hljs language-shell copyable" lang="shell">  "scripts": &#123;
        "web": "lerna exec --scope example-web -- yarn start",
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>lerna exec --scope example-web</code> 命令是在 <code>example-web</code> 包下执行 <code>yarn start</code>。</p>
<p>并且在顶层 <code>lerna.json</code> 中增加配置</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
<span class="hljs-attr">"npmClient"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"true"</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在顶层执行 <code>yarn web</code> 就可以运行 <code>example-web</code> 项目了。</p>
<p>配置完成后尝试一下，项目正常启动。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c7528e2b0c54de0b0b578164144f9ca~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">example-web 模块中 引用 ui-common 中的函数</h4>
<p>我们在 <code>ui-common</code>中定义一个网络请求公共函数，在 <code>ui-web</code> 和 <code>example-web</code> 项目中都会用到。在项目 <code>example-web</code> 中增加 <code>ui-common</code> 模块依赖，执行命令</p>
<pre><code class="hljs language-shell copyable" lang="shell">lerna add ui-common --scope=example-web
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行命令后，在 <code>example-web</code> 的 <code>package.josn</code>中会出现</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f56c09af67341a98ec526978ff08ecb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>ui-common</code> 已经成功被 <code>example-web</code> 中引用，然后在 <code>example-web</code> 项目中引用 <code>request</code> 函数并使用，例子中只是简单使用下 <code>ui-common</code> 中的函数。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">"ui-common"</span>;

<span class="hljs-keyword">interface</span> <span class="hljs-title class_">IProps</span> &#123;&#125;
<span class="hljs-keyword">interface</span> <span class="hljs-title class_">IState</span> &#123;
  <span class="hljs-attr">conents</span>: <span class="hljs-title class_">Array</span><<span class="hljs-built_in">string</span>>;
&#125;
<span class="hljs-keyword">class</span> <span class="hljs-title class_">CommentList</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">React.Component</span><<span class="hljs-title class_">IProps</span>, <span class="hljs-title class_">IState</span>> &#123;
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">props: IProps</span>) &#123;
    <span class="hljs-variable language_">super</span>(props);
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span> = &#123;
      <span class="hljs-attr">conents</span>: [<span class="hljs-string">"我是列表第一条"</span>],
    &#125;;
  &#125;
  <span class="hljs-title function_">componentDidMount</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-title function_">request</span>(&#123;
      <span class="hljs-attr">url</span>: <span class="hljs-string">"www.baidu.com"</span>,
      <span class="hljs-attr">method</span>: <span class="hljs-string">"get"</span>,
    &#125;);
  &#125;
  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
          &#123;this.state.conents.map((item, index) => &#123;
            return <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>></span> &#123;item&#125; <span class="hljs-tag"></<span class="hljs-name">li</span>></span>;
          &#125;)&#125;
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"></></span></span>
    );
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">CommentList</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">发布</h4>
<p>项目结构已基本搭建完成，我们尝试发布一下 ,使用命令</p>
<pre><code class="hljs language-shell copyable" lang="shell">lerna publish
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于之前我们在 <code>lerna.json</code>  中配置了</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"packages"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-string">"packages/*"</span>
  <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"independent"</span><span class="hljs-punctuation">,</span><span class="hljs-comment">// 不同模块不同版本</span>
  <span class="hljs-attr">"npmClient"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"yarn"</span><span class="hljs-punctuation">,</span> 
  <span class="hljs-attr">"useWorkspaces"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span> 
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行命令后在会出现如下内容，针对 <code>packages</code> 中的每个模块单独选择版本进行发布。</p>
<p>如果想要发布的模块统一，使用相同的版本号，需要修改<code> lerna.json</code> ,将 <code>"version": "independent"</code>, 改为固定版本号,修改后尝试重新使用 <code>lerna publish</code>进行发布，</p>
<blockquote>
<p>注意⚠️：这里再次声明一下，如果使用了 <code>independent</code> 方式进行版本控制，在 <code>packages</code> 内部的包进行互相依赖时，每次发布之后记得修改下发布后的版本号，否则在本地调试时会出现刚发布的代码不生效问题(这个问题本人亲自遇到过，单独说下)</p>
</blockquote>
<h3 data-id="heading-25">框架类项目</h3>
<h4 data-id="heading-26">公司组件库项目</h4>
<p>组件库项目类似上面实战的目录结构，但是会在 <code>packages</code> 包下添加很多其他的模块，比如 <code>ui-h5</code> , <code>example-h5</code> 等</p>
<h3 data-id="heading-27">工具类项目</h3>
<p>举例一些开源项目。</p>
<ul>
<li><code>babel</code> 使用的就是 <code>lerna</code> 进行管理</li>
<li><code>facebook/jest</code> 使用的是 <code>lerna</code> 进行管理</li>
<li><code>alibaba/rax</code> 使用的是 <code>lerna</code> 进行管理</li>
</ul>
<h2 data-id="heading-28">lerna 弊端</h2>
<p>和传统的 <code>git submodules</code> 多仓库方式对比，我觉得 <code>lerna</code> 优势很明显的，个人认为唯一不足的是: 由于源码在一起，仓库变更非常常见，存储空间也变得很大，甚至几<code>G</code>，<code>CI</code> 测试运行时间也会变长,虽然如此也是可以接受的。</p>
<h2 data-id="heading-29">下期预告</h2>
<p>本文主要讲解了 <code>lerna</code> 的基本使用，并且用它搭建了一个基础目录结构(我会补充一些基础的配置 <code>eslint</code>，<code>prettier</code> 等,本文不多写之前有写过)，这种搭建我们没有必要每次都配置一遍，尝试一遍就好了，<strong>工程化的最终目的是让业务开发可以 100% 聚焦在业务逻辑上</strong>，下一篇文章会讲解 轮子 <code>create-mono-repo cli</code> 脚手架的完整实现过程，如何快速创建 <code>mono-repo</code> 项目</p>
<h4 data-id="heading-30">参考文章</h4>
<ul>
<li>[1] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%2Ftree%2Fmain%2Futils%2Fcreate-symlink" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna/tree/main/utils/create-symlink" ref="nofollow noopener noreferrer">github.com/lerna/lerna…</a></li>
<li>[2] <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.cn%2Fapi%2Ffs.html%23fs_fs_unlink_path_callback" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.cn/api/fs.html#fs_fs_unlink_path_callback" ref="nofollow noopener noreferrer">nodejs.cn/api/fs.html…</a></li>
<li>[3] <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.febeacon.com%2Flerna-docs-zh-cn" target="_blank" rel="nofollow noopener noreferrer" title="http://www.febeacon.com/lerna-docs-zh-cn" ref="nofollow noopener noreferrer">www.febeacon.com/lerna-docs-…</a></li>
<li>[4] <a href="https://juejin.cn/post/6844903885312622606" target="_blank" title="https://juejin.cn/post/6844903885312622606">juejin.cn/post/684490…</a></li>
<li>[5] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdkypooh%2Ffront-end-develop-demo%2Ftree%2Fmaster%2Fbase%2Flerna" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dkypooh/front-end-develop-demo/tree/master/base/lerna" ref="nofollow noopener noreferrer">github.com/dkypooh/fro…</a></li>
<li>[6] <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.febeacon.com%2Flerna-docs-zh-cn%2Froutes%2Fcommands%2Fbootstrap.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.febeacon.com/lerna-docs-zh-cn/routes/commands/bootstrap.html" ref="nofollow noopener noreferrer">www.febeacon.com/lerna-docs-…</a></li>
<li>[7] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%2Ftree%2Fmain%2Futils%2Fcreate-symlink" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna/tree/main/utils/create-symlink" ref="nofollow noopener noreferrer">github.com/lerna/lerna…</a></li>
</ul></div>  
</div>
            