
---
title: '用 poudriere 完成包管理 (blog.delphij.net)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9638'
author: 技术头条
comments: false
date: 2022-06-19 10:09:19
thumbnail: 'https://picsum.photos/400/300?random=9638'
---

<div>   
由于使用的 port 的编译选项与官方的往往不一致（例如我非常讨厌 gnutls、avahi 这两个包，此外有时我希望使用一个和官方不太一样的 OpenLDAP 版本，或者采用不同的编译选项等等），我之前一直是 portmaster(8) 的用户。 portmaster 是Doug Barton 早年用 shell 脚本写的一个 portupgrade(1)的替代品，和后者相比，它不需要使用数据库，并且充分利用了 shell 的任务管理功能实现了尽可能利用 CPU 的计算能力，我个人也从这个脚本中学到了不少shell 脚本的技巧。
    
</div>
            