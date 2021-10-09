
---
title: 'Delphi 11'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ce1acdf026ce0e08af463947cb07a7cbbee.png'
author: 开源中国
comments: false
date: Sat, 09 Oct 2021 07:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ce1acdf026ce0e08af463947cb07a7cbbee.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px; margin-right:0px; text-align:start"><span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c8c3bc; background-color:#ffffff; color:#333333">Delphi 11, C++Builder 11 和 RAD Studio 11</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.embarcadero.com%2Fannouncing-the-availability-of-rad-studio-11-alexandria%2F" target="_blank">已正式发布</a>，代号 "Alexandria"，新版本引入了许多重要的新特性和增强功能，改进了 IDE 的用户体验，旨在提升开发者的生产力。例如支持高分屏（4k+ 显示器）；支持 Windows 11、Android 30 API 和 macOS 64 位 ARM M1 处理器；引入 C++ <span data-darkreader-inline-bgcolor data-darkreader-inline-color style="--darkreader-inline-bgcolor:#181a1b; --darkreader-inline-color:#c1bcb4; background-color:#ffffff; color:#3d3d3d">格式化程序；增强的 Delphi 和 C++ 之间的跨语言支持；增强 FMX 设计器等。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-ce1acdf026ce0e08af463947cb07a7cbbee.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.embarcadero.com%2Fcn%2Fproducts%2Frad-studio%2Fstart-for-free" target="_blank">https://www.embarcadero.com/cn/products/rad-studio/start-for-free</a></p> 
<h3>IDE 新功能和增强功能</h3> 
<ul> 
 <li>支持高分屏，支持 4K 显示器，字体和图标的显示更清晰。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f6aed4b1ece6d69cc99ea3847fa616779c9.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>针对多窗口和多显示器显示的改进</li> 
 <li>完全重构的“欢迎界面”</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5e4f5480dab7883bf2f9fb3840cef8f158b.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>新增 C++ 代码格式化程序</li> 
 <li>改进对 VCL 和 IDE 的远程桌面支持</li> 
</ul> 
<h3>目标平台和编译器</h3> 
<ul> 
 <li>新增 Delphi macOS 64 位 ARM 编译器和工具链，包括为 Intel/Arm AppStore 提交构建通用二进制文件</li> 
 <li>Delphi 语言支持二进制小数和数字分隔符</li> 
 <li>改进 C++ 工具链，对 C++ 类型进行了全面的 Delphi 风格 RTTI 改进，包括在 Delphi 风格类型上使用 typeid</li> 
 <li>改进 Delphi 类型的 C++ 风格 RTTI</li> 
 <li>改进 CMake 质量，以及大幅度优化 Win32 和 Win64 上的异常处理</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-81cbb4c631a5e658df8c39ad3aaa3bbd6c9.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">使用 LSP 增强 <span>Delphi Code Insight 功能</span></h2> 
<ul> 
 <li><span><span>.pas 文件中使用的包含 (.inc) 文件的 LSP 感知</span></span></li> 
 <li><span><span>LSP 服务器支持自动重启</span></span></li> 
 <li><span><span>支持使用 Tab 键自动补全代码</span></span></li> 
 <li><span><span>支持 </span></span>Class helper</li> 
 <li><span><span>指派数组时提供建议</span></span></li> 
 <li><span><span>支持使用 Visual Studio Code 来编辑 Delphi 源代码以及完整代码补全</span></span></li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cf22454fe831d4184689b860eda1de672bb.png" referrerpolicy="no-referrer"></p> 
<h3>数据连接</h3> 
<ul> 
 <li>新版本中的 FireDAC 为 PostgreSQL、Oracle 和 Firebird 数据库提供了特定的改进</li> 
 <li>HTTP 和 REST 客户端库对超时机制进行了扩展，支持 HTTP/2、TLS 1.3、Base64 URL 编码</li> 
 <li> <p>新组件 TRESTRequestDataSetAdapter 简化了将数据集上传到 RAD 服务器的操作</p> </li> 
</ul> 
<p>相关 Demo 演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FEmbarcadero%2FRADStudio11Demos" target="_blank">https://github.com/Embarcadero/RADStudio11Demos</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.embarcadero.com%2Fannouncing-the-availability-of-rad-studio-11-alexandria%2F" target="_blank">详情查看发布公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            