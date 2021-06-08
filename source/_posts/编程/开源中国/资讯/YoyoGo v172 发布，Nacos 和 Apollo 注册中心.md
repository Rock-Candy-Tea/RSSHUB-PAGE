
---
title: 'YoyoGo v1.7.2 发布，Nacos 和 Apollo 注册中心'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 05:22:00 GMT
thumbnail: 'https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#40485b">🦄🌈 YoyoGo （Go语言框架）一个简单、轻量、快速、基于依赖注入的微服务框架( web 、grpc ),支持Nacos/Consoul/Etcd/Eureka/k8s /Apollo等 .</span></p> 
<p><img alt="framework desgin" src="https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg" referrerpolicy="no-referrer"></p> 
<p>v1.7.2 更新内容</p> 
<ul> 
 <li>Apollo 配置中心支持</li> 
 <li>修改配置中心快速设置包的位置：github.com/yoyofx/yoyogo/pkg/configuration/&#123; nacos or apollo &#125;</li> 
</ul> 
<p>实例：</p> 
<pre><code class="language-go">config := nacosConfig.RemoteConfig("config")
config := apolloConfig.RemoteConfig("config")</code></pre> 
<p>v1.7.0/1 更新内容</p> 
<ul> 
 <li>集成xxl-job-go sdk ，支持远程日志查询</li> 
 <li>添加consul服务发现与身份认证 </li> 
 <li>Nacos配置中心支持</li> 
</ul> 
<p>v1.6.9 更新</p> 
<ul> 
 <li>web binding</li> 
</ul> 
<p>v1.6.8 更新</p> 
<ul> 
 <li> grpc 宿主支持 & grpc client 与 负载均衡 , 实例   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofx%2Fyoyogo%2Ftree%2Fmaster%2Fexamples" target="_blank">https://github.com/yoyofx/yoyogo/tree/master/examples</a></li> 
 <li>控制台宿主支持 , 实例    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofx%2Fyoyogo%2Ftree%2Fmaster%2Fexamples" target="_blank">https://github.com/yoyofx/yoyogo/tree/master/examples</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            