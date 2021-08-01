
---
title: '前端工程化之 Webpack5 Module-Federation 入门手册'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ed74c3ccafc4252aaa7a14771657849~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 05:57:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ed74c3ccafc4252aaa7a14771657849~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>现代 WEB 开发中,越来越多的 IT 技术厂使用<code>微前端</code>。所谓微前端,简单点就是多个单独构建子应用可以形成一个统一的应用程序。 这些单独的构建之间不存在依赖关系，因此可以单独开发和部署它们。</p>
<h2 data-id="heading-0">微前端简介</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ed74c3ccafc4252aaa7a14771657849~tplv-k3u1fbpfcp-zoom-1.image" alt="download" loading="lazy" referrerpolicy="no-referrer"></p>
<p>微前端现有的落地方案可以分为三类:</p>
<ul>
<li>自组织模式</li>
<li>基座模式</li>
<li>模块加载模式</li>
</ul>
<p>与基座模式相比，模块加载模式没有中心容器，这就意味着，我们可以将任意一个微应用当作项目入口，整个项目的微应用与微应用之间相互串联，打破项目的固定加载模式，彻底释放项目的灵活机动性，这样的模式，也被称为<code>去中心化模式</code>。</p>
<p>其实这个方案在微前端的架构理念中早已提及，但直到 2020 年 10 月 Webpack 5 正式发布之后才被真正落地应用。</p>
<p>因为 Webpack 5 带来了一个全新特性：<code>Module Federation</code>(模块联邦)，这是我们使用模块加载模式实现微前端架构的核心特性。</p>
<p>今天，我们来看看 <code>Module Federation</code> 的基本使用，然后再通过解读源码的方式，带你深入了解 Webpack 5 实现微前端的工作原理，以及实战中常见的应用场景，详细介绍如何使用模块联邦落地微前端架构。</p>
<h2 data-id="heading-1">Module Federation 是什么</h2>
<p>在官方文档中，关于 <code>Module Federation</code> 的动机中，有这样一段介绍:</p>
<blockquote>
<p>多个独立的构建可以组成一个应用程序，这些独立的构建之间不应该存在依赖关系，因此可以单独开发和部署它们。</p>
</blockquote>
<blockquote>
<p>这通常被称作微前端，但并不仅限于此。</p>
</blockquote>
<p>注：如果你感兴趣，可以点击这里查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fconcepts%2Fmodule-federation%2F%23motivation" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/concepts/module-federation/#motivation" ref="nofollow noopener noreferrer">英文原文</a>，以获取更多信息。</p>
<p><code>Module Federation</code> 中文直译为“模块联邦”，为了方便我们这里简称为 <code>MF</code>。如果你去 Webpack 官方文档中查看，最多可以从前面的“动机”中看到模糊的解释，而对于“模块联邦”准确的定义，其实并没有给出。</p>
<p>但是，根据 “动机”的描述，不难看出，<code>MF</code> 实际想要做的事，便是把多个无相互依赖、单独部署的应用合并为一个。</p>
<p>通俗点讲，<code>MF</code> 提供了能在当前应用中加载其他应用的能力。</p>
<p>所以，在 <code>MF</code> 中，如果一个模块想要载入其他模块:</p>
<ul>
<li>就需要一个<strong>引入</strong>的动作；</li>
<li>同样如果想让其他模块使用，就需要一个<strong>导出</strong>的动作。</li>
</ul>
<p>对此，可以引出下面两个概念</p>
<ul>
<li>
<p><code>expose</code>：导出应用，被其他应用导入</p>
</li>
<li>
<p><code>remote</code>：引入其他应用</p>
</li>
</ul>
<p>一个模块既可以导出给其他模块使用，又可以导入一个其他模块，这与“基座模式”完全不同。</p>
<p>要知道，无论是 <code>single-spa</code> 还是 <code>qiankun</code>，加载不同模块，都需要有一个容器中心来承载；而在 <code>MF</code> 中，没有且也不需要容器中心。</p>
<p>总之</p>
<p>鉴于 <code>MF</code> 的能力，我们完全可以实现一个去中心化的应用部署群：</p>
<p><strong>多个微应用单独部署在各自的服务器中，而每个微应用都可以引用其他应用，也能被其他应用导入使用，即每个应用都可以导出又导入，也就没有了容器中心的概念</strong>。</p>
<h2 data-id="heading-2">Module Federation 如何使用</h2>
<p>下面我们再来说说具体的操作方法。</p>
<p>在本讲开篇我们说过，<code>Module Federation</code> 是 Webpack 5 中新增的特性，所以，我们需要安装对应版本的 Webpack 及所需的工具。</p>
<p>因为是多个应用之间互相导入导出，因此，我们这里需要创建至少两个应用，来展示相关配置操作，然后分别在两个应用下安装相关工具，这里我以 <code>remoteApp</code>(用来引入子模块的父应用)  和 <code>exposeApp</code>(用来导出模块的子应用)  两个应用为例进行展示。</p>
<h3 data-id="heading-3"><code>exposeApp</code>(用来导出模块的子应用)项目基础配置</h3>
<p>基础配置内容如下</p>
<p>使用 <code>MF</code>，需要在配置文件中引入 <code>ModuleFederationPlugin</code>，从名字就可以看出这是一个插件。因为是内置插件，所以也不需要单独安装，直接通过 <code>require</code> 关键字引入即可，这和一个普通插件的引入方式并没有区别。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> Mfp = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>).container.ModuleFederationPlugin;

