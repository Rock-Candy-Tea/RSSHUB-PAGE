
---
title: 'GNU Coreutils 9.1 发布，效率增强'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5010'
author: 开源中国
comments: false
date: Mon, 18 Apr 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5010'
---

<div>   
<div class="content">
                                                                                            <p>GNU Coreutils 9.1 现已发布。GNU Core Utilities 是 GNU 操作系统的基本文件、shell 和文本操作实用程序，这些是预期存在于每个操作系统上的核心实用程序。。</p> 
<p>GNU Coreutils 9.1 包含了广泛的修复、改进和其他改动。一个令人兴奋的方面是各种效率改进，如 cat 现在使用 copy_file_range 系统调用，对其他命令则使用更优化的 syscalls 以提高效率。</p> 
<p>一些亮点更新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dnews_item%26px%3DGNU-Coreutils-9.1" target="_blank">内容</a>如下：</p> 
<ul> 
 <li>cat 命令现在使用 copy_file_range 系统调用，在常规文件之间进行简单的拷贝。反过来，在可能的复制卸载/重新链接中，这应该是更有效的。copy_file_range 系统调用用于从一个文件拷贝到另一个文件--在两个文件描述符之间拷贝一定范围的数据，而不需要通过用户空间。</li> 
 <li>cp、mv 和 install 命令在复制到一个目录时，现在使用类似 openat 的系统调用，这将避免一些 race conditions，并且更有效率。</li> 
 <li>ls 命令默认情况下不再给文件着色，因为它们很少被使用，而且每个文件的处理时间会增加约 30%。</li> 
 <li>ls 和 stat 命令默认不再尝试自动挂载文件，而是恢复到早期的行为。</li> 
 <li>如果遇到符号链接，使用 chmod -R 的递归 chmod'ing 将不再以错误状态退出。</li> 
 <li>修复了 macOS 上的 copy 行为，如果从苹果 APFS 文件系统复制到其他文件系统，可能导致误复制问题。还有其他的 macOS 修复，当源文件和目标文件是 APFS 上的普通文件时，copy 现在会创建一个 copy-on-write clone。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fforum%2Fforum.php%3Fforum_id%3D10158" target="_blank">https://savannah.gnu.org/forum/forum.php?forum_id=10158</a></p>
                                        </div>
                                      
</div>
            