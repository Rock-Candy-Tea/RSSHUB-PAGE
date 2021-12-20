
---
title: '开源游戏引擎 Godot 3.4.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9879'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9879'
---

<div>   
<div class="content">
                                                                                            <p>Godot 3.4.1 现已发布，这是 3.4 稳定分支的第一个维护版本；是所有 Godot 3.4 用户的推荐升级版本。修复了一些问题（包括一些 3.4 回归），同时保留了与 3.4-stable 的兼容性。除了一般的 bug 修复外，它还提高了 Godot 与 Windows 11 的新 Windows 终端的兼容性，该终端无法从项目管理器中启动 Godot 编辑器。</p> 
<p>主要更新内容如下：</p> 
<ul> 
 <li>Android：修复<code>get_screen_orientation()</code>未返回有效值的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55210" target="_blank">GH-55210</a> )。</li> 
 <li>Android：添加配置以指定最小和目标 sdk 版本 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55735" target="_blank">GH-55735</a> )。</li> 
 <li>Android：添加对配置 XR 手部跟踪频率模式的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55768" target="_blank">GH-55768</a> )。</li> 
 <li>Camera2D：修复了“jump to limits”逻辑的条件（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55417" target="_blank">GH-55417</a>）。</li> 
 <li>Core：修复<code>Color.v</code>整数分配（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55963" target="_blank">GH-55963</a>）。</li> 
 <li>Editor：修复 Skeleton2D 编辑器中交换的静止姿势动作名称 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54851" target="_blank">GH-54851</a> ) 。</li> 
 <li>Editor：修复主题编辑器在单击元素选择器时的崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55186" target="_blank">GH-55186</a> )。</li> 
 <li>Editor：改进项目导出和 MeshLibrary 导出复选框 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55215" target="_blank">GH-55215</a> )。</li> 
 <li>GDScript：不要忽略 setter 函数中的类型不匹配（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54117" target="_blank">GH-54117</a>）。</li> 
 <li>GDScript：支持多行索引<code>[]</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54227" target="_blank">GH-54227</a>）。</li> 
 <li>HTML5：修复输入不聚焦画布，检查 Gamepad API 错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55111" target="_blank">GH-55111</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55342" target="_blank">GH-55342</a>）。</li> 
 <li>HTML5：修复多点触控输入处理 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55466" target="_blank">GH-55466</a> )。</li> 
 <li>HTML5：使用 JS lib/pre/externs 的绝对路径以与最新的 Emscripten 兼容 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55347" target="_blank">GH-55347</a> )。</li> 
 <li>Import：防止 OBJ 导入器打印误导性错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54694" target="_blank">GH-54694</a> )。</li> 
 <li>Input：添加<code>Input.is_physical_key_pressed()</code>方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55251" target="_blank">GH-55251</a>）。</li> 
 <li>iOS：捕获和显示<code>xcodebuild</code>输出（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54711" target="_blank">GH-54711</a>）。</li> 
 <li>LSP：防止 LSP 向非 GDScript 添加信号回调（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55624" target="_blank">GH-55624</a>）。</li> 
 <li>macOS：在使用多线程 VisualServer 时启用多线程 OpenGL 引擎标志( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54526" target="_blank">GH-54526</a> )。</li> 
 <li>macOS：以 16K 块读取和压缩项目文件，而不是一次读取整个文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54673" target="_blank">GH-54673</a> )。</li> 
 <li>Networking：修复响应中包含的 HTTP request headers（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F54683" target="_blank">GH-54683</a>）。</li> 
 <li>Particles：修复了在随机着色器变量中重复使用种子的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55607" target="_blank">GH-55607</a> ) 。</li> 
 <li>Viewport：即使在暂停或<code>time_scale</code>为 0 时也显示工具提示（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55224" target="_blank">GH-55224</a>）。</li> 
 <li>Windows：为 Windows 11 上的编辑器实例打开一个新的控制台窗口（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55925" target="_blank">GH-55925</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55967" target="_blank">GH-55967</a>）。 
  <ul> 
   <li>这是解决 Windows 11 的新 Windows 终端中的设计更改所必需的，该更改破坏了 Godot ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fissues%2F54076" target="_blank">GH-54076</a> )。</li> 
  </ul> </li> 
 <li>XR：添加对 OpenXR 导出配置的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F55158" target="_blank">GH-55158</a> )。</li> 
 <li>第三方库更新：libogg 1.3.5、libvorbis 1.3.7、minimp3 from 2021-11-30、CA certificates from 2021-11-01。</li> 
 <li>API 文档和翻译更新。</li> 
 <li>......</li> 
</ul> 
<p>更多详情可查看官方公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fmaintenance-release-godot-3-4-1" target="_blank">https://godotengine.org/article/maintenance-release-godot-3-4-1</a></p>
                                        </div>
                                      
</div>
            