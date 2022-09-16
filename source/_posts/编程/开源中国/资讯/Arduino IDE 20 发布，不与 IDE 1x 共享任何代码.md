
---
title: 'Arduino IDE 2.0 发布，不与 IDE 1.x 共享任何代码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-949e3476f35fb1c96d63c236a40d498d5b3.png'
author: 开源中国
comments: false
date: Fri, 16 Sep 2022 07:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-949e3476f35fb1c96d63c236a40d498d5b3.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Arduino IDE 2.0 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.arduino.cc%2F2022%2F09%2F14%2Fits-here-please-welcome-arduino-ide-2-0%2F" target="_blank">发布</a>。Arduino IDE 2.x 是一次重大改写，不与 IDE 1.x 共享任何代码。它基于 Theia IDE 框架并使用 Electron 构建。编译和上传等后端操作被卸载到以守护程序模式运行的 arduino-cli 实例。官方表示，开发此新 IDE 的目的是保留与先前主要版本相同的界面和用户体验，以提供无摩擦升级。</span></p> 
<p><span style="color:#000000">Arduino IDE 2.0 带有一个现代化的编辑器，并通过响应式界面和更快的编译时间以提供更好的整体用户体验。除了核心功能外，IDE 2.0 还受益于许多增强功能和额外支持。Serial Monitor 和 Plotter 可以一起使用，使用户能够在其数据输出上拥有两个 viewports。以前用户必须在 text 和 graphs 之间进行选择，而现在可以两者兼得。</span></p> 
<p><span style="color:#000000">除了在使用 Arduino IDE 2.0 时提供更直观体验的更新用户界面外，速度也至关重要。语言服务器中的 Arduino 优化 code-completion 和 code-assist，可帮助用户快速编写代码并在键入时发现错误。开发团队根据大量的用户反馈识别出了其最薄弱的环节，例如 code assist 和 completion、串行输出、加载和编译时间。</span></p> 
<p><span style="color:#000000">具体更新内容如下：</span></p> 
<p><span style="color:#000000"><strong>sketch editing 时的自动完成</strong></span></p> 
<p><span style="color:#000000">在输入时，编辑器可以根据你的代码和你所包含的库建议自动完成变量和函数：</span></p> 
<p><span style="color:#000000"><img alt height="332" src="https://oscimg.oschina.net/oscnet/up-949e3476f35fb1c96d63c236a40d498d5b3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">右键单击变量或函数时，上下文菜单将提供导航快捷方式以跳转到声明它们的行（和文件）：</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><img alt height="361" src="https://oscimg.oschina.net/oscnet/up-17ddc96ba6e34d7a3eda680316e3008b31f.png" width="500" referrerpolicy="no-referrer"></span></p> 
<div style="margin-left:0; margin-right:0"> 
 <p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#000000"><strong>Dark 模式</strong></span></p> 
 <p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">可以快速更改设置并切换到 Dark 模式。和 Beta 期间的相比，整个 Dark 主题已经重新设计，变得更加一致、美观和易于观看<em>。</em> </span></p> 
</div> 
<p><span style="color:#000000"><img alt height="332" src="https://oscimg.oschina.net/oscnet/up-0c5dcced2d7fe93e1b0fc1b625e5c3b78fa.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#000000"><strong>永远不会丢失 sketch，将它们安全地保存在 Arduino 云端</strong></span></p> 
<p><span style="color:#000000">对于在多台电脑上工作或想把他们的 Sketches 安全地存储在云端的人来说，Remote Sketchbook 的集成是一个非常有用的功能。现在，你在 Arduino Cloud 和 Arduino Web Editor 中的所有 sketches 都可以在 IDE 2.0 中进行编辑。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><strong>Serial Plotter</strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">IDE 2.0 具有更丰富的 Serial Plotter，它是一种多功能工具，用于跟踪从 Arduino 板接收的不同数据和变量。Serial Plotter 是一个非常有用的可视化工具，可以帮助你更好地理解和比较数据点。它可用于测试和校准传感器、比较数值和其他类似场景。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-94f73f2d9697bc6268329fd60ba10328adb.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#000000">更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.arduino.cc%2F2022%2F09%2F14%2Fits-here-please-welcome-arduino-ide-2-0%2F" target="_blank">查看官方博客</a>。</span></p>
                                        </div>
                                      
</div>
            