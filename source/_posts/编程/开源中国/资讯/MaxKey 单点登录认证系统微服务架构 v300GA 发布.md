
---
title: 'MaxKey 单点登录认证系统微服务架构 v3.0.0GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 09:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; text-align:left"><img alt height="52" src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" width="203" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; text-align:left"><a href="https://gitee.com/dromara/MaxKey/blob/master/README_en.md" target="_blank"><strong>English</strong></a><span> </span>|<span> </span><a href="https://gitee.com/dromara/MaxKey/blob/master/README_zh.md" target="_blank"><strong>中文</strong></a></p> 
<h1>概述</h1> 
<p style="color:#40485b; text-align:left"><strong>MaxKey</strong>单点登录认证系统，谐音<strong>马克思的钥匙</strong>寓意是最大钥匙,是<strong>业界领先的企业级IAM身份管理和认证产品</strong>,国内开源IAM第一品牌；支持OAuth 2.0/OpenID Connect、SAML 2.0、JWT、CAS、SCIM等标准协议，提供<strong>简单、标准、安全和开放</strong>的用户身份管理(IDM)、身份认证(AM)、单点登录(SSO)、RBAC权限管理和资源管理等。</p> 
<p style="color:#40485b; text-align:left">官方网站<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.maxkey.top%2F" target="_blank"><strong>官网</strong></a><span> </span>|<span> </span><a href="https://maxkeytop.gitee.io/" target="_blank"><strong>官网二线</strong></a></p> 
<p style="color:#40485b; text-align:left">邮箱email:<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Amaxkeysupport%40163.com" target="_blank">maxkeysupport@163.com</a></strong></p> 
<p style="color:#40485b; text-align:left">代码托管<span> </span><a href="https://gitee.com/dromara/MaxKey" target="_blank"><strong>码云(Gitee)</strong></a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2FMaxKey" target="_blank"><strong>GitHub</strong></a></p> 
<p style="color:#40485b; text-align:left"><strong>单点登录(Single Sign On）</strong>简称为<strong>SSO，</strong>用户只需要登录认证中心一次就可以访问所有相互信任的应用系统，无需再次登录。</p> 
<p style="color:#40485b; text-align:left">主要功能：</p> 
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
  <tr> 
   <td style="border-color:#dfe2e5">2.8</td> 
   <td style="border-color:#dfe2e5"><span style="background-color:#f6f8fa; color:#40485b">扫码登录</span> <span style="background-color:#f6f8fa; color:#40485b">企业微信/钉钉扫码登录</span></td> 
  </tr> 
 </tbody> 
</table> 
<ol> 
 <li> <p>提供标准的认证接口以便于其他应用集成SSO，安全的移动接入，安全的API、第三方认证和互联网认证的整合。</p> </li> 
 <li> <p>提供用户生命周期管理，支持SCIM 2协议，基于Apache Kafka代理，通过连接器(Connector)实现身份供给同步。</p> </li> 
 <li> <p>认证中心具有平台无关性、环境多样性，支持Web、手机、移动设备等, 如Apple iOS，Andriod等，将认证能力从B/S到移动应用全面覆盖。</p> </li> 
 <li> <p>多种认证机制并存，各应用系统可保留原有认证机制，同时集成认证中心的认证；应用具有高度独立性，不依赖认证中心，又可用使用认证中心的认证，实现单点登录。</p> </li> 
 <li> <p>基于Java EE平台，采用Spring、MySQL、Tomcat、Apache Kafka、Redis等开源技术，微服务架构，扩展性强。</p> </li> 
 <li> <p>开源、安全、自主可控，许可证 Apache 2.0 License &<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Flicenses.html" target="_blank">MaxKey版权声明</a>。</p> </li> 
</ol> 
<h1>界面</h1> 
<p style="color:#40485b; text-align:left"><strong>MaxKey认证</strong></p> 
<p style="color:#40485b; text-align:left">登录界面<span> </span></p> 
<p style="color:#40485b; text-align:left"><img alt height="605" src="https://oscimg.oschina.net/oscnet/up-9bf25b2f0d96d148db8bcaa22428a191584.png" width="1152" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; text-align:left">主界面</p> 
<p style="color:#40485b; text-align:left"><span> <img alt height="1243" src="https://oscimg.oschina.net/oscnet/up-af08ebec3680923e9c449076b4a164c878f.png" width="1436" referrerpolicy="no-referrer"></span></p> 
<p style="color:#40485b; text-align:left"> </p> 
<h1>下载</h1> 
<p style="color:#40485b; text-align:left">当前版本百度网盘下载,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Fdownload.html" target="_blank"><span> </span>历史版本</a></p> 
<table cellspacing="0" style="width:835px"> 
 <tbody> 
  <tr> 
   <th>版本</th> 
   <th>日期</th> 
   <th>Docker</th> 
   <th>下载地址</th> 
   <th>提取码</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">v 3.0.0 GA</td> 
   <td style="border-color:#dfe2e5">2021/09/29</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fu%2Fmaxkeytop" target="_blank">链接</a></td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1UtEgLD1Pz7FQXZePZaP9Tw" target="_blank">链接下载</a></td> 
   <td style="border-color:#dfe2e5"><strong>mxk9</strong></td> 
  </tr> 
 </tbody> 
</table> 
<h1>Roadmap</h1> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:835px; word-break:initial; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>序号</th> 
   <th>计划</th> 
   <th>时间</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Maxkey-Cloud (micro service support)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021Q3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Zero trust scenario integration</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021Q4</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">React, and Ant Design</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021Q4</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OAuth 2.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">5</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OpenID Connect optimize</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q2</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">6</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Java 17+</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">7</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Jakarta EE 9+</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">8</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Framework 6</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q4</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">9</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Boot 3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q4</td> 
  </tr> 
 </tbody> 
</table> 
<h2>版本发行说明</h2> 
<p><span style="background-color:#ffffff; color:#24292e">MaxKey v 3.0.0 GA 2021/09/29<br>     *(MAXKEY-210701) 好雨科技Rainbond适配，实现基于Rainbond应用商店的快速部署<br>     *(MAXKEY-210702) 制定MaxKey技术路线图<br>     *(MAXKEY-210703) CHINER元数建模构建MaxKEY ER模型完善，数据库字段说明完善<br>     *(MAXKEY-210704) Nacos配置中心支持，可选支持本地和Nacos配置中心配置，配置更加灵活<br>     *(MAXKEY-210705) springcloud &springcloud alibaba微服务支持<br>     *(MAXKEY-210706) spring cloud gateway支持<br>     *(MAXKEY-210707) application.properties参数调整和优化，支持外部Docker及环境变量的配置<br>     *(MAXKEY-210708) 同步器定时任务功能优化<br>     *(MAXKEY-210709) mgt增加会话管理功能<br>     *(MAXKEY-210710) mgt报表功能优化<br>     *(MAXKEY-210711) SAML ID调整为MXK_开头，修复类型匹配的bug，增加常用的用户字段<br>     *(MAXKEY-210712) JWT单点登录的权限控制，修复bug<br>     *(MAXKEY-210713) Gradle升级7.2<br>     *(MAXKEY-210714) Gradle 标准、JAR、Docker编译打包脚本优化<br>     *(MAXKEY-210715) Shell启动脚本优化<br>     *(MAXKEY-210716) 新增MySql Docker支持及初始化脚本<br>     *(MAXKEY-210717) Readme优化，增加MaxKey Docker的仓库地址<br>     *(MAXKEY-210718) 产品介绍pdf的优化<br>     *(MAXKEY-210719) mgt批量删除的优化<br>     *(MAXKEY-210720) Jira SAML集成指南<br>     *(MAXKEY-210721) 官方网站内容的优化，增加同类产品的比较，用户构建指南，完善集成应用列表<br>     *(MAXKEY-210722) 日志信息的完善，包括登录过程日志，初始化日志，单点登录日志等<br>     *(MAXKEY-210723) mgt登录错误提示信息<br>     *(MAXKEY-210724) 警告提示信息修复<br>     *(MAXKEY-210725) 工具类增强和优化<br>     *(MAXKEY-210726) 登录认证优化，增加密码策略应用和验证<br>     *(MAXKEY-210727) CAS登录中参数回传的修复，增加'#'停止符的优化<br>     *(MAXKEY-210728) StringUtils优化，直接继承org.apache.commons.lang3.StringUtils，增加自有逻辑<br>     *(MAXKEY-210729) 依赖jar引用、更新和升级<br>         spring              5.3.10<br>         springBoot          2.5.5<br>         springkafka         2.7.7<br>         spring-cloud        3.0.4<br>         springcloudalibabacspl 1.8.2<br>         mybatis-jpa-extra   2.5<br>         tomcat              9.0.53<br>         kafkaclients        2.8.1<br>         jibGradlePlugin     3.1.4<br>         gson                2.8.8<br>         mysqlconnector      8.0.26<br>         jedis               3.7.0<br>         ehcache             3.9.6<br>         nacos               2.0.3<br>         jacksonVersion      2.12.5<br>         httpasyncclient     4.1.4<br>         bouncycastle        1.69<br>         JustAuth            1.16.4</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            