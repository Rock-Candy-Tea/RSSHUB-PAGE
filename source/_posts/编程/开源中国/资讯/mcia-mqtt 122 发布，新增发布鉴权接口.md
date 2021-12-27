
---
title: 'mcia-mqtt 1.2.2 发布，新增发布鉴权接口'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1315'
author: 开源中国
comments: false
date: Mon, 27 Dec 2021 12:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1315'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start"><span>一、简介</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>mica-mqtt</span></strong></span><span> 基于 </span><span><strong><span>t-io</span></strong></span><span> 实现的</span><span><strong><span>简单</span></strong></span><span>、</span><span><strong><span>低延迟</span></strong></span><span>、</span><span><strong><span>高性能</span></strong></span><span> 的 mqtt 物联网开源组件。</span><span><strong><span>mica-mqtt</span></strong></span><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></p> 
<h2 style="text-align:start"><span>二、功能</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li style="list-style-type:none"><span>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></li> 
 <li style="list-style-type:none"><span>支持 websocket mqtt 子协议（支持 mqtt.js）。</span></li> 
 <li style="list-style-type:none"><span>支持 http rest api，</span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>http api 文档详见</span></a></span><span>。</span></li> 
 <li style="list-style-type:none"><span>支持 MQTT client 客户端。</span></li> 
 <li style="list-style-type:none"><span>支持 MQTT server 服务端。</span></li> 
 <li style="list-style-type:none"><span>支持 MQTT 遗嘱消息。</span></li> 
 <li style="list-style-type:none"><span>支持 MQTT 保留消息。</span></li> 
 <li style="list-style-type:none"><span>支持自定义消息（mq）处理转发实现集群。</span></li> 
 <li style="list-style-type:none"><span>MQTT 客户端 阿里云 mqtt 连接 demo。</span></li> 
 <li style="list-style-type:none"><span>支持 GraalVM 编译成本机可执行程序。</span></li> 
 <li style="list-style-type:none"><span>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></li> 
 <li style="list-style-type:none"><span>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></li> 
 <li style="list-style-type:none"><span>基于 redis pub/sub 实现集群，详见 </span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker"><span>mica-mqtt-broker 模块</span></a></span><span>。</span></li> 
