
---
title: 'JPress v4.0.1 发布，一个用 Java 开发的类似 WordPress 的软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 02:03:00 GMT
thumbnail: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:center"><img src="https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。</p> 
<p style="text-align:left">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。然而，JPress不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"><strong>JPress v4.0.1 更新内容如下：</strong></p> 
<ul> 
 <li>新增：用户中心财务和个人信息菜单可以通过 MenuManager 进行管理的功能，方便插件化定制</li> 
 <li>优化：优化 CKEditor5 编辑器，移除一些不必要的插件和新增code插件</li> 
 <li>优化：所有的 Module 应该继承 ModuleBase</li> 
 <li>修复：安装模版之后，跳转模版页面错误的问题。close #I3UKIF</li> 
 <li>修复：模板编辑不能保存的问题。close #I3UJAX</li> 
 <li>修复：文章列表页>点击文章标题>跳到新增页面去了。close #I3UJAW</li> 
 <li>修复：文章编辑、产品编辑页面的时间选择组件无法正确弹出的问题。</li> 
 <li>修复：在安装页面 AdminLTE.min.css 引用路径错误的问题</li> 
</ul> 
<p> </p> 
<p style="text-align:left">说的再多，不如亲自一试。</p> 
<p style="text-align:left"><strong>在 Linux 上一键运行</strong></p> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <div> 
    <pre><span style="color:#005cc5">wget</span> https://gitee.com/JPressProjects/jpress/raw/master/install.sh && bash install.s
</pre> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left"><strong>通过 Docker 上运行</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#005cc5">curl</span> -O https://gitee.com/JPressProjects/jpress/raw/master/docker-compose.yml && docker-compose up -d</pre> 
 </div> 
</div> 
<p style="text-align:left"><strong>通过 Eclipse 或者 Idea 等开发工具运行</strong></p> 
<ul> 
 <li>1、在本地安装好 Java、Maven 等开发环境</li> 
 <li>2、将源码下载、并导入 eclipse 或者 idea</li> 
 <li>3、在项目的<strong>根目录</strong>，执行 <code>mvn clean install</code> 命令进行编译</li> 
 <li>4、在开发工具，右键运行 <code>starter/src/main/java/io.jpress.Starter</code> 下的 <code>main()</code> 方法</li> 
 <li>5、通过浏览器访问 <code>http://127.0.0.1:8080</code>，进行自动安装</li> 
</ul> 
<p> </p> 
<h3 style="text-align:left"><strong>交流</strong></h3> 
<ul> 
 <li>官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2F" target="_blank">http://www.jpress.io</a></li> 
 <li>论坛社区：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Fclub" target="_blank">点击这里</a></li> 
 <li>插件列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Farticle%2Fcategory%2Fplugin" target="_blank">点击这里</a></li> 
 <li>模板列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Farticle%2Fcategory%2Ftemplate" target="_blank">点击这里</a></li> 
</ul> 
<p style="text-align:left">接下来的时间里，JPress 将更加专注为中国互联网生态，会基于 JPress 陆续推出 微信小程序、百度小程序、文档和视频教程等，呼吁广大的 前端工程师、Javaer 起来完善 JPress 模板及插件生态。一起见证一个更好的中国的 JPress。</p>
                                        </div>
                                      
</div>
            