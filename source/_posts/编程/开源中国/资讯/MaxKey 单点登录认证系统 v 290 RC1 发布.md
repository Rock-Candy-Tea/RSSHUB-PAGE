
---
title: 'MaxKey 单点登录认证系统 v 2.9.0 RC1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 00:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><img alt height="52" src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" width="203" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><a href="https://gitee.com/dromara/MaxKey/blob/master/README_en.md" target="_blank"><strong>English</strong></a> | <a href="https://gitee.com/dromara/MaxKey/blob/master/README_zh.md" target="_blank"><strong>中文</strong></a></p> 
<h1>概述</h1> 
<p style="text-align:left"><strong>MaxKey</strong>单点登录认证系统，谐音<strong>马克思的钥匙</strong>寓意是最大钥匙,是<strong>业界领先的企业级IAM身份管理和认证产品</strong>,国内开源IAM第一品牌；支持OAuth 2.0/OpenID Connect、SAML 2.0、JWT、CAS、SCIM等标准协议，提供<strong>简单、标准、安全和开放</strong>的用户身份管理(IDM)、身份认证(AM)、单点登录(SSO)、RBAC权限管理和资源管理等。</p> 
<p style="text-align:left">官方网站 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.maxkey.top%2F" target="_blank"><strong>官网</strong></a> | <a href="https://maxkeytop.gitee.io/" target="_blank"><strong>官网二线</strong></a></p> 
<p style="text-align:left">邮箱email: <strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Amaxkeysupport%40163.com" target="_blank">maxkeysupport@163.com</a></strong></p> 
<p style="text-align:left">代码托管 <a href="https://gitee.com/dromara/MaxKey" target="_blank"><strong>码云(Gitee)</strong></a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2FMaxKey" target="_blank"><strong>GitHub</strong></a></p> 
<p style="text-align:left"><strong>单点登录(Single Sign On）</strong>简称为<strong>SSO，</strong>用户只需要登录认证中心一次就可以访问所有相互信任的应用系统，无需再次登录。</p> 
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
 <li> <p>基于Java平台开发，采用Spring、MySQL、Tomcat、Apache Kafka、Redis等开源技术，支持微服务，扩展性强。</p> </li> 
 <li> <p>开源、安全、自主可控，许可证 Apache 2.0 License & <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Flicenses.html" target="_blank">MaxKey版权声明</a>。</p> </li> 
</ol> 
<h1>界面</h1> 
<p style="text-align:left"><strong>MaxKey认证</strong></p> 
<p style="text-align:left">登录界面 </p> 
<p style="text-align:left"><img alt height="724" src="https://oscimg.oschina.net/oscnet/up-607e43885b935e4ca5fab0607e3e726ddb9.png" width="1446" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">主界面</p> 
<p style="text-align:left"> <img alt height="1243" src="https://oscimg.oschina.net/oscnet/up-86d644c52e1155a69d1912a84b821986fc0.png" width="1436" referrerpolicy="no-referrer"></p> 
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
   <td style="border-color:#dfe2e5">v 2.9.0 RC1</td> 
   <td style="border-color:#dfe2e5">2021/08/10</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1cfe8NHH_yqUn2uk4VR-AvQ" target="_blank">链接下载</a></td> 
   <td style="border-color:#dfe2e5"><strong>63v1</strong></td> 
  </tr> 
 </tbody> 
</table> 
<h1>Roadmap</h1> 
<p style="text-align:left">1.零信任场景整合</p> 
<p style="text-align:left">2.MaxKey Cloud(微服务版)-2021年</p> 
<h2>版本说明</h2> 
<p><span style="background-color:#ffffff; color:#24292e">MaxKey v 2.9.0 RC1    2021/08/10</span><br> <span style="background-color:#ffffff; color:#24292e">    *(MAXKEY-210601) 企业微信扫描登录<br>     *(MAXKEY-210602) 钉钉扫描登录<br>     *(MAXKEY-210603) 第三方登录异常问题修复<br>     *(MAXKEY-210604) 新建maxkey-webs目录，包含maxkey-web-maxkey、maxkey-web-mgt、maxkey-web-resources<br>     *(MAXKEY-210605) 静态文件的合并到maxkey-web-resources<br>     *(MAXKEY-210606) 腾讯企业邮箱适配器优化<br>     *(MAXKEY-210607) 移除*.xml的spring配置文件<br>     *(MAXKEY-210608) 后台管理员自动生成密码的问题修复<br>     *(MAXKEY-210609) 密码重置接口的优化<br>     *(MAXKEY-210610) KAFKA数据同步接口优化，重新定义同步TOPIC<br>     *(MAXKEY-210611) LDAP及ActiveDirectory属性和连接的优化<br>     *(MAXKEY-210612) Synchronizers同步器的模块化，分成activedirectory、ldap、dingding、workweixin<br>     *(MAXKEY-210613) Synchronizers增加定时同步功能<br>     *(MAXKEY-210614) 后台用户和机构查询排序优化<br>     *(MAXKEY-210615) 增加连接器日志查询<br>     *(MAXKEY-210616) 增加同步器日志查询<br>     *(MAXKEY-210617) 应用配置适配器不生效修复<br>     *(MAXKEY-210618) FormBased认证功能的优化<br>     *(MAXKEY-210619) FormBased密码首次初始化问题修复<br>     *(MAXKEY-210620) 重新登录地址优化<br>     *(MAXKEY-210621) 实体类型的ID全部调整为雪花ID<br>     *(MAXKEY-210622) 后台报表优化<br>     *(MAXKEY-210623) 底层数据库mybatis-jpa-extra优化及问题修复<br>     *(MAXKEY-210624) 登录模块的模块化<br>     *(MAXKEY-210625) LDAP登录成功，密码自动同步到MaxKey<br>     *(MAXKEY-210626) 社交账号企业微信LOGO<br>     *(MAXKEY-210627) 找回密码时密码不匹配问题修复<br>     *(MAXKEY-210628) SHELL脚本优化<br>     *(MAXKEY-210629) 官方网站优化<br>     *(MAXKEY-210630) 标准构建优化<br>     *(MAXKEY-210631) maxkey-web-mgt配置文件分离，方便后续不同环境的切换<br>     *(MAXKEY-210632) 密码过期，当密码错误时，跳转到密码过期页面错误问题，流程：密码验证正确，然后跳转密码过期界面<br>     *(MAXKEY-210633) 登录密码错误n次,n小于设定的次数，后一次登录密码正确，设置密码错误次数为0<br>     *(MAXKEY-210634) 依赖jar引用、更新和升级<br>         spring          5.3.9<br>         springBoot      2.5.3<br>         springSession   2.5.1<br>         tomcat          9.0.50<br>         JustAuth        1.16.</span></p>
                                        </div>
                                      
</div>
            