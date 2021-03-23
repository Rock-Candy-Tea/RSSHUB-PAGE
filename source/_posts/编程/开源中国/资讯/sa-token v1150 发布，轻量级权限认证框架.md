
---
title: 'sa-token v1.15.0 发布，轻量级权限认证框架'
categories: 
    - 编程
    - 开源中国
    - 资讯

author: 开源中国
comments: false
date: Tue, 23 Mar 2021 07:43:00 GMT
thumbnail: ''
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">sa-token是一个轻量级Java权限认证框架，主要解决：登录认证、权限认证、Session会话、单点登录、OAuth2.0 等一系列权限相关问题。</p> 
<p style="text-align:left">框架针对踢人下线、自动续签、前后台分离、分布式会话……等常见业务进行N多适配，通过sa-token，你可以以一种极简的方式实现系统的权限认证部分</p> 
<p style="text-align:left">sa-token v1.15.0 版本更新包括以下内容：</p> 
<p style="text-align:left">- 新增：文档添加源码涉及技术栈说明 <br> - 优化：优化路由拦截器模块文档，更简洁的示例<br> - 修复：修复非web环境下的错误提示，Request->Response<br> - 修复：修复Cookie注入时path判断错误，感谢@zhangzi0291提供的PR<br> - 新增：文档集成Redis章节新增redis配置示例说明，感谢群友 `@-)` 提供的建议<br> - 新增：增加token前缀模式，可在配置token读取前缀，适配`Bearer token`规范 **[重要]**<br> - 优化：`SaTokenManager`初始化Bean去除`initXxx`方法，优化代码逻辑<br> - 新增：`SaTokenManager`新增`stpLogicMap`集合，记录所有`StpLogic`的初始化，方便查找<br> - 新增：`Session`新增timeout操作API，可灵活修改Session的剩余有效时间 <br> - 新增：token前缀改为强制校验模式，如果配置了前缀，则前端提交token时必须带有<br> - 优化：精简`SaRouteInterceptor`，只保留自定义验证和默认的登陆验证，去除冗余功能 <br> - 优化：`SaRouterUtil`迁移到core核心包，优化依赖架构<br> - 优化：默认Dao实现类里`Timer定时器`改为子线程 + sleep 模拟 <br> - 新增：`Session`新增各种类型转换API，可快速方便存取值  **[重要]** <br> - 升级注意：<br>     - `SaRouterUtil`类迁移到核心包，注意更换import地址<br>     - `SaRouteInterceptor`去出冗余API，详情参考路由鉴权部分</p> 
<p style="text-align:left">更多详细信息请关注官方文档</p>
                                        </div>
                                      
</div>
            