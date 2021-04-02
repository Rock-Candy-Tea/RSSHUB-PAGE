
---
title: 'EasyDomain v1.2 发布，领域驱动开发实用库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/lixiaojing/easy-domain/raw/master/easy-domainevent-rocketmq/domainevent.png'
author: 开源中国
comments: false
date: Fri, 02 Apr 2021 15:55:00 GMT
thumbnail: 'https://gitee.com/lixiaojing/easy-domain/raw/master/easy-domainevent-rocketmq/domainevent.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>EasyDomain v1.2 已经发布，这是一个领域驱动开发实用库。</p> 
<p>此版本更新内容包括：</p> 
<h1>基于RocketMQ实现的领域事件发布订阅能力</h1> 
<h2>功能介绍</h2> 
<p>基于RocketMQ的领域事件发布订阅组件，充分借助了RocketMQ可靠性能力、消息持久化能力、消息回溯能力以及分布式处理能力。同时，便于问题的排查。该组件规避了使用线程池方式领域事件发布订阅能力缺陷。该组件实现了IDomainEventManager接口，可以无缝的在基于线程池发布订阅组件和基于RocketMQ发布订阅之间切换使用，并且发布和订阅的相关业务代码无需修改。</p> 
<blockquote> 
 <p>领域事件、以及发布订阅的能力，属于一个应用内部的运行逻辑，用于领域事件的topic,一般情况下不应该被外部系统消费。如果，外部应用需要接受一个消息来触发相关的操作，那么可以单独创建一个供外部系统使用的topic,系统内部相关的领域事件，可以增加一个领域事件订阅，用于发送供外部系统使用的消息。</p> 
</blockquote> 
<p><img alt="领域事件示意" src="https://gitee.com/lixiaojing/easy-domain/raw/master/easy-domainevent-rocketmq/domainevent.png" referrerpolicy="no-referrer"></p> 
<h2>版本说明</h2> 
<ul> 
 <li>RocketMQ版本：4.7.1</li> 
 <li>JAVA：1.8</li> 
</ul> 
<h2>Maven</h2> 
<p>编辑您的pom.xml文件</p> 
<pre><code>
<profiles>
    <profile>
        <id>coding</id>
        <repositories>
            <repository>
                <id>leebmw-easy-snapshoot</id>
                <name>snapshoot</name>
                <url>https://leebmw-maven.pkg.coding.net/repository/easy/snapshoot/</url>
                <releases>
                    <enabled>true</enabled>
                </releases>
                <snapshots>
                    <enabled>true</enabled>
                </snapshots>
            </repository>
        </repositories>
    </profile>
</profiles>
</code></pre> 
<p>编辑您的 pom.xml 文件</p> 
<pre><code>
<dependency>
    <groupId>easy-domain</groupId>
    <artifactId>easy-domainevent-rocketmq</artifactId>
    <version>1.0</version>
</dependency>
</code></pre> 
<h2>使用方法</h2> 
<ol> 
 <li>应用服务层服务类的父类构造函数接受一个IDomainEventManager接口实现，RocketMQ领域事件发布订阅组件实现了该接口。无参数的构造函数默认使用基于线程池的组件。以下代码 1 、2处</li> 
</ol> 
<pre><code>public abstract class BaseApplication implements IApplication &#123;

    private final IDomainEventManager manager;

    /**
     * 1
     * 使用默认 事件处理器的构造函数
     */
    protected BaseApplication() &#123;
        this.manager = new ThreadPoolTaskDomainEventManager();
    &#125;

    /**
     * 2
     * 带事件处理器的构造函数
     *
     * @param manager 事件处理器
     */
    protected BaseApplication(IDomainEventManager manager) &#123;
        this.manager = manager;
    &#125;
    ....无关代码省略
&#125;
</code></pre> 
<ol start="2"> 
 <li> </li> 
</ol> 
<p>使用RocketMQ领域事件发布订阅组件需要实例化RocketMqDomainEventManager类。该类接受三个参数分别是IProducerCreator、IConsumerCreator、environmentName。以下代码 1 处</p> 
<pre><code>public class RocketMqDomainEventManager implements IDomainEventManager, MessageListenerConcurrently &#123;
    //1
    public RocketMqDomainEventManager(IProducerCreator producerCreator, IConsumerCreator consumerCreator, String environmentName) &#123;
        this.mqProducer = producerCreator.create();
        this.consumer = consumerCreator.create();
        this.environmentName = (environmentName == null || environmentName.equals("")) ? "prod" : environmentName;

        this.initConsumer();
    &#125;
       ....无关代码省略
&#125;
</code></pre> 
<ul> 
 <li>IProducerCreator接口用于创建RocketMQ的生产者实例，ProducerCreator类是默认的实现类。可以根据具体的情况重新实现IProducerCreator接口，以满足特定的环境。</li> 
 <li>IConsumerCreator接口用于创建RocketMQ的消费者实例，ConsumerCreator类是默认的实现类。可以根据具体的情况重新实现IConsumerCreator接口，以满足特定的环境。</li> 
 <li>environmentName参数，用于实现消息的环境隔离（如，生产环境和灰度环境的消息隔离），当使用该参数是，RocketMQ的topic名字由 environmentName_<事件名称> 组成。</li> 
</ul> 
<p>3.事件的注册需要调用registerDomainEvent方法。见代码1处。</p> 
<pre><code>private void initSubscriber()&#123;
        // 1
        this.registerDomainEvent(MyDomainEvent.class);

        this.registerSubscriber(factory.build(MyDomainEvent.class,s->&#123;
        this.countDownLatch.countDown();

        System.out.println("执行相应的操作");

        &#125;),"test1");
        &#125;
</code></pre> 
<ol start="4"> 
 <li>事件的订阅可以使用RocketmqSubscriberFactory类来创建，该类实现了ISubscriberFactory接口</li> 
</ol> 
<pre><code>        RocketmqSubscriberFactory factory=new RocketmqSubscriberFactory();
        this.registerSubscriber(factory.build(MyDomainEvent.class,s->&#123;
        this.countDownLatch.countDown();
        System.out.println("执行相应的操作");
        &#125;),"test1");

</code></pre> 
<ol start="5"> 
 <li>定义领域事件类</li> 
</ol> 
<pre><code>
@EventName(value = "ShareDomainEvent", shareTopicName = "SharedTopic")
public class ShareDomainEvent extends BaseDomainEvent &#123;
   ...省略无关代码
&#125;
</code></pre> 
<ul> 
 <li>@EventName注解 是可选项，如果不设置，需要在RocketMQ中创建和类名一样的Topic,如："ShareDomainEvent"</li> 
 <li>指定@EventName注解，value值必须设置，设置value后，value的值是RocketMQ对应的Topic。</li> 
 <li>shareTopicName 是可选项，该值用于多个事件共用一个RocketMQ的Topic,可以在多个领域事件类中指定相同shareTopicName值。</li> 
 <li>领域事件是一个业务上的概念，它是由领域实体状态变化产生的，对领域事件的命名上应更多的体现业务含义。领域事件和领域实体紧密相连，领域事件类应和领域实体类放在相同模块或包里。</li> 
</ul> 
<pre><code>这里输入代码
</code></pre> 
<p>详情查看：<a href="https://gitee.com/lixiaojing/easy-domain/releases/v1.2">https://gitee.com/lixiaojing/easy-domain/releases/v1.2</a></p>
                                        </div>
                                      
</div>
            