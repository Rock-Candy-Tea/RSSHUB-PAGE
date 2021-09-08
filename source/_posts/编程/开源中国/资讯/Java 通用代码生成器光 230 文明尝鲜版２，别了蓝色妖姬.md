
---
title: 'Java 通用代码生成器光 2.3.0 文明尝鲜版２，别了蓝色妖姬'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1fa0ceaf45fcf48ecd774d0a3ae4a2f11fd.jpg'
author: 开源中国
comments: false
date: Wed, 08 Sep 2021 08:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1fa0ceaf45fcf48ecd774d0a3ae4a2f11fd.jpg'
---

<div>   
<div class="content">
                                                                                            <p><strong>Java通用代码生成器光2.3.0 文明尝鲜版２，别了蓝色妖姬</strong></p> 
<p>光2.3.0 文明尝鲜版２在原先的版本上有了重要更新。首先是使用Maven管理代码生成器的jar包。方便您从源码构建代码生成器。其实是代码生成器开始支持Tomcat9。目前可以使用Tomcat8.5和Tomcat9运行该代码生成器。因为Tomcat10对Servlet API进行了根本性的更新。故代码生成器暂不支持Tomcat 10。然后，尝鲜版２完善了对SMEU技术栈的支持。您现在可以使用全部三个技术栈了。</p> 
<p>光2.3.0 文明尝鲜版２使用了最新版的EasyUI 1.9.2。EasyUI虽然素面朝天，然而清丽脱俗，细致精细。别了，浓装艳抹的UI蓝色妖姬。</p> 
<p>光2.3.0 文明新增ShiroAuth弹性登录模块，使用Apache Shiro权限框架。本弹性登录模块具有强大的变形能力。您可以指定User,Role,Privilege的具体对象。系统会严格校验，并生成相应的Shiro登录模块。完全无需人工编程。请见GirlOnlyMaria示例，它使用Girl,RightSet和Permission三个对象完成权限登录系统。</p> 
<p>注意，Privilege对象的数据由系统生成，您无需配置。Role会自动增加admin和user两个Role。admin和user都自动关联所有权限。但是admin可以访问User,Role,Privilege三个对象，而user不行。系统会在User表中新增admin和jerry两个用户。其中amdin的角色是admin。jerry的角色是user。用户的密码您可以以明文设置。系统自动把密码转化为密文。若您未设置。amdin的密码为admin。而jerry的密码为jerry。</p> 
<p>新增三种复杂版面。包括父子表，树表和树父子表。把复杂版面串接起来的字段均可以配置。</p> 
<p>新增三种报表。使用Echarts报表框架。包括报表，带数据网格的报表和计划与执行对比报表，带双数据网格。显著增强编译错与编译警告功能，增强更准确的错误信息和域对象簿记检查功能。数据报表支持折线图，柱状图和饼图。数据格式支持原始数据和累加数据。</p> 
<p>项目地址：<a href="https://gitee.com/jerryshensjf/LightSBMEU">https://gitee.com/jerryshensjf/LightSBMEU</a><br> 二进制发布版地址：<a href="https://gitee.com/jerryshensjf/LightSBMEU/attach_files">https://gitee.com/jerryshensjf/LightSBMEU/attach_files</a></p> 
<p style="text-align:left">项目图片</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-1fa0ceaf45fcf48ecd774d0a3ae4a2f11fd.jpg" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">新功能截图</p> 
<p style="text-align:left">登录页面</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9aa1092a9e5fb07582028419cd640f29c6d.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">错误页面</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-d097ba6c334af5547456a2e378198f66eef.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000">登录后界面</span></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000"><img alt src="https://oscimg.oschina.net/oscnet/up-b0d88c6bb96f2370e1310fc82b6ca1e93a0.png" referrerpolicy="no-referrer"></span></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000">登录弹性模块设置页签</span></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000"><img alt src="https://oscimg.oschina.net/oscnet/up-0bfda019217abbae35b7b16e6588b028e0b.png" referrerpolicy="no-referrer"></span></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000">新功能，复杂版面，树表</span></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000"><img alt src="https://oscimg.oschina.net/oscnet/up-414d824ab05ea45f2ee00d0f58a75247e08.png" referrerpolicy="no-referrer"></span></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000">新功能，报表</span></p> 
<p style="text-align:left"><span style="background-color:#efefef; color:#000000"><img alt src="https://oscimg.oschina.net/oscnet/up-f336402df3b09d66d6f3aef81ca680669be.png" referrerpolicy="no-referrer"></span></p>
                                        </div>
                                      
</div>
            