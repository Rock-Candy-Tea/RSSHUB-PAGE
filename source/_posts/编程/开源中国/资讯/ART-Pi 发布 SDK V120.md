
---
title: 'ART-Pi 发布 SDK V1.2.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-814c9b64d0cb78d89166086bf602ab73f27.png'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 17:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-814c9b64d0cb78d89166086bf602ab73f27.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">ART-Pi SDK v1.2.0 正式发布 ，更多 DEMO，欢迎体验</h2> 
<p style="text-align:start">ART-Pi 自去年发布以来，得到了很多小伙伴的肯定，从SDK v1.1.0 发布之后，我们先后举办了《全连接创意大赛》，《ART-Pi 扩展板创意大赛》，也收货了很多小伙伴们精彩的创意。在这段时间，我们的SDK也做了大量的更新，收录了很多精彩的展示DEMO.</p> 
<p style="text-align:start"><strong>今天正式发布 v1.2.0 版本啦，本次更新内容如下:</strong></p> 
<h3 style="text-align:start">软件篇：</h3> 
<ol> 
 <li> <p>修复 SDIO 可能存在内存泄露的问题</p> </li> 
 <li> <p>更新 pin 框架</p> </li> 
 <li> <p>支持 UART1_DMA 的配置</p> </li> 
 <li> <p>增加 PWM 的测试例程</p> </li> 
 <li> <p>修复 SAL 可能存在内存泄露的问题</p> </li> 
 <li> <p>修复 2路 SDMMC 共享资源未加锁的问题</p> </li> 
 <li> <p>完善 wifi_image 分区格式化的说明</p> </li> 
 <li> <p>修复一处扩展引脚说明的错误</p> </li> 
 <li> <p>修复 QSPI FLASH 在复位后会初始化失败的问题</p> </li> 
 <li> <p>增加出厂数据 FLASH 的固件</p> </li> 
 <li> <p>修复 drv_usart.c 中一处引脚描述错误</p> </li> 
 <li> <p>修复 drv_eth.c 中 cache 对齐的问题</p> </li> 
 <li> <p>修复 浮点数精度设置错误的问题</p> </li> 
</ol> 
<p style="text-align:start">增加示例工程 8 个：</p> 
<ol> 
 <li> <p>增加 摄像头 gc0328c_camera 工程</p> </li> 
 <li> <p>增加 接收 485 传感器的消息，发送到 MAQTT 服务器 art_pi_sensor485_app 工程 (开源手机客户端)</p> </li> 
 <li> <p>增加 NES 游戏机 art_pi_nes 工程</p> </li> 
 <li> <p>增加 支持 OTA 升级 art_pi_qboot 工程</p> </li> 
 <li> <p>增加 USB 升级 uf2_boot(裸机工程)</p> </li> 
 <li> <p>增加 语音识别蓝牙网关 art_pi_ble_mesh_gateway 工程</p> </li> 
 <li> <p>增加 利尔达 ART-Pi LoRa 开发套件 lrs007_lora_radio 工程</p> </li> 
 <li> <p>增加 利尔达 ART-Pi LoRa 开发套件 lrs007_lorawan_end_device 工程</p> </li> 
