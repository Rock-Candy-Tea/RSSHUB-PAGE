
---
title: 'smart-mqtt v0.1 首发，国产开源 MQTT Broker 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d49d180b5e95b7a421eaf86111767610fe9.png'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 10:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d49d180b5e95b7a421eaf86111767610fe9.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="margin-left:0; margin-right:0"><span style="color:#333333">smart-mqtt 是用 java 语言开发的 MQTT Broker 服务，也是 smartboot 组织下首款真正意义上面向物联网的解决方案。旨在帮助企业以较低的成本快速搭建稳定、可靠的物联网服务，助力万物互联互通。</span></p> 
 <p style="margin-left:0; margin-right:0"><img height="481" src="https://oscimg.oschina.net/oscnet/up-d49d180b5e95b7a421eaf86111767610fe9.png" width="750" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#333333">smart-mqtt 底层通信采用了异步非阻塞通信框架 smart-socket，现已实现了完整的 mqtt v3.1.1 协议编解码规范，未来还将考虑支持 mqtt v5.0 及其他物联网协议。</span></p> 
 <h2 style="margin-left:0; margin-right:0"><span>项目发展</span></h2> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>2018年，创建 smart-mqtt 项目，完成基本的协议编解码结构搭建。</span></li> 
  <li><span>2019~2021年，项目基本处于停更状态，期间重心在于提升底层通信框架 smart-socket 的性能。</span></li> 
  <li><span>2022年3月，重启 smart-mqtt。</span></li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0">更新内容</h2> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span>✅  </span><span>支持MQTT v3.1.1协议标准</span></li> 
  <li><span>✅  </span><span>支持</span><span style="color:#333333">Qos0、Qos1、Qos2 的消息传递。</span></li> 
  <li><span>✅  </span><span>支持遗嘱消息</span></li> 
  <li><span>✅  </span><span>支持 retain 消息</span></li> 
  <li><span>✅  </span><span>支持心跳消息</span></li> 
  <li><span>✅  </span><span>插件化设计模式</span></li> 
  <li><span>✅  </span><span>mqtt client 相关功能</span></li> 
  <li><span>✅  </span><span>优雅停机</span></li> 
  <li><span>✅  </span><span>Broker生命周期及各类事件监听</span></li> 
  <li><span>客户端鉴权</span></li> 
  <li><span>支持集群部署模式</span></li> 
  <li><span>支持通配符订阅模式</span></li> 
  <li><span>精准流控</span></li> 
  <li><span>待补充。。。</span></li> 
 </ul> 
 <h2 style="margin-left:0; margin-right:0"><span>功能演示</span></h2> 
 <p style="margin-left:0; margin-right:0"><strong><span>步骤一：启动 MQTT Broker</span></strong></p> 
 <p style="margin-left:0; margin-right:0"><span>我们可以通过两种方式启动MQTT Broker服务。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>第一种是下载工程源码后，运行 smart-mqtt-broker 模块下的 Boostrap 程序（如下图）。</span></p> 
 <p><img height="510" src="https://oscimg.oschina.net/oscnet/up-d8c8bf700c84280eed57ff2492314044145.png" width="750" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0"><span>第二种是通过二进制发行包启动broker服务，进入bin目录后执行 start.sh 脚本即可。软件包下载地址为：</span><a href="https://gitee.com/smartboot/smart-mqtt/releases" target="_blank"><span>https://gitee.com/smartboot/smart-mqtt/releases</span></a><span> </span></p> 
 <p><img height="193" src="https://oscimg.oschina.net/oscnet/up-9b1f699c700ef010b5292b1ffbc4f4858fc.png" width="567" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0"><strong><span>步骤二：启动 MQTT Client</span></strong></p> 
 <p style="margin-left:0; margin-right:0"><span>smart-mqtt 现已提供了比较基础的 client 能力，通过下图所示代码启动即可。当然，也可以采用任意遵循 MQTT 协议的第三方客户端连接 smart-mqtt broker。</span></p> 
 <p><img height="364" src="https://oscimg.oschina.net/oscnet/up-8f25fc904b164eeae5b72f634e8bfff4770.png" width="750" referrerpolicy="no-referrer"></p> 
 <h1 style="margin-left:0; margin-right:0"><span>参考资料</span></h1> 
 <ol style="margin-left:0; margin-right:0"> 
  <li><span style="color:#333333">《MQTT协议3.1.1中文版》</span></li> 
  <li><span>moquette</span><span> </span></li> 
 </ol> 
 <h1><span>最后</span></h1> 
 <p><span>smart-mqtt 正处于代码研发阶段，功能、文档、产品规划都还存在诸多的不完善。这个项目在我过往研发的开源作品中算不上难度最大的，但一定是复杂性最高的，这里面涵盖了通信、MQTT协议规范、消息队列、分布式架构、消息质量、数据持久化等一系列技术挑战。保守估计还需数月的研发才可使 MQTT Broker具备生产应用的成熟度，对该项目感兴趣的朋友欢迎留言交流。</span></p> 
</div>
                                        </div>
                                      
</div>
            