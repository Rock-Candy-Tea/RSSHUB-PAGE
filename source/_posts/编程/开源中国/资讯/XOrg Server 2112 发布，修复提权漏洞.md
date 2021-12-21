
---
title: 'X.Org Server 21.1.2 发布，修复提权漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5ee10a4841451ddac8785ada792fa4cdbee.png'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 07:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5ee10a4841451ddac8785ada792fa4cdbee.png'
---

<div>   
<div class="content">
                                                                                            <p>X.Org Server 21.1.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.x.org%2Farchives%2Fxorg%2F2021-December%2F060842.html" target="_blank">已发布</a>，主要更新内容是修复四个会导致本地提权的严重安全漏洞。</p> 
<p>据介绍，当 xorg-server 作为特权进程运行时，可能会出现四个导致本地提权的安全漏洞，新版本已对此进行修复。此外，通过 Haswell 驱动程序向 DRI2 va_gl_users 列表添加了新的英特尔“Crocus”Gallium3D i965，修复了 logind 支持，以及其他回归错误修复。</p> 
<p>最后还一个值得注意的回归错误修复——不再报告来自 DRM 连接器的物理显示尺寸。因为启用输出的物理尺寸报告的变化被认为“<span style="background-color:#ffffff; color:#121212">太具有破坏性</span>”，因此 X.Org 服务器又回到了只报告 96DPI，恢复先前变更的补丁继续显示：</p> 
<blockquote> 
 <p>很多应用程序当前希望 X server 服务器显示的屏幕 DPI 为 96，即使实际显示的 DPI 是不同的。此外，目前 Xwayland 完全忽略任何硬件信息并将 DPI 设置为 96。因此，新行为即使修复了错误，也不应该自动对所有用户启用。</p> 
 <p>更好的解决方案是让默认的 DPI 保持不变，并通过命令行选项（也许是 -dpi auto，或类似的）来启用正确的行为。现在我们只需恢复这个错误修复。</p> 
</blockquote> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5ee10a4841451ddac8785ada792fa4cdbee.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.x.org%2Farchives%2Fxorg%2F2021-December%2F060842.html" target="_blank">详细内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            