
---
title: 'Spring Cloud 2021.0.0-M3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8805'
author: 开源中国
comments: false
date: Wed, 27 Oct 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8805'
---

<div>   
<div class="content">
                                                                                            <p>Spring Cloud 2021.0.0-M3 已发布，代号"Jubilee"，可从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo.spring.io%2Fmilestone%2F" target="_blank"> Spring Milestone </a>仓库获取新版本，相关 issue 和 PR 信息查看其<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-cloud%2Fwiki%2FSpring-Cloud-2021-Release-Notes" target="_blank"> GitHub 项目页面</a>。另外，此版本与 Spring Boot 2.6.0-M3 兼容。</p> 
<h3 style="text-align:start">Spring Cloud Gateway</h3> 
<ul> 
 <li>初步支持 gRPC<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fpull%2F2388" target="_blank">#2388</a></li> 
</ul> 
<h3 style="text-align:start">Spring Cloud Function</h3> 
<ul> 
 <li>除了多项功能增强和错误修复之外，Spring Cloud Function 的这个里程碑引入了对 gRPC 的初始支持。<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-function%2Ftree%2Fmain%2Fspring-cloud-function-adapters%2Fspring-cloud-function-grpc" target="_blank">点此查看初始文档</a>。示例、更多文档和单独的博客文章也会即将推出。</li> 
</ul> 
<h3 style="text-align:start">Spring Cloud Vault</h3> 
<ul> 
 <li>来自文件的 TOKEN auth (~/.vault_token) [#609](<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-vault%2Fissues%2F609" onclick="s_objectID='apps_scodevmw : https://github.com/spring-cloud/spring-cloud-vault/issues/609 : 84'" target="_blank">https://github.com/spring-cloud/spring-cloud-vault/issues/609</a></li> 
</ul> 
<h3 style="text-align:start">Spring Cloud Sleuth</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F2039" target="_blank">添加 Exemplars 支持</a></li> 
</ul> 
<h3 style="text-align:start">Spring Cloud Kubernetes</h3> 
<ul> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">为 Config Maps 和 Secrets 添加了<code>EnvironmentRepsitory</code><span>，用于支持使用 </span>Spring Cloud Config Server 从 Kubernetes 资源提供配置数据。<code>EnvrionmentRepository</code><span> </span>现在可以在 DockerHub 上使用包含此新实现的 Spring Cloud Config Server 镜像。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-cloud-kubernetes%2Fdocs%2F2.1.0-M3%2Freference%2Fhtml%2F%23spring-cloud-kubernetes-configserver" target="_blank">点此查看文档</a>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fpull%2F881" target="_blank">#881</a></p> </li> 
 <li> <p style="color:#333333; margin-left:0; margin-right:0">添加了新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-cloud-kubernetes%2Fdocs%2F2.1.0-M3%2Freference%2Fhtml%2F%23spring-cloud-kubernetes-configserver" target="_blank">Kubernetes<span> </span><code>DiscoveryClient</code><span> 实现</span></a>，它使用了新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-cloud-kubernetes%2Fdocs%2F2.1.0-M3%2Freference%2Fhtml%2F%23spring-cloud-kubernetes-discoveryserver" onclick="s_objectID='apps_scodevmw : Kubernetes Discovery Sever : 90'" target="_blank">Kubernetes Discovery Sever</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fpull%2F886" target="_blank">#886</a></p> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#000000">作为 2021.0.0-M3 的一部分，以下模块进行了升级：</span></p> 
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
   <td style="border-left:none; border-top:1px solid #ffffff">Spring Cloud Zookeeper</td> 
   <td style="border-top:1px solid #ffffff">3.1.0-M3</td> 
   <td style="border-top:1px solid #ffffff"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Cli</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Consul</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Bus</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Gateway</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fmilestone%2F57%3Fclosed%3D1" onclick="s_objectID='apps_scodevmw : issues : 92'" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Starter Build</td> 
   <td style="border-top:1px solid #ebf2f2">2021.0.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Vault</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Cloudfoundry</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Commons</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Openfeign</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Task</td> 
   <td style="border-top:1px solid #ebf2f2">2.4.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-task%2Fmilestone%2F50%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Config</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Sleuth</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fmilestone%2F95%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Netflix</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-netflix%2Fmilestone%2F105%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Kubernetes</td> 
   <td style="border-top:1px solid #ebf2f2">2.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fmilestone%2F36%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Circuitbreaker</td> 
   <td style="border-top:1px solid #ebf2f2">2.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2"> </td> 
  </tr> 
  <tr> 
   <td style="border-left:none; border-top:1px solid #ebf2f2">Spring Cloud Contract</td> 
   <td style="border-top:1px solid #ebf2f2">3.1.0-M3</td> 
   <td style="border-top:1px solid #ebf2f2">(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-contract%2Fmilestone%2F80%3Fclosed%3D1" target="_blank">issues</a>)</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F10%2F20%2Fspring-cloud-2021-0-0-m3-codename-jubilee-has-been-released" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            