
---
title: 'Typescript 泛型包教包会'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4718ffeeee524d95b4154d984c70c26e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Apr 2021 03:10:48 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4718ffeeee524d95b4154d984c70c26e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>不知道在你的日常工作中，是否出现过这样的场景：明明 <code>Typescript</code> 官方文档已经看了很多遍，实际写起代码来却各种煎熬，遇到报错，在搜索无果之后，无奈写下 any。🤷‍♀️
（我猜有，不然你也不会点开这篇文章。👻</p>
<p>而阻碍你强类型更近一步的，绝大多数情况下是因为<strong>泛型</strong>还没完全掌握。这篇文章将从我日常工作中遇到的一个例子入手，一步步介绍哪里需要用到泛型，怎么写~</p>
<p>（如果除了泛型，Typescript 其他知识点也不太熟怎么办 😰 ？可以我之前整理的另一篇比较全面的文章<a href="https://juejin.cn/post/6876981358346895368" target="_blank">结合实例学习 Typescript</a>。</p>
<p>Let's begin。</p>
<h3 data-id="heading-0">问题</h3>
<p>说，后端提供了多个支持分页查列表数据的接口，这些接口的<strong>参数格式、响应结果、分页形式</strong>可能都不一样。拿分页形式来说，常见的分页参数类型就有好几种，传页数和每页数量、传偏移值和 limit、使用上一页最后一个 id 来查询等等。</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">page_size</span>: number,
  <span class="hljs-attr">page_num</span>: number
&#125;

&#123;
  <span class="hljs-attr">offset</span>: number,
  <span class="hljs-attr">limit</span>: number
&#125;

&#123;
  <span class="hljs-attr">forward</span>: boolean
  <span class="hljs-attr">last_id</span>: string
  <span class="hljs-attr">page_size</span>: number
&#125;

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些接口数据量都在几千条数据左右，考虑数据库的压力，后端同学不建议一次拉几千条数据，需要前端分页去全部拉取。</p>
<p>为了避免分页的逻辑每个接口都写一次，要求实现一个<strong>强类型</strong>的工具方法，实现自动分页拉取全部数据的功能。</p>
<h4 data-id="heading-1">代码实现</h4>
<p>这篇文章的重点不在如何实现这样的功能，简单画一下流程图，相信大部分人都能实现。</p>
<p><img alt="WX20210401-171127.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4718ffeeee524d95b4154d984c70c26e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>一份可行的代码实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> unpaginate = <span class="hljs-function">(<span class="hljs-params">
  api,
  config,
</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; getParams, hasMore, dataAdaptor &#125; = config

  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">iterator</span>(<span class="hljs-params">time, lastRes</span>) </span>&#123;
    <span class="hljs-comment">// 通过上一次请求结果和第几次请求获取下一次请求的参数</span>
    <span class="hljs-keyword">const</span> params = getParams(lastRes, time)
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> api(params)

    <span class="hljs-keyword">let</span> next = []

    <span class="hljs-comment">// 如果还有下一页，继续拉取</span>
    <span class="hljs-keyword">if</span> (hasMore(res, params)) &#123;
      next = <span class="hljs-keyword">await</span> iterator(time + <span class="hljs-number">1</span>, res)
    &#125;

    <span class="hljs-comment">// 拼接结果一起返回</span>
    <span class="hljs-keyword">return</span> dataAdaptor(res).concat(next)
  &#125;

  <span class="hljs-keyword">return</span> iterator()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>代码解读</strong>：<code>unpaginate </code> 方法第一个参数传入一个返回 Promise 结果的 api 方法；第二个参数支持传入一个可配置对象：</p>
