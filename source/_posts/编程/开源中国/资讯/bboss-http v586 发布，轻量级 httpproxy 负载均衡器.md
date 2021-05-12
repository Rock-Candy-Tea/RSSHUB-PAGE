
---
title: 'bboss-http v5.8.6 发布，轻量级 httpproxy 负载均衡器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5514'
author: 开源中国
comments: false
date: Wed, 12 May 2021 09:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5514'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#333333">bboss-http v5.8.6 发布。</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">bboss-http是一款轻量级 java 客户端http proxy 负载均衡器，简单而功能强大的 http 负载均衡器模块，基于 http 协议实现 客户端到服务端点到点负载均衡和集群容灾，支持服务端节点自动发现。</span></p> 
<p style="text-align:left"><strong>功能改进</strong></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#34495e">1.改进http-proxy负载均衡调度机制：如果所有节点都被标记为不可用时，可以通过控制开关设置返回故障节点用于处理请求，如果请求能够被正常处理则将节点标记为正常节点 默认值true </span></p> 
<p style="text-align:left">非spring boot项目配置</p> 
<pre style="text-align:left"><code><span style="color:#2973b7">     http.failAllContinue</span> <span style="color:#525252">=</span> <span style="color:var(--theme-color,#42b983)">true</span></code></pre> 
<p style="text-align:left">spring boot配置项</p> 
<pre style="text-align:left"><code><span style="color:#2973b7">     spring.bboss.http.failAllContinue</span> <span style="color:#525252">=</span> <span style="color:var(--theme-color,#42b983)">true</span></code></pre> 
<p style="text-align:left">2. <span style="background-color:#ffffff; color:#34495e">http-proxy节点自动发现和故障节点健康检查后台线程模型调整为daemon模式</span></p> 
<p style="text-align:left">3. <span style="background-color:#ffffff; color:#34495e">调整bboss-http源码工程gradle构建脚本语法，保持与gradle 7的兼容性</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#34495e">4.</span> <span style="background-color:#ffffff; color:#34495e">升级httpcliet组件版本到最新的官方版本4.5.13</span></p> 
<p style="text-align:left">5. <span style="background-color:#ffffff; color:#34495e">升级fastxml jackson databind版本2.9.10.8</span></p> 
<p style="text-align:left"><strong>功能特点</strong></p> 
<ol> 
 <li>服务负载均衡（目前提供 RoundRobin 负载算法）</li> 
 <li>服务健康检查</li> 
 <li>服务容灾故障恢复</li> 
 <li>服务自动发现（zk，etcd，consul，eureka，db，其他第三方注册中心）</li> 
 <li><span style="background-color:#f8f8f8; color:#525252">动态监听切换节点路由规则，支持主备和灰度生产自动切换</span></li> 
 <li>分组服务管理，可以配置多组服务集群地址，每一组地址清单支持的配置格式：</li> 
</ol> 
<p style="text-align:left">           http://ip:port,http://ip1:port,http://ip2:port<br>            https://ip:port,https://ip1:port,https://ip2:port<br>            ip:port,ip1:port,ip2:port（默认http协议）<br>        多个地址用逗号分隔</p> 
<p style="text-align:left">10.服务安全认证（配置basic账号和口令）</p> 
<p style="text-align:left">11.主备路由/异地灾备特色</p> 
<p style="text-align:left">12.负载均衡器主备功能，如果主节点全部挂掉，请求转发到可用的备用节点，如果备用节点也挂了，就抛出异常; 如果主节点恢复正常，那么请求重新发往主节点 </p> 
<p style="text-align:left">13.异地灾备，服务采用异地灾备模式部署，服务优先调用本地，当本地服务全部挂掉，服务请求转发到异地服务; 如果本地服务部分恢复或者全部恢复，那么请求重新发往本地服务</p> 
<p style="text-align:left"><strong>开发文档</strong><br> <a href="https://my.oschina.net/bboss/blog/3067430" target="_blank">bboss http负载均衡器使用指南</a></p>
                                        </div>
                                      
</div>
            