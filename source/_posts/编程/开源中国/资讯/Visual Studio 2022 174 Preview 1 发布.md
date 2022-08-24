
---
title: 'Visual Studio 2022 17.4 Preview 1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-340a9b7d8eb5c92d0f34c4dfe3bb1c5d52b.png'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 07:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-340a9b7d8eb5c92d0f34c4dfe3bb1c5d52b.png'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio 2022 17.4 上周<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvisual-studio-2022-17-4-preview-1%2F" target="_blank">发布</a>了首个预览版 (Preview 1)。</p> 
<blockquote> 
 <p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvisualstudio.microsoft.com%2Fzh-hans%2Fvs%2Fpreview%2F" target="_blank">https://visualstudio.microsoft.com/zh-hans/vs/preview/</a></p> 
</blockquote> 
<p>在推出正式版之前，开发团队还会持续添加更多对 Arm64 的支持。</p> 
<p>官方表示，Visual Studio 2022 17.4 GA 将是<strong>首个正式原生支持 Arm64 架构的版本</strong>。此外，17.4 正式发布后会成为 LTSC 版本，在 2024 年 1 月 9 日之前都会获得支持。详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fvisualstudio%2Freleases%2F2022%2Fservicing-vs2022" target="_blank">Visual Studio 2022 的支持策略</a>。</p> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li><strong>原生支持 Arm 架构</strong></li> 
 <li><strong>移除不受支持的组件</strong></li> 
 <li><strong>引入回滚 Visual Studio 更新的功能</strong></li> 
 <li><strong>Visual Studio 管理员模板 (ADMX/ADML) 预览版反馈</strong></li> 
</ul> 
<hr> 
<p style="color:#171717; margin-left:0; margin-right:0; text-align:start"><strong>Arm64</strong></p> 
<p style="color:#171717; margin-left:0; margin-right:0; text-align:start">此预览版将继续在 Windows 11 上构建原生 Arm64 支持。 除了支持 .NET 桌面开发 (WinForms 和 WPF) ，还支持基于 MSBuild 的项目的 C++ (桌面开发) 和 ASP.NET 和 Web 开发，现在启用了<strong>通用 Windows 平台开发</strong>工作负荷。</p> 
<p style="color:#171717; margin-left:0; margin-right:0; text-align:start">详情查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fvs%2Farm64%2Fpreview" target="_blank">博客文章</a>。</p> 
<p><strong>F#</strong></p> 
<ul> 
 <li>本地函数的工具提示现在显示参数名称</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-340a9b7d8eb5c92d0f34c4dfe3bb1c5d52b.png" referrerpolicy="no-referrer"></p> 
<p><strong>C++</strong></p> 
<ul> 
 <li>添加了“创建声明/定义后导航”选项，允许你选择“创建声明/定义”功能的导航行为。 可以在查看 (默认) 或打开文档或无导航之间进行选择。</li> 
 <li>Visual Studio 的 Arm64 版本现在捆绑了 CMake 和 Ninja 的 Arm64 版本。</li> 
 <li>添加了对 CMake 预设版本 4 的支持。 有关可用内容的详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcmake.org%2Fcmake%2Fhelp%2Fv3.23%2Frelease%2F3.23.html%23id6" target="_blank">CMake 发行说明</a>。</li> 
 <li>使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fcpp%2Flinux%2Fconnect-to-your-remote-linux-computer%3Fview%3Dmsvc-170" target="_blank">连接管理器</a>连接到远程系统现在支持 SSH ProxyJump，该 SSH 代理Jump用于通过另一个 SSH 主机访问 SSH 主机 (，例如，访问防火墙后面的主机) 。</li> 
 <li>现在，可以使用 devcontainers 通过 CMake 跨平台 C++ 开发。 只需将 devcontainer.json 文件与项目一起使用即可启用该功能Visual Studio Code一样。 这目前仅限于使用 CMakeLists.txt 和 CMakePresets.json 配置的 C++ 项目。</li> 
 <li>添加了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcppblog%2Fvcpkg-artifacts%2F" target="_blank">vcpkg 项目的</a>集成。<code>vcpkg activate</code>如果<code>vcpkg-configuration.json</code>找到文件，则会在后台运行环境变量，并在新环境完成时加载环境变量。</li> 
 <li>我们继续跟踪 C++ 标准化的最新开发，可通过在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fcpp%2Fbuild%2Freference%2Fcompiler-options%3Fview%3Dmsvc-170" target="_blank">编译器选项</a>中包含 /std：c++最新版来支持以下 C++ 23 功能 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.open-std.org%2Fjtc1%2Fsc22%2Fwg21%2Fdocs%2Fpapers%2F2021%2Fp0849r8.html" target="_blank">P0849r8</a><code>auto(x)</code>：<code>decay-copy</code>语言 
    <ul> 
     <li>编译器部件尚未实现;最初实现范围时，库部件是在 C++20 模式下实现的。</li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.open-std.org%2Fjtc1%2Fsc22%2Fwg21%2Fdocs%2Fpapers%2F2020%2Fp0881r7.html" target="_blank">P0881R7</a><code><stacktrace></code></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.open-std.org%2Fjtc1%2Fsc22%2Fwg21%2Fdocs%2Fpapers%2F2021%2Fp2301r1.html" target="_blank">P2301R1</a><code>pmr</code>为<code>std::stacktrace</code></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.open-std.org%2Fjtc1%2Fsc22%2Fwg21%2Fdocs%2Fpapers%2F2021%2Fp1328r1.html" target="_blank">P1328R1</a><code>constexpr type_info::operator==()</code></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.open-std.org%2Fjtc1%2Fsc22%2Fwg21%2Fdocs%2Fpapers%2F2021%2Fp2440r1.html" target="_blank">P2440R1</a><code>ranges::iota</code>、<code>ranges::shift_left</code>、<code>ranges::shift_right</code></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.open-std.org%2Fjtc1%2Fsc22%2Fwg21%2Fdocs%2Fpapers%2F2022%2Fp2441r2.html" target="_blank">P2441R2</a><code>views::join_with</code></li> 
  </ul> </li> 
</ul> 
<p style="color:#171717; margin-left:0; margin-right:0; text-align:start"><strong>Git 工具</strong></p> 
<ul> 
 <li>引入了从解决方案资源管理器和 Git 更改工具窗口中取消跟踪和忽略跟踪的 Git 文件的功能</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2022/0823/160154_FfAf_2720166.gif" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>通过改进存储库状态和使用新的信任对话框，增强了信任单个和多个 Git 存储库的用户体验。 此增强功能解决了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2FUntrustedGitRepositories" target="_blank">最近的 Git 安全更新</a>，该更新要求用户信任不同用户拥有的存储库</li> 
 <li>Git 分支切换性能增强功能。 有关详细信息<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fvisualstudio%2Fvs2022-performance-enhancements-git-branch-switching%2F" target="_blank">，阅读 VS2022 性能增强功能：Git 分支切换博客</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fvisualstudio%2Freleases%2F2022%2Frelease-notes-preview" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            