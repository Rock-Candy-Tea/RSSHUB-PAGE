
---
title: '一个 WordPress 国产替代版，JPress v4.0.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
author: 开源中国
comments: false
date: Tue, 15 Jun 2021 09:41:00 GMT
thumbnail: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:center"><img src="https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。</p> 
<p style="text-align:left">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。然而，JPress不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</p> 
<p style="text-align:left"><strong>JPress v4.0.5 更新内容如下：</strong></p> 
<div>
 优化：升级 Jboot 到 v3.9.18 最新版本
</div> 
<div> 
 <div>
  优化：获取当前页面的分页页码的代码
 </div> 
</div> 
<div>
 修复：用户中心非管理员账户无法查看内容和投稿的问题
</div> 
<div>
 修复：calmlog 模板的页面评论会产生 2 此评论的问题
</div> 
<div>
 修复：文章页面的评论 pageNumber 获取错误的问题
</div> 
<div>
 修复：用户注册时可能出现返回 json 内容，而未跳转登录页面的问题
</div> 
<p style="text-align:left">说的再多，不如亲自一试。</p> 
<p style="text-align:left"><strong>在 Linux 上一键运行</strong></p> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <div> 
    <pre><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">wget</span></span></span> https://gitee.com/JPressProjects/jpress/raw/master/install.sh && bash install.s
</pre> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left"><strong>通过 Docker 上运行</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">curl</span></span></span> -O https://gitee.com/JPressProjects/jpress/raw/master/docker-compose.yml && docker-compose up -d</pre> 
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
<h3 style="text-align:left"><strong>交流</strong></h3> 
<ul> 
 <li>官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2F" target="_blank">http://www.jpress.io</a></li> 
 <li>文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jpress.io" target="_blank">http://doc.jpress.io</a></li> 
 <li>论坛社区：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Fclub" target="_blank">点击这里</a></li> 
 <li>插件列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Farticle%2Fcategory%2Fplugin" target="_blank">点击这里</a></li> 
 <li>模板列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.io%2Farticle%2Fcategory%2Ftemplate" target="_blank">点击这里</a></li> 
</ul>
                                        </div>
                                      
</div>
            