
---
title: '微前端学习系列(三)：qiankun'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4c1fd8382534ec5ac708aa5689258fa~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 22:00:29 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4c1fd8382534ec5ac708aa5689258fa~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4c1fd8382534ec5ac708aa5689258fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">目录</h3>
<ul>
<li><a href="https://juejin.cn/post/6955342295998660615#1">前言</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#2">如何使用 qiankun 快速搭建一个微前端应用</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#3">手动加载微应用/组件</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#4">常用 API</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#5">qiankun 是如何来解决 single-spa 使用过程中遇到的问题的</a>
<ul>
<li><a href="https://juejin.cn/post/6955342295998660615#5-1">子应用加载 - Html Entry vs Js Entey</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#5-2">js 隔离</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#5-3">css 隔离</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#5-4">子应用卸载副作用清理</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#5-5">子应用状态重新恢复</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#5-6">子应用通信</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#5-7">子应用预加载</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6955342295998660615#6">qiankun 的整个工作过程</a></li>
<li><a href="https://juejin.cn/post/6955342295998660615#8">结束语</a></li>
</ul>
<h3 id="user-content-1" data-id="heading-1">前言</h3>
<p>目前 <strong>single-spa</strong> 是一种比较流行且成熟的<strong>微前端方案</strong>，它可以为我们<strong>提供类似单页应用的用户体验</strong>，做到<strong>技术栈无关</strong>、<strong>多应用共存</strong>，并且通过其<strong>丰富的生态</strong>帮我们提高开发效率。但在实际项目中，面对诸如<strong>子应用加载</strong>、<strong>应用之间 js、css 的隔离</strong>、<strong>子应用切换遗留的副作用清理</strong>、<strong>子应用状态恢复</strong>以及<strong>子应用之间通信</strong>、<strong>子应用预加载</strong>之类的常见问题，<strong>single-spa</strong> 框架本身并没有给出对应的解决方案，需要开发人员自己去写代码解决，对开发人员来说不是很友好。</p>
<p>针对上述这些问题，<strong>qiankun</strong> 提供了一种新的<strong>微前端方案</strong>。在 <strong>single-spa</strong> 的基础上，<strong>qiankun</strong> 做了<strong>二次开发</strong>，提供了<strong>通用的子应用加载、通信、预加载方案</strong>，并通过<strong>技术手段</strong>实现了<strong>应用之间的 js、css 隔离</strong>以及<strong>副作用清理工作</strong>、<strong>状态恢复</strong>，帮助开发人员更加简单快捷的实现一个微前端应用。</p>
<p>接下来我们就来了解一下 <strong>qiankun</strong> 的用法，以及它是怎么来解决上面提到的问题的。</p>
<h3 id="user-content-2" data-id="heading-2">如何使用 qiankun 快速搭建一个微前端应用</h3>
<p>由于 <strong>qiankun</strong> 是在 <strong>single-spa</strong> 的基础上做的二次开发，所以 <strong>qiankun</strong> 的用法和 <strong>single-spa</strong> 基本一样，也分为 <strong>application</strong> 模式和 <strong>parcel</strong> 模式。</p>
<p><strong>application</strong> 模式是<strong>基于路由</strong>工作的，它将应用分为两类：<strong>基座应用</strong>和<strong>子应用</strong>。其中，<strong>基座应用</strong>需要维护一个<strong>路由注册表</strong>，根据<strong>路由的变化来切换子应用</strong>；<strong>子应用</strong>是一个个<strong>独立的应用</strong>，需要提供<strong>生命周期方法</strong>供<strong>基座应用</strong>使用。<strong>parcel</strong> 模式和 <strong>application</strong> 模式相反，它与<strong>路由无关</strong>，子应用切换是<strong>手动控制</strong>的。</p>
<p>接下来，我们通过官方示例 <strong><a href="https://github.com/umijs/qiankun/tree/master/examples" target="_blank" rel="nofollow noopener noreferrer">github.com/umijs/qiank…</a></strong>, 来看看 <strong>application</strong> 模式是如何使用的。</p>
<p>示例的项目结构如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00cc70e0839a4a0584bd32b3268d3438~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>示例启动以后效果如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6f0dae7a8ff44c291baee53e436dd6e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>和 <strong>single-spa</strong> 一样，我们需要对<strong>基座应用</strong>和<strong>子应用</strong>分别做改造。</p>
<ul>
<li>
<h4 data-id="heading-3"> 基座应用改造 </h4>
<p><strong>qiankun 基座应用</strong>的改造和 <strong>single-spa</strong> 基本相同，即<strong>构建一个路由注册表</strong>，然后根据<strong>路由注册表</strong>使用 <strong>qiankun</strong> 提供的 <strong>registerMicroApps</strong> 方法<strong>注册子应用</strong>，最后执行 <strong>start</strong> 方法来启动 <strong>qiankun</strong>。</p>
<p>具体代码如下：</p>
<pre><code class="copyable">  import &#123; registerMicroApps, start &#125; from 'qiankun';

  ...

  const apps = [
    &#123;
      name: 'react16',
      entry: '//localhost:7100',
      container: '#subapp-viewport',
      activeRule: '/react16',
      ...
    &#125;,
    &#123;
      name: 'react15',
      entry: '//localhost:7102',
      container: '#subapp-viewport',
      activeRule: '/react15',
      ...
    &#125;,
    &#123;
      name: 'vue',
      entry: '//localhost:7101',
      container: '#subapp-viewport',
      activeRule: '/vue',
      ...
    &#125;,
    &#123;
      name: 'angular9',
      entry: '//localhost:7103',
      container: '#subapp-viewport',
      activeRule: '/angular9',
      ...
    &#125;,
    &#123;
      name: 'purehtml',
      entry: '//localhost:7104',
      container: '#subapp-viewport',
      activeRule: '/purehtml',
    &#125;,
    &#123;
      name: 'vue3',
      entry: '//localhost:7105',
      container: '#subapp-viewport',
      activeRule: '/vue3',
      ...
    &#125;,
  ]

  const lifeCycles = &#123;
    beforeLoad: [
      app => &#123;
        console.log('[LifeCycle] before load %c%s', 'color: green;', app.name);
      &#125;,
    ],
    beforeMount: [
      app => &#123;
        console.log('[LifeCycle] before mount %c%s', 'color: green;', app.name);
      &#125;,
    ],
    afterUnmount: [
      app => &#123;
        console.log('[LifeCycle] after unmount %c%s', 'color: green;', app.name);
      &#125;,
    ],
  &#125;
  
  registerMicroApps(apps, lifeCycles);

  ...

  start();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>qiankun</strong> 基座应用中的<strong>路由注册表</strong>的结构和 <strong>single-spa</strong> 有点类似，每个子应用对应的配置项需要指定 <strong>name</strong>、<strong>entry</strong>、<strong>container</strong>、<strong>activeRule</strong>。</p>
