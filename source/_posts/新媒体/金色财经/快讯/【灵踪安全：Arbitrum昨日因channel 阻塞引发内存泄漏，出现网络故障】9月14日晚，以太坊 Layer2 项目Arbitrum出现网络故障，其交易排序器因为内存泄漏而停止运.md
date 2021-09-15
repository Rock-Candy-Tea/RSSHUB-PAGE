
---
title: '【灵踪安全：Arbitrum昨日因channel 阻塞引发内存泄漏，出现网络故障】9月14日晚，以太坊 Layer2 项目Arbitrum出现网络故障，其交易排序器因为内存泄漏而停止运...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=5593'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=5593'
---

<div>   
【灵踪安全：Arbitrum昨日因channel 阻塞引发内存泄漏，出现网络故障】9月14日晚，以太坊 Layer2 项目Arbitrum出现网络故障，其交易排序器因为内存泄漏而停止运行。根据灵踪安全漏洞检测系统提示：内存泄漏的位置在源码SequencerBatcher.SendTransaction() 函数中。 
此处漏洞是因为channel 阻塞导致大量goroutine 没有及时释放，引发内存泄漏。建议在处理并发时，考虑channel的阻塞情况。当存在高并发条件时，为channel写入数据时，加上select default 处理。  
</div>
            