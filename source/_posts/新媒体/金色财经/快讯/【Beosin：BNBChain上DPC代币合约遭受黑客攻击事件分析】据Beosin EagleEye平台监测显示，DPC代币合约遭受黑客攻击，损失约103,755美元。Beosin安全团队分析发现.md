
---
title: '【Beosin：BNBChain上DPC代币合约遭受黑客攻击事件分析】据Beosin EagleEye平台监测显示，DPC代币合约遭受黑客攻击，损失约103,755美元。Beosin安全团队分析发现...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=1388'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=1388'
---

<div>   
【Beosin：BNBChain上DPC代币合约遭受黑客攻击事件分析】据Beosin EagleEye平台监测显示，DPC代币合约遭受黑客攻击，损失约103,755美元。Beosin安全团队分析发现攻击者首先利用DPC代币合约中的tokenAirdop函数为满足领取奖励条件做准备，然后攻击者使用USDT兑换DPC代币再添加流动性获得LP代币，再抵押LP代币在代币合约中。前面的准备，是为了满足领奖条件。然后攻击者反复调用DPC代币中的claimStakeLp函数反复领取奖励。因为在getClaimQuota函数中的” ClaimQuota = ClaimQuota.add(oldClaimQuota[addr]);”，导致奖励可以一直累积。最后攻击者调用DPC合约中claimDpcAirdrop 函数提取出奖励（DPC代币），换成Udst离场。目前被盗资金还存放在攻击者地址，Beosin安全团队将持续跟踪。  
</div>
            