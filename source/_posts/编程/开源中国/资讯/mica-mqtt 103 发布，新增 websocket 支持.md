
---
title: 'mica-mqtt 1.0.3 发布，新增 websocket 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6b982b8f8c33606ba7f2c07158779a4debe.JPEG'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 09:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6b982b8f8c33606ba7f2c07158779a4debe.JPEG'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start">一、简介</h2> 
<p style="text-align:start"><strong>mica-mqtt</strong> 基于 <strong>t-io</strong> 实现的<strong>简单</strong>、<strong>低延迟</strong>、<strong>高性能</strong> 的 mqtt 物联网开源组件。<strong>使用详见 mica-mqtt gitee 源码</strong><code>mica-mqtt-example</code> 模块。</p> 
<h2 style="text-align:start">二、功能</h2> 
<ul> 
 <li>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</li> 
 <li>支持 websocket mqtt 子协议（支持 mqtt.js）。</li> 
 <li>支持 MQTT client 客户端。</li> 
 <li>支持 MQTT server 服务端。</li> 
 <li>支持 MQTT 遗嘱消息。</li> 
 <li>支持 MQTT 保留消息。</li> 
 <li>支持自定义消息（mq）处理转发实现集群。</li> 
 <li>MQTT 客户端 阿里云 mqtt 连接 demo。</li> 
 <li>支持 GraalVM 编译成本机可执行程序。</li> 
 <li>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</li> 
 <li>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</li> 
</ul> 
<h2 style="text-align:start">三、待办</h2> 
<ul> 
 <li>优化处理 mqtt session，以及支持部分 mqtt v5.0 新特性。</li> 
</ul> 
<h2 style="text-align:start">四、更新记录</h2> 
<ul> 
 <li> <p>✨mica-mqtt server 添加 websocket mqtt 子协议支持（支持 mqtt.js）。</p> </li> 
 <li> <p>✨mica-mqtt server ip，默认为空，可不设置。</p> </li> 
 <li> <p>✨mica-mqtt client去除 CountDownLatch 避免启动时未连接上服务端卡住。</p> </li> 
 <li> <p>✨mica-mqtt client 添加最大包体长度字段，避免超过 8092 长度的包体导致解析异常。</p> </li> 
 <li> <p>✨mica-mqtt client 添加连接监听 IMqttClientConnectListener。</p> </li> 
 <li> <p>✨mica-mqtt 3.1 协议会校验 clientId 长度，添加配置项 maxClientIdLength。</p> </li> 
 <li> <p>✨mica-mqtt 优化 mqtt 解码异常处理。</p> </li> 
 <li> <p>✨mica-mqtt 日志优化，方便查询。</p> </li> 
 <li> <p>✨mica-mqtt 代码优化，部分 Tio.close 改为 Tio.remove。</p> </li> 
 <li> <p>✨mica-mqtt-spring-boot-example 添加 Dockerfile，支持spring-boot:build-image。</p> </li> 
 <li> <p>✨完善 mica-mqtt-spring-boot-starter，添加遗嘱消息配置。</p> </li> 
 <li> <p>⬆️ 升级 t-io 到 3.7.4。</p> </li> 
</ul> 
<h2 style="text-align:start">五、Spring boot 快速接入</h2> 
<h3 style="text-align:start">5.1 添加依赖</h3> 
<pre style="text-align:left"> <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
     <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
     <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-spring-boot-starter<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
     <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.0.3<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
 <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></pre> 
