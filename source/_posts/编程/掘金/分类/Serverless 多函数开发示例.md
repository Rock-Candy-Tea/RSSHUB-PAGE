
---
title: 'Serverless 多函数开发示例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5638'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 19:49:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=5638'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">01. 什么是 Serverless？</h2>
<p>Serverless 的定义和理解在不同的角度和场景会有不同的解读，AWS 将 Serverless(在 AWS 云上) 定义为 “是一种用于描述服务、实践和策略的方式，使您能够构建更敏捷的应用程序，从而能够更快地创新和响应变化”的一种服务。 而红帽认为 Serverless 是 “可使开发人员专注构建和运行应用，而无需管理服务器” 的一种开发模型,并进一步将 Serverless 的产品分为两类：BaaS(后端即服务，让开发人员访问各种各样的第三方服务和应用) 与 FaaS(功能即服务，开发人员编写逻辑，部署到完全由平台管理的容器中，然后按需执行) 两种形态。 而 Serverless Framework 则认为 Serverless 是“一场由开发人员和企业推动,让单个开发人员可以完成高流量的应用开发，同时只将精力集中在产生价值的方面”的运动，</p>
<p>不管哪个方面，哪种角度，Serverless 都具有以下共同特点：</p>
<ol>
<li>快速开发，快速部署</li>
<li>按量付费，降低成本</li>
<li>自动扩容，无需维护</li>
</ol>
<p>而目前都是基于各个云厂商的 FaaS 服务来实现，如： 腾讯云的 SCF， AWS 的 Lambda， Azure 云的 Azure Funcitons 等。</p>
<h3 data-id="heading-1">Serverless 解决什么问题？</h3>
<p>随着计算能力的加强，系统复杂度的增加，用户规模的增长，软件问题（如下， 也称为软件危机）也会发生指数型的增长。</p>
<ul>
<li>软件开发进度难以预测</li>
<li>软件开发成本难以控制</li>
<li>软件产品质量无法保证</li>
<li>软件产品难以维护</li>
</ul>
<p>而 Serverless 则可以通过以下方式提出了对于软件危机问题的解决方案：</p>
<ul>
<li>通过函数方式将系统功能拆分为更小的颗粒度，更便于设计，开发，测试和维护。</li>
<li>通过按量计费大幅度减少资源闲置时的开销费用，降低服务器成本。</li>
<li>通过自动扩容以及云平台的支持，大幅减少运维工作量以及软件维护成本。</li>
</ul>
<p>同时在现在普遍倡导敏捷工作方式的现代工作环境中，Serverless 也为快速验证想法、迭代功能提供了开发方式的最佳实践，同时而不需要担心代码改动会影响系统的其他功能，也无需考虑部署前的服务器配置以及部署后的维护工作。</p>
<h2 data-id="heading-2">02. Serverless Framework</h2>
<p>Serverless Framework 是业界非常受欢迎的无服务器应用框架，通过与众多一流云供应商如腾讯云，AWS 等的紧密合作，为广大开发者提供无需关心底层基础设施，即可编写和部署代码的无服务开发体验。</p>
<p>Serverless Framework 同时提供资源管理、自动伸缩、统计分析等能力，让广大开发者可以节省运维成本，真正做到“按量付费”的同时，也无需花费精力处理日志收集、异常统计等任务。</p>
<p>Serverless Framework 通过 CLI 工具与腾讯云紧密合作，为中国用户提供了基于组件（Serverless Components)的完整解决方案。覆盖了无服务应用编码、测试、部署等全生命周期，同时切合中国用户的使用场景和习惯。</p>
<h3 data-id="heading-3">为什么选用 Serverless Framework？</h3>
<p>通过 Serverless Framework 的短短几行配置文件和 CLI 工具，开发者就可以额外获得：</p>
<ul>
<li>在本地进行函数开发，并一键部署到云端，无需额外适配云函数，也无需登录控制台。</li>
<li>支持将传统开发框架的应用 （如：Express, Next.js, Flask, Laravel 等）部署为 Serverless 应用。</li>
<li>在本地对函数代码进行调试，或使用远程开发模式在本地实时查看部署服务的日志输出，并进行调试。</li>
<li>通过简单配置即可完成所有基础设施配置（如：API 网关、COS 存储、DB 链接等）</li>
<li>快速切换应用的部署环境（开发，演示，生产），地区。</li>
<li>更详细轻松的了解应用状态，查看日志、报错统计等信息。</li>
</ul>
<h2 data-id="heading-4">03. 多函数开发示例</h2>
<p>本示例使用 Serverless Framework 的多函数组件（multi-scf）和 PostgreSQL 组件（postgresql）实现，实现以下 3 个 API 接口。</p>
<ul>
<li><code>GET /todos/</code> 获取所有的 todo 事项</li>
<li><code>POST /todos/</code> 创建新的 todo 事项</li>
<li><code>POST /todos/&#123;id&#125;/actions/complete</code> 完成 todo 事项</li>
</ul>
<p>并使用 Serverless Framework 提供的 invoke 和 logs 功能进行调试以及查看生产环境实时日志。</p>
<p>本示例相关代码可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fole3021%2Fsls-demo-msn-todo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ole3021/sls-demo-msn-todo" ref="nofollow noopener noreferrer">Git 仓库</a> 中获取。</p>
<h4 data-id="heading-5">步骤 1: 安装 Serverless Framework</h4>
<p>执行以下命令安装 Serverless Framework</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm install serverless -g
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm update serverless -g
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此命令会安装最新的 Serverless Framework 到你的计算机，安装成功后可以通过 <code>serverless</code> 或者 <code>sls</code> 开始使用 Serverless Framework</p>
<h4 data-id="heading-6">步骤 2: 初始化多函数项目</h4>
<pre><code class="hljs language-sh copyable" lang="sh">$ sls init multi-scf-nodejs --name sls-demo-msn-todo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此命令会使用应用模板 <code>multi-scf-nodejs</code> 初始化名为 <code>my-multi-scf-demo</code> 的应用目录。初始化成功后该目录结构为</p>
<pre><code class="copyable">.
├── README.md
├── index.js
└── serverless.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的文件用途如下：</p>
<ul>
<li>index.js：函数文件。</li>
<li>serverless.yml：Serverless Framework 配置文件。
<ul>
<li>app：应用名称，会作为应用识别的唯一标识。</li>
<li>stage：应用环境，通过不同环境，部署不同的应用实例。</li>
<li>component：组件名称</li>
<li>name：组件实例名称</li>
<li>inputs：组件部署的输入参数</li>
</ul>
</li>
</ul>
<h4 data-id="heading-7">步骤 3: 链接数据库</h4>
<p>因为 Serverless 是无状态的（运行后就会销毁）， 所以这里需要链接数据库用来持久化 todo 信息。添加数据库需要先借助 VPC 网络连接。</p>
<p><strong>1. 添加 VPC</strong></p>
<p>创建子目录 <code>vpc</code> 并在子目录中添加新的 <code>serverless.yml</code> 文件如下：</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">component:</span> <span class="hljs-string">vpc</span> <span class="hljs-comment"># [必选]要使用组件，更多组件请查看 https://github.com/serverless-components</span>
<span class="hljs-attr">name:</span> <span class="hljs-string">sls-demo-msn-vpc</span> <span class="hljs-comment"># [必选]组件实例名称</span>

