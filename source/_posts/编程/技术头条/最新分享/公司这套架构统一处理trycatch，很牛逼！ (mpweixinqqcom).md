
---
title: '公司这套架构统一处理try...catch，很牛逼！ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=5627'
author: 技术头条
comments: false
date: 2022-01-22 01:46:03
thumbnail: 'https://picsum.photos/400/300?random=5627'
---

<div>   
软件开发springboot项目过程中，不可避免的需要处理各种异常,spring mvc 架构中各层会出现大量的try &#123;...&#125; catch &#123;...&#125; finally &#123;...&#125;代码块，不仅有大量的冗余代码，而且还影响代码的可读性。这样就需要定义个全局统一异常处理器，以便业务层再也不必处理异常。
    
</div>
            