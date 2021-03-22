
---
title: '硬件安全：ARM体系架构的安全特性演进 (www.secrss.com)'
categories: 
    - 编程
    - 技术头条
    - 最新分享

author: 技术头条
comments: false
date: 2021-03-22 18:40:22
thumbnail: ''
---

<div>   
安全从业者脑中有一系列的安全名词，比如安全三要素Confidenciality 、Integrity、Availability，比如硬件安全品牌TPM、TrustZone、SGX、Titan-M，比如软件层面的安全能力Isolation、Access Control，又比如漏洞缓解措施DEP、ASLR、CFI。

从这些名词可以看出，软件最基础的安全能力都得自于硬件的支持，如果一个硬件没有特权级别，那就不要期望能实现什么安全能力了(没有MPU，基本的隔离都没办法做了)。

硬件能力如同原材料，能做成什么样的美味佳肴就靠厨师(工程师)的本领了。

因此在考虑未来产品安全的发展趋势时，硬件安全的未来演进是非常值得参考的。硬件安全系列主要讲述下ARM指令集的演进、Intel SGX解决方案以及苹果和Google硬件安全芯片的应用。本篇文章就从我们最熟悉的ARM开始讲起。
    
</div>
            