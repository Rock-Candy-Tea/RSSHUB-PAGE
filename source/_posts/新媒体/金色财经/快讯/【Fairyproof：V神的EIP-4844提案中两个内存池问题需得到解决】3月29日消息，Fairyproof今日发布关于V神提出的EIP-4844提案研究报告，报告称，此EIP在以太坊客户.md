
---
title: '【Fairyproof：V神的EIP-4844提案中两个内存池问题需得到解决】3月29日消息，Fairyproof今日发布关于V神提出的EIP-4844提案研究报告，报告称，此EIP在以太坊客户...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=3761'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=3761'
---

<div>   
【Fairyproof：V神的EIP-4844提案中两个内存池问题需得到解决】3月29日消息，Fairyproof今日发布关于V神提出的EIP-4844提案研究报告，报告称，此EIP在以太坊客户端和汇总解决方案的实施中引入了重大变化，虽然可能不会引入明显的漏洞，但是新引入的blob交易可能会导致两种内存池问题。第一个是blob交易具有可变的内在GAS成本，这会使内存池受到攻击，因为交易可能有资格被包含在一个区块中，但可能没有资格被包含在下一个区块中。为防止此类攻击，该EIP建议仅广播“gas至少为当前最小值的两倍”的交易，以大大增加合法交易被包含在区块中的机会。第二个是blob交易在内存池层具有较大的数据量，这会使内存池暴露于DoS攻击。该EIP建议将“mempool替换的最小增量从1.1倍增加到2倍”以增加攻击者的成本，从而减少其攻击尝试。就安全性而言，开发人员必须在代码中解决这些问题。此外，报告称，用户应该注意，这两项建议是为了应对对内存池的攻击，如果它们被实施，则意味着如果非恶意用户希望交易得到及时处理，需要支付符合这些建议的Gas费用。此前消息，以太坊V神提出新的分片建议：EIP-4844。<br><a href="https://medium.com/@FairyproofT/exploring-security-checkpoints-in-shard-blob-transactions-based-on-eip-4844-by-fairyproof-8c3fc755fb14#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjU4YjQyOTY2MmRiMDc4NmYyZWZlZmUxM2MxZWIxMmEyOGRjNDQyZDAiLCJ0eXAiOiJKV1QifQ.eyJpc3Mi" target="_blank">原文链接</a>  
</div>
            