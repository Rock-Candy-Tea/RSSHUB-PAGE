
---
title: 'MaxKey 单点登录认证系统 v3.5.6GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 09:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png'
---

<div>   
<div class="content">
                                                                                            <h1><img alt src="https://oscimg.oschina.net/oscnet/up-3bfd568be0ce2a51bf9a3f5bbd94fbe314f.png" referrerpolicy="no-referrer"></h1> 
<p><a href="https://gitee.com/dromara/MaxKey/blob/master/README_en.md"><strong>English</strong></a>|<a href="https://gitee.com/dromara/MaxKey/blob/master/README_zh.md"><strong>中文</strong></a></p> 
<h1>概述</h1> 
<p><strong>MaxKey</strong>单点登录认证系统，谐音马克思的钥匙寓意是最大钥匙,是<strong>业界领先的IAM身份管理和认证产品</strong>,支持OAuth 2.x/OpenID Connect、SAML 2.0、JWT、CAS、SCIM等标准协议，提供<strong>安全、标准和开放</strong>的用户身份管理(IDM)、身份认证(AM)、单点登录(SSO)、RBAC权限管理和资源管理等。</p> 
<p>官方网站<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.maxkey.top%2F" target="_blank"><strong>官网</strong></a>|<a href="https://maxkeytop.gitee.io/"><strong>官网二线</strong></a></p> 
<p>官方QQ：<strong>1054466084</strong></p> 
<p>邮箱email:<strong><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Asupport%40maxsso.net" target="_blank">support@maxsso.net</a></strong></p> 
<p>代码托管<a href="https://gitee.com/dromara/MaxKey"><strong>Gitee</strong></a>|<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2FMaxKey" target="_blank"><strong>GitHub</strong></a></p> 
<h1>产品特性</h1> 
<p>1.标准协议</p> 
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
<p>2.登录支持</p> 
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
<p>3.提供标准的认证接口以便于其他应用集成SSO，安全的移动接入，安全的API、第三方认证和互联网认证的整合。</p> 
<p>4.提供用户生命周期管理，支持SCIM 2协议；开箱即用的连接器(Connector)实现身份供给同步。</p> 
<p>5.简化微软Active Directory域控、标准LDAP服务器机构和账号管理，密码自助服务重置密码。</p> 
<p>6.认证多租户功能，支持集团下多企业独立管理或企业下不同部门数据隔离的，降低运维成本。</p> 
<p>7.认证中心具有平台无关性、环境多样性，支持Web、手机、移动设备等, 如Apple iOS，Andriod等，将认证能力从B/S到移动应用全面覆盖。</p> 
<p>8.基于Java EE平台，微服务架构，采用Spring、MySQL、Tomcat、Redis、MQ等开源技术，扩展性强。</p> 
<p>9.开源、安全、自主可控，许可证 Apache 2.0 License &<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaxkey.top%2Fzh%2Fabout%2Flicenses.html" target="_blank">MaxKey版权声明</a>。</p> 
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
   <td>v 3.5.6 GA</td> 
   <td>2022/09/07</td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fu%2Fmaxkeytop" target="_blank">链接</a></td> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpan.baidu.com%2Fs%2F1J-A3GehHiS4SyMZMzi_Dig" target="_blank">下载</a></td> 
   <td><strong>mxk9</strong></td> 
  </tr> 
 </tbody> 
</table> 
<h1>版本说明</h1> 
<p>MaxKey v 3.5.6 GA 2022/09/07</p> 
<pre><code>
    *(MAXKEY-221101) 解决springcloud JAR包冲突问题
    *(MAXKEY-221102) CAS 未注册URL登录错误提示优化CAS service $&#123;errorMessage!&#125; not registered .
    *(MAXKEY-221103) 同步代码优化org.maxkey.persistence -->org.maxkey.provision
    *(MAXKEY-221104) 优化对象转换类ObjectTransformer
    *(MAXKEY-221105) 数据同步的对象经过序列化后存储到数据库,下一版本在后台系统定义同步线程实现数据同步
    *(MAXKEY-221106) 优化HMAC512签名的代码
    *(MAXKEY-221107) 腾讯企业邮箱登录优化
    *(MAXKEY-221108) 开源之夏SDK的提交
    *(MAXKEY-221109) 压缩images包下面的图片尺寸
    *(MAXKEY-221110) 添加知识星球扫码连接
    *(MAXKEY-221111) 默认组织根节点不可删除，隐藏删除按钮
    *(MAXKEY-221112) 默认角色组不可删除，隐藏删除按钮
    *(MAXKEY-221113) 移除KAFKA支持
    *(MAXKEY-221114) 移除RocketMQ支持
    *(MAXKEY-221115) 移除非必须的监控模块maxkey-monitor，该模块建议开发者自行部署
    *(MAXKEY-221016) 依赖项引用、更新和升级
        springcloudalibabacspl  1.8.5
        jbosslogging            3.4.3.Final
        hibernateVersion        6.2.4.Final
</code></pre> 
<p> </p> 
<p><img height="500" src="https://oscimg.oschina.net/oscnet/up-d751b5ceb2bde22e73010bfe791c72ab248.jpg" width="900" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            