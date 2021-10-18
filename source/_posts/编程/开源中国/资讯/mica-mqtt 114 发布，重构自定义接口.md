
---
title: 'mica-mqtt 1.1.4 发布，重构自定义接口'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5805d01baf336f1081505d0e0d39c7790de.png'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 09:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5805d01baf336f1081505d0e0d39c7790de.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0"><span>一、简介</span></h2> 
<p style="margin-left:0; margin-right:0"><strong><span>mica-mqtt</span></strong><span> 基于 </span><strong><span>t-io</span></strong><span> 实现的</span><strong><span>简单</span></strong><span>、</span><strong><span>低延迟</span></strong><span>、</span><strong><span>高性能</span></strong><span> 的 mqtt 物联网开源组件。</span><strong><span>使用详见 mica-mqtt gitee 源码</span></strong><span> </span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-example" target="_blank"><span>mica-mqtt-example 模块</span></a><span>。</span></p> 
<p style="margin-left:0; margin-right:0"><strong><span>mica-mqtt</span></strong><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></p> 
<h2 style="margin-left:0; margin-right:0"><span>二、功能</span></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span>✅</span><span>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></li> 
 <li><span>✅</span><span>支持 websocket mqtt 子协议（支持 mqtt.js）。</span> </li> 
 <li><span>✅</span><span>支持 http rest api，</span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md" target="_blank"><span>http api 文档详见</span></a><span>。</span></li> 
 <li><span>✅</span><span>支持 MQTT client 客户端。</span></li> 
 <li><span>✅</span><span>支持 MQTT server 服务端。</span></li> 
 <li><span>✅</span><span>支持 MQTT 遗嘱消息。</span> </li> 
 <li><span>✅</span><span>支持 MQTT 保留消息。</span></li> 
 <li><span>✅</span><span>支持自定义消息（mq）处理转发实现集群。</span></li> 
 <li><span>✅</span><span>MQTT 客户端 阿里云 mqtt 连接 demo。</span></li> 
 <li><span>✅</span><span>支持 GraalVM 编译成本机可执行程序。</span> </li> 
 <li><span>✅</span><span>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></li> 
 <li><span>✅</span><span>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></li> 
 <li><span>✅</span><span>基于 redis pub/sub 实现集群，详见 </span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker" target="_blank"><span>mica-mqtt-broker 模块</span></a><span>。</span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"><span>三、待办</span></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span>🔲</span><span>优化处理 mqtt session，以及支持部分 mqtt v5.0 新特性。</span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"><span>四、更新记录</span></h2> 
<h3 style="margin-left:0; margin-right:0"><span>1.1.4</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span>✨ 添加 IMqttServerUniqueIdService 接口，用来处理 clientId 不唯一的场景。详见：gitee </span><a href="https://gitee.com/596392912/mica-mqtt/issues/I4DXQU" target="_blank"><span>#I4DXQU</span></a></li> 
 <li><span>✨ 微调 IMqttServerAuthHandler 认证，添加 uniqueId 参数。</span></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0"><span>1.1.3</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span>✨ 状态事件接口 IMqttConnectStatusListener 添加 ChannelContext 参数。</span></li> 
 <li><span>✨ 从认证中拆分 IMqttServerSubscribeValidator 订阅校验接口，添加 ChannelContext、clientId 参数。</span> </li> 
 <li><span>✨ 认证 IMqttServerAuthHandler 调整包、添加 ChannelContext 参数。</span></li> 
 <li><span>✨ 完善文档和示例，添加默认端口号说明。</span></li> 
 <li><span>⬆️ 依赖升级。</span></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0"><span>五、Spring boot 快速接入</span></h2> 
<p style="margin-left:0; margin-right:0"><span>5.1 添加依赖</span></p> 
<pre><dependency>
    <groupId>net.dreamlu</groupId>
    <artifactId>mica-mqtt-spring-boot-starter</artifactId>
    <version>1.1.4</version>
</dependency></pre> 
<p style="margin-left:0; margin-right:0"> </p> 
<h3 style="margin-left:0; margin-right:0"><span>5.2 服务端配置示例</span></h3> 
<pre>mqtt:
  server:
    enabled: true               # 是否开启，默认：true
    ip: 127.0.0.1               # 服务端 ip 默认：127.0.0.1
    port: 5883                  # 端口，默认：1883
    name: Mica-Mqtt-Server      # 名称，默认：Mica-Mqtt-Server
    buffer-allocator: HEAP      # 堆内存和堆外内存，默认：堆内存
    heartbeat-timeout: 120000   # 心跳超时，单位毫秒，默认: 1000 * 120
    read-buffer-size: 8092      # 接收数据的 buffer size，默认：8092
    max-bytes-in-message: 8092  # 消息解析最大 bytes 长度，默认：8092
    debug: true                 # 如果开启 prometheus 指标收集建议关闭
    websocket-enable: true      # 开启 websocket 子协议，默认开启
    websocket-port: 8083        # websocket 端口，默认：8083</pre> 
