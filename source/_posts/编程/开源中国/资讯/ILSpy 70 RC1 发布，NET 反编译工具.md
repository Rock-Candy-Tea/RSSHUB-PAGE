
---
title: 'ILSpy 7.0 RC1 发布，.NET 反编译工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2240'
author: 开源中国
comments: false
date: Sun, 11 Apr 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2240'
---

<div>   
<div class="content">
                                                                                            <p>ILSppy 是一个开源的 .NET 反编译工具。目前，ILSpy 7.0 RC1 现已发布，具体更新内容如下：</p> 
<h4>General</h4> 
<ul> 
 <li> <p>Dark 模式</p> </li> 
 <li>现在可以在 .NET 5 中构建 ILSpy（参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fblob%2Fmaster%2Fmultitargeting.props.template%23L3" target="_blank">multitargeting.props.template</a>）</li> 
 <li>在元数据中添加了 CustomDebugInformation table entries 的内联显示</li> 
 <li>为 blob、guid、string 和 user string heap 添加元数据树节点</li> 
</ul> 
<h4>Contributions</h4> 
<ul> 
 <li> <p>DataGrid 过滤器中的性能改进</p> </li> 
 <li>调整析构函数的适应度计算</li> 
 <li>重构插入搜索结果</li> 
 <li>在 Search MSDN 命令中使用正确的 URL 格式</li> 
 <li>Warning fixes</li> 
 <li>修复 ConnectionIdRewritePass</li> 
</ul> 
<h4>Bug fixes</h4> 
<ul> 
 <li>PDBGen：忽略重复的 ILFunction（参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fcommit%2F5a8b488e99415c1e1b5c2f44820be666c491b91a" target="_blank">5a8b488</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2314" target="_blank">＃2314</a>：当 WindowsDesktop.App 和 NETCore.App 中都存在 dll 时，ILSpy 会错误地解析运行时依赖项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1648" target="_blank">＃1648</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2133" target="_blank">＃2133</a>：对 KnownThings 使用简单的 assembly names，以允许解析器使用相对的框架版本。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2349" target="_blank">＃2349</a>：对 DynamicCompoundAssign 使用正确的 ExpressionType。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1512" target="_blank">＃1512</a>：XmlDocumentationProvider 无法加载某些 XML 文件中的特殊字符</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2342" target="_blank">＃2342</a>：请勿为 foreach 循环变量生成空名称。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2340" target="_blank">＃2340</a>：请勿在 AssemblyList.GetAllAssemblies() 中遍历有加载错误的 assemblies</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2356" target="_blank">＃2356</a>：如果在 Analyze 面板中切换语言，则无法导航。</li> 
 <li>改进了异步方法中 rethrow/throw 和 finally blocks 的反编译。（参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1749" target="_blank">＃1749</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2339" target="_blank">＃2339</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2353" target="_blank">＃2353</a>）</li> 
 <li>以及许多其他修复，有关完整列表，可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fcompare%2Fv7.0-preview3...v7.0-rc1" target="_blank">此处</a>。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Freleases%2Ftag%2Fv7.0-rc1" target="_blank">https://github.com/icsharpcode/ILSpy/releases/tag/v7.0-rc1</a></p>
                                        </div>
                                      
</div>
            