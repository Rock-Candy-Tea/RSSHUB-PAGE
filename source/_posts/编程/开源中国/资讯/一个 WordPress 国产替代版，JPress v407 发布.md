
---
title: '一个 WordPress 国产替代版，JPress v4.0.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 10:49:00 GMT
thumbnail: 'https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:center"><img src="https://gitee.com/JPressProjects/jpress/raw/master/doc/images/screenshot.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。</p> 
<p style="text-align:left">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。然而，JPress不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</p> 
<p style="text-align:left"><strong>JPress v4.0.7 更新内容如下(包含 v4.0.6)：</strong></p> 
<ul> 
 <li style="text-align:left">新增：模板编辑、文章编辑、页面编辑、产品编辑 的快捷键保存功能</li> 
 <li style="text-align:left">新增：文章和产品搜索引擎的高亮显示...</li> 
 <li style="text-align:left">新增：文章搜索引擎和产品搜索引擎切换后，自动重建搜索引擎的索引功能</li> 
 <li style="text-align:left">优化：一键安装脚本，方便阿里云和腾讯云等服务器进行一键安装</li> 
 <li style="text-align:left">优化：升级 Jboot JFinal 到最新版本</li> 
 <li style="text-align:left">优化：日志框架由 logback 切换到 log4j2，性能更高</li> 
 <li style="text-align:left">优化：重构 product-provider 模块的包结构</li> 
 <li style="text-align:left">修复：文章和产品搜索引擎切换到 es 的时候可能出错的问题</li> 
 <li style="text-align:left">修复：setting_v4.html 不能使用的问题</li> 
 <li style="text-align:left">修复：ElasticSearch 在 Mysql8 下更新文章会导致类型出错的问题</li> 
 <li style="text-align:left">修复：开启文章 Lucene 搜索引擎后，导致 elastic 包冲突的而造成 NoClassDefFoundError 的异常问题</li> 
 <li style="text-align:left">修复：开启扁平化 URL 后，个别菜单可能无法正常高亮的问题</li> 
 <li style="text-align:left">文档：完善系统配置的 Http API 相关文档和单元测试用例</li> 
 <li style="text-align:left">文档：完善用户 Http API 相关的文档和单元测试用例</li> 
 <li style="text-align:left">文档：完善文章相关 Http API 相关的文档和单元测试用例</li> 
 <li style="text-align:left">文档：完善 API 签名算法的相关文档</li> 
</ul> 
<p style="text-align:left">说的再多，不如亲自一试。</p> 
<p style="text-align:left"><strong>在 阿里云（腾讯云） 上一键通过 8080 端口运行</strong></p> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <div> 
    <pre><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">wget</span></span></span></span> https://gitee.com/JPressProjects/jpress/raw/master/install.sh && bash install.sh 8080
</pre> 
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left"><strong>通过 Docker 上运行</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5"><span style="color:#005cc5">curl</span></span></span></span> -O https://gitee.com/JPressProjects/jpress/raw/master/docker-compose.yml && docker-compose up -d</pre> 
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
            