
---
title: 'Visual Studio 2022 17.1 正式发布，生产力大增强！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-07f6638cb7da9969bf872a70a5f307f0556.gif'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 07:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-07f6638cb7da9969bf872a70a5f307f0556.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Visual Studio 2022 17.1 版本已正式发布，该版本包含大量增强生产力的更新项，小编结合微软的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvisual-studio-2022-17-1-is-now-available%2F" target="_blank">版本介绍博客</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fvisualstudio%2Freleases%2F2022%2Frelease-notes" target="_blank">版本发布页面</a>，摘取一些较为重要的更新项介绍一下：</span></p> 
<h2>文件索引查找功能，缩短代码搜索时间</h2> 
<p> Visual Studio 2022 17.1 默认启用文件中的索引查找，将代码搜索时间缩短至 1 秒左右。</p> 
<p>启用“在文件中查找”后，Visual Studio 将在加载或文件夹打开时启动附属进程“ServiceHub.IndexingService.exe”，然后将文件列表发送给它进行索引。然后，索引器将遍历文件并构建一个索引，当您执行查找操作时，该索引又用于加速搜索结果。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">VS 17.0（左）和 VS 17.1 （右）的搜索速度对比，在 1,560 个项目中搜索约 50,000 个文件：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="284" src="https://oscimg.oschina.net/oscnet/up-07f6638cb7da9969bf872a70a5f307f0556.gif" width="750" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">该功能默认开启，可在 <span style="background-color:#ffffff; color:#333333"><em>工具 > 选项 > 环境 > 预览功能</em> 中关闭。</span></p> 
<h2>代码/文件自动保存功能</h2> 
<p><span style="background-color:#ffffff; color:#333333">17.1 引入自动保存文件的新功能，每当 Visual Studio 失去焦点（例如在 Windows 中切换到另一个应用程序），它都会尝试保存 IDE 中的每个脏代码文档（dirty document），包括项目代码、解决方案以及其他杂项文件。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">可在</span><em>“工具”>“选项”>“环境”>“文档” </em>中设置开启或关闭该功能。</p> 
<p><img alt height="472" src="https://oscimg.oschina.net/oscnet/up-a29ae7d7971aaf7c71e9cc5faf0f42c7587.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>增强 Git 相关功能</h2> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333"><strong>分支比较功能</strong>，可以将当前分支与存储库中的其他分支进行比较，更轻松地处理拉取请求（PR）或删除分支。</span></li> 
</ul> 
<p><img alt height="277" src="https://oscimg.oschina.net/oscnet/up-aef0ea6d590e6f15848298adb7247beca7d.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="240" src="https://oscimg.oschina.net/oscnet/up-eb2b9e4b39bc21417f29f70e98e2cd11c81.png" width="700" referrerpolicy="no-referrer"></span></p> 
<ul> 
 <li>签出提交（Checkout comit）</li> 
</ul> 
<p>增强 Head 分离的能力，对代码审查和测试都有帮助。比如可以通过签出（可以理解为“分离”）最近的几个提交，进而回到之前的代码节点进行测试。</p> 
<p><img alt height="608" src="https://oscimg.oschina.net/oscnet/up-f2efad6e7bcbe3fe77ace2115186868356b.png" width="700" referrerpolicy="no-referrer"></p> 
<p><img alt height="383" src="https://oscimg.oschina.net/oscnet/up-2d4df7ad6600566f165f9cefba83f682553.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>需要注意：签出提交之后，你将处于分离的 HEAD 状态，意味着当前存储库的 HEAD 将<strong>直接指向提交</strong>而不是当前分支（可以理解成：相对于代码仓库的实际分支，当前的所有更改都属于离线状态）。因此，如果要保留你签出提交后的更改，请在退出分离的 HEAD 状态之前，创建一个新的分支来保存你更改的内容。</p> 
<p>有关“签出提交”功能和更多 Git 增强功能，可在<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fintroducing-new-git-features-to-visual-studio-2022%2F" target="_blank"> Taysser 的博客</a>中细阅。</p> 
<h2>嵌入式和 RTOS 的 C++ 增强功能</h2> 
<p><span style="background-color:#ffffff; color:#333333">嵌入式寄存器和 RTOS 线程引进了一些可视化功能，比如：</span></p> 
<ul> 
 <li>可以通过 <em>Debug > Windows > Embedded Registers </em>访问寄存器视图，它提供所有可用寄存器、它们映射的内存位置和值的视图。</li> 
