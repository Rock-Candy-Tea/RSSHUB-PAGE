
---
title: 'mica-mqtt 1.0.0 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-651f520285c064d6633b045e659ba764bf3.gif'
author: 开源中国
comments: false
date: Fri, 30 Jul 2021 10:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-651f520285c064d6633b045e659ba764bf3.gif'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start">一、简介</h2> 
<p style="text-align:start"><strong>mica-mqtt</strong> 基于 <strong>t-io</strong> 实现的<strong>简单</strong>、<strong>低延迟</strong>、<strong>高性能</strong> 的 mqtt 物联网开源组件。<strong>使用详见Gitee</strong>： <a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-example/src/main/java/net/dreamlu/iot/mqtt"><code>mica-mqtt-example</code></a> 模块。</p> 
<h2 style="text-align:start">二、功能</h2> 
<ul> 
 <li>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</li> 
 <li>支持 MQTT client 客户端。</li> 
 <li>支持 MQTT server 服务端。</li> 
 <li>支持 MQTT 遗嘱消息。</li> 
 <li>支持 MQTT 保留消息。</li> 
 <li>支持自定义消息（mq）处理转发实现集群。</li> 
 <li>支持 GraalVM 编译成本机可执行程序。</li> 
 <li>MQTT 客户端 阿里云 mqtt 连接 demo。</li> 
</ul> 
<h2 style="text-align:start">三、待办</h2> 
<ul> 
 <li>添加 Spring boot stater。</li> 
 <li>添加 websocket 子协议支持 mqtt.js。</li> 
</ul> 
<h2 style="text-align:start">四、使用</h2> 
<h3 style="text-align:start">4.1 maven 依赖</h3> 
<pre style="text-align:left"> <span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>mica-mqtt-core<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
   <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>$&#123;最新版本&#125;<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
 <span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></pre> 
