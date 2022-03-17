
---
title: '物联网通讯协议 iot-modbus V3.2.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2713'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 05:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2713'
---

<div>   
<div class="content">
                                                                    
                                                        <h1>iot-modbus</h1> 
<h4>介绍</h4> 
<p>物联网通讯协议，基于netty框架，支持COM（串口）和TCP协议，支持服务端和客户端两种模式，实现Java控制智能设备，同时支持设备组多台设备高并发通讯。采用工厂设计模式，代码采用继承和重写的方式实现高度封装，可作为SDK提供封装的接口，让具体的业务开发人员无需关心通讯协议的底层实现，直接调用接口即可使用。实现了心跳、背光灯、扫码、刷卡、指静脉、温湿度和门锁（支持多锁）、LCD显示屏等指令控制、三色报警灯控制。代码注释丰富，包括上传和下发指令调用例子，非常容易上手。</p> 
<h4>版本说明</h4> 
<ol> 
 <li>V1.0.0版本仅支持TCP服务端通讯模式；</li> 
 <li>V2.0.0版本支持TCP服务端和客户端两种模式，客户端模式还增加了心跳重连机制。</li> 
 <li>V3.0.0版本支持COM（串口）和TCP协议，增加logback日志按文件大小和时间切割输出。</li> 
 <li>V3.1.0版本代码优化，抽取公共模块子工程。</li> 
 <li>V3.2.0版本TCP通讯增加支持LCD显示屏控制指令，支持批量控制LCD显示屏。</li> 
 <li>V3.2.1版本串口通讯增加支持LCD显示屏控制指令，支持批量控制LCD显示屏。</li> 
 <li>V3.2.2版本串口通讯接收指令数据拆包处理代码优化，网口通讯增加支持三色报警灯控制指令。</li> 
 <li>V3.2.3版本串口通讯增加支持三色报警灯控制指令，串口通讯接收指令数据拆包处理代码优化。</li> 
 <li>V3.2.4版本使用netty集成Rxtx对串口数据进行数据拆包处理，并且对指静脉指令进行优化。</li> 
</ol> 
<h4>软件架构</h4> 
<p>软件架构说明 基础架构采用Spring Boot2.x + Netty4.X + Maven3.6.x，日志采用logback。</p> 
<h4>安装教程</h4> 
<ol> 
 <li>系统Windows7以上；</li> 
 <li>安装Jdk1.8以上；</li> 
 <li>安装Maven3.6以上；</li> 
 <li>代码以Maven工程导入Eclipse或Idea。</li> 
</ol> 
<h4>使用说明</h4> 
<ol> 
 <li>工程结构说明：</li> 
</ol> 
<ul> 
 <li>iot-modbus                //物联网通讯父工程</li> 
 <li>├── doc                   //文档管理</li> 
 <li>├── iot-modbus-client     //netty通讯客户端</li> 
 <li>├── iot-modbus-common     //公共模块子工程</li> 
 <li>├── iot-modbus-netty      //netty通讯子工程</li> 
 <li>├── iot-modbus-serialport //串口通讯子工程</li> 
 <li>├── iot-modbus-server     //netty通讯服务端</li> 
 <li>├── iot-modbus-test       //使用样例子工程</li> 
 <li>└── tools                 //通讯指令调试工具</li> 
</ul> 
<ol start="2"> 
 <li>配置文件查看iot-modbus-test子工程resources目录下的application.yml文件；</li> 
 <li>启动文件查看iot-modbus-test子工程App.java文件；</li> 
 <li>服务启动后，服务端端口默认为：8080，网口通讯端口默认为：4000，串口通讯默认串口为：COM1；</li> 
 <li>通讯指令调试工具，TCP通讯模式使用tools目录下的NetAssist.exe，串口通讯模式使用tools目录下的UartAssist.exe；</li> 
 <li>通讯指令采用Hex编码（十六进制）；</li> 
 <li>串口通讯依赖文件查看doc/serialport目录，Windows环境下rxtxParallel.dll和rxtxSerial.dll文件拷贝到JDK安装的bin目录下，Linux环境将librxtxParallel.so和librxtxSerial.so文件拷贝到JDK安装的bin目录下；</li> 
 <li>postman指令下发样例请查看doc/postman/通讯指令下发.postman_collection.json文件，包括门锁（单锁/多锁）、扫码、背光灯、LCD显示屏、三色报警灯指令。</li> 
