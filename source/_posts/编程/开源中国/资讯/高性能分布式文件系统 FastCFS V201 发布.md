
---
title: '高性能分布式文件系统 FastCFS V2.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4630'
author: 开源中国
comments: false
date: Fri, 14 May 2021 09:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4630'
---

<div>   
<div class="content">
                                                                    
                                                        <p>FastCFS V2.0.1发布，主要改进如下：</p> 
<p> 1. 确保顺序写盘，调用writev实现批量写；<br>  2. 设置线程名称用于性能调优；<br>  3. 将配置文件servers.conf合并到cluster.conf；<br>  4. 修复4个bug：<br>    1）解决磁盘空间统计不准的问题；<br>    2）修改skiplist实例创建方式，确保线程安全；<br>    3）修复current_size整数溢出问题；<br>    4）修复数据分组序号计算错误（没有减去基数）。</p> 
<p>gitee项目地址：<a href="https://gitee.com/fastdfs100/FastCFS">https://gitee.com/fastdfs100/FastCFS</a>，FastCFS支持一键部署单机环境，欢迎体验。</p>
                                        </div>
                                      
</div>
            