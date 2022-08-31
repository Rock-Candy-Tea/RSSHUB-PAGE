
---
title: 'ReShade 5.4.0 发布，游戏视频画面自定义工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6555'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6555'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">ReShade 5.4.0 现已发布。ReShade 是一个开放源代码的后处理注入器，可以拦截游戏引擎从 CPU 发送到 GPU 的某些信息，并更改该数据，以整合用于改变最终游戏视觉效果的全新渲染技术。借助此应用程序，PC 游戏玩家可以轻松地将各种自定义处理模板添加到他们喜欢的视频游戏中，并添加新元素，例如抗锯齿，屏幕空间环境光遮挡，色差，景深效果，胶片颗粒，色彩校正，色彩后处理，多通道模糊以及许多视频游戏本身不支持的许多其他效果。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">具体更新内容如下：</span></p> 
<p><span style="color:#000000"><strong><span style="background-color:#ffffff">Features</span></strong></span></p> 
<ul> 
 <li>添加了可配置的预设键盘快捷键（右键单击 overlay 中的预设选择按钮以设置该预设的键盘快捷键）</li> 
 <li>添加了“Choose last clear operation with high number of draw calls”深度缓冲区检测选项（在 Source Engines 游戏中启用此选项，修复 Garry's Mod 中的深度缓冲区检测）</li> 
 <li>添加了附加 API 方法以启用/禁用所有效果并更改预设</li> 
 <li>添加了 ReShade 渲染的每种技术都会调用的“reshade_render_technique”附加事件</li> 
</ul> 
<p><strong><span style="color:#000000"><span style="background-color:#ffffff">Bug fixes</span></span></strong></p> 
<ul> 
 <li>修复了 Tony Hawk American Wasteland 的崩溃</li> 
 <li>修复了 vkQuake 中的崩溃</li> 
 <li>修复了 D3D9 运行时在内部使用 D3D9on12 时的崩溃</li> 
 <li>修复了 VKD3D 的崩溃问题</li> 
 <li>修复了 Jak Project 中的黑屏问题</li> 
 <li>修复了存在多个运行时实例时不保存的配置更改</li> 
 <li>修复了用于缩放鼠标位置的窗口大小在调整大小后不更新</li> 
 <li>修复了使用标量变量进行矩阵乘法的错误 SPIR-V 代码生成（修复了 Vulkan 下的 MotionEstimation.fx）</li> 
 <li>修复了 controller force feedback 在 Mafia 等 DirectInput 游戏中不起作用的问题</li> 
 <li>修复了不支持 OpenGL 4.5 的旧 OpenGL 驱动程序的潜在崩溃</li> 
 <li>修复了应用程序在 OpenGL 中创建的附加 API pipeline handles</li> 
 <li>再次修复了《DOOM Eternal》中的深度缓冲区检测（以及其他在不同队列中渲染和呈现的游戏）</li> 
</ul> 
<p><strong><span style="color:#000000"><span style="background-color:#ffffff">Miscellaneous</span></span></strong></p> 
<ul> 
 <li>添加了对“ID3D12Device11”和“ID3D12GraphicsCommandList8”接口的支持</li> 
 <li>在 D3D12 创建例程中添加了未知接口的警告日志消息</li> 
 <li>将“ID3D12PipelineLibrary”的 hooking 更改为使用 vtable hooking，并且仅在附加组件需要时挂钩</li> 
 <li>更改了效果文件搜索以跳过重复的搜索路径（当路径多次在搜索路径中时不再使用重复的技术）</li> 
 <li>更改了默认变量编辑器高度，以便在 VR 叠加中获得更好的可见性</li> 
 <li>默认情况下禁用生成的着色器代码中的行信息以减少效果缓存大小（因为没有文件路径添加到生成的代码中，这意味着它可以跨游戏重用；可以通过在 ReShade.ini 中将“NoDebugInfo”设置为 0 再次启用）</li> 
 <li>通过避免在插件不需要时注册资源/管道/...销毁回调来略微改善内存占用</li> 
 <li>删除了“ReShadeGUI.ini”，改为始终在主配置文件中保存窗口状态</li> 
</ul> 
<p><strong><span style="color:#000000"><span style="background-color:#ffffff">Setup tool</span></span></strong></p> 
<ul> 
 <li>将 txt 文件添加到预设选择文件扩展名过滤器</li> 
 <li>在兼容性列表中添加了对“DepthCopyAtClearIndex”的支持</li> 
 <li>修复了设置工具效果文件选择中下划线字符的显示</li> 
 <li>稍微改进了应用程序列表过滤以跳过常见的崩溃报告并更新 helper executables</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情可</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freshade.me%2Freleases%2F8216-5-4" target="_blank">查看发布说明</a><span style="background-color:#ffffff; color:#333333">。 </span> </p>
                                        </div>
                                      
</div>
            