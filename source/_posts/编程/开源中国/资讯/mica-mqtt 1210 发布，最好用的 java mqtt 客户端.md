
---
title: 'mica-mqtt 1.2.10 发布，最好用的 java mqtt 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8594'
author: 开源中国
comments: false
date: Sun, 03 Apr 2022 17:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8594'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start"><span>一、简介</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>mica-mqtt</span></strong></span><span> 基于 </span><span><strong><span>t-io</span></strong></span><span> 实现的</span><span><strong><span>简单</span></strong></span><span>、</span><span><strong><span>低延迟</span></strong></span><span>、</span><span><strong><span>高性能</span></strong></span><span> 的 mqtt 物联网开源组件。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>mica-mqtt</span></strong></span><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></p> 
<h2 style="text-align:start"><span>二、功能</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 websocket mqtt 子协议（支持 mqtt.js）。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 http rest api，</span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>http api 文档详见</span></a></span><span>。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT client 客户端。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT server 服务端。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT 遗嘱消息。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 MQTT 保留消息。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持自定义消息（mq）处理转发实现集群。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>MQTT 客户端 阿里云 mqtt 连接 demo。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 GraalVM 编译成本机可执行程序。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>基于 redis pub/sub 实现集群，详见 </span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker"><span>mica-mqtt-broker 模块</span></a></span><span>。</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>三、使用场景</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>物联网（云端 mqtt broker）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>物联网（边缘端消息通信）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>群组类 IM</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>消息推送</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>简单、易用的 mqtt client 客户端</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>四、更新记录</span></h2> 
<h3 style="text-align:start"><span>v1.2.10</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 添加 MQTT 客户端 </span><span><code>keepalive</code></span><span> 系数 </span><span><code>keepalive-backoff</code></span><span>。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client、server 调整发布的日志级别为 debug。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 优化 javadoc。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 重连时，支持重新设置新的鉴权账号和密码。</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>v1.2.9</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mqttServer#publishAll() 日志级别调整 gitee #I4W4IS</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ </span><span><code>@MqttClientSubscribe</code></span><span> 支持 springboot 配置 gitee #I4UOR3</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 代码优化</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt-spring-boot-example 拆分</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>五、使用文档和示例</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-core/README.md"><span>mica-mqtt 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-spring-boot-starter/README.md"><span>mica-mqtt-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>mica-mqtt http api 文档详见</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md"><span>mica-mqtt 发行版本记录</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-broker"><span>基于 redis 的 mqtt broker 集群示例</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/openharmony-tpc/talkweb_mqtt"><span>基于 kafka 的 mqtt broker 集群示例</span></a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            