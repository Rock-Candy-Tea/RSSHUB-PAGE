
---
title: 'mica-mqtt 1.3.9 发布，修复 mqtt client QOS2 retry bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1170'
author: 开源中国
comments: false
date: Fri, 02 Sep 2022 09:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1170'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start"><span>一、简介</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>mica-mqtt</span></strong></span><span> 基于 </span><span><strong><span>t-io</span></strong></span><span> 实现的</span><span><strong><span>简单</span></strong></span><span>、</span><span><strong><span>低延迟</span></strong></span><span>、</span><span><strong><span>高性能</span></strong></span><span> 的 mqtt 物联网开源组件。</span><span><strong><span>mica-mqtt</span></strong></span><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></p> 
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
<h3 style="text-align:start"><span>v1.3.9 - 2022-08-28</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt server 添加消息拦截器，gitee #I5KLST</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt client、server ack 优化和完善，可自定义 ackService。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt client stater MqttClientTemplate 完善，统一调整客户端示例。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt client 优化客户端心跳和心跳日志优化。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt client 订阅代码优化。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt codec 代码优化。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> test 代码优化，更加符合 junit5 规范。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛</span><span> mqtt client Qos2 retry 问题修复。</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>v1.3.8 - 2022-08-11</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt codec 代码优化。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt server 使用 Spring event 解耦消息监听。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt client stater，@MqttClientSubscribe topic 支持其他变量 $&#123;productKey&#125; 自动替换成 +。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>📝</span><span> 添加演示地址</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>🐛</span><span> 修复 mica-mqtt client 心跳更好的支持 emqx。gitee #I5LQXV 感谢 </span><span><code>@iTong</code></span><span> 反馈。</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>v1.3.7 - 2022-07-24</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> 添加 mica-mqtt jfinal client 和 server 插件。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt server 代码优化，useQueueDecode 默认为 true。 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨</span><span> mica-mqtt client 监听回调代码优化。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>📝</span><span> 添加赞助，让你我走的更远！！！</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>⬆️</span><span> 依赖升级。</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>五、重点说明</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在 1.3.8 和 1.3.9 中均对 mica mqtt client 进行了 bug 修复，建议升级到最新版本。 </span></p> 
<h2 style="text-align:start"><span>六、使用文档和示例</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/example/README.md"><span>mica-mqtt 快速开始</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-client-spring-boot-starter/README.md"><span>mica-mqtt-client-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-server-spring-boot-starter/README.md"><span>mica-mqtt-server-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-core/README.md"><span>mica-mqtt 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>mica-mqtt http api 文档详见</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md"><span>mica-mqtt 发行版本</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-broker"><span>基于 redis 的 mqtt broker 集群示例</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/openharmony-tpc/talkweb_mqtt"><span>基于 kafka 的 mqtt broker 集群示例</span></a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            