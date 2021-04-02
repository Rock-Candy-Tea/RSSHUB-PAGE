
---
title: 'Visual Studio Code 1.55 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-00b5ff54962627323268fdcabd552fe469a.png'
author: 开源中国
comments: false
date: Fri, 02 Apr 2021 07:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-00b5ff54962627323268fdcabd552fe469a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Visual Studio Code 1.55 稳定版已发布，其中一些主要<strong>亮点内容如下</strong>：</p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_accessibility" target="_blank">辅助功能改进</a>：</strong>多光标支持，屏幕阅读器的行数限制增加到 1000 行。</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_updated-brand-icons-for-macos-big-sur" target="_blank">macOS Big Sur 的图标更新</a>：</strong>与 Big Sur 的视觉风格相匹配的 brand icons。</li> 
</ul> 
<p><img alt height="50" src="https://oscimg.oschina.net/oscnet/up-00b5ff54962627323268fdcabd552fe469a.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="136" src="https://oscimg.oschina.net/oscnet/up-072c30c549817a1623e1ee4006db722683f.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_improvements-to-breakpoints" target="_blank">改进断点</a>：</strong>内联断点菜单等。</li> 
</ul> 
<p><img alt height="120" src="https://oscimg.oschina.net/oscnet/up-527118456b1e2b0df3dc880a3353d69bda9.png" width="326" referrerpolicy="no-referrer">  <img alt height="120" src="https://oscimg.oschina.net/oscnet/up-01c05c996929e8fc3ba78a5e4d55e4d3cad.png" width="193" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_tab-decorations-on-by-default" target="_blank">Editor status decorations</a>：</strong>Editor tab status decorations  默认情况下处于启用状态。</li> 
</ul> 
<p><img alt height="313" src="https://oscimg.oschina.net/oscnet/up-47b714fe1ca38c5db7a399950bf9f7278f0.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_resizing-columns-in-keyboard-shortcuts-editor" target="_blank">自定义键盘快捷键编辑器</a>：</strong>键盘快捷键编辑器现在已经重构为使用新的表格部件，允许用户调整编辑器中的列的大小。</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_remote-development" target="_blank">改进的远程端口管理</a>：</strong>端口转发自动检测，regex 命名等。</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_terminal-profiles" target="_blank">Terminal</a></strong> <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_terminal-profiles" target="_blank">配置文件</a>：</strong>在 terminal 中定义配置文件，以方便地启动非默认 Shell。</li> 
</ul> 
<p><img alt height="266" src="https://oscimg.oschina.net/oscnet/up-9c695384d73816001697c32694649fa3dcc.png" width="338" referrerpolicy="no-referrer"></p> 
<p>VS Code 会通过这个菜单自动检测并显示一些比较常用的 shell，但也可以通过 terminal.integrated.profiles.<platform> 设置进行配置。通过这个设置，可以添加新的配置文件，更改现有的配置文件和删除默认的配置文件。比如：</p> 
<pre><code>"terminal.integrated.profiles.windows": &#123;
  // Add a PowerShell profile that doesn't run the profile
  "PowerShell (No Profile)": &#123;
      // Some sources are available which auto detect complex cases
      "source": "PowerShell",
      "args": ["-NoProfile"],
      // Name the terminal "PowerShell (No Profile)" to differentiate it
      "overrideName": true
  &#125;,
  // Remove the builtin Git Bash profile
  "Git Bash": null,
  // Add a Cygwin profile
  "Cygwin": &#123;
    "path": "C:\\cygwin64\\bin\\bash.exe",
    "args": ["--login"]
  &#125;
&#125;</code></pre> 
<p>推荐的初始添加配置文件的方法是通过“<strong>选择默认配置文件”</strong>命令，该命令允许基于现有配置文件或其他检测到的 shell 创建配置文件。</p> 
<p><img alt height="180" src="https://oscimg.oschina.net/oscnet/up-0b9fbd2ad5b90b717c40e92397cf9b68eed.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_notebooks" target="_blank">Notebook</a></strong> <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_notebooks" target="_blank">的改进</a>：</strong>多个单元格选择，以及更具可定制性的 diff 编辑器。</li> 
</ul> 
<p><img alt height="260" src="https://oscimg.oschina.net/oscnet/up-6ebf613c137a194a8b13d24d28705ce66cc.gif" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="313" src="https://oscimg.oschina.net/oscnet/up-acae6b22eed392a214a3420095aabfd7593.gif" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55%23_raspberry-pi" target="_blank">Raspberry Pi 上的 VS Code</a>：</strong>新主题，描述了如何在 Raspberry Pi 设备上安装 VS Code。</li> 
</ul> 
<p>更多详细信息可查看<strong>官方发布公告</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fupdates%2Fv1_55" target="_blank">https://code.visualstudio.com/updates/v1_55</a></p> 
<p><strong>下载：</strong>Windows: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Fwin32-x64-user%2Fstable" target="_blank">User</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Fwin32-x64%2Fstable" target="_blank">System</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Fwin32-arm64-user%2Fstable" target="_blank">ARM</a> | Mac: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Fdarwin-universal%2Fstable" target="_blank">Universal</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Fdarwin%2Fstable" target="_blank">64 bit</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Fdarwin-arm64%2Fstable" target="_blank">Arm64</a> | Linux: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Flinux-snap-x64%2Fstable" target="_blank">snap</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Flinux-deb-x64%2Fstable" target="_blank">deb</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Flinux-rpm-x64%2Fstable" target="_blank">rpm</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fupdate.code.visualstudio.com%2F1.55.0%2Flinux-x64%2Fstable" target="_blank">tarball</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Fsupporting%2Ffaq%23_previous-release-versions" target="_blank">ARM</a></p>
                                        </div>
                                      
</div>
            