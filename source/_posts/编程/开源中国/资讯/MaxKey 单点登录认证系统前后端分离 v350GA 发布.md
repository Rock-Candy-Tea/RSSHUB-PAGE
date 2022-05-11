
---
title: 'MaxKey 单点登录认证系统前后端分离 v3.5.0GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Wed, 11 May 2022 09:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="margin-left:0; margin-right:0; text-align:left">研发历程</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#000000">三年磨一剑，3.5.0GA 历时半载，MaxKey 开源 3 年，团队使用 Ant Design UI 设计，基于 Ant Design of Angular 前端技术进行重构，与此同时 3.3.x 将继续研发和提供技术支持。</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="52" src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" width="203" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dromara/MaxKey/blob/master/README_en.md" target="_blank"><strong>English</strong></a><span> </span>|<span> </span><a href="https://gitee.com/dromara/MaxKey/blob/master/README_zh.md" target="_blank"><strong>中文</strong></a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">概述</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>MaxKey</strong><span> </span>单点登录认证系统，谐音马克思的钥匙寓意是最大钥匙，是<strong>业界领先的 IAM 身份管理和认证产品</strong><span> </span>, 支持 OAuth 2.x/OpenID Connect、SAML 2.0、JWT、CAS、SCIM 等标准协议，提供<strong>简单、标准、安全和开放</strong>的用户身份管理 (IDM)、身份认证 (AM)、单点登录 (SSO)、RBAC 权限管理和资源管理等。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">官方网站<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.maxkey.top" target="_blank"><strong>官网</strong></a><span> </span>|<span> </span><a href="https://maxkeytop.gitee.io/" target="_blank"><strong>官网二线</strong></a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">邮箱 email:<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Amaxkeysupport%40163.com" target="_blank">maxkeysupport@163.com</a></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">代码托管<span> </span><a href="https://gitee.com/dromara/MaxKey" target="_blank"><strong>Gitee</strong></a><span> </span>|<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2FMaxKey" target="_blank"><strong>GitHub</strong></a></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><strong>单点登录 (Single Sign On）</strong>简称为<span> </span><strong>SSO</strong>，用户只需要登录认证中心一次就可以访问所有相互信任的应用系统，无需再次登录。</p> 
 <p style="margin-left:0; margin-right:0"><strong>主要功能：</strong></p> 
 <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
  <li>所有应用系统共享一个身份认证系统</li> 
  <li>所有应用系统能够识别和提取 ticket 信息</li> 
 </ol> 
</blockquote> 
<h1 style="margin-left:0; margin-right:0; text-align:left">产品特性</h1> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>标准协议</li> 
</ol> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,"system-ui","Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:835px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>序号</th> 
   <th>协议</th> 
   <th>支持</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OAuth 2.0/OpenID Connect</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">SAML 2.0</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">JWT</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">CAS</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">高</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.5</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">FormBased</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">中</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.6</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">TokenBased(Post/Cookie)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">中</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.7</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">ExtendApi</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">低</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1.8</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">EXT</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">低</td> 
  </tr> 
 </tbody> 
</table> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>登录支持</li> 
</ol> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,"system-ui","Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:835px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>序号</th> 
   <th>登录方式</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.1</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">动态验证码 字母 / 数字 / 算术</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">双因素认证</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">短信认证 腾讯云短信 / 阿里云短信 / 网易云信</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">登录易 / Google/Microsoft Authenticator/FreeOTP/ 支持 TOTP 或者 HOTP</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.5</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Kerberos/SPNEGO/AD 域</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.6</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span style="background-color:#f6f8fa; color:#40485b">OpenLDAP/ActiveDirectory/ 标准 LDAP 服务器</span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.7</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">社交账号 微信 / QQ / 微博 / 钉钉 / Google/Facebook/ 其他</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2.8</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span style="background-color:#f6f8fa; color:#40485b">扫码登录</span><span> </span><span style="background-color:#f6f8fa; color:#40485b">企业微信 / 钉钉 / 飞书扫码登录</span></td> 
  </tr> 
 </tbody> 
</table> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">提供标准的认证接口以便于其他应用集成 SSO，安全的移动接入，安全的 API、第三方认证和互联网认证的整合。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提供用户生命周期管理，支持 SCIM 2 协议；开箱即用的连接器 (Connector) 实现身份供给同步。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">简化微软 Active Directory 域控、标准 LDAP 服务器机构和账号管理，密码自助服务重置密码。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">认证多租户功能，支持集团下多企业独立管理或企业下不同部门数据隔离的，降低运维成本。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">认证中心具有平台无关性、环境多样性，支持 Web、手机、移动设备等，如 Apple iOS，Andriod 等，将认证能力从 B/S 到移动应用全面覆盖。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">基于 Java EE 平台，微服务架构，采用 Spring、MySQL、Tomcat、Redis、MQ 等开源技术，扩展性强。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">开源、安全、自主可控，许可证 Apache 2.0 License &<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Flicenses.html" target="_blank">MaxKey 版权声明</a>。</p> </li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">界面</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>MaxKey 认证</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">登录界面<span> </span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/dromara/MaxKey/raw/master/images/maxkey_login.png?raw=true" referrerpolicy="no-referrer"><img alt src="https://gitee.com/dromara/MaxKey/raw/main/images/maxkey_login.png?raw=true" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">主界面</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><span> </span><img src="https://gitee.com/dromara/MaxKey/raw/main/images/maxkey_index.png?raw=true" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"> </p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">下载</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">当前版本百度网盘下载，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Fdownload.html" target="_blank"><span> </span>历史版本</a></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
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
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">v 3.5.0 GA</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022/05/10</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fhub.docker.com%2Fu%2Fmaxkeytop" target="_blank">链接</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F17eNhzZ-LcBYyxBXhQk85QQ" target="_blank">下载</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><strong>mxk9</strong></td> 
  </tr> 
 </tbody> 
</table> 
<h1 style="margin-left:0; margin-right:0; text-align:left">Roadmap</h1> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:634px; word-break:initial; word-spacing:0px"> 
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
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Java 17+</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Jakarta EE 9+</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q3</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Framework 6</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q4</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Spring Boot 3</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022Q4</td> 
  </tr> 
 </tbody> 
</table> 
<h1 style="margin-left:0; margin-right:0; text-align:left">版本发行说明</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292e">MaxKey v 3.5.0 GA 2022/05/10</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><br> <span style="background-color:#ffffff; color:#24292e">    *(MAXKEY-220501) 前后端分离改造，Angular 和 TypeScript 支持<br>     *(MAXKEY-220502) Ant Design of Angular 前端<br>     *(MAXKEY-220503) remeber me 功能优化<br>     *(MAXKEY-220504) 图片显示功能优化<br>     *(MAXKEY-220505) token 和 refresh_token 前端优化支持<br>     *(MAXKEY-220506) 日志打印优化<br>     *(MAXKEY-220507) 验证码功能优化<br>     *(MAXKEY-220508) 单点登录功能优化<br>     *(MAXKEY-220509) 元数据提供优化<br>     *(MAXKEY-220510) 会话功能调整优化<br>     *(MAXKEY-220511) 依赖项引用、更新和升级<br>         spring                   5.3.19<br>         springBoot               2.6.6<br>         springbootadmin          2.6.6</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            