<ul>
<li>
<p><strong>name</strong></p>
<p><strong>子应用的唯一标识</strong>，是一个<strong>字符串</strong>，<strong>不可重复</strong>。</p>
</li>
<li>
<p><strong>entry</strong></p>
<p><strong>子应用的入口</strong>，一般情况下是一个 <strong>url 字符串</strong>，即<strong>子应用的访问地址</strong>，如 <strong>localhost:8080</strong>;</p>
</li>
<li>
<p><strong>container</strong></p>
<p><strong>子应用挂载的节点</strong>，可以是一个 <strong>domElement 实例</strong>，也可以是一个 <strong>dom 元素的 id 字符串</strong>；</p>
</li>
<li>
<p><strong>activeRule</strong></p>
<p><strong>子应用激活的条件</strong>，一般是一个函数。路由发生变化时，基座应用会遍历注册的子应用，通过子应用的 <strong>activeRule</strong> 条件，找到需要激活的子应用。</p>
</li>
</ul>
</li>
<li>
<h4 data-id="heading-4"> 子应用改造</h4>
<p><strong>子应用的改造</strong>，和 <strong>single-spa</strong> 是完全一样的，涉及两个方面：</p>
<ul>
<li><strong>入口文件 index.js 添加生命周期方法 - mount、unmount、update 等</strong>；</li>
<li><strong>打包构建改造</strong>；</li>
</ul>
<p>子应用<strong>入口文件 - index</strong> 的改造如下：</p>
<pre><code class="copyable">...

function render() &#123; ... &#125;

export function mount(props) &#123; 
    ...
    render();
&#125;