</ul> 
<p><img alt height="295" src="https://oscimg.oschina.net/oscnet/up-e2d6eae09fd6dddce247494996ce9a83fe3.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>通过 <em>Debug > Windows > RTOS Objects </em>打开 RTOS Objects 窗口，可以查看系统中运行的线程及其上下文。</li> 
</ul> 
<p><img alt height="86" src="https://oscimg.oschina.net/oscnet/up-adec25e9a5a13cafac0332d7cbf52ec031b.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>改良方案过滤器（Solution Filters）</h2> 
<p>方案过滤器可以筛选加载的项目，比如你<span style="background-color:#ffffff; color:#333333">可以选择加载单个项目，或加载带有整个依赖关系树的项目。问题是添加新项目或依赖项发生变化时，依赖关系图和</span>方案过滤器<span style="background-color:#ffffff; color:#333333">就会过时，因此 Visual Studio 2022 17.1 引进了 “更新项目依赖项” 功能，该功能可以随时检查新的依赖项，把项目的依赖关系更新到最新状态。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="522" src="https://oscimg.oschina.net/oscnet/up-3c5ba3568332680b69b73eb52c6bc374b53.png" width="700" referrerpolicy="no-referrer"></span></p> 
<h2><strong>IDE</strong></h2> 
<ul> 
 <li>使用集成帐户管理体验添加 Github 自动曝光帐户 (需要启用 GitHub Enterprise 服务器帐户) 。</li> 
 <li>添加了切换颜色方案的功能，可以按文件扩展名或项目为你的标签着色。</li> 
 <li>添加了启用彩色标签时自定义标签颜色的功能。 在一个颜色标签上点击右键，选择“设置标签颜色”。</li> 
</ul> 
<h2><strong>.NET 生产力</strong></h2> 
<ul> 
 <li><strong>源文件导航功能</strong>，如果引用程序集具有嵌入的源代码或源链接，现在将嵌入的源代码和源链接显示为“转到定义”的一部分。这意味着可以导航到声明目标符号的原始源文件，将光标放在一个符号上，然后按 F12 即可导航到原始源文件。</li> 
</ul> 
<p><img alt height="423" src="https://oscimg.oschina.net/oscnet/up-505020ef13ef1f0c6fb8616d5e6b9b64a50.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#171717"><strong>新增“堆栈跟踪资源管理器”窗口</strong>，其中显示剪贴板中的堆栈跟踪，可以单击并直接导航到相关代码。 默认情况下，如果从解决方案复制一个堆栈跟踪，然后将焦点切换到“堆栈跟踪资源管理器”窗口，随即将自动显示该堆栈跟踪。 </span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#171717"><img alt height="371" src="https://oscimg.oschina.net/oscnet/up-ef99779650e21f19e550b6ad3e3940a51f7.gif" width="700" referrerpolicy="no-referrer"></span></p> 
<p><span style="background-color:#ffffff; color:#171717">若要打开“堆栈跟踪资源管理器”窗口，请转到“查看”>“其他窗口”，然后选择“堆栈跟踪资源管理器”。</span></p> 
<p> </p> 
<p>Visual Studio 2022 17.1 版本还包括其他更新内容，比如调试和诊断功能增强、安装和更新优化，可在发行页面查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fvisualstudio%2Freleases%2F2022%2Frelease-notes" target="_blank">完整的更新列表</a>。</p>
                                        </div>
                                      
</div>
            