</ol> 
<p style="text-align:start"><strong>重磅推出摄像头框架</strong>：ART-Pi 抢先体验 Linux V4L2 摄像头框架(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fclub.rt-thread.org%2Fask%2Farticle%2F2721.html" target="_blank">https://club.rt-thread.org/ask/article/2721.html</a>)</p> 
<h3 style="text-align:start">硬件篇：</h3> 
<p style="text-align:start"><strong>ART-Pi LoRa 开发套件正式开售</strong></p> 
<p style="text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-814c9b64d0cb78d89166086bf602ab73f27.png" referrerpolicy="no-referrer"></p> 
<ol> 
 <li> <p>硬件兼容：支持ART-Pi、Arduino、树莓派等主流开源硬件。</p> </li> 
 <li> <p>系统稳定：搭载RT-Thread国产操作系统，在国内有成熟的平台，用户群体大，开发者生态活跃。</p> </li> 
 <li> <p>易于开发：通过成熟可靠的LoRa射频硬件，开发者可专注于应用开发。</p> </li> 
 <li> <p>云端服务：开放LoRaWAN云平台，便于接入设备，对数据进行管理维护。</p> </li> 
 <li> <p>LoRa技术：多年射频技术沉淀，可适配利尔达全系LoRa模组硬件。</p> </li> 
 <li> <p>开源平台：开源RT-Thread OS、开源LoRa / LoRaWAN 示例应用。</p> </li> 
</ol> 
<p style="text-align:start">资料下载 : <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbbs.lierda.com%2Fforum.php%3Fmod%3Dviewthread%26tid%3D11289%26extra%3Dpage%253D1" target="_blank">http://bbs.lierda.com/forum.php?mod=viewthread&tid=11289&extra=page%3D1</a></p> 
<p style="text-align:start">购买链接 : <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fspm%3Da1z0d.6639537.1997196601.4.75ac748446VAHR%26id%3D638999908986" target="_blank">https://item.taobao.com/item.htm?spm=a1z0d.6639537.1997196601.4.75ac748446VAHR&id=638999908986</a></p> 
<p style="text-align:start"><strong>《ART-Pi 扩展板创意大赛》 已经落下帷幕，目前我们收获了各种天马星空的想象力的作品：</strong></p> 
<p style="text-align:start">一等奖.</p> 
<p style="text-align:start"><strong>飞梭+RF+4G+LCD触屏智能家居控制系统</strong></p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">1.解决懒得下床去关灯，离家后忘记关电器等事件。</p> 
<p style="text-align:start">2.可以通过手机APP通信控制电器。</p> 
<p style="text-align:start">3.编码开关+RF模块无线调控+按键选择功能。 4.独立的电器有MCU+RF模块+继电器控制。</p> 
<p style="text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-f28264d55c7b76635c1f0845cb193ae60a1.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">二等奖：</p> 
<p style="text-align:start"><strong>ART-Pi 类PC多媒体扩展板</strong></p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">本项目为RT-Thread旗下开源硬件ART-Pi的扩展板。为ART-Pi扩展了VGA和USB接口。可以用来连接VGA显示器和键盘，将ART-Pi打造成一台类似“PC”的设备。或者作为简单的GUI开发平台。</p> 
<p style="text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-a9693bf5097fab9fcc20139b13cb783c2f7.JPEG" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong>目标星辰大海：无限可能的小车车</strong></p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">一台兼容 ART-Pi 开发板和 ESP32-DevkitC 开发板的小车扩展板，拥有e53标准接口再扩展触发无限可能小车车！</p> 
<p style="text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-7b2b3c63587ec481e6aef2a06bcaa3a6a76.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">三等奖：</p> 
<p style="text-align:start"><strong>FM-Radio</strong></p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">板载RDA5820FM收发一体芯片，RDA5807M FM接收芯片、PT2314高低音调节，HT6871 3W D类数字功放，2.4寸TFT显示屏（带触摸功能）</p> 
<p style="text-align:start">离线TTS语音合成+识别</p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">1.支持离线中文、英文语音合成；</p> 
<p style="text-align:start">2.语音编码、解码；</p> 
<p style="text-align:start">3.芯片内部集成 80 种常用提示音；</p> 
<p style="text-align:start">4.支持 30 个命令词的识别。</p> 
<p style="text-align:start"><strong>基于ART-Pi的热敏打印机</strong></p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">在ART-Pi主控上增加热敏打印机扩展板。在这个扩展板上集成了热敏打印机头，3个LED和3个按键。将手机连接到板子WIFI，通过手机APP可以打印汉字，二维码和图片等信息，LED和按键可以提示运行状态和交互。</p> 
<p style="text-align:start"><strong>4G通信扩展板</strong></p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">该项目基于RT-Thread的 ART-Pi 开发板为主控，使用合宙公司的Air724UG CAT.1模块为扩展通模块，可实现产品的4G连网服务。</p> 
<p style="text-align:start">信号采集及控制</p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">用于实际工业现场排放源监测设备前端预处理辅助设备的信号采样及控制。</p> 
<p style="text-align:start"><strong>ART-Pi GPIB物联网扩展板</strong></p> 
<p style="text-align:start">工程简介：</p> 
<p style="text-align:start">实验室设备主要接口还是GPIB，RS232以及新的接口LXI，接入物联网相对来说需要很多工作。本物联网扩展板使用MQTT接入阿里云等平台，可以远程控制仪器仪表，定时获取数据，云平台数据处理等。</p> 
<p style="text-align:start">更多优秀作品可前往工程合集查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foshwhub.com%2Frecommend%2Fart_pi_tuo_zhan_ban" target="_blank">https://oshwhub.com/recommend/art_pi_tuo_zhan_ban</a></p> 
<h3 style="text-align:start">文章分享篇</h3> 
<p style="text-align:start">技术分享文章现已超过 100 篇，<a href="https://art-pi.gitee.io/website/docs/#/tutorial/README">https://art-pi.gitee.io/website/docs/#/tutorial/README</a></p> 
<h3 style="text-align:start">致谢</h3> 
<p style="text-align:start">感谢以下小伙伴对本开源项目发布 SDK V1.2.0 的大力支持(排名不分先后)：heyuanjie87, caixf , dkk0918, forest-rain, My_Noob, iysheng, Ghazigq , hth945, lizimu2020, hyhkjiy, adaphoto, SimonLiu009, LZS, Embeded 小飞哥, 飘雪冰峰 , Z_Tam, MyJYHao, Ouxiaolong, 张竞豪, sgf201, 就是菜啊！, 爱FC的捷哥, 游泳的鱼儿, 爱学习的乐乐。</p> 
<p style="text-align:start">还要特别感谢一位开发者: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdillon-min" target="_blank">dillon-min</a>, 在这位开发者的帮助下， ART-Pi 不仅仅可以玩裸机工程，RT-Thread 工程，也可以尝试玩以下 Linux 了。目前已实现 u-boot 和 kernel 的支持，并进入他们主线。</p> 
<p style="text-align:start">uboot : <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsource.denx.de%2Fu-boot%2Fu-boot%2F-%2Ftree%2Fmaster%2Fboard%2Fst%2Fstm32h750-art-pi" target="_blank">https://source.denx.de/u-boot/u-boot/-/tree/master/board/st/stm32h750-art-pi</a></p> 
<p style="text-align:start">kernel : <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgit.kernel.org%2Fpub%2Fscm%2Flinux%2Fkernel%2Fgit%2Fnext%2Flinux-next.git%2Ftree%2Farch%2Farm%2Fboot%2Fdts%2Fstm32h750i-art-pi.dts%3Fh%3Dnext-20210409" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/tree/arch/arm/boot/dts/stm32h750i-art-pi.dts?h=next-20210409</a></p> 
<p style="text-align:start"> </p> 
<p style="text-align:start"><strong>SDK 获取地址：</strong></p> 
<p style="text-align:start">github : <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FRT-Thread-Studio%2Fsdk-bsp-stm32h750-realthread-artpi" target="_blank">https://github.com/RT-Thread-Studio/sdk-bsp-stm32h750-realthread-artpi</a></p> 
<p style="text-align:start">gitee : <a href="https://gitee.com/mirrors/ART-Pi">https://gitee.com/mirrors/ART-Pi</a> (镜像仓库，每日更新一次)</p> 
<p style="text-align:start"><strong>RTT Studio 可以在资源管理器直接下载</strong></p> 
<p style="text-align:start"> </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b643f2377c7bd67e813c40fcc5c4977847a.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            