export function unmount(props) &#123;...&#125;

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包构建改造如下：</p>
<pre><code class="copyable">// vue.config.js

    module.exports = &#123;
        configureWebpack: &#123;
            ...
            publicPath: 'http://localhost:7101'
            output: &#123;
                library: 'vue',
                libraryTarget: 'umd'
            &#125;,
            ...
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>完成<strong>基座应用</strong>和<strong>子应用</strong>的改造以后，<strong>启动基座应用</strong>，我们即可通过<strong>修改 url</strong> 来进行<strong>子应用的切换</strong>。</p>
<p>了解完 <strong>qiankun</strong> 的 <strong>application</strong> 模式外，我们在再了解一下 <strong>parcel</strong> 模式。</p>
<p><strong>parcel 模式</strong>是<strong>路由无关</strong>的，给了我们<strong>手动挂载/卸载/更新子应用</strong>的机会，具体是通过 <strong>qiankun</strong> 提供的 <strong>loadMicroApp</strong> 来实现的。关于 <strong>loadMicroApp</strong> 的用法，[官网] (<a href="https://qiankun.umijs.org/zh/api#loadmicroappapp-configuration)%E5%B7%B2%E7%BB%99%E4%BA%86%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E%EF%BC%8C%E5%9C%A8%E8%BF%99%E9%87%8C%E5%B0%B1%E4%B8%8D%E5%86%8D%E6%8F%90%E4%BE%9B%E7%A4%BA%E4%BE%8B%E8%AF%B4%E6%98%8E%E4%BA%86%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">qiankun.umijs.org/zh/api#load…</a></p>
<h3 id="user-content-4" data-id="heading-5">常用 API</h3>
<p><strong>qiankun</strong> 的相关 API，官方文档已经有了详细说明，本文就不再一一说明。下面列出了 <strong>qiankun</strong> 所有 <strong>API</strong> 的官网链接，大家可以移步<a href="https://qiankun.umijs.org/zh/api" target="_blank" rel="nofollow noopener noreferrer">官网</a>去查看。</p>
<ul>
<li><a href="https://qiankun.umijs.org/zh/api#registermicroappsapps-lifecycles" target="_blank" rel="nofollow noopener noreferrer">registerMicroApps</a></li>
<li><a href="https://qiankun.umijs.org/zh/api#startopts" target="_blank" rel="nofollow noopener noreferrer">start</a></li>
<li><a href="https://qiankun.umijs.org/zh/api#setdefaultmountappapplink" target="_blank" rel="nofollow noopener noreferrer">setDefaultMountApp</a></li>
<li><a href="https://qiankun.umijs.org/zh/api#runafterfirstmountedeffect" target="_blank" rel="nofollow noopener noreferrer">runAfterFirstMounted</a></li>
<li><a href="https://qiankun.umijs.org/zh/api#loadmicroappapp-configuration" target="_blank" rel="nofollow noopener noreferrer">loadMicroApp</a></li>
<li><a href="https://qiankun.umijs.org/zh/api#prefetchappsapps-importentryopts" target="_blank" rel="nofollow noopener noreferrer">prefetchApps</a></li>
<li><a href="https://qiankun.umijs.org/zh/api#initglobalstatestate" target="_blank" rel="nofollow noopener noreferrer">initGlobalState</a></li>
</ul>
<h3 id="user-content-5" data-id="heading-6">qiankun 是如何解决 single-spa 在使用过程中遇到的问题的</h3>
<h4 id="user-content-5-1" data-id="heading-7">子应用加载 - Html Entry vs Js Entry</h4>
<p>在使用 <strong>single-spa</strong> 时，最关键的步骤就是在<strong>创建路由注册表</strong>时，确定<strong>子应用的加载方法</strong> - <strong>loadAppFunc</strong>。</p>
<p>通常情况下，我们会将子应用的所有<strong>静态资源 - js、css、img等</strong>打包成一个 <strong>js bundle</strong>，然后在 <strong>loadAppFunc</strong> 中通过加载执行这个 <strong>js bundle</strong> 的方式，获取<strong>子应用</strong>提供的<strong>生命周期方法</strong>，然后执行子应用的 <strong>mount</strong> 方法来加载子应用。这种方式称为 <strong>Js Entry</strong>。</p>
<p><strong>Js Entry</strong> 方式使用起来会比较麻烦，具体表现为：</p>
<ul>
<li>
<p>首先，不同的子应用打包出来的 <strong>js bundle</strong> 的名称可能会不一样，而且子应用更新也会导致 <strong>js bundle</strong> 的名称随时会变化，这就使得我们在定义 <strong>loadAppFunc</strong> 时，必须能<strong>动态获取</strong>子应用 <strong>js bundle</strong> 名称(子应用 <strong>js bundle</strong> 名称得保存起来以便 <strong>loadAppFunc</strong> 来获取)。</p>
</li>
<li>
<p>其次，所有的静态资源打包到一起，<strong>css 提取</strong>、<strong>资源并行加载</strong>、<strong>首屏加载</strong>等优化也就没有了。</p>
</li>
<li>
<p>最后，为了使得子应用的<strong>按需加载</strong>功能生效，我们需要在子应用打包过程中，修改相应的配置以补全子应用 js 资源的路径。</p>
</li>
</ul>
<p><strong>qiankun</strong> 使用了一种新的子应用加载方式 - <strong>html entry</strong>，来帮助我们解决 <strong>js entry</strong> 方式的痛点。</p>
<p>使用 <strong>qiankun</strong> 时，创建<strong>路由注册表</strong>依旧是最关键的步骤。但不同的是，我们不再需要给子应用定义<strong>加载方法 - loadAppFunc</strong>，只需要确定子应用的<strong>入口 - entry</strong> 即可，<strong>子应用加载方法 - loadAppFunc</strong>， <strong>qiankun 会帮我们实现</strong>。</p>
<p><strong>qiankun</strong> 是基于<strong>原生 fetch</strong> 来实现 <strong>loadAppFunc</strong> 的。简单来说，就是<strong>加载子应用</strong>时，<strong>qiankun</strong> 会根据子应用 <strong>entry</strong> 配置项指定的 <strong>url</strong>，通过 <strong>fetch</strong> 方法来获取子应用对应的 <strong>html 内容字符串</strong>，然后<strong>解析 html 内容</strong>，收集子应用的<strong>样式</strong>、<strong>js 脚本</strong>，<strong>安装样式</strong>并执行 <strong>js 脚本</strong>来获取子应用的<strong>生命周期方法</strong>，然后执行子应用的 <strong>mount</strong> 方法。</p>
<p>整个详细过程，可以通过下面的流程图来了解：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/392e99d9980e47f19f578b2a12dcca1c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上述的过程，我们可以拿到子应用所有的 <strong>js 脚本</strong>和<strong>解析以后的 html 模板</strong>，然后把<strong>解析以后的 html 模板</strong>添加到 <strong>container</strong> 指定的节点上，然后<strong>手动触发所有 js 脚本的执行</strong>，这样就可以拿到子应用的<strong>生命周期方法 - mount</strong>，然后挂载子应用。</p>
<p>对比 <strong>Js Entry</strong>，<strong>Html Entry</strong> 的优点如下：</p>
<ul>
<li>
<p><strong>不需要将子应用打包成一个 js bundle</strong>，<strong>css 提取</strong>、<strong>资源并行加载</strong>、<strong>首屏加载优化</strong>可以照常使用(通过 fetch 获取外部样式表的内容是并行的)；</p>
</li>
<li>
<p><strong>不用关心子应用 js 文件的名称以及子应用更新以后导致 js 文件名发生变化</strong>；</p>
</li>
<li>
<p><strong>不用为按需加载功能特别修改打包配置</strong>(qiankun 在懒加载 js 脚本的时候会基于 entry 配置项自动补全 url)；</p>
</li>
</ul>
<p>结合上面 <strong>Html Entry</strong> 的工作流程图，我们再来梳理一下 <strong>qiankun</strong> 是如何工作的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd977e76749a41a0a3218681f5ffaa11~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，提一个问题。为什么 <strong>qiankun</strong> 要将<strong>外部样式表</strong>转化成<strong>内部样式表</strong>添加到 <strong>html 模板</strong>中并且要把 <strong>js 脚本</strong>收集起来<strong>手动执行</strong>呢？这样做有什么意义呢？</p>
<p>其实，之所以 <strong>qiankun</strong> 会这样做，是为了能通过<strong>技术手段</strong>来解决 <strong>js</strong>、<strong>css</strong> 隔离。接下来我们就在 <a href="https://juejin.cn/post/undefined">js 隔离</a>、<a href="https://juejin.cn/post/undefined">css 隔离</a> 章节中具体分析。</p>
<h4 id="user-content-5-2" data-id="heading-8">js 隔离</h4>
<p>使用<strong>微前端方案</strong>时，我们要确保<strong>应用之间全局变量</strong>不能互相影响。比如，子应用 A 给 window 对象定义了新的属性 - globalState，子应用 B 也给 window 对象定义了新的属性 globalState，那我们就需要确保子应用 A 和子应用 B 能获取到各自定义的 globalState。</p>
<p>在 <strong>single-spa</strong> 中，我们一般通过<strong>人为约定添加命名前缀</strong>的方式来进行 <strong>js 隔离</strong>，如子应用 A 给 window 对象定义了新的属性 - A_globalState，子应用 B 给 window 对象定义了新的属性 B_globalState。这种方式低效不说，还容易引发 bug。相比这个方式，<strong>qiankun</strong> 提供了更好的方式 - <strong>沙盒(sandbox)</strong>, 来帮助我们实现 <strong>js 隔离</strong>。</p>
<p><strong>沙盒（英语：sandbox，又译为沙箱)</strong>，计算机术语，是计算机安全领域中的一种安全机制，可以<strong>运行中的程序提供的隔离环境</strong>。通过<strong>沙盒</strong>，<strong>qiankun</strong> 为每个子应用，提供了<strong>隔离的运行环境</strong>，保证子应用的 js 代码在执行时使用的<strong>全局变量</strong>都是<strong>独属于当前子应用</strong>的。</p>
<p><strong>qiankun</strong> 实现 <strong>sandbox</strong> 的原理其实很好理解，简单来说就是：</p>
<ul>
<li>
<p>第一步，为每一个子应用创建一个<strong>唯一</strong>的<strong>类 window 对象</strong>；</p>
</li>
<li>
<p>第二步，<strong>手动执行</strong>子应用的 js 脚本，将<strong>类 window 对象</strong>作为<strong>全局变量</strong>，对全局变量的读写都作用在<strong>类 window 对象</strong>上；</p>
<p>在这一步，<strong>html entry</strong> 阶段解析出来的所有 <strong>js 脚本字符串</strong> 在执行时会先使用一个 <strong>IIFE - 立即执行函数</strong>包裹，然后通过 <strong>eval</strong> 方法手动触发，如下：</p>
<pre><code class="copyable">var fakeWindowA = &#123; name: 'appA'&#125;; // 子应用 appA 对应的类 window 对象
var fakeWindowB = &#123; name: 'appB'&#125;; // 子应用 appB 对应的类 window 对象
var jsStr = 'console.log(name)'; // 子应用 appA、appB 的都有的脚本字符串
var codeA = `(function(window)&#123;with(window)&#123;$&#123;jsStr&#125;&#125;&#125;)(fakeWindowA)`; 
var codeB = `(function(window)&#123;with(window)&#123;$&#123;jsStr&#125;&#125;&#125;)(fakeWindowB)`;
eval(codeA); // appA
eval(codeB); // appB
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>这样，通过上述的两个步骤，每个子应用的 js 代码在执行时使用的<strong>全局变量</strong>都是独属于当前子应用的，不会互相影响。</p>
<p>了解完 <strong>sandbox</strong> 的原理以后，我们具体来看一下 <strong>qiankun</strong> 是如何实现 <strong>sandbox</strong> 的。相关源代码如下：</p>
<pre><code class="copyable">class ProxySandbox &#123;
    ...
    name: string;  // 沙盒的名称
    proxy: WindowProxy; // 沙盒对应的 proxy 对象
    sandboxRunning: boolean; // 判断沙盒是否激活
    
    // 沙盒的激活方法，当子应用挂载时，要先通过 active 方法将沙盒激活
    active() &#123;
        ...
        this.sandboxRunning = true;
    &#125;
    
    // 沙盒的失活方法。当子应用卸载以后，要执行 inactive 方法将沙盒失活
    inactive() &#123;
        ...
        this.sandboxRunning = false;
    &#125;
    
    constructor(name) &#123;
        // 以子应用的名称作为沙盒的名称
        this.name = name;
        const self = this;
        // 获取原生的 window 对象
        const rawWindow = window;
        // 假的 window 对象
        const fakeWindow = &#123;&#125;;
        // 在这里，qiankun 之所以要使用 proxy，主要是想拦截 fakeWindow 的读写等操作
        // 比如，子应用中要使用 setTimeout 方法，fakeWindow 中并没有，就需要从 rawWindow 获取
        this.proxy = new Proxy(fakeWindow, &#123;
            set(target, key, value) &#123;
                if (self.sandboxRunning) &#123; // 沙盒已经激活
                    ...
                    // 子应用新增/修改的全局变量都保存到对应的fakeWindow
                    target[key] = value;
                &#125;
            &#125;,
            get(target, key) &#123;
                ...
                // 读取属性时，先从 fakeWindow 中获取，如果没有，就从 rawWindow 中获取
                return key in target ? target[key] : rawWindow[key];
            &#125;,
            ...
        &#125;);
        
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>qiankun</strong> 在实现 <strong>sandbox</strong> 时，先构建一个<strong>空对象 - fakeWindow</strong> 作为一个假的 <strong>window</strong> 对象，然后在 <strong>fakeWindow</strong> 的基础上通过原生的 <strong>Proxy</strong> 创建一个 <strong>proxy</strong> 对象，这个 <strong>proxy</strong> 最后会作为子应用 js 代码执行时的<strong>全局变量</strong>。有了这个 <strong>proxy</strong>，我们就可以很方便的<strong>劫持 js 代码中对全局变量的读写操作</strong>。当子应用中需要添加(修改)全局变量时，直接在 <strong>fakeWindow</strong> 中添加(修改)；当子应用需要从全局变量中读取某个属性(方法)时，先从 <strong>fakeWindow</strong> 中获取，如果 <strong>fakeWindow</strong> 中没有，再从<strong>原生 window</strong> 中获取。</p>
<p>当然，针对不支持 <strong>proxy</strong> 的浏览器，qiankun 也提供了相应的解决方案，具体实现如下：</p>
<pre><code class="copyable">class SnapshotSandbox &#123;
    ...
    name: string;  // 子应用的名称
    proxy: WindowProxy; // 沙盒对应的 proxy 对象
    sandboxRunning: boolean; // 判断沙盒是否激活
    private windowSnapshot!: Window; // window 对象的快照
    private modifyPropsMap: Record<any, any> = &#123;&#125;; // 收集修改的 window 属性
    
    constructor(name: string) &#123;
        this.name = name;
        this.proxy = window;
        this.type = SandBoxType.Snapshot; // 快照类型
     &#125;
     
     // 沙盒的激活方法
     active() &#123;
        // 记录当前快照
        this.windowSnapshot = &#123;&#125; as Window;
        // 遍历 window 对象的属性，把 window 对象可枚举的属性添加到 windowSnapshot 中
        iter(window, (prop) => &#123;
          this.windowSnapshot[prop] = window[prop];
        &#125;);

        // 恢复之前的变更
        Object.keys(this.modifyPropsMap).forEach((p: any) => &#123;
          window[p] = this.modifyPropsMap[p];
        &#125;);

        this.sandboxRunning = true;
     &#125;
     // 沙盒的失活方法
     inactive() &#123;
        this.modifyPropsMap = &#123;&#125;;

        iter(window, (prop) => &#123;
          if (window[prop] !== this.windowSnapshot[prop]) &#123;
            // 记录变更，恢复环境
            this.modifyPropsMap[prop] = window[prop];
            window[prop] = this.windowSnapshot[prop];
          &#125;
        &#125;);
        
        ...

        this.sandboxRunning = false;
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>SnapshotSandbox</strong> 称为<strong>快照沙盒</strong>。<strong>qiankun</strong> 在实现 <strong>SnapshotSandbox</strong> 时，也是先创建一个 <strong>fakeWindow</strong> 作为<strong>假的 window 对象</strong>，这个 <strong>fakeWindow</strong> 最后会作为子应用 js 代码执行时的<strong>全局变量</strong>。由于不支持 <strong>proxy</strong>(也不支持 <strong>setter/getter</strong>)，所以 <strong>qiankun</strong> 将原生 <strong>window</strong> 上的<strong>属性、方法</strong>全部拷贝了一份到 <strong>fakeWindow</strong>，以便子应用在读取全局变量时，可以在 <strong>fakeWindow</strong> 中全部获取到。</p>
<p>另外，除了 <strong>ProxySandbox</strong>、<strong>SnapshotSandbox</strong>，<strong>qiankun</strong> 还提供了另外一种 <strong>sandbox</strong> - <strong>SingularProxySandbox</strong>，<strong>单例沙盒</strong>。<strong>单例沙盒</strong>，是 <strong>qiankun</strong> 在启用<strong>单例模式(父应用只有一个子应用挂载)<strong>时，会自动创建。<strong>SingularProxySandbox</strong> 也是基于 <strong>proxy</strong> 实现的。但是和 <strong>ProxySandbox</strong> 不同，<strong>SingularProxySandbox</strong> 是在</strong>原生 window</strong> 对象上直接修改属性的，这会导致父子应用之间全局变量的互相影响。目前，不管是<strong>单子应用</strong>还是<strong>多子应用</strong>，<strong>qiankun</strong> 默认都使用 <strong>ProxySandbox</strong>。<strong>SingularProxySandbox</strong> 只有我们我们在 <strong>start</strong> 方法中显示配置 <strong>&#123; sandbox: &#123;loose: true &#125;&#125;</strong> 才会使用。</p>
<blockquote>
<p><strong>最新版本的 qiankun 中，SingularProxySandbox 会逐步废弃, 改为使用 ProxySandbox</strong>。</p>
</blockquote>
<p>综上，由于 <strong>qiankun</strong> 使用了 <strong>sandbox</strong>，各个子应用在工作工程中都会有各自<strong>独立的全局变量</strong>，不会修改<strong>原生的 window</strong> 对象，因此父子应用、多子应用之间都能保证全局变量互不影响。</p>
<p>最后，我们再来解释一下<strong>为什么 html entry 解析子应用 html 模板字符串时需要将所有的 js 脚本收集起来然后手动触发了</strong>。之所以这么做，是为了<strong>动态修改 js 脚本执行时的全局对象</strong>，保证每个子应用的 js 脚本执行时的全局对象都是各自独立的 <strong>fakeWindow</strong>，而不是<strong>原生的 window</strong>。</p>
<h4 id="user-content-5-3" data-id="heading-9">css 隔离</h4>
<p>和 <strong>js 隔离</strong>一样，<strong>qiankun</strong> 也通过<strong>技术手段</strong>实现了 <strong>css 隔离</strong>。</p>
<p>具体的方式有两种：<strong>严格样式隔离</strong>和 <strong>scoped 样式隔离</strong>。</p>
<ul>
<li>
<p><strong>严格样式隔离</strong></p>
<p>启动<strong>严格样式隔离</strong>，我们需要在使用 <strong>start</strong> 方法时添加 <strong>strictStyleIsolation</strong> 配置项，即：</p>
<pre><code class="copyable">import &#123; start &#125; from 'qiankun';

start(&#123;
    sandbox: &#123;
       strictStyleIsolation: true 
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>严格样式隔离，默认情况下是关闭的。如果需要开启，必须显示配置</strong>。</p>
</blockquote>
<p><strong>严格样式隔离</strong>，是基于 <strong>Web Component</strong> 的 <strong><a href="https://developer.mozilla.org/zh-CN/docs/Web/Web_Components/Using_shadow_DOM" target="_blank" rel="nofollow noopener noreferrer">shadow Dom</a></strong> 实现的。通过 <strong>shadow Dom</strong>, 我们可以将一个<strong>隐藏的、独立的 dom</strong> 附加到一个另一个 dom 元素上，保证<strong>元素的私有化</strong>，不用担心与文档的其他部分发生冲突。</p>
<p>具体的实现如下：</p>
<pre><code class="copyable">  ...
  if (appElement.attachShadow) &#123;
    shadow = appElement.attachShadow(&#123; mode: 'open' &#125;);
  &#125; else &#123;
    // createShadowRoot was proposed in initial spec, which has then been deprecated
    shadow = (appElement as any).createShadowRoot();
  &#125;
  shadow.innerHTML = innerHTML;
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，<strong>appElement</strong> 为子应用挂载的 dom 节点， <strong>innerHTML</strong> 为 <strong>Html Entry</strong> 解析生成的 <strong>html 模板字符串</strong>。 通过 <strong>shadow dom</strong>，可<strong>自动实现父子应用、多个子应用之间的样式隔离</strong>。</p>
</li>
<li>
<p><strong>scoped 样式隔离</strong></p>
<p><strong>qiankun</strong> 实现<strong>样式隔离</strong>的另一种方式为 <strong>scoped 样式隔离</strong>，具体的用法如下：</p>
<pre><code class="copyable">import &#123; start &#125; from 'qiankun';

start(&#123;
    sandbox: &#123;
       experimentalStyleIsolation: true 
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>scoped 样式隔离</strong>，是基于<strong>属性选择器实现</strong>的，具体如下：</p>
<pre><code class="copyable">div["data-qiankun=vue"] div &#123;
    background-color: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>html entry</strong> 解析以后的 <strong>html 模板字符串</strong>，在添加到 <strong>container</strong> 指定的节点之前，会先包裹一层 <strong>div</strong>，并且为这个 <strong>div</strong> 节点添加 <strong>data-qian</strong> 属性，属性值为子应用的 <strong>name</strong> 属性；然后遍历 <strong>html 模板字符串</strong>中所有的 <strong>style</strong> 节点，依次为<strong>内部样式表</strong>中的样式添加 <strong>div["data-qiankun=xxx"] 前缀</strong>。<strong>qiankun</strong> 中子应用的 <strong>name</strong> 属性值是唯一的，这样通过<strong>属性选择器</strong>的限制，就可实现<strong>样式隔离</strong>。</p>
<p>到这里，我们就可以解释<strong>为什么 html entry 解析子应用 html 模板字符串时需要将外部样式表转化为内部样式表</strong>了。如果不转化，我们是无法为<strong>外部样式表</strong>中的样式添加<strong>属性选择器前缀</strong>的，也就无法实现<strong>样式隔离</strong>了。</p>
<blockquote>
<p><strong>严格样式隔离，即使是外部样式表，也可以实现样式隔离，因此不需要将外部样式表转化为内部样式表。另外，严格样式隔离和 scoped 样式隔离不能同时使用，当两者对应的配置项都为 true 时，严格样式隔离的优先级更高</strong>。</p>
</blockquote>
</li>
</ul>
<p>在实际的项目中，我们常常会遇到<strong>动态添加 style</strong> 的情形，比如<strong>没有进行 css 提取</strong>、<strong>react 应用使用 styled-components</strong> 等。通常，这些动态添加的 <strong>style</strong> 会通过 <strong>document.head.appendChild</strong> 的方式添加到 <strong>head</strong> 节点中。此时，如果 <strong>qiankun</strong> 启用<strong>严格样式隔离</strong>或者 <strong>scoped 样式隔离</strong>，那 <strong>css 隔离</strong>是不是会失效呢？</p>
<p>答案是不会的。</p>
<p><strong>qiankun</strong> 针对<strong>动态添加 style</strong> 的情形，也做了相应的处理。为了能获知<strong>子应用动态添加 style 的操作</strong>，<strong>qiankun</strong> 对 <strong>document.head.appendChild</strong> 方法进行了<strong>劫持操作</strong>，具体如下：</p>
<pre><code class="copyable">// 原生的 appendChild 方法
const rawHeadAppendChild = document.head.appendChild;
// 重写原生方法
document.head.appendChild = function(newChild) &#123;
    if (newChild.tagName === 'STYLE') &#123;
        // 对 style 节点做处理
        ...
    
    &#125;
    ...
    // 找到子应用对应的 html 片段的根 dom 节点
    const mountDOM = ....;
    // 通过原生的 appendChild 将动态 style 添加到子应用对应的 html 片段中
    rawHeadAppendChild.call(mountDOM, newChild);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当子应用调用 <strong>document.head.appendChild</strong> 动态添加 <strong>style</strong> 时，会被 <strong>qiankun</strong> 劫持，然后将 <strong>style</strong> 添加到<strong>子应用对应的 html 片段</strong>中。此时如果 <strong>qiankun</strong> 配置了<strong>严格样式隔离</strong>，新增的 <strong>style</strong> 是添加到 <strong>shadow dom</strong> 中的，<strong>css 隔离</strong>自然生效；如果 <strong>qiankun</strong> 配置了 <strong>scoped 样式隔离</strong>，在将 style 添加到子应用对应的 html 片段之前，会先获取到<strong>样式内容</strong>，然后为<strong>样式内容</strong>添加 <strong>div["data-qiankun=xxx"] 前缀</strong>，<strong>css 隔离</strong>也生效。</p>
<h4 id="user-content-5-4" data-id="heading-10">子应用卸载副作用清理</h4>
<p>每个子应用在工作过程中，或多或少都会产生一些<strong>副作用</strong>，如 <strong>setInterval 生成的定时器</strong>、<strong>widnow.addEventListener 注册的事件</strong>、<strong>修改全局变量 window</strong>、<strong>动态添加 dom 节点</strong>等。如果在子应用卸载的时候，不对这些副作用进行处理，那么将会造成<strong>内存泄漏</strong>，甚至会<strong>对下一个子应用造成影响</strong>。<strong>副作用</strong>的处理相当重要，然而在实际的项目中，如果靠我们开发人员自行处理，不仅费时费力，还不能面面俱到。</p>
<p>幸运的是 <strong>qiankun</strong> 可以帮我们在子应用卸载时及时处理<strong>副作用</strong>。</p>
<p>首先是<strong>修改全局变量</strong>引发的副作用。由于 <strong>qiankun</strong> 使用了 <strong>sandbox</strong> 机制，每个子应用工作过程中都有<strong>各自独立的全局变量</strong>，不会修改 <strong>window</strong>，因此<strong>不会出现修改全局变量 window 的副作用</strong>，也就不用处理了，😊。</p>
<p>其次是<strong>动态添加 dom 节点</strong>引发的副作用。由于 <strong>qiankun</strong> 劫持了 <strong>document.head.appendChild</strong>、<strong>document.body.appendChild</strong>、 <strong>document.head.insertBefore</strong>, <strong>动态添加的 dom 节点</strong>都是自动添加到子应用对应的 <strong>html</strong> 片段中。当子应用<strong>卸载</strong>时，子应用对应的 <strong>html</strong> 片段会自动移除，<strong>动态添加的 dom 节点</strong>自然也就一起移除了，😊。</p>
<p>关于 <strong>setInterval</strong> 引发的副作用，<strong>qiankun</strong> 是通过<strong>劫持</strong>原生的 <strong>setInterval</strong> 方法来解决的，具体代码如下：</p>
<pre><code class="copyable">const rawWindowInterval = window.setInterval;
const rawWindowClearInterval = window.clearInterval;

function patch(global: Window) &#123;
  // 收集子应用定义的定时器
  let intervals: number[] = [];
  // 重写原生的 clearInterval
  global.clearInterval = (intervalId: number) => &#123;
    intervals = intervals.filter((id) => id !== intervalId);
    return rawWindowClearInterval(intervalId);
  &#125;;
  // 重写原生的 setInterval
  global.setInterval = (handler: Function, timeout?: number, ...args: any[]) => &#123;
    const intervalId = rawWindowInterval(handler, timeout, ...args);
    intervals = [...intervals, intervalId];
    return intervalId;
  &#125;;
  // free 函数在子应用卸载时调用
  return function free() &#123;
    intervals.forEach((id) => global.clearInterval(id));
    global.setInterval = rawWindowInterval;
    global.clearInterval = rawWindowClearInterval;

    return noop;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过劫持 <strong>setInterval</strong>，子应用生成的定时器都会被收集，当子应用卸载时，收集的定时器会自动被 <strong>qiankun</strong> 清除掉。</p>
<p>和 <strong>setInterval</strong> 一样， <strong>window.addEventListener</strong> 引发的<strong>副作用</strong>，<strong>qiankun</strong> 也是通过<strong>劫持</strong>原生的 <strong>window.addEventListener</strong>、<strong>window.removeEventListener</strong> 来处理的。子应用在工作过程中绑定的<strong>事件</strong>都会被<strong>收集</strong>，当子应用<strong>卸载</strong>时，收集的事件会自动被 <strong>qiankun</strong> 解绑。</p>
<h4 id="user-content-5-5" data-id="heading-11">子应用重新挂载状态恢复</h4>
<p>在实际的<strong>微前端项目</strong>中，我们除了要<strong>在子应用卸载时清除副作用</strong>，还需要<strong>在子应用重新挂载时恢复子应用的状态</strong>。</p>
<p>子应用<strong>重新加载</strong>时，需要恢复的状态包括：</p>
<ul>
<li><strong>子应用修改的全局变量</strong>；</li>
<li><strong>子应用动态添加的 style</strong>；</li>
</ul>
<p>有些时候，我们需要在<strong>子应用重新加载时恢复上一次子应用对全局变量的修改</strong>。关于这一点，<strong>qiankun</strong> 的 <strong>sandbox</strong> 可以帮完美实现这一点。每个<strong>子应用</strong>都有一个独属于自己的 <strong>fakeWindow</strong>，这个 <strong>fakeWindow</strong> 会一直伴随子应用存在(子应用卸载时也存在)。<strong>子应用</strong>所有对<strong>全局变量</strong>的修改，实际上都发生在 <strong>fakeWindow</strong> 上，当子应用<strong>重新挂载</strong>时，<strong>全局变量自动恢复</strong>。</p>
<p>在解释<strong>恢复动态添加 style</strong> 这一点时，我们先通过一个使用 <strong>webpack</strong> 打包的<strong>子应用</strong>为例来解释一下<strong>为什么子应用重新挂载时需要恢复之前动态添加的 style</strong>。</p>
<p><strong>webpack</strong> 打包子应用时，会将每一个<strong>子应用</strong>中的<strong>组件</strong>转化为一个<strong>可执行函数</strong>，这个<strong>可执行函数</strong>会返回<strong>组件</strong>对外的 <strong>export</strong>。子应用<strong>第一次启动执行 js 脚本</strong>时，会先执行组件的<strong>可执行函数</strong>，得到组件的 <strong>export</strong> 并缓存起来。这个<strong>收集组件 export 的缓存</strong>会伴随着子应用一直存在。当子应用<strong>重新挂载</strong>时，可以直接从<strong>缓存</strong>中获取组件的 <strong>export</strong> 而<strong>不用再执行组件的可执行函数</strong>。</p>
<p>另外，<strong>webpack</strong> 打包子应用时，如果未使用 <strong>MiniCssExtractPlugin</strong> 提取 <strong>css</strong>，那么项目中所有的 <strong>css</strong> 会经过 <strong>css-loader</strong>、<strong>style-loader</strong> 处理以后也会转化为一个<strong>可执行方法</strong>，执行这个方法会将<strong>动态创建一个 style</strong>，并通过 <strong>document.head.appendChild</strong> 的方式添加到页面中。这个 <strong>css 可执行方法</strong>，只有在<strong>组件可执行方法</strong>执行时才会执行，这就意味着<strong>子应用重新挂载时 css 可执行方法不会触发，样式也就不会动态添加</strong>。</p>
<p>综上，所以我们需要<strong>在子应用重新挂载时恢复之前动态添加的 style</strong>。</p>
<p>关于这一点， <strong>qiankun</strong> 是这样做的：</p>
<ul>
<li>第一，<strong>qiankun</strong> 会劫持 <strong>document.head.appendChild</strong> 方法。当<strong>子应用第一次挂载</strong>时，遇到<strong>动态添加 style</strong> 的操作，会被<strong>劫持</strong>，<strong>新增的 style 会被缓存起来</strong>。这个<strong>缓存</strong>会一直伴随子应用存在。</li>
<li>第二，<strong>子应用重新挂载</strong>，将之前<strong>缓存的 style</strong> 添加到子应用对应的 <strong>html</strong> 片段中。</li>
</ul>
<h4 id="user-content-5-6" data-id="heading-12">子应用通信</h4>
<p>在<strong>父子应用、多个子应用相互通信方面</strong>，<strong>qiankun</strong> 也提供了一套完整的方案，不需要开发人员自己实现。</p>
<p>使用方式如下：</p>
<pre><code class="copyable">// 主应用

import &#123; initGlobalState, MicroAppStateActions &#125; from 'qiankun';

// 初始化 state
const actions: MicroAppStateActions = initGlobalState(state);

actions.onGlobalStateChange((state, prev) => &#123;
  // state: 变更后的状态; prev 变更前的状态
  console.log(state, prev);
&#125;);
actions.setGlobalState(state);
actions.offGlobalStateChange();


// 子应用
export function mount(props) &#123;
  props.onGlobalStateChange((state, prev) => &#123;
    // state: 变更后的状态; prev 变更前的状态
    console.log(state, prev);
  &#125;);

  props.setGlobalState(state);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>qiankun</strong> 提供的 <strong>通信机制</strong> 是基于<strong>发布订阅模式</strong>实现的，非常好理解。<strong>主应用</strong>通过 <strong>initGlobalState</strong> 方法创建一个全局的 <strong>globalState</strong>，并维护一个 <strong>deps</strong> 列表来<strong>收集订阅</strong>。 <strong>订阅方法 onGlobalStateChange</strong> 和<strong>修改 globalState 的 setGlobalState 方法</strong>，会在<strong>子应用的生命周期方法</strong>执行时传递给子应用。<strong>子应用</strong>首先通过 <strong>onGlobalStateChange</strong> 方法绑定 <strong>callback</strong>，该 <strong>callback</strong> 会添加到 <strong>golbalState</strong> 的 <strong>deps</strong> 列表中。当我们通过 <strong>setGlobalState</strong> 方法修改 <strong>globalState</strong> 时，<strong>qiankun</strong> 会遍历 <strong>deps</strong> 列表，依次触发收集的 <strong>callback</strong>。</p>
<p>子应用<strong>卸载</strong>时，绑定的 <strong>callback</strong> 会被<strong>卸载</strong>，从 <strong>deps</strong> 列表中<strong>移除</strong>。</p>
<h4 id="user-content-5-7" data-id="heading-13">子应用预加载</h4>
<p><strong>qiankun</strong> 在<strong>资源预加载</strong>方面也给我们提供一套完整的方案，具体的用法如下：</p>
<pre><code class="copyable">import &#123; start &#125; from 'qiankun';

...

start(&#123;
    prefetch: true // prefetch: boolean | 'all' | string[] | function
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>prefetch</strong> 根据配置项的不同，提供了不同的<strong>资源预加载策略</strong>：</p>
<ul>
<li><strong>boolean</strong>：<strong>是否开启资源预加载</strong>。如果配置为 <strong>true</strong>， <strong>qiankun</strong> 会在<strong>第一个子应用挂载完成</strong>以后，开始加载其他子应用的静态资源；</li>
<li><strong>'all'</strong>: <strong>qiankun</strong> 执行 <strong>start</strong> 方法以后立即开始预加载<strong>所有子应用的静态资源</strong>，一般不推荐使用；</li>
<li><strong>string[]</strong>: <strong>qiankun</strong> 会在<strong>第一个子应用挂载完成</strong>以后，预加载<strong>指定的子应用</strong>；</li>
<li><strong>function</strong>: <strong>用户完全自定义子应用资源的加载时机</strong>；</li>
</ul>
<h3 id="user-content-6" data-id="heading-14">qiankun 的整个工作过程</h3>
<p>在了解了 <strong>qiankun</strong> 的用法以及 <strong>qiankun</strong> 在 <strong>single-spa</strong> 基础上做出的相关优化以后，我们来对 <strong>qiankun</strong> 的整个工作过程做一个<strong>全面梳理</strong>，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6278fba7c1354278aa82b3dd1767cdc5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 id="user-content-8" data-id="heading-15">结束语</h3>
<p>到这里，<strong>qiankun</strong> 的学习就结束了。本文主要对 <strong>qiankun 的用法</strong>、<strong>整个工作流程</strong>以及<strong>对 single-spa 的改进</strong>做了详细介绍。如果你还没有使用过 qiankun 或者对 qiankun 是什么还没有一个了解，那么阅读此文可能对你用处不大，可以移步<a href="https://qiankun.umijs.org/zh" target="_blank" rel="nofollow noopener noreferrer">官网</a>先做一个简单了解。本文的篇幅较长，阅读起来比较花时间，希望能给到大家帮助，如果有疑问或者错误，欢迎大家提出。共同学习，一起进步，😁。</p>
<p>参考资料如下：</p>
<ul>
<li><a href="https://qiankun.umijs.org/zh/guide" target="_blank" rel="nofollow noopener noreferrer">qiankun</a></li>
<li><a href="https://mp.weixin.qq.com/s/RnwUEWrjIO8j3Y6kkSOpJw" target="_blank" rel="nofollow noopener noreferrer">探索微前端的场景极限</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/78362028" target="_blank" rel="nofollow noopener noreferrer">可能是你见过最完善的微前端解决方案</a></li>
<li><a href="https://juejin.cn/post/6885211340999229454" target="_blank">微前端框架 之 qiankun 从入门到源码分析</a></li>
</ul></div>  
</div>
            