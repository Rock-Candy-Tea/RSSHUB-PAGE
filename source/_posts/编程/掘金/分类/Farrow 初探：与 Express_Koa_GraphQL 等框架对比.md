
---
title: 'Farrow 初探：与 Express_Koa_GraphQL 等框架对比'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ac1b0326f743e88b0cd5517e64ea8e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 19:49:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ac1b0326f743e88b0cd5517e64ea8e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>几个月前我的 Mentor 也就是 <a href="https://juejin.cn/user/2664871913078168" target="_blank">@工业聚</a> 开发了一个新的 Node.js Web 框架: <a href="https://github.com/Lucifier129/farrow" target="_blank" rel="nofollow noopener noreferrer">Farrow</a>。</p>
<p>这篇文章的内容就是围绕这个框架展开，如果你还不了解 Farrow，可以移步 <a href="https://juejin.cn/user/2664871913078168" target="_blank">@工业聚</a> 大大<a href="https://juejin.cn/post/6916708689705435150" target="_blank">介绍 Farrow 的文章</a>。</p>
<p>可以简单概括这个框架的特点：友好的 TypeScript 类型和函数式风格。</p>
<p>作为 TypeScript 和函数式编程的爱好者，在这个框架完成之初，我就成为了第一个吃螃蟹的人。</p>
<p>我基于这个框架重构了我的个人博客项目，也趁此机会谈一下我体会到的 Farrow 相对现有的 <a href="https://expressjs.com/" target="_blank" rel="nofollow noopener noreferrer">Express</a>/<a href="https://koajs.com/" target="_blank" rel="nofollow noopener noreferrer">Koa</a>/<a href="https://graphql.orh/" target="_blank" rel="nofollow noopener noreferrer">GraphQL</a> 的优势，以及不足。</p>
<p>虽然我有一定的 Express/Koa/GraphQL 的使用经验，碍于职业生涯的长度，不管是在框架设计方面涉及的广度和深度还是开发经验来说，我都尚有不足的。因此文章中出现错误和偏颇，在所难免，希望各位看官手下留情。</p>
<p>好，话不多说，我们开始吧。</p>
<h2 data-id="heading-0">现有框架的问题</h2>
<p>已有框架的能力已经非常强大，基本可以覆盖所有场景，因此问题不在能力方面，而是易用程度。</p>
<p>在使用 Express/Koa/GraphQL 时遇到的共同的问题是类型闭合，也叫类型安全，即 <a href="https://juejin.cn/user/2664871913078168" target="_blank">@工业聚</a> 在文章中说的 type safe。</p>
<p>可能由于 Express/Koa/GraphQL 出现的时候，TypeScript 还有没有兴起，所以这个问题在它们中都比较明显。</p>
<p>主要出在三个地方：共享上下文（Context）、接口入参类型（input type）和接口返回值类型（output type）。</p>
<h3 data-id="heading-1">共享上下文（Context）</h3>
<p>在不同的框架中，它们都是如何实现 requestHandler/resolver 间变量共享的？</p>
<p>GraphQL 挂载在 <code>ctx</code> 上</p>
<p>Koa 挂载在 <code>ctx</code> 上</p>
<p>Express 挂载在 <code>req</code> 上</p>
<p>可以看出，目前的解决方案都是将变量挂载在一个会被传递给每一个 requestHandle/resolver 的对象上。</p>
<p>这种方案的问题就是类型，一个requestHandle/resolver 它如何知道传递给它的那个对象中有没有挂载哪个变量？</p>
<p>它无法预测，而在实际的场景中，常用的做法是 <code>@ts-ignore</code> 或者构造一个有那个变量的 <code>ctx/req</code> 类型，然后使用 <code>as</code>。</p>
<p>我不知道其他人如何评价这两种方案，我个人认为它们应该是后门（backdoor），不应频繁使用。</p>
<h3 data-id="heading-2">接口入参（input type）</h3>
<p>这里的期望接口入参是 type-safe 类型安全的，是指校验入参类型是否正确，并体现在类型上。</p>
<p>GraphQL 做了类型校验，Express/Koa 等框架需要引入 joi/ajv/superstruct 等库配合。 GraphQL 的类型校验难以体现到 TypeScript 类型上，在客户端开发的时候依旧需要使用 as，也并不便利。</p>
<p>RESTful 支持通过URL 传参，然而对 URL 中参数的类型校验，并且体现在语言的类型上，也是必要的。这里可以参考一个 Rust 的 Web 框架：<a href="https://rocket.rs/" target="_blank" rel="nofollow noopener noreferrer">Rocket</a>。</p>
<h3 data-id="heading-3">接口返回值（output type）</h3>
<p>在不同的框架中，他们都是如何设置接口的返回值的？</p>
<p>Express 通过调用 <code>res.send</code></p>
<p>Koa 通过设置 <code>ctx.body</code></p>
<p>GraphQL 通过 resolver 函数的返回值</p>
<p>而这些设置方式，都无法反映在语言层面的类型上，进行语言层面的类型约束（GraphQL 可以做到，但需要做很多事情）。</p>
<p>在服务器端无法在语言层面约束返回值类型，只能在逻辑层面去约束。客户端请求时的问题，客户端无法知道接口返回值的类型，不管是使用 Express、Koa 还是 GraphQL，客户端都只能进行假设。</p>
<hr>
<p>在使用 GraphQL 时，接口入参和接口返回值类型约束的部分，我做过一些尝试。在服务器端将 GraphQL schema 转成 TypeScript 类型，并将之对应到不同的 Query，同步到客户端，但遇到了如下问题：</p>
<ul>
<li>GraphQL Schema 的类型系统和 TypeScript 的类型系统不是同构的，即无法完美的互相转换，导致使用时体验很差。</li>
<li>因为 GraphQL 支持请求合并和数据切片，所以如果要有完整的体验，在客户端编写 Query 语句的时候还要做一些其他事情，当然，这一部分是可以做到的（如 facebook 的 relay 框架通过 compiler 去提取）。但考虑到第一个问题，即使这一部分做好了，使用体验也会是差强人意。</li>
</ul>
<p>GraphQL 同时也会增加代码量。同样功能的接口，除了业务逻辑处理部分的代码 GraphQL 需要的代码量和 RESTful 根本不是一个数量级，使用 GraphQL 完成一次请求需要写 2 份类型（服务器端的 Schema 、客户端的 Query），如果使用 TypeScript，则将会变成 4 份（加上服务器端的入参类型、客户端的入参类型与返回值类型），这是一个不小得负担。</p>
<h2 data-id="heading-4">Farrow 提供的解决方式</h2>
<h3 data-id="heading-5">友好的变量共享：Context</h3>
<p>在 Farrow 中内置了类似 React Context 的工具，创建 Context，然后可以在所有中间件中通过 Hook 拿到 Context 中的值，而不必通过参数。不必重复标记 ctx 参数类型。</p>
<p>Farrow Context 可以做到同一个请求的中间件和 requestHandler 间的变量共享，还可以做到不同的请求之间的变量共享，这个工具的具体细节可以查看 Farrow 文档，大佬可以直接看源码。</p>
<h3 data-id="heading-6">接口入参与返回值校验（input type & output type)</h3>
<p>在上面的讨论中可以发现，Express 和 Koa 的方案没有内置这个校验功能，而 GraphQL尽管内置了，但有类型系统跟 TS 的同步问题。</p>
<p>Farrow 的方式是，自己实现了一套与 TypeScript 类型同构的类型系统，一次请求只需要实现一份类型，其他的通过推导、生成的方式（<a href="https://github.com/Lucifier129/farrow/issues/19#issuecomment-751370197" target="_blank" rel="nofollow noopener noreferrer">introspection</a>）完成，从而也规避了 GraphQL 代码量增加的问题。</p>
<p>除此之外，基于 TypeScript 4.1 发布的特性——Template Literal Types，Farrow 实现了 Rocket 框架所实现的对 URL 中参数的校验并映射到了 TypeScript 的类型中。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ac1b0326f743e88b0cd5517e64ea8e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">Farrow 实战</h2>
<p>现在结合我重构个人博客项目：<a href="https://github.com/tqma113/me" target="_blank" rel="nofollow noopener noreferrer">me</a> 的具体场景，来呈现一下上述方案的具体使用方式。</p>
<p>技术栈使用了 react-torch（我基于 React 和 Webpack 实现的简单的 SSR 框架）、farrow。</p>
<h3 data-id="heading-8">通过 Farrow Context 跨多个中间件共享变量</h3>
<p>原因：webpack-dev-middleware 会在 webpack 打包完成之后将打包的信息 <code>stats</code> 挂载在 <code>res.locals.webpack</code> 上，而这些信息在 SSR 的时候会用到，当然这个不重要，你现在只需要知道后面的一个 requestHandler 需要用到一个变量，而这个变量需要在这个中间件中设置好，即需要共享变量。</p>
<p>像 React 那样创建 Context 和 Hook</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-pipeline'</span>

