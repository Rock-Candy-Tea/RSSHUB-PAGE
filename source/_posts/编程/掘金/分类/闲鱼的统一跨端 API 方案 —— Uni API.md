
---
title: '闲鱼的统一跨端 API 方案 —— Uni API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe8b68a3d1b045e1ad0a4e2436789c71~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 19:16:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe8b68a3d1b045e1ad0a4e2436789c71~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：闲鱼技术——叶遥</p>
<p>随着 C 端流量红利的逐渐消失，端外投放已成为业务寻求增长的重要抓手之一。而不同 App 上存在不同应用场景、不同时期诞生的前端容器：</p>
<ol>
<li>基于浏览器的 Webview 容器（h5</li>
<li>基于客户端渲染衍生的 React Native、Weex 容器</li>
<li>基于自绘渲染的 flutter 容器，</li>
<li>平台开放能力的小程序容器</li>
</ol>
<p>业务在端外进行跨端时，就需要前端同学对投放目标环境逐一评估和适配。在初期阶段，前端侧通常通过同一业务针对不同目标环境维护多套实现的方式进行支持，这使得工作量成倍增加。效率提升空间下，催生了跨端方案</p>
<p>在跨端业务的前端代码中，通常存在大量的跨端 JS API 调用的重复逻辑：</p>
<pre><code class="copyable">if (isH5) &#123;
  if (isXianyu) &#123;   // 闲鱼
    webXianyuToast();
  &#125;else if (isTaobao) &#123; // 淘宝
    webTaobaoToast();
  &#125; else if(isAlipay)&#123; // 支付宝
    webAlipayToast()
  &#125;
  // ...
&#125; else if(isWeex)
// ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些调用从开发到上线通常需要经历的路径：</p>
<ol>
<li>和业务同学确定需要投放的目标环境。如 H5（支付宝、淘宝、天猫等）</li>
<li>向目标容器维护者询问 API 调用方式</li>
<li>在不同环境下调试、开发</li>
<li>测试同学使用不同机型在不同 App 上适配</li>
</ol>
<p>每一步都是比较耗时的体力活。假想，能够满足可用性、易用性、丰富性、可扩展性，使得业务直接开发如下代码，正常测试后即可上线。跨端 API 解决方案应该解决什么问题，提供什么能力呢？</p>
<pre><code class="copyable">import toast from 'uni-toast'