<p><code>getParams</code> 方法会把上一次请求的结果以及当前是第几次请求回传，方便使用者设置请求参数；<br>
<code>hasMore</code> 方法会回传当前请求的结果和参数，需要使用者告知程序是否已经拉取完毕；<br>
<code>dataAdaptor</code> 方法则把每次请求得到的结果，回传回去允许自定义返回结果的格式（例如把某个字段下划线改成驼峰），并把返回值作为最终结果存下来；</p>
<p>想一想，你在用 <code>Typescript</code> 的时是否也实现过类型的功能，类型安全吗？编码时会有代码提示吗？还是说也是 <code>any</code> 一把梭呢？</p>
<p>接下来，我们将为一步一步为这个方法提供<strong>类型支持</strong>。</p>
<h3 data-id="heading-2">Typescritp 泛型加持</h3>
<p>首先从参数入手，为 api 和 config 编写<strong>最基本</strong>的类型声明。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface Config &#123;
  <span class="hljs-attr">hasMore</span>: <span class="hljs-function">(<span class="hljs-params">res?: any, params?: any</span>) =></span> boolean
  <span class="hljs-attr">getParams</span>: <span class="hljs-function">(<span class="hljs-params">res?: any, time?: number</span>) =></span> any
  <span class="hljs-attr">dataAdaptor</span>: <span class="hljs-function">(<span class="hljs-params">res: any</span>) =></span> any[]
&#125;

<span class="hljs-keyword">const</span> unpaginate = (
  api: <span class="hljs-function">(<span class="hljs-params">params: any</span>) =></span> <span class="hljs-built_in">Promise</span><any[]>,
  config: Config,
): <span class="hljs-built_in">Promise</span><any[]> => &#123;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的类型声明能起的作用不大（因为到处是 <code>any</code>），不过也比没有好，至少在给 <code>api</code> 和 <code>config</code> 传不符合类型的参数时会报错。</p>
<h4 data-id="heading-3">第一个泛型——参数类型</h4>
<p>很容易看到，<code>Config</code> 类型中方法的参数和 <code>api</code> 类型<strong>强关联</strong>。<code>api</code> 的参数的类型决定了 <code>hasMore</code> 方法的 <code>params</code> 参数类型。而返回结果的类型，三个方法都会用到了。</p>
<blockquote>
<p>说到方法，在 Typescript 中，可以用 <code>Parameters </code>，<code>ReturnType</code> 来从方法的类型上提取参数类型和返回值类型。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">type EventListenerParamsType = Parameters<<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span>.addEventListener>;
<span class="hljs-comment">// [type: string, listener: EventListenerOrEventListenerObject, options?: boolean | AddEventListenerOptions | undefined]</span>

type A = <span class="hljs-function">(<span class="hljs-params">a: number</span>) =></span> string
type B = ReturnType<A>
<span class="hljs-comment">// string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而这里 <code>api</code> 不是固定的类型，需要根据<strong>动态</strong>的 <code>api</code> 类型上提取类型，<strong>泛型</strong>登场。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> unpaginate = <T extends (params: any) => Promise<any>>(
  api: T,
  config: Config,
): Promise<any[]> => &#123;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在方法前加上了 <code><T extends (params: any) => Promise<any>></code> 这段代码，表示声明了一个泛型，<code>extends</code> 限制了这个泛型的下限：必须是一个方法，并且返回一个 Promise 结果。</p>
<p>然后又将 <code>T</code> 类型赋予 <code>api</code>，这样写完后面再使用类型 <code>T</code>，Typescript 就<strong>动态</strong>地根据实际调用的 <code>api</code> 方法类型<strong>自动推导</strong>了。</p>
<p><code>api</code> 是泛型，<code>Config</code> 当然也需要是泛型，<strong>泛型是当做参数可以传递的</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface Config<P> &#123;
  <span class="hljs-attr">hasMore</span>: <span class="hljs-function">(<span class="hljs-params">res?: R, params?: P</span>) =></span> boolean
  <span class="hljs-comment">//  ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>interface Config<P></code> 这里我们让 Config 也支持了泛型参数，将其传给了 <code>parmas</code> 参数。可以认为这里的 <code>P</code> 只是<strong>随意</strong>起的变量名，换成 <code>T</code> 也是可以的。</p>
<p>结合 <code>Parameters</code> 泛型工具方法，取 <code>T</code> 的第一个参数类型传给 <code>Config</code>，这样它们的类型就关联起来了。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> unpaginate = <T extends (params: any) => Promise<any>>(
  api: T,
  config: Config<Parameters<T>[0]>,
): Promise<any[]> => &#123;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Parameters<T>[0]</code> 的意思是，取 T 类型的参数（是一个数组类型）的第一个参数类型。</p>
<h4 data-id="heading-4">第二个泛型——返回值的类型</h4>
<p>参数类型能动态推导出来，按道理 <code>api</code> 的返回结果也可以使用同样的操作实现。</p>
<p>不过这里会遇到一个棘手的问题，<code>api</code> 返回结果的类型是 <code>Promsie<R></code>，而 config 回传回去的结果应该去 <code>Promise</code> 化的 <code>R</code> 类型。</p>
<p>从泛型中提取类型，我们会用到 <a href="https://juejin.cn/post/6876981358346895368#heading-26" target="_blank"><code>infer</code></a>，直接看代码吧：</p>
<pre><code class="hljs language-js copyable" lang="js">type UnPromise<T> = T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Promise</span><infer U> ? U : <span class="hljs-literal">undefined</span>

