
---
title: '又快又美又好用的前端框架 Ant Design Pro V5 发布了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd92abbe6054b7b83b483f47772fb59~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 00:04:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd92abbe6054b7b83b483f47772fb59~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>距离上次 Pro 发布已经过去了两年，这两年间前端的生态也发生了一些变化， Low-Code 大行其道，Bundleless 也随着 Snowpack，Vite 的发布越来越火热，前端在国际化，权限，数据流和布局方面已经有了最佳实践。 Ant Design Pro 致力于提升中后台的开发体验，在这些领域我们也提出了自己的解决方案。
​</p>
<p>我们基于以上的问题，分别提供了<strong>最佳实践</strong>，<strong>模板组件</strong>，<strong>编译提速</strong>，<strong>项目集成组件</strong>，** OpenAPI **五项重大功能更新，接下来我会详细介绍这些功能。</p>
<h2 data-id="heading-0">🍣 最佳实践</h2>
<p>在 V5 中我们基于内外部的经验对中后台的常用领域做出了抽象，Ant Design Pro 研发框架基于 umi，在 V5 中我们通过一系列 umi 插件提供了一套中后台最佳实践。Pro 内置了以下的插件：</p>
<ul>
<li><a href="https://umijs.org/zh-CN/plugins/plugin-access" target="_blank" rel="nofollow noopener noreferrer">plugin-access</a>，权限管理</li>
<li><a href="https://umijs.org/zh-CN/plugins/plugin-antd" target="_blank" rel="nofollow noopener noreferrer">plugin-antd</a>，整合 antd UI 组件</li>
<li><a href="https://umijs.org/zh-CN/plugins/plugin-initial-state" target="_blank" rel="nofollow noopener noreferrer">plugin-initial-state</a>，初始化数据管理</li>
<li><a href="https://umijs.org/zh-CN/plugins/plugin-layout" target="_blank" rel="nofollow noopener noreferrer">plugin-layout</a>，配置启用 ant-design-pro 的布局</li>
<li><a href="https://umijs.org/zh-CN/plugins/plugin-locale" target="_blank" rel="nofollow noopener noreferrer">plugin-locale</a>，国际化能力</li>
<li><a href="https://umijs.org/zh-CN/plugins/plugin-model" target="_blank" rel="nofollow noopener noreferrer">plugin-model</a>，基于 hooks 的简易数据流</li>
<li><a href="https://umijs.org/zh-CN/plugins/plugin-request" target="_blank" rel="nofollow noopener noreferrer">plugin-request</a>，基于 umi-request 和 umi-hooks 的请求方案</li>
</ul>
<p>这些插件都支持快速关闭，方便我们组合这些能力。同时基于 umi 的运行时的能力，这些 API 都可以从 umi 中直接导出。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 从一个地方导出国际化，数据流，权限，网络请求</span>
<span class="hljs-keyword">import</span> &#123; useModel, request, useAccess, getLocale, useIntl &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"umi"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">📯 数据流插件</h3>
<p>在过去的几年中，前端一直都使用 redux 来作为默认的数据流方案，但是 redux 系列一直存在样板代码多，代码提示效果差等问题，导致开发体验一直不是很好。虽然 redux 的功能很强大， 但是在中后台开发中全局公用数据较少，没有忒额复杂的数据流。借着 hooks 的东风我们在 V5 中提供了一个轻量的数据流方案  <a href="https://umijs.org/zh-CN/plugins/plugin-model" target="_blank" rel="nofollow noopener noreferrer">plugin-model</a> 。</p>
<p><a href="https://umijs.org/zh-CN/plugins/plugin-model" target="_blank" rel="nofollow noopener noreferrer">plugin-model</a> 提供了 hooks 方案的 API, 并且基于 umi 的运行时能力提供了实时的 TypeScript 提示。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; useModel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"umi"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => &#123;
  <span class="hljs-keyword">const</span> &#123; user, fetchUser &#125; = useModel(<span class="hljs-string">"user"</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;user.name&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"></h3>
<h3 data-id="heading-3">🌎 国际化插件</h3>
<p>国际化一直是各很重要的功能，对于一部分来说用户并不需要，但是对于一部分用户来说是必不可少的。所以在 Pro 中的自带了国际化的功能。在 V5 中我们提供了更简单的 API, 我们可以从 umi 中导出  react-intl 的所有 API。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; useIntl &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"umi"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> intl = useIntl();
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>
      &#123;intl.formatMessage(&#123;
        id: "name",
        defaultMessage: "你好，旅行者",
      &#125;)&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了照顾不想只用国际化的用户，我们提供了<code>i18n-remove</code> 命令来删除所有国际化。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">npm run i18n-remove 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd92abbe6054b7b83b483f47772fb59~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">🖥️  模板组件</h2>
