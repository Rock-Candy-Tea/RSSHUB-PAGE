
---
title: 'Godot 3.4.3 发布，多平台游戏引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7809'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7809'
---

<div>   
<div class="content">
                                                                                            <p>Godot Engine 是一个功能丰富的跨平台游戏引擎，可以从一个统一的界面创建 2D 和 3D 游戏。它提供了一套全面的通用工具，因此用户可以专注于制作游戏。游戏可以一键导出到多个平台，包括主要的桌面平台（Linux、macOS、Windows）、移动平台（Android、iOS），以及基于 Web 的平台和游戏机。</p> 
<p>Godot 3.4.3 是一个维护版本，修复了许多问题，同时保持与以前的 3.4.x 版本的兼容性。</p> 
<ul> 
 <li>Android：修复了自定义构建的 Android 导出器上的相对密钥库路径</li> 
 <li>动画：将 <code>AnimationNodeOneShot::mix_mode</code> 作为一个属性公开</li> 
 <li>音频：修复 PitchShift 效果的质量下降并提高性能</li> 
 <li>C#：允许用命令行参数配置 Mono 调试器代理</li> 
 <li>C#：修复 <code>KeyValuePairAt</code> 内存泄漏</li> 
 <li>C#：修复重载脚本时获取属性状态</li> 
 <li>C#：修复通用 Godot 字典的 marshaling 值</li> 
 <li>C#: 修复 Android AAB 导出时无法加载本地 libs 的问题</li> 
 <li>C#: 在获取 <code>nativeName</code> 字段前附加 mono 线程，修复潜在的工具脚本崩溃</li> 
 <li>C#: 增加对将 Visual Studio 2022 作为外部编辑器打开的支持</li> 
 <li>Core: 修复变体解码中潜在的无限递归崩溃</li> 
 <li>Core: 修复解压时 UTF-8 文件名的解码问题</li> 
 <li>Core: 在节点复制时复制 load-as-placeholder 状态</li> 
 <li>Core: 在 <code>Expression</code> 解析器中添加十六进制和二进制字样支持，修复指数字样的解析</li> 
 <li>编辑器：修复 Input Map 中的撤销/重做操作</li> 
 <li>编辑器：提高在大项目上打开编辑器的性能</li> 
 <li>GDScript：重载脚本时清除待定功能状态</li> 
 <li>GDScript：重载脚本时清除待定功能状态</li> 
 <li>GDScript: 修正当 <code>is</code> 关键字针对 String 变量进行测试时的崩溃</li> 
 <li>网络：修复 HTTPRequest 对“content-length” 超过 2.1 GB 的请求的支持</li> 
 <li>API 文档和翻译更新</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Freleases" target="_blank">https://github.com/godotengine/godot/releases</a></p>
                                        </div>
                                      
</div>
            