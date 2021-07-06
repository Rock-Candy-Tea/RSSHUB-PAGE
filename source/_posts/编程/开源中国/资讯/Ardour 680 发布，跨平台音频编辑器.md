
---
title: 'Ardour 6.8.0 发布，跨平台音频编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5548'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 06:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5548'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ardour 6.8.0 正式发布，该版本更新内容如下：</p> 
<h3>新功能</h3> 
<p>播放列表操作，一个新的菜单 Track > Playlist，提供了为所有轨道创建新的播放列表(或复制的播放列表)的操作。播放列表的命名和分组行为已经改变：</p> 
<ul> 
 <li>当创建一个新的播放列表时，总是提示用户一个播放列表名称（默认值是 Take.N，其中 N 自动递增）。在过去，一些播放列表操作没有提示名称，而另一些则提示，导致命名不一致。</li> 
 <li>当一个播放列表被创建时，ardour 给它分配了一个组 ID（时间戳），之后可以用来识别作为同一操作的一部分而创建的播放列表。在过去，ardour 试图通过名字来匹配分组的播放列表，但这种关系对用户来说并不清楚。</li> 
 <li>当你第一次录入一个空的播放列表时，播放列表组的 ID 也会被隐式地创建。这解决了过去的问题，即用户创建的播放列表会作为一个组一起选择，但最初的曲目播放列表没有组关系，因此不能跟随组的选择。</li> 
</ul> 
<p>Performance Meters： <code><strong>Window > Performance Meters</strong></code> 现在提供了在 Ardour 内部发生的 "DSP" 的低水平计量；</p> 
<p>增加对请求特定 CPU DMA 延迟值的支持（在某些系统上可以提高 DSP 性能，而在其他系统上则会降低性能或没有影响）。如果你不明白这有什么作用，那么最好不要管它；</p> 
<p>为 MIDI 编辑增加扩展选择和反选操作；</p> 
<p>新增音轨编辑操作 "remove gaps"，可调整阈值和 "leave" 参数；</p> 
<p>增加 M4A 导入支持；</p> 
<p>MIDI 跟踪窗口现在有了自己的端口，可以任意跟踪 MIDI 数据；</p> 
<h3>改进</h3> 
<ul> 
 <li>为 ACE-Fluidsynth 增加旁路控制；</li> 
 <li>增加雅马哈 P-121/125 键盘的 MIDNAM 文件；</li> 
 <li>在网格的 BBT 分区之间变化时不触发标尺显示；</li> 
 <li>对 ProTools 会话导入进行崩溃修复和速度改进；</li> 
 <li>允许重命名区域/源提示标记；</li> 
 <li>允许拖动区域/源提示标记；</li> 
 <li>停止在系统范围内使用命名的信号，以避免与其他软件发生冲突；</li> 
 <li>当切换 to/from 非实时输出时忽略 xruns；</li> 
 <li>删除 CoreAudio 设备列表中的重复内容；</li> 
 <li>重构输入端口的监控；</li> 
 <li>改进为关键线程设置实时优先级的方法；</li> 
 <li>为支持 websocket 提供更好的事件循环整合；</li> 
 <li>自动化控制点不再服从 "锁定编辑" 模式，它应该只锁定区域和注释；</li> 
 <li>Slip-contents 的拖动更方便了；</li> 
 <li>对画笔拖动行为的一些改进；</li> 
 <li>覆盖 Ubuntu 全局菜单行为；</li> 
 <li>改进了启动时 splash 窗口的可见性管理；</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>修复时钟显示的内存泄漏；</li> 
 <li>修复 ripple edits 撤销/重做的问题；</li> 
 <li>修复编辑器中区域和源列表消失的问题；</li> 
 <li>修复控制面的 "transport-play" 操作的行为；</li> 
 <li>修复处理MIDI bounce 时的崩溃；</li> 
 <li>修复多时间段导出时的挂起问题；</li> 
 <li>修复使用外部位置同步（MTC、LTC等）和切换后端时的崩溃问题；</li> 
 <li>修复长时间运行会话（2-5天）中的 deadlock 问题；</li> 
</ul> 
<h3>翻译更新</h3> 
<ul> 
 <li>巴斯克语；</li> 
 <li>捷克语；</li> 
 <li>俄语；</li> 
 <li>德语；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FArdour%2Fardour%2Freleases%2Ftag%2F6.8" target="_blank">https://github.com/Ardour/ardour/releases/tag/6.8</a></p>
                                        </div>
                                      
</div>
            