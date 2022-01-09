
---
title: 'mica-mqtt 1.2.4 发布，优化完善 mqtt 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=687'
author: 开源中国
comments: false
date: Sun, 09 Jan 2022 13:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=687'
---

<div>   
<div class="content">
                                                                                            <h2><span>一、简介</span></h2> 
<p style="margin-left:.8em; margin-right:.8em"><span><span><strong><span>mica-mqtt</span></strong><span> 基于 </span><span><strong><span>t-io</span></strong><span> 实现的</span><span><strong><span>简单</span></strong><span>、</span><span><strong><span>低延迟</span></strong><span>、</span><span><strong><span>高性能</span></strong><span> 的 mqtt 物联网开源组件。</span></span></span></span></span></span></span></p> 
<p style="margin-left:.8em; margin-right:.8em"><span><span><strong><span>mica-mqtt</span></strong><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></span></span></p> 
<h2><span>二、功能</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT v3.1、v3.1.1 以及 v5.0 协议。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 websocket mqtt 子协议（支持 mqtt.js）。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 http rest api，</span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>http api 文档详见</span></a><span>。</span></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT client 客户端。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT server 服务端。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT 遗嘱消息。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 MQTT 保留消息。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持自定义消息（mq）处理转发实现集群。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>MQTT 客户端 阿里云 mqtt 连接 demo。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 GraalVM 编译成本机可执行程序。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>支持 Spring boot 项目快速接入（mica-mqtt-spring-boot-starter）。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>mica-mqtt-spring-boot-starter 支持对接 Prometheus + Grafana。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>基于 redis pub/sub 实现集群，详见 </span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-broker"><span>mica-mqtt-broker 模块</span></a><span>。</span></span></span></p> </li> 
</ul> 
<h2><span>三、使用场景</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>物联网（云端 mqtt broker）</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>物联网（边缘端消息通信）</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>群组类 IM</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>消息推送</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>简单、易用的 mqtt client 客户端</span></span></p> </li> 
</ul> 
<h2><span>四、更新记录</span></h2> 
<h3><span>v1.2.4 - 2022-01-09</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>🔥 mica-mqtt-core 排除一些不需要的依赖。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>🔥 mica-mqtt-core http websocket 都不开启时，可以排除 tio-websocket-server 依赖。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-core MqttTopicUtil 改名为 TopicUtil。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-spring-boot-starter @MqttClientSubscribe 支持 IMqttClientMessageListener bean。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-spring-boot-starter @MqttClientSubscribe 支持自定义 MqttClientTemplate Bean。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-spring-boot-starter 完善。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-codec 缩短 mqtt 版本 key。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>🐛 mica-mqtt-codec 修复 will message。</span></span></p> </li> 
</ul> 
<h3><span>v1.2.3 - 2022-01-03</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-spring-boot-starter @MqttClientSubscribe value 改为数组，支持同时订阅多 topic。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-core 缓存 TopicFilter Pattern。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt-core 优化客户端和服务端订阅逻辑 IMqttServerSubscribeValidator 接口调整。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt client 添加批量订阅。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt client 添加批量取消订阅。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt client 添加客户端是否断开连接。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt client 客户端断开重新订阅时支持配置批次大小。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>✨ mica-mqtt client 订阅 IMqttClientMessageListener 添加 onSubscribed 回调方法（默认方法用于自定义实现）。</span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span>⬆️ mica-mqtt-example 升级 log4j2 到 2.17.1</span></span></p> </li> 
</ul> 
<h2><span>五、使用文档和示例</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-core/README.md"><span>mica-mqtt 使用文档</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-spring-boot-starter/README.md"><span>mica-mqtt-spring-boot-starter 使用文档</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>mica-mqtt http api 文档详见</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md"><span>mica-mqtt 发行版本记录</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-broker"><span>基于 redis 的 mqtt broker 集群示例</span></a></span></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:.5rem"><span><span><a href="https://gitee.com/openharmony-tpc/talkweb_mqtt"><span>基于 kafka 的 mqtt broker 集群示例</span></a></span></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            