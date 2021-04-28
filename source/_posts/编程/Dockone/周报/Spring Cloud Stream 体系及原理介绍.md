
---
title: 'Spring Cloud Stream 体系及原理介绍'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/9c5c4b05b4204ed4be1bf22688ad3731.png'
author: Dockone
comments: false
date: 2021-04-28 08:08:43
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/9c5c4b05b4204ed4be1bf22688ad3731.png'
---

<div>   
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/9c5c4b05b4204ed4be1bf22688ad3731.png" alt="头图.png" referrerpolicy="no-referrer"><br>
<br>作者 | 洛夜<br>
来源 | <a href="https://mp.weixin.qq.com/s/D_rTQO0hiLduPvqO3T9THA">阿里巴巴云原生公众号</a><br>
<br><strong>Spring Cloud Stream</strong>在 Spring Cloud 体系内用于构建高度可扩展的基于事件驱动的微服务，其目的是为了简化消息在 Spring Cloud 应用程序中的开发。<br>
<br>Spring Cloud Stream (后面以 SCS 代替 Spring Cloud Stream) 本身内容很多，而且它还有很多外部的依赖，想要熟悉 SCS，必须要先了解 Spring Messaging 和 Spring Integration 这两个项目，接下来，文章将围绕以下三点进行展开：<br>
<ul><li>什么是 Spring Messaging</li><li>什么是 Spring Integration</li><li>什么是 SCS 体系及其原理</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/ae062a3cef02de353eee36519b78b341.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/ae062a3cef02de353eee36519b78b341.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>本文配套可交互教程已登录阿里云知行动手实验室，PC 端登录 <a href="https://start.aliyun.com/">_start.aliyun.com_</a>_ _在浏览器中立即体验。<br>
<br><h1>Spring Messaging</h1>Spring Messaging 是 Spring Framework 中的一个模块，其作用就是统一消息的编程模型。<br>
<ul><li>比如消息 Messaging 对应的模型就包括一个消息体 Payload 和消息头 Header：</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/42e39bf17c86e16cdd1678eaeb5ed0c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/42e39bf17c86e16cdd1678eaeb5ed0c4.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><code class="prettyprint">package org.springframework.messaging;<br>
public interface Message&lt;T> &#123;<br>
    T getPayload();<br>
    MessageHeaders getHeaders();<br>
&#125;</code><br>
<ul><li>消息通道 MessageChannel 用于接收消息，调用send方法可以将消息发送至该消息通道中：</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/51adf61ea01ebbcf1be883640d608f58.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/51adf61ea01ebbcf1be883640d608f58.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>```<br>
@FunctionalInterface<br>
public interface MessageChannel &#123;<br>
    long INDEFINITE_TIMEOUT = -1;<br>
    default boolean send(Message<?> message) &#123;<br>
<br>         return send(message, INDEFINITE_TIMEOUT);<br>
<br>     &#125;<br>
     boolean send(Message<?> message, long timeout);<br>
&#125;<br>
```<br>
<br><h4>消息通道里的消息如何被消费呢？</h4><ul><li>由消息通道的子接口可订阅的消息通道SubscribableChannel实现，被MessageHandler消息处理器所订阅：</li></ul><br>
<br><code class="prettyprint">public interface SubscribableChannel extends MessageChannel &#123;<br>
    boolean subscribe(MessageHandler handler);<br>
    boolean unsubscribe(MessageHandler handler);<br>
&#125;</code><br>
<ul><li>由MessageHandler真正地消费/处理消息：</li></ul><br>
<br><code class="prettyprint">@FunctionalInterface<br>
public interface MessageHandler &#123;<br>
    void handleMessage(Message&lt;?> message) throws MessagingException;<br>
