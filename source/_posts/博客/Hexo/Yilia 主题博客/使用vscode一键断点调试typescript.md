
---
title: '使用vscode一键断点调试typescript'
categories: 
 - 博客
 - Hexo
 - Yilia 主题博客
headimg: 'https://picsum.photos/400/300?random=7015'
author: Hexo
comments: false
date: Sun, 22 Oct 2017 15:04:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=7015'
---

<div>   
本来我是webstorm死忠，只是近一年来vscode发展迅速，感觉其性(功能)价(内存)比已经超过webstorm，虽然有一些细节功能还不如webstorm，不过就typescript而言，同是微软自家的东西，会支持的更好一些，所以近来就转战vscode了~
目前typescript的断点调试方案，很多编辑器/IDE官方或一些技术博文，大多都是先手动(或其他相对自动化的方式)编译生成javascript以及相应sourcemap，然后以javascript为入口进行调试。这种方式，还是不够便捷。
本文介绍的断点调试，『无需手动编译ts文件』，就像调试javascript代码一样，乃真正的『一键』调试。另外，本文针对node环境的代码进行调试，对于前端代码不一定试用
      
      
</div>
            