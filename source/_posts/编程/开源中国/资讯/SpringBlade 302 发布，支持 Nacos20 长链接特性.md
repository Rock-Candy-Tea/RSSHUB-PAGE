
---
title: 'SpringBlade 3.0.2 发布，支持 Nacos2.0 长链接特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/201905/05103447_GA1q.png'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 09:11:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/201905/05103447_GA1q.png'
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
 <li>升级 SpringBoot 至 2.4.4</li> 
 <li>升级 SpringCloud 至 2020.0.2</li> 
 <li>升级 AlibabaCloud 至 2.2.5.RELEASE</li> 
 <li>升级 FastJson 至 1.2.75</li> 
 <li>升级 Avue 至 2.8.2</li> 
 <li>升级 ElementUI 至 2.15.1</li> 
 <li>新增支持Nacos2.0长链接特性</li> 
 <li>优化七牛云地域配置为自动获取</li> 
 <li>优化Xss过滤支持通配符匹配逻辑</li> 
 <li>优化接口放行支持通配符匹配逻辑</li> 
 <li>修复Feign请求头传递丢失的问题</li> 
 <li>修复用户管理导出查询功能失效的问题</li> 
</ol> 
<h3 style="text-align:left">Nacos2.0注意点</h3> 
<p> 1. 本次升级适配了Nacos2.0，支持长链接特性。2.0版本的兼容性介绍可以见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2F2.0.0-compatibility.html" target="_blank">https://nacos.io/zh-cn/docs/2.0.0-compatibility.html</a></p> 
<p style="text-align:left"> 2. Nacos2.0版本相比1.X新增了gRPC的通信方式，需要增加2个端口。新增端口是在配置的主端口(server.port)基础上，进行一定偏移量自动生成。客户端拥有相同的计算逻辑，用户如同1.X的使用方式，配置主端口(默认8848)，通过相同的偏移量，计算对应gRPC端口(默认9848)。如果客户端和服务端之前存在端口转发，或防火墙时，需要对端口转发配置和防火墙配置做相应的调整。</p> 
<p style="text-align:left"> 3. <span style="background-color:#ffffff; color:#333333">若是docker启动，需要映射新端口并且服务器将其对外开放，启动命令如下：</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333"> docker run --name nacos-standalone -e MODE=standalone -d -p 8848:8848 -p 9848:9848 -p 9849:9849 nacos/nacos-server:2.0.0</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333"> 4. 端口描述如下：</span></p> 
<table cellspacing="0" style="width:934px"> 
 <thead> 
  <tr> 
   <th>端口</th> 
   <th>与主端口的偏移量</th> 
   <th>描述</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">9848</td> 
   <td style="border-color:#dfe2e5">1000</td> 
   <td style="border-color:#dfe2e5">客户端gRPC请求服务端端口，用于客户端向服务端发起连接和请求</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">9849</td> 
   <td style="border-color:#dfe2e5">1001</td> 
   <td style="border-color:#dfe2e5">服务端gRPC请求服务端端口，用于服务间同步等</td> 
  </tr> 
 </tbody> 
</table> 
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
<p style="text-align:left"><strong><img alt height="339" src="https://static.oschina.net/uploads/img/201905/05103447_GA1q.png" width="700" referrerpolicy="no-referrer"><img alt height="336" src="https://static.oschina.net/uploads/img/201905/05103447_OUvJ.png" width="700" referrerpolicy="no-referrer"><img alt height="388" src="https://static.oschina.net/uploads/img/201905/05103447_jQls.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="text-align:left"><img alt height="389" src="https://static.oschina.net/uploads/img/201905/05103447_Kg7V.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt height="422" src="https://static.oschina.net/uploads/img/201905/05103448_AXa8.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong><img alt height="354" src="https://static.oschina.net/uploads/img/201905/05103448_2Btr.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="text-align:left"><strong><img alt height="380" src="https://static.oschina.net/uploads/img/201905/05103448_EyDG.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="text-align:left"><strong><img alt height="381" src="https://static.oschina.net/uploads/img/201905/05103449_HAor.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p style="text-align:left"><img alt height="378" src="https://static.oschina.net/uploads/img/201905/05103451_DnCK.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong><img alt height="347" src="https://static.oschina.net/uploads/img/201905/05103452_NVS3.png" width="700" referrerpolicy="no-referrer"><img alt height="349" src="https://static.oschina.net/uploads/img/201905/05103453_wskj.png" width="700" referrerpolicy="no-referrer"><img alt height="348" src="https://static.oschina.net/uploads/img/201905/05103453_pbHV.png" width="700" referrerpolicy="no-referrer"><img alt height="348" src="https://static.oschina.net/uploads/img/201905/05103454_JmSJ.png" width="700" referrerpolicy="no-referrer"></strong></p>
                                        </div>
                                      
</div>
            