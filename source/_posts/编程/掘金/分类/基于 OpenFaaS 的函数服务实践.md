
---
title: '基于 OpenFaaS 的函数服务实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb47368904a461ea046e6f1687e335b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 00:46:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb47368904a461ea046e6f1687e335b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">内容摘要</h1>
<p>随着云计算的发展，业务系统的服务模型也在不断演变。本文主要是通过讲述团队在过去一段时间不断探索 BFF 开发模式的历程，分享我们在新的业务场景中通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.openfaas.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.openfaas.com" ref="nofollow noopener noreferrer">OpenFaaS</a> 建设团队自有函数服务的实践经验以及底层原理。</p>
<h1 data-id="heading-1">背景</h1>
<p>首先通过一张图来简要回顾一下云服务的几种模式。这里就不再赘述各个模式的概念，通过这张图我们可以清晰地看出从 IaaS 到 FaaS，开发者需要关心的东西是越来越少的，其本质就是在不断帮助我们减少运维成本、提高研发效率。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bb47368904a461ea046e6f1687e335b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前虽然团队很多业务服务仍然是基于 IaaS 部署的，但是我们也在逐步跟随时代潮流去实践新的开发模式。下面先简单介绍一下团队在不同阶段所采用的一些技术方案。</p>
<h2 data-id="heading-2">前后端分离</h2>
<p>几年前，在业务高速发展时期，部门为了提升前后端的合作效率，决定由前端团队接手 Java Web 应用，负责接口聚合、模板渲染等工作，而几个后端团队则专注于业务流程及数据处理，并提供 RPC 服务。前端当时虽然对应用代码进行了重构，但部署方式仍然是沿用了原有模式，通过 CentOS 虚拟机自行搭建服务器，在不同机房一共部署了 8 台 8U16G 的虚拟机。</p>
<p>不支持在 Docs 外粘贴 block</p>
<p>这种方式相比传统模式还是有很大优点的，团队分工明确，前端接口和展现可以自给自足。缺点是对前端同学来说，运维成本直线上升，在上线、回滚、扩容、迁移等环节均需要人工介入，耗时耗力。这个阶段的关键词可以概括为：虚拟机、人工运维。</p>
<h2 data-id="heading-3">微服务</h2>
<p>随着业务的快速发展，后端逐步演变为微服务架构。而前端的 Java BFF 应用则逐渐膨胀为一个庞大的单体应用，接口和页面的数量多达几百个，迫切需要一种更为灵活高效的开发模式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/713e393cc5c14f6da085f797e529c15a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过一段时间的探索，我们基于业界的一些技术理念及最佳实践，将原有的 Java BFF 逐步改造成了 Node.js + Docker 的研发模式。后续又将 Web 应用拆分为多个微前端子应用，从而大大降低了系统的复杂性和耦合度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ae1f189e3f04e028442aac1ef2a96db~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前这种方式是线上运行的主要模式，在开发效率和运维成本上都能够基本满足团队的需求。这个阶段的关键词可以概括为：微服务、容器。</p>
<h2 data-id="heading-4">云原生</h2>
<p>随着云技术的发展，像 K8S、Service Mesh、Serverless、FaaS 等技术概念开始出现在我们视野中，弹性扩缩容、低运维成本等特性对现有的开发模式带了新的冲击。</p>
<p>由于公司基础设施还在逐步建设中，因此前端团队开始自行探索 Serverless 模式在业务落地的可行性。经过调研对比 OpenFaaS、KNative、OpenWhisk 等开源框架后，最终我们决定采用 OpenFaaS 在公司提供的 K8S 集群上搭建自己的函数服务，随后在工具服务、小程序接口、周边业务接口等多个场景进行了实践。</p>
<p>不支持在 Docs 外粘贴 block</p>
<p>虽然短期维护 OpenFaaS 确实需要一定人力成本，但是灵活的开发模式也大大提高了团队迭代的效率。而且后续也可以逐步迁移至公司建设的 FaaS 平台上。</p>
<h1 data-id="heading-5">函数服务实践</h1>
<p>下面分享一下我们在搭建及实践 OpenFaaS 服务的一些经验。</p>
<h2 data-id="heading-6">搭建 OpenFaaS 服务</h2>
<p>核心的前置依赖就是需要有一个 K8S 集群 + 私有 Docker 镜像仓库。得益于 K8S 的 Helm 包管理工具，搭建的步骤跟 <code>npm install</code> 一样简单，当然各种配置过程中踩坑是不可避免的，需要自行解决。下图是安装成功后，OpenFaaS 运行的核心服务及容器实例。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf95830a8d64491a8871e55a58a96f1f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f975b5789c94322aa3bf3967abd15ba~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">业务实践</h2>
<p>实际业务开发中，只需要安装 OpenFaaS <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fopenfaas%2Ffaas-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/openfaas/faas-cli" ref="nofollow noopener noreferrer">官方</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fopenfaas%2Ffaas-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/openfaas/faas-cli" ref="nofollow noopener noreferrer">CLI 工具</a>，同时登录到公司内网 Docker Registry，就可以正式开发了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62e0e0aa2a524e089fe5500f48ff7bd4~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官方支持 go/python/node 等语言模板，也支持任意自定义 Dockerfile，下面分享一下我们在项目中的实际应用。</p>
<h3 data-id="heading-8">工具服务</h3>
<p>一般通用的工具型服务都可以通过直接引入开源的第三方库来快速实现，例如拼音转换、简繁转换等功能。下面的示例通过 3 行 python 代码快速实现了一个极简版的拼音转换函数：</p>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-comment"># handler.py</span>

