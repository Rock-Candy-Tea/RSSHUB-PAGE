
---
title: 'Git for Windows 2.36.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9712'
author: 开源中国
comments: false
date: Wed, 11 May 2022 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9712'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Git for Windows 2.36.1 现已发布，主要更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Upcoming breaking changes</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">官方计划在 Git for Windows 2.36.0 发布后不久，将其中的 bash 更新到 5.1 版本（目前是 4.4）。建议用户先检查自己的 shell 脚本是否有潜在的兼容性问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Git for Windows 2.36.0 发布后不久，Git for Windows 也将停止支持 Windows Vista。大约在 2023 年初，继<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.msys2.org%2Fdocs%2Fwindows_support%2F" target="_blank">Cygwin 和 MSYS2</a> 之后，Git for Windows 将放弃对 Windows 7 和 Windows 8 的支持。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>New Features</strong></p> 
<ul> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit%2Fgit%2Fblob%2Fv2.36.1%2FDocumentation%2FRelNotes%2F2.36.1.txt" target="_blank">Git v2.36.1</a>。</li> 
 <li>在较新的 Windows 版本上，Git <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3751" target="_blank">现在假定是一个具有全彩功能的 Win32 控制台</a>。例如，当 NeoVIM 被配置为 Git 的编辑器时，这将有所帮助。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssh.com%2Ftxt%2Frelease-9.0" target="_blank">OpenSSH v9.0p1</a>。</li> 
 <li>当<code>git clean</code>由于路径长而失败时，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3817" target="_blank">Git 现在建议用户设置<code>core.longPaths</code></a>.</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.haxx.se%2Fchanges.html%237_83_0" target="_blank">cURL v7.83.0</a>。</li> 
 <li>Git Credential Manager 的二进制文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F406" target="_blank">不再与 core Git 自己的 dashed programs 安装在同一位置</a>。这更清楚地将 core Git 可执行文件与第三方提供的 Git 可执行文件区分开来。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FGitCredentialManager%2Fgit-credential-manager%2Freleases%2Ftag%2Fv2.0.696" target="_blank">Git Credential Manager Core v2.0.696</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fnews%2Fopenssl-1.1.1-notes.html" target="_blank">OpenSSL v1.1.1o</a>。</li> 
 <li>随附基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcygwin.com%2Fpipermail%2Fcygwin-announce%2F2022-January%2F010438.html" target="_blank">Cygwin 3.3.4</a> 的 MSYS2 运行时（Windows 版本的 Git）的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fmsys2-runtime%2Fcommit%2Fd72d5e8aeb7df99c55bdc438fb71fdeffd2bd1e5" target="_blank">patch level 4</a>。</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2FMSYS2-packages%2Fcommit%2F002b641e4409ce76709419e835e1fb2a6de14e7c" target="_blank">修复</a>了 Git for Windows v2.36.0 中引入的回归，即 32 位版本的 GPG 根本无法工作。</li> 
 <li><code>proxy-lookup</code>helper <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3818" target="_blank">只报告了 proxy 的第一个字母</a>，已修复。</li> 
 <li>安装程序在提供 Git Credential Manager（GCM）选项之前，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F329" target="_blank">现在会先验证 .NET Framework 4.7.2 是否可用</a>（因为 GCM 需要它才能工作）。</li> 
 <li>修复了 v2.36.0 中引入的错误，其中 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3825" target="_blank">shell 脚本无法在某些网络共享上运行，并出现“Too many levels of symbolic links”的错误</a>。</li> 
</ul> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:0px !important; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>Filename</th> 
   <th>SHA-256</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.36.1-64-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">08a0c20374d13d1b448d2c5713222ff55dd1f4bffa15093b85772cc0fc5f30e7</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.36.1-32-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">0a50735bd088698e6015265d9373cb0cc859f46a0689d3073f91da0dc0fe66aa</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.36.1-64-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">af17a2803c5c6406b9b60dfef2d34f72f218975f9d78df21005a44f6e2f0caf9</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.36.1-32-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">71ad967137a4da096f3e3406bd8a761f59c3a1edbf32e81e69e1f75efb9a44c4</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.36.1-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">a7a78c306dea018cc7ca3efe6a0d87c1dd7a43762705ccb0c5e31e3e44349207</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.36.1-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">dbd24baed2bbc0a5bb784cf3cb877bf9a66ff3fb029e95231f46db5e5b4bc4f5</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.36.1-busybox-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">5c7a819187dbcb0d8941c6a71bc384b01a942a6c2b5385202bb79a0fcc52d8a5</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.36.1-busybox-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">42dfaec1999393ba8b8e472fecc6b9435fed59415e404eedbe847c975c1840c2</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.36.1-64-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">38f4888db497ebe11f67c42a88ac1708fb5c68d53a398b4030b51a6116cce0e5</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.36.1-32-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">7b7cce2d1a29bb18b661720c692b39a27b406cd4916d75cc62d5fe1bfd9a57ea</td> 
  </tr> 
 </tbody> 
</table> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Freleases%2Ftag%2Fv2.36.1.windows.1" target="_blank">https://github.com/git-for-windows/git/releases/tag/v2.36.1.windows.1</a></p>
                                        </div>
                                      
</div>
            