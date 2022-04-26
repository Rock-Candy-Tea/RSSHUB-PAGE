
---
title: '【成都链安：WienerDogeToken遭遇闪电贷攻击事件分析】据成都链安_链必应-区块链安全态势感知平台_安全舆情监控数据显示，WienerDogeToken遭受闪电贷攻击。成...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=8109'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=8109'
---

<div>   
【成都链安：WienerDogeToken遭遇闪电贷攻击事件分析】据成都链安“链必应-区块链安全态势感知平台”安全舆情监控数据显示，WienerDogeToken遭受闪电贷攻击。成都链安安全团队对此事件进行了简要分析，分析结果如下：攻击者通过闪电贷借贷了2900个BNB，从WDOGE和BNB的交易对交换了5,974,259,851,654个WDOGE代币，然后将4,979,446,261,701个代币重新转入了交易对。这时攻击者再调用skim函数，将交易对中多余的WDOGE代币重新提取出来，由于代币的通缩性质，在交易对向攻击地址转账的过程中同时burn掉了199,177,850,468个代币。这时交易对的k值已经被破坏，攻击者利用剩下WDOGE代币将交易对内的2,978个BNB成功swap出来，并且将获利的78个BNB转到了获利地址。 
这次攻击事件中，攻击者利用了代币的通缩性质，让交易对在skim的过程中burn掉了一部分交易对代币，破坏了k值的计算。成都链安安全团队建议项目上线前最好进行安全审计，通缩代币在与交易对的交互时尽量将交易对加入手续费例外。  
</div>
            