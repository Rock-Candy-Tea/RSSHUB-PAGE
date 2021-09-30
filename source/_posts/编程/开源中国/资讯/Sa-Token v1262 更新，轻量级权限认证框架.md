
---
title: 'Sa-Token v1.26.2 更新，轻量级权限认证框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
author: 开源中国
comments: false
date: Thu, 30 Sep 2021 10:49:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Sa-Token是一个轻量级Java权限认证框架，主要解决：登录认证、权限认证、分布式Session会话、单点登录、OAuth2.0 等一系列权限相关问题。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过 Sa-Token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Sa-Token v1.26.2  版本更新包括以下内容：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>废弃 SaTokenAction 接口，新增 SaStrategy 策略类，方便内部逻辑按需重写  </li> 
 <li>SaTokenConfig 配置类中属性 jwtSecretKey 改为 jwtSecretkey </li> 
 <li>临时认证模块新增 deleteToken 方法用于回收 Token </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left">SaStrategy例：</p> 
<pre><code class="language-java">// SaStrategy全局单例，所有方法都用以下形式重写 
SaStrategy.me.setCreateToken((loginId, loginType) -> &#123;
// 自定义Token生成的算法 
return "xxxx";
&#125;);</code></pre> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong>代码仓库：<a href="https://gitee.com/dromara/sa-token">https://gitee.com/dromara/sa-token</a></strong></h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>框架功能结构图</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt height="274" src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js3.png" width="500" referrerpolicy="no-referrer"></strong></p> 
<p> </p>
                                        </div>
                                      
</div>
            