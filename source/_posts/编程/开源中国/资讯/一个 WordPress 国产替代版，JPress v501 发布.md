
---
title: '一个 WordPress 国产替代版，JPress v5.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-18d8f446ef973f57dee5a86d29638f306df.png'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 09:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-18d8f446ef973f57dee5a86d29638f306df.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="1384" src="https://oscimg.oschina.net/oscnet/up-18d8f446ef973f57dee5a86d29638f306df.png" width="2418" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">JPress 是一个使用 Java 开发的类似 WordPress 的产品，始于2015年。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200 + 上市公司，中科院、红 + 字会等。然而，JPress 不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>JPress v5.0.1 更新内容如下：</strong></p> 
<ul> 
 <li>优化：增强 #pages() 指令，可以通过更多的参数获取内容</li> 
 <li>优化：升级 JQuery BsFormBuilder 等到最新版本</li> 
 <li>修复：在 JPress 进行安装的时候，可能有 NPE 的问题</li> 
 <li>修复：后台表单功能无法删除的问题</li> 
 <li>修复：重置密码和邮箱激活可能有 NPE 的问题</li> 
 <li>修复：后台图片批量删除无用的问题</li> 
</ul> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">说的再多，不如亲自一试。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>在 阿里云（腾讯云） 上一键通过 8080 端口运行</strong></p> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">wget</span></span></span></span></span></span></span></span></span></span></span></span></span></span> https://gitee.com/JPressProjects/jpress/raw/master/install.sh && bash install.sh <span><span><span><span><span><span>8080</span></span></span></span></span></span>
</pre> 
  </div> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>通过 Docker 上运行</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">curl</span></span></span></span></span></span></span></span></span></span></span></span></span></span> -O https://gitee.com/JPressProjects/jpress/raw/master/docker-compose.yml 
&& docker-compose up -d</pre> 
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
 <li>官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.cn" target="_blank">http://www.jpress.cn</a></li> 
 <li>文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jpress.cn" target="_blank">http://doc.jpress.cn</a></li> 
 <li>JPress的案例：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.cn%2Farticle%2Fcategory%2Fcase" target="_blank">点击这里</a></li> 
 <li>JPress插件列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.cn%2Fproduct%2Fcategory%2Fplugin" target="_blank">点击这里</a></li> 
 <li>JPress模板列表：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.cn%2Fproduct%2Fcategory%2Ftemplate" target="_blank">点击这里</a></li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            