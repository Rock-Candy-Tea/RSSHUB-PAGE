
---
title: 'Visual Studio 2022 17.4 Preview 2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-418f049d1a00a30955bc6b105c85ecbb315.png'
author: 开源中国
comments: false
date: Tue, 20 Sep 2022 07:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-418f049d1a00a30955bc6b105c85ecbb315.png'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio 2022 17.4 上周<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvisual-studio-2022-17-4-preview-2%2F" target="_blank">发布</a>了第 2 个预览版。</p> 
<blockquote> 
 <p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvisualstudio.microsoft.com%2Fvs%2Fpreview%2F" target="_blank">https://visualstudio.microsoft.com/vs/preview/</a></p> 
</blockquote> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Fcontent%2Fidea%2F395028%2Fintroduce-the-ability-to-roll-back-a-visual-studio.html" target="_blank">引入回滚 Visual Studio 更新的功能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Fcontent%2Fidea%2F351156%2Fallow-multiple-git-repositories-to-be-active-at-on.html" target="_blank">允许多个 Git 存储库一次性处于活动状态</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Fcontent%2Fidea%2F744285%2Fadding-a-button-to-test-explorer-to-reset-the-test.html" target="_blank">向测试资源管理器添加按钮以将测试重置为“未运行”</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Fidea%2F793209%2Fcmake-weird-test-name-prefix.html" target="_blank">CMake 奇怪的测试名称前缀</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Fcontent%2Fidea%2F548880%2Fmovingmigrating-from-preview-channel-to-release-ch.html" target="_blank">从预览频道迁移到 Visual Studio 2019 安装发布通道</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Ft%2FArm64-support-for-Nodejs%2F10107705" target="_blank">对 Node.js的 Arm64 支持</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Fidea%2F485527%2Fc-android-development-gradle.html" target="_blank">C++ Android 开发 - gradle</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Ft%2FArm64-support-for-Visual-Studio-SDK%2F10107690" target="_blank">对 Visual Studio SDK 的 Arm64 支持</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Ft%2FFeedback-on-the-rollback-feature-introdu%2F10103571" target="_blank">VS 2022 版本 17.4 P1 中引入的回滚功能的反馈</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Ft%2FArm64-support-for-Game-Development-with-%2F10107702" target="_blank">使用 C++ 进行游戏开发的 Arm64 支持</a></li> 
</ul> 
<hr> 
<p><strong>F#</strong></p> 
<ul> 
 <li>我们继续改进 F# 标识符的工具提示，修复几个边缘情况： 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Ffsharp%2Fissues%2F13610" target="_blank">活动模式</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Ffsharp%2Fissues%2F13609" target="_blank">匿名记录字段</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Ffsharp%2Fissues%2F13593" target="_blank">异常名称</a></li> 
  </ul> </li> 
 <li>还修复了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Ffsharp%2Fissues%2F13549" target="_blank">Visual Studio 崩溃</a>，用于在<code>--version</code>编译器标志中指定</li> 
