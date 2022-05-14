
---
title: 'Godot 4.0 Alpha 8 发布，跨平台游戏引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9410'
author: 开源中国
comments: false
date: Sat, 14 May 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9410'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#000000"><span style="background-color:#ffffff">Godot 4.0 Alpha 8 现已发布，它包括在所有平台上明显的文本到语音支持（作为游戏/应用程序的功能，Godot editor 本身暂时没有使用它），以及重构模块/扩展的初始化级别，以允许第三方代码更灵活。</span></span></p> 
<p><span style="color:#000000">值得注意的是，在 Alpha 阶段的引擎仍然不完整也不够稳定，且与后续的 beta 版本会有较大的变化，建议谨慎使用。只有进入 Beta 阶段才会 “冻结功能”。</span></p> 
<p><span style="color:#000000">此更新中一些最值得注意的功能变化是：</span></p> 
<ul> 
 <li>Audio：在所有平台上实现文本到语音的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56192" target="_blank">GH-56192</a> )。</li> 
 <li>Buildsystem：将官方构建系统升级到更新的工具链（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fbuild-containers%2Fpull%2F104" target="_blank">build-containers#104</a>）： 
  <ul> 
   <li>Windows：MinGW GCC 11.2.1 和 binutils 2.37。</li> 
   <li>macOS/iOS：LLVM 14 - Edit<em>：</em>似乎 macOS 不喜欢 LLVM 14，它正在崩溃。</li> 
  </ul> </li> 
 <li>Core：使<code>&#123;call,set,notify&#125;_group()</code>默认为立即生效 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F51591" target="_blank">GH-51591</a> )。</li> 
 <li>Core：实现 placeholder assets  ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F60583" target="_blank">GH-60583</a> )。</li> 
 <li>Core：实现缺少的 Node & Resource placeholders ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F60597" target="_blank">GH-60597</a> )。</li> 
 <li>Core：打印时引用数组和字典中的字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F60609" target="_blank">GH-60609</a> )。</li> 
 <li>Core：重构模块初始化 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F60723" target="_blank">GH-60723</a> )。</li> 
 <li>Core：崩溃处理程序：使用<code>print_error</code>在日志中包含回溯（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F60782" target="_blank">GH-60782</a>）。</li> 
 <li>Editor：将复制 UID 选项添加到 filesystem dock ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F60707" target="_blank">GH-60707</a> )。</li> 
 <li>Export：改进嵌入式 PCK 加载和导出 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56093" target="_blank">GH-56093</a> )。</li> 
 <li>GUI：向 ProgressBar 添加更多填充模式 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F46208" target="_blank">GH-46208</a> ) 。</li> 
 <li>GUI：将 Skew 属性添加到 StyleBoxFlat ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F58599" target="_blank">GH-58599</a> )。</li> 
 <li>Linux：在单独的线程中读取和存储 joypad events ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F56125" target="_blank">GH-56125</a> )。</li> 
 <li>Rendering：向 ProceduralSkyMaterial 添加 dithering，以 combat banding ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F60070" target="_blank">GH-60070</a> )。</li> 
 <li><span style="color:#000000">Rendering：幕后的大量重构工作，在 OpenGL 3 上的工作正在进行中（尚不可用）</span></li> 
</ul> 
<p><span style="color:#000000">已知的问题：</span></p> 
<ul> 
 <li><span style="color:#000000">4.0 alpha 8 的 macOS 构建在苹果 M1 上崩溃，官方正在调查原因。在此期间，用户可以继续使用 4.0 alpha 7 正常工作。</span></li> 
 <li><span style="color:#000000">Editor：一个新的 macOS 编辑器二进制文件已经上传，应该可以正常工作。用于 ARM64 的导出模板可能仍有问题。</span></li> 
</ul> 
<p>发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fdev-snapshot-godot-4-0-alpha-8" target="_blank">https://godotengine.org/article/dev-snapshot-godot-4-0-alpha-8</a></p>
                                        </div>
                                      
</div>
            