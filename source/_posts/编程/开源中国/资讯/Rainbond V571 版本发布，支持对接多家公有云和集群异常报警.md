
---
title: 'Rainbond V5.7.1 版本发布，支持对接多家公有云和集群异常报警'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.goodrain.com/wechat/5.7.1/v5.7.1.png'
author: 开源中国
comments: false
date: Tue, 05 Jul 2022 11:47:00 GMT
thumbnail: 'https://static.goodrain.com/wechat/5.7.1/v5.7.1.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://static.goodrain.com/wechat/5.7.1/v5.7.1.png" referrerpolicy="no-referrer"></p> 
<h2>新增功能解读</h2> 
<h3>支持快速对接多家公有云</h3> 
<p>在之前的版本中，仅支持对接阿里云 ACK 集群，对于使用其他云厂商的用户不够友好。为了方便用户快速对接不同公有云厂商的集群。我们优化了安装流程。现在支持通过 helm 方式对接阿里云、华为云、腾讯云等多家云厂商提供的集群。</p> 
<p>用户选择不同的云厂商，可以自己提供相关资源的配置，最终生成完整的安装命令，在云厂商管理的集群中执行。当 Rainbond 的数据中心端安装完成后，将会自动对接上该控制台。即可在控制台管理多家云服务商集群。</p> 
<p><img alt src="https://static.goodrain.com/wechat/5.7.1/1.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://static.goodrain.com/wechat/5.7.1/2.png" referrerpolicy="no-referrer"></p> 
<h3>支持集群异常报警</h3> 
<p>结合用户的使用反馈，我们发现用户在使用中，在控制台经常会遇到集群通信异常的问题。虽然并不一定直接影响到上面跑的业务组件。但对于使用者来说，无法直接管理自己的业务也是很严重的问题。</p> 
<p>此时往往需要用户手动去 Kubernetes 集群中排查问题。比如当集群中资源使用过度导致 Pod 被驱逐或节点出现异常都有可能导致这种情况的发生。</p> 
<p>在之前，我们也提供了 Rainbond 监控报警系统，但使用用户较少。因此为了方便用户提前了解可能会出现的问题。我们基于之前的报警规则，将报警信息在页面上进行展示。以便平台管理员及时处理相关问题。</p> 
<p><img alt src="https://static.goodrain.com/wechat/5.7.1/3.png" referrerpolicy="no-referrer"></p> 
<h2>详细变更点</h2> 
<h3>新增功能</h3> 
<ul> 
 <li> <p>【安装】支持通过 helm 快速对接多家公有云（ACK、TKE、CCE）</p> </li> 
 <li> <p>【报警管理】支持将集群异常信息在页面直接展示</p> </li> 
</ul> 
<h3>BUG 修复</h3> 
<ul> 
 <li> <p>【团队管理】集群失去响应时团队列表无法展示的问题</p> </li> 
 <li> <p>【插件管理】插件存储类型错误的问题</p> </li> 
</ul> 
<p>About Rainbond ❝ Rainbond 核心100%开源,使用简单,不需要懂容器和Kubernetes,支持管理多种Kubernetes集群,提供企业级应用的全生命周期管理。 🌟 Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond" target="_blank">https://github.com/goodrain/rainbond</a> 💻 官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com" target="_blank">https://www.rainbond.com</a>❞</p>
                                        </div>
                                      
</div>
            