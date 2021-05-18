
---
title: '2021 你可能错过的DevOps趋势'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210515/563a0ee5bebee55f6fa7e036be32881c.gif'
author: Dockone
comments: false
date: 2021-05-18 04:14:00
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210515/563a0ee5bebee55f6fa7e036be32881c.gif'
---

<div>   
<br>【编者的话】DevOps已经蓬勃发展起来，DevOps无处不在，现在一切都跟DevOps息息相关。但是我发现关于Deveops的一个新的趋势是大家都未注意到的。<br>
<br>最近，我读很多人做的关于2021年DevOps的发展趋势时，DevOps欣欣向荣。 DevOps就是一切，如今一切都是DevOps。<br>
<br>以下是如今爆炸性增长的DevOps趋势的部分列表：<br>
<ul><li>混合部署（Hybrid Deployments）</li><li>数据运维（DataOps）</li><li>弹性测试</li><li>生产测试</li><li>GitOps</li><li>微服务（当然）</li><li>无服务器（Serverless）</li><li>以云服务为中心的基础架构</li><li>边缘计算</li><li>基础架构即代码</li><li>开发安全（DevSecOps）</li><li>应用程序性能监视（APM）工具</li><li>混合计算（Hybrid Computing）</li><li>Kubernetes</li><li>功能开关（Feature Toggles）</li></ul><br>
<br>这样的例子不胜枚举……<br>
<br>但是，在阅读了所有这些文章后，令我震惊的是，没有一个人将“非侵入式生产环境调试”视为DevOps工具链的标准组件。而这就是我所看到的DevOps趋势。<br>
<h3>那么什么是“非侵入式生产环境调试”</h3>让我们从零开始，当我们想要调试生产环境的问题时我们最常用的方式就是——查看日志文件。这个痛苦的、重复的过程就像下面这样：<br>
<ol><li>令人讨厌的错误</li><li>该死，我没有足够的数据。</li><li>让我在日志中添加几行</li><li>构建</li><li>部署</li><li>复现错误步骤</li><li>看一下日志</li><li><br>找到问题了么？<br>
<ol><li>没有 - 回到步骤2</li><li>找到了（在几次耗时很久尝试以后）- 终于结束了</li></ol></li></ol><br>
<br>就像下面这个图展示一样：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210515/563a0ee5bebee55f6fa7e036be32881c.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210515/563a0ee5bebee55f6fa7e036be32881c.gif" class="img-polaroid" title="1-min.gif" alt="1-min.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
你还可以选择将远程调试器直接连接到生产环境，但是通常情况下，运维团队不允许这样做。出于安全考虑，你并不想在断点处暂停执行而中断服务。<br>
<br>非侵入式生产环境调试遵循可观察性工具的概念。这些是APM（应用程序性能监视工具），用于展示，分片和分块日志，指标和追踪（trace）。这就是可观察性。在不中断或干扰系统运行的情况下，了解系统的状况（以便您解决错误）。<br>
<br>但是，在修复生产环境中的错误时，这些工具往往不能提供足够的数据。通常它们能获得的最详尽的信息是显示抛出异常的位置，以及堆栈追踪（stack trace）以及有关错误情况的一些常规元数据，例如浏览器或操作系统的信息。<br>
<br>通常这些信息并不足以找到错误。微服务和无服务器等现代软件体系结构使事情变得更加困难。想象一下，跟踪一个使Kubernetes集群中的节点崩溃的错误，而Kubernetes只会启动一个新实例。或无服务器方法（serverless function）中的逻辑错误。当您调试这些问题时，证据已随着销毁的实例而不复存在。<br>
<br>非侵入式生产环境调试使可观察性更进一步，即便对于微服务和无服务器（serverless）代码，也能在代码级别逐行显示了应用程序的行为。这就是我们所说的<strong>代码级可观察性</strong>，它弥补了DevOps从APM（应用程序性能监视工具）无法获得的可观察性。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210515/29781a3ad5e13ca6a018b4db60de4c81.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210515/29781a3ad5e13ca6a018b4db60de4c81.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>为什么我认为这是一个很重要的趋势？</h3>你应该猜到为什么我如此着迷于非侵入式生产环境调试。因为这就是我公司的基础，我们的感受在与潜在客户和客户的会议中有了明显的转变。<br>
<br>一年前，主持会议的同行是开发人员，尽管是高级开发人员或开发经理，但仍然是开发人员。 DevOps工程师可能在会议室里，但是他们在开会过程中只是在后排坐着，只有在我们开始讨论软件如何影响或不影响生产系统，以及关于安全性，性能，部署等还有很多问题时参与讨论。但Devops工程师对于我们的生产环境调试器的使用方式或对它们的用途却没有太多的了解，至少不是由DevOps员工提供的。他们只是将其视为开发人员需要他们在生产环境中维护的另一种工具。<br>
<br>在过去的一年中，重点已经明显转移。坐在会议室的DevOps工程师坐在前排，提出了更多问题，并且开始意识到有效的生产调试可以如何显式的影响DevOps KPI，即便实际上是开发团队中的工程师在进行根本原因（root cause）分析并提出建议或者提交代码。DevOps团队开始更加关注 生产调试。<br>
<h3>为什么DevOps工程师开始对生产环境调试感兴趣？</h3>这种情况的部分原因是生产调试器也可以在预生产环境（例如QA和Staging）中运行。 DevOps工程师知道，在QA或Staging以及生产环境中，如果能调试并更快地修复bug，这意味着可以帮助提升的DevOps KPI：<br>
<ul><li>Staging环境会过滤掉更多的bug（更低的变更失败率，较低的缺陷遗失率，以及更高的平均无故障时间（MTBF））</li><li>能够自动捕获和显示异常的生产环境调试器不仅会在发生错误时立即通知你，而且会记录完整的错误执行流，使你能够非常快速地了解你是要处理真正的错误还是无关紧要的错误，以及错误的严重性及其影响（降低平均探测时间 （MTTD））。</li><li>生产环境调试器极大地减少了识别，分析和修复生产错误所需的时间（即平均恢复时间（MTTR））。当我们开始讨论此KPI时，坐在房间里的所有DevOps工程师都会坐起来，因为这反映了当生产中出现问题时服务将不可用多长时间。我们知道这种事一定会发生，<a href="http://xn--downdetector-rv0u738s9q5b33wg.com/">只需查看这个记录网站不可用的探测网站downdetector.com</a>，你就会明白我的意思。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210515/466498fc9df47d8b913b4b1c246e87ed.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210515/466498fc9df47d8b913b4b1c246e87ed.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
DevOps工程师和SRE意识到，生产环境调试器不仅仅是作为开发人员工具，更像是监控以及代码可观察性。它还非常符合DevOps的反馈和协作原则，弥合了DevOps与开发人员之间仍然存在的鸿沟（这在许多组织中仍然存在）。通过生产环境调试器，开发人员可以直接从生产系统中获取所需的数据，用来解决错误。 使用生产环节调试器，DevOps和开发人员可以直接合作以解决生产环境中的错误，这是修复bug和快速解决生产事故的催化剂。<br>
<h3>那么生产环境调试器是如何工作的呢？</h3><h4>远程调试器</h4>生产环境调试并不是一个全新的概念。远程调试已经存在了一段时间，你可以在运行时注入断点，在每次断点命中时收集数据，然后立即继续该过程并重复。尽管这是获取生产数据的简便方法，但它具有<strong>侵入性</strong>，并且会对性能产生重大影响，因此现在并未得到广泛使用。<br>
<h4>快照调试</h4>另一种方式是快照调试，调试器将会fork进程一份进程的副本（使用写时复制copy-on-write技术），然后通过检查副本来进行调试。尽管此方法让您可以检查调试过程的整个内存占用量，但它也是侵入性的，给正在运行的主机上增加了很大的内存负载，因此进行快照的dian数量是有限制。<br>
<h4>插装（instrumentation）</h4>现代生产环境调试器使用第三种方法——字节码插装。它们将插装添加到执行不同功能的字节码中，例如测量性能，捕获应用程序状态，捕获异常等。这是APM多年来一直在做的事情。生产环境调试器将其进一步扩展。它和APM使用相同的技术，目标是解决报错和逻辑错误，而不是解决生产和预生产环境中的性能问题。<br>
<br>由于人类看不懂字节码，因此让我们看看如果在源代码中添加检测功能，字节码会是什么样子。<br>
<br>代码如下：<br>
<pre class="prettyprint">public async Task<BasketModel> ApplyBundleCode(string code)<br>
&#123;<br>
var customer = await ProfileService.FetchProfile(User);<br>
var basket = await BasketService.LoadBasketForCustomer(customer);<br>
var bundle = await BundlesService.FetchBundle(code);<br>
if (bundle.IsCustomerEligible(customer))<br>
&#123;<br>
   bundle.ApplyOn(basket);<br>
   await BasketService.UpdateBasketForCustomer(customer, basket);<br>
