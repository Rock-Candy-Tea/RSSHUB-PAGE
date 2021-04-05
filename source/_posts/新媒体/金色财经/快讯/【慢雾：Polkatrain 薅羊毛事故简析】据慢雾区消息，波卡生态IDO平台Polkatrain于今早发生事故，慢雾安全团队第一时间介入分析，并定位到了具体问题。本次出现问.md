
---
title: '【慢雾：Polkatrain 薅羊毛事故简析】据慢雾区消息，波卡生态IDO平台Polkatrain于今早发生事故，慢雾安全团队第一时间介入分析，并定位到了具体问题。本次出现问...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=1966'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=1966'
---

<div>   
【慢雾：Polkatrain 薅羊毛事故简析】据慢雾区消息，波卡生态IDO平台Polkatrain于今早发生事故，慢雾安全团队第一时间介入分析，并定位到了具体问题。本次出现问题的合约为Polkatrain项目的POLT_LBP合约，该合约有一个swap函数，并存在一个返佣机制，当用户通过swap函数购买PLOT代币的时候获得一定量的返佣，该笔返佣会通过合约里的_update函数调用transferFrom的形式转发送给用户。由于_update函数没有设置一个池子的最多的返佣数量，也未在返佣的时候判断总返佣金是否用完了，导致恶意的套利者可通过不断调用swap函数进行代币兑换来薅取合约的返佣奖励。慢雾安全团队提醒DApp项目方在设计AMM兑换机制的时候需充分考虑项目的业务场景及其经济模型，防止意外情况发生。  
</div>
            