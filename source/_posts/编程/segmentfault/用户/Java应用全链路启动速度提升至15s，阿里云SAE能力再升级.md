
---
title: 'Java应用全链路启动速度提升至15s，阿里云SAE能力再升级'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/remote/1460000039709743'
author: segmentfault
comments: false
date: 2021-03-28 00:26:57
thumbnail: 'https://segmentfault.com/img/remote/1460000039709743'
---

<div>   
<p><strong>简介：</strong> Java 作为一门面向对象编程语言，在性能方面的卓越表现独树一帜。但在高性能的背后，Java 的启动性能差也令人印象深刻，大家印象中的 Java 笨重、缓慢的印象也大多来源于此，高性能和快启动速度似乎有一些相悖。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039709743" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><p>近日，阿里云Serverless应用引擎(SAE)重磅发布 Java 应用启动加速功能，<strong>首度将 Alibaba Dragonwell(阿里巴巴开源的 Open JDK 长期支持版本)的冷启动加速技术、多线程运行加速技术和 SAE 自身的原地升级策略、镜像预热策略相结合，实现了 Java 应用的端到端启动速度提升至仅15s，多线程性能提升30%，再加上其自身的0代码改造优势，已成为企业享受 Serverless 价值的最短路径。</strong></p><h3>难点分析</h3><p>众所周知，微服务的用户在应用启动层面面临着一些难题：<br>• 软件包大：几百 MB 甚至 GB 级别<br>• 依赖包多：上百个依赖包，几千个 Class<br>• 加载耗时：从磁盘加载依赖包，再到 Class 按需加载，最高可占启动耗时的一半<br>借助 Dragonwell 快速启动和多线程运行加速能力，SAE 为 Serverless Java 应用提供了一套，让应用尽可能加速启动的最佳实践，让开发者更专注于业务开发：<br>• Java 环境 + JAR/WAR 软件包部署：集成 Dragonwell 11 ，提供加速启动环境<br>• JVM 快捷设置：支持一键开启快速启动，简化操作<br>• NAS 网盘：支持跨实例加速，在新包部署时，加速新启动实例/分批发布启动速度<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039709744" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><h3>加速效果</h3><p>我们选择一些微服务、复杂依赖的业务场景典型 Demo 或内部应用，测试启动效果，发现应用普遍能降低 5%～45% 的启动耗时。若应用启动，存在下列场景，会有明显加速效果：<br>• 类加载多（spring-petclinic 启动加载约 12000+ classes）<br>• 依赖外部数据越少<br><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039709742" alt="image.png" title="image.png" referrerpolicy="no-referrer"></span></p><h3>客户案例</h3><h4>阿里巴巴搜索推荐 Serverless 平台</h4><p>阿里内部的搜索推荐 Serverless 平台通过类加载隔离机制，将多个业务的合并部署在同一个 Java 虚拟机中。调度系统会按需地将业务代码合并部署到空闲的容器中，让多个业务可以共享同一个资源池，大大提高部署密度和整体的 CPU 使用率。<br>由于要支撑大量不同的业务研发运行，平台本身需要提供足够丰富的功能，如缓存、RPC调用。因此搜索推荐 Serverless 平台的每个 JVM 都需要拉起类似 Pandora Boot 的中间件隔离容器，这将加载大量的类，拖累了平台自身的启动速度。当突增的需求进入，调度系统需要拉起更多容器以供业务代码部署，此时容器本身的启动时间就显得尤为重要。<br>基于 Dragonwell 的快速启动技术，搜索推荐平台在预发布环境会执行 AppCDS、Jarindex 等优化，将产生的 archive 文件打入容器镜像中，这样每一个容器在启动时都能享受加速，减少约30%的启动耗时。</p><h4>潮牌秒杀SAE极致弹性</h4><p>某外部客户，借助 SAE 提供的 Jar 包部署与 Dragonwell 11，快速迭代上线了某潮牌商场 App。<br>在面对大促秒杀时，借助 SAE Serverless 极致弹性，与应用指标 QPS RT 指标弹性能力，轻松面对 10 倍以上快速扩容需求；同时一键开启 Dragonwell 增强的 AppCDS 启动加速能力，降低 Java 应用 20% 以上启动耗时，进一步加速应用启动，保证业务平稳健康运行。<br>SAE 是面向应用的 aPaaS 平台，实现了Serverless 架构 + 微服务架构的完美融合，此次再磅以 Dragonwell 的启动和运行加速技术，使得客户可以轻松享受应用加速带来的技术红利。</p><p><a href="https://developer.aliyun.com/article/782978?utm_content=g_1000255900" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            