<span class="hljs-keyword">const</span> deps = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../package.json"</span>).dependencies;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">//  mode 工作模式</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
  <span class="hljs-comment">//  服务器</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-number">4000</span>,
  &#125;,
  <span class="hljs-comment">//  插件</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> Mfp(&#123;
      <span class="hljs-comment">// 当前微应⽤名称</span>
      <span class="hljs-attr">name</span>: <span class="hljs-string">"studentProject"</span>,
      <span class="hljs-comment">// 对外提供的打包后的⽂件名（引⼊时使⽤）</span>
      <span class="hljs-attr">filename</span>: <span class="hljs-string">"student.js"</span>,
      <span class="hljs-comment">// 暴露的应用内具体模块</span>
      <span class="hljs-attr">exposes</span>: &#123;
        <span class="hljs-comment">// 格式   名称:代码路径</span>
        <span class="hljs-string">"./studentModule"</span>: path.join(__dirname, <span class="hljs-string">"../src/App"</span>),
      &#125;,
      <span class="hljs-comment">// 共享依赖</span>
      <span class="hljs-attr">shared</span>: &#123;
        ...deps,
        <span class="hljs-attr">antd</span>: &#123; <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span> &#125;,
        <span class="hljs-attr">react</span>: &#123;
          <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-string">"react-dom"</span>: &#123;
          <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span>,
        &#125;,
      &#125;,
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为导出应用中的模块是具体可选的，因此需要将导出的模块进行单独文件的打包。</p>
<p>参数</p>
<ul>
<li><code>filename</code> 就是指定具体导出的模块文件名；</li>
<li><code>name</code> 参数则代表当前导出的应用名称；</li>
<li><code>exposes</code> 参数是一个对象，在这里具体指定哪个模块需要导出，对象中的属性表示具体导出模块的名字，值则是指定具体导出模块的路径及文件名。</li>
</ul>
<p>总体来说，我们导出的是一个微应用，而组成微应用的，便是当前应用下的某些模块，可以是一个，也可以指定多个。</p>
<p>其他详细配置可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fnsuedu%2Fmodule-federation-examples%2Fblob%2Fmaster%2FApp1%2Fconfig%2Fwebpack.common.js" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/nsuedu/module-federation-examples/blob/master/App1/config/webpack.common.js" ref="nofollow noopener noreferrer">module-federation-examples 源码</a></p>
<p>需要注意的是，为了防止开发服务器的端口冲突，我这里将两个应用端口分别设置了 <code>4000</code> 及 <code>4001</code> 。</p>
<h3 data-id="heading-4"><code>remoteApp</code>(用来引入子模块的父应用)项目基础配置</h3>
<h4 data-id="heading-5">WebPack 配置</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> Mfp = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>).container.ModuleFederationPlugin;

