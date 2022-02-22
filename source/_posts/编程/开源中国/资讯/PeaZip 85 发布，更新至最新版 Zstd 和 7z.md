
---
title: 'PeaZip 8.5 发布，更新至最新版 Zstd 和 7z'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6664'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6664'
---

<div>   
<div class="content">
                                                                                            <p>PeaZip 是一个适用于 Windows 和 Linux 的免费文件存档工具和 rar 提取器，可处理 200 多种存档类型（7z, ace, arc, bz2, cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...），处理跨区存档（001, r01, z01...）并支持多种存档加密标准。</p> 
<p>该项目旨在为多种开源技术（7-Zip、FreeArc、PAQ、PEA、UPX）提供一个跨平台、可移植的 GUI 前端，专注于文件和档案管理，以及安全（强加密、双因素认证、加密密码管理器、安全删除）。</p> 
<p>PeaZip 8.5.0 正式发布，该版本更新内容如下：</p> 
<h3>后端</h3> 
<ul> 
 <li>7z 更新至 21.07</li> 
 <li>pea 更新至 1.06</li> 
 <li>Zstd 更新至 1.5.2（在 macOS 和 Windows 上）</li> 
</ul> 
<h3>代码</h3> 
<ul> 
 <li>清理了在某些非 Windows 版本的 Lazarus IDE 中引起错误的条件编译部分</li> 
 <li>使用 Lazarus 2.2.0 进行编译</li> 
 <li>macOS： 
  <ul> 
   <li>现在可以通过以下方式打开选定的文件：双击、从系统上下文菜单中 "open with" 打开、在应用程序中拖动文件</li> 
   <li>一些键盘快捷键被有条件地修改以更好地适应 macOS 的习惯</li> 
   <li>各种修正</li> 
  </ul> </li> 
</ul> 
<h3>文件管理器：</h3> 
<ul> 
 <li>Linux 
  <ul> 
   <li>在文件系统树状图中增加了对挂载在 /var/run/media 中的设备的链接，如果适用的话 文件浏览器现在可以选择显示更大的细节和大的列表模式（从状态栏上的样式菜单），以提高可读性和触摸的可用性</li> 
  </ul> </li> 
 <li>macOS 
  <ul> 
   <li>添加了文件系统树状视图链接到 ~/Library/Mobile Documents/，其中包含 iCloud 同步文件夹。</li> 
   <li>探索路径菜单项现在使用 open -R 显示选项，在 Finder 打开时突出显示 PeaZip 中选择的项目</li> 
   <li>移动到回收站（垃圾桶）的删除选项现在可以在文件管理器和归档/提取后的删除选项中使用</li> 
  </ul> </li> 
 <li>改进了图标的间距 
  <ul> 
   <li>现在有了更大的间距选项</li> 
   <li>主题 > 间距选项现在也适用于文件浏览器列表视图的各种样式</li> 
  </ul> </li> 
 <li>新的键盘快捷方式</li> 
</ul> 
<h3>提取和存档</h3> 
<ul> 
 <li>macOS 
  <ul> 
   <li>增加了对 Brotli、Zpaq 和 Zstandard 后端的支持</li> 
  </ul> </li> 
 <li>改进了压缩设置 
  <ul> 
   <li>为 LZMA 和 LZMA2 压缩增加了使用高达 4GB 内存的字典的选项</li> 
   <li>现在可以为非 Defalte/Deflate64 ZIP 压缩使用自定义字典大小</li> 
   <li>更新了 LZMA、LZMA2/XZ 和 PPMd 的压缩默认值，以适应新的 7z 默认值</li> 
   <li>更新了（peazip）/res/share/presets 中的压缩预设值</li> 
   <li>修正：现在可以用键盘改变压缩级别和算法</li> 
  </ul> </li> 
 <li>改进了布局的使用 
  <ul> 
   <li>在主菜单 "选项">"设置"，"档案管理器" 选项卡中，现在可以设置在启动 PeaZip 时自动打开的布局</li> 
   <li>现在可以从文件管理器加载和保存布局</li> 
  </ul> </li> 
 <li>改进了脚本编写 
  <ul> 
   <li>创建脚本时，交互式提取选项现在被忽略了，否则会指向一个临时的工作路径，而不是预期的输出目的地。</li> 
  </ul> </li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fchangelog.html" target="_blank">https://peazip.github.io/changelog.html</a></p>
                                        </div>
                                      
</div>
            