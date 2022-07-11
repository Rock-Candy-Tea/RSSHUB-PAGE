
---
title: 'zlt-mp v5.4.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a3ed4ccd0987d8434fe11056644a41c074a.png'
author: 开源中国
comments: false
date: Mon, 11 Jul 2022 07:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a3ed4ccd0987d8434fe11056644a41c074a.png'
---

<div>   
<div class="content">
                                                                                            <p><img src="https://oscimg.oschina.net/oscnet/up-a3ed4ccd0987d8434fe11056644a41c074a.png" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">功能介绍</h1> 
<p><img src="https://oscimg.oschina.net/oscnet/up-2ba2d06a6a1d728c5fd8af4e3cce1810d54.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>特性 / 增强</span></h3> 
<ul style="list-style-type:disc"> 
 <li>支持<span> </span><code>webSocket</code><span> </span>鉴权</li> 
 <li>增加<span> </span><code>webSocket</code><span> </span>鉴权样例工程</li> 
 <li>支持手动<span> </span><strong>获取当前登录人</strong><span> </span>对象</li> 
 <li>增加手动<span> </span><strong>token鉴权</strong><span> </span>工具</li> 
 <li>增加<span> </span><strong>资源服务</strong><span> </span>样例工程</li> 
 <li>解决只要请求携带<span> </span><code>access_token</code>，排除鉴权的<span> </span><code>url</code><span> </span>依然会被拦截的问题</li> 
 <li>升级<span> </span><code>spring-boot</code><span> </span>到<span> </span><code>2.5.14</code></li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px">更新内容</h2> 
<h3><span>一、支持webSocket接口鉴权</span></h3> 
<p style="color:black; margin-left:0; margin-right:0">增加 <code>webSocket</code> 接口的通用鉴权拦截器，使用方式如下：</p> 
<pre><code><span style="color:#61aeee">@ServerEndpoint</span>(value = <span style="color:#98c379">"/websocket/test"</span>, configurator = WcAuthConfigurator<span>.<span style="color:#c678dd">class</span>)
</span></code></pre> 
<p style="color:black; margin-left:0; margin-right:0">在 <code>@ServerEndpoint</code> 注解中添加 <code>configurator</code> 参数，指定 <code>WcAuthConfigurator.class</code></p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">详细请参考样例工程 <code>websocket-demo</code></p> 
</blockquote> 
<h3><span>二、支持手动获取当前登录人对象</span></h3> 
<p style="color:black; margin-left:0; margin-right:0">在 contoller、service 或者 dao 层使用以下方法:</p> 
<pre><code>SysUser user = LoginUserContextHolder.getUser()
</code></pre> 
<p style="color:black; margin-left:0; margin-right:0">需要服务满足以下两个条件：</p> 
<blockquote> 
 <ol style="list-style-type:decimal"> 
  <li> <p>服务依赖 zlt-common-spring-boot-starter</p> </li> 
  <li> <p>请求的入口方法需要鉴权（排除鉴权的无法使用）</p> </li> 
 </ol> 
</blockquote> 
<h3><span>三、增加手动token鉴权工具</span></h3> 
<p style="color:black; margin-left:0; margin-right:0"><code>zlt-auth-client-spring-boot-starter</code> 依赖只会对 <code>http</code> 请求进行拦截鉴权。</p> 
<p style="color:black; margin-left:0; margin-right:0">对于其他协议如 <code>webSocket</code>、<code>dubbo</code>、<code>MQ</code>等如果需要进行 token 鉴权，可手动使用以下方法：</p> 
<pre><code>SysUser user = AuthUtils.checkAccessToken(String accessTokenValue)
</code></pre> 
<h3><span>四、增加资源服务样例工程</span></h3> 
<p style="color:black; margin-left:0; margin-right:0">增加工程 <code>resources-server-demo</code> 以最简化的代码演示如何快速集成一个带鉴权功能的服务，适用于 <code>无网络隔离</code> 架构。</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">对于 <code>无网络隔离</code> 架构，每个暴露 <code>http</code> 接口服务都需要进行 <code>access_token</code> 鉴权。</p> 
</blockquote> 
<h3><span>五、解决排除鉴权的url依然会被拦截的问题</span></h3> 
<p style="color:black; margin-left:0; margin-right:0">由于 <code>Security</code> 默认的机制，只要请求携带了 <code>access_token</code> 参数，无论是否配置了排除鉴权，都必定会进行鉴权；</p> 
<p style="color:black; margin-left:0; margin-right:0">新版本解决了上述问题。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></h2> 
<p style="color:black; margin-left:0; margin-right:0">Gitee地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="color:black; margin-left:0; margin-right:0">Github地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目文档</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目更新日志</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/936235</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            