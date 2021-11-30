
---
title: 'mica-mqtt 1.2.0 发布完善集群功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cdn.nlark.com/yuque/0/2021/jpeg/188203/1628396634437-08540312-ab7a-4430-9c61-a9264b89f981.jpeg#clientId=u812afff3-4832-4&from=ui&id=ubbe58455&margin=%5Bobject%20Object%5D&name=mqtt%E7%9B%91%E6%8E%A71.jpg&originHeight=977&originWidth=959&originalType=binary&ratio=1&size=133185&status=done&style=none&taskId=udccd7dee-0a1f-4fa2-93b4-55a1bcb3da3#id=aUw6i&originHeight=977&originWidth=959&originalType=binary&ratio=1&status=done&style=none#id=SWMfn&originHeight=977&originWidth=959&originalType=binary&ratio=1&status=done&style=none'
author: 开源中国
comments: false
date: Mon, 29 Nov 2021 21:53:00 GMT
thumbnail: 'https://cdn.nlark.com/yuque/0/2021/jpeg/188203/1628396634437-08540312-ab7a-4430-9c61-a9264b89f981.jpeg#clientId=u812afff3-4832-4&from=ui&id=ubbe58455&margin=%5Bobject%20Object%5D&name=mqtt%E7%9B%91%E6%8E%A71.jpg&originHeight=977&originWidth=959&originalType=binary&ratio=1&size=133185&status=done&style=none&taskId=udccd7dee-0a1f-4fa2-93b4-55a1bcb3da3#id=aUw6i&originHeight=977&originWidth=959&originalType=binary&ratio=1&status=done&style=none#id=SWMfn&originHeight=977&originWidth=959&originalType=binary&ratio=1&status=done&style=none'
---

<div>   
<div class="content">
                                                                    
                                                        <h2><span>一、简介</span></h2> 
<p style="margin-left:.8em; margin-right:.8em"><span><span><strong><span>mica-mqtt</span></strong><span> 基于 </span><span><strong><span>t-io</span></strong><span> 实现的</span><span><strong><span>简单</span></strong><span>、</span><span><strong><span>低延迟</span></strong><span>、</span><span><strong><span>高性能</span></strong><span> 的 mqtt 物联网开源组件。</span><span><strong><span>使用详见 mica-mqtt gitee 源码</span></strong><span> </span><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-example"><span>mica-mqtt-example 模块</span></a><span>。</span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:.8em; margin-right:.8em"><span><span><strong><span>mica-mqtt</span></strong><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></span></span></p> 
<h2><span>二、功能</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 websocket mqtt 子协议（支持 mqtt.js）。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 http rest api，</span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>http api 文档详见</span></a><span>。</span></span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT client 客户端。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT server 服务端。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT 遗嘱消息。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT 保留消息。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持自定义消息（mq）处理转发实现集群。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>MQTT 客户端 阿里云 mqtt 连接 demo。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 GraalVM 编译成本机可执行程序。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>基于 redis pub/sub 实现集群，详见 </span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker"><span>mica-mqtt-broker 模块</span></a><span>。</span></span></span></p> </li> 
</ul> 
<h2><span>三、使用场景</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>物联网（云端）</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>物联网（边缘端）</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>群组类 IM</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>消息推送</span></span></p> </li> 
</ul> 
<h2><span>四、待办</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>优化处理 mqtt session，以及支持部分 mqtt v5.0 新特性。</span></span></p> </li> 
 <li style="list-style-type:none"> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>基于 easy-rule + druid sql 解析，实现规则引擎。</span></span></p> </li> 
