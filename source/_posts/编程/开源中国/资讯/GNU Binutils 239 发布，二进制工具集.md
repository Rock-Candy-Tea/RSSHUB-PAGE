
---
title: 'GNU Binutils 2.39 发布，二进制工具集'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4217'
author: 开源中国
comments: false
date: Sun, 07 Aug 2022 08:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4217'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">GNU Binutils 是创建和管理二进制程序的编程工具，目前 GNU Binutils 2.39 发布了，更新内容如下：</span><br> <br> GNU Binutils 2.39 最值得注意的是，如果堆栈可执行，ELF 链接器现在将生成警告。如果输出二进制文件包含设置了所有三个读/写/执行权限位的段，链接器现在也会发出警告。这些警告帮助开发人员识别可能容易受到可执行内存区域攻击的软件。Binutils 2.39 的这些警告默认启用，但可以通过新的命令行开关禁用。<br> <br> GNU Binutils 2.39 还在 ELF 链接器中添加了一个“--package-metadata”选项，用于嵌入 JSON 有效负载以支持包元数据规范。同时，Binutils 的 objdump 程序现在支持在其反汇编器输出中突出显示彩色语法。<br> <br> GNU Binutils 2.39 还具有其他改进，如<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceware.org%2Fpipermail%2Fbinutils%2F2022-August%2F122246.html" target="_blank">发布公告</a>中所述。</p>
                                        </div>
                                      
</div>
            