<span class="hljs-attr">inputs:</span>
  <span class="hljs-attr">region:</span> <span class="hljs-string">ap-guangzhou</span> <span class="hljs-comment"># 实例所属地区</span>
  <span class="hljs-attr">zone:</span> <span class="hljs-string">ap-guangzhou-2</span> <span class="hljs-comment"># 实例所属地区区域</span>
  <span class="hljs-attr">vpcName:</span> <span class="hljs-string">$&#123;name&#125;</span> <span class="hljs-comment"># 实例名称，这里复用字段 name 作为名称。</span>
  <span class="hljs-attr">subnetName:</span> <span class="hljs-string">sls-demo-msn-subnet</span> <span class="hljs-comment"># 子网的名称</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多 VPC 的配置内容，查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.serverless.com%2Fcn%2Fframework%2Fdocs%2Finfrastructure%2Fvpc%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.serverless.com/cn/framework/docs/infrastructure/vpc/" ref="nofollow noopener noreferrer">VPC 私有网络</a> 获取更多详情信息。</p>
<blockquote>
<p>在子组件的配置文件中，app 名称会自动继承父目录的 serverless.yml 中的配置。 同时同一个应用的 app 名称需要保持一致。</p>
</blockquote>
<p><strong>2. 添加数据库</strong></p>
<p>创建子目录 <code>db</code> 并在子目录中添加新的 <code>serverless.yml</code> 文件如下：</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">component:</span> <span class="hljs-string">postgresql</span> <span class="hljs-comment">#(必填) 引用 component 的名称，当前用到的是 postgresql 组件</span>
<span class="hljs-attr">name:</span> <span class="hljs-string">sls-demo-msn-DB</span> <span class="hljs-comment"># (必填) 该 postgresql 组件创建的实例名称</span>

