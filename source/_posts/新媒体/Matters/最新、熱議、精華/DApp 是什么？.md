
---
title: 'DApp 是什么？'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/6ea160b4-b220-4527-a34b-3bd55f7e9541.jpeg'
author: Matters
comments: false
date: Sun, 11 Apr 2021 04:21:50 GMT
thumbnail: 'https://assets.matters.news/embed/6ea160b4-b220-4527-a34b-3bd55f7e9541.jpeg'
---

<div>   
<p>DApp 也就是「Decentralized Application」的简称，按照很多营销号的说法是一个跨时代的技术。但是这东西其实远没有他们说的这么跨时代。这篇文章会从技术角度介绍一下什么是 DApp，以及它涉及到了哪些相关的技术，及其现阶段的问题有哪些，算是对我前段时间研究的一个小总结。另外本文不涉及到任何的投资建议，任何时候关于虚拟货币的投资都应该小心谨慎。本文是我前段时间研究的一个小总结。</p><p>DApp 其实指的不是一个单一的技术，它是一系列技术的综合体，整体架构可以用下图来表示。</p><figure class="image"><img src="https://assets.matters.news/embed/6ea160b4-b220-4527-a34b-3bd55f7e9541.jpeg" data-asset-id="6ea160b4-b220-4527-a34b-3bd55f7e9541" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>在这张图中，展现了一个基于 IPFS 网络的 DApp 的架构。</p><p>可以看到其实整个 DApp 最为核心的部分是个前端的「单页应用（single page application）」。这个也是用户可以直接接触的部分。在 DApp 的架构中，页面会通过一个 IPFS 的网关呈现（当然其实不一定要 IPFS，其他的技术比如 Hypercore 也行，当然如果有 BT 的网关，也是可以的（笑），只是目前 IPFS 用的比较多而已）。这里 IPFS 网关的主要作用就是通过去中心化的方式来提供前端需要的资源（比如JS、CSS、HTML、图片等）。这部分通讯等方式和传统的网页没什么区别，就是普通的HTTP协议。</p><p>当然一般情况下，你是会希望你的 DApp 是可以和区块链进行操作的。比如查询余额之类的事情。这个时候你就需要一个接口，来进行链上操作，也就是上图提供的区块链网关。这个网关的作用和 IPFS 网关类似，只是这里提供的是区块链操作的相关接口。目前来看，真正实用的公链（其实差不多只有以太坊）的网关用的是 JSON-RPC 协议通讯，但这里要用什么样子的协议都行，看你用的区块链网关支持哪些协议。</p><p>最后一部分是和用户钱包的交互，一般会要求用户装一个钱包插件，这样你就可以通过钱包提供API进行交互了，这个要看具体钱包的要求，不同的钱包可能会有不同的初始化方式，具体要看他们的文档。比如这里就是 <a href="https://docs.metamask.io/guide/#why-metamask" target="_blank">MetaMask</a> 的文档。</p><h2><strong>好处</strong></h2><p>最大的好处在理想情况下（也就是用户用自己的 IPFS 节点和自己的区块链网关），这套技术是彻底的去中心化的，不需要某台服务器来提供服务。自然而然也享受到这些技术带来的好处，比如减少了单点失效的危险、高匿名、抗审查等。</p><h2><strong>不足</strong></h2><p>但是这套系统结构还是面临了很多的不足，首先就是网关问题，大部分用户都无法提供上图提到的两种网关，其中 IPFS 的网关还可能自己搭建，但是区块链的网关让普通用户自己搭建会非常困难。这导致了，目前来说这两个网关还是非常中心化的，并没有体现出中心化的优势。</p><p>另外一个非常大的问题就是区块链的性能还是不行，吞吐量非常小而且不是可水平扩展（Scale-out）的。这导致上链的操作，可能有很长的延时和需要付很多的手续费。</p><p>另外用户要想使用 DApp 一般还需要安装钱包插件，对于不理解插件是什么的用户会很麻烦。</p>  
</div>
            