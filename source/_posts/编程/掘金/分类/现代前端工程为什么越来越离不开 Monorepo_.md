
---
title: '现代前端工程为什么越来越离不开 Monorepo_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a56317bdf94794a8b29f6cd184c888~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 17:12:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a56317bdf94794a8b29f6cd184c888~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>随着前端工程日益复杂，某些业务或者工具库通常涉及到很多个仓库，那么时间一长，多个仓库开发弊端日益显露，由此出现了一种新的项目管理方式——Monorepo。本文主要以 <strong>Monorepo 的概念</strong>、<strong>MultiRepo的弊端</strong>、<strong>Monorepo 的收益</strong>以及<strong>Monorepo 的落地</strong>这几个角度来认识和学习一下 Monorepo，文末会有思考题，欢迎大家来踊跃讨论。</p>
<h2 data-id="heading-0">什么是 Monorepo?</h2>
<p>Monorepo 其实不是一个新的概念，在软件工程领域，它已经有着十多年的历史了。概念上很好理解，就是把<strong>多个项目</strong>放在<strong>一个仓库</strong>里面，相对立的是传统的 MultiRepo 模式，即每个项目对应一个单独的仓库来分散管理。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a56317bdf94794a8b29f6cd184c888~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>现代的前端工程已经越来越离不开 Monorepo 了，无论是业务代码还是工具库，越来越多的项目已经采用 Monorepo 的方式来进行开发。Google 宁愿把所有的代码都放在一个 Monorepo 工程下面，Vue 3、Yarn、Npm7 等等知名开源项目的源码也是采用 Monorepo 的方式来进行管理的。</p>
<p>一般 Monorepo 的目录如下所示，在 packages 存放多个子项目，并且每个子项目都有自己的<code>package.json</code>:</p>
<pre><code class="copyable">├── packages
|   ├── pkg1
|   |   ├── package.json
|   ├── pkg2
|   |   ├── package.json
├── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那 Monorepo 究竟有什么魔力，让大家如此推崇，落地如此之广呢？</p>
<h2 data-id="heading-1">MultiRepo 之痛</h2>
<p>要想知道 Monorepo 的优势，首先得弄清楚之前的开发方式有什么痛点。</p>
<p>之前传统的方式<code>MultiRepo</code>当中，每个项目都对应单独的一个代码仓库。我之前也是用这种方式开发的，是真真切切地感受到了这种方式带来的诸多弊端。现在就和大家一一分享一下。</p>
<h3 data-id="heading-2">1.代码复用</h3>
<p>在维护多个项目的时候，有一些逻辑很有可能会被多次用到，比如一些基础的组件、工具函数，或者一些配置，你可能会想: 要不把代码直接 copy 过来，多省事儿！但有个问题是，如果这些代码出现 bug、或者需要做一些调整的时候，就得修改多份，维护成本越来越高。</p>
<p>那如何来解决这个问题呢？比较好的方式是将公共的逻辑代码抽取出来，作为一个 npm 包进行发布，一旦需要改动，只需要改动一份代码，然后 publish 就行了。</p>
<p>但这真的就完美解决了么？我举个例子，比如你引入了 <code>1.1.0</code> 版本的 A 包，某个工具函数出现问题了，你需要做这些事情：</p>
<ul>
<li>
<ol>
<li>去修改一个工具函数的代码</li>
</ol>
</li>
<li>
<ol start="2">
<li>发布<code>1.1.1</code>版本的新包</li>
</ol>
</li>
<li>
<ol start="3">
<li>项目中安装新版本的 A。</li>
</ol>
</li>
</ul>
<p>可能只是改了一行代码，需要走这么多流程。然而开发阶段是很难保证不出 bug 的，如果有个按钮需要改个样式，又需要把上面的流程重新走一遍......停下来想想，这些重复的步骤真的是必须的吗？我们只是想复用一下代码，为什么每次修改代码都这么复杂？</p>
<p>上述的问题其实是 <code>MultiRepo</code>普遍存在的问题，因为不同的仓库工作区的割裂，导致复用代码的成本很高，开发调试的流程繁琐，甚至在基础库频繁改动的情况下让人感到很抓狂，体验很差。</p>
<h3 data-id="heading-3">2.版本管理</h3>
<p>在 MultiRepo 的开发方式下，依赖包的版本管理有时候是一个特别玄学的问题。比如说刚开始一个工具包版本是 v1.0.0，有诸多项目都依赖于这个工具包，但在某个时刻，这个工具包发了一个 <code>break change</code> 版本，和原来版本的 API 完全不兼容。而事实上有些项目并没有升级这个依赖，导致一些莫名的报错。</p>
<p>当项目多了之后，很容易出现这种依赖更新不及时的情况。这又是一个痛点。</p>
<h3 data-id="heading-4">3.项目基建</h3>
<p>由于在 MultiRepo 当中，各个项目的工作流是割裂的，因此每个项目需要单独配置开发环境、配置 CI 流程、配置部署发布流程等等，甚至每个项目都有自己单独的一套脚手架工具。</p>
<p>其实，很容易发现这些项目里的很多基建的逻辑都是重复的，如果是 10 个项目，就需要维护 10 份基建的流程，逻辑重复不说，各个项目间存在构建、部署和发布的规范不能统一的情况，这样维护起来就更加麻烦了。</p>
<h2 data-id="heading-5">Monorepo 的收益</h2>
<p>说清楚 <code>MultiRepo</code> 的痛点之后，相信你也大概能理解为什么要诞生<code>Monorepo</code>这个技术了。现在就来细致地分析一下<code>Monorepo</code>到底给现代的前端工程带来了哪些收益。</p>
<p>首先是<strong>工作流的一致性</strong>，由于所有的项目放在一个仓库当中，复用起来非常方便，如果有依赖的代码变动，那么用到这个依赖的项目当中会立马感知到。并且所有的项目都是使用最新的代码，不会产生其它项目版本更新不及时的情况。</p>
<p>其次是<strong>项目基建成本的降低</strong>，所有项目复用一套标准的工具和规范，无需切换开发环境，如果有新的项目接入，也可以直接复用已有的基建流程，比如 CI 流程、构建和发布流程。这样只需要很少的人来维护所有项目的基建，维护成本也大大减低。</p>
<p>再者，<strong>团队协作也更加容易</strong>，一方面大家都在一个仓库开发，能够方便地共享和复用代码，方便检索项目源码，另一方面，git commit 的历史记录也支持以功能为单位进行提交，之前对于某个功能的提交，需要改好几个仓库，提交多个 commit，现在只需要提交一次，简化了 commit 记录，方便协作。</p>
<h2 data-id="heading-6">Monorepo 的落地</h2>
<p>如果你还从来没接触过 Monorepo 的开发，到这可能你会疑惑了: 刚刚说了这么多 Monorepo 的好处，可是我还是不知道怎么用啊！是直接把所有的代码全部搬到一个仓库就可以了吗?</p>
<p>当然不是，在实际场景来落地 Monorepo，需要一套完整的工程体系来进行支撑，因为基于 Monorepo 的项目管理，绝不是仅仅代码放到一起就可以的，还需要考虑项目间依赖分析、依赖安装、构建流程、测试流程、CI 及发布流程等诸多工程环节，同时还要考虑项目规模到达一定程度后的性能问题，比如项目<code>构建/测试</code>时间过长需要进行<strong>增量构建/测试</strong>、<strong>按需执行 CI</strong>等等，在实现全面工程化能力的同时，也需要兼顾到性能问题。</p>
<p>因此，要想从零开始定制一套完善的 Monorepo 的工程化工具，是一件难度很高的事情。不过社区已经提供了一些比较成熟的方案，我们可以拿来进行定制，或者对于一些上层的方案直接拿来使用。</p>
<p>其中比较底层的方案比如 <a href="https://lerna.js.org/" target="_blank" rel="nofollow noopener noreferrer"><code>lerna</code></a>，封装了 Monorepo 中的依赖安装、脚本批量执行等等基本的功能，但没有一套构建、测试、部署的工具链，整体 Monorepo 功能比较弱，但要用到业务项目当中，往往需要基于它进行顶层能力的封装，提供全面工程能力的支撑。</p>
<p>当然也有一些集成的 Monorepo 方案，比如<a href="https://nx.dev/latest/react/getting-started/getting-started" target="_blank" rel="nofollow noopener noreferrer"><code>nx</code></a>(官网写的真心不错，还有不少视频教程)、<a href="https://rushstack.io/" target="_blank" rel="nofollow noopener noreferrer"><code>rushstack</code></a>，提供从初始化、开发、构建、测试到部署的全流程能力，有一套比较完整的 Monorepo 基础设施，适合直接拿来进行业务项目的开发。不过由于这些顶层方案内部各种流程和工具链都已经非常完善了，如果要基于这些方案来定制，适配和维护的成本过高，基本是不可行的。</p>
<h2 data-id="heading-7">总结</h2>
<p>总而言之，Monorepo 的开发模式就是将各自独立的项目，变成一个统一的工程整体，解决 MultiRepo 下出现的各种痛点，提升研发效率和工程质量。那最后我还有有一个问题，采用 Monorepo 解决了之前的痛点之后，产生了哪些新的问题呢？这些问题可以解决吗？欢迎大家在留言区一起讨论。</p>
<blockquote>
<p>本文首发于公众号《前端三元同学》欢迎大家关注，原文：<a href="https://mp.weixin.qq.com/s?__biz=MzU0MTU4OTU2MA==&mid=2247486144&idx=1&sn=9f9248285a315555b52157115f2fa09a&chksm=fb26e397cc516a81098d5727ca46fc58d85d6e0516828a5f8711e712b8798a654e79fe810a48&token=733579633&lang=zh_CN#rd" target="_blank" rel="nofollow noopener noreferrer">现代前端工程为什么越来越离不开 Monorepo?</a></p>
</blockquote>
<blockquote>
<p>字节跳动 IES 前端架构团队急缺人才（p5/p6/p7大量HC），欢迎加我微信 sanyuan0704 一起来搞事情。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            