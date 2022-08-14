
---
title: '【安全团队：Acala项目方对aUSD池子的奖励倍率进行了修改，导致池子的奖励被放大】8月14日消息，波卡生态项目Acala因链上设置错误，导致aUSD增发。以下是慢雾安...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6305'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=6305'
---

<div>   
【安全团队：Acala项目方对aUSD池子的奖励倍率进行了修改，导致池子的奖励被放大】8月14日消息，波卡生态项目Acala因链上设置错误，导致aUSD增发。以下是慢雾安全团队分析： 
1. 项目方在2022-08-13 22:23:12 (+UTC)调用了 update_dex_saving_rewards 对 aUSD 池子的奖励倍率进行了修改，修改为500000000000000000。 
2. 在区块的 hook 函数 on_initialize 中会去调用 accumulate_dex_saving 函数,在函数中池子的奖励总量是由 dex_saving_reward_rate 乘上 dex_saving_reward_base，由于 dex_saving_reward_rate 在上一步中已经被放大了导致池子的奖励也被放大。 
3. 最后用户领取到了错误的奖励。  
</div>
            