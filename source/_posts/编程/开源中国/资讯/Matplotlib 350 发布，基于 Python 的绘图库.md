
---
title: 'Matplotlib 3.5.0 发布，基于 Python 的绘图库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1946'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1946'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Matplotlib 是一个用于 Python 编程语言及其数值数学扩展 NumPy 的绘图库。它提供了一个面向对象的 API，用于将绘图嵌入到使用 Tkinter、wxPython、Qt 或 GTK 等通用 GUI 工具箱的应用程序中。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">该版本中值得关注的更新内容包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Figure 和 Axes 的创建/管理 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>subplot_mosaic</code><span> </span>支持简单的 Axes 共享</li> 
   <li>Figure 现在有<span> </span><code>draw_without_rendering</code><span> </span>方法</li> 
   <li>Figure<span> </span><code>__init__</code><span> </span>将关键字参数传递给 set</li> 
  </ul> </li> 
 <li>Plotting 方法 
  <ul style="margin-left:0; margin-right:0"> 
   <li>添加<span> </span><code>Auunlus</code><span> </span>补丁</li> 
   <li>为<span> </span><code>FancyArrow</code><span> </span>补丁添加<span> </span><code>set_data</code><span> </span>方法</li> 
   <li>在<span> </span><code>ArrowStyle</code><span> </span>和<span> </span><code>ConnectionPatch</code><span> </span>中加入新的箭头样式</li> 
  </ul> </li> 
 <li>Colors 和 Colormaps 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Colormap 注册表（实验性）</li> 
   <li>现在可以在 RGBA 阶段进行图像插值了</li> 
   <li><code>imshow</code><span> </span>支持半浮点数组</li> 
   <li>为<span> </span><code>Normalize</code><span> </span>对象添加了一个回调注册表</li> 
  </ul> </li> 
 <li>Titles、ticks 和 labels 
  <ul style="margin-left:0; margin-right:0"> 
   <li>在<span> </span><code>set_ticks</code><span> </span>中同时设置 ticks 位置和 labels</li> 
  </ul> </li> 
 <li>Fonts 和 Text 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>Text</code><span> </span>和<span> </span><code>TextBox</code><span> </span><code>parse_math</code><span> </span>选项</li> 
   <li>Text 可以在<span> </span><code>TextBox</code><span> </span>小部件内定位</li> 
   <li>简化了<span> </span><code>usetex</code><span> </span>模式的字体设置</li> 
   <li>……</li> 
  </ul> </li> 
 <li>rcParams 的改进 
  <ul style="margin-left:0; margin-right:0"> 
   <li>允许全局设置默认的图例<span> </span><code>labelcolor</code></li> 
  </ul> </li> 
 <li>3D Axes 的改进 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>Axes3D</code><span> </span>现在允许手动控制绘制顺序</li> 
   <li>允许在 3D plots 中改变垂直轴的位置</li> 
   <li><code>plot_surface</code><span> </span>支持 NaNs</li> 
   <li>3D plotting 方法支持<span> </span><code>data</code><span> </span>关键字参数</li> 
  </ul> </li> 
 <li>交互式工具的改进 
  <ul style="margin-left:0; margin-right:0"> 
   <li>Colorbars 现在具有平移和缩放功能</li> 
   <li>更新了<span> </span><code>Slider</code><span> </span>小工具的外观</li> 
   <li>选择器增加了清除、拖动和移除的功能</li> 
   <li><code>CallbackRegistry</code><span> </span>对象获得了一个暂时阻断信号的方法</li> 
  </ul> </li> 
 <li>Sphinx extensions 
  <ul style="margin-left:0; margin-right:0"> 
   <li>More configuration of mathmpl sphinx extension</li> 
  </ul> </li> 
 <li>后端的具体改进 
  <ul style="margin-left:0; margin-right:0"> 
   <li>新的 GTK4 后端</li> 
   <li>新的 Qt6 后端</li> 
   <li>在 Cairo-based、GTK 和 Tk 后端支持 HiDPI</li> 
   <li>Qt 图形选项编辑器的改进</li> 
   <li>WX 后端支持鼠标导航按钮</li> 
   <li>WebAgg 使用 asyncio 而不是 Tornado</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatplotlib%2Fmatplotlib%2Freleases%2Ftag%2Fv3.5.0" target="_blank">https://github.com/matplotlib/matplotlib/releases/tag/v3.5.0</a></p>
                                        </div>
                                      
</div>
            