<p>模板组件是我们去年工作的重点，早在 Pro 的第一个版本我们就提供了一系列的区块来帮助用户开发页面，在 2.0 中我们还提供了 umi ui 来管理区块。但是在实际的使用中我们发现区块上手成本高，耦合太强。并没有取得很好的反响。</p>
<p>在 2.0 中我们增加了 ProLayout 在社区得到了很好的反馈，ProLayout 给了我们灵感，我们是不是可以用抽象 Layout 的方式来抽象我们的常见页面。而在中后台中我们最常用的就是 CURD。在 <a href="https://procomponents.ant.design/" target="_blank" rel="nofollow noopener noreferrer">ProCompoents</a> 就是我们对于 CRUD 的抽象。</p>
<p><a href="https://procomponents.ant.design/" target="_blank" rel="nofollow noopener noreferrer">ProCompoents</a> 以 valueType 为核心抽象了不同的 <a href="https://procomponents.ant.design/components/schema#valuetype-%E6%9F%A5%E7%9C%8B" target="_blank" rel="nofollow noopener noreferrer">Field</a>，而每个 <a href="https://procomponents.ant.design/components/schema#valuetype-%E6%9F%A5%E7%9C%8B" target="_blank" rel="nofollow noopener noreferrer">Field</a> 都包含了编辑和只读两种模式，这样一套抽象可以同时用于表格和表单。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ab0a8c722f241d7b6ea16a6c1859b45~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我们可以根据 ProTable 的列配置生成查询表单。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e73c0ff83b154de49d8711f634d8e6ab~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样 valueType 就可以生成表单和表格，并且在此之上增加了Field 的布局功能，我们可以用一套 Field 配置不用的 Layout 来生成不同的表单，同时我们还提供了可编辑表格，FormList 等低频高复杂度的组件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c3f85f9db644a1093a3eab4fdea5854~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于开发者来说 ProTable 可以大大的减少代码量, 只需简单几行就可以得到一个全功能的表格。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> columns: ProColumns<GithubIssueItem>[] = [
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"标题"</span>,
    <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">"title"</span>,
    <span class="hljs-attr">copyable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">ellipsis</span>: <span class="hljs-literal">true</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"创建时间"</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">"showTime"</span>,
    <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">"created_at"</span>,
    <span class="hljs-attr">valueType</span>: <span class="hljs-string">"date"</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"操作"</span>,
    <span class="hljs-attr">valueType</span>: <span class="hljs-string">"option"</span>,
    <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">text, record, _, action</span>) =></span> [<span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span>></span>编辑<span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>, <span class="xml"><span class="hljs-tag"><<span class="hljs-name">a</span>></span>查看<span class="hljs-tag"></<span class="hljs-name">a</span>></span></span>],
  &#125;,
];

