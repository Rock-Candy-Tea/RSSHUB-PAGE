
---
title: 'PuTTY 0.77 发布，SSH_Telnet 程序'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6931'
author: 开源中国
comments: false
date: Tue, 31 May 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6931'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chiark.greenend.org.uk%2F%7Esgtatham%2Fputty%2F" target="_blank">PuTTY 0.77 现已发布</a>。PuTTY 是一款集成虚拟终端、系统控制台和网络文件传输为一体的自由开源程序。它支持多种网络协议，包括 SCP，SSH，Telnet，rlogin 和原始的套接字连接，它也可以连接到串行端口。其软件名字 “PuTTY” 并没有特殊含义。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">v0.77 是一个 feature release 版本。最重要的功能是改进了对代理的支持：原生支持通过另一个 SSH 服务器转发连接，以及在代理设置过程中，如果代理需要密码或其他登录信息，能够以交互方式提示。此外，还有许多错误的修复，一些加密技术的改进，以及一个新的应用程序 pterm.exe，包含一个 Windows command prompt。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">具体更新内容如下：</span></p> 
<ul> 
 <li>网络代理支持的重大改进： 
  <ul> 
   <li>如果代理服务器需要身份验证，支持以交互方式提示用户。</li> 
   <li>内置支持通过另一个 SSH 服务器进行代理，因此 PuTTY 将通过 SSH 连接到代理，然后通过它自动将端口转发到目标主机。（类似于运行<code>plink -nc</code>作为一个子进程，但设置起来更方便，并允许你回答代理呈现的交互式提示。）</li> 
   <li>与 HTTP 代理通信时支持 HTTP Digest 身份验证。</li> 
  </ul> </li> 
 <li>引入了 <code>pterm.exe</code>，一个类似 PuTTY 的包装程序，用于 Windows  command prompts（或在 Windows 控制台中运行的任何其他内容）。该程序尚未包含在安装程序中，但可作为下载页面中的<code>.exe</code>文件提供。</li> 
 <li>将 Unicode 和 bidi 支持更新到 Unicode 14.0.0。</li> 
 <li>新的命令行选项<code>-pwfile</code>， 与<code>-pw</code>类似，，只是它从文件中读取密码，这样就不会在命令行中显示出来。</li> 
 <li>Windows Pageant：选项<code>--openssh-config</code>允许与 Windows 的<code>ssh.exe</code>轻松地交互。</li> 
 <li><code>-pw</code>(和 <code>-pwfile</code>) 现在不会在提供的密码失败时退回到交互式提示密码。（这是初衷。）</li> 
 <li>键盘处理的新配置选项： 
  <ul> 
   <li>控制 Shift + 箭头键处理的选项</li> 
   <li>功能键选项中的额外模式，适用于现代 xterm（v216 及更高版本）。</li> 
  </ul> </li> 
 <li>在发送我们自己的 SSH 问候之前等待服务器的问候语的 Bug workaround flag，用于在看到任何传入数据之前丢失传出数据的服务器（或代理）。</li> 
 <li>Crypto update：在 probabilistic RSA key generation 中增加了 side-channel resistance。</li> 
 <li>Crypto update：不再使用短 Diffie-Hellman 指数（以防万一）。</li> 
 <li>错误修复：多次重新配置远程端口转发不再崩溃。</li> 
 <li>错误修复：Windows Pageant 现在可以处理大量并发连接而不会挂起或崩溃。</li> 
 <li>错误修复：如果同时启动 Windows Pageant 多次，实例应该可靠地同意其中一个作为持久服务器。</li> 
 <li>错误修复：window title 的远程控制更改现在根据配置的字符集进行解释。</li> 
 <li>错误修复：window title 的远程控制更改不再被编码包括字节 0x9C 的 UTF-8 字符混淆（在非 UTF-8 上下文中终止控制序列）。</li> 
 <li>错误修复：在拖动选择的过程中弹出窗口上下文菜单，现在不再使拖动处于卡住的状态。</li> 
 <li>错误修复：当 PSCP 报告服务器发送不允许的复合路径名时，它会正确报告它用于下载文件的替换名称。</li> 
 <li>对于开发人员：将构建系统迁移到 CMake，删除旧的 idiosyncratic<code>mkfiles.pl</code>和自动工具系统。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chiark.greenend.org.uk%2F%7Esgtatham%2Fputty%2Fchanges.html" target="_blank">https://www.chiark.greenend.org.uk/~sgtatham/putty/changes.html</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            