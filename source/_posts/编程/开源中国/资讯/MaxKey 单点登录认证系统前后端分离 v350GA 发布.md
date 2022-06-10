
---
title: 'MaxKey 单点登录认证系统前后端分离 v3.5.0GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Fri, 10 Jun 2022 08:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><img alt height="52" src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" width="203" referrerpolicy="no-referrer"></h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dromara/MaxKey/blob/master/README_en.md" target="_blank"><strong>English</strong></a><span> </span>|<span> </span><a href="https://gitee.com/dromara/MaxKey/blob/master/README_zh.md" target="_blank"><strong>中文</strong></a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">概述</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>MaxKey</strong><span> </span>单点登录认证系统，谐音马克思的钥匙寓意是最大钥匙，是<strong>业界领先的 IAM 身份管理和认证产品</strong><span> </span>, 支持 OAuth 2.x/OpenID Connect、SAML 2.0、JWT、CAS、SCIM 等标准协议，提供<strong>安全、标准和开放</strong>的用户身份管理 (IDM)、身份认证 (AM)、单点登录 (SSO)、RBAC 权限管理和资源管理等。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">官方网站<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.maxkey.top" target="_blank"><strong>官网</strong></a><span> </span>|<span> </span><a href="https://maxkeytop.gitee.io/" target="_blank"><strong>官网二线</strong></a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">邮箱 email:<span> </span></span><strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Asupport%40maxsso.net" target="_blank">support@maxsso.net</a></strong></p> 
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
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">v 3.5.1 GA</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022/06/09</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fhub.docker.com%2Fu%2Fmaxkeytop" target="_blank">链接</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F11ioAH1qlmYlMV1PjMrz2Sw" target="_blank">下载</a></td> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292e">MaxKey v 3.5.1 GA 2022/06/09</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292e">    *(MAXKEY-220601) session 会话增加二级缓存<br>     *(MAXKEY-220602) session 会话超时及 token 刷新的问题<br>     *(MAXKEY-220603) 认证界面优化，支持账号登录和扫码登录<br>     *(MAXKEY-220604) 用户管理增加启用、禁用、锁定等功能<br>     *(MAXKEY-220605) 用户管理增加角色、用户组、账号管理和密码修改功能<br>     *(MAXKEY-220606) 繁体中文支持<br>     *(MAXKEY-220607) 认证端菜单靠左对齐<br>     *(MAXKEY-220608) 单点登录应用跳转错误问题 (woshiwangjijun@qq.com)<br>     *(MAXKEY-220609) 管理端界面问题调整<br>     *(MAXKEY-220610) 前端界面多租户 knowHost 及自定义<br>     *(MAXKEY-220611) 社交账号登录问题<br>     *(MAXKEY-220612) 第三方 JWT 登录支持<br>     *(MAXKEY-220613) 管理端选择框映射值问题<br>     *(MAXKEY-220614) 鉴于监管问题，QQ 群禁言，未来以信息发布为主<br>     *(MAXKEY-220615) 变更支持邮箱 support@maxsso.net<br>     *(MAXKEY-220616) 管理日志记录<br>     *(MAXKEY-220617) ZyXEL 网络设备 Portal 登录支持<br>     *(MAXKEY-220618) 动态组和动态角色优化，删除固定配置<br>     *(MAXKEY-220619) 动态组和动态角色的成员管理显示所属组或者角色<br>     *(MAXKEY-220620) 管理端列表按钮样式整体调整，删除 primary<br>     *(MAXKEY-220621) 零信任标准工作组连接<br>     *(MAXKEY-220622) 角色、用户组、账号策略部门选择改用 TreeSelect 组件<br>     *(MAXKEY-220623) 增加控制台域名配置<br>     *(MAXKEY-220624) 资源表增加权限标识字段<br>     *(MAXKEY-220625) 开关控件控制的优化<br>     *(MAXKEY-220626) 提示信息国际化优化<br>     *(MAXKEY-220627) NGINX 转发头添加 proxy_set_header host<br>     *(MAXKEY-220628) 简化权限控制，合并角色 + 用户组 --> 角色<br>     *(MAXKEY-220629) 简化账号管理功能<br>     *(MAXKEY-220630) 优化管理端 UI 功能<br>     *(MAXKEY-220631) 社交账号登录跳转问题<br>     *(MAXKEY-220632) 字段名称的调整<br>     *(MAXKEY-220633) 图片上传问题修复<br>     *(MAXKEY-220634) 依赖项引用、更新和升级<br>         spring                   5.3.20<br>         springBoot               2.6.8<br>         springSecurity           5.6.5<br>         tomcat                   9.0.63<br>         gson                     2.9.0<br>         guava                    31.1-jre<br>         zxingcore                3.5.0<br>         mysqlconnectorjava       8.0.29<br>         druid                    1.2.10<br>         caffeine                 2.9.3<br>         mybatis                  3.5.10<br>         jackson                  2.13.3<br>         fastjson                 1.2.83<br>         jodatime                 2.10.14<br>         passay                   1.6.1</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            