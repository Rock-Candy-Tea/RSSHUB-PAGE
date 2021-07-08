
---
title: 'YoyoGo v1.7.4 发布 cli & dependence upgrade'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 19:46:00 GMT
thumbnail: 'https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">🦄🌈 YoyoGo （Go语言框架）一个简单、轻量、快速、基于依赖注入的微服务框架( web 、grpc ),支持Nacos/Consoul/Etcd/Eureka/k8s /Apollo等 .</span></p> 
<p style="text-align:left"><img alt="framework desgin" src="https://mnur-prod-public.oss-cn-beijing.aliyuncs.com/0/tech/framework-desgin.jpg" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">v1.7.4 更新内容</p> 
<p><strong>CLI tempates upgrade:</strong><br> 1. grpc<br> 2. xxl-job</p> 
<p><strong>Frameworks upgrade:</strong><br> 1. upgrade gRPC to v1.38.0<br> 2. upgrade etcd to v3.5.0<br> 3. upgrade protobuf to v1.5.2<br> 4. upgrade go-redis to v8.11.0<br> 5. upgrade go-grpc-middleware to v1.3.0<br> 6. upgrade gorm to v1.21.11<br> 7. upgrade logrus to v1.8.1<br> 8. upgrade go2sky to v1.1.0<br> 9. upgrade fasthttp v1.28.0</p> 
<p style="text-align:left">v1.7.3 更新内容</p> 
<p style="text-align:left"><strong>yygctl (cli)</strong></p> 
<p style="text-align:left"><strong>install</strong></p> 
<pre><code class="language-bash">go install github.com/yoyofx/yoyogo/cli/yygctl</code></pre> 
<h1 style="text-align:start">Commands</h1> 
<p style="text-align:start">There are commands working with application root folder</p> 
<h2 style="text-align:start">new</h2> 
<div style="text-align:start"> 
 <pre>yygctl new <span style="color:var(--color-prettylights-syntax-keyword)"><</span>TEMPLATE<span style="color:var(--color-prettylights-syntax-keyword)">></span> [-l<span style="color:var(--color-prettylights-syntax-keyword)">|</span>--list] [-n <span style="color:var(--color-prettylights-syntax-keyword)"><</span>PROJECTNAME<span style="color:var(--color-prettylights-syntax-keyword)">></span>] [-p <span style="color:var(--color-prettylights-syntax-keyword)"><</span>TARGETDIR<span style="color:var(--color-prettylights-syntax-keyword)">></span>]</pre> 
</div> 
<h3 style="text-align:start">--list</h3> 
<p style="text-align:start">list all templates</p> 
<h4 style="text-align:start">TEMPLATE LIST</h4> 
<p style="text-align:start">console / webapi / mvc / grpc / xxl-job</p> 
<h3 style="text-align:start">-n</h3> 
<p style="text-align:start">generate folder by project name</p> 
<h3 style="text-align:start">-p</h3> 
<p style="text-align:start">output files to target directory.</p> 
<h2 style="text-align:start">such as</h2> 
<div style="text-align:start"> 
 <pre>yygctl new console -n demo -p /Projects</pre> 
</div> 
<p style="text-align:left">v1.7.2 更新内容</p> 
<ul> 
 <li>Apollo 配置中心支持</li> 
 <li>修改配置中心快速设置包的位置：github.com/yoyofx/yoyogo/pkg/configuration/&#123; nacos or apollo &#125;</li> 
</ul> 
<p style="text-align:left">实例：</p> 
<pre style="text-align:left"><code class="language-go">config := nacosConfig.RemoteConfig(<span style="color:#032f62">"config"</span>)
config := apolloConfig.RemoteConfig(<span style="color:#032f62">"config"</span>)</code></pre> 
<p style="text-align:left">v1.7.0/1 更新内容</p> 
<ul> 
 <li>集成xxl-job-go sdk ，支持远程日志查询</li> 
 <li>添加consul服务发现与身份认证 </li> 
 <li>Nacos配置中心支持</li> 
</ul> 
<p style="text-align:left">v1.6.9 更新</p> 
<ul> 
 <li>web binding</li> 
</ul> 
<p style="text-align:left">v1.6.8 更新</p> 
<ul> 
 <li> grpc 宿主支持 & grpc client 与 负载均衡 , 实例   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofx%2Fyoyogo%2Ftree%2Fmaster%2Fexamples" target="_blank">https://github.com/yoyofx/yoyogo/tree/master/examples</a></li> 
 <li>控制台宿主支持 , 实例    <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyoyofx%2Fyoyogo%2Ftree%2Fmaster%2Fexamples" target="_blank">https://github.com/yoyofx/yoyogo/tree/master/examples</a></li> 
</ul>
                                        </div>
                                      
</div>
            