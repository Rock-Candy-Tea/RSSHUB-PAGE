
---
title: '_重学 Next.js_  — 你应该知道的 Next.js 高级技巧 10 点 （下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d97057f0f9de4d579552cd71e50a450f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 05:00:26 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d97057f0f9de4d579552cd71e50a450f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>上一篇文章 <a href="https://juejin.cn/post/6999966838780067853" target="_blank" title="https://juejin.cn/post/6999966838780067853">[重学 Next.js]  — 你应该知道的 Next.js 高级技巧 10 点 （上）</a> 进行了 Next.js 高级用法的前五点，今天我们来说说剩下的五点，可谓是一个比一个有用，以后在 Next.js 开发过程中都会有极大的帮助。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2Fblog%2F10-next-js-tips-you-might-not-know" target="_blank" rel="nofollow noopener noreferrer" title="https://vercel.com/blog/10-next-js-tips-you-might-not-know" ref="nofollow noopener noreferrer">原文链接</a></p>
<h2 data-id="heading-1">VI - Absolute Imports and Module Path Aliases - 模块路径导入</h2>
<p>这一点毋庸置疑，大部分人平时在自己搭建项目的时候，也会通过各种复杂的配置比如 Webpack alias/Babel 等进行配置，配置的好处就是：</p>
<ul>
<li>原来的代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">"../../../components/button"</span>;
<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">"../../../utils/request"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>新的代码</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">"@/components/button"</span>;
<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">"@/utils/request"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做并不是强制性的，看开发者的个人习惯，但是这样做有两点好处：</p>
<ul>
<li>
<p>使用简单，再也不用去费劲吧啦的去数相对路径有几层了</p>
</li>
<li>
<p>如果某天你的相对路径层级发生了变化，也不需要去手动修复，因为它看起来就和绝对路径一样</p>
</li>
</ul>
<h3 data-id="heading-2">示例代码</h3>
<p>那么在 Next.js 里，这个功能是如何简单的进行配置实现呢？</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"."</span>,
    <span class="hljs-attr">"paths"</span>: &#123;
      <span class="hljs-attr">"@/*"</span>: [<span class="hljs-string">"src/*"</span>]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两个配置就是核心的配置，真的是非常简单，配置过后的效果，如下图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d97057f0f9de4d579552cd71e50a450f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果你使用的是 TS，那么对应修改的就是 <code>tsconfig.json</code>， 如果你使用的是 JS，那么对应修改的就是 <code>jsconfig.json</code>。</p>
</blockquote>
<h2 data-id="heading-3">VII - CRUD API Routes —— 动态 API 路由</h2>
<blockquote>
<p><strong>【版本】：</strong> >= Next.js Version 9.1.4</p>
<p><strong>【功能】：</strong> 动态 API 路由。</p>
<p><strong>【解释】：</strong> 动态 API 路由扩展了 Next.js 框架自身的能力，更为方便的做 node 层处理以及不需要任何改造就能实现一个全栈框架。</p>
</blockquote>
<p>动态路由 API 的出现，算是 Next.js 浓墨重彩的一笔，官方给的是名称是 Dynamic API Route，但是其实如果你是一个 Next.js 的入门使用者，你其实可能也不知道这东西到底能干啥，这里使用的词是 CURD API Routes，就从 CURD 这个角度，来给大家简单看看这个功能的强大之处。</p>
<h3 data-id="heading-4">示例代码1 - 最简单的 GET 数据</h3>
<p>这里没有链接数据库，简单的构造了一下数据：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> users = [];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">126</span>; i++) users.push(i);

