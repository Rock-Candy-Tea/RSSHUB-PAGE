
---
title: '飞猪基于 Serverless 的云+端实践与思考'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/db139c269534470e890a8c2c22d29929.png'
author: Dockone
comments: false
date: 2021-05-25 08:10:20
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/db139c269534470e890a8c2c22d29929.png'
---

<div>   
<br>作者 | 王恒飞（承荫）<br>
来源 | <a href="https://mp.weixin.qq.com/s/5H4EmHMmIRoA0DGfssFAyg">阿里巴巴云原生公众号</a><br>
<br>本文整理自飞猪旅行前端技术专家--王恒飞（承荫）在【阿里云 Serverless Developer Meetup 上海站】上的分享。点击查看直播回放：<a href="https://developer.aliyun.com/live/246653"></a><a href="https://developer.aliyun.com/live/246653" rel="nofollow" target="_blank">https://developer.aliyun.com/live/246653</a>。<br>
​<br>
过去两年，飞猪前端一直在积极地进行 Serverless 建设和实践，2019 年 - 2020 年我们和集团 Node 架构组、研发平台一起完成了基础能力的建设和业务试点，成为集团率先落地 Serverless 实践的 BU，2020 年 - 2021 年我们开始大规模地在飞猪推广使用 Serverless 的能力，从导购全链路到核心中后台，都能够看到 Serverless 的身影，这一年我们完成了 Serverless 从业务试点到生产力工具的转变，本文将主要分享飞猪基于 Serverless 的实践成果以及未来想要做的事情。<br>
​<br>
<h1>Serverless 的使用规模</h1>​<br>
2020 年 - 2021 年飞猪 Serverless 的规模和重要度都有很大的变化，主要表现在三方面：<br>
​<br>
- 一是函数组规模增长一倍以上，Qps 峰值增长 650%。<br>
- 二是使用 FaaS 开发的人员规模增长 560%，其中前端人员 80% 以上参与到 FaaS 的开发中。<br>
- 三是影响力的表现，目前不仅飞猪前端都对 Serverless 很熟悉，客户端也有很多人参与到 FaaS 的开发，更重要的是后端和产品同学也知道我们有 Serverless 进行服务开发的能力。<br>
<br>具体的数据如下：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/db139c269534470e890a8c2c22d29929.png" alt="1.png" referrerpolicy="no-referrer"><br>
<br><h1>为什么要引入 Serverless</h1>​<br>
飞猪为什么这么迫切地要引入 Serverless？这主要是出于前后端研发模式升级以及前端职能扩展的考虑，下面回顾一下飞猪前端架构的发展和研发模式的演进。<br>
​<br>
<h2>1. 飞猪前端架构的发展</h2>​<br>
飞猪前端架构总结下来就是从最初纯粹的前端开发，到解决多端一致性的跨端开发，再到接管视图服务端逻辑的前台开发，Serverless 就是前端升级转变的核心一环。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/19391a0458474be8a4da5b62275b7d77.png" alt="2.png" referrerpolicy="no-referrer"><br>
<br><h2>2. 研发模式的演进历程</h2>​<br>
前端人员为什么一定要参与服务侧开发？从前后端研发模式的演进来看，主要经历了以下三个大的阶段：<br>
​<br>
第一阶段是<strong>资源解耦</strong>，这个阶段前端把静态资源分离出来部署到 cdn，解决了和后端服务同机部署的耦合。<br>
​<br>
第二阶段是<strong>模板解耦</strong>，我们之前提到的前后端解耦大部分指的就是模板的解耦，一种不彻底的解法就是渲染解耦，服务端放一个空模板内容部分全靠 CSR，彻底的解法就是前端接管模板，可以独立部署模板也可以使用 node.js 替代。<br>
​<br>
第三个阶段就是<strong>试图解耦</strong>，一方面是由于客户端体系和前端的离线体系的限制，端侧对于视图的动态性要求极高，没有服务侧能力的前端只能将视图的动态性放在服务端做，另一方面由于端侧架构对于数据接口协议的特殊要求，需要服务端来进行协议的转换，也就是服务端常说的 Do 到 Vo 的处理，这就造成了前后端视图的耦合，为了去除这部分耦合，前端通过 Node.js 做 BFF 层来接管视图层的逻辑，Serverless 则是给了前端做 BFF 开发的最佳选择。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/8ed5accec6634872954e0336b8164a3c.png" alt="3.png" referrerpolicy="no-referrer"><br>
<br><h2>3. 为什么一定是 Serverless</h2>​<br>
其实在 Serverless 出现之前，前端也尝试了用 node 应用来做 BFF 层的开发，飞猪也是在 2017 年通过 Midway + React SSR 的架构将飞猪 PC 主链路首页、搜索、商品详情、订单详情 Node 化，但是应用级别的开发在前端存在以下几个问题：<br>
​<br>
- <strong>开发成本高</strong>：Node 应用级别的开发对于新手前端还是具备一定的开发成本，之前做过粗略的估计，上手成本至少需要 3 人/日，还不包括后续的性能优化、内存泄漏排查等一系列能力。<br>
<ul><li><br><strong>运维成本高</strong>：Docker、镜像、机器日志查看、域名申请、机器替换等一系列运维能力对于前端来说具备非常高的复杂度，也是注定无法推广的一个重要原因。</li><li><br><strong>机器成本高</strong>：前端在使用应用开发时过度偏向于前端架构设计带来的应用离散和机器利用率低的问题，根本原因是前端在用页面开发的思维去做应用开发，导致新建一堆应用占用大量闲置机器。</li></ul><br>
<br>2017 - 2019 年也是集团 Node 开发停滞的两年，这个阶段由于上述问题的闲置，Node 开发无法在移动端铺开，前端使用  Node 主要在中后台的开发，这时矛盾主要表现在前端迫切渴望研发模式转变和涉足服务端开发的高昂成本，直到 Serverless 浪潮的出现让我们看到了曙光，下面来看下 Serverless 能给前端带来什么样的变化：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/c940c9210a1748f8b74daf3cac6b732c.png" alt="4.png" referrerpolicy="no-referrer"><br>
<br>Node FaaS 通过将中间件集成到 Runtime 的上下文中，开发通过 Api 的方式调用来实现极低上手和开发成本，只要会写 js 就能在 0.5 人/日内上手 FaaS 开发，同时 Serverless 容器底层通过机器统一管理、镜像统一、灵活调度、按需付费等方式向开发者屏蔽容器的运维，两者结合完美地帮我们解决了之前 Node 应用开发遇到的三大问题，至此前后端研发模式升级的最后一块拼图集齐，前端开始云+端的变革。<br>
<br><h1>飞猪云+端的核心落地场景</h1>​<br>
<h2>1. 落地场景总览</h2>​<br>
从飞猪首页到搜索、频道，再到大促会场，Serverless FaaS 实现了在飞猪导购全链路的覆盖，成为飞猪前端的常用生产力工具之一。另外中后台开发已全面使用 FaaS 开发，并且赋能客户端同学，下图右侧的包体积平台就是飞猪客户端同学使用 Node FaaS 开发完成。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/8fe38b432c7c4ab9bd52198ce63c578e.png" alt="5.png" referrerpolicy="no-referrer"><br>
<br><h2>2. 云+端场景 - 数据协议处理</h2>​<br>
数据协议处理是 BFF 层最为常见的场景，包括接口合并、Do 到 Vo 的转换等，飞猪 80% 以上的 C 端 FaaS 场景都是用作数据协议的处理，通过 FaaS 来做协议转换能够解放服务端，同时增强前端对视图层的控制，可谓一举两得。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/1a1482f615bc4120bce820d8a3951698.png" alt="6.png" referrerpolicy="no-referrer"><br>
<br>一个最新的例子（如下图所示），这是一个飞猪的内容详情页，页面涉及内容中台、评价中台、互动、算法等 5 个以上接口，这些接口都是现成的分散在各个系统，对于前端来说肯定是不想在端上调 5 次接口，不管是从性能还是架构设计上考虑，都是不合理的，这时就需要一个服务端接口的合并，FaaS 就非常适合做这样的事情，通过原子能力的拼装，无需服务端介入，极大缩短了需求的交付周期。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/9b4be41badf04caaaf9a30d1589c562c.png" alt="7.png" referrerpolicy="no-referrer"><br>
<br><h2>3. 云+端场景 - SSR 同构渲染</h2>​<br>
SSR 同构渲染并不是一个新的概念，最早在 React 支持 SSR 的时候，前端就具备一套代码在 Server 和 Client 端执行的能力，飞猪这边早在 2017 年就在 pc 端上线了 Midway + React SSR 的页面。<br>
​<br>
移动端由于流量比 PC 大很多，且在 Server 侧执行 Js 是一个极耗机器资源的操作，通过 Node 应用的方式做 SSR 机器和运维成本跟随着页面流量指数级上升，ROI 并不高，但是 Serverless FaaS 的自动托管，能帮前端解决机器利用率和运维成本的问题。<br>
​<br>
再配合客户端的文档预加载，我们可以做到客户端预加载直出率（500ms下）100%，端外渲染 2s 达标率 90+%，性能提升 80% 以上。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/79b51d18c4d64f3d806945aae58740b8.png" alt="8.png" referrerpolicy="no-referrer"><br>
<br><h2>4. 云+端场景 - 一体化应用</h2>​<br>
一体化研发是一种更加符合前端人员习惯的开发模式，常见的分为中后台一体化和 Rax+FaaS 一体化，将 FaaS 代码和 Assets 代码在一个仓库下开发，调试和部署能够极大地提高开发效率，目前飞猪用得最多的就是中后台一体化开发。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/224d4c1959564effbacd562751d0c814.png" alt="9.png" referrerpolicy="no-referrer"><br>
<br><h1>Serverless 研发配套建设</h1>​<br>
在基础建设方面定义为两部分：<strong>研发态效率的提升</strong>和<strong>运行时稳定性的保障</strong>。<br>
​<br>
<h2>1. 研发态效率</h2>​<br>
开发阶段主要涉及的操作是新建项目、调试和发布，飞猪通过已有的 Clam 工程体系集成 FaaS 的脚手架模板，对接 def api 打通创建项目、迭代和发布的能力，让前端同学开发 FaaS 能有和开发页面一样的体验，降低上手和开发成本，同时封装 Mtop 调用和容灾 SDK，封装常用 FaaS Utils 集合的方式提高代码的复用度。<br>
​<br>
<h2>2. 运行时稳定性</h2>​<br>
通过函数监控 Alinode、网关监控 Sunfire 以及全链路日志的排查能力，做到问题的快速发现和定位。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/ad9bb299b1c24bd59effafa5299f7154.png" alt="10.png" referrerpolicy="no-referrer"><br>
<br>通过 tair 容灾和 cdn 容灾，保障大部分场景在函数或者网关挂掉的情况下，仍能够正常展示页面。<br>
<br><h1>未来</h1>​<br>
2020 年 - 2021 年我们完成了 Serverless 向生产力工具的转变，2021 年 - 2022 年总体来看是彻底完成飞猪研发模式转变的目标，让 FaaS 成为前后端都习以为常的一环，规划还没做具体，有以下几个关键的事情要做：<br>
​<br>
- <strong>中后台和长尾函数 0 - 1 的弹起尝试</strong>：这块考虑到一些中后台函数和长尾函数每天可能只有几十个 Uv 够不到 Qps 级别，目前预留 1 核机器的方式仍是有些浪费，考虑在不影响初次请求的情况下尝试 0 到 1 的弹起，做到机器的极致利用率。<br>
<ul><li><br><strong>飞猪物理网关的替换</strong>：目前虽然飞猪 Java 的网关出于维护状态投入较低，但是一旦流量发生变化，网关的稳定性会成为瓶颈，希望能够有 Fc 专门的团队接管流量网关，之前飞猪也是完成了一个线上试点，2021 年 - 2022 年继续推进。</li><li><br><strong>研发态和运行时问题的可观测增强</strong>：从 FC 底层容器到函数代码内部再到函数依赖、流量网关，不管是部署出现的问题还是线上的问题，都比较难定位，通常需要拉着 FC、研发平台、Runtime 的同学一块排查，后续希望能推动可观测性的增强，让业务开发能够快速发现问题。</li></ul><br>
<br><h1>写在最后</h1>​<br>
基于 Serverless 的云+端结合已经基本成型，这将是前端近些年来最大的变革之一，未来 FaaS 将是前端开发不可或缺的一环，我们需要用它来做研发模式升级，也需要用它帮助前端扩大职能，通过 FaaS 的能力让前端开发深入到服务层，更好地贴近业务、理解业务、帮助业务。<br>
​<br>
<h2>作者简介</h2>​<br>
<strong>王恒飞（承荫）</strong>，飞猪旅行前端技术专家，飞猪 Serverless 引进和实践者，探索和推动云+端的研发模式。
                                
                                                              
</div>
            