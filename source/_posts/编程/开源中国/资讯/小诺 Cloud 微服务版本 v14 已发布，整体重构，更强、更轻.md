
---
title: '小诺 Cloud 微服务版本 v1.4 已发布，整体重构，更强、更轻'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2020/1231/124319_60ca9563_1980003.png'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 01:00:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2020/1231/124319_60ca9563_1980003.png'
---

<div>   
<div class="content">
                                                                                            <p>        <strong>小诺cloud版本为小诺框架中微服务版本，创造之时秉承着能让所有用户在不装插件的情况下完全能跑起来使用微服务框架，之继承了eureka为服务的注册中心。</strong></p> 
<p><strong>        项目采用 </strong><span style="background-color:#ffffff; color:#40485b">SpringCloud Hoxton + SpringCloud Gateway + SpringBoot2 + MybatisPlus3</span><strong><span style="background-color:#ffffff; color:#40485b">为后端，</span></strong><span style="background-color:#ffffff; color:#40485b">AntDesignVue</span><strong><span style="background-color:#ffffff; color:#40485b">为前端，也是想的能玩微服务的用户应该会驾驭前后分离，同时在我们框架产品之中，微服务为技术含量最高的一款，后面的版本中会陆续接入</span></strong><span style="background-color:#ffffff; color:#40485b">Nacos、</span>Sentinel、RocketMQ、Dubbo、Seata<strong>等多个套件，下面请看小诺项目整体架构流程图：</strong></p> 
<p style="text-align:center"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/1231/124319_60ca9563_1980003.png" referrerpolicy="no-referrer"></p> 
<p>        <strong>重构后从整体代码结构层面再次解剖【工程树】：</strong><br>                 xiaonuo-cloud                              工程顶级目录<br>                 ├─xiaonuo-api                               接口     <br>                 │  ├─xiaonuo-auth-api                  认证接口组件<br>                 │  ├─xiaonuo-context-api             上下文接口组件<br>                 │  └─xiaonuo-tenant-api               多租户接口组件<br>                 ├─xiaonuo-base                            基础     <br>                 │  ├─xiaonuo-cache                       缓存基础组件<br>                 │  ├─xiaonuo-common                 通用基础组件<br>                 │  ├─xiaonuo-core                         核心基础组件<br>                 │  └─xiaonuo-security                   安全基础组件<br>                 ├─xiaonuo-biz                               业务<br>                 │  ├─xiaonuo-gen                         代码业务组件<br>                 │  └─xiaonuo-system                     系统业务组件<br>                 ├─xiaonuo-modules                     应用模块    <br>                 │  ├─xiaonuo-main-app                主服务应用模块<br>                 │  └─xiaonuo-sample-app             案例服务应用模块<br>                 ├─xiaonuo-server                           依赖服务<br>                 │  ├─xiaonuo-actuator-app            监控中心依赖服务<br>                 │  ├─xiaonuo-config-app               配置中心依赖服务<br>                 │  ├─xiaonuo-eureka-app              注册中心依赖服务<br>                 │  └─xiaonuo-gateway-app            网关中心依赖服务<br>                 ├─_sql                                             初始化sql<br>                 └─_web                                           前端应用模块</p> 
<p>        <strong>项目启动后相关截图：</strong></p> 
<p style="text-align:center"><img height="1318" src="https://oscimg.oschina.net/oscnet/up-ea337e87e82564eae35d37937ae8b1165eb.png" width="2559" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img height="1297" src="https://oscimg.oschina.net/oscnet/up-0280b8898e9e6caeee7a17c3fd77d621e02.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img height="1297" src="https://oscimg.oschina.net/oscnet/up-2a799ec8fbb0b7a20c58c189ae005101c09.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img height="1297" src="https://oscimg.oschina.net/oscnet/up-3fde3387e3b5a803daf9e49756f95e1db0c.png" width="2560" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img height="1297" src="https://oscimg.oschina.net/oscnet/up-c323095553453d771523392e5accafb0f43.png" width="2560" referrerpolicy="no-referrer"></p> 
<p><strong>        近期不少小伙伴发起提议，</strong>将目前版本eureka版本注册中心更换为阿里巴巴Nacos最新，团队目前的战斗力除了维护升级layui单体版与主打项目vue版本外，也一在加紧速度投入Nacos的改造，下一期大版本预计将在5月底之前完成并发布与各位小伙伴见面。</p> 
<p><strong>       </strong> 我们的官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.xiaonuo.vip" target="_blank">https://www.xiaonuo.vip</a></p>
                                        </div>
                                      
</div>
            