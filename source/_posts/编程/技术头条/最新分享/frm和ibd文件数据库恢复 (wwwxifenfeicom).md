
---
title: 'frm和ibd文件数据库恢复 (www.xifenfei.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=1337'
author: 技术头条
comments: false
date: 2022-02-05 06:08:32
thumbnail: 'https://picsum.photos/400/300?random=1337'
---

<div>   
这次客户rm -rf /var/lib/mysql删除文件,删除一半及时终止,但是已经有很多mysql相关文件被删除,重要的ibdata文件已经被删除,并且客户尝试了大量的恢复工作,对该分区进行了大量的写入操作,导致后面通过对xfs文件系统进行分析，确认无法恢复对应的ibdata文件.比较幸运客户需要的核心的mysql库都还在（frm和ibd文件还存在）。
    
</div>
            