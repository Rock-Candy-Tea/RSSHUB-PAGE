
---
title: 'Sa-Token v1.31.0 发布，轻量级 Java 权限认证框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js4.png'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 11:31:00 GMT
thumbnail: 'https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js4.png'
---

<div>   
<div class="content">
                                                                                            <h1>Sa-Token v1.31.0 更新，新增账号分类封禁、阶梯封禁功能</h1> 
<p>Sa-Token 是一个轻量级 Java 权限认证框架，主要解决：登录认证、权限认证、分布式 Session 会话、单点登录、OAuth2.0 等一系列权限相关问题。</p> 
<p>框架针对踢人下线、自动续签、前后台分离、分布式会话…… 等常见业务进行 N 多适配，通过 Sa-Token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p>Sa-Token v1.31.0 版本更新包括以下内容：</p> 
<ul> 
 <li>文档：新增优秀开源案例展示。</li> 
 <li>文档：新增博客展示，欢迎大家投稿。</li> 
 <li>新增：新增 <code>SaInterceptor</code> 综合拦截器。 <strong>[重要]</strong> <strong>[不向下兼容]</strong></li> 
 <li>新增：新增 新增 <code>@SaIgnore</code> 忽略鉴权注解。 <strong>[重要]</strong></li> 
 <li>新增：新增插件 <code>sa-token-dao-redis-fastjson</code>，感谢 <code>@sikadai</code> 提交的pr。 <strong>[重要]</strong></li> 
 <li>新增：新增插件 <code>sa-token-context-grpc</code>，感谢 <code>@LiYiMing666</code> 提交的pr。 <strong>[重要]</strong></li> 
 <li>重构：SaSession 取消 <code>tokenSignList</code> 的 final 修饰符。</li> 
 <li>新增：SaSession 添加 <code>setTokenSignList</code> 方法。</li> 
 <li>重构：TokenSign 新增 <code>setValue</code> 和 <code>setDevice</code> 方法。</li> 
 <li>修复：修复多账号模式下不能正确重置 <code>StpLogic</code> 的问题。</li> 
 <li>修复：修复 SaSession 对象中 TokenSign 判断有可能空指针的问题。</li> 
 <li>修复：解决当权限码为 null 时可能带来的空指针问题。</li> 
 <li>新增：新增 <code>StpUtil.getExtra(tokenValue, key)</code> 方法，用于获取任意 token 的扩展参数。</li> 
 <li>优化：优化 <code>StpLogic#logoutByTokenValue</code> 方法逻辑，精简代码。</li> 
 <li>重构：<code>SaTokenConfig</code> 配置类字段 <code>isReadHead</code> 改为 <code>isReadHeader</code>。 <strong>[不向下兼容]</strong></li> 
 <li>修复：修复部分场景下踢人下线会抛出异常 <code>非Web上下文无法获取Request</code> 的问题。</li> 
 <li>新增：新增方法 <code>StpLogic#getAnonTokenSession</code>，可在未登录情况下安全的获取 Token-Session。 <strong>[重要]</strong></li> 
 <li>新增：新增 <code>SaApplication</code> 对象，用于全局作用域存取值。 <strong>[重要]</strong></li> 
 <li>重构：将 <code>SaTokenListener</code> 改为事件发布订阅模式，允许同时注册多个侦听器。 <strong>[重要]</strong> <strong>[不向下兼容]</strong></li> 
 <li>重构：StpUtil.login(id) 不再强制校验账号是否禁用，需要手动校验。 <strong>[不向下兼容]</strong></li> 
 <li>重构：新增对账号限制、分类封禁、阶梯封禁功能。 <strong>[重要]</strong></li> 
 <li>新增：会话查询API增加反序获取会话方式。</li> 
 <li>新增：SSO模块增加 server-url 属性，用于简化各种 url 配置。 <strong>[重要]</strong></li> 
 <li>修复：修复单点登录模块 <code>ssoLogoutCall</code> 配置项无效的问题。</li> 
 <li>优化：优化 <code>SaSsoHandle.checkTicket(ticket, currUri);</code> 方法，使其不提供 currUri 参数时将不再注册单点注销回调。</li> 
 <li>修复：修复 <code>SaOAuth2Handle</code> 类中 <code>doLogin</code> 方法没有使用 <code>Param.pwd</code> 常量的问题。</li> 
 <li>新增：新增 <code>SaOAuth2Util.checkClientTokenScope(clientToken, scopes)</code> 方法，校验 Client-Token 是否含有指定 Scope。</li> 
 <li>删除：删除 <code>sa-token-jwt</code> 模块过期 class。</li> 
 <li>重构：<code>sa-token-jwt</code> 模块依赖改为 <code>hutool-jwt</code>，并升级版本为 5.8.5。</li> 
 <li>重构：<code>sa-token-jwt</code> 模块改为 <code>Util + Template</code> 形式，方便针对部分代码重写。 <strong>[重要]</strong></li> 
 <li>新增：在线文档添加API手册。</li> 
 <li>重构：<code>sa-token-oauth2</code> 模块密码模式新增 <code>client_secret</code> 参数校验。<strong>[不向下兼容]</strong></li> 
 <li>新增：集成 <code>jacoco</code> 插件，核心包单元测试覆盖率提高至 90% 以上。</li> 
 <li>优化：开源案例分离专属仓库：<a href="https://gitee.com/sa-token/awesome-sa-token">Awesome-Sa-Token</a></li> 
</ul> 
<h4>代码仓库：<a href="https://gitee.com/dromara/sa-token">https://gitee.com/dromara/sa-token</a></h4> 
<p>框架功能结构图</p> 
<p><img alt="js" src="https://color-test.oss-cn-qingdao.aliyuncs.com/sa-token/x/sa-token-js4.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            