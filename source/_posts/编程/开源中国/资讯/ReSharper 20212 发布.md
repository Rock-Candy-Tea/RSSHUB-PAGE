
---
title: 'ReSharper 2021.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1a7f29516ac1ef061f80c64f708a2ba026e.png'
author: 开源中国
comments: false
date: Wed, 04 Aug 2021 06:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1a7f29516ac1ef061f80c64f708a2ba026e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ReSharper 2021.2 现已发布，该版本更新了 C# 代码分析、可空引用类型和源生成器并引入 HttpClient URI 支持。该版本需要在计算机上安装 .NET Framework 4.7.2 或更高版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1a7f29516ac1ef061f80c64f708a2ba026e.png" referrerpolicy="no-referrer"></p> 
<h4>代码分析</h4> 
<ul> 
 <li>新的 Swap via deconstruction quick-fix 可用于交换变量值</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7ca5207b30d861699788c55836d7607b89a.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>带有相应快速修复的新检查：用 Array.Empty<T> 替换空数组创建，用 EventArgs.Empty 替换 new EventArgs()，用 Type.EmptyTypes 替换 Type[0]</li> 
 <li>ReSharper 反映了 .editorconfig 文件中的 generated_code 属性，允许指定在其代码分析中忽略哪些文件</li> 
 <li>代码分析在查找类似问题功能以及大型复杂的 switch 语句和 switch 表达式方面获得了一些性能改进</li> 
</ul> 
<h4>可空引用类型</h4> 
<ul> 
 <li>ReSharper 表示不再需要且可以安全移除抑制（!）</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f747e9d6823f917937e3a8e55de097cf56b.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>新的上下文操作允许在范围内搜索所有可为空的警告抑制</li> 
 <li>引入了一种新的重构来更改可空性，它将更新可空性注释并建议在整个代码库中传播更改。</li> 
 <li>当使用 JetBrains.Annotations 属性和可为空引用类型时，可以使用几个带有相应快速修复的新检查。将 JetBrains.Annotations 属性更新为 NRT 语法和编译器支持的属性</li> 
 <li>ReSharper 添加了新的检查和快速修复，以帮助使用编译器支持的注释，例如 [DisallowNull]、[AllowNull]、[MaybeNull] 和 [NotNull]</li> 
</ul> 
<h4>源码生成器支持</h4> 
<ul> 
 <li>对于生成的代码，警告和错误显示在编辑器和标记栏上</li> 
 <li>解决方案范围分析 (SWEA) 现在包括由源生成器生成的文件。如果项目中生成的文件中有错误，将能够立即看到它并导航到它</li> 
 <li>重构，如重命名或更改签名，现在可以从源生成的文件中触发</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-386f23ccc59558d00269e06ca780ae858f4.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>现在可以使用 Find Usages、搜索继承者以及使用 Ctrl+单击和导航到从生成的代码导航到手动编写的代码</li> 
 <li>启用语义突出显示，以便正确突出显示事件、字段和属性等类成员</li> 
 <li>在适当的地方显示所有镶嵌提示</li> 
 <li>调试时显示 ReSharper 自己的 DataTips</li> 
</ul> 
<h4>HttpClient URI 支持</h4> 
<ul> 
 <li>使用 HttpClient 时，代码完成将建议所有可以解析为使用 [Route]、[Http&#123;Method&#125;] 或 [AcceptVerbs] 属性注释的控制器中的操作的 URI</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f8746be8f05747498815c30b7f5f2145d22.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>可以使用 Go to Declaration 和 Find Usages 在控制器内部的路由属性和这些 URI 之间导航</li> 
 <li>重命名控制器中的属性路由会影响其在 URI 中的使用，可以直接从 URI 字符串重命名路由</li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fdotnet%2F2021%2F08%2F03%2Fresharper-2021-2-release%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            