
---
title: 'Lyft 如何提升微服务的研发效能（一）'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220405/8f6683beec9bf1210eac8b6b14595a66.png'
author: Dockone
comments: false
date: 2022-04-17 02:26:06
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220405/8f6683beec9bf1210eac8b6b14595a66.png'
---

<div>   
<br>【编者的话】本系列讲述了 lyft 是如何从本地开发、联调测试以及线上发布等多个环节提升微服务的研发效能，本文是该系列的第一篇。<br>
<br>2018 年底，Lyft 工程团队完成了将原来基于 PHP 的单体架构拆分成一组由 Python 和 Go 组成的微服务。几年下来，微服务架构在允许团队之间相互独立地进行运维和交付服务方面取得了很大的成功。微服务架构带来的关注点分离让我们得以更快地进行实验和交付功能 —— 每天部署数百次 —— 而且为我们提供了一些灵活性：我们可以根据编程语言的偏好选择各自适合的场景，根据服务的重要程度设定更加严格或者宽松的要求，等等。然而，随着工程师、服务和测试案例数量的不断增加，我们的开发工具难以跟上微服务的爆炸式增长，这进一步侵蚀了我们一直努力想要去提升的研发效能。<br>
<br>本系列分成四个部分，它将会介绍服务于 Lyft 工程团队的开发环境是如何支撑从 100 名工程师和少量服务发展到 1000 多名工程师以及数百个服务。我们将会讨论到规模方面带来的挑战，这导致之前建设的大多数环境都不再适用，我们还会介绍到一种主要为重度集成测试服务（通常接近端对端）的测试方案，以支持采用本地优先的方式来单独测试一些组件。<br>
<ul><li>第一部分: 开发及测试环境的历史（本文）</li><li><a href="https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-2-optimizing-for-fast-local-development-9f27a98b47ee">第二部分: 加快本地开发的一些优化</a></li><li><a href="https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f">第三部分: 预发布环境通过重载形式来扩展服务网格</a></li><li><a href="https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-4-gating-deploys-with-automated-acceptance-4417e0ebc274">第四部分: 通过自动化验收测试来控制发布</a></li></ul><br>
<br><h3>开发及测试环境的历史</h3>我们对综合开发环境的第一次重大投资始于 2015 年，当时我们的工程师人数达到了 100 人。几乎所有的开发仍然围绕着一套单体的 PHP 服务进行，与此同时，一小部分微服务涌现出来，用于不同的用例场景，比如司机入职。<br>
<br>由于存在这样的预期：我们需要服务的工程师和服务数量将会持续增长，迁移到容器无疑是很有意义的。我们的计划是构建一个基于 Docker 的容器编排环境 —— 当时仍然处于起步阶段 —— 首先为开发人员提供测试服务，然后再延伸到生产环境，如此一来我们将可以受益于多租户的工作负载所带来的更低的成本和更快的扩容速度。<br>
<h4>通过 Devbox 实现本地开发</h4>Devbox —— Lyft 的盒式开发环境 —— 于 2016 年初上线，随即很快被大多数工程师采用。Devbox 的工作内容是帮助用户管理本地虚拟机 —— 无需他们再去手动安装或者更新软件包、配置 <a href="http://smarden.org/runit/">runit</a> 来启动服务，添加共享文件夹等。一旦虚拟机跑起来以后，只需要敲一个命令然后等上几分钟即可实现拉取最新版本的镜像、创建/填充数据库、启动一个<a href="https://www.envoyproxy.io/"> envoy 代理</a> sidecar，以及其他开始发送请求前需要做的一些准备工作。<br>
<br>相比于之前，这是一次很棒的升级，我们曾经需要为每个开发人员和他们开发的服务组合手动配置一台 EC2 实例，这些配置和更新维护工作太过于乏味。如今，我们第一次采用一种一致的、可重复而且简单的方式来实现跨多个服务的开发。<br>
<h4>使用 Onebox 进行远程开发</h4>随着时间的推移，对于可以和其他工程师或者职能人员（比如设计）共享的长期运行时环境的需求很快就变得明显，这便有了 Onebox。Onebox 本质上是跑在一台 ec2 实例上的 Devbox，它带来的一些好处让很多用户纷纷从 Devbox 转投它的阵营。我们将这些 Onebox 托管在一组 r3.4xlarge 型号的 ec2 实例上，这些实例具有 16 个 vCPU 和 122 GiB 内存，比工程师们随身携带的 MacBook Pro 更强大。Onebox 上面可以运行更多的服务，而且下载容器镜像的速度更快（因为跑在 AWS 上），更不用说避免了在笔记本上跑 VirtualBox 然后搞得风扇像喷气发动机一样嗡嗡作响的情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220405/8f6683beec9bf1210eac8b6b14595a66.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220405/8f6683beec9bf1210eac8b6b14595a66.png" class="img-polaroid" title="01.png" alt="01.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>我们有两种不同风格的开发环境，它们都支持运行多个服务</em><br>
<h4>集成测试</h4>除了单元测试之外，Onebox 由于采用的是云基础设施，因此非常适合在 CI 上运行集成测试。一个服务只需要在 <code class="prettyprint">manifest.yaml</code> 文件里定义它所需的依赖项组合，CI 将会起一个临时的 Onebox，在上面运行这些服务并在每个拉取请求（PR）上执行对应的测试。许多服务，尤其是更接近移动客户端的组合服务，大都构建了大型集成测试套件来减少故障风险。一些故障的复盘分析往往以添加一组新的集成测试来收尾。有了如此灵活和强大的测试能力，单元测试逐渐退居二线。<br>
<pre class="prettyprint">name: api<br>
type: service<br>
groups:<br>
- name: integration<br>
members:<br>
 - driver_onboarding<br>
 - users<br>
