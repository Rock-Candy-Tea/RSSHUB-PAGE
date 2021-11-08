
---
title: 'Sa-Token v1.28.0 发布，新增 jwt 集成插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
author: 开源中国
comments: false
date: Mon, 08 Nov 2021 09:18:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Sa-Token 是一个轻量级 Java 权限认证框架，主要解决：登录认证、权限认证、分布式 Session 会话、单点登录、OAuth2.0 等一系列权限相关问题。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过 Sa-Token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Sa-Token v1.28.0  版本更新包括以下内容：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新增：新增<span> </span><code>sa-token-jwt</code><span> </span>插件，用于与jwt的整合<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>新增：新增<span> </span><code>sa-token-context-dubbo</code><span> </span>插件，用于与 Dubbo 的整合<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>文档：文档新增章节：Sa-Token 插件开发指南<span> </span><strong style="color:#2c3e50">[重要]</strong></li> 
 <li>文档：文档新增章节：名称解释</li> 
 <li>优化：抽离<span> </span><code>getSaTokenDao()</code><span> </span>方法，方便重写</li> 
 <li>新增：单元测试新增多账号模式数据不互通测试</li> 
 <li>优化：优化在线文档，修复部分错误之处</li> 
 <li>优化：优化未登录异常抛出提示，标注无效的Token值</li> 
 <li>修复：修复单词拼写错误<span> </span><code>getDeviceOrDefault</code></li> 
 <li>优化：优化 jwt 集成示例</li> 
 <li>文档：新增常见问题总结</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>代码仓库：<a href="https://gitee.com/dromara/sa-token">https://gitee.com/dromara/sa-token</a></strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>框架功能结构图</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="274" src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png" width="500" referrerpolicy="no-referrer"></strong></p>
                                        </div>
                                      
</div>
            