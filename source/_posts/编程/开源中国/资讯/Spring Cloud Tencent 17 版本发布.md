
---
title: 'Spring Cloud Tencent 1.7 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8329'
author: 开源中国
comments: false
date: Fri, 16 Sep 2022 11:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8329'
---

<div>   
<div class="content">
                                                                                            <p>Spring Cloud Tencent 1.7 版本现已发布，支持 Spring Cloud Hoxton、2020、2021 版。</p> 
<p>Spring Cloud Tencent 是腾讯开源的一站式微服务解决方案，实现了Spring Cloud 标准微服务 SPI，开发者可以基于 Spring Cloud Tencent 快速开发 Spring Cloud 云原生分布式应用。Spring Cloud Tencent 的核心依托腾讯开源的一站式服务发现与治理平台 Polaris，实现各种分布式微服务场景。</p> 
<p>一、发布项列表：</p> 
<ol> 
 <li>1.7.1-Hoxton.SR12</li> 
 <li>1.7.0-2020.0.5</li> 
 <li>1.7.0-2021.0.3</li> 
</ol> 
<p>二、版本号说明：</p> 
<p>Spring Cloud Tencent 的版本号由两部分组成，前半段为 Spring Cloud Tencent 自身迭代的版本号，后半段为 Spring Cloud Tencent 针对特定版本的 Spring Cloud 的接口做出的实现，例如 1.7.0-2021.0.3 为 1.7.0 版本的 Spring Cloud Tencent 基于 2021.0.3 版本的 Spring Cloud 作出的实现。Spring Cloud Tencent 自身迭代的版本号分为三段，第一个为大版本号，不同大版本号不兼容，第二个为特性版本号，用于新特性发布迭代使用，第三位是Bugfix版本号，用于不同版本的 Spring Cloud 对应的 Spring Cloud Tencent 作BUG修复使用,不同版本的 Spring Cloud 对应的 Spring Cloud Tencent 的Bugfix版本号可能不同。实际使用时，引入不同版本的 Spring Cloud 对应的 Spring Cloud Tencent 最新版即可。</p> 
<p>版本管理说明文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FSpring-Cloud-Tencent-%25E7%2589%2588%25E6%259C%25AC%25E7%25AE%25A1%25E7%2590%2586" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/Spring-Cloud-Tencent-版本管理</a></p> 
<p>三、主要新特性：</p> 
<p>（一）服务治理</p> 
<ol> 
 <li>添加多特性环境路由插件，以帮助快速实现开发测试阶段的环境维护。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2F%25E6%25B5%258B%25E8%25AF%2595%25E7%258E%25AF%25E5%25A2%2583%25E8%25B7%25AF%25E7%2594%25B1" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/测试环境路由</a></li> 
 <li>添加SCG网关动态流量染色插件，可以配合多特性环境路由插件使用。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FSpring-Cloud-Gateway-%25E6%25B5%2581%25E9%2587%258F%25E6%259F%2593%25E8%2589%25B2" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/Spring-Cloud-Gateway-流量染色</a></li> 
 <li>元数据传递支持单跳传递，即指传到下一跳服务实例就不继续往后传。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FSpring-Cloud-Tencent-Metadata-Transfer-%25E4%25BD%25BF%25E7%2594%25A8%25E6%258C%2587%25E5%258D%2597%23%25E4%25BD%25BF%25E7%2594%25A8%25E8%25AF%25B4%25E6%2598%258E" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/Spring-Cloud-Tencent-Metadata-Transfer-使用指南#使用说明</a></li> 
 <li>支持 Zuul 网关路由（仅限 Hoxton 版本）。</li> 
