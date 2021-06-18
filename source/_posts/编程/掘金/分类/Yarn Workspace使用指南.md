
---
title: 'Yarn Workspace使用指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4265'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:16:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=4265'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Yarn Workspaces（工作区）是Yarn提供的<code>monorepo</code>的依赖管理机制，从Yarn 1.0开始默认支持，用于在代码仓库的根目录下管理多个package的依赖。</p>
<h2 data-id="heading-0">Monorepo</h2>
<p>假如你是一个npm工具的维护者，管理着多个功能相近的包，或者这些包之间存在依赖关系。如果将这些包拆分在不同仓库里，那么面临要跨多个包进行更改时，工作会非常繁琐和复杂。</p>
<p>为了简化流程，很多大型项目采用了menorepo的做法，即把所有的包放在一个仓库中管理。Babel、React、Vue、Jest等都使用了menorepo的管理方式。</p>
<p>Menorepo的优点是可以在一个仓库里维护多个package，可统一构建，跨package调试、依赖管理、版本发布都十分方便，搭配工具还能统一生成CHANGELOG；</p>
<p>缺点是代码仓库体积会变大，只开发其中一个package也需要安装整个项目的依赖。</p>
<p>来看一下<a href="https://github.com/babel/babel/tree/master" target="_blank" rel="nofollow noopener noreferrer">Babel</a>的仓库目录（简化）：</p>
<pre><code class="copyable">babel/
|--package.json
|--yarn.lock
|--packages/
|  |--babel-cli/
|  |  |--package.json
|  |--babel-core/
|  |  |--package.json
|  |--babel-parser/
|  |  |--package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">Why Yarn Workspace?</h2>
<ul>
<li>开发多个互相依赖的package时，workspace会自动对package的引用设置软链接（symlink），比yarn link更加方便，且链接仅局限在当前workspace中，不会对整个系统造成影响</li>
<li>所有package的依赖会安装在最根目录的node_modules下，节省磁盘空间，且给了yarn更大的依赖优化空间</li>
<li>所有package使用同一个yarn.lock，更少造成冲突且易于审查</li>
</ul>
<h2 data-id="heading-2">如何使用Workspace</h2>
<p>根目录的package.json设置：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"mono-demo"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"private"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"workspaces"</span>: [
    <span class="hljs-string">"packages/*"</span>
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>private</code>：</p>
<p>根目录一般是项目的脚手架，无需发布，<code>"private": true</code>会确保根目录不被发布出去。</p>
<p><code>workspaces</code>:</p>
<p>声明workspace中package的路径。值是一个字符串数组，支持Glob通配符。</p>
<p>其中<code>"packages/*"</code>是社区的常见写法，也可以枚举所有package： <code>"workspaces": ["package-a", "package-b"]</code>。</p>
<h2 data-id="heading-3">命令和示例</h2>
<blockquote>
<p>PS：以下命令基于<a href="mailto:yarn@1.x">yarn@1.x</a></p>
</blockquote>
<p>假设项目中有foo和bar两个package：</p>
<pre><code class="hljs language-bash copyable" lang="bash">mono-demo/
|--package.json
|--packages/
|  |--foo/
|  |  |--package.json
|  |--bar/
|  |  |--package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><code>yarn workspace <workspace_name> <command></code></h3>
<p>在指定的package中运行指定的命令。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 在foo中添加react，react-dom作为devDependencies</span>
yarn workspace foo add react react-dom --dev

<span class="hljs-comment"># 移除bar中的lodash依赖</span>
yarn workspace bar remove lodash

<span class="hljs-comment"># 运行bar中package.json的 scripts.test 命令</span>
yarn workspace bar run <span class="hljs-built_in">test</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><code>yarn workspaces run <command></code></h3>
<p>在所有package中运行指定的命令，若某个package中没有对应的命令则会报错。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 运行所有package（foo、bar）中package.json的 scripts.build 命令</span>
yarn workspaces run build
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><code>yarn workspaces info [--json]</code></h3>
<p>查看项目中的workspace依赖树。</p>
<p>例如我的bar依赖了foo，如下：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// bar/package.json</span>
&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"bar"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"foo"</span>: <span class="hljs-string">"^1.0.0"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目中的依赖结构是这样的（假设foo/package.json的版本匹配bar的依赖版本，否则会另外安装一个匹配的foo）：</p>
<pre><code class="hljs language-bash copyable" lang="bash">/package.json
/yarn.lock

/node_modules
/node_modules/foo -> /packages/foo

/packages/foo/package.json
/packages/bar/package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么运行<code>yarn workspaces info</code>会得到如下输出：</p>
<pre><code class="hljs language-bash copyable" lang="bash">yarn workspaces v1.22.4
&#123;
  <span class="hljs-string">"bar"</span>: &#123;
    <span class="hljs-string">"location"</span>: <span class="hljs-string">"packages/bar"</span>,
    <span class="hljs-string">"workspaceDependencies"</span>: [
      <span class="hljs-string">"foo"</span>
    ],
    <span class="hljs-string">"mismatchedWorkspaceDependencies"</span>: []
  &#125;,
  <span class="hljs-string">"foo"</span>: &#123;
    <span class="hljs-string">"location"</span>: <span class="hljs-string">"packages/foo"</span>,
    <span class="hljs-string">"workspaceDependencies"</span>: [],
    <span class="hljs-string">"mismatchedWorkspaceDependencies"</span>: []
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><code>yarn <add|remove> <package> -W</code></h3>
<ul>
<li>-W: --ignore-workspace-root-check ，允许依赖被安装在workspace的根目录</li>
</ul>
<p>管理根目录的依赖。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装eslint作为根目录的devDependencies</span>
yarn add eslint -D -W
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Yarn Workspace与Lerna</h2>
<p><a href="https://github.com/lerna/lerna#readme" target="_blank" rel="nofollow noopener noreferrer">Lerna</a>是社区主流的monorepo管理工具之一，集成了依赖管理、版本发布管理等功能。</p>
<p>使用Learn管理的项目的目录结构和yarn workspace类似。</p>
<p>Lerna的依赖管理是也基于<code>yarn/npm</code>，但是安装依赖的方式和yarn workspace有些差异：</p>
<p>Yarn workspace只会在根目录安装一个node_modules，这有利于提升依赖的安装效率和不同package间的版本复用。而Lerna默认会进到每一个package中运行<code>yarn/npm install</code>，并在每个package中创建一个node_modules。</p>
<p>目前社区中最主流的方案，也是yarn官方推荐的方案，是集成yarn workspace和lerna。使用yarn workspace来管理依赖，使用lerna来管理npm包的版本发布。</p>
<h2 data-id="heading-9">参考</h2>
<ul>
<li><a href="https://classic.yarnpkg.com/en/docs/workspaces" target="_blank" rel="nofollow noopener noreferrer">Workspaces Document</a></li>
<li><a href="https://classic.yarnpkg.com/blog/2017/08/02/introducing-workspaces/" target="_blank" rel="nofollow noopener noreferrer">Workspaces in Yarn</a></li>
</ul></div>  
</div>
            