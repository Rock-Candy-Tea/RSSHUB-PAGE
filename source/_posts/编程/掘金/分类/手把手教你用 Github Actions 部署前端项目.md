
---
title: '手把手教你用 Github Actions 部署前端项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/062656aeb5364e1fa7336e772b67d859~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 16:15:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/062656aeb5364e1fa7336e772b67d859~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/062656aeb5364e1fa7336e772b67d859~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 96 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://zoo.team/article/use-git-actions" target="_blank" rel="nofollow noopener noreferrer">手把手教你用 Github Actions 部署前端项目</a></p>
</blockquote>
<p><img alt="明昼.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de4e33841ece4711a7b2688ae4ae1393~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">为什么使用 Github Actions ？</h1>
<p>众所周知，前端部署无非就是把打包之后的代码丢到 nginx html 目录下就完事了，但是每逢产品频繁改需求，甚至只是让你改线上一个字的时候，你总要重复一遍遍以下动作：修改，打包，登录服务器，上传代码，重启服务器。久而久之，别说是你受不了了，搁我旁边看着都受不了。这个时候，有没有想过有个机器人，能帮我们完成以上这些重复又没技术含量的活。没错，你猜对了，Github Actions 就是我们需要的那个机器人。</p>
<h1 data-id="heading-1">Github Actions 是什么？</h1>
<p>大家知道，<a href="https://www.ruanyifeng.com/blog/2015/09/continuous-integration.html?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">持续集成</a>由很多操作组成，比如拉取最新代码、运行测试、登录服务器、部署服务器等，GitHub 把这些操作统一称为 Actions 。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8b91cda03b24380b88417a8fbfd5a68~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们再梳理下正常需求的开发流程（如上图），以上操作是可重复利用的，利用这一概念，Github 集成了 Actions  市场，允许开发者把操作写成独立的脚本，发布到 Actions 市场，允许所有开发者使用，这里有点像 npm 和 vscode 中的插件。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10d0a151f9f645948754902968bec7ce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Github 给我们提供了一个以下配置的服务器来运行我们配置对应的 Actions</p>
<ul>
<li>2-core CPU</li>
<li>7 GB of RAM memory</li>
<li>14 GB of SSD disk space</li>
</ul>
<p>这个配置足够我们使用了，当然，如果你有网络时延的需求，（比如推送及拉取镜像时产生的网络时延），你也可以<a href="https://docs.github.com/cn/actions/hosting-your-own-runners?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">自建服务器</a>。</p>
<h1 data-id="heading-2">开始：部署自己的前端项目</h1>
<h2 data-id="heading-3">1、选择 Github 项目仓库</h2>
<p>这里我选择了刚开始很久以前学习 vue 时做的模仿bilibili做的项目 <a href="https://github.com/zlyyyy/bilibili-vue?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">bilibili-vue</a> ，进入项目仓库，可以看到对应的 Actions 标签，点击进入。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd6f838d27c74d099e90a735088fb0b6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">2、新建工作流，配置  Actions</h2>
<p>进入 Actions 后可以看到很多推荐的工作流模版，这里可以根据需要自行选择需要的模版，或者跳过模版，自行设置。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/857904631a6f480cb38d68a93d06782a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里因为我是纯前端项目，所以我选择 Node.js 模版。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86efdace59c74792b0c74a192954a454~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>点击 node.js 模版，会自动在项目 <code>.github/workflows 目录下生成 node.js.yml</code> 文件，我们可以把文件名字改成我们工作流的名称。当然，这里可以设置并存在很多工作流 <code>yml</code> 文件，例如 deploy.yml、test.yml、gh-page.yml 等。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-comment"># workflow名称。省略的话，默认为当前workflow文件名</span>
<span class="hljs-attr">name:</span> <span class="hljs-string">Node.js</span> <span class="hljs-string">CI</span>
<span class="hljs-comment"># 触发workflow的条件，</span>
<span class="hljs-attr">on:</span>
<span class="hljs-attr">push:</span>
<span class="hljs-comment"># 只有master分支发生push事件时，才会触发workflow</span>
<span class="hljs-attr">branches:</span> [ <span class="hljs-string">master</span> ]
<span class="hljs-attr">pull_request:</span>
<span class="hljs-attr">branches:</span> [ <span class="hljs-string">master</span> ]
<span class="hljs-comment"># jobs表示执行的一项或多项任务</span>
<span class="hljs-attr">jobs:</span>
<span class="hljs-comment"># 任务的job_id，具体名称自定义，这里build代表打包</span>
<span class="hljs-attr">build:</span>

