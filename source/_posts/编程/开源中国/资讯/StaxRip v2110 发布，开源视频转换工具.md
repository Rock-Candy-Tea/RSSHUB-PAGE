
---
title: 'StaxRip v2.11.0 发布，开源视频转换工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5050'
author: 开源中国
comments: false
date: Mon, 04 Apr 2022 07:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5050'
---

<div>   
<div class="content">
                                                                                            <p>StaxRip v2.11.0 现已发布。StaxRip 是一个开源的视频转换工具，可以将蓝光光盘或 DVD 中的视频转换成 PC 常用的视频格式，具有一系列解复用器，复用器，编码器和解码器。需要在 .NET Framework 和 DirectX<strong> </strong>的 Windows 环境下运行。 </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次更新内容包括：</p> 
<ul> 
 <li>修复设置目录对话框中的错字（bdr99，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F798" target="_blank">#798</a>）</li> 
 <li>更新 AOMEnc 的参数（badcf00d，Dendraspis，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F821" target="_blank">#821</a>）</li> 
 <li>为 VS 重新安排 SMDegrain 的列表位置和定义（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F797" target="_blank">#797</a>）</li> 
 <li>将“Processing”添加到记忆中的窗口位置</li> 
 <li>添加新的宏 %random:digits%, %current_date%, %current_time%, %current_time24% ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F802" target="_blank">#802</a> )</li> 
 <li>修复有关 mkvextract 的 UI 问题</li> 
 <li>即使选择了多个项目，也修复了仅显示第一个项目名称的列表上的删除确认</li> 
 <li>重新组织编码器配置文件</li> 
 <li>添加 NVEnc 参数--lut3d、--lut3d_interp、--dolby-vision-rpu、--dolby-vision-profile</li> 
 <li>添加 VCEEnc 参数 --thread-affinity, --qvbr, --qvbr-quality ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F792" target="_blank">#792</a> )</li> 
 <li>添加 QSVEnc 参数--thread-affinity、--dhdr10-info、--dolby-vision-rpu、--dolby-vision-profile、--qvbr、--qvbr-quality</li> 
 <li>添加 x265 Dolby Vision Profile 8.4</li> 
 <li>修复较小的 mkvextract demux 问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F833" target="_blank">#833</a> )</li> 
 <li>为 DVBSUB 字幕添加 demux 支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F833" target="_blank">#833</a> )</li> 
 <li>添加新的音频命令行宏 %streamid0% 和 %streamid1% ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F842" target="_blank">#842</a> )</li> 
 <li>提高 x265 atc-sei 参数上限（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Fissues%2F815" target="_blank">#815</a>）</li> 
 <li>优化检查更新</li> 
 <li>未找到项目时也显示项目的路径</li> 
 <li>如果项目无法加载，不要关闭 Jobs 窗口</li> 
 <li>在项目选项中添加“Demux Attachments”和“Add Attachments to Muxer”</li> 
 <li>将“<span style="background-color:#ffffff; color:#24292f">Bitrate</span>”添加到 VCEEnc 和 QSVEnc 选项</li> 
 <li>更新工具 
  <ul> 
   <li>AOMEnc v3.2.0-393-g402e264b9-x64-gcc11.2.0 <span style="background-color:#ffffff; color:#24292f">Patman</span></li> 
   <li>ffmpeg-N v106445-g723065a346-x64-gcc11.2.0 <span style="background-color:#ffffff; color:#24292f">Patman</span></li> 
   <li>媒体信息 v22.03</li> 
   <li>MediaInfo.NET v7.3.0.0</li> 
   <li>MP4Box v2.1-DEV-rev79-gdf29bc8a0-x64-gcc11.2.0 <span style="background-color:#ffffff; color:#24292f">Patman</span></li> 
   <li>mpvnet v5.7.0.0</li> 
   <li>MKVToolNix v66.0</li> 
   <li>NVEnc v5.46</li> 
   <li>qaac v2.73</li> 
   <li>QSVEnc v6.10</li> 
   <li>Rav1e v0.5.0 (p20220322-2-gcbdf0703)-x64-gcc11.2.0 <span style="background-color:#ffffff; color:#24292f">Patman</span></li> 
   <li><span style="background-color:#ffffff; color:#24292f">Subtitle Edit</span> v3.6.5</li> 
   <li>SvtAv1EncApp v0.9.1-81-gdf313c62-x64-gcc11.2.0 <span style="background-color:#ffffff; color:#24292f">Patman</span></li> 
   <li>VCEEnc v6.17</li> 
   <li>x264 v0.164.3094+13-7816202-[Mod-by-P​​atman]-x64-gcc11.2.0</li> 
   <li>x265 v3.5+37+12-4e46995bc-[Mod-by-P​​atman]-x64-msvc1931</li> 
  </ul> </li> 
 <li>更新 <span style="background-color:#ffffff; color:#24292f">filters</span> 
  <ul> 
   <li>TemporalDegrain2 v2.4.3</li> 
   <li>G41Fun v2021-09-23</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstaxrip%2Fstaxrip%2Freleases%2Ftag%2Fv2.11.0" target="_blank">https://github.com/staxrip/staxrip/releases/tag/v2.11.0</a></p>
                                        </div>
                                      
</div>
            