
---
title: 'Visual Studio Code 1.70 发布，支持用作 Git 合并工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ba379879e68a96850b67ffb05fd8f5e70fa.png'
author: 开源中国
comments: false
date: Fri, 05 Aug 2022 07:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ba379879e68a96850b67ffb05fd8f5e70fa.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#333333">Visual Studio Code 1.70 现已</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70" target="_blank">发布</a>，<span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>一些主要亮点包括：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_easier-title-bar-customization" target="_blank">标题栏自定义</a></strong></li> 
</ul> 
<p>隐藏/显示菜单栏、命令中心或布局控制。</p> 
<p>对于使用自定义标题栏（Windows、macOS 和 Web 上的默认设置）的用户，该版本向标题栏引入更多交互式内容。虽然已经有单独隐藏这些元素的设置，但现在可以右键单击标题栏，以访问切换菜单栏（暂不支持 macOS）、命令中心和布局控件的上下文菜单。</p> 
<p><img alt height="366" src="https://oscimg.oschina.net/oscnet/up-ba379879e68a96850b67ffb05fd8f5e70fa.png" width="600" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_fold-selection" target="_blank">折叠选择</a></strong></li> 
</ul> 
<p>在编辑器中创建自己的折叠区域。</p> 
<p>之前官方尝试将菜单栏缩小为汉堡菜单，以腾出空间给命令中心。在听到用户反馈后，又切换回旧的菜单栏折叠行为：直到大部分菜单折叠才切换到汉堡菜单。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5b5f84005a0f762dbe211922ece9366a0cf.gif" width="600" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_search-multiple-selection" target="_blank">搜索多选</a></strong></li> 
</ul> 
<p>搜索视图现在支持多选，方便对多个搜索结果进行操作。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-fde4382c86b6859b67d8bc5c1ff3f9a5198.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_tree-find-control" target="_blank">树视图搜索和过滤</a></strong></li> 
</ul> 
<p>树视图例如文件资源管理器，现在支持查找控件。可以在树内按 Ctrl+F 以弹出 Find 控件。可以使用 Find 控件突出显示匹配的元素，或切换 Filter 按钮以隐藏所有与搜索词不匹配的元素。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-03a95c1a9479f5f7b9351d5f7a96cc54208.gif" width="500" referrerpolicy="no-referrer"><img alt src="https://oscimg.oschina.net/oscnet/up-f595c919d8d76c34af1a36445ccc4191541.gif" width="600" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_terminal" target="_blank">终端改进</a></strong></li> 
</ul> 
<p>默认情况下集成 Shell ，绑定扩展的 PowerShell 键。对于受支持的 shell 设置（大多数 bash/zsh/pwsh 配置），应该都可以正常工作而无需任何更改。</p> 
<p><img alt height="60" src="https://oscimg.oschina.net/oscnet/up-b5944b57e17dcc30e9af47fca4aca475de9.png" width="500" referrerpolicy="no-referrer"></p> 
<p><strong style="color:#444444">注意</strong>：在 Windows 上，需要 PowerShell 7 (pwsh) 来支持 shell 集成。</p> 
<p>其他扩展的 PowerShell 键绑定：</p> 
<ul> 
 <li><span><span><span><span style="color:#0072be"><span style="background-color:#f4f2f9">Ctrl+Space</span></span></span></span></span> - 默认为<code>MenuComplete</code>。(仅 Windows)</li> 
 <li><span><span><span><span style="color:#0072be"><span style="background-color:#f4f2f9">Alt+空格</span></span></span></span></span>- 默认为<code>SetMark</code>.</li> 
 <li><span><span><span><span style="color:#0072be"><span style="background-color:#f4f2f9">Shift+Enter</span></span></span></span></span> - 默认为<code>AddLine</code>.</li> 
 <li><span><span><span><span style="color:#0072be"><span style="background-color:#f4f2f9">Shift+End</span></span></span></span></span> - 默认为<code>SelectLine</code>.</li> 
 <li><span><span><span><span style="color:#0072be"><span style="background-color:#f4f2f9">Shift+Home</span></span></span></span></span> - 默认为<code>SelectBackwardsLine</code>.</li> 
</ul> 
<p> </p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_command-line-option-merge" target="_blank">命令行选项 --merge</a></strong> - 使用 3-way 合并编辑器作为默认合并工具。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>现在可以使用命令行选项在 VS Code 中调出合并编辑器：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code>-m --merge <path1> <path2> <base> <result> Perform a three-way merge by providing paths for two modified versions of a file, the common origin of both modified versions, and the output file to save merge results.</code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>这意味着<strong>可以将 VS Code 用作 Git 的合并工具</strong>，例如在以下位置进行配置<code>.gitconfig</code>：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code>[merge]
  tool = code-insiders
[mergetool "code-insiders"]
  cmd = code-insiders --wait --merge $REMOTE $LOCAL $BASE $MERGED</code></pre> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_go-to-most-recently-failed-cell" target="_blank">NoteBook：转到最近失败的单元格</a></strong>- 直接跳转到笔记本。</li> 
</ul> 
<p>有一个按钮可以跳转到运行失败的 NoteBook 单元格。也可以运行 Notebook: Go to Most Recent Failed Cell<strong style="color:#444444"> </strong>来执行相同的操作。</p> 
<p><img alt height="232" src="https://oscimg.oschina.net/oscnet/up-4ddd44c7c38dfd83c853610ae7154a1448f.gif" width="600" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_python" target="_blank">Python 入门体验</a></strong></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dms-python.python" target="_blank">Python</a> 扩展现在可以让用户在 VS Code 中快速安装和配置 Python。任何与解释器相关的提示仅在用户操作需要解释器时才显示，而不是在启动时显示。此外，UI 提示已得到改进，以更准确地显示错误和建议的更改。</p> 
<p><img alt height="357" src="https://oscimg.oschina.net/oscnet/up-e598bdb1bf20a6c155a625bc8a9392f3d64.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>自动调试配置</strong></p> 
<p>Python 扩展现在支持自动调试配置，可以分析当前项目并提供不需要额外修改的调试配置。</p> 
<p>该扩展识别 Django、Flask 和 FastApi 项目，以及简单的 Python 文件。</p> 
<p> </p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_editor-sticky-scroll" target="_blank">粘性滚动预览</a></strong>-</li> 
</ul> 
<p>新的滚动 UI 会显示当前源代码的范围，将显示编辑器顶部所在的类/接口/命名空间/函数/方法/构造函数。</p> 
<p>使用 <code>editor.experimental.stickyScroll.enabled</code>设置启用粘性滚动。</p> 
<p><img alt height="345" src="https://oscimg.oschina.net/oscnet/up-38183a5441ac55fe241fbf4542a5c1df903.gif" width="600" referrerpolicy="no-referrer"></p> 
<p> </p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_development-container-cli" target="_blank">开发容器 CLI 主题</a></strong></li> 
</ul> 
<p>开发容器命令行界面(CLI) 主题已针对 CLI 的最新版本进行了更新。开发容器 CLI 允许构建和运行开发容器，它是开发容器规范的开源参考实现</p> 
<p><img alt height="72" src="https://oscimg.oschina.net/oscnet/up-af1f6fcec6cc4c10bbd254573c2db179fe9.png" width="600" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>更多详情可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_70%23_development-container-cli" target="_blank">发布界面</a>中阅读。</p>
                                        </div>
                                      
</div>
            