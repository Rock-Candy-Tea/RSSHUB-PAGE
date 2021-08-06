
---
title: '京东购物小程序 _ Taro3 项目分包实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18815dc96e494cd692dbbe4bc6145228~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 03:43:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18815dc96e494cd692dbbe4bc6145228~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>京东购物小程序作为京东小程序业务流量的主要入口，承载着许多的活动和页面，而很多的活动在小程序开展的同时，也会在京东 APP 端进行同步的 H5 端页面的投放。这时候，一个相同的活动，<strong>需要同时开发原生小程序页面和H5页面的难题</strong>又摆在了前端程序员的面前。
幸运的是，我们有 Taro，一个开放式跨端跨框架解决方案。可以帮助我们很好地解决这种跨端开发的问题。但不幸的是，<strong>Taro 并没有提供一套完整的将项目作为独立分包运行在小程序中的解决方案</strong>。因此，本篇文章将介绍如何<strong>通过一套合适的混合开发实践方案，解决 Taro 项目作为独立分包后出现的一些问题</strong>。</p>
<h2 data-id="heading-1">目录</h2>
<ul>
<li>背景</li>
<li>整体流程</li>
<li>应用过程
<ul>
<li>准备合适的开发环境</li>
<li>将 Taro 项目作为独立分包进行编译打包</li>
<li>引入 @tarojs/plugin-indie 插件，保证 Taro 前置逻辑优先执行</li>
<li>引入 @tarojs/plugin-mv 插件，自动化挪动打包后的文件</li>
<li>引入公共方法、公共基类和公共组件
<ul>
<li>引入公共方法</li>
<li>引入公共组件</li>
<li>引入页面公共基类</li>
</ul>
</li>
</ul>
</li>
<li>存在问题</li>
<li>后续</li>
</ul>
<h2 data-id="heading-2">整体流程</h2>
<p>总的来说，若要使用 Taro 3 将项目作为独立分包运行在京东购物小程序，我们需要完成以下四个步骤：</p>
<ol>
<li><strong>准备开发环境</strong>，下载正确的 Taro 版本</li>
<li>安装 <strong>Taro 混合编译插件</strong>，解决独立分包的运行时逻辑问题</li>
<li>调用 Taro 提供的<strong>混合编译命令</strong>，对 Taro 项目进行打包</li>
<li><strong>挪动打包后 Taro 文件</strong>到主购小程序目录下</li>
</ol>
<p>那么接下来，我们将对每个步骤进行详细的说明，告诉大家怎么做，以及为什么要这样做。</p>
<h2 data-id="heading-3">应用过程</h2>
<h3 data-id="heading-4">准备合适的开发环境</h3>
<p>首先我们需要全局安装 Taro 3，并保证<strong>全局和项目下的 Taro 的版本高于<code>3.1.4</code></strong>，这里我们以新建的<code>Taro 3.2.6</code>项目为例：</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn global add @tarojs/cli@3.2.6

taro init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后我们在项目中用<code>React</code>语法写入简单的 <code>hello word</code> 代码，并在代码中留出一个<code>Button</code>组件来为将来调用京东购物小程序的公共跳转方法做准备。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/pages/index/index.jsx</span>

<span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View, Text, Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/components'</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.scss'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  handleButtonClick () &#123;
    <span class="hljs-comment">// 调用京东购物小程序的公共跳转方法</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'trigger click'</span>)
  &#125;

  render () &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span>></span>Hello world!<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleButtonClick.bind(this)&#125;</span> ></span>点击跳转到主购首页<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>俗话说得好，有竟者事竟成，在开始编码前，我们来简单地定几个小目标：</p>
