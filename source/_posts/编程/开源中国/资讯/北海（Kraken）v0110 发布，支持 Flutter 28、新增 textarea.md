
---
title: '北海（Kraken）v0.11.0 发布，支持 Flutter 2.8、新增 textarea'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.alicdn.com/imgextra/i2/O1CN017CaWCn1fL0emgAyyM_!!6000000003989-1-tps-1080-2400.gif'
author: 开源中国
comments: false
date: Wed, 13 Apr 2022 06:45:00 GMT
thumbnail: 'https://img.alicdn.com/imgextra/i2/O1CN017CaWCn1fL0emgAyyM_!!6000000003989-1-tps-1080-2400.gif'
---

<div>   
<div class="content">
                                                                                            <h1 style="text-align:start"><span><strong><span>前言</span></strong></span></h1> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>历经 3 个月的开发后，北海 Kraken 发布了全新的 v0.11.0 版本。如果你对 </span><span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopenkraken.com%2F" target="_blank"><span>Kraken</span></a></span><span> 还不是那么了解，那么你可以跳到文末阅读我们往期的文章来了解 Kraken 是什么以及它解决了哪些场景下的问题。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>这个版本我们主要进行了几次大的重构，面向未来地给出更合理的架构设计。同时，还增加了 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Ftree%2Fmain%2Fperformance_tests%2Fbenchmark" target="_blank"><span>Benchmark</span></a></span><span> 以及自动化的 CI 工具以衡量首屏性能以及支持了 Textarea。此外，Flutter 的版本也正式升级到了 2.8 。详细的更新日志可以参考</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2Fkraken%2FCHANGELOG.md" target="_blank"><span>CHANGELOG</span></a></span><span>。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>下面为大家介绍该版本的一些重要更新。</span></p> 
