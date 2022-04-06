
---
title: 'kunlun-admin v1.3.0 发布，昆仑管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-80ade19e0fc813d73816b77c0f706a4dc07.png'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 02:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-80ade19e0fc813d73816b77c0f706a4dc07.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">昆仑管理系统 v1.3.0 发布了！</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新日志</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1、升级SpringBoot至2.5.11，SpringCloud至2020.0.5；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2、<span style="background-color:#ffffff; color:#333333">增加父级依赖工程kunlun-parent-api，</span><span> 以pom形式依赖到各个项目，包含所有依赖的jar</span>；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3、更新网管gateway的设置和GlobalFilter的适配；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4、登录验证更新、上下文缓存更新、操作日志更新、自动配置更新；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">5、升级前端umi及其他依赖版本，并适配代码；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">6、<span style="background-color:#ffffff; color:#333333">优化并修复前端及后台若干问题</span><span style="background-color:#ffffff; color:#333333"> 。</span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>系统介绍</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">昆仑管理系统是一套基于前后端分离架构的后台管理系统。kunlun-web 基于React + Umi(乌米) + Ant Design (蚂蚁金服) 构建开发，提供前端解决方案；kunlun-service 基于 SpringBoot 与 Spring Cloud 构建开发，提供后端基于微服务架构的解决方案。系统通过Apache Shiro与Jwt组件，用token进行数据交互认证，可快速开发并独立进行Docker容器化部署。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">使用说明</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1.  npm安装前端依赖库，并启动kunlun-home-web与kunlun-system-web服务；<br> 2.  安装并启动PostgreSQL；<br> 3.  安装并启动RabbitMQ和Redis；<br> 4.  启动注册中心服务kunlun-register-service；<br> 5.  依次启动kunlun-gateway-service、kunlun-basedata-service与kunlun-system-service服务；<br> 6.  访问URL：http://localhost:8000；<br> 7.  输入账号：admin，密码：admin及验证码。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>工具插件</strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="up-80ade19e0fc813d73816b77c0f706a4dc07.png" height="300" src="https://oscimg.oschina.net/oscnet/up-80ade19e0fc813d73816b77c0f706a4dc07.png" width="359" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">页面截图</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-cce01fbb8b8359e7b6c54f93ec5b4cbf8d1.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="937" src="https://oscimg.oschina.net/oscnet/up-814bbf60c4d4235dc562f0c9df214fe79c4.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="934" src="https://oscimg.oschina.net/oscnet/up-d2167a0ae231dd61d9c0f5316a18c98259e.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="935" src="https://oscimg.oschina.net/oscnet/up-69247d2af95f8644ac18c65f7cc6fac4874.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="935" src="https://oscimg.oschina.net/oscnet/up-a1e572e6341a27114707bbfe0f5053f350c.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="937" src="https://oscimg.oschina.net/oscnet/up-2389c610721734c66277a54a2a62a1fecd4.png" width="1920" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            