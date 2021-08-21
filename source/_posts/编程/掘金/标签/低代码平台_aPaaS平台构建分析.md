
---
title: '低代码平台_aPaaS平台构建分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3895edb289a247899bcab317214296fc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 18:33:00 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3895edb289a247899bcab317214296fc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>现今低代码市场越来越火爆，随着技术的进步，5G技术的发展，软件技术的不断成熟，设计思想的不断完善，降本增效是每个企业管理的主旋律，推动企业内部信息化迈向数字化的改造，选择一款类似瑞士军刀的开发工具快速落地，加速企业的数字化改造是每个企业的需求。</p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>传统的一行一行代码进行定制开发，不仅费时费力，低代码的推出为市场注入了新的理念；以下就低代码平台的构建以及行业信息做简要分享</p>
<h1 data-id="heading-1">低代码系统规划</h1>
<h2 data-id="heading-2">通用低代码平台能力框架</h2>
<p>➢ 代表了能帮助开发人员用拖拽式操作、直观地创建出应用程序的一系列的开发工具(即低代码开发平台)和方法(即低 代码开发方案)。</p>
<p>➢ 低代码开发”就是开发人员可以通过编写少量代码甚至无需代码就可以快速生成应用程序的一种方法。我们有时把“低 代码”作为名词用，这时候我们把它看作一个像Python语言和C#语言一样的一种“东西”。我们有时也把“低代码” 作为动词用，这时候它表达的是它字面上代表的一种应用程序开发方式，因为用这种方式开发应用程序时，你需要手写 的代码比通常的开发方式要少很多，在部分场景下甚至可以完全不写代码。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3895edb289a247899bcab317214296fc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">低代码平台构建技术</h2>
<p><strong>以数据和工作流为基础，通过IDE或模型驱动实现平台搭建</strong></p>
<p>用户通常可以利用表结构、视图、统计、自定义页面、用户角色权限、工作流6个组件，以数据管理和工作流为基础，通 过IDE开发环境驱动或模型驱动两种技术路径来搭建低代码平台。基于IDE框架的快速开发平台是指将传统的集成开发环境 (IDE)充分可视化，允许开发者使用配置面板和控制台来替代相当比例的代码编写。IDE模式灵活性更高，但应用开发过 程管理复杂，所以主要针对IT专业人员，典型厂商如美国Outsystems和欧洲Bettyblocks均采用此技术路径。而模型驱动 开发平台进一步降低了代码开发工作量，但在一定程度上牺牲了应用实现自由度，国内厂商如奥哲、轻流、明道云、伙伴 云等均采用此技术路径。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/babe38538c744b62a4a3d69248649f01~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">低代码生态技术</h2>
<h3 data-id="heading-5">供给端角度</h3>
<pre><code class="copyable">完善底层架构模型，丰富应用模板，拓展产品应用能力圈
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从供给端来看，低代码生态主要集中在云计算产业链上，在底层部署上可以实现私有云、公有云、混合云多种部署方式， 满足不同行业客户需求。在低代码的核心APaaS层，产品相关应用主要涉及到各种引擎、数据库等中间件，以及DevOps 和监控安全等服务。目前越来越多的底层框架采用更加灵活的微服务架构，使得低代码可以更好的完成二次开发和应用拓 展。SaaS层产品如ERP、CRM、HRM等可以满足跨行业、跨部门的通用性需求，未来随着APaaS层引擎种类的增加、底 层架构模型的完善、应用模板的丰富度提升，低代码将赋予SaaS应用更多能力。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a053af007f984bcca1db1c626b42f3f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">需求端角度</h3>
<pre><code class="copyable">通过与渠道伙伴合作，增加低代码产品的应用渗透
<span class="copy-code-btn">复制代码</span></code></pre>
<p>低代码需求端生态建设主要在于应用客户的拓展，目前低代码的应用客户更多集中在IT开发人员、部分业务人员，众多场 景仍依赖于实施方或者低代码厂商的服务。低代码在客户应用中的渗透整体较低，根据Forrester预测，全球低代码渗透率 达到三分之一，中国整体应用渗透率仍然较低约在5%左右，一方面是因为市场教育不足，厂商对于低代码的认知度有待 提升，另一方面是因为需求端生态不完善，渠道代理商和专业培训商的数量不足，在客户中的渗透速度较慢。但随着低代 码的核心价值被企业客户感知，叠加渠道方的全方位宣传，软件开发的形式一定会产生质的变化，行业的需求生态也会随之丰富。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68d186e666614e909c561a9ff02ae169~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">低代码厂商图谱</h2>
<pre><code class="copyable">通用型厂商和垂直型厂商共同为企业应用开发赋能
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前国内低代码行业竞争格局主要分为通用型厂商、垂直型厂商、其他低代码开发平台三种类型，其中通用型厂商中又 有低代码原生厂商、以应用开发为主的厂商以及SaaS软件或者云厂商转型做低代码的厂商，市场整体格局较为分散。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ace5e9661fc64d67bacd88c9ccd626e9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上仅为部分分享，如果你也对低代码平台建设感兴趣，欢迎加入“<strong>一起学开源</strong>”公众号，大家一起交流学习</p></div>  
</div>
            