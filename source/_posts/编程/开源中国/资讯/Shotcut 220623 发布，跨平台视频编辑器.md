
---
title: 'Shotcut 22.06.23 发布，跨平台视频编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f5256a26acfb3197b18fe6668b6258f0056.png'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 07:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f5256a26acfb3197b18fe6668b6258f0056.png'
---

<div>   
<div class="content">
                                                                                            <p>Shotcut 22.06.23 已经发布。Shotcut 是一款免费、开源、跨平台的视频编辑器，适用于 Windows、Mac 和 Linux。主要功能包括支持多种格式、本地时间线编辑且无需导入、支持输入和预览监视的 Blackmagic Design、支持 4k 分辨率。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<h4>Glaxnimate</h4> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Glaxnimate 是一个 2D 矢量绘图和动画程序，现在与 Shotcut 集成并捆绑在一起：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>添加了对读取 Lottie 和 rawr JSON 动画格式作为剪辑的支持。</li> 
 <li>添加了<strong> </strong><strong>Open Other > Animation </strong>以制作新的绘图或动画。</li> 
 <li>添加了<strong> </strong><strong>Mask: Draw (Glaxnimate) </strong>视频过滤器。</li> 
 <li>在 Glaxnimate 中预览 Shotcut timeline。</li> 
 <li>已知的问题： 
  <ul> 
   <li>由于资源不足，macOS 上的预览可能会停止工作，直到重新启动。</li> 
   <li>一些 Lottie 动画导致导出失败。已遇到问题有，在 Glaxnimate 中打开时会显示警告。</li> 
   <li>另可参阅 Glaxnimate 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fmattbas%2Fglaxnimate%2F-%2Fissues" target="_blank">bug tracker</a></li> 
  </ul> </li> 
 <li>教程视频： 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutu.be%2FZ2mRSpS3WWs" target="_blank">Animation as Clip</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutu.be%2FCaN98ub9vfg" target="_blank">Open Other > Animation</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutu.be%2FN4SQlOceFbI" target="_blank">Mask: Draw (Glaxnimate)</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutu.be%2FKUSY5nIeVHI" target="_blank">Shotcut-Glaxnimate Workflow</a></li> 
  </ul> </li> 
</ul> 
<h4><span><span><span><strong><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更多新东西</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></span></h4> 
<ul> 
 <li>添加了<strong> </strong><strong>Timeline > menu > More > Align To Reference Track </strong>以基于相似音频同步剪辑。可参阅其<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.shotcut.org%2Ft%2Falign-to-reference-track%2F33893" target="_blank">文档</a>。</li> 
</ul> 
<p><img height="206" src="https://oscimg.oschina.net/oscnet/up-f5256a26acfb3197b18fe6668b6258f0056.png" width="500" referrerpolicy="no-referrer"> </p> 
<ul> 
 <li>为以下音频过滤器添加了对 <strong>Keyframes </strong><strong>的支持：</strong> 
  <ul> 
   <li><strong>Low Pass</strong></li> 
   <li><strong>High Pass</strong></li> 
   <li><strong>Reverb</strong></li> 
  </ul> </li> 
 <li>添加了键盘快捷键 Ctrl+Alt+A 以选择当前轨道上的所有片段。（macOS 上为option+ command+A ）</li> 
 <li>为<strong> File > Export > Markers as Chapters </strong>添加了一个选项对话框，以排除颜色或包括范围标记。</li> 
 <li>将<strong> Edit... </strong>添加到 <strong>Timeline > Output > Properties</strong>。</li> 
 <li>在 Windows 上添加了对分数显示比例（125%、150%、175%）的支持。</li> 
</ul> 
<h4><span><span><span><strong><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></span></h4> 
<ul> 
 <li>修复<strong> </strong><strong>Text: Rich </strong>不会导出与 Windows 上具有分数显示比例的系统上的预览相同的内容。</li> 
 <li>修复了<strong> </strong><strong>Record Audio </strong>和<strong> </strong><strong>Open Other > Audio/Video Device </strong>在 macOS 上由于权限不足而崩溃的问题。</li> 
 <li>修复了<strong> </strong><strong>Time Remap > Image mode > Blend </strong>不起作用。</li> 
 <li>修复了在方形视频模式下将两个<strong>大小、位置和旋转</strong>过滤器与蒙版过滤器组合在一起的崩溃。</li> 
 <li>修复了奇数宽度视频可能导致的崩溃。</li> 
 <li>修复了在<strong> Timeline > Ripple </strong>打开的情况下将剪辑向左拖动超出其他剪辑的问题。</li> 
 <li>修复了更改颜色剪辑的颜色会重置自定义名称的问题。</li> 
 <li>修复了更改<strong> </strong><strong>Properties > Speed </strong>后，如果添加了 <strong>Crop: Source</strong> filter，则会丢失。</li> 
 <li>修复了将不可搜索的文件拖到 <strong>Playlist </strong>时提示持续时间并可能导致崩溃的问题。</li> 
 <li>修复了在改变属性后撤销时，剪辑上的过滤器被删除。</li> 
 <li>修复了<strong> </strong><strong>File > Export > Markers as Chapters </strong>不正确的文本编码导致 Unicode 字符损坏的问题。</li> 
 <li>修复了视频轨道混合可能会在移动轨道后中断。</li> 
 <li>修复了使用<strong> </strong><strong>Settings > Proxy > Use Proxy </strong> 来修复项目，将代理文件路径保存到修复的项目文件中。</li> 
 <li>修复了<strong> </strong><strong>Ripple Markers </strong>不适用于 ripple trimming 的问题。</li> 
 <li>修复了在时间线上修剪片段可能会改变相邻片段的长度。</li> 
</ul> 
<h4><span><span><span><strong><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>变化</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></span></h4> 
<ul> 
 <li>将构建系统从 qmake 转换为 CMake（已删除 qmake）。</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更多详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.shotcut.org%2Fblog%2Fnew-release-220623%2F" target="_blank">https://www.shotcut.org/blog/new-release-220623/</a></p>
                                        </div>
                                      
</div>
            