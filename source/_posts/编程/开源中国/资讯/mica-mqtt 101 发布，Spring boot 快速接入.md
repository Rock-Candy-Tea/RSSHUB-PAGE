
---
title: 'mica-mqtt 1.0.1 发布，Spring boot 快速接入'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-651f520285c064d6633b045e659ba764bf3.gif'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 10:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-651f520285c064d6633b045e659ba764bf3.gif'
---

<div>   
<div class="content">
                                                                                            <h1 style="text-align:start">一、简介</h1> 
<p style="text-align:start"><strong>mica-mqtt</strong> 基于 <strong>t-io</strong> 实现的<strong>简单</strong>、<strong>低延迟</strong>、<strong>高性能</strong> 的 mqtt 物联网开源组件。<strong>使用详见</strong>：<code>mica-mqtt-example</code> 模块。</p> 
<h2 style="text-align:start">二、功能</h2> 
<ul> 
 <li>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</li> 
 <li>支持 MQTT client 客户端。</li> 
 <li>支持 MQTT server 服务端。</li> 
 <li>支持 MQTT 遗嘱消息。</li> 
 <li>支持 MQTT 保留消息。</li> 
 <li>支持自定义消息（mq）处理转发实现集群。</li> 
 <li>MQTT 客户端 阿里云 mqtt 连接 demo。</li> 
 <li>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</li> 
</ul> 
<h2 style="text-align:start">三、待办</h2> 
<ul> 
 <li>添加 websocket 支持（已预研成功）。</li> 
 <li>优化处理 mqtt session，以及支持 v5.0</li> 
</ul> 
<h2 style="text-align:start">四、更新记录</h2> 
<ul> 
 <li> <p>✨ 订阅管理集成到 session 管理中。</p> </li> 
 <li> <p>✨ MqttProperties.MqttPropertyType 添加注释，考虑 mqtt V5.0 新特性处理。</p> </li> 
 <li> <p>✨ 添加 Spring boot starter 方便接入，兼容低版本 Spring boot。</p> </li> 
 <li> <p>✨ 调研 t-io websocket 子协议。</p> </li> 
 <li> <p>🐛 修复 java8 运行期间的部分问题，NoSuchMethodError: java.nio.ByteBuffer.xxx</p> </li> 
</ul> 
<h2 style="text-align:start">五、Spring boot 快速接入</h2> 
<h3 style="text-align:start">5.1 添加依赖</h3> 
<pre style="text-align:left"> <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
     <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
     <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-spring-boot-starter<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
     <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>$&#123;最新版本&#125;<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
 <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></pre> 
<h3 style="text-align:start">5.2 配置项</h3> 
<table cellspacing="0" style="width:1140px"> 
 <thead> 
  <tr> 
   <th>配置项</th> 
   <th>默认值</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.name</td> 
   <td style="border-color:#dfe2e5">Mica-Mqtt-Server</td> 
   <td style="border-color:#dfe2e5">名称</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.port</td> 
   <td style="border-color:#dfe2e5">1883</td> 
   <td style="border-color:#dfe2e5">端口</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.ip</td> 
   <td style="border-color:#dfe2e5">127.0.0.1</td> 
   <td style="border-color:#dfe2e5">服务端 ip</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.buffer-allocator</td> 
   <td style="border-color:#dfe2e5">堆内存</td> 
   <td style="border-color:#dfe2e5">堆内存和堆外内存</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.heartbeat-timeout</td> 
   <td style="border-color:#dfe2e5">120s</td> 
   <td style="border-color:#dfe2e5">心跳超时时间(单位: 毫秒 默认: 1000 * 120)，如果用户不希望框架层面做心跳相关工作，请把此值设为0或负数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.read-buffer-size</td> 
   <td style="border-color:#dfe2e5">8092</td> 
   <td style="border-color:#dfe2e5">接收数据的 buffer size，默认：8092</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.max-bytes-in-message</td> 
   <td style="border-color:#dfe2e5">8092</td> 
   <td style="border-color:#dfe2e5">消息解析最大 bytes 长度，默认：8092</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">mqtt.server.debug</td> 
   <td style="border-color:#dfe2e5">false</td> 
   <td style="border-color:#dfe2e5">debug</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">5.3 可实现接口（注册成 Spring Bean 即可）</h3> 
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
   <td style="border-color:#dfe2e5">IMqttMessageDispatcher</td> 
   <td style="border-color:#dfe2e5">集群是，单机否</td> 
   <td style="border-color:#dfe2e5">消息转发</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">IpStatListener</td> 
   <td style="border-color:#dfe2e5">否</td> 
   <td style="border-color:#dfe2e5">t-io ip 转态监听</td> 
  </tr> 
 </tbody> 
</table> 
<h3 style="text-align:start">5.4 自定义配置（可选）</h3> 
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
<h2 style="text-align:start">六、普通 java 项目接入</h2> 
<h3 style="text-align:start">6.1 maven 依赖</h3> 
<pre style="text-align:left">  <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-core<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>1.0.1<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
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
  <span style="color:#000000">mqttServer</span>.<span style="color:#000000">publish</span>(<span style="color:#aa1111">"clientId"</span>,<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()), <span style="color:#000000">MqttQoS</span>.<span style="color:#000000">EXACTLY_ONCE</span>);
  
  <span style="color:#aa5500">// 发送给所有在线监听这个 topic 的客户端</span>
  <span style="color:#000000">mqttServer</span>.<span style="color:#000000">publishAll</span>(<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()), <span style="color:#000000">MqttQoS</span>.<span style="color:#000000">EXACTLY_ONCE</span>);
  
  <span style="color:#aa5500">// 停止服务</span>
  <span style="color:#000000">mqttServer</span>.<span style="color:#000000">stop</span>();</pre> 
<h2 style="text-align:start">七、效果演示</h2> 
<p style="text-align:start"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-651f520285c064d6633b045e659ba764bf3.gif" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">八、相关文档</h2> 
<ul> 
 <li> <p><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/starter.md">mica-mqtt-spring-boot-starter 使用文档</a></p> </li> 
 <li> <p><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/docs.md">mica-mqtt 使用文档</a></p> </li> 
 <li> <p><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md">mica-mqtt 发行版本</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.tiocloud.com%2Fdoc%2Ftio%2F85" target="_blank">t-io 官方文档</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmcxiaoke%2Fmqtt" target="_blank">mqtt 协议文档</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            