<span class="hljs-keyword">const</span> WebpackContext = createContext<WebpackContextType | <span class="hljs-literal">null</span>>(<span class="hljs-literal">null</span>)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useWebpackCTX = (): <span class="hljs-function"><span class="hljs-params">WebpackContextType</span> =></span> &#123;
  <span class="hljs-keyword">let</span> ctx = WebpackContext.use()

  <span class="hljs-keyword">if</span> (ctx.value === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`assest not found`</span>)
  &#125;

  <span class="hljs-keyword">return</span> ctx.value
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写 Farrow 中间件，动态更新 Context value</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> ctx: WebpackContextType = &#123;
  <span class="hljs-attr">assets</span>: &#123;&#125;,
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> webpackDevMiddleware = (
  compiler: Compiler
): <span class="hljs-function"><span class="hljs-params">HttpMiddleware</span> =></span> &#123;
  compile(compiler, ctx)

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">async</span> (_, next) => &#123;
    <span class="hljs-keyword">const</span> userCtx = WebpackContext.use()

    userCtx.value = ctx

    <span class="hljs-keyword">return</span> next()
  &#125;
&#125;

<span class="hljs-keyword">const</span> compile = <span class="hljs-function">(<span class="hljs-params">compiler: Compiler, context: WebpackContextType</span>) =></span> &#123;
  ...

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">done</span>(<span class="hljs-params">stats: Stats</span>) </span>&#123;
    ...

    context.assets = webpackStats.assets

    ...
  &#125;

  compiler.hooks.done.tap(<span class="hljs-string">'WebpackDevMiddleware'</span>, done)
  
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挂载中间件到 farrow-http pipeline</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Http &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-http'</span>
<span class="hljs-keyword">import</span> webpack <span class="hljs-keyword">from</span> <span class="hljs-string">'webpack'</span>

