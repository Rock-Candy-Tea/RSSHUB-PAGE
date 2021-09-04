
---
title: '【DAO Maker的Vesting合约遭到黑客攻击，攻击者最终获利近400万美金】据慢雾区情报，DAO Maker的Vesting合约遭到黑客攻击。DeRace Token (DERC)，Coinspaid (CPD...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=5193'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=5193'
---

<div>   
【DAO Maker的Vesting合约遭到黑客攻击，攻击者最终获利近400万美金】据慢雾区情报，DAO Maker的Vesting合约遭到黑客攻击。DeRace Token (DERC)，Coinspaid (CPD)，Capsule Coin (CAPS)，Showcase Token (SHO)都使用了Dao Maker的分发系统，在DAO Maker中进行持有者发行（SHO）时因DAO Maker合约被攻击，即SHO参与者的分发系统中出现了一个漏洞：init未初始化保护，攻击者初始化了init的关键参数，同时变更了owner，然后通过emergencyExit将目标代币盗走，并兑换成了DAI，攻击者最终获利近400万美金。 
黑客利用Vesting合约中的漏洞，将Vesting合约中的代币提走，如下是简要分析： 
对Vesting合约的实现合约0xf17ca0e0f24a5fa27944275fa0cedec24fbf8ee2进行反编译得到如下信息： 
1. Vesting合约中的init函数 (函数签名：0x84304ad7)，没有对调用者进行鉴权，黑客通过执行init函数成为Vesting合约的Owner。 
2. Owner可以执行Vesting合约中的emergencyExit函数，进行紧急提款。 
利用同样的手法其攻击其他Vesting合约，转移如下代币：DeRace Token (DERC)、Coinspaid (CPD)、Capsule Coin (CAPS)、Showcase Token (SHO)。  
</div>
            