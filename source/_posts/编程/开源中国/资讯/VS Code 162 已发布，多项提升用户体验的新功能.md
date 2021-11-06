
---
title: 'VS Code 1.62 已发布，多项提升用户体验的新功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1106/074359_dNCJ_5430600.png'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 07:51:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1106/074359_dNCJ_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Visual Studio Code 1.62 版本发布了，此版本除了推出网页版 VS Code 以外，还更新了很多设置项来优化用户体验，包括参数提示高亮、新的快捷键、</span>Unicode 方式格式字符提示等，主要<span style="color:#333333">亮点内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"> 网页版 VS Code - vscode.dev（预览版）</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#444444">1.62 发布了 Visual Studio Code for the Web 的预览版，支持在浏览器直接运行 VS Code 。主要的编辑功能</span>网页版<span style="color:#444444">都支持，</span>不过少了很多扩展：像主题、片段或语法这种纯声明性的扩展可以在浏览器直接运行，需要运行代码的扩展必须由扩展的作者更新。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">参数提示高亮</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在会突出显示当前参数，可以通过<span> </span><code>editorHoverWidget.highlightForeground</code><span> </span>设置颜色</p> 
<p><img alt height="136" src="https://static.oschina.net/uploads/space/2021/1106/074359_dNCJ_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">改进支架对指引</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">水平线勾勒出括号对的范围，垂直线取决于括号对包围的代码缩进。</p> 
<p><br> <img alt height="280" src="https://static.oschina.net/uploads/space/2021/1106/074445_2coA_5430600.gif" width="350" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>可以通过设置<span> </span><code>editor.guides.bracketPairs</code><span> </span>为<span> </span><code>true</code>（默认为<code>false</code>）来启用支架对指引。</li> 
 <li>添加了第三个选项“<span> </span><code>active</code>”：仅显示活动括号对的指引。</li> 
 <li>新设置<span> </span><code>editor.guides.bracketPairsHorizontal</code><span> </span>可以控制是否、何时渲染水平参考线（默认为<code>active</code>）。</li> 
 <li>新的主题颜色<span> </span><code>editorBracketPairGuide.background&#123;1,...,6&#125;</code>，<code>editorBracketPairGuide.activeBackground&#123;1,...,6&#125;</code><span> </span>可用于自定义支架对指南的颜色。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">可定制的括号对</h3> 
<p><span style="background-color:#ffffff; color:#444444">现在可以为特定的编程语言配置括号对：</span></p> 
<p><span style="background-color:#ffffff; color:#444444"><img alt height="166" src="https://static.oschina.net/uploads/space/2021/1106/074520_tbrQ_5430600.png" width="700" referrerpolicy="no-referrer"></span></p> 
<p> </p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>editor.language.bracketPairs</code><span> </span>用于配置指定语言的括号字符。</li> 
 <li><code>editor.language.colorizedBracketPairs</code><span> </span>用于配置对应语言的支架对颜色。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">可以选择悬停的显示位置</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">现在可以选择<span> </span><span style="color:#444444">IntelliSense 悬停显示</span>在代码行的上面还是下面。设置<span> </span><code>editor.hover.above</code><span> </span>为<span> </span><code>false</code>，悬停将显示在当前行下方。<br> <img alt height="133" src="https://static.oschina.net/uploads/space/2021/1106/074618_L9co_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Unicode 方向格式字符</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">为了解决 Unicode  CVE-2021-42574 问题（关于此漏洞可以查看文章：<a href="https://www.oschina.net/news/167032/unicode-trojan-source-influenced-all-programming-language">Unicode 算法漏洞“Trojan Source”几乎影响所有编程语言</a>），<span style="color:#444444">VS Code 现在默认显示 Unicode 方向格式字符，比如：</span></p> 
<p><img alt height="72" src="https://static.oschina.net/uploads/space/2021/1106/074639_l46W_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#000000">上图包含两个明确的方向格式字符，</span><code>U+202E</code><span style="background-color:#ffffff; color:#000000">( 从右到左覆盖) 和</span><code>U+202C</code><span style="background-color:#ffffff; color:#000000">(<span> </span></span><code>POP DIRECTIONAL FORMATTING</code><span style="background-color:#ffffff; color:#000000">)。为了避免漏洞被利用，现在默认显示特殊的字符格式：</span></p> 
<p><img alt height="77" src="https://static.oschina.net/uploads/space/2021/1106/074656_b9Y2_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#000000">通过把<span> </span></span><code>editor.renderControlCharacters</code><span style="background-color:#ffffff; color:#000000"><span> </span>设置为<span> </span></span><code>false</code><span style="background-color:#ffffff; color:#000000">， 可以关闭特殊格式提示（默认设置是<span> </span></span><code>true</code><span style="background-color:#ffffff; color:#000000">）。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">扩展会显示是否经过验证</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#444444">VS Code 现在显示扩展发布者的域是否由 Visual Studio Marketplace 验证。</span></p> 
<p><img alt height="286" src="https://static.oschina.net/uploads/space/2021/1106/074805_Fqa4_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新的默认组合键</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">添加了几个其他编辑器支持的按键绑定：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>ctrl+shift+2</code>: 输入空字符 (<span> </span><code>0x00</code>)。</li> 
 <li><code>ctrl+shift+6</code>: 输入记录分隔符 (<span> </span><code>0x1E</code>)。</li> 
 <li><code>ctrl+/</code>: 输入单位分隔符 (<span> </span><code>0x1F</code>)。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">可以配置 HTML 属性的填充位置</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新设置<span> </span><code>html.completion.attributeDefaultValue</code>，可以选择写完 HTML 属性的时候填充值的位置：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>doublequotes</code>: 值放在双引号中（默认）</li> 
 <li><code>singlequotes</code>: 值放在单引号中</li> 
 <li><code>empty</code>: 值为空</li> 
</ul> 
<p><img alt height="223" src="https://static.oschina.net/uploads/space/2021/1106/074849_h7CM_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">文件备注支持使用表情符号</h3> 
<p><span style="background-color:#ffffff; color:#000000">如图：</span></p> 
<p><span style="background-color:#ffffff; color:#000000"><img alt height="301" src="https://static.oschina.net/uploads/space/2021/1106/074911_XDGG_5430600.png" width="600" referrerpolicy="no-referrer"></span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">查找和替换支持正则表达式</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#444444">notebook 编辑器的查找和替换组件现在支持用正则表达式抓取，如下图：</span></p> 
<p><img alt height="139" src="https://static.oschina.net/uploads/space/2021/1106/074933_oyVl_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">1.62 版本还包含其他更新内容，比如对</span><a href="https://www.oschina.net/news/167384/typescript-4-5-released"><span> </span>TypeScript 4.5<span> </span></a><span style="background-color:#ffffff; color:#000000">的支持、对 Electron 沙箱支持的进展等，详情可查看<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_62" target="_blank">VS Code 1.62 更新公告</a><span style="color:#000000">。</span></p>
                                        </div>
                                      
</div>
            