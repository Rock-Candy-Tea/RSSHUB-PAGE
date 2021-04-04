
---
title: '【Force DAO 代币增发漏洞简析】据慢雾区消息，DeFi 量化对冲基金 Force DAO 项目的 FORCE 代币被大量增发。经慢雾安全团队分析发现： 在用户进行 deposit 操纵...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6182'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=6182'
---

<div>   
【Force DAO 代币增发漏洞简析】据慢雾区消息，DeFi 量化对冲基金 Force DAO 项目的 FORCE 代币被大量增发。经慢雾安全团队分析发现： 在用户进行 deposit 操纵时，Force DAO 会为用户铸造 xFORCE 代币，并通过 FORCE 代币合约的 transferFrom 函数将 FORCE 代币转入 ForceProfitSharing 合约中。但 FORCE 代币合约的 transferFrom 函数使用了 if-else 逻辑来检查用户的授权额度，当用户的授权额度不足时 transferFrom 函数返回 false，而 ForceProfitSharing 合约并未对其返回值进行检查。导致了 deposit 的逻辑正常执行，xFORCE 代币被顺利铸造给用户，但由于 transferFrom 函数执行失败 FORCE 代币并未被真正充值进 ForceProfitSharing 合约中。最终造成 FORCE 代币被非预期的大量铸造的问题。 此漏洞发生的主要原因在于 FORCE 代币的 transferFrom 函数使用了`假充值`写法，但外部合约在对其进行调用时并未严格的判断其返回值，最终导致这一惨剧的发生。慢雾安全团队建议在对接此类写法的代币时使用 require 对其返回值进行检查，以避免此问题的发生。  
</div>
            