&#125;</code><br>
<br><h4>Spring Messaging 内部在消息模型的基础上衍生出了其它的一些功能，如：</h4><ul><li>消息接收参数及返回值处理：消息接收参数处理器HandlerMethodArgumentResolver配合@Header, @Payload等注解使用；消息接收后的返回值处理器HandlerMethodReturnValueHandler配合@SendTo注解使用；</li><li>消息体内容转换器MessageConverter；</li><li>统一抽象的消息发送模板AbstractMessageSendingTemplate；</li><li>消息通道拦截器ChannelInterceptor；</li></ul><br>
<br><h1>Spring Integration</h1>Spring Integration 提供了 Spring 编程模型的扩展用来支持企业集成模式(Enterprise Integration Patterns)，是对 Spring Messaging 的扩展。<br>
<br>它提出了不少新的概念，包括消息路由MessageRoute、消息分发MessageDispatcher、消息过滤Filter、消息转换Transformer、消息聚合Aggregator、消息分割Splitter等等。同时还提供了MessageChannel和MessageHandler的实现，分别包括 DirectChannel、ExecutorChannel、PublishSubscribeChannel和MessageFilter、ServiceActivatingHandler、MethodInvokingSplitter 等内容。<br>
<br><h4>这里为大家介绍几种消息的处理方式：</h4><ul><li>消息的分割：</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/7159d7dbaa6084dfeaf7b3a4cb837209.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/7159d7dbaa6084dfeaf7b3a4cb837209.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>消息的聚合：</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/08fce38074d9a211dd961456b0c638c5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/08fce38074d9a211dd961456b0c638c5.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>消息的过滤：</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/13ed55be433160b678ca6eca9f2bc01c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/13ed55be433160b678ca6eca9f2bc01c.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>消息的分发：</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/2fc1b02152591185cd0fcac315d7444d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/2fc1b02152591185cd0fcac315d7444d.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h4>接下来，我们以一个最简单的例子来尝试一下 Spring Integration。</h4>这段代码解释为：<br>
<br>```<br>
SubscribableChannel messageChannel =new DirectChannel(); // 1<br>
<br>messageChannel.subscribe(msg-> &#123; // 2<br>
 System.out.println("receive: " +msg.getPayload());<br>
&#125;);<br>
<br>messageChannel.send(MessageBuilder.withPayload("msgfrom alibaba").build()); // 3<br>
```<br>
<ul><li>构造一个可订阅的消息通道messageChannel。</li><li>使用MessageHandler去消费这个消息通道里的消息。</li><li>发送一条消息到这个消息通道，消息最终被消息通道里的MessageHandler所消费。</li><li>最后控制台打印出:receive: msg from alibaba。</li></ul><br>
<br>DirectChannel内部有个UnicastingDispatcher类型的消息分发器，会分发到对应的消息通道MessageChannel中，从名字也可以看出来，UnicastingDispatcher是个单播的分发器，只能选择一个消息通道。那么如何选择呢? 内部提供了LoadBalancingStrategy负载均衡策略，默认只有轮询的实现，可以进行扩展。<br>
<br>我们对上段代码做一点修改，使用多个 MessageHandler 去处理消息：<br>
<br>```<br>
SubscribableChannel messageChannel = new DirectChannel();<br>
<br>messageChannel.subscribe(msg -> &#123;<br>
     System.out.println("receive1: " + msg.getPayload());<br>
&#125;);<br>
<br>messageChannel.subscribe(msg -> &#123;<br>
     System.out.println("receive2: " + msg.getPayload());<br>
&#125;);<br>
<br>messageChannel.send(MessageBuilder.withPayload("msg from alibaba").build());<br>
messageChannel.send(MessageBuilder.withPayload("msg from alibaba").build());<br>
```<br>
<br>由于DirectChannel内部的消息分发器是UnicastingDispatcher单播的方式，并且采用轮询的负载均衡策略，所以这里两次的消费分别对应这两个MessageHandler。控制台打印出：<br>
<br><code class="prettyprint">receive1: msg from alibaba<br>
receive2: msg from alibaba</code><br>
<br>既然存在单播的消息分发器UnicastingDispatcher，必然也会存在广播的消息分发器，那就是BroadcastingDispatcher，它被 PublishSubscribeChannel 这个消息通道所使用。广播消息分发器会把消息分发给所有的 MessageHandler：<br>
<br>```<br>
SubscribableChannel messageChannel = new PublishSubscribeChannel();<br>
<br>messageChannel.subscribe(msg -> &#123;<br>
     System.out.println("receive1: " + msg.getPayload());<br>
&#125;);<br>
<br>messageChannel.subscribe(msg -> &#123;<br>
     System.out.println("receive2: " + msg.getPayload());<br>
&#125;);<br>
<br>messageChannel.send(MessageBuilder.withPayload("msg from alibaba").build());<br>
messageChannel.send(MessageBuilder.withPayload("msg from alibaba").build());<br>
```<br>
<br><h1>Spring Cloud Stream</h1><h4>SCS 与各模块之间的关系是：</h4><ul><li>SCS 在 Spring Integration 的基础上进行了封装，提出了Binder, Binding, @EnableBinding, @StreamListener等概念。</li><li>SCS 与 Spring Boot Actuator 整合，提供了/bindings, /channelsendpoint。</li><li>SCS 与 Spring Boot Externalized Configuration 整合，提供了BindingProperties, BinderProperties等外部化配置类。</li><li>SCS 增强了消息发送失败的和消费失败情况下的处理逻辑等功能。</li><li>SCS 是 Spring Integration 的加强，同时与 Spring Boot 体系进行了融合，也是 Spring Cloud Bus 的基础。它屏蔽了底层消息中间件的实现细节，希望以统一的一套 API 来进行消息的发送/消费，底层消息中间件的实现细节由各消息中间件的 Binder 完成。</li></ul><br>
<br>Binder是提供与外部消息中间件集成的组件，为构造Binding提供了 2 个方法，分别是bindConsumer和bindProducer，它们分别用于构造生产者和消费者。目前官方的实现有 Rabbit Binder 和 Kafka Binder， Spring Cloud Alibaba 内部已经实现了 RocketMQ Binder。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/bb470e9aa908f9fb5c2ae9cf55de9382.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/bb470e9aa908f9fb5c2ae9cf55de9382.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>从图中可以看出，Binding是连接应用程序跟消息中间件的桥梁，用于消息的消费和生产。我们来看一个最简单的使用 RocketMQ Binder 的例子，然后分析一下它的底层处理原理：<br>
<ul><li>启动类及消息的发送：</li></ul><br>
<br>```<br>
@SpringBootApplication<br>
@EnableBinding(&#123; Source.class, Sink.class &#125;) // 1<br>
public class SendAndReceiveApplication &#123;<br>
<br>    public static void main(String[] args) &#123;<br>
        SpringApplication.run(SendAndReceiveApplication.class, args);<br>
    &#125;<br>
<br>       @Bean // 2<br>
    public CustomRunner customRunner() &#123;<br>
        return new CustomRunner();<br>
    &#125;<br>
<br>    public static class CustomRunner implements CommandLineRunner &#123;<br>
<br>        @Autowired<br>
        private Source source;<br>
<br>        @Override<br>
        public void run(String... args) throws Exception &#123;<br>
            int count = 5;<br>
            for (int index = 1; index <= count; index++) &#123;<br>
                source.output().send(MessageBuilder.withPayload("msg-" + index).build()); // 3<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
```<br>
<ul><li>消息的接收：</li></ul><br>
<br>```<br>
@Service<br>
public class StreamListenerReceiveService &#123;<br>
<br>    @StreamListener(Sink.INPUT) // 4<br>
    public void receiveByStreamListener1(String receiveMsg) &#123;<br>
        System.out.println("receiveByStreamListener: " + receiveMsg);<br>
    &#125;<br>
<br>&#125;<br>
```<br>
<br>这段代码很简单，没有涉及到 RocketMQ 相关的代码，消息的发送和接收都是基于 SCS 体系完成的。如果想切换成 RabbitMQ 或 Kafka，只需修改配置文件即可，代码无需修改。<br>
<br>我们来分析下这段代码的原理：<br>
<br>1.@EnableBinding对应的两个接口属性Source和Sink是 SCS 内部提供的。SCS 内部会基于Source和Sink构造BindableProxyFactory，且对应的 output 和 input 方法返回的 MessageChannel 是DirectChannel。output 和 input 方法修饰的注解对应的 value 是配置文件中 binding 的 name。<br>
<br><code class="prettyprint">public interface Source &#123;<br>
    String OUTPUT = &quot;output&quot;;<br>
    @Output(Source.OUTPUT)<br>
    MessageChannel output();<br>
