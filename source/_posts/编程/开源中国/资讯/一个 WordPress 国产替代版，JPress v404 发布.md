
---
title: '一个 WordPress 国产替代版，JPress v4.0.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
author: 开源中国
comments: false
date: Sun, 13 Jun 2021 17:28:00 GMT
thumbnail: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:center"><img src="https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。</p> 
<p style="text-align:left">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。然而，JPress不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</p> 
<p style="text-align:left"><strong>JPress v4.0.4 更新内容如下：</strong></p> 
<ul> 
 <li>新增：articles 路径的支持，用于渲染 "所有文章"</li> 
 <li>新增：products 路径的支持，用于渲染 "所有产品"</li> 
 <li>优化：增强文章、产品以及分类的固定连接支持 "-" 字符</li> 
 <li>优化：产品分类指令 productCategoryList 修改为 allProductCategories</li> 
 <li>优化：移除 AddonClassPath 的定义，Jboot 已经解决了动态加载的日志问题</li> 
 <li>优化：删除无用代码、重构 Service 的方法名称、移动 UrlUtils 的类到 utils 包下</li> 
 <li>优化：弹出的 layer 有小滚动条的问题</li> 
 <li>优化：安装时，某些 UI 细节错位的问题</li> 
 <li>优化：开启伪静态后，若没有填写后缀，默认后缀为 .html</li> 
 <li>优化：评论框以及前台导航菜单的样式细节</li> 
 <li>修复：后台商品编辑时无法显示最近标签的问题</li> 
 <li>修复：用户登录页面在某些情况下不跳转用户中心的问题</li> 
 <li>修复：用户中心下拉的购物车列表的产品无法点击的问题</li> 
 <li>修复：用户中心里，用户无法对产品评论进行删除的问题</li> 
 <li>修复：当开启扁平化 URL 后，文章详情、产品详情和页面的评论分页 URL 不正确的问题</li> 
 <li>修复：文章 tag 的 url 错误的问题</li> 
 <li>修复：在 tomcat 二级目录下，登录的验证码不能正确显示的问题</li> 
 <li>修复：后台的某些菜单无法显示的问题</li> 
 <li>修复：后台开启 扁平化 URL 不起作用的问题</li> 
 <li>修复：文章中 git 路径错误的问题</li> 
 <li>修复：设置伪静态后缀后，重启失效的问题</li> 
 <li>修复：后台启用第三方登录后，默认登录页面 UI 错位的问题</li> 
 <li>修复：自定义后台登录地址时，后台无法登录的问题</li> 
 <li>修复：git 上还保存着大写的 AdminLTE.min.css 的问题</li> 
 <li>修复：JPress初始化时可能的一些安全问题</li> 
 <li>修复：某些页面出现 js 错误的问题</li> 
 <li>修复：docker-compose.yml 版本号错误的问题</li> 
</ul> 
<p style="text-align:left">说的再多，不如亲自一试。</p> 
<p style="text-align:left"><strong>在 Linux 上一键运行</strong></p> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <div> 
    <pre><span style="color:#005cc5"><span style="color:#005cc5">wget</span></span> https://gitee.com/JPressProjects/jpress/raw/master/install.sh && bash install.s
</pre> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left"><strong>通过 Docker 上运行</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#005cc5"><span style="color:#005cc5">curl</span></span> -O https://gitee.com/JPressProjects/jpress/raw/master/docker-compose.yml && docker-compose up -d</pre> 
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
            