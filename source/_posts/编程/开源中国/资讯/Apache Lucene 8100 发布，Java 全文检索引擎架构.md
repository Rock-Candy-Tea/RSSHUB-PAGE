
---
title: 'Apache Lucene 8.10.0 发布，Java 全文检索引擎架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5940'
author: 开源中国
comments: false
date: Thu, 30 Sep 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5940'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flucene.apache.org%2Fcore%2Fcorenews.html%23apache-lucenetm-8100-available" target="_blank">Apache Lucene 8.10.0 已发布</a>，Lucene 是完全用 Java 编写的高性能、功能齐全的全文检索引擎架构，提供了完整的查询引擎和索引引擎、部分文本分析引擎。目的是为软件开发人员提供一个简单易用的工具包，以方便地在目标系统中实现全文检索的功能，或者是以此为基础建立起完整的全文检索引擎。</span></p> 
<p>此版本增加了多项新功能，以及其他优化和错误修复。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>新特性</strong></p> 
<ul> 
 <li>数值型的 range facet 计数现已支持多值字段 (Multi-valued)</li> 
 <li>为 Telugu 添加新的分析器</li> 
 <li>从 IndexCommit 中打开的 Near-real-time 阅读器现在支持对它们的叶子进行排序</li> 
 <li>编译码器已实现跳过其发布列表的功能</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>优化</strong></p> 
<ul style="margin-left:10px; margin-right:10px"> 
 <li>改进 facet 性能，包括引入新的受保护的 API 来控制在 drill sideway 期间对哪些字段进行钻取 (drill-down) 操作，以及优化 drill sideway 迭代</li> 
 <li>RegexpQuery 对对抗性 (ReDoS) 正则表达式的检测得到改进，可以捕获之前错过的特殊情况，并抛出 TooComplexToDeterminizeException 异常</li> 
 <li>加速计算 Automaton 的前导前缀和尾随后缀，以及在确定期间管理功率集</li> 
 <li>提升使用默认编解码器 (BEST_SPEED) 存储字段检索的速度</li> 
 <li>IndexWriter 在缓冲文档时使用较少的 RAM，尤其是在许多唯一字段的情况下</li> 
 <li>forceMerge 现在将一次性合并任意数量的段，提升在许多情况下的速度</li> 
 <li>针对文档值存储的压缩改进</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">除了以上的内容，此版本还修复了许多错误，详情查看变更日志：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flucene.apache.org%2Fcore%2F8_10_0%2Fchanges%2FChanges.html" target="_blank">https://lucene.apache.org/core/8_10_0/changes/Changes.html</a>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">下载地址：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flucene.apache.org%2Fcore%2Fdownloads.html" target="_blank">https://lucene.apache.org/core/downloads.html</a></p>
                                        </div>
                                      
</div>
            