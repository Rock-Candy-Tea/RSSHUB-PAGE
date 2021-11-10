
---
title: 'ILSpy 7.2 Preview 2 发布，.NET 反编译工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5971'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 06:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5971'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">ILSppy 是一个开源的 .NET 反编译工具。目前，ILSpy 7.2 Preview 2 现已发布，具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>New Language Features</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>C# 9.0 跳过 locals init</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Contributions</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>records 模式检测的各种改进（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2476" target="_blank">#2476</a>）</li> 
 <li>ILSpyCmd：添加了对单文件包的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2499" target="_blank">#2499</a>）</li> 
 <li>BAML 反编译器：添加缺失的<code>x:Static</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2536" target="_blank">#2536</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Visual Studio 插件</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">现在有一个 VS2022 的插件 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DSharpDevelopTeam.ILSpy2022" target="_blank">https://marketplace.visualstudio.com/items?itemName=SharpDevelopTeam.ILSpy2022</a>，它与<span style="color:#24292f">旧</span>插件是分开的。如果你在 VS2022 的预览版中安装了 ILSpy，需要卸载旧版本并安装这个新版本。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Enhancements</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>向反编译器添加了 ETW 检测以进行性能测量。</li> 
 <li>添加<code>DecompilerTypeSystem.CreateAsync</code>以允许异步初始化。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2522" target="_blank">#2522</a>：在搜索类型时支持完全限定名称中的 backticks</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2520" target="_blank">#2520</a> : 在深色主题中几乎看不到匹配的对</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2298" target="_blank">#2298</a>：允许通过滚动更改 DecompilerTextView 的字体大小。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2518" target="_blank">#2518</a>：资源文件中的“Other resources”部分未正确显示</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2534" target="_blank">#2534</a>：处理接口中属性和事件的默认实现</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2458" target="_blank">#2458</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2459" target="_blank">#2459</a>：修复了 C++/CLI 生成的 IL 代码中的各种正确性问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2530" target="_blank">#2530</a>：模式匹配检测中的稳定性修复</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2378" target="_blank">#2378</a>：解构检测中的稳定性修复</li> 
 <li>以及许多其他修复程序，有关完整列表，可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fcompare%2Fv7.2-preview1...v7.2-preview2" target="_blank">此处</a>。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Freleases%2Ftag%2Fv7.2-preview2" target="_blank">https://github.com/icsharpcode/ILSpy/releases/tag/v7.2-preview2</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            