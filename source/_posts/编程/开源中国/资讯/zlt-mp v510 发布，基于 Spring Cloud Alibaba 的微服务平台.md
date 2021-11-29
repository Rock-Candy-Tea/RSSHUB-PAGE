
---
title: 'zlt-mp v5.1.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
author: 开源中国
comments: false
date: Mon, 29 Nov 2021 07:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="275" src="https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png" width="500" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">功能介绍</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="414" src="https://oscimg.oschina.net/oscnet/up-b7726359902d450aab833cda3b17a69b85c.png" width="500" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">特性/增强</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>认证中心支持<strong style="color:black">单点登出</strong></p> </li> 
 <li> <p>sso-demo增加单点登出支持</p> </li> 
 <li> <p>日志链路追踪增加spanId和parentId字段</p> </li> 
 <li> <p>升级spring-boot到2.5.7</p> </li> 
 <li> <p>升级spring-cloud到2020.0.4</p> </li> 
</ul> 
<h3 style="text-align:left"><span>问题修复</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>解决客户端模式授权报错问题</p> </li> 
</ul> 
<h3 style="text-align:left"><span>变更语句</span></h3> 
<pre style="text-align:left"><code><span style="color:#c678dd">Use</span> <span style="color:#98c379">`oauth-center`</span>;
<span style="color:#c678dd">update</span> oauth_client_details <span style="color:#c678dd">set</span> additional_information = <span style="color:#98c379">'&#123;"LOGOUT_NOTIFY_URL_LIST":"http://127.0.0.1:8082/logoutNotify"&#125;'</span>
<span style="color:#c678dd">where</span> client_id = <span style="color:#98c379">'webApp'</span>;

<span style="color:#c678dd">update</span> oauth_client_details <span style="color:#c678dd">set</span> additional_information = <span style="color:#98c379">'&#123;"LOGOUT_NOTIFY_URL_LIST":"http://127.0.0.1:8081/logoutNotify"&#125;'</span>
<span style="color:#c678dd">where</span> client_id = <span style="color:#98c379">'app'</span>;
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">内容说明</h2> 
<h3 style="text-align:left"><span>一、认证中心支持单点登出</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">认证中心支持多个系统在基于<span> </span><code>OAuth2.0</code><span> </span>实现单点登录之后，当其中一个系统登出之后，其他系统也同时登出的功能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">在<span> </span><code>zlt-uaa</code><span> </span>工程中通过参数<span> </span><code>unifiedLogout</code>来配置是否开启单点登出功能，默认为<span> </span><code>false</code></p> 
<pre style="text-align:left"><code><span style="color:#d19a66">zlt:</span>
  <span style="color:#d19a66">security:</span>
    <span style="color:#d19a66">auth:</span>
      <span style="color:#d19a66">unifiedLogout:</span> <span style="color:#56b6c2">true</span>
</code></pre> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">相关原理和代码解析看在线文档：https://www.kancloud.cn/zlt2000/microservices-platform/2539642</p> 
</blockquote> 
<h3 style="text-align:left"><span>二、sso-demo增加单点登出支持</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><code>oidc-sso</code><span> </span>和<span> </span><code>web-sso</code><span> </span>这两个单点登录 demo 已经改造支持<strong style="color:black">单点登出</strong>功能。</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">关于 demo 的具体的使用步骤大家直接看每个 demo 工程下的 README.md 文件即可。</p> 
</blockquote> 
<h3 style="text-align:left"><span>三、日志链路追踪优化</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><code>zlt-log-spring-boot-starter</code><span> </span>工程中的日志全链路追踪，由之前的单个<span> </span><code>traceId</code><span> </span>的基础上增加 2 个字段：<code>spanId</code><span> </span>和<span> </span><code>parentId</code></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">格式为：[traceId,spanId,parentId]</p> 
<pre style="text-align:left"><code>[a4013b536bbda96d,<span style="color:#d19a66">2258e9</span>dde4eb40a2,a4013b536bbda96d]
</code></pre> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">相关原理和代码解析看在线文档：https://www.kancloud.cn/zlt2000/microservices-platform/1228555</p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Github地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目文档</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目更新日志</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/936235</a></p>
                                        </div>
                                      
</div>
            