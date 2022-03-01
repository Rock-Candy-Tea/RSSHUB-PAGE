
---
title: '时隔 3 年， MPlayer 发布 1.5 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5215'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 23:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5215'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">MPlayer 是 GNU/Linux 生态系统中一款优秀的开源视频播放软件，自 2019 年 4 月 发布 1.4 版本的三年后，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.mplayerhq.hu%2Fdesign7%2Fnews.html" target="_blank">Mplayer 1.5 正式发布</a>，版本代号“希望”。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">MPlayer 1.5 兼容最新的 FFmpeg 版本（5.0）和当前的 FFmpeg 开发版本（FFmpeg master），带来以下变更：</p> 
<h3>解码器、分流器、流：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>FFmpeg 不再支持 ffmpeg12vpdau，改为单独提供 ffmpeg1vpdau 和 ffmpeg2vdpau 。</li> 
 <li>Live555 已弃用并禁用，未来将被移除</li> 
</ul> 
<h3>GUI</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修正了离开全屏模式后，视频窗口大小错误的问题</li> 
 <li>使用 x11 切换到全屏模式时，清除屏幕视频输出驱动</li> 
 <li><span style="color:#2e3033">命令行选项 -fs 现在可以识别 GUI 选项<span> </span><code>load_fullscreen</code></span> </li> 
 <li><span style="color:#2e3033">在 OpenGL 视频输出驱动程序的 X11 中拥有正常的视觉效果</span></li> 
 <li><span style="color:#2e3033">提供一个默认的主题皮肤，以在未安装主题的情况下使用 Mplayer GUI </span></li> 
 <li><span style="color:#2e3033">提供本地语言支持，即可以更改 GUI 的语言</span></li> 
 <li><span style="color:#2e3033">其他</span>小错误修正</li> 
</ul> 
<h3>其他</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新的配置选项<span> </span><code>--enable-nls</code><span> </span>，用于运行时的本地语言支持（目前仅适用于 GUI，默认情况下启用）</li> 
 <li>macOS：修复视网膜显示器的显示、输入处理缓慢等问题。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmplayerhq.hu%2FMPlayer%2Freleases%2FChangeLog-1.5" target="_blank">https://mplayerhq.hu/MPlayer/releases/ChangeLog-1.5</a></p>
                                        </div>
                                      
</div>
            