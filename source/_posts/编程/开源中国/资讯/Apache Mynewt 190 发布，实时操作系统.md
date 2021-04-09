
---
title: 'Apache Mynewt 1.9.0 发布，实时操作系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4800'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4800'
---

<div>   
<div class="content">
                                                                                            <p>Apache Mynewt 提供了一套系统软件，以实现受限物联网（IoT）设备上的核心功能和服务。其核心组件是一个实时操作系统，适用于资源受限的嵌入式系统，如可穿戴设备、灯泡、门锁、门铃等。它可以在各种微控制器架构上工作，如 ARM Cortex-M 和 MIPs 架构。围绕操作系统构建的是中间件和实用程序，如闪存文件系统和丰富的、抽象的跨硬件和程序任务的仪器，以实现一致的管理和监控。此外，还提供了网络协议软件，从兼容蓝牙 4.2（BLE 4.2）的协议栈开始。</p> 
<p>项目的第二个方面是一个统一的工具框架，让开发人员可以轻松地编译和移植软件到他们的设备上，并实现远程管理的系统服务。</p> 
<p>项目的最后一块是一个远程管理工具，用于远程查询、收集统计数据、配置、升级和管理设备。</p> 
<p>Apache Mynewt 1.9.0 正式发布，其更新内容如下：</p> 
<ul> 
 <li> <p>USB 外设支持</p> <p>通过集成 tinyusb 库，现在可以将 Mynewt 设备作为 USB 外设运行。当前支持的平台包括 STM32F1 系列、STM32F4 系列、STM32L4 系列；</p> </li> 
 <li> <p>Inter-<strong>IC Sound（I2S）支持</strong></p> <p>Inter-IC Sound 是用于发送数字音频数据的接口。当前支持的平台包括 STM32F1 系列和 nRF52；</p> </li> 
 <li> <p>通用温度传感器接口 新的温度读取界面；</p> </li> 
 <li> <p>支持 Dialog CMAC CMAC 是一个独立的 hw 块，其 Cortex-M0+ 内核和无线电外设集成在 DA1469x 中，能够运行 BLE 等协议；</p> </li> 
 <li> <p>支持 Nordic nRF9160 该版本增加了对运行 Nordic nRF9160 MCU 的支持。目前支持的有 UART、SPI 和 I2C；</p> </li> 
 <li> <p>支持 Nordic nRF5340 该版本增加了对 Nordic nRF5340 MCU 的支持。同时支持应用核和网络核，包括核之间的 IPC；目前支持的有 UART、SPI、ADC、I2C 和 GPIO 传递；</p> </li> 
 <li> <p>支持开放监督设备协议（OSDP）库；</p> </li> 
 <li> <p>支持 LittleFS 文件系统 LittleFS 被集成，可以通过标准的 FS 子系统使用，也可以将其作为 sys/config 的后端使用；</p> </li> 
 <li> <p>mbedTLS 更新至 2.16.10；</p> </li> 
 <li> <p>nrfx 更新至 2.3.0；</p> </li> 
 <li> <p>LWIP 更新到 2.1.2；</p> </li> 
 <li> <p>恩智浦 SDK 已更新至 2.9.0；</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcwiki.apache.org%2Fconfluence%2Fdisplay%2FMYNEWT%2FRN-1.9.0" target="_blank">https://cwiki.apache.org/confluence/display/MYNEWT/RN-1.9.0</a></p>
                                        </div>
                                      
</div>
            