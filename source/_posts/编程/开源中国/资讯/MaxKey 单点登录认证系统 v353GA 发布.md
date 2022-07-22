
---
title: 'MaxKey 单点登录认证系统 v3.5.3GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 09:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                                            <h1><img alt src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" referrerpolicy="no-referrer"></h1> 
<p><a href="https://gitee.com/dromara/MaxKey/blob/master/README_en.md"><strong>English</strong></a>|<a href="https://gitee.com/dromara/MaxKey/blob/master/README_zh.md"><strong>中文</strong></a></p> 
<h1>概述</h1> 
<p><strong>MaxKey</strong>单点登录认证系统，谐音马克思的钥匙寓意是最大钥匙,是<strong>业界领先的IAM身份管理和认证产品</strong>,支持OAuth 2.x/OpenID Connect、SAML 2.0、JWT、CAS、SCIM等标准协议，提供<strong>安全、标准和开放</strong>的用户身份管理(IDM)、身份认证(AM)、单点登录(SSO)、RBAC权限管理和资源管理等。</p> 
<p>官方网站<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.maxkey.top%2F" target="_blank"><strong>官网</strong></a>|<a href="https://maxkeytop.gitee.io/"><strong>官网二线</strong></a></p> 
<p>邮箱email:<strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Asupport%40maxsso.net" target="_blank">support@maxsso.net</a></strong></p> 
<p>代码托管<a href="https://gitee.com/dromara/MaxKey"><strong>Gitee</strong></a>|<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2FMaxKey" target="_blank"><strong>GitHub</strong></a></p> 
<blockquote> 
 <p><strong>单点登录(Single Sign On）<strong>简称为</strong>SSO</strong>，用户只需要登录认证中心一次就可以访问所有相互信任的应用系统，无需再次登录。</p> 
 <p><strong>主要功能：</strong></p> 
 <ol> 
  <li>所有应用系统共享一个身份认证系统</li> 
  <li>所有应用系统能够识别和提取ticket信息</li> 
 </ol> 
</blockquote> 
<h1>产品特性</h1> 
<ol> 
 <li>标准协议</li> 
</ol> 
<table> 
 <thead> 
  <tr> 
   <th>序号</th> 
   <th>协议</th> 
   <th>支持</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>1.1</td> 
   <td>OAuth 2.0/OpenID Connect</td> 
   <td>高</td> 
  </tr> 
  <tr> 
   <td>1.2</td> 
   <td>SAML 2.0</td> 
   <td>高</td> 
  </tr> 
  <tr> 
   <td>1.3</td> 
   <td>JWT</td> 
   <td>高</td> 
  </tr> 
  <tr> 
   <td>1.4</td> 
   <td>CAS</td> 
   <td>高</td> 
  </tr> 
  <tr> 
   <td>1.5</td> 
   <td>FormBased</td> 
   <td>中</td> 
  </tr> 
  <tr> 
   <td>1.6</td> 
   <td>TokenBased(Post/Cookie)</td> 
   <td>中</td> 
  </tr> 
  <tr> 
   <td>1.7</td> 
   <td>ExtendApi</td> 
   <td>低</td> 
  </tr> 
  <tr> 
   <td>1.8</td> 
   <td>EXT</td> 
   <td>低</td> 
  </tr> 
 </tbody> 
</table> 
<ol> 
 <li>登录支持</li> 
</ol> 
<table> 
 <thead> 
  <tr> 
   <th>序号</th> 
   <th>登录方式</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>2.1</td> 
   <td>动态验证码 字母/数字/算术</td> 
  </tr> 
  <tr> 
   <td>2.2</td> 
   <td>双因素认证</td> 
  </tr> 
  <tr> 
   <td>2.3</td> 
   <td>短信认证 腾讯云短信/阿里云短信/网易云信</td> 
  </tr> 
  <tr> 
   <td>2.4</td> 
   <td>登录易/Google/Microsoft Authenticator/FreeOTP/支持TOTP或者HOTP</td> 
  </tr> 
  <tr> 
   <td>2.5</td> 
   <td>Kerberos/SPNEGO/AD域</td> 
  </tr> 
  <tr> 
   <td>2.6</td> 
   <td>OpenLDAP/ActiveDirectory/标准LDAP服务器</td> 
  </tr> 
  <tr> 
   <td>2.7</td> 
   <td>社交账号 微信/QQ/微博/钉钉/Google/Facebook/其他</td> 
  </tr> 
  <tr> 
   <td>2.8</td> 
   <td>扫码登录 企业微信/钉钉/飞书扫码登录</td> 
  </tr> 
 </tbody> 
</table> 
<ol> 
 <li> <p>提供标准的认证接口以便于其他应用集成SSO，安全的移动接入，安全的API、第三方认证和互联网认证的整合。</p> </li> 
 <li> <p>提供用户生命周期管理，支持SCIM 2协议；开箱即用的连接器(Connector)实现身份供给同步。</p> </li> 
 <li> <p>简化微软Active Directory域控、标准LDAP服务器机构和账号管理，密码自助服务重置密码。</p> </li> 
 <li> <p>认证多租户功能，支持集团下多企业独立管理或企业下不同部门数据隔离的，降低运维成本。</p> </li> 
 <li> <p>认证中心具有平台无关性、环境多样性，支持Web、手机、移动设备等, 如Apple iOS，Andriod等，将认证能力从B/S到移动应用全面覆盖。</p> </li> 
 <li> <p>基于Java EE平台，微服务架构，采用Spring、MySQL、Tomcat、Redis、MQ等开源技术，扩展性强。</p> </li> 
 <li> <p>开源、安全、自主可控，许可证 Apache 2.0 License &<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Flicenses.html" target="_blank">MaxKey版权声明</a>。</p> </li> 
</ol> 
<h1>界面</h1> 
<p><img alt src="https://gitee.com/dromara/MaxKey/raw/master/images/maxkey_login.png?raw=true" referrerpolicy="no-referrer"><img alt src="https://gitee.com/dromara/MaxKey/raw/main/images/maxkey_login.png?raw=true" referrerpolicy="no-referrer"></p> 
<h1>下载</h1> 
<p>当前版本百度网盘下载,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Fdownload.html" target="_blank">历史版本</a></p> 
<table> 
 <thead> 
  <tr> 
   <th>版本</th> 
   <th>日期</th> 
   <th>Docker</th> 
   <th>网盘</th> 
   <th>网盘提取码</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>v 3.5.3 GA</td> 
   <td>2022/07/23</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fu%2Fmaxkeytop" target="_blank">链接</a></td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1lrSsARpyLlmkXeCbgrCy2g" target="_blank">下载</a></td> 
   <td><strong>mxk9</strong></td> 
  </tr> 
 </tbody> 
</table> 
<h1>Roadmap</h1> 
<table> 
 <thead> 
  <tr> 
   <th>序号</th> 
   <th>计划</th> 
   <th>时间</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>1</td> 
   <td>Java 17+</td> 
   <td>2022Q3</td> 
  </tr> 
  <tr> 
   <td>2</td> 
   <td>Jakarta EE 9+</td> 
   <td>2022Q3</td> 
  </tr> 
  <tr> 
   <td>3</td> 
   <td>Spring Framework 6</td> 
   <td>2022Q4</td> 
  </tr> 
  <tr> 
   <td>4</td> 
   <td>Spring Boot 3</td> 
   <td>2022Q4</td> 
  </tr> 
 </tbody> 
</table> 
<h1>版本发行说明</h1> 
<p>MaxKey v 3.5.3 GA 2022/07/23</p> 
<p>*(MAXKEY-220801) formbase用户初始化跳转问题修复<br> *(MAXKEY-220802) OAuth2 select多选保存问题<br> *(MAXKEY-220803) OAuth2密码保存不一致修复<br> *(MAXKEY-220804) HttpSessionListenerAdapter中userinfo空指针异常<br> *(MAXKEY-220805) 增加LDAP登录认证的参数配置<br> *(MAXKEY-220806) 组织增加公司、分支机构、部门、组四种类型<br> *(MAXKEY-220807) REDIS的key统一MXK_开头<br> *(MAXKEY-220808) HttpRequestAdapter增加REST方法<br> *(MAXKEY-220809) 新增应用时增加初始化默认值<br> *(MAXKEY-220810) Ldap认证配置的判断<br> *(MAXKEY-220811) 前端refresh_token报错问题，Header可为空，在程序中进行判断<br> *(MAXKEY-220812) 新增或者编辑图片无法上传的问题<br> *(MAXKEY-220813) JWT增加GET方式<br> *(MAXKEY-220814) 验证码字段调整<br> *(MAXKEY-220815) 账号管理中应用选择未显示问题<br> *(MAXKEY-220816) 删除打jar包时maxkey-web-resources依赖问题<br> *(MAXKEY-220817) 依赖项引用、更新和升级<br> log4j 2.18.0<br> tomcat 9.0.64<br> druid 1.2.11<br> druidspringboot 1.2.11</p>
                                        </div>
                                      
</div>
            