
---
title: 'zlt-mp v4.5.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
author: 开源中国
comments: false
date: Mon, 24 May 2021 06:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:left">功能介绍</h1> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a40df48eb5e79bff3622171ee91f4269395.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">更新内容</h2> 
<h3 style="text-align:left">特性/增强</h3> 
<ul> 
 <li> <p>支持<strong>OIDC协议</strong>授权</p> </li> 
 <li> <p>应用管理界面增加ID令牌相关的配置</p> </li> 
 <li> <p>增加oidc协议单点登录样例工程<strong>oidc-sso</strong></p> </li> 
 <li> <p>增加zookeeper工具类<strong>zookeeperTemplate</strong></p> </li> 
 <li> <p>替换默认PasswordEncoder实现类为<strong>DelegatingPasswordEncoder</strong></p> </li> 
 <li> <p>修改文件中心默认依赖为<strong>s3</strong></p> </li> 
 <li> <p>升级spring-boot到<strong>2.3.11.RELEASE</strong></p> </li> 
</ul> 
<h3 style="text-align:left">问题修复</h3> 
<ul> 
 <li> <p>修复token过期时访问网关返回500状态码</p> </li> 
</ul> 
<h3 style="text-align:left">变更语句</h3> 
<pre style="text-align:left"><code><span style="color:#c678dd">Use</span> <span style="color:#98c379">`oauth-center`</span>;
<span style="color:#c678dd">alter</span> <span style="color:#c678dd">table</span> oauth_client_details <span style="color:#c678dd">add</span> support_id_token <span style="color:#e6c07b">tinyint</span>(<span style="color:#d19a66">1</span>) <span style="color:#c678dd">DEFAULT</span> <span style="color:#d19a66">1</span> <span style="color:#c678dd">COMMENT</span> <span style="color:#98c379">'是否支持id_token'</span>;
<span style="color:#c678dd">alter</span> <span style="color:#c678dd">table</span> oauth_client_details <span style="color:#c678dd">add</span> id_token_validity <span style="color:#e6c07b">int</span>(<span style="color:#d19a66">11</span>) <span style="color:#c678dd">DEFAULT</span> <span style="color:#d19a66">60</span> <span style="color:#c678dd">COMMENT</span> <span style="color:#98c379">'id_token有效期'</span>;
</code></pre> 
<p style="text-align:left"> </p> 
<h2 style="text-align:left">内容说明</h2> 
<h3 style="text-align:left">一、支持OIDC协议授权</h3> 
<p style="text-align:left">OIDC是 <code>OpenID Connect</code> 的简称，它在OAuth2上构建了一个身份层，是一个基于OAuth2协议的身份认证标准协议。</p> 
<p style="text-align:left">在使用 <code>授权码模式</code> 或者 <code>简化模式</code> 时，通过在参数 <code>response_type</code> 中增加 <strong>id_token </strong>值即可，例子如下：</p> 
<pre style="text-align:left"><code>http://localhost:9900/api-uaa/oauth/authorize?client_id=zlt&redirect_uri=http://127.0.0.1&response_type=code id_token
</code></pre> 
<p style="text-align:left"> </p> 
<p style="text-align:left"><strong>OIDC协议返回示例</strong>：</p> 
<pre style="text-align:left"><code>&#123;
    <span style="color:#d19a66">"resp_code"</span>: <span style="color:#d19a66">200</span>,
    <span style="color:#d19a66">"resp_msg"</span>: <span style="color:#98c379">"ok"</span>,
    <span style="color:#d19a66">"datas"</span>: &#123;
        <span style="color:#d19a66">"access_token"</span>: <span style="color:#98c379">"d1186597-aeb4-4214-b176-08ec09b1f1ed"</span>,
        <span style="color:#d19a66">"token_type"</span>: <span style="color:#98c379">"bearer"</span>,
        <span style="color:#d19a66">"refresh_token"</span>: <span style="color:#98c379">"37fd65d8-f017-4b5a-9975-22b3067fb30b"</span>,
        <span style="color:#d19a66">"expires_in"</span>: <span style="color:#d19a66">3599</span>,
        <span style="color:#d19a66">"id_token"</span>: <span style="color:#98c379">"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwOi8vemx0MjAwMC5jbiIsImlhdCI6MTYyMTY5NjU4MjYxNSwiZXhwIjoxNjIxNjk2NjQyNjE1LCJzdWIiOiIxIiwibmFtZSI6IueuoeeQhuWRmCIsImxvZ2luX25hbWUiOiJhZG1pbiIsInBpY3R1cmUiOiJodHRwOi8vcGtxdG1uMHAxLmJrdC5jbG91ZGRuLmNvbS_lpLTlg48ucG5nIiwiYXVkIjoiYXBwIiwibm9uY2UiOiJ0NDlicGcifQ.UhsJpHYMWRmny45K0CygXeaASFawqtP2-zgWPDnn0XiBJ6yeiNo5QAwerjf9NFP1YBxuobRUzzhkzRikWGwzramNG9na0NPi4yUQjPNZitX1JzlIA8XSq4LNsuPKO7hS1ALqqiAEHS3oUqKAsjuE-ygt0fN9iVj2LyL3-GFpql0UAFIHhew_J7yIpR14snSh3iLVTmSWNknGu2boDvyO5LWonnUjkNB3XSGD0ukI3UEEFXBJWyOD9rPqfTDOy0sTG_-9wjDEV0WbtJf4FyfO3hPu--bwtM_U0kxRbfLnOujFXyVUStiCKG45wg7iI4Du2lamPJoJCplwjHKWdPc6Zw"</span>
    &#125;
