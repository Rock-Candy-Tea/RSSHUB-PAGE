
---
title: 'NuGet 6.3 发布，.NET 平台包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a76f4fcec9f16a844a37c7f219172e7c1ab.png'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 07:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a76f4fcec9f16a844a37c7f219172e7c1ab.png'
---

<div>   
<div class="content">
                                                                                            <p>NuGet 6.3 已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fnuget%2Frelease-notes%2Fnuget-6.3" target="_blank">发布</a>，NuGet 是 .NET 平台的包管理器，NuGet 客户端工具提供了生成和使用包的能力，可更好地管理项目中的包依赖、包更新等xi'xiang</p> 
<p>NuGet 6.3 在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvisualstudio.microsoft.com%2Fdownloads%2F" target="_blank">Visual Studio 2022</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload%2Fdotnet%2F6.0" target="_blank">.NET 6.0</a> 中开箱即用。也可以将 NuGet 6.3 作为独立的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdist.nuget.org%2Fwin-x86-commandline%2Fv6.3.0%2Fnuget.exe" target="_blank">可执行文件</a>下载，适用于 Windows、macOS 和 Linux。</p> 
<h2>亮点</h2> 
<p>NuGet 6.3 有许多新功能：</p> 
<ul> 
 <li><strong>NuGet 在指定重复的 PackageReference、PackageVersion 或 PackageDownload 项时发出警告 - <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNuGet%2FHome%2Fissues%2F9467" target="_blank">#9467 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNuGet%2FHome%2Fissues%2F9864" target="_blank">#9864</a></strong></li> 
 <li><strong>在 Visual Studio 中查看传递依赖项</strong></li> 
</ul> 
<p>现在有一个标记为“传递包”的新依赖部分，可以根据日常使用选择折叠或展开</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a76f4fcec9f16a844a37c7f219172e7c1ab.png" width="600" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>在 Visual Studio 中安装具有自定义浮动版本的包 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNuGet%2FHome%2Fissues%2F9829" target="_blank">#9829 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNuGet%2FHome%2Fissues%2F3788" target="_blank">#3788</a></strong></li> 
</ul> 
<p>可以使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fnuget%2Fconcepts%2Fpackage-versioning%23floating-version-resolutions" target="_blank">浮动版本语法</a>安装自定义版本的软件包。</p> 
<p><img alt height="318" src="https://oscimg.oschina.net/oscnet/up-75d23e385aeefac00aecd905c9f9d36d29f.gif" width="560" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>为 Linux 重新启用签名的 NuGet 包验证 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fcore%2Fissues%2F7688" target="_blank">#7688</a></strong></li> 
</ul> 
<p>从 Preview 7 开始，在 .NET 7 SDK Linux 版本中默认启用签名 NuGet 包验证。</p> 
<ul> 
 <li><strong>确保启用 HTTPS </strong></li> 
</ul> 
<p>引入了一个新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fnuget%2Freference%2Ferrors-and-warnings%2Fnu1803" target="_blank">NU1803 警告</a>，在使用非 HTTPS 来源时发出提醒。</p> 
<ul> 
 <li><strong>从 PackageReference 中的包中使用 pdb</strong></li> 
</ul> 
<p>对于来自 <PackageReference> 的 lib 和 runtime 文件夹下的任何给定程序集，如果它旁边的文件通过扩展名不同，NuGet 将在资产文件的目标部分中的程序集下方添加一个相关属性，列出这些文件的扩展名，用 ; 分隔。</p> 
<pre><code class="language-cs">"lib/netstandard2.0/Newtonsoft.Json.dll": &#123;
    "related": [".pdb", ".xml"]
&#125;</code></pre> 
<p>此功能允许 .NET SDK 使用 .pdb 和 .xml 文件以及 <PackageReference> 的程序集，用于调试和 API 文档等场景。</p> 
<p> </p> 
<p>更多内容可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fnuget%2Fannouncing-nuget-6-3-transitive-dependencies-floating-versions-and-re-enabling-signed-package-verification%2F" target="_blank">微软博客</a>中细阅。</p>
                                        </div>
                                      
</div>
            