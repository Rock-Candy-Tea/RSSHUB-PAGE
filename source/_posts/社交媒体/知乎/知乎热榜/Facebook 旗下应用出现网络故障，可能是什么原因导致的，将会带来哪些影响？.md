
---
title: 'Facebook 旗下应用出现网络故障，可能是什么原因导致的，将会带来哪些影响？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=2452'
author: 知乎
comments: false
date: Tue, 05 Oct 2021 08:43:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=2452'
---

<div>   
彭勇的回答<br><br><p>10月4日15:39 UTC - 21:20 UTC，Facebook发生重大安全事故, 全球宕机六个小时。脸书股票暴跌，高管通过twitter道歉。</p><p>事故的原因是15:39 UTC，Facebook的路由器 通过BGP协议撤销了 185.89.218.0/23 和 129.134.30.0/23 两段明细路由。而facebook 的四台授权域名服务器工作在这两段明细路由，BGP路由问题，导致Facebook的域名服务器从互联网上消失，期间Facebook, WhatsApp, Instagram 和 Messenger（Facebook 的即时通讯工具，也用于facebook内部通讯，域名 <a href="http://link.zhihu.com/?target=http%3A//m.me/" class=" wrap external" target="_blank" rel="nofollow noreferrer">m.me</a>)的相关域名无法解析，所有服务无法访问。</p><p>一些教训：</p><p>1、DNS这个关键服务设计不合理，虽然设计了四台授权域名服务器，但是都位于两段/23地址，都是使用AS32934自治号发布的，网络接入的多样性不够，导致四台域名服务器同时出问题；</p><p>2、Facebook 这样的公司，网络运维都是自动化运维（DevOPs)，加上变更管理没有严格审查，两条小小的路由发布，导致了整个事故发生；</p><p>3、恢复过程为什么耗时将近六个小时，原因是门禁系统、即时通讯工具、监控、运维等DEVOP工具都依赖域名服务，出问题的时候，无法使用正常流程恢复。据说脸书的员工由于门禁问题无法进入办公地点和机房，后来是用切割机暴力破解才解决问题的；</p><p>4、新冠疫情，员工都是在家在线办公，没法及时响应；</p><p>5、现场工作人员只能处理简单的问题。</p><p>就像评论里面<a href="https://www.zhihu.com/people/jiang-xun-93" class="internal">江浔</a>提到的，对于关键路径的依赖，还是要梳理清楚，在紧急情况发生的时候，如何有逃生通道？比如</p><ul><li>对重要网络设备，采用带外管理（OOB）</li><li>监控、DEVOP等工具假设在第三方的平台上</li><li>门禁、监控、DEVOP等工具使用主服务不一样的域名</li><li>DNS服务器的网络接入的多样性</li></ul>  
</div>
            