</ul> 
<h2 style="text-align:start"><span>三、使用场景</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>物联网（云端）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>物联网（边缘端）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>群组类 IM</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>消息推送</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>简单易用的 MQTT 客户端</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>四、更新记录</span></h2> 
<h3 style="text-align:start"><span>1.2.2 - 2021-12-26</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 添加发布权限接口，无权限直接断开连接，避免高级别 qos 重试浪费资源。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt-broker 优化节点信息存储</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 重复订阅优化。感谢 @一片小雨滴</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 抽象 IMqttClientSession 接口。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛 修复重构 AbstractMqttMessageDispatcher 保持跟 mica-mqtt-broker 逻辑一致 gitee #I4MA6A 感谢 @胡萝博</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>⬆️ mica-mqtt-example 升级 log4j2 到 2.17.0</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>1.2.1 - 2021-12-11</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt 优化 topic 匹配。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client disconnect 不再自动重连 gitee #I4L0WK 感谢 @willianfu。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 添加 retryCount 配置 gitee #I4L0WK 感谢 @willianfu。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt-model message 添加 json 序列化。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt-broker 重新梳理逻辑。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛 mica-mqtt-spring-boot-starter 在 boot 2.6.x 下 bean 循环依赖 gitee #I4LUZP 感谢 @hongfeng11。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛 mica-mqtt server 同一个 clientId 踢出时清除老的 session。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛 mica-mqtt server 集群下一个 clientId 只允许连接到一台服务器。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛 mica-mqtt client 修复 IMqttClientConnectListener onDisconnect 空指针。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>📝 mica-mqtt-model 添加 README.md</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>五、Spring boot 快速接入</span></h2> 
<h3 style="text-align:start"><span>5.1 添加依赖</span></h3> 
<pre style="text-align:left"><span><span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-spring-boot-starter<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.2.2<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span></span>
<span><span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span></pre> 
<h3 style="text-align:start"><span>5.2 服务端配置示例</span></h3> 
<pre style="text-align:left"><span><span style="color:#221199">mqtt</span><span style="color:#555555">:</span></span>
<span><span style="color:#221199">  server</span><span style="color:#555555">:</span></span>
<span><span style="color:#221199">    enabled</span><span style="color:#555555">: </span>true               <span style="color:#aa5500"># 是否开启，默认：true</span></span>
<span><span style="color:#221199">    ip</span><span style="color:#555555">: </span>0.0.0.0                 <span style="color:#aa5500"># 服务端 ip 默认：0.0.0.0</span></span>
<span><span style="color:#221199">    port</span><span style="color:#555555">: </span>5883                  <span style="color:#aa5500"># 端口，默认：1883</span></span>
<span><span style="color:#221199">    name</span><span style="color:#555555">: </span>Mica-Mqtt-Server      <span style="color:#aa5500"># 名称，默认：Mica-Mqtt-Server</span></span>
<span><span style="color:#221199">    buffer-allocator</span><span style="color:#555555">: </span>HEAP      <span style="color:#aa5500"># 堆内存和堆外内存，默认：堆内存</span></span>
<span><span style="color:#221199">    heartbeat-timeout</span><span style="color:#555555">: </span>120000   <span style="color:#aa5500"># 心跳超时，单位毫秒，默认: 1000 * 120</span></span>
<span><span style="color:#221199">    read-buffer-size</span><span style="color:#555555">: </span>8092      <span style="color:#aa5500"># 接收数据的 buffer size，默认：8092</span></span>
<span><span style="color:#221199">    max-bytes-in-message</span><span style="color:#555555">: </span>8092  <span style="color:#aa5500"># 消息解析最大 bytes 长度，默认：8092</span></span>
<span><span style="color:#221199">    debug</span><span style="color:#555555">: </span>true                 <span style="color:#aa5500"># 如果开启 prometheus 指标收集建议关闭</span></span>
<span><span style="color:#221199">    websocket-enable</span><span style="color:#555555">: </span>true      <span style="color:#aa5500"># 开启 websocket 子协议，默认开启</span></span>
<span><span style="color:#221199">    websocket-port</span><span style="color:#555555">: </span>8083        <span style="color:#aa5500"># websocket 端口，默认：8083</span></span></pre> 
<h3 style="text-align:start"><span>5.3 服务端可实现接口（注册成 Spring Bean 即可）</span></h3> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:800px; word-break:initial"> 
 <thead> 
  <tr> 
   <th><span><span>接口</span></span></th> 
   <th><span><span>是否必须</span></span></th> 
   <th><span><span>说明</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttServerUniqueIdService</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>否</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>用于 clientId 不唯一时，自定义实现唯一标识，后续接口使用它替代 clientId</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttServerAuthHandler</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>是</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>用于服务端认证</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttServerSubscribeValidator</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>否（建议实现）</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>1.1.3 新增，用于对客户端订阅校验</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttServerPublishPermission</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>否（建议实现）</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>1.2.2 新增，用于对客户端发布权限校验</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttMessageListener</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>是</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>消息监听</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttConnectStatusListener</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>是</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>连接状态监听</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttSessionManager</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>否</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>session 管理</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IMqttMessageStore</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>集群是，单机否</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>遗嘱和保留消息存储</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>AbstractMqttMessageDispatcher</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>集群是，单机否</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>消息转发，（遗嘱、保留消息转发）</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>IpStatListener</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>否</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>t-io ip 状态监听</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start"><span>5.4 Prometheus + Grafana 监控对接</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>得益于 </span><span><strong><span>t-io</span></strong></span><span> 良好的设计，监控指标直接对接的 </span><span><strong><span>t-iostat</span></strong></span><span>，目前支持下列指标，后期会不断完善。</span></p> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:800px; word-break:initial"> 
 <thead> 
  <tr> 
   <th><span><span>支持得指标</span></span></th> 
   <th><span><span>说明</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_connections_accepted</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>共接受过连接数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_connections_closed</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>关闭过的连接数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_connections_size</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>当前连接数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_messages_handled_packets</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>已处理消息数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_messages_handled_bytes</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>已处理消息字节数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_messages_received_packets</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>已接收消息数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_messages_received_bytes</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>已处理消息字节数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_messages_send_packets</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>已发送消息数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>mqtt_messages_send_bytes</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>已发送消息字节数</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>关于 </span><span><strong><span>mica-mqtt-spring-boot-starter</span></strong></span><span> 更多请查看文档：</span><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter"><span>https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter</span></a></span></p> 