<h3 style="text-align:start">5.2 服务端配置示例</h3> 
<pre style="text-align:left"> <span style="color:#221199">mqtt</span><span style="color:#555555">:</span>
 <span style="color:#221199">  server</span><span style="color:#555555">:</span>
 <span style="color:#221199">    enabled</span><span style="color:#555555">: </span>true               <span style="color:#aa5500"># 是否开启，默认：true</span>
 <span style="color:#221199">    ip</span><span style="color:#555555">: </span>127.0.0.1               <span style="color:#aa5500"># 服务端 ip 默认：127.0.0.1</span>
 <span style="color:#221199">    port</span><span style="color:#555555">: </span>5883                  <span style="color:#aa5500"># 端口，默认：1883</span>
 <span style="color:#221199">    name</span><span style="color:#555555">: </span>Mica-Mqtt-Server      <span style="color:#aa5500"># 名称，默认：Mica-Mqtt-Server</span>
 <span style="color:#221199">    buffer-allocator</span><span style="color:#555555">: </span>HEAP      <span style="color:#aa5500"># 堆内存和堆外内存，默认：堆内存</span>
 <span style="color:#221199">    heartbeat-timeout</span><span style="color:#555555">: </span>120000   <span style="color:#aa5500"># 心跳超时，单位毫秒，默认: 1000 * 120</span>
 <span style="color:#221199">    read-buffer-size</span><span style="color:#555555">: </span>8092      <span style="color:#aa5500"># 接收数据的 buffer size，默认：8092</span>
 <span style="color:#221199">    max-bytes-in-message</span><span style="color:#555555">: </span>8092  <span style="color:#aa5500"># 消息解析最大 bytes 长度，默认：8092</span>
 <span style="color:#221199">    debug</span><span style="color:#555555">: </span>true                 <span style="color:#aa5500"># 如果开启 prometheus 指标收集建议关闭</span>
 <span style="color:#221199">    websocket-enable</span><span style="color:#555555">: </span>true      <span style="color:#aa5500"># 开启 websocket 子协议，默认开启</span>
 <span style="color:#221199">    websocket-port</span><span style="color:#555555">: </span>8083        <span style="color:#aa5500"># websocket 端口，默认：8083</span></pre> 
<h3 style="text-align:start">5.3 服务端可实现接口（注册成 Spring Bean 即可）</h3> 
<table cellspacing="0" style="width:1140px"> 
 <thead> 
  <tr> 
   <th>接口</th> 
   <th>是否必须</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">IMqttServerAuthHandler</td> 
   <td style="border-color:#dfe2e5">是</td> 
   <td style="border-color:#dfe2e5">用于客户端认证</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">IMqttMessageListener</td> 
   <td style="border-color:#dfe2e5">是</td> 
   <td style="border-color:#dfe2e5">消息监听</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">IMqttConnectStatusListener</td> 
   <td style="border-color:#dfe2e5">是</td> 
   <td style="border-color:#dfe2e5">连接状态监听</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">IMqttSessionManager</td> 
   <td style="border-color:#dfe2e5">否</td> 
   <td style="border-color:#dfe2e5">session 管理</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">IMqttMessageStore</td> 
   <td style="border-color:#dfe2e5">集群是，单机否</td> 
   <td style="border-color:#dfe2e5">遗嘱和保留消息存储</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">AbstractMqttMessageDispatcher</td> 
   <td style="border-color:#dfe2e5">集群是，单机否</td> 
   <td style="border-color:#dfe2e5">消息转发，（遗嘱、保留消息转发）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">IpStatListener</td> 
   <td style="border-color:#dfe2e5">否</td> 
   <td style="border-color:#dfe2e5">t-io ip 状态监听</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">5.4 服务端自定义配置（可选）</h3> 
<pre style="text-align:left"> <span style="color:#555555">@Configuration</span>(<span style="color:#000000">proxyBeanMethods</span> <span style="color:#981a1a">=</span> <span style="color:#221199">false</span>)
 <span style="color:#770088">public</span> <span style="color:#770088">class</span> <span style="color:#0000ff">MqttServerCustomizerConfiguration</span> &#123;
 ​
     <span style="color:#555555">@Bean</span>
     <span style="color:#770088">public</span> <span style="color:#000000">MqttServerCustomizer</span> <span style="color:#000000">activeRecordPluginCustomizer</span>() &#123;
         <span style="color:#770088">return</span> <span style="color:#770088">new</span> <span style="color:#000000">MqttServerCustomizer</span>() &#123;
             <span style="color:#555555">@Override</span>
             <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">customize</span>(<span style="color:#000000">MqttServerCreator</span> <span style="color:#000000">creator</span>) &#123;
                 <span style="color:#aa5500">// 此处可自定义配置 creator，会覆盖 yml 中的配置</span>
                 <span style="color:#000000">System</span>.<span style="color:#000000">out</span>.<span style="color:#000000">println</span>(<span style="color:#aa1111">"----------------MqttServerCustomizer-----------------"</span>);
             &#125;
         &#125;;
     &#125;
 ​
 &#125;</pre> 
