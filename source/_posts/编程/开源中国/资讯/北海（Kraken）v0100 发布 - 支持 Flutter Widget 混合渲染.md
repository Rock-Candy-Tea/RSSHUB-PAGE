
---
title: '北海（Kraken）v0.10.0 发布 - 支持 Flutter Widget 混合渲染'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.alicdn.com/imgextra/i3/O1CN01a5CQfQ1CXimHsTvx5_!!6000000000091-2-tps-1500-776.png'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 15:58:00 GMT
thumbnail: 'https://img.alicdn.com/imgextra/i3/O1CN01a5CQfQ1CXimHsTvx5_!!6000000000091-2-tps-1500-776.png'
---

<div>   
<div class="content">
                                                                                            <h2>前言</h2> 
<p>经过 2 个多月紧张的开发工作，今天我们发布了全新的 0.10.0 版本，该版本的核心功能是支持 Flutter Widget 混合渲染方案，将 Flutter Widget 简单封装成 Custom Element 就可以提供给前端使用，不仅丰富了前端的组件生态，而且可以通过接入 Native 的高性能容器接入更多的业务场景。以下介绍该版本的主要更新内容。</p> 
<h2>更新内容</h2> 
<h3>支持 Flutter Widget 混合渲染</h3> 
<p>之前 Kraken 对于 Flutter Widget 的支持只限于简单的 leaf 节点（如图片、视频、文本等），在 0.10.0 版本中 Kraken 支持了完整的混合渲染，可以接入类似瀑布流、长列表这种的复杂容器类型，使得 Flutter Widget 与 Kraken 互相嵌套成为可能。</p> 
<p>下面示例演示了如何将 Flutter 的下拉刷新与瀑布流 Widget 封装成自定义组件，并且在前端使用。</p> 
<ol> 
 <li>在 Dart 侧将 EasyFresh 与 WaterfallFlow Widget 封装成 Custom Element。</li> 
</ol> 
<p><img alt src="https://img.alicdn.com/imgextra/i3/O1CN01a5CQfQ1CXimHsTvx5_!!6000000000091-2-tps-1500-776.png" referrerpolicy="no-referrer"></p> 
<ol start="2"> 
 <li>在前端通过标准的 DOM API 创建自定义组件，然后在 JSX 中使用。</li> 
