
---
title: 'Apache APISIX 2.10.2 发布，云原生的微服务 API 网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1742'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1742'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache APISIX 2.10.2 已发布，这是一个动态、实时、高性能的 API 网关，提供负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性等丰富的流量管理功能。从其主要功能和特点角度来看，Apache APISIX 可以替代 Nginx 来处理南北流量，也可以扮演 Istio 控制平面和 Envoy 数据平面的角色来处理东西向流量。</span></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>Bug 修复 
  <ul> 
   <li>response.set_header 应该删除 header，如 request.set_header</li> 
   <li>更正管道中的客户端 ip</li> 
   <li>upstream：当它被多个路由引用时负载不平衡</li> 
   <li>hmac-auth)：检查 X-HMAC-ALGORITHM header 是否丢失</li> 
   <li>防止被不可信的 request_uri 攻击 </li> 
   <li>admin：使用 PATCH 修改布尔参数</li> 
   <li>traffic-split：每个规则下有多个 weighted_upstreams 的多个规则导致 upstream_key 重复</li> 
   <li>为无效的基本身份验证标头值添加处理程序 </li> 
  </ul> </li> 
 <li>改动 
  <ul> 
   <li>仅记录不敏感的消费者信息</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202111.mbox%2F%253CCAA-X7T6bO%2B7V-hKN%3DF87my0GbMEG-rAe9vyXkG93wgx%3Dm9sCSw%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            