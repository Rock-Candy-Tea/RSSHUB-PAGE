
---
title: '智能电表 DDSU666 接入 HomeAssistant 详细安装教程'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/12/08/article/af196c29f9f7dd5bdeb5b33e895bab48?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Wed, 08 Dec 2021 04:04:21 GMT
thumbnail: 'https://cdn.sspai.com/2021/12/08/article/af196c29f9f7dd5bdeb5b33e895bab48?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-1eaafa2a><div class="content wangEditor-txt minHeight" data-v-1eaafa2a><p> </p><p>DDSU666电表RS485 + ESP32 + ESPHome + HomeAssistant</p><p style="margin-left:0px;">本方案是使用 正泰 DDSU666 带 RS485 通讯的电表，添加一个 ESPHome 模块连接到 HomeAssistant 智能家居系统，在线查看电压、电流、功率等数据。</p><p style="margin-left:0px;">最终选择此方案原因：</p><ul><li>导轨式安装方便小巧</li><li>数据在本地随便自己折腾</li><li>精度有足够保障及安全性</li></ul><p style="margin-left:0px;">考虑过的方案：</p><p style="margin-left:0px;">立新 DDS238-2 这款有可以直接使用渡鸦APP控制，不过数据是直接到他们的服务器，再通过 APP 查看，同步到 HA 比较麻烦。优势是可以远程拉闸，不过这个对于我使用价值不大。价格 140元左右相对较贵。</p><p style="margin-left:0px;">安培那种 DIY 的也有，不过那种精度和安全性就没法和品牌的比了。</p><p style="margin-left:0px;">数据加入 HA 都需要一个 485 转换模块，才能将电表数据传输给 HA 设备，通过 Wi-Fi 或 网线 或 其他，我选择了最简单的 Wi-Fi 无线也方便。</p><p style="margin-left:0px;">所以这一套系统的基本结构就是：</p><p style="margin-left:0px;"><code>电表 + 485转换模块 + 模块电源</code></p><p style="margin-left:0px;">485 模块都不便宜，还要供电电源也不小，网上找了很多方案都不太满意。</p><p style="margin-left:0px;">最后是看到这个大佬 <a href="https://github.com/liwei19920307/ESP485"><u>https://github.com/liwei19920307/ESP485</u></a> 的教程做的，应该是最小化了，安装后简洁美观。</p><p style="margin-left:0px;">我买的这个电表是 Modbus-RTU 协议，直接使用，其他协议不懂如何调试。注意正泰 DDSU666 这个电表有其他协议，购买请咨询一下客服，购买 Modbus 协议的。</p><p style="margin-left:0px;"> </p><h2 style="margin-left:0px;">准备工作</h2><h3 style="margin-left:0px;">打印 PCB 板</h3><p style="margin-left:0px;">去大佬 Github <a href="https://github.com/liwei19920307/ESP485">ESP485</a> 中找到 EDA 文件下载，解压后里面有 3个文件，找到 1-PCB_PCB_ESP485.json 这个文件需要用到。</p><p style="margin-left:0px;">1、打开 <a href="https://lceda.cn/editor">立创</a> 网站注册登陆后，选择菜单 文件 > 打开 > 立创EDA ；</p><p style="margin-left:0px;">2、选择刚刚的 1-PCB_PCB_ESP485.json 文件，打开后可以看到 PCB板了，接着选择菜单 制造 > PCB制版文件Gerber > 生成 将这个文件保存到电脑；</p><p style="margin-left:0px;">3、进入下单网址 <a href="https://www.jlc.com/">PCB下单</a> 这里是同一个账号，使用 Windows 系统安装 <code>PC小助手</code> 进去下单可以免费包邮样板 5片。下单需要的 PCB 文件就是刚刚保存的 Gerber 文件，不清楚可以在线客服咨询。</p><h3 style="margin-left:0px;">购买硬件</h3><p style="margin-left:0px;"> </p><figure class="table"><table><thead><tr><th style="background-color:rgb(241, 241, 241);border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">名称</th><th style="background-color:rgb(241, 241, 241);border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">型号</th><th style="background-color:rgb(241, 241, 241);border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">数量</th></tr></thead><tbody><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">ESP-C3-13U</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">4M</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">AMS1117-3.3 稳压电源芯片降压IC</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">AMS1117-3.3</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">MAX13487EESA SOIC-8</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">/</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">0603贴片电阻 4.7KΩ</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">/</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">0603贴片电容 50V 100NF ±10%</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">/</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">2.4G内置柔性FPC软天线</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">IPEX接头</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">220V转5V700mA电源模块</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">5V700mA</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">正泰DDSU666</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">5-80A ModBus</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">正泰模数化插座</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">AC30-103</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">尖嘴元件镊子</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">弯嘴</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">热缩管</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">直径5mm</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">40P彩排杜邦线</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">公对母</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">CH341A编程器</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">/</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">电烙铁（要有尖烙铁头）</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">/</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr><tr><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">电线（连接电表强电）</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">6平方</td><td style="border-bottom:1px solid rgb(221, 221, 221);border-left:1px solid rgb(221, 221, 221);border-right:1px solid rgb(221, 221, 221);border-top:1px solid rgb(221, 221, 221);padding:0.5em 1em;">1</td></tr></tbody></table></figure><p style="margin-left:0px;"> </p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/af196c29f9f7dd5bdeb5b33e895bab48?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="IMG_3827" data-original="https://cdn.sspai.com/2021/12/08/article/af196c29f9f7dd5bdeb5b33e895bab48" referrerpolicy="no-referrer"><figcaption>购买元器件</figcaption></figure><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/17e27594d6758cb5e1998c7957ec0847?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="IMG_3830" data-original="https://cdn.sspai.com/2021/12/08/article/17e27594d6758cb5e1998c7957ec0847" referrerpolicy="no-referrer"><figcaption>电表 和 数字插座</figcaption></figure><p style="margin-left:0px;"> </p><h2 style="margin-left:0px;">刷固件</h2><p style="margin-left:0px;">对于我这样的小白这个地方折腾了很久，从来没有刷过一头雾水。折腾了很久，最后是安装下面流程顺利完成。</p><h3 style="margin-left:0px;">ESPHome</h3><p style="margin-left:0px;">安装这个错误很多次，很多不能用各种报错。Windows10 命令安装后不能编译，后来使用 R2S（OpenWrt）中的 Docker 安装 ESPHome 还是无法编译，最后使用 macOS 系统安装 Docker 再安装 ESPHome 后终于编译成功了。</p><h4 style="margin-left:0px;">ESPHome 文件</h4><pre class="language-python"><code>esphome:
  name: esp32_c3
  platform: ESP32
  board: esp32-c3-devkitm-1
  platformio_options:
    platform: https://github.com/platformio/platform-espressif32.git#feature/arduino-upstream
    platform_packages:
      - framework-arduinoespressif32@https://github.com/espressif/arduino-esp32.git#2.0.0
    board_build.variant: esp32c3
    board_build.f_cpu: 160000000L
    board_build.f_flash: 40000000L
    upload_protocol: esptool
    board_build.flash_mode: dio

