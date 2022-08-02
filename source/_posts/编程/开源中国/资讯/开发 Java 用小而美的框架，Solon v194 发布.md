
---
title: '开发 Java 用小而美的框架，Solon v1.9.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4636'
author: 开源中国
comments: false
date: Tue, 02 Aug 2022 09:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4636'
---

<div>   
<div class="content">
                                                                                            <h4 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目：</h4> 
<ul> 
 <li>启动快 5 ～ 10 倍。<span> </span><strong>（更快）</strong></li> 
 <li>qps 高 2～ 3 倍。<span> </span><strong>（更高）</strong></li> 
 <li>运行时内存节省 1/3 ~ 1/2。<span> </span><strong>（更少）</strong></li> 
 <li>打包可以缩小到 1/2 ~ 1/10；比如，90Mb 的变成了 9Mb。<span> </span><strong>（更小）</strong></li> 
 <li>基于服务 name 进行注册发现 与 k8s svc 相互对应</li> 
 <li>支持 Service Mesh 架构部署方案</li> 
</ul> 
<h4 style="text-align:start">本次更新：</h4> 
<ul> 
 <li>解决 @Service 类重写基类函数时会出错的问题</li> 
 <li>解决 Websocket 可能会发一次空数据的情况(1.9.2 出现的)</li> 
 <li>解决 NamedThreadFactory 前缀处理错误</li> 
 <li>解决 Nami @Mapping("GET hello?age=12") String sayHello(String name)，会出现两个?的问题</li> 
</ul> 
<h4 style="text-align:start">进一步了解 Solon：</h4> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul>
                                        </div>
                                      
</div>
            