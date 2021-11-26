
---
title: 'Cocos Creator 2.4.7 正式发布，优化编辑器兼容性与稳定性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cd29418aa40864fd213bbe59b8d0a82f682.png'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 07:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cd29418aa40864fd213bbe59b8d0a82f682.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Cocos Creator 2.4.7 已正式发布。此次更新对近期发现的一些 2.x 相关问题集中进行了修复，重点提升了编辑器的稳定性、兼容性，官方建议所有 2.x 用户升级。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cd29418aa40864fd213bbe59b8d0a82f682.png" referrerpolicy="no-referrer"></p> 
<p>Cocos Creator 是以内容创作为核心，实现了脚本化、组件化和数据驱动的游戏开发工具。 具备了易于上手的内容生产工作流，以及功能强大的开发者工具套件，可用于实现游戏逻辑和高性能游戏效果。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-e622ff52598dc6383c70d6d03fb9a963de8.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">主要变化如下：</p> 
<p><strong>Stack Changes </strong></p> 
<ul> 
 <li style="text-align:justify"><span>升级编辑器的 Electron 版本到 13.1.4。解决了 Windows 上部分用户频繁出现的 WebGL 崩溃问题，还支持了 M1（Apple Silicon）的原生 ARM 指令集，建议所有 M1 用户升级以获得更好的性能。详见升级说明。</span></li> 
 <li style="text-align:justify"><span>升级 Android 工程 Gradle 版本到 4.2.2 版本，详见升级说明。</span></li> 
</ul> 
<p><span><strong><strong><span>Editor </span></strong></strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span>修复 Prefab 打开时点击保存，可能覆盖场景数据的问题</span></strong></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span>修复编辑器下刷新脚本时，若无场景切换操作则内存会持续增长的问题，感谢 isilent</span></strong></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span>修复重复构建部分文件 MD5 可能发生变化的问题</span></strong></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span>修复 2.4.5 出现的部分第三方插件 ui-section 内 header 使用 class 注册的语法不兼容的问题</span></strong></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span>调整构建时的资源压缩操作到拷贝构建模板和 `beforeFinish` 事件之后</span></strong></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复构建后修改脚本并绑定节点后再次构建，运行时绑定内容可能为空的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复资源管理器，搜索后键盘上下选择节点错误的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复在资源管理器全选 audio-clip、sprite-frame、texture 后拖动面板会报 resize 错误的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复聚焦场景后，选中节点无法删除的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复预制体自动同步弹窗状态无法保存的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复节点上 Color 等属性改动后，使用撤销和重置节点属性无效的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复资源路径或项目路径中带有括号时，打开编辑器出错的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复点击 Markdown 中的超链接失效的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复 Prefab 未修改保存后数据发生变化的问题</span></p> </li> 
</ul> 
<p><span><strong><strong><span>Engine</span></strong></strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span>修复预加载没有下载自动图集的图片的问题</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span><span>修复修改父节点后，节点的透明度级联计算错误的问题</span><span style="color:#0e88eb"> [#9322]</span></span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span><span>修复 Scroll View 同时到达水平和竖直边界时，没有正确触发事件的问题，感谢 </span><strong><span>zty8023ys</span></strong><span style="color:#0e88eb"> [#9445]</span></span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span><span>修复 Mask 组件在运行时调整节点大小无效的问题</span><span style="color:#0e88eb"> [#9444]</span></span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span><span>修复 Graphics Bezier 曲线的重绘问题，感谢<strong> caogtaa</strong></span><span style="color:#0e88eb"> [#9194]</span></span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span><span>修复 EditBox 在 PhoneNumber 模式下，鼠标滚轮导致数字为负数的情况，感谢 <strong>wanghaha1991</strong></span><span style="color:#0e88eb"> [#9138]</span></span></p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F4GETYsOlS1-2omLZsQfRHw" target="_blank">开发团队在发布公告写道</a>：</p> 
<blockquote> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>在 2.4.5 中，我们为了兼容 Mac M1 尽快升级了编辑器底层的 Electron，导致了开发者的部分插件出现异常，很抱歉给大家造成了不好的体验。<strong>针对有关问题，我们在近期进行了大量的专项测试，将兼容性适配代码集中汇总到了 2.4.7，最终为开发者抹平了 Electron 版本的差异，并且确保不会引入新的相关问题。</strong></span></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>在之后的版本中，不论是 2.x 还是 3.x，我们都将秉持兼容第一的原则，并且持续验证 Cocos Store 中的插件兼容性，尽可能在基础设施变化时不影响项目、插件的运行，减少适配成本，提升升级体验。</span></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>根据今年 2 月 7 日 3.0 版本正式发布时的计划，2.4 作为 LTS 版本将在今年继续提供缺陷修复。<strong>同时明年全年，我们还将持续关注 2.4 的关键问题和重大的平台适配问题，不定期更新版本，支撑线上项目的安全运营，请大家放心。</strong></span></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>再次集中解答一下关于 3.x 的升级问题：</span></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><strong><span>新项目不再建议基于 2.4，请统一使用 3.x 版本进行开发，</span></strong><span>我们会一如既往地优化 3.x 的开发体验，关注轻量级游戏的包体和效率，支撑好 2D、3D 等不同品类的游戏开发。</span></p> </li> 
  <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span><strong><span>当前 2.x 项目如果已到开发中期，或者即将上线，不必升级 3.x。</span></strong></span></p> </li> 
  <li> <p style="margin-left:8px; margin-right:8px; text-align:justify"><span><strong><span>当前 2.x 项目如果还在开发前期，可以评估是否需要升级 3.x。</span></strong><span>如果确认一定要升级，可以使用 Creator 提供的<strong> 2.x 资源导入工具</strong>。此工具将支持旧项目资源完美导入，以及代码的辅助导入。代码辅助导入会把 js 转换成 ts，添加组件类型声明、属性声明及函数声明，组件在场景中的引用都会得到保留，并且函数内部的代码会以注释的形式导入进来，可以减轻开发者的升级难度。详细的升级说明请参考</span><span style="color:#0e88eb">[升级指南]</span><span>。如果开发者们在升级中遇到困难，欢迎向我们反馈，我们会尽力协助。</span></span></p> </li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            