
---
title: 'GNU Binutils 2.37 发布，新增 ARMv9 Realm 管理扩展支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1135'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 06:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1135'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GNU Binutils 是创建和管理二进制程序的编程工具，GNU Binutils 2.37 发布，更新内容如下：</p> 
<ul> 
 <li>GNU Binutils 源码现在需要一个 C99 编译器和库来构建；</li> 
 <li>对 Arm Symbian OS 的支持已被移除；</li> 
 <li>增加了对 <strong>ARMv9</strong> RME 的支持；</li> 
 <li>Nm 有一个新的命令行选项：'--quiet'；</li> 
 <li>Readelf 和 objdump 现在可以显示并使用 .debug_sup 部分的内容；</li> 
 <li>在 nm 程序中增加了一个新的格式，指定 <code>--format=just-symbols</code>将告诉程序只显示符号名称，而不显示其他；</li> 
 <li>一个新的命令行选项 <code>--keep-section-symbols</code> 已经被添加到 objcopy 和 strip。 这将停止在复制文件时删除未使用的部分符号；</li> 
 <li>增加了各种新的链接器选项； 
  <ul> 
   <li>为 x86 ELF 目标增加了一个新的链接器选项 <code>-z report-relative-reloc</code>；</li> 
   <li>增加了一个新的链接器选项 <code>-Bno-symbolic</code>，它将取消 <code>-Bsymbolic</code> 和 <code>-Bsymbolic-functions</code> 选项；</li> 
  </ul> </li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceware.org%2Fpipermail%2Fbinutils%2F2021-July%2F117384.html" target="_blank">https://sourceware.org/pipermail/binutils/2021-July/117384.html</a></p>
                                        </div>
                                      
</div>
            