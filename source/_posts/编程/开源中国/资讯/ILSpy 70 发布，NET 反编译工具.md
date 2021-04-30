
---
title: 'ILSpy 7.0 发布，.NET 反编译工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=852'
author: 开源中国
comments: false
date: Fri, 30 Apr 2021 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=852'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ILSppy 是一个开源的 .NET 反编译工具。目前，ILSpy 7.0 现已发布，具体更新内容如下：</p> 
<p><strong>New Language Features</strong></p> 
<ul> 
 <li>C# 9.0: record classes</li> 
 <li>C# 9.0: with expressions</li> 
 <li>C# 9.0: primary constructors</li> 
 <li>支持 .NET 5 的自定义调用约定</li> 
 <li>改进了对 Unsafe-intrinsics 的支持</li> 
</ul> 
<p><strong>UI Improvements</strong> </p> 
<ul> 
 <li>Dark 模式（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2347" target="_blank">＃2347</a>）</li> 
 <li>.NET bundles 和 Nuget packages 现在直接嵌入到树状视图中</li> 
 <li>在 NuGet packages 中启用了搜索</li> 
 <li>增加了在代码视图中高亮显示当前行的设置（参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2224" target="_blank">＃2224</a>）</li> 
 <li>简单的 UI 语言切换支持</li> 
</ul> 
<p><strong>General</strong> </p> 
<ul> 
 <li>支持 .NET bundles（参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2191" target="_blank">＃2191</a>）</li> 
 <li>检测 csc/deterministic 开关的使用情况</li> 
 <li>改进 assembly resolver API 以允许异步使用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2286" target="_blank">＃2286</a>：在 ILSpy 中启用服务器模式 GC</li> 
 <li>现在可以为 .NET 5 构建 ILSpy（参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fblob%2Fmaster%2Fmultitargeting.props.template%23L3" target="_blank">multitargeting.props.template</a>）</li> 
 <li>改进了项目/解决方案的反编译（参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2186" target="_blank">＃2186</a>）</li> 
 <li>更新了 ReadyToRun（参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2238" target="_blank">＃2238</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2279" target="_blank">＃2279</a>）</li> 
 <li>在元数据中添加了 CustomDebugInformation table entries 的内联显示</li> 
 <li>为 blob、guid、string 和 user string heap 添加元数据树节点</li> 
 <li>DataGrid filter 中的性能改进</li> 
 <li>调整 destructors 的适配性计算（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2344" target="_blank">＃2344</a>）</li> 
 <li>重构了 search results 的插入（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2335" target="_blank">＃2335</a>）</li> 
 <li>将依赖关系与 Roslyn 3.8.0 对齐，参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2173" target="_blank">＃2173</a>（影响 ICSharpCode.Decompiler NuGet package 用户）</li> 
 <li>删除了对 Humanizer 的依赖（参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2232" target="_blank">＃2232</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fpull%2F2235" target="_blank">＃2235</a>）</li> 
</ul> 
<p><strong>Bug 修复</strong> </p> 
<ul> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2192" target="_blank">＃2192</a>：添加对 VB.NET delegate construction 的支持</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1079">＃1079</a>：CSharpFormattingOptions.AutoPropertyFormatting 无效</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2222">＃2222</a>：switch-expression 不支持隐式转换</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2241">＃2241</a>：修复 TypeProvider.GetTypeFromReference 中可能存在的 NRE</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2233">＃2233</a>：ResourcesFileTreeNode 不再为 BAML 文件创建子节点</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2230">＃2230</a>：不直接发出连续的空传播运算符</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F603">＃603</a>：单元素数组不应跨越多行</li> 
 <li>修复了加载 DLLs 时，在其<code>.deps.json</code>中含有无效部分时的崩溃问题</li> 
 <li>PDBGen：忽略重复的 ILFunction（参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fcommit%2F5a8b488e99415c1e1b5c2f44820be666c491b91a">5a8b488</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2314">＃2314</a>：当 WindowsDesktop.App 和 NETCore.App 中都存在 dll 时，ILSpy 会错误地解析运行时依赖项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1648">＃1648</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2133">＃2133</a>：对 KnownThings 使用简单的 assembly names，以允许解析器使用相对的框架版本。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2349">＃2349</a>：对 DynamicCompoundAssign 使用正确的 ExpressionType。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1512">＃1512</a>：XmlDocumentationProvider 无法加载某些 XML 文件中的特殊字符</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2342">＃2342</a>：请勿为 foreach 循环变量生成空名称。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2340">＃2340</a>：请勿在 AssemblyList.GetAllAssemblies() 中遍历有加载错误的 assemblies</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2356">＃2356</a>：如果在 Analyze 面板中切换语言，则无法导航。</li> 
 <li>改进了异步方法中 rethrow/throw 和 finally blocks 的反编译。（参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1749">＃1749</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2339">＃2339</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2353">＃2353</a>）</li> 
 <li>......</li> 
</ul> 
<p>详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Freleases%2Ftag%2Fv7.0" target="_blank">https://github.com/icsharpcode/ILSpy/releases/tag/v7.0</a></p>
                                        </div>
                                      
</div>
            