<span class="hljs-keyword">import</span> pinyin

<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">handle</span>(<span class="hljs-params">req</span>):</span>
    <span class="hljs-keyword">return</span> pinyin.get(<span class="hljs-built_in">str</span>(req), <span class="hljs-built_in">format</span>=<span class="hljs-string">"strip"</span>, delimiter=<span class="hljs-string">" "</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 CLI 发布之后，我们的服务就相当于完成了部署。省去了申请资源、安装依赖、配置服务等一系列过程。简单测试一下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5933b41683f2432893727ff000a17b6a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>工具型的服务都比较离散，逻辑也比较简单。下面以小程序接口为例介绍一下业务模块的开发模式。</p>
<h3 data-id="heading-9">小程序接口</h3>
<p>为了满足业务需求，我们基于公司 IM 快速开发了一个系统对应的小程序版本。由于功能不多，所需要的接口仅十余个，且核心业务逻辑与 Web 端相同。为了降本提效，我们放弃了 Nest BFF 的研发模式，转而采用多个函数的方式组织 API 服务。该服务的目录结构及描述文件大致如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">mobile
├── <span class="hljs-built_in">functions</span>
│   ├── notice                 <span class="hljs-comment"># 通知接口</span>
│   │   ├── handler.js
│   │   └── package.json
│   └── search                 <span class="hljs-comment"># 搜索接口</span>
│       ├── handler.js
│       └── package.json
└── mobile.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-comment"># file: mobile.yml</span>

<span class="hljs-attr">version:</span> <span class="hljs-number">1.0</span>
<span class="hljs-attr">provider:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">openfaas</span>
  <span class="hljs-attr">gateway:</span> <span class="hljs-string">https://openfaas.demo.domain</span>
<span class="hljs-attr">functions:</span>
  <span class="hljs-attr">m-search:</span>
    <span class="hljs-attr">lang:</span> <span class="hljs-string">node12</span>
    <span class="hljs-attr">handler:</span> <span class="hljs-string">./functions/search</span>
    <span class="hljs-attr">image:</span> <span class="hljs-string">docker.demo.domain/mobile-search:latest</span>
    <span class="hljs-attr">secrets:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">docker-auth</span>
  <span class="hljs-attr">m-notice:</span>
    <span class="hljs-attr">lang:</span> <span class="hljs-string">node14</span>
    <span class="hljs-attr">handler:</span> <span class="hljs-string">./functions/notice</span>
    <span class="hljs-attr">image:</span> <span class="hljs-string">docker.demo.domain/mobile-notice:latest</span>
    <span class="hljs-attr">secrets:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">docker-auth</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认可以通过 CLI 批量发布，由于每个函数本质上是一个单独的镜像，因此是可以参数单独进行发布。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 单独部署 Search 函数</span>
faas up --filter <span class="hljs-string">"*search"</span> -f mobile.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">函数开发</h4>
<p>函数代码的写法比较简洁，与大多数函数平台的开发模式相似，也可以根据需求安装第三方依赖。此外，为了满足开发测试的需求，一般第三方服务的 URL/Token 等信息都通过环境变量来指定。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">'axios'</span>);

<span class="hljs-comment">// 通过环境变量指定 API 地址</span>
<span class="hljs-keyword">const</span> API_URL = process.env.API_URL;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">async</span> (event, context) => &#123;
  <span class="hljs-keyword">const</span> &#123; q &#125; = event.query;
  <span class="hljs-keyword">const</span> response = <span class="hljs-keyword">await</span> axios.get(API_URL, &#123;<span class="hljs-comment">/* options */</span>&#125;);
  
  <span class="hljs-comment">/* process stuff */</span>

  <span class="hljs-keyword">return</span> context.status(<span class="hljs-number">200</span>).succeed(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">用户鉴权</h4>
<p>由于小程序版本的接口需要开放公网访问，并且有单独的权限控制，我们的做法是将其封装为一个单独的 NPM 包，然后导出为一个高阶函数来完成鉴权操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mobileAuth = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@internal/mobile-auth'</span>);

<span class="hljs-keyword">const</span> handler = <span class="hljs-keyword">async</span> (event, context) => &#123;
  <span class="hljs-keyword">const</span> &#123; user, token &#125; = event.auth;
  
  <span class="hljs-comment">/* process stuff */</span>

  <span class="hljs-keyword">return</span> context.status(<span class="hljs-number">200</span>).succeed(data);
&#125;

<span class="hljs-built_in">module</span>.exports = mobileAuth(handler);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">调用其他函数</h4>
<p>实际业务场景中，函数之间也有互相调用的场景。在 OpenFaaS 中，可以直接通过内部网关 <code>gateway.openfaas</code> 进行调用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">'axios'</span>);
<span class="hljs-keyword">const</span> faas = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: <span class="hljs-string">'http://gateway.openfaas:8080/function/'</span>
&#125;);

<span class="hljs-built_in">module</span>.exports = <span class="hljs-keyword">async</span> (event, context) => &#123;
  <span class="hljs-keyword">const</span> &#123; q &#125; = event.query;
  <span class="hljs-keyword">const</span> pinyin = <span class="hljs-keyword">await</span> faas.post(<span class="hljs-string">'/pinyin'</span>, <span class="hljs-comment">/* data */</span>);
  
  <span class="hljs-comment">/* process stuff */</span>

  <span class="hljs-keyword">return</span> context.status(<span class="hljs-number">200</span>).succeed(data);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">底层原理分析</h1>
<p>实践的过程也是一次很好的学习机会。下面我们简要介绍一下 OpenFaaS 的一些整体架构及底层原理。</p>
<h2 data-id="heading-14">整体技术栈</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05cbaabe06e44abcafc58394e91f49e1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>OpenFaas 整体框架底层基于 K8S 及 Docker，通过 Gateway 组件对外提供服务，同时集成了 Prometheus 及 NATS 等服务用于实现自动扩缩容等功能。平台层面，官方提供了 OpenFaaS Cloud 用于集成研发流程，可以对接至 Github/Gitlab 等代码托管平台。</p>
<h2 data-id="heading-15">抽象服务流程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9609c2ef50c44e50b8c5e658fb522a53~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图是 OpenFaaS 的抽象服务流程，下面是各个节点的简单介绍：</p>
<ul>
<li>Gateway：HTTP 网关，用于接收用户请求及内部指令。</li>
<li>NATS Streaming：用于异步执行函数。</li>
<li>Prometheus / AlertManager：用于收集服务指标及扩缩容操作。</li>
<li>faas-netes：针对 K8S 的 Provider，可以定制其他的 Provider 例如 Docker Swarm 等。</li>
<li>Docker Registry：用于拉取函数镜像的仓库。</li>
</ul>
<h2 data-id="heading-16">自动扩缩容</h2>
<p>自动扩缩容是 FaaS 的核心特性。OpenFaaS 的扩容流程可以总结如下：</p>
<ol>
<li>AlertManager 根据监控指标触发扩容动作；</li>
<li>Gateway 向 FaaS Netes 发起创建容器请求；</li>
<li>K8S 寻找合适的节点；</li>
<li>拉取镜像；</li>
<li>启动容器实例。</li>
</ol>
<p>优化思路：</p>
<ul>
<li>减少镜像大小。</li>
<li>在节点上预拉取镜像。</li>
<li>有规律的流量可以按照规则提前扩容。</li>
</ul>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-comment"># file: mobile.yml</span>

<span class="hljs-attr">functions:</span>
  <span class="hljs-attr">m-search:</span>
    <span class="hljs-attr">labels:</span>
      <span class="hljs-attr">com.openfaas.scale.min:</span> <span class="hljs-number">1</span>
      <span class="hljs-attr">com.openfaas.scale.max:</span> <span class="hljs-number">20</span>
      <span class="hljs-attr">com.openfaas.scale.factor:</span> <span class="hljs-number">20</span>
      <span class="hljs-attr">com.openfaas.scale.zero:</span> <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">Watchdog</h2>
<p>官方默认的函数模板中，每个容器实例中都有一个 Watchdog 进程，用于代理 Gateway 的请求，并将其转发给用户的函数进程。函数通过处理标准输入输出来响应请求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a701a0931b904a64b95ce7ac09155919~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">函数运行时</h2>
<p>由于一般开发的函数都用于 HTTP API，因此希望可以获取到更多的请求上下文。这时候也可以通过引入框架来解决问题。下面是通过 Express 框架来封装 Node.js 运行时的部分示例。</p>
<p>首先是基础镜像，需要引入 watchdog，同时将 <code>mode</code> 改为 <code>http</code> 模式，同时指定函数入口文件及服务地址。</p>
<pre><code class="hljs language-dockerfile copyable" lang="dockerfile"><span class="hljs-keyword">FROM</span> ghcr.io/openfaas/of-watchdog:<span class="hljs-number">0.8</span>.<span class="hljs-number">4</span> as watchdog
<span class="hljs-keyword">FROM</span> node:<span class="hljs-number">12</span>-alpine as ship

<span class="hljs-keyword">COPY</span><span class="bash"> --from=watchdog /fwatchdog /usr/bin/fwatchdog</span>
<span class="hljs-keyword">RUN</span><span class="bash"> chmod +x /usr/bin/fwatchdog</span>

<span class="hljs-comment"># 省略部分配置...</span>

<span class="hljs-keyword">COPY</span><span class="bash"> <span class="hljs-keyword">function</span>/ ./</span>

<span class="hljs-keyword">RUN</span><span class="bash"> npm i</span>

<span class="hljs-keyword">WORKDIR</span><span class="bash"> /home/app/</span>

<span class="hljs-keyword">ENV</span> fprocess=<span class="hljs-string">"node index.js"</span>
<span class="hljs-keyword">ENV</span> mode=<span class="hljs-string">"http"</span>
<span class="hljs-keyword">ENV</span> upstream_url=<span class="hljs-string">"http://127.0.0.1:3000"</span>

<span class="hljs-keyword">CMD</span><span class="bash"> [<span class="hljs-string">"fwatchdog"</span>]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数入口文件部分，我们需要新建一个 Express 应用，在接收到请求时，封装函数事件及上下文对象传递给用户代码执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">const</span> handler = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./function/handler'</span>);  <span class="hljs-comment">// 用户函数代码</span>

<span class="hljs-keyword">const</span> app = express();

<span class="hljs-comment">// 函数事件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FunctionEvent</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">req</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.body = req.body;
        <span class="hljs-built_in">this</span>.headers = req.headers;
        <span class="hljs-comment">// ...</span>
    &#125;
&#125;

<span class="hljs-comment">// 函数上下文</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FunctionContext</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">cb</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.statusValue = <span class="hljs-number">200</span>;
        <span class="hljs-built_in">this</span>.cb = cb;
    &#125;

    <span class="hljs-function"><span class="hljs-title">status</span>(<span class="hljs-params">value</span>)</span> &#123;&#125;

    <span class="hljs-function"><span class="hljs-title">succeed</span>(<span class="hljs-params">value</span>)</span> &#123;&#125;
&#125;

<span class="hljs-comment">// 构造中间件，执行用户代码</span>
<span class="hljs-keyword">const</span> middleware = <span class="hljs-keyword">async</span> (req, res) => &#123;
    <span class="hljs-keyword">const</span> cb = <span class="hljs-function">(<span class="hljs-params">err, functionResult</span>) =></span> &#123;
        <span class="hljs-comment">// res.status().send()</span>
    &#125;;

    <span class="hljs-keyword">const</span> fnEvent = <span class="hljs-keyword">new</span> FunctionEvent(req);
    <span class="hljs-keyword">const</span> fnContext = <span class="hljs-keyword">new</span> FunctionContext(cb);

    <span class="hljs-comment">// handler(fnEvent, fnContext)</span>
&#125;;

app.get(<span class="hljs-string">'/*'</span>, middleware);

<span class="hljs-keyword">const</span> port = process.env.http_port || <span class="hljs-number">3000</span>;

app.listen(port, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`listening on port: <span class="hljs-subst">$&#123;port&#125;</span>`</span>)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">总结</h1>
<p>简单再回顾一下本文的内容。首先我们介绍了 BFF 应用研发模式的发展以及团队探索 OpenFaaS 的背景，然后讲述了团队在业务中的一些实践，最后简单介绍了 OpenFaaS 的一些底层原理。希望对大家有所帮助，感兴趣的同学可以留言讨论。</p>
<p>最后再分享一下个人的一些看法。在 FaaS 基础设施逐渐完善的情况下，虽然开发运维的效率有所提升，但是业务的复杂度并没有降低，因此怎么构建抽象灵活的 BaaS 服务也是一个非常值得思考的方向。例如我们想快速构建一个视频在线服务，理想的状态就是能够直接通过 FaaS 函数把用户、文件存储、视频转码、数据库等 BaaS 服务串联起来，完全不需要关心服务端的细节，专注于业务流程的封装。</p>
<p>作者：杨鹏飞</p></div>  
</div>
            