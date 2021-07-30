
---
title: '【产品动态】解读Dataphin流批一体的实时研发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8657891b4a7840aa83401d7735c2b167~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 18:02:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8657891b4a7840aa83401d7735c2b167~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> Dataphin作为一款企业级智能数据构建与管理产品，具备全链路实时研发能力，从2019年开始就支撑可集团天猫双11的实时计算需求，文章将详细介绍Dataphin实时计算的能力。</p>
<h1 data-id="heading-0">背景</h1>
<p>每当双11全球购物狂欢节钟声响起，上千万用户涌入天猫、淘宝，流畅的购物体验背后是阿里工程师用技术打造出的营地，支撑了每年双11所带来的数据洪峰。2020年11月1日至11月12日0:00，天猫“双11”累计总交易额达4982亿元，物流订单总量达到23.21亿单。这一切的背后都离不开实时计算技术。</p>
<p>Dataphin作为一款企业级智能数据构建与管理产品，具备全链路实时研发能力，从2019年开始支撑集团天猫双11的实时计算需求。就以下文介绍Dataphin实时计算的能力。</p>
<h1 data-id="heading-1">传统的数仓架构</h1>
<p>在数仓建设过程中，一般来说都是先建设离线数仓，同时围绕着离线数据构建应用。然后随着业务的发展或者体验的优化，再建设实时计算的链路去提升数据的时效性。</p>
<p>在这个过程中相似的代码写两遍就难以避免，还会出现实时和离线口径不一致，分别维护成本增加等各种各样的问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8657891b4a7840aa83401d7735c2b167~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>传统的数仓架构流与批从<strong>存储计算中分离</strong>带来以下的问题：</p>
<ol>
<li><strong>效率问题</strong>：流批底层数据模型不一致，导致应用层做大量的拼接逻辑（同比、环比、二次加工等），搭建效率低且容易出错</li>
<li><strong>质量问题</strong>：一个业务逻辑，两个引擎两套代码，SQL逻辑不能复用，数据一致性和质量问题难以保证</li>
<li><strong>成本问题</strong>：</li>
<li>流批存储系统隔离（面向不同写入场景），提供的数据服务不一，维护成本高</li>
<li>手工建数据同步任务，开发成本/存储成本高（两份）</li>
<li>批处理&流处理集群无法做到错峰，资源利用率低</li>
</ol>
<h1 data-id="heading-2">Dataphin流批一体优势</h1>
<p>为解决传统数仓架构的存储计算分离的问题，有了“流批一体”的思路：</p>
<ol>
<li>流批存储透明化，查询逻辑完全一致，应用端接入成本大幅降低，点查/OLAP分析统一支持</li>
<li>服务层统一存储，无需手工同步，无重复存储</li>
<li>一套代码，两种计算模式，逻辑统一，灵活切换，研发效率大幅提升</li>
<li>流批计算资源混部，资源利用率提升</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41f8879c30c14a4bbc85346e10568bc9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Dataphin在Flink流批一体的能力之上额外提供了更多的平台能力，如数据源管理、元数据管理、资产血缘、资产质量控制、预编译、调试等能力：</p>
<ol>
<li><strong>开发生产隔离</strong>：提供开发环境和生产环境隔离，保证开发环境开发的业务代码和生产相互之间不干扰</li>
<li><strong>元数据管理</strong>：各系统组件包括数据源、元表、UDX等具备权限控制功能，敏感型配置信息加密保护。支持数据源敏感字段访问订阅。元表、函数、资源等全部单元化可视化的管理，支持跨项目鉴权（字段级）调用，让使用者聚焦业务逻辑。</li>
<li><strong>流批一体</strong>：流批存储层的统一管理，实现模型层统一，流批代码统一、通过流批各自专属配置，生产独立有协同的额调度实例</li>
<li><strong>研发提效</strong>：</li>
<li>提供了预编译的能力，提供语法校验、权限校验、字段血缘提取的功能；</li>
<li>容器化调试，支持上传自定义数据或直接消费真实生产数据用来观察作业运行、检查各个节点的输出结果</li>
<li>支持元数据检索，作业依赖、字段血缘的可视化探查</li>
<li><strong>稳定性及质量保障</strong>：</li>
<li>支持流量阈值设置，防止计算资源过度竞争，避免下游系统过载</li>
<li>支持实时元表质量监测，可配置统计趋势监测、实时多链路对比、实时离线数据核对。</li>
</ol>
<h1 data-id="heading-3">开发生产隔离</h1>
<p>Dataphin支持开发生产隔离的项目，支持开发和生产双环境的数据源配置。这样在开发模式下，任务就会自动使用开发数据源和开发环境下的物理表；而当发布到生产环境时，Datpahin则会自动切换为生产数据源及生产环境的物理表。这个过程完全自动化，不用手动修改代码或配置。</p>
<h1 data-id="heading-4">元数据管理</h1>
<p>Dataphin创造性的引入了实时元表和镜像表的概念，将实时研发过程中的表进行了平台化、资产化的统一管理，并简化了研发，提升研发效率和体验。</p>
<p>传统实时任务研发工具需要用户重复写Create table建表语句，需要进行繁琐的输入输出表映射等操作。实时元表将实时开发任务中所有用到的数据表进行了统一表构建与管理，统一维护了所有实时元表和相关schema信息。开发者在开发过程中不用重复写DDL语句；同时，也不需要进行繁杂的输入、输出、维表映射，采用简单的纯代码研发模式，简单的SET语句及权限申请，即可引用表数据，进行直接查询或写入数据，轻松做到一次建表，多次引用，大幅度提升研发效率和体验。</p>
<p>镜像表顾名思义则是用于维护离线表与实时表之间字段的映射关系。创建镜像表并提交发布后，就可以在流批一体的Flink任务中使用镜像表的字段，Datpahin会在编译时自动映射到流表和批表上，实现一份代码，两种计算，代码逻辑、口径变更强一致。</p>
<h1 data-id="heading-5">流批一体的代码任务</h1>
<p>除了引入实时元表与镜像表，Dataphin也支持了流批一体的任务，使用Flink引擎作为统一的流批计算引擎，在一份代码上可同时配置流+批的任务配置，基于同一份代码生成不同模式下的实例。而对于流批差异化的代码，Dataphin也提供了不同的方式给与支持。</p>
<p>流批一体任务中会广泛使用镜像表，而镜像表在最终使用时会翻译为对应的流表/批表，为了适应流表/批表的多样性（流表/批表的数据源可能不一样，带来with参数中key可能不一样；流表/批表的某些设置可能不一样，比如batchSize等），可以利用tableHints进行流表/批表的对应。方法如下：</p>
<p>set project.table.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mrow><mi>m</mi><mi>o</mi><mi>d</mi><mi>e</mi></mrow><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">&#123;mode&#125;.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord"><span class="mord mathnormal">m</span><span class="mord mathnormal">o</span><span class="mord mathnormal">d</span><span class="mord mathnormal">e</span></span><span class="mord">.</span></span></span></span></span>&#123;key&#125; --mode: 流任务：`stream` 批任务：batch</p>
<p>举个例子，设置批任务的起停时间：</p>
<p>set project.table.batch.startTime='2020-11-11 00:00:00'; set project.table.batch.endTime='2020-11-12 00:00:00';</p>
<p>第二种是在Dataphin的任务配置实时和离线模式分别任务参数的方式是利用任务参数进行替换。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/168b14c9ae04407a8d3cdc475c1ec22f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5faa2f3639e4c4cbb0b307b9f2ace46~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b57e98608404d1e845539d4cd03097c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">实时质量监控</h1>
<p>Dataphin实时数据质量主要面向开发者，针对产品中实时产出的数据表，通过对产出结果进行数据质量分析和校验，来保障数据的最终有效与准确。Dataphin支持统计趋势监测、实时多链路对比、实时离线数据核对。</p>
<ol>
<li><strong>统计趋势监测</strong>：趋势监测指的是基于数据趋势变化以及专家经验以捕获波动异常的监测方式；如 实时GMV的趋势陡增有些异常</li>
<li><strong>实时多链路趋势对比</strong>：实时多链路指的是在实时计算的场景中，由于数据的恢复成本较高，无法快速从起点重新计算，因此需要使用多个计算链路，当发生计算异常时，自动/手动切换计算链路，是一种用资源换稳定的策略，当有重大的保障业务时，往往会采用该种类型；如每年双十一大屏都会采用多链路保障。</li>
<li><strong>实时离线核对</strong>：实时离线核对，是保障实时数据常用的一种措施，由于实时计算处于一种持续运算状态，计算时间持久且受资源与源数据的扰动较大；离线数据在逻辑、数据复用性方面可以被更好地操作，因此，为了保障实时数据的准确性，常用离线数据与实时数据进行对比；如每年双十一前都会使用离线数据对实时数据进行校验；</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5210f1e3d03040fcb5fb1c251f0690b2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">双十一大屏后的Dataphin</h1>
<p>回到文章开始的天猫双十一，了解了Dataphin平台特有的能力，我们来具体拆解Dataphin为什么能支撑天猫双十一的实时数据大屏。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d11c49daa8f24e32882d1ad35b25218f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>快</strong></p>
<ol>
<li>Dataphin为实时提供研发、调试、测试、运维全链路一站式服务，极大降低用户开发门槛；</li>
<li>同时提供统一元数据管理，元数据仅需初始化一次，轻松做到一次建表，多次引用，让开发聚焦业务逻辑，大幅度提升研发效率和体验；</li>
<li>另外有数据研发经历的同学都有这样的体会，很多数据口径都惊人的类似，甚至有些只是输入输出表不同，典型的场景比如主备链路，针对这种场景我们提供了模版研发的能力，相同逻辑封装在模版中，差异逻辑通过模版参数体现，新任务仅需引用模版配置模版参数即可，极大提升研发效率的同时也降低了口径维护成本。</li>
</ol>
<p>基于以上能力，在双十一大屏的支持上，尽管业务玩法很多，需求井喷，仍然仅以2人便支撑上百需求。</p>
<p><strong>稳</strong></p>
<p>Dataphin提供任务监控及数据质量监控全方位保障任务稳定，快速发现问题；基于模版的主备多链路在异常发生时可以秒级切换，快速止血；基于实时任务血缘，快速定位问题根因；基于调试、测试、细粒度资源配置，快速验证并修复，真正做到1min发现、5min定位、10min解决。</p>
<p><strong>准</strong></p>
<p>基于流批一体的能力，真正做到代码统一，口径统一，存储统一，数据服务接口统一，研发提效的同时，保证数据一致。</p>
<h1 data-id="heading-8">未来规划</h1>
<p>在即将发布的Flink VVP（Ververica Platform）适配版本将支持新的VVR引擎，也将在未来支持开源Flink引擎已支持更多的部署环境。Dataphin也将持续提升实时研发的能力和体验，帮助企业降低实时研发的门槛，挖掘更多的场景，获得实时数据带来的业务价值！</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000286547%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000286547/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            