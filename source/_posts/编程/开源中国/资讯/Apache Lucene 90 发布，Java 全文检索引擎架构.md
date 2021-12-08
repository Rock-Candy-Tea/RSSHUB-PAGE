
---
title: 'Apache Lucene 9.0 发布，Java 全文检索引擎架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8071'
author: 开源中国
comments: false
date: Wed, 08 Dec 2021 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8071'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Apache Lucene 9.0 现已发布，Lucene 是完全用 Java 编写的高性能、功能齐全的全文检索引擎架构，提供了完整的查询引擎和索引引擎、部分文本分析引擎。目的是为软件开发人员提供一个简单易用的工具包，以方便地在目标系统中实现全文检索的功能，或者是以此为基础建立起完整的全文检索引擎。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">支持索引高维度的数字向量，以执行最近的邻居搜索，使用分层可导航的小世界图算法</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">针对塞尔维亚语、尼泊尔语和泰米尔语的新分析器</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">对日语的 IME 友好的自动建议</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333"> Snowball 2，增加了印地语、印度尼西亚语、尼泊尔语、塞尔维亚语、泰米尔语和意第绪语的词干</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">为瑞典语和挪威语提供了新的规范化/词干功能</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">分类法分面的速度提高了400%</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">多维点的索引速度提高 10-15%</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">对以点为索引的字段的排序速度提高了数倍。这个优化在 8.x 版本后期是一个选择项，现在从 9.0 版本开始也是选择项了</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">ConcurrentMergeScheduler 现在假定快速 I/O，在启发式方法会错误地检测系统是否有现代 I/O 的情况下，可能会提高索引的速度</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">发布列表的编码从 FOR-delta 改为 PFOR-delta，以进一步节省磁盘空间</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">文件格式都从 big-endian 顺序改为 little-endian 顺序</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">Lucene 9 不再有分支的包。这需要在 lucene-core JAR 之外重新命名一些包，所以你需要相应地调整一些导入</span></li> 
 <li style="text-align:left"><span style="background-color:#ffffff; color:#333333">在模块系统中使用 Lucene 9 应该被认为是实验性的</span></li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202112.mbox%2F%253CCAPsWd%2BOZmAyMjBoaoxyNbt%3DmW0TMSHpTWp9RN6UiC2tH5CH3Vw%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            