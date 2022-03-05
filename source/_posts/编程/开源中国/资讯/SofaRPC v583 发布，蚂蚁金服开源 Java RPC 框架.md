
---
title: 'SofaRPC v5.8.3 发布，蚂蚁金服开源 Java RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6917'
author: 开源中国
comments: false
date: Sat, 05 Mar 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6917'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">SOFARPC 是一个高可扩展性、高性能、生产级的 Java RPC 框架。在蚂蚁金服 SOFARPC 已经经历了十多年及五代版本的发展。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">SOFARPC 致力于简化应用之间的 RPC 调用，为应用提供方便透明、稳定高效的点对点远程服务调用方案。为了用户和开发者方便的进行功能扩展。同时提供了丰富的模型抽象和可扩展接口，包括过滤器、路由、负载均衡等等。还围绕 SOFARPC 框架及其周边组件提供丰富的微服务治理方案。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">SofaRPC v5.8.3 现已发布，此版本带来<span style="color:#24292f">对 sofa-rpc 框架的增强和一些错误修复（需要JDK8 版本支持），官方鼓励升级。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#24292f">具体更新内容如下：</span></p> 
<h4>New Features</h4> 
<ul> 
 <li>修改 triple unique id logic <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1006" target="_blank">#1006</a></li> 
</ul> 
<h4>Enhancement</h4> 
<ul> 
 <li>支持 getUserThreadPoolSet 和重新定义自定义线程名称 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1161" target="_blank">#1161</a></li> 
 <li>添加序列化异常日志 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1152" target="_blank">#1152</a></li> 
 <li>删除未使用的 <span style="background-color:#ffffff; color:#24292f">triple proxy</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1166" target="_blank">#1166</a></li> 
 <li>StringBuilder 优化</li> 
 <li>Chore(deps)：在 /bom 中将 protobuf-java 从 3.11.0 升级到 3.16.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1157" target="_blank">#1157</a></li> 
 <li>Chore(deps)：在​​​​​​​ /bom 中将 jackson-databind 从 2.9.10.7 升级到 2.9.10.8 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1136" target="_blank">#1136</a></li> 
</ul> 
<h4>Bug fix</h4> 
<ul> 
 <li>Fix-destroy 方法的错误代码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1164" target="_blank">#1164</a></li> 
 <li>在 triple invoke 完成后移除 RpcInvokeContext <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Fpull%2F1167" target="_blank">#1167</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsofastack%2Fsofa-rpc%2Freleases%2Ftag%2Fv5.8.3" target="_blank">https://github.com/sofastack/sofa-rpc/releases/tag/v5.8.3</a></p>
                                        </div>
                                      
</div>
            