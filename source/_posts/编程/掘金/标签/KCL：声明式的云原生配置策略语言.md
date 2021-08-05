
---
title: 'KCL：声明式的云原生配置策略语言'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d13ce442a634194a6656b4ed4843091~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 00:47:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d13ce442a634194a6656b4ed4843091~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d13ce442a634194a6656b4ed4843091~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p>楔子: 以蚂蚁典型的建站场景为例，在接入 Kusion 后，用户侧配置代码减少到 5.5%，用户面对的 4 个平台通过接入统一代码库而消减，在无其他异常的情况下交付时间从 2 天下降到 2 小时……</p>
</blockquote>
<blockquote>
<p>注：本文是柴树杉在 2021 GIAC 大会上分享的内容。相关 PPT 内容请点击下方自行下载</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgw.alipayobjects.com%2Fos%2Fbmw-prod%2F2cb0c283-5f24-485e-b635-b6efac887eba.pdf" target="_blank" rel="nofollow noopener noreferrer" title="https://gw.alipayobjects.com/os/bmw-prod/2cb0c283-5f24-485e-b635-b6efac887eba.pdf" ref="nofollow noopener noreferrer">GIAC 大会 PPT 下载：KCL声明式的云原生配置策略语言 </a></p>
<h2 data-id="heading-0">0. 你好GIAC</h2>
<p>大家好，我是来自蚂蚁的同学，很高兴能在GIAC的编程语言新范式板块和大家分享《KCL配置策略语言》。KCL语言是蚂蚁内部的Kusion解决方案中针对云原生基础设施配置代码化自研的DSL语言，目前已经在建站场景等一些场景开始小范围推广试用。</p>
<p>我们先看一下简单的KCL代码：</p>
<pre><code class="hljs language-python copyable" lang="python">schema GIACInvitation[name: <span class="hljs-built_in">str</span>]:
Name:     <span class="hljs-built_in">str</span> = name
Topic:    <span class="hljs-built_in">str</span> = <span class="hljs-string">"分享主题"</span>
Company?: <span class="hljs-built_in">str</span> = <span class="hljs-literal">None</span>
<span class="hljs-type">Type</span>:     <span class="hljs-built_in">str</span> = <span class="hljs-string">"分享嘉宾"</span>
Address:  <span class="hljs-built_in">str</span> = <span class="hljs-string">"深圳"</span>

