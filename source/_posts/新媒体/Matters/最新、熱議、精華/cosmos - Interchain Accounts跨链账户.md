
---
title: 'cosmos - Interchain Accounts跨链账户'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://picsum.photos/400/300?random=1628'
author: Matters
comments: false
date: Wed, 16 Mar 2022 15:10:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=1628'
---

<div>   
<p>跨链<strong>账户</strong>是一项关键功能，它有助于在不显着增加开发资源的情况下释放互连区块链的潜力。</p><p><strong>简单地说，跨链账户允许区块链使用 IBC 安全地控制另一个区块链上的账户。</strong></p><p>其目的是，与其为每个模块的功能创建应用程序级 IBC，不如让跨链帐户允许某人利用帐户的功能来访问区块链的特定于应用程序的功能。</p><p>跨链账户的规范在跨链<a href="https://github.com/cosmos/ics/blob/master/spec/ics-027-interchain-accounts/README.md" rel="noopener noreferrer" target="_blank">标准 #27</a>中进行了概述。它最初是在 2019 年 8 月作为一个想法提出的，经过数月的<a href="https://github.com/cosmos/ics/pull/278" rel="noopener noreferrer" target="_blank">公开讨论、反馈和修订</a>——它于 2019 年 12 月被合并为官方链间标准。</p><p>跨链账户最重要的两个特点如下：</p><ul><li><strong>通过 IBC 确定性地创建一个新的跨链账户</strong></li><li><strong>将交易中继到跨链账户并提交到目标区块链</strong>。</li></ul><p>虽然 IBC 的这种灵活且相当简单的设计在允许跨链<a href="https://github.com/cosmos/ics/tree/master/spec" rel="noopener noreferrer" target="_blank">标准（ICS）</a>在各种区块链中采用方面具有显着优势，但它也意味着许多特定于应用程序的功能（如代币转移、代币交换、 staking 等）必须单独构建在 IBC TAO 层之上并作为应用层。</p><p>即使 IBC 已经准备好，除了跨区块链的代币传输之外，可能没有太多可以使用的功能。</p><h1><strong>跨链账户解决的问题</strong></h1><p><strong>Cosmos Zones 之间的可组合性而不降低区域主权</strong></p><p>为 IBC 上的每个应用程序功能创建新的标准和实现需要时间。</p><p>这意味着要在 IBC 上实现特定于应用程序的交易（例如打开 CDP、进行 DEX 交易、跨链 DAO 等），需要花费时间和资源来实现这些IBC 应用层的特性。</p><p>IBC 本身可能已准备好生产，但在链间代币转移之外几乎没有可用的应用程序级功能。这可能会延迟 IBC 在 Cosmos 生态系统中采用的时间。</p><p>跨链账户通过允许一个区块链通过“账户”可以做的事情来访问另一个区块链的应用程序功能（例如股权、投票、交换代币等）来帮助解决这个问题。这提供了一种创建应用程序可组合性的简单方法，<strong>类似于智能合约在 EVM 上的交互方式</strong>，通过利用 IBC。</p><p>因为“主权、可互操作的区块链”的基本架构仍然存在，跨链账户引入的可组合性并没有带走<a href="https://blog.cosmos.network/why-application-specific-blockchains-make-sense-32f2073bfb37" rel="noopener noreferrer" target="_blank">特定应用区块链的好处</a>。</p><p>这对于在 Cosmos 生态系统中建立应用程序的网络效应至关重要，因为它能够从 IBC 采用的早期阶段相互交叉交互。</p><blockquote>跨链账户交易只是打包在 IBC 交易中的目标区块链的非 IBC 区块链交易。<strong>跨链账户交易将如何处理</strong>非 IBC 交易留给目标区块链的内部逻辑。跨链账户本身与功能无关，因为跨链账户并不关心它包含的交易试图做什么。</blockquote><p>只要实现跨链账户，区块链上的新功能就可以立即作为 IBC 交易得到支持。</p><h1><strong>总结</strong></h1><p>跨链账户旨在在 IBC 投入生产的早期阶段为 IBC 采用提供可扩展的路径。由于大多数可以从 IBC 中受益的功能都是普通账户已经可以做到的（例如质押、开立 CDP 头寸、代币交换），跨链账户简化了构建跨链应用程序的过程，几乎没有缺点。</p><p>通过将 Cosmos 区块链上的应用程序变成乐高块，可以轻松构建以下应用程序：</p><ul><li>类似跨链钱包</li><li>跨链代币互换</li><li>多链 DAO</li></ul><h1><strong>参考</strong></h1><p><a href="https://medium.com/chainapsis/why-interchain-accounts-change-everything-for-cosmos-interoperability-59c19032bf11" rel="noopener noreferrer" target="_blank">Why Interchain Accounts Change Everything for Cosmos Interoperability</a></p><p><strong>Links：</strong> <a href="https://twitter.com/Changeli0n" rel="noopener noreferrer" target="_blank">个人推特</a> <a href="https://matters.news/@hellolinux" rel="noopener noreferrer" target="_blank">matters</a> <a href="https://t.me/hellolinuxLab" rel="noopener noreferrer" target="_blank">个人分享TG频道</a> </p>  
</div>
            