<span class="hljs-keyword">const</span> deps = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../package.json"</span>).dependencies;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> Mfp(&#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"userProject"</span>,
      <span class="hljs-comment">// 导⼊远程子应用模块</span>
      <span class="hljs-attr">remotes</span>: &#123;
        <span class="hljs-comment">// 导⼊后给模块起个别名：“微应⽤名称@地址/导出的⽂件名”</span>
        <span class="hljs-attr">remoteStudentProject</span>: <span class="hljs-string">"student@http://localhost:4000/student.js"</span>,
      &#125;,
      <span class="hljs-comment">// 共享依赖</span>
      <span class="hljs-attr">shared</span>: &#123;
        ...deps,
        <span class="hljs-attr">antd</span>: &#123; <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span> &#125;,
        <span class="hljs-attr">react</span>: &#123;
          <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-string">"react-dom"</span>: &#123;
          <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span>,
        &#125;,
      &#125;,
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果只作为导入其他应用的微前端配置，其实非常简单，只需要在 <code>remotes</code> 中具体配置要导入的应用即可，具体的导入规则是:</p>
<pre><code class="copyable">导入应用别名:' 微应⽤名称@应用远程地址/导出的⽂件名 '
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">业务代码配置</h4>
<p>导入的相关配置完成后，接下来如何在应用中使用导入的内容呢？我们在 <code>src/index.js</code> 中引入使用，具体代码如下：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> &#123; BrowserRouter <span class="hljs-keyword">as</span> Router, Switch, Route, Link &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;

<span class="hljs-comment">// 该组件是动态加载的</span>
<span class="hljs-keyword">const</span> Home = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"@/pages/Home"</span>));
<span class="hljs-keyword">const</span> About = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"@/pages/About"</span>));

<span class="hljs-comment">// MF导入</span>
<span class="hljs-comment">// import("子应用别名/子应用路径"))</span>
<span class="hljs-keyword">const</span> ChildApp = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"remoteStudentProject/studentModule"</span>));

<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"@/redux/store"</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">"./index.less"</span>;

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Router</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">'/'</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">'/about'</span>></span>About<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">'/ChildApp'</span>></span>ChildApp<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">hr</span> /></span>

      <span class="hljs-tag"><<span class="hljs-name">React.Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">div</span>></span>loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125;>
        <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">Home</span> /></span>
          <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/about'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">About</span> /></span>
          <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
          &#123;/*远程子应用 */&#125;
          <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">'/ChildApp'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ChildApp</span> /></span>
          <span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">React.Suspense</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Router</span>></span></span>
);

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码你能够发现，引入微应用返回的是一个 <code>Promise</code>，最终会返回一个 "模块对象" 的结果，</p>
<p>我们前面说过，<code>MF</code> 是去中心化的，一个微应用，既可以导出也可以导入，如果你想将 <code>remoteApp</code> 作为一个微应用导出，那么，你可以在配置中继续添加导出的配置选项，比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> Mfp = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>).container.ModuleFederationPlugin;