<span class="hljs-keyword">const</span> Page = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ProTable</span>
      <span class="hljs-attr">columns</span>=<span class="hljs-string">&#123;columns&#125;</span>
      <span class="hljs-attr">request</span>=<span class="hljs-string">&#123;request(</span>"<span class="hljs-attr">https:</span>//<span class="hljs-attr">proapi.azurewebsites.net</span>/<span class="hljs-attr">github</span>/<span class="hljs-attr">issues</span>", &#123;
        <span class="hljs-attr">params</span>,
      &#125;)&#125;
      <span class="hljs-attr">rowKey</span>=<span class="hljs-string">"id"</span>
      <span class="hljs-attr">headerTitle</span>=<span class="hljs-string">"高级表格"</span>
    /></span></span>
  );
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68fba0fbcc874a9389f9d2642b45a843~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">⚡ 编译提速</h2>
<p>随着前端工程化做的越来越深，前端的依赖越来越多，以 Pro 项目为例，一个初始化的项目包含了react， react-router，antd, ProComponents 。 一个初始化的项目启动就需要 50s。</p>
<h2 data-id="heading-6"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed00058a2c5f4c019788a6e01e07b59d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></h2>
<p>Bundleless  就在此时应运而生。现代浏览器已经支持了 es6 的模块，那么我们就可以再项目中直接使用的 es6 ，而减少编译甚至于不编译。在首次生成 es 模块之后，获得极快的项目启动速度。umi 也提供了 Bundleless  方案 <strong>mfsu</strong>。</p>
<p><a href="https://zhuanlan.zhihu.com/p/385272270" target="_blank" rel="nofollow noopener noreferrer">mfsu <strong>(Module Federation Speed Up)</strong></a>** **是一种基于 webpack5 新特性 Module Federation 的打包提速方案。核心原理是将应用的依赖构建为一个 Module Federation 的 remote 应用，以免去应用热更新时对依赖的编译。 因此，开启 mfsu 可以大幅减少热更新所需的时间。在生产模式，也可以通过提前编译依赖，大幅提升部署效率。</p>
<p>我们在 config.s 中配置 <code>mfsu:&#123;&#125;</code> 和 <code>wepack5:&#123;&#125;</code> 就能享受到编译性能提升的快乐。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123; 
+  mfsu : &#123;&#125;,
+  webpack5: &#123;&#125;, 
+  dynamicImport: &#123;&#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3822bbb21aac4a89a06075f98e1f9f9b~tplv-k3u1fbpfcp-zoom-1.image" alt="Kapture 2021-06-30 at 18.50.33.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们用 Pro 的基础项目整理了一个对比列表，打开 webpack5 和 mfsu 的 Pro 在启动速度和热更新速度上有压倒性的优势。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8223cb3e2455490b98ea4df9d5fad24e~tplv-k3u1fbpfcp-zoom-1.image" alt="图片1.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">📚 项目集成模式组件文档</h2>
<p>我们在实际的项目开发中经常需要抽象一些组件出来，这些组件在应用中广泛使用，但是文档和测试缺失， TypeScript 可能解决部分问题。但是一些设计方面的考虑需要一份文档协同起来才会更佳流畅。所以 Pro 中我们内置了 dumi 的项目集成模式，在登录之后看到业务组件文档的菜单。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e931c5c8f1cd47c08edf67505b734953~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击之后就可以看到 Pro 自带的业务组件文档，文档中包含了 Pro 所有内置组件的简单文档和 API .
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6003fb16894a91844ac2f4fb7d2066~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作为一个项目开发者，集成模式还给我提供了一个良好的 debug 环境。我们的写法与正常的文档写法并无区别。
​</p>
<p>​</p>
<pre><code class="hljs language-matlab copyable" lang="matlab"># 业务组件

这里列举了 Pro 中所有用到的组件，这些组件不适合作为组件库，但是在业务中却真实需要。所以我们准备了这个文档，来指导大家是否需要使用这个组件。

## Footer 页脚组件

这个组件自带了一些 Pro 的配置，你一般都需要改掉它的信息。

```tsx
/**
 * background: <span class="hljs-string">'#f0f2f5'</span>
 */
import React from <span class="hljs-string">'react'</span>;
import Footer from <span class="hljs-string">'@/components/Footer'</span>;

export default () => <Footer />;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">

dumi 会将 md 文件渲染为一个页面，其中的代码块会渲染成一个组件。
​

![image.png](https://cdn.nlark.com/yuque/0/2021/png/84868/1625106761257-3f62de3f-613a-4fe6-97e8-7097f11d5bf4.png#clientId=u09530022-258c-4&from=paste&height=381&id=u4a776da6&margin=%5Bobject%20Object%5D&name=image.png&originHeight=762&originWidth=2192&originalType=binary&ratio=2&size=79703&status=done&style=none&taskId=uc0bead2d-d1c7-44f1-94bb-5f0d4ca7842&width=1096)
点击右下角还可以还可以在 CodeSandbox，快速打开 demo。想要了解更多可以查看 [dumi 基础使用文档](https://d.umijs.org/zh-CN/guide/basic)。


> 内置的文档在项目发布之后便会自动删除，不用担心文档出现在线上。



## 🏷️ OpenAPI


中后台开发中最重要的事情之一就是联调，在这期间后端一般都需要维护一份文档来告诉我们具体的 API 有什么功能，具体的字段信息有哪些，这些信息的维护成本相当高的。如果中途作了更改但是忘记更新文档就会造成信息不同步，在测试时很有可能会造成一个 bug。 Pro V5 支持使用 OpenAPI 3.0.1 的接口描述文档，这份文档可以用 [Swagger](https://swagger.io/) 来生成，对于后端来说可能需要一点工作量，但是带来的收益是远远超出投入的。


Pro 会根据 OpenAPI 来自动生成接口和基础类，配合 TypeScript 的使用，我们可以丝滑的接入后端的数据，并且与使用 `tsc` 来监控后端字段改变导致的字段不对齐问题。


```typescript
declare namespace API &#123;
  type RuleListItem = &#123;
    key?: number;
    disabled?: boolean;
    href?: string;
    avatar?: string;
    name?: string;
    owner?: string;
    desc?: string;
    callNo?: number;
    status?: number;
    updatedAt?: string;
    createdAt?: string;
    progress?: number;
  &#125;;