<span class="hljs-attr">inputs:</span>
  <span class="hljs-attr">region:</span> <span class="hljs-string">ap-guangzhou</span> <span class="hljs-comment"># 实例所属地区</span>
  <span class="hljs-attr">zone:</span> <span class="hljs-string">ap-guangzhou-2</span> <span class="hljs-comment"># 实例所属地区区域</span>
  <span class="hljs-attr">dBInstanceName:</span> <span class="hljs-string">$&#123;name&#125;-$&#123;stage&#125;</span> <span class="hljs-comment"># 数据库实例名称唯一，且同一个数据库只能存在同一个vpc内。</span>
  <span class="hljs-attr">extranetAccess:</span> <span class="hljs-literal">true</span> <span class="hljs-comment"># 是否开启实例外网访问</span>
  <span class="hljs-attr">vpcConfig:</span> <span class="hljs-comment"># vpc网络配置</span>
    <span class="hljs-attr">vpcId:</span> <span class="hljs-string">$&#123;output:$&#123;stage&#125;:$&#123;app&#125;:sls-demo-msn-vpc.vpcId&#125;</span> <span class="hljs-comment"># 私有网络Id</span>
    <span class="hljs-attr">subnetId:</span> <span class="hljs-string">$&#123;output:$&#123;stage&#125;:$&#123;app&#125;:sls-demo-msn-vpc.subnetId&#125;</span> <span class="hljs-comment"># 子网Id</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在数据库配置中添加数据库到 vpc 网络，这里使用输出变量(output)来动态获取 vpc 的 id 信息。</p>