<span class="hljs-keyword">const</span> http = Http()

<span class="hljs-keyword">const</span> config = &#123; ... &#125;
<span class="hljs-keyword">const</span> compiler = webpack(config)

http.use(webpackDevMiddleware(compiler))
然后，在任意中间件里，通过 hooks 访问 Context value。不用修改参数。也不用标记类型。

http.use(<span class="hljs-keyword">async</span> (req) => &#123;
  <span class="hljs-keyword">const</span> webpackCTX = useWebpackCTX()
  <span class="hljs-comment">// 拿到变量</span>
  <span class="hljs-keyword">const</span> assets = webpackCTX.assets

  ...
&#125;)

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此我们就完整的实现了这个功能，而且实现过程类型安全。为了演示，我删除了部分不相关的代码，这个功能的完整实现可以去 <a href="https://github.com/tqma113/me/blob/main/webpackHook.ts" target="_blank" rel="nofollow noopener noreferrer">webpackHook.ts</a> 查看。</p>
<h3 data-id="heading-9">使用 Farrow-Api 编写后端接口，并生成代码给前端使用</h3>
<p>接口入参与返回值：简单的接口实现</p>
<blockquote>
<p>我这个项目内容非常简单，没有动态的数据变更，完全可以做成静态页面，但我依旧把它做成了支持 SSR 的 SPA 项目。希望各位看官不要在意这一点，多关注 farrow 的特性。</p>
</blockquote>
<p>1）用 farrow-schema 定义数据类型：model type</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Int, List, ObjectType, Type, Literal, TypeOf &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-schema'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Numbers = List(<span class="hljs-built_in">Number</span>)

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Note</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ObjectType</span> </span>&#123;
  id = &#123;
    <span class="hljs-attr">description</span>: <span class="hljs-string">`Note id`</span>,
    [Type]: Int,
  &#125;

  title = &#123;
    <span class="hljs-attr">description</span>: <span class="hljs-string">`Note title`</span>,
    [Type]: <span class="hljs-built_in">String</span>,
  &#125;

  ...

  tags = &#123;
    <span class="hljs-attr">description</span>: <span class="hljs-string">`Note tags`</span>,
    [Type]: Numbers,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2）定义接口入参与返回值类型（这里和 GraphQL 的 Schema 很像）：input type 和 output type</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; ObjectType, Type, Literal, Union &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-schema'</span>

<span class="hljs-comment">// get notes 不需要参数，因此留空</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> GetNotesInput = &#123;&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> NoteList = List(Note)

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GetNotesSuccess</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ObjectType</span> </span>&#123;
  <span class="hljs-keyword">type</span> = Literal(<span class="hljs-string">'GetNotesSuccess'</span>)
  notes = &#123;
    <span class="hljs-attr">description</span>: <span class="hljs-string">'Note list'</span>,
    [Type]: NoteList,
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SystemError</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ObjectType</span> </span>&#123;
  <span class="hljs-keyword">type</span> = Literal(<span class="hljs-string">'SystemError'</span>)
  message = &#123;
    <span class="hljs-attr">description</span>: <span class="hljs-string">'SystemError message'</span>,
    [Type]: <span class="hljs-built_in">String</span>,
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> GetNotesOutput = Union(GetNotesSuccess, SystemError)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3）有了 input type 和 output type，可以构建 API 函数</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Api &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-api'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getNotes = Api(&#123;
  <span class="hljs-attr">description</span>: <span class="hljs-string">'get notes'</span>,
  <span class="hljs-attr">input</span>: GetNotesInput,
  <span class="hljs-attr">output</span>: GetNotesOutput,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4）为 getNotes API 函数实现 handler</p>
<pre><code class="hljs language-ts copyable" lang="ts">getNotes.use(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">const</span> notes = <span class="hljs-built_in">require</span>(path.resolve(process.cwd(), <span class="hljs-string">'./data/notes.json'</span>))
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'GetNotesSuccess'</span>,
      notes,
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'SystemError'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-built_in">JSON</span>.stringify(err),
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5）合并 API 为 Service，以便挂载到 http pipeline 里。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; ApiService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-api-server'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> entries = &#123;
  getNotes,
  <span class="hljs-comment">// 这里可以添加其他的 API</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> notesService = ApiService(&#123; entries &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6）挂载 Service</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Http &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-http'</span>

<span class="hljs-keyword">const</span> http = Http()

http.route(<span class="hljs-string">'/api'</span>).use(notesService)

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7）配置客户端代码生成规则</p>
<pre><code class="copyable">// 启动服务器，运行以下代码
import &#123; createApiClients &#125; from 'farrow/dist/api-client'

export const syncClient = () => &#123;
  const client = createApiClients(&#123;
    services: [
      &#123;
        src: `http://localhost:3000/api`,
        dist: `$&#123;__dirname&#125;/src/api/model.ts`,
        alias: '/api',
      &#125;,
    ],
  &#125;)

  return client.sync()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成给客户端使用的代码如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; apiPipeline &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'farrow-api-client'</span>

<span class="hljs-comment">/**
 * &#123;<span class="hljs-doctag">@label </span>SystemError&#125;
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> SystemError = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'SystemError'</span>
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@remarks </span>SystemError message
   */</span>
  <span class="hljs-attr">message</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-comment">/**
 * &#123;<span class="hljs-doctag">@label </span>Note&#125;
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> Note = &#123;
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@remarks </span>Note id
   */</span>
  <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span>

  ...

  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@remarks </span>Note tags
   */</span>
  <span class="hljs-attr">tags</span>: <span class="hljs-built_in">number</span>[]
&#125;

<span class="hljs-comment">/**
 * &#123;<span class="hljs-doctag">@label </span>GetNotesSuccess&#125;
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> GetNotesSuccess = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'GetNotesSuccess'</span>
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@remarks </span>Note list
   */</span>
  <span class="hljs-attr">notes</span>: Note[]
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> url = <span class="hljs-string">'/api'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> api = &#123;
  <span class="hljs-comment">/**
   * <span class="hljs-doctag">@remarks </span>get notes
   */</span>
  <span class="hljs-attr">getNotes</span>: <span class="hljs-function">(<span class="hljs-params">input: &#123;&#125;</span>) =></span>
    apiPipeline.invoke(url, &#123; <span class="hljs-attr">path</span>: [<span class="hljs-string">'getNotes'</span>], input &#125;) <span class="hljs-keyword">as</span> <span class="hljs-built_in">Promise</span><
      GetNotesSuccess | SystemError
    >,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在客户端，我们不必再从头编写如何 fetch 接口数据的代码。而是直接 import 前面生成的代码文件。直接接口调用，如下所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts">api.getNotes(&#123;&#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (res.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'GetNotesSuccess'</span>: &#123;
      store.dispatch(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'SET_NOTES'</span>,
        <span class="hljs-attr">payload</span>: res.notes,
      &#125;)
      <span class="hljs-keyword">break</span>
    &#125;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'SystemError'</span>: &#123;
      store.dispatch(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'SET_ERRORS'</span>,
        <span class="hljs-attr">payload</span>: [res.message],
      &#125;)
      <span class="hljs-keyword">break</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一部分的详细实现已经开源，可以点击 <a href="https://github.com/tqma113/me/tree/main/api" target="_blank" rel="nofollow noopener noreferrer">server api</a> 或 <a href="https://github.com/tqma113/me/tree/main/src/api" target="_blank" rel="nofollow noopener noreferrer">client api</a> 查看完整实现。客户端同步代码的实现则在 <a href="https://github.com/tqma113/me/blob/main/syncClient.ts" target="_blank" rel="nofollow noopener noreferrer">syncClient.ts</a>。</p>
<p>也可以访问 <a href="https://github.com/Lucifier129/farrow" target="_blank" rel="nofollow noopener noreferrer">Farrow 项目</a>，了解更多。</p>
<h2 data-id="heading-10">Farrow 使用总结</h2>
<ul>
<li>最明显的感受，类型衔接真的很流畅，<code>as</code>、<code>any</code>、<code>@ts-ignore</code> 不存在的。对于有强迫症的 TypeScript 开发者来说，简直就是福音。</li>
<li>类型系统相对 GraphQL 好了很多，没有那么多的东西需要写。</li>
<li>在项目重构的过程中，我还向 Farrow 项目提了许多 issue 和 PR，并对项目中用的 webpack-dev-middleware 进行了重构。</li>
</ul>
<p>在使用 Farrow-Api 重构个人项目后，我还发现 Farrow-Api 也可以像 GraphQL 那样 batch 多个接口请求，将它们合并为一次，从而减少前后端 http request 数量，提升性能。后续我将尝试实现它，验证一下，然后提 Pull-Request。</p>
<h2 data-id="heading-11">个人结论</h2>
<p>Farrow 的优势：</p>
<ul>
<li>类型安全。类型系统和 TypeScript 类型生成（<a href="https://github.com/Lucifier129/farrow/issues/19#issuecomment-751370197" target="_blank" rel="nofollow noopener noreferrer">introspection</a>）优势很大，如果结合 <a href="https://github.com/sequelize/sequelize" target="_blank" rel="nofollow noopener noreferrer">sequelize</a> ，应该可以实现从数据库到前端应用的类型安全。</li>
</ul>
<p>Farrow 的不足：</p>
<ul>
<li>生态不健全。在实践过程中需要做好自己造轮子的准备，这无疑增加了工作量，对开发者也是一种考验。</li>
<li>只针对 Node.js 技术栈，目前没有支持其他语言的计划。</li>
</ul>
<h2 data-id="heading-12">对 Farrow 的未来展望</h2>
<ul>
<li>类型系统还有提升空间。如果类型系统做成像 GraphQL Schema 一样语言无关的 DSL，然后服务器端和客户端都根据这个生成部分代码，有望支持更多语言。</li>
<li>支持 <a href="https://github.com/denoland/deno" target="_blank" rel="nofollow noopener noreferrer">Deno</a> 。</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            