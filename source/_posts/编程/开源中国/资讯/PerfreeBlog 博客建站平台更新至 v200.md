
---
title: 'PerfreeBlog 博客建站平台更新至 v2.0.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e473f240c4528c9087e0e4ca2d1a6dabfaf.png'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 11:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e473f240c4528c9087e0e4ca2d1a6dabfaf.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">PerfreeBlog </span><span style="background-color:#ffffff; color:#333333">是一款基于 Java SpringBoot 开发的博客建站平台,支持主题在线切换,支持扩展插件等功能</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能一览</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>设计简洁，界面美观</li> 
 <li>采用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.markdownguide.org%2F" target="_blank">Markdown</a>编辑器,支持一键插入视频、图片</li> 
 <li>支持多主题自由切换</li> 
 <li>主题在线编辑,及时生效</li> 
 <li>友情链接管理</li> 
 <li>支持附件管理</li> 
 <li>支持扩展插件</li> 
 <li>主题开发简单快速</li> 
 <li>支持邮件服务</li> 
 <li>安装部署简单</li> 
 <li>支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.mysql.com%2F" target="_blank">mysql</a>/<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sqlite.org%2F" target="_blank">sqlite</a>数据库</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>此版本更新内容包括：</strong></h2> 
<ul> 
 <li style="text-align:start">新增 模板语法新增WEB_SITE全局变量,用于获取当前网址</li> 
 <li style="text-align:start">修复 修复seo展示异常问题</li> 
 <li style="text-align:start">优化 完善接口/接口swagger文档(可参考文档-主题开发-api接口)</li> 
 <li style="text-align:start">优化 新增配置项/注册等API接口</li> 
 <li style="text-align:start">优化 修改自定义页面流程,文章和页面可自定义slug</li> 
 <li style="text-align:start">优化 其他修改</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start"><strong>注意事项一: 此版本为大版本变更,修改了文章及页面的slug逻辑,如之前有配置友链菜单则会形成访问404的问题,请在页面管理,编辑友链页面,将slug修改为link,同时在菜单管理修改地址为/page/link,其他自定义菜单及页面同理</strong></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start"><strong>注意事项二: 此版本为大版本变更,内置的主题perfree/simpl均已更新支持2.0.0版本,如使用的其他主题,请进行同步更新</strong></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">站点</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官网地址:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.perfree.org.cn%2F" target="_blank">http://www.perfree.org.cn</a></li> 
 <li>文档地址:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.perfree.org.cn%2Fdoc" target="_blank">http://www.perfree.org.cn/doc</a></li> 
 <li>演示站点:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yinpengfei.com%2F" target="_blank">https://www.yinpengfei.com</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">主题预览</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">fly</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-e473f240c4528c9087e0e4ca2d1a6dabfaf.png" width="1415" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">indigo</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-c40400dced7da8b3c3a3d4e52af6076d08d.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">admas</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-436a56564ba8756efe7be90920aca7bb5d4.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">perfree</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-00812eb8ee615618a81317a80f1ceb6a251.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">simple</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-e9afb27d92a533ed0d414d60e97d0ce2622.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后台界面</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">写文章</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-89ee5e6f55874dccb911f905f22a6382976.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">文章管理</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-557e1f08c28efb5427d0bc6658aa973e585.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">主题</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-d1c2f80ce7750cdac99843246d9719d05ea.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">主题编辑</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-5f46afcc4648e7e2c10105ebd285846222a.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">插件管理</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="961" src="https://oscimg.oschina.net/oscnet/up-484c55037c318a97ef89ed8290de2a5ce58.png" width="1920" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            