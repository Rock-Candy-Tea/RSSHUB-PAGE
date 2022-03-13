
---
title: '【黑客利用重入漏洞攻击Paraluni，获利逾170万美元，约1_3已流入Tornado】今日8时04分（HKT），BSC链上的元宇宙金融项目Paraluni遭受黑客攻击，黑客获利逾170万...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=1535'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=1535'
---

<div>   
【黑客利用重入漏洞攻击Paraluni，获利逾170万美元，约1/3已流入Tornado】今日8时04分（HKT），BSC链上的元宇宙金融项目Paraluni遭受黑客攻击，黑客获利逾170万美元。据欧科云链链上天眼初步分析： 
1、攻击者资金来自PancakeSwap的闪电贷； 
2、问题出在项目方MasterCheif合约的depositByAddLiquidity方法，该方法未校验代币数组参数address[2] memory _tokens是否和pid参数指向的LP相吻合，在涉及到LP数额变化时，也未加重入锁。 
目前黑客在BSC链上的地址「0x94bc」的账户余额为3000.01 BNB（约112.58万美元），另有235.45 ETH（约60.86万美元）通过cBridge跨链到了ETH网络「0x94bc」。其中约1/3被盗资金（230 ETH）已流入Tornado Cash。 
该事件提醒我们，在涉及到金额变动的合约方法中，一定要关注重入漏洞，尽量使用重入锁modifier。 
链上天眼团队已对相关地址进行了监控，并将进一步跟进事件进展。  
</div>
            