<p style="margin-left:0; margin-right:0"> </p> 
<h3 style="margin-left:0; margin-right:0"><span>5.3 服务端可实现接口（注册成 Spring Bean 即可）</span></h3> 
<table border="1" cellspacing="0" class="ne-table" id="aa6e808f" style="border-collapse:collapse; border:1px solid #d9d9d9; table-layout:fixed; width:750px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>接口</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是否必须</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>说明</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IMqttServerUniqueIdService</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>1.1.4 新增，用于 clientId 不唯一时，自定义实现唯一标识，后续接口使用它替代 clientId</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IMqttServerAuthHandler</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>用于服务端认证</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IMqttServerSubscribeValidator</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>1.1.3 新增，用于服务端订阅校验</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IMqttMessageListener</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>消息监听</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IMqttConnectStatusListener</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>是</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>连接状态监听</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IMqttSessionManager</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>session 管理</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IMqttMessageStore</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>集群是，单机否</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>遗嘱和保留消息存储</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>AbstractMqttMessageDispatcher</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>集群是，单机否</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>消息转发，（遗嘱、保留消息转发）</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>IpStatListener</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>否</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>t-io ip 状态监听</span></p> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:0; margin-right:0"> </p> 
<h3 style="margin-left:0; margin-right:0"><span>5.4 Prometheus + Grafana 监控对接</span></h3> 
<p style="margin-left:0; margin-right:0"><span>得益于 </span><strong><span>t-io</span></strong><span> 良好的设计，监控指标直接对接的 </span><strong><span>t-iostat</span></strong><span>，目前支持下列指标，后期会不断完善。</span></p> 
<table border="1" cellspacing="0" class="ne-table" id="d7d0695f" style="border-collapse:collapse; border:1px solid #d9d9d9; table-layout:fixed; width:750px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>支持得指标</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>说明</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_connections_accepted</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>共接受过连接数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_connections_closed</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>关闭过的连接数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_connections_size</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>当前连接数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_messages_handled_packets</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>已处理消息数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_messages_handled_bytes</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>已处理消息字节数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_messages_received_packets</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>已接收消息数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_messages_received_bytes</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>已处理消息字节数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_messages_send_packets</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>已发送消息数</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>mqtt_messages_send_bytes</span></p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0"><span>已发送消息字节数</span></p> </td> 
  </tr> 
 </tbody> 
</table> 
<p><img height="977" src="https://oscimg.oschina.net/oscnet/up-5805d01baf336f1081505d0e0d39c7790de.png" width="959" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><span>关于 </span><strong><span>mica-mqtt-spring-boot-starter</span></strong><span> 更多请查看文档：</span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter" target="_blank"><span>https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter</span></a></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<h2 style="margin-left:0; margin-right:0"><span>六、普通 java 项目接入</span></h2> 
<h3 style="margin-left:0; margin-right:0"><span>6.1 maven 依赖</span></h3> 
<pre> <dependency>
   <groupId>net.dreamlu</groupId>
   <artifactId>mica-mqtt-core</artifactId>
   <version>1.1.4</version>
 </dependency></pre> 
<p style="margin-left:0; margin-right:0"> </p> 
<h3 style="margin-left:0; margin-right:0"><span>6.2 mica-mqtt 客户端</span></h3> 
<pre> // 初始化 mqtt 客户端
 MqttClient client = MqttClient.create()
     .ip("127.0.0.1")
     .port(1883)                     // 默认：1883
     .username("admin")
     .password("123456")
     .version(MqttVersion.MQTT_5)    // 默认：3_1_1
     .clientId("xxxxxx")             // 默认：MICA-MQTT- 前缀和 36进制的纳秒数
     .connect();                     // 连接
 
     // 消息订阅，同类方法 subxxx
     client.subQos0("/test/#", (topic, payload) -> &#123;
         logger.info(topic + '\t' + ByteBufferUtil.toString(payload));
     &#125;);
     // 取消订阅
     client.unSubscribe("/test/#");
 
     // 发送消息
     client.publish("/test/client", ByteBuffer.wrap("mica最牛皮".getBytes(StandardCharsets.UTF_8)));
 
     // 断开连接
     client.disconnect();
     // 重连
     client.reconnect();
     // 停止
     client.stop();</pre> 
<p style="margin-left:0; margin-right:0"> </p> 
<h3 style="margin-left:0; margin-right:0"><span>6.3 mica-mqtt 服务端</span></h3> 
<pre> // 注意：为了能接受更多链接（降低内存），请添加 jvm 参数 -Xss129k
 MqttServer mqttServer = MqttServer.create()
     // 默认：127.0.0.1
     .ip("127.0.0.1")
     // 默认：1883
     .port(1883)
     // 默认为： 8092（mqtt 默认最大消息大小），为了降低内存可以减小小此参数，如果消息过大 t-io 会尝试解析多次（建议根据实际业务情况而定）
     .readBufferSize(512)
     // 消息监听
     .messageListener((clientId, topic, mqttQoS, payload) -> &#123;
         logger.info("clientId:&#123;&#125; topic:&#123;&#125; mqttQoS:&#123;&#125; message:&#123;&#125;", clientId, topic, mqttQoS, ByteBufferUtil.toString(payload));
     &#125;)
     .debug() // 开启 t-io debug 信息日志
     .start();
 
 // 发送给某个客户端
 mqttServer.publish("clientId","/test/123", ByteBuffer.wrap("mica最牛皮".getBytes()));
 
 // 发送给所有在线监听这个 topic 的客户端
 mqttServer.publishAll("/test/123", ByteBuffer.wrap("mica最牛皮".getBytes()));
 
 // 停止服务
 mqttServer.stop();</pre> 
<p style="margin-left:0; margin-right:0"> </p> 
<h2 style="margin-left:0; margin-right:0"><span>七、集群演示</span></h2> 
<p><img height="720" src="https://oscimg.oschina.net/oscnet/up-fe9774d3ca40b1eb33efc1dc5468c33980f.png" width="1280" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            