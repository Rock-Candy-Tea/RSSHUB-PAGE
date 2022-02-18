
---
title: '物联网通讯协议 iot-modbus V3.2.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7903'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 12:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7903'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:left">iot-modbus</h1> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">物联网通讯协议，基于netty框架，支持COM（串口）和TCP协议，支持服务端和客户端两种模式，实现Java控制智能设备，同时支持设备组多台设备高并发通讯。采用工厂设计模式，代码采用继承和重写的方式实现高度封装，可作为SDK提供封装的接口，让具体的业务开发人员无需关心通讯协议的底层实现，直接调用接口即可使用。实现了心跳、背光灯、扫码、刷卡、指静脉、温湿度和门锁（支持多锁）、LCD显示屏等指令控制。代码注释丰富，包括上传和下发指令调用例子，非常容易上手。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">版本说明</h4> 
<ol> 
 <li>V1.0.0版本仅支持TCP服务端通讯模式；</li> 
 <li>V2.0.0版本支持TCP服务端和客户端两种模式，客户端模式还增加了心跳重连机制。</li> 
 <li>V3.0.0版本支持COM（串口）和TCP协议，增加logback日志按文件大小和时间切割输出。</li> 
 <li>V3.1.0版本代码优化，抽取公共模块子工程。</li> 
 <li>V3.2.0版本支持LCD显示屏控制指令，支持批量控制LCD显示屏。</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">软件架构</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">软件架构说明 基础架构采用Spring Boot2.x + Netty4.X + Maven3.6.x，日志采用logback。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">安装教程</h4> 
<ol> 
 <li>系统Windows7以上；</li> 
 <li>安装Jdk1.8以上；</li> 
 <li>安装Maven3.6以上；</li> 
 <li>代码以Maven工程导入Eclipse或Idea。</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">使用说明</h4> 
<ol> 
 <li>工程结构说明：</li> 
</ol> 
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
<ol start="2"> 
 <li>配置文件查看iot-modbus-test子工程resources目录下的application.yml文件；</li> 
 <li>启动文件查看iot-modbus-test子工程App.java文件；</li> 
 <li>服务启动后，服务端端口默认为：8080，网口通讯端口默认为：4000，串口通讯默认串口为：COM1；</li> 
 <li>通讯指令调试工具，TCP通讯模式使用tools目录下的NetAssist.exe，串口通讯模式使用tools目录下的UartAssist.exe；</li> 
 <li>通讯指令采用Hex编码（十六进制）；</li> 
 <li>串口通讯依赖文件查看doc/serialport目录，Windows环境下rxtxParallel.dll和rxtxSerial.dll文件拷贝到JDK安装的bin目录下，Linux环境将librxtxParallel.so和librxtxSerial.so文件拷贝到JDK安装的bin目录下；</li> 
 <li>postman指令下发样例请查看doc/postman/通讯指令下发.postman_collection.json文件，包括门锁（单锁/多锁）、扫码、背光灯、LCD显示屏灯指令。</li> 
</ol>
                                        </div>
                                      
</div>
            