</ol> 
<h4>指令格式</h4> 
<ol> 
 <li>以心跳指令（7E 04 00 BE 01 00 00 74 77 7F）作为样例说明，下标从0开始；</li> 
 <li>第0位为起始符，长度固定占1个字节，固定格式：7E；</li> 
 <li>第1、2位为数据长度，计算方法是从命令符到数据位（即：从3位到指令长度-3位），长度固定占2个字节，例如：04 00，表示长度为4；</li> 
 <li>第3位为指令符，长度固定占1个字节，例如：BE，表示心跳指令；</li> 
 <li>第4位为设备号，长度固定占1个字节，例如：01，表示设备号为1；</li> 
 <li>第5位为层地址，长度固定占1个字节，例如：00，表示设备所有的层不执行；</li> 
 <li>第6位为槽地址，长度固定占1个字节，例如：00，表示设备所有的槽不执行；</li> 
 <li>指令长度-3位到-2位为校验位，采用CRC16_MODBUS（长度,命令,地址,数据）校验，例如：74 77，详细查看：ModbusCrc16Utils.java工具类；</li> 
 <li>末位为结束符，长度固定占1个字节，固定格式：7F。</li> 
</ol> 
<h4>通讯指令</h4> 
<ol> 
 <li>心跳上传指令</li> 
</ol> 
<ul> 
 <li>iot-modbus作为服务端，通过心跳来维持通讯，启动服务端后，打开NetAssist.exe指令调试工具，先往服务端发送心跳指令；</li> 
 <li>硬件往服务端发送：7E 04 00 BE 01 00 00 74 77 7F ，为必要指令。</li> 
</ul> 
<ol start="2"> 
 <li>背光灯上传指令</li> 
</ol> 
<ul> 
 <li>硬件往服务端发送：7E 05 00 88 01 00 00 00 AF E3 7F</li> 
</ul> 
<ol start="3"> 
 <li>扫码指令下发</li> 
</ol> 
<ul> 
 <li>服务端往硬件下发：7E 05 00 08 01 00 00 01 6F FD 7F</li> 
 <li>第7位为数据位，长度固定占1个字节，例如：01，表示开开启扫码头。</li> 
</ul> 
<ol start="4"> 
 <li>扫码指令上传</li> 
</ol> 
<ul> 
 <li>硬件往服务端发送：7E 24 00 8F 01 00 00 03 45 30 30 34 30 31 30 38 32 38 30 32 41 36 39 33 0D 02 00 00 01 02 13 73 02 00 00 01 02 13 73 9B 79 7F</li> 
 <li>数据位：03 45 30 30 34 30 31 30 38 32 38 30 32 41 36 39 33 0D 02 00 00 01 02 13 73 02 00 00 01 02 13 73为条码信息。</li> 
</ul> 
<ol start="5"> 
 <li>刷卡指令上传</li> 
</ol> 
<ul> 
 <li>硬件往服务端发送：7E 08 00 84 01 00 00 86 14 AE 02 7C 53 7F</li> 
 <li>数据位：86 14 AE 02为卡号信息。</li> 
</ul> 
<ol start="6"> 
 <li>单开锁下发指令</li> 
</ol> 
<ul> 
 <li>服务端往硬件下发：7E 05 00 03 01 00 00 01 CA 3C 7F</li> 
 <li>第7位为数据位，长度固定占1个字节，例如：01，表示开1号锁。</li> 
</ul> 
<ol start="7"> 
 <li>多开锁下发指令</li> 
</ol> 
<ul> 
 <li>服务端往硬件下发：7E 08 00 03 FF FF FF 01 00 02 01 7F B0 7F</li> 
 <li>FF FF FF为指令做兼容填补位，后面 01 00 02 01是数据位，其中：01表示1号锁，00表示上锁；02表示2号锁，01表示开锁。</li> 
</ul> 
<ol start="8"> 
 <li>锁状态上传指令</li> 
</ol> 
<ul> 
 <li>硬件往服务端发送：7E 0D 00 83 01 00 00 FF FF FF 01 00 05 02 00 01 EE 99 7F</li> 
 <li>FF FF FF为指令做兼容填补位，后面 01 00 05 02 00 01是数据位，其中：01表示1号锁，00表示上锁，05表示传感器状态码；02表示2号锁，00表示上锁，01表示传感器状态码。</li> 
</ul> 
<ol start="9"> 
 <li>指静脉和温湿度指令（不作说明，详细查看代码）；</li> 
 <li>LCD显示屏批量控制下发指令（不作说明，详细查看代码）；</li> 
 <li>三色报警灯控制下发指令（不作说明，详细查看代码）。</li> 
</ol>
                                        </div>
                                      
</div>
            