</ol> 
<p>（二）动态配置</p> 
<ol> 
 <li>动态配置刷新新增反射的方式，以提升刷新性能。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FSpring-Cloud-Tencent-Config-%25E4%25BD%25BF%25E7%2594%25A8%25E6%2596%2587%25E6%25A1%25A3%23%25E7%25AC%25AC%25E4%25B8%2583%25E6%25AD%25A5%25E5%25AE%259E%25E7%258E%25B0%25E5%258A%25A8%25E6%2580%2581%25E5%2588%25B7%25E6%2596%25B0%25E9%2585%258D%25E7%25BD%25AE%25E8%2583%25BD%25E5%258A%259B" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/Spring-Cloud-Tencent-Config-使用文档#第七步实现动态刷新配置能力</a></li> 
 <li>支持 Spring Config Data 的方式注入配置文件（仅限 2021 版本）。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FSpring-Cloud-Tencent-Config-%25E4%25BD%25BF%25E7%2594%25A8%25E6%2596%2587%25E6%25A1%25A3%23%25E6%2594%25AF%25E6%258C%2581-spring-config-data" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/Spring-Cloud-Tencent-Config-使用文档#支持-spring-config-data</a></li> 
 <li>支持自定义设置应用启动时连不上配置中心的行为，包括快速失败和忽略。相关参数见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FSpring-Cloud-Tencent-Config-%25E4%25BD%25BF%25E7%2594%25A8%25E6%2596%2587%25E6%25A1%25A3%23%25E5%25AE%258C%25E6%2595%25B4%25E7%259A%2584%25E9%2585%258D%25E7%25BD%25AE%25E5%258F%2582%25E6%2595%25B0" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/Spring-Cloud-Tencent-Config-使用文档#完整的配置参数</a></li> 
</ol> 
<p>（三）监控运维</p> 
<ol> 
 <li>支持北极星指标监控上报功能（Prometheus Pull 模式）。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FRPC%25E5%25A2%259E%25E5%25BC%25BA%23%25E6%258C%2587%25E6%25A0%2587%25E7%259B%2591%25E6%258E%25A7%25E6%258F%2592%25E4%25BB%25B6" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/RPC增强#指标监控插件</a></li> 
 <li>支持北极星指标监控上报功能（Prometheus Push Gateway 模式）。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2F%25E5%259C%25BA%25E6%2599%25AF%25E5%258C%2596%25E6%258F%2592%25E4%25BB%25B6%231-push-gateway-%25E4%25B8%258A%25E6%258A%25A5%25E6%258F%2592%25E4%25BB%25B6%25E8%2587%25AA-170-%25E7%2589%2588%25E6%259C%25AC%25E5%25BC%2580%25E5%25A7%258B" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/场景化插件#1-push-gateway-上报插件自-170-版本开始</a></li> 
 <li>Actuator端点新增限流规则和路由规则的查询。详细接口见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FActuator-Endpoint-%25E6%2589%25A9%25E5%25B1%2595" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/Actuator-Endpoint-扩展</a></li> 
</ol> 
<p>（四）其他</p> 
<ol> 
 <li>对Feign进行增强，允许开发者在Feign调用过程中添加自定义的增强行为。详细操作参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki%2FRPC%25E5%25A2%259E%25E5%25BC%25BA%23feign%25E5%25A2%259E%25E5%25BC%25BA" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki/RPC增强#feign增强</a></li> 
 <li>添加 spring-cloud-starter-tencent-all 依赖，开发者能够借此一步接入全量 Spring Cloud Tencent 基础服务治理功能。快速接入样例参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Ftree%2Fmain%2Fspring-cloud-tencent-examples%2Fquickstart-example" target="_blank">https://github.com/Tencent/spring-cloud-tencent/tree/main/spring-cloud-tencent-examples/quickstart-example</a></li> 
</ol> 
<p>四、开源共建开发者（GitHub）</p> 
<p>@SkyeBeFreeman @lepdou @misselvexu @DerekYRC @pandaapo @weihubeats @lingxiao-wu @LuckyCaesar @DoubleLuXu</p> 
<p>欢迎大家使用体验、Star、Fork、Issue，也欢迎大家参与 Spring Cloud Tencent 开源共建！</p> 
<p>仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent" target="_blank">https://github.com/Tencent/spring-cloud-tencent</a> 项目文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Fwiki" target="_blank">https://github.com/Tencent/spring-cloud-tencent/wiki</a> 往期发布：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Fspring-cloud-tencent%2Freleases" target="_blank">https://github.com/Tencent/spring-cloud-tencent/releases</a></p>
                                        </div>
                                      
</div>
            