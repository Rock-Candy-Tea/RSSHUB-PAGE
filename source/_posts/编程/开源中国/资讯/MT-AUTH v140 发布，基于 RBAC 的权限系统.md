
---
title: 'MT-AUTH v1.4.0 发布，基于 RBAC 的权限系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2195'
author: 开源中国
comments: false
date: Wed, 30 Mar 2022 10:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2195'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0px; margin-right:0px; text-align:start">演示链接</h1> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.duoshu.org%2F" target="_blank">商城</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.duoshu.org%2Fadmin" target="_blank">商城后台</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fauth.duoshu.org%2F" target="_blank">登录中心</a></li> 
 <li>测试账户(2)：<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Auser1%40duoshu.org" target="_blank">user1@duoshu.org</a><span> </span>密：root</li> 
 <li>超级管理员(3)：<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Asuperadmin%40duoshu.org" target="_blank">superadmin@duoshu.org</a><span> </span>密：root</li> 
 <li>请勿删除任何数据，谢谢</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:start">更新日志</h1> 
<h2 style="text-align:start">通用</h2> 
<ul> 
 <li>修复了软删除数据唯一性BUG</li> 
 <li>改进了事件的发布方式</li> 
 <li>新增了延迟扫描来确保事件不被漏掉</li> 
 <li>修复了事件重复存储BUG</li> 
 <li>采用了自动清除MDC的线程池</li> 
 <li>重构了Enum相关SQL Utility</li> 
 <li>添加checkstyle检查代码</li> 
</ul> 
<h2 style="text-align:start">mt-access</h2> 
<ul> 
 <li>新增了验证服务</li> 
 <li>配置最大Http header(1MB)来解决413响应</li> 
</ul> 
<h2 style="text-align:start">mt-proxy</h2> 
<ul> 
 <li>配置最大Http header(1MB)来解决413响应</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            