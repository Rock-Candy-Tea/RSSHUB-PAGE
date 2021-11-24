
---
title: 'kisso 3.8.1 发布新增 SameSite 防跨站 CSRF 攻击'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://static.oschina.net/uploads/space/2015/1122/121717_Rl6y_241218.png'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 10:20:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://static.oschina.net/uploads/space/2015/1122/121717_Rl6y_241218.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><img alt src="https://cors.zfour.workers.dev/?http://static.oschina.net/uploads/space/2015/1122/121717_Rl6y_241218.png" referrerpolicy="no-referrer"></strong></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left"><span style="color:#e53333">kisso</span><span> </span><span style="color:#ffe500"> </span><span style="color:#b8d100">=<span> </span></span> <span style="color:#009900">cookie<span> </span></span><span style="color:#ee33ee">sso </span></h4> 
<h4 style="margin-left:0px; margin-right:0px; text-align:left">基于 Cookie 的 SSO 中间件，它是一把快速开发 java Web 登录系统（SSO）的瑞士军刀。欢迎大家使用<span> </span><span style="color:#e53333"><strong>ki</strong><span style="color:#009900"><strong>ss</strong></span></span><span style="color:#009900"><strong>o</strong></span><strong> </strong><strong>!! </strong></h4> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">前后分离可选：请求 Header 票据模式, 请求 Cookie 模式</p> 
</blockquote> 
<h3>常见安全策略</h3> 
<div> 
 <h3>Secure</h3> 
 <p>标记为 Secure 的 Cookie 只应通过被HTTPS协议加密过的请求发送给服务端。使用 HTTPS 安全协议，可以保护 Cookie 在浏览器和 Web 服务器间的传输过程中不被窃取和篡改。</p> 
 <h3>HTTPOnly</h3> 
 <p>设置 HTTPOnly 属性可以防止客户端脚本通过 document.cookie 等方式访问 Cookie，有助于避免 XSS 攻击。</p> 
 <h3>SameSite</h3> 
 <p>SameSite 也是这篇博客的主体，首先我们来看看这个参数的作用。<br> SameSite 属性可以让 Cookie 在跨站请求时不会被发送，从而可以阻止跨站请求伪造攻击（CSRF）。至于什么是CSRF这里就不具体说了。<br> SameSite 可以有下面三种值：<br> 1、Strict仅允许一方请求携带 Cookie，即浏览器将只发送相同站点请求的 Cookie，即当前网页 URL 与请求目标 URL 完全一致。<br> 2、Lax允许部分第三方请求携带 Cookie<br> 3、None无论是否跨站都会发送 Cookie<br> 造成现在无法获取cookie是因为之前默认是 None 的，Chrome80 后默认是 Lax</p> 
 <p><img height="410" src="https://oscimg.oschina.net/oscnet/up-8f5dd1aca8f9acdc1f09ec012be3a572920.png" width="1102" referrerpolicy="no-referrer"></p> 
</div> 
<h2><strong>KISSO 安全配置</strong></h2> 
<pre><span style="color:#cc7832">kisso</span>:
  <span style="color:#cc7832">config</span>:
    <em># </em><em>开启</em><em> https </em><em>有效，传输更安全
</em><em>    </em><span style="color:#cc7832">cookie-secure</span>: <span style="color:#cc7832">true
</span><span style="color:#cc7832">    </span><em># </em><em>防止</em><em> XSS </em><em>防止脚本攻击
</em><em>    </em><span style="color:#cc7832">cookie-http-only</span>: <span style="color:#cc7832">true
</span><span style="color:#cc7832">    </span><em># </em><em>防止</em><em> CSRF </em><em>跨站攻击
</em><em>    </em><span style="color:#cc7832">cookie-same-site</span>: Lax
    <em># </em><em>加密算法</em><em> RSA
</em><em>    </em><span style="color:#cc7832">sign-algorithm</span>: RS512
    ...
</pre> 
<h1 style="margin-left:0; margin-right:0; text-align:left">使用文档</h1> 
<div style="text-align:left"> 
 <div> 
  <pre><span>// 生成 jwt 票据，访问请求头设置‘ accessToken=票据内容 ’ 适合前后分离模式单点登录</span>
<span>String jwtToken = SSOToken.create().setId(1).setIssuer("admin").setOrigin(TokenOrigin.HTML5).getToken();</span>

<span>// 解析票据</span>
<span>SSOToken ssoToken = SSOToken.parser(jwtToken);</span>

<span>// Cookie 模式设置</span>
<span>SSOHelper.setCookie(request, response,  new SSOToken().setId(String.valueOf(1)).setIssuer("admin"));</span>

<span>// 登录权限拦截器类 SSOSpringInterceptor</span>
<span>// 注解不拦截 @LoginIgnore</span>
<span>// yml 配置 kisso.config....</span></pre> 
 </div> 
</div> 
<ul> 
 <li>Spring Boot</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span>@ControllerAdvice</span>
<span>@Configuration</span>
<span>public class WebConfig extends WebServiceConfigurer &#123;</span>

<span>    @Override</span>
<span>    public void addInterceptors(InterceptorRegistry registry) &#123;</span>
<span>        // SSO 授权拦截器</span>
<span>        SSOSpringInterceptor ssoInterceptor = new SSOSpringInterceptor();</span>
<span>        ssoInterceptor.setHandlerInterceptor(new LoginHandlerInterceptor());</span>
<span>        registry.addInterceptor(ssoInterceptor).addPathPatterns("/**").excludePathPatterns("/v1/sso/**");</span>
<span>    &#125;</span>
<span>&#125;</span>

</pre> 
 </div> 
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:left">切换 RS512 算法</h1> 
<ul> 
 <li>1，配置算法 kisso.config.sign-algorithm = RS512</li> 
 <li>2，配置私钥公钥证书，默认放置 resources 目录即可</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span>// RSA 密钥，配置参数 kisso.config.rsa-jks-store</span>
<span>// 其它参数 CN=Server,OU=Unit,O=Organization,L=City,S=State,C=US</span>
<span>// RSA 生成 jks 密钥</span>
<span>$ keytool -genkeypair -alias jwtkey -keyalg RSA -dname "CN=llt" -keypass keypassword -keystore key.jks -storepass jkspassword</span>

<span>// RSA 生成证书</span>
<span>// RSA 公钥，配置参数 kisso.config.rsa-cert-store</span>
<span>$ keytool -export -alias jwtkey -file public.cert -keystore key.jks -storepass jksp</span>
</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            