tests:<br>
- name: integration<br>
group: integration<br>
</pre><br>
<em>定义在 CI 里要运行的集成测试的一个服务示例</em><br>
<h4>预发布环境</h4>Lyft 的预发布环境几乎与生产环境相同 —— 只是作用范围更小，也没有生产数据 —— 这里部署的所有服务最终目的都是要上线到生产环境。虽然它不属于开发环境，但是由于它在端到端测试中发挥着越来越重要的作用，如何建设预发布环境无疑是值得讨论的。<br>
<br>在 2017 年初发布 Devbox 和 Onebox 后不久，我们还解决了另外一种增长问题：压力测试。一些活动导致的拼车流量暴涨，比如新年前夜和万圣节，会暴露我们系统中的瓶颈，这常常会引发故障。为了提前解决这些问题，我们构建了一个模拟海量打车请求的框架。该框架针对我们的生产环境，协调数以万计的不同设定（例如，经常取消订单的洛杉矶司机）的模拟用户并且把 Lyft 当成是一个黑盒子来进行测试。<br>
<br>作为在预发布环境测试模拟框架本身的副产品，我们意识到生成的流量对于一般的端到端测试也很有价值。在预发布环境里不断地演习公共 API 端点为部署提供了一个很好的参考依据。例如，如果部署破坏了乘客下车的 API 端点，那么发起部署的人几乎会立马看到错误日志和告警。模拟框架还会不断为用户、打车、支付等生成最新的数据，从而消除了开发过程中必要的手动测试所需的大部分设置时间。借着压力测试，预发布环境变得比以往任何时候都更加地实际、有用，在一些团队里把 PR 分支部署到那里作为一个统一的地方来获取真实数据的反馈的做法变得十分常见。<br>
<h3>转折点</h3>时间线快进到 2020 年 —— 在将 Devbox 和 Onebox 作为容器化开发环境引入到 Lyft 的四年后 —— 尽管我们尽了最大地努力，"Lyft-in-a-box" 风格的环境变得越来越难以跟上我们的发展。使用这些环境的工程师增加了十倍，现在有数百个微服务为更复杂的业务提供动力。 尽管这套方案针对一些依赖关系比较简单的服务开发仍然相当有效，但是绝大多数的开发工作都是围绕着那些已经建立了一棵庞大复杂的依赖关系树的服务上 —— 这使得在 CI 上启动环境或者运行测试变得异常缓慢。<br>
<br>虽然这些环境和测试功能<em>曾经</em>十分强大也很方便，但是突破临界点之后已经是弊大于利了。我们构建了一套针对测试少数服务进行了优化的系统，然而并没有就服务的数量重新评估我们的策略 —— 这个数字伴随着我们拆分 PHP 单体架构而加速增长 —— 从 5 增加到 50、50 增加到 100 甚至更多。为了开发去支撑这么多服务不仅需要付出巨大的努力来维护和扩容，而且还会因为他们被迫要去考虑整个系统而不是一次只考虑一个组件，如此进一步大规模降低了开发人员的生产力。<br>
<br>我们不妨详细研究一下这个问题的几个方面：<br>
<h4>可扩展性</h4>由于涉及的资源数量庞大而且存在和类生产环境的差异，Onebox 环境在突破某个临界点之后就会变得不再实用。比如，在数百个环境之间运行一套相同的可观察性工具是不可行的。当出现问题时，很难查清楚问题的根因（已经运行的 70 个服务里，哪一个行为不一致？），人们往往会在放弃和测试预发布环境之前多点几次 "reset" 按钮。<br>
<br>预发布环境，从另一个角度来说，既易于扩展，也更加忠实地反映了生产环境。它提供相同的日志记录（ logging ）、链路追踪（ tracing ）和指标（ metrics ）功能来帮助调试。部署到一套共享的预发布环境里进行测试的最主要缺点是：（1）一些实验性质的变动可能会干扰到使用该环境的其他用户；（2）每个服务同一时间只能有效测试一个变更；以及（3）需要更长的时间（分钟级）来构建和部署，而不仅仅只是同步代码和热加载（秒级单位）。<br>
<h4>可维护性</h4>由于上面提到的可扩展性挑战，维护和优化这些环境也花费了不少时间，以至于随着时间的推移，这套技术栈也显得过时了。生产和预发布环境已经迁到 Kubernetes 上进行容器编排，同时也切换到了更加精简的单进程容器镜像。开发环境使用了更重的多进程镜像，它们一般绑定了一些 sidecar 和其他基础设施组件（监控指标、日志等），这使得镜像的构建和下载速度变得更慢。<br>
<br>每周都会发生因为变更导致的故障，它们尽管不妨碍预发布或者生产环境，但是却影响着开发环境。由于大多数开发人员用的大都是常见的服务，因此一个服务如果出问题，影响面会很大。有些团队已经将所有的端到端测试转移到了预发布环境，把他们在开发环境部署的服务丢在那里，这一事实加剧了这种情况。<br>
<h4>所有权</h4>开发环境里一些问题的归属（ Ownership ）并不清晰。谁应该负责修复那些出问题的指定服务？启动 Onebox 的人、服务的所有者还是开发基础架构（ Developer Infra ）团队？ 在实践中，这经常落到开发基础架构团队的头上，他们其实没有能力诊断和解决特定于应用程序的问题（例如，改了一个配置项导致应用程序在启动时崩溃）。<br>
<h4>臃肿的测试</h4>笨拙的集成测试套件严重消耗了开发生产力。运行时间长达一个小时的测试套件司空见惯，它们一般跑在一套复杂的分片式基础设施上，并且支持自动重试，这样设计是想给不稳定的环境填坑。导致这种情况的两个主要因素是依赖关系和测试本身的不断膨胀。传递性质的依赖会在服务所有者不注意的情况下逐渐增加，在统一的 30s 时间块里吃掉一部分的测试时间。测试套件本身的体积也在稳步增长，因为尽管我们会在出现问题时立即加上对应的测试用例，却很少会在现有的测试用例已经满足目的的前提下把它删掉。<br>
<br>那么，我们为什么要在合并 PR 前付出这个等待时间的成本？当然是因为这些测试会在它们投入生产之前帮助捕获错误了！但是实践过程中通过仔细检查，我们发现这个说法并不那么站得住脚。通过分析一些开发最活跃的服务对应的集成测试，我们发现，80% 或者甚至更多的测试，要么是不必要的（比如已经过时，或者和现有的测试用例重复了），要么是可以在很短的时间内重写成无需外部依赖即可运行。当测试报错了，绝大多数都是误报 —— 我们还得花上几个小时的调试时间 —— 其余的通常会在造成生产环境影响之前，在预发布环境或者金丝雀环境被发现。<br>
<pre class="prettyprint"># 2013 (monolith), duration: 1 minute<br>
def test_driver_approval():<br>
"""<br>
Requires: <br>
    - api<br>
"""<br>
user = get_user()<br>
approve_driver(user)<br>
assert user.is_approved<br>
<br>
# ------------------------------------------------------------ #<br>
<br>
# 2015 (mostly monolithic, a few services), duration: 3 minutes<br>
def test_driver_approval():<br>
"""<br>
Requires:<br>
    - api (monolith)<br>
    - users<br>
        - mongodb<br>
    - driver_onboarding<br>
        - mongodb<br>
        - redis<br>
"""<br>
user = user_service.create_user()<br>
user = driver_onboarding_service.approve_driver(user)<br>
assert user.is_approved<br>
<br>
# ------------------------------------------------------------ #<br>
<br>
# 2018 (post-decomp, microservices), duration: 20 minutes<br>
def test_driver_approval__california():<br>
"""<br>
Requires:<br>
    - users<br>
        - redis<br>
        - experimentation<br>
        - fraud<br>
            - dynamodb<br>
        - messaging<br>
            - mongodb<br>
    - driver_onboarding<br>
        - messaging<br>
            - email<br>
            - experimentation<br>
        - dmv_checks<br>
            - vehicles<br>
                - payments<br>
"""<br>
user = user_service.create_user()<br>
user = driver_onboarding_service.approve_driver(user)<br>
assert user.is_approved<br>
<br>
def test_driver_approval__newyork():<br>
# ...<br>
def test_driver_approval__montreal():<br>
# ...<br>
</pre><br>
<em>随着我们继续拆分新的微服务，集成测试变得更加笨拙</em><br>
<h3>改变路线</h3>大约在一年前，我们开始着手把我们的开发环境迁移到 Kubernetes ，自那以后，工程资源的变化是我们聚焦和重新审视我们更大方向的催化剂。维护基础设施以支持这些按需环境的成本变得过于高昂，而且只会随着时间的推移不断恶化。解决这一问题需要对我们开发和测试微服务的方式进行一次更为彻底的改变。是时候重新搞一套替代方案（对于由数百个微服务组成的系统而言必须是可持续发展的）来替换之前跑在 CI 上的 Devbox、Onebox 和集成测试了。<br>
<br>在仔细调研开发人员是如何使用现有环境之后，我们确定了三个关键工作流程（在下图中以紫色表示），维护这些工作流程至关重要并且需要一些投入：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220405/a5462b3d57a1ffbf4c81514765c4cd62.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220405/a5462b3d57a1ffbf4c81514765c4cd62.png" class="img-polaroid" title="02.png" alt="02.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ol><li>本地开发：对于任何给定的服务，运行单元测试或启动 Web 服务器然后发送请求都应该是简单、超快的。</li><li>手动的端到端测试：测试指定的变更在更大的系统里的执行情况是许多工程师依赖的关键工作流程。我们希望扩展预发布环境，从而让开发人员能够更轻松、更安全地以一个相对隔离的方式进行测试。</li><li>自动化端到端测试：尽管不能过度依赖这种测试，但如果没有自动化 E2E 测试提供的信心，我们就无法每天持续交付数百次的变更。我们将保留一小部分有价值的测试作为验收测试 —— 在部署到生产期间运行的测试。</li></ol><br>
<br>本系列的后续帖子将深入探讨这三个领域中的每一个部分，包括讨论问题域、我们如何解决这些问题以及我们从中学到了什么。查看关于<strong>本地开发</strong>的<a href="https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-2-optimizing-for-fast-local-development-9f27a98b47ee">下一篇文章</a>，它将分享更多关于我们在本地开发时用于检查、模拟和魔改网络请求的工具。<br>
<br><strong>原文链接：<a href="https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-1-a2f5d9a77813">Scaling productivity on microservices at Lyft (Part 1)</a>（翻译：吴佳兴）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            