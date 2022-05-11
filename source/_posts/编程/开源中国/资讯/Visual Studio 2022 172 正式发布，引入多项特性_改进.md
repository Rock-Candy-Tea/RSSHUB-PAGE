
---
title: 'Visual Studio 2022 17.2 正式发布，引入多项特性_改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e7d2c407308b7cbfac286a8cd25787fb577.gif'
author: 开源中国
comments: false
date: Tue, 10 May 2022 23:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e7d2c407308b7cbfac286a8cd25787fb577.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Visual Studio 2022 v17.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvisual-studio-2022-17-2-is-now-available%2F" target="_blank">正式发布</a>了，此版本持续改进 C# 和 .NET 体验、新的 Git 性能和体验、针对 C++ 开发人员的更新以及用于本地开发和部署的新 Azure 工具。该版本共带来 400 多项改动，下面摘录部分重点特性作介绍：</p> 
<h2>源链接</h2> 
<p>如果引用的程序集提供了此信息，则嵌入式源和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fdotnet%2Fstandard%2Flibrary-guidance%2Fsourcelink" target="_blank">源链接</a>可作为“转到实现”的一部分，允许导航到实现目标符号的原始源文件。</p> 
<p>如下图所示，只需将光标放在符号上，然后按 CTRL + F12 即可导航到原始源文件。</p> 
<p><img alt height="486" src="https://oscimg.oschina.net/oscnet/up-e7d2c407308b7cbfac286a8cd25787fb577.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2>原始字符串</h2> 
<p>C# 11 新增了原始字符串（关于该特性可阅读过往文章：<a href="https://www.oschina.net/news/192315/csharp-11-preview-features-updates">原始字符串、Spans 模式匹配...C# 11 第二波新特性来啦！</a>），该版本的 VS 2022 引入了该特性。</p> 
<p>要使用原始字符串，请将项目文件中的语言版本设置为预览（使用）<LangVersion>preview</LangVersion>。然后将光标放在普通或逐字字符串上，按 CTRL + '.' 触发快速操作和重构菜单，并选择“转换为原始字符串”。</p> 
<p><img alt height="229" src="https://oscimg.oschina.net/oscnet/up-699769f18e693f53de870f68a571956366a.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">调试集合</h2> 
<p><span style="background-color:#ffffff; color:#333333">如果你定期调试 .NET 代码并希望检查大型且复杂的集合，VS 17.2 在 IEnumerable 对象类型的调试体验中引入了一个新的可视化工具，使你可以更轻松地查看此类数据，快速查看寻找的信息并能够快速导航。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="415" src="https://oscimg.oschina.net/oscnet/up-6ea6931d0fd5bcd52f550d4b692953dfbd9.gif" width="700" referrerpolicy="no-referrer"></span></p> 
<h2><span style="background-color:#ffffff; color:#333333">Razor 编辑器</span></h2> 
<p><span style="background-color:#ffffff; color:#333333"> Visual Studio 自 17.1 以来一直在提高新的 Razor 编辑体验的可靠性， 17.2 版本对编辑器添加了以下支持：</span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">能够折叠区域，以便于阅读和组织</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">新的 Razor 编辑器现在支持片段功能。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">使用 Shift + Alt + W 执行启用“wrap div”快捷方式</span></li> 
</ul> 
<h2><span style="background-color:#ffffff; color:#333333">ASP.NET Framework 的 Web 实时预览</span></h2> 
<p>Visual Studio 2022 的初始版本为使用 Web 窗体应用程序和设计器的用户引入了一项新功能。  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fdesign-your-web-forms-apps-with-web-live-preview-in-visual-studio-2022%2F" target="_blank">Web Live Preview</a> 功能使正在运行的应用程序成为设计界面，并提供跨源代码和 Web 界面的代码同步，以帮助直接导航到正在编辑的元素代码文件。</p> 
<p><img alt height="421" src="https://oscimg.oschina.net/oscnet/up-c712a8ae7d2b351a0658e199df0a54e4e14.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>此版本中进一步改进了功能体验，微软与几家 ASP.NET 控件供应商合作，以确保他们对这个新设计器进行支持。</p> 
<h2>Azure 优化</h2> 
<p>Visual Studio 2022 扩展了 Connected Services 中的功能，允许将容器用于已配置的 Azure 服务，从而提供本地调试体验。此支持已扩展为允许使用容器映像配置 Redis 缓存、MongoDB、RabbitMQ、存储、SQL 和 Cosmos DB 等区域。</p> 
<p><img alt height="491" src="https://oscimg.oschina.net/oscnet/up-013825cd1ea9f88a259737ef4d79658e554.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>C++ 优化</h2> 
<p>Visual Studio 中的 CMake 即将支持 C++20 模块！现在可以通过向编译器提供 /std:c++20 或 /std:c++latest 开关，并为 CMake （而不是 Ninja） 使用 MSBuild (Visual Studio) 生成器，来试用实验性支持。</p> 
<p>其他新功能包括内联提示，它在编辑器中提供函数参数名称和推导类型的指示符，可以通过按两次 ctrl 或 Alt + F1 来切换它。</p> 
<p><img alt height="184" src="https://oscimg.oschina.net/oscnet/up-83f58bd0c6ab1ff91ec3f3b8af98d5db014.png" width="500" referrerpolicy="no-referrer"></p> 
<p>此外，该版本还改进了<span style="background-color:#ffffff; color:#333333">外设寄存器和 RTOS 视图功能：</span></p> 
<ul> 
 <li>RTOS 工具窗口现在默认隐藏</li> 
 <li>当用户双击工具窗口中的 RTOS 对象时，它会为该对象添加一个监视。</li> 
 <li>当用户在 RTOS 工具窗口中选择堆栈指针开始/结束值时，它会在内存窗口中打开。</li> 
 <li>为调用堆栈窗口的设备目标添加了线程感知。</li> 
</ul> 
<h2>Git 工具优化</h2> 
<p>此版本集成了一个称为 Commit Graph（提交图） 的 Git 功能，能大幅减少加载 Commit 的时间。</p> 
<p><img height="394" src="https://static.oschina.net/uploads/space/2022/0416/083210_FDMR_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>有关该功能的详细介绍可看往期文章（<a href="https://www.oschina.net/news/191454/visual-studio-commit-graph-released" target="_blank">Visual Studio 集成 Commit Graph 功能，可提高 Git 操作性能</a>）</p> 
<p> </p> 
<p>更多内容可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvisual-studio-2022-17-2-is-now-available%2F" target="_blank">官方博客</a>。</p>
                                        </div>
                                      
</div>
            