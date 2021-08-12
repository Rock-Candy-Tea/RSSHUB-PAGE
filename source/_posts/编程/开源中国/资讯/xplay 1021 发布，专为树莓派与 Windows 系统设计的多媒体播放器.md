
---
title: 'xplay 1.0.21 发布，专为树莓派与 Windows 系统设计的多媒体播放器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8930bbdc35dc67f90bf09149e1b4536d922.JPEG'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 12:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8930bbdc35dc67f90bf09149e1b4536d922.JPEG'
---

<div>   
<div class="content">
                                                                                            <p>xplay <a href="https://gitee.com/nljb/xplay/tree/v1.0.21.v20210806">v1.0.21.v20210806</a> 发布了，在 v1.0.20.v20210117 基础上更新如下 ...</p> 
<p>1. 重构渲染线程与控制控制，在渲染时素材的增删改查响应更及时，渲染速度更快。<br> 2. 增加素材在切换时的过渡帧（缓存上个素材的停止时帧，在新的素材加载完成前渲染上个素材帧）。<br> 3. 增加命令行参数 buflen 可以指定视频缓存帧数量，低缓存帧可以在更低的可用内存中 。<br> 4. 支持预加载、预停止，在 play 与 stop 中均可以指定指令开始时间（毫秒精度）。<br> 5. 升级 FFmpeg（Raspberry Pi：4.3.2、Windows 10：4.4.5）与 SDL（2.0.14）。<br> 6. 在该版本中，进一步整合 Qt 框架（在线程与信号的传递中）...<br> 7. 修复一些 BUG ...</p> 
<p style="text-align:left"><a href="https://gitee.com/nljb/xplay">https://gitee.com/nljb/xplay</a>（树莓派）</p> 
<p style="text-align:left"><a href="https://gitee.com/nljb/winxplay">https://gitee.com/nljb/winxplay</a>（Windows）</p> 
<hr> 
<h3 style="text-align:left"> </h3> 
<p><img alt height="1024" src="https://oscimg.oschina.net/oscnet/up-8930bbdc35dc67f90bf09149e1b4536d922.JPEG" width="1024" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5a0386c2a2669f421f07464e9c8bd588ef6.gif" referrerpolicy="no-referrer"></p> 
<hr> 
<h3 style="text-align:left">支持硬件</h3> 
<table cellspacing="0" style="width:835px"> 
 <thead> 
  <tr> 
   <th>硬件</th> 
   <th>分辨率</th> 
   <th>FPS</th> 
   <th>测试</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi Zero</td> 
   <td style="border-color:#dfe2e5">1080p/v720p</td> 
   <td style="border-color:#dfe2e5">30</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi 3A+</td> 
   <td style="border-color:#dfe2e5">1080p/v720p</td> 
   <td style="border-color:#dfe2e5">30</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi 3B+</td> 
   <td style="border-color:#dfe2e5">1080p/v720p</td> 
   <td style="border-color:#dfe2e5">30</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi 2B</td> 
   <td style="border-color:#dfe2e5">1080p/v720p</td> 
   <td style="border-color:#dfe2e5">30</td> 
   <td style="border-color:#dfe2e5">未测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi 3B</td> 
   <td style="border-color:#dfe2e5">1080p/v720p</td> 
   <td style="border-color:#dfe2e5">30</td> 
   <td style="border-color:#dfe2e5">未测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi 4B</td> 
   <td style="border-color:#dfe2e5">1080p/<a href="https://gitee.com/nljb/xplay/issues/I1HPLH">【双】</a></td> 
   <td style="border-color:#dfe2e5">30</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Android 系统</td> 
   <td style="border-color:#dfe2e5">-</td> 
   <td style="border-color:#dfe2e5">-</td> 
   <td style="border-color:#dfe2e5">可定制</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Linux 系统</td> 
   <td style="border-color:#dfe2e5">-</td> 
   <td style="border-color:#dfe2e5">-</td> 
   <td style="border-color:#dfe2e5">可定制</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Windows 系统</td> 
   <td style="border-color:#dfe2e5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnulijiabei%2Fwinxplay" target="_blank">github</a> / <a href="https://gitee.com/nljb/winxplay">gitee</a></td> 
   <td style="border-color:#dfe2e5">-</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:left"><em><strong>理论上支持所有树莓派，但是经过测试的树莓派只有上面几款</strong></em></p> 
