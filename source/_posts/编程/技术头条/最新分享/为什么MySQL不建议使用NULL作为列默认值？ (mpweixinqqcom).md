
---
title: '为什么MySQL不建议使用NULL作为列默认值？ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=4044'
author: 技术头条
comments: false
date: 2022-07-24 12:16:54
thumbnail: 'https://picsum.photos/400/300?random=4044'
---

<div>   
通常能听到的答案是使用了NULL值的列将会使索引失效,但是如果实际测试过一下,你就知道IS NULL会使用索引.所以上述说法有漏洞
    
</div>
            