<p>更多变量的配置内容，查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.serverless.com%2Fcn%2Fframework%2Fdocs%2Fbasic%2Fvariables%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.serverless.com/cn/framework/docs/basic/variables/" ref="nofollow noopener noreferrer">Serverless 变量</a> 获取更多详情信息。</p>
<p>更多 PostgreSQL 的配置内容，查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.serverless.com%2Fcn%2Fframework%2Fdocs%2Finfrastructure%2Fpostgresql%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.serverless.com/cn/framework/docs/infrastructure/postgresql/" ref="nofollow noopener noreferrer">PostgreSQL 数据库</a> 获取更多详情信息。</p>
<blockquote>
<p>在组件部署完成后，可以在组件目录内，使用 <code>sls info</code> 查看组件的输出变量，或者可以到腾讯云的应用控制台查看相关信息。</p>
</blockquote>
<p><strong>3. 初始化应用目录</strong></p>
<ol>
<li>创建子目录 <code>src</code> 并将创建生成的 <code>index.js</code> （重命名为<code>todos.js</code>） 和 <code>serverless.yml</code> 移动到目录中。</li>
<li>在<code>src</code>目录中执行<code>npm init</code>初始化 Node.js 项目。</li>
<li>在<code>src</code>目录中执行<code>npm i pg --save</code>安装数据库链接依赖包<code>pg</code>。</li>
<li>在项目根目录添加根配置文件<code>serverless.yml</code>，文件如下：</li>
</ol>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">app:</span> <span class="hljs-string">sls-demo-msn-todo-3e5a2134</span> <span class="hljs-comment"># 应用唯一识别标识，同账号下需要保持唯一。</span>
<span class="hljs-attr">stage:</span> <span class="hljs-string">dev</span> <span class="hljs-comment"># 应用部署环境名称，这里使用环境变量 STAGE 的值。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>根目录的配置文件信息会被子组件继承，不需要在子组件中重复定义。（仅限于 app 与 stage）。</p>
</blockquote>
<p>最终完成的项目目录结构如下：</p>
<pre><code class="copyable">.
├── README.md
├── db # 数据库
│   └── serverless.yml # 数据库配置文件
├── serverless.yml
├── src # 多函数应用
│   ├── node_modules
│   ├── package-lock.json
│   ├── package.json # Node.js依赖文件
│   ├── serverless.yml # 多函数应用配置文件
│   └── todos.js # todo 应用主文件
└── vpc # vpc
    └── serverless.yml # vpc配置文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4. 修改多函数应用配置</strong></p>
<p>在多函数目录<code>src</code>内修改配置文件如下：</p>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-attr">component:</span> <span class="hljs-string">multi-scf</span>
<span class="hljs-attr">name:</span> <span class="hljs-string">sls-demo-msn</span>

