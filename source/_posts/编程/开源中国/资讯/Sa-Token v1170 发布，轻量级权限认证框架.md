
---
title: 'Sa-Token v1.17.0 发布，轻量级权限认证框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png'
author: 开源中国
comments: false
date: Sat, 17 Apr 2021 22:17:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">sa-token是一个轻量级Java权限认证框架，主要解决：登录认证、权限认证、分布式Session会话、单点登录、OAuth2.0 等一系列权限相关问题。</p> 
<p style="text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过sa-token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="text-align:left">sa-token v1.17.0  版本更新包括以下内容：</p> 
<p style="text-align:left">- 修复：在WebFlux环境中引入Redis集成包无法启动的问题<br> - 修复：修复JWT集成示例中版本升级API的变更<br> - 优化：优化启动时字符画打印<br> - 文档：新增集成环境说明<br> - 文档：新增功能介绍图<br> - 新增：全局过滤器增加限定[拦截路径]与[排除路径]功能<br> - 重构：全局过滤器执行函数放到成员变量里，连缀风格配置<br> - 新增：新增全局侦听器，可在用户登陆、注销、被踢下线等关键性操作时进行一些AOP操作 [重要]</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-9dcf2d8f60bf05c3f31d6f8a6ce60f1c6c3.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">更多详细信息请关注官方文档</p>
                                        </div>
                                      
</div>
            