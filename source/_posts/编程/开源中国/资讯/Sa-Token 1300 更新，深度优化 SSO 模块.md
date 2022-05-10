
---
title: 'Sa-Token 1.30.0 更新，深度优化 SSO 模块'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c4746965cd2648a29beeac030a8c0a8eea3.png'
author: 开源中国
comments: false
date: Tue, 10 May 2022 02:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c4746965cd2648a29beeac030a8c0a8eea3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p> </p> 
<p><img height="800" src="https://oscimg.oschina.net/oscnet/up-c4746965cd2648a29beeac030a8c0a8eea3.png" width="1850" referrerpolicy="no-referrer"></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">Sa-Token 是一个轻量级 Java 权限认证框架，主要解决：登录认证、权限认证、分布式 Session 会话、单点登录、OAuth2.0 等一系列权限相关问题。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">框架针对踢人下线、自动续签、前后台分离、分布式会话…… 等常见业务进行 N 多适配，通过 Sa-Token，你可以以一种极简的方式实现系统的权限认证部分。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>Sa-Token v1.30.0 版本更新包括以下内容：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增：新增集成 Web-Socket 鉴权示例。[重要]</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新增：</span><span>新增集成 Web-Socket（Spring封装版） 鉴权示例。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新增：</span><span>新增 jfinal 集成包 sa-token-jfinal-plugin [重要]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新增：</span><span>新增 jboot 集成包 sa-token-jboot-plugin （感谢 @nxstv 提交的pr）</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复：</span><span>修复整合 sa-token-jwt Style 模式时，StpUtil.getExtra("key") 无效的bug</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>升级 sa-token-context-dubbo dubbo版本：</span><span>2.7.11 -> 2.7.15</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>借助 flatten-maven-plugin 统一版本号定义 （感谢 @ruansheng8 提交的pr） [重要]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复：</span><span>修复在 springboot 2.6.x 下 quick-login 插件循环依赖无法启动的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化：</span><span>sa-token-spring-aop 依赖改为 sa-token-core，避免在webflux环境下启动报错的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化：</span><span>源码注释 设备标识 改为 设备类型 更符合语义</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复：</span><span>解决部分协议下 dubbo 参数变为小写导致 Id-Token 鉴权无效的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>单元测试升级为 JUnit5</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新增：</span><span>新增 maxLoginCount 配置，指定同一账号可同时在线的最大数量 [重要]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>彻底删除 SaTokenAction 接口，完全由 SaStrategy 代替</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新增：</span><span>新增 sa-token-dao-redisx 插件，感谢 @noear 提交的pr [重要]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化：</span><span>增加 parseToken 未配置 jwt 密钥时的异常提示，感谢 @BATTLEHAWK00 提交的pr</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化：</span><span>sso,oauth2 插件中调用配置类使用 getter 方法，感谢 @Naah 提交的pr</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新增：</span><span>新增 json 转换器模块</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构：</span><span>SaTokenListener#doLogin 方法新增 tokenValue 参数 [不向下兼容]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>SpringBoot 相关组件依赖版本升级至 2.5.12</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>文档：</span><span>在线文档所有 AjaxJson 改为 SaResult</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>文档：</span><span>“多账号认证” -> 改为 “多账户认证”</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>文档：</span><span>部分章节新增动态演示图 [重要]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>顶级异常类 SaTokenException 增加 code 异常细分状态码。</span><span>详见 [重要]</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>注意升级：受异常细分状态码影响，NotPermissionException 类中 getCode() 方法改为 getPermission()。[不向下兼容]</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>SSO 模块升级：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">重构：SSO 模块从核心包拆分为独立插件 sa-token-sso [重要]</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化：</span><span>SSO模式三单点注销回调方法中，注销语句改为：</span><span>stpLogic.logout(loginId) 更符合情景</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复：</span><span>解决 sso 构建认证地址时，部分 Servlet 版本内部实现不一致带来的双 back 参数问题。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>SSO 模块提供精细化异常处理</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构：</span><span>SSO 模式三接口 /sso/checkTicket、/sso/logout，更改响应体格式 [不向下兼容]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化：</span><span>SSO 模式三单点注销搭建示例增加 try-catch，提高容错性</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化：</span><span>SsoUtil.singleLogout 改为 SsoUtil.ssoLogout，且无需再提供 secretkey 参数 [不向下兼容]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>升级：</span><span>将 SSO 模式三的接口调用改为签名式校验。</span><span>[重要] [不向下兼容]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>新增：</span><span>新增 SSO 模式三下无 sdk 的对接示例， 感谢 @Sa-药水 的建议反馈 [重要]</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>sa-token-jwt 模块升级：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">重构：sa-token-jwt 的创建，强制校验loginType [不向下兼容]</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构：</span><span>StpLogicJwtForStateless 由重写 login 方法改为重写 createLoginSession</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构：</span><span>SaJwtUtil 工具类不再吞并异常消息，且提供精细化异常 code 码。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构：</span><span>改名：</span><span>StpLogicJwtForStyle -> StpLogicJwtForSimple</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>重构：</span><span>改名：</span><span>StpLogicJwtForMix -> StpLogicJwtForMixin</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复：</span><span>修复 StpLogicJwtForSimple 模式下 Extra 数据可能受到旧 token 影响的bug</span></p> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>代码仓库：https://gitee.com/dromara/sa-token</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>框架功能结构图：</strong></p> 
<p><img height="1278" src="https://oscimg.oschina.net/oscnet/up-dbf41511d31f7dd7944892cdac73cf60723.png" width="1962" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            