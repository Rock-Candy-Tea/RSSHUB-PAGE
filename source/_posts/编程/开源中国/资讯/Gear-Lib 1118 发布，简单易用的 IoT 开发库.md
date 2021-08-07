
---
title: 'Gear-Lib 1.1.18 发布，简单易用的 IoT 开发库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 12:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">Gear Lib 是一组面向IOT及网络流媒体开发的Ｃ基础库，接口简洁易用，适用于物联网嵌入式设备端的开发，如IOT采集传感器，视频监控，设备端网络直播等场景。</p> 
<p style="text-align:left">新版本 1.1.18 更新日志如下：</p> 
<ul> 
 <li>新增bitmap的接口，移植kernel的bitmap库</li> 
 <li>重新移植libptcp到p2p的接口</li> 
 <li>更新librpc的接口，优化p2p的调用流程</li> 
 <li>优化pipe为eventfd，减少fd的使用</li> 
 <li>修复libconfig的json适配</li> 
</ul> 
<p style="text-align:left"><img align="left" alt="gear-lib" height="248" src="https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png" width="731" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"> </p> 
<p style="text-align:left">Gear Lib库内容包括：</p> 
<p style="text-align:start">网络库</p> 
<table cellspacing="0" style="width:942.188px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">librtsp: RTSP协议，适合IPCamera和NVR开发</td> 
   <td style="border-color:#dfe2e5">librtmpc: RTMP协议，适合推流直播</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libskt: Socket封装</td> 
   <td style="border-color:#dfe2e5">librpc: 远程过程调用库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libipc: 进程间通信</td> 
   <td style="border-color:#dfe2e5">libp2p: p2p穿透传输</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libhomekit: Apple homekit协议库</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left">数据结构</p> 
<table cellspacing="0" style="width:942.188px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">libdict: 哈希字典</td> 
   <td style="border-color:#dfe2e5">libhash: linux内核原生哈希库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libringbuffer: 循环缓冲</td> 
   <td style="border-color:#dfe2e5">libqueue: 数据队列</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">librbtree: 内核rbtree</td> 
   <td style="border-color:#dfe2e5">libsort:</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libvector: 容器库</td> 
   <td style="border-color:#dfe2e5">libdarray: 动态数组</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start">异步</p> 
<table cellspacing="0" style="width:942.188px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">libgevent: 事件驱动</td> 
   <td style="border-color:#dfe2e5">libthread: 线程</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libworkq: 工作队列</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start">I/O</p> 
<table cellspacing="0" style="width:942.188px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">libbase64: Base64/32 编解码</td> 
   <td style="border-color:#dfe2e5">libconfig: 配置文件库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">liblog: 日志库</td> 
   <td style="border-color:#dfe2e5">libfile: 文件操作库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libstrex:</td> 
   <td style="border-color:#dfe2e5">libsubmask: 网络地址翻译</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start">多媒体</p> 
<table cellspacing="0" style="width:942.188px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">libuvc: USB摄像头库</td> 
   <td style="border-color:#dfe2e5">libmp4: MP4解析库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libjpeg-ex:</td> 
   <td style="border-color:#dfe2e5">libmedia-io: 音频视频格式定义</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start">系统抽象层</p> 
<table cellspacing="0" style="width:942.188px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">libposix4win: windows平台poxix适配库</td> 
   <td style="border-color:#dfe2e5">libposix4rtos: FreeRTOS平台poxix适配库</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start">其他</p> 
<table cellspacing="0" style="width:942.188px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">libdebug: 调试辅助库</td> 
   <td style="border-color:#dfe2e5">libhal: 硬件抽象层</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libplugin: 动态加载库</td> 
   <td style="border-color:#dfe2e5">libtime: 时间库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">libfsm: 有限状态机</td> 
   <td style="border-color:#dfe2e5"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left">码云主页：<a href="https://gitee.com/gozfreee/gear-lib">https://gitee.com/gozfreee/gear-lib</a></p> 
<p style="text-align:left">github主页：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgozfree%2Fgear-lib" target="_blank">https://github.com/gozfree/gear-lib </a></p>
                                        </div>
                                      
</div>
            