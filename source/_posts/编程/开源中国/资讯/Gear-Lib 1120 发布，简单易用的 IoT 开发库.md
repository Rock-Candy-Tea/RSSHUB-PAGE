
---
title: 'Gear-Lib 1.1.20 发布，简单易用的 IoT 开发库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 00:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gear Lib 是一组面向IOT及网络流媒体开发的Ｃ基础库，接口简洁易用，适用于物联网嵌入式设备端的开发，如IOT采集传感器，视频监控，设备端网络直播等场景。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新版本 1.1.20 更新日志如下：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>[新增] librtsp的rtp over tcp传输</li> 
 <li>[新增] libuvc的ioctl和图像质量调节控制</li> 
 <li>[新增] wepoll支持windowns到libgevent</li> 
 <li>[新增] 开源库pthreads4w到libposix</li> 
 <li>[新增] MsvcLibx到libposix</li> 
 <li>[新增] visual studio sln 编译工程</li> 
 <li>[修复] libuvc的cancelfd退出机制</li> 
 <li>[修复] librtsp的重新打开断流问题</li> 
 <li>[修复] libipc的sock文件存在导致打开失败的问题</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img align="left" alt="gear-lib" height="248" src="https://oscimg.oschina.net/oscnet/up-30d1151b27a171139de0888af90fecaf42f.png" width="731" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gear Lib库内容包括：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">网络库</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librtsp: RTSP协议，适合IPCamera和NVR开发</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librtmpc: RTMP协议，适合推流直播</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libskt: Socket封装</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librpc: 远程过程调用库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libipc: 进程间通信</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libp2p: p2p穿透传输</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">libmqttc: MQTT客户端协议</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px">libhomekit: Apple homekit协议库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">数据结构</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libdict: 哈希字典</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libhash: linux内核原生哈希库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libringbuffer: 循环缓冲</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libqueue: 数据队列</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">librbtree: 内核rbtree</td> 
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
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
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
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libbase64: Base64/32 编解码</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libconfig: 配置文件库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">liblog: 日志库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libfile: 文件操作库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libstrex:</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libsubmask: 网络地址翻译</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">多媒体</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libuvc: USB摄像头库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libmp4: MP4解析库</td> 
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
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libposix4win: windows平台poxix适配库</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">libposix4rtos: FreeRTOS平台poxix适配库</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">其他</p> 
<table cellspacing="0" style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-border-bottom:initial; --darkreader-inline-border-left:initial; --darkreader-inline-border-right:initial; --darkreader-inline-border-top:initial; --darkreader-inline-color:#bdb7af; -webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 20px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:942.188px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th> </th> 
   <th> </th> 
  </tr> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github主页：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgozfree%2Fgear-lib" target="_blank">https://github.com/gozfree/gear-lib </a></p>
                                        </div>
                                      
</div>
            