<span class="hljs-comment"># runs-on字段指定运行所需要的虚拟机环境。注意：这个是必填字段</span>
<span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
<span class="hljs-comment"># 用于配置当前workflow的参数</span>
<span class="hljs-attr">strategy:</span>
<span class="hljs-attr">matrix:</span>
<span class="hljs-attr">node-version:</span> [<span class="hljs-number">10.</span><span class="hljs-string">x</span>, <span class="hljs-number">12.</span><span class="hljs-string">x</span>, <span class="hljs-number">14.</span><span class="hljs-string">x</span>, <span class="hljs-number">15.</span><span class="hljs-string">x</span>]
<span class="hljs-comment"># See supported Node.js release schedule at https://nodejs.org/en/about/releases/</span>
<span class="hljs-comment"># steps字段指定每个job的运行步骤，可以包含一个或多个步骤，每个步骤都可以配置指定字段</span>
<span class="hljs-attr">steps:</span>
<span class="hljs-comment"># 切代码到 runner</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>
<span class="hljs-comment"># 在当前操作系统安装node</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Use</span> <span class="hljs-string">Node.js</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">matrix.node-version</span> <span class="hljs-string">&#125;&#125;</span>
<span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-node@v1</span>
<span class="hljs-attr">with:</span>
<span class="hljs-attr">node-version:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">matrix.node-version</span> <span class="hljs-string">&#125;&#125;</span>
<span class="hljs-comment"># 该运行的命令或者action</span>
<span class="hljs-comment"># 安装依赖、运行测试、打包</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">install</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">test</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">run</span> <span class="hljs-string">build</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3、常见的 Actions 配置</h2>
<h3 data-id="heading-6">打版本标签 Create Tag Release</h3>
<blockquote>
<p>这里使用 Actions 市场中的 <a href="https://github.com/marketplace/actions/create-tag-release?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">Create Tag Release</a> 插件</p>
</blockquote>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">on:</span>
  <span class="hljs-attr">push:</span>
    <span class="hljs-comment"># Sequence of patterns matched against refs/tags</span>
    <span class="hljs-attr">tags:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">'v*'</span> <span class="hljs-comment"># Push events to matching v*, i.e. v1.0, v20.15.10</span>
<span class="hljs-attr">name:</span> <span class="hljs-string">Create</span> <span class="hljs-string">Release</span>
<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">build:</span>
    <span class="hljs-attr">name:</span> <span class="hljs-string">Create</span> <span class="hljs-string">Release</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
    <span class="hljs-attr">steps:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Checkout</span> <span class="hljs-string">code</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@master</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Create</span> <span class="hljs-string">Release</span>
        <span class="hljs-attr">id:</span> <span class="hljs-string">create_release</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/create-release@latest</span>
        <span class="hljs-attr">env:</span>
          <span class="hljs-attr">GITHUB_TOKEN:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.GITHUB_TOKEN</span> <span class="hljs-string">&#125;&#125;</span> <span class="hljs-comment"># This token is provided by Actions, you do not need to create your own token</span>
        <span class="hljs-attr">with:</span>
          <span class="hljs-attr">tag_name:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">github.ref</span> <span class="hljs-string">&#125;&#125;</span>
          <span class="hljs-attr">release_name:</span> <span class="hljs-string">Release</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">github.ref</span> <span class="hljs-string">&#125;&#125;</span>
          <span class="hljs-attr">body:</span> <span class="hljs-string">|
            Changes in this Release
            - First Change
            - Second Change
</span>          <span class="hljs-attr">draft:</span> <span class="hljs-literal">false</span>
          <span class="hljs-attr">prerelease:</span> <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">创建 Github Pages 站点</h3>
<blockquote>
<p>这里使用 Actions 市场中的 <a href="https://github.com/marketplace/actions/github-pages-v3?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">GitHub Pages v3</a> 插件</p>
</blockquote>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">github</span> <span class="hljs-string">pages</span>
<span class="hljs-attr">on:</span>
  <span class="hljs-attr">push:</span>
    <span class="hljs-attr">branches:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">master</span> <span class="hljs-comment"># default branch</span>
