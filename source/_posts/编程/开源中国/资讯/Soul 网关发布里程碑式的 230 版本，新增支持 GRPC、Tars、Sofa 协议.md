
---
title: 'Soul 网关发布里程碑式的 2.3.0 版本，新增支持 GRPC、Tars、Sofa 协议'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://chart.giteye.net/gitee/dromara/soul/2ZKY3P9W.png'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 03:16:00 GMT
thumbnail: 'https://chart.giteye.net/gitee/dromara/soul/2ZKY3P9W.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align: left;">距离上一次发布长达半年之久，在这半年的时间里，我与我的社区小伙伴们，做了太多太多的事情。</p> 
<p style="text-align: left;">完成了将近<code>200</code> 多次PR，发表了将近<code>300</code> 篇文章的源码解析，新增贡献者 <code>120</code> 多位，晋升了 <code>7</code>位committer，并且全部获得正版 <code>jetbrains</code> 全家桶。非常感谢他们，在他们的帮助下，我们完成了非常多非常多的功能。</p> 
<h3 style="text-align:left">soul-admin（dashboard）</h3> 
<p style="text-align:left"><code>admin</code>是整个网关的控制面板，掌管所有的流量，规则的匹配。</p> 
<ul> 
 <li> <p>整合<code>shior</code>框架，完成了用户按钮级别的权限控制。</p> </li> 
 <li> <p>模板化插件，让用户无需感知前端页面，只专注于数据的配置。</p> </li> 
 <li> <p>admin整个后端的国际化，支持中英文切换。</p> </li> 
 <li> <p>新增支持<code>H2</code>来存储数据。</p> </li> 
 <li> <p>admin界面的美观优化（表格，按钮）。</p> </li> 
 <li> <p>新增单元测试，覆盖率达到百分之七十。</p> </li> 
</ul> 
<h3 style="text-align:left">soul网关插件</h3> 
<h4 style="text-align:left">插件新增</h4> 
<ul> 
 <li> <p>新增<code>GRPC</code>插件，全面支持<code>GRPC</code>协议。</p> </li> 
 <li> <p>新增 <code>Tars</code>插件，支持腾讯 <code>tars RPC</code>协议。</p> </li> 
 <li> <p>新增<code>Sofa</code> 插件，支持 <code>sofa RPC</code>协议。</p> </li> 
 <li> <p>新增 <code>Sentinel</code> 插件，整合 <code>sentinel</code> 框架的熔断限流功能。</p> </li> 
 <li> <p>新增 <code>Resilience4j</code> 插件，整合 <code>Resilience4j</code>框架的熔断限流功能。</p> </li> 
 <li> <p>新增 <code>Rediect</code> 插件，支持用户的重定向。</p> </li> 
 <li> <p>新增 <code>Context-path</code>插件，支持用户自定义 <code>context-path</code></p> </li> 
</ul> 
<h4 style="text-align:left">插件优化</h4> 
<ul> 
 <li> <p><code>Divide</code> 插件 ： 节点探活方式的优化，流量预热方式的优化。</p> </li> 
 <li> <p><code>Ratelimiter</code>插件 ：新增并发，漏桶等不同的限流算法，供用户选择。</p> </li> 
 <li> <p><code>Sgin</code> 插件 ： 修复必须设置 url的bug，新增是否验证 标记，可以用来做开放平台的URI认证。</p> </li> 
 <li> <p><code>Dubbo</code>插件 : 新增 form表单，URI参数请求， 新增注册中心直连，参数校验等功能。</p> </li> 
</ul> 
<h3 style="text-align:left">Soul Client</h3> 
<p style="text-align:left">soul-client只是提供一种快速接入网关的客户端，不是必须的。如果用户不使用，可以在soul-admin自行配置规则即可。</p> 
<ul> 
 <li> <p><code>spring-mvc</code>客户端的优化，支持<code>spring</code>， <code>spring-boot</code>所有版本。</p> </li> 
 <li> <p><code>spring-cloud</code>客户端的优化，支持<code>spring</code>， <code>spring-boot</code>所有版本。</p> </li> 
 <li> <p><code>dubbo</code>客户端的优化，支持<code>spring</code>， <code>spring-boot</code>所有版本。</p> </li> 
 <li> <p>新增 <code>soul-grpc-client</code> 支持 <code>grpc-java</code>用户接入。</p> </li> 
 <li> <p>新增 <code>soul-tars-client</code> 支持 <code>tars-java</code>用户接入。</p> </li> 
 <li> <p>新增 <code>soul-sofa-client</code> 支持 <code>sofa-java</code>用户接入。</p> </li> 
</ul> 
<p style="text-align:left">在之前的版本中，只支持 http 方式接入 而这次新增注册中心方式接入。</p> 
<ul> 
 <li> <p>新增 <code>zookeeper</code> 作为注册中心的方式接入<code>soul</code>网关。</p> </li> 
 <li> <p>新增 <code>Nacos</code> 作为注册中心的方式接入<code>soul</code>网关。</p> </li> 
 <li> <p>新增 <code>Consul</code> 作为注册中心的方式接入<code>soul</code>网关。</p> </li> 
 <li> <p>新增 <code>Etcd</code> 作为注册中心的方式接入<code>soul</code>网关。</p> </li> 
</ul> 
<p style="text-align:left">使用方式请参考: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdromara.org%2Fprojects%2Fsoul%2Fregister-center-access%2F" target="_blank">https://dromara.org/projects/soul/register-center-access/</a></p> 
<h3 style="text-align:left">Soul 数据同步</h3> 
<ul> 
 <li> <p>修复<code>Nacos</code> 配置中心同步未设置 <code>NameSpace</code> 的Bug。</p> </li> 
 <li> <p>优化 <code>Websocket</code> 同步方式。</p> </li> 
 <li> <p>解决 <code>soul-admin</code>集群部署时候， <code>Http</code>长轮询方式同步数据Bug。</p> </li> 
</ul> 
<h3 style="text-align:left">鸣谢</h3> 
<p style="text-align:left">这是一次具有里程碑意义的发布，也是 <code>soul</code> 网关，正式正规的一次变革，我们的 <code>dashboard</code>, <code>代码</code>， <code>文档</code>， <code>issue</code>， <code>PR</code> 全部英文国际化，整个项目的单元测试覆盖率达到了百分之<code>70</code>。再次感谢你们的辛苦付出。 虽然我们完成了非常多的功能（在上面我没有完全列举），但是在接下来，我们会有更多的挑战，我相信有你们在，这并不是我们的终点，而是我们腾飞起点。</p> 
<p style="text-align:left"><img alt height="952" src="https://chart.giteye.net/gitee/dromara/soul/2ZKY3P9W.png" width="910" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">加入我们</h3> 
<p style="text-align:left">目前 <code>soul</code> 处于高速发展阶段，如果你追求写高质量的代码，或者想深刻的理解API网关，或者享受开源的乐趣，结识很多优秀的朋友，欢迎大家加入我们的社区。</p> 
<ul> 
 <li> <p>github : <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fsoul" target="_blank">https://github.com/dromara/soul</a></p> </li> 
 <li> <p>gitee : <a href="https://gitee.com/dromara/soul">https://gitee.com/dromara/soul</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            