
---
title: 'Rainbond 5.4.1 发布，支持 1.20-1.22Kubernetes 集群、优化团队视图'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/5.4.0-teamdashboard.jpg'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 13:43:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/5.4.0-teamdashboard.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond" target="_blank">Rainbond<span> </span></a>是云原生且易用的应用管理平台。云原生应用交付的最佳实践。专注于以应用为中心的理念，赋能企业搭建云原生开发云、云原生交付云。</p> 
 <p style="margin-left:0; margin-right:0"><strong>对于企业：</strong><span> </span>Rainbond 是开箱即用的云原生平台，借助 Rainbond 可以快速完成企业研发和交付体系的云原生转型。</p> 
 <p style="margin-left:0; margin-right:0"><strong>对于开发者：</strong><span> </span>基于 Rainbond 开发、测试和运维企业业务应用，开箱即用的获得全方位的云原生技术能力。包括但不仅限于持续集成、服务治理、架构支撑、多维度应用观测、流量管理。</p> 
 <p style="margin-left:0; margin-right:0"><strong>对于项目交付：</strong><span> </span>基于 Rainbond 搭建产品版本化管理体系，搭建标准化客户交付环境，使传统的交付流程可以自动化、简单化和可管理。</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Rainbond 5.4.1 版本发布，本次版本更新主要提升了Rainbond的兼容性，支持 1.16-1.22 的 Kubernetes 集群对接并使用 Rainbond 。并对安装流程以及团队视图做了优化。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">有许多用户已经在使用较新的 Kubernetes 版本，但由于之前 Rainbond 并未兼容高版本的 Kubernetes 集群，导致这些用户无法感受到 Rainbond 带来的价值。因此为了能使更多的用户更高效的完成企业研发和交付体系的云原生转型，我们支持了 1.20-1.22 的 Kubernetes 集群对接和使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在过去的一些使用场景中，我们发现，用户在进入团队视图时，无法快速获取他所关注的信息，比如每个应用的状态，占用资源等情况，这会带来一些额外的操作，用户体验较差。因此现在我们优化了团队视图下应用的展示，用户可以在团队视图快速了解到当前应用的状态以及内存占用等情况，并可直接在此快速访问，而不必点进应用视图。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">主要功能点解读：</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:left">1. 支持1.20-1.22 的 Kubernetes 集群对接</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次版本新支持了 1.20-1.22 的 Kubernetes 集群对接和使用。已有1.19 以上 Kubernetes 集群的用户，可以通过接入 Kubernetes 集群直接对接到控制台，并完成初始化 Rainbond 的操作。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">初始化 Rainbond: 对于 Kubernetes 而言 Rainbond 整个架构是一套应用，我们定义了Rainbond-operator来将 Rainbond 安装到 Kubernetes 集群中，使用 Kubernetes 来管理 Rainbond 组件，同时 Rainbond 又可以反过来管理调度 Kubernetes 资源。</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在之前的5.3.3版本中，由于我们升级了 ingress 版本，导致集群版本为 1.16-1.18 的用户无法正常体验到 5.3.3 版本的相关功能，因此本次升级还修复了不兼容问题，用户可以参考升级文档先升级到 5.3.3 版本，再升级到 5.4.1，即可体验到 5.3.3 及 5.4.1 相关功能。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">2. 优化团队视图的展示数据</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在旧版本中，团队视图只能获取应用列表。无法直接访问对应的应用。对于不关心应用内部拓扑和组件详情的用户来说，还需要点击进入应用，才能访问。同时，在资源不足的情况下，想要快速关闭某些占用资源较大的应用，也需要单独进入应用查看。在这种情况下，我们对团队视图做了调整，新版本的团队视图如下所示。可以看到，每个应用使用的内存以及相关的信息一目了然。同时还可以通过访问按钮快速访问应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="5.4.0-teamdashboard.jpg" src="https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/5.4.0-teamdashboard.jpg" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">3. 支持从压缩包构建java代码</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在之前使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fcomponent-create%2Flanguage-support%2Fjava%2Fjava-jar%2F" target="_blank">jar包构建</a><span> </span>或<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fcomponent-create%2Flanguage-support%2Fjava%2Fjava-war%2F" target="_blank">war包构建<span> </span></a>时，用户需要将本地的 jar 包或 war 包托管在 git/svn 等服务上，这样一次源码构建的过程。通常是这样，用户拿源码编译成对应的jar包或war包，再将其拷贝到对应的服务，推送再构建。因此现在支持了下载对应的压缩包进行构建，你可以将其与现有的 CI流程集成，如 Jenkins 等，你可以创建流水线，在提交代码通过 Jenkins 构建完成后，通过流水线打包（支持 tar , tar.gz , zip 格式）上传到 WebServer上，然后即可直接通过下载地址从 WebServer 拉包构建。示例操作如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="oss-jar.gif" src="https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.4/oss-jar.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">详细变更点：</h3> 
<h3 style="margin-left:0; margin-right:0; text-align:left">新增功能</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">【兼容性】<strong>支持1.20-1.22 的Kubernetes对接并使用；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【团队管理】<strong>优化团队视图展示信息；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【应用管理】<strong>支持应用设置logo；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【组件管理】<strong>支持从对象存储获取压缩包进行源码构建；</strong></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">优化功能</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>【性能】<strong>优化团队页面展示速度；</strong></li> 
 <li>【安装】<strong>优化离线安装的新手引导策略；</strong></li> 
 <li>【安装】<strong>优化集群检测脚本；</strong></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">BUG 修复</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">【兼容性】<strong>修复不兼容k8s 1.16-1.18 版本的问题；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【安全性】<strong>升级网关的nginx版本，防止CVE-2019-9511，CVE-2019-9513，CVE-2021-23017安全漏洞；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【组件库管理】<strong>修复helm应用安装提示应用商店不存在的问题；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【应用管理】<strong>修复应用无法正常回滚的问题；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【应用管理】<strong>修复安装部分应用服务端异常的问题；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【团队管理】<strong>修复团队列表分页问题；</strong></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">【组件管理】<strong>修复组件多个网关策略无法同时生效的问题；</strong></p> </li> 
</ul>
                                        </div>
                                      
</div>
            