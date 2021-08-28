
---
title: '【BlockSec：以太坊分叉因Geth旧版本在处理预编译合约调用时未考虑异常值的处理】BlockSec团队发文称，北京时间2021年8月27日20点50分左右（区块高度13107518）...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=2738'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=2738'
---

<div>   
【BlockSec：以太坊分叉因Geth旧版本在处理预编译合约调用时未考虑异常值的处理】BlockSec团队发文称，北京时间2021年8月27日20点50分左右（区块高度13107518），以太坊突然出现分叉。BlockSec通过分析Geth的代码版本修改和这笔造成分叉的交易（0x1cb6fb36633d270edefc04d048145b4298e67b8aa82a9e5ec4aa1435dd770ce4）厘清了以太坊分叉的根本原因：Geth旧版本在处理预编译合约调用时，并未考虑特殊情况（corner case）下参数值的处理，从而引发重叠拷贝（overlapping copy），导致返回值异常。该漏洞（CVE-2021-39137）已提交Geth官方，目前尚未披露细节，但攻击者已经利用漏洞实施了攻击。 
BlockSec总结称，通过对整个攻击流程的梳理和Geth源代码的分析，BlockSec认为根本原因在于Geth旧版本在处理预编译合约的调用时并未考虑异常值的处理，导致攻击者利用该漏洞实施了重叠拷贝，影响了返回值，最终导致分叉的出现。由于Geth是BSC、HECO、Polygon等公链的基础，因此该漏洞影响范围甚广。目前各公链也先后推出了升级和补丁，BlockSec也呼吁各相关节点尽早升级打上补丁，以确保基础设施的安全。  
</div>
            