<span class="hljs-keyword">const</span> data = <span class="hljs-built_in">Array</span>.from(users, <span class="hljs-function">(<span class="hljs-params">item</span>) =></span> (&#123;
  <span class="hljs-attr">id</span>: item,
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">60</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">`luffy-<span class="hljs-subst">$&#123;++item&#125;</span>`</span>,
  <span class="hljs-attr">email</span>: <span class="hljs-string">`luffy-<span class="hljs-subst">$&#123;++item&#125;</span>@126.com`</span>,
&#125;));

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> data;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后使用 Next.js API 路由来编写一个接口：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/pages/api/user/list</span>

<span class="hljs-keyword">import</span> type &#123; NextApiRequest, NextApiResponse &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'next'</span>
<span class="hljs-keyword">import</span> users <span class="hljs-keyword">from</span> <span class="hljs-string">'@/data/user'</span>;

type IUserData = &#123;
  <span class="hljs-attr">id</span>: number,
  <span class="hljs-attr">age</span>: number,
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">email</span>: string,
&#125;


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sleep</span>(<span class="hljs-params">time: number</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">setTimeout</span>(resolve, time))
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handler</span>(<span class="hljs-params">
  req: NextApiRequest,
  res: NextApiResponse<IUserData[]>
</span>) </span>&#123;
  <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">3000</span>);
  res.status(<span class="hljs-number">200</span>).json(users);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>非常简单就是把我们的构造数据返回，我们可以来调用一下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1897ce720ca450295c1a233b668cfc9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，接口正常返回数据了，然后我们在页面里获取一下然后渲染。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Table &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> swr <span class="hljs-keyword">from</span> <span class="hljs-string">'swr'</span>;

<span class="hljs-keyword">const</span> columns = [
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'ID'</span>,
    <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'id'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">'id'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'姓名'</span>,
    <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'name'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">'name'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'年龄'</span>,
    <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'age'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">'age'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'邮箱'</span>,
    <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'email'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-string">'email'</span>,
  &#125;,
];

<span class="hljs-keyword">const</span> fetcher = <span class="hljs-function">(<span class="hljs-params">url: string</span>) =></span> fetch(url).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> res.json()).then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> data);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">UserList</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data, error &#125; = swr(<span class="hljs-string">'/api/user/list'</span>, fetcher)
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Table</span>
      <span class="hljs-attr">rowKey</span>=<span class="hljs-string">"id"</span>
      <span class="hljs-attr">loading</span>=<span class="hljs-string">&#123;!data&#125;</span>
      <span class="hljs-attr">dataSource</span>=<span class="hljs-string">&#123;data&#125;</span>
      <span class="hljs-attr">columns</span>=<span class="hljs-string">&#123;columns&#125;</span>
    /></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个非常简单的页面，展示用户列表，看一下实际效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/963ab503c88542ef9a5cbe4eb8aece23~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-25 16.14.05.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面就是一个简单的数据流程，mock api -> 获取数据 -> 渲染页面，最主要的是这一切都闭环在 Next.js 项目里，你不需要去其他网站或者平台，真的很方便。</p>
<h3 data-id="heading-5">示例代码2 - CURD</h3>
<p>上面是一个简单的 GET api 请求，既然是 CURD，那么肯定是不仅仅一个 GET 这么简单，这里再通过一小段代码，来给大家看看强大的 Next.js CURD API Routes。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// Next.js API route support: https://nextjs.org/docs/api-routes/introduction</span>
<span class="hljs-keyword">import</span> type &#123; NextApiRequest, NextApiResponse &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'next'</span>
<span class="hljs-keyword">import</span> users <span class="hljs-keyword">from</span> <span class="hljs-string">'@/data/user'</span>;

type IUserData = &#123;
  <span class="hljs-attr">id</span>: number,
  <span class="hljs-attr">age</span>: number,
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">email</span>: string,
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sleep</span>(<span class="hljs-params">time: number</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">setTimeout</span>(resolve, time))
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handler</span>(<span class="hljs-params">
  req: NextApiRequest,
  res: NextApiResponse<IUserData[] | any>
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (req.method === <span class="hljs-string">'PUT'</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'req.body: '</span>, req.body);
    res.status(<span class="hljs-number">200</span>).json(&#123; <span class="hljs-attr">message</span>: <span class="hljs-string">`PUT 请求接受成功，请求的 body 数据是 <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(req.body)&#125;</span>`</span> &#125;);
  &#125;

  <span class="hljs-keyword">if</span> (req.method === <span class="hljs-string">'GET'</span>) &#123;
    <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">1000</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'req.query: '</span>, req.query);
    res.status(<span class="hljs-number">200</span>).json(users.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.id === +req.query.id));
  &#125;

  <span class="hljs-keyword">if</span> (req.method === <span class="hljs-string">'POST'</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'req.body: '</span>, req.body);
    res.status(<span class="hljs-number">200</span>).json(&#123; <span class="hljs-attr">message</span>: <span class="hljs-string">`POST 请求接受成功，请求的 body 数据是 <span class="hljs-subst">$&#123;req.body&#125;</span>`</span> &#125;);
  &#125;

  <span class="hljs-keyword">if</span> (req.method === <span class="hljs-string">'DELETE'</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'req.body: '</span>, req.body);
    res.status(<span class="hljs-number">200</span>).json(&#123; <span class="hljs-attr">message</span>: <span class="hljs-string">`DELETE 请求接受成功，想要删除的数据是 <span class="hljs-subst">$&#123;req.body&#125;</span>`</span> &#125;);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面就是一个简单的增删改查 CURD API ROUTES，是不是非常的简单？也来看一下效果如何：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/977b774288ea42fbb477be2d01d6ac69~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-25 19.40.00.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面两个例子相信大家很容易就能发现这个功能的强大之处，Next.js CURD API 我这边简单总结的话有如下几点好处：</p>
<ul>
<li>
<p>开发中可以模拟真实的数据交互流程而不用自己虚假的构造数据</p>
</li>
<li>
<p>Mock 数据打通 API 接口很方便，场景也更真实</p>
</li>
<li>
<p>有了这个 API，Next.js 基本上是无缝切换全栈</p>
</li>
<li>
<p>更多需要大家使用过程中自己去体会...</p>
</li>
</ul>
<h2 data-id="heading-6">VIII - Setting Response HTTP Caching Headers —— 设置 HTTP 请求缓存头</h2>
<p>这个理解起来就很简单了，Next.js 其实一直在做的就是静态增量，对于静态页面以及资源来说，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2Fdocs%2Fedge-network%2Foverview" target="_blank" rel="nofollow noopener noreferrer" title="https://vercel.com/docs/edge-network/overview" ref="nofollow noopener noreferrer">Vercel Edge Network</a> 将自动 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2Fdocs%2Fedge-network%2Fcaching" target="_blank" rel="nofollow noopener noreferrer" title="https://vercel.com/docs/edge-network/caching" ref="nofollow noopener noreferrer">缓存</a> 静态资产，以便尽快提供数据。不过当需要使用 API 路由或服务器端渲染页面时，开发者需要手动设置一个<code>Cache-Control</code>头部来缓存这些资源。</p>
<h3 data-id="heading-7">示例代码</h3>
<p>下面代码，将对应的 json 响应换存在 Vercel 服务器一天。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handler</span>(<span class="hljs-params">
  req: NextApiRequest,
  res: NextApiResponse<IUserData[]>
</span>) </span>&#123;
  res.setHeader(
    <span class="hljs-string">'Cache-Control'</span>,
    <span class="hljs-string">'s-maxage=86400'</span>
  );
  res.status(<span class="hljs-number">200</span>).json(users);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果大家平时自己使用 Next.js 开发，更建议大家用 Vercel 部署，毕竟生态都是一体的，优化得更好。</p>
</blockquote>
<h2 data-id="heading-8">IX - Shared Component Attributes —— 共享组件属性</h2>
<p>关于这个概念，其实很多框架都在做，也确实是方便了开发者，举个最简单的例子来说明<strong>共享组件属性</strong>。</p>
<h3 data-id="heading-9">示例代码</h3>
<ul>
<li>没有/不使用共享组件之前</li>
</ul>
<pre><code class="copyable">// pages/list.tsx

import Head from 'next/head';

export default function List() &#123;
  return (
    <>
      <Head>
        <title>列表页</title>
        <meta name="description" content="我是列表页的描述" />
      </Head>
      我是列表页面，路径是 /list
    </>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用共享组件后</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// pages/list.tsx</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">List</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      我是列表页面，路径是 /list
    <span class="hljs-tag"></></span></span>
  );
&#125;

List.title = <span class="hljs-string">'列表页'</span>;
List.description = <span class="hljs-string">'我是列表页的描述'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// pages/_app.tsx</span>

<span class="hljs-keyword">import</span> type &#123; AppProps&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'next/app'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyApp</span>(<span class="hljs-params">&#123; Component, pageProps &#125;: AppProps</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">Head</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>&#123;Component.title || 'Next App'&#125;<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">&#123;Component.description</span> || ''&#125; /></span>
      <span class="hljs-tag"></<span class="hljs-name">Head</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Component</span> &#123;<span class="hljs-attr">...pageProps</span>&#125; /></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MyApp

<span class="copy-code-btn">复制代码</span></code></pre>
<p>仔细一看，感觉没方便啥样，但是我举的例子只是一个组件，当你的系统有几十个几百个页面的时候，这种方式的便利性就体现出来了，大家可以仔细对比思考一下。最后效果就是如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a707942acd349ca860415a498b49bb7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">X - Next.js Mobile Applications? —— 基于 Next.js 的移动端应用</h2>
<p>是的你没看错，就是带着一个问号，但是我觉得已经是一个肯定的结论了，在跨端框架盛行的今天，RN、Flutter 等框架为前端赋能，同时 Next.js 也在跨端这条路上开始行自己的路了，比如接下来要介绍的 —— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcapacitorjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://capacitorjs.com/" ref="nofollow noopener noreferrer">CapacitorJS</a>，感谢 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftwitter.com%2Fmaxlynch" target="_blank" rel="nofollow noopener noreferrer" title="https://twitter.com/maxlynch" ref="nofollow noopener noreferrer">Ionic</a> 团队，他们创建了 CapacitorJS 让我们可以使用 Next.js 构建类似移动端应用的体验，这是一个可以在手机上为您提供原生体验的库。</p>
<p>因为我也没有过多的研究过，所以在这里就简单的照葫芦画瓢给大家跑一个 Demo 看看。</p>
<h3 data-id="heading-11">示例代码</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmlynch%2Fnextjs-tailwind-ionic-capacitor-starter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mlynch/nextjs-tailwind-ionic-capacitor-starter" ref="nofollow noopener noreferrer">官方仓库</a></p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 打包编译</span>
yarn install
yarn build
yarn <span class="hljs-built_in">export</span>

<span class="hljs-comment"># 运行 IOS APP</span>
npx <span class="hljs-built_in">cap</span> sync
npx <span class="hljs-built_in">cap</span> run ios

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我这边是运行的是 IOS APP，选择的模拟器是 iPhone11，启动项目后效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72dafcb60ec8495ca56995917e9f6ae4~tplv-k3u1fbpfcp-watermark.image" alt="2021-08-25 20.51.06.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官方的架构原理图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96215ab5c98946778c2c4f3054e7b00a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总的来说，开发模式基本上就是 Next.js 的开发模式，使用体验上也还 OK，个人觉得可以尝试玩玩。</p>
<h2 data-id="heading-12">总结</h2>
<p>算是个人重新开始用 Next.js 的第一次输出文章，后面决定深入 Next.js，希望能跟大家分享更多关于 Next.js 的文章，感兴趣可以加交流群，随时沟通，有问必答～</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45f237daf43f4008b7efcf120bd5379b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            