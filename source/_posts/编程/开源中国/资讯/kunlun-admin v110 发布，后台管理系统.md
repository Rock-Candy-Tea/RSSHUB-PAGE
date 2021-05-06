
---
title: 'kunlun-admin v1.1.0 发布，后台管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-80ade19e0fc813d73816b77c0f706a4dc07.png'
author: 开源中国
comments: false
date: Thu, 06 May 2021 15:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-80ade19e0fc813d73816b77c0f706a4dc07.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">昆仑管理系统 v1.1.0 发布了。</p> 
<h4 style="text-align:left">更新日志</h4> 
<p style="text-align:left">1、在用户管理菜单下增加部门管理、岗位管理和关联授权页面；</p> 
<p style="text-align:left">2、修改前端框架，使首页始终显示；</p> 
<p style="text-align:left">3、增加基础模型Model及树状模型Model；</p> 
<p style="text-align:left">4、增加递归封装树状数据工具类；</p> 
<p style="text-align:left">5、优化并修复前端及后台若干问题；</p> 
<h4 style="text-align:left"><strong>系统介绍</strong></h4> 
<p style="text-align:left">昆仑管理系统是一套基于前后端分离架构的后台管理系统。kunlun-web 基于React + Umi(乌米) + Ant Design (蚂蚁金服) 构建开发，提供前端解决方案；kunlun-service 基于 SpringBoot 与 Spring Cloud 构建开发，提供后端基于微服务架构的解决方案。系统通过Apache Shiro与Jwt组件，用token进行数据交互认证，可快速开发并独立进行Docker容器化部署。</p> 
<h4 style="text-align:left">使用说明</h4> 
<p style="text-align:left">1.  npm安装前端依赖库，并启动kunlun-home-web与kunlun-system-web服务；<br> 2.  启动PostgreSQL，执行kunlun-basedata-service与kunlun-system-service服务resources下的sql文件；<br> 3.  启动RabbitMQ和Redis；<br> 4.  启动注册中心kunlun-register-service；<br> 5.  依次启动kunlun-gateway-service、kunlun-basedata-service与kunlun-system-service服务；<br> 6.  访问URL：http://localhost:8000；<br> 7.  输入账号：admin，密码：admin及验证码。</p> 
<h4 style="text-align:left"><strong>工具插件</strong></h4> 
<p style="text-align:left"><img alt="up-80ade19e0fc813d73816b77c0f706a4dc07.png" height="300" src="https://oscimg.oschina.net/oscnet/up-80ade19e0fc813d73816b77c0f706a4dc07.png" width="359" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">页面截图</h4> 
<p style="text-align:left"><img height="936" src="https://oscimg.oschina.net/oscnet/up-cce01fbb8b8359e7b6c54f93ec5b4cbf8d1.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img height="937" src="https://oscimg.oschina.net/oscnet/up-814bbf60c4d4235dc562f0c9df214fe79c4.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img height="934" src="https://oscimg.oschina.net/oscnet/up-d2167a0ae231dd61d9c0f5316a18c98259e.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img height="935" src="https://oscimg.oschina.net/oscnet/up-69247d2af95f8644ac18c65f7cc6fac4874.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img height="935" src="https://oscimg.oschina.net/oscnet/up-a1e572e6341a27114707bbfe0f5053f350c.png" width="1920" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img height="937" src="https://oscimg.oschina.net/oscnet/up-2389c610721734c66277a54a2a62a1fecd4.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            