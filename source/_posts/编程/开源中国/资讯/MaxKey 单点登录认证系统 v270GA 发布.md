
---
title: 'MaxKey 单点登录认证系统 v2.7.0GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 09:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left"><img alt height="52" src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" width="203" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><a href="https://gitee.com/maxkeytop/MaxKey/blob/master/README_en.md" target="_blank"><strong>English</strong></a> | <a href="https://gitee.com/maxkeytop/MaxKey/blob/master/README_zh.md" target="_blank"><strong>中文</strong></a></p> 
<h1>概述</h1> 
<p style="text-align:left"><strong>MaxKey</strong>单点登录认证系统(Single Sign On System)，MaxKey中文谐音<strong>马克思的钥匙</strong>寓意是最大钥匙,是<strong>业界领先的企业级开源IAM身份管理和身份认证产品</strong>,国内开源IAM第一品牌；支持OAuth 2.0/OpenID Connect、SAML 2.0、JWT、CAS、SCIM等标准协议，提供<strong>简单、标准、安全和开放</strong>的用户身份管理(IDM)、身份认证(AM)、单点登录(SSO)、RBAC权限管理和资源管理等。</p> 
<p style="text-align:left">官方网站 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.maxkey.top%2F" target="_blank"><strong>官网</strong></a> | <a href="https://maxkeytop.gitee.io/" target="_blank"><strong>官网二线</strong></a></p> 
<p style="text-align:left">邮箱email: <strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Amaxkeysupport%40163.com" target="_blank">maxkeysupport@163.com</a></strong></p> 
<p style="text-align:left">代码托管 <strong><a href="https://gitee.com/dromara/MaxKey" target="_blank">Gitee</a> </strong>| <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2FMaxKey" target="_blank"><strong>GitHub</strong></a> </p> 
<p style="text-align:left">什么是<strong>单点登录(Single Sign On）</strong>，简称为<strong>SSO</strong>？</p> 
<p style="text-align:left">用户只需要登录认证中心一次就可以访问所有相互信任的应用系统，无需再次登录。</p> 
<p style="text-align:left">主要功能：</p> 
<ol> 
 <li> <p>所有应用系统共享一个身份认证系统</p> </li> 
 <li> <p>所有应用系统能够识别和提取ticket信息</p> </li> 
</ol> 
<h1>产品特性</h1> 
<ol> 
 <li>标准认证协议：</li> 
</ol> 
<table cellspacing="0" style="width:835px"> 
 <tbody> 
  <tr> 
   <th>序号</th> 
   <th>协议</th> 
   <th>支持</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">1.1</td> 
   <td style="border-color:#dfe2e5">OAuth 2.0/OpenID Connect</td> 
   <td style="border-color:#dfe2e5">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1.2</td> 
   <td style="border-color:#dfe2e5">SAML 2.0</td> 
   <td style="border-color:#dfe2e5">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1.3</td> 
   <td style="border-color:#dfe2e5">JWT</td> 
   <td style="border-color:#dfe2e5">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1.4</td> 
   <td style="border-color:#dfe2e5">CAS</td> 
   <td style="border-color:#dfe2e5">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1.5</td> 
   <td style="border-color:#dfe2e5">FormBased</td> 
   <td style="border-color:#dfe2e5">中</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1.6</td> 
   <td style="border-color:#dfe2e5">TokenBased(Post/Cookie)</td> 
   <td style="border-color:#dfe2e5">中</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1.7</td> 
   <td style="border-color:#dfe2e5">ExtendApi</td> 
   <td style="border-color:#dfe2e5">低</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">1.8</td> 
   <td style="border-color:#dfe2e5">EXT</td> 
   <td style="border-color:#dfe2e5">低</td> 
  </tr> 
 </tbody> 
</table> 
<ol> 
 <li>登录支持</li> 
</ol> 
<table cellspacing="0" style="width:835px"> 
 <tbody> 
  <tr> 
   <th>序号</th> 
   <th>登录方式</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">2.1</td> 
   <td style="border-color:#dfe2e5">动态验证码 字母/数字/算术</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2.2</td> 
   <td style="border-color:#dfe2e5">双因素认证</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2.3</td> 
   <td style="border-color:#dfe2e5">短信认证 腾讯云短信/阿里云短信/网易云信</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2.4</td> 
   <td style="border-color:#dfe2e5">登录易/Google/Microsoft Authenticator/FreeOTP/支持TOTP或者HOTP</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2.5</td> 
   <td style="border-color:#dfe2e5">Kerberos/SPNEGO/AD域</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2.6</td> 
   <td style="border-color:#dfe2e5"><span style="background-color:#f6f8fa; color:#40485b">OpenLDAP/ActiveDirectory/标准LDAP服务器</span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">2.7</td> 
   <td style="border-color:#dfe2e5">社交账号 微信/QQ/微博/钉钉/Google/Facebook/其他</td> 
  </tr> 
 </tbody> 
</table> 
<ol> 
 <li> <p>提供标准的认证接口以便于其他应用集成SSO，安全的移动接入，安全的API、第三方认证和互联网认证的整合。</p> </li> 
 <li> <p>提供用户生命周期管理，支持SCIM 2协议，基于Apache Kafka代理，通过连接器(Connector)实现身份供给同步。</p> </li> 
 <li> <p>认证中心具有平台无关性、环境多样性，支持Web、手机、移动设备等, 如Apple iOS，Andriod等，将认证能力从B/S到移动应用全面覆盖。</p> </li> 
 <li> <p>多种认证机制并存，各应用系统可保留原有认证机制，同时集成认证中心的认证；应用具有高度独立性，不依赖认证中心，又可用使用认证中心的认证，实现单点登录。</p> </li> 
 <li> <p>基于Java平台开发，采用Spring、MySQL、Tomcat、Apache Kafka、Redis等开源技术，支持微服务，扩展性强。</p> </li> 
 <li> <p>开源、安全、自主可控，许可证 Apache 2.0 License & <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Flicenses.html" target="_blank">MaxKey版权声明</a>。</p> </li> 
</ol> 
<h1>界面</h1> 
<p style="text-align:left"><strong>MaxKey认证</strong></p> 
<p style="text-align:left">登录界面 </p> 
<p style="text-align:left"><img alt height="900" src="https://oscimg.oschina.net/oscnet/up-f0ac594bd8700659eedc0ca025969f5819e.png" width="1686" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">主界面</p> 
<p style="text-align:left"> <img alt height="903" src="https://oscimg.oschina.net/oscnet/up-3d5e1411e260cd3420a2ab4f56e8eefb7ba.png" width="1530" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"> </p> 
<h1>下载</h1> 
<p style="text-align:left">当前版本百度网盘下载,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Fdownload.html" target="_blank"> 历史版本</a></p> 
<table cellspacing="0" style="width:835px"> 
 <tbody> 
  <tr> 
   <th>版本</th> 
   <th>日期</th> 
   <th>下载地址</th> 
   <th>提取码</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">v 2.7.0 GA</td> 
   <td style="border-color:#dfe2e5">2021/04/15</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1shP3ld63r39ugyZCG5f1lQ" target="_blank">链接下载</a></td> 
   <td style="border-color:#dfe2e5"><strong>hf73</strong></td> 
  </tr> 
 </tbody> 
</table> 
<h1>Roadmap</h1> 
<p style="text-align:left">1.零信任场景整合</p> 
<p style="text-align:left">2.MaxKey Cloud(微服务版)-2021年</p> 
<h2>版本说明</h2> 
<p><span style="background-color:#ffffff; color:#24292e">MaxKey v 2.7.0 GA    2021/04/15<br>     *(MAXKEY-210301)  加入Dromara开源组织，官方网站的优化，文档优化<br>     *(MAXKEY-210302)  BootJar，Docker，Standard三种打包方式的配置优化<br>     *(MAXKEY-210303)  openldap,activedirectory密码验证支持<br>     *(MAXKEY-210304)  数据库访问注释由@Service改为<a href="https://my.oschina.net/u/3055569" target="_blank">@Repository</a><br>     *(MAXKEY-210305)  cas logout优化支持<br>     *(MAXKEY-210306)  CAS单点注销及返回数据类型适配器的优化<br>     *(MAXKEY-210307)  CAS返回数据类重构<br>     *(MAXKEY-210308)  CAS地址优化统一配置到常量类CasConstants<br>     *(MAXKEY-210309)  注销空指针异常BUG<br>     *(MAXKEY-210310)  OAuth2地址优化统一配置常量类OAuth2Constants<br>     *(MAXKEY-210311)  OAuth2 Token多次调用时认证转换的BUG<br>     *(MAXKEY-210312)  ExtendApi标准优化<br>     *(MAXKEY-210313)  增加基于时间签名的ExtendApi适配器<br>     *(MAXKEY-210314)  返回数据Constants整合<br>     *(MAXKEY-210315)  扩展数据配置优化<br>     *(MAXKEY-210316)  LDAP和MS AD固定属性Constants<br>     *(MAXKEY-210317)  SpringSecurity OAuth 2客户端登录适配<br>     *(MAXKEY-210318)  移除Desktop的支持，后续可以开发FormBase的适配器定制<br>     *(MAXKEY-210319)  application.properties profiles的优化，不同环境启动更加简单<br>     *(MAXKEY-210320)  删除maxkey.properties，配置整合到 application.properties<br>     *(MAXKEY-210321)  增加适配器注册功能，在配置应用时只需选择对应的适配器<br>     *(MAXKEY-210322)  增加Synchronizer接口同步的功能<br>     *(MAXKEY-210323)  增加TimeBased OTP接口支持<br>     *(MAXKEY-210324)  XSS安全防护功能<br>     *(MAXKEY-210325)  禅道项目管理系统单点登录适配<br>     *(MAXKEY-210326)  GitLab单点登录适配<br>     *(MAXKEY-210327)  云速邮箱单点登录适配<br>     *(MAXKEY-210328)  JumpServer开源堡垒机单点登录适配<br>     *(MAXKEY-210329)  华为云单点登录适配<br>     *(MAXKEY-210330)  Jenkins单点登录适配<br>     *(MAXKEY-210331)  通知公告简单功能实现<br>     *(MAXKEY-210332)  查询参数优化<br>     *(MAXKEY-210333)  SDK优化<br>     *(MAXKEY-210334)  依赖jar引用、更新和升级<br>         log4j         2.14.1<br>         spring        5.3.6<br>         springBoot  2.4.4<br>         springSecurity 5.4.6<br>         tomcat        9.0.44</span></p>
                                        </div>
                                      
</div>
            