
---
title: 'Visual Studio Code 1.71 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fdaa98d01f9401f5dcc434f549830718a62.gif'
author: 开源中国
comments: false
date: Fri, 02 Sep 2022 07:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fdaa98d01f9401f5dcc434f549830718a62.gif'
---

<div>   
<div class="content">
                                                                                            <p>Visual Studio Code 1.71 现已发布，具体更新内容如下：</p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_merge-editor-improvements" target="_blank">合并编辑器改进</a></strong>- 文本和合并编辑器之间的转换更容易。</li> 
</ul> 
<p><img alt height="373" src="https://oscimg.oschina.net/oscnet/up-fdaa98d01f9401f5dcc434f549830718a62.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="375" src="https://oscimg.oschina.net/oscnet/up-5bbd9ffd0af0092c2f93359560eca72ee9f.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="374" src="https://oscimg.oschina.net/oscnet/up-b40083f010318f5f66e6f35f5477e2e7ea9.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_ffmpeg-codecs-support" target="_blank">扩展的编解码器支持</a></strong>- 帮助在 notebooks 和 webviews 中显示嵌入的音频和视频。</li> 
</ul> 
<p>作为 VS Code 一部分提供的 FFmpeg 共享库以前只支持<code>FLAC</code>编解码器。在此版本中，该库已更新为支持以下编解码器和容器列表：</p> 
<ol> 
 <li>Vorbis</li> 
 <li>Flac</li> 
 <li>H.264</li> 
 <li>VP8</li> 
 <li>WAV</li> 
 <li>MP3</li> 
 <li>Ogg</li> 
</ol> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-80434b151a86efe6b4de1bdad7f28bb2599.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_explorer-rename-selection-improvements" target="_blank">文件重命名选择</a></strong>- 按 F2 选择文件名、全名或文件扩展名。</li> 
</ul> 
<p><img alt height="287" src="https://oscimg.oschina.net/oscnet/up-d27bf056573a10faec9cb8a0101cddc343c.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_new-code-action-control" target="_blank">新的 Code Action UI</a></strong> - 快速找到你正在寻找的 Code Action。</li> 
</ul> 
<p>对 Code Action 控件进行了彻底的修改。现在不再是一个简单的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Feditor%2Frefactoring%23_code-actions-quick-fixes-and-refactorings" target="_blank">Code Actions 菜单</a>，而是有一个自定义控件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Feditor%2Frefactoring%23_code-actions-quick-fixes-and-refactorings" target="_blank">，可以更轻松地找到所需的 Code Action：</a></p> 
<p><img alt height="367" src="https://oscimg.oschina.net/oscnet/up-9ce8434c99901d3c9b344b4807201386f8f.png" width="500" referrerpolicy="no-referrer"></p> 
<p>新控件还允许 VS Code 显示附加信息。例如，你现在可以将鼠标悬停在禁用的 Code Action 上以了解它们被禁用的原因：</p> 
<p><img alt height="97" src="https://oscimg.oschina.net/oscnet/up-812f7fd9500fd4f302cfa79efb58c3a9326.png" width="300" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_terminal" target="_blank">终端更新</a></strong>- Fish 和 Git Bash 的 shell 集成，新的平滑滚动。 
  <ul> 
   <li><span style="background-color:#ffffff; color:#444444">对 shell 集成进行了改进</span></li> 
   <li><span style="background-color:#ffffff; color:#444444">终端现在支持平滑滚动，它会在短时间内动画滚动，以帮助n 在滚动后看到您的位置，类似于编辑器和列表。</span></li> 
   <li>现在使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsw.kovidgoyal.net%2Fkitty%2Funderlines%2F" target="_blank">kitty 终端首创</a>的转义序列支持下划线样式和颜色。</li> 
   <li><span style="background-color:#ffffff; color:#444444">对终端渲染进行了几项改进</span></li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#444444"><img alt height="143" src="https://oscimg.oschina.net/oscnet/up-c5029b6634ad735ac7381083dd961cefd93.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="background-color:#ffffff; color:#444444"><img alt height="23" src="https://oscimg.oschina.net/oscnet/up-2eca559f45700f0738b3b4eaee9dabf2d4b.png" width="200" referrerpolicy="no-referrer"></span></p> 
<p><img height="135" src="https://oscimg.oschina.net/oscnet/up-358efdf001d7171e993e30198e9cce216b4.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img height="83" src="https://oscimg.oschina.net/oscnet/up-cd75a3ab96735bffbb6856cea8e99268950.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img height="212" src="https://oscimg.oschina.net/oscnet/up-6ec59c2d86e790b1e5643770deba4bdd893.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img height="86" src="https://oscimg.oschina.net/oscnet/up-bb86d35078149d73940c4d1ec5dd6061f14.png" width="247" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_jupyter" target="_blank">Jupyter notebook 图像粘贴</a></strong>- 在 notebook Markdown 单元格中粘贴和预览图像文件。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dms-toolsai.jupyter" target="_blank">Jupyter</a> 扩展现在允许用户将屏幕截图或图像文件粘贴到他们笔记本中的 Markdown 单元格中。<span><span><span><span style="color:#444444"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>目前仅支持<code>image/png</code>mime 类型。要使用该功能，需添加/启用以下设置：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#a31515">"ipynb.experimental.pasteImages.enabled"</span><span style="color:#000000">: </span><span style="color:#0000ff">true</span>
<span style="color:#a31515">"editor.experimental.pasteActions.enabled"</span><span style="color:#000000">: </span><span style="color:#0000ff">true</span></code></pre> 
<p><img alt height="374" src="https://oscimg.oschina.net/oscnet/up-9fdae2b3fe88a36088ab85bc51a4b9f8ff9.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="321" src="https://oscimg.oschina.net/oscnet/up-616a7eced120a12f467b2e5ac8306daa407.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_typescript-livestreams" target="_blank">TypeScript 直播</a></strong>- 在 YouTube 上观看 TS“速成课程”或“提示和技巧”。</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_live-preview" target="_blank">Live Preview 扩展</a></strong>- Live Preview 现在支持 multi-root Web 项目。</li> 
</ul> 
<p><img alt height="269" src="https://oscimg.oschina.net/oscnet/up-488a84e25ee01b53c666b04932bd1623eac.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="168" src="https://oscimg.oschina.net/oscnet/up-6adaa6abb5d6ca3f4956962cf3321a78d72.png" width="300" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71%23_markdown-language-server" target="_blank">Markdown Language Server blog</a></strong>- 了解 Markdown 支持如何转移到语言服务器。</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更多详情可</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_71" target="_blank">查看官方公告</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            