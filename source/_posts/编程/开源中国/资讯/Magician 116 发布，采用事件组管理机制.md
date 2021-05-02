
---
title: 'Magician 1.1.6 发布，采用事件组管理机制'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-aab00f1bf563cd0c741fca786826acf92f0.png'
author: 开源中国
comments: false
date: Sun, 02 May 2021 11:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-aab00f1bf563cd0c741fca786826acf92f0.png'
---

<div>   
<div class="content">
                                                                                            <p>Magician 1.1.6，作为第一个正式的版本，内部对NIO的实现部分做了大量优化与重构，采用了事件组管理机制，具体模型如下图所示：</p> 
<p><img alt height="463" src="https://oscimg.oschina.net/oscnet/up-aab00f1bf563cd0c741fca786826acf92f0.png" width="798" referrerpolicy="no-referrer"></p> 
<p>采用了两个事件组来进行事件和线程池的管理，一个叫ioEventGroup，一个叫workerEventGroup，都是通过EventGroup类创建。 每个EventGroup 都对应一个EventRunner，每个EventRunner对应一个任务队列，可以管理多个事件。  当队列空了以后，可以去其他的EventRunner窃取任务，不会造成资源浪费。</p> 
<p>ioEventGroup是用来管理Selector的，一个端口对应一个EventRunner里的一个事件，也就是说如果要监听多个端口就需要在ioEventGroup初始化多个EventRunner，这么做是因为EventRunner是按顺序消费事件的，如果多个监听事件都给一个EventRunner管理，可能会执行不到后面的事件，因为Selector是一个死循环 他会一直占用当前线程。</p> 
<p>workerEventGroup是用来管理 业务事件的，一个连接对应一个EventRunner，一个EventRunner对应多个连接，当连接里有了read事件就会往EventRunner里添加一个事件，EventRunner会按顺序消费这些事件，在消费时 如果发现协议报文不完整会立刻停止该事件 继续执行下一个，如果报文完整会调用handler执行业务逻辑。 建议按照CPU的核心数来合理的设置workerEventGroup里的EventRunner数量。</p> 
<h2>具体如何使用</h2> 
<h2 style="text-align:start">一、创建TCP服务(默认使用http解码器)</h2> 
<h3 style="text-align:start">创建Handler</h3> 
<div style="text-align:start"> 
 <pre><code class="language-java">public class DemoHandler implements MagicianHandler<MagicianRequest> &#123;

    @Override
    public void request(MagicianRequest magicianRequest) &#123;
        // 响应数据
        magicianRequest.getResponse()
                .sendJson(200, "&#123;'status':'ok'&#125;");
    &#125;
&#125;</code></pre> 
 <h3>创建服务(默认线程池配置)</h3> 
</div> 
<div style="text-align:start"> 
 <pre><code class="language-java">Magician.createTCPServer()
                    .httpHandler("/", new DemoHandler())
                    .bind(8080);</code></pre> 
 <h3>创建服务(自定义线程池配置)</h3> 
</div> 
<div style="text-align:start"> 
 <pre><code class="language-java">EventGroup ioEventGroup = new EventGroup(1, Executors.newCachedThreadPool());
EventGroup workerEventGroup = new EventGroup(10, Executors.newCachedThreadPool());

// 当前EventRunner没任务的时候，允许从其他EventRunner窃取任务
workerEventGroup.setSteal(EventEnum.STEAL.YES);

Magician.createTCPServer(ioEventGroup, workerEventGroup)
                    .httpHandler("/", new DemoHandler())
                    .bind(8080);</code></pre> 
 <h3>创建服务(监听多端口)</h3> 
</div> 
<div style="text-align:start"> 
 <pre><code class="language-java">// 监听几个端口，ioEventGroup的第一个参数就写几
EventGroup ioEventGroup = new EventGroup(2, Executors.newCachedThreadPool());
EventGroup workerEventGroup = new EventGroup(10, Executors.newCachedThreadPool());

// 当前EventRunner没任务的时候，允许从其他EventRunner窃取任务
workerEventGroup.setSteal(EventEnum.STEAL.YES);

TCPServer tcpServer = Magician
                         .createTCPServer(ioEventGroup, workerEventGroup)
                         .httpHandler("/", new DemoHandler())

tcpServer.bind(8080);
tcpServer.bind(8088);</code></pre> 
 <h2>二、创建WebSocket</h2> 
</div> 
<p style="text-align:start">只需要在创建http服务的时候加一个handler即可</p> 
<div style="text-align:start"> 
 <pre><code class="language-java">Magician.createTCPServer()
                    .httpHandler("/", new DemoHandler())
                    .webSocketHandler("/websocket", new DemoSocketHandler())
                    .bind(8080);</code></pre> 
 <h2>三、创建UDP服务</h2> 
</div> 
<div style="text-align:start"> 
 <pre><code class="language-java">Magician.createTCPServer()
                    .httpHandler("/", new DemoHandler())
                    .webSocketHandler("/websocket", new DemoSocketHandler())
                    .bind(8080);</code></pre> 
 <p>除了这种写法，也可以单独创建handler，在这里add进去</p> 
 <p>官网：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmagician-io.com%2F" target="_blank">http://magician-io.com/</a></p> 
</div>
                                        </div>
                                      
</div>
            