</ul> 
<h2><span>五、更新记录</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> mqtt-mqtt-core client IMqttClientConnectListener 添加 onDisconnect 方法。gitee #I4JT1D 感谢 </span><span><code>@willianfu</code><span> 同学反馈。</span></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> mica-mqtt-core server IMqttMessageListener 接口调整，不兼容老版本。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> mica-mqtt-broker 调整上下行消息通道。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> mica-mqtt-broker 添加节点管理，抽象业务层，方便接入，后续版本会对接规则引擎。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> mica-mqtt-broker 调整默认的 Message 序列化方式，不兼容老版本。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> mica-mqtt-broker 优化设备上下线，处理节点停机的情况。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> 抽取 mica-mqtt-model 模块，方便后期支持消息桥接，Message 添加默认的消息序列化。 gitee #I4ECEO</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨</span><span> mica-mqtt-model 完善 Message 消息模型，方便集群。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>🐛</span><span> mica-mqtt-core MqttClient 修复 ssl 没有设置，感谢 </span><span><code>@hjkJOJO</code><span> 同学反馈。</span></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>🐛</span><span> 修复 websocket mqtt.js 需要拆包 gitee #I4JYJX 感谢 </span><span><code>@Symous</code><span> 同学反馈。</span></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>📝</span><span> 完善 mica-mqtt-broker README.md，添加二开说明。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>📝</span><span> 统一 mica-mqtt server ip 文档。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>📝</span><span> 更新 README.md</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>⬆️</span><span> 升级 tio 到 3.7.5.v20211028-RELEASE AioDecodeException 改为 TioDecodeException，</span></span></p> </li> 
</ul> 
<h2><span>六、重要更新说明</span></h2> 
<h3><span>6.1 客户端 IMqttClientConnectListener 添加 onDisconnect 方法</span></h3> 
<pre style="text-align:left"><span><span style="color:#770088">public</span> <span style="color:#770088">interface</span> <span style="color:#0000ff">IMqttClientConnectListener</span> &#123;</span>
<span><span>​</span></span>
<span>    <span style="color:#aa5500">/**</span></span>
<span>     <span style="color:#aa5500">* 监听到消息</span></span>
<span>     <span style="color:#aa5500">*</span></span>
<span>     <span style="color:#aa5500">* @param context     ChannelContext</span></span>
<span>     <span style="color:#aa5500">* @param isReconnect 是否重连</span></span>
<span>     <span style="color:#aa5500">*/</span></span>
<span>    <span style="color:#008855">void</span> <span style="color:#000000">onConnected</span>(<span style="color:#000000">ChannelContext</span> <span style="color:#000000">context</span>, <span style="color:#008855">boolean</span> <span style="color:#000000">isReconnect</span>);</span>
<span><span>​</span></span>
<span>    <span style="color:#aa5500">/**</span></span>
<span>     <span style="color:#aa5500">* 连接关闭前触发本方法</span></span>
<span>     <span style="color:#aa5500">*</span></span>
<span>     <span style="color:#aa5500">* @param channelContext the channelContext</span></span>
<span>     <span style="color:#aa5500">* @param throwable      the throwable 有可能为空</span></span>
<span>     <span style="color:#aa5500">* @param remark         the remark 有可能为空</span></span>
<span>     <span style="color:#aa5500">* @param isRemove       is removed</span></span>
<span>     <span style="color:#aa5500">*/</span></span>
<span>    <span style="color:#008855">void</span> <span style="color:#000000">onDisconnect</span>(<span style="color:#000000">ChannelContext</span> <span style="color:#000000">channelContext</span>, <span style="color:#000000">Throwable</span> <span style="color:#000000">throwable</span>, <span style="color:#008855">String</span> <span style="color:#000000">remark</span>, <span style="color:#008855">boolean</span> <span style="color:#000000">isRemove</span>);</span>
<span><span>​</span></span>
<span>&#125;</span></pre> 
<h3><span>6.2 服务端 IMqttMessageListener onMessage 参数调整</span></h3> 
<pre style="text-align:left"><span><span style="color:#555555">@FunctionalInterface</span></span>
<span><span style="color:#770088">public</span> <span style="color:#770088">interface</span> <span style="color:#0000ff">IMqttMessageListener</span> &#123;</span>
<span><span>​</span></span>
<span>    <span style="color:#aa5500">/**</span></span>
<span>     <span style="color:#aa5500">* 监听到消息</span></span>
<span>     <span style="color:#aa5500">*</span></span>
<span>     <span style="color:#aa5500">* @param context  ChannelContext</span></span>
<span>     <span style="color:#aa5500">* @param clientId clientId</span></span>
<span>     <span style="color:#aa5500">* @param message  Message</span></span>
<span>     <span style="color:#aa5500">*/</span></span>
<span>    <span style="color:#008855">void</span> <span style="color:#000000">onMessage</span>(<span style="color:#000000">ChannelContext</span> <span style="color:#000000">context</span>, <span style="color:#008855">String</span> <span style="color:#000000">clientId</span>, <span style="color:#000000">Message</span> <span style="color:#000000">message</span>);</span>
<span><span>​</span></span>
<span>&#125;</span></pre> 
<h3><span>6.3 Message 对象添加更多属性</span></h3> 
<p style="margin-left:.8em; margin-right:.8em"><span><span>为了以后版本更方便的对接规则引擎对 Message 中的属性进行了扩充，并且内置 DefaultMessageSerializer 序列化，基于 </span><span><code>ByteBuffer</code><span> 进行的类协议解析的方式，速度更快，报文更小。</span></span></span></p> 
<pre style="text-align:left"><span><span style="color:#008855">byte</span>[] <span style="color:#000000">data</span> <span style="color:#981a1a">=</span> <span style="color:#000000">DefaultMessageSerializer</span>.<span style="color:#000000">INSTANCE</span>.<span style="color:#000000">serialize</span>(<span style="color:#000000">message</span>);</span>
<span><span style="color:#000000">Message</span> <span style="color:#000000">message1</span> <span style="color:#981a1a">=</span> <span style="color:#000000">DefaultMessageSerializer</span>.<span style="color:#000000">INSTANCE</span>.<span style="color:#000000">deserialize</span>(<span style="color:#000000">data</span>);</span></pre> 
<h2><span>七、Spring boot 快速接入</span></h2> 
<h3><span>7.1 添加依赖</span></h3> 
<pre style="text-align:left"><span><span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-spring-boot-starter<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span></span>
<span>    <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.2.0<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span></span>
<span><span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span></pre> 
<h3><span>7.2 服务端配置示例</span></h3> 
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
<h3><span>7.3 服务端可实现接口（注册成 Spring Bean 即可）</span></h3> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; margin:0.8em 0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:792px; word-break:initial"> 
 <thead> 
  <tr> 
   <th style="text-align:left"><span><span>接口</span></span></th> 
   <th style="text-align:left"><span><span>是否必须</span></span></th> 
   <th style="text-align:left"><span><span>说明</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IMqttServerUniqueIdService</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>否</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>用于 clientId 不唯一时，自定义实现唯一标识，后续接口使用它替代 clientId</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IMqttServerAuthHandler</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>是</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>用于服务端认证</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IMqttServerSubscribeValidator</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>是</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>1.1.3 新增，用于服务端订阅校验</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IMqttMessageListener</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>是</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>消息监听</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IMqttConnectStatusListener</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>是</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>连接状态监听</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IMqttSessionManager</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>否</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>session 管理</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IMqttMessageStore</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>集群是，单机否</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱和保留消息存储</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>AbstractMqttMessageDispatcher</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>集群是，单机否</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>消息转发，（遗嘱、保留消息转发）</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>IpStatListener</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>否</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>t-io ip 状态监听</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<h3><span>7.4 Prometheus + Grafana 监控对接</span></h3> 
