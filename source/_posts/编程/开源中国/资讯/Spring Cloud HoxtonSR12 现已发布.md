
---
title: 'Spring Cloud Hoxton.SR12 现已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cbf534e9751b9a978d6b1a02f23a1c9ccfa.png'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 07:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cbf534e9751b9a978d6b1a02f23a1c9ccfa.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>于美国时间2021年7月7日，Spring Cloud Hoxton.SR12 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F07%2F07%2Fspring-cloud-hoxton-sr12-has-been-released" target="_blank">现已发布</a>。该版本已经在中央仓库中可以下载。SR12版本主要是一个错误修复和文档发布。Hoxton.SR12 与 Spring Boot 2.3.x 和 2.2.x 兼容。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-cbf534e9751b9a978d6b1a02f23a1c9ccfa.png" referrerpolicy="no-referrer"></p> 
<h2>一、主要更新内容</h2> 
<h3 style="text-align:start">Spring Cloud Commons</h3> 
<ul> 
 <li>添加 <code>TaskSchedulerWrapper</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fpull%2F974" target="_blank">#974</a>)</li> 
</ul> 
<h3 style="text-align:start">Spring Cloud Gateway</h3> 
<ul> 
 <li><span style="color:#191e1e">启用禁用</span> <code>GatewayRedisAutoConfiguration</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fissues%2F2052" target="_blank">#2052</a>)</li> 
 <li><span style="color:#191e1e">使路由的 URI 方案不区分大小写</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fissues%2F2207" target="_blank">#2207</a>)</li> 
</ul> 
<h3 style="text-align:start">Spring Cloud OpenFeign</h3> 
<ul> 
 <li><span style="color:#191e1e">改进了对</span><code>SpringFormEncoder</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-openfeign%2Fissues%2F549" target="_blank">#549</a>) 支持</li> 
</ul> 
<h3 style="text-align:start">Spring Cloud Netflix</h3> 
<ul> 
 <li><span style="color:#191e1e">为</span> <code>TraceProxyRequestHelper</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-netflix%2Fissues%2F3873" target="_blank">#3873</a>) <span style="color:#191e1e">添加了特殊字符支持</span></li> 
 <li><span style="color:#191e1e">修复了在</span> <code>eureka.client.healthcheck.enabled= true</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-netflix%2Fissues%2F1571" target="_blank">#1571</a>) <span style="color:#191e1e">时将状态传播到注册表的问题</span></li> 
</ul> 
<h3 style="text-align:start">Spring Cloud <span style="color:#191e1e">断路器</span></h3> 
<ul> 
 <li>Reactive Resilience4J CircuitBreakers <span style="color:#191e1e">现在可以通过配置属性进行配置</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-circuitbreaker%2Fissues%2F107" target="_blank">#107</a>)</li> 
</ul> 
<p style="text-align:start"><span style="color:#333333">以下模块已作为 Hoxton.SR12 的一部分进行了更新：</span></p> 
<table cellspacing="0"> 
 <thead> 
  <tr> 
   <th>模块</th> 
   <th>版本</th> 
   <th>问题</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>Spring Cloud Starter Build</td> 
   <td>Hoxton.SR12</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Netflix</td> 
   <td>2.2.9.RELEASE</td> 
   <td>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-netflix%2Fmilestone%2F103%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Openfeign</td> 
   <td>2.2.9.RELEASE</td> 
   <td>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-openfeign%2Fmilestone%2F37%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Gateway</td> 
   <td>2.2.9.RELEASE</td> 
   <td>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fmilestone%2F52%3Fclosed%3D1" target="_blank">issues</a></td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Commons</td> 
   <td>2.2.9.RELEASE</td> 
   <td>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fmilestone%2F91%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Contract</td> 
   <td>2.2.8.RELEASE</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Kubernetes</td> 
   <td>1.1.10.RELEASE</td> 
   <td>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fmilestone%2F32%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud CircuitBreaker</td> 
   <td>1.0.6.RELEASE</td> 
   <td>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-circuitbreaker%2Fmilestone%2F10%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Stream</td> 
   <td>Horsham.SR13</td> 
   <td> </td> 
  </tr> 
 </tbody> 
</table> 
<h2> 二、注意事项</h2> 
<p>这将是 Hoxton Release Train 的最后一次定期发布。它现在进入安全修复和关键错误的特殊维护期，直到 2022 年 2 月结束（遵循<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-boot%2Fwiki%2FSupported-Versions%23released-versions" target="_blank">Spring Boot 2.3.x</a>的生命周期）。有关更多信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-release%2Fwiki%2FSupported-Versions%23supported-releases" target="_blank">wiki</a>。</p> 
<h2>三、关于MateCloud</h2> 
<p><a href="https://gitee.com/matevip/matecloud">MateCloud</a>一直是致力于微服务的快速开发平台。</p>
                                        </div>
                                      
</div>
            