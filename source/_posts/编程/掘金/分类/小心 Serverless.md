
---
title: '小心 Serverless'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e915cb9d8bec41ccac2e0970c84a68a9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 08:31:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e915cb9d8bec41ccac2e0970c84a68a9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">技术乐观主义陷阱</h2>
<p>技术具有商品属性，这是常常被我们忽略的一个事实。且不谈垄断之后带来的商业利益，一方面技术依赖市场的认可来彰显它的价值，另一方面技术还需要依靠大众的反馈才得以完善自己，所以庞大的用户群体是它繁荣的基石，它需要尽可能的为人所知。 无论你是想吸引更多的项目和开发者加入某个社区中，还是想让某个框架摆脱默默无闻乃至脱颖而出，过程都务必依赖于大量的运营活动，其中不少也要倚靠背后大厂的资源投入。从近乎寿终正寝的 Silverlight 到近些年大火的 Flutter，无不遵循着类似的模式。</p>
<p>既然是面向大众的商品，商家必然会以利益相关者的姿态为其辩护和呐喊，这无可厚非。但在此影响之下，当技术人员对某项技术进行调研或者在被动接收来自行业内的更新时，得到的信息会不知不觉的向积极侧偏移，这对技术人员来说未必是好事情。因为我们很难分辨感官里的哪一些是事实，哪一些是观点，哪一些是有条件成立，更重要的是还有哪一些是它没有告诉你的。</p>
<p>Serverless 就是其中一个例子。</p>
<p>这篇文章不是对 serverless 的批评。Serverless 是云原生架构（Cloud Native ）下水到渠成的必然产物，从 IaaS（Infrastructure as a Service） 到 Paas（Platform as a Service） 甚至再到 Saas （Software as a Service），我们看到的是运维能力不断外包的迁移过程，这有助于塑造精锐团队专注于交付业务价值以及灵活应对市场变化——为什么我们要千篇一律的写登陆注册模块？如何才能将代码的维护成本降至最低？Serverless 便是在这些前提下诞生的。但 Serverless 只是其中一种解决方案（a solution），而非唯一的解决方案（the solution），更重要的是这篇文章会让你意识到它绝非是方案中的理想首选。</p>
<p>例如在每一篇介绍 serverless 的文章中，都一定会提到因为冷启动缘故导致 serverless 函数具有较慢的首次响应时间问题，但它们能够提供的信息通常到此便戛然而止了，这无法给我们带来任何帮助，我们也不会对它产生任何的警惕。如果我继续告诉你不同供应商的延迟各不相同，我所在项目中 Azure Serverless 的第一次启动延迟可以长达6秒，那么我相信此时你会更慎重的看待这条信息，并开始降低对于它作为 web server 的预期。</p>
<p>本文想强调的另一点是，虽然 serverless 看似是近几年才诞生的“新”技术，但它背后遵循最佳实践依然是“旧”世界下人们早已达成的共识；在实际将它应用到现有产品的过程中，你需要关心内容与前 serverless 时代也并无二致。例如在  OWASP 整理出的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fowasp.org%2Fwww-project-serverless-top-10%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://owasp.org/www-project-serverless-top-10/" ref="nofollow noopener noreferrer">有关 Serverless 排名前十的安全问题 </a>中，我不认为有哪一则是 serverless 架构“独享”的。Serverless 与传统服务相比的优势之一可能是前人的宝贵经验被固化到了平台和产品形态之中，用以确保你不必再走弯路。</p>
<p>考虑到通识性，本文主要使用 Azure 和 AWS 旗下的 serverless 服务对问题进行说明</p>
<h2 data-id="heading-1">被轻视的供应商锁定（vendor lock-in）</h2>
<h3 data-id="heading-2">供应商的三道锁</h3>
<p>供应商锁定在云原生架构下是无法避免的问题，如果你选择 Azure 作为你的云服务提供商，那么你大概率会顺带选择 Azure Blob Storage 而不是 AWS S3 作为你的存储服务，因为来自于同一个供应商下的服务契合度更高，维护起来更容易。同样考虑到成本和风险，自此之后更换服务的可能性也几乎为零。</p>
<p>好在编程语言和编程框架依然通用无界，加之容器化技术早已成熟，在开发常规业务代码的方面供应商并没有给我们造成太大的困恼。此时的供应商只充当配角，无论你是选择 AWS EventBridge 还是 Azure Event Grid，背后 Event-Driven 的决策不会发生改变，核心的业务代码不会受到影响，用 ExpressJS 写出的代码在不同服务商之间仍可复用。这种模式最明显的特点是业务人员可以专心开发业务代码，它们不用关心公司购买的是哪家提供商的产品。虽然听起来有些反模式，但代码与环境的适配可以全权交给运维人员去处理的这条路是可行的。</p>
<p>而 serverless 模式恰恰相反，它的崛起像是一道命题作文，在概念先行的前提下不同的供应商根据自己现存基础设施优先推出自己的解决方案。对于这一点有意思的是，如果你现在去看市面上讲解 serverless 的技术图书，书中谈及的概念和代码实施方案一定是围绕某个单一平台编写的。</p>
<p>serverless 中有一个很重要的概念正是这方面的体现：trigger.</p>
<p>顾名思义，trigger 是 function（本文的 function 泛指广义各个云平台上 serverless 的实现代码，同时代指 Azure Function 和 AWS Lambda）的触发器，由它来负责启动 function。 例如对于一个响应前端请求的 function 而言，http 请求就是它的 trigger。</p>
<p>但在 serverless 生态中，http 是最不重要的。你不妨回想一下我们最经典的 serverless 用例，离线创建略缩图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e915cb9d8bec41ccac2e0970c84a68a9~tplv-k3u1fbpfcp-watermark.image" alt="triggers.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在该流程中需要有 function 响应处理略缩图的消息，在存储之后需要有 function 将数据更新进数据库中。其中的消息服务和储存服务就是 function 的 trigger。</p>
<p>此时不难发现当你开始编写 function 时，你需要确认你的云供应商提供这类服务的具体产品是什么，消息服务在 Azure 中可以是 Azure Service Bus，但是到了 AWS 则变成了Message Queuing Service。不同服务提供的 API 和模型不尽相同，同时代码与服务集成的方式也是量身定做的，这是第一层锁。</p>
<p>其次为了在 function 代码中访问这类服务，裸写的代码是不被允许的，因为你需要在访问服务时用指定的方式传递 API Key，通常解决这个问题的办法是直接集成供应商提供的 client SDK，比如 @azure/service-bus 或是 AWS SDK。事实上从接收到请求的那一刻起，代码差异就已经注定了，虽然 Azure 和 AWS 都同意以 event handler 函数的形式来响应 trigger 的请求，但两者的函数签名差异明显，你能取得的函数所在的上下文也各有千秋。这是第二层锁。</p>
<p>这两者看上去似乎把硬件和软件层面都覆盖到了，最重要的“隐形锁”却无形中被忽略了——那就是供应商的意志，即它们希望你以什么样的方式去设计和编写 function。</p>
<p>以 API 架构为例，Azure 提供的服务比如 Azure Serverless 或者是 App Service 可以是相互独立的，哪怕你只购买其中的一项服务，你也可以单独为其配置 API Management, Identity 等属性。服务被允许对外暴露 HTTP 端口。在其<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Farchitecture%2Fserverless-quest%2Freference-architectures" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/en-us/azure/architecture/serverless-quest/reference-architectures" ref="nofollow noopener noreferrer">官网</a>给出的架构模式中，移动端设备可以直接访问 Azure Serverless 服务</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a944ffd48184b5cac9f1bfa49effe42~tplv-k3u1fbpfcp-watermark.image" alt="mobile-app-backends.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而在 AWS 中，服务的职责更为垂直，而非 Azure 般全能。HTTP 端点大多要被托管在 API Gateway 上，它为你提供了丰富的功能，比如权限验证、日志监控、缓存等等。同样在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Faws.amazon.com%2Flambda%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://aws.amazon.com/lambda/" ref="nofollow noopener noreferrer">AWS 官网</a> 给出的后端架构模式中，移动设备的请求必须要经过 API Gateway</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0e1670569f74219953acd73c5098960~tplv-k3u1fbpfcp-watermark.image" alt="lambda-mobilebackends.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 Azure Serverless 中每一个 serverless 项目都有属于自己的配置文件 host.json，如果我们想要限制 function 处理的最大请求数，你只需要修改该文件的配置项即可：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"extensions"</span>: &#123;
    <span class="hljs-attr">"http"</span>: &#123;
      <span class="hljs-attr">"routePrefix"</span>: <span class="hljs-string">"api"</span>,
      <span class="hljs-attr">"maxConcurrentRequests"</span>: <span class="hljs-number">100</span>,
      <span class="hljs-attr">"customHeaders"</span>: &#123;
        <span class="hljs-attr">"X-Content-Type-Options"</span>: <span class="hljs-string">"nosniff"</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中的 maxConcurrentRequests 就能用来控制并发请求数。</p>
<p>而在在 AWS 中，对于同步的 HTTP 端请求，<a href="https://link.juejin.cn/?target=https%3A%2F%2Faws.amazon.com%2Fblogs%2Farchitecture%2Frate-limiting-strategies-for-serverless-applications%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://aws.amazon.com/blogs/architecture/rate-limiting-strategies-for-serverless-applications/" ref="nofollow noopener noreferrer">官方建议</a>你可以通过 API Gateway 限流功能（throtting）和设定 AWS WAF 规则来实现</p>
<p>这层锁的危害在于你必须从一开始就在供应商的框架内来设计自己的解决方案。在 AWS 中你当然可以不选择 API Gateway 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.aws.amazon.com%2Fapigateway%2Flatest%2Fdeveloperguide%2Fapigateway-use-lambda-authorizer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html" ref="nofollow noopener noreferrer">Lambda authorizer</a> 功能作为 function 权限校验的解决方案，但我不确定其他路会让你绕多远。</p>
<p>即使你没有接触过 Lambda authorizer 也没有关系，我后面会有详细的讲解。在后面的章节我们也会看到，在抱怨它的同时我们不得不承认它背后遵循的依然是业内的最佳实践，我们看似无路可选，但实际上我们唯一能走的恰恰是前任留下的捷径。</p>
<h3 data-id="heading-3">解“锁”</h3>
<p>好消息是在这一层可见的危机面前我们依然有能够缓和的余地。</p>
<p>2019 年 ThoughtWorks 刚好发布了一篇关于如何避免 serverless 供应商锁定的文章 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.thoughtworks.com%2Finsights%2Fblog%2Fmitigating-serverless-lock-fears" target="_blank" rel="nofollow noopener noreferrer" title="https://www.thoughtworks.com/insights/blog/mitigating-serverless-lock-fears" ref="nofollow noopener noreferrer">Mitigating serverless lock-in fears</a>，文章从硬件到软件层面都给出了很多减少迁移成本的建议。但在我看来其中最为实用的一则是：为程序设计一组好的架构。</p>
<p>虽然低入门门槛是 serverless 不争的卖点之一，但是它的天花板依然可以达到传统技术栈程序相同的高度，一脉相承的优秀设计可给予后期维护上的便利。</p>
<p>例如一个对外发送邮件的用例首先采用 Azure Serverless Function 编写，我们在 httpTrigger 入口函数中可以直接引用 Azure SendGrid SDK 执行发送服务</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> SendGrid <span class="hljs-keyword">from</span> <span class="hljs-string">"@sendgrid/mail"</span>;
SendGrid.setApiKey(process.env[<span class="hljs-string">"SENDGRID_API_KEY"</span>] <span class="hljs-keyword">as</span> string);
 
<span class="hljs-keyword">const</span> httpTrigger: AzureFunction = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context: Context, req: HttpRequest</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">void</span>> </span>&#123;
    <span class="hljs-keyword">const</span> email = &#123;
     <span class="hljs-attr">to</span>: <span class="hljs-string">'test@example.com'</span>, <span class="hljs-comment">// Change to your recipient</span>
     <span class="hljs-attr">from</span>: <span class="hljs-string">'test@example.com'</span>, <span class="hljs-comment">// Change to your verified sender</span>
     <span class="hljs-attr">subject</span>: <span class="hljs-string">'Sending with SendGrid is Fun'</span>,
     <span class="hljs-attr">text</span>: <span class="hljs-string">'and easy to do anywhere, even with Node.js'</span>,
     <span class="hljs-attr">html</span>: <span class="hljs-string">'<strong>and easy to do anywhere, even with Node.js</strong>'</span>,
    &#125;

    <span class="hljs-keyword">await</span> SendGrid.send(email);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后如果想将它迁移至 AWS Lambda 的话，发送邮件部分需要完全替换为调用 AWS 的 SES 服务：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; SendEmailCommand &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@aws-sdk/client-ses"</span>;
<span class="hljs-keyword">import</span> &#123; sesClient &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./libs/sesClient.js"</span>;

<span class="hljs-comment">// Set the parameters</span>
<span class="hljs-keyword">const</span> params = &#123;
<span class="hljs-attr">Destination</span>: &#123;&#125;,
<span class="hljs-attr">Message</span>: &#123;&#125;,
&#125;;

<span class="hljs-keyword">const</span> data = <span class="hljs-keyword">await</span> sesClient.send(<span class="hljs-keyword">new</span> SendEmailCommand(params));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但事实上我们并不关心谁在为我们提供邮件发送服务，无论是 SendGrid 或者 SES 功能上并无差别。所以在设计这个程序时，我们完全可以提取一个公共的 email client，让 httpTrigger 入口函数调用 client 即可：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> emailClient <span class="hljs-keyword">from</span> <span class="hljs-string">"./email-client"</span>;
 
<span class="hljs-keyword">const</span> httpTrigger: AzureFunction = <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context: Context, req: HttpRequest</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">void</span>> </span>&#123;
 
<span class="hljs-comment">// ...</span>
<span class="hljs-keyword">await</span> emailClient.send(email);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么在迁移的过程中，入口函数几乎无需改动，更改只发生在 client 中，我们也只需对 client 重新测试验证即可。如果你使用的是 C#，我们甚至可以将 EmailClient 抽象为一个接口注入后使用。说白了我们又回到了分离关注点，甚至可以说是六边形架构的老路。</p>
<p>针对接口编程还有一个优势——便于我们进行组件测试。</p>
<p>我们可以把上面的流程扩展一下，再被 trigger 之后首先需要从 KeyVault 中获取用于使用 SendGrid 的 API_KEY，在发送完毕 SendGrid 之后再使用 Application Insights 记录日志，流程如下图所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bb444e01303415bab68e8815b000673~tplv-k3u1fbpfcp-watermark.image" alt="e2e-test.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可能有兴趣对虚线框内整套功能进行E2E（端到端）测试，这并非无法实现，但是难且代价极大。它的难首先体现在E2E本身的测试性质上，如果你对测试金字塔还有印象的话，处于金字塔顶端的 E2E 测试无论是运行成本还是维护成本都是最高的；其次由于 serverless 第三方提供服务的差异性，你很难在每个人的本地搭建出一套线下稳定的测试环境来，由此产生的不确定和对线上环境的依赖有悖于我们对于测试能够快速反馈和重复执行的期望。</p>
<p>所以我建议在 serverless 中从代码中抽象出<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmartinfowler.com%2FeaaCatalog%2FserviceLayer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://martinfowler.com/eaaCatalog/serviceLayer.html" ref="nofollow noopener noreferrer">服务层（Service Layer）</a>，优先针对服务层进行测试。服务层是应用的边界和对业务逻辑和用例的封装，即使发生技术栈迁移它也应该是最不被影响的功能，它应该作为测试中的一个风险点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56a01bd00dfc44c5bc0608b6f2abfc8b~tplv-k3u1fbpfcp-watermark.image" alt="component-test.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而服务层打交道的对象不再是具体的供应商服务而是抽象的接口，这也便于我们在针对服务层的测试中对依赖进行 mock，优化测试流程。</p>
<h2 data-id="heading-4">Serverless 里的旧酒</h2>
<h3 data-id="heading-5">身份验证</h3>
<p>无论你使用什么样的技术栈，微服务、Serverless、Low-Code 等等，认证（Authentication）和授权（Authorization）始终是你无法逃避的问题。但不同技术栈下解决授权问题的模式并无不同。在这里先统一一下语言，以下用“验证”同时代指“认证”和“授权”。</p>
<p>以微服务架构为例，服务于接口背后的每一组微服务不可能都拥有独立的验证机制。如果你执意这么做的话需要解决不仅限于以下的问题：</p>
<ul>
<li>如果每一组微服务有需要共享的验证逻辑，那么将相似的代码散布在不同的代码库中的做法会在将来带来散弹式修改的成本</li>
<li>具体的业务发开人员需要学习它们本不应该关心的认证逻辑，暴露出去的认证代码难免与业务代码耦合</li>
<li>如果在访问每一组微服务之前都要验证一次权限，势必整体会增加我们的系统延迟以及带来重复工作。</li>
</ul>
<p>所以通常我们会在系统的边界（Edge Layer）进行验证。我们对边界外的一切调用保持怀疑态度，对边界内的服务无条件信任，这被公认为业内的最佳实践。</p>
<p>而这种边界在现代企业架构中的化身就是 API Gateway。值得强调的是身份验证只是 API Gateway 承担的其中一项职责，实际上 API Gateway 能做的远不止于此。</p>
<p>AWS Lambda 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.aws.amazon.com%2Fzh_cn%2Fapigateway%2Flatest%2Fdeveloperguide%2Fapigateway-use-lambda-authorizer.html" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.aws.amazon.com/zh_cn/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html" ref="nofollow noopener noreferrer">官方验证机制</a>亦是如此：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10275b5e29334713b99ad5f99f9ce2fa~tplv-k3u1fbpfcp-watermark.image" alt="custom-auth-workflow.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上图中最左侧的 client 的请求必须经过 API Gateway 的验证之后才可以继续访问后续的 Lambda 或者是 EC2 服务。</p>
<p>在回答了“在哪里验证”这个问题之后，借上面的流程我们要继续回答第二个问题：如何验证。</p>
<p>鉴于上面论述的每个服务/函数都不应该各自实现一遍验证功能，AWS API Gateway 为我们准备了验证机制 custom authorizer （也可以称之为 lambda authorizer，因为 authorizer 由 lambda 函数实现），它的工作原理如下：</p>
<ul>
<li>当客户端请求到达 API     Gateway 时，authorizer 函数可以从请求中获取到用于验证的关键信息，比如 JWT</li>
<li>假设客户端使用的是 Auth0 进行登陆，authorizer     则需要将 JWT 交由 Auth0 进行验证</li>
<li>如果验证成功，authorizer 便会返回对应的 policy，API     Gateway 根据 policy 来决定时许允许访问后续资源</li>
</ul>
<p>从上述流程中不难看出验证通过与否决定自 authorizer 的代码实现。但无论你是利用 JWT还是 SAML 进行验证，背后遵循的依然是传统 OAuth 的经典流程。我不想对 OAuth 着过多笔墨，下面的流程图也许能唤起你的不少回忆</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60692e3ea7b34b84a75d47b6a79a1ffe~tplv-k3u1fbpfcp-watermark.image" alt="oauth-workflow.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上述 AWS 的身份验证流程中，当 client 在向 AWS Lambda 发送请求时，我们首先需要向 Authorization Server 验证身份之后才允许将资源返回给 client。不难看出 authorizer 是流程图中步骤 6 的体现</p>
<p>我要对潜在的“错误”做一个解释：你可能会认为 OAuth 并不适用于 AWS API Gateway 这类情况，因为 OAuth 本质上是针对“授权”操作设计的，即决定你能够访问哪些资源；而 API Gateway 的例子像是“认证”场景，即你是否是合法用户。</p>
<p>你对于 OAuth 的理解是对的，借此我们不妨继续对 OAuth 进行一次深入说明：OAuth 实质上是一则委托协议，它开放了软件程序以用户的姿态访问第三方资源的一种可能。OAuth 中的 client 不是指拥有这些资源的用户，而是被用户委托的应用程序，比如再网易相册需要访问用户的谷歌网盘里的照片的场景中，client 其实代指的是网易相册。正因为它只关心授权资源，所以它可以不用关心谁以及用什么方式授权的这些资源。残酷点说网易相册只关心它是否能够获取到允许它调用 Google API 拿到文件信息 token 而已。</p>
<p>回到 API Gateway 的例子中，API 所代表的资源通常是公用的，自然作为资源拥有方的 AWS 无需关心背后的 client 是谁，也无权限制用户可能授权给多少个应用，它只关心请求里的验证凭据。从这个角度上说，lambda 的验证工作与 OAuth 不谋而合。</p>
<p>如果对 OAuth 再做一次抽象的话，我们可以将它称之为“基于 token 的身份验证机制（token-based authentication）”。和传统的用户名密码授权验证方式相比会带来以下优势：</p>
<ul>
<li>因为不用把用户名和密码暴露给客户，安全性得到提升</li>
<li>限定访问期限，支持随时撤销访问权限</li>
<li>细粒度的控制用户可访问的资源</li>
</ul>
<p>例如 Azure Serverless 就支持存粹基于 token 的验证方式，在你将 HttpTrigger 的 authLevel 参数设置为 function 之后，需要从 UI 上获取 Function Key 值并将其放入名为 x-function-key 的 http header 中才得以让请求抵达 function，否则</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3db925a31c1549198e2ca9a4711bea65~tplv-k3u1fbpfcp-watermark.image" alt="azure-function-keys.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出在解决 serverless 场景下的身份验证问题时，我们仰仗的依然是前人留下的宝贵财富。</p>
<h3 data-id="heading-6">部署 Serverless</h3>
<p>最后简短的提一下 Serverless 的部署问题</p>
<p>灵活和轻量是 serverless 主打的卖点之一，超级便捷的部署方式便是这一系列特性的最佳体现。例如 AWS 支持通过上传 zip 文件部署 Lambda；Firebase 支持通过 CLI 部署 Cloud Function；而 Azure Serverless 则为 VSCode 开发了 Azure Functions 插件，允许你在 IDE 中开发过程中一键部署 Azure Function。</p>
<p>如果你对这些手段的改进仅仅理解为免去了繁琐的步骤便于我们可以更快速的将代码部署到生产环境的话，那么我建议你还是不要使用这些手段为妙。因为在软件交付的过程中纯手工的部署行为是一类反模式行为：这种一步到位的手工部署意味着你必须用手工测试的方式验证功能是否正常，同时未经试运行环境的检测而直接部署到生产环境的话，会导致我们无法验证在开发环境中产生的假设在生产环境中是依然成立的，甚至在发生问题之后没有配套机制保证我们的代码回滚到上一个稳定版本。我们可以引用《持续交付》一书中的话对理想中的持续交付进行归纳：软件发布能够（也应该）成为一个低风险、频繁、廉价、迅速且可预见的过程。</p>
<p>所以 serverless 的交付环节依然需要被管理，例如配置管理、编译、自动化测试、灰度发布等等过程对 serverless 仍然适用。那为什么 serverless 服务商不继续迈出一步为我们提供更丰富的交付解决方案呢？这个问题的答案既是肯定的也是否定的。</p>
<p>肯定回答的理由是，现有平台工具早已支持我们达成此类目标。例如 Azure DevOps 平台支持我们为 serverless 应用创建 pipeline 以及管理每一次构建后的 artifact； Azure Serverless 也支持灰度发布（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fazure-functions%2Ffunctions-deployment-slots" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots" ref="nofollow noopener noreferrer">Deployment slots</a>），你可以选择首先将构建后的代码首先发布到 staging 环境上，待验证无误后一键将现存的 production 代码替换。</p>
<p>而否定答案也同样成立的理由是因为所有这些配套设施都并非只为 serverless 精心定制，几乎所有 Azure 提供的服务都能通过 Azure DevOps 平台进行部署，所有服务在Azure DevOps 上被一视同仁对待。</p>
<p>所以不难看出 Azure DevOps 出售的并不是预置好的标准化流程，而是支持定制化的公共能力。它们之所以止步于此不是因为代编码能力有限，而是因为无法在代码层面做进一步抽象。</p>
<p>如果你对编码稍有经验的话，你应该明白在软件开发中最困难的不是编码环节，而是在于前期的程序设计，以及将各类模式恰如其分的融入其中。然而你也应该理解，哪怕是耳熟能详的 MVC 模式，在不同编程语言下的含义也不尽相同，甚至在同一种编程语言下实现也可以不同（例如 Angular 的双向绑定模式之于 Backbone.js 的事件机制）。我们无法用一成不变的代码精准对其定义。</p>
<p>持续交付知识也具有类似的性质，大部分时候我们需要有的放矢的为项目设计交付流程。例如为团队选择恰当的 Git 工作流，判断是否有必要为项目添加冒烟测试等等。这些都是无法通过代码计算出来的，这部分工作往往也是最难的，因为你需要对项目进行评估以及团队沟通之后才能将方案确定下来。正是因为 DevOps 环节里存在太多不确定因素，项目之间千差万别，平台能做的也只能是在众多因素之间寻找最大公约数（所有的项目都需要部署，都需要灰度发布，都需要环境变量管理），又或者将把所有可能性打包作为公共能力提供给你（比如 Azure DevOps 平台）</p>
<h2 data-id="heading-7">尾声</h2>
<p>因为篇幅的关系我们只能谈论到这里，希望你能从上述的文字中勾勒出一个有关 serverless 更清晰的轮廓。我们很难说服自己 serverless 是一类纯粹的革新，它更多的包含了前人智慧结晶。但无需沮丧，这是技术创新的常态，创新不是空中楼阁，它只有继承自经典，才有可能超越经典。</p>
<p>本文同时发布在我的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fcolumn%2Ffront-end" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/column/front-end" ref="nofollow noopener noreferrer">知乎专栏：前端技术漫游指南</a>，欢迎订阅</p></div>  
</div>
            