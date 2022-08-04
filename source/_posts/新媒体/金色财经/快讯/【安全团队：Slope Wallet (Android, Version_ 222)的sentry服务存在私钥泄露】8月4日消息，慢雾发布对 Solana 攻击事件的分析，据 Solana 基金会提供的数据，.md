
---
title: '【安全团队：Slope Wallet (Android, Version_ 2.2.2)的sentry服务存在私钥泄露】8月4日消息，慢雾发布对 Solana 攻击事件的分析，据 Solana 基金会提供的数据，...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=581'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=581'
---

<div>   
【安全团队：Slope Wallet (Android, Version: 2.2.2)的sentry服务存在私钥泄露】8月4日消息，慢雾发布对 Solana 攻击事件的分析，据 Solana 基金会提供的数据，被盗用户种约 60% 使用 Phantom、约 30% 使用 Slope，其余使用 Trust Wallet、Coin98 Wallet 等，IOS 和 Android 均未能幸免。 
在分析 Slope Wallet (Android, Version: 2.2.2) 时，发现其使用了 sentry 的服务。Sentry 是一项广泛使用的服务，在“o7e.slope[.]finance”上运行。Sentry 的服务从 Slope 钱包中收集助记词和私钥等敏感数据，并在创建钱包时将其发送到 https://o7e.slope[.]finance/api/4/envelope/，并发现 Version:>=2.2.0 包中的 sentry 服务会收集助记词发给“o7e.slope[.]finance”，而 Version:2.1.3 则没有找到收集助记词或私钥的明显行为。Slope Wallet(Android, >= Version: 2.2.0) 于 06/24/2022 之后发布，所以 Slope 该日期之后的用户受到影响。 
对于另外 60% 的使用 Phantom Wallet 用户，分析 Phantom（版本：22.07.11_65）钱包后发现，Phantom（Android，版本：22.07.11_65）也使用 sentry 服务收集用户信息，但目前没有发现任何明显的收集助记词或私钥的行为。  
</div>
            