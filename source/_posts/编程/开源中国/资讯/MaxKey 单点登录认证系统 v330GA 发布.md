
---
title: 'MaxKey 单点登录认证系统 v3.3.0GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Fri, 21 Jan 2022 09:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; text-align:left"><img alt height="52" src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" width="203" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; text-align:left"><a href="https://gitee.com/dromara/MaxKey/blob/master/README_en.md" target="_blank"><strong>English</strong></a><span> </span>|<span> </span><a href="https://gitee.com/dromara/MaxKey/blob/master/README_zh.md" target="_blank"><strong>中文</strong></a></p> 
<h1>概述</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>MaxKey</strong>单点登录认证系统，谐音马克思的钥匙寓意是最大钥匙,是<strong>业界领先的企业级IAM身份管理和认证产品</strong>,支持OAuth 2.x/OpenID Connect、SAML 2.0、JWT、CAS、SCIM等标准协议，提供<strong>简单、标准、安全和开放</strong>的用户身份管理(IDM)、身份认证(AM)、单点登录(SSO)、RBAC权限管理和资源管理等。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">官方网站<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.maxkey.top" target="_blank"><strong>官网</strong></a><span> </span>|<span> </span><a href="https://maxkeytop.gitee.io/" target="_blank"><strong>官网二线</strong></a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">邮箱email:<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Amaxkeysupport%40163.com" target="_blank">maxkeysupport@163.com</a></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">代码托管<span> </span><a href="https://gitee.com/dromara/MaxKey" target="_blank"><strong>Gitee</strong></a><span> </span>|<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2FMaxKey" target="_blank"><strong>GitHub</strong></a></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><strong>单点登录(Single Sign On）</strong>简称为<strong>SSO</strong>，用户只需要登录认证中心一次就可以访问所有相互信任的应用系统，无需再次登录。</p> 
 <p style="margin-left:0; margin-right:0"><strong>主要功能：</strong></p> 
 <ol> 
  <li>所有应用系统共享一个身份认证系统</li> 
  <li>所有应用系统能够识别和提取ticket信息</li> 
 </ol> 
</blockquote> 
<h1>产品特性</h1> 
<ol> 
 <li>标准协议：</li> 
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
 <li> <p style="margin-left:0; margin-right:0">提供标准的认证接口以便于其他应用集成SSO，安全的移动接入，安全的API、第三方认证和互联网认证的整合。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供用户生命周期管理，支持SCIM 2协议，基于Apache Kafka代理，通过连接器(Connector)实现身份供给同步。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">认证多租户功能，支持集团下多企业独立管理或企业下不同部门数据隔离的，降低运维成本。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">认证中心具有平台无关性、环境多样性，支持Web、手机、移动设备等, 如Apple iOS，Andriod等，将认证能力从B/S到移动应用全面覆盖。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">多种认证机制并存，各应用系统可保留原有认证机制，同时集成认证中心的认证；应用具有高度独立性，不依赖认证中心，又可用使用认证中心的认证，实现单点登录。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">基于Java EE平台，微服务架构，采用Spring、MySQL、Tomcat、Redis、Apache Kafka等开源技术，扩展性强。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">开源、安全、自主可控，许可证 Apache 2.0 License &<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Flicenses.html" target="_blank">MaxKey版权声明</a>。</p> </li> 
</ol> 
<h1>界面</h1> 
<p style="color:#40485b; text-align:left"><strong>MaxKey认证</strong></p> 
<p style="color:#40485b; text-align:left">登录界面<span> </span></p> 
<p style="color:#40485b; text-align:left"><img src="https://gitee.com/dromara/MaxKey/raw/master/images/maxkey_login.png?raw=true" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; text-align:left">主界面</p> 
<p style="color:#40485b; text-align:left"><span> </span><img src="https://gitee.com/dromara/MaxKey/raw/master/images/maxkey_index.png?raw=true" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; text-align:left"> </p> 
<h1>下载</h1> 
<p style="color:#40485b; text-align:left">当前版本百度网盘下载,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Fdownload.html" target="_blank"><span> </span>历史版本</a></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>版本</th> 
   <th>日期</th> 
   <th>Docker</th> 
   <th>网盘</th> 
   <th>网盘提取码</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">v 3.3.0 GA</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022/01/21</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fhub.docker.com%2Fu%2Fmaxkeytop" target="_blank">链接</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F1BV9K1ki4TnV8R2Fddaqx7w" target="_blank">下载</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><strong>mxk9</strong></td> 
  </tr> 
 </tbody> 
</table> 
<h1>Roadmap</h1> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
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
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OAuth 2.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q1</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">React, and Ant Design</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q2</td> 
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
<h1>版本发行说明</h1> 
<p><span style="background-color:#ffffff; color:#24292e">MaxKey v 3.3.0 GA 2022/01/21<br>     *(MAXKEY-220101) 机构管理配置管理<br>     *(MAXKEY-220102) 应用系统名称后台配置及国际化支持<br>     *(MAXKEY-220103) 初步实现国际化存储在数据库<br>     *(MAXKEY-220104) 租户管理邮箱地址<br>     *(MAXKEY-220105) 租户管理短信网关<br>     *(MAXKEY-220106) 租户管理LDAP配置<br>     *(MAXKEY-220107) 官方网站增加Dromara标识<br>     *(MAXKEY-220108) LDAP认证从租户读取配置<br>     *(MAXKEY-220109) 租户管理社交账号<br>     *(MAXKEY-220110) 社交账号自动识别http,https<br>     *(MAXKEY-220111) 增加prometheus支持<br>     *(MAXKEY-220112) 增加find和findOne的方法，可根据where的过滤条件查询数据<br>     *(MAXKEY-220113) log4j日志pattern调整 <br>     *(MAXKEY-220114) 数据库方法统一命名<br>     *(MAXKEY-220115) 修复新增应用oauth2协议 多租户新增bug<br>     *(MAXKEY-220116) Logger统一使用slf4j<br>     *(MAXKEY-220117) maxkey-synchronizers-dingding改为maxkey-synchronizers-dingtalk<br>     *(MAXKEY-220118) org.maxkey.persistence.db调整为org.maxkey.persistence.repository<br>     *(MAXKEY-220119) org.maxkey.constants下的类统一以Consts开头<br>     *(MAXKEY-220120) 认证协议返回的数据统一增加机构institution<br>     *(MAXKEY-220121) 机构institution，使用instid作为租户标识，对应instance(实例)<br>     *(MAXKEY-220122) 增加mxk_inst cookie，代表当前登录的租户编号<br>     *(MAXKEY-220123) 修复钉钉同步器bug<br>     *(MAXKEY-220124) 修复LDAP同步器bug<br>     *(MAXKEY-220125) 修复企业微信同步器bug<br>     *(MAXKEY-220126) 增加在线集成指南<br>     *(MAXKEY-220127) 官方网站更新和优化<br>     *(MAXKEY-220128) opensaml的jar存放在本地，加速构建的效率<br>     *(MAXKEY-220129) readme完善<br>     *(MAXKEY-220130) 依赖jar引用、更新和升级<br>         log4j           2.17.1<br>         spring          5.3.15<br>         springBoot      2.6.1<br>         springbootadmin 2.6.0<br>         xmlbeans        5.0.2<br>         poi             5.1.0<br>         jedis           3.8.0<br>         mybatis         3.5.9<br>         mybatis-jpa-extra 2.7</span></p>
                                        </div>
                                      
</div>
            