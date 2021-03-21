
---
title: Spring Cloud 2020.0.2 (aka Ilford) 发布
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Fri, 19 Mar 2021 08:01:00 GMT
thumbnail: 
---

<div>   
<div class="content">
                                                                                            <p>Spring Cloud 2020.0.2 (aka Ilford) 已发布，这是一个小版本升级，更新内容主要是修复 bug 以及升级依赖，可从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Forg%2Fspringframework%2Fcloud%2Fspring-cloud-dependencies%2F2020.0.2%2F" target="_blank"> Maven Central </a>获取更新。</p> 
<p>以下模块作为 Spring Cloud 2020.0.2 的一部分已升级：</p> 
<table> 
 <thead> 
  <tr> 
   <th>Module</th> 
   <th>Version</th> 
   <th>Issues</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>Spring Cloud Bus</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Circuitbreaker</td> 
   <td>2.0.1</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Cli</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Cloudfoundry</td> 
   <td>3.0.1</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Commons</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Config</td> 
   <td>3.0.3</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Consul</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Contract</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Gateway</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Kubernetes</td> 
   <td>2.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Netflix</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Openfeign</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Sleuth</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Task</td> 
   <td>2.3.1</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Vault</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>Spring Cloud Zookeeper</td> 
   <td>3.0.2</td> 
   <td> </td> 
  </tr> 
 </tbody> 
</table> 
<h3>Spring Cloud Commons</h3> 
<ul> 
 <li>添加针对 SC LoadBalancer 的基于提示的实例选择 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fissues%2F672" target="_blank">#672</a>)</li> 
 <li>在阻塞 LoadBalancer 客户端中添加对基于请求的 sticky-session 支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-commons%2Fissues%2F901" target="_blank">#901</a>)</li> 
</ul> 
<h3>Spring Cloud Config</h3> 
<ul> 
 <li>当使用<code>ConfigData</code> 时添加对 TLS 的支持(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-config%2Fissues%2F1689" target="_blank">#1689</a>)</li> 
</ul> 
<h3>Spring Cloud Consul</h3> 
<ul> 
 <li>为<code>spring.config.import=consul:</code>添加 Retry 支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-consul%2Fissues%2F703" target="_blank">#703</a>)</li> 
 <li>如果服务从本地代理进行注销，会尝试注册 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-consul%2Fissues%2F703" target="_blank">#703</a>)</li> 
 <li>添加对多个默认 query tag 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-consul%2Fpull%2F684" target="_blank">#684</a>)</li> 
</ul> 
<h3>Spring Cloud Gateway</h3> 
<ul> 
 <li>支持添加服务实例 ID cookie (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fissues%2F2070" target="_blank">#2070</a>)</li> 
 <li><code>HttpClient</code> 代理类型可定制 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-gateway%2Fissues%2F2140" target="_blank">#2140</a>)</li> 
</ul> 
<h3>Spring Cloud Kubernetes</h3> 
<ul> 
 <li>添加配置用于服务的主端口的功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fissues%2F733" target="_blank">#733</a>)</li> 
 <li>升级 Kubernetes Java Client 至 11.0.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-kubernetes%2Fpull%2F708" target="_blank">#708</a>)</li> 
</ul> 
<h3>Spring Cloud CircuitBreaker</h3> 
<ul> 
 <li>添加使用 Resilience4J Bulkhead 模块的功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-circuitbreaker%2Fissues%2F86" target="_blank">#86</a>)</li> 
 <li>添加通过配置属性配置 Resilience4J 的功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-circuitbreaker%2Fissues%2F61" target="_blank">#61</a>)</li> 
</ul> 
<h3>Spring Cloud OpenFeign</h3> 
<ul> 
 <li>添加对 Micrometer 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-openfeign%2Fissues%2F457" target="_blank">#457</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-openfeign%2Fpull%2F462" target="_blank">#462</a>)</li> 
</ul> 
<h3>Spring Cloud Sleuth</h3> 
<ul> 
 <li><code>SleuthFeignBuilder</code> 现在可以提供自定义功能<code>delegate</code> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-cloud%2Fspring-cloud-sleuth%2Fissues%2F1865" target="_blank">#1865</a>)</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F03%2F18%2Fspring-cloud-2020-0-2-aka-ilford-is-available" target="_blank">发布公告</a></p>
                                        </div>
                                      
</div>
            