<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">deploy:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-18.04</span>
    <span class="hljs-attr">steps:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">install</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">run</span> <span class="hljs-string">docs:build</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Deploy</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">peaceiris/actions-gh-pages@v3</span>
        <span class="hljs-attr">with:</span>
          <span class="hljs-attr">github_token:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.GITHUB_TOKEN</span> <span class="hljs-string">&#125;&#125;</span>
          <span class="hljs-attr">publish_dir:</span> <span class="hljs-string">./docs-dist</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">多人协作开发，云端代码检测</h3>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">Test</span>

<span class="hljs-attr">on:</span> [<span class="hljs-string">push</span>, <span class="hljs-string">pull_request</span>]

<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">lint:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
    <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-node@v1</span>
      <span class="hljs-attr">with:</span>
        <span class="hljs-attr">node-version:</span> <span class="hljs-string">'12.x'</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">dependencies</span>
      <span class="hljs-attr">uses:</span> <span class="hljs-string">bahmutov/npm-install@v1</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Run</span> <span class="hljs-string">linter</span>
      <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">run</span> <span class="hljs-string">lint</span>

  <span class="hljs-attr">test:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
    <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-node@v1</span>
      <span class="hljs-attr">with:</span>
        <span class="hljs-attr">node-version:</span> <span class="hljs-string">'12.x'</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">dependencies</span>
      <span class="hljs-attr">uses:</span> <span class="hljs-string">bahmutov/npm-install@v1</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Run</span> <span class="hljs-string">test</span>
      <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">test</span>

  <span class="hljs-attr">build:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
    <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-node@v1</span>
      <span class="hljs-attr">with:</span>
        <span class="hljs-attr">node-version:</span> <span class="hljs-string">'12.x'</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span> <span class="hljs-string">dependencies</span>
      <span class="hljs-attr">uses:</span> <span class="hljs-string">bahmutov/npm-install@v1</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Build</span>
      <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">run</span> <span class="hljs-string">build</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是 Github 中常见的一些配置，更多 <a href="https://docs.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">Actions 配置</a>可以参考官网。</p>
<h2 data-id="heading-9">4、搭配 docker</h2>
<blockquote>
<p>为什么要使用 docker ？</p>
</blockquote>
<p>没有 docker 之前，我是使用 webhook 实现自动部署，但后面遇到了服务器到期更换服务器的时候，就只能一个个重复操作来做迁移，而且文件目录管理混乱，项目变多时，维护成本也会越来越高。再看 docker 五大优势：持续集成、版本控制、可移植性、隔离性和安全性，是不是就是用来解决我们上述遇到的问题的。</p>
<p>举例：<a href="https://github.com/zlyyyy/bilibili-vue?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">bilibili-vue</a> ，不明白的同学可以参考我的配置。</p>
<h3 data-id="heading-10">4.1 项目根目录新建 Nginx 配置</h3>
<p>项目根目新建 nginx 配置文件命名 vhost.nginx.conf（名字随便定，跟后面 <strong>Dockerfile</strong> 中引用一致即可）供后续使用，例：</p>
<pre><code class="hljs language-json copyable" lang="json">server &#123;
listen 80;
server_name localhost;
location / &#123;
root /usr/share/nginx/html;
index index.html index.htm;
proxy_set_header Host $host;
if (!-f $request_filename) &#123;
rewrite ^.*$ /index.html break;
&#125;
&#125;
error_page <span class="hljs-number">500</span> <span class="hljs-number">502</span> <span class="hljs-number">503</span> <span class="hljs-number">504</span> /<span class="hljs-number">50</span>x.html;
location = /<span class="hljs-number">50</span>x.html &#123;
root /usr/share/nginx/html;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">4.2 项目根目录新建 <strong>Dockerfile</strong> 文件</h3>
<p>项目根目录新建 <strong>Dockerfile</strong> 文件，构建镜像包使用，例：</p>
<pre><code class="hljs language-dockerfile copyable" lang="dockerfile"><span class="hljs-keyword">FROM</span> nginx
<span class="hljs-keyword">COPY</span><span class="bash"> ./dist/ /usr/share/nginx/html/</span>
<span class="hljs-comment"># 第一步nginx配置文件名称</span>
  <span class="hljs-keyword">COPY</span><span class="bash"> ./vhost.nginx.conf /etc/nginx/conf.d/bilibili-vue.conf</span>