wifi:
  ssid: "#你的WIFI名称#"
  password: "#你的WIFI密码#"

captive_portal:

logger:

api:
  password: '#api密码，简单好记就行#'

ota:
  password: '#ota密码，可以跟上面一样#'

web_server:
  port: 80
  
time:
  - platform: sntp
    id: esp485_time
  
uart:
  id: esp485_uart
  rx_pin: 18
  tx_pin: 19
  baud_rate: 9600
  data_bits: 8
  stop_bits: 1

modbus:
  id: esp485_modbus
  send_wait_time: 200ms

modbus_controller:
  - id: esp485_modbus_controller
    modbus_id: esp485_modbus
    address: 0x01 #设备地址码（一般是1根据实际情况填）#
    command_throttle: 200ms
    setup_priority: -10
    update_interval: 10s

sensor:
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_u
    name: "U"
    address: 0x2000
    register_count: 2
    unit_of_measurement: "V"
    register_type: holding
    value_type: FP32
    accuracy_decimals: 1
    device_class: voltage
    
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_i
    name: "I"
    address: 0x2002
    register_count: 2
    unit_of_measurement: "A"
    register_type: holding
    value_type: FP32
    accuracy_decimals: 3
    device_class: current
    
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_p
    name: "P"
    address: 0x2004
    register_count: 2
    unit_of_measurement: "W"
    register_type: holding
    value_type: FP32
    accuracy_decimals: 1
    filters:
      - multiply: 1000
    device_class: power
    
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_q
    name: "Q"
    address: 0x2006
    register_count: 2
    unit_of_measurement: "var"
    register_type: holding
    value_type: FP32
    accuracy_decimals: 1
    filters:
      - multiply: 1000
    device_class: power
    
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_s
    name: "S"
    address: 0x2008
    register_count: 2
    unit_of_measurement: "VA"
    register_type: holding
    value_type: FP32
    accuracy_decimals: 1
    filters:
      - multiply: 1000
    device_class: power
    
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_pf
    name: "PF"
    address: 0x200A
    register_count: 2
    register_type: holding
    value_type: FP32
    accuracy_decimals: 3
    device_class: power_factor
    
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_freq
    name: "Freq"
    address: 0x200E
    register_count: 2
    unit_of_measurement: "Hz"
    register_type: holding
    value_type: FP32
    accuracy_decimals: 2
    
  - platform: modbus_controller
    modbus_controller_id: esp485_modbus_controller
    id: esp485_modbus_ep
    name: "Ep"
    address: 0x4000
    register_count: 2
    unit_of_measurement: "kWh"
    register_type: holding
    value_type: FP32
    accuracy_decimals: 2
    device_class: energy
    state_class: total_increasing