type A = <span class="hljs-built_in">Promise</span><number>
type B = UnPromise<A>
<span class="hljs-comment">// number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果说泛型是动态类型，infer 就是动态的动态类型</strong>。上面的例子中，我们在 <code>extends</code> 子句中使用，告诉 <code>Typescript</code> 这里的类型需要动态推导一下。</p>
<p>提取出了返回值的实体类型，继续完善类型定义：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface Config<P, R> &#123;
  <span class="hljs-attr">hasMore</span>: <span class="hljs-function">(<span class="hljs-params">res?: R, params?: P</span>) =></span> boolean

  <span class="hljs-attr">getParams</span>: <span class="hljs-function">(<span class="hljs-params">res?: R, time?: number</span>) =></span> Partial<P>

  dataAdaptor: <span class="hljs-function">(<span class="hljs-params">res: R</span>) =></span> any[]
&#125;

type UnPromise<T> = T <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Promise</span><infer U> ? U : <span class="hljs-literal">undefined</span>

<span class="hljs-keyword">const</span> unpaginate = <
  T <span class="hljs-keyword">extends</span> (params: any) => <span class="hljs-built_in">Promise</span><any>,
  U <span class="hljs-keyword">extends</span> UnPromise<ReturnType<T>>
>(
  api: T,
  <span class="hljs-attr">config</span>: Config<Parameters<T>[<span class="hljs-number">0</span>], U>,
): <span class="hljs-built_in">Promise</span><any[]> => &#123;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个泛型 <code>U</code> 是动态从 <code>UnPromise<ReturnType<T>></code> 推导出来的，然后再将其传递给 <code>Config</code> 就完成了返回结果的类型传导。</p>
<h4 data-id="heading-5">第三个泛型——格式化后的结果类型</h4>
<p>剩下最后一个要处理的问题，是 <code>dataAdaptor</code> 的返回值结果类型。我们对其返回结果没有任何限制，需要做的也是让 Typescirpt 自行推导和传递。
并做为 <code>unpaginate</code> 方法的返回结果类型。</p>
<p>这里需要再定义一个泛型：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface Config<P, R, V> &#123;
  <span class="hljs-comment">//  ...</span>
  <span class="hljs-attr">dataAdaptor</span>: <span class="hljs-function">(<span class="hljs-params">res: R</span>) =></span> V[]
&#125;

<span class="hljs-keyword">const</span> unpaginate = <
  T <span class="hljs-keyword">extends</span> (params: any) => <span class="hljs-built_in">Promise</span><any>,
  U <span class="hljs-keyword">extends</span> UnPromise<ReturnType<T>>,
  V <span class="hljs-keyword">extends</span> any
