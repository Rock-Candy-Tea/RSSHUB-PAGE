
---
title: 'ILSpy 7.1 发布，.NET 反编译工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9629'
author: 开源中国
comments: false
date: Tue, 01 Jun 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9629'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ILSppy 是一个开源的 .NET 反编译工具。目前，ILSpy 7.1 现已发布，具体更新内容如下：</p> 
<p><strong>General</strong></p> 
<ul> 
 <li>Roslyn 3.10 的调整模式检测</li> 
</ul> 
<p><strong>Cross-platform support</strong></p> 
<ul> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2417" target="_blank">#2417</a>：如果找不到有效的 ICU 包，ilspycmd 将崩溃</li> 
 <li>修复 Unix 系统上的 DotNetCorePathFinder：realpath 总是返回垃圾</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2358" target="_blank">#2358</a>：使用当前的 Path.DirectorySeparatorChar 而不是 hard-coded backslashes</li> 
</ul> 
<p><strong>Contributions</strong></p> 
<ul> 
 <li>支持 .NET 6 single-file bundles</li> 
 <li>添加了 .vsconfig</li> 
 <li>中文翻译更新</li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2406" target="_blank">#2406</a>：对于只有 getter 的 readonly 属性，将 readonly 移动到 property 而不是 getter</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2409" target="_blank">#2409</a>：Windows 标题栏的样式现在是可选的</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fcommit%2F6a34df5cd0ebb65e6d416eedc3937a19e3af87bc" target="_blank">6a34df5</a>：metadata explorer UI 的小错误修复</li> 
 <li>修复了 ReflectionDisassembler 中的源代码生成错误：包含多个连续点的标识符未正确转义</li> 
</ul> 
<p><strong>Bug fixes</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2392" target="_blank">#2392</a>：避免使用 ?: 运算符进行一些冗余转换</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2398" target="_blank">#2398</a>：TranslateCondition：必要时截断条件值</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2391" target="_blank">#2391</a>：将 null 传递给指针类型的参数时将方法标记为不安全</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2396" target="_blank">#2396</a>：将<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F1903" target="_blank">#1903</a>解决方法扩展到不受约束的泛型类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2389" target="_blank">#2389</a>：属性和事件中缺少 extern 关键字</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2395" target="_blank">#2395</a>：如果集合不是数组，则不要使用 for->foreach 转换</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2390" target="_blank">#2390</a>：添加对通用对象初始值设定项的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2390" target="_blank">#2390</a>：确保即使在 lambdas 中也删除所有未使用的捕获变量</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2407" target="_blank">#2407</a>：运算符“-”不能应用于“nuint”类型的操作数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fissues%2F2354" target="_blank">#2354</a>：对 nullable value types 的一元和二元运算符进行反编译</li> 
 <li>以及许多其他修复程序，有关完整列表，可单击<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Fcompare%2Fv7.0...v7.1-preview1" target="_blank">此处</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ficsharpcode%2FILSpy%2Freleases%2Ftag%2Fv7.1" target="_blank">https://github.com/icsharpcode/ILSpy/releases/tag/v7.1</a></p>
                                        </div>
                                      
</div>
            