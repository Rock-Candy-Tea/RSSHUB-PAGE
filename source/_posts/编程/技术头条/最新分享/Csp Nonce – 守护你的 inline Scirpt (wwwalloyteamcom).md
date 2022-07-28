
---
title: 'Csp Nonce – 守护你的 inline Scirpt (www.alloyteam.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=8920'
author: 技术头条
comments: false
date: 2022-07-28 11:10:10
thumbnail: 'https://picsum.photos/400/300?random=8920'
---

<div>   
CSP 的默认策略是不允许 inline 脚本执行，所以当我们没有必要进行脚本 inline 时，CSP 域名白名单的机制足以防范注入脚本的问题。然而在实际项目中，我们还是会因为一些场景需要将部分脚本进行 inline。于是需要在 CSP 的规则中增加 script-src 'unsafe-inline' 配置，允许了 inline 资源执行。但也带来了新的安全隐患。
    
</div>
            