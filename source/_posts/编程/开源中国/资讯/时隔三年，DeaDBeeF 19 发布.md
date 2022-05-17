
---
title: '时隔三年，DeaDBeeF 1.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0517/071023_keOe_4937141.png'
author: 开源中国
comments: false
date: Tue, 17 May 2022 07:10:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0517/071023_keOe_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>DeaDBeeF 是一个模块化的跨平台音频播放器，可在 Linux、macOS、Windows 和类 Unix 系统上运行。该播放器于 2009 年首次发布。</p> 
<p>自 DeaDBeeF 1.8 发布后，如今时隔三年，1.9 版本正式发布，更新内容如下：</p> 
<p><img height="1018" src="https://static.oschina.net/uploads/space/2022/0517/071023_keOe_4937141.png" width="1412" referrerpolicy="no-referrer"></p> 
<h3>修复：</h3> 
<ul> 
 <li>导致播放损坏的 WMA 退步</li> 
 <li>ALSA 插件中的死锁</li> 
 <li>错误地将原始 AAC 文件检测为 MP4 文件</li> 
 <li>处理空的标题格式化脚本</li> 
 <li>通过 Playlist Browser 拖动播放列表时的内存错误</li> 
 <li>跨播放列表标签的键盘导航问题</li> 
 <li>播放列表标签和播放列表自定义颜色的错误</li> 
 <li>强制退出后，暂停状态不能正确保持</li> 
 <li>保存播放列表和配置文件时性能不佳</li> 
 <li>sndfile 无法打开文件，因为存在未初始化的内存访问错误</li> 
 <li>在播放时从播放列表中删除曲目时发生崩溃</li> 
 <li>渲染带有空白文本的组标题</li> 
 <li>在标签栏上拖放时延迟激活播放列表标签</li> 
</ul> 
<h3>新增：</h3> 
<ul> 
 <li>支持 Opus 和 FFMPEG 的长文件搜索</li> 
 <li>通过 libmbedtls 在可移植构建中对 vfs_curl 的 HTTPS 支持</li> 
 <li>CocoaUI 的设计模式</li> 
 <li>新的范围和频谱分析器的可视化功能</li> 
 <li>可视化外观偏好窗格</li> 
 <li>新的专辑艺术加载器</li> 
 <li>通过上下文菜单可配置音量条刻度</li> 
 <li>标题格式化 $year(time) 函数</li> 
 <li>在表格界面中编辑多个选定曲目的选定字段的 GTK UI</li> 
 <li>通过点击播放列表标签条中的 "+" 按钮创建新的播放列表</li> 
 <li>改进了 DSP 偏好的 GTK 界面</li> 
 <li>改进了对无效 MP3 文件的处理</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2FLast.fm" target="_blank">Last.fm</a> scrobbler 将默认使用 HTTPS</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDeaDBeeF-Player%2Fdeadbeef" target="_blank">https://github.com/DeaDBeeF-Player/deadbeef</a></p>
                                        </div>
                                      
</div>
            