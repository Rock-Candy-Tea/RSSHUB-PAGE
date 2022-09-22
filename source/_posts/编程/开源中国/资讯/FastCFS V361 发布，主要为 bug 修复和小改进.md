
---
title: 'FastCFS V3.6.1 发布，主要为 bug 修复和小改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=459'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 10:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=459'
---

<div>   
<div class="content">
                                                                                            <p> FastCFS V3.6.1发布，这个版本主要为bug修复和一些小改进：<br>   1）集群管理工具 fcfs.sh 支持 Ubuntu 和 Debian；<br>   2）使用最新的libserverframe库（v1.1.19支持FastDFS v6.09）；<br>   3）修复了cluster_deal_join_leader动态分配buffer后response指针没有更新的问题；<br>   4）修复了磁盘可用空间统计不准确的问题；<br>   5）动态扩大网络buffer时，解决了buffer大小可能不足的隐患；<br>   6）任命数据分组master时采用批量入队方式，大幅提升处理效率；解决了数据分组达到512，cluster通信超时问题；<br>   7）当fuseclient的根目录不存时，自动创建返回EEXIST时需要再次检查根目录是否存在；<br>   8）当配置的base_path不存在时，自动创建以减少人工操作（注：只支持创建最后一级子目录）；<br>   9）fuse模块的fi->direct_io 选项对kernel版本进行适配，当kernel版本 >= 4.18才生效。</p> 
<p>  强烈建议正在使用FastCFS v3.6.0的用户尽快升级到V3.6.1。有任何问题和建议，欢迎随时反馈。</p>
                                        </div>
                                      
</div>
            