toast()
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li><strong>可用性：</strong> 适配业务常投放的 Webview、小程序、Wap 等前端容器和 App。并最大化保障 API 能力使用，调用 APP 定制能力 -> 调用容器通用能力 -> Wap 环境模拟能力 -> 返回支持度信息，避免调用异常</li>
<li><strong>易用性：</strong> 让不同环境的 API 调用有可靠、可快速调试支持度的统一入口</li>
<li><strong>丰富性：</strong> 所支持的目标环境、 API 集合足够多，满足绝大部分业务诉求</li>
<li><strong>可扩展性：</strong> 随着业务的发展，能够支持更多 App 、API；随着前端技术的发展，能够支持更多形态的容器</li>
</ol>
<h2 data-id="heading-0">整体设计</h2>
<p>在项目起步阶段，了解到不止是闲鱼，整个阿里经济体前端支撑跨端业务也有相同的问题。于是，跨端 API 项目站在经济体的的视角，以共建的方式进行推进。针对上述问题的方案设计：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe8b68a3d1b045e1ad0a4e2436789c71~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
我们将跨端 API 整体方案定义为规范、SDK 和配套设施三个部分：</p>
<ul>
<li>规范作为跨端 API 抹平标准，使得对上层业务只感知一套成为可能。</li>
<li>SDK 遵循规范，对不同环境调用底层 API 进行抹平。通过自定义构建、分端构建等工程能力，透出可定制、可扩展的跨端 API 产物；</li>
<li>配套设施通过 API 文档、CANIUSE 工具提供快速检索能力，一码多端调用示例提供快速试用能力；</li>
</ul>
<h2 data-id="heading-1">促成规范</h2>
<p>跨端 API 规范的意义是：</p>
<ol>
<li>向上为 SDK 层 API 设计提供参考标准，提高业务侧使用时的确定性、合理性；</li>
<li>向下为 Native 层 JSAPI 设计提供参考标准，减缓底层分化趋势；</li>
</ol>
<p>规范能否普遍推广和保持生命力取决于 <strong>自身合理性</strong> 和 <strong>上下游认可度</strong>，为保障以上两点，邀请了经济体各现有跨端方案作者成立了跨端 API 规范小组，从以下四个方面制定了跨端 API 规范：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6e5d56a486416aae3afb468de2f3f3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>确定范围</strong>：什么样的 API 应该算作跨端 API。</li>
</ul>
<p>跨端 API 应该具备 <strong>跨端属性</strong> 和 <strong>高频属性</strong>：跨端属性可通过各容器支持度客观反映，高频属性一方面通过各方案的调用统计作为依据，一方面通过跨端规范小组成员逐个投票判断</p>
<ul>
<li><strong>环境探针</strong>：跨端 API 核心在于根据不同环境调用相应实现，精确的环境感知尤为重要。</li>
</ul>
<p>环境判断涉及到经济体内、外的标准容器、特殊容器，在环境探针规范中通过 容器识别协议、端识别协议、系统识别协议、识别次序约定 的组合机制覆盖了全场景；</p>
<ul>
<li><strong>标准 API 定义</strong>：标准 API 模型是真实 API 的 interface，也是所有 API 的骨骼。</li>
</ul>
<p>通过标准 API 合集进行分析，API 之间的差异主要体现在：方法命名、调用方式、出入参结构、返回错误码 四个部分，这四部分加上 出入参扩展机制 就定义了标准 API 模型；</p>
<ul>
<li><strong>扩展机制：</strong> 标准 API 合集未覆盖的场景，通过定制、扩展能力支持。</li>
</ul>
<p>基于标准 API 扩展新的端容器实现，或者扩展一个全新的 API；</p>
<h2 data-id="heading-2">SDK 实现</h2>
<p>有了规范作为实现依据和指导之后，我们开始进行进行 SDK 实现。在整个过程中，主要面临了以下挑战：</p>
<p><strong>【实现】巨大的维护工作量：</strong> 55+ API 在 8 容器、30+ APP 上的适配和长期维护，且 API 和环境数量均无收敛趋势<br>
<strong>【工程】多场景产物输出：</strong> 多场景使用 -> 多形态产物。如日常业务开发期望的使用方式是<code>window.uni.toast()</code>；跨端基础物料开发期望的是 <code>import toast from 'uni-toast'</code> 。多场景的使用使得产物需要多形态输出<br>
<strong>【工程】方案的可定制性：</strong> 站在经济体视角，场景不只是面向闲鱼自身业务。业务侧场景通常只需要投放方案所支持容器环境中的一部分，使用整个方案会引入不必要的冗余。所以方案需要支持从全集中定义构建出子集的能力</p>
<p>应对上述挑战的关键解法是：  <strong>分层按端适配 API。</strong> API 差异分布在容器层、APP 层，SDK 设计时，也按照分层进行抹平。容器层抹平了通用 API 差异，APP 层基于容器层进行定制。按端适配的设计带来了天然的<strong>扩展性</strong>，在支持一个新端时，只需实现对应的 API 适配集合，其余环境判断、挂载 API、多维度输出包的部分就交给工程和 uniapi-core 完成了。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d336b3ed1578459cae5e66635e23c507~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>开放方案扩展能力，降低中心化维护工作量</strong>。官方优先保障高频 APP、容器的 API 维护，当业务跨端投放目标环境未适配时，可通过共建的方式按照规范进行适配；另外，建立 APP 适配维护认领机制，使得维护多端适配具备长效性。</p>
<p><strong>自定义构建能力。</strong> 原子化 API 的设计 + 组合机制可以使整个方案具备了自定义构建能力。<br>
原子化 API：将指定容器、APP 上的 API 适配作为最小单元，进行无副作用的实现；<br>
组合机制：通过配置提取所需 API 及目标投放环境，以代码模板的方式自动组合 API 进行构建、发布；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5936ff9eace490d9f9c5892399d7ecf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
拥有全环境的 API 原子化实现，便能构建出任意支持度的跨端 API 方案。目前已输数个 BU 级定制包。</p>
<h2 data-id="heading-3">配套设施建设</h2>
<p>规范和 SDK 满足了可用性、丰富性、可扩展性诉求。在易用性，跨端 API 提供复杂 API 的查询、调试能力，建设了内部、开源站点：文档（支持度信息细致到参数、APP 粒度）、CAN I USE 工具、一码多端调用示例等<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdca88d8fe8747f58d8d20caeaa216c7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">业务接入后</h2>
<p>在接入跨端 API 方案后，跨端业务的工作流有了以下优化：</p>
<ol>
<li>中心化的容器能力信息维护，使得产品、开发同学不再逐个环境询问能力，而是通过统一入口快速查询评估</li>
<li>统一多端适配 API 的 SDK，使得开发同学不再逐个环境拼凑、调试、开发 API，而是像标准 API 一样直接使用</li>
<li>统一维护 SDK，免去测试同学针对不同机型、不同环境下容器能力使用的工作量</li>
</ol>
<p>从 SDK 1.0 release 开始，闲鱼会玩社区、端外分享承接页等业务就开始陆续进行试点和落地。此外，方案 SDK Uni API 已在阿里经济体内 10+ BU 应用，逐渐成为经济体前端开发的基础设施。</p>
<h2 data-id="heading-5">展望</h2>
<ul>
<li>抹平不是终点，上层适配应对分化永远是中间态方案，一套底层标准 API 才是最优解。「跨端 API 调用规范」为「容器 API 标准」提供来自上层使用侧的输入，使得新容器 API 在设计时能够有所参考，避免不必要的分化</li>
<li>开源社区版本（<a href="https://universal-api.js.org/" target="_blank" rel="nofollow noopener noreferrer">universal-api.js.org</a>）建设（由跨端 API 小组、Rax 等团队共同建设）。目前 Uni API 开源版本已支持阿里系、微信、字节系、百度等小程序和 h5 容器，预期后续持续扩展 API 和支持容器等丰富度</li>
</ul>
<p>所以在端技术仍在日益发展的背景下，下一代的跨端方案，是由底层的 Fuchsia OS、HarmonyOS 等多端操作系统统一，还是依旧通过上层适配实现呢，你怎么认为呢？</p></div>  
</div>
            