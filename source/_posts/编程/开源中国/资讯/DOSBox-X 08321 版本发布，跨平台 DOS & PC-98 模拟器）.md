
---
title: 'DOSBox-X 0.83.21 版本发布，跨平台 DOS & PC-98 模拟器）'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=116'
author: 开源中国
comments: false
date: Mon, 03 Jan 2022 07:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=116'
---

<div>   
<div class="content">
                                                                                            <p>最新版 DOSBox-X 0.83.21 现已正式发布！</p> 
<p>与原来专注于 DOS 游戏的 DOSBox 不同，DOSBox-X 正式打算涵盖不同类型的 DOS 软件，并实现硬件行为的准确模拟。所以除了DOS游戏外，DOSBox-X 正式支持模拟运行 Windows 3.x、9x 和 ME 的环境以及为这些版本的 Windows 编写的软件。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">新功能</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>支持在 shell 中查看 Unicode（UTF-8 或 UTF-16）文档</span></span></span></span></span></span></span></span>
  </div> DOSBox-X 现在支持 UTF8 和 UTF16 命令，允许转换 UTF-8 和 UTF-16 编码的文本以在当前代码页中查看，包括 SBCS 和 DBCS 代码页。例如，命令“UTF8 < UTF8TEXT.TXT”将在当前代码页中输出转换后的文本 UTF8TEXT.TXT，对于 UTF16 命令，有可选的 /BE & /LE 选项来指定字节序。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>支持用于调制解调器和零调制解调器仿真的 ENET 可靠 UDP</span></span></span></span></span></span></span></span>
  </div> 现在支持 ENET 可靠 UDP 作为调制解调器和零调制解调器仿真的选项。您可以使用“sock:1”选项为与串行端口 (COM1-COM9) 连接的调制解调器/空调制解调器启用它，例如“serial1=modem listenport:5000 sock:1”让 COM1 侦听端口 5000可靠的 ENET UDP ，而不是 TCP 连接。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>支持 NE2000 网络的 Slirp 后端的端口转发</span></span></span></span></span></span></span></span>
  </div> NE2000 网络功能的 Slirp 后端现在支持端口转发。[ethernet, slirp] 部分中有新的配置选项“tcp_port_forwards”和“udp_port_forwards”，用于 TCP 和 UDP 端口转发选项。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>支持查看或更改文件扩展名关联</span></span></span></span></span></span></span></span>
  </div> DOSBox-X 现在允许您定义命令或程序以使用 ASSOC 命令打开具有特定文件扩展名的文件，例如“assoc .txt=edit”在输入 .TXT 文件名时使用 EDIT 命令打开 .TXT 文件。 DOS 命令行。还支持通配符（* 或 ?）。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>支持 CONFIG 命令的更多特殊属性</span></span></span></span></span></span></span></span>
  </div> CONFIG 命令现在支持特殊属性，包括“cd”、“date”、“errorlevel”、“random”、“time”和“lastmount”，以便像“CONFIG -GET cd”和“CONFIG -GET errorlevel”这样的命令将得到当前 DOS 目录和 ERRORLEVEL 值。返回值也将保存到 %CONFIG% 变量。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>支持重新扫描内部虚拟驱动器 Z：</span></span></span></span></span></span></span></span>
  </div> 内部虚拟驱动器 Z: 现在可以像安装的本地驱动器一样重新扫描。对“drivez”目录或代码页的任何更改现在都将在 Z: 驱动器重新扫描后反映出来。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>支持提供用于在启动时启动程序的命令行选项</span></span></span></span></span></span></span></span>
  </div> 现在有一个命令行选项“-o”，如果指定程序在启动 DOSBox-X 时启动，它允许您提供命令行选项或参数，例如 dosbox-x program.exe - o“opt1 opt2”</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>大大改进了对中文/日文/韩文的 DBCS 支持</span></span></span></span></span></span></span></span>
  </div> DBCS 对中文/日文/韩文的支持在此版本中以各种方式进一步改进。例如，改进了对中文/日文/韩文的 IME 支持；支持位于 \\COMPUTER\FOLDER\FILEDOS 格式的 UNC 网络路径中的 DBCS 字符；ATTRIB、ECHO、TYPE、MORE 和 TRUENAME 等 DOS 命令现在可以更好地处理 DBCS 字符；现在还有一个用于 Big5-HKSCS 编码或 Big5 Unicode-At-On (Big5-UAO) 编码的隐藏代码页 951。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>改进了对 Windows for Workgroups 3.11 网络的支持</span></span></span></span></span></span></span></span>
  </div> 此版本中改进了对 Windows for Workgroups 3.11 网络的支持，以便您在从内部 DOS 外壳运行时可以充分利用 Windows for Workgroups 3.11 的网络功能。在从 shell 运行 WFW 3.11 之前，请务必执行命令“DEVICE IFSHLP.SYS”和“NET START”，以便其网络功能按预期工作。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>改进了对保存状态功能的支持</span></span></span></span></span></span></span></span>
  </div> 保存状态功能在此版本中得到了进一步改进，因此您可以期望保存和加载状态比以前更可靠地工作。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>改进的剪贴板复制和粘贴支持</span></span></span></span></span></span></span></span>
  </div> 剪贴板复制和粘贴已针对不同的代码页进行了改进，包括 DBCS 代码页（包括 PC-98 模式）中的框绘图字符。此外，对于 Toshiba J-3100 模式，当您尝试选择要复制的文本时，所选文本现在将突出显示。</li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><strong><span style="color:#373737">可用性改进</span></strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>更易于使用的配置工具</span></span></span></span></span></span></span></span>
  </div> 在此版本中，配置工具的可用性得到了显着改进。“...”按钮被添加到值数量有限的属性中，以便您可以在新对话框中选择一个值，而不是手动输入它们。此外，当从配置工具修改时，将立即应用更多设置。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>允许通过消息框强制缩放器</span></span></span></span></span></span></span></span>
  </div> 如果配置中指定的缩放器可能无法按预期工作并且如果没有强制，DOSBox-X 将显示一个消息框，询问是否加载缩放器，而不是总是默默地忽略它。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>允许在不打开调试器的情况下输入调试器命令</span></span></span></span></span></span></span></span>
  </div> “输入调试器命令”按钮被添加到“DOSBox-X 日志输出”和“代码概览”窗口（来自“调试”菜单”），用户可以直接输入调试器命令并查看结果，而无需打开调试器。此外，还添加了调试器命令 DATE 和 TIME 以查看或更改 DOSBox-X 的内部日期和时间。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>允许为无效的 DOS 命令自定义处理程序</span></span></span></span></span></span></span></span>
  </div> 现在，您可以通过 [dos] 部分中的配置选项“badcommandhandler”在 DOS shell 中显示错误消息“错误的命令或文件名”之前指定自定义错误处理程序。例如，当通过“startcmd=true”选项启用 START 命令时，设置“badcommandhandler=start”允许在主机系统中运行指定的命令。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>允许使用按键输入自动停止 Turbo 模式</span></span></span></span></span></span></span></span>
  </div> DOSBox-X 现在将在检测到键盘输入时停止 Turbo（快进）模式，以便您可以在默认情况下正确键入键。您可以通过 [cpu] 部分中的配置选项“stop turbo on key”更改此行为。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>允许在运行时更改大多数打印机选项</span></span></span></span></span></span></span></span>
  </div> 您现在可以使用 CONFIG -set 命令更改虚拟打印机配置的 [printer] 部分中的大多数配置选项，例如“CONFIG -set printoutput=png”将默认打印机输出设置为 PNG。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>允许在非 Windows 系统上完成 Bash-shell</span></span></span></span></span></span></span></span>
  </div> 对于 Linux 和 macOS 系统，此版本现在支持 DOSBox-X 命令行的 Bash-shell 补全。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>提高加载 Direct3D 像素着色器的灵活性</span></span></span></span></span></span></span></span>
  </div> 为了通过配置选项“pixelshader”设置 Direct3D 像素着色器，DOSBox-X 现在允许使用不带 .fx 扩展名的着色器文件名，或当前目录中的着色器文件。</li> 
 <li> 
  <div style="margin-left:0; margin-right:0">
   <span><span><span><span><span><span><span><span>能够显示或清除命令行历史记录</span></span></span></span></span></span></span></span>
  </div> 现在有一个 HISTORY 命令，它允许显示或清除内部 DOS shell 的命令行历史记录。命令历史通过 Tab 键影响文件完成功能的结果。</li> 
</ul> 
<p>完整更新项可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdosbox-x.com%2Frelease-0.83.21.html" target="_blank">更新公告中</a>查看。</p>
                                        </div>
                                      
</div>
            