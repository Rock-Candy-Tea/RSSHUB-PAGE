
---
title: '【灵踪安全：Nimbus和Nowswap因恒定乘积K值验证出现问题，遭闪电贷攻击】9月15日，以太坊上的AMM去中心化交易所项目Nimbus 和 Nowswap 先后遭遇闪电贷攻击。根据...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=1608'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=1608'
---

<div>   
【灵踪安全：Nimbus和Nowswap因恒定乘积K值验证出现问题，遭闪电贷攻击】9月15日，以太坊上的AMM去中心化交易所项目Nimbus 和 Nowswap 先后遭遇闪电贷攻击。根据灵踪安全漏洞分析系统显示：被攻击的原因是两者的交易函数中存在k值验证逻辑不完善的漏洞，交易时对用户收取了两笔费用：一笔是跟Uniswap 相同的交易手续费，为万分之15，另一笔是refFee。 第一笔费用的计算没有问题，但第二笔费用在对k值进行验证时没有考虑，使得攻击者偿还闪电贷的金额小于借出金额时也能通过k值验证，完成闪电贷交易，进而顺利实施攻击。  
</div>
            