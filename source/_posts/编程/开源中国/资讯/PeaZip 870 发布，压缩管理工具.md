
---
title: 'PeaZip 8.7.0 发布，压缩管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1838'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1838'
---

<div>   
<div class="content">
                                                                                            <p>PeaZip 是一个适用于 Windows 和 Linux 的免费文件存档工具和 rar 提取器，可处理 200 多种存档类型（7z, ace, arc, bz2, cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...），处理跨区存档（001, r01, z01...）并支持多种存档加密标准。</p> 
<p>该项目旨在为多种开源技术（7-Zip、FreeArc、PAQ、PEA、UPX）提供一个跨平台、可移植的 GUI 前端，专注于文件和档案管理，以及安全（强加密、双因素认证、加密密码管理器、安全删除）。</p> 
<p>PeaZip 8.7.0 正式发布，该版本更新内容如下：</p> 
<h3>后端：</h3> 
<ul> 
 <li>(Linux, Windows) 7z 22.00</li> 
 <li>Pea 1.08</li> 
</ul> 
<h3>代码</h3> 
<ul> 
 <li>现在可以通过主菜单 "Tools">"Verify hash of binaries"，选择性地检查被 PeaZip 调用的后端二进制文件的哈希值，以便发现被修改的二进制文件。</li> 
 <li>现在可以选择在编译时将后端二进制文件、配置和非二进制资源目录的路径硬编码为绝对路径，即 HBINPATH、HCONFPATH 和 HSHAREPATH 常量。</li> 
 <li>重新组织了源码包以提高可用性，并引入了更多构建 peazip 包的快速入门例子；源码现在在包的 dev 子文件夹中。</li> 
 <li>各种修复和改进</li> 
</ul> 
<h3>文件管理器</h3> 
<ul> 
 <li>(macOS) 现在能够正确识别用户 home 目录中的电影目录</li> 
 <li>在导航菜单中添加了 "在新标签中打开"。</li> 
 <li>现在可以将导航/搜索过滤器的内容导出为 CSV</li> 
 <li>CSV 分离器现在可以从选项 > 设置，常规标签，本地化选择器的右侧进行自定义</li> 
 <li>文件管理器现在可以显示文件大小和归档内目录的压缩文件大小</li> 
 <li>许多视觉上的改进 
  <ul> 
   <li>文件浏览器的默认列尺寸现在可以知道 DPI 的缩放比例</li> 
   <li>地址栏中的搜索栏现在可以选择保持扩展（宽度被记住）</li> 
   <li>重新组织了主题屏幕，使之更容易理解</li> 
   <li>改进了嵌入式图标</li> 
   <li>改进了主题：更新了 Different 和 Main 主题，Gray 主题被 Minimal 主题取代</li> 
   <li>……</li> 
  </ul> </li> 
</ul> 
<h3>提取和归档</h3> 
<ul> 
 <li>现在可以记住默认的归档创建动作</li> 
 <li>改进了在归档创建屏幕上显示目录大小</li> 
 <li>重新组织了选项>设置中的归档管理器设置页面</li> 
 <li>对于 Zpaq 格式，现在默认启用了 "绝对路径" 提取选项</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeazip.github.io%2Fchangelog.html%23latest_software_release" target="_blank">https://peazip.github.io/changelog.html#latest_software_release</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            