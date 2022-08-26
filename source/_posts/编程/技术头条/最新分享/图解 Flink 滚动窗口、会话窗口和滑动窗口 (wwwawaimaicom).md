
---
title: '图解 Flink 滚动窗口、会话窗口和滑动窗口 (www.awaimai.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2414'
author: 技术头条
comments: false
date: 2022-08-26 12:18:44
thumbnail: 'https://picsum.photos/400/300?random=2414'
---

<div>   
Flink 作业中的窗口是指一种对无限数据流设置有限数据集，从而实现了处理无线数据流的机制。

窗口本身只是个划分数据集的依据，它并不存储数据。

当我们需要在时间窗口维度上对数据进行聚合时，窗口是流处理应用中经常需要解决的问题。Flink的窗口算子为我们提供了方便易用的API，我们可以将数据流切分成一个个窗口，对窗口内的数据进行处理。

窗口主要有两种，一种基于时间的时间窗口（TimeWindow），一种基于数量的计数窗口（CountWindow），计数窗口与时间无关，本文主要讨论时间窗口。
    
</div>
            