
---
title: '鹅厂最新黑科技：两分钟一键迁移Github Pages'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09d6ed21367d4004a08cbff6d36fb393~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 00:09:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09d6ed21367d4004a08cbff6d36fb393~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天我们非常荣幸地宣布腾讯云 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Fwebify" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/product/webify" ref="nofollow noopener noreferrer">CloudBase Webify</a></strong> （中文名：Web应用托管）正式上线，这是一个专为 Web 开发者打造的云上开发、部署平台，<strong>帮助开发者快速开发、预览、部署自己的 Web 应用</strong>。</p>
<p>前往 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fconsole.cloud.tencent.com%2Fwebify%2Findex" target="_blank" rel="nofollow noopener noreferrer" title="https://console.cloud.tencent.com/webify/index" ref="nofollow noopener noreferrer">Webify 快速开始页面</a>，选择自己的代码仓库，或者从现有的模板中，创建你的第一个 Web 应用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09d6ed21367d4004a08cbff6d36fb393~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0"><strong>一、Webify 想要解决什么问题？</strong></h2>
<p>对于大多数前端开发者而言，互联网的基础设施也许不那么友好。</p>
<p>例如，将一个前端项目从零开始发布上线到公网，通常需要考虑到下面的事情：</p>
<ul>
<li>申请域名，修改DNS</li>
<li>将静态资源部署到服务器，并配置 Nginx（或者放到对象存储上）</li>
<li>配置CDN</li>
<li>配置 HTTPS 证书</li>
<li>后续如果需要二次开发，还需要配置一套 CI/CD 工作流</li>
</ul>
<p>除此之外，还有大量应用层面的问题：</p>
<ul>
<li>我的单页面应用（SPA）要怎么配置路由？</li>
<li>我的 SSR 应用要怎么部署？</li>
<li>我用的框架能直接发布到云上吗？</li>
<li>我想用 Serverless 云函数写 HTTP API，要怎么处理？</li>
</ul>
<p>这些问题正是 Webify 想要解决的问题，我们期望为 Web 开发者提供一个专属的平台， 让开发者免除以上来自基础设施的烦恼，专注于 Coding，而不是管理基建。</p>
<h2 data-id="heading-1"><strong>二、Webify 提供怎样的能力？</strong></h2>
<h3 data-id="heading-2"><strong>1、从 Git 托管平台快速创建应用</strong></h3>
<p>Webify 支持从第三方代码托管平台直接创建应用，目前支持 Github、Gitlab、Gitee码云三种平台，后续我们也会放开支持更多的 Git 平台。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fconsole.cloud.tencent.com%2Fwebify%2Findex" target="_blank" rel="nofollow noopener noreferrer" title="https://console.cloud.tencent.com/webify/index" ref="nofollow noopener noreferrer">点击此处，立刻创建你的第一个 Webify 应用</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccbaafee96aa4807acb883d10a793c98~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>例如，很多开发者会使用 Hexo 框架搭建自己的个人博客，并将博客推送至 Github，使用 Github Pages 部署。</p>
<p>这些类型的个人博客也可以直接一键导入并部署到 Webify 上：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d5d1890894d48baacc8651608550900~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看 Demo：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fmy-hexo-site-0g2fpeyz0f499162-1255679239.ap-shanghai.app.tcloudbase.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//my-hexo-site-0g2fpeyz0f499162-1255679239.ap-shanghai.app.tcloudbase.com/" ref="nofollow noopener noreferrer">my-hexo-site-0g2fpeyz0f499162-1255679239.ap-shanghai.app.tcloudbase.com/</a></p>
<h3 data-id="heading-3"><strong>2、从模板快速创建应用</strong></h3>
<p>我们还为开发者提供了一系列模板，包括 Vue、React、Angular、Next.js、Gatsby.js、Docusaurus 等流行的 Web 框架。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d51c8cf734674e77a9ef00d2da8ba74a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发者可以选取任意模板，然后使用模板创建一个新的代码仓库：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6a55d919e34837958069bc644d56e0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>随后只需要把变更推送至代码仓库，便可以<strong>自动触发应用的重新构建和部署</strong>。</p>
<h3 data-id="heading-4"><strong>3、基于 Git 的持续发布（CD）工作流</strong></h3>
<p>在 CloudBase Webify 中，每个应用都可以与一个 Git 代码仓库绑定。<strong>绑定后，代码仓库上相应分支的任何提交，都会触发应用的构建及部署。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bc1ab135e464c4aa1c9dbc99db3c66a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发者可以基于此特性搭建自己的 Git 工作流：</p>
<p>例如，将应用与仓库的 master 分支进行绑定，平时采用 dev 分支进行开发，那么在发布新版应用时，只需要将 dev 分支合入 master 分支，便可以全自动构建及发布应用，无需任何手工流程，也无需集成任何第三方 CI/CD 系统。</p>
<h3 data-id="heading-5"><strong>4、域名与 CDN</strong></h3>
<p>Webify 为每个 Web 应用提供独有的默认域名，默认域名以 <code>.app.tcloudbase.com</code> 为后缀，开发者可以使用默认域名直接访问应用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4832219beffd4460be32520e97a6b64e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>应用也支持绑定开发者自己的域名，在应用配置页面中可以直接进行操作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9813476f136c4a30aee7096096e63e26~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>无论是默认域名还是绑定的自定义域名，均<strong>默认带有 CDN 加速能力</strong>，最大程度加速 Web 应用的加载性能。</p>
<h2 data-id="heading-6"><strong>三、Webify 还有能力在筹划中？</strong></h2>
<h3 data-id="heading-7"><strong>筹划能力1：边缘路由</strong></h3>
<p>对于单页面应用（SPA）、服务端渲染（SSR）、Serverless 等较为复杂的 Web 应用场景，开发者通常需要进行服务端路由的配置</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd064b25b9354cf1a0d680d9743becf9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们正在筹划边缘路由能力，开发者可以在应用的根目录下放置一份路由配置文件，配置应用的路由逻辑，例如：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-comment">// 路由配置</span>
  <span class="hljs-attr">routes</span>: [&#123;
    <span class="hljs-comment">// 单页应用（SPA），需要对所有路由都响应 index.html，由前端接管路由</span>
    <span class="hljs-attr">src</span>: <span class="hljs-string">'*'</span>,
    <span class="hljs-attr">static</span>: <span class="hljs-string">'dist/index.html'</span> 
  &#125;, &#123;
    <span class="hljs-comment">// 将 /api/query 指向到某个云函数</span>
    <span class="hljs-attr">src</span>: <span class="hljs-string">'/api/query'</span>,
    <span class="hljs-attr">cloudFunction</span>: &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'api/query.js'</span> &#125;
  &#125;],
  
  <span class="hljs-comment">// HTTP错误码重写</span>
  <span class="hljs-attr">errorOverrides</span>: [
    &#123; <span class="hljs-attr">status</span>: <span class="hljs-number">404</span>, <span class="hljs-attr">static</span>: <span class="hljs-string">'dist/404.html'</span> &#125;, <span class="hljs-comment">// 对 404 错误返回 dist/404.html</span>
    &#123; <span class="hljs-attr">status</span>: <span class="hljs-number">401</span>, <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/login'</span> &#125; <span class="hljs-comment">// 将 401 状态码重定向到 /login</span>
  ],
  
  <span class="hljs-comment">// 自定义 HTTP 响应头</span>
  <span class="hljs-attr">globalHeaders</span>: &#123;
    <span class="hljs-string">'x-my-custom-header'</span>: <span class="hljs-string">'xxxxxx'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（以上只是初期设计，具体使用方式以实际上线后的技术文档为准）</p>
<h3 data-id="heading-8"><strong>筹划能力2：免费HTTPS证书</strong></h3>
<p>目前应用绑定自定义域名时，需要手工选择已有 HTTPS 证书。</p>
<p>我们正在计划为 Webify 应用的自定义域名，提供免费的 DV 型证书，并提供自动续期功能，免除开发者手工申请、维护、续期证书的烦恼。</p>
<h3 data-id="heading-9"><strong>筹划能力3：Serverless HTTP API</strong></h3>
<p>开发一个高可用、能应对高流量的后端 API，对于一些前端开发者而言并不简单，而近年来兴起的 Serverless 技术正是解决这一问题的绝佳方法。</p>
<p>Webify 正在筹划支持 Serverless HTTP API，开发者只需要在项目的 <code>api</code> 目录下，添加对应的路由处理代码，即可直接部署一个云上 Serverless 化的 HTTP API（基于云托管或云函数）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// api/hello.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handler</span>(<span class="hljs-params">req, res</span>) </span>&#123;
  res.send(<span class="hljs-string">`<span class="hljs-subst">$&#123;req.params.name&#125;</span> 的第一个 Webify Serverless API !`</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应用部署后，即可直接访问：</p>
<pre><code class="hljs language-bash copyable" lang="bash">> curl https://<AppName>.<Region>.app.tcloudbase.com/api/hello?name=CloudBase
> CloudBase 的第一个 Webify Serverless API !
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（以上只是初期设计，具体使用方式以实际上线后的技术文档为准）</p>
<p>Serverless API 中，开发者可以直接使用云开发 CloudBase 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cloudbase.net%2Fapi-reference%2Fserver%2Fnode-sdk%2Fintroduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cloudbase.net/api-reference/server/node-sdk/introduction.html" ref="nofollow noopener noreferrer">服务端 SDK</a>，直接调用云数据库、云存储等云开发提供的 BaaS 能力：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// api/query.js</span>
<span class="hljs-keyword">const</span> cloudbase = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@cloudbase/node-sdk'</span>)
cloudbase.init()
​
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handler</span>(<span class="hljs-params">req, res</span>) </span>&#123;
  <span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> cloudbase.database()
    .where(&#123;
      <span class="hljs-attr">name</span>: req.params.name
    &#125;)
    .get()
  res.send(data.result)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10"><strong>筹划能力4：更多的框架集成，包括 SSR、ISR、JAMStack</strong></h3>
<p>目前 Webify 集成了 React、Vue 等基础的静态 Web 框架，以及主流的静态网站生成器（Static Site Generator, SSG）如 Gatsby.js、Next.js 等.</p>
<p>我们后续也正在考虑集成更多更加复杂的 Web 技术栈或者框架，例如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnextjs.org%2Fdocs%2Fbasic-features%2Fdata-fetching%23incremental-static-regeneration" target="_blank" rel="nofollow noopener noreferrer" title="https://nextjs.org/docs/basic-features/data-fetching#incremental-static-regeneration" ref="nofollow noopener noreferrer">Next.js SSR/ISR</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F281085404" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/281085404" ref="nofollow noopener noreferrer">JAMStack</a> 等，方便开发者基于这些集成的框架，快速开发、预览并部署自己的 Web 应用。</p>
<h2 data-id="heading-11">四、尾声</h2>
<p>CloudBase Webify 专为前端、Web开发者打造，集成了诸多流行的前端框架，与开源社区生态深度融合，我们希望能够为国内的开发者提供标准、高效、对开发者友好的一站式Web开发部署平台， 未来我们也会持续优化产品，提供更多的产品能力，包括 Serverless、预览、免费SSL证书等能力，敬请期待。</p></div>  
</div>
            