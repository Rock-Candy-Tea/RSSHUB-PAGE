
---
title: 'FastCFS V2.2.0 发布，性能全面超越 Ceph！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8298'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 10:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8298'
---

<div>   
<div class="content">
                                                                    
                                                        <p>​  历经大约一个月的研发，FastCFS V2.2.0 发布，主要改进如下：<br>     1. [fstore] 使用libaio实现异步读，随机读性能提升明显；<br>     2. [fstore] 支持预读机制，顺序读性能提升显著；<br>     3. 修复了3个bug：<br>       1）[fstore] 修复V2.1.0引入的bug：第一次运行时，一个关键bool变量没有正确赋值；<br>       2）[fuseclient] 修复列举目录导致元数据缓存的一致性问题；<br>       3）[fauth] 修复username和poolname格式修饰符不当导致的乱码问题。</p> 
<p>    另，sungness 开发的集群运维工具（fcfs.sh） 和 vazmin 开发的k8s驱动（fastcfs-csi）已同步发布，欢迎大家测试和使用（FastCFS项目主页有链接）。</p> 
<p>    FastCFS V2.2.0采用异步读取和预读机制，读性能显著提升，至此FastCFS的IOPS全面超越Ceph：顺序写是Ceph的6.x倍，顺序读是Ceph的2.x倍，随机写大约是Ceph的2倍。详细的测试数据参见FastCFS项目官网：https://gitee.com/fastdfs100/FastCFS</p> 
<p>    V2.2.0是FastCFS一个里程碑版本，敬请朋友们多多支持！</p>
                                        </div>
                                      
</div>
            