
---
title: '咱也来做 Likecoin 验证人了——续'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://picsum.photos/400/300?random=6682'
author: Matters
comments: false
date: Tue, 08 Jun 2021 16:00:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=6682'
---

<div>   
<p><s>做验证人比在 Matters 写文赚 Likecoin 快多了哈</s>（不是</p><h2>跋 - 调整验证人节点的佣金率</h2><p>所谓的佣金率，简单来说就是汝委托所获得的收益中验证人会分走多少。例如采用默认的 50% 的话，就是分走一半这样子。</p><p>但如果想要修改的话：</p><pre class="ql-syntax">docker exec -it likechain_liked likecli --home /likechain/.likecli tx staking edit-validator --commission-rate <这里是汝的新佣金率，最大为1（也就是 100%），最小为 0（也就是0%）>  --from validator --chain-id likecoin-chain-sheungwan
</pre><p>然后输入汝的私钥密码签名并提交更改（大概是这个意思吧……）</p><p>不过汝所设置的新佣金率不能大于汝在创建验证人节点时设置的最大佣金限制，每次变更的幅度也不能大于设置的每天最大佣金变化限制。以及佣金率每 24 小时只能变更一次。</p><p>所以咱最近就把佣金率改到咱能改到的最大的 80% 了，如果汝有咱的委托而且对这点不满的话，转移或者取回委托也是汝等的自由。但是如果汝愿意再听咱讲下去的话……</p><h2>关于 LikeCoin Chain 最近通过的新治理提案</h2><p>之前其实<a href="https://likecoin.bigdipper.live/proposals/9" target="_blank">已经有一个委托社群基金到新验证人的提案了</a>，当时的做法是将社群基金平均的分配给新增的验证人们。不过在后续的治理议案增加了验证人的上限以后，一度出现了几个几乎同时创建和上下线的验证人。于是在顾虑有可能被一个实体用多个验证人来套取多份社群基金的收益的情况下（咱这样理解没错吧），就有了上面的新议案。</p><p>这也就是汝为啥会看到这篇文章的原因（啥？）</p><h2>为啥咱要把佣金率设置的那么高？</h2><p><s>其实咱本来想更黑心一点设置到 100% 的</s>，奈何最大佣金率是在创建的时候就已经决定下来了，也没有办法再去修改……</p><p>以及更高的也不是没有啦，汝看看 <a href="https://likecoin.bigdipper.live/validator/cosmosvaloper1v8njts96gl5eqstnen4gksdy5k860fau65c3sw" target="_blank">Forbole</a> 和 <a href="https://likecoin.bigdipper.live/validator/cosmosvaloper1vmxv34ed7jwyk7h8qkfpndcxl2k20xuawenlvc" target="_blank">jason</a> ……</p><p>先说结论，在咱的验证人节点上线到现在的这三个月里，验证人节点在社群基金的赞助下给咱带来了差不多 16 万 LikeCoin 的收入（虽然其他人的委托占比实在太少，但还是在这里向给咱委托的各位说声谢谢。）。</p><p>这不由得让咱有了那么一点点妄想（？），说不定验证人节点的佣金能成为咱的一笔收入呢？（不怕各位笑话的讲，在年初生了一场大病辞职回家以后，咱还是绝赞的 Nerd 状态的样子…… ）</p><p>当然咱也想装作（喂？）吃水不忘挖井人的样子嘛，所以：</p><ul><li>以咱目前的委托量（11,009,405，其实就是 BigDipper 上投票权的千分之一）为基准，咱每再获得一百万 LikeCoin 的委托，咱就会把佣金比例下调 1%。（先这么做，以后看情况有可能降得更多。）</li><li>咱会拿出咱获得的佣金的一部分来在马特市上更用力的支持咱喜欢和/或者咱觉得很有价值的作品。（之前因为 BigDipper 的 Bug 没发现咱其实已经攒了那么多，加上咱发文章的频率很低于是靠写作没赚到多少就不太舍得的样子（嗯？）） </li></ul><p>虽然这两个承诺都很像空头支票的样子，但还是希望大家能相信咱这么一次。</p><h2>以及最后……</h2><p>虽然是咱和不少 Civic Liker 吆喝过很多次的话题了，如果汝也支持化赞为赏的开放的生态的话，其实有一个很好的方法就是成为赞赏公民。不管是成为<a href="http://liker.land/kenookamihoro/civic" target="_blank">咱的</a>、<a href="https://liker.land/foundation/civic?utm_source=portfolio" target="_blank">基金会的</a>、其它汝所喜好的作者的、或是<a href="https://docs.like.co/v/zh/user-guide/civic-liker/civic-liker-paid-by-likecoin" target="_blank">以 LikeCoin 支付年费成为经典赞赏公民</a> ，汝都在以实际行动向整个互联网展示汝对这一运动的支持。</p><p>谢谢大家。</p>  
</div>
            