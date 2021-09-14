
---
title: 'PeaZip 8.2.0 发布，压缩管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7943'
author: 开源中国
comments: false
date: Tue, 14 Sep 2021 06:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7943'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">PeaZip 是一个适用于 Windows 和 Linux 的免费文件存档工具和 rar 提取器，可处理 200 多种存档类型（7z, ace, arc, bz2, cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...），处理跨区存档（001, r01, z01...）并支持多种存档加密标准。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">该项目旨在为多种开源技术（7-Zip、FreeArc、PAQ、PEA、UPX）提供一个跨平台、可移植的 GUI 前端，专注于文件和档案管理，以及安全（强加密、双因素认证、加密密码管理器、安全删除）。</p> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">PeaZip 8.2.0 正式发布，该版本更新内容如下：</p> 
 <h3 style="margin-left:.6em; margin-right:0; text-align:start">后端：</h3> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>(Linux) 将 Brotli 升级到 1.0.9 版本</li> 
  <li>(Linux) 为<span> </span><strong>Lzip .lz</strong><span> </span>文件类型添加了读取支持（浏览/测试/提取）</li> 
  <li>增加了对 .apkm, .apks 和 .aab 包的支持</li> 
 </ul> 
 <h3 style="margin-left:.6em; margin-right:0; text-align:start">代码：</h3> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>(Linux) 在 Linux 系统上生成的 CL 的最大长度现在增加到 128K 字符，而在 Windows 系统上允许的字符数则为 32K</li> 
  <li>「关于页面」现在可以显示构建中的部件集和 CPU 架构的信息，以便更好地排除故障</li> 
  <li>改进了命令行的使用 
   <ul style="margin-left:0; margin-right:0"> 
    <li>新的 res\batch\folder 包含指向主要应用程序功能的样本脚本，以帮助移植和在多种环境下部署应用程序；</li> 
    <li>修正了 -add27z, -add2zip 和相关的 switches；</li> 
    <li>新增 -ext2here, -ext2folder (alias -ext2smart), -ext2newfolder switches；</li> 
   </ul> </li> 
  <li>改进了从 GUI 生成更紧凑的命令行的方法，更好地检测了自动切换到 "全部提取" 的情况：</li> 
 </ul> 
 <h3 style="margin-left:.6em; margin-right:0; text-align:start">文件管理器：</h3> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>(Linux) 改进了文件管理器左侧导航树中默认显示的系统目录</li> 
  <li>(Linux) 在上下文菜单>文件管理器中启用了系统工具子菜单</li> 
  <li>(Windows) 改进并重新组织了上下文菜单>文件管理器中的系统工具子菜单</li> 
  <li>改进了档案浏览器</li> 
  <li>新增 Ctrl+Alt+A 链接，自动调整文件浏览器栏目</li> 
  <li>主题：在颜色选择器的右侧添加了 "预设" 链接，允许根据参考操作系统（如Mint、Ubuntu、Windows）的常见颜色主题快速定制应用程序和文本颜色</li> 
 </ul> 
 <h3 style="margin-left:.6em; margin-right:0; text-align:start">提取和归档</h3> 
 <ul style="margin-left:0; margin-right:0"> 
  <li>从存档/转换屏幕的高级选项卡中添加了<span> </span><strong>XZ</strong>（Linux、Windows）和<span> </span><strong>Zstd</strong>（Linux）作为 ZIP/ZIPX 压缩的可选算法</li> 
 </ul> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fchangelog.html" target="_blank">https://peazip.github.io/changelog.html</a></p> 
</div>
                                        </div>
                                      
</div>
            