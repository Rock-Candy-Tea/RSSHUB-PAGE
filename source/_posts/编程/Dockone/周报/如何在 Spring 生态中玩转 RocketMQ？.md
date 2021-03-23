
---
title: '如何在 Spring 生态中玩转 RocketMQ？'
categories: 
    - 编程
    - Dockone
    - 周报

author: Dockone
comments: false
date: 2021-03-23 05:36:33
thumbnail: 'http://dockone.io/uploads/article/20210319/9e59ca0cce457e073fe617a5327d8602.png'
---

<div>   
<br>作者 | 通融、洛夜<br>
来源 | <a href="https://mp.weixin.qq.com/s/4QUWP1nQPkLu0u9GMkOeyw">阿里巴巴云原生公众号</a><br>
<br>RocketMQ 作为业务消息的首选，在消息和流处理领域被广泛应用。而微服务生态 Spring 框架也是业务开发中最受欢迎的框架，两者的完美契合使得 RocketMQ 成为 Spring Messaging 实现中最受欢迎的消息实现。本文展示了 5 种在 Spring 生态中文玩转 RocketMQ 的方式，并描述了每个项目的特点和使用场景。文末可以直达在线体验。<br>
<br><h1>前言</h1>上世纪 90 年代末，随着 Java EE(Enterprise Edition) 的出现，特别是 Enterprise Java Beans 的使用需要复杂的描述符配置和死板复杂的代码实现，增加了广大开发者的学习曲线和开发成本，由此基于简单的 XML 配置和普通 Java 对象 (Plain Old Java Objects) 的 Spring 技术应运而生，依赖注入 (Dependency Injection)，控制反转 (Inversion of Control) 和面向切面编程 (AOP) 的技术更加敏捷地解决了传统 Java 企业及版本的不足。随着 Spring 的持续演进，基于注解 (Annotation) 的配置逐渐取代了 XML 文件配置。除了依赖注入、控制翻转、AOP 这些技术，Spring 后续衍生出 AMQP、Transactional、Security、Batch、Data Access 等模块，涉及开发的各个领域。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/9e59ca0cce457e073fe617a5327d8602.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/9e59ca0cce457e073fe617a5327d8602.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>2014 年 4 月 1 日，Spring Boot 1.0.0 正式发布。它基于“约定大于配置”（Convention over configuration）这一理念来快速地开发，测试，运行和部署 Spring 应用，并能通过简单地与各种启动器（如 spring-boot-web-starter）结合，让应用直接以命令行的方式运行，不需再部署到独立容器中。Spring Boot 的出现可以说是 Spring 框架的第二春，它不但简化了开发的流程，目前更是事实标准。下面这幅图可以看出相同功能的 Spring 和 Spring Boot 的代码实现对比。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/8cba4c14301dc70fc3b36db3bc0b72fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/8cba4c14301dc70fc3b36db3bc0b72fd.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Apache RocketMQ 是一款是业界知名的分布式消息和流处理中间件，它主要功能是消息分发、异步解耦、削峰填谷等。RocketMQ 是一款金融级消息及流数据平台，RocketMQ 在交易、支付链路上用的很多，主要是对消息链路质量要求非常高的场景，能够支持万亿级消息洪峰。RocketMQ 在业务消息中被广泛应用，并衍生出顺序消息、事务消息、延迟消息等匹配各类业务场景的特殊消息。<br>
<br>本文的主角就是 Spring 和 RocketMQ，那几乎每个 Java 程序员都会使用 Spring 框架与支持丰富业务场景的 RocketMQ 会碰撞出怎么样的火花？<br>
<br><h1>RocketMQ 与 Spring 的碰撞</h1>在介绍 RocketMQ 与 Spring 故事之前，不得不提到 Spring 中的两个关于消息的框架，Spring Messaging 和 Spring Cloud Stream。它们都能够与 Spring Boot 整合并提供了一些参考的实现。和所有的实现框架一样，消息框架的目的是实现轻量级的消息驱动的微服务，可以有效地简化开发人员对消息中间件的使用复杂度，让系统开发人员可以有更多的精力关注于核心业务逻辑的处理。<br>
<br><h2>1. Spring Messaging</h2>Spring Messaging 是 Spring Framework 4 中添加的模块，是 Spring 与消息系统集成的一个扩展性的支持。它实现了从基于 JmsTemplate 的简单的使用 JMS 接口到异步接收消息的一整套完整的基础架构，Spring AMQP 提供了该协议所要求的类似的功能集。在与 Spring Boot 的集成后，它拥有了自动配置能力，能够在测试和运行时与相应的消息传递系统进行集成。<br>
<br>单纯对于客户端而言，Spring Messaging 提供了一套抽象的 API 或者说是约定的标准，对消息发送端和消息接收端的模式进行规定，比如消息 Messaging 对应的模型就包括一个消息体 Payload 和消息头 Header。不同的消息中间件提供商可以在这个模式下提供自己的 Spring 实现：在消息发送端需要实现的是一个 XXXTemplate 形式的 Java Bean，结合 Spring Boot 的自动化配置选项提供多个不同的发送消息方法；在消息的消费端是一个 XXXMessageListener 接口（实现方式通常会使用一个注解来声明一个消息驱动的 POJO），提供回调方法来监听和消费消息，这个接口同样可以使用 Spring Boot 的自动化选项和一些定制化的属性。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/0ff8d7a8aeb0956fa89beccf5225d116.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/0ff8d7a8aeb0956fa89beccf5225d116.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>在 Apache RocketMQ 生态中，RocketMQ-Spring-Boot-Starter（下文简称 RocketMQ-Spring）就是一个支持 Spring Messaging API 标准的项目。该项目把 RocketMQ 的客户端使用 Spring Boot 的方式进行了封装，可以让用户通过简单的 annotation 和标准的 Spring Messaging API 编写代码来进行消息的发送和消费，也支持扩展出 RocketMQ 原生 API 来支持更加丰富的消息类型。在 RocketMQ-Spring 毕业初期，RocketMQ 社区同学请 Spring 社区的同学对 RocketMQ-Spring 代码进行 review，引出一段<a href="https://www.infoq.cn/article/G-og5V8x3BK8i4z90y6P">罗美琪（RocketMQ）和春波特（Spring Boot）故事的佳话</a>，著名 Spring 布道师 Josh Long 向国外同学介绍<a href="https://spring.io/blog/2020/02/25/spring-tips-apache-rocketmq">如何使用 RocketMQ-Spring 收发消息</a>。RocketMQ-Spring 也在短短两年时间超越 Spring-Kafka 和 Spring-AMQP（注：两者均由 Spring 社区维护），成为 Spring Messaging 生态中最活跃的消息项目。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/98afa1bbf7bddcc8c38bda0b294990a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/98afa1bbf7bddcc8c38bda0b294990a4.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>2. Spring Cloud Stream</h2>Spring Cloud Stream 结合了 Spring Integration 的注解和功能，它的应用模型如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/2b362ed6a03b4e33bd35e4bb728feeba.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/2b362ed6a03b4e33bd35e4bb728feeba.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>Spring Cloud Stream 框架中提供一个独立的应用内核，它通过输入 (@Input) 和输出 (@Output) 通道与外部世界进行通信，消息源端 (Source) 通过输入通道发送消息，消费目标端 (Sink) 通过监听输出通道来获取消费的消息。这些通道通过专用的 Binder 实现与外部代理连接。开发人员的代码只需要针对应用内核提供的固定的接口和注解方式进行编程，而不需要关心运行时具体的 Binder 绑定的消息中间件。<br>
<br>在运行时，Spring Cloud Stream 能够自动探测并使用在 classpath 下找到的 Binder。这样开发人员可以轻松地在相同的代码中使用不同类型的中间件：仅仅需要在构建时包含进不同的 Binder。在更加复杂的使用场景中，也可以在应用中打包多个 Binder 并让它自己选择 Binder，甚至在运行时为不同的通道使用不同的 Binder。 <br>
<br>Binder 抽象使得 Spring Cloud Stream 应用可以灵活的连接到中间件，加之 Spring Cloud Stream 使用利用了 Spring Boot 的灵活配置配置能力，这样的配置可以通过外部配置的属性和 Spring Boot 支持的任何形式来提供（包括应用启动参数、环境变量和 application.yml 或者 application.properties 文件），部署人员可以在运行时动态选择通道连接 destination（例如，RocketMQ 的 topic 或者 RabbitMQ 的 exchange）。<br>
<br>Spring Cloud Stream 屏蔽了底层消息中间件的实现细节，希望以统一的一套 API 来进行消息的发送/消费，底层消息中间件的实现细节由各消息中间件的 Binder 完成。Spring 官方实现了 Rabbit binder 和 Kafka Binder。<a href="https://github.com/alibaba/spring-cloud-alibaba/wiki/RocketMQ">Spring Cloud Alibaba 实现了 RocketMQ Binder</a>，其主要实现原理是把发送消息最终代理给了 RocketMQ-Spring 的 RocketMQTemplate，在消费端则内部会启动 RocketMQ-Spring Consumer Container 来接收消息。以此为基础，Spring Cloud Alibaba 还实现了 Spring Cloud Bus RocketMQ， 用户可以使用 RocketMQ 作为 Spring Cloud 体系内的消息总线，来连接分布式系统的所有节点。通过 Spring Cloud Stream RocketMQ Binder，RocketMQ 可以与 Spring Cloud 生态更好的结合。比如与 Spring Cloud Data Flow、Spring Cloud Funtion 结合，让 RocketMQ 可以在 Spring 流计算生态、Serverless(FaaS) 项目中被使用。<br>
<br>如今 Spring Cloud Stream RocketMQ Binder 和 Spring Cloud Bus RocketMQ 作为 Spring Cloud Alibaba 的实现<a href="https://spring.io/projects/spring-cloud-alibaba">已登陆 Spring 的官网</a>，Spring Cloud Alibaba 也成为 Spring Cloud 最活跃的实现。<br>
<br><h1>如何在 Spring 生态中选择 RocketMQ 实现？</h1>通过介绍 Spring 中的消息框架，介绍了以 RocketMQ 为基础与 Spring 消息框架结合的几个项目，主要是 RocketMQ-Spring、Spring Cloud Stream RocketMQ Binder、Spring Cloud Bus RocketMQ、Spring Data Flow 和 Spring Cloud Function。它们之间的关系可以如下图表示。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210319/e88be8a900082a282f4be75b9c1a934f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210319/e88be8a900082a282f4be75b9c1a934f.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>如何在实际业务开发中选择相应项目进行使用？下面分别列出每个项目的特点和使用场景。<br>
<br><h2>1. RocketMQ-Spring</h2>特点：<br>
<ul><li><br>作为起步依赖，简单引入一个包就能在 Spring 生态用到 RocketMQ 客户端的所有功能。</li><li><br>利用了大量自动配置和注解简化了编程模型，并且支持 Spring Messaging API。</li><li><br>与 RocketMQ 原生 Java SDK 的功能完全对齐。</li></ul><br>
<br>使用场景：<br>
<ul><li>适合在 Spring Boot 中使用 RocketMQ 的用户，希望能用到 RocketMQ 原生 java 客户端的所有功能，并通过 Spring 注解和自动配置简化编程模型。</li></ul><br>
<br><h2>2. Spring Cloud Stream RocketMQ Binder</h2>特点：<br>
<ul><li><br>屏蔽底层 MQ 实现细节，上层 Spring Cloud Stream 的 API 是统一的。如果想从 Kafka 切到 RocketMQ，直接改个配置即可。</li><li><br>与 Spring Cloud 生态整合更加方便。比如 Spring Cloud Data Flow，这上面的流计算都是基于 Spring Cloud Stream；Spring Cloud Bus 消息总线内部也是用的 Spring Cloud Stream。</li><li><br>Spring Cloud Stream 提供的注解，编程体验都是非常棒。</li></ul><br>
<br>使用场景：<br>
<ul><li>在代码层面能完全屏蔽底层消息中间件的用户，并且希望能项目能更好的接入 Spring Cloud 生态（Spring Cloud Data Flow、Spring Cloud Funtcion等）。</li></ul><br>
<br><h2>3. Spring Cloud Bus RocketMQ</h2>特点：<br>
<ul><li>将 RocketMQ 作为事件的“传输器”，通过发送事件（消息）到消息队列上，从而广播到订阅该事件（消息）的所有节点上，完成事件的分发和通知。</li></ul><br>
<br>使用场景：<br>
<ul><li>在 Spring 生态中希望用 RocketMQ 做消息总线的用户，可以用在应用间事件的通信，配置中心客户端刷新等场景。</li></ul><br>
<br><h2>4. Spring Cloud Data Flow</h2>特点：<br>
<ul><li>以 Source/Processor/Sink 组件进行流式任务处理。RocketMQ 作为流处理过程中的中间存储组件。</li></ul><br>
<br>使用场景：<br>
<ul><li>流处理，大数据处理场景。</li></ul><br>
<br><h2>5. Spring Cloud Function</h2>特点：<br>
<ul><li>消息的消费/生产/处理都是一次函数调用，融合 Java 生态的 Function 模型。</li></ul><br>
<br>使用场景：<br>
<ul><li>Serverless 场景。</li></ul><br>
<br>本文整体介绍了在 Spring 生态中接入 RockeMQ 的 5 种方法，让各位开发者对几种经典场景有宏观的了解。后续会有专栏详细介绍上述各个项目的具体使用方法和应用场景，真正地在 Spring 生态中玩转 RocketMQ！
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            