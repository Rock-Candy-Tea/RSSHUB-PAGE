
---
title: 'Stats v2.7.0 发布，macOS 系统监视器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8231'
author: 开源中国
comments: false
date: Tue, 18 Jan 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8231'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Stats 是一款开源的 macOS 系统监控工具，可以驻留在菜单栏中对 CPU、GPU、内存、磁盘和网络等进行实时监测。</p> 
<p style="margin-left:0px">目前 Stats v2.7.0 发布了 ，此版本带来如下变更:</p> 
<h2><strong>关闭 issues</strong></h2> 
<ul> 
 <li>feat: 重新设计蓝牙阅读器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fexelban%2Fstats%2Fissues%2F750" target="_blank">#750</a>)</li> 
 <li>fix: 移除 Apple Silicon 的调度器和速度限制 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fexelban%2Fstats%2Fissues%2F749" target="_blank">#749</a>)</li> 
 <li>fix: 修复网络图标的单颜色 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fexelban%2Fstats%2Fissues%2F784" target="_blank">#784</a>)</li> 
 <li>feat: 为 Apple Silicon 传感器添加了新的 SMC 密钥 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fexelban%2Fstats%2Fissues%2F700" target="_blank">#700</a>)</li> 
</ul> 
<h2>新特性和 bug 修复</h2> 
<ul> 
 <li>feat: 合并 HID 和 SMC 传感器读取器，此外还改善了 Apple Silicons MacBook 的 CPU 消耗（10% -> 4-5%）</li> 
 <li>feat: 禁用 large_tuple swiftlint 规则</li> 
 <li>feat: 在 GPU 信息中添加了核心数（Apple Silicon）</li> 
 <li>feat:  为 mac 添加了电池电量健康线</li> 
 <li>fix: 为 macOS Monterey 固定设置窗口小部件的控件按钮位置</li> 
 <li>feat: 为 Apple Silicon 图形添加了更好的 GPU 名称、渲染和平铺利用率</li> 
 <li>feat: 为 Apple Silicon 新增 CPU 温度检测</li> 
 <li>feat: 添加了一个选项，用于启用/禁用带有 Apple Silicon 的 Mac 的 HID 传感器（默认禁用）</li> 
 <li>feat: 添加了将风扇速度保存到传感器模块的选项</li> 
 <li>feat: 风扇视图的微小变化（传感器模块）</li> 
 <li>fix: 修复弹出视图中传感器的顺序</li> 
 <li>feat: 为 GPU 视窗添加渲染和平铺利用率图表</li> 
</ul> 
<h2>本地化</h2> 
<ul> 
 <li>feat: 更新简体中文翻译 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fexelban%2Fstats%2Fpull%2F789" target="_blank">#789</a>)</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fexelban%2Fstats%2Freleases%2Ftag%2Fv2.7.0" target="_blank">https://github.com/exelban/stats/releases/tag/v2.7.0</a></p>
                                        </div>
                                      
</div>
            