</ul> 
<p><strong>C++</strong></p> 
<ul> 
 <li>我们已使用 CMake 项目为 Visual Studio 添加了对 vcpkg 项目的支持。 对于包含 vcpkg 清单的项目，将在项目打开时自动激活环境。 可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fvsvcpkgenv" target="_blank">Visual Studio 博客文章中的 vcpkg 环境激活中</a>了解有关此操作的详细信息。</li> 
 <li>现在可以将开发容器用于 C++ 项目。 可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fvscppdevcontainer" target="_blank">适用于 C++ 的开发容器博客文章</a>中了解有关此功能的详细信息。</li> 
 <li>使 IntelliSense 遵循 PCH 时排除标头的顺序。 以前，当 PCH 通过且通过<code>/Yu</code>强制包含<code>/FI</code>时，IntelliSense 将始终先处理它，然后再处理通过<code>/FI</code>任何其他标头。 这与生成行为不匹配，因此按照指定的顺序处理此更改<code>/FI</code>标头。</li> 
 <li>从测试资源管理器中的 CTest 名称中删除了内部前缀。</li> 
 <li>将 Visual Studio 随附的 CMake 版本更新为 3.24.1 版。 有关可用内容，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcmake.org%2Fcmake%2Fhelp%2Flatest%2Frelease%2F3.24.html" target="_blank">CMake 发行说明</a>。</li> 
 <li>Android SDK 更新 
  <ul> 
   <li>已删除 Ant 脚本，因此用户将不再在“新建项目”对话框中看到基于 Ant 的模板。 有关从 Ant 模板迁移到 Gradle 模板的帮助，请参阅：从 Apache Ant (<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgradle.org" target="_blank">gradle.org</a>) 迁移生成</li> 
   <li>添加了对使用 NDK 23 和 24 构建的支持</li> 
   <li>已将 NDK 组件更新到 LTS 版本 23</li> 
  </ul> </li> 
 <li><code>ranges::min_element()</code>添加了 、<code>ranges::max_element()</code>和<code>ranges::minmax_element()</code></li> 
 <li>我们继续跟踪 C++ 标准化的最新开发，可通过在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fcpp%2Fbuild%2Freference%2Fcompiler-options%3Fview%3Dmsvc-170" target="_blank">编译器选项</a>中包含 /std：c++最新版来支持以下 C++ 23 功能 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwg21.link%2FP2302R4" target="_blank">P2302</a><code>ranges::contains</code>、<code>ranges::contains_subrange</code></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwg21.link%2FP2499R0" target="_blank">P2499</a><code>string_view</code>范围构造函数应为<code>explicit</code></li> 
  </ul> </li> 
</ul> 
<p><strong>音频提示</strong></p> 
<ul> 
 <li>在此预览版中添加了另外两个音频提示。 若要启用音频提示，请转到“工具 > 管理预览功能”，然后选中“为编辑器启用音频提示”。</li> 
 <li>当插入符到达在差异查看器中查看文件时添加或删除的行时，将播放这两个新的音频提示。 这些音频提示将添加到 17.3 中添加的错误、断点和警告音频提示。</li> 
</ul> 
<p><strong>Markdown</strong></p> 
<ul> 
 <li>我们已为 Visual Studio 添加了 markdown 编辑器的早期预览版。 若要启用 markdown 编辑器，请转到“工具 > 管理预览功能”，然后选中“Markdown 语言服务”选项。</li> 
 <li>启用该功能后，打开任何 .md 文件将在 Visual Studio 中打开新的 markdown 编辑器。 若要打开 markdown 的预览，编辑器右下角有一个“预览”按钮，) 行和列信息旁边 (。</li> 
 <li>这种体验是一个非常早期的预览版，我们期望其中的大部分内容会改变。 如果你有有关体验的反馈，请在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevelopercommunity.visualstudio.com%2Ft%2FFeedback-on-the-Preview-Markdown-Editing%2F10134757" target="_blank">开发者社区</a>加入此处的对话。</li> 
</ul> 
<p><strong>.NET 效率</strong></p> 
<ul> 
 <li>有一个新的内联重命名 UI，可用于重命名类型。 按_Ctrl_+<em>R</em>，_R_打开新的内联重命名体验。 请注意，新 UI 现在将显示在类型下，并带有重命名注释、字符串和符号文件的选项。</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-418f049d1a00a30955bc6b105c85ecbb315.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>现在有一个选项可以禁用 Source Link 和 Embedded 源。 可以在“工具>选项>文本编辑器 > C# > 高级”中禁用此功能，并取消选择“启用导航”以Source Link和嵌入源。</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2022/0920/071551_eGE1_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><strong>调试和诊断</strong></p> 
<ul> 
 <li>DataTable 可视化工具现已升级，在筛选、排序、导出和主题设置等方面进行了新改进。</li> 
 <li>若要导出 CSV/Excel 格式的数据导出，请使用右上角的下拉列表。</li> 
 <li>可视化工具还允许筛选基于所需筛选字符串的数据。 它将返回包含与筛选器字符串匹配的值的所有行。 还可以以 CSV/Excel 格式导出经筛选和排序的结果。</li> 
 <li>可视化工具窗口将按照所选 Visual Studio 主题进行主题设置。</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2022/0920/071644_7v9W_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvisual-studio-2022-17-4-preview-2%2F" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            