</code></pre><p style="margin-left:0px;"> </p><h4 style="margin-left:0px;">安装 Docker</h4><p style="margin-left:0px;">使用 macOS 安装 <a href="https://www.runoob.com/docker/macos-docker-install.html">Docker</a> （点击进入有其他系统安装方法）</p><pre class="language-python"><code>$ brew install --cask --appdir=/Applications docker</code></pre><p style="margin-left:0px;"> </p><h4 style="margin-left:0px;">安装 ESPHome 及 编译固件</h4><p style="margin-left:0px;">使用刚刚安装好的 Docker 安装 ESPHome 容器</p><p style="margin-left:0px;">下载镜像文件</p><pre class="language-python"><code>docker pull esphome/esphome:latest</code></pre><p style="margin-left:0px;"> </p><p style="margin-left:0px;">运行，端口 6052，打开网页</p><pre class="language-python"><code>docker run -d -p 6052:6052 esphome/esphome

# 打开网页
http://localhost:6052/</code></pre><p style="margin-left:0px;"> </p><p style="margin-left:0px;">添加设备</p><p style="margin-left:0px;">根据提示输入名称、Wi-Fi、芯片类型 创建完成</p><p style="margin-left:0px;">创建后点击卡片 EDIT 编辑，删除其中代码，将上面的 ESPHome 代码复制进去，记得修改其中的Wi-Fi及密码信息，点击保存。</p><p style="margin-left:0px;">继续操作点击 Insta > Manual download</p><p style="margin-left:0px;">编译成功会输出 <code>INFO Successfully compiled program.</code> 并自动下载 bin 文件。</p><p style="margin-left:0px;">将下载文件 <code>esp32_c3.bin</code> 改名成 <code>firmware.bin</code> 等会刷机会用到</p><p style="margin-left:0px;"> </p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/0514b48536a01517fe34938ca23bcf7f?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="截屏2021-11-14 12.46.02" data-original="https://cdn.sspai.com/2021/12/08/article/0514b48536a01517fe34938ca23bcf7f" referrerpolicy="no-referrer"><figcaption>固件编译中</figcaption></figure><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/21e3fea52a51abbc9ce68e20a00cb751?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="截屏2021-11-14 12.47.21" data-original="https://cdn.sspai.com/2021/12/08/article/21e3fea52a51abbc9ce68e20a00cb751" referrerpolicy="no-referrer"><figcaption>成功后自动下载</figcaption></figure><p style="margin-left:0px;"> </p><h3 style="margin-left:0px;">esptool.py 安装</h3><p style="margin-left:0px;"> </p><h4 style="margin-left:0px;">Python3 安装</h4><p style="margin-left:0px;">使用 Windows10 到 <a href="https://www.python.org/">Python</a> 官方网站下一个 <code>Python3</code> 版本文件直接安装，安装时需要勾选 <code>PATH</code> 。（eg：安装的 Python 3.8.7(64-bit) 版本，勾选 Add Python 3.8 to PATH）</p><pre class="language-python"><code># 命令窗口输入 py 查看是否安装成功

C:\Users\Carl>py
Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

