
---
title: 'Lapce 0.2.0 发布，Rust 编写的代码编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2c442ea762f2798e9fe8ed2c9d91063c823.png'
author: 开源中国
comments: false
date: Tue, 06 Sep 2022 07:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2c442ea762f2798e9fe8ed2c9d91063c823.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Lapce 是一个<span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>用 Rust 编写的快速且功能强大的代码编辑器。Lapce 0.2.0 现已发布，具体更新内容如下：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong>Features/Changes</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F776" target="_blank">#776</a>：实现了 error lens</li> 
</ul> 
<p><img height="84" src="https://oscimg.oschina.net/oscnet/up-2c442ea762f2798e9fe8ed2c9d91063c823.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F780" target="_blank">#780</a> : 为 packaging 添加 Fedora 规范</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F787" target="_blank">#787</a> : 将 LSP stderr output 添加到日志</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F809" target="_blank">#809</a> : 当插件描述太长时用省略号截断</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F805" target="_blank">#805</a> : 添加 goto 类型定义支持（可以跳转到变量所属类型的定义）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F800" target="_blank">#800</a> : 添加 alpine dev-container</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F806" target="_blank">#806</a> : 添加下一个/上一个选项卡命令和键绑定。（请注意，这是在选项卡中向左/向右移动，而不是到最后使用的选项卡）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2Fc5f1692ec7fdfe6f0bf54fe2cb8251959a36fc1b" target="_blank">c5f1692</a> : 使撤消更细化</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2F69e6b83c1710dce942e7737167604bc304c4b357" target="_blank">69e6b83</a>：修复绘画中的 alpha-depth 问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F821" target="_blank">#821</a>：显示 completion items 的文档。</li> 
</ul> 
<p><img height="116" src="https://oscimg.oschina.net/oscnet/up-1ae613c3dce082866c997dccc15692e2263.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F825" target="_blank">#825</a> : 添加光标闪烁间隔的配置选项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F836" target="_blank">#836</a> : 为 Julia 使用新的 highlighter 查询</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2Fbcd6ff762d59437b3cae12ad465d8dad61d950b7" target="_blank">bcd6ff7</a> : 标题更新</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2Fc3bcc13172e464905f90fcc8d9e3059f44d8d709" target="_blank">c3bcc13</a>：全屏修复。更改 Lapce 图标以更好地处理常见的配色方案。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F848" target="_blank">#848</a> : 将插件面板分成两部分，安装和卸载。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2F722c67883deb8d364bb626514d5f2114b740315c" target="_blank">722c678</a>：Linux 上的自定义标题栏和调色板栏</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F840" target="_blank">#840</a> : 关闭时保留未保存的文件，再次打开 Lapce 时将恢复这些文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F880" target="_blank">#880</a> : 添加启用、禁用和删除插件的功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F887" target="_blank">#887</a> : 不要绘制 tiny tab drags</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F905" target="_blank">#905</a> : 添加切换嵌套提示的命令</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F913" target="_blank">#913</a> : 添加 daily nightly 构建</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F916" target="_blank">#916</a>：空格键后不显示自动完成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F927" target="_blank">#927</a> : 使 completion/palette 允许向上/向下翻页键</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F895" target="_blank">#895</a> : 添加设置以控制调色板预览编辑器的宽度</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F937" target="_blank">#937</a>：在空格上退格后不显示自动完成</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F948" target="_blank">#948</a> : 添加调整编辑器/终端/各种拆分大小的功能</li> 
</ul> 
<p><img alt height="378" src="https://oscimg.oschina.net/oscnet/up-84f12bbe69b703cc94afa8e74b99cf8539b.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F972" target="_blank">#972</a>：自动更新</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F979" target="_blank">#979</a> : 添加 elixir 文件扩展名（以便它们可以被识别）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F807" target="_blank">#807</a> : 为 WGSL 添加语法高亮</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F903" target="_blank">#903</a> : 添加更多文件扩展名（以便可以识别它们）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F981" target="_blank">#981</a>：区分 stable/nightly/debug。这会将配置放在不同的文件夹中，具体取决于你的版本。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F990" target="_blank">#990</a>：重做标题栏</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F1010" target="_blank">#1010</a> : 添加调色板命令以打开各种 Lapce 目录</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F1009" target="_blank">#1009</a> : 添加 about dialog</li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2F8687b7d33b9f7a6fc33f4c9d012675c1f817098a" target="_blank">8687b7d</a>：添加重命名符号的功能</p> </li> 
</ul> 
<p style="text-align:start"><strong>Bug Fixes</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F781" target="_blank">#781</a> : 给插件面板一个滚动条</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F789" target="_blank">#789</a> : 在发送命令之前检查 LSP 功能。修复了大部分 Julia LSP 支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F788%2Ffiles" target="_blank">#788</a>：使用 FS 模块</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F831" target="_blank">#831</a> : 修复单个引用上的 goto ref</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2F1008682d285635fdc5ebb36c65eb99919740f9e4" target="_blank">1008682</a>：在文件更改时重新加载资源管理器，以防 watching code 未激活。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F849" target="_blank">#849</a> : (LSP) 指定  root uri 的工作区文件夹（如果可用）。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F850" target="_blank">#850</a> : 启动 LSP 时设置当前目录</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F884" target="_blank">#884</a> : 使用 UTF16 编码与 LSP 通信。这应该会修复一堆导致 RA 或编辑器崩溃的 unicode 错误。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2F474bb00d099bb222f50735d0fd0b0b7163567a05" target="_blank">474bb00</a>：修复 MacOS 选项键</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F930" target="_blank">#930</a> : 防止使用多个窗口保存时崩溃</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F843" target="_blank">#843</a> : 更好地遵循系统操作系统路径</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2Ffd74be8d7ff29265725013d158b85f1be7348292" target="_blank">fd74be8</a>：代理重写！这应该不会发生锁定，并且更容易添加。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fcommit%2F85e41dcc50aa1c36754b64c9709f268159dc5eca" target="_blank">85e41dc</a> : 查找框结果计数应使用当前缓冲区</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F996" target="_blank">#996</a> : 将 uname 作为多个 args 传递以修复 WSL</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F1011" target="_blank">#1011</a> : 将设置按钮大小与窗口控件对齐</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Fpull%2F1017" target="_blank">#1017</a> : 不要因缺少 primary monitor 而失败</li> 
 <li>各种其他错误修复</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flapce%2Flapce%2Freleases%2Ftag%2Fv0.2.0" target="_blank">https://github.com/lapce/lapce/releases/tag/v0.2.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            