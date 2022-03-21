
---
title: 'IntelliJ IDEA 2022.1 EAP 6：依赖分析器、UI_UX 更新...'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0321/074211_uC5c_5430600.png'
author: 开源中国
comments: false
date: Mon, 21 Mar 2022 07:47:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0321/074211_uC5c_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2022.1 Beta 之前的最后一个 EAP 版本现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F03%2Fintellij-idea-2022-1-eap-6%2F" target="_blank">已发布</a>，此版本包括<em><strong>依赖分析器（Dependency Analyzer）</strong></em>、重新设计的<em><strong>结构搜索和替换（Structural Search and Replace</strong> <strong>）</strong></em>对话框、对 <strong>Thymeleaf</strong> 的更好支持、一些 <strong>UI/UX 更新</strong>等内容。</p> 
<h3 style="margin-left:0px">构建工具</h3> 
<h4 style="margin-left:0px"><em>依赖分析器 </em></h4> 
<p style="margin-left:0px">为了促进依赖管理和冲突解决，IntelliJ IDEA 实现了<em>依赖分析器</em>，它提供有关项目和子项目中使用的所有依赖项（包括传递性依赖项）的广泛信息。</p> 
<p style="margin-left:0px">这个新功能允许轻松检测冲突的依赖关系并解决问题，比如可以过滤掉相同的依赖项，并查看它们在不同库中的存在，还可以快速浏览依赖项以正确构建配置。 </p> 
<p style="margin-left:0px"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074211_uC5c_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0px">用户体验 </h2> 
<h3 style="margin-left:0px">更新了 <em>结构搜索和替换 </em>对话框</h3> 
<p style="margin-left:0px">重新设计了<em>结构搜索和替换</em>对话框，提供所有模板的列表，以便更轻松地在它们之间导航。 </p> 
<p style="margin-left:0px"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074220_S9cT_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px">此外还在<em>结构搜索和替换</em>对话框的右上角添加了 <em><strong>Pin Dialog</strong> 图标，并将 <strong>Injected code </strong></em>和 <em><strong>Match case</strong> 复选框移至<strong>Search template</strong> </em>窗格的底部。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074247_rSY4_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">均匀拆分选项卡</h3> 
<p style="margin-left:0px">IntelliJ IDEA 2022.1 EAP 6 <span style="color:#27282c">可以在编辑器选项卡之间平均分配工作空间，使它们具有相同的宽度。</span></p> 
<p style="margin-left:0px"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074257_C9x6_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px"><em>新建项目</em>向导：更新的 Java 生成器</h3> 
<p style="margin-left:0px">作为 <em>新建项目 </em>向导 UI 改造的一部分，EAP 6 引入了一个新的工作流程来启动新的 Java 项目：</p> 
<p style="margin-left:0px"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074308_4RV5_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0px">框架和技术</h2> 
<h3 style="margin-left:0px">Thymeleaf 支持改进</h3> 
<p style="margin-left:0px"> IntelliJ IDEA 2022.1 改进了对 Thymeleaf 的支持，致力于减少误报检查的数量，并在编辑 Thymeleaf 模板时增强了 IDE 的性能。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074319_A4m6_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">Helidon 配置文件自动补全</h3> 
<p style="margin-left:0px">改进了 IntelliJ IDEA Ultimate 中对 Helidon 框架的支持，IDE 现在在属性文件和 <em>.yaml </em>文件中提供配置键补全，且支持<em><strong>Go to Declaration</strong> </em>和 <em><strong>Quick Doc</strong> </em>操作。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074327_y0NQ_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074420_NoUk_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="280" src="https://static.oschina.net/uploads/space/2022/0321/074431_vwrq_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>以上是 EAP 6 的重点更新内容，更多细节更新项请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FIDEA-A-140%2FIntelliJ-IDEA-2022.1-EAP-6-%28221.5080.9-build%29-Release-Notes" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            