<h2 style="text-align:start"><span><strong><span>更新内容</span></strong></span></h2> 
<h3 style="text-align:start"><span><strong><span>支持 textarea 标签</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在本次更新中，Kraken 支持了 textarea 标签，用户可以通过该标签支持多行纯文本的编辑。如果业务场景需要编辑（提交）大量的纯文本信息时，这个标签可以满足需求。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><img align="center" alt="textarea" src="https://img.alicdn.com/imgextra/i2/O1CN017CaWCn1fL0emgAyyM_!!6000000003989-1-tps-1080-2400.gif" width="300" referrerpolicy="no-referrer"></span></p> 
<h3 style="text-align:start"><span><strong><span>增加自动化 Benchmark 统计及衡量首屏性能</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>首屏性能是衡量引擎性能的一个重要重要指标，首屏性能意味着白屏时间的长短，对用户体验有着非常大的影响。Kraken 通过将 QuickJS 作为默认的 JS 引擎，用户可以直接下发 ByteCode 格式的文件来优化应用程序的 JS 执行时间。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Kraken 基于 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Ftree%2Fmain%2Fperformance_tests%2Fbenchmark" target="_blank"><span>Benchmark</span></a></span><span> 衡量首屏数据，该 Benchmark 是一个实际业务场景比较常见的商品列表页。统计从加载完成并开始执行入口文件到 window 上的 load 事件触发的时间，以此衡量实际用户从打开页面到可见的时间。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2Fscripts%2Frun_benchmark.js" target="_blank"><span>Kraken Performance Benchmark</span></a></span><span> 会在当分支 merge 到 main 分支时自动采集以及上传 Kraken 与 Webview 之间的上述性能数据，多次采集后去除抖动并计算平均值。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>具体的最新性能数据可以点击 </span><span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopenkraken.com%2Fguide%2Fperformance" target="_blank"><span>Kraken 官网</span></a></span><span>查看。</span></p> 
<h3 style="text-align:start"><span><strong><span>TSC 会议直播</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>我们期望通过 TSC 的机制来让社区的贡献者更多地参与共建，同时规划以及对设计的讨论能够更加透明，让每个关注 Kraken 的同学了解 Kraken 已经有什么能力，正在做什么功能以及未来要怎么样发展。基于此，我们在每两周例行的 TSC 会议上开始尝试直播，让大家能够了解到 Kraken 的一些讨论以及规划。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>更详细的协作机制以及入群看直播的方式请移步 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2FTSC%2Fblob%2Fmain%2FGOVERNANCE.zh-CN.md" target="_blank"><span>Github TSC</span></a></span><span> 来了解更多。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<h3 style="text-align:start"><span><strong><span>重构事件机制</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>为了形成面向未来的架构设计，以及更好地解决目前已有手势交互及事件体系的复杂度，我们对事件机制进行了一次大的重构。重构后，开发者无论使用 Dart 还是 JavaScript 去监听事件做对应处理，体验上是完全一致的。未来，我们也会基于此在下个版本支持 HTMLView 以支持纯 Dart 的 Web 渲染，敬请期待。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"> </p> 
<h3 style="text-align:start"><span><strong><span>规范发布规则</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>TSC 会议上我们明确了版本的迭代以及发布计划，后续我们将会采用更加规范化的发布规则，具体规则如下：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>增加例行 Patch 位版本发布时机：每周的周四, 采取搭火车的形式，将 main 分支上的内容发布 x.y.(z+1)。</span></p> </li> 
</ul> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>如遇紧急 Bugfix, maintainer 可以随时决定发布 x.y.z+(n+1) 的版本，如 </span><span><code>0.10.2+1</code></span><span>。此决策需至少 2 名 tsc 成员同意。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>增加每天的 nightly version (prerelease) 机器人自动化发布 例如 </span><span><code>0.10.3-nightly.$&#123;commit-hash&#125;。</code></span></p> </li> 
</ul> 
<h3 style="text-align:start"><span><strong><span>Flutter 版本支持</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>0.11.0 版本，Kraken 继续升级所依赖的 Flutter 版本，目前我们已经将依赖的版本升至 2.8.1 。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此外，0.11.0 版本会继续支持 Flutter 2.5.3 的版本，直到 0.12.0 版本发布为止。</span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>注：Kraken 0.11.0 只会发布支持 Flutter 2.8.1 版本的 release 包，支持 Flutter 2.5.3 版本的 release 包需要开发者在 Kraken 的 Github 上 checkout 对应</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Ftree%2Frelease%2Fflutter-2.5.x" target="_blank"><span>分支</span></a></span><span> 的源码下来自行编译。</span></p> 
</blockquote> 
<h3 style="text-align:start"><span><strong><span>Roadmap</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此外，我们也明确了今年计划做的一些新的功能，把具体的一些目标确定了下来，详细细节可以查看</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fwiki%2FRoadmap.zh_CN" target="_blank"><span>Kraken Roadmap</span></a></span><span>。我们的迭代计划可以直接从 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fwiki%2FIteration-Plans" target="_blank"><span>Iteration-Plans</span></a></span><span> 中查看。</span></p> 
<h3 style="text-align:start"><span><strong><span>其他更新</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>除了以上介绍的能力之外，我们也修复了大量的 bug，详细请见 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2Fkraken%2FCHANGELOG.md" target="_blank"><span>CHANGELOG</span></a></span><span>。</span></p> 
<h2 style="text-align:start"><span><strong><span>关于北海 KRAKEN 更多的内容</span></strong></span></h2> 
<h3 style="text-align:start"><span><strong><span>社区协作机制</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>我们期望通过一种良好的社区协作机制，来与社区的众多开发者一起共建 Kraken 底层能力及生态。 Kraken 团队通过</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2FGOVERNANCE.zh-CN.md%23%25E5%258D%258F%25E4%25BD%259C%25E8%2580%2585" target="_blank"><span><strong><span>协作者</span></strong></span></a></span><span>的方式来参与 Kraken 功能迭代以及 issue 讨论等工作。同时，通过由一部分协作者组成的</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2FGOVERNANCE.zh-CN.md%23%25E6%258A%2580%25E6%259C%25AF%25E5%25A7%2594%25E5%2591%2598%25E4%25BC%259A" target="_blank"><span><strong><span>技术委员会（TSC）</span></strong></span></a></span><span>来确定技术方向、发布以及定制标准等工作。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>简单地说，只要向 Openkraken Group 提交一定质量和数量的代码即可成为协作者；对项目提交建设性的贡献后，TSC 成员有权提名协作者参与到 TSC 中。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Kraken 团队期望通过一种友好、共同参与的协作机制，让社区的开发者能够更好地参与到对项目的演进中去，让每个人的声音都能被听到，共同促进 Kraken 以及 Web 标准 的发展。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>更详细的协作机制可以移步 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2FTSC%2Fblob%2Fmaster%2FGOVERNANCE.zh-CN.md" target="_blank"><span><strong><span>Github TSC</span></strong></span></a></span><span>。</span>,</p> 
<h3 style="text-align:start"><span>往期文章推荐</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F366587010" target="_blank"><span>基于 Flutter 的 Web 渲染引擎「北海」正式开源</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F401698292" target="_blank"><span>深入解析基于 Flutter 的 Web 渲染引擎「北海 Kraken 」技术原理</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F453474514" target="_blank"><span>北海（Kraken）构建大前端混合渲染技术体系 —— Web 与 Flutter Widget 混合渲染方案</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F311233545" target="_blank"><span>Flutter 手势原理</span></a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            