
---
title: 'TokenManager 0.0.2 发布：新增隔离环境配置'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/marker/token-manager/raw/master/image/img.png'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 17:45:00 GMT
thumbnail: 'https://gitee.com/marker/token-manager/raw/master/image/img.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">TokenManager是一款基于Java开发的Spring Boot组件，用于管理 三方平台的Token的中间件。</p> 
<p style="text-align:start">TokenManager将全场景的远程调用获取Token抽象到TokenManager接口中，通过调用指定的三方TokenAPI 实现各类三方平台的Token的管理。</p> 
<p style="text-align:start">TokenManager通过Redis的消息订阅特性实现了延时消息监听Token生命周期过期时间，从而自动刷新Token。 确保在高并发请求下，用户不会调用具体的三方接口实时获取Token。</p> 
<p style="text-align:start">TokenManager 默认实现了WEIXIN微信平台的accessToken（非用户授权码token）</p> 
<p style="text-align:start">TokenManager原理图如下所示：</p> 
<p style="text-align:start"><img alt src="https://gitee.com/marker/token-manager/raw/master/image/img.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"> </p> 
<h3 style="text-align:start">TokenManager特性</h3> 
<ul> 
 <li> <p><strong><u>多环境支持</u> </strong>例如：调试微信，获取appid+secrt换取accessToken，在开发环境、测试环境共用appid的情况，<u>可配置Token共享也可配置环境隔离</u>。</p> </li> 
 <li> <p><strong>自动刷新accessToken</strong> 支持基于Oauth2协议的刷新Token机制，无需干预自动刷新，最佳的管理方式，提高接口响应速度。</p> </li> 
 <li> <p><strong>多级缓存（待实现) </strong>支持本地缓存与远程缓存。本地缓存JVM级别的，远程缓存基于Redis。提高Token的访问速度，防止Redis击穿雪崩。 本地缓存的生命周期动态管理。</p> </li> 
 <li> <p><strong>可扩展 </strong>支持扩展现有的API实现，能够支持除了微信以外的其他平台。采用自动装配技术，实例动态注入到Spring容器中。</p> </li> 
 <li> <p><strong>支持请求日志拦截 </strong>通过RestTempalte 拦截器实现了请求日志拦截，默认实现了请求Slf4j的info级别日志。可以自定义配置个性化的拦截实现。</p> </li> 
</ul> 
<h3 style="text-align:start">TokenManger最新更新历史</h3> 
<pre><em>### 2021-11-06
</em><span style="color:#cc7832">- </span>增加多环境支持，默认单环境共享模式（适配有的内部平台同时提供了对应的多环境支持的情况）；
<span style="color:#cc7832">- </span>优化配置项； 
</pre> 
<h3 style="text-align:start">TokenManger快速开始</h3> 
<p style="text-align:start">  <a href="https://www.oschina.net/p/token-manager" target="_blank">《TokenManger快速开始》</a></p> 
<pre><span style="color:#808080">```
</span><span style="color:#808080"><!-- 开发者：marker 三方Token管理器 -->
</span><span style="color:#808080"><dependency>
</span><span style="color:#808080">    <groupId>com.wuweibi</groupId>
</span><span style="color:#808080">    <artifactId>token-manager</artifactId>
</span><span style="color:#808080">    <version>0.0.2</version>
</span><span style="color:#808080"></dependency>
</span><span style="color:#808080">```  </span>
</pre>
                                        </div>
                                      
</div>
            