</ol> 
<p><img alt src="https://img.alicdn.com/imgextra/i3/O1CN01jZdy4o25Wch9sSsyv_!!6000000007534-2-tps-2088-790.png" referrerpolicy="no-referrer"></p> 
<p>Web 与 Flutter Widget 混合渲染能力在大前端的技术体系融合的背景下，使得前端能发挥自身渲染能力强、开发效率高的优势专注于页面排版和业务逻辑组装，客户端能发挥性能好、交互丰富的优势专注于各种高性能容器（如下拉刷新、可回收列表、瀑布流）的开发，达到能力与生产效率的最大化。详细的技术方案可以参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F453474514" target="_blank">《北海（Kraken）构建大前端混合渲染技术体系 —— Web 与 Flutter Widget 混合渲染方案</a> 这篇文章。</p> 
<h3>样式能力增强</h3> 
<p>0.10.0 版本在渲染能力上主要是补强了样式方面的能力，我们补齐了 <code><style></code> 、<code><link></code> 标签与 <code>className</code> 这些常用的 CSS 能力，通过 className 实现的样式共享，相对于内联样式能减少样式字符串在 JSBridge 上的传输时间，并减少 dart 侧内存占用。</p> 
<p>另外我们支持了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2FUsing_CSS_custom_properties" target="_blank">CSS Variables</a> 特性，通过 CSS Variables 可以在前端方便地适配 APP 的深色模式(Dark Mode)，下图为问大家页面的深色模式示例。</p> 
<p><img alt height="600" src="https://img.alicdn.com/imgextra/i4/O1CN01jvEFYU1nTGi9SBJNi_!!6000000005090-0-tps-1080-2160.jpg" width="300" referrerpolicy="no-referrer"></p> 
<h3>性能优化</h3> 
<p>0.10.0 版本的另一个重点是优化性能与提升应用稳定性，通过代码架构上系统的重构，我们修复了诸多影响首屏性能、滚动帧率、内存占用的问题，保证了落地的业务能够通过发布的性能基线。</p> 
<h4>JSBridge 性能优化</h4> 
<p>在 JSBridge 侧通过优化 JS 对象创建时间、以及优化 createElement 与 createTextNode 的耗时的手段，提升 C++ 侧创建 JS DOM tree 的整体时间。</p> 
<h4>Layout 性能优化</h4> 
<p>通过加缓存的方式减少不必要 renderObject 的 constraints 计算减少 Layout 阶段耗时，在深度 Flex 容器嵌套的场景下性能提升 45% 左右。另外我们也优化了长文本的渲染性能，在 overflow hidden 容器中只渲染可见部分本文，减少不必要的文本渲染。</p> 
<h4>性能测试</h4> 
<p>我们构造了一个无限加载的长列表页面，测试机为低端安卓机小米 6，分别对比了 0.9.0 与 0.10.0 版本在首屏加载与滚动帧率方面的表现。</p> 
<p>下面视频为两个版本在 0.5 倍速下首屏加载时间的对比，左侧为 0.10.0 版本，右侧为 0.9.0 版本，优化首屏时间提升 10% 左右。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-43fa7ca63f1ed0ec3ee3e11a0effa303e17.gif" referrerpolicy="no-referrer"></p> 
<p>下面视频为两个版本滚动帧率的对比，左侧为 0.10.0 版本，右侧为 0.9.0 版本，无限滚动时滚动到一定的数量的节点会动态创建新的节点，旧版本 Layout 耗时较多有比较明显的卡顿，新版本优化后滚动会顺畅许多，在低端安卓机小米 6 上帧率能达到 50 fps 左右。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2098791431f7a89fc1d5ac38515c792ef84.gif" referrerpolicy="no-referrer"></p> 
<h3>Flutter 版本支持</h3> 
<p>0.10.0 版本对 Flutter 的支持度升级到了 2.5.3，Flutter 2.5 是 Flutter 历史上排名第二的大版本更新，主要对性能与开发工具方面进行了大量改进。</p> 
<p>另外 0.10.0 版本会继续支持 Flutter 2.2 版本，直到 0.11.0 版本发布为止，注意 Kraken 0.10.0 只会发布支持 Flutter 2.5.3 版本的 release 包，支持 Flutter 2.2 版本的 release 包需要开发者在 Kraken 的 Github 上 checkout <code>0.10.0-flutter-2.2tag</code> 的源码下来自行编译。</p> 
<h3>Linux 支持</h3> 
<p>0.10.0 版本新增了对于 Linux 系统的支持，编译方式请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2FREADME.md" target="_blank">README</a>。</p> 
<h3>其他更新</h3> 
<p>除了以上介绍的能力之外，我们也修复了大量渲染一致性方面与性能方面的 bug，详细请见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2Fkraken%2FCHANGELOG.md" target="_blank">CHNAGELOG</a>。</p> 
<h2>关于北海 KRAKEN 更多的内容</h2> 
<h3>社区协作机制</h3> 
<p>我们期望通过一种良好的社区协作机制，来与社区的众多开发者一起共建 Kraken 底层能力及生态。 Kraken 团队通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2FGOVERNANCE.zh-CN.md%23%25E5%258D%258F%25E4%25BD%259C%25E8%2580%2585" target="_blank">协作者</a>的方式来参与 Kraken 功能迭代以及 issue 讨论等工作。同时，通过由一部分协作者组成的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2FGOVERNANCE.zh-CN.md%23%25E6%258A%2580%25E6%259C%25AF%25E5%25A7%2594%25E5%2591%2598%25E4%25BC%259A" target="_blank">技术委员会（TSC）</a>来确定技术方向、发布以及定制标准等工作。</p> 
<p>简单地说，只要向 Openkraken Group 提交一定质量和数量的代码即可成为协作者；对项目提交建设性的贡献后，TSC 成员有权提名协作者参与到 TSC 中。</p> 
<p>Kraken 团队期望通过一种友好、共同参与的协作机制，让社区的开发者能够更好地参与到对项目的演进中去，让每个人的声音都能被听到，共同促进 Kraken 以及 Web 标准 的发展。</p> 
<p>更详细的协作机制可以移步 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2FTSC%2Fblob%2Fmaster%2FGOVERNANCE.zh-CN.md" target="_blank">Github TSC</a>。</p>
                                        </div>
                                      
</div>
            