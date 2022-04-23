
---
title: '【欧科云链链上天眼：Aku项目方价值3,400万美元ETH被永久锁定，系合约实现逻辑问题】4月23日消息，NFT项目方Akutar的11,539.5 ETH（约合3,400万美元）被永久锁定...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=3773'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=3773'
---

<div>   
【欧科云链链上天眼：Aku项目方价值3,400万美元ETH被永久锁定，系合约实现逻辑问题】4月23日消息，NFT项目方Akutar的11,539.5 ETH（约合3,400万美元）被永久锁定在拍卖合约。 
Aku采用的是类似荷兰降价拍卖的形式，拍卖结束后会按照结束价格给用户退还超过最低价格的部分，因此这涉及refund以及total bids统计两个方面，而项目方在这两个方面均存在实现逻辑问题。 
第一个漏洞，processRefunds() 会被恶意合约阻断，实现DoS攻击，也确有用户使用恶意合约阻断了processRefunds(）执行，但该名用户表示只是让项目方确认问题存在，随即设置恶意合约变量，使得processRefunds(）顺利执行完，因此该漏洞虽被利用，但已成功解决。 
第二个漏洞，也就是真正导致项目方无法提款的关键所在，processRefunds(）是按照msg.sender的数量记录在了refundProgress变量，拍卖结束项目方调用claimProjectFunds()取出合约内的ETH时，要求满足refundProgress >= totalBids，而totalBids记录的是NFT的数量，合约最终状态refundProgress数值为3669，totalBids数值为5495，从而导致项目方无法提取合约内的11539.5 ETH。 
需要指出的是，在执行processRefunds(）之前，参与拍卖的用户可以在三天后通过emergencyWithdraw()将个人投入的ETH取回，但由于processRefunds(）的执行，导致用户的拍卖状态由未处理变为refund，从而不能再进行emergencyWithdraw()。  
</div>
            