<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">80</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4.3 配置容器镜像服务</h3>
<p>这里我选择了<a href="https://www.aliyun.com/product/acr?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">阿里云的</a><a href="https://www.aliyun.com/product/acr?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">容器镜像服务</a>，为什么不使用国外的 <a href="https://hub.docker.com/?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">dockhub</a> 呢，因为这样使用起来速度快一点，而且有免费的个人版足够我们使用。</p>
<h4 data-id="heading-13">4.3.1 第一步</h4>
<p>初次打开需要开通服务，配置登录密码（记下来，后面要用）。</p>
<h4 data-id="heading-14">4.3.2 第二步</h4>
<p>然后创建命名空间，再创建我们的镜像仓库，这里如果不想别人下载你的镜像的话就可以选择私有。然后点击下一步配置代码源，这里我选择了本地仓库，一方面是为了日志统一，可以在 Github Actions 看到所有日志，一方面是可以通过命令行直接推送镜像到镜像仓库，自由度比较高。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d6a271741c64d03b4996cefacd4cd32~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">4.3.3 第三步</h4>
<p>之后就可以在页面看到我们创建的仓库，点击仓库名称进入，可以看到仓库的基本信息和操作指南，这个时候一个镜像仓库就完全创建成功了。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4947305f1d3245b583f677c2124f95c5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbe33f7db28f4de3a796bddcfbd3e79b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">4.4 如何跟 Actions 联动</h3>
<p>我们只用在 Actions 中 build 镜像后登录阿里云 Registry 实例就好了，但是这个时候如果明文直接写在 yml 中肯定是不行的，Github 早就帮我们考虑到了这点，回到 Github 项目中，依次点击 Settings => Secrets => New repository secret ，设置 secret ，配置上述容器镜像账号的用户名（阿里云用户名）和密码（上述配置容器镜像服务时设置的登录密码）。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ca798f732d34d6ba23504e67582c752~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">5、完整的 Actions</h2>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">Docker</span> <span class="hljs-string">Image</span> <span class="hljs-string">CI</span> <span class="hljs-comment"># Actions名称</span>
<span class="hljs-attr">on:</span> [<span class="hljs-string">push</span>] <span class="hljs-comment"># 执行时机</span>
<span class="hljs-attr">jobs:</span>

<span class="hljs-comment"># 这里我使用的是yarn，想用npm的同学将yarn命令修改为npm命令即可</span>
<span class="hljs-attr">build:</span>
<span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
<span class="hljs-attr">steps:</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">checkout</span>
<span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@master</span>
<span class="hljs-comment"># 安装依赖</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">install</span>
<span class="hljs-attr">run:</span> <span class="hljs-string">yarn</span>
<span class="hljs-comment"># 打包</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">build</span> <span class="hljs-string">project</span>
<span class="hljs-attr">run:</span> <span class="hljs-string">yarn</span> <span class="hljs-string">run</span> <span class="hljs-string">build</span>

<span class="hljs-comment"># 打包镜像推送到阿里云容器镜像服务</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Build</span> <span class="hljs-string">the</span> <span class="hljs-string">Docker</span> <span class="hljs-string">image</span>
<span class="hljs-attr">run:</span> <span class="hljs-string">|</span>
<span class="hljs-string">docker</span> <span class="hljs-string">login</span> <span class="hljs-string">--username=$&#123;&#123;</span> <span class="hljs-string">secrets.DOCKER_USERNAME</span> <span class="hljs-string">&#125;&#125;</span> <span class="hljs-string">registry.cn-hangzhou.aliyuncs.com</span> <span class="hljs-string">--password=$&#123;&#123;</span> <span class="hljs-string">secrets.DOCKER_PASSWORD</span> <span class="hljs-string">&#125;&#125;</span>
<span class="hljs-string">docker</span> <span class="hljs-string">build</span> <span class="hljs-string">-t</span> <span class="hljs-string">bilibili-vue:latest</span> <span class="hljs-string">.</span>
<span class="hljs-string">docker</span> <span class="hljs-string">tag</span> <span class="hljs-string">bilibili-vue</span> <span class="hljs-string">registry.cn-hangzhou.aliyuncs.com/zlyyyy/bilibili-vue:latest</span>
<span class="hljs-string">docker</span> <span class="hljs-string">push</span> <span class="hljs-string">registry.cn-hangzhou.aliyuncs.com/zlyyyy/bilibili-vue:latest</span> <span class="hljs-comment"># 推送</span>
<span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">ssh</span> <span class="hljs-string">docker</span> <span class="hljs-string">login</span> <span class="hljs-comment"># 使用appleboy/ssh-action@master登录服务器执行拉取镜像脚本，服务器ip、用户名、密码配置方式同容器镜像服务配置方式一样</span>
<span class="hljs-attr">uses:</span> <span class="hljs-string">appleboy/ssh-action@master</span>
<span class="hljs-attr">with:</span>
        <span class="hljs-attr">host:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.SSH_HOST</span> <span class="hljs-string">&#125;&#125;</span> 
