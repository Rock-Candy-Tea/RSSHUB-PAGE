
---
title: '高性能分布式文件系统 FastCFS V3.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6023'
author: 开源中国
comments: false
date: Fri, 14 Jan 2022 09:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6023'
---

<div>   
<div class="content">
                                                                                            <p>V3.1主要对核心组件FastDIR进行改进，实现了LRU淘汰算法，以有限内存支持海量文件。</p> 
<p>分布式目录服务FastDIR的淘汰算法具有两大特性：<br>   1. 按目录结构淘汰：先淘汰子节点，然后淘汰父节点；<br>   2. 按数据线程淘汰：每个数据线程作为一个独立的数据单元，数据存取和淘汰均在其数据线程中以无锁方式完成。</p> 
<p>其他改进和bug修复如下：<br>   1. 采用引用计数方式，不再延迟释放 dentry；<br>   2. delay free namespace string for lockless；<br>   3. bugfixed: get trunk_file_size from ini file correctly。</p> 
<p>欢迎大家下载体验，安装和使用过程中有任何疑问欢迎随时反馈。</p>
                                        </div>
                                      
</div>
            