<p style="margin-left:.8em; margin-right:.8em"><span><span>得益于 </span><span><strong><span>t-io</span></strong><span> 良好的设计，监控指标直接对接的 </span><span><strong><span>t-iostat</span></strong><span>，目前支持下列指标，后期会不断完善。</span></span></span></span></p> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; margin:0.8em 0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:792px; word-break:initial"> 
 <thead> 
  <tr> 
   <th style="text-align:left"><span><span>支持得指标</span></span></th> 
   <th style="text-align:left"><span><span>说明</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_connections_accepted</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>共接受过连接数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_connections_closed</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>关闭过的连接数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_connections_size</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>当前连接数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_messages_handled_packets</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>已处理消息数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_messages_handled_bytes</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>已处理消息字节数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_messages_received_packets</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>已接收消息数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_messages_received_bytes</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>已处理消息字节数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_messages_send_packets</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>已发送消息数</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>mqtt_messages_send_bytes</span></span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"><span><span>已发送消息字节数</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:.8em; margin-right:.8em"><span><span><img src="https://cdn.nlark.com/yuque/0/2021/jpeg/188203/1628396634437-08540312-ab7a-4430-9c61-a9264b89f981.jpeg#clientId=u812afff3-4832-4&from=ui&id=ubbe58455&margin=%5Bobject%20Object%5D&name=mqtt%E7%9B%91%E6%8E%A71.jpg&originHeight=977&originWidth=959&originalType=binary&ratio=1&size=133185&status=done&style=none&taskId=udccd7dee-0a1f-4fa2-93b4-55a1bcb3da3#id=aUw6i&originHeight=977&originWidth=959&originalType=binary&ratio=1&status=done&style=none#id=SWMfn&originHeight=977&originWidth=959&originalType=binary&ratio=1&status=done&style=none" referrerpolicy="no-referrer"></span></span></p> 
<p style="margin-left:.8em; margin-right:.8em"><span><span>关于 </span><span><strong><span>mica-mqtt-spring-boot-starter</span></strong><span> 更多请查看文档：</span><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter"><span>https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter</span></a></span></span></span></p> 
<h2><span>八、普通 java 项目接入</span></h2> 
<h3><span>8.1 maven 依赖</span></h3> 
<pre style="text-align:left"><span> <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span>
<span>   <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span></span>
<span>   <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-core<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span></span>
<span>   <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.2.0<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span></span>
<span> <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></span></pre> 
<h3><span>8.2 mica-mqtt 客户端</span></h3> 
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
<h3><span>8.3 mica-mqtt 服务端</span></h3> 
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
<span><span style="color:#000000">mqttServer</span>.<span style="color:#000000">stop</span>();</span></pre> 
<h2><span>九、集群演示视频</span></h2> 
<p style="margin-left:.8em; margin-right:.8em"><img alt height="720" src="https://oscimg.oschina.net/oscnet/up-86bca6ea16871d83dd636ed15763b2cf1dc.gif" width="1280" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            