&#125;<br>
return basket;<br>
&#125; <br>
</pre><br>
加入检测后，可能看起来像这样：<br>
<pre class="prettyprint">public async Task<BasketModel> ApplyBundleCode(string code)<br>
&#123;<br>
Telemetry.startTimer(“ApplyBundleCode”);<br>
Telemetry.logVariable(“User.Id”,User?.Id);<br>
var customer = await ProfileService.FetchProfile(User);<br>
Telemetry.logVariable(“Customer.FullName”,customer?.FullName);<br>
Telemetry.logVariableAsJson(“Customer.Address”,customer?.Address); <br>
<br>
var basket = await BasketService.LoadBasketForCustomer(customer);<br>
Telemetry.logVariableAsJson(“basket”,basket);<br>
Telemetry.logVariable(“code”,code);       <br>
<br>
var bundle = await BundlesService.FetchBundle(code);<br>
Telemetry.logVariable(“code”,code);<br>
<br>
if (bundle.IsCustomerEligible(customer))<br>
&#123;<br>
 Telemery.log(“bundle &#123;0&#125; eligible for customer &#123;1&#125;”, code, customer.FullName);<br>
 bundle.ApplyOn(basket);<br>
 Telemery.log(“about to update basket”);<br>
 await BasketService.UpdateBasketForCustomer(customer, basket);<br>
&#125;<br>
else &#123;<br>
Telemery.log(“bundle &#123;0&#125; not eligible for customer &#123;1&#125;”, code, customer.FullName);<br>
&#125;<br>
<br>
Telemery.endTimer(“ApplyBundleCode”);<br>
return basket;<br>
&#125; <br>
</pre><br>
调试检测代码同样有挑战性。大多数现代生产环境调试器都需要先用Git找到精确的生产环境使用的commit，从中构建出和生产环境相同的二进制文件以便调试。将所有正确的源文件与生产环境中当前正在运行的文件进行匹配并不总是一件容易的事，并且您还需要匹配一组构建和编译设置。以及如何处理第三方代码？一些工具通过反编译正在调试的生产代码来解决此问题。这使工作变得更加轻松，因为它消除了匹配源文件的要求，并且将第三方代码与旧代码一起反编译。<br>
<h3>为什么非侵入式打败侵入式</h3>远程调试器具有很强的侵入性，因为它们连接到主机应用程序并将断点放置在实时运行的系统中。即使应用程序只是短暂中断了以供远程调试器收集数据，仍然存在许多生产系统所不能容忍的巨大稳定性风险。同样，快照调试器通过其使用的侵入式写时复制技术对运行中的系统造成的内存开销也存在耗尽系统内存的风险。例如，Microsoft的Snapshot Debugger默认为每分钟最多五个快照，以避免抛出内存不足的异常。<br>
<h3>插装（instrumentation）和生产调试器一起可以做什么？</h3>现代生产环境调试器所做的大部分工作都是基于不间断的断点（也称为追踪点）。在希望获取数据的那一行打上断点（即追踪点）让调试器插装来获取数据。你实际上可以做很多事情：<br>
<ul><li><strong>动态日志</strong>：记录代码中任何位置的数据，包括局部变量和方法参数的值。</li><li><strong>动态指标</strong>：就像是动态日志，从局部变量中您可以提取到应用程序级别数据，从而衡量不同的指标。</li><li><strong>集成</strong>：您可以在无需中断的断点/跟踪点的情况下，将测量的任何内容通过API传播到第三方应用程序。因此，你可以创建Slack通知或将动态日志和指标数据传递到APM，在其中您可以进一步对数据进行分片和分块，以精美的图形和图表查看数据，并且创建有意义的警报。</li></ul><br>
<br>除了使用不中断的断点/跟踪点来完成的工作外，某些生产环境调试器还可以执行以下操作：<br>
<br>捕获异常：这已经是许多APM所做的事情，但是生产环境调试器将提供有关异常以及抛出异常的局部信息和变量值的更多信息。<br>
时间旅行记录：某些生产环境调试器不仅捕获异常，而且捕获整个过程中导致异常的完整错误执行流以及应用程序数据。这样就可以逐行调试异常，这与开发环境的IDE中的调试体验非常相似。<br>
<h3>那么哪些公司是主要参与者？</h3>APM和可观察性已经存在大约十年了，出现了很多出色的企业级产品。而现代生产环境调试工具出现较晚，它提供了找出错误根源所需的代码级可观察性。由于我本人来自Ozcode，因此在描述市场上主要的现代生产调试工具时，我不想冒存在偏见的风险，因此，请自行浏览下面的网站并做出评测。<br>
<ul><li><a href="https://www.rookout.com/" rel="nofollow" target="_blank">https://www.rookout.com/</a></li><li><a href="https://lightrun.com/" rel="nofollow" target="_blank">https://lightrun.com/</a></li><li><a href="https://www.nerd.vision/" rel="nofollow" target="_blank">https://www.nerd.vision/</a></li><li><a href="https://oz-code.com/" rel="nofollow" target="_blank">https://oz-code.com/</a></li><li><a href="https://www.thundra.io/sidekick" rel="nofollow" target="_blank">https://www.thundra.io/sidekick</a></li></ul><br>
<br><h3>非侵入式生产环境调试将成为DevOps工具链中不可或缺的一部分</h3>任何新技术要成为企业的年度预算中的标准项目，都需要花费一些时间。 APM已经存在，并且任何在软件方面值得关注的企业都使用这些工具来管理，监视其生产系统并对其进行故障排除。但是，DevOps专业人员现在意识到，在调试生产环境问题时，需要逐行挖掘代码，APM不能提供足够的数据进行调试。非侵入式生产环境调试器已证明，当你提供代码级可观察性，动态日志和跟踪以及时间旅行调试时，可以将生产调试时间最多减少80％。而且，当停机成本高达<a href="https://blogs.gartner.com/andrew-lerner/2014/07/16/the-cost-of-downtime/">每分钟5600美元</a>时，DevOps专业人员将无法忽略这笔实际的企业成本。<br>
<br>APM是今天确定需要的技术。不久之后，非侵入式生产环境调试器的价值也会成为企业必不可少的技术之一。 DevOps革命使运维人员更接近开发人员。现在是时候让这种合作迈出下一步，进入调试领域了。<br>
<br><strong>原文链接：<a href="https://dzone.com/articles/the-2021-devops-trend-everyone-is-missing">The 2021 DevOps Trend Everyone Is Missing</a>（翻译：Grace）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            