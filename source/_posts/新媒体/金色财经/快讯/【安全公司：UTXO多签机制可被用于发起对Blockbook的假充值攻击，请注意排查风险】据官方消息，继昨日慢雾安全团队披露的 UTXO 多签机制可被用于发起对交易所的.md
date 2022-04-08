
---
title: '【安全公司：UTXO多签机制可被用于发起对Blockbook的假充值攻击，请注意排查风险】据官方消息，继昨日慢雾安全团队披露的 UTXO 多签机制可被用于发起对交易所的...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=6307'
author: 金色财经
comments: false
date: Fri, 08 Apr 2022 10:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6307'
---

<div>   
【安全公司：UTXO多签机制可被用于发起对Blockbook的假充值攻击，请注意排查风险】据官方消息，继昨日慢雾安全团队披露的 UTXO 多签机制可被用于发起对交易所的假充值攻击之后，慢雾区安全伙伴安全鹭(Safeheron)反馈了新的威胁情报，知名开源中间件 Blockbook (Trezor 开源产品) 也受此特性影响，安全鹭发现 Blockbook 获取交易数据接口返回结果中对 MultiSig 类型交易展示不完善，如果 output 为 MultiSig 脚本，Blockbook 将会选择脚本中最后一个地址展示，和普通地址交易无法区分 。如果交易所、钱包客户端或者其它中心化服务仅根据 Blockbook 返回结果进行入账判断，将会造成误判导致假充值。目前已知可能受此多签特性影响的代币有 BTC/LTC/DOGE/BCH/BSV/BHD/CPU/DFI/BTCV/BXC/ZCL，慢雾安全团队建议相关运营方注意排查风险。  
</div>
            