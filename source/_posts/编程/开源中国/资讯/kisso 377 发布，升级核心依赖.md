
---
title: 'kisso 3.7.7 发布，升级核心依赖'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7153'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 18:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7153'
---

<div>   
<div class="content">
                                                                                            <p>kisso 3.7.7 发布，升级核心依赖</p> 
<p style="text-align:left">kisso = cookie sso 基于 Cookie 的 SSO 中间件，它是一把快速开发 java Web 登录系统（SSO）的瑞士军刀。</p> 
<ul> 
 <li> <p>前后分离可选：请求 Header 票据模式, 请求 Cookie 模式</p> </li> 
</ul> 
<h1 style="text-align:left">仓库</h1> 
<p style="text-align:left"><code>https://search.maven.org/search?q=g:com.baomidou</code></p> 
<div style="text-align:left"> 
 <div> 
  <pre><dependency>
  <groupId>com.baomidou</groupId>
  <artifactId>kisso</artifactId>
  <version>3.7.7</version>
</dependency></pre> 
 </div> 
</div> 
<h1 style="text-align:left">使用文档</h1> 
<div style="text-align:left"> 
 <div> 
  <pre>// 生成 jwt 票据，访问请求头设置‘ accessToken=票据内容 ’ 适合前后分离模式单点登录
String jwtToken = SSOToken.create().setId(1).setIssuer("admin").setOrigin(TokenOrigin.HTML5).getToken();

// 解析票据
SSOToken ssoToken = SSOToken.parser(jwtToken);

// Cookie 模式设置
SSOHelper.setCookie(request, response,  new SSOToken().setId(String.valueOf(1)).setIssuer("admin"));

// 权限拦截器类 SSOSpringInterceptor
// 注解不拦截 @Login(action = Action.Skip)
// yml 配置 kisso.config....</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            