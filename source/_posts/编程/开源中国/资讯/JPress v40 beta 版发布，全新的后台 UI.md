
---
title: 'JPress v4.0 beta 版发布，全新的后台 UI'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c774d00916d12236ef6d7aa95e86400ba14.png'
author: 开源中国
comments: false
date: Mon, 17 May 2021 09:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c774d00916d12236ef6d7aa95e86400ba14.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>JPress v4.0 来了</p> 
<p><span style="background-color:#ffffff; color:#333333">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。然而，JPress不仅仅只是建站，我们认为不管世界的互联网发生什么样的变化，APP、小程序都需要有网站支持，这才是我们的切入点。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">目前是 JPress v4.0 的第一个 beta 版本，请勿使用在正式环境上。尝鲜或做模板开发的同学，可以开始来做模板功能兼容测试。</span></p> 
<p> </p> 
<p>JPress v4.0 中，后台进行了全新的升级，使用 bootstrap 4 在作为底层 UI 框架，编辑也移除了 ckeditor 和 simplemd，而使用国产编辑器 wangEditor 和 vditor 替换。</p> 
<p><img height="1182" src="https://oscimg.oschina.net/oscnet/up-c774d00916d12236ef6d7aa95e86400ba14.png" width="1719" referrerpolicy="no-referrer"></p> 
<p><img height="1175" src="https://oscimg.oschina.net/oscnet/up-2cb5b381f59ead82f797e7a184e243dda0b.png" width="1703" referrerpolicy="no-referrer"></p> 
<p>同时，JPress v4.0 的相关依赖升级到了最新版本，防止依赖带来的可能性漏洞，比如 fastjson 、jboot、jfinal 等。</p> 
<p>尝鲜的小伙伴赶紧用起来吧，注意使用 JPress v4 的 git 分支：<a href="https://gitee.com/JPressProjects/jpress/tree/v4.0/">https://gitee.com/JPressProjects/jpress/tree/v4.0/</a></p> 
<p style="text-align:left"><strong>通过 Eclipse 或者 Idea 等开发工具运行</strong></p> 
<ul> 
 <li>1、在本地安装好 Java、Maven 等开发环境</li> 
 <li>2、将源码下载、并导入 eclipse 或者 idea</li> 
 <li>3、在项目的<strong>根目录</strong>，执行 <code>mvn clean install</code> 命令进行编译</li> 
 <li>4、在开发工具，右键运行 <code>starter/src/main/java/io.jpress.Starter</code> 下的 <code>main()</code> 方法</li> 
 <li>5、通过浏览器访问 <code>http://127.0.0.1:8080</code>，进行自动安装</li> 
</ul> 
<p>使用国产中有任何问题，直接到 <a href="https://gitee.com/JPressProjects/jpress/issues">https://gitee.com/JPressProjects/jpress/issues</a> 反馈即可。</p>
                                        </div>
                                      
</div>
            