&#125;
</code></pre> 
<p style="text-align:left"> </p> 
<p style="text-align:left"><strong>id_token包含以下内容</strong>：</p> 
<pre style="text-align:left"><code>&#123;
  <span style="color:#d19a66">"iss"</span>: <span style="color:#98c379">"http://zlt2000.cn"</span>,
  <span style="color:#d19a66">"iat"</span>: <span style="color:#d19a66">1621696582615</span>,
  <span style="color:#d19a66">"exp"</span>: <span style="color:#d19a66">1621696642615</span>,
  <span style="color:#d19a66">"sub"</span>: <span style="color:#98c379">"1"</span>,
  <span style="color:#d19a66">"name"</span>: <span style="color:#98c379">"管理员"</span>,
  <span style="color:#d19a66">"login_name"</span>: <span style="color:#98c379">"admin"</span>,
  <span style="color:#d19a66">"picture"</span>: <span style="color:#98c379">"http://xxx/头像.png"</span>,
  <span style="color:#d19a66">"aud"</span>: <span style="color:#98c379">"app"</span>,
  <span style="color:#d19a66">"nonce"</span>: <span style="color:#98c379">"t49bpg"</span>
&#125;
</code></pre> 
<p style="text-align:left"> </p> 
<h3 style="text-align:left">二、应用管理界面增加ID令牌相关的配置</h3> 
<p><img alt src="https://files.mdnice.com/user/514/794bcadf-f8e7-4c7c-ac50-3a1994280cfb.png" referrerpolicy="no-referrer"><img alt src="https://oscimg.oschina.net/oscnet/up-3fb326c57585454518e2a9bc09ddfeb6de8.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p><strong>支持ID令牌</strong>：为是则支持返回id_token</p> </li> 
 <li> <p><strong>ID时效</strong>：为配置id_token的有效时间</p> </li> 
</ul> 
<p style="text-align:left"> </p> 
<h3 style="text-align:left">三、增加zookeeper工具类zookeeperTemplate</h3> 
<p style="text-align:left">依赖：</p> 
<pre style="text-align:left"><code><<span style="color:#e06c75">dependency</span>>
    <<span style="color:#e06c75">groupId</span>>com.zlt</<span style="color:#e06c75">groupId</span>>
    <<span style="color:#e06c75">artifactId</span>>zlt-zookeeper-spring-boot-starter</<span style="color:#e06c75">artifactId</span>>
</<span style="color:#e06c75">dependency</span>>
</code></pre> 
<p style="text-align:left">使用：</p> 
<pre style="text-align:left"><code><span style="color:#61aeee">@Resource</span>
<span style="color:#c678dd">private</span> ZookeeperTemplate zkTemplate;

zkTemplate.createNode(<span style="color:#98c379">"/"</span>, <span style="color:#98c379">"test"</span>);
</code></pre> 
<p style="text-align:left"> </p> 
<h3 style="text-align:left">四、替换默认PasswordEncoder实现类为DelegatingPasswordEncoder</h3> 
<p style="text-align:left">用于同时兼容多种加密方式的密码数据同时存在时的密码校验。</p> 
<p style="text-align:left">修改旧的密码数据的值，添加前缀标识，支持以下三种格式：</p> 
<ul> 
 <li> <p>无前缀</p> </li> 
</ul> 
<pre style="text-align:left"><code>//只支持使用bcrypt方式加密的密码
格式：密码

例如：<span style="color:#d19a66">$2a</span><span style="color:#d19a66">$10</span><span style="color:#d19a66">$EgTOU7PMe</span>.3jaMwFsumdweJcnY3TsTqyuJEdSaSKxdgwYchAwUJ1C
</code></pre> 
<ul> 
 <li> <p>无盐值</p> </li> 
</ul> 
<pre style="text-align:left"><code>格式：&#123;encodingId&#125;密码

例如：&#123;bcrypt&#125;<span style="color:#d19a66">$2a</span><span style="color:#d19a66">$10</span><span style="color:#d19a66">$EgTOU7PMe</span>.3jaMwFsumdweJcnY3TsTqyuJEdSaSKxdgwYchAwUJ1C
</code></pre> 
<ul> 
 <li> <p>有盐值</p> </li> 
</ul> 
<pre style="text-align:left"><code>格式：&#123;encodingId&#125;&#123;salt&#125;密码

例如：&#123;MD5&#125;&#123;5Hstj&#125;0758f7131c6c95c8e3df05e1ac50214c
</code></pre> 
<p style="text-align:left"> </p> 
<h3 style="text-align:left">五、升级zlt-register到2.0.1</h3> 
<p style="text-align:left"><code>zlt-register/nacos</code> 替换为官方最新的 <code>2.0.1</code> 版本</p> 
<blockquote> 
 <p>内容与官网一致，只是方便大家直接使用</p> 
</blockquote> 
<p style="text-align:left"> </p> 
<h2 style="text-align:left"><strong>项目地址</strong></h2> 
<p style="text-align:left">Gitee地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="text-align:left">Github地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="text-align:left">项目文档</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="text-align:left">项目更新日志</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/93623</a></p>
                                        </div>
                                      
</div>
            