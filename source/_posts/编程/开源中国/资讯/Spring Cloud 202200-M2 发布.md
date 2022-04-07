
---
title: 'Spring Cloud 2022.0.0-M2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=265'
author: 开源中国
comments: false
date: Thu, 07 Apr 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=265'
---

<div>   
<div class="content">
                                                                                            <p>Spring Cloud 2022.0.0-M2 已发布，代号"Kilburn"。</p> 
<p>值得关注的变化</p> 
<p><strong>Spring Cloud Stream</strong></p> 
<ul> 
 <li>Spring Cloud Stream 的 Kafka 和 RabbitMQ 绑定器都已迁移为核心 Spring Cloud Stream 仓库的一部分。通过此项变更，Spring Cloud Stream 现在采用单一存储库 (mono-repo)，其中 Spring Cloud Stream 的所有与框架相关的代码库现在都是单个存储库的一部分。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-stream%2Ftree%2Fmain%2Fbinders%2Fkafka-binder" target="_blank">在此处</a>查看 Kafka binder 的更多详细信息，在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-stream%2Ftree%2Fmain%2Fbinders%2Frabbit-binder" target="_blank">此处</a>查看 RabbitMQ binder 的更多详细信息。</li> 
 <li>引入了对基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fprojectreactor.io%2Fdocs%2Fkafka%2Frelease%2Freference%2F" target="_blank">Reactor Kafka </a>的新反应式 Kafka 绑定器的初始支持。此支持包含在幕后使用 Reactor Kafka 的消费者和生产者绑定。有关详细信息，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-stream%2Fissues%2F2293" target="_blank">查看此 issue。</a></li> 
 <li>此外，鉴于所依赖新的测试绑定器已 3 年多，现在还删除了旧的测试模块</li> 
</ul> 
<p style="text-align:start"><strong>Spring Cloud Config</strong></p> 
<ul> 
 <li>当收到错误响应代码时尝试多个 URL (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fissues%2F1845" target="_blank">#1845</a>)</li> 
 <li>允许指定停机健康状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fpull%2F2056" target="_blank">#2056</a>)</li> 
</ul> 
<p style="text-align:start"><strong>Spring Cloud Kubernetes</strong></p> 
<ul> 
 <li>重构 configmaps 和 secrets 实现 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fpull%2F917" target="_blank">#917</a>)</li> 
</ul> 
<p style="text-align:start"><strong>Spring Cloud Contract</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-contract%2Fissues%2F1661" target="_blank">Bumped Pact to 4.2</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-contract%2Fissues%2F1762" target="_blank">Bumped Groovy to 4</a></li> 
</ul> 
<p style="text-align:start"><strong>Spring Cloud Gateway</strong></p> 
<ul> 
 <li>为 “X-Forwarded-For” header 添加路由谓词 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fissues%2F783" target="_blank">#2384</a>)</li> 
</ul> 
<p style="text-align:start"><strong>Spring Cloud Function</strong></p> 
<ul> 
 <li>支持添加多个路由器</li> 
 <li>支持不区分大小写的 header key 评估</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F03%2F29%2Fcve-report-published-for-spring-cloud-function" target="_blank">cve-2022-22963</a></li> 
</ul> 
<p style="text-align:start"><strong>Spring Cloud Commons</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fissues%2F1043" target="_blank">增加了重试 LoadBalancer 特定异常的可能性</a></li> 
</ul> 
<p style="color:#333333; text-align:start">以下模块作为 2022.0.0-M2 的一部分也进行了升级：</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; border-spacing:0px; color:#191e1e; font-family:"Open Sans",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; orphans:2; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Module</th> 
   <th>Version</th> 
   <th>Issues</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ffffff">Spring Cloud Stream</td> 
   <td style="border-top:1px solid #ffffff">4.0.0-M2</td> 
   <td style="border-top:1px solid #ffffff"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Config</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fmilestone%2F100%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Build</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Kubernetes</td> 
   <td style="border-top:1px solid #ebf2f2">3.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fmilestone%2F42%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Circuitbreaker</td> 
   <td style="border-top:1px solid #ebf2f2">3.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-circuitbreaker%2Fmilestone%2F13%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Contract</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-contract%2Fmilestone%2F85%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Consul</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Gateway</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fmilestone%2F64%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Starter Build</td> 
   <td style="border-top:1px solid #ebf2f2">2022.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Function</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Vault</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Bus</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Zookeeper</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Task</td> 
   <td style="border-top:1px solid #ebf2f2">3.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-task%2Fmilestone%2F56%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Commons</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fmilestone%2F99%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Openfeign</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M2</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-openfeign%2Fmilestone%2F51%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F04%2F05%2Fspring-cloud-2022-0-0-m2-codename-kilburn-has-been-released" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            