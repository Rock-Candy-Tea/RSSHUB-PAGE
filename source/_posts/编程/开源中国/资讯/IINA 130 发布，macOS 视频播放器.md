
---
title: 'IINA 1.3.0 发布，macOS 视频播放器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8021'
author: 开源中国
comments: false
date: Mon, 30 May 2022 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8021'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">IINA 是采用 Swift 开发的 </span>macOS<span style="color:#333333"> </span>开源<span style="color:#333333">多媒体播放器，界面简洁运行流畅，兼具颜值和功能。 IINA 支持绝大部分常见音视频编码格式（甚至 GIF），此外还支持画中画播放、自动搜索字幕、视频截图和预览。</span></p> 
<p><span style="color:#333333">目前，IINA 更新了 1.3.0 版本，带来如下变更：</span></p> 
<h3><strong>新的</strong></h3> 
<ul> 
 <li>添加了对 M1 Pro/Max Macbook 14/16 的 HDR 支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3526" target="_blank"> #3526</a> )</li> 
 <li>添加了“上次打开日期”Finder 元数据的更新（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F579" target="_blank">#579</a>）</li> 
 <li>添加文件循环切换时的 OSD 通知 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3229" target="_blank">#3229</a> )</li> 
 <li>添加了对 macOS 减少运动可访问性首选项的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3437" target="_blank">#3437</a> )</li> 
 <li>添加了对在流式传输时从 Open Subtitles 下载字幕的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3431" target="_blank">#3431</a> )</li> 
</ul> 
<h3><strong>修复</strong></h3> 
<ul> 
 <li>修复了在 macOS 11+ 下使用旧版全屏时的崩溃问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3543" target="_blank">#3543</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3650" target="_blank">#3650</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3382" target="_blank">#3382</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3315" target="_blank">#3315</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3177" target="_blank">#3177</a>）</li> 
 <li>修复旧版全屏忽略双击（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3211" target="_blank">#3211</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3661" target="_blank">#3661</a>）</li> 
 <li>使用旧版全屏固定相机外壳块控制器 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3558" target="_blank">#3558</a> )</li> 
 <li>修复了在传统全屏模式下屏幕更改时未调整窗口大小的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3715" target="_blank">#3715</a> )</li> 
 <li>修复文件循环模式打开后无法通过菜单命令关闭（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3626" target="_blank">#3626</a>）</li> 
 <li>修复文件循环菜单项在打开时不显示 ✔︎ ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3625" target="_blank">#3625</a> )</li> 
 <li>修复了无法删除同名音频过滤器的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3620" target="_blank">#3620</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3088" target="_blank">#3088</a>）</li> 
 <li>修复了无法在菜单中切换音频过滤器的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3462" target="_blank">#3462</a> )</li> 
 <li>修复了 OpenGL 代码中的崩溃问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3475" target="_blank">#3475</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F2238" target="_blank">#2238</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F2588" target="_blank">#2588</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F2958" target="_blank">#2958</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3031" target="_blank">#3031</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3223" target="_blank">#3223</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3410" target="_blank">#3410</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3644" target="_blank">#3644</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3733" target="_blank">#3733</a>）</li> 
 <li>修复致命错误：视频信息不可用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3013" target="_blank">#3013</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3266" target="_blank">#3266</a>）</li> 
 <li>修复了与 macOS 电源管理相关的崩溃问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3478" target="_blank">#3478</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3361" target="_blank">#3361</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3379" target="_blank">#3379</a>）</li> 
 <li>修复了由于缩略图损坏而导致的崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3413" target="_blank">#3413</a> )</li> 
 <li>修复了 IINA 因“代码签名无效”而崩溃的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3551" target="_blank">#3551</a> )</li> 
 <li>修复 NSInvalidArgumentException 崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3584" target="_blank">#3584</a> )</li> 
 <li>修复了打开播放列表面板时 CPU 消耗过多的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3162" target="_blank">#3162</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3194" target="_blank">#3041</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3194" target="_blank">#3194</a>、 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3341" target="_blank">#3341</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3411" target="_blank">#3411</a>）</li> 
 <li>修复当前打开的文件名不同步（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3159" target="_blank">#3159</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3097" target="_blank">#3097</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3253" target="_blank">#3253</a>）</li> 
 <li>修复了升级到 Big Sur 后极其频繁的挂起；IINA 基本无法使用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3364" target="_blank">#3364</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3378" target="_blank">#3378</a>）</li> 
 <li>固定媒体键不起作用（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3574" target="_blank">#3574</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3681" target="_blank">#3681</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3340" target="_blank">#3340</a>）</li> 
 <li>固定纵横比随旋转变化不适用于自定义快捷方式（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F1168" target="_blank">#1168</a>）</li> 
 <li>修复了外部显示器断开连接时打开时的崩溃问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3695" target="_blank">#3695</a> )</li> 
 <li>修复了在扩展坞中暂停和最小化时消耗的 CPU ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3537" target="_blank">#3537</a> )</li> 
 <li>修复 PlaylistViewController 中的死锁 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3405" target="_blank">#3405</a> )</li> 
 <li>修复了忽略的自定义键绑定（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3692" target="_blank">#3692</a>）</li> 
 <li>修复了在目录中搜索媒体文件时的内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3445" target="_blank">#3445</a> )</li> 
 <li>修复了生成缩略图时的内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F1720" target="_blank">#1720</a> )</li> 
 <li>修复进度条未结束（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3331" target="_blank">#3331</a>）</li> 
 <li>修复左上栏动画与实际音量不同步的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3686" target="_blank">#3686</a>）</li> 
 <li>修复了 mpv 默认键绑定缺少键 mpv 添加（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3718" target="_blank">#3718</a>）</li> 
 <li>纠正了整个项目中的许多拼写错误</li> 
</ul> 
<h3><strong>更新</strong></h3> 
<ul> 
 <li>更新 mpv 到 0.34.1，FFmpeg 到 4.4.2，libgmp 到 6.2.1_1，libass 0.15.2</li> 
 <li>更新 mpv 以修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2021-30145" target="_blank">CVE-2021-30145</a> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3472" target="_blank">#3472</a> )</li> 
 <li>更新 mpv 以修复涉及 mpv/Lua 的内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3463" target="_blank">#3463</a> )</li> 
 <li>更新 mpv 以修复 mpv "advanced_editlist" 的内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3460" target="_blank">#3460</a> )</li> 
 <li>更新了 libgmp 以修复无法加载“打开 URL...”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3503" target="_blank">#3503</a>）</li> 
 <li>更新 libass 以修复 IINA 无法正确呈现波斯语字幕 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3222" target="_blank">#3222</a> )</li> 
 <li>更新 FFmpeg 以修复添加音频过滤器触发堆缓冲区溢出 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Fissues%2F3668" target="_blank">#3668</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fiina%2Fiina%2Freleases%2Ftag%2Fv1.3.0" target="_blank">https://github.com/iina/iina/releases/tag/v1.3.0</a></p>
                                        </div>
                                      
</div>
            