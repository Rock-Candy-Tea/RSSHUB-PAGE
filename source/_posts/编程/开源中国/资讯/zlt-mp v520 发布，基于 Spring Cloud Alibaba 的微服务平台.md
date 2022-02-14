
---
title: 'zlt-mp v5.2.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 08:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="275" src="https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png" width="500" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">功能介绍</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="414" src="https://oscimg.oschina.net/oscnet/up-b7726359902d450aab833cda3b17a69b85c.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新内容</h2> 
<h3 style="text-align:left"><span>特性/增强</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>日志链路spanId生成规则优化</p> </li> 
 <li> <p>增加日志链路页面</p> </li> 
 <li> <p>增强授权中心UAA可配置功能</p> </li> 
 <li> <p>提高nacos日志打印级别</p> </li> 
 <li> <p>升级spring-boot到2.5.9</p> </li> 
 <li> <p>升级spring-boot-admin到2.5.5</p> </li> 
 <li> <p>升级hutool到5.7.20</p> </li> 
</ul> 
<h2 style="text-align:left"><strong style="color:#ffffff">内容说明</strong></h2> 
<h3 style="text-align:left"><span>一、spanId生成规则优化</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">合并spanId和parentId，由原来的UUID，如下图所示：</p> 
<p><img alt src="https://files.mdnice.com/user/514/89f71acf-808e-418c-95f0-dd3a330656f5.png" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">优化为有序数字，能直观分辨调用顺序与层级关系，如下图所示：</p> 
<p><img alt src="https://files.mdnice.com/user/514/93121a56-9ecd-4f13-8a8b-c209716a1853.png" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">上图示例中spanId的生成规则，如下链路拓扑图所示：</p> 
<p><img alt src="https://files.mdnice.com/user/514/7350cc05-ae68-406c-a209-227a0637c2fd.png" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="text-align:left"><span>二、增加日志链路页面</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">系统日志列表页面<span> </span><strong style="color:black">追踪id</strong><span> </span>字段增加超链接，点击弹出<span> </span><strong style="color:black">日志链路</strong><span> </span>页面：</p> 
<p><img alt src="https://files.mdnice.com/user/514/058aa337-8947-4255-8a9a-2d04ad03974f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">以树形方式展示对应<span> </span><strong style="color:black">追踪id</strong><span> </span>的全链路。</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">只显示存在日志数据的链路。</p> 
</blockquote> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="text-align:left"><span>三、增强授权中心UAA可配置功能</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">授权中心<span> </span><code>zlt-uaa</code><span> </span>工程增加以下配置功能：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p>是否<span> </span><strong style="color:black">同账号登录互踢</strong>：<code>zlt.security.auth.isSingleLogin</code></p> </li> 
</ol> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">如果为<span> </span><code>true</code><span> </span>则同一个账号如果在不同的客户端中重复登录多次，之前登录的状态会失效。</p> 
</blockquote> 
<ol start="2" style="margin-left:0; margin-right:0"> 
 <li> <p>是否<span> </span><strong style="color:black">同账号登录公用token</strong>：<code>zlt.security.auth.isShareToken</code></p> </li> 
</ol> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">如果为<span> </span><code>true</code><span> </span>则多个用户使用同一账号登录时共用一个token，意味着其中一个登出则使用该账号的所有用户都登出；只有<span> </span><code>isSingleLogin</code><span> </span>为<span> </span><code>false</code><span> </span>时会生效。</p> 
</blockquote> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="text-align:left"><span>四、提高nacos日志打印级别</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">提升项目的nacos日志级别，屏蔽疯狂打印的<span> </span><code>com.alibaba.nacos.client.naming</code><span> </span>日志。</p> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Github地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目文档</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目更新日志</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/93623</a></p>
                                        </div>
                                      
</div>
            