&#125;<br>
public interface Sink &#123;<br>
    String INPUT = &quot;input&quot;;<br>
    @Input(Sink.INPUT)<br>
    SubscribableChannel input();<br>
&#125;</code><br>
<br>配置文件里 bindings 的 name 为 output 和 input，对应Source和Sink接口的方法上的注解里的 value：<br>
<br>```<br>
spring.cloud.stream.bindings.output.destination=test-topic<br>
spring.cloud.stream.bindings.output.content-type=text/plain<br>
spring.cloud.stream.rocketmq.bindings.output.producer.group=demo-group<br>
<br>spring.cloud.stream.bindings.input.destination=test-topic<br>
spring.cloud.stream.bindings.input.content-type=text/plain<br>
spring.cloud.stream.bindings.input.group=test-group1<br>
```<br>
<ol><li><br>构造CommandLineRunner，程序启动的时候会执行CustomRunner的run方法。</li><li><br>调用Source接口里的 output 方法获取DirectChannel，并发送消息到这个消息通道中。这里跟之前 Spring Integration 章节里的代码一致。<br>
<ul><li>Source 里的 output 发送消息到DirectChannel消息通道之后会被AbstractMessageChannelBinder#SendingHandler这个MessageHandler处理，然后它会委托给AbstractMessageChannelBinder#createProducerMessageHandler创建的 MessageHandler 处理(该方法由不同的消息中间件实现)。</li><li>不同的消息中间件对应的AbstractMessageChannelBinder#createProducerMessageHandler方法返回的 MessageHandler 内部会把 Spring Message 转换成对应中间件的 Message 模型并发送到对应中间件的 broker。</li></ul></li><li><br>使用@StreamListener进行消息的订阅。请注意，注解里的Sink.input对应的值是 "input"，会根据配置文件里 binding 对应的 name 为 input 的值进行配置：<br>
<ul><li>不同的消息中间件对应的AbstractMessageChannelBinder#createConsumerEndpoint方法会使用 Consumer 订阅消息，订阅到消息后内部会把中间件对应的 Message 模型转换成 Spring Message。</li><li>消息转换之后会把 Spring Message 发送至 name 为 input 的消息通道中。</li><li>@StreamListener对应的StreamListenerMessageHandler订阅了 name 为 input 的消息通道，进行了消息的消费。</li></ul></li></ol><br>
<br>这个过程文字描述有点啰嗦，用一张图总结一下(黄色部分涉及到各消息中间件的 Binder 实现以及 MQ 基本的订阅发布功能)：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/3b7ef5b22b1072e30c73cbe23f81af1d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/3b7ef5b22b1072e30c73cbe23f81af1d.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h4>SCS 章节的最后，我们来看一段 SCS 关于消息的处理方式的一段代码：</h4>```<br>
@StreamListener(value = Sink.INPUT, condition = "headers['index']=='1'")<br>
public void receiveByHeader(Message msg) &#123;<br>
     System.out.println("receive by headers['index']=='1': " + msg);<br>
&#125;<br>
<br>@StreamListener(value = Sink.INPUT, condition = "headers['index']=='9999'")<br>
public void receivePerson(@Payload Person person) &#123;<br>
     System.out.println("receive Person: " + person);<br>
&#125;<br>
<br>@StreamListener(value = Sink.INPUT)<br>
public void receiveAllMsg(String msg) &#123;<br>
     System.out.println("receive allMsg by StreamListener. content: " + msg);<br>
&#125;<br>
<br>@StreamListener(value = Sink.INPUT)<br>
public void receiveHeaderAndMsg(@Header("index") String index, Message msg) &#123;<br>
     System.out.println("receive by HeaderAndMsg by StreamListener. content: " + msg);<br>
&#125;<br>
```<br>
<br>有没有发现这段代码跟 Spring MVC Controller 中接收请求的代码很像? 实际上他们的架构都是类似的，Spring MVC 对于 Controller 中参数和返回值的处理类分别是org.springframework.web.method.support.HandlerMethodArgumentResolver、org.springframework.web.method.support.HandlerMethodReturnValueHandler。<br>
<br>Spring Messaging 中对于参数和返回值的处理类之前也提到过，分别是org.springframework.messaging.handler.invocation.HandlerMethodArgumentResolver、org.springframework.messaging.handler.invocation.HandlerMethodReturnValueHandler。<br>
<br>它们的类名一模一样，甚至内部的方法名也一样。<br>
<br><h1>总结</h1><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/ddf3c21d6f3daff19b940f8306317e9a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210428/ddf3c21d6f3daff19b940f8306317e9a.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>上图是 SCS 体系相关类说明的总结，关于 SCS 以及 RocketMQ Binder 更多相关的示例，可以参考 <a href="https://github.com/fangjian0423/rocketmq-binder-demo">RocketMQ Binder Demos</a>，包含了消息的聚合、分割、过滤；消息异常处理；消息标签、SQL 过滤；同步、异步消费等等。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            