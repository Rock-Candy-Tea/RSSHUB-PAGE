
---
title: 'Android对so体积优化的探索与实践 (tech.meituan.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8950'
author: 技术头条
comments: false
date: 2022-07-25 12:20:15
thumbnail: 'https://picsum.photos/400/300?random=8950'
---

<div>   
减小应用安装包的体积，对提升用户体验和下载转化率都大有益处。本文将结合美团平台的实践经验，分享 so 体积优化的思路、收益，以及工程实践中的注意事项。本文将先从 so 文件格式讲起，结合文件格式分析哪些内容可以优化，然后再具体讲解每项优化手段以及注意事项，最后介绍相关的工程实践经验。希望能对从事包体积优化的同学有所帮助或启发。
    
</div>
            