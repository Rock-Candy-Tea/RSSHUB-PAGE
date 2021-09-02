
---
title: 'Eurynome Cloud v2.5.4.90 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8846'
author: 开源中国
comments: false
date: Thu, 02 Sep 2021 01:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8846'
---

<div>   
<div class="content">
                                                                                            <p>Eurynome Cloud v2.5.4.90 已经发布，企业级技术中台微服务架构。</p> 
<p>此版本更新内容包括：</p> 
<ol> 
 <li>使用Mybatis Plus全面替换已有Mybatis，与Spring Boot Data JPA共存且支持同时使用。使用任何技术都可以无障碍的进行业务代码编写。</li> 
 <li>整合Mybatis Plus和Spring Boot Data JPA更换数据库配置属性，一处修改即可以同时修改Mybatis Plus和Spring Boot Data JPA使用数据库类型。</li> 
 <li>新增接口XSS脚本攻击过滤机制，同时支持请求参数和JSON请求体过滤。采用Ebay XSS过滤模型，进一步提升防控能力。</li> 
 <li>新增SQL 注入攻击防控机制。</li> 
 <li>解决eurynome-cloud-gateway和eurynome-cloud-management服务启动调用Kafka问题。</li> 
 <li>解决CacheConfigException错误问题，在错误体系中增加配置参数不合理提醒，让信息反馈更加友好。</li> 
 <li>解决Spring Boot Admin 不支持Java 8 时间类型问题。</li> 
 <li>解决Spring Boot Admin 不显示 Git Properties 信息问题。</li> 
 <li>解决修改Redis密码配置生效问题</li> 
 <li>梳理dependencies依赖包，对已有依赖进行进行更合理的分类，更加便于依赖包的找寻和维护。</li> 
 <li>升级依赖包版本 
  <ul> 
   <li>spring-boot-admin 升级至 2.5.1</li> 
   <li>git-commit-id-plugin 升级至 4.9.10</li> 
   <li>docker-maven-plugin 升级至 0.37.0</li> 
   <li>hutool 升级至 5.7.10</li> 
   <li>okhttps 升级至 3.1.4</li> 
   <li>JustAuth 升级至1.16.3</li> 
   <li>aliyun-java-sdk-core 升级至 4.5.25</li> 
   <li>baiducloud-java-sdk 升级至 0.10.175</li> 
   <li>aliyun-java-sdk-oss 升级至 3.13.1</li> 
   <li>cn.jpush.api 升级至 3.5.2</li> 
  </ul> </li> 
 <li>规范项目文档，增加系统部署、数据库切换等多部分内容</li> 
 <li>增加Nacos配置导入包，在没有自动部署功能支持的情况下，也可以更加方便的导入配置。</li> 
 <li>替换 UI SweetAlert 过期方法，解决弹出框不会关闭问题</li> 
 <li>解决授权码模式（authorization code）验证码被拦截问题</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.90">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.90</a></p>
                                        </div>
                                      
</div>
            