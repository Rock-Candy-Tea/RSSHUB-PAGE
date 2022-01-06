
---
title: 'SofaRPC v5.8.2 发布，蚂蚁金服开源 Java RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7793'
author: 开源中国
comments: false
date: Thu, 06 Jan 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7793'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">SOFARPC 是一个高可扩展性、高性能、生产级的 Java RPC 框架。在蚂蚁金服 SOFARPC 已经经历了十多年及五代版本的发展。</span></p> 
<p><span style="color:#333333">SOFARPC 致力于简化应用之间的 RPC 调用，为应用提供方便透明、稳定高效的点对点远程服务调用方案。为了用户和开发者方便的进行功能扩展。同时提供了丰富的模型抽象和可扩展接口，包括过滤器、路由、负载均衡等等。还围绕 SOFARPC 框架及其周边组件提供丰富的微服务治理方案。</span></p> 
<p>SofaRPC v5.8.2 已发布，此版本带来<span style="color:#24292f">对 sofa-rpc 框架的增强和一些错误修复（需要JDK8 版本支持），完整内容如下：</span></p> 
<h3>新功能</h3> 
<ul> 
 <li><span style="color:#2e3033">修改在三重协议（</span><span style="color:#24292f">triple protocol</span><span style="color:#2e3033">）中设置自定义标头的方式。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1138" target="_blank">#1138</a> </li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li><span style="color:#24292f">弃用未使用的记录器方法。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1144" target="_blank">#1144</a></li> 
</ul> 
<h3><span style="color:#24292f">Bug 修复</span></h3> 
<ul> 
 <li><span style="color:#24292f">修复 baggage 包含 Null 时，</span><code>putAll</code><span style="color:#24292f"> 方法抛出 NPE 的问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1140" target="_blank">#1140</a><span style="color:#24292f"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1146" target="_blank">#1146</a> </li> 
 <li><span style="color:#2e3033">修复顺序比较器溢出的问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1150" target="_blank">#1150</a> </li> 
 <li><span style="color:#2e3033">修复 ProviderConfig setTimeout 的通用错误。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1143" target="_blank">#1143</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Freleases%2Ftag%2Fv5.8.2" target="_blank">https://github.com/sofastack/sofa-rpc/releases/tag/v5.8.2</a></p>
                                        </div>
                                      
</div>
            