
---
title: '物联网通讯协议 iot-modbus V3.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4999'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 09:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4999'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">物联网通讯协议，基于netty框架，支持COM（串口）和TCP协议，支持服务端和客户端两种模式，实现Java控制智能设备，同时支持设备组多台设备高并发通讯。采用工厂设计模式，代码采用继承和重写的方式实现高度封装，可作为SDK提供封装的接口，让具体的业务开发人员无需关心通讯协议的底层实现，直接调用接口即可使用。实现了心跳、背光灯、扫码、刷卡、指静脉、温湿度和门锁（支持多锁）等指令控制。代码注释丰富，包括上传和下发指令调用例子，非常容易上手。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">版本说明</h4> 
<ol> 
 <li>V1.0.0版本仅支持TCP服务端通讯模式；</li> 
 <li>V2.0.0版本支持TCP服务端和客户端两种模式，客户端模式还增加了心跳重连机制。</li> 
 <li>V3.0.0版本支持COM（串口）和TCP协议，增加logback日志按文件大小和时间切割输出。</li> 
 <li>V3.1.0版本代码优化，抽取公共模块子工程。</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">工程机构</h4> 
<ul> 
 <li>iot-modbus //物联网通讯父工程</li> 
 <li>├── doc //文档管理</li> 
 <li>├── iot-modbus-client //netty通讯客户端</li> 
 <li>├── iot-modbus-common //公共模块子工程</li> 
 <li>├── iot-modbus-netty //netty通讯子工程</li> 
 <li>├── iot-modbus-serialport //串口通讯子工程</li> 
 <li>├── iot-modbus-server //netty通讯服务端</li> 
 <li>├── iot-modbus-test //使用样例子工程</li> 
 <li>└── tools //通讯指令调试工具</li> 
</ul>
                                        </div>
                                      
</div>
            