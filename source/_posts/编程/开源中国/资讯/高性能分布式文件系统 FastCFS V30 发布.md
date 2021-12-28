
---
title: '高性能分布式文件系统 FastCFS V3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5143'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 09:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5143'
---

<div>   
<div class="content">
                                                                                            <p>经过整整5个月的潜心研发，FastCFS v3.0终于发布了。FastCFS 3.0 主要改进：核心组件FastDIR通过插件方式实现数据存储引擎，采用binlog + 存储引擎插件，按需加载inode数据，单机以有限内存（如64GB）支持100亿级的海量文件。</p> 
<p>通过binlog实现数据持久化比较简单，程序重启时通过binlog重放将inode数据全部加载到内存中，这种方式存储海量文件存在如下两个问题：<br>   1. 程序启动就绪时间长；<br>   2. 对内存空间要求非常高。</p> 
<p>V3.0引入存储引擎插件，很好地解决了单纯通过binlog实现数据持久化的两大问题。后续会有技术文章详细介绍FastDIR存储引擎的原理和特点，敬请期待。</p> 
<p>另外，FastCFS 3.0 修复了如下3个bug：<br>    [fdir] increase/decrease parent's nlink on rename operation<br>    [fdir] set dentry->kv_array->count to 0 correctly<br>    [fstore] should init barray->count to 0</p> 
<p>欢迎大家安装使用最新版本的FastCFS，有任何疑问和建议随时交流。</p>
                                        </div>
                                      
</div>
            