<span class="hljs-attr">inputs:</span>
  <span class="hljs-attr">src:</span>
    <span class="hljs-attr">src:</span> <span class="hljs-string">./</span>
    <span class="hljs-attr">exclude:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">.env</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">"node_modules/**"</span> <span class="hljs-comment"># 部署时忽略node_modules目录中所有文件，以加快部署速度</span>
  <span class="hljs-attr">environments:</span> <span class="hljs-comment"># 应用环境变量信息</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">key:</span> <span class="hljs-string">PG_CONNECT_STRING</span>
      <span class="hljs-attr">value:</span> <span class="hljs-string">$&#123;output:$&#123;stage&#125;:$&#123;app&#125;:sls-demo-msn-DB.private.connectionString&#125;</span>
  <span class="hljs-attr">region:</span> <span class="hljs-string">ap-guangzhou</span>
  <span class="hljs-attr">runtime:</span> <span class="hljs-string">Nodejs12.16</span>
  <span class="hljs-attr">memorySize:</span> <span class="hljs-number">128</span>
  <span class="hljs-attr">vpc:</span> <span class="hljs-comment"># vpc网络配置</span>
    <span class="hljs-attr">vpcId:</span> <span class="hljs-string">$&#123;output:$&#123;stage&#125;:$&#123;app&#125;:sls-demo-msn-vpc.vpcId&#125;</span> <span class="hljs-comment"># 私有网络Id</span>
    <span class="hljs-attr">subnetId:</span> <span class="hljs-string">$&#123;output:$&#123;stage&#125;:$&#123;app&#125;:sls-demo-msn-vpc.subnetId&#125;</span> <span class="hljs-comment"># 子网Id</span>
  <span class="hljs-attr">installDependency:</span> <span class="hljs-literal">true</span> <span class="hljs-comment"># 是否在线安装依赖</span>
  <span class="hljs-attr">timeout:</span> <span class="hljs-number">6</span> <span class="hljs-comment"># 默认超时时间（秒）</span>
  <span class="hljs-attr">functions:</span> <span class="hljs-comment"># 多函数定义</span>
    <span class="hljs-attr">allTodo:</span> <span class="hljs-comment"># 函数别名</span>
      <span class="hljs-attr">handler:</span> <span class="hljs-string">todos.all</span> <span class="hljs-comment"># 处理函数</span>
      <span class="hljs-attr">memorySize:</span> <span class="hljs-number">256</span> <span class="hljs-comment"># 自定义次函数的内存空间</span>
    <span class="hljs-attr">addTodo:</span>
      <span class="hljs-attr">handler:</span> <span class="hljs-string">todos.add</span>
      <span class="hljs-attr">timeout:</span> <span class="hljs-number">9</span> <span class="hljs-comment"># 自定义此函数的超时时间（秒）</span>
    <span class="hljs-attr">completeTodo:</span>
      <span class="hljs-attr">handler:</span> <span class="hljs-string">todos.comp</span>
      <span class="hljs-attr">timeout:</span> <span class="hljs-number">9</span>
  <span class="hljs-attr">triggers:</span> <span class="hljs-comment"># 触发器配置</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">type:</span> <span class="hljs-string">apigw</span>
      <span class="hljs-attr">parameters:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">todosAPIGW</span>
        <span class="hljs-attr">protocols:</span>
          <span class="hljs-bullet">-</span> <span class="hljs-string">https</span>
          <span class="hljs-bullet">-</span> <span class="hljs-string">http</span>
        <span class="hljs-attr">apis:</span> <span class="hljs-comment"># API配置</span>
          <span class="hljs-bullet">-</span> <span class="hljs-attr">path:</span> <span class="hljs-string">/todos/</span> <span class="hljs-comment"># 路由路径</span>
            <span class="hljs-attr">method:</span> <span class="hljs-string">GET</span> <span class="hljs-comment"># 路由方法</span>
            <span class="hljs-attr">function:</span> <span class="hljs-string">allTodo</span> <span class="hljs-comment"># 路由处理函数别名</span>
          <span class="hljs-bullet">-</span> <span class="hljs-attr">path:</span> <span class="hljs-string">/todos/</span>
            <span class="hljs-attr">method:</span> <span class="hljs-string">POST</span>
            <span class="hljs-attr">function:</span> <span class="hljs-string">addTodo</span>
          <span class="hljs-bullet">-</span> <span class="hljs-attr">path:</span> <span class="hljs-string">/todos/&#123;id&#125;/actions/complete</span>
            <span class="hljs-attr">method:</span> <span class="hljs-string">POST</span>
            <span class="hljs-attr">function:</span> <span class="hljs-string">completeTodo</span>
            <span class="hljs-attr">param:</span> <span class="hljs-comment"># 动态路由参数配置</span>
              <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">id</span>
                <span class="hljs-attr">position:</span> <span class="hljs-string">PATH</span>
                <span class="hljs-attr">required:</span> <span class="hljs-literal">true</span>
                <span class="hljs-attr">type:</span> <span class="hljs-string">number</span>
                <span class="hljs-attr">desc:</span> <span class="hljs-string">Todo</span> <span class="hljs-string">ID</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里修改主要内容有：</p>
<ul>
<li>使用<code>installDependency</code>开启部署后依赖自动安装并忽略<code>node_module</code>目录下的全部文件(无需上传 node_modules，加快部署)</li>
<li>使用<code>vpc</code>添加 vpc 网络并链接到项目同一个 vpc 网络中。</li>
<li>使用<code>environments</code>添加项目环境变量，并使用输出变量（output）来动态生成数据库连接字符串。</li>
<li>使用<code>functions</code>来声明项目中的函数及其别名。</li>
<li>使用<code>triggers</code>声明函数的触发器，并在触发器的<code>apis</code>中配置各个函数对应的路径，以及参数信息。</li>
</ul>
<p>更多函数开发的配置内容和详情，查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.serverless.com%2Fcn%2Fframework%2Fdocs%2Finfrastructure%2Fpostgresql%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.serverless.com/cn/framework/docs/infrastructure/postgresql/" ref="nofollow noopener noreferrer">PostgreSQL 数据库</a> 获取更多详情信息。</p>
<p>更多 函数开发 的说明内容，查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.serverless.com%2Fcn%2Fframework%2Fdocs%2Ffunction%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.serverless.com/cn/framework/docs/function/" ref="nofollow noopener noreferrer">函数开发</a> 获取更多详情信息。</p>
<h4 data-id="heading-8">步骤 4: 开发功能</h4>
<p>修改<code>todos.js</code>并完成相关功能的开发，最终该文件代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">const</span> &#123; Client &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"pg"</span>);

