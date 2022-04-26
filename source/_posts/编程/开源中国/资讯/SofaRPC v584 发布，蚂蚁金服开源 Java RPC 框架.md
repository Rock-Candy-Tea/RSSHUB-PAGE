
---
title: 'SofaRPC v5.8.4 发布，蚂蚁金服开源 Java RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6337'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6337'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">SOFARPC 是一个高可扩展性、高性能、生产级的 Java RPC 框架。在蚂蚁金服 SOFARPC 已经经历了十多年及五代版本的发展。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">SOFARPC 致力于简化应用之间的 RPC 调用，为应用提供方便透明、稳定高效的点对点远程服务调用方案。为了用户和开发者方便的进行功能扩展。同时提供了丰富的模型抽象和可扩展接口，包括过滤器、路由、负载均衡等等。还围绕 SOFARPC 框架及其周边组件提供丰富的微服务治理方案。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SofaRPC v5.8.4 现已发布，此版本带来<span style="color:#24292f">对 sofa-rpc 框架的增强和一些错误修复（需要 JDK8 版本支持），官方鼓励升级。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#24292f">具体更新内容如下：</span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>New Features</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>支持 polaris registry <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1147" target="_blank">#1147</a><span style="background-color:#ffffff; color:#24292f"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1179" target="_blank">#1179</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Enhancement</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Consul registry 支持 acl <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fissues%2F1168" target="_blank">#1168</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1169" target="_blank">#1169</a></li> 
 <li>Ut 和 bootstrap api 的优化 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1163" target="_blank">#1163</a></li> 
 <li>将 grpc 从 1.28.0 升级到 1.33.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1147" target="_blank">#1147</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug fix</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Sub unSub 和 unRegister request 增加了 ProtocolType <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1190" target="_blank">#1190</a></li> 
 <li>修复<code>JacksonSerializer</code> 中的通用接口服务反序列化错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1193" target="_blank">#1193</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Freleases%2Ftag%2Fv5.8.4" target="_blank">https://github.com/sofastack/sofa-rpc/releases/tag/v5.8.4</a></p>
                                        </div>
                                      
</div>
            