
---
title: 'Visual Studio Code 1.65 已发布，支持多种 UI 布局'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0304/071857_Pk7T_5430600.gif'
author: 开源中国
comments: false
date: Fri, 04 Mar 2022 07:58:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0304/071857_Pk7T_5430600.gif'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio Code 1.65 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_65" target="_blank">现已发布</a>，该版本更新内容很多，下面摘录部分新特性作介绍：</p> 
<h2 style="text-align:start"><span style="background-color:#ffffff">工作台</span></h2> 
<h3>新的编辑器历史导航</h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff"><strong>编辑组感知导航</strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start">现在在编辑器历史中导航时会考虑编辑器组。在编辑器历史记录中来回导航将激活编辑器，并将其集中在那些编辑器组中。删除编辑器组时，所有关联的历史条目都将被丢弃。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff">在下面的动图中，第一个 <strong>Go Back </strong>将光标放在新的编辑器组中，然后第二个 <strong>Go Back </strong>导航返回到原始编辑器组。</span></p> 
<p><img alt height="378" src="https://static.oschina.net/uploads/space/2022/0304/071857_Pk7T_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>关于历史导航的新设置</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff">有一项新设置<code>workbench.editor.navigationScope</code>，可以将编辑器历史导航范围限定为活动编辑器组甚至编辑器。支持的值是：</span></p> 
<ul> 
 <li><code>default</code>：编辑器导航适用于所有打开的编辑器组和编辑器。</li> 
 <li><code>editorGroup</code>：编辑器导航仅限于活动编辑器组的已打开编辑器。</li> 
 <li><code>editor</code>：编辑器导航仅限于活动编辑器。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff">如果将范围配置为<code>editorGroup</code>或<code>editor</code>，则每个编辑器组或编辑器都将拥有自己的导航堆栈，可以单独导航。</span></p> 
<p><strong style="color:#444444">Notebook 支持</strong></p> 
<p>可以在任何 Notebook 中选择的单元格之间导航，导航可以跨编辑器工作。</p> 
<p><img alt height="378" src="https://static.oschina.net/uploads/space/2022/0304/072307_JN94_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">新的布局控制选项</span></h3> 
<p>在标题栏中引入了实验性<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_64%23_customize-layout-control" target="_blank">布局控件</a>（启用：通过设置<code>workbench.experimental.layoutControl.enabled</code>为<code>true</code>），通过 <span style="background-color:#f9f2f4">layoutControl.type</span> 设置，可选择对应的 UI 布局 ，此设置具有以下三个选项：</p> 
<ul> 
 <li><code>menu</code>: 旧版布局，可以打开菜单的单个按钮（默认）。</li> 
</ul> 
<ul> 
 <li><code>toggles</code>：新选项，显示三个按钮来切换主面板、侧边栏和侧面板。</li> 
</ul> 
<ul> 
 <li><code>both</code>：新选项，显示三个切换按钮的同时，也有菜单按钮。</li> 