<ul>
<li><strong>成功地将 Taro 项目 Hello world 在京东购物小程序的分包路由下跑通</strong></li>
<li><strong>引入京东购物小程序的公共组件 nav-bar 并能正常使用</strong></li>
<li><strong>引入公共方法 navigator.goto 并能正常使用</strong></li>
<li><strong>引入公共基类 JDPage 并能正常使用</strong></li>
</ul>
<h3 data-id="heading-5">将 Taro 项目作为独立分包进行编译打包</h3>
<p>在将 Taro 项目打包进主购小程序时，我们很快就遇到了第一个难题：Taro 项目下默认的命令打包出来的文件是一整个小程序，<strong>如何打包成一个单独的分包？</strong></p>
<p>幸运的是，在<code>3.1.4</code>版本后的 Taro，提供了混合开发的功能，意思为可以让原生项目和 Taro 打包出来的文件混合使用，只需要<strong>在打包时加入 <code>--blended</code> 命令</strong>即可。</p>
<pre><code class="copyable">cross-env NODE_ENV=production taro build --type weapp --blended
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>blended</code> 中文翻译是混合的意思，在加入了这个命令后，Taro 会在构建出来的 <code>app.js</code> 文件中导出 <code>taroApp</code>，我们可以通过引入这个变量来在原生项目下的 <code>app.js</code> 调用 Taro 项目 app 的 onShow、onHide 等生命周期。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 必须引用 Taro 项目的入口文件</span>
<span class="hljs-keyword">const</span> taroApp = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./taro/app.js'</span>).taroApp