<span class="hljs-attr">username:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.SSH_USERNAME</span> <span class="hljs-string">&#125;&#125;</span>
<span class="hljs-attr">password:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.SSH_PASSWORD</span> <span class="hljs-string">&#125;&#125;</span>
<span class="hljs-attr">script:</span> <span class="hljs-string">cd</span> <span class="hljs-string">~</span> <span class="hljs-string">&&</span> <span class="hljs-string">sh</span> <span class="hljs-string">bilibili-vue-deploy.sh</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.DOCKER_USERNAME</span> <span class="hljs-string">&#125;&#125;</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.DOCKER_PASSWORD</span> <span class="hljs-string">&#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一步登录服务器后，我执行了一个脚本来拉取云端最新镜像，并删除旧镜像，启动新镜像。脚本内容如下。</p>
<pre><code class="hljs language-shell copyable" lang="shell">echo -e "---------docker Login--------"
docker login --username=$1 registry.cn-hangzhou.aliyuncs.com --password=$2
echo -e "---------docker Stop--------"
docker stop bilibili-vue
echo -e "---------docker Rm--------"
docker rm bilibili-vue
docker rmi registry.cn-hangzhou.aliyuncs.com/zlyyyy/bilibili-vue:latest
echo -e "---------docker Pull--------"
docker pull registry.cn-hangzhou.aliyuncs.com/zlyyyy/bilibili-vue:latest
echo -e "---------docker Create and Start--------"
docker run --rm -d -p 8081:80 --name bilibili-vue registry.cn-hangzhou.aliyuncs.com/zlyyyy/bilibili-vue:latest
echo -e "---------deploy Success--------"
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">6、测试流程，查看日志</h2>
<p>我们推送一次代码测试，打开 Actions 后可以看到自动运行的实时 workflow 结果，以及每步的日志信息。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca263a1a9a749b28a2fb3659e68b970~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92112ab947984c40b0a8b47abc535a0e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-19">总结</h1>
<p>到此我们自动化部署成功，再也不要每次修改代码，手动更新线上了，后面迁移也会更方便，当然还有更多的自动化部署方式，比如直接使用 Github + 阿里云镜像仓库的触发器一样可以做到，容器服务也不仅限于阿里云，腾讯云等其他云服务厂商同样也是一样的使用方式。以上是我个人使用 Actions 的一些总结，如有错误，劳烦指正修改。当然对更多 Actions 玩法感兴趣的同学欢迎一起交流学习。当然这个仅限于个人的项目玩法，公司内部的项目有更加成熟完善的自动化方案，比如我们内部所使用的云长系统，就是解决此类问题的，具体云长的功能，他做了些什么，敬请期待。</p>
<h1 data-id="heading-20">参考文献</h1>
<p><a href="http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">GitHub Actions 入门教程</a></p>
<p><a href="https://www.ruanyifeng.com/blog/2015/09/continuous-integration.html?fileGuid=1PWJAvQBtLA5IGh3" target="_blank" rel="nofollow noopener noreferrer">持续集成是什么？</a></p>
<h2 data-id="heading-21">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6945624014643855367" target="_blank">通过自定义Vue指令实现前端曝光埋点</a></p>
<p><a href="https://juejin.cn/post/6948210854126944292" target="_blank">H5 页面列表缓存方案</a></p>
<h2 data-id="heading-22">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab2a1ec7678442a7a8943f76fb0bdea0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            