<span class="hljs-keyword">const</span> deps = <span class="hljs-built_in">require</span>(<span class="hljs-string">"../package.json"</span>).dependencies;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> Mfp(&#123;
      <span class="hljs-comment">// 名称</span>
      <span class="hljs-attr">name</span>: <span class="hljs-string">"userProject"</span>,
      <span class="hljs-comment">// 导⼊远程子应用模块</span>
      <span class="hljs-attr">remotes</span>: &#123;
        <span class="hljs-comment">// 导⼊后给模块起个别名：“微应⽤名称@地址/导出的⽂件名”</span>
        <span class="hljs-attr">remoteStudentProject</span>: <span class="hljs-string">"student@http://localhost:4000/student.js"</span>,
      &#125;,
      <span class="hljs-comment">// 作为子应用还可以再次导出，同样可以被其他项目引用</span>
      <span class="hljs-attr">exposes</span>: &#123;
        <span class="hljs-string">"./userAbout"</span>: path.join(__dirname, <span class="hljs-string">"../src/About"</span>),
      &#125;,
      <span class="hljs-comment">// 共享依赖</span>
      <span class="hljs-attr">shared</span>: &#123;
        ...deps,
        <span class="hljs-attr">antd</span>: &#123; <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span> &#125;,
        <span class="hljs-attr">react</span>: &#123;
          <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-string">"react-dom"</span>: &#123;
          <span class="hljs-attr">singleton</span>: <span class="hljs-literal">true</span>,
        &#125;,
      &#125;,
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，不管是导入还是导出，绝大多数插件模块都需要实例化对象，我们这里的 <code>ModuleFederationPlugin</code> 也不例外，使用它，就是将这个实例对象，放入 <code>plugins</code> 数组中，实例化时，在传入的对象中，设置不同的属性参数。</p>
<p>为了方便你记忆，我把前面用到的不同参数的含义整理在下面这张表格中：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e73c129a45f04e2d995a90bd047d5cce~tplv-k3u1fbpfcp-zoom-1.image" alt="MF-desc" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中，</p>
<ul>
<li><code>remotes</code> 代表导入远程模块，</li>
<li><code>exposes</code> 表示导出了当前模块，这样就完成了模块的导入和导出</li>
</ul>
<p>这就是前面介绍的去中心化的体现——一个模块既可以导出又可以导入，不需要通过中心基座在各个微应用之间连接，任何一个微应用都可以当作一个中心，也都可以被其他模块导入。</p>
<p>通过以上简单的应用，我们对 <code>MF</code> 有了一个初步的认识，而上面的配置在 Webpack 打包时会执行怎样的操作呢？</p>
<p>打包后的结果代码，是如何加载远程模块的？自己的模块又是如何导出提供给其他应用导入的呢？这就需要我们阅读打包之后的代码去一探究竟了。</p>
<h2 data-id="heading-7">Module Federation 的构建解析</h2>
<p>我们分别在 <code>exposeApp</code>(用来导出模块的子应用) 和 <code>remoteApp</code>(用来引入子模块的父应用) 中， 找到打包后的 <code>dist</code> 目录。</p>
<h3 data-id="heading-8">应用导出分析</h3>
<p>其中 <code>exposeApp</code>打包后的 <code>student.js</code> 文件，具体如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2adb6e4e9e0d4db7abc8d1a7966e0027~tplv-k3u1fbpfcp-zoom-1.image" alt="webpack-bundle-remotes" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>moduleMap</code>：通过 <code>exposes</code> 生成的模块集合。</li>
</ul>
<h3 data-id="heading-9">应用导入分析</h3>
<p>而最关键的则是导入部分，在 <code>remoteApp</code> 中，我们找到打包后的 <code>bundle.js</code> 文件，其中具体代码如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa10ffaced334ce7bdd206ae94900441~tplv-k3u1fbpfcp-zoom-1.image" alt="webpack-bundle-daoru-1" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们能到 <code>Promise</code> 方式的代码加载</p>
<p>其实 <code>Promise</code> 的作用就是加载了指定 <code>URL</code> 路径的 <code>em.js</code>，这就是我们导出的模块文件名。</p>
<ul>
<li>其中<code>__webpack_require__.l</code>函数作用就是读取 <code>URL</code> 路径，然后动态生成<code>script</code>标签并插入到代码中</li>
</ul>
<p>现在已经可以读取到远程模块的内容了,那<code>如何加载指定的模块代码呢？</code></p>
<p>继续往下看，我们能够看到 <code>webpack_require.f.remotes</code> 的处理：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7d996f3c56043398238b880df5e38ad~tplv-k3u1fbpfcp-zoom-1.image" alt="webpack-bundle-daoru-2" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>首先，<code>MF</code> 会让 Webpack 以 <code>filename</code> 作为文件名生成文件，并将具体代码打包到 <code>xxx,bundle.js</code> 文件中。</p>
</li>
<li>
<p>其次，文件中以 <code>var</code> 的形式暴露了一个名为 <code>name</code> 的全局变量，其中包含 <code>exposes</code> 中配置的内容。</p>
</li>
<li>
<p>最后，先通过 <code>remote</code> 的 <code>init</code> 方法将自身写入 <code>remote</code> 中，再通过 <code>get</code> 获取 <code>remote</code> 中 <code>expose</code> 的组件；</p>
</li>
<li>
<p>而作为 <code>remote</code> 时，先判断是否有可用的共享依赖。若有，则加载这部分依赖；如果没有，则加载自身依赖。</p>
</li>
</ol>
<h2 data-id="heading-10">Module Federation 的应用场景</h2>
<p>英雄也怕无用武之地，让我们看看 <code>MF</code> 的应用场景有哪些。</p>
<p>最明显的就是微前端的应用，通过 <code>remote</code> 和 <code>expose</code> 可以将一个应用作为微应用导入导出，微应用之间相互独立，也可以互相导入导出，没有中心基座的限制。而由 <code>YY 业务中台 Web 前端组团队</code>自主研发的 <code>EMP 微前端方案</code>就是基于 <code>MF</code> 的能力而实现的。</p>
<p>再就是资源复用，以减少编译体积，可以将多个应用的通用组件进行单独部署，通过 <code>MF</code> 的功能在运行时引入到其他项目中，这样组件代码就不会编译到项目中，同时也能满足多个项目同时使用的需求，一举两得。</p>
<h2 data-id="heading-11">总结</h2>
<p>我们通过对 <code>Module Federation</code> 特性的解读，简单了解了 Webpack 通过插件的方式导入导出一个模块，实现一个微前端架构应用。</p>
<p>从一定程度上来说，<code>Module Federation</code> 是目前去中心化模式唯一落地的技术，通过简单的配置就能够很轻松地完成一个微前端架构的基本模型。而去中心化的方案，让我们脱离了固定的中心基座，极大地增加了项目的灵活性。</p>
<p>但是，如果换一个角度想，没有了统一管理的基座中心，每一个微应用的管理维护就显得极其重要了，这也对我们开发者团队提出了挑战。此外，随着项目数量和规模越来越大，一个项目下的微应用必然增加，如果管理不到位，极有可能带来致命的混乱。</p>
<p>最后，也请你思考一下，你现在的项目是否适合做去中心化的微前端架构的升级呢？欢迎在评论区留言交流哦。</p>
<h2 data-id="heading-12">思考</h2>
<ol>
<li>webpack 设置了 <code>publicPath:"auto"</code>会有什么效果</li>
<li>当子项目单独抽离 CSS 时，在主项目中引用，可能会找不到 CSS 文件吗?如何解决</li>
<li><code>Module Federation</code> 的导入导出与 ES6 的导入导出有什么区别</li>
<li>如何搭建 <code>Module Federation</code> 并用于远程部署环境</li>
</ol>
<h2 data-id="heading-13">最后</h2>
<p>文章浅陋,欢迎各位看官评论区留下的你的见解！</p>
<p>觉得有收获的同学欢迎点赞，关注一波!</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cb960eef74641da98663568611b348f~tplv-k3u1fbpfcp-zoom-1.image" alt="good" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">往期好文</h2>
<ul>
<li><a href="https://juejin.cn/post/6976157870014332935" target="_blank" title="https://juejin.cn/post/6976157870014332935">15 张前端高清知识地图，强烈建议收藏</a></li>
<li><a href="https://juejin.cn/post/6940976355097985032" target="_blank" title="https://juejin.cn/post/6940976355097985032">二维码扫码登录是什么原理</a></li>
<li><a href="https://juejin.cn/post/6950584088462163982" target="_blank" title="https://juejin.cn/post/6950584088462163982">让我告诉你一些强无敌的 NPM 软件包</a></li>
<li><a href="https://juejin.cn/post/6968269593206849572" target="_blank" title="https://juejin.cn/post/6968269593206849572">最全 ECMAScript 攻略</a></li>
<li><a href="https://juejin.cn/post/6951684431597797389" target="_blank" title="https://juejin.cn/post/6951684431597797389">前端开发者应该知道的 Centos/Docker/Nginx/Node/Jenkins 操作(🍡 长文)</a></li>
</ul>
<h2 data-id="heading-15">参考文档</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F115403616" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/115403616" ref="nofollow noopener noreferrer">精读《Webpack5 新特性 - 模块联邦》</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Fmodule-federation%2F%23dynamic-remote-containers" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/concepts/module-federation/#dynamic-remote-containers" ref="nofollow noopener noreferrer">webpack 官方文档-动态远程容器</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fmjzhang1993%2Farticle%2Fdetails%2F115871597" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/mjzhang1993/article/details/115871597" ref="nofollow noopener noreferrer">webpack 5 模块联邦实现微前端疑难问题解决</a></li>
</ul></div>  
</div>
            