<h3 style="text-align:start">4.2 mica-mqtt 客户端</h3> 
<pre style="text-align:left"> <span style="color:#aa5500">// 初始化 mqtt 客户端</span>
 <span style="color:#000000">MqttClient</span> <span style="color:#000000">client</span> <span style="color:#981a1a">=</span> <span style="color:#000000">MqttClient</span>.<span style="color:#000000">create</span>()
     .<span style="color:#000000">ip</span>(<span style="color:#aa1111">"127.0.0.1"</span>)
     .<span style="color:#000000">port</span>(<span style="color:#116644">1883</span>)                     <span style="color:#aa5500">// 默认：1883</span>
     .<span style="color:#000000">username</span>(<span style="color:#aa1111">"admin"</span>)
     .<span style="color:#000000">password</span>(<span style="color:#aa1111">"123456"</span>)
     .<span style="color:#000000">version</span>(<span style="color:#000000">MqttVersion</span>.<span style="color:#000000">MQTT_5</span>)    <span style="color:#aa5500">// 默认：3_1_1</span>
     .<span style="color:#000000">clientId</span>(<span style="color:#aa1111">"xxxxxx"</span>)             <span style="color:#aa5500">// 默认：MICA-MQTT- 前缀和 36进制的纳秒数</span>
     .<span style="color:#000000">bufferAllocator</span>(<span style="color:#000000">ByteBufferAllocator</span>.<span style="color:#000000">DIRECT</span>) <span style="color:#aa5500">// 堆内存和堆外内存，默认：堆内存</span>
     .<span style="color:#000000">readBufferSize</span>(<span style="color:#116644">512</span>)            <span style="color:#aa5500">// 消息一起解析的长度，默认：为 8092 （mqtt 消息最大长度）</span>
     .<span style="color:#000000">keepAliveSecs</span>(<span style="color:#116644">120</span>)             <span style="color:#aa5500">// 默认：60s</span>
     .<span style="color:#000000">timeout</span>(<span style="color:#116644">10</span>)                    <span style="color:#aa5500">// 超时时间，t-io 配置，可为 null，为 null 时，t-io 默认为 5</span>
     .<span style="color:#000000">reconnect</span>(<span style="color:#221199">true</span>)                <span style="color:#aa5500">// 是否重连，默认：true</span>
     .<span style="color:#000000">reInterval</span>(<span style="color:#116644">5000</span>)               <span style="color:#aa5500">// 重连重试时间，reconnect 为 true 时有效，t-io 默认为：5000</span>
     .<span style="color:#000000">willMessage</span>(<span style="color:#000000">builder</span> <span style="color:#981a1a">-></span> &#123;
     <span style="color:#000000">builder</span>.<span style="color:#000000">topic</span>(<span style="color:#aa1111">"/test/offline"</span>).<span style="color:#000000">messageText</span>(<span style="color:#aa1111">"hello"</span>);    <span style="color:#aa5500">// 遗嘱消息</span>
     &#125;)
     <span style="color:#aa5500">// .properties()                // mqtt5 properties</span>
     .<span style="color:#000000">connect</span>();                     <span style="color:#aa5500">// 连接</span>
 ​
     <span style="color:#aa5500">// 消息订阅，同类方法 subxxx</span>
     <span style="color:#000000">client</span>.<span style="color:#000000">subQos0</span>(<span style="color:#aa1111">"/test/#"</span>, (<span style="color:#000000">topic</span>, <span style="color:#000000">payload</span>) <span style="color:#981a1a">-></span> &#123;
         <span style="color:#000000">logger</span>.<span style="color:#000000">info</span>(<span style="color:#000000">topic</span> <span style="color:#981a1a">+</span> <span style="color:#aa1111">'\t'</span> <span style="color:#981a1a">+</span> <span style="color:#000000">ByteBufferUtil</span>.<span style="color:#000000">toString</span>(<span style="color:#000000">payload</span>));
     &#125;);
     <span style="color:#aa5500">// 取消订阅</span>
     <span style="color:#000000">client</span>.<span style="color:#000000">unSubscribe</span>(<span style="color:#aa1111">"/test/#"</span>);
 ​
     <span style="color:#aa5500">// 发送消息</span>
     <span style="color:#000000">client</span>.<span style="color:#000000">publish</span>(<span style="color:#aa1111">"/test/client"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>(<span style="color:#000000">StandardCharsets</span>.<span style="color:#000000">UTF_8</span>)));
 ​
     <span style="color:#aa5500">// 断开连接</span>
     <span style="color:#000000">client</span>.<span style="color:#000000">disconnect</span>();
     <span style="color:#aa5500">// 重连</span>
     <span style="color:#000000">client</span>.<span style="color:#000000">reconnect</span>();
     <span style="color:#aa5500">// 停止</span>
     <span style="color:#000000">client</span>.<span style="color:#000000">stop</span>();</pre> 
<h3 style="text-align:start">4.3 mica-mqtt 服务端</h3> 
<pre style="text-align:left"> <span style="color:#aa5500">// 注意：为了能接受更多链接（降低内存），请添加 jvm 参数 -Xss129k</span>
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
     <span style="color:#aa5500">// 堆内存和堆外内存选择，默认：堆内存</span>
     .<span style="color:#000000">bufferAllocator</span>(<span style="color:#000000">ByteBufferAllocator</span>.<span style="color:#000000">HEAP</span>)
     <span style="color:#aa5500">// 心跳超时时间，默认：120s</span>
     .<span style="color:#000000">heartbeatTimeout</span>(<span style="color:#116644">120_1000L</span>)
     <span style="color:#aa5500">// ssl 配置</span>
     .<span style="color:#000000">useSsl</span>(<span style="color:#aa1111">""</span>, <span style="color:#aa1111">""</span>, <span style="color:#aa1111">""</span>)
     <span style="color:#aa5500">// 自定义客户端上下线监听</span>
     .<span style="color:#000000">connectStatusListener</span>(<span style="color:#770088">new</span> <span style="color:#000000">IMqttConnectStatusListener</span>() &#123;
         <span style="color:#555555">@Override</span>
         <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">online</span>(<span style="color:#008855">String</span> <span style="color:#000000">clientId</span>) &#123;
 ​
         &#125;
 ​
         <span style="color:#555555">@Override</span>
         <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">offline</span>(<span style="color:#008855">String</span> <span style="color:#000000">clientId</span>) &#123;
 ​
         &#125;
     &#125;)
     <span style="color:#aa5500">// 自定义消息转发，可用 mq 广播实现集群化处理</span>
     .<span style="color:#000000">messageDispatcher</span>(<span style="color:#770088">new</span> <span style="color:#000000">IMqttMessageDispatcher</span>() &#123;
         <span style="color:#555555">@Override</span>
         <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">config</span>(<span style="color:#000000">MqttServer</span> <span style="color:#000000">mqttServer</span>) &#123;
 ​
         &#125;
 ​
         <span style="color:#555555">@Override</span>
         <span style="color:#770088">public</span> <span style="color:#008855">boolean</span> <span style="color:#000000">send</span>(<span style="color:#000000">Message</span> <span style="color:#000000">message</span>) &#123;
             <span style="color:#770088">return</span> <span style="color:#221199">false</span>;
         &#125;
 ​
         <span style="color:#555555">@Override</span>
         <span style="color:#770088">public</span> <span style="color:#008855">boolean</span> <span style="color:#000000">send</span>(<span style="color:#008855">String</span> <span style="color:#000000">clientId</span>, <span style="color:#000000">Message</span> <span style="color:#000000">message</span>) &#123;
             <span style="color:#770088">return</span> <span style="color:#221199">false</span>;
         &#125;
     &#125;)
     .<span style="color:#000000">debug</span>() <span style="color:#aa5500">// 开启 t-io debug 信息日志</span>
     .<span style="color:#000000">start</span>();
 ​
 <span style="color:#aa5500">// 发送给某个客户端</span>
 <span style="color:#000000">mqttServer</span>.<span style="color:#000000">publish</span>(<span style="color:#aa1111">"clientId"</span>,<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()), <span style="color:#000000">MqttQoS</span>.<span style="color:#000000">EXACTLY_ONCE</span>);
 ​
 <span style="color:#aa5500">// 发送给所有在线监听这个 topic 的客户端</span>
 <span style="color:#000000">mqttServer</span>.<span style="color:#000000">publishAll</span>(<span style="color:#aa1111">"/test/123"</span>, <span style="color:#000000">ByteBuffer</span>.<span style="color:#000000">wrap</span>(<span style="color:#aa1111">"mica最牛皮"</span>.<span style="color:#000000">getBytes</span>()), <span style="color:#000000">MqttQoS</span>.<span style="color:#000000">EXACTLY_ONCE</span>);
 ​
 <span style="color:#aa5500">// 停止服务</span>
 <span style="color:#000000">mqttServer</span>.<span style="color:#000000">stop</span>();
</pre> 
<h2 style="text-align:start">五、效果演示</h2> 
<p style="text-align:start"><img alt height="450" src="https://oscimg.oschina.net/oscnet/up-651f520285c064d6633b045e659ba764bf3.gif" width="800" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">六、文档和资源</h2> 
<ul> 
 <li><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/docs.md">mica-mqtt 使用文档</a></li> 
 <li><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md">mica-mqtt 发行版本</a></li> 
</ul>
                                        </div>
                                      
</div>
            