# 输入 exit() 退出</code></pre><p style="margin-left:0px;"> </p><h4 style="margin-left:0px;">CH34X 驱动安装</h4><p style="margin-left:0px;">使用 Windows10 系统安装，首先安装刷机设备需要的驱动，购买 <code>CH341</code> 时找卖家要一个驱动文件，安装就可以了。可以在 <code>开始 > 右键 > 设备管理器 > 端口COM</code> 中看到设备及端口号，记住这个端口，比如：COM3。</p><p style="margin-left:0px;"><a href="http://www.wch.cn/download/CH341SER_EXE.html">CH341SER.EXE 及其他版本驱动下载</a></p><p style="margin-left:0px;">根据自己使用的刷机设备安装对应驱动即可。</p><h4 style="margin-left:0px;">安装 esptool.py</h4><p style="margin-left:0px;">Windows10 打开CMD命令窗口，输入：</p><pre class="language-python"><code>pip install esptool
  
.... 等待安装完成
  
# 最后输出下面代码成功

Installing collected packages: esptool
Running setup.py install for esptool ... done
Successfully installed esptool-3.2</code></pre><p style="margin-left:0px;"> </p><p style="margin-left:0px;">可以在刷写固件前先执行擦除固件</p><pre class="language-python"><code>esptool.py --port COM4(你的端口) erase_flash</code></pre><p style="margin-left:0px;"> </p><h3 style="margin-left:0px;">刷写固件</h3><p style="margin-left:0px;"> </p><h4 style="margin-left:0px;">芯片接线</h4><p style="margin-left:0px;">刷机设备对应接芯片 <code>3.3V</code> 和 <code>GND</code></p><p style="margin-left:0px;">刷机设备 <code>TX</code> 接芯片 <code>RXD</code>，刷机设备 <code>RX</code> 接芯片 <code>TXD</code></p><p style="margin-left:0px;">芯片 <code>IO9</code> 接一根线备用，在刷机时需要接刷机设备 <code>GND</code></p><p style="margin-left:0px;">接线参考图片</p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/b37c2aa0a2002ef5f8098e7f2991d5a7?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="IMG_3877" data-original="https://cdn.sspai.com/2021/12/08/article/b37c2aa0a2002ef5f8098e7f2991d5a7" referrerpolicy="no-referrer"><figcaption>注意接线不要短路</figcaption></figure><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/12/08/9a6a7c7d149411b5310bee6c55bd9b4c.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/12/08/9a6a7c7d149411b5310bee6c55bd9b4c.jpeg" referrerpolicy="no-referrer"><figcaption>刷机设备接线</figcaption></figure><p style="margin-left:0px;"> </p><h3 style="margin-left:0px;">写入固件</h3><p style="margin-left:0px;">Windows10 桌面新建文件夹 esp32 ，去 Github <a href="https://github.com/liwei19920307/ESP485">ESP485</a> 下载 firmware 文件夹中 3个固件，并将文件放到刚刚创建好的esp32文件夹中，还有刚刚编译成功的改名固件 firmware.bin 也放在这个文件夹，共有以下 4个固件。</p><p style="margin-left:0px;"><code>boot_app0.bin / bootloader_dout_40m.bin / partitions.bin / firmware.bin</code></p><p style="margin-left:0px;">其他系统刷机根据自己情况选择。</p><p style="margin-left:0px;"> </p><p style="margin-left:0px;">刷写固件前，将 IO09 接到刷机设备 GND ，再插入电脑 USB。</p><pre class="language-python"><code># esptool.py 命令应该是全局命令
# 进入固件所在目录

cd /xxx/xxx/

# 命令窗口粘贴以下命令回车运行