&#125;

import &#123; request &#125; from 'umi';

/** 获取规则列表 GET /api/rule */
export async function rule(params: API.PageParams, options?: &#123; [key: string]: any &#125;) &#123;
  return request<API.RuleList>('/api/rule', &#123;
    method: 'GET',
    params: &#123;
      ...params,
    &#125;,
    ...(options || &#123;&#125;),
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>详细的接入流程可以查看 <a href="https://beta-pro.ant.design/docs/openapi-cn" target="_blank" rel="nofollow noopener noreferrer">OpenApi 的接入文档</a> 。</p>
<h2 data-id="heading-8">🧵 如何升级到 V5</h2>
<p>Pro 的 V4 与 V5 的底层架构是对齐，我们可以只选配自己喜欢的功能来使用新的特性。</p>
<ul>
<li><a href="https://umijs.org/plugins/plugin-access" target="_blank" rel="nofollow noopener noreferrer">plugin-access</a>，权限管理</li>
<li><a href="https://umijs.org/plugins/plugin-analytics" target="_blank" rel="nofollow noopener noreferrer">plugin-analytics</a>，统计管理</li>
<li><a href="https://umijs.org/plugins/plugin-antd" target="_blank" rel="nofollow noopener noreferrer">plugin-antd</a>，整合 antd UI 组件</li>
<li><a href="https://umijs.org/plugins/plugin-crossorigin" target="_blank" rel="nofollow noopener noreferrer">plugin-crossorigin</a>，通常用于 JS 出错统计</li>
<li><a href="https://umijs.org/plugins/plugin-dva" target="_blank" rel="nofollow noopener noreferrer">plugin-dva</a>，整合 dva</li>
<li><a href="https://umijs.org/plugins/plugin-helmet" target="_blank" rel="nofollow noopener noreferrer">plugin-helmet</a>，整合 <a href="https://github.com/nfl/react-helmet" target="_blank" rel="nofollow noopener noreferrer">react-helmet</a>，管理 HTML 文档标签（如标题、描述等）</li>
<li><a href="https://umijs.org/plugins/plugin-initial-state" target="_blank" rel="nofollow noopener noreferrer">plugin-initial-state</a>，初始化数据管理</li>
<li><a href="https://umijs.org/plugins/plugin-layout" target="_blank" rel="nofollow noopener noreferrer">plugin-layout</a>，配置启用 ant-design-pro 的布局</li>
<li><a href="https://umijs.org/plugins/plugin-locale" target="_blank" rel="nofollow noopener noreferrer">plugin-locale</a>，国际化能力</li>
<li><a href="https://umijs.org/plugins/plugin-model" target="_blank" rel="nofollow noopener noreferrer">plugin-model</a>，基于 hooks 的简易数据流</li>
<li><a href="https://umijs.org/plugins/plugin-request" target="_blank" rel="nofollow noopener noreferrer">plugin-request</a>，基于 umi-request 和 umi-hooks 的请求方案</li>
<li><a href="https://umijs.org/plugins/plugin-esbuild" target="_blank" rel="nofollow noopener noreferrer">plugin-esbuild</a>， 使用 esbuild 作为压缩器,来获得火箭般的代码压缩速度</li>
<li><a href="https://umijs.org/zh-CN/docs/mfsu" target="_blank" rel="nofollow noopener noreferrer">mfsu 提速方案</a> ，浪费时间的是可耻的，打开 mfsu 可以获得极大的编译速度提升</li>
</ul>
<p>如果需要完全切换成我们的最佳实践，可以参考<a href="https://beta-pro.ant.design/docs/upgrade-v5-cn" target="_blank" rel="nofollow noopener noreferrer">升级到 Pro V5</a> 进行操作。</p>
<h2 data-id="heading-9">❤️ 特别鸣谢</h2>
<p>感谢所有提交错误、发起PR、回复问题、编写文档等的人！在这里特别要感谢  <a href="https://github.com/kaoding" target="_blank" rel="nofollow noopener noreferrer">@kaoding</a> 同学承担了 v5 很大一部分开发工作。
如果你在使用 Ant Design Pro 时遇到任何问题，可随时在 GitHub <a href="https://link.zhihu.com/?target=https%3A//github.com/ant-design/ant-design-pro/issues" target="_blank" rel="nofollow noopener noreferrer">提交问题</a>。
感谢你的阅读，敬请安装、尝试。</p></div>  
</div>
            