>(
  api: T,
  <span class="hljs-attr">config</span>: Config<Parameters<T>[<span class="hljs-number">0</span>], U, V>,
): <span class="hljs-built_in">Promise</span><V[]>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们使用 <code>V extends any</code> 定义了新的泛型类型，将其传递给 <code>Config.dataAdaptor</code> 的返回结果，<code>dataAdaptor: (res: R) => V[]</code> 这样 Typescript 在具体的场景下就可以根据 <code>dataAdaptor</code> 返回的数组类型 => 推导出 <code>V</code> 的类型了。</p>
<p>再将 <code>V[]</code> 作为 <code>unpaginate</code> 的返回值类型，这样就可以全串起来了。</p>
<h3 data-id="heading-6">最终效果</h3>
<p>API 方法参数推导：</p>
<p><img alt="WX20210401-183613.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a1c613021f84bb5a4490a04ef01ffb1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>API 方法返回结果推导：
<img alt="WX20210401-183554.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b84b524e9e204967b75bf60abc240fbe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>格式化后返回结果推导：
<img alt="WX20210401-183347.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a996007ae88b45d0a40e9fb472c29bb0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以在<a href="https://www.typescriptlang.org/play?#code/KYDwDg9gTgLgBASwHY2FAZgQwMbDgYQiXQQHMAeABQBo4AlWgNQD44BvAKDjgHoe5A9GaAyFUD3yoFO5QOd+gW79Ak0aA15S5wAFpgDOAWWjAAXHAAUUYKoD8uhnDCYomALYndlKzASYANlWYBKOAF5WAIwgIV2BMJA5FPjhAduC5QGg5QAA5QEJrQHfowCEbQBC3QCHlQAdTRVJgGEdrO109ZxsdOCQAVxt-NFpDe3pvPzhi5zcPCO4onMA7Y0AgBMBZRMUAE0wYTABBSbAYaDLmszbWRgBtAF0OAF8IqMBI7UALRUAANMAYf8AAc0ByTXTAKDlABTSObCJVeABlTHRCgE9GNwAbngfHAAIwABgO-EAC8ZyDpQCA2BCqPCAbZtANHqHBgPzAeAAqkhKAikSjyAAVVggslwUCoJDjVTwxHI4DkZDfKBwPGsYxcuC6Gr04AkJDAcZQuCAMCVAK4ZgAPTB7pZ6veCCyykZBTYFwNQ-JDYODkRTU2nAemMvSWEqqXRhH5rJkk1m25jURR4mkgOkMrmE4ks8h0Qo1KBIMk41kUl2KRger2M20cZh6RSYMAIXRk13cF7EMi6Qi5ijFWyFNCqcnMDbgra0PFMKOeBx+0mbLaU1icbPK9jKNSaQy0ApFKy2VS0SbTOapxac3a+OA5kikXra1S6-XoQXYZxERCoawz8oISq6Wr1NDz8G0VxqGCBlp4xsO-2tjuKPr8QD+CYBZRUAX4qABudAG9rQAq-UAeudzkAUNjAHH4pIckAaTlADgVQBSo0ATFT30QdB9AqPBWE+b5sX+VwgW8TtuDImAlARAB3apgBogBRKAESgPQAHJAxwJQ4BsTAQD3NApmgOBsNUVjPHQ-Z0JzN4LBHOx5yHYs7CPSpr1ve9xLIhdu2aedMCozAEHgVMEAtOTVHE9CQngUVPV0Vt522FcPzgQAgzUAHPNAA34wBIc0SaVzmkeR0IQTC9BUDQtAMIxaEtUdPBI9DuFs+AQX0wz4CMgTD2wuAAGowSaIxNLIyStKiQAfo0AUuNAGW-dyEkAd1jABX4wA9tXQwwYGDJA4AnWZ5kPZpPAAOhzbApj0ZLitKuB2s6-iD2gPRxMk6T4CHd4ZyMeczKtXQ2Fkgp3gQAAvKozwaWd7SJZkUUG5pgiBPRSMWaZXF0CEr0UN4tGtOANnQ0itIQcY3qzLTqhLXRWK+wxQVYiTQe4AGyKB3QACYEbIpAIbgKGNtRuGtN2DGke4FG4AAZgxpLsdxrRyYJkrFB2XZLJWuBoeAABJb0QVVTB1Sx1A9DWjax3YfJCiUn6VNOupzvtJGZpDcWwf24BDpOsocoAH21uBwW8fLQQkxQicUcL+2AKKxdiuwEsB0KAEIBpVsGla6mAoBqYATa093pqMQaOdUQaQiQUgKN8HwQVtkxBrVdXjp97gze4HqpwWJZ9F09pmiD0XBp4sA9A53xWA5wagfivZPCAA" target="_blank" rel="nofollow noopener noreferrer">Typescript playground</a> 上体验，代码也可以在我的 <a href="https://github.com/HelKyle/unpaginate/blob/main/src/index.ts" target="_blank" rel="nofollow noopener noreferrer">github</a> 上找到。</p>
<h3 data-id="heading-7">Ending</h3>
<p>这篇文章通过一步步介绍如何使用泛型为一个通用方法实现类型声明，希望看完之后对你有所帮助。对 Typescript 还不太熟悉的同学可以看我之前写的另一篇文章<a href="https://juejin.cn/post/6876981358346895368" target="_blank">《结合实例学习 Typescript》</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            