<h3 style="text-align:start">5.5 MqttServerTemplate 使用示例</h3> 
<pre style="text-align:left"> <span style="color:#770088">import</span> <span style="color:#000000">net</span>.<span style="color:#000000">dreamlu</span>.<span style="color:#000000">iot</span>.<span style="color:#000000">mqtt</span>.<span style="color:#000000">codec</span>.<span style="color:#000000">MqttQoS</span>;
 <span style="color:#770088">import</span> <span style="color:#000000">net</span>.<span style="color:#000000">dreamlu</span>.<span style="color:#000000">iot</span>.<span style="color:#000000">mqtt</span>.<span style="color:#000000">spring</span>.<span style="color:#000000">server</span>.<span style="color:#000000">MqttServerTemplate</span>;
 <span style="color:#770088">import</span> <span style="color:#000000">org</span>.<span style="color:#000000">springframework</span>.<span style="color:#000000">beans</span>.<span style="color:#000000">factory</span>.<span style="color:#000000">annotation</span>.<span style="color:#000000">Autowired</span>;
 <span style="color:#770088">import</span> <span style="color:#000000">org</span>.<span style="color:#000000">springframework</span>.<span style="color:#000000">stereotype</span>.<span style="color:#000000">Service</span>;
 ​
 <span style="color:#770088">import</span> <span style="color:#000000">java</span>.<span style="color:#000000">nio</span>.<span style="color:#000000">ByteBuffer</span>;
 ​
 <span style="color:#aa5500">/**</span>
  <span style="color:#aa5500">* @author wsq</span>
  <span style="color:#aa5500">*/</span>
 <span style="color:#555555">@Service</span>
 <span style="color:#770088">public</span> <span style="color:#770088">class</span> <span style="color:#0000ff">ServerService</span> &#123;
     <span style="color:#555555">@Autowired</span>
     <span style="color:#770088">private</span> <span style="color:#000000">MqttServerTemplate</span> <span style="color:#000000">server</span>;
 ​
     <span style="color:#770088">public</span> <span style="color:#008855">boolean</span> <span style="color:#000000">publish</span>(<span style="color:#008855">String</span> <span style="color:#000000">body</span>) &#123;
         <span style="color:#000000">server</span>.<span style="color:#000000">publishAll</span>(<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#000000">body</span>.<span style="color:#000000">getBytes</span>()));
         <span style="color:#770088">return</span> <span style="color:#221199">true</span>;
     &#125;
 &#125;</pre> 
<h3 style="text-align:start">5.6 基于 mq 消息广播集群处理</h3> 
<ul> 
 <li> <p>实现 <code>IMqttConnectStatusListener</code> 处理设备状态存储。</p> </li> 
 <li> <p>实现 <code>IMqttMessageListener</code> 将消息转发到 mq，业务按需处理 mq 消息。</p> </li> 
 <li> <p>实现 <code>IMqttMessageStore</code> 存储遗嘱和保留消息。</p> </li> 
 <li> <p>实现 <code>AbstractMqttMessageDispatcher</code> 将消息发往 mq，mq 再广播回 mqtt 集群，mqtt 将消息发送到设备。</p> </li> 
 <li> <p>业务消息发送到 mq，mq 广播到 mqtt 集群，mqtt 将消息发送到设备。</p> </li> 
</ul> 
<h3 style="text-align:start">5.7 Prometheus + Grafana 监控对接</h3> 
<p style="text-align:start">得益于 <strong>t-io</strong> 良好的设计，监控指标直接对接的 <strong>t-iostat</strong>，目前支持下列指标，后期会不断完善。</p> 
<table cellspacing="0" style="width:1140px"> 
 <thead> 
  <tr> 
   <th>支持得指标</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_connections_accepted</td> 
   <td style="border-color:#dfe2e5">共接受过连接数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_connections_closed</td> 
   <td style="border-color:#dfe2e5">关闭过的连接数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_connections_size</td> 
   <td style="border-color:#dfe2e5">当前连接数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_messages_handled_packets</td> 
   <td style="border-color:#dfe2e5">已处理消息数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_messages_handled_bytes</td> 
   <td style="border-color:#dfe2e5">已处理消息字节数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_messages_received_packets</td> 
   <td style="border-color:#dfe2e5">已接收消息数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_messages_received_bytes</td> 
   <td style="border-color:#dfe2e5">已处理消息字节数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_messages_send_packets</td> 
   <td style="border-color:#dfe2e5">已发送消息数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt_messages_send_bytes</td> 
   <td style="border-color:#dfe2e5">已发送消息字节数</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start"><img alt height="766" src="https://oscimg.oschina.net/oscnet/up-6b982b8f8c33606ba7f2c07158779a4debe.JPEG" width="752" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">关于 <strong>mica-mqtt-spring-boot-starter</strong> 更多请查看文档：<a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter">https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-spring-boot-starter</a></p> 
<h2 style="text-align:start">六、普通 java 项目接入</h2> 
<h3 style="text-align:start">6.1 maven 依赖</h3> 
<pre style="text-align:left">  <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-core<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.0.3<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
  <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></pre> 
<h3 style="text-align:start">6.2 mica-mqtt 客户端</h3> 
<pre style="text-align:left">  <span style="color:#aa5500">// 初始化 mqtt 客户端</span>
  <span style="color:#000000">MqttClient</span> <span style="color:#000000">client</span> <span style="color:#981a1a">=</span> <span style="color:#000000">MqttClient</span>.<span style="color:#000000">create</span>()
      .<span style="color:#000000">ip</span>(<span style="color:#aa1111">"127.0.0.1"</span>)
      .<span style="color:#000000">port</span>(<span style="color:#116644">1883</span>)                     <span style="color:#aa5500">// 默认：1883</span>
      .<span style="color:#000000">username</span>(<span style="color:#aa1111">"admin"</span>)
      .<span style="color:#000000">password</span>(<span style="color:#aa1111">"123456"</span>)
      .<span style="color:#000000">version</span>(<span style="color:#000000">MqttVersion</span>.<span style="color:#000000">MQTT_5</span>)    <span style="color:#aa5500">// 默认：3_1_1</span>
      .<span style="color:#000000">clientId</span>(<span style="color:#aa1111">"xxxxxx"</span>)             <span style="color:#aa5500">// 默认：MICA-MQTT- 前缀和 36进制的纳秒数</span>
      .<span style="color:#000000">connect</span>();                     <span style="color:#aa5500">// 连接</span>
  
      <span style="color:#aa5500">// 消息订阅，同类方法 subxxx</span>
      <span style="color:#000000">client</span>.<span style="color:#000000">subQos0</span>(<span style="color:#aa1111">"/test/#"</span>, (<span style="color:#000000">topic</span>, <span style="color:#000000">payload</span>) <span style="color:#981a1a">-></span> &#123;
          <span style="color:#000000">logger</span>.<span style="color:#000000">info</span>(<span style="color:#000000">topic</span> <span style="color:#981a1a">+</span> <span style="color:#aa1111">'\t'</span> <span style="color:#981a1a">+</span> <span style="color:#000000">ByteBufferUtil</span>.<span style="color:#000000">toString</span>(<span style="color:#000000">payload</span>));
      &#125;);
      <span style="color:#aa5500">// 取消订阅</span>
      <span style="color:#000000">client</span>.<span style="color:#000000">unSubscribe</span>(<span style="color:#aa1111">"/test/#"</span>);
  
      <span style="color:#aa5500">// 发送消息</span>
      <span style="color:#000000">client</span>.<span style="color:#000000">publish</span>(<span style="color:#aa1111">"/test/client"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>(<span style="color:#000000">StandardCharsets</span>.<span style="color:#000000">UTF_8</span>)));
  
      <span style="color:#aa5500">// 断开连接</span>
      <span style="color:#000000">client</span>.<span style="color:#000000">disconnect</span>();
      <span style="color:#aa5500">// 重连</span>
      <span style="color:#000000">client</span>.<span style="color:#000000">reconnect</span>();
      <span style="color:#aa5500">// 停止</span>
      <span style="color:#000000">client</span>.<span style="color:#000000">stop</span>();</pre> 
<h3 style="text-align:start">6.3 mica-mqtt 服务端</h3> 
<pre style="text-align:left">  <span style="color:#aa5500">// 注意：为了能接受更多链接（降低内存），请添加 jvm 参数 -Xss129k</span>
  <span style="color:#000000">MqttServer</span> <span style="color:#000000">mqttServer</span> <span style="color:#981a1a">=</span> <span style="color:#000000">MqttServer</span>.<span style="color:#000000">create</span>()
      <span style="color:#aa5500">// 默认：127.0.0.1</span>
      .<span style="color:#000000">ip</span>(<span style="color:#aa1111">"127.0.0.1"</span>)
      <span style="color:#aa5500">// 默认：1883</span>
      .<span style="color:#000000">port</span>(<span style="color:#116644">1883</span>)
      <span style="color:#aa5500">// 默认为： 8092（mqtt 默认最大消息大小），为了降低内存可以减小小此参数，如果消息过大 t-io 会尝试解析多次（建议根据实际业务情况而定）</span>
      .<span style="color:#000000">readBufferSize</span>(<span style="color:#116644">512</span>)
      <span style="color:#aa5500">// 自定义认证</span>
      .<span style="color:#000000">authHandler</span>((<span style="color:#000000">clientId</span>, <span style="color:#000000">userName</span>, <span style="color:#000000">password</span>) <span style="color:#981a1a">-></span> <span style="color:#221199">true</span>)
      <span style="color:#aa5500">// 消息监听</span>
      .<span style="color:#000000">messageListener</span>((<span style="color:#000000">clientId</span>, <span style="color:#000000">topic</span>, <span style="color:#000000">mqttQoS</span>, <span style="color:#000000">payload</span>) <span style="color:#981a1a">-></span> &#123;
          <span style="color:#000000">logger</span>.<span style="color:#000000">info</span>(<span style="color:#aa1111">"clientId:&#123;&#125; topic:&#123;&#125; mqttQoS:&#123;&#125; message:&#123;&#125;"</span>, <span style="color:#000000">clientId</span>, <span style="color:#000000">topic</span>, <span style="color:#000000">mqttQoS</span>, <span style="color:#000000">ByteBufferUtil</span>.<span style="color:#000000">toString</span>(<span style="color:#000000">payload</span>));
      &#125;)
      <span style="color:#aa5500">// ssl 配置</span>
      .<span style="color:#000000">useSsl</span>(<span style="color:#aa1111">""</span>, <span style="color:#aa1111">""</span>, <span style="color:#aa1111">""</span>)
      <span style="color:#aa5500">// 自定义客户端上下线监听</span>
      .<span style="color:#000000">connectStatusListener</span>(<span style="color:#770088">new</span> <span style="color:#000000">IMqttConnectStatusListener</span>() &#123;
          <span style="color:#555555">@Override</span>
          <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">online</span>(<span style="color:#008855">String</span> <span style="color:#000000">clientId</span>) &#123;
  
          &#125;
  
          <span style="color:#555555">@Override</span>
          <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">offline</span>(<span style="color:#008855">String</span> <span style="color:#000000">clientId</span>) &#123;
  
          &#125;
      &#125;)
      <span style="color:#aa5500">// 自定义消息转发，可用 mq 广播实现集群化处理</span>
      .<span style="color:#000000">messageDispatcher</span>(<span style="color:#770088">new</span> <span style="color:#000000">IMqttMessageDispatcher</span>() &#123;
          <span style="color:#555555">@Override</span>
          <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">config</span>(<span style="color:#000000">MqttServer</span> <span style="color:#000000">mqttServer</span>) &#123;
  
          &#125;
  
          <span style="color:#555555">@Override</span>
          <span style="color:#770088">public</span> <span style="color:#008855">boolean</span> <span style="color:#000000">send</span>(<span style="color:#000000">Message</span> <span style="color:#000000">message</span>) &#123;
              <span style="color:#770088">return</span> <span style="color:#221199">false</span>;
          &#125;
  
          <span style="color:#555555">@Override</span>
          <span style="color:#770088">public</span> <span style="color:#008855">boolean</span> <span style="color:#000000">send</span>(<span style="color:#008855">String</span> <span style="color:#000000">clientId</span>, <span style="color:#000000">Message</span> <span style="color:#000000">message</span>) &#123;
              <span style="color:#770088">return</span> <span style="color:#221199">false</span>;
          &#125;
      &#125;)
      .<span style="color:#000000">debug</span>() <span style="color:#aa5500">// 开启 t-io debug 信息日志</span>
      .<span style="color:#000000">start</span>();
  
  <span style="color:#aa5500">// 发送给某个客户端</span>
  <span style="color:#000000">mqttServer</span>.<span style="color:#000000">publish</span>(<span style="color:#aa1111">"clientId"</span>,<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()));
  
  <span style="color:#aa5500">// 发送给所有在线监听这个 topic 的客户端</span>
  <span style="color:#000000">mqttServer</span>.<span style="color:#000000">publishAll</span>(<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()));
  
  <span style="color:#aa5500">// 停止服务</span>
  <span style="color:#000000">mqttServer</span>.<span style="color:#000000">stop</span>();</pre> 
<h2 style="text-align:start">七、效果演示</h2> 
<p style="text-align:start"><img alt height="437" src="https://oscimg.oschina.net/oscnet/up-1183eb0e85ef5279586b2ee90467ece3df5.gif" width="720" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="background-color:#ffffff; color:#333333">建议关注</span><code>如梦技术</code><span style="background-color:#ffffff; color:#333333">码云：</span><a href="https://gitee.com/596392912">https://gitee.com/596392912</a><span style="background-color:#ffffff; color:#333333"> ，更多优秀开源项目</span><span style="background-color:#f6f6f6; color:#333333">等你来发现</span><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            