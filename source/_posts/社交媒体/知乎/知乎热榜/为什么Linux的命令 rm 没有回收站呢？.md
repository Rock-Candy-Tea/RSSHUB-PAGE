
---
title: '为什么Linux的命令 rm 没有回收站呢？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=7595'
author: 知乎
comments: false
date: Thu, 04 Aug 2022 11:39:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=7595'
---

<div>   
pansz的回答<br><br><p data-pid="wNYDmRfA">因为 rm 就相当于你 shift-del 的操作了，所以当然没有回收站。</p><p data-pid="FqNnnScr">但其实命令行也是可以调用回收站的，你把 rm 给 alias 到回收站的命令上去就行。</p><p data-pid="2b1EIBNo">首先确认你安装了 trash-cli，然后 alias rm=trash-put 。这样 rm 命令就变成进入回收站了。</p><p><br></p><p data-pid="psXpyzMp">注意，尽量只在 interactive shell 里边启用这个 alias，非 interactive  shell 不要启用它。</p><p></p>  
</div>
            