<hr> 
<h3 style="text-align:left">支持系统</h3> 
<table cellspacing="0" style="width:835px"> 
 <thead> 
  <tr> 
   <th>系统版本</th> 
   <th>发布日期</th> 
   <th>安装程序</th> 
   <th>测试</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5">2021-05-07</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5">2021-05-07</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5">2021-03-04</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5">2021-03-04</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5">2021-01-11</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5">2021-01-11</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5">2020-12-02</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5">2020-12-02</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5">2020-08-20</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5">2020-08-20</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with desktop</td> 
   <td style="border-color:#dfe2e5">2020-05-27</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspberry Pi OS with Lite</td> 
   <td style="border-color:#dfe2e5">2020-05-27</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspbian Buster with desktop</td> 
   <td style="border-color:#dfe2e5">2019-09-26</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspbian Buster Lite</td> 
   <td style="border-color:#dfe2e5">2019-09-26</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspbian Buster with desktop</td> 
   <td style="border-color:#dfe2e5">2020-02-13</td> 
   <td style="border-color:#dfe2e5">buster/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Raspbian Buster Lite</td> 
   <td style="border-color:#dfe2e5">2020-02-13</td> 
   <td style="border-color:#dfe2e5">buster-lite/</td> 
   <td style="border-color:#dfe2e5">已测试</td> 
  </tr> 
 </tbody> 
</table> 
<hr> 
<h3 style="text-align:left">支持功能</h3> 
<ol> 
 <li>支持自定义播放器分辨率、帧率(FPS)，支持音频采样率(Sample Rate)自适应</li> 
 <li>支持使用(TCP)连接播放器发送指令控制(播放、覆盖、停止、移动、等)</li> 
 <li>支持(视频、音频、流媒体、图片、摄像头、动画、文本、滚动字幕、日期时间、二维码)素材播放</li> 
 <li>支持(视频)多种格式(例如：MP4、AVI、MOV、等)、音频(AAC)</li> 
 <li>支持(流媒体)RTMP、RTSP、HTTP、H264/H265(YUV420P/YUVJ420P)</li> 
 <li>支持(图片)JPG与PNG格式</li> 
 <li>支持(动画)GIF格式</li> 
 <li>支持(视频)硬解播放(MMAL、VAAPI、VDPAU、QSV、MediaCodec、RKMPP、NVDEC)、(H264)</li> 
 <li>支持(视频)预加载</li> 
 <li>支持(视频)单线程解码与多线程解码双模式</li> 
 <li>支持(摄像头)设备(Raspberry Pi Camera V2)</li> 
 <li>支持(视频、图片)无黑场切换播放</li> 
 <li>支持(视频、图片)序列播放</li> 
 <li>支持(视频)音频同步(视频帧时间戳与音轨帧时间戳)播放</li> 
 <li>支持(视频)时钟同步(视频帧时间戳与时钟时间戳)播放</li> 
 <li>支持(视频、流媒体、图片、摄像头、动画、文本、滚动字幕、日期时间、二维码)多层(Overlay)播放</li> 
 <li>支持(文本)自定义(字体大小、字体颜色、背景颜色、透明度、对齐方式、风格样式、多行段落)</li> 
 <li>支持(滚动字幕)自定义(字体大小、字体颜色、背景颜色、透明度、风格样式、移动速度、移动方向)</li> 
 <li>支持(信息提示框)自定义提示文本及多种状态标识(notice、success、warning、error)</li> 
 <li>支持(日期时间)自定义(字体大小、字体颜色、背景颜色、透明度、对齐方式、风格样式)</li> 
 <li>支持(字体)自定义(可以通过自定义指定TTC字体来实现不同效果的文本样式)</li> 
 <li>支持自定义布局(通过多层功能可以实现多种自定义布局)</li> 
 <li>支持自定义(视频)是否循环播放(视频在播放到结尾时是否停留在最后一帧)</li> 
 <li>支持自定义素材尺寸(width，height)，任意拉伸缩放素材尺寸播放</li> 
 <li>支持自定义素材位置(x，y)播放，任意定义素材播放位置</li> 
 <li>支持自定义移动素材位置(x，y)及改变素材尺寸(width，height)</li> 
 <li>支持自定义素材横竖屏旋转(横屏角度：0、180，竖屏角度：90、270)</li> 
 <li>支持自定义素材开始播放时间(多个播放器间可以实现同步播放)</li> 
 <li>支持实时屏幕快照(截屏)</li> 
 <li>支持静音播放</li> 
</ol>
                                        </div>
                                      
</div>
            