<span class="hljs-keyword">const</span> client = <span class="hljs-keyword">new</span> Client(&#123;
  <span class="hljs-attr">connectionString</span>: process.env.PG_CONNECT_STRING,
&#125;);

<span class="hljs-comment">/**
 * 初始化数据库和表结构
 */</span>
<span class="hljs-keyword">const</span> initDB = <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> isConnected = client && client._connected;

  <span class="hljs-keyword">if</span> (!isConnected) &#123;
    <span class="hljs-keyword">await</span> client.connect();

    <span class="hljs-keyword">await</span> client.query(<span class="hljs-string">`
    CREATE TABLE IF NOT EXISTS todo (
      ID              SERIAL          NOT NULL,
      TITLE           VARCHAR         NOT NULL,
      NOTE            TEXT,
      IS_COMPLETE     BOOLEAN         DEFAULT FALSE
    );`</span>);
  &#125;
&#125;;

<span class="hljs-comment">/**
 * 获取所有Todo事项
 */</span>
<span class="hljs-built_in">exports</span>.all = <span class="hljs-keyword">async</span> (event, context) => &#123;
  <span class="hljs-comment">// async 需要关闭事件循环等待，以避免日志记录超时或函数无返回的问题。</span>
  context.callbackWaitsForEmptyEventLoop = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">await</span> initDB();

  <span class="hljs-keyword">const</span> &#123; rows &#125; = <span class="hljs-keyword">await</span> client.query(&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"SELECT * FROM todo"</span> &#125;);

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">message</span>: <span class="hljs-string">"Tencent SCF execute successful!"</span>,
    <span class="hljs-attr">data</span>: rows,
  &#125;;
&#125;;

<span class="hljs-comment">/**
 * 添加新的Todo事项
 */</span>
<span class="hljs-built_in">exports</span>.add = <span class="hljs-keyword">async</span> (event, context) => &#123;
  <span class="hljs-comment">// async 需要关闭事件循环等待，以避免日志记录超时或函数无返回的问题。</span>
  context.callbackWaitsForEmptyEventLoop = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">const</span> &#123; title, note &#125; = <span class="hljs-built_in">JSON</span>.parse(event.body);
  <span class="hljs-keyword">if</span> (!title) &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">statusCode</span>: <span class="hljs-number">400</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">"Missing Todo Title"</span>,
    &#125;;
  &#125;

  <span class="hljs-keyword">await</span> initDB();
  <span class="hljs-keyword">const</span> &#123; rowCount &#125; = <span class="hljs-keyword">await</span> client.query(&#123;
    <span class="hljs-attr">text</span>: <span class="hljs-string">"INSERT INTO todo (title, note) VALUES($1, $2)"</span>,
    <span class="hljs-attr">values</span>: [title, note],
  &#125;);

  <span class="hljs-keyword">return</span> rowCount === <span class="hljs-number">1</span>
    ? &#123;
        <span class="hljs-attr">statusCode</span>: <span class="hljs-number">201</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">"Todo added success."</span>,
      &#125;
    : &#123;
        <span class="hljs-attr">statusCode</span>: <span class="hljs-number">400</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">"Todo added failed."</span>,
      &#125;;
&#125;;

<span class="hljs-comment">/**
 * 完成指定Todo事项
 */</span>
<span class="hljs-built_in">exports</span>.comp = <span class="hljs-keyword">async</span> (event, context) => &#123;
  <span class="hljs-comment">// async 需要关闭事件循环等待，以避免日志记录超时或函数无返回的问题。</span>
  context.callbackWaitsForEmptyEventLoop = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">const</span> todoId = event.pathParameters.id;

  <span class="hljs-keyword">if</span> (!todoId && !<span class="hljs-built_in">isNaN</span>(todoId)) &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">statusCode</span>: <span class="hljs-number">400</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">"Missing Todo Id"</span>,
    &#125;;
  &#125;

  <span class="hljs-keyword">await</span> initDB();
  <span class="hljs-keyword">const</span> &#123; rowCount &#125; = <span class="hljs-keyword">await</span> client.query(&#123;
    <span class="hljs-attr">text</span>: <span class="hljs-string">"UPDATE todo SET is_complete = true WHERE id=$1"</span>,
    <span class="hljs-attr">values</span>: [todoId],
  &#125;);

  <span class="hljs-keyword">return</span> rowCount === <span class="hljs-number">1</span>
    ? &#123;
        <span class="hljs-attr">statusCode</span>: <span class="hljs-number">200</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">"Todo Complete success."</span>,
      &#125;
    : &#123;
        <span class="hljs-attr">statusCode</span>: <span class="hljs-number">400</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">"Todo Complete failed."</span>,
      &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">步骤 5: 调试功能</h4>
<p><strong>1. Invoke 调试</strong></p>
<p>要调试代码除了使用第三方开发工具通过配置的 API 网关 url 调试，还可以使用 Serverless Framework 的 Invoke 功能 或 远程调试 功能. 这里使用 invoke 功能演示如何调试函数功能。</p>
<blockquote>
<p>invoke 和 远程调试功能 需要在组件的目录内执行。</p>
</blockquote>
<p><strong>2. 获取全部 Todo</strong></p>
<p>在 src 目录下执行</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ serverless invoke -f allTodo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后可以得到的结果</p>
<pre><code class="hljs language-bash copyable" lang="bash">使用授权信息 default 授权中，如果需要使用临时密钥，请使用 --login 重新登陆
billDuration:      36
duration:          36
errMsg:
functionRequestId: fe6d302d-f6db-42ad-9c7b-8d0c61ead9b3
invokeResult:      0
<span class="hljs-built_in">log</span>:
  <span class="hljs-string">""</span><span class="hljs-string">"
    START RequestId: fe6d302d-f6db-42ad-9c7b-8d0c61ead9b3
    Event RequestId: fe6d302d-f6db-42ad-9c7b-8d0c61ead9b3

    END RequestId: fe6d302d-f6db-42ad-9c7b-8d0c61ead9b3
    Report RequestId: fe6d302d-f6db-42ad-9c7b-8d0c61ead9b3 Duration:36ms Memory:256MB MemUsage:11.3984MB
  "</span><span class="hljs-string">""</span>
memUsage:          11952128
---------------------------------------------
Serverless: 调用成功

&#123;
  message: <span class="hljs-string">'Tencent SCF execute successful!'</span>,
  data: []
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 invoke 返回的结果中，会包含函数执行后的 meta 信息，如运行时间，错误，RequestId，执行的日志 和函数返回的结果。</p>
<p><strong>3. 创建新的 Todo</strong></p>
<p>在 src 目录下执行</p>
<pre><code class="hljs language-bash copyable" lang="bash">$  serverless invoke -f addTodo --data <span class="hljs-string">"&#123;\"body\":\"&#123;\\\"title\\\":\\\"Create multi-scf project demo\\\",\\\"note\\\":\\\"Todo App with postgreSQL\\\"&#125;\"&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后可以得到的结果</p>
<pre><code class="copyable">使用授权信息 default 授权中，如果需要使用临时密钥，请使用 --login 重新登陆
billDuration:      35
duration:          35
errMsg:
functionRequestId: 93f50016-064f-468d-9e98-31645fc254fd
invokeResult:      0
log:
  """
    START RequestId: 93f50016-064f-468d-9e98-31645fc254fd
    Event RequestId: 93f50016-064f-468d-9e98-31645fc254fd

    END RequestId: 93f50016-064f-468d-9e98-31645fc254fd
    Report RequestId: 93f50016-064f-468d-9e98-31645fc254fd Duration:35ms Memory:128MB MemUsage:11.293MB
  """
memUsage:          11841536
---------------------------------------------
Serverless: 调用成功

&#123;
  statusCode: 201,
  message: 'Todo added success.'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">步骤 6：部署和日志</h4>
<p><strong>1. 部署代码到生产环境</strong></p>
<p>使用下面命令可以快速部署项目到生产环境（这里命名生产环境为<code>prod</code>）</p>
<pre><code class="copyable">$ serverless deploy --stage prod
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 即时查看生产环境日志</strong></p>
<p>在项目目录<code>src</code>中执行以下命令可以查看项目的即时日志信息</p>
<pre><code class="copyable">$ sls logs --tail -f allTodo --stage prod
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是返回结果：</p>
<pre><code class="copyable">使用授权信息 default 授权中，如果需要使用临时密钥，请使用 --login 重新登陆

serverless ⚡components
Action: "logs" - Stage: "prod" - App: "sls-demo-msn-todo-3e5a2134" - Name: "sls-demo-msn"

START RequestId:6f31857109130f092c547337c073ea91

Response RequestId:dbb3a8ed63a32be8e6b7a2dd8a32bbe2 RetMsg:&#123;"message":"Tencent SCF execute successful!","data":[&#123;"id":1,"title":"Create multi-scf project demo","note":"Todo App with postgreSQL","is_complete":false&#125;]&#125;
END RequestId:dbb3a8ed63a32be8e6b7a2dd8a32bbe2
Report RequestId:dbb3a8ed63a32be8e6b7a2dd8a32bbe2 Duration:4ms Memory:256MB MemUsage:12.113281MB

Response RequestId:485a87cfc6ad385b7e9c84343962391b RetMsg:&#123;"message":"Tencent SCF execute successful!","data":[&#123;"id":1,"title":"Create multi-scf project demo","note":"Todo App with postgreSQL","is_complete":false&#125;]&#125;
END RequestId:485a87cfc6ad385b7e9c84343962391b
Report RequestId:485a87cfc6ad385b7e9c84343962391b Duration:4ms Memory:256MB MemUsage:11.886719MB

START RequestId:0ede6d26dca55362a701c10ff51c9021


Serverless › 监听中 ...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">总结</h2>
<p>感谢长久以来对 Serverless Framework 支持的广大开发者，未来我们也会继续迭代产品，推出新功能，改进产品使用体验，最终我们会为中国的开发者打造一套符合中国开发者习惯的无服务器开发的完整解决方案。</p>
<p>也欢迎大家到 Serverless 中文社区分享经验和想法以及反馈问题和 BUG。</p>
<p>Serverless 中文社区：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless-tencent%2Fdiscussions" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/serverless/serverless-tencent/discussions" ref="nofollow noopener noreferrer">github.com/serverless/…</a></p>
<p>最后希望大家可以参与我们的有奖调查问卷：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.surveymonkey.com%2Fr%2Fblog-msntodo" target="_blank" rel="nofollow noopener noreferrer" title="https://www.surveymonkey.com/r/blog-msntodo" ref="nofollow noopener noreferrer">www.surveymonkey.com/r/blog-msnt…</a></p>
<h2 data-id="heading-12">One More Thing</h2>
<p>立即体验腾讯云 Serverless Demo，领取 Serverless 新用户礼包 👉  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fserverless.cloud.tencent.com%2Fstart%3Fc%3Djuejin" target="_blank" rel="nofollow noopener noreferrer" title="https://serverless.cloud.tencent.com/start?c=juejin" ref="nofollow noopener noreferrer">腾讯云 Serverless 新手体验</a></p>
<blockquote>
<p>欢迎访问：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fserverlesscloud.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://serverlesscloud.cn/" ref="nofollow noopener noreferrer">Serverless 中文网</a>！</p>
</blockquote></div>  
</div>
            