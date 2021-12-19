
---
title: '【Grim Finance 被黑简析：攻击者通过闪电贷借出 WFTM 与 BTC 代币】据慢雾区情报，2021 年 12 月 19 日，Fantom 链上 Grim Finance 项目遭受攻击。慢雾安全团队...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=7953'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=7953'
---

<div>   
【Grim Finance 被黑简析：攻击者通过闪电贷借出 WFTM 与 BTC 代币】据慢雾区情报，2021 年 12 月 19 日，Fantom 链上 Grim Finance 项目遭受攻击。慢雾安全团队进行分析后以简讯的形式分享给大家。 
1. 攻击者通过闪电贷借出 WFTM 与 BTC 代币，并在 SpiritSwap 中添加流动性获得 SPIRIT-LP 流动性凭证。 
2. 随后攻击者通过 Grim Finance 的 GrimBoostVault 合约中的 depositFor 函数进行流动性抵押操作，而 depositFor 允许用户指定转入的 token 并通过 safeTransferFrom 将用户指定的代币转入 GrimBoostVault 中，depositFor 会根据用户转账前后本合约与策略池预期接收代币(预期接收 want 代币，本次攻击中应为 SPIRIT-LP)的差值为用户铸造抵押凭证。 
3. 但由于 depositFor 函数并未检查用户指定转入的 token 的合法性，攻击者在调用 depositFor 函数时传入了由攻击者恶意创建的代币合约地址。当 GrimBoostVault 通过 safeTransferFrom 函数调用恶意合约的 transferFrom 函数时，恶意合约再次重入调用了 depositFor 函数。攻击者进行了多次重入并在最后一次转入真正的 SPIRIT-LP 流动性凭证进行抵押，此操作确保了在重入前后 GrimBoostVault 预期接收代币的差值存在。随后 depositFor 函数根据此差值计算并为攻击者铸造对应的抵押凭证。 
4. 由于攻击者对 GrimBoostVault 合约重入了多次，因此 GrimBoostVault 合约为攻击者铸造了远多于预期的抵押凭证。攻击者使用此凭证在 GrimBoostVault 合约中取出了远多于之前抵押的 SPIRIT-LP 流动性凭证。随后攻击者使用此 SPIRIT-LP 流动性凭证移除流动性获得 WFTM 与 BTC 代币并归还闪电贷完成获利。 
此次攻击是由于 GrimBoostVault 合约的 depositFor 函数未对用户传入的 token 的合法性进行检查且无防重入锁，导致恶意用户可以传入恶意代币地址对 depositFor 进行重入获得远多于预期的抵押凭证。慢雾安全团队建议：对于用户传入的参数应检查其是否符合预期，对于函数中的外部调用应控制好外部调用带来的重入攻击等风险。  
</div>
            