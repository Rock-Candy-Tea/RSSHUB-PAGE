
---
title: 'VASSAL 3.6.1 发布，开源棋牌游戏构建引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5502'
author: 开源中国
comments: false
date: Wed, 08 Dec 2021 06:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5502'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">VASSAL Engine 3.6.1 版本现已发布。VASSAL 是一个游戏引擎，用于在线构建棋盘游戏和纸牌游戏，构建的游戏可在 Internet 上或通过电子邮件实时运行。VASSAL Engine 可在所有平台上运行，并且是免费的开源软件。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">主要更新内容如下：</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>IMPORTANT</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新的 64 位 ARM 软件包。现在有针对 64 位 ARM 处理器的 MacOS 和 Windows 软件包。如果你有一台装有 Apple Silicon CPU（这是一个 64 位 ARM 处理器）的 Mac，官方建议使用 64 位 ARM 构建。</li> 
 <li>一年多以前弃用的代码已经被删除。使用该代码的模块如果要在 3.6 版本中工作，就必须进行更新。</li> 
 <li>以前能用的东西现在可能会被破坏。官方建议用户及时反馈发现的新错误。</li> 
 <li>在 3.6 中保存的模块不能被早期版本的 VASSAL 打开。以防万一，官方建议用户保留一份 3.6 之前的模块的备份。</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Download</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvassalengine%2Fvassal%2Freleases%2Fdownload%2F3.6.1%2FVASSAL-3.6.1-linux.tar.bz2" target="_blank">Linux</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvassalengine%2Fvassal%2Freleases%2Fdownload%2F3.6.1%2FVASSAL-3.6.1-macos-aarch64.dmg" target="_blank">MacOS (64-bit ARM)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvassalengine%2Fvassal%2Freleases%2Fdownload%2F3.6.1%2FVASSAL-3.6.1-macos-x86_64.dmg" target="_blank">MacOS (64-bit x86)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvassalengine%2Fvassal%2Freleases%2Fdownload%2F3.6.1%2FVASSAL-3.6.1-windows-aarch64.exe" target="_blank">Windows (64-bit ARM)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvassalengine%2Fvassal%2Freleases%2Fdownload%2F3.6.1%2FVASSAL-3.6.1-windows-x86_64.exe" target="_blank">Windows (64-bit x86)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvassalengine%2Fvassal%2Freleases%2Fdownload%2F3.6.1%2FVASSAL-3.6.1-windows-x86_32.exe" target="_blank">Windows (32-bit x86)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvassalengine%2Fvassal%2Freleases%2Fdownload%2F3.6.1%2FVASSAL-3.6.1-other.zip" target="_blank">Other</a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Changes since 3.6.0</strong></h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#222222"><strong>新功能</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>10879：Dice Button 原始结果和计数报告</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#222222"><strong>Bug 修复</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>10876：从清单中删除不需要的空值</li> 
 <li>10871：在编辑器中显示设置全局属性和位置标记的专有名称</li> 
 <li>10869：库存不应在当前无法访问的私人窗口中显示图片/文字</li> 
 <li>10861：从坐标列表中读取的多边形不应为空</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#222222"><strong>其他改进</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>10880：Create HintTextFields lazily</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> 更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.vassalengine.org%2Ft%2Fvassal-3-6-1-released%2F73205%2F1" target="_blank">https://forum.vassalengine.org/t/vassal-3-6-1-released/73205/1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            