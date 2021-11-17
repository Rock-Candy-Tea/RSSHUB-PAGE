
---
title: 'PeaZip 8.3.0 发布，压缩管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4739'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4739'
---

<div>   
<div class="content">
                                                                                            <p>PeaZip 是一个适用于 Windows 和 Linux 的免费文件存档工具和 rar 提取器，可处理 200 多种存档类型（7z, ace, arc, bz2, cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...），处理跨区存档（001, r01, z01...）并支持多种存档加密标准。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">该项目旨在为多种开源技术（7-Zip、FreeArc、PAQ、PEA、UPX）提供一个跨平台、可移植的 GUI 前端，专注于文件和档案管理，以及安全（强加密、双因素认证、加密密码管理器、安全删除）。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">PeaZip 8.3.0 正式发布，该版本更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>后端</strong></p> 
<ul> 
 <li>(Linux) 应用程序生成的命令脚本的最大总长度可以在 Options > Settings > General, Performances 中从 32KB 到 2MB 进行自定义。</li> 
 <li>(Linux) szcnick/p7zip 从 17.04 退到 17.02，因为可能存在处理某些 zip 文件的错误。</li> 
 <li>p7zip 的不同版本/分支（如果采用相同的语法）可以简单地替换 (peazip)res/bin/7z 路径中的二进制文件。</li> 
 <li>更新到 pea 1.04</li> 
 <li>为了提高 PeaZip 在多个操作系统和架构上的可移植性，应用程序的文件夹现在的结构如下： 
  <ul> 
   <li>应用程序的根文件夹包含 pea 和 peazip 二进制文件（以及 Windows 上的 dragdropfiles.dll），针对特定架构，由 src 包编译而成。 
    <ul> 
     <li>/res 目录，包含按类型划分的资源 
      <ul> 
       <li><span style="background-color:#ffffff; color:#333333">/res/portable（空）文件，将包标记为可移植：如果丢失，应用程序将作为可安装包工作并重新搜索用户路径中的配置（取决于主机系统）</span></li> 
       <li><span style="background-color:#ffffff; color:#333333">/res/bin 目录包含第三方架构的二进制文件，应该用合适的目标架构的二进制文件来替换；在Windows下，它还包含PeaZip配置向导的执行文件。</span></li> 
       <li><span style="background-color:#ffffff; color:#333333">/res/share目录包含非架构特定的资源，如文本、媒体、许可证、文档（关于二进制文件的许可证和注释已经被移到这里的注释子目录中），对于任何系统上的任何 PeaZip 包，它都可以简单地被复制。</span></li> 
       <li><span style="background-color:#ffffff; color:#333333">/res/conf目录包含用户特定的配置文件</span></li> 
      </ul> </li> 
    </ul> </li> 
   <li>在可安装的软件包中，res/conf 被写到适当的用户特定路径中，安装人员注意将 /res/bin 和 /res/share 替换为根据目标系统放在适当路径中的目录链接。</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0px; margin-right:0px; text-align:start"><strong>代码</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">(</span>Linux) 改进了对 Open Desktop 规范的遵从性：配置现在保存在 $XDG_CONFIG_HOME/peazip 目录中；如果 $XDG_CONFIG_HOME 未定义，则配置保存到 $HOME/.config/peazip 
  <ul> 
   <li><span style="background-color:#ffffff; color:#333333">要导入现有配置，只需将 $HOME/.PeaZip 目录的内容复制到新位置</span></li> 
  </ul> </li> 
 <li>GitHub：合并 ACTom 的“对 MacOS #25 的初始支持”</li> 
 <li>各种修复 
  <ul> 
   <li>修复了进度条</li> 
   <li>修复了在打开某些加密档案时不询问密码的可能错误，并减少了应用程序建议提供密码的错误情况。</li> 
   <li>修复了有关多卷档案的错误报告信息</li> 
   <li>修复了文件管理器中选择与所选项目具有相同特征的文件的错误</li> 
   <li>(Windows) 修复了在某些情况下不显示系统文件属性对话框的问题</li> 
  </ul> </li> 
</ul> 
<p><strong>文件管理器</strong></p> 
<ul> 
 <li>(Linux) /media、/run/media 和 /mnt（如果不为空）的快捷方式现在出现在导航树中的文件系统组下</li> 
 <li>(Linux) 在“Open with”菜单中改进了自动配置 XFCE 应用程序的替代选项：Mousepad、Midori , Parole, Ristretto</li> 
 <li>(Linux) 修复了 GTK2 的主题设置问题</li> 
 <li>Column header 的上下文菜单现在可以通过右键点击状态栏进行访问。</li> 
 <li>改进主题 </li> 
 <li><span style="background-color:#ffffff; color:#333333">Options > Settings > General, Privacy / Reset group, Working directory 现在默认设置为 system's temp（与大多数此类应用程序一致）</span></li> 
 <li>Options > Settings > General, Privacy / Reset group 现在允许以静默方式跳过锁定的临时工作文件的删除（默认开启，与大多数此类应用程序的行为一致）；然后可以选择单独删除临时工作文件</li> 
 <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Options > Settings > File manager 现在允许设置多字节单位：二进制、1024（IEC 千字节）或十进制、1000（IEC 千字节）或无（精确字节大小）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Options > Settings > File manager 现在允许自定义用于计算文件校验和和 hashes 的首选算法列表；当需要 checksum/hash 文件时，列表中的所有首选算法将在一</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>个步骤中执行。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p><strong>提取和归档</strong></p> 
<ul> 
 <li>为 7z 格式添加了 Deflate 和 Deflate64 压缩选项</li> 
 <li>改进了 -ext2here、-ext2folder（-alias -ext2smart）和 -ext2newfolder 功能，添加了命令行选项： 
  <ul> 
   <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>-i 在提取设置后忽略删除原始存档</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>-o 下一个参数中的输出目录</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>-p下一个参数中的密码</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> </li> 
</ul> 
<p><strong>WINDOWS 和 LINUX 安装程序</strong></p> 
<ul> 
 <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>(Windows) Improved installer</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> 
  <ul> 
   <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>“Extract here (in new folder)”条目现在默认出现在上下文菜单和 SendTo 菜单中</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复了某些情况下不显示的附加提取条目</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在应用程序中运行"Configure PeaZip"向导时，安装文件夹选择屏幕现在也可以使用；对于便携式版本，这可以方便地与主机系统集成。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> </li> 
 <li><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>(Linux) 改进了 DEB 和 RPM 安装程序，更好地符合文件系统层次结构标准，将特定于架构的资源和非特定于架构的资源分开</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p> 更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fchangelog.html" target="_blank">https://peazip.github.io/changelog.html</a></p>
                                        </div>
                                      
</div>
            