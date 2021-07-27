
---
title: 'PeaZip 8.1.0 发布，压缩管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7577'
author: 开源中国
comments: false
date: Tue, 27 Jul 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7577'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PeaZip 是一个适用于 Windows 和 Linux 的免费文件存档工具和 rar 提取器，可处理 200 多种存档类型（7z, ace, arc, bz2, cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...），处理跨区存档（001, r01, z01...）并支持多种存档加密标准。</p> 
<p>该项目旨在为多种开源技术（7-Zip、FreeArc、PAQ、PEA、UPX）提供一个跨平台、可移植的 GUI 前端，专注于文件和档案管理，以及安全（强加密、双因素认证、加密密码管理器、安全删除）。</p> 
<p>PeaZip 8.1.0 正式发布，该版本更新内容如下：</p> 
<p><strong>后端</strong></p> 
<p>PEA 1.02</p> 
<ul> 
 <li>提高了十六进制预览功能的速度，更新了 secure delete 功能</li> 
</ul> 
<p>Zstd 1.50</p> 
<ul> 
 <li>(Windows) Tino Reichardt codecs for 7z v1.5.0r1 
  <ul> 
   <li>更新编解码器至 Brotli 1.0.9、FLZMA2 1.0.1、Lizard 1.0、LZ4 1.9.3、LZ5 1.5、Zstandard 1.5.0</li> 
  </ul> </li> 
 <li>(Linux) szcnick p7zip 17.04: 
  <ul> 
   <li>引入对 Brotli、Lizard、LZ5 的支持</li> 
   <li>更新 LZ4 1.9.3 和 zstd 1.4.9</li> 
   <li>在 Linux 系统上，Brotli 和 Zstandard 预设现在指向使用 Brotli 或 Zstd 压缩的 7z single step 压缩（tar.br 和 tar.zst 预设仍可作为替代）。</li> 
  </ul> </li> 
 <li>(Windows) 增加了对系统的 Extrac32 作为替代 CAB extraction engine 的支持 
  <ul> 
   <li>在 "选项">"设置"，"高级"标签中启用 Extrac32 backend。</li> 
   <li>CAB 仍将使用 7z 后端 listed/tested，Extrac32（如果启用）将被用于提取操作。</li> 
  </ul> </li> 
</ul> 
<p><strong>CODE</strong></p> 
<ul> 
 <li>各种修复。改进了处理含有大量项目（文件、文件夹）的档案的性能。 
  <ul> 
   <li>在 64K 项目的归档中，速度提高 50%，RAM 使用率为 -25%。</li> 
   <li>在 128K 项目的归档中，速度提高 2 倍，RAM 使用率为 -25%。</li> 
   <li>在 256K 项目的归档中，速度提高了 4 倍，RAM 使用率为 -35%。</li> 
   <li>提高了列表归档的速度，也提高了涉及大量文件的测试、存档和提取操作的速度。</li> 
  </ul> </li> 
</ul> 
<p><strong>文件管理器 </strong></p> 
<ul> 
 <li>增加了新的用户提供的主题：KDE Breeze、Oxygen</li> 
 <li>改进 browsing archives：点击面包屑栏中的根目录，现在只列出根目录，而按刷新（F5）重新打开档案，完全重新解析内容。</li> 
 <li>如果是 spanned archive，在当前路径中实际发现的 volumes（如 PeaZip 提取所需）会显示在应用程序的标题栏和状态栏中。</li> 
 <li>改进设置 
  <ul> 
   <li>在 General 选项卡的 Performances group 中进行更灵活的浏览器优化</li> 
   <li>重新组织了各种设置以提高可读性</li> 
  </ul> </li> 
 <li>更新翻译</li> 
</ul> 
<p><strong>EXTRACTION and ARCHIVING</strong></p> 
<ul> 
 <li>增加了对 .whl Python archives 和 .gem Ruby gem archives 的支持（作为容器文件）</li> 
 <li>在提取下拉菜单中增加了提取全部、选定或显示项目的选项，复制了提取按钮的上下文菜单</li> 
 <li>在测试按钮的上下文菜单中增加了测试所有、选定或显示项目的操作</li> 
 <li>改进了存档转换程序 
  <ul> 
   <li>提取阶段现在显示为一个单一的任务序列，主屏幕被隐藏起来以减少视觉上的杂乱</li> 
   <li>如果在提取阶段遇到错误，将报告给用户，因此可以停止转换（以纠正错误）或继续转换（如果需要）</li> 
  </ul> </li> 
 <li>改进了提取命令行的创建：当所有项目被选中时，使用过滤器而不是项目列表切换到一个更紧凑的命令行</li> 
</ul> 
<p><strong>WINDOWS 和 LINUX 安装程序 </strong></p> 
<ul> 
 <li>Windows 安装程序现在支持命令行参数，在安装过程中设置语言 
  <ul> 
   <li>语言可以作为最后一个参数声明，可以有或没有"/"的前缀</li> 
   <li>为了识别语言，请检查 PeaZip/res/lang/ 目录中的语言文件名称</li> 
  </ul> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fchangelog.html%23software_development_log" target="_blank">https://peazip.github.io/changelog.html#software_development_log</a></p>
                                        </div>
                                      
</div>
            