invitation = GIACInvitation(<span class="hljs-string">"姓名"</span>) &#123;
Topic:   <span class="hljs-string">"KCL配置策略语言"</span>
Company: <span class="hljs-string">"蚂蚁集团"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子代码先通过 <code>schema</code> 定义了一个 <code>GIACInvitation</code> 结构体：该结构体有一个 <code>str</code> 类型的 <code>name</code> 参数，同时还有一组标注了类型和默认值的属性。然后通过声明式的语法构造了<code>GIACInvitation</code> 的实例 <code>invitation</code>。</p>
<p>这个例子虽然简单，但是包含了 KCL 最重要的 schema 语言结构。从例子可以看出 KCL 尝试通过声明式的语法、静态类型检查特性来改进配置代码的编写和维护工作。这也是设计 KCL 语言的初衷，我们希望通过编程领域成熟的技术理论来解决云原生领域的配置代码化的问题。</p>
<h2 data-id="heading-1">1. KCL语言的诞生背景</h2>
<p>在经典的 Linux/UNIX 操作系统中，我们通过 Shell 和系统内置的各种工具和内核进行交互，同时通过 Shell 脚本来管理更上层的 App。可以说 Shell 语言极大地简化了内核的编程界面，不仅仅提升了操作系统易用性也简化了上层 App 的管理和运维，也提高了生产效率。而 Kubernetes 作为容器管理领域的事实标准，已经成为云计算时代的Linux/UNIX。类比 UNIX 系统，Kubernetes 目前还缺少一种符合其声明式、开放、共享设计理念的交互语言及工具。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2255f8ca582944e78c71eb8c9e2d7c45~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-2">1.1 为何要设计KCL语言？</h3>
<p>K8s已经成为云计算的操作系统，但是目前尚缺少功能完备的SHELL交互界面。目前虽然有很多而且开源方案，但是还没有像UNIX的Shell那种出现比较成熟的方案，特别是尚无法满足头部互联网企业大规模工程化的要求。云原生技术与企业落地之间存在Gap需要填补，这正是云原生工程化要解决的问题，也是设计KCL语言的出发点。</p>
<h3 data-id="heading-3">1.2 目前是一个好时机</h3>
<p>云原生的思路是高度的开放化和民主化，结果就是万物可配置，一切配置都是代码。带配置代码面前人人平等，每个用户都可以通过调整配置代码和基础平台设施进行交互。因此对配置的编写和维护正在成为云计算时代软件工程师的必备的技能和需求。基于对云原生配置代码化需求的日益旺盛，硅谷的诸多头部公司已经对这个方向进行了大规模的实践和验证，这些都给了我们大量可以参考的经验。</p>
<p>因此蚂蚁的 Kusion 项目尝试通过 KCL 配置策略语言正是为了简化云原生技术设施的接入方式设计，其设计目标不仅仅是为了提升蚂蚁基础设施的开放程度及使用效率，同时希望能够优化共享、协同的开发流程，可以说其定位正是云原生时代的 Shell 语言。虽然目前还处于探索和实践阶段，我们通过此文和大家分享下 KCL 语言的设计与实现的一些理念，为云原生的快速到来贡献一点绵薄之力。</p>
<h3 data-id="heading-4">1.3 KCL诞生历史</h3>
<p>KCL 语言从2019年开始初期的调研和设计工作。到2020年3月发布kcl-0.1，基于Python定制语法，采用Go版本的Grumpy和AntLR等工具开发。2020年下半年改用Python语言并加快了开发和迭代速度，发布的kcl-0.2.x引入了大量语言特性、增加了Plugin扩展支持、同时支持IDEA插件。2021年上半年开始统一优化和整合语言特性，发布的kcl-0.3优化类型系统、集成单元测试工具、优化执行性能并提供了Go等多语言的API支持、同时通过LSP为VSCode提供支持。2021年下半年开始在建站等常见落地，同时引入静态类型检查和优化性能，完善语言的文档支持。</p>
<h2 data-id="heading-5">2. KCL语言的设计原则</h2>
<p>基于蚂蚁践行多年的经典运维中台沉淀的经验和对各种问题利弊的思考，Kusion 项目对如何充分利用云原生技术带来的红利，打造一个开放、透明、声明式、可协同的运维体系进行了探索和思考，提出并实践了基于基础设施代码化的云原生协同开发的模型。而 KCL 语言正是 Kusion 项目为了解决云原生协同开发而设计的声明式的配置编程语言，简单、稳定、高效和工程化是 KCL 语言设计的设计理念。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e39be894f5746708d8cf195247840b2~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-6">2.1 简单为王</h3>
<p>简单不仅仅可以降低学习和沟通的成本，而且可以减少代码出问题的风险。不论是 UNIX 奉行的 KISS 原则还是 Go语言推崇的 Less is more 设计理念，简化易用的界面始终是各种成功产品追求的一个目标。同样从简单原则出发，KCL 语言在参考现代编程语言之上只保留了必要的元素，同时通过类型自动推导、引入受限的控制流和 schema 提供了基础灵活的配置定义编写能力，删减语言特性始终是 KCL 语言设计工作的一个重要目标。</p>
<h4 data-id="heading-7">2.1.1 声明式语法</h4>
<p>声明式编程是和命令式编程并列的一种编程范式，声明式编程只告诉你想要的结果，执行引擎负责执行的过程。声明式编程使用更加简单，可以降低命令式拼装造成的复杂性和副作用，保持配置代码清晰可读，而复杂的执行逻辑已经由 Kubernetes 系统提供支持。KCL 语言通过简化对 schema 结构体实例化的语法结构对声明式语法提供支持，通过仅提供少量的语句来减少命令过程式编程带来的复杂性。 围绕 schema 和配置相关的语法，KCL 希望每种配置需求尽可能通过固定的写法完成，使得配置代码尽可能的统一化。</p>
<p>比如作为 KCL 声明式语法的核心结构 schema 可以采用声明式方式实例化：</p>
<pre><code class="hljs language-python copyable" lang="python">schema Name:
    firstName: <span class="hljs-built_in">str</span>
    lastName: <span class="hljs-built_in">str</span>

schema Person:
    name: Name = &#123;
        firstName: <span class="hljs-string">"John"</span>
        lastName: <span class="hljs-string">"default"</span>
    &#125;

JohnDoe = Person &#123;
    name.lastName: <span class="hljs-string">"Doe"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先通过schema定义了一个 Name 结构，结构包含2个字符串类型的必填属性。然后在 Person 中复用 Name 类型声明一个name属性，并且给name属性设置了默认值以简化用户使用。最终在定义 JohnDoe 配置定义的时候，只需填写 name.lastName 一个属性参数即可，其他部分属性均采用默认的参数。</p>
