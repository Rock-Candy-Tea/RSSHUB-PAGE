
---
title: '聊聊Push系统'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70264879199244bdb6507b07d213dfc4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 16:40:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70264879199244bdb6507b07d213dfc4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近一年多工作的主要精力都放在了Push系统的开发上，投入了不少心血在里面，但是这一年多的时间一直在写代码埋头赶路，疏于总结，借此机会回顾总结下系统的相关设计，希望对自己与读者都有所帮助。</p>
<h3 data-id="heading-0">概念</h3>
<p>Push：有主动推的意思，实际上就是一个服务端主动推送消息到用户App的一个系统。从用户的视角Push</p>
<ul>
<li>App外部：主要展示形式为手机通知(手机系统功能，样式固定)。</li>
<li>App内部：展示根据需求可以定制展示样式，各种Pop</li>
</ul>
<p>从技术的角度来看，主动推送的东西主要是数据，数据可以用作上面的展示，也可以推一些无需展示内部处理的数据到客户端端上，但最终目的都是为了用户的体验。</p>
<h3 data-id="heading-1">架构</h3>
<p>Push系统初始状态下包含的元素，只有发送者，系统通道，接收者。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70264879199244bdb6507b07d213dfc4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210524072122446" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发送者：生产推送内容的人，生产内容的方式
系统通道：将生产的内容触达的用户的通道，可以看做Push系统的核心</p>
<ul>
<li>能对接各大手机厂商，用户设备离线状态下交给厂商发送</li>
<li>自建服务器与用户App的长连接通道，在线状态下直接通过自建通道触达用户</li>
</ul>
<p>接收者：用户，内容在用户手机上展示</p>
<p>以上肯定比较简化，想要让其真正成为一个系统，还需要更多的事情在其中，比如说单次发送1亿条用户呢？
系统上则需要将人群进行分片，分到不同的机器上处理这件事情，还有最好能灰度发送，如果对系统有一定压力还需要进行限流。当然还有对后续的效果有一定的监控措施，实时的数据表现。</p>
<ul>
<li>大数据处理：任务分发</li>
<li>并发处理：灰度，限流</li>
<li>数据监控：数据平台</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9b3c704e7534eb59436df5f58475926~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210524073656071" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然还可以在运营侧做一些东西，降低风险，增加一些审批流，所有发送内容数据管控，运营之外还有许多需要用到通道的业务进行支持。</p>
<ul>
<li>内容系统：所有的用户可接触内容</li>
<li>开放平台：系统功能对外服务，支持横线业务</li>
<li>审批流：保护系统安全，防止一些胡乱操作</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eec90552b9d44e09fa763e7ca8b6c1e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210524074728974" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果用户量较大，纯手动方式肯定是无法完成的，需要一些精细化的控制，个性化服务，内容个性化，时间个性化。此时系统的各种入口在抢占通道资源，还需要对通道做一些优先级分配，一些监控报警。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52637691e5904c79a1888223aa4286e8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210524080953525" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里基本上大致的元素都具备了，还能做的是一些细节的打磨，还有组件的职责，做一些决策：</p>
<ul>
<li>通过系统定义运营的工作流程</li>
<li>整个开放平台，运营平台的易用性</li>
<li>系统的稳定性，扩展性；一些压测链路改造，模型的设计。除了Push，系统还可以是什么？</li>
</ul>
<h4 data-id="heading-2">服务组成</h4>
<p>其中一些比较重要的的服务或者依赖的平台：</p>
<ul>
<li>内容平台
<ul>
<li>内容安全工具</li>
</ul>
</li>
<li>审批流平台</li>
<li>算法平台</li>
<li>数据平台</li>
<li>长连接平台</li>
<li>配置中心</li>
<li>监控报警中心</li>
<li>...</li>
</ul>
<h4 data-id="heading-3">技术使用</h4>
<p>主要用到的技术：</p>
<ul>
<li>缓存，限流，降级</li>
<li>配置中心，消息队列，调度中心，集群存储，RPC调用，日志管理</li>
<li>实时计算平台，离线计算平台</li>
<li>多线程知识，一些设计模式</li>
</ul>
<h3 data-id="heading-4">想法</h3>
<p>技术上不见得多么高深，主要因为用户基数较大，一定程度上增加了系统的复杂性。在技术上，在内部都有对应的平台封装了技术难点，真正技术难点的地方在一些底层或者中间件那边处理。</p>
<p>而业务开发主要做的事情，目前变成了理清楚业务重点，识别技术阻碍，推动项目进行。对分析能力，社交能力的要求高于技术的能力。</p>
<p>当然因为自己是技术，还是不能停下对技术的学习和探索上。</p>
<h3 data-id="heading-5">最后</h3>
<p>时间有限，能想到的Push中比较有印象的东西应该都有提到，希望能对读者有所帮助。</p></div>  
</div>
            