
---
title: 'star 4k+ 的 JPress 博客系统发布新版，修复 Log4j 漏洞问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
author: 开源中国
comments: false
date: Fri, 10 Dec 2021 10:21:00 GMT
thumbnail: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img src="https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。然而，JPress不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</p> 
<blockquote> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">JPress v4.2.0 发布本来可以晚点发布的，但 Log4j 漏洞的爆出，为了保证用户能够及时升级，因此决定在第一时间发布了修复版本。</p> 
</blockquote> 
<p><strong>另外：JPress 正在参加2021年度OSC中国开源项目评选~  JPress 在 2022 也将会有大动作，来更好的服务大家，麻烦大家给 JPress 投一票。</strong></p> 
<p><strong>JPress 投票地址： <a href="https://www.oschina.net/project/top_cn_2021/?id=12">https://www.oschina.net/project/top_cn_2021/?id=12</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>JPress v4.2.0 更新内容如下：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新增：添加后台验证码开关，方便在某些场景下进行自动化测试</li> 
 <li>新增：支持发布0元的商品，支付金额为 0 时，直接支付成功，感谢<span> </span><a href="https://gitee.com/alienjunx">@AlienJunX</a></li> 
 <li>新增：插件安装目录自定义的功能，方便安装插件后，在编译清空 target 目录时，插件仍然可用</li> 
 <li>优化：完善文章模块添加收藏功能，感谢<span> </span><a href="https://gitee.com/xiasimao">@吓死猫的老鼠</a></li> 
 <li>优化：Option 系统配置允许传入空数据，用于清空配置</li> 
 <li>优化：调整上传默认附件大小，图片默认为 10MB，其他文件默认为 100MB</li> 
 <li>优化：升级 Jboot、Log4j2 等到最新版本</li> 
 <li>修复：后台自定义非法关键字无效的问题</li> 
 <li>修复：通过 API 删除 Option 可能不及时生效的问题</li> 
 <li>修复：插件依赖外部 jar ，在某些情况下可能会导致无法被安装的问题</li> 
 <li>修复：微信 H5 支付成功返回页面后出现 500 错误，感谢<span> </span><a href="https://gitee.com/alienjunx">@AlienJunX</a></li> 
 <li>修复：文章插入附件，当出现附件文件过大错误时，页面没有提示的问题</li> 
 <li>修复：CKEditor 编辑器 图片无法粘贴上传的问题</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">说的再多，不如亲自一试。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在 阿里云（腾讯云） 上一键通过 8080 端口运行</strong></p> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">wget</span></span></span></span></span></span></span></span></span></span></span></span></span> https://gitee.com/JPressProjects/jpress/raw/master/install.sh && bash install.sh <span><span><span><span><span>8080</span></span></span></span></span></pre> 
  </div> 
  <p style="margin-left:0; margin-right:0"> 一键运行视频教程：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ketang8.com%2Fcourse%2Fstudy%3FchapterId%3D184" target="_blank">http://www.ketang8.com/course/study?chapterId=184</a></p> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>通过 Docker 上运行</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">curl</span></span></span></span></span></span></span></span></span></span></span></span></span> -O https://gitee.com/JPressProjects/jpress/raw/master/docker-compose.yml && docker-compose up -d</pre> 
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
</ul>
                                        </div>
                                      
</div>
            