
---
title: 'JPress v4.0 rc.1 发布，大量的 UI 优化和简化模板制作成本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bc7a63ef2edd977c7886db82136085aee48.png'
author: 开源中国
comments: false
date: Mon, 24 May 2021 16:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bc7a63ef2edd977c7886db82136085aee48.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">JPress v4.0 rc 版本来了</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。</span></p> 
<p>JPress v4.0 rc 版本中，新增了一个全新的指令 @defaultMenu() ，一行代码完成前端菜单展示，并带有多级菜单显示的功能。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bc7a63ef2edd977c7886db82136085aee48.png" referrerpolicy="no-referrer"></p> 
<p>此外，JPress v4 的用户中心 和 后台功能还进行了大量的细节优化，比如：</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-b45679f70f0cd04f4d5c54945906b61e4b2.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">(旧版本的文章编写功能)</span></p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-93968bd6469a0919d3c605551a9b132f5ff.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">(新版本的文章编写功能)</span></p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-a4a105d867a85e699c7065425c95731f329.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">(旧版本的用户中心)</span></p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-90c490ec42af51ef405371ea9c7180a9cce.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">(新版本的用户中心)</span></p> 
<p style="text-align:left">同时，JPress v4.0 的相关依赖升级到了最新版本，防止依赖带来的可能性漏洞，比如 fastjson 、jboot、jfinal 等。</p> 
<p style="text-align:left">尝鲜的小伙伴赶紧用起来吧，注意使用 JPress v4 的 git 分支：<a href="https://gitee.com/JPressProjects/jpress/tree/v4.0/">https://gitee.com/JPressProjects/jpress/tree/v4.0/</a></p> 
<p style="text-align:left"><strong>通过 Eclipse 或者 Idea 等开发工具运行</strong></p> 
<ul> 
 <li>1、在本地安装好 Java、Maven 等开发环境</li> 
 <li>2、将源码下载、并导入 eclipse 或者 idea</li> 
 <li>3、在项目的<strong>根目录</strong>，执行 <code>mvn clean install</code> 命令进行编译</li> 
 <li>4、在开发工具，右键运行 <code>starter/src/main/java/io.jpress.Starter</code> 下的 <code>main()</code> 方法</li> 
 <li>5、通过浏览器访问 <code>http://127.0.0.1:8080</code>，进行自动安装</li> 
</ul> 
<p style="text-align:left">使用国产中有任何问题，直接到 <a href="https://gitee.com/JPressProjects/jpress/issues">https://gitee.com/JPressProjects/jpress/issues</a> 反馈即可。</p>
                                        </div>
                                      
</div>
            