
---
title: 'Envoy Gateway来了'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=2191'
author: Dockone
comments: false
date: 2022-05-27 00:44:26
thumbnail: 'https://picsum.photos/400/300?random=2191'
---

<div>   
<br>今天，我们很高兴向大家推介Envoy Gateway——Envoy代理家族的新成员。它的出现，将显著降低大家在使用Envoy for API Gateway时的上手门槛。<br>
<h3>背景介绍</h3>Envoy项目最初以开源软件的姿态亮相于2016年秋季。令我们意想不到的是，Envoy很快在整个行业中广受关注，用户们被它包容而开放的社区、强大的可扩展性、API驱动的配置模型、直观的可观察输出以及日益广泛的功能集所吸引，纷纷给予好评。<br>
<br>尽管在早期发展阶段，Envoy总让人们联想到“服务网格（Service Mesh）”，但它在Lyft上的首秀其实是以API网关/边缘代理的角色出现的。当时的Envoy主要提供深入的可观察输出，帮助Lyft从单体式架构迁移至微服务架构。<br>
<br>过去五年多以来，Envoy得到众多最终用户的青睐，也逐渐从API网关成长为“服务网格”中的sidecar代理。与此同时，我们还看到围绕Envoy涌现出了庞大的供应商生态系统，他们开始在开源软件及专有领域提供各类解决方案。Envoy的供应商生态系统也成为项目成功的牢固根基——如果没有这股力量反哺项目中的全职或兼职贡献者，Envoy绝对不可能成长到今天的规模。<br>
<br>作为各种架构类型和供应商解决方案中的常客，Envoy特别招人喜欢的一点就是它在本质上属于底层工具。Envoy这款软件并不容易上手，虽然项目已经在全球各类大型工程团队中得到肯定和成功，但那些体量不大、难度较低的用例仍然是Nginx和HAProxy的天下。<br>
<br>Envoy Gateway项目的诞生正源自这样一个信念，即让Envoy通过以下两大改进以API网关的姿态“走入寻常百姓家”：<br>
<ul><li>针对轻量化用例提供经过简化的部署模型和API层。</li><li>将现有CNCF API网关项目（包括Contour和Emissary）合并成统一的通用核心，在提供最佳上手体验的同时，继续支持供应商构建基于Envoy Proxy和Envoy Gateway的增值解决方案。</li></ul><br>
<br>我们坚信，只要社区能够团结Envoy家族旗下的统一API网关核心周围，就能：<br>
<ul><li>减少由安全、控制平面技术细节及其他关注重点所带来的重复性工作。</li><li>帮助供应商专注于在Envoy Proxy和Envoy Gateway之上，通过扩展、管理平面UI等形式打造出更多分层增值功能。</li><li>正所谓“水涨船高”，无论具体规模如何，全球用户将更多享受到Envoy软件家族的强大功能。用户数量的增加将吸引更多潜在使用者，进而为核心Envoy项目提供更多支持，最终让所有人都获得最佳整体体验。</li></ul><br>
<br><h3>项目概述</h3>总体来讲，Envoy Gateway可以被理解成Envoy Proxy核心的打包器。它不会对核心代理、xDS、go-control-plane等做出任何更改（潜在的驱动功能、bug修复和常规改进除外）。Envoy Gateway可提供以下功能：<br>
<ul><li>一个面向网关用例的简化API。这里的API正是Kubernetes Gateway API，其中附带有Envoy专用扩展。之所以选择Kubernetes Gateway API，是因为它最初的设计目标就是作为部署在Kubernetes上的入口控制器，而且已经得到了行业的广泛认可。</li><li>提供“内含电池”体验，确保用户能够快速启动、快速运行。这一体验具体涵盖控制器资源、控制平面资源、代理实例等工具。</li><li>可扩展的API接口。虽然Envoy Gateway主要强调以开箱即用方式为用户提供通用API网关功能（例如速率限制、身份验证、Let’s Encrypt集成等），但供应商也可借此提供所有API的SaaS版本、其他API，以及包括WAF、增强可观察性、混沌工程在内的各类增值功能。</li><li>包含高质量的文档和入门指南。Envoy Gateway项目的主要目标，就是为普通用户赋能、引导他们轻松实现各类常见网关用例。</li></ul><br>
<br>说起API的话题，我们发现很多朋友好像不太清楚如何在面向高级用例时，要如何在其他项目中有效对Envoy的xDS API进行重新实现。正是这个问题，导致用户往往需要学习多个复杂API（借此最终转换回xDS）才能达成目的。为此，Envoy Gateway致力于“拨乱反正”，强调Kubernetes Gateway API（以及此API所支持的任何扩展）为唯一受支持的附加API。其他高级用例将由“xDS模式”提供支持，其中的现有API资源将自动由系统替最终用户进行转换。换言之，用户可以直接切换至使用xDS API。这既明确了主API的官方定位，同时也能超越主API的表达能力，允许用户继续通过xDS充分利用Envoy功能。<br>
<h3>未来计划</h3>这里，我们要感谢Envoy Gateway的初始赞助商（Ambassador Labs、Fidelity、Tetrate和VMware），也很高兴能与大家共同踏上新的旅程。Envoy Gateway尚处于发展早期，目前的重点就是先在未来目标和顶层设计方面达成共识。因此欢迎大家把握时机、参与讨论，我们诚邀各位最终用户和系统集成商的加入。<br>
<br>我们还想强调一点：Contour和Emissary的用户不必担心。Envoy Gateway项目将联手VMware以及Ambassador Labs，致力于确保Contour和Emissary用户通过翻译、替换和转为Envoy Gateway核心打包器等方式顺利完成迁移。<br>
<br>我们很高兴能通过Envoy Gateway项目将Envoy家族介绍给更多朋友，也期待能与各位共同携手共进、奔赴前程！<br>
<br><strong>原文链接：<a href="https://www.cncf.io/blog/2022/05/16/introducing-envoy-gateway/">Introducing Envoy Gateway</a></strong>
                                
                                                              
</div>
            