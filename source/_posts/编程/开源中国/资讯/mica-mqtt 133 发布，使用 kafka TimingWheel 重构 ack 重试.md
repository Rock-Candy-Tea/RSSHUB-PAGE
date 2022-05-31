
---
title: 'mica-mqtt 1.3.3 发布，使用 kafka TimingWheel 重构 ack 重试'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-09dde76bcd99f3a9712d022d37110d64f78.gif'
author: 开源中国
comments: false
date: Tue, 31 May 2022 08:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-09dde76bcd99f3a9712d022d37110d64f78.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start"><span>一、简介</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:start"><span><strong><span>mica-mqtt</span></strong></span><span> 基于 </span><span><strong><span>t-io</span></strong></span><span> 实现的</span><span><strong><span>简单</span></strong></span><span>、</span><span><strong><span>低延迟</span></strong></span><span>、</span><span><strong><span>高性能</span></strong></span><span> 的 mqtt 物联网开源组件。</span><span><strong><span>mica-mqtt</span></strong></span><span> 更加易于集成到已有服务和二次开发，降低自研物联网平台开发成本。</span></p> 
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
<h3 style="text-align:start"><span>v1.3.3 - 2022-05-28</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt 添加 kafka TimingWheel 重构 ack。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt 优化线程池。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt 添加 Compression 压缩接口。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt server 添加 MqttClusterMessageListener 方便集群消息处理。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>✨ mica-mqtt client 优化客户端取消订阅逻辑，gitee #I5779A 感谢 @杨钊 同学反馈。</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>⬆️ 升级 fastjson 到 1.2.83。</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>五、重点说明</span></h2> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:start"><span>此版本优化了订阅、取消订阅和 Qos1~2 的 ack 重试机制，默认重试 5 次，重试间隔为 10s。</span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:start"><span>将 ack 重试由 ScheduledThreadPoolExecutor 改为了更加 kafka TimingWheel 多层时间轮。未来会使用 TimingWheel 实现更多业务需求，例如延迟消息等。</span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:start"><span><img alt height="717" src="https://oscimg.oschina.net/oscnet/up-09dde76bcd99f3a9712d022d37110d64f78.gif" width="720" referrerpolicy="no-referrer"></span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#c8c3bc; color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:start"><span>更多详见：《</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F121483218" target="_blank"><span>一张图理解Kafka时间轮(TimingWheel),看不懂算我输!</span></a></span><span>》 </span></p> 
<h2 style="text-align:start"><span>六、使用文档和示例</span></h2> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/example/README.md"><span>mica-mqtt 快速开始</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-client-spring-boot-starter/README.md"><span>mica-mqtt-client-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/starter/mica-mqtt-server-spring-boot-starter/README.md"><span>mica-mqtt-server-spring-boot-starter 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/mica-mqtt-core/README.md"><span>mica-mqtt 使用文档</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/docs/http-api.md"><span>mica-mqtt http api 文档详见</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/blob/master/CHANGELOG.md"><span>mica-mqtt 发行版本</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/596392912/mica-mqtt/tree/master/mica-mqtt-broker"><span>基于 redis 的 mqtt broker 集群示例</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><a href="https://gitee.com/openharmony-tpc/talkweb_mqtt"><span>基于 kafka 的 mqtt broker 集群示例</span></a></span></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            