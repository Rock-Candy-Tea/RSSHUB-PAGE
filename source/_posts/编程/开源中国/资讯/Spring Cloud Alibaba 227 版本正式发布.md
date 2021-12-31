
---
title: 'Spring Cloud Alibaba 2.2.7 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/d0e4cacaf51746cfb477c37ee0e7faa0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 14:07:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/d0e4cacaf51746cfb477c37ee0e7faa0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">作者 | 铖朴</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">什么是 Spring Cloud Alibaba？</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1、简介</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Spring Cloud Alibaba 是由阿里巴巴（后文简称：阿里）中间件团队于 2018 年 7 月开源，为业界提供的一套基于阿里内部分布式技术的一站式微服务构建解决方案。基于 Spring Cloud 微服务框架标准，针对微服务架构中的服务注册与发现、分布式消息、服务限流降级以及分布式事务等核心模块，都提供了相应的面向业界的成熟解决方案，与 Spring Cloud 之间的关系如下图所示：<span> </span><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d0e4cacaf51746cfb477c37ee0e7faa0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">依托 Spring Cloud Alibaba，用户仅需要添加一些注解和少量配置，就可以将 Spring Cloud 应用接入阿里微服务解决方案，通过阿里中间件来迅速搭建稳定可靠的分布式应用系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2、主要功能</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在 Spring Cloud 众多的实现方案中，Spring Cloud Alibaba 凭借其支持组件最多，方案最完善，在 Spring Cloud 生态家族中扮演了重要角色。Spring Cloud Alibaba 与 Spring Cloud 生态其他方案之间对比图如下：<span> </span><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dd4050c258fa4907a956c0633e032fe9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Spring Cloud Alibaba 所提供的一套微服务系统构建解决方案组件如下： • Nacos：阿里开源的一款易于构建云原生应用的动态服务发现、配置管理和服务管理平台。 • Sentinel：阿里开源的一款限流降级产品，将流量作为切入点，从流量控制、熔断降级、系统负载保护等多个维度保护服务的稳定性。 • RocketMQ：阿里捐献给 Apache 基金会的一款分布式消息产品，是一个基于 Java 的高性能、高吞吐量的分布式消息和流计算平台。 • Dubbo：阿里捐献给 Apache 基金会的一款高性能的 Java RPC 框架。 • Seata：阿里开源的一套易于使用的高性能微服务分布式事务解决方案。 • Alibaba Cloud OSS：阿里云对象存储服务（Object Storage Service，简称 OSS），是阿里云提供的海量、安全、低成本、高可靠的云存储服务。您可以在任何应用、任何时间、任何地点存储和访问任意类型的数据。 • Alibaba Cloud SchedulerX：阿里中间件团队开发的一款分布式任务调度产品，支持周期性的任务与固定时间点触发任务。 • Alibaba Cloud SMS：覆盖全球的短信服务，友好、高效、智能的互联化通讯能力，帮助企业迅速搭建客户触达通道。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3、快速上手</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为了让广大开发者，快速学习与上手。项目维护团队于 2020 年 12 月，联合阿里云知行实验室推出了 Spring Cloud Alibaba 入门系列课程与 Java 工程脚手架工具，方便让广大开发同学快速了解和构建 Spring Cloud Alibaba 项目。Spring Cloud Alibaba 入门系列课程可在知行实验室首页获取：<span> </span><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a22c06b322364c5e9cef289ac6860010.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">基于阿里云 Java 脚手架，开发者可告别复杂的依赖管理，通过脚手架工具选择所需依赖，便可生成包含相关依赖的项目模板供开发者下载使用。相关项目构建过程如下图所示：<span> </span><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a87c9e22958b43c38d0b380d1fc2ab2f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">新版本特性预览</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">介绍完 Spring Cloud Alibaba 后，本次隆重发布的 Spring Cloud Alibaba 2.2.7 版本对其中包括注册配置中心、分布式消息等在内的众多组件进行重大升级：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">• Nacos：升级 Nacos 客户端到 2.0 版本，注册发现过程支持 gRPC 长链接，可显著降低资源开销，提高系统吞吐量，在性能上有大幅提升。更多细节可参见Nacos 2.0 介绍资料。 • RocketMQ：将之前项目中的 RocketMQ 单独分支融入到了项目主分支，跟随大版本一起发布迭代，使用户可在最新 Spring Cloud Alibaba 中直接使用 RocketMQ 新支持的批量消息、异步消息回调处理、Push 模式下指定消费起始位等众多新特性。 • Spring Boot：升级 Spring Boot 版本到 2.3.12，相比于之前的 2.3.2，不仅升级了大量底层组件的依赖增加了一些新特性，并修复了很多遗留问题，提高了框架稳定性。 • Spring Cloud：升级 Spring Cloud 版本到 Hoxton.SR12，相比于之前的 Hoxton.SR9 在基础组件的稳定性方面有了进一步提升。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了组件升级，另外也修复了很多之前版本所存在的问题，进一步提升了 Spring Cloud Alibaba 使用的稳定性与健壮性。更多资料可参见发版公告。Spring Cloud Alibaba 与 Spring Cloud 和 Spring Boot 当前各版本对应关系可参见官网 Wiki 版本说明。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">回顾与展望</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">经过三年多的飞速发展，截止到当前，Spring Cloud Alibaba 共发布了 26 个版本，在GitHub上的累计 star 数目超过了 2W，folk 数达到了 6.4k，用户数达到了 19.4k 之多，各项关键数据遥遥领先国内外各大云厂商推出的同类开源微服务项目。<span> </span><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/54734a54c4214185aa67a370f0c76546.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了支撑阿里巴巴经济体日常复杂的微服务应用场景，Spring Cloud Alibaba也被数千家外部企业用户在生产场景中广泛使用。<span> </span><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/865b016d0b5442688bcb82c0aa8d092c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Zi_6YeM5be05be05Lit6Ze05Lu2,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">未来 Spring Cloud Alibaba 会继续对齐 Spring Cloud 主流版本发展演进，近期会同时支持以 Spring Cloud 2020.0.X 和 Hoxton 两个当前主流版本对应的 Spring Cloud Alibaba 2021.X 和 2.2.X 版本迭代。社区未来初步规划会持续在完善当前所支持的 Nacos、RocketMQ 和 Spring Cloud Dubbo 等组件的稳定性与丰富组件所支持的功能上持续努力。（也欢迎大家提 issue 告诉社区你所认为项目值得演进的具体方向哈：）</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">最后，作为一个业界知名开源项目，未来发展还需要持续依托社区大家共同的努力，也非常欢迎新同学的加入！只要能贡献 3~5 次社区认可具有价值的 Pull requests，即可有机会被邀请成为社区 Collaborator，共同主导未来社区发展建设！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Spring Cloud Alibaba 企业版</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">除了开源的 Spring Cloud Alibaba 以外，针对企业级用户复杂繁重的微服务治理诉求，阿里云中间件团队推出的阿里云微服务引擎（Microservices Engine，MSE）提供了包括全链路灰度、无损上下线、服务预热、离群实例摘除等在内的大量企业级微服务治理功能，让用户可不改一行代码即可将应用接入 MSE 便捷、低成本地拥有企业级微服务治理能力。除了微服务治理，MSE 还提供了企业级的 Nacos 注册配置中心和企业级云原生网关等众多产品，帮助企业用户迅速拥抱云原生微服务。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">点击了解更多 Spring Cloud Alibaba 企业版相关内容：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.aliyun.com%2Fproduct%2Faliware%2Fmse" target="_blank">https://www.aliyun.com/product/aliware/mse</a></p>
                                        </div>
                                      
</div>
            