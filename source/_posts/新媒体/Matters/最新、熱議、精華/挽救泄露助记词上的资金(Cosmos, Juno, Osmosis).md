
---
title: '挽救泄露助记词上的资金(Cosmos, Juno, Osmosis)'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/280bd4c4-f845-4150-9eb5-e0d7aa846465.png'
author: Matters
comments: false
date: Sat, 09 Apr 2022 04:08:33 GMT
thumbnail: 'https://assets.matters.news/embed/280bd4c4-f845-4150-9eb5-e0d7aa846465.png'
---

<div>   
<figure class="image"><img src="https://assets.matters.news/embed/280bd4c4-f845-4150-9eb5-e0d7aa846465.png" data-asset-id="280bd4c4-f845-4150-9eb5-e0d7aa846465" referrerpolicy="no-referrer"><figcaption><span>(Image Source: Pixabay)</span></figcaption></figure><p><br></p><p>前段时间，有个群友说他的助记词泄露了，资金被盗，质押的代币也正在解除质押中，问我有没有办法解除质押的第一时间把代币转走？</p><p>所以给这个群友写了一个挽救被泄露助记词上的代币的脚本: <a href="https://github.com/ericet/cosmos-learn/blob/master/fundRescue.js" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://github.com/ericet/cosmos-learn/blob/master/fundRescue.js</a></p><p>这个脚本会查看解锁时间，解锁最后10分钟会每秒查看钱包余额，一查到有余额就会转到新钱包</p><p>脚本虽然写好了，但是没有实战过，所以并不知道效果怎么样</p><p>今天群友给我发了红包，说我的脚本很顺利的帮他把刚解锁的ATOM转到安全的钱包去了~ 说明脚本还是有效果的</p><p>之前脚本只支持Cosmos，刚修改了一下脚本，支持了Juno和Osmosis</p><p>如果你的助记词不小心泄露了，可以用我写的脚本尝试挽救资金</p><hr><p>最近建了一个twitter新号专门分享自己开发的工具，脚本等。对这些有兴趣的可以关注我的twitter账号：<a href="https://twitter.com/ericet369" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://twitter.com/ericet369</a></p><figure class="image"><img src="https://assets.matters.news/embed/3a246522-96d4-4a31-902c-f30ddd149aec.png" data-asset-id="3a246522-96d4-4a31-902c-f30ddd149aec" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p>  
</div>
            