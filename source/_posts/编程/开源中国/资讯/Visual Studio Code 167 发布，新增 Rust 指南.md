
---
title: 'Visual Studio Code 1.67 发布，新增 Rust 指南'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0506/075554_W0Cn_4937141.png'
author: 开源中国
comments: false
date: Fri, 06 May 2022 07:58:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0506/075554_W0Cn_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio Code 是一个开源的代码编辑器，支持 IntelliSense、调试、Git 和代码片断。可在 Windows、Linux 和 macOS 上下载使用。支持常见的脚本和编程语言，还可以通过安装扩展来获得更多语言和功能的支持。</p> 
<p>近日微软发布了 1.67 版本，一些关键的更新内容如下：</p> 
<h3>资源管理器文件嵌套：在源文件下嵌套生成的文件。</h3> 
<p><img alt height="410" src="https://static.oschina.net/uploads/space/2022/0506/075554_W0Cn_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>资源管理器现在支持根据文件名来嵌套相关文件。有几个设置可以控制这种行为： 
  <ul> 
   <li><code>explorer.fileNesting.enabled</code> ：控制文件嵌套是否被全面启用。它可以被设置为全局或特定工作区。</li> 
   <li><code>explorer.fileNesting.expand</code> ：控制嵌套的文件是否被默认展开。</li> 
   <li><code>explorer.fileNesting.pattern</code> ：控制文件的嵌套方式。默认配置为 TypeScript 和 JavaScript 项目提供了智能嵌套。</li> 
  </ul> </li> 
</ul> 
<h3>「设置」的编辑器过滤器：过滤器按钮会显示 @Modified 设置等搜索。</h3> 
<p><img alt height="218" src="https://static.oschina.net/uploads/space/2022/0506/075606_RhQh_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>「设置」的编辑器搜索控件现在在右侧包含一个漏斗按钮。点击该按钮会显示一个过滤器列表，你可以将其应用到搜索查询中，以便过滤结果。</li> 
</ul> 
<h3>括号对着色：现在默认启用括号对着色功能。</h3> 
<p><img alt height="211" src="https://static.oschina.net/uploads/space/2022/0506/075616_M8Qr_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>鉴于 1.60 版本中引入的新括号对着色功能获得了积极的反馈，1.67 版本默认启用了括号对着色功能。</li> 
 <li>可以通过设置 <code>"editor.bracketPairColorization.enabled": false</code>禁用括号对着色功能。</li> 
</ul> 
<h3>切换嵌套提示：使用 Ctrl+Alt 在编辑器中快速隐藏或显示嵌套提示。</h3> 
<ul> 
 <li>嵌套提示是在源代码中显示额外信息的一个好方法。然而，有时你只想看到实际的源代码。为了支持快速隐藏嵌套提示， <code>editor.inlayHints.enabled</code> 设置已经被改变：除了 <code>on</code> 和 <code>off</code>，还有 <code>onUnlessPressed</code> 和 <code>offUnlessPressed</code> 的值。 <code>on/offUnlessPressed</code> 值可以在按住 <code>Ctrl+Alt</code> 的时候隐藏或显示嵌套提示。</li> 
</ul> 
<p>如何使用：</p> 
<ul> 
 <li><code>on</code> - 嵌套提示被启用。</li> 
 <li><code>off</code> - 嵌套提示被禁用。</li> 
 <li><code>onUnlessPressed</code> - 用 Ctrl+Alt 显示和隐藏嵌套提示。</li> 
 <li><code>offUnlessPressed</code> - 用 Ctrl+Alt 隐藏和显示嵌套提示。</li> 
</ul> 
<h3>拖放创建 Markdown 链接：将文件拖入编辑器以创建 Markdown 链接。</h3> 
<p><img alt height="363" src="https://static.oschina.net/uploads/space/2022/0506/075628_zjGI_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>现在你可以通过将文件从 VS Code 的资源管理器中拖放到 Markdown 编辑器中来快速创建 Markdown 链接。按住 Shift 键，同时将文件拖到 Markdown 编辑器上，就可以把它放到编辑器里，并创建一个链接。</li> 
 <li>如果文件是图片，VS Code 会自动插入 Markdown 图片，否则就会添加一个普通的 Markdown 链接。</li> 
</ul> 
<h3>查找 Markdown 中的所有引用：快速查找所有对 header、文件、URL 的引用。</h3> 
<p><img alt height="431" src="https://static.oschina.net/uploads/space/2022/0506/075645_EAhf_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3>Java 扩展更新：现在支持嵌套提示和 lazy 变量解析</h3> 
<ul> 
 <li> <p>嵌套提示</p> 
  <ul> 
   <li> <p>包含在 Extension Pack for Java 中的 Java 语言服务现在支持嵌套提示（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Feditor%2Feditingevolved%23_inlay-hints" target="_blank">inlay hints</a>），以显示方法签名的参数名称。</p> <p><img alt height="420" src="https://static.oschina.net/uploads/space/2022/0506/075712_Z14Z_4937141.gif" width="700" referrerpolicy="no-referrer"></p> </li> 
   <li> <p>Java 参数名称嵌套提示有三种模式：</p> 
    <ul> 
     <li><code>literals</code> - 仅对字面参数启用参数名称提示（默认）。</li> 
     <li><code>all</code> - 对字面参数和非字面参数启用参数名称提示。</li> 
     <li><code>none</code> - 禁用参数名称提示。</li> 
    </ul> </li> 
  </ul> </li> 
 <li> <p>lazy 变量解析</p> <p><img alt height="525" src="https://static.oschina.net/uploads/space/2022/0506/075734_NuOn_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
  <ul> 
   <li>Debugger for Java 扩展现在支持 "lazy" 变量。这个功能让你推迟对变量的操作，直到你明确地展开调试器用户界面来查看它的值。</li> 
  </ul> </li> 
</ul> 
<h3>扩展作者的 UX 指南：VS Code 扩展的 UI 最佳实践指南</h3> 
<p><img alt height="331" src="https://static.oschina.net/uploads/space/2022/0506/075751_35m1_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>针对扩展作者的 UX 指南已经被重做，有了自己的目录，在这里你可以找到使用各种 VS Code 用户界面元素的最佳实践。特定主题讨论了推荐的注意事项，以便它们能够无缝集成到 VS Code 中。</li> 
</ul> 
<h3>新的 Rust 语言指南：了解如何在 VS Code 中使用 Rust 编程语言。</h3> 
<p><img alt height="226" src="https://static.oschina.net/uploads/space/2022/0506/075801_TPyY_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>在 Visual Studio Code 中，有一个新的 Rust 指南，详细介绍了在 VS Code 中设置和使用 Rust 编程语言以及 rust-analyzer 扩展。rust-analyzer 扩展包括丰富的语言功能，如代码补全、提示、重构、调试等。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_67" target="_blank">https://code.visualstudio.com/updates/v1_67</a></p>
                                        </div>
                                      
</div>
            