
---
title: 'Solon 1.6.34 发布，更现代感的应用开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5496'
author: 开源中国
comments: false
date: Sat, 26 Mar 2022 17:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5496'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目</h3> 
<ul> 
 <li>启动快 5 ～ 10 倍</li> 
 <li>qps 高 2～ 3 倍</li> 
 <li>运行时内存节省 1/3 ~ 1/2</li> 
 <li>打包可以缩小到 1/2 ~ 1/10（比如，90Mb 的变成了 9Mb）</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个更现代感的应用开发框架，轻量、开放生态型的。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放 + 生态的原则</strong></li> 
 <li>力求，<strong>更小、更少、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前有近<strong>130</strong>个生态插件，含盖了日常开发的各种需求。</p> 
<h3 style="text-align:start">本次主要更新</h3> 
<ul> 
 <li>插件 mybatis-solon-plugin 
  <ul> 
   <li>增加 bean 方式添加拦截截器</li> 
   <li>增加 mybatis.xxx.configuration 配置节支持</li> 
  </ul> </li> 
 <li>统一日志配置体验 
  <ul> 
   <li>增加 root 等级配置，做为 logger 的默认等级!!!</li> 
   <li>统一 root,logger,appender 的 level 关系</li> 
   <li>包括 solon.logging.impl, log4j2-solon-plugin, logback-solon-plugin</li> 
  </ul> </li> 
 <li>统一文件上传限制配置体验 
  <ul> 
   <li>插件 solon.boot.jlhttp 增加文件上传大小限制</li> 
   <li>插件 solon.boot.smarthttp 增加文件上传大小限制</li> 
   <li>插件 solon.boot.jetty 增加文件上传大小限制</li> 
   <li>增加 "server.request.maxFileSize" 配置（其默认值为 maxBodySize；可以只用 fileSize）</li> 
  </ul> </li> 
 <li>优化 Multipart 安全机制 
  <ul> 
   <li>增加 Multipart 解析改为延迟按需加载模式（不然内存可能被人刷暴了）!!!</li> 
   <li>增加 Context::autoMultipart() 接口，控制在参数解析时自动解析分片内容</li> 
   <li>增加 Mapping::multipart 属性，用于显示申明分片处理（默认为自动）</li> 
  </ul> </li> 
 <li>新增 nacos2-solon-plugin 插件</li> 
 <li>新增 dubbo3-solon-plugin 插件</li> 
</ul> 
<h3 style="text-align:start">进一步了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul>
                                        </div>
                                      
</div>
            