<h2 style="text-align:start"><span>六、普通 java 项目接入</span></h2> 
<h3 style="text-align:start"><span>6.1 maven 依赖</span></h3> 
<pre style="text-align:left"><span> <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span>
<span>   <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span></span>
<span>   <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-core<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span></span>
<span>   <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.2.2<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span></span>
<span> <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span></pre> 
<h3 style="text-align:start"><span>6.2 mica-mqtt 客户端</span></h3> 
<pre style="text-align:left"><span> <span style="color:#aa5500">// 初始化 mqtt 客户端</span></span>
<span> <span style="color:#000000">MqttClient</span> <span style="color:#000000">client</span> <span style="color:#981a1a">=</span> <span style="color:#000000">MqttClient</span>.<span style="color:#000000">create</span>()</span>
<span>     .<span style="color:#000000">ip</span>(<span style="color:#aa1111">"127.0.0.1"</span>)</span>
<span>     .<span style="color:#000000">port</span>(<span style="color:#116644">1883</span>)                     <span style="color:#aa5500">// 默认：1883</span></span>
<span>     .<span style="color:#000000">username</span>(<span style="color:#aa1111">"admin"</span>)</span>
<span>     .<span style="color:#000000">password</span>(<span style="color:#aa1111">"123456"</span>)</span>
<span>     .<span style="color:#000000">version</span>(<span style="color:#000000">MqttVersion</span>.<span style="color:#000000">MQTT_5</span>)    <span style="color:#aa5500">// 默认：3_1_1</span></span>
<span>     .<span style="color:#000000">clientId</span>(<span style="color:#aa1111">"xxxxxx"</span>)             <span style="color:#aa5500">// 默认：MICA-MQTT- 前缀和 36进制的纳秒数</span></span>
<span>     .<span style="color:#000000">connect</span>();                     <span style="color:#aa5500">// 连接</span></span>
<span> </span>
<span>     <span style="color:#aa5500">// 消息订阅，同类方法 subxxx</span></span>
<span>     <span style="color:#000000">client</span>.<span style="color:#000000">subQos0</span>(<span style="color:#aa1111">"/test/#"</span>, (<span style="color:#000000">topic</span>, <span style="color:#000000">payload</span>) <span style="color:#981a1a">-></span> &#123;</span>
<span>         <span style="color:#000000">logger</span>.<span style="color:#000000">info</span>(<span style="color:#000000">topic</span> <span style="color:#981a1a">+</span> <span style="color:#aa1111">'\t'</span> <span style="color:#981a1a">+</span> <span style="color:#000000">ByteBufferUtil</span>.<span style="color:#000000">toString</span>(<span style="color:#000000">payload</span>));</span>
<span>     &#125;);</span>
<span>     <span style="color:#aa5500">// 取消订阅</span></span>
<span>     <span style="color:#000000">client</span>.<span style="color:#000000">unSubscribe</span>(<span style="color:#aa1111">"/test/#"</span>);</span>
<span> </span>
<span>     <span style="color:#aa5500">// 发送消息</span></span>
<span>     <span style="color:#000000">client</span>.<span style="color:#000000">publish</span>(<span style="color:#aa1111">"/test/client"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>(<span style="color:#000000">StandardCharsets</span>.<span style="color:#000000">UTF_8</span>)));</span>
<span> </span>
<span>     <span style="color:#aa5500">// 断开连接</span></span>
<span>     <span style="color:#000000">client</span>.<span style="color:#000000">disconnect</span>();</span>
<span>     <span style="color:#aa5500">// 重连</span></span>
<span>     <span style="color:#000000">client</span>.<span style="color:#000000">reconnect</span>();</span>
<span>     <span style="color:#aa5500">// 停止</span></span>
<span>     <span style="color:#000000">client</span>.<span style="color:#000000">stop</span>();</span></pre> 
<h3 style="text-align:start"><span>6.3 mica-mqtt 服务端</span></h3> 
<pre style="text-align:left"><span><span style="color:#aa5500">// 注意：为了能接受更多链接（降低内存），请添加 jvm 参数 -Xss129k</span></span>
<span><span style="color:#000000">MqttServer</span> <span style="color:#000000">mqttServer</span> <span style="color:#981a1a">=</span> <span style="color:#000000">MqttServer</span>.<span style="color:#000000">create</span>()</span>
<span>    <span style="color:#aa5500">// 默认：0.0.0.0</span></span>
<span>    .<span style="color:#000000">ip</span>(<span style="color:#aa1111">"0.0.0.0"</span>)</span>
<span>    <span style="color:#aa5500">// 默认：1883</span></span>
<span>    .<span style="color:#000000">port</span>(<span style="color:#116644">1883</span>)</span>
<span>    <span style="color:#aa5500">// 默认为： 8092（mqtt 默认最大消息大小），为了降低内存可以减小小此参数，如果消息过大 t-io 会尝试解析多次（建议根据实际业务情况而定）</span></span>
<span>    .<span style="color:#000000">readBufferSize</span>(<span style="color:#116644">512</span>)</span>
<span>    <span style="color:#aa5500">// 消息监听</span></span>
<span>    .<span style="color:#000000">messageListener</span>((<span style="color:#000000">context</span>, <span style="color:#000000">clientId</span>, <span style="color:#000000">message</span>) <span style="color:#981a1a">-></span> &#123;</span>
<span>        <span style="color:#000000">logger</span>.<span style="color:#000000">info</span>(<span style="color:#aa1111">"clientId:&#123;&#125; message:&#123;&#125; payload:&#123;&#125;"</span>, <span style="color:#000000">clientId</span>, <span style="color:#000000">message</span>, <span style="color:#000000">ByteBufferUtil</span>.<span style="color:#000000">toString</span>(<span style="color:#000000">message</span>.<span style="color:#000000">getPayload</span>()));</span>
<span>    &#125;)</span>
<span>    .<span style="color:#000000">debug</span>() <span style="color:#aa5500">// 开启 t-io debug 信息日志</span></span>
<span>    .<span style="color:#000000">start</span>();</span>
<span><span>​</span></span>
<span><span style="color:#aa5500">// 发送给某个客户端</span></span>
<span><span style="color:#000000">mqttServer</span>.<span style="color:#000000">publish</span>(<span style="color:#aa1111">"clientId"</span>,<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()));</span>
<span><span>​</span></span>
<span><span style="color:#aa5500">// 发送给所有在线监听这个 topic 的客户端</span></span>
<span><span style="color:#000000">mqttServer</span>.<span style="color:#000000">publishAll</span>(<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()));</span>
<span><span>​</span></span>
<span><span style="color:#aa5500">// 停止服务</span></span>
<span><span style="color:#000000">mqttServer</span>.<span style="color:#000000">stop</span>()</span>
</pre>
                                        </div>
                                      
</div>
            