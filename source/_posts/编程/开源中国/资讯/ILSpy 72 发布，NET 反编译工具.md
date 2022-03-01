
---
title: 'ILSpy 7.2 发布，.NET 反编译工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=450'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=450'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">ILSppy 是一个开源的 .NET 反编译工具。目前，ILSpy 7.2 现已发布，具体更新内容如下：</span></p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>New Language Features</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>C# 7.0 模式匹配</li> 
 <li>C# 8.0 <span style="background-color:#ffffff; color:#222222">嵌套表达式中</span>的 stackalloc</li> 
 <li>C# 9.0 跳过 locals init</li> 
 <li>C# 9 协变返回</li> 
 <li>C# 10 文件范围的<code>namespace</code>声明</li> 
 <li>C# 10<code>abstract static</code>接口成员</li> 
 <li>更新了 Roslyn 4.0 的模式检测</li> 
 <li>更新了 Mono C# 编译器 5.x 的模式检测</li> 
 <li>更新 Roslyn 3.11 的模式检测</li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start">Contributions</h4> 
<ul> 
 <li>引入基于 MSI 的安装程序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2558" target="_blank">#2558</a>）</li> 
 <li>ILSpyCmd：增加了对单文件包的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2499" target="_blank">#2499</a>）</li> 
 <li>支持加载压缩的 Xamarin 程序集（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2471" target="_blank">#2471</a>）</li> 
 <li><span style="background-color:#ffffff; color:#333333">BAML 反编译器：添加缺失的</span><code>x:Static</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2536" target="_blank">#2536</a>）</li> 
 <li><span style="background-color:#ffffff; color:#333333">records 模式检测的各种改进</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2476" target="_blank">#2476</a>）</li> 
 <li>将 TypeDefinitionDocuments 添加到自定义调试信息数据（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2578" target="_blank">#2578</a>）</li> 
 <li>修复<code>MainWindow.OpenLink</code>net6.0（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2585" target="_blank">#2585</a>）</li> 
 <li>修复加载嵌入为资源的图标标（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2595" target="_blank">#2595</a>）</li> 
 <li>使用 Trace.Listeners 而不是 Debug.Listeners（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2555" target="_blank">#2555</a>）</li> 
 <li>更新 ReadyToRun。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2489" target="_blank">#2489</a>）</li> 
 <li>Analyzers：仅返回有效模块（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2496" target="_blank">#2496</a>）</li> 
 <li>Extensibility：使 SearchTermMatches 虚拟化（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2494" target="_blank">#2494</a>）</li> 
 <li>修复<code>BamlDecompilerTypeSystem.HasType</code>中的 null check（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2509" target="_blank">#2509</a>）</li> 
 <li>更新了中文翻译（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2606" target="_blank">#2606</a>）</li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Enhancements</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>Assembly resolver：GetReferenceAssemblyPath 现在选择最接近的可用版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1175" target="_blank">#1175</a>：添加<code>inassembly:</code>和<code>innamespace:</code>搜索谓词</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2298" target="_blank">#2298</a> : 允许通过滚动更改 DecompilerTextView 的字体大小。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2404" target="_blank">#2404</a> : 切换 tabs 时缓存反编译结果</li> 
 <li>更好地支持语音命令/键盘导航</li> 
 <li>在<code>WholeProjectDecompiler</code>中正确支持 Windows 10 的长路径。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2608" target="_blank">#2608</a> : 支持子菜单项</li> 
 <li>添加了 metadata explorer tables 的超链接</li> 
 <li>为<code>XamlDecompiler</code>添加了简单的公共 API</li> 
 <li>改进了 LoadedAssembly.GetTargetFrameworkId、LoadedAssembly.GetRuntimePackAsync 等的性能</li> 
 <li>改进的窗口菜单</li> 
 <li>向 Analyzer 添加了“Copy results”菜单项</li> 
 <li>向反编译器添加了 ETW 检测以进行性能测量</li> 
 <li>添加<code>DecompilerTypeSystem.CreateAsync</code>以允许异步初始化</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2522" target="_blank">#2522</a> : <span style="background-color:#ffffff; color:#333333">在搜索类型时支持完全限定名称中的 backticks</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2520" target="_blank">#2520</a> : <span style="background-color:#ffffff; color:#333333">在深色主题中几乎看不到匹配的对</span></li> 
 <li>......</li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDirkster99%2FAvalonDock%2Fpull%2F324" target="_blank">Dirkster99/AvalonDock#324</a> Navigator window a11y 修复</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2579" target="_blank">#2579</a>：使用“ILSpyInstance”mutex 等待第一个 ILSpy 实例准备好接收<code>WM_COPYDATA</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2615" target="_blank">#2615</a> : 由于 fp 舍入错误，溢出检查无法可靠地工作</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2612" target="_blank">#2612</a> : 用 int.MaxValue 对 newarr 进行反编译会导致 OOME</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2533" target="_blank">#2533</a>：修复 pinned-region detection 中的各种错误修复。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2547" target="_blank">#2547</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2495" target="_blank">#2495</a>：改进了 VB.NET 十进制常量的反编译。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2545" target="_blank">#2545</a>：LINQ 不支持 null-forgiving 运算符，抑制转换。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2518" target="_blank">#2518</a> : <span style="background-color:#ffffff; color:#333333">资源文件中的“Other resources”部分未正确显示</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2534" target="_blank">#2534</a>：<span style="background-color:#ffffff; color:#333333">处理接口中属性和事件的默认实现</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2458" target="_blank">#2458</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2459" target="_blank">#2459</a>：<span style="background-color:#ffffff; color:#333333">修复了 C++/CLI 生成的 IL 代码中的各种正确性问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2530" target="_blank">#2530</a>：模式匹配检测中的稳定性修复</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2378" target="_blank">#2378</a>：解构检测中的稳定性修复</li> 
 <li>以及许多其他修复，完整列表可单击<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fcompare%2Fv7.1...v7.2" target="_blank">此处</a></li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>ilspycmd</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>删除了 .NET Core 2.1 TFM，添加了 .NET 6.0 TFM</li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Visual Studio 插件</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>允许在 project 和 package references 上打开 ILSpy</li> 
 <li>现在有一个 VS2022 的插件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DSharpDevelopTeam.ILSpy2022" target="_blank">https://marketplace.visualstudio.com/items?itemName=SharpDevelopTeam.ILSpy2022</a> 与旧插件分开。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Freleases%2Ftag%2Fv7.2" target="_blank">https://github.com/icsharpcode/ILSpy/releases/tag/v7.2</a></p>
                                        </div>
                                      
</div>
            