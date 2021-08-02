
---
title: 'web-flash 2.1 发布，集成 activit 工作流引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1292c352b4513e50a79ba9e0178ffc82e2e.gif'
author: 开源中国
comments: false
date: Mon, 02 Aug 2021 10:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1292c352b4513e50a79ba9e0178ffc82e2e.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">web-flash 是一个</span><span style="background-color:#ffffff; color:#40485b">基于 Spring Boot+Vue.js 的后台管理系统，权限管理，包含功能：字典，配置，定时任务，短信，邮件，根据excel模板导出，cms内容管理，手机端h5，IDEA 代码生成插件。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">本次更新重点为：集成activit工作流引擎提供了基本的工作功能。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">全部更新内容如下:</span></p> 
<h3 style="text-align:start">Issues</h3> 
<ul> 
 <li>Issue 集成activiti实现基本的工作流功能</li> 
 <li>Issue 启用keep-Alive保存标签页状态</li> 
 <li>Change 路由模式由默认的hash调整为history</li> 
 <li>Change 去掉maven冗余的依赖</li> 
 <li>Change 完善单元测试</li> 
 <li>Change 完善代码生成器中controller生成模板中关于权限配置部分</li> 
</ul> 
<h3 style="text-align:start">Fixes</h3> 
<ul> 
 <li>Fix  后端启动后，API接口访问不到后端，中途权限被拦截</li> 
 <li>Fix token验证失败后，弹出过多token过期提示</li> 
 <li>Fix 初始化sql语句中菜单资源地址重复的问题</li> 
</ul> 
<p style="text-align:left">后台管理预览：</p> 
<p style="text-align:left"><img alt height="375" src="https://oscimg.oschina.net/oscnet/up-1292c352b4513e50a79ba9e0178ffc82e2e.gif" width="666" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">手机端cms站点预览：</span></p> 
<p style="text-align:left"><img alt height="482" src="https://oscimg.oschina.net/oscnet/up-4c17d6aafcd4ae71d4e819a2582a35e225e.gif" width="222" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">后台管理在线预览：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fflashadmin.enilu.cn%2F" target="_blank">http://flashadmin.enilu.cn</a></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#40485b">手机端cms站点预览：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fflash-mobile.enilu.cn%2F%23%2Findex" target="_blank">http://flash-mobile.enilu.cn/#/index</a></span></p> 
<p style="text-align:start">在线文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwebflash.enilu.cn%2F" target="_blank">http://webflash.enilu.cn</a></p>
                                        </div>
                                      
</div>
            