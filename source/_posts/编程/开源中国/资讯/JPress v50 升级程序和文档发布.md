
---
title: 'JPress v5.0 升级程序和文档发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-99eedaa3be4d4eeec05cd97d9eeb3c7b0be.png'
author: 开源中国
comments: false
date: Thu, 25 Aug 2022 11:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-99eedaa3be4d4eeec05cd97d9eeb3c7b0be.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:left">前几天发布了 JPress v5.0 正式版，但是其相关的升级程序和文档尚未发布。今天 JPress v5.0 的升级程序来了，支持 JPress v3.x 和 v4.x 平滑升级到 JPress v5.0。</p> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">升级流程如下：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>1、下载最新的 JPress v5.0</p> </li> 
 <li> <p>2、Copy 低版本的 JPress 里的 attachement 目录到 JPress5 的根目录</p> </li> 
 <li> <p>3、若低版本的 JPress 安装了其他模板，则也需要把这个模板模板 Copy 放到 JPress5 的 templates 目录里面。</p> </li> 
 <li> <p>4、启动最新的 JPress5，访问浏览器时，浏览器页面会自动引导用户走安装（升级）流程。</p> </li> 
</ul> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left"> </p> 
<p><img height="604" src="https://oscimg.oschina.net/oscnet/up-99eedaa3be4d4eeec05cd97d9eeb3c7b0be.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">第一步：主要是告诉用户需要准备一些必要的数据信息。</p> 
<p><img height="604" src="https://oscimg.oschina.net/oscnet/up-b183c4cd547ab6fa2b5d1b02c269af4fbfd.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">第二步：非常重要，如果是升级，则需要填写低版本的 JPress 链接的数据库；如果是安装，则填写一个全新的数据库即可。</p> 
<p><img height="604" src="https://oscimg.oschina.net/oscnet/up-34608d6e071d984fe34883b12a3448e36b9.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">第三步：主要告知用户必须备份数据库，因为 JPress 在升级的过程中，会执行许多的 ddl 语句，这个过程是无法回退的，因此告知用户必须对数据进行备份。</p> 
<blockquote>
 <strong style="color:#555555">“</strong> 
 <p style="color:black; margin-left:0; margin-right:0">虽然我们做过了非常多的测试，在我们本地没问题的，但是不保证任何场景下都是没问题，因此，备份数据库是目前唯一可以回退的办法。</p> 
</blockquote> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">在这个步骤中，我们可以设置超级管理员的账号和密码。在忘记超级管理员账号和密码的情况下，也可以通过重新安装的这种方式，对超级管理员的账号和密码进行重置。这个步骤若不填写任何内容，则保留之前的超级管理员账户信息。</p> 
<p> </p> 
<p><img height="649" src="https://oscimg.oschina.net/oscnet/up-f5971bd17b015b8dce527bf9668510a11c3.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">当用户确认备份好数据，并点击确认升级，不出意外的话稍等片刻，会告知用户升级成功，并跳转到登录页面，此时，代表 JPress 已经正常升级完成。</p> 
<p> </p> 
<p><img height="604" src="https://oscimg.oschina.net/oscnet/up-038888337363c2c9628a007110cd6b18ab6.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">另外，关于更多的 JPress 安装，比如</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p>在 Linux 上安装</p> </li> 
 <li> <p>在 Windows 上安装</p> </li> 
 <li> <p>通过 Docker 进行安装</p> </li> 
 <li> <p>通过 宝塔 进行安装</p> </li> 
 <li> <p>.. 等等</p> </li> 
</ul> 
<p style="color:#595959; margin-left:0; margin-right:0; text-align:left">可以通过 JPress 的文档站点：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jpress.cn%2F" target="_blank">http://doc.jpress.cn</a><span> </span>获取更多。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>交流</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jpress.cn" target="_blank">http://www.jpress.cn</a></li> 
 <li>文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jpress.cn" target="_blank">http://doc.jpress.cn</a></li> 
</ul>
                                        </div>
                                      
</div>
            