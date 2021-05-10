
---
title: 'SpringBlade 3.0.3 发布，新增 kuboard-k8s 一键部署方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://kuboard.cn/assets/img/image-20210501171012263.10858241.png'
author: 开源中国
comments: false
date: Mon, 10 May 2021 09:20:00 GMT
thumbnail: 'https://kuboard.cn/assets/img/image-20210501171012263.10858241.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:left"><strong>简介：</strong></h3> 
<ul> 
 <li> <p>SpringBlade 是由一个商业级项目升级优化而来的 SpringCloud 微服务架构，采用 Java8 API 重构了业务代码，完全遵循阿里巴巴编码规范。采用 Spring Boot 2.4 、Spring Cloud 2020 、Mybatis 等核心技术，用于快速搭建企业级的 SaaS 微服务系统平台。</p> </li> 
 <li> <p>SpringBlade 同时提供 SpringBoot 单体架构版本，为中小型项目保驾护航，可与两套分别基于 React 和 Vue 的前端框架无缝对接。</p> </li> 
 <li> <p>SpringBlade 致力于创造新颖的开发模式，将开发中遇到的痛点、生产中所踩的坑整理归纳，并将解决方案都融合到框架中。</p> </li> 
</ul> 
<h3 style="text-align:left"><strong>版本更新信息：</strong></h3> 
<ol> 
 <li>新增blade-develop的dockerfile</li> 
 <li>新增blade-develop推送docker配置</li> 
 <li>新增saber的dockerfile</li> 
 <li>新增kuboard k8s部署脚本</li> 
 <li>新增kuboard k8s部署方案</li> 
 <li>优化pom配置适配新版部署方案</li> 
 <li>优化swagger加载逻辑默认开启knife4j</li> 
</ol> 
<h3><strong>K8s部署文档</strong></h3> 
<ul> 
 <li>k8s部署文档请见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkuboard.cn%2Flearning%2Fk8s-practice%2Fspring-blade" target="_blank">点击查看</a></li> 
</ul> 
<h3>Kubord简介</h3> 
<p style="text-align:left">Kuboard 是一款基于 Kubernetes 的微服务管理界面。目的是帮助用户快速在 Kubernetes 上落地微服务。在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkuboard.cn%2F" onclick="openOutboundLink(this)" target="_blank">https://kuboard.cn</a> 上，您可以获得：</p> 
<ul> 
 <li>最新版本的 Kubernetes 安装文档</li> 
 <li>免费的 Kubernetes 中文教程</li> 
 <li>免费的 Kubernetes 图形化管理界面 Kuboard</li> 
 <li>在 Kubernetes 上部署 Spring Cloud 的实战分享</li> 
</ul> 
<h3 style="text-align:left"><strong>SpringBlade 系列项目地址：</strong></h3> 
<ul> 
 <li> <p>前端 UI 项目地址(基于 React)：<a href="https://gitee.com/smallc/Sword">Sword</a></p> </li> 
 <li> <p>前端 UI 项目地址(基于 Vue)：<a href="https://gitee.com/smallc/Saber">Saber</a></p> </li> 
 <li> <p>核心框架项目地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchillzhuang%2Fblade-tool.git" target="_blank">BladeTool</a></p> </li> 
 <li> <p>后端框架项目地址：<a href="https://gitee.com/smallc/SpringBlade">SpringBlade</a></p> </li> 
 <li> <p>后端 SpringBoot 版本地址：<a href="https://gitee.com/smallc/SpringBlade/tree/2.0-boot/">BladeBoot</a></p> </li> 
 <li> <p>发行版地址：<a href="https://gitee.com/smallc/SpringBlade/releases">https://gitee.com/smallc/SpringBlade/releases</a></p> </li> 
</ul> 
<h3 style="text-align:left"><strong>官网演示地址：</strong></h3> 
<ul> 
 <li> <p>Blade 官网地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbladex.vip%2F" target="_blank">Blade</a></p> </li> 
 <li> <p>Sword 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsword.bladex.vip%2F" target="_blank">Sword 演示</a></p> </li> 
 <li> <p>Saber 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsaber.bladex.vip%2F" target="_blank">Saber 演示</a></p> </li> 
 <li> <p>Archer 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Farcher.bladex.vip%2F" target="_blank">Archer 演示</a></p> </li> 
 <li> <p>Caster 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdata.avuejs.com%2F" target="_blank">Caster 演示</a></p> </li> 
</ul> 
<h3 style="text-align:left"><strong>系统界面一览</strong></h3> 
<p><img alt="image-20210501171012263" src="https://kuboard.cn/assets/img/image-20210501171012263.10858241.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210502165610161" src="https://kuboard.cn/assets/img/image-20210502165610161.1bd5670d.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210502170037521" src="https://kuboard.cn/assets/img/image-20210502170037521.71850262.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210502170212388" src="https://kuboard.cn/assets/img/image-20210502170212388.f771006c.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210502171300961" src="https://kuboard.cn/assets/img/image-20210502171300961.f5fbc9a5.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210503194614214" src="https://kuboard.cn/assets/img/image-20210503194614214.7fd3d838.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210503204714644" src="https://kuboard.cn/assets/img/image-20210503204714644.43a7b798.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210504130036681" src="https://kuboard.cn/assets/img/image-20210504130036681.7dfaa9b7.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210504130950532" src="https://kuboard.cn/assets/img/image-20210504130950532.76b99dfc.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210504152141789" src="https://kuboard.cn/assets/img/image-20210504152141789.d58cfc30.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image-20210504171020607" src="https://kuboard.cn/assets/img/image-20210504171020607.e77c0119.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img src="https://gitee.com/smallc/SpringBlade/raw/master/pic/springblade-k8s1.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            