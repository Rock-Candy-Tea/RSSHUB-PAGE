
---
title: '低代码开发工具，J2PaaS-Studio 正式发布 V1.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c6f0b071a522ff735303d899f5702fa0f91.png'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 10:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c6f0b071a522ff735303d899f5702fa0f91.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#40485b">J2PaaS是综合性低代码开发平台，覆盖了软件项目需求分析、设计、开发、测试、运行、维护与管理等全过程。</span></p> 
<p>J2PaaS-Studio是J2PaaS低代码平台的开发服务引擎（开发工具），<span style="background-color:#ffffff; color:#40485b">首创“参数式”低代码开发模式，通过简单快速的拖拉拽，就能实现页面、列表、报表、逻辑、工作流等系统功能的敏捷开发。开发者</span><span>用studio开发好的应用系统会保存在参数数据库，J2PaaS平台的运行服务引擎从参数数据库加载参数运行。</span></p> 
<p><span>通过J2PaaS平台的运行服务引擎和开发服务引擎，即可完成系统的开发、运行、管理。</span></p> 
<p><strong><span style="color:#16a085">下载地址：</span><a href="https://gitee.com/j2paas/j2paas-studio"><span style="color:#16a085">https://gitee.com/j2paas/j2paas-studio</span></a></strong><br> <strong><span style="color:#16a085">官方社区：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbbs.jikaiyun.com%2F" target="_blank"><span style="color:#16a085">https://bbs.jikaiyun.com</span></a></strong></p> 
<p> </p> 
<p><span><img alt height="872" src="https://oscimg.oschina.net/oscnet/up-c6f0b071a522ff735303d899f5702fa0f91.png" width="1888" referrerpolicy="no-referrer"></span></p> 
<p> </p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">J2PaaS-Studio安装教程</h4> 
<p><strong><span style="color:#c0392b">注：需同时下载</span><u><a href="https://gitee.com/j2paas" target="_blank"><span style="color:#c0392b">j2paas-framework</span></a></u><span style="color:#c0392b">及</span><u><a href="https://gitee.com/j2paas/j2paas-studio"><span style="color:#c0392b">j2paas-studi</span></a></u><a href="https://gitee.com/j2paas/j2paas-studio"><u><span style="color:#c0392b">o</span></u></a><span style="color:#c0392b">才可运行使用</span></strong></p> 
<p>一、安装对应的数据库及中间件，导入数据库数据</p> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">数据库文件下载地址（mysql 版本）：<a href="https://gitee.com/j2paas/j2paas-examples/blob/master/gnys/scheme.zip">https://gitee.com/j2paas/j2paas-examples/blob/master/gnys/scheme.zip</a></p> <p style="margin-left:0; margin-right:0">说明：app_metadata.sql 数据库需要修改到下面的 conf 文件中，两个数据库都必须导入</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">目前支持的数据库包括MySQL、Oracle、SqlServer等主流数据库，支持的国产数据库包含达梦等。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">目前支持的中间件包括Tomcat等、支持的国产中间件包括东方通等。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">目前支持的操作系统包括Windows、Linux等。</p> </li> 
</ol> 
<p>二、Tomcat 安装步骤</p> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">复制 studio 文件夹到 tomcat/webapps 目录下</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">打开 studio/WEB-INF/config/ 目录下的 easyplatform.conf 配置文件</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修改 dbcp 开头的数据库连接配置，其中 app_metadata 即为上述数据库文件所导入的数据库名称</p> <p style="margin-left:0; margin-right:0"><img alt="image-20210930112719941" src="https://gitee.com/j2paas/j2paas-studio/raw/master/.gitee/conf.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">使用 tomcat/bin 目录下的 startup.bat 启动 Tomcat（Linux 下进入 bin 目录输入 ./startup.sh 启动）</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fstudio" target="_blank">http://localhost:8080/studio</a></p> </li> 
</ol>
                                        </div>
                                      
</div>
            