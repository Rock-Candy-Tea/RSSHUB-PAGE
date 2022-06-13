
---
title: 'Gear-Lib 1.1.21 发布，跨平台的 POSIX 扩展库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 00:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gear Lib 是一组面向 IOT 及网络流媒体开发的Ｃ基础库，接口简洁易用，适用于物联网嵌入式设备端的开发，如 IOT 采集传感器，视频监控，设备端网络直播等场景。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本 1.1.21 更新日志如下：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>[新增] 快速构建C/C++工程的编译环境 （来自 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdianjixz" target="_blank">dianjixz</a> 的PR）</li> 
 <li>[新增] httpd服务的支持 （来自 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdianjixz" target="_blank">dianjixz</a> 的PR）</li> 
 <li>[新增] utf2gbk，集合类的支持（来自 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdianjixz" target="_blank">dianjixz</a> 的PR）</li> 
 <li>[新增] avcap捕获音视频的接口，统一uvc/v4l2/Dshow/XCB linux桌面截屏/esp32 cam/linux pulseaudio等接口</li> 
 <li>[修复] 跨平台编译的问题，支持win32/linux/msys2(mingw32/64)/raspberrypi/esp32等环境的编译</li> 
 <li>[修复] libdict/libconfig/libstrex/libdarray/libposix/libworkq等多处兼容性问题</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img align="left" alt="gear-lib" height="248" src="https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png" width="731" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gear Lib 库内容包括：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">网络库</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librtsp: RTSP 协议，适合 IPCamera 和 NVR 开发</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librtmpc: RTMP 协议，适合推流直播</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libskt: Socket 封装</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librpc: 远程过程调用库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libipc: 进程间通信</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libp2p: p2p 穿透传输</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">libmqttc: MQTT 客户端协议</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">libhomekit: Apple homekit 协议库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">libhttpd: 移植于mongoose</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据结构</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libdict: 哈希字典</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libhash: linux 内核原生哈希库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libringbuffer: 循环缓冲</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libqueue: 数据队列</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librbtree: 内核 rbtree</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libsort:</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libvector: 容器库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libdarray: 动态数组</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">异步</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libgevent: 事件驱动</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libthread: 线程</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libworkq: 工作队列</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">I/O</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libstrex:字符串扩展库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libconfig: 配置文件库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">liblog: 日志库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libfile: 文件操作库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libsubmask: 网络地址翻译</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">多媒体</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libavcap: 音视频捕获库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libmp4: MP4 解析库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libjpeg-ex:</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libmedia-io: 音频视频格式定义</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">系统抽象层</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libposix: Win32/Linux/FreeRTOS/RT-Thread平台适配库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">其他</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libdebug: 调试辅助库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libhal: 硬件抽象层</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libplugin: 动态加载库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libtime: 时间库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libfsm: 有限状态机</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云主页：<a href="https://gitee.com/gozfreee/gear-lib">https://gitee.com/gozfreee/gear-lib</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github 主页：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgozfree%2Fgear-lib" target="_blank">https://github.com/gozfree/gear-lib</a></p>
                                        </div>
                                      
</div>
            