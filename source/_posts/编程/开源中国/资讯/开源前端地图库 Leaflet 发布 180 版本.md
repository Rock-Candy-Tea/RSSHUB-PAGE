
---
title: '开源前端地图库 Leaflet 发布 1.8.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4977'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 09:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4977'
---

<div>   
<div class="content">
                                                                                            <p>Leaflet 是一个开源的 JavaScript 库，用于构建 Web 地图应用。首次发布于 2011 年，它支持大多数移动和桌面平台，支持 HTML5 和 CSS3。其用户包括FourSquare、Pinterest和Flickr。</p> 
<p>Leaflet发布了 v1.8.0 版本，这是一年半以来的开发成果。这是一个巨大的版本，主要集中在错误修复，主要的可靠性和可访问性的改进，清理遗留代码，以及对文档、开发工作流程和发布过程的大量改进。这是数百人的贡献的结晶，也是为未来更大的变化做准备。🍃从现在开始，发布将变得更加频繁。</p> 
<p>Leaflet 的作者 Vladimir Agafonkin 来自乌克兰，在他开发这个版本的时候，外面的基辅正在响起空袭警报，警告说俄罗斯即将进行空袭。他希望这个版本献给乌克兰为自由和民主对抗俄罗斯入侵的斗争🇺🇦。</p> 
<h3>⚠️<span> 打破向后兼容的改动</span></h3> 
<ul> 
 <li>通过引入新的 TapHold 处理程序，替换传统的 Tap （#7026,@johnd0e） ，提高移动 Safari 上右键菜单事件模拟的可靠性</li> 
 <li>重新组织 DivOverlay/Popup/Tooltip api （#7540 by @johnd0e） 
  <ul> 
   <li>将 Popup 相关选项从 DivOverlay 移动到 Popup（#7778 by @Falke-Design）</li> 
   <li>将 Tooltip 类从 leaflet-clickable 改为 leaflet-interactive（#7719 by @Falke-Design）</li> 
   <li>Map.closeTooltip 现在需要一个 Layer 作为参数（#7533 by @johnd0e）</li> 
  </ul> </li> 
 <li>改进事件监听器的错误/参数处理（#7518 by @johnd0e）</li> 
 <li>提高非接触设备上触摸事件模拟的可靠性（DomEvent.Pointer）（#7059，#7084，#7415 by @johnd0e）</li> 
 <li>提高触摸设备上 dblclick 事件模拟的可靠性（DomEvent.DoubleTap）（#7027 by @johnd0e）</li> 
 <li>提高 disablecklickpropagation 的可靠性（#7439 by @johnd0e）</li> 
 <li>改进 Map hasLayer() 和 LayerGroup hasLayer() ，使其需要一个层作为参数（#6999 by @johnd0e）</li> 
 <li>修复 Class.include 不覆盖选项（#7756 by @johnd0e）</li> 
 <li>修正 Class.extend 以不修改源 props 对象（#6766 by @johnd0e）</li> 
 <li>改进 Browser.touch 触摸设备检测（#7029 by @johnd0e）</li> 
 <li>去除遗留的安卓hack（#7022 by @johnd0e）</li> 
 <li>允许字体通过使字体大小相对于地图容器来尊重用户的浏览器设置。（如果需要的话，你可以改变 leaflet-container 上的字体大小来调整它。）（#7800，@chandu-4444）</li> 
</ul> 
<h3>❇️ API 变化</h3> 
<ul> 
 <li>使 DivOverlay/Tooltip 具有交互性（#7531，#7532 by @johnd0e）</li> 
 <li>给 DivOverlay 添加 openOn，close，toggle函数 （#6639 by @johnd0e）</li> 
 <li>引入 DomEvent.off (el) 以删除所有监听器（#7125 by @johnd0e）</li> 
 <li>允许通过向 Util.formatNum/tenojson （#7100 by @johnd0e）传递 false 来防止舍入错误</li> 
 <li>添加 autoPanOnFocus 到 Marker （#8042 by @IvanSanchez）</li> 
 <li>将 referrerPolicy 添加到 TileLayer （#7945 by @natevw）</li> 
 <li>将 playsInline 添加到 VideoOverlay （#7928,@falke-Design）</li> 
 <li>添加 getCenter 到 ImageOverlay （#7848 by @Falke-Design）</li> 
 <li>当 TileLayer 加载取消时，启动一个 tileabort 事件（#6786 by @dstndstn）</li> 
 <li>在 Icon 中添加 crossOrigin（#7298 by @syedmuhammadabid）</li> 
</ul> 
<h3>✨ 改进</h3> 
<ul> 
 <li>通过删除 will-change CSS 属性（#7872 by @janjaap）改善内存占用</li> 
 <li>提高图标路径检测试探法的可靠性（#7092 by @johnd0e）</li> 
 <li>通过避免 GridLayer.onAdd （#7570 by @johnd0e）中的过度更新，提高添加平铺源的性能</li> 
 <li><span><span><span>改进 panInside 中边缘情况的处理</span></span></span>（#7469 by @daverapayment）</li> 
 <li>缩小标记图标 SVG （#7600 by @rala72）</li> 
 <li>允许在 TileLayer URL 中使用带空格的模板键（#7216 by @lubojr）</li> 
 <li>改进绑定到 ImageOverlay （#7306 by @IvanSanchez）的 Tooltip 行为</li> 
 <li>删除 Popup 和内容对话框之间的间隙（#7920 by @Malvoz）</li> 
 <li>如果没有图层，可以通过 Canvas <span><span><span>触发 mousemove 事件</span></span></span>（#7809 by @johnd0e）</li> 
 <li>添加打印样式，以防止打印机删除控件中的背景图像（#7851 by @Malvoz）</li> 
 <li>将属性代码从 Layer 移动到 Control.Attribution （#7764 by @johnd0e）</li> 
 <li>重构 vmlCreate() ，这样它就不会将闭包暴露给 TypeError （#7279 by @darcyparker）</li> 
 <li>提高 Control.Layers 的可靠性，不依赖浏览器 android 和触摸属性（#7057 by @johnd0e）</li> 
 <li>通过不依赖浏览器的触摸检查（#7535, @johnd0e）来提高 Tooltip 的可靠性</li> 
 <li>使浏览器易于自动化测试（#7335 by @bozdoz）</li> 
 <li>在 Control.Layers 容器中用 span 替换 div，以修复 HTML 验证错误（#7914 by @tmiaa）</li> 
 <li>添加一面乌克兰国旗作为默认署名（@mourner，#8109）</li> 
</ul> 
<hr> 
<p>更多变更请查看 https://github.com/Leaflet/Leaflet/releases/tag/v1.8.0。</p>
                                        </div>
                                      
</div>
            