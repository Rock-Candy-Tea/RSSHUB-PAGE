
---
title: 'LibreELEC 10.0.0 发布，放弃对老款树莓派的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2054'
author: 开源中国
comments: false
date: Tue, 31 Aug 2021 05:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2054'
---

<div>   
<div class="content">
                                                                                            <p>LibreELEC 10.0.0 正式发布，为 LibreELEC 用户带来 Kodi (Matrix) v19.1。正在使用 LibreELEC 10 Beta 或 RC1 的用户会自动更新到最新版本。LibreELEC 9.2 则将不会自动更新，用户需要手动更新。</p> 
<h3>树莓派 0-3</h3> 
<p>LibreELEC 10.0.0 没有 Raspberry Pi 0-3 版本。RPi 的图形驱动仍在完全重写的过程中，此外，目前的开发工作主要集中在 Raspberry Pi 4 上。</p> 
<ul> 
 <li>对 RPi 0-1 的支持被放弃了；</li> 
 <li>RPi 2 和 3 的驱动目前还没有完整和稳定的功能</li> 
</ul> 
<h3>树莓派 4</h3> 
<p>RPi 4 的情况则完全不同，目前版本是可以正常使用的。</p> 
<h3>正在开发</h3> 
<ul> 
 <li>HDMI 输出高达 4k@30</li> 
 <li>H264 和 H265 HW 解码</li> 
 <li>新：HDR 输出（HDR10 和 HLG）</li> 
 <li>新：HD 音频（Dolby TrueHD、DTS HD）</li> 
</ul> 
<h3>自 LibreELEC 9.2 以来的重要变化：</h3> 
<p>config.txt 中的 <code>hdmi_mode</code>、 <code>hdmi_group</code>、 <code>hdmi_edid_file</code> 等设置不再用来解决显示问题。</p> 
<p>替代方法：</p> 
<ul> 
 <li>运行 <code>getedid create</code> 来安装永久的 EDID 文件</li> 
 <li>使用 <code>video=...</code> 内核命令行选项来强制选择视频模式，例如：在 cmdline.txt 中添加 <code>video=HDMI-A-1:1280x720M@60D</code></li> 
</ul> 
<p>默认情况下，模拟音频输出未被启用</p> 
<p>解决方案：在 config.txt 中添加 <code>dtparam=audio=on</code> 和 <code>audio_pwm_mode=1</code> 来启用它。</p> 
<h3>遗留的 bug</h3> 
<p>尽管 LibreELEC 10.0.0 经过了很长时间的开发，但目前仍有一个主要的 bug。当你使用配置文件时，LibreELEC 的设置插件会在切换到另一个配置文件时崩溃。目前这个 bug 还没有被修复，因此，如果用户特别依赖配置文件，那么就最好暂时不要升级。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flibreelec.tv%2F2021%2F08%2F26%2Flibreelec-matrix-10-0%2F" target="_blank">https://libreelec.tv/2021/08/26/libreelec-matrix-10-0/</a></p>
                                        </div>
                                      
</div>
            