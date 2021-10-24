
---
title: 'JPress v4.1.5 发布，终于可以选择附件的视频和图片了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 11:06:00 GMT
thumbnail: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img src="https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。然而，JPress不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">JPress v4.1.5 发布，主要是带了了一个选择附件里的图片、视频和附件的功能。这个功能在v3.x 的版本就已经存在了，但是不好用，在 v4 的时候去掉了，但是很多用户建议又增加进来，这次做了一个全面的重写，极度好用：</p> 
<p><img height="1236" src="https://oscimg.oschina.net/oscnet/up-644b609afd4548925f8dd18f749eb74d210.png" width="1729" referrerpolicy="no-referrer"></p> 
<p>可以直接选择附件里的 视频、图片、附件资料插入到编辑器，简单省事。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>JPress v4.1.5 更新内容如下：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新增：文章、页面、产品编辑器新增选择附件的功能，可以直接插入附件、图片和视频</li> 
 <li>优化：加强对 xss 的防护，默认启用全局 xss 拦截</li> 
 <li>优化：输入选择框 'form-control-clear' 的样式</li> 
 <li>优化：优化许些提示文字，使之更加友好</li> 
 <li>修复：选择用户弹出页面，输入关键字搜索时 404 的问题</li> 
 <li>修复：JPress 弹出 layer 无法上下滚动的问题</li> 
 <li>修复：#defaultMenu() 指令三级以上菜单无法打开的问题</li> 
 <li>修复：后台 Dashboard 移动评论到垃圾箱出错的问题</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">说的再多，不如亲自一试。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在 阿里云（腾讯云） 上一键通过 8080 端口运行</strong></p> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">wget</span></span></span></span></span></span></span></span></span></span></span></span> https://gitee.com/JPressProjects/jpress/raw/master/install.sh && bash install.sh <span><span><span><span>8080</span></span></span></span></pre> 
  </div> 
  <p style="margin-left:0; margin-right:0"> 一键运行视频教程：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ketang8.com%2Fcourse%2Fstudy%3FchapterId%3D184" target="_blank">http://www.ketang8.com/course/study?chapterId=184</a></p> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>通过 Docker 上运行</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">curl</span></span></span></span></span></span></span></span></span></span></span></span> -O https://gitee.com/JPressProjects/jpress/raw/master/docker-compose.yml && docker-compose up -d</pre> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>通过 Eclipse 或者 Idea 等开发工具运行</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>1、在本地安装好 Java、Maven 等开发环境</li> 
 <li>2、将源码下载、并导入 eclipse 或者 idea</li> 
 <li>3、在项目的<strong>根目录</strong>，执行 <code>mvn clean install</code> 命令进行编译</li> 
 <li>4、在开发工具，右键运行 <code>starter/src/main/java/io.jpress.Starter</code> 下的 <code>main()</code> 方法</li> 
 <li>5、通过浏览器访问 <code>http://127.0.0.1:8080</code>，进行自动安装</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>交流</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2F" target="_blank">http://www.jpress.io</a></li> 
 <li>文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jpress.io" target="_blank">http://doc.jpress.io</a></li> 
 <li>论坛社区：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Fclub" target="_blank">点击这里</a></li> 
 <li>插件列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Farticle%2Fcategory%2Fplugin" target="_blank">点击这里</a></li> 
 <li>模板列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Farticle%2Fcategory%2Ftemplate" target="_blank">点击这里</a></li> 
</ul>
                                        </div>
                                      
</div>
            