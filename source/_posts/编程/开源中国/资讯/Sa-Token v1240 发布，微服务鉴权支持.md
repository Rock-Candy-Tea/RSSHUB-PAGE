
---
title: 'Sa-Token v1.24.0 发布，微服务鉴权支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
author: 开源中国
comments: false
date: Mon, 26 Jul 2021 01:34:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">Sa-Token是一个轻量级Java权限认证框架，主要解决：登录认证、权限认证、Session会话、单点登录、OAuth2.0 等一系列权限相关问题</p> 
<p style="text-align:left">框架集成简单、开箱即用、API设计清爽，通过Sa-Token，你将以一种极其简单的方式实现系统的权限认证部分</p> 
<p style="text-align:left">Sa-Token v1.24.0  版本更新主要为微服务鉴权支持，包括以下内容：</p> 
<ul> 
 <li>修复：修复部分场景下Alone-Redis插件导致项目无法启动的问题</li> 
 <li>优化：增加对SpringBoot1.x版本的兼容性</li> 
 <li>新增：SaOAuth2Util新增checkScope函数，用于校验令牌是否具备指定权限</li> 
 <li>新增：OAuth2.0模块新增revoke接口，用于提前回收 Access-Token 令牌</li> 
 <li>新增：新增<code>Sa-Id-Token</code> 模块，解决微服务内部调用鉴权 <strong>[重要]</strong></li> 
 <li>文档：新增OAuth2.0模块常用方法说明</li> 
 <li>优化：大幅度优化文档示例</li> 
</ul> 
<h4 style="text-align:left"><strong>代码仓库：<a href="https://gitee.com/dromara/sa-token">https://gitee.com/dromara/sa-token</a></strong></h4> 
<p style="text-align:left">框架功能结构图</p> 
<p style="text-align:left"><img alt src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png" referrerpolicy="no-referrer"></p> 
<p>更多信息请参考官方文档</p>
                                        </div>
                                      
</div>
            