esptool.py --chip esp32c3 --port COM3(改成你的端口) --baud 460800 --before default_reset --after hard_reset write_flash -z --flash_mode dout --flash_freq 40m --flash_size detect 0x0000 bootloader_dout_40m.bin 0x8000 partitions.bin 0xe000 boot_app0.bin 0x10000 firmware.bin</code></pre><p style="margin-left:0px;"> </p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/e2d60711dd66d2e6b9d03d28598da0bf?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="Screenshot 2021-11-13 102322" data-original="https://cdn.sspai.com/2021/12/08/article/e2d60711dd66d2e6b9d03d28598da0bf" referrerpolicy="no-referrer"><figcaption>固件写入成功</figcaption></figure><p style="margin-left:0px;"> </p><h4 style="margin-left:0px;">查看是否成功</h4><p style="margin-left:0px;">固件刷写完成后，从电脑拔下刷写设备，将刚刚接地的 <code>IO9</code> 线断开接地，再次插入电脑 USB 通电，等待一会。</p><p style="margin-left:0px;">登陆你的路由器（刚刚填写Wi-Fi密码的路由器），查找到新连网设备 esp32 ，找到设备 IP 地址复制。</p><p style="margin-left:0px;">在浏览器中打开此 IP 地址，如果成功加载下面页面并显示正常，就是说明刷写固件成功了，接下来焊接芯片连接电表。</p><p style="margin-left:0px;"> </p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/8ea9c9c6339bc3bb6ad143257be912c1?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="截屏2021-11-25 11.41.49" data-original="https://cdn.sspai.com/2021/12/08/article/8ea9c9c6339bc3bb6ad143257be912c1" referrerpolicy="no-referrer"><figcaption>浏览器打开页面表示写入成功</figcaption></figure><ul><li>数据是没有的，接电表后才有数据</li><li>下次可以直接在线升级固件，不用刷机了，点击“选择文件”上传更新就好了。</li></ul><p style="margin-left:0px;"> </p><h2 style="margin-left:0px;">焊接芯片和安装</h2><h3 style="margin-left:0px;">焊接芯片和元器件</h3><p style="margin-left:0px;">焊接芯片时注意不要有虚焊，PCB板质量一般容易掉焊盘，把握好温度。</p><h3 style="margin-left:0px;">连接电源模块和芯片板</h3><p style="margin-left:0px;">电源模块可以用绝缘胶包起来防止短路</p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/8dd706a371dec7c1341edbcb2ceea164?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="截屏2021-11-25 11.51.29" data-original="https://cdn.sspai.com/2021/12/08/article/8dd706a371dec7c1341edbcb2ceea164" referrerpolicy="no-referrer"><figcaption>焊接元器件 小心操作</figcaption></figure><p style="margin-left:0px;"> </p><h3 style="margin-left:0px;">改造数字插座</h3><p style="margin-left:0px;">数字插座铜片用的热缩管包起来绝缘作用，电源 L N 线是焊接在铜片上，需要用刀片对塑料外壳做小加工以更好的盖合外壳。芯片下面用了双面胶粘在外壳上，其实不沾也可以，只要做好了绝缘工作。</p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/f55477d60e7e9904a06c4b10a35cf3db?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="IMG_3883" data-original="https://cdn.sspai.com/2021/12/08/article/f55477d60e7e9904a06c4b10a35cf3db" referrerpolicy="no-referrer"><figcaption>485模块 + 电源模块</figcaption></figure><p style="margin-left:0px;"> </p><h3 style="margin-left:0px;">连接模块和电表</h3><p style="margin-left:0px;">esp32 模块 rs485 通讯线 A（黄），B（橙）依次接正泰电表 24 和 25 端口。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/12/08/b91597cca920e2d58e75f8e60bd6f265.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/12/08/b91597cca920e2d58e75f8e60bd6f265.jpeg" referrerpolicy="no-referrer"><figcaption>485模块连接电表通讯</figcaption></figure><h3 style="margin-left:0px;">测试功能</h3><p style="margin-left:0px;">先用家中插座接电源测试功能完整性，如果能够获取电表数据并正常显示说明刷写固件成功了，并且焊接没有问题。</p><p style="margin-left:0px;"> </p><h2 style="margin-left:0px;">装入电箱</h2><p style="margin-left:0px;">⚠️ <strong>强电危险操作，请勿模仿</strong></p><p style="margin-left:0px;">经过测试没有问题后，断开家中总闸开关，一定要确认家中强电接线情况，并且用测电笔经过检测电压情况，准备工作做好后，按照下面指示图接线，一定不能接错。</p><p style="margin-left:0px;"> </p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/e0a530e573b92241cdd753d26b297d1a?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="963D368F768A54D3DDA3160C848350F3" data-original="https://cdn.sspai.com/2021/12/08/article/e0a530e573b92241cdd753d26b297d1a" referrerpolicy="no-referrer"></figure><p style="margin-left:0px;"> </p><p style="margin-left:0px;">产品说明书接线方法（我购买的上图升级款，就是下图中 5(80)A 款）</p><figure class="image ss-img-wrapper image_resized" style="width:574px;"><img src="https://cdn.sspai.com/2021/12/08/article/5cf8a77facfd20c9553af336c5056231?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="IMG_3943" data-original="https://cdn.sspai.com/2021/12/08/article/5cf8a77facfd20c9553af336c5056231" referrerpolicy="no-referrer"></figure><p style="margin-left:0px;">我是按照上图中接线</p><p style="margin-left:0px;"> </p><p style="margin-left:0px;">自己购买的 6平方电线，接入户空气开关输出端，再接到电表输入端（下面），电表输出端（上面）再接到空开旁边的欠压保护器的输入端（下面）。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/12/08/bff1a957a393d1b9bfceeae1a477f36a.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/12/08/bff1a957a393d1b9bfceeae1a477f36a.jpeg" referrerpolicy="no-referrer"><figcaption>强电接线有危险，断开总开</figcaption></figure><p style="margin-left:0px;">数字插座 零N 火L 线接到上面电表旁的空气漏保开关输出端。</p><p style="margin-left:0px;">esp32 模块 rs485 通讯线 A B 依次接电表 24 25 端口。</p><p style="margin-left:0px;">数字插座引出黑色天线，尽量不要遮挡以防信号不好。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/12/08/2d28c59e9f7dd67e8be4a4c41d26dc89.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/12/08/2d28c59e9f7dd67e8be4a4c41d26dc89.jpeg" referrerpolicy="no-referrer"><figcaption>检查是否工作正常</figcaption></figure><p style="margin-left:0px;">通电后可以看到智能电表已经在工作了，按 蓝色箭头 按钮可以依次切换显示的各种数据信息，说明书有详细说明。这款电表带背光，一段时间后自动熄灭。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/12/08/f544d406c2543cc037dd0bfffcd45ad3.jpeg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/12/08/f544d406c2543cc037dd0bfffcd45ad3.jpeg" referrerpolicy="no-referrer"><figcaption>整体美观整洁也安全</figcaption></figure><p style="margin-left:0px;">看起来简洁美观，也有安全保障。</p><p style="margin-left:0px;"> </p><h2 style="margin-left:0px;">配置 HomeAssistant</h2><p style="margin-left:0px;">完成这些操作后，打开 HomeAssistant 后台，进入配置应该就能看到新的 esp32-c3 设备，直接添加就行了，可以在能源中设置相关信息。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/12/08/644cf3b7c90d55aeac61e384b8feb0d2.PNG?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/12/08/644cf3b7c90d55aeac61e384b8feb0d2.PNG" referrerpolicy="no-referrer"><figcaption>电表数据</figcaption></figure><p style="margin-left:0px;">可以在 配置 - 能源 中设置一个电费价格，我设置的固定价格，不会弄阶梯价格。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/12/08/d613af4898886cd2df7bfc75b68215ce.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/12/08/d613af4898886cd2df7bfc75b68215ce.png" referrerpolicy="no-referrer"><figcaption>设置电价</figcaption></figure><h2 style="margin-left:0px;">下载文件</h2><p style="margin-left:0px;">CH34x_Install_V1.5.pkg（macOS 10.15 安装无效）</p><p style="margin-left:0px;">DDSU666 电表说明书.pdf</p><p style="margin-left:0px;">esp-c3-13u 规格书.pdf</p><p style="margin-left:0px;">ESP32-C3 资料</p><p style="margin-left:0px;">GitHub库文件：ESP485-main</p><p style="margin-left:0px;"><a href="https://www.aliyundrive.com/s/B9MzKMJKUuG">阿里云盘下载：https://www.aliyundrive.com/s/B9MzKMJKUuG</a></p></div><!----></div><div style="border:1px solid transparent;" data-v-1eaafa2a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-1eaafa2a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>2</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-7757" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E6%99%BA%E8%83%BD%E7%94%B5%E8%A1%A8%20DDSU666%20%E6%8E%A5%E5%85%A5%20HomeAssistant%20%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B%E3%80%91layout%3Aposttitle%3A%22%E6%99%BA%E8%83%BD%E7%94%B5%E8%A1%A8DDSU666%E9%85%8DESP32%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B%22subtitle%3A%22DDSU666%E7%94%B5%E8%A1%A8RS485%2BESP%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F12%2F08%2F546059eaa516fa19c8975d7f296b2496.jpeg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-6625" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E6%99%BA%E8%83%BD%E7%94%B5%E8%A1%A8%20DDSU666%20%E6%8E%A5%E5%85%A5%20HomeAssistant%20%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B%E3%80%91layout%3Aposttitle%3A%22%E6%99%BA%E8%83%BD%E7%94%B5%E8%A1%A8DDSU666%E9%85%8DESP32%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B%22subtitle%3A%22DDSU666%E7%94%B5%E8%A1%A8RS485%2BESP%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            