
---
title: 'Spring Cloud 2022.0.0-M4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5158'
author: 开源中国
comments: false
date: Thu, 04 Aug 2022 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5158'
---

<div>   
<div class="content">
                                                                                            <p>Spring Cloud 2022.0.0-M4 现已发布，代号 Kilburn。<span style="color:#333333">Spring Cloud 2022.0.0-M4 与 Spring Boot 3.0.0-M4 兼容，</span>一些<span style="background-color:#ffffff; color:#333333">值得关注的变化包括：</span></p> 
<p style="text-align:start"><strong><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Stream</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>完全反应式 Kafka binder 的初始版本</li> 
 <li>通过 BiFunction 改进了对 Kafka tombstone records 录的支持</li> 
 <li>Spring Native 改进</li> 
</ul> 
<p style="text-align:start"><strong><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Config</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>移至 AWS SDK V2 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fpull%2F2111" target="_blank">#2111</a> )</li> 
 <li>从 JSCH 迁移到 Apache MINA ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fissues%2F1901" target="_blank">#1901</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Gateway</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>将 JSON 添加到 gRPC 过滤器 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fpull%2F2657" target="_blank">#2657</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Function</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>支持 BiFunction 表示 Spring Message</li> 
 <li>Spring 可观察性模块</li> 
</ul> 
<p style="text-align:start"><strong><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Task</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>支持应用程序中 ApplicationRunner 和 CommandlineRunner 的观察。</li> 
 <li>Spring Cloud Task 现在利用 Micrometer Observations 来捕获任务指标。</li> 
 <li>用户可以在单步批处理作业中为 jdbc-item reader 和/或 jdbc-item writer 指定不同的数据源。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-task%2Fpull%2F848" target="_blank">#848</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Vault</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>升级到 Spring Vault 3.0.0-M2（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-vault%2Fissues%2F647" target="_blank">#647</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span style="color:#191e1e"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Spring Cloud Commons</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加了急于创建 LoadBalancer child contexts 的可能性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fissues%2F729" target="_blank">#729</a>）</li> 
</ul> 
<p style="text-align:start"><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>以下模块已作为 2022.0.0-M4 的一部分进行了更新：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; border-spacing:0px; color:#191e1e; font-family:"Open Sans",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; orphans:2; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>Module</th> 
   <th>Version</th> 
   <th>Issues</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ffffff">Spring Cloud Stream</td> 
   <td style="border-top:1px solid #ffffff">4.0.0-M4</td> 
   <td style="border-top:1px solid #ffffff"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Config</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fmilestone%2F103%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Build</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Consul</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-consul%2Fmilestone%2F62%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Kubernetes</td> 
   <td style="border-top:1px solid #ebf2f2">3.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fmilestone%2F47%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Gateway</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Starter Build</td> 
   <td style="border-top:1px solid #ebf2f2">2022.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Circuitbreaker</td> 
   <td style="border-top:1px solid #ebf2f2">3.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Contract</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-contract%2Fmilestone%2F92%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Bus</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Function</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Task</td> 
   <td style="border-top:1px solid #ebf2f2">3.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-task%2Fmilestone%2F61%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Zookeeper</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Openfeign</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Vault</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-vault%2Fmilestone%2F51%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Commons</td> 
   <td style="border-top:1px solid #ebf2f2">4.0.0-M4</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fmilestone%2F102%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start"><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F08%2F01%2Fspring-cloud-2022-0-0-m4-codename-kilburn-has-been-released" target="_blank">查看发布公告</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            