</ul> 
<p>比如设置成 <code>both</code>，就是如下图所示，三个切换按钮加一个下拉菜单按钮：</p> 
<p><img alt height="330" src="https://static.oschina.net/uploads/space/2022/0304/072831_6Eg9_5430600.png" width="600" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">浅色高对比度主题</span></h3> 
<p><span style="background-color:#ffffff">添加了新的 Light High Contrast 主题（感觉对比度太高看起来有点累）</span></p> 
<p><img alt height="444" src="https://static.oschina.net/uploads/space/2022/0304/073104_FswI_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">音频提示</span></h3> 
<p>添加了新的音频提示，包括警告、内联建议和调试器断点点击的音频提示。此前的<code>audioCues.enabled</code>设置已被弃用，取而代之的是<code>audioCues.*</code>设置：</p> 
<p><img alt height="711" src="https://static.oschina.net/uploads/space/2022/0304/073251_ssbA_5430600.png" width="500" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff">新的音频提示命令 </span><strong style="color:#444444">Help: List Audio Cues </strong><strong style="color:#444444">，</strong>可查看所有可用的音频效果。</p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">拖放问题和搜索结果</span></h3> 
<p><span style="background-color:#ffffff">可以将问题、搜索或参考结果拖放到编辑器中，打开文件并显示结果位置。</span></p> 
<p><span style="background-color:#ffffff"><img alt height="397" src="https://static.oschina.net/uploads/space/2022/0304/073654_rQFf_5430600.gif" width="700" referrerpolicy="no-referrer"></span></p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">设置编辑器拆分视图</span></h3> 
<p><span style="background-color:#ffffff">使用可调整的拆分视图将目录与设置列表分开。</span></p> 
<p><span style="background-color:#ffffff"><img alt height="458" src="https://static.oschina.net/uploads/space/2022/0304/073735_crXR_5430600.gif" width="700" referrerpolicy="no-referrer"></span></p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">改进的自动语言检测</span></h3> 
<p>启用新设置<code>workbench.editor.historyBasedLanguageDetection</code>后，无标题编辑器将使用改进过的自动语言检测算法，该算法会考虑编辑器历史记录和当前工作区的内容，新算法只需少量文本输入即可提供检测结果。</p> 
<p><span style="background-color:#ffffff">下面是在 JavaScript、TypeScript、Markdown、Python、PHP 和 C++（支持更多语言）中使用新算法的示例：</span><br> <img alt height="460" src="https://static.oschina.net/uploads/space/2022/0304/073908_X8y4_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">改进的语言扩展建议</span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff">语言扩展推荐现在会在推荐时考虑扩展市场中其他突出的语言扩展。例如，如果安装了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DASF.apache-netbeans-java" target="_blank">Apache NetBeans Java</a> 扩展，VS Code 就不会推荐使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dvscjava.vscode-java-pack" target="_blank">Java 扩展包</a>。</span></p> 
<h3 style="text-align:start"><span style="background-color:#ffffff">扩展树悬停的键盘快捷键</span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff">可以使用键盘快捷键 <code>Ctrl/Cmd+K, Ctrl/Cmd+I</code></span>触发悬停，以显示在由扩展提供的自定义树视图中</p> 
<h2 style="text-align:start"><span style="background-color:#ffffff">编辑器</span></h2> 
<h3 style="text-align:start"><span style="background-color:#ffffff">片段环绕</span></h3> 
<p><span style="background-color:#ffffff; color:#2e3033">有一个新命令可以用代码片段包围当前选择：先</span>选择一些文本，从命令面板 ( <span><span><span><span style="color:#0072be"><span style="background-color:#f4f2f9">Ctrl+Shift+P</span></span></span></span></span> )调用<strong style="color:#444444">Surround With Snippet</strong>命令，然后从下拉列表中选择一个片段。<span style="background-color:#ffffff; color:#444444">在下面的动图中，一个选定的方法被一个 try/catch 片段包围。</span></p> 
<p><img alt height="396" src="https://static.oschina.net/uploads/space/2022/0304/074359_TIL6_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>上下文 Unicode 突出显示</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p><span style="background-color:#ffffff; color:#444444">在受信任的工作空间中，仅突出显示不可见或可能与 ASCII 字符混淆的字符</span></p> 
<p><span style="background-color:#ffffff; color:#444444">之前在 const 字符串中会看到多个误报：</span></p> 
<p><img alt height="287" src="https://static.oschina.net/uploads/space/2022/0304/074743_jY1x_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p>现在只会展示容易混淆的字符</p> 
<p><img alt height="289" src="https://static.oschina.net/uploads/space/2022/0304/074807_ZFX1_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>源代码管理</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h3 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>差异编辑器管理</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p><span style="background-color:#ffffff; color:#444444">命令面板中有一个新命令 </span><strong style="color:#444444">Git: Close All Diff Editors ，</strong>可用于关闭所有打开的差异编辑器。还有一个新设置<code>git.closeDiffOnOperation</code>可以在隐藏、提交、丢弃、暂存或取消暂存更改时自动关闭差异编辑器。</p> 
<h3 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Git 命令输出日志记录</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p>执行 Git 命令时，其内容<code>stderr</code>会记录在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Feditor%2Fversioncontrol%23_git-output-window" target="_blank">Git 输出窗口</a>中。有一个新设置 <code>git.commandsToLog</code>用于指定 Git 命令的列表，这些命令的内容将<code>stdout</code>记录在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Feditor%2Fversioncontrol%23_git-output-window" target="_blank">Git 输出窗口</a>中</p> 
<h2 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>调试</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h3 style="text-align:start"><span><span><span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>惰性变量</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p>VS Code 的通用调试器现在可以显示一个按钮，供用户按需获取变量值。这可用于支持新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_65%23_debugger-extension-authoring" target="_blank">“惰性”变量特性</a>的调试扩展。</p> 
<p><img alt height="495" src="https://static.oschina.net/uploads/space/2022/0304/075349_GO3L_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>此外，该版本还包含大量其他更新，比如对单门语言的更新，支持最新的 Typescript 4.6 等，详细内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_65" target="_blank">发布公告</a>中查看。</p>
                                        </div>
                                      
</div>
            