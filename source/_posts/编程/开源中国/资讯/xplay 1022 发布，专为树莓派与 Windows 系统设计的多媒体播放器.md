
---
title: 'xplay 1.0.22 发布，专为树莓派与 Windows 系统设计的多媒体播放器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8cd27e4ed8ca80082d4d7fc8789b772ecae.gif'
author: 开源中国
comments: false
date: Thu, 24 Feb 2022 13:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8cd27e4ed8ca80082d4d7fc8789b772ecae.gif'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:left">v1.0.22.v20220213 更新内容：</p> 
<p>在 1.0.21 稳定版本基础上升级了最新的 SDL、FFmpeg 等 ...</p> 
<p>因为新 <span style="background-color:#f6f8fa; color:#40485b">Raspberry Pi OS 已经无法支持 OMX，官方推出了 </span><span style="background-color:#ffffff; color:#40485b">Raspberry Pi OS (Legacy)</span> 来兼容旧版</p> 
<p>所以 xplay 分别发布兼容 rpios（x11、drm） 与 rpios l<span style="background-color:#ffffff; color:#40485b">egacy（omx）版本来兼容两款系统</span></p> 
<p>同时 xplay 还推出了 linux 版本（已支持：ubuntu 20.04）</p> 
<hr> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">https://gitee.com/nljb/xplay（Raspberry Pi）</p> 
<p>https://gitee.com/nljb/winxplay（Windows）</p> 
<p>https://gitee.com/nljb/ubuntu-xplay（Ubuntu）</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">专为树莓派(Raspberry Pi)设计的多媒体播放器且支持(Windows、Linux、Android)系统</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-8cd27e4ed8ca80082d4d7fc8789b772ecae.gif" referrerpolicy="no-referrer"></p> 
<hr> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">支持(视频、音频、流媒体、图片、摄像头、动画、文本、滚动字幕、日期时间、二维码)</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支持硬件</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:835px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>硬件</th> 
   <th>模式</th> 
   <th>分辨率</th> 
   <th>FPS</th> 
   <th>测试</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi Zero</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/OMX</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1080p/v720p</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi Zero 2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/OMX</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1080p/v720p</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">待测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi 3A+</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/OMX</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1080p/v720p</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi 3B+</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/OMX</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1080p/v720p</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi 2B</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/OMX</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1080p/v720p</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">未测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi 3B</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/OMX</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1080p/v720p</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">未测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi 4B</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/X11</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">1080p/<a href="https://gitee.com/nljb/xplay/issues/I1HPLH">【双】</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Android 系统</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">可定制</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Linux 系统</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">DRM/X11</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fnulijiabei%2Fubuntu-xplay">github</a><span> </span>/<span> </span><a href="https://gitee.com/nljb/ubuntu-xplay">gitee</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Windows 系统</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Microsoft Direct3D</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fnulijiabei%2Fwinxplay">github</a><span> </span>/<span> </span><a href="https://gitee.com/nljb/winxplay">gitee</a></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">-</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><em><strong>理论上支持所有树莓派，但是经过测试的树莓派只有上面几款</strong></em></p> 
<hr> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支持系统</h3> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:835px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>系统版本</th> 
   <th>发布日期</th> 
   <th>安装程序</th> 
   <th>测试版本</th> 
   <th>测试状态</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS (Legacy) with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022-01-28</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">raspios-legacy/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">master</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2022-01-28</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">raspios/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">master</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS (Legacy) with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-12-02</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">raspios-legacy/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">master</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-10-30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">raspios/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">master</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-10-30</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">→</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">→</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">不兼容</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-05-07</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">v1.0.21.v20210806</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-05-07</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">v1.0.21.v20210806</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-03-04</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-03-04</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-01-11</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2021-01-11</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-12-02</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-12-02</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-08-20</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-08-20</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-05-27</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-05-27</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspbian Buster with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2019-09-26</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspbian Buster Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2019-09-26</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">↑</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspbian Buster with desktop</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-02-13</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">v1.0.1.v20191105</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Raspbian Buster Lite</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">2020-02-13</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">buster-lite/</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">v1.0.1.v20191105</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">已测试</td> 
  </tr> 
 </tbody> 
</table> 
<hr> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支持功能</h3> 
<pre><code>支持自定义播放器分辨率、帧率(FPS)，支持音频采样率(Sample Rate)自适应
支持使用(TCP)连接播放器发送指令控制(播放、覆盖、停止、移动、等)
支持(视频、音频、流媒体、图片、摄像头、动画、文本、滚动字幕、日期时间、二维码)素材播放
支持(视频)多种格式(例如：MP4、AVI、MOV、等)、音频(AAC)
支持(流媒体)RTMP、RTSP、HTTP、H264/H265(YUV420P/YUVJ420P)
支持(图片)JPG与PNG格式
支持(动画)GIF格式
支持(视频)硬解播放(MMAL、VAAPI、VDPAU、QSV、MediaCodec、RKMPP、NVDEC)、(H264)
支持(视频)预加载
支持(视频)单线程解码与多线程解码双模式
支持(摄像头)设备(Raspberry Pi Camera V2)
支持(视频、图片)无黑场切换播放
支持(视频、图片)序列播放
支持(视频)音频同步(视频帧时间戳与音轨帧时间戳)播放
支持(视频)时钟同步(视频帧时间戳与时钟时间戳)播放
支持(视频、流媒体、图片、摄像头、动画、文本、滚动字幕、日期时间、二维码)多层(Overlay)播放
支持(文本)自定义(字体大小、字体颜色、背景颜色、透明度、对齐方式、风格样式、多行段落)
支持(滚动字幕)自定义(字体大小、字体颜色、背景颜色、透明度、风格样式、移动速度、移动方向)
支持(信息提示框)自定义提示文本及多种状态标识(notice、success、warning、error)
支持(日期时间)自定义(字体大小、字体颜色、背景颜色、透明度、对齐方式、风格样式)
支持(字体)自定义(可以通过自定义指定TTC字体来实现不同效果的文本样式)
支持自定义布局(通过多层功能可以实现多种自定义布局)
支持自定义(视频)是否循环播放(视频在播放到结尾时是否停留在最后一帧)
支持自定义素材尺寸(width，height)，任意拉伸缩放素材尺寸播放
支持自定义素材位置(x，y)播放，任意定义素材播放位置
支持自定义移动素材位置(x，y)及改变素材尺寸(width，height)
支持自定义素材横竖屏旋转(横屏角度：0、180，竖屏角度：90、270)
支持自定义素材开始播放时间(多个播放器间可以实现同步播放)
支持实时屏幕快照(截屏)
支持静音播放</code></pre>
                                        </div>
                                      
</div>
            