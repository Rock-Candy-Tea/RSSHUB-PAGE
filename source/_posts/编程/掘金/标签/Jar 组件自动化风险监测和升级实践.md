
---
title: 'Jar 组件自动化风险监测和升级实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2bd4093beb940dcb6cfb0959bc81ec4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 19:56:10 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2bd4093beb940dcb6cfb0959bc81ec4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2bd4093beb940dcb6cfb0959bc81ec4~tplv-k3u1fbpfcp-watermark.image" width="60%" loading="lazy" referrerpolicy="no-referrer">
<p><strong>曾兆祜</strong></p>
<blockquote>
<p>2018年5月加入去哪儿网,现负责基础安全攻防平台的开发建设以及日常的安全运营工作</p>
</blockquote>
<h2 data-id="heading-0">背景</h2>
<p>以 Xstream、Jackson、Fasjson 等为代表的 Jar 组件高危漏洞层出不穷，安全组每年 N 次推动业务线进行第三方 Jar 组件升级，每次升级动辄涉及成百上千个应用服务，给双方都带来了沉重的负担。为了降低安全组在 Jar 组件升级期间的工作量，同时尽量给业务线减负，Qunar 安全组在 Jar 组件自动化风险监测和升级上进行了大量实践，并总结形成了一套相对完善的解决方案。本主主要聊一下 Qunar 安全组在 Jar 组件自动化风险监测和升级方面的探索和实践。</p>
<h2 data-id="heading-1">流程介绍</h2>
<p>Jar 组件风险监测和升级本质是由风险情报驱动的一个工作流，主要包括外部安全通告监控、Jar 组件资产收集、受影响资产分析、通知业务线升级等流程。在之前一段时期，Jar 组件漏洞升级依靠安全运营人员人工的方式来串联每个流程，这样效率低下，甚至容易出错。随着 SOAR（安全编排自动化与响应）近年来的备受关注，Qunar 安全组也在 SOAR 项目上进行了建设，依托 SOAR 对事件的整合和安全服务串联能力，我们针对 Jar 组件风险监测和升级场景进行了合理编排，达到了自动化的效果，极大提升了安全运营效率。除此之外基础架构的同事，提供了 TCDEV 自动升级服务，为业务线升级操作提供了极大便利。事件流程如下图所示：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b5bc9cacf1415ea55a9cc430af4643~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">技术实现</h2>
<p>本部分主要介绍 SOAR 串联的每部分安全工具、服务的技术实现。</p>
<h4 data-id="heading-3">1. 安全通告监控</h4>
<p>安全运营人员第一时间获取漏洞通告，对漏洞的评估研判、迅速响应和有序推动至关重要。早在19年，安全组借助应届生项目，实现了“安全漏洞智能感知系统”。系统主要功能为：\</p>
<ul>
<li>CVE、CNVD 以及知名厂商漏洞风险告警抓取</li>
<li>漏洞信息去重整合</li>
<li>对存在 POC 的漏洞抓取 POC</li>
<li>漏洞信息模糊匹配关联 Jar 组件资产库（SecDB），IM 预警安全运营人员</li>
</ul>
<p>该系统关键点在于会通过模糊匹配的方式关联 Jar 组件资产库，关联到资产后 IM 发送预警信息给安全运营人员，进行进一步的风险评估以及后续的 Jar 组件升级流程。系统流程图如下：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/683d8b443206485e8e6313cfa0c170fc~tplv-k3u1fbpfcp-watermark.image" alt="3.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>漏洞感知平台，以 Xstream 为例抓取效果图：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95c0827404f749209f5f9792dc72a1e2~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">2. Jar资产收集</h4>
<p>安全资产收集是安全运营的必备基础能力之一，Qunar 安全组历来都把资产收集做到了业内最好的水准。当前我们采用以 HIDS 为主要平台，通过在 Agent 端调度资产收集插件的方式，高效的对主机的资产进行定时、实时的采集。Agent 调度示意图：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aad3f3f2b2cf4a22a3df22b618d63f6b~tplv-k3u1fbpfcp-watermark.image" alt="5.jpg" loading="lazy" referrerpolicy="no-referrer">
Jar 组件资产收集插件的主要实现思路如下：</p>
<ul>
<li>查找 cataline.base 列表</li>
</ul>
<pre><code class="copyable">items=$(ps aux | grep catalina.base | grep -v grep)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>获取 catalina.home、catalina.base 等路径信息</li>
</ul>
<pre><code class="copyable">catalina_home=$(echo "$item" | tr ' ' '\n' | grep catalina.home | cut -d= -f2 | sort | uniq)
catalina_base=$(echo "$item" | tr ' ' '\n' | grep catalina.base | cut -d= -f2 | sort | uniq)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>根据 server.xml 获取  以及  信息</li>
<li>根据 appBase 或者 docBase 定位 WEB-INF/lib 路径</li>
<li>枚举 WEB-INF/lib 路径下 Jar 包，提取每个 Jar 包的 pom.properties 信息，这样就可以进行资产收集了，例如：</li>
</ul>
<pre><code class="copyable">jar_version=$(echo "$pom_properties" | grep -m 1 -E '^version=' | awk -F'=' '&#123;print $NF&#125;' | tr -d '\n\r')
jar_groupid=$(echo "$pom_properties" | grep -m 1 -E '^groupId=' | awk -F'=' '&#123;print $NF&#125;' | tr -d '\n\r')
jar_artifactid=$(echo "$pom_properties" | grep -m 1 -E '^artifactId=' | awk -F'=' '&#123;print $NF&#125;' | tr -d '\n\r')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上手段的就可以获取主机上存活 Java 项目依赖的 Jar 包信息，一旦爆发漏洞根据以上信息，关联应用以及 Owner 快速响应。以 Xstream 为例，收集的资产信息如下：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97ca4a55e95f4a43a297d2c82b5a302c~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3. SOAR</h3>
<p>SOAR 全称 Security Orchestration, Automation and Response，即安全编排自动化与响应，该技术主要聚焦于安全运营领域。Qunar 安全组基于 StackStorm 工作流引擎二次开发打造了 SOAR 项目，安全组件和剧本通过 python 和 yaml 实现。在 Jar 组件自动化风险监测和升级场景中流程如下图所示：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dc844d352154258b01f149e31182ce4~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer">
从工作流流程图，我们可以看出：</p>
<p>① 安全通告监控服务发出预警信息后，需要人工干预。安全运营人员会研判是否启动升级流程，如果是，则填写配置漏洞信息，启动升级流程；否则，忽略该告警信息</p>
<p>② 启动升级流程后，首先需要关联信息生成受影响资产清单
a) 资产列表生成：根据配置的版本信息进行逻辑过滤，生成受影响资产的列表，同时标记内外网，以执行不同的优先级策略<br>
b) 关联 Appcode：通过 Portal API 获取受影响主机对应的 Appcode<br>
c) 关联 Owner：通过  Portal API 获取受影响主机对应的 Owner<br>
d) 关联技术 TL：通过 ISAPI 员工信息关联 Owner 的技术 TL（技术 TL 充当安全对接人的角色，执行自上而下的漏洞升级推动工作）</p>
<p>③ 接下来会将资产清单提供给 tcdev，tcdev 会接管可自动化升级的应用，剩余部分继续由安全负责通知业务线技术 TL 升级</p>
<p>Xstream 漏洞升级示例，配置漏洞信息，启动自动关联信息升级通知流程：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bfaa0fa89df4c2cab77ab34a781d57e~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Xstream 安全通知示例，通过内部 IM 通知技术 TL 执行升级任务：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/529a4c905a2e4fc6b07f8a661b194261~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">4. TCDEV自动升级服务</h3>
<p>一般的公司，将风险事件通知负责人后整个事件流程就结束了，然后执行周期性的通知升级。但是在 Qunar 内部，基于 TCDEV 开发的自动升级服务，可以极大解放业务线的风险组件升级压力。<br>
TCDEV 自动升级服务可以帮助业务线自动进行 Jar 组件升级，当前 50% 的应用可以自动化升级， 30% 的应用可以通过 TCDEV 提供的一键升级服务进行一键升级（需业务线开发评估风险），另外 20% 应用执行安全组传统的升级策略。TCDEV 自动升级详情如下：</p>
<ul>
<li>
<p>应用已经升级 tcdev 4.x，且已接入灭霸自动化测试的应用，tcdev 接管升级，届时会联系业务确认（应用占比 50%）</p>
</li>
<li>
<p>应用已升级 tcdev 4.x，但自动化测试未覆盖的应用，可在 portal 上点击 “tcbom升级” 快速完成（应用占比30%）\</p>
</li>
<li>
<p>尚未升级 tcdev 4.x 的应用，建议手动升级 tcdev 至 4.0.x （应用占比20%）</p>
</li>
</ul>
<h2 data-id="heading-7">总结</h2>
<p>以上就是 Jar 组件自动化风险监测和升级实践中涉及的方方面面。整体流程还有优化提升的空间，比如在漏洞评估和 TCDEV 自动升级服务还需要人工介入等。另外，TCDEV 自动升级服务价值极大，由于资料较少，没有触及原理实现，希望基础架构的同学可以写一篇文章介绍一下。由于水平有限，文章多有纰漏不足，也恳请大家指正。</p></div>  
</div>
            