App(&#123;
  onShow () &#123;
    <span class="hljs-comment">// 可选，调用 Taro 项目 app 的 onShow 生命周期</span>
    taroApp.onShow()
  &#125;,

  onHide () &#123;
    <span class="hljs-comment">// 可选，调用 Taro 项目 app 的 onHide 生命周期</span>
    taroApp.onHide()
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果单纯地使用 <code>blended</code> 命令，即使我们不需要调用 onShow、onHide 这些生命周期，我们也需要<strong>在原生项目下的 <code>app.js</code> 里引入Taro项目的入口文件</strong>，因为在执行我们的小程序页面时，我们需要提前初始化一些运行时的逻辑，因此要保证 Taro 项目下的 <code>app.js</code> 文件里的逻辑能优先执行。</p>
<p>理想很丰满，现实很骨感，由于我们需要将 Taro 项目作为单独的分包打包到主购项目中，因此这种直接在原生项目的 app.js 中引入的方式<strong>只适用于主包内的页面，而不适用于分包。</strong></p>
<h3 data-id="heading-6">引入 @tarojs/plugin-indie 插件，保证 Taro 前置逻辑优先执行</h3>
<p>要解决混合开发在分包模式下不适用的问题，我们需要引入另外一个 Taro 插件 <code>@tarojs/plugin-indie</code>。</p>
<p>首先我们先在 Taro 项目中对该插件进行安装</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add --dev @tarojs/plugin-indie
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后我们在 Taro 的配置项文件中对该插件进行引入</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// config/index.js</span>
<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-string">'@tarojs/plugin-indie'</span>
  ] 
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看该插件的源码，我们可以发现该插件处理的逻辑非常简单，就是在编译代码时，对每个页面下的 <code>js chunk</code> 文件内容进行调整，在这些 js 文件的开头加上 <code>require("../../app")</code>,并增加对应 <code>module</code> 的 <code>sourceMap</code> 映射。在进行了这样的处理后，便能保证<strong>每次进入 Taro 项目下的小程序页面时，都能优先执行 Taro 打包出来的运行时文件了。</strong></p>
<h3 data-id="heading-7">引入 @tarojs/plugin-mv 插件，自动化挪动打包后的文件</h3>
<p>到目前为止，我们已经可以成功打包出能独立分包的 Taro 小程序文件了，接下来，我们需要将打包出来的 <code>dist</code> 目录下的文件挪到主购项目中。</p>
<p>手动挪动？no，一个优秀的程序员应该想尽办法在开发过程中“偷懒”。
因此我们会自定义一个 Taro 插件，在 Taro 打包完成的时候，<strong>自动地将打包后的文件移动到主购项目中。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// plugin-mv/index.js</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs-extra'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (ctx, options) => &#123;
  ctx.onBuildFinish(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> blended = ctx.runOpts.blended || ctx.runOpts.options.blended
    
    <span class="hljs-keyword">if</span> (!blended) <span class="hljs-keyword">return</span>

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'编译结束！'</span>)

    <span class="hljs-keyword">const</span> rootPath = path.resolve(__dirname, <span class="hljs-string">'../..'</span>)
    <span class="hljs-keyword">const</span> miniappPath = path.join(rootPath, <span class="hljs-string">'wxapp'</span>)
    <span class="hljs-keyword">const</span> outputPath = path.resolve(__dirname, <span class="hljs-string">'../dist'</span>)

    <span class="hljs-comment">// testMini是你在京东购物小程序项目下的路由文件夹</span>
    <span class="hljs-keyword">const</span> destPath = path.join(miniappPath, <span class="hljs-string">`./pages/testMini`</span>)

    <span class="hljs-keyword">if</span> (fs.existsSync(destPath)) &#123;
      fs.removeSync(destPath)
    &#125;
    fs.copySync(outputPath, destPath)

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'拷贝结束！'</span>)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置文件中加入这个自定义插件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// config/index.js</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-string">'@tarojs/plugin-indie'</span>,
    path.join(process.cwd(), <span class="hljs-string">'/plugin-mv/index.js'</span>)
  ] 
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新执行<code>cross-env NODE_ENV=production taro build --type weapp --blended</code>打包命令，即可将 Taro 项目打包并拷贝到京东购物小程序项目对应的路由文件夹中。</p>
<p>至此，我们便可在开发者工具打开主购小程序项目，在 <code>app.json</code> 上添加对应的页面路由，并条件编译该路由，即可顺利地在开发者工具上看到 <code>Hello World</code> 字样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18815dc96e494cd692dbbe4bc6145228~tplv-k3u1fbpfcp-watermark.image" alt="效果图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">引入公共方法、公共基类和公共组件</h3>
<p>在日常的主购项目开发中，我们经常需要用到主购原生项目下封装的一些公共模块和方法，那么，通过混合编译打包过来的 Taro 项目是否也能通过某种办法顺利引用这些方法和模块呢？</p>
<p>答案是可以的。</p>
<h4 data-id="heading-9">引入公共方法</h4>
<p>先简单说一下思路，更改 webpack 的配置项，<strong>通过 externals 配置处理公共方法和公共模块的引入</strong>，保留这些引入的语句，并将引入方式设置成 commonjs 相对路径的方式，详细代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">mini</span>: &#123;
    <span class="hljs-comment">// ...</span>
    webpackChain (chain) &#123;
      chain.merge(&#123;
        <span class="hljs-attr">externals</span>: [
          <span class="hljs-function">(<span class="hljs-params">context, request, callback</span>) =></span> &#123;
            <span class="hljs-keyword">const</span> externalDirs = [<span class="hljs-string">'@common'</span>, <span class="hljs-string">'@api'</span>, <span class="hljs-string">'@libs'</span>]
            <span class="hljs-keyword">const</span> externalDir = externalDirs.find(<span class="hljs-function"><span class="hljs-params">dir</span> =></span> request.startsWith(dir))

            <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">'production'</span> && externalDir) &#123;
              <span class="hljs-keyword">const</span> res = request.replace(externalDir, <span class="hljs-string">`../../../../<span class="hljs-subst">$&#123;externalDir.substr(<span class="hljs-number">1</span>)&#125;</span>`</span>)

              <span class="hljs-keyword">return</span> callback(<span class="hljs-literal">null</span>, <span class="hljs-string">`commonjs <span class="hljs-subst">$&#123;res&#125;</span>`</span>)
            &#125;

            callback()
          &#125;,
        ],
      &#125;)
    &#125;
    <span class="hljs-comment">// ...</span>
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这样的处理之后，我们就可以顺利地在代码中通过 <code>@common/*</code>、<code>@api/*</code> 和 <code>@libs/*</code> 来引入原生项目下的 <code>common/*</code>、<code>api/*</code> 和 <code>libs/*</code> 了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/pages/index/index.jsx</span>

<span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View, Text, Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/components'</span>

<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> navigator <span class="hljs-keyword">from</span> <span class="hljs-string">'@common/navigator.js'</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.scss'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  handleButtonClick () &#123;
    <span class="hljs-comment">// 调用京东购物小程序的公共跳转方法</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'trigger click'</span>)
    <span class="hljs-comment">// 利用公共方法跳转京东购物小程序首页</span>
    navigator.goto(<span class="hljs-string">'/pages/index/index'</span>)
  &#125;

  render () &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span>></span>Hello world!<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleButtonClick.bind(this)&#125;</span> ></span>点击跳转到主购首页<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>能看到引入的公共方法在打包后的小程序页面中也能顺利跑通了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c22b68a481d24a439918ab1e9566048c~tplv-k3u1fbpfcp-watermark.image" alt="跳转动画" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">引入公共组件</h4>
<p>公共组件的引入更加简单，Taro 默认有提供引入公共组件的功能，但是如果是在混合开发模式下打包后，会发现公共组件的引用路径无法对应上，打包后页面配置的 json 文件引用的是以 Taro 打包出来的 dist 文件夹为小程序根目录，所以引入的路径也是以这个根目录为基础进行引用的，因此我们<strong>需要利用 Taro 的 alias 配置项来对路径进行一定的调整：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// pages/index/index.config.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">navigationBarTitleText</span>: <span class="hljs-string">'首页'</span>,
  <span class="hljs-attr">navigationStyle</span>: <span class="hljs-string">'custom'</span>,
  <span class="hljs-attr">usingComponents</span>: &#123;
    <span class="hljs-string">'nav-bar'</span>: <span class="hljs-string">'@components/nav-bar/nav-bar'</span>,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// config/index.js</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">alias</span>: &#123;
    <span class="hljs-string">'@components'</span>: path.resolve(__dirname, <span class="hljs-string">'../../../components'</span>),
  &#125;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们在代码中直接对公共组件进行使用，并且无需引入：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/pages/index/index.jsx</span>

<span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View, Text, Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/components'</span>

<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> navigator <span class="hljs-keyword">from</span> <span class="hljs-string">'@common/navigator.js'</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.scss'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  handleButtonClick () &#123;
    <span class="hljs-comment">// 调用京东购物小程序的公共跳转方法</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'trigger click'</span>)
    <span class="hljs-comment">// 利用公共方法跳转京东购物小程序首页</span>
    navigator.goto(<span class="hljs-string">'/pages/index/index'</span>)
  &#125;

  render () &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'index'</span>></span>
        &#123;/* 公共组件直接引入，无需引用 */&#125;
        <span class="hljs-tag"><<span class="hljs-name">nav-bar</span>
          <span class="hljs-attr">navBarData</span>=<span class="hljs-string">&#123;&#123;</span>
            <span class="hljs-attr">title:</span> '测试公共组件导航栏',
            <span class="hljs-attr">capsuleType:</span> '<span class="hljs-attr">miniReturn</span>',
            <span class="hljs-attr">backgroundValue:</span> '<span class="hljs-attr">rgba</span>(<span class="hljs-attr">0</span>, <span class="hljs-attr">255</span>, <span class="hljs-attr">0</span>, <span class="hljs-attr">1</span>)'
          &#125;&#125;
        /></span>
        <span class="hljs-tag"><<span class="hljs-name">Text</span>></span>Hello world!<span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleButtonClick.bind(this)&#125;</span> ></span>点击跳转到主购首页<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样打包出来的 <code>index.json</code> 文件中 <code>usingComponents</code> 里的路径就能完美匹配原生小程序下的公共组件文件了，我们也由此能看到公共导航栏组件 <code>nav-bar</code> 在项目中的正常使用和运行了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29b22600ce3341d5ba802039bb1ac445~tplv-k3u1fbpfcp-watermark.image" alt="导航栏使用效果图" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">引入页面公共基类</h4>
<p>在京东购物小程序，每一个原生页面在初始化的时候，基本都会引入一个 JDPage 基类，并用这个基类来修饰原本的 Page 实例，<strong>会给 Page 实例上原本的生命周期里添加一些埋点上报和参数传递等方法。</strong></p>
<p>而我们在使用 Taro 进行混合编译开发时，再去单独地实现一遍这些方法显然是一种很愚蠢的做法，所以我们需要想办法在 Taro 项目里进行类似的操作，去引入 JDPage 这个基类。</p>
<p>首先第一步，我们需要在编译后的 JS 文件里，找到 Page 实例的定义位置，这里我们会<strong>使用正则匹配</strong>，去匹配这个 Page 实例在代码中定义的位置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> pageRegx = <span class="hljs-regexp">/(Page)(\(Object.*createPageConfig.*?\&#123;\&#125;\)\))/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找到 Page 实例中，将 Page 实例转换成我们需要的 JDPage 基类，这些步骤我们都可以将他们写在我们之前自制 Taro 插件 <code>plugin-mv</code> 中去完成：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isWeapp = process.env.TARO_ENV === <span class="hljs-string">'weapp'</span>
<span class="hljs-keyword">const</span> jsReg = <span class="hljs-regexp">/pages\/(.*)\/index\.js$/</span>
<span class="hljs-keyword">const</span> pageRegx = <span class="hljs-regexp">/(Page)(\(Object.*createPageConfig.*?\&#123;\&#125;\)\))/</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (ctx, options) => &#123;
  ctx.modifyBuildAssets(<span class="hljs-function">(<span class="hljs-params">&#123; assets &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">Object</span>.keys(assets).forEach(<span class="hljs-function"><span class="hljs-params">filename</span> =></span> &#123;
      <span class="hljs-keyword">const</span> isPageJs = jsReg.test(filename)

      <span class="hljs-keyword">if</span> (!isWeapp || !isPageJs) <span class="hljs-keyword">return</span>

      <span class="hljs-keyword">const</span> replaceFn = <span class="hljs-function">(<span class="hljs-params">match, p1, p2</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`new (require('../../../../../bases/page.js').JDPage)<span class="hljs-subst">$&#123;p2&#125;</span>`</span>
      &#125;

      <span class="hljs-keyword">if</span> (
        !assets[filename]._value &&
        assets[filename].children
      ) &#123;
        assets[filename].children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
          <span class="hljs-keyword">const</span> isContentValid = pageRegx.test(child._value)

          <span class="hljs-keyword">if</span> (!isContentValid) <span class="hljs-keyword">return</span>

          child._value = child._value.replace(pageRegx, replaceFn)
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        assets[filename]._value = assets[filename]._value.replace(pageRegx, replaceFn)
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过插件处理之后，打包出来的页面 JS 里的 Page 都会被替换成 JDPage，也就拥有了基类的一些基础能力了。</p>
<p>至此，我们的 Taro 项目就基本已经打通了京东购物小程序的混合开发流程了。<strong>在能使用 Taro 无痛地开发京东购物小程序原生页面之余，还为之后的双端甚至多端运行打下了结实的基础。</strong></p>
<h2 data-id="heading-12">存在问题</h2>
<p>在使用 Taro 进行京东购物小程序原生页面的混合开发时，会发现 Taro 在一些公共样式和公共方法的处理上面，存在着以下一些兼容问题：</p>
<ol>
<li>Taro 会将多个页面的公共样式进行提取，放置于 <code>common.wxss</code> 文件中，但打包后的 <code>app.wxss</code> 文件却没有对这些公共样式进行引入，因此会导致页面的公共样式丢失。解决办法也很简单，只要在插件对 <code>app.wxss</code> 文件进行调整，添加对 <code>common.wxss</code> 的引入即可：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> wxssReg = <span class="hljs-regexp">/pages\/(.*)\/index\.wxss$/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insertContentIntoFile</span> (<span class="hljs-params">assets, filename, content</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; children, _value &#125; = assets[filename]
  <span class="hljs-keyword">if</span> (children) &#123;
    children.unshift(content)
  &#125; <span class="hljs-keyword">else</span> &#123;
    assets[filename]._value = <span class="hljs-string">`<span class="hljs-subst">$&#123;content&#125;</span><span class="hljs-subst">$&#123;_value&#125;</span>`</span>
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (ctx, options) => &#123;
  ctx.modifyBuildAssets(<span class="hljs-function">(<span class="hljs-params">&#123; assets &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">Object</span>.keys(assets).forEach(<span class="hljs-function"><span class="hljs-params">filename</span> =></span> &#123;
      <span class="hljs-keyword">const</span> isPageWxss = wxssReg.test(filename)

      <span class="hljs-comment">// ...</span>

      <span class="hljs-keyword">if</span> (isPageWxss) &#123;
        insertContentIntoFile(assets, filename, <span class="hljs-string">"@import '../../common.wxss';\n"</span>)
      &#125;
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用 Taro 打包后的 <code>app.js</code> 文件里会存在部分对京东购物小程序公共方法的引用，该部分内容使用的是和页面 JS 同一个相对路径进行引用的，因此会存在引用路径错误的问题，解决办法也很简单，对 <code>app.js</code> 里的引用路径进行调整即可：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> appReg = <span class="hljs-regexp">/app\.js$/</span>
<span class="hljs-keyword">const</span> replaceList = [<span class="hljs-string">'common'</span>, <span class="hljs-string">'api'</span>, <span class="hljs-string">'libs'</span>]
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (ctx, options) => &#123;
  ctx.modifyBuildAssets(<span class="hljs-function">(<span class="hljs-params">&#123; assets &#125;</span>) =></span> &#123;
    <span class="hljs-built_in">Object</span>.keys(assets).forEach(<span class="hljs-function"><span class="hljs-params">filename</span> =></span> &#123;
      <span class="hljs-keyword">const</span> isAppJS = appReg.test(filename)
      <span class="hljs-keyword">const</span> handleAppJsReplace = <span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        replaceList.forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
          item = item.replace(<span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`../../../../../<span class="hljs-subst">$&#123;name&#125;</span>`</span>, <span class="hljs-string">'g'</span>), <span class="hljs-string">`'../../../<span class="hljs-subst">$&#123;name&#125;</span>`</span>)
        &#125;)
      &#125;
      <span class="hljs-keyword">if</span> (isAppJS) &#123;
        <span class="hljs-keyword">if</span> (
          !assets[filename]._value &&
          assets[filename].children
        ) &#123;
          assets[filename].children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
            replaceList.forEach(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
              <span class="hljs-keyword">const</span> value = child._value ? child._value : child

              handleAppJsReplace(value)
            &#125;)
          &#125;)
        &#125; <span class="hljs-keyword">else</span> &#123;
          handleAppJsReplace(assets[filename]._value)
        &#125;
      &#125;
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">后续</h2>
<p>本篇文章主要是讲述了 Taro 项目在京东购物小程序端的应用方式和开发方式，暂无涉及 H5 部分的内容。之后计划输出一份 Taro 项目在 H5 端的开发指南，并讲述 Taro 在多端开发中的性能优化方式。</p></div>  
</div>
            