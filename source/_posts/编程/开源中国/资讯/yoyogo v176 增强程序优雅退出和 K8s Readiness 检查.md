
---
title: 'yoyogo v1.7.6 增强程序优雅退出和 K8s Readiness 检查'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg'
author: 开源中国
comments: false
date: Wed, 21 Jul 2021 10:39:00 GMT
thumbnail: 'https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">🦄🌈 YoyoGo （Go语言框架）一个简单、轻量、快速、基于依赖注入的微服务框架( web 、grpc ),支持Nacos/Consoul/Etcd/Eureka/k8s /Apollo等 .</p> 
<p style="text-align:start"><img alt="framework desgin" height="645" src="https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg" width="802" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong>本次更新增强了Kubernetes Readiness 健康检查的能力，基本流程如下</strong>：</p> 
<ul> 
 <li><code>old pod</code> 未退出之前，先启动 <code>new pod</code></li> 
 <li><code>old pod</code> 继续处理完已经接受的请求，并且不再接受新请求</li> 
 <li><code>new pod</code>接受并处理新请求的方式</li> 
 <li><code>old pod</code> 退出</li> 
</ul> 
<p style="text-align:start">这样整个服务重启就算是成功了，如果 <code>new pod</code> 没有启动成功，<code>old pod</code> 也可以提供服务，不会对目前线上的服务造成影响。</p> 
<p style="text-align:start"><strong><img alt height="262" src="https://img2020.cnblogs.com/blog/176287/202107/176287-20210721104501322-892039988.png" width="743" referrerpolicy="no-referrer"></strong></p> 
<p style="text-align:start"><strong>运行在容器中的程序响应流程：</strong></p> 
<p style="text-align:start">程序在 <code>docker</code> 容器中运行，所以在服务发布过程中，<code>k8s</code> 会向容器发送一个 <code>SIGTERM</code> 信号，然后容器中程序接收到信号，开始执行 <code>ShutDown</code></p> 
<p style="text-align:start"><img alt height="404" src="https://img2020.cnblogs.com/blog/176287/202107/176287-20210721110442001-613190080.png" width="798" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong>v1.7.6 更新内容</strong></p> 
<p style="text-align:start"><strong> 修复内容:</strong></p> 
<ul> 
 <li>fixed graceful stop and readiness bugs.</li> 
 <li>fixed parallel problem by mvc template, that match it for route path .</li> 
 <li>fixed read remote config hight priority then flags .</li> 
</ul> 
<p style="text-align:start"><strong>新增特性:</strong></p> 
<ul> 
 <li>add endpoint /actuator/health/detail, and then output db,redis and more .</li> 
 <li>add endpoint /actuator/routers, and then output all route info list<br>  </li> 
</ul> 
<p style="text-align:start"><strong>v1.7.5 更新内容</strong></p> 
<p style="text-align:start">框架依赖升级，独立DI组件</p> 
<ul> 
 <li>New dependency injection framework<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofxteam%2Fdependencyinjection" target="_blank">https://github.com/yoyofxteam/dependencyinjection</a></li> 
</ul> 
<h2 style="text-align:start"><strong>新增特性:</strong></h2> 
<ul> 
 <li>Support grpc connection timeout with context. (fix)</li> 
</ul> 
<p style="text-align:start"><strong>v1.7.4 更新内容</strong></p> 
<p style="text-align:start"><strong>应用模板升级</strong>：</p> 
<ul> 
 <li><strong>grpc</strong> </li> 
 <li><strong>xxl-job</strong></li> 
</ul> 
<p style="text-align:start"><strong>框架依赖升级:</strong><br> 1. upgrade gRPC to v1.38.0<br> 2. upgrade etcd to v3.5.0<br> 3. upgrade protobuf to v1.5.2<br> 4. upgrade go-redis to v8.11.0<br> 5. upgrade go-grpc-middleware to v1.3.0<br> 6. upgrade gorm to v1.21.11<br> 7. upgrade logrus to v1.8.1<br> 8. upgrade go2sky to v1.1.0<br> 9. upgrade fasthttp v1.28.0</p>
                                        </div>
                                      
</div>
            