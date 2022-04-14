
---
title: 'Mall4j-2.0 发布啦~'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-13fa9c7f53fafedd5a5b834159f664eacf0.png'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 01:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-13fa9c7f53fafedd5a5b834159f664eacf0.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start"><span>Mall4j开源登录重构啦！</span></h2> 
<p><img height="731" src="https://oscimg.oschina.net/oscnet/up-13fa9c7f53fafedd5a5b834159f664eacf0.png" width="1510" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此次开源登录重构更新了不少内容，详情如下：</span></p> 
<ol start style="margin-left:.8em; margin-right:.8em"> 
 <li> <p><span>去除Spring OAuth2使用自研的Token代替授权</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>去除</span><span><code>spring-security-oauth2</code></span><span>相关依赖，自己写</span><span><code>TokenStore</code></span><span>来对Token进行管理，包括存储token并返回，刷新token，清除token，校验token等方法</span></p> </li> 
 <li> <p><span>使用Controller代替Filter进行登录授权</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>移除原本</span><span><code>LoginAuthenticationFilter</code></span><span>之类的登录过滤，使用</span><span><code>AdminLoginController</code></span><span>和</span><span><code>LoginController</code></span><span>进行登录授权</span></p> </li> 
 <li> <p><span>保留Spring Security作为Web防火墙，不使用security的认证授权登录</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>使用</span><span><code>MallWebSecurityConfigurerAdapter</code></span><span>来实现防火墙功能</span></p> </li> 
 <li> <p><span>将Token相关逻辑重新抽取，阅读起来简单易懂</span></p> 
  <ol start style="margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>将</span><span><code>yami-shop-security</code></span><span>模块拆分成三大块，分别为admin，api，common模块</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>移除原</span><span><code>com.yami.shop.security.exception</code></span><span>下的异常，使用</span><span><code>YamiShopBindException</code></span><span>进行统一处理</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>统一了</span><span><code>SecurityUtils</code></span><span>中获取普通用户和平台用户信息的代码</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>移除原</span><span><code>yami-shop-api</code></span><span>模块下</span><span><code>com.yami.shop.api.security</code></span><span>的代码，同时移除原</span><span><code>yami-shop-admin</code></span><span>模块下</span><span><code>com.yami.shop.admin.security</code></span><span>的代码</span></p> </li> 
  </ol> </li> 
 <li> <p><span>前端登录加密</span></p> 
  <ol start style="margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>前端使用密钥对时间戳+密码组成的字符串进行ASE加密</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>后台在</span><span><code>com.yami.shop.security.common.manager.PasswordManager</code></span><span>的</span><span><code>decryptPassword</code></span><span>方法对前端传过来的密码进行解密</span></p> </li> 
  </ol> </li> 
 <li> <p><span>后台登录验证码更新</span></p> 
  <ol start style="margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>引入captcha做验证码功能</span></p> <pre style="text-align:left"><span><span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>com.anji-plus<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>captcha<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.3.0<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span></span>
<span><span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span></pre> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span><code>yami-shop-security/yami-shop-security-common/src/main/resources/captcha</code></span><span>新增资源文件</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>使用</span><span><code>CaptchaConfig</code></span><span>存储底图到redis中，</span><span><code>CaptchaCacheServiceRedisImpl</code></span><span>适配验证码在redis中的储存</span></p> </li> 
  </ol> </li> 
 <li> <p><span>使用Kryo序列化替代原本的Fst序列化</span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>为了兼容token和验证码相关序列化逻辑，此番Mall4j使用Kryo替代了原本的fst</span></p> 
  <ol start style="margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>kryo版本：4.0.2</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>移除原本的</span><span><code>com.yami.shop.common.serializer.redis.FstRedisSerializer</code></span><span>，新增了</span><span><code>com.yami.shop.common.serializer.redis.KryoRedisSerializer</code></span><span>做redis序列化</span></p> </li> 
  </ol> </li> 
 <li> <p><span>更新了版本依赖</span></p> 
  <ol start style="margin-left:0; margin-right:0"> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>spring-boot：2.3.12.RELEASE</span></p> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>升级了一系列第三方依赖库</span></p> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:.5rem; margin-right:0"><span>hutool：5.7.15</span></p> </li> 
     <li> <p style="margin-left:.5rem; margin-right:0"><span>swagger-bootstrap：1.9.6</span></p> </li> 
     <li> <p style="margin-left:.5rem; margin-right:0"><span>redisson：3.12.5</span></p> 
      <ul style="margin-left:0; margin-right:0"> 
       <li> <p style="margin-left:.5rem; margin-right:0"><span>由于</span><span><strong><span>redisson版本提升</span></strong></span><span>，相关配置文件也相对应更新了，删除了原本</span><span><code>singleServerConfig</code></span><span>的</span><span><code>pingTimeout</code></span><span>、</span><span><code>reconnectionTimeout</code></span><span>、</span><span><code>failedAttempts</code></span><span>这三个配置</span></p> </li> 
       <li> <p style="margin-left:.5rem; margin-right:0"><span>序列化由原本的</span></p> <pre style="text-align:left"><span><span style="color:#221199">codec</span><span style="color:#555555">:</span></span>
<span><span style="color:#221199">  class</span><span style="color:#555555">: </span>com.yami.shop.common.serializer.redisson.FstCodec</span></pre> <p style="margin-left:.5rem; margin-right:.5rem"><span>修改为</span></p> <pre style="text-align:left"><span><span style="color:#221199">codec</span><span style="color:#555555">:</span></span>
<span><span style="color:#221199">  class</span><span style="color:#555555">: </span>org.redisson.codec.KryoCodec</span></pre> </li> 
      </ul> </li> 
    </ul> </li> 
   <li> <p style="margin-left:.5rem; margin-right:0"><span>新增了版本依赖</span></p> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:.5rem; margin-right:0"><span>transmittable-thread-local：2.12.1</span></p> </li> 
    </ul> <p style="margin-left:.5rem; margin-right:.5rem"> </p> </li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">相关截图</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">1. 后台截图</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/1110/143738_88a8a1e6_5094767.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2. 移动端截图</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/1110/145209_2ec1ad04_5094767.png" referrerpolicy="no-referrer"></p> 
<div style="text-align:start"> 
 <h3 style="margin-left:0; margin-right:0">相关链接</h3> 
</div> 
<div style="text-align:start"> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>mall4j商城系统 的详细介绍：<a href="https://www.oschina.net/p/mall4j" target="_blank">点击查看</a></li> 
  <li>mall4j商城系统 的下载地址：<a href="https://gitee.com/gz-yami/mall4j" target="_blank">点击下载</a></li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            