<p>对于一些标准的业务应用，通过将可复用的模型封装为 KCL schema，这样可以为前端用户提供最简单的配置界面。比如基于蚂蚁内部Konfig大库中 sofa.SofaAppConfiguration 只需添加少量的配置参数就可以定制一个 App</p>
<pre><code class="hljs language-python copyable" lang="python">appConfiguration = sofa.SofaAppConfiguration &#123;
    resource: resource.Resource &#123;
        cpu: <span class="hljs-string">"4"</span>
        memory: <span class="hljs-string">"8Gi"</span>
        disk: <span class="hljs-string">"50Gi"</span>
    &#125;
    overQuota: <span class="hljs-literal">True</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过声明式语法描述必要的参数（其他的参数全部采用默认配置），可以极大简化普通用户的配置代码。</p>
<h4 data-id="heading-8">2.1.2 顺序无关语法</h4>
<p>有别于命令式编程，KCL 推崇的是更适合于配置定义的声明式语法。以斐波那契数列为例，可以把一组声明式的定义看作一个方程组，方程式的编写顺序本质上不影响方程组的求解，而计算属性依赖并“求解”的过程由 KCL 解释器完成，这样可以避免大量命令式拼装过程及顺序判断代码。</p>
<pre><code class="hljs language-python copyable" lang="python">schema Fib:
    n1: <span class="hljs-built_in">int</span> = n - <span class="hljs-number">1</span>
    n2: <span class="hljs-built_in">int</span> = n1 - <span class="hljs-number">1</span>
    n: <span class="hljs-built_in">int</span>
    value: <span class="hljs-built_in">int</span>

    <span class="hljs-keyword">if</span> n <= <span class="hljs-number">1</span>:
        value = <span class="hljs-number">1</span>
    <span class="hljs-keyword">elif</span> n == <span class="hljs-number">2</span>:
        value = <span class="hljs-number">1</span>
    <span class="hljs-keyword">else</span>:
        value = (Fib &#123;n: n1&#125;).value + (Fib &#123;n: n2&#125;).value

fib8 = (Fib &#123;n: <span class="hljs-number">8</span>&#125;).value  <span class="hljs-comment"># 21</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中 Fib 定义的成员n、n1和n2有一定的依赖关系，但是和它们书写的顺序并无关系。KCL 语言引擎会根据声明式代码中的依赖关系自动计算出正确的执行顺序，同时对类似循环引用等异常状态告警。</p>
<h4 data-id="heading-9">2.2.3 同名配置合并</h4>
<p>当整个业务和开发维护团队都变得复杂时，配置代码的编写和维护也将变得复杂化：同一份配置参数可能散落在多个团队的多个模块中，同时一个完整的应用配置则需要合并这些散落在不同地方的相同和不同配置参数才可以生效，而相同的配置参数可能因为不同团队的修改而产生冲突。通过人工方式同步这些同名配置和合并不同的配置都是一个极大的挑战。</p>
<p>比如 Konfig 大库中应用配置模型分为 base 和各环境 stack 配置，要求程序运行时按照某一 merge 策略合并为一份应用配置，相当于要求大库前端配置能够自动合并，即能够分开多次定义并且合并，然后实例化生成相应的唯一前端配置。借助 KCL 语言的能力和 Konfig 的最佳实践，可通过将基线配置和环境配置自动合并简化配置的编写。比如对于标准 SOFA 应用 opsfree，其基线配置和环境配置分别维护，最终交由平台工具进行配置合并和检查。KCL 语言通过自动化合并同名配置实现简化团队协同开发的设计目标。</p>
<p>比如 base 配置收集的通用的配置：</p>
<pre><code class="hljs language-python copyable" lang="python">appConfiguration = sofa.SofaAppConfiguration &#123;
    mainContainer: container.Main &#123;
        readinessProbe: probe_tpl.defaultSofaReadinessProbe
    &#125;
    resource: res_tpl.medium
    releaseStrategy: <span class="hljs-string">"percent"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再预发环境在 base 配置的基础之上针对某些参数进行微调：</p>
<pre><code class="hljs language-python copyable" lang="python">appConfiguration = sofa.SofaAppConfiguration &#123;
    resource: resource.Resource &#123;
        cpu: <span class="hljs-string">"4"</span>
        memory: <span class="hljs-string">"8Gi"</span>
        disk: <span class="hljs-string">"50Gi"</span>
    &#125;
    overQuota: <span class="hljs-literal">True</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>合并的 pre 配置实际是一份 SofaAppConfiguration 配置（相当于如下等效代码，环境配置的优先级默认高于基线配置）</p>
<pre><code class="hljs language-python copyable" lang="python">appConfiguration = sofa.SofaAppConfiguration &#123;
    mainContainer: container.Main &#123;
        readinessProbe: probe_tpl.defaultSofaReadinessProbe
    &#125;
    resource: resource.Resource &#123;
        cpu: <span class="hljs-string">"4"</span>
        memory: <span class="hljs-string">"8Gi"</span>
        disk: <span class="hljs-string">"50Gi"</span>
    &#125;
    overQuota: <span class="hljs-literal">True</span>
    releaseStrategy: <span class="hljs-string">"percent"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前的同名配置虽然只针对应用的主包配置有效，但已经带来了可观察的收益。</p>
<h3 data-id="heading-10">2.2 稳定压倒一切</h3>
<p>越是基础的组件对稳定性要求越高，复用次数越多的稳定性带来的收益也更好。因为稳定性是基础设施领域一个必备的要求，不仅仅要求逻辑正确，而且需要降低错误出现的几率。</p>
<h4 data-id="heading-11">2.2.1 静态类型和强不可变性</h4>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20b6002014c84022a29b61403cd2b884~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>很多配置语言采用运行时动态检查类型。动态类型最大的缺点只能检查正在被执行属性的类型，这非常不利于开发阶段提前发现类型的错误。静态类型不仅仅可以提前分析大部分的类型错误，还可以降低后端运行时的动态类型检查的性能损耗。</p>
<p>除了静态类型，KCL 还通过 final 关键字禁止某些重要属性被修改。静态类型再结合属性的强不可变性，可以为配置代码提供更强的稳定性保障。 比如对于 CafeDeployment 中的 apiVersion 信息是一种常量类型的配置参数，final 为这类配置提供保障：</p>
<pre><code class="hljs language-python copyable" lang="python">schema CafeDeployment:
    final apiVersion: <span class="hljs-built_in">str</span> = <span class="hljs-string">"apps.cafe.cloud.alipay.com/v1alpha1"</span>
    final kind: <span class="hljs-built_in">str</span> = <span class="hljs-number">123</span>  <span class="hljs-comment"># 类型错误</span>

schema ContainerPort:
    containerPort: <span class="hljs-built_in">int</span> = <span class="hljs-number">8080</span>
    protocol: <span class="hljs-string">"TCP"</span> | <span class="hljs-string">"UDP"</span> | <span class="hljs-string">"SCTP"</span> = <span class="hljs-string">"TCP"</span>
    ext? : <span class="hljs-built_in">str</span> = <span class="hljs-literal">None</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中 apiVersion 和 kind 属性都被 final 保护禁止被修改。但是 kind 因为属性类型初始值不同而隐含一个错误，通过静态类型检查很容易在开发阶段发现错误并改正。</p>
<h4 data-id="heading-12">2.2.2 运行时类型和逻辑check验证</h4>
<p>KCL 的 schema 不仅仅是带类型的结构体，也可以用于在运行时校验存量的无类型的 JSON 和 YAML 数据。此外 schema 的 check 块可以编写语义检查的代码，在运行时实例化 schema 时会自动进行校验。同时，基于 schema 的继承和 mixin 可以产生跟多关联的 check 规则。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72f344c025774ae8812e66c2e3fab3be~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>比如以下的例子展示 check 的常见用法：</p>
<pre><code class="hljs language-python copyable" lang="python">schema sample:
    foo: <span class="hljs-built_in">str</span>
    bar: <span class="hljs-built_in">int</span>
    fooList: [<span class="hljs-built_in">str</span>]

    check:
        bar > <span class="hljs-number">0</span> <span class="hljs-comment"># minimum, also support the exclusive case</span>
        bar < <span class="hljs-number">100</span>, <span class="hljs-string">"message"</span> <span class="hljs-comment"># maximum, also support the exclusive case</span>
        <span class="hljs-built_in">len</span>(fooList) > <span class="hljs-number">0</span> <span class="hljs-comment"># min length, also support exclusive case</span>
        <span class="hljs-built_in">len</span>(fooList) < <span class="hljs-number">100</span> <span class="hljs-comment"># max length, also support exclusive case</span>
        regex.match(foo, <span class="hljs-string">"^The.*Foo$"</span>) <span class="hljs-comment"># regex match</span>
        isunique(fooList) <span class="hljs-comment"># unique</span>
        bar <span class="hljs-keyword">in</span> [<span class="hljs-built_in">range</span>(<span class="hljs-number">100</span>)] <span class="hljs-comment"># range</span>
        bar <span class="hljs-keyword">in</span> [<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">6</span>, <span class="hljs-number">8</span>] <span class="hljs-comment"># enum</span>
        multiplyof(bar, <span class="hljs-number">2</span>) <span class="hljs-comment"># multipleOf</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>check 中每个语句都是一个可以产生 bool 结果的表达式和可选的错误信息组成（每个普通的 bool 表达式其实是assert 语句的简化而来）。通过内置的语法和函数可以实现在运行时对属性值的逻辑验证。</p>
<h4 data-id="heading-13">2.2.3 内置测试支持</h4>
<p>单元测试是提升代码质量的有效手段。KCL 基于已有的 schema 语法结构，配合一个内置 kcl-test 命令提供灵活的单元测试框架（结合 testing 包可指定面值类型的命令行参数）。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/572aab6f2aec48779e3d0f7cc1c909ec~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>内置测试工具</p>
<pre><code class="hljs language-python copyable" lang="python">schema TestPerson:
    a = Person&#123;&#125;
    <span class="hljs-keyword">assert</span> a.name == <span class="hljs-string">'kcl'</span>

schema TestPerson_age:
    a = Person&#123;&#125;
    <span class="hljs-keyword">assert</span> a.age == <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>kcl-test 命令不仅仅执行单元测试，还会统计每个测试执行的时间，而且可以通过正则表达式参数选择执行指定的测试。此外通过 <code>kcl-test ./...</code> 可以递归执行子目录的单元测试，同时支持集成测试和Plugin测试。</p>
<h3 data-id="heading-14">2.3 高效是永恒的追求</h3>
<p>KCL 代码不仅仅通过声明式的风格简化编程，同时通过模块支持、mixin 特性、内置的 lint 和 fmt 工具、以及 IDE 插件提供高效的开发体验。</p>
<h4 data-id="heading-15">2.3.1 schema 中好用的语法</h4>
<p>schema 是 KCL 编写配置程序的核心语法结构，其中几乎每个特性均是针对具体的业务场景提效而设计。比如在定义和实例化深层次嵌套的配置参数时，均可以直接指定属性的路径定义和初始化。</p>
<pre><code class="hljs language-python copyable" lang="python">schema A:
    a: b: c: <span class="hljs-built_in">int</span>
    a: b: d: <span class="hljs-built_in">str</span> = <span class="hljs-string">'abc'</span>

A &#123;
    a.b.c: <span class="hljs-number">5</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时为了安全，对于每个属性默认都是非空的字段，在实例化时会自动进行检查。</p>
<p>schema 不仅仅是一个独立的带类型注解的配置对象，我们也可以通过继承的方式来扩展已有的 schema：</p>
<pre><code class="hljs language-python copyable" lang="python">schema Person:
    firstName: <span class="hljs-built_in">str</span>
    lastName: <span class="hljs-built_in">str</span>

<span class="hljs-comment"># schema Scholar inherits schema Person</span>
schema Scholar(Person):
    fullName: <span class="hljs-built_in">str</span> = firstName + <span class="hljs-string">'_'</span> + lastName
    subject: <span class="hljs-built_in">str</span>

JohnDoe = Scholar &#123;
    firstName: <span class="hljs-string">"John"</span>,
    lastName: <span class="hljs-string">"Doe"</span>,
    subject: <span class="hljs-string">"CS"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中 Scholar 从 Person 继承，然后又扩展了一些属性。作为子类的 Scholar 可以直接访问父类中定义的firstName 等属性信息。</p>
<p>继承是 OOP 编程中基础的代码复用手段，但同时也有多继承导致的菱形继承的技术问题。KCL 语言刻意简化了继承的语法，只保留了单继承的语法。同时 schema 可以通过 mixin 特性混入复用相同的代码片段，对于不同的能力配套，我们通过 mixin 机制编写，并通过 mixin 声明的方式“混入”到不同的结构体中。</p>
<p>比如通过在 Person 中混入 FullnameMixin 可以给 schema 增加新的属性或逻辑（包括 check 代码块）：</p>
<pre><code class="hljs language-python copyable" lang="python">schema FullnameProtocol:
    firstName : <span class="hljs-built_in">str</span> = <span class="hljs-string">"default"</span>
    lastName : <span class="hljs-built_in">str</span>

mixin FullnameMixin <span class="hljs-keyword">for</span> FullnameProtocol:
    fullName : <span class="hljs-built_in">str</span> = <span class="hljs-string">"$&#123;firstName&#125; $&#123;lastName&#125;"</span>

schema relax Person:
    mixin [FullnameMixin]
    firstName : <span class="hljs-built_in">str</span> = <span class="hljs-string">"default"</span>
    lastName : <span class="hljs-built_in">str</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 KCL 的语言能力，平台侧同学可以通过单继承的方式扩展结构体，通过 mixin 机制定义结构体内属性的依赖关系及值内容，通过结构体内顺序无关的编写方式完成声明式的结构体定义，此外还支持如逻辑判断、默认值等常用功能。</p>
<h4 data-id="heading-16">2.3.2 doc、fmt、lint和外围的LSP工具</h4>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1deef1617f054595bc12bc6e1e60f693~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>在编程领域代码虽然是最核心的部分，但是代码对应的文档和配套的工具也是和编程效率高度相关的部分。策略设计哲学并不局限于语言本身，还包括文档、代码格式化工具、代码风格评估工具和IDE的支持等。KCL 通过 kcl-doc 支持从配置代码直接提取产生文档，自动化的文档不仅仅减少了手工维护的成本，也降低的学习和沟通成本。kcl-fmt 则很方便将当前目录下的全部代码（包含嵌套的子目录）格式化为唯一的一种风格，而相同格式的代码同样降低的沟通和代码评审的成本。kcl-lint 工具则是通过将一些内置的风险监测策略对 KCL 代码平行评估，方便用户根据评估结果优化代码的风格。</p>
<h3 data-id="heading-17">2.4 工程化的解决方案</h3>
<p>任何语言想要在工程中实际应用，不仅仅需要很好的设计，还需要为升级、扩展和集成等常规的场景提供完整的解决方案。</p>
<h4 data-id="heading-18">2.4.1 多维度接口</h4>
<blockquote>
<p><img src="https://gw.alipayobjects.com/mdn/rms_1c90e8/afts/img/A*sCtjT6rBtXIAAAAAAAAAAAAAARQnAQg" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>KCL语言设计通过在不同的抽象层次为普通用户（KCL命令行）、KCL语言定制者（Go-API、Python-API）、KCL库扩展者（Plugin）和IDE开发者（LSP服务）均提供了几乎等价的功能界面，从而提供了最大的灵活度。</p>
<h4 data-id="heading-19">2.4.2 千人千面的配置DB</h4>
<p>KCL 是面向配置的编程语言，而配置的核心是结构化的数据。因此，我们可以将完整 KCL 代码看做是一种配置数据库。通过 KCL 的配置参数的查询和更新（override/-O命令）可以和对应的配置属性路径，可以实现对属性参数的查询、临时修改和存盘修改。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3138a1654044eafa6ed58c2b2a0f661~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>将代码化的配置作为DB的唯一源，不仅仅可以集成DB领域成熟的查询和分析手段，而且可以通过配置代码视角调整配置代码的逻辑结构。特别是在自动化运维实践中，通过程序自动生成的配置代码修改的PullRequest可以方便引入开发人员进行代码评审，很好地达到人机通过不同界面配合运维。</p>
<h4 data-id="heading-20">2.4.3 版本平滑升级</h4>
<p>随着业务和代码的演化，相关模块的 API 也会慢慢腐化。KCL 语言设计通过严格的依赖版本管理，然后结合语言内置的语法和检查工具保障 API 平滑的升级和过渡，再配合代码集成测试和评审流程提升代码安全。KCL 语言通过@deprecated特性在代码出现腐化早期给出提示，同时为用户的过渡升级留出一定的时间窗口，甚至等到API彻底腐烂前通过报错的方式强制要求同步升级相关的代码。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3dde1c6e922452f879aee075ae4e66c~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>比如在某次升级中，name 属性被 fullName 替代了，则可以通过@deprecated特性标志：</p>
<pre><code class="hljs language-python copyable" lang="python">schema Person:
<span class="hljs-meta">    @deprecated(<span class="hljs-params">version=<span class="hljs-string">"1.1.0"</span>, reason=<span class="hljs-string">"use fullName instead"</span>, strict=<span class="hljs-literal">True</span></span>)</span>
    name: <span class="hljs-built_in">str</span>
    ... <span class="hljs-comment"># Omitted contents</span>

person = Person &#123;
    <span class="hljs-comment"># report an error on configing a deprecated attribute</span>
    name: <span class="hljs-string">"name"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在实例化 Person 时，name 属性的初始化语句将会及时收到报错信息。</p>
<h4 data-id="heading-21">2.4.4 内置模块、KCL模块、插件模块</h4>
<p>KCL 是面向配置的编程语言，通过内置模块、KCL 模块和插件模块提供工程化的扩展能力。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a00bb58c8ab242dd8aaf6894f69fa239~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>用户代码中不用导入直接使用 builtin 的函数（比如用 len 计算列表的长度、通过 typeof 获取值的类型等），而对于字符串等基础类型也提供了一些内置方法（比如转化字符串的大小写等方法）。对于相对复杂的通用工作则通过标志库提供，比如通过 import 导入 math 库就可以使用相关的数学函数，可以通过导入 regex 库使用正则表达式库。而针对 KCL 代码也可以组织为模块，比如 Konfig 大库中将基础设施和各种标准的应用抽象为模块供上层用户使用。此外还可以通过 Plugin 机制，采用 Python 为 KCL 开发插件，比如目前有 meta 插件可以通过网络查询中心配置信息，app-context 插件则可以用于获取当前应用的上下文信息从而简化代码的编写。</p>
<h2 data-id="heading-22">3. KCL语言的实现原理</h2>
<h3 data-id="heading-23">3.1 整体架构</h3>
<p>KCL 虽然作为一个专用于云原生配置和策略定义的语言，但是保持大多数过程式和函数式编程语言的相似实现架构，其内部整体架构组成也是经典的编译器 “三段式” 架构。下面是KCL实现的架构图：</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cef84120a054412ea5d8e4983ed3b4be~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>主要有以下几个关键模块：</p>
<ul>
<li>解析器 Parser：解析器分析 KCL 源代码产生 AST（抽象语法树）。</li>
<li>编译器 Compiler：对 AST 进行多次遍历，对 AST 进行语义检查（比如进行类型检查、无效代码检查）并对 AST 进行优化（合并常量表达式等），最终产生虚拟机可以执行的字节码。</li>
<li>虚拟机 Virtual Machine (VM)：执行 Compiler 产生的字节码，计算产生相应的配置结果，并将配置结果序列化为 YAML/JSON 进行输出。</li>
</ul>
<p>整体架构分为三段式的好处是可以把针对 KCL 源语言的前端和针对目标机器的后端组合起来，这种创建编译器组合的方法可以大大减少工作量。比如目前的 KCL 字节码定义和后端虚拟机采用自研实现，KCL 虚拟机主要用于计算产生配置结果并序列化为 YAML/JSON 进行输出。如果遇到在其他特殊使用 KCL 的场景比如在浏览器中执行 KCL，则可以重写一个适配 WASM 的后端，就可轻易将 KCL 移植到浏览器中使用，但是 KCL 本身的语法和语义不需要发生任何变化，编译器前端代码也无需任何改动。</p>
<h3 data-id="heading-24">3.2 Go和Python通信原理</h3>
<p>为了更好地释放 KCL 配置策略语言的能力以及遍于上层自动化产品集成（比如著名的编译器后端 LLVM 就因其 API 设计良好，开发人员可以利用其 API 快速地构建自己的编程语言），KCLVM 目前提供了 Python 和 Go 两种语言的 API，使得用户可以使用相应的 API 快速地构建语言外围工具，语言自动化查询修改工具等提升语言的自动化能力，并且进一步可以基于此构建服务化能力，帮助更多的用户构建自己云原生配置代码化应用或者快速接入基础设施。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03d0f4fc94f547bab34081128a5c8d1a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>KCLVM 主体采用 Python 代码实现，而很多的云原生应用以 Go 程序构建，因此为了更好地满足云原生应用用户诉求。KCLVM 首先基于 CGo 和 CPython 构建了 Go 程序和 Python程序通信媒介，基于此设计了 Python 函数到 Go 函数的 RPC 调用，调用参数以 JSON 形式存储，使得 KCLVM-Python 编译器的能力平滑地过度到 Go 代码中，通过 Go 一行 import 调用即可操作 KCL 代码。</p>
<p><strong>补充：</strong> 在服务化实践的过程中，基于CGO调用Python的方案也遇到了一些问题：首先是Go+CGO+Python导致交叉编译困难，对ACI的自动化测试和打包产生了挑战；其次是CGO之后的Python不支持多语言多线程并发，无法利用多核的性能；最后即使通过CGO将Python虚拟机编译到了Go程序中，依然还是需要安装Python的标准库和第三方库。</p>
<h3 data-id="heading-25">3.3 协同配置原理</h3>
<p>当有了一个简单易用并能够保证稳定性的配置语言后，另一个面临的问题是如何使用配置代码化的方式提升协同能力。基于此，KCL 配置可分为用户侧和平台侧配置两类，最终的配置内容由各自用户侧和平台侧的配置内容共同决定，因此存在两个方面的协同问题：</p>
<ul>
<li>平台侧配置与用户侧配置之间的协同</li>
<li>用户侧配置之间的协同</li>
</ul>
<p>针对上述协同问题，KCL 在技术侧提出了顺序无关语法，同名配置合并等抽象模型来满足不同的协同配置场景。</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6cf60f807a646958f6c813165230102~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<p>以上图为例，首先 KCL 代码在编译过程中形成两张图（用户不同配置直接的引用和从属关系一般形式一张有向无环图），分别对应结构体内部声明代码及结构体使用声明代码。编译过程可以简单分为三步</p>
<ul>
<li>首先定义平台侧的结构体并形成结构体内部声明代码图</li>
<li>其次声明并合并不同用户侧配置代码图</li>
<li>最后将用户侧配置代码图计算的结果代入平台侧结构体内部声明代码图求解，最终得到完整配置图定义。</li>
</ul>
<p>通过这样简单的计算过程，可以在编译时完成大部分代换运算，最终运行时仅进行少量计算即可得到最终的解。同时在编译合并图过程中仍然能够执行类型检查和值的检查，区别是类型检查是做泛化、取偏序上确界（检查某个变量的值是否满足既定类型或者既定类型的子类型），值检查是做特化、取偏序下确界（比如将两个字典合并为一个字典）。</p>
<h2 data-id="heading-26">4. 对未来的展望</h2>
<p>KCL 语言目前依然处于一个高速发展的阶段，目前已经有一些应用开始试用。我们希望通过 KCL 语言为 Kusion 技术栈提供更强的能力，在运维、可信、云原生架构演进方面起到积极的作用。同时对于一些特殊的非标应用提供灵活的扩展和集成方案，比如我们正在考虑如何让后端支持 WebAssembly 平台，从而支持更多的集成方案。</p>
<p>在合适的时间我们希望能够开放 KCL 的全部代码，为云原生代码化的快速落地贡献绵薄之力。</p>
<p>谢谢大家。</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247491409%26idx%3D1%26sn%3Dd6c0722d55b772aedb6ed8e34979981d%26chksm%3Dfaa0f08bcdd7799dabdb3b934e5068ff4e171cffb83621dc08b7c8ad768b8a5f2d8668a4f57e%26token%3D2126738339" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247491409&idx=1&sn=d6c0722d55b772aedb6ed8e34979981d&chksm=faa0f08bcdd7799dabdb3b934e5068ff4e171cffb83621dc08b7c8ad768b8a5f2d8668a4f57e&token=2126738339" ref="nofollow noopener noreferrer">蚂蚁集团万级规模 K8s 集群 etcd 高可用建设之路</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247491198%26idx%3D1%26sn%3Da4607e6a8492e8749f31022ea9e22b80%26chksm%3Dfaa0f1a4cdd778b214403e36fb4322f91f3d1ac47361bf752c596709f8453b8482f582fe7e2e%26token%3D2126738339" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247491198&idx=1&sn=a4607e6a8492e8749f31022ea9e22b80&chksm=faa0f1a4cdd778b214403e36fb4322f91f3d1ac47361bf752c596709f8453b8482f582fe7e2e&token=2126738339" ref="nofollow noopener noreferrer">我们做出了一个分布式注册中心</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247490185%26idx%3D1%26sn%3Dcfc301e20a1ae5d0754fab3f05ea094a%26chksm%3Dfaa0f553cdd77c450bf3c8e34cf3c27c3bbd89092ff30e6ae6b2631953c4886086172a37cb48%26token%3D2126738339" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247490185&idx=1&sn=cfc301e20a1ae5d0754fab3f05ea094a&chksm=faa0f553cdd77c450bf3c8e34cf3c27c3bbd89092ff30e6ae6b2631953c4886086172a37cb48&token=2126738339" ref="nofollow noopener noreferrer">开启云原生 MOSN 新篇章 — 融合 Envoy 和 GoLang 生态</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzUzMzU5Mjc1Nw%3D%3D%26mid%3D2247488835%26idx%3D1%26sn%3Dd645b9abc866048e679b56bfe3b72482%26chksm%3Dfaa0fa99cdd7738ff1749ae75b1670f953c92b70dcf0358337977438fd74b632b21a7b17ece3%26token%3D2126738339d" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzUzMzU5Mjc1Nw==&mid=2247488835&idx=1&sn=d645b9abc866048e679b56bfe3b72482&chksm=faa0fa99cdd7738ff1749ae75b1670f953c92b70dcf0358337977438fd74b632b21a7b17ece3&token=2126738339d" ref="nofollow noopener noreferrer">MOSN 子项目 Layotto：开启服务网格+应用运行时新篇章</a></p>
</li>
</ul>
<p>更多文章请扫码关注“金融级